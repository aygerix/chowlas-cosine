"""Optimize the exact mixed-certificate margin over coarse Sidon references.

Gurobi nonconvex quadratic objective; each returned Boolean witness and
its integer cubic are checked separately. All computation on Dirichlet.
"""
from collections import Counter
from fractions import Fraction as F
import json
import math
from pathlib import Path
import socket
import numpy as np
import gurobipy as gp
from gurobipy import GRB
from scipy.sparse import coo_matrix
from cstar_reference_entropy import moments,signed


def solve(row):
    p=row['p'];g=row['grid'];P=list(map(tuple,row['actual_points']));k=len(P);n=k*(k-1)//2
    A=signed(P);counts=Counter((g*x//p,g*y//p) for x,y in P)
    V=[(x,y) for x in range(p) for y in range(p) if counts[g*x//p,g*y//p]];N=len(V)
    i,j=np.triu_indices(N,1);M=len(i);coords=np.array(V);dx=coords[i,0]-coords[j,0];dy=coords[i,1]-coords[j,1]
    modx=dx%p;mody=dy%p;classes=np.minimum(modx*p+mody,((-modx)%p)*p+(-mody)%p)
    _,cindex=np.unique(classes,return_inverse=True)
    sign=np.where((dx<0)|((dx==0)&(dy<0)),-1,1)
    freq,Findex=np.unique(np.stack([sign*dx,sign*dy],axis=1),axis=0,return_inverse=True);nf=len(freq)
    freq=[tuple(map(int,w)) for w in freq]
    cyc=coo_matrix((np.ones(M),(cindex,np.arange(M))),shape=(int(cindex.max())+1,M)).tocsr()
    fmat=coo_matrix((np.ones(M),(Findex,np.arange(M))),shape=(nf,M)).tocsr()
    cell=np.array([g*(g*x//p)+g*y//p for x,y in V]);rhs=np.array([counts[c//g,c%g] for c in range(g*g)])
    cmat=coo_matrix((np.ones(N),(cell,np.arange(N))),shape=(g*g,N)).tocsr()
    model=gp.Model();model.Params.OutputFlag=0;model.Params.Threads=2;model.Params.TimeLimit=12
    model.Params.NonConvex=2;model.Params.IntFeasTol=1e-9;model.Params.FeasibilityTol=1e-8
    x=model.addMVar(N,vtype=GRB.BINARY);y=model.addMVar(M,lb=0,ub=1);z=model.addMVar(nf,vtype=GRB.BINARY)
    model.addConstr(x.sum()==k);model.addConstr(y.sum()==n);model.addConstr(x[i]+x[j]-y<=1)
    model.addConstr(cyc@y<=1);model.addConstr(cmat@x==rhs);model.addConstr(z==fmat@y)
    mask=np.array([int(w in A) for w in freq]);model.addConstr(mask@z<=3*n//4)
    conv=Counter((a+c,b+d) for a,b in A for c,d in A);H0=sum(conv[s] for s in A)
    linear=np.array([-4*conv[w] for w in freq]);quadratic=[]
    for ii,w in enumerate(freq):
        for jj in range(ii,nf):
            v=freq[jj];c=2*(int((w[0]+v[0],w[1]+v[1]) in A)+int((w[0]-v[0],w[1]-v[1]) in A))
            if c:quadratic.append((ii,jj,c if ii==jj else 2*c))
    Hexpr=H0+linear@z+gp.quicksum(c*z[ii].item()*z[jj].item() for ii,jj,c in quadratic)
    aexpr=2*(n-mask@z)
    # Twice the margin at K=k/2 has integer coefficients.
    objective=2*aexpr*aexpr-k*Hexpr-k*k*aexpr
    model.setObjective(objective,GRB.MAXIMIZE)
    warm=max(row['references'],key=lambda r:F(r['global_M_lower']));W=set(map(tuple,warm['points']))
    x.Start=np.array([int(v in W) for v in V]);y.Start=np.array([int(V[a] in W and V[b] in W) for a,b in zip(i,j)])
    T=signed(list(W));z.Start=np.array([int(w in T) for w in freq])
    model.optimize()
    out=dict(p=p,grid=g,label=row['label'],actual_points=P,k=k,n=n,candidates=N,
             frequencies=nf,quadratic_terms=len(quadratic),K_target=str(F(k,2)),
             solver_status=int(model.Status),solver_bound_float=float(model.ObjBound),
             solver_optimality_independently_verified=False)
    if model.SolCount:
        Q=[V[t] for t in np.flatnonzero(x.X>.5)]
        assert len(Q)==k and Counter((g*a//p,g*b//p) for a,b in Q)==counts
        assert len({((a-c)%p,(b-d)%p) for a,b in Q for c,d in Q if (a,b)!=(c,d)})==k*(k-1)
        result=moments(P,Q);a=result['a'];H=result['H'];margin2=2*a*a-k*H-k*k*a
        assert int(round(float(Hexpr.getValue())))==H
        assert int(round(model.ObjVal))==margin2
        out.update(reference_points=Q,**result,margin_twice=margin2,target_certified=margin2>0,
                   baseline_best_M_lower=row['best_M_lower'])
    return out


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    root=Path('.research/experiments/reference_entropy_2026-10-20')
    baseline=json.loads((root/'results.json').read_text());out=[]
    for row in baseline['cases']:
        if row['p']!=11 or row['grid'] not in [3,7] or row['label'] not in ['prefix','random','endpoint']:continue
        result=solve(row);out.append(result)
        (root/'miqp.json').write_text(json.dumps(dict(qualification='Finite reference optimization; '
            'no global optimality claim without separate exhaustive verification.',cases=out),indent=2)+'\n')
        print(json.dumps({k:result.get(k) for k in ['p','grid','label','solver_status','a','H','margin_twice',
                  'target_certified','global_M_lower','baseline_best_M_lower']}),flush=True)


if __name__=='__main__':main()
