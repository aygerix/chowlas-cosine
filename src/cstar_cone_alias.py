"""Positive Fejer plane certificates and exact alias witnesses.

Run on Dirichlet. Gurobi only locates short integer kernel vectors; every
reported vector and collision is checked exactly and is not called shortest.
"""
from fractions import Fraction as F
import json
import math
import os
from pathlib import Path
import socket
import flint
import gurobipy as gp
from gurobipy import GRB
import numpy as np


def short_collision(C,X):
    bound=32*X;witnesses=[]
    for index in range(4):
        model=gp.Model('cone_alias')
        model.Params.OutputFlag=0;model.Params.Threads=1;model.Params.TimeLimit=2
        model.Params.IntFeasTol=1e-9;model.Params.FeasibilityTol=1e-9
        v=model.addMVar(4,lb=-bound,ub=bound,vtype=GRB.INTEGER)
        radius=model.addVar(lb=1,ub=bound,vtype=GRB.INTEGER)
        model.addConstr(np.array(C)@v==0)
        model.addConstr(v[index]>=1)
        model.addConstr(v<=radius);model.addConstr(v>=-radius)
        model.setObjective(radius,GRB.MINIMIZE);model.optimize()
        if model.SolCount:
            z=[int(round(t)) for t in v.X]
            if sum(a*b for a,b in zip(C,z))==0 and any(z):
                norm2=max(z[0]**2+z[1]**2,z[2]**2+z[3]**2)
                assert norm2>X*X
                first=[z[0],z[1],0,0];second=[0,0,-z[2],-z[3]]
                assert sum(a*b for a,b in zip(C,first))==sum(a*b for a,b in zip(C,second))
                witnesses.append(dict(kernel=z,first=first,second=second,
                                      radius_squared=norm2,radius_over_X_float=math.sqrt(norm2)/X,
                                      model_status=int(model.Status),verified=True))
        model.dispose()
    return min(witnesses,key=lambda r:r['radius_squared']) if witnesses else None


def kernel_certificate(A,C,X):
    a,b,c,d=C;m=32*X;den=(m+1)**2
    support=set(A)|{-z for z in A}
    total=[0]*(2*m+1);mass=[0]*(2*m+1);plane=[0]*(2*m+1)
    for r in range(-m,m+1):
        wr=m+1-abs(r)
        for s in range(-m,m+1):
            f=a*r+b*s;weight=wr*(m+1-abs(s))
            if f in support:total[r+m]+=weight
            if f==0:mass[r+m]+=weight
            if 0<r*r+s*s<=X*X:plane[r+m]+=weight
    cosines=[(flint.arb(5*r)/X).cos() for r in range(-m,m+1)]
    def evaluate(coeff):
        return sum((z*w for z,w in zip(coeff,cosines)),flint.arb(0))/den
    mean=evaluate(mass);H=evaluate(total);main=evaluate(plane)
    aliases=evaluate([u-v for u,v in zip(total,plane)])
    assert mean>0
    lower=F(0)
    if H<0:
        estimate=-float(H.mid())/(2*float(mean.mid()))
        lower=F(max(0,math.floor(estimate*10**6)),10**6)
        assert H+2*lower.numerator*mean/lower.denominator<0
    return dict(m=m,alpha_rational=str(F(5,X)),mean_ball=str(mean),
                main_plane_integral_ball=str(main),alias_integral_ball=str(aliases),
                total_D_integral_ball=str(H),M_lower_rational=str(lower),
                R_lower_float=float(lower)/math.sqrt(len(A)),
                alias_weight_numerator=sum(total)-sum(plane),
                origin_alias_pairs=sum(1 for z in mass if z)-1,
                qualification='Nonnegative product-Fejer test; no point-sampling inference.',verified=True)


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Run through src/dirun.sh')
    flint.ctx.prec=128
    root=Path('.research/experiments/cone_comparable_2026-10-20')
    data=json.loads((root/'results.json').read_text())
    # The disk transform at radius five is strictly below -1/8.
    upper=sum(F((-1)**k,math.factorial(k)*math.factorial(k+1))*F(25,4)**k
              for k in range(21))
    assert upper<F(-1,8)
    out=dict(qualification='Finite certificates and exact collision witnesses; no universal exclusion of comparable encodings.',
             disk_at_5_upper_rational=str(upper),gurobi=list(gp.gurobi.version()),cases=[])
    for row in data['global_probes']:
        X,C,A=row['X'],row['C'],row['A']
        point=max([row['initial_point'],row['fine_grid_point']],key=lambda z:z['R_lower_float'])
        q,j=point['q'],point['j']
        residues=[(j*z+q//2)%q-q//2 for z in C]
        Y=(2*np.pi*X/q*np.array(residues,dtype=float)).reshape(2,2)
        result=dict(X=X,C=C,n=len(A),fejer=kernel_certificate(A,C,X),
                    collision=short_collision(C,X),
                    negative_point_phase=dict(j=j,q=q,centered_residues=residues,
                        scaled_entries_float=Y.tolist(),singular_values_float=np.linalg.svd(Y,compute_uv=False).tolist()))
        out['cases'].append(result)
        (root/'alias.json').write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps(dict(X=X,n=len(A),fejer=result['fejer'],collision=result['collision'])),flush=True)


if __name__=='__main__':main()
