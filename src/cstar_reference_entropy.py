"""Gurobi references preserving point-cell counts and changing differences.

Endpoint mechanism probe, all computation on Dirichlet. Solver output is
checked as a Boolean cyclic Sidon set; exact cubic arithmetic certifies
negative minima. Solver infeasibility alone is not an exact exclusion.
"""
from collections import Counter
from fractions import Fraction as F
import itertools
import json
import math
from pathlib import Path
import socket
import sys
import numpy as np
import gurobipy as gp
from gurobipy import GRB
from scipy.sparse import coo_matrix


def signed(B):
    ans={(x-u,y-v) for x,y in B for u,v in B if (x,y)!=(u,v)}
    assert len(ans)==len(B)*(len(B)-1)
    return ans


def positive(w):return w[0]>0 or (w[0]==0 and w[1]>0)


def moments(P,Q):
    A=signed(P);B=signed(Q);q={w:int(w in A)-int(w in B) for w in A|B}
    q={w:c for w,c in q.items() if c};a=len(A-B);norm=len(A^B)
    H=sum(c*q.get((s[0]-t[0],s[1]-t[1]),0) for s in A for t,c in q.items())
    assert norm==2*a and norm*len(P)**2+H*len(P)-a*a>=0
    approximate=2*a*a/(H+math.sqrt(H*H+4*norm*a*a)) if H>=0 else (-H+math.sqrt(H*H+4*norm*a*a))/(2*norm)
    bound=F(max(0,math.floor(approximate*10**8)-2),10**8)
    assert norm*bound*bound+H*bound-a*a<0
    ys=np.array([(s,0) for s in [.5,1,2,3,4]]+[(0,s) for s in [.5,1,2,3,4]]+[(s,s) for s in [1,2,3,4]])
    pbox=max(max(x,y) for x,y in P+Q)+1
    FP=np.exp(1j*np.array(P)@ys.T/pbox).sum(axis=0);FQ=np.exp(1j*np.array(Q)@ys.T/pbox).sum(axis=0)
    return dict(a=a,Q=norm,H=H,H_over_k3=H/len(P)**3,
                integer_difference_overlap=len(A&B)//2,global_M_lower=str(bound/2),
                global_M_upper=str(F(len(P),2)),front_diagnostic_float=float(np.max(np.abs(abs(FP)**2-abs(FQ)**2)))/len(P)**2)


def run_case(p,indices,g,rng):
    P=[(t,t*t%p) for t in indices];k=len(P);n=k*(k-1)//2;actual=signed(P)
    counts=Counter((g*x//p,g*y//p) for x,y in P)
    candidates=[(x,y) for x in range(p) for y in range(p) if counts[g*x//p,g*y//p]]
    N=len(candidates);ci,cj=np.triu_indices(N,1);M=len(ci);coords=np.array(candidates)
    dx=coords[ci,0]-coords[cj,0];dy=coords[ci,1]-coords[cj,1]
    modx=dx%p;mody=dy%p;cyclic=np.minimum(modx*p+mody,((-modx)%p)*p+(-mody)%p)
    classes,inverse=np.unique(cyclic,return_inverse=True)
    cyc=coo_matrix((np.ones(M),(inverse,np.arange(M))),shape=(len(classes),M)).tocsr()
    cell=np.array([g*(g*x//p)+g*y//p for x,y in candidates])
    cmat=coo_matrix((np.ones(N),(cell,np.arange(N))),shape=(g*g,N)).tocsr()
    rhs=np.array([counts[i//g,i%g] for i in range(g*g)])
    overlap=np.array([int((int(x),int(y)) in actual) for x,y in zip(dx,dy)],dtype=float)
    model=gp.Model();model.Params.OutputFlag=0;model.Params.Threads=2
    model.Params.TimeLimit=2 if p==11 else 5;model.Params.FeasibilityTol=1e-8;model.Params.IntFeasTol=1e-9
    x=model.addMVar(N,vtype=GRB.BINARY);y=model.addMVar(M,lb=0,ub=1)
    model.addConstr(x.sum()==k);model.addConstr(y.sum()==n)
    model.addConstr(x[ci]+x[cj]-y<=1);model.addConstr(cyc@y<=1)
    model.addConstr(cmat@x==rhs);cap=3*n//4;model.addConstr(overlap@y<=cap)
    references=[];statuses=[]
    for attempt in range(3):
        model.setObjective(overlap@y+1e-5*(rng.uniform(-1,1,size=N)@x),GRB.MINIMIZE)
        model.optimize();statuses.append(int(model.Status))
        if not model.SolCount:break
        chosen=np.flatnonzero(x.X>.5);Q=[candidates[i] for i in chosen]
        assert len(Q)==k and Counter((g*a//p,g*b//p) for a,b in Q)==counts
        cyc_diffs=[((a-c)%p,(b-d)%p) for a,b in Q for c,d in Q if (a,b)!=(c,d)]
        assert len(set(cyc_diffs))==k*(k-1)
        record=moments(P,Q);assert record['integer_difference_overlap']<=cap
        record.update(points=Q,attempt=attempt,status=int(model.Status),solver_objective=float(model.ObjVal))
        references.append(record);model.addConstr(x[chosen].sum()<=k-1)
    result=dict(p=p,k=k,grid=g,n=n,actual_t_indices=indices,actual_points=P,
                cell_counts={f'{a},{b}':c for (a,b),c in sorted(counts.items())},
                candidates=N,pair_variables=M,overlap_cap=cap,references=references,statuses=statuses,
                feasible=bool(references),infeasibility_independently_verified=False)
    if references:
        best=max(references,key=lambda z:F(z['global_M_lower']));result['best_M_lower']=best['global_M_lower']
        result['best_ratio_lower']=float(F(best['global_M_lower']))/math.sqrt(n)
    return result


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    rng=np.random.default_rng(20261104);cases=[];fine='--fine' in sys.argv
    for p in ([11] if fine else [11,31]):
        k=(p-1)//2
        shapes={'prefix':list(range(k)),
                'quadratic_arc':sorted(sorted(range(p),key=lambda t:(t*t%p,t))[:k]),
                'random':sorted(map(int,rng.choice(p,size=k,replace=False)))}
        if p==11:shapes['spread']=list(range(0,2*k,2));shapes['endpoint']=[0,1,3,4,8]
        for label,I in shapes.items():
            for g in ([9,10,11] if fine else [3,5,7] if p==11 else [5,7]):cases.append((p,label,I,g))
    root=Path('.research/experiments/reference_entropy_2026-10-20');root.mkdir(parents=True,exist_ok=True)
    out=dict(qualification='Exact finite Boolean references and mixed certificates; no all-input theorem '
             'from MIP success, and no exact infeasibility claim without a separate enumeration.',seed=20261104,cases=[])
    for p,label,I,g in cases:
        row=run_case(p,I,g,rng);row['label']=label;out['cases'].append(row)
        (root/('fine.json' if fine else 'results.json')).write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps({key:row[key] for key in ['p','label','grid','candidates','statuses','feasible']}
                        |dict(best_ratio_lower=row.get('best_ratio_lower'))),flush=True)


if __name__=='__main__':main()
