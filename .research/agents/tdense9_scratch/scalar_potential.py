"""Scalar nonlinear doubly-positive certificate, discovered with Gurobi, exact Bernstein."""
import json,sys,math
from pathlib import Path
from fractions import Fraction as F
from math import comb
import numpy as np
import gurobipy as gp
from gurobipy import GRB
OUT=Path('.research/agents/tdense9_scratch')
sys.path.insert(0,str(Path('.research/agents/tdense8_scratch').resolve()))
from potential import add,mul,compose,peval,certify

def bernrow(x,m):return np.array([comb(m,k)*x**k*(1-x)**(m-k) for k in range(m+1)])
def run(m):
    mod=gp.Model();mod.Params.OutputFlag=0;mod.Params.Threads=2
    mod.Params.FeasibilityTol=1e-9;mod.Params.OptimalityTol=1e-9
    kap=mod.addVar(lb=.7,ub=.92);bs=mod.addVars(m+1,lb=0,ub=10)
    mod.addConstr(bs[0]==0)
    for k in range(m):mod.addConstr(bs[k+1]>=bs[k])
    uu=np.unique(np.r_[np.linspace(0,1-1e-7,7001),np.geomspace(1e-8,.001,100)])
    for u in uu:
        x=1-u*u;y=max(0,2*x*x-1,x-u)
        row=(bernrow(y,m)-bernrow(x,m)/2)/x
        mod.addConstr(kap-1/(1+u)+gp.quicksum(float(row[k])*bs[k] for k in range(m+1))>=0)
    mod.setObjective(kap,GRB.MINIMIZE);mod.optimize();assert mod.SolCount
    rec=dict(degree=m,kappa=kap.X,b=[bs[k].X for k in range(m+1)])
    OUT.joinpath(f'scalar_d{m}_numeric.json').write_text(json.dumps(rec,indent=2));print('DISCOVERY',json.dumps(rec),flush=True)
    bb=[F(round(v*10**10),10**10) for v in rec['b']]
    assert bb[0]==0 and all(bb[i+1]>=bb[i] for i in range(m))
    beta=[F(0)]*(m+1)
    for k,v in enumerate(bb):
        for j in range(m-k+1):beta[k+j]+=v*comb(m,k)*comb(m-k,j)*(-1)**j
    xpoly=[F(1),F(0),-F(1)]
    for slack in (F(1,10**5),F(1,10**4),F(1,1000)):
        kap=F(math.ceil(rec['kappa']*10**6),10**6)+slack
        A=add(add([kap-1,F(1),-kap],[-v/2 for v in compose(beta,xpoly)]),[F(0)])
        # A(1)=0; divide by (1-u).
        assert peval(A,F(1))==0
        low=[];v=F(0)
        for c in A[:-1]:v+=c;low.append(v)
        assert -low[-1]==A[-1]
        middle=add(A,compose(beta,[F(1),-F(1),-F(1)]))
        high=add(A,compose(beta,[F(1),F(0),-F(4),F(0),F(2)]))
        derivative=[(i+1)*beta[i+1] for i in range(m)]
        checks=[certify(derivative,-F(1,100000),F(1)),
                certify(high,F(0),F(366026,10**6)),
                certify(middle,F(366025,10**6),F(618035,10**6)),
                certify(low,F(618033,10**6),F(1))]
        if all(c['ok'] for c in checks):break
    out=dict(status='PROVED' if all(c['ok'] for c in checks) else 'UNRESOLVED',degree=m,kappa=str(kap),beta_bernstein=list(map(str,bb)),beta_power=list(map(str,beta)),checks=checks)
    r=F(769801,10**6);reach=4/(r*kap);out.update(C_exact=str(reach),C_float=float(reach),r=str(r))
    OUT.joinpath(f'scalar_d{m}_exact.json').write_text(json.dumps(out,indent=2));print('EXACT',json.dumps(out),flush=True)
if __name__=='__main__':
    for m in map(int,sys.argv[1:] or ['4','8','12']):run(m)
