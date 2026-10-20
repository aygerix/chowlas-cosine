"""VM-only Gurobi discovery; rational rectangle certificate for joint p,e PD."""
import json,sys,math
from fractions import Fraction as F
from pathlib import Path
import numpy as np
import gurobipy as gp
from gurobipy import GRB
from math import comb,isqrt
OUT=Path('.research/agents/tdense9_scratch')
sys.path.insert(0,str(Path('.research/agents/tdense8_scratch').resolve()))
from potential import add,mul,compose,peval,bern

def brow(x,m):return np.array([comb(m,k)*x**k*(1-x)**(m-k) for k in range(m+1)])
def lower(x,a):
    ex=x*(1-a*x)/(1-a)
    z=max(0,2*ex*ex-1,ex-math.sqrt(max(0,1-ex)))
    ye=2*z*(1-a)/(1+math.sqrt(max(0,1-4*a*z*(1-a))))
    return max(0,2*x*x-1,x-math.sqrt(max(0,1-x)),ye)

def discover(a0,deg=8):
    mod=gp.Model();mod.Params.OutputFlag=0;mod.Params.Threads=2
    mod.Params.FeasibilityTol=1e-9;mod.Params.OptimalityTol=1e-9
    rho=mod.addVar(lb=.65,ub=.83);b=mod.addVars(deg+1,lb=0,ub=10)
    mod.addConstr(b[0]==0)
    for k in range(deg):mod.addConstr(b[k+1]>=b[k])
    for x in np.unique(np.r_[np.linspace(1e-6,1,3501),.5,.75]):
        # Sample every amplitude. The certificate later covers the entire interval.
        y=min(lower(float(x),float(a)) for a in np.linspace(a0,.5,21))
        row=(brow(y,deg)-brow(x,deg)/2)/x
        mod.addConstr(rho-x+gp.quicksum(float(row[k])*b[k] for k in range(deg+1))>=0)
    mod.setObjective(rho,GRB.MINIMIZE);mod.optimize()
    assert mod.SolCount
    rec=dict(a0=str(F(str(a0))),deg=deg,rho=rho.X,b=[b[k].X for k in range(deg+1)])
    OUT.joinpath(f'joint_a{a0:.3f}_d{deg}_numeric.json').write_text(json.dumps(rec,indent=2))
    print('DISCOVERY',json.dumps(rec),flush=True)
    return rec

def sqrtup(q,bits=70):
    assert q>=0
    den=1<<bits
    z=isqrt(q.numerator*den*den//q.denominator)
    if F(z*z,den*den)<q:z+=1
    return F(z,den)
def lowerbox(x,alo,ahi):
    ex=x*(1-alo*x)/(1-alo)
    z=max(F(0),2*ex*ex-1,ex-sqrtup(1-ex))
    ye=2*z*(1-ahi)/(1+sqrtup(1-4*ahi*z*(1-ahi)))
    return max(F(0),2*x*x-1,x-sqrtup(1-x),ye)
def certificate(rec,slack=F(1,10000),maxdepth=30):
    deg=rec['deg'];bb=[F(round(v*10**10),10**10) for v in rec['b']]
    assert bb[0]==0 and all(bb[i+1]>=bb[i] for i in range(deg))
    beta=[F(0)]*(deg+1)
    for k,v in enumerate(bb):
        for j in range(deg-k+1):beta[k+j]+=v*comb(deg,k)*comb(deg-k,j)*(-1)**j
    rho=F(math.ceil(rec['rho']*10**6),10**6)+slack
    A=add([F(0),rho,-F(1)],[-v/2 for v in beta]);A=A[1:]
    a0=F(rec['a0']);stack=[(F(0),F(1),a0,F(1,2),0)];leaves=0;maxd=0;unresolved=[]
    while stack:
        l,u,al,au,depth=stack.pop()
        yl=lowerbox(l,al,au)
        bound=min(bern(A,l,u))+peval(beta,yl)/u
        if bound>=0:
            leaves+=1;maxd=max(maxd,depth);continue
        if depth>=maxdepth:
            unresolved.append([str(v) for v in (l,u,al,au,bound)]);break
        # Relative sensitivity is concentrated near a=1/2; split both coordinates.
        if (u-l)>2*(au-al) or al==au:
            mid=(l+u)/2;stack.extend([(l,mid,al,au,depth+1),(mid,u,al,au,depth+1)])
        else:
            mid=(al+au)/2;stack.extend([(l,u,al,mid,depth+1),(l,u,mid,au,depth+1)])
    out=dict(status='PROVED' if not unresolved else 'UNRESOLVED',a_interval=[str(a0),'1/2'],rho=str(rho),beta_bernstein=[str(v) for v in bb],beta_power=[str(v) for v in beta],leaves=leaves,maxdepth=maxd,unresolved=unresolved)
    # Below a0, use the quoted rho .815276; above it use joint rho.
    r=F(769801,10**6);old=F(203819,250000)
    dlow=(r/2)*a0*(1-a0)/(1-old*a0);dhigh=r/(4*(2-rho));dmax=max(dlow,dhigh)
    out.update(d_bound=str(dmax),C_bound=str(1/dmax),C_float=float(1/dmax),old_range_C=float(1/dlow),joint_C=float(1/dhigh))
    OUT.joinpath(f'joint_a{float(a0):.3f}_d{deg}_exact.json').write_text(json.dumps(out,indent=2))
    print('CERTIFICATE',json.dumps(out),flush=True)
    return out

if __name__=='__main__':
    for a in map(float,sys.argv[1:] or ['.4','.45','.48','.49']):certificate(discover(a))
