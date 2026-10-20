"""Correlate center choices to suppress finite zero phases, then attack them.

Gurobi optimizes only a finite surrogate. Arb certifies its actual listed
angle floors and a separate missed negative point. All work on Dirichlet.
"""
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import socket
import sys
import flint
import gurobipy as gp
from gurobipy import GRB
import numpy as np
from scipy.special import jn_zeros
from cstar_fiber_centers import geometry,encoding,residues_for_phase,crt,matrices_for_choices
from cstar_lens_shell import point


def floors(matrices,h,C,targets):
    P=math.prod(h);balls=[]
    for residues in targets:
        j=crt(residues,h);counts=Counter()
        for M in matrices:
            r=j*sum(c*z for c,z in zip(C,M))%P;counts[min(r,P-r)]+=1
        balls.append(sum((n*flint.arb.cos_pi_fmpq(flint.fmpq(2*r,P))
                          for r,n in counts.items()),flint.arb(0)))
    lower=min(float(v.mid()) for v in balls)
    B=F(max(1,math.ceil(-lower*10**6)+2),10**6)
    assert all(v+flint.arb(B.numerator)/B.denominator>0 for v in balls)
    return dict(B_rational=str(B),ratio_float=float(B)/math.sqrt(len(matrices)),
                target_residues=[list(z) for z in targets],value_balls=list(map(str,balls)),
                qualification='Lower floor only at these finitely many exact CRT angles; not a global upper bound for M',
                verified=True)


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Run through src/dirun.sh')
    if '--repair-snapshots' in sys.argv:
        path=Path('.research/experiments/fiber_centers_2026-10-20/correlated.json')
        saved=json.loads(path.read_text());fibers=geometry(saved['X']);h,P,C=encoding(saved['X'])
        counts=[]
        for row in saved['rounds']:
            cert=row['finite_floor'];old=len(cert['target_residues']);intended=row['targets']
            assert len(cert['value_balls'])==intended and old>=intended
            cert['target_residues']=[list(z) for z in cert['target_residues'][:intended]]
            matrices=matrices_for_choices(fibers,row['choices'])
            A=sorted(abs(sum(c*m for c,m in zip(C,M))) for M in matrices)
            row['adversarial_point']['n']=len(A)
            row['adversarial_point']['encoded_set_sha256']=hashlib.sha256((' '.join(map(str,A))).encode()).hexdigest()
            counts.append(dict(iteration=row['iteration'],old_count=old,corrected_count=intended))
        saved['serialization_repair']=dict(reason='Mutable target-list alias extended historical snapshots; '
            'restore each original prefix matching its saved value balls. All restored floors require independent recheck.',
            counts=counts)
        path.write_text(json.dumps(saved,indent=2)+'\n');print(json.dumps(saved['serialization_repair']),flush=True)
        return
    flint.ctx.prec=144;rng=np.random.default_rng(20261027);X=64
    fibers=geometry(X);h,P,C=encoding(X);tau=2*float(jn_zeros(1,1)[0])
    target_n=round(sum(float(f['n'].mean()) for f in fibers))
    option_indices=[];offsets=[0];sizes=[]
    for fiber in fibers:
        zero=int(np.where((fiber['B']==[0,0]).all(axis=1))[0][0])
        order=[zero]+list(map(int,rng.permutation(len(fiber['B']))))
        seen=set();indices=[]
        for i in order:
            packed=np.packbits(fiber['incidence'][i]).tobytes()
            if packed not in seen:seen.add(packed);indices.append(i)
            if len(indices)==12:break
        option_indices.append(indices);offsets.append(offsets[-1]+len(indices))
        sizes.extend(int(fiber['n'][i]) for i in indices)
    sizes=np.array(sizes,dtype=float);nvar=len(sizes)
    targets=[]
    for j in range(8):
        c=math.cos(math.pi*j/8);s=math.sin(math.pi*j/8)
        targets.append(residues_for_phase(np.array([c,-s,s,c])*tau/X,h))
    out=dict(qualification='Bounded finite-surrogate correlated-center experiment. '
             'No all-angle bound, global optimum, or general counterexample claimed.',
             X=X,seed=20261027,moduli=h,C=C,target_n=target_n,fibers=len(fibers),
             option_center_indices=option_indices,gurobi_version=list(gp.gurobi.version()),rounds=[])
    root=Path('.research/experiments/fiber_centers_2026-10-20');root.mkdir(parents=True,exist_ok=True)
    previous=None
    for iteration in range(3):
        phases=2*np.pi*np.array(targets,dtype=float)/np.array(h,dtype=float)
        columns=[]
        for fiber,indices in zip(fibers,option_indices):
            a,b=fiber['u'];q=np.stack([phases[:,0]*a+phases[:,2]*b,
                                    phases[:,1]*a+phases[:,3]*b],axis=0)
            columns.append((fiber['incidence'][indices]@np.cos(fiber['W']@q)).T)
        coefficients=np.concatenate(columns,axis=1)
        model=gp.Model('fiber_center_surrogate');model.Params.OutputFlag=0
        model.Params.Threads=2;model.Params.TimeLimit=15;model.Params.MIPFocus=1
        model.Params.IntFeasTol=1e-9;model.Params.FeasibilityTol=1e-8
        z=model.addMVar(nvar,vtype=GRB.BINARY);t=model.addVar(lb=0.)
        for a,b in zip(offsets[:-1],offsets[1:]):model.addConstr(z[a:b].sum()==1)
        model.addConstr(sizes@z==target_n)
        model.addConstr(coefficients@z+t>=0)
        if previous is not None:
            start=np.zeros(nvar)
            for i,index in enumerate(previous):start[offsets[i]+index]=1
            z.Start=start;t.Start=max(0.,float(-(coefficients@start).min()))+1
        model.setObjective(t,GRB.MINIMIZE);model.optimize()
        assert model.SolCount>0
        choices=[];selected=[]
        for j,indices in enumerate(option_indices):
            local=int(np.argmax(z.X[offsets[j]:offsets[j+1]]))
            assert z.X[offsets[j]+local]>.999999
            selected.append(local);choices.append(indices[local])
        previous=selected
        matrices=matrices_for_choices(fibers,choices);assert len(matrices)==target_n
        finite=floors(matrices,h,C,targets)
        adversarial=point(X,C,h,P,matrices,rng)
        A=sorted(abs(sum(c*m for c,m in zip(C,M))) for M in matrices)
        adversarial['n']=len(A)
        adversarial['encoded_set_sha256']=hashlib.sha256((' '.join(map(str,A))).encode()).hexdigest()
        row=dict(iteration=iteration,targets=len(targets),choices=choices,
                 solver_status=int(model.Status),solver_objective=float(model.ObjVal),
                 solver_bound=float(model.ObjBound),finite_floor=finite,adversarial_point=adversarial)
        out['rounds'].append(row);(root/'correlated.json').write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps(dict(iteration=iteration,n=len(matrices),targets=len(targets),
                             finite_ratio=finite['ratio_float'],
                             missed_R_lower=adversarial['R_lower_float'],status=int(model.Status))),flush=True)
        targets.append(list(map(int,adversarial['residues'])))
        model.dispose()


if __name__=='__main__':main()
