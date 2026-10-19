"""VM-only Gurobi discovery and exact rational verification of doubling potentials."""
import os
os.environ['SYMPY_GROUND_TYPES']='flint'
import json, math, sys
from fractions import Fraction as F
from math import comb
from pathlib import Path
import numpy as np
import gurobipy as gp
from gurobipy import GRB

OUT=Path('.research/agents/tdense8_scratch')

def bernrow(x,m):
    return np.array([comb(m,k)*x**k*(1-x)**(m-k) for k in range(m+1)])

def discovery(m,gram4=False):
    mod=gp.Model();mod.Params.OutputFlag=0;mod.Params.Threads=2
    mod.Params.FeasibilityTol=1e-9;mod.Params.OptimalityTol=1e-9
    rho=mod.addVar(lb=.7,ub=.86)
    b=mod.addVars(m+1,lb=0,ub=10)
    mod.addConstr(b[0]==0)
    for k in range(m):mod.addConstr(b[k+1]>=b[k])
    xx=np.unique(np.r_[np.linspace(1e-6,1,6001),1/math.sqrt(2)])
    for x in xx:
        y=max(0,2*x*x-1)
        if gram4:y=max(y,x-math.sqrt(max(0,1-x)))
        row=(bernrow(y,m)-bernrow(x,m)/2)/x
        mod.addConstr(rho-x+gp.quicksum(float(row[k])*b[k] for k in range(m+1))>=0)
    mod.setObjective(rho,GRB.MINIMIZE);mod.optimize()
    rec=dict(degree=m,rho=rho.X,b=[b[k].X for k in range(m+1)],status=mod.Status,gram4=gram4)
    print('DISCOVERY',json.dumps(rec),flush=True)
    OUT.joinpath(f'potential_{"g4_" if gram4 else ""}d{m}_numeric.json').write_text(json.dumps(rec,indent=2))
    return rec

def add(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,v in enumerate(a):c[i]+=v
    for i,v in enumerate(b):c[i]+=v
    return c
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c
def compose(a,b):
    c=[F(0)]
    for v in a[::-1]:c=add(mul(c,b),[v])
    return c
def power(a,k):
    c=[F(1)]
    for _ in range(k):c=mul(c,a)
    return c
def peval(a,x):
    y=F(0)
    for v in a[::-1]:y=y*x+v
    return y
def bern(a,lo,hi):
    n=len(a)-1
    q=[sum(a[j]*comb(j,k)*lo**(j-k)*(hi-lo)**k for j in range(k,n+1)) for k in range(n+1)]
    return [sum(q[j]*F(comb(k,j),comb(n,j)) for j in range(k+1)) for k in range(n+1)]
def certify(a,lo,hi,depth=0):
    bb=bern(a,lo,hi)
    if min(bb)>=0:return dict(ok=True,leaves=1,depth=depth,min_bound=str(min(bb)))
    if peval(a,(lo+hi)/2)<0:return dict(ok=False,negative_at=str((lo+hi)/2))
    if depth>=24:return dict(ok=False,unresolved=True)
    mid=(lo+hi)/2;l=certify(a,lo,mid,depth+1);r=certify(a,mid,hi,depth+1)
    return dict(ok=l['ok'] and r['ok'],leaves=l.get('leaves',0)+r.get('leaves',0),depth=max(l.get('depth',0),r.get('depth',0)))

def exact(rec):
    m=rec['degree'];den=10**9
    bs=[F(round(v*den),den) for v in rec['b']]
    assert bs[0]==0 and all(bs[k+1]>=bs[k] for k in range(m))
    beta=[F(0)]*(m+1)
    for k,v in enumerate(bs):
        for j in range(m-k+1):beta[k+j]+=v*comb(m,k)*comb(m-k,j)*(-1)**j
    # Rational cutoff is strictly above 1/sqrt(2). Tiny slack absorbs rounding.
    cut=F(707107,10**6);assert 2*cut*cut>1
    for slack in (F(1,10**5),F(1,10**4),F(1,1000)):
        rho=F(math.ceil(rec['rho']*10**6),10**6)+slack
        low=add([F(0),rho,F(-1)],[-v/2 for v in beta])
        high=add(low,compose(beta,[F(-1),F(0),F(2)]))
        assert low[0]==0
        if rec.get('gram4'):
            middle=add(compose(low,[F(1),F(0),F(-1)]),compose(beta,[F(1),F(-1),F(-1)]))
            deriv=[(i+1)*beta[i+1] for i in range(len(beta)-1)]
            checks=[certify(deriv,F(-1,1000),F(1)),certify(low[1:],F(0),F(61804,100000)),
                    certify(middle,F(366,1000),F(61804,100000)),certify(high,F(86603,100000),F(1))]
        else:checks=[certify(low[1:],F(0),cut),certify(high,cut,F(1))]
        if all(c['ok'] for c in checks):break
    result=dict(degree=m,gram4=rec.get('gram4',False),rho=str(rho),rho_float=float(rho),beta_bernstein=[str(v) for v in bs],
                beta_power=[str(v) for v in beta],cutoff=str(cut),checks=checks,proved=all(c['ok'] for c in checks))
    # Rational sufficient condition for a concrete T-dense reach, from P58.
    reaches=[]
    for rr in (F(769801,10**6),F(811,1000)):
        Cf=(2/float(rr))*(1+math.sqrt(1-float(rho)))**2
        C=F(math.floor(Cf*1000),1000);k=2/rr
        margin=k-(k*rho+C)**2/(4*C)
        reaches.append(dict(r=str(rr),C=str(C),margin=str(margin),positive=margin>0,limit_numeric=Cf))
    result['reaches']=reaches
    OUT.joinpath(f'potential_{"g4_" if rec.get("gram4") else ""}d{m}_exact.json').write_text(json.dumps(result,indent=2))
    print('EXACT',json.dumps(result),flush=True)
    return result

if __name__=='__main__':
    args=sys.argv[1:];g4='g4' in args;args=[v for v in args if v!='g4']
    for m in map(int,args or ['1','4','8','12']):exact(discovery(m,g4))
