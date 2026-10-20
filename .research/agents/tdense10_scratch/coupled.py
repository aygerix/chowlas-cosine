"""Support-coupled potential: Gurobi discovery, all mathematical execution on VM."""
import os
os.environ['SYMPY_GROUND_TYPES']='flint'
import json,sys,math
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
import gurobipy as gp
from math import comb
OUT=Path('.research/agents/tdense10_scratch')
sys.path.insert(0,str(Path('.research/agents/tdense8_scratch').resolve()))
from potential import add,mul,compose,peval,bern,certify

def brow(x,m):return np.array([comb(m,k)*x**k*(1-x)**(m-k) for k in range(m+1)])
def main(deg=12,K=12):
    # bins [0,1/K], [1/K,1/(K-1)], ..., [1/2,1]
    edges=np.r_[0.,1/np.arange(K,0,-1)]
    caps=np.r_[1.,[np.cos(np.pi/(k+1)) for k in range(K,1,-1)]]
    # For t>1/k, nonzero sequence lasts at most k-1: cap=cos(pi/(k+1)).
    # Initial Schur test u, positive symmetric polynomial.
    ss=np.linspace(0,1,801);nq=4000;tt=(np.arange(nq)+.5)/nq
    for shape in (0., .5, 1.):
        U=lambda x: 1+shape*(4*x*(1-x))
        bins=np.minimum(K-1,np.searchsorted(edges,np.abs(ss[:,None]-tt[None,:]),side='right')-1)
        weights=np.array([(np.where(bins==j,U(tt)[None,:],0).sum(axis=1)/nq)/U(ss) for j in range(K)]).T
        model=gp.Model();model.Params.OutputFlag=0;model.Params.Threads=4
        model.Params.FeasibilityTol=1e-9;model.Params.OptimalityTol=1e-9
        aa=model.addVars(K,lb=0,ub=2);bb=model.addVars(deg+1,lb=0,ub=10);D=model.addVar(lb=0)
        model.addConstr(bb[0]==0)
        for i in range(deg):model.addConstr(bb[i+1]>=bb[i])
        for j,cap in enumerate(caps):
            # rational circle parameter x=2u/(1+u*u), F=x*u/2.
            umax=cap/(1+np.sqrt(max(0,1-cap*cap)))
            for u in np.r_[np.linspace(1e-8,umax,2501),np.geomspace(1e-9,1e-3,50)]:
                if u>umax:continue
                x=2*u/(1+u*u);y=max(0.,2*x*x-1,x-np.sqrt(max(0,1-x)))
                row=(brow(y,deg)-brow(x,deg)/2)/x
                model.addConstr(aa[j]-u/2+gp.quicksum(float(row[i])*bb[i] for i in range(deg+1))>=0)
        for row in weights:model.addConstr(gp.quicksum(float(row[j])*aa[j] for j in range(K))<=2*D)
        model.setObjective(D,gp.GRB.MINIMIZE);model.optimize();assert model.SolCount
        rec=dict(degree=deg,K=K,shape=shape,D=D.X,C=1/D.X,edges=edges.tolist(),caps=caps.tolist(),a=[aa[j].X for j in range(K)],beta=[bb[i].X for i in range(deg+1)])
        OUT.joinpath(f'coupled_d{deg}_K{K}_s{shape}.json').write_text(json.dumps(rec,indent=2))
        print(json.dumps(rec),flush=True)
if __name__=='__main__':main(*map(int,sys.argv[1:]))
