"""Long Toeplitz bounds via exact nonnegative trigonometric polynomial certificates.
Every optimization is a Gurobi LP. Discovery grids are not certificates.
"""
import json,sys,math
from pathlib import Path
from fractions import Fraction as F
from math import comb
import numpy as np
import gurobipy as gp
from gurobipy import GRB
OUT=Path('.research/agents/tdense9_scratch')
sys.path.insert(0,str(Path('.research/agents/tdense8_scratch').resolve()))
from potential import add,mul,compose,peval,bern,certify

def chebs(N):
    out=[[F(1)],[F(0),F(1)]]
    for n in range(2,N+1):out.append(add(mul([F(0),F(2)],out[-1]),[-v for v in out[-2]]))
    return out

def discover_bounds(N=24):
    model=gp.Model();model.Params.OutputFlag=0;model.Params.Threads=2
    model.Params.FeasibilityTol=1e-9;model.Params.OptimalityTol=1e-9
    zz=model.addMVar(N,lb=np.r_[-100.,-100.,np.zeros(N-2)],ub=100.)
    m=zz[0];b=zz[1];lam=zz[2:]
    th=np.linspace(0,np.pi,4097);A=np.column_stack([np.cos(th),np.ones(len(th)),np.cos(np.outer(th,np.arange(3,N+1)))])
    model.addConstr(A@zz<=np.cos(2*th))
    polys=chebs(N);records=[]
    for x0 in np.r_[np.arange(.25,.95,.05),.95,.97,.985,.995]:
        model.setObjective(b+float(x0)*m,GRB.MAXIMIZE);model.optimize();assert model.SolCount
        mm=F(round(float(m.X)*10**9),10**9);ll=[max(F(0),F(round(v*10**9),10**9)) for v in lam.X]
        for slack in (F(1,100000),F(1,10000),F(1,1000)):
            bb=F(round(float(b.X)*10**9),10**9)-slack
            pp=add(polys[2],[-bb,-mm])
            for n,v in enumerate(ll,3):pp=add(pp,[-v*c for c in polys[n]])
            ck=certify(pp,F(-1),F(1))
            if ck['ok']:break
        row=dict(x0=float(x0),m=str(mm),b=str(bb),lambda_coefficients=list(map(str,ll)),N=N,check=ck,status='PROVED' if ck['ok'] else 'UNRESOLVED')
        if ck['ok']:records.append(row)
        print('GRAM_BOUND',json.dumps({k:v for k,v in row.items() if k!='lambda_coefficients'}),flush=True)
        OUT.joinpath('long_gram_bounds.json').write_text(json.dumps(records,indent=2))
    return records

def brow(x,m):return np.array([comb(m,k)*x**k*(1-x)**(m-k) for k in range(m+1)])
def potential(records,degree=12):
    lines=[(float(F(r['m'])),float(F(r['b']))) for r in records]
    model=gp.Model();model.Params.OutputFlag=0;model.Params.Threads=2
    model.Params.FeasibilityTol=1e-9;model.Params.OptimalityTol=1e-9
    kap=model.addVar(lb=.7,ub=.8);bb=model.addVars(degree+1,lb=0,ub=10);model.addConstr(bb[0]==0)
    for j in range(degree):model.addConstr(bb[j+1]>=bb[j])
    for u in np.unique(np.r_[np.linspace(0,1-1e-7,8001),np.geomspace(1e-8,.001,100)]):
        x=1-u*u;y=max([0,2*x*x-1,x-u]+[m*x+b for m,b in lines]);y=min(1,y)
        row=(brow(y,degree)-brow(x,degree)/2)/x
        model.addConstr(kap-1/(1+u)+gp.quicksum(float(row[j])*bb[j] for j in range(degree+1))>=0)
    model.setObjective(kap,GRB.MINIMIZE);model.optimize();assert model.SolCount
    bs=[F(round(bb[j].X*10**10),10**10) for j in range(degree+1)];assert bs[0]==0 and all(bs[j+1]>=bs[j] for j in range(degree))
    beta=[F(0)]*(degree+1)
    for k,v in enumerate(bs):
        for j in range(degree-k+1):beta[k+j]+=v*comb(degree,k)*comb(degree-k,j)*(-1)**j
    branches=[[F(0)],[F(1),F(0),-F(4),F(0),F(2)],[F(1),-F(1),-F(1)]]+[[F(r['m'])+F(r['b']),F(0),-F(r['m'])] for r in records]
    for slack in (F(1,100000),F(1,10000),F(1,1000)):
        kk=F(math.ceil(kap.X*10**6),10**6)+slack
        A=add([kk-1,F(1),-kk],[-v/2 for v in compose(beta,[F(1),F(0),-F(1)])])
        assert peval(A,F(1))==0
        low=[];v=F(0)
        for c in A[:-1]:v+=c;low.append(v)
        ps=[low]+[add(A,compose(beta,br)) for br in branches[1:]]
        leaves=[];stack=[(F(0),F(1),0)];unresolved=[]
        while stack:
            l,h,depth=stack.pop();mid=(l+h)/2
            j=max(range(len(branches)),key=lambda j:peval(branches[j],mid))
            ar=bern(branches[j],l,h)
            P=ps[j];vmin=min(bern(P,l,h))
            if min(ar)>=-F(1,100000) and max(ar)<=1 and vmin>=0:
                leaves.append(dict(lo=str(l),hi=str(h),branch=j,min_bernstein=str(vmin)));continue
            if depth>=28:unresolved.append(dict(lo=str(l),hi=str(h),branch=j));break
            stack.extend([(l,mid,depth+1),(mid,h,depth+1)])
        # beta is monotone on tiny enlargement, independently of active-branch selection.
        deriv=[(i+1)*beta[i+1] for i in range(degree)];mon=certify(deriv,-F(1,100000),F(1))
        if not unresolved and mon['ok']:break
    rr=F(769801,10**6);reach=4/(rr*kk)
    out=dict(status='PROVED' if not unresolved and mon['ok'] else 'UNRESOLVED',degree=degree,kappa=str(kk),discovery_kappa=kap.X,beta_bernstein=list(map(str,bs)),beta_power=list(map(str,beta)),branches=[[str(v) for v in br] for br in branches],leaves=leaves,monotonicity=mon,unresolved=unresolved,C_exact=str(reach),C_float=float(reach))
    OUT.joinpath(f'long_scalar_d{degree}_exact.json').write_text(json.dumps(out,indent=2))
    print('LONG_SCALAR',json.dumps({k:v for k,v in out.items() if k not in ('leaves','branches','beta_power','beta_bernstein')}),flush=True)
    return out

if __name__=='__main__':
    path=OUT/'long_gram_bounds.json'
    records=json.loads(path.read_text()) if path.exists() else discover_bounds(int(sys.argv[1]) if len(sys.argv)>1 else 24)
    for deg in (8,12,24):potential(records,deg)
