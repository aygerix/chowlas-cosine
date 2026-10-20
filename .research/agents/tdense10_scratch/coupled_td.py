"""t-dependent doubling potentials; sampled discovery only. Gurobi LP, VM only."""
import os
os.environ['SYMPY_GROUND_TYPES']='flint'
import json,sys,math
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
import gurobipy as gp
from math import comb
OUT=Path('.research/agents/tdense10_scratch')

def brow(x,m):return np.array([comb(m,k)*x**k*(1-x)**(m-k) for k in range(m+1)])
def run(deg=6,K=32,shape=.2):
    # uniform dyadic cells. B(t,x) piecewise in t. B=0 outside [0,1].
    # 2t maps each cell's halves into known cells.
    edges=np.linspace(0,1,K+1);ss=np.linspace(0,1,501);nq=6000;tt=(np.arange(nq)+.5)/nq
    U=lambda x:1+shape*4*x*(1-x)
    bins=np.minimum(K-1,(np.abs(ss[:,None]-tt[None,:])*K).astype(int))
    weights=np.array([(np.where(bins==j,U(tt)[None,:],0).sum(axis=1)/nq)/U(ss) for j in range(K)]).T
    model=gp.Model();model.Params.OutputFlag=0;model.Params.Threads=4
    model.Params.FeasibilityTol=1e-9;model.Params.OptimalityTol=1e-9
    aa=model.addVars(K,lb=0,ub=2);bb=model.addVars(K,deg+1,lb=0,ub=10);D=model.addVar(lb=0)
    for j in range(K):
        model.addConstr(bb[j,0]==0)
        for i in range(deg):model.addConstr(bb[j,i+1]>=bb[j,i])
    for j in range(K):
        for jj in (2*j,2*j+1):
            # lower endpoint for half-cell: (jj/2)/K.
            tlo=jj/(2*K)
            k=math.ceil(1/max(tlo,1e-300))-1 if tlo else 10**9
            cap=np.cos(np.pi/(k+2)) if k<10**8 else 1.
            umax=cap/(1+np.sqrt(max(0,1-cap*cap)))
            for u in np.r_[np.linspace(1e-7,umax,801),np.geomspace(1e-9,1e-3,20)]:
                if u>umax:continue
                x=2*u/(1+u*u);y=max(0,2*x*x-1,x-np.sqrt(max(0,1-x)))
                bx=brow(x,deg)/(2*x);by=brow(y,deg)/x
                expr=aa[j]-u/2-gp.quicksum(float(bx[i])*bb[j,i] for i in range(deg+1))
                if jj<K:expr+=gp.quicksum(float(by[i])*bb[jj,i] for i in range(deg+1))
                else:
                    # w(2t)=0. Also CF cap at most 1/2. B outside zero.
                    pass
                model.addConstr(expr>=0)
    for row in weights:model.addConstr(gp.quicksum(float(row[j])*aa[j] for j in range(K))<=2*D)
    model.setObjective(D,gp.GRB.MINIMIZE);model.optimize();assert model.SolCount
    rec=dict(degree=deg,K=K,shape=shape,D=D.X,C=1/D.X,a=[aa[j].X for j in range(K)],beta=[[bb[j,i].X for i in range(deg+1)] for j in range(K)])
    OUT.joinpath(f'coupled_td_d{deg}_K{K}_s{shape}.json').write_text(json.dumps(rec,indent=2));print(json.dumps({k:v for k,v in rec.items() if k!='beta'}),flush=True)
if __name__=='__main__':run(int(sys.argv[1]),int(sys.argv[2]),float(sys.argv[3]))
