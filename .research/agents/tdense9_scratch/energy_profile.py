"""VM-only Gurobi PWL ENERGY optimization, with p=(1-sqrt(1-q))/2.

q PD is the finite cosine symbol condition. Then e=q/4 is PD, and p PD
follows exactly from its Catalan series. No interpolation of p-p^2 is used.
Only discovery and dense-grid checks here; exact witness is separate.
"""
import json,math,sys,time
from pathlib import Path
import numpy as np
import gurobipy as gp
from gurobipy import GRB
OUT=Path('.research/agents/tdense9_scratch');R=4/(3*math.sqrt(3))

def vals(c):
    v=np.r_[c,0.];u=np.maximum(0,1-v[:-1]);w=np.maximum(0,1-v[1:]);aa=np.sqrt(u);bb=np.sqrt(w)
    ff=1-(2/3)*(u+aa*bb+w)/(aa+bb)
    num=ff.sum();den=.5*c[0]+c[1:].sum()
    gl=(aa+2*bb)/(3*(aa+bb)**2);gr=(bb+2*aa)/(3*(aa+bb)**2)
    grad=gl.copy();grad[1:]+=gr[:-1]
    return num,den,grad

def optimize(B,start,direct=False):
    if start=='triangle':cur=1-np.arange(B)/B
    else:
        g=np.sin(np.pi*(np.arange(B)+.5)/B)
        if start=='random':g=np.random.default_rng(2026101909+B).random(B)+.1
        cur=np.correlate(g,g,'full')[B-1:];cur/=cur[0]
    ang=np.linspace(0,np.pi,32*B+1);A=2*np.cos(np.outer(ang,np.arange(B)));A[:,0]=1
    fine=np.linspace(0,np.pi,512*B+1);Fine=2*np.cos(np.outer(fine,np.arange(B)));Fine[:,0]=1
    mod=gp.Model();mod.Params.OutputFlag=0;mod.Params.Threads=2
    mod.Params.FeasibilityTol=1e-9;mod.Params.OptimalityTol=1e-9
    q=mod.addMVar(B,lb=0,ub=1);mod.addConstr(q[0]==1);mod.addConstr(A@q>=0)
    if direct:mod.addConstr(np.r_[.5,np.ones(B-1)]@q<=B*R/2)
    for it in range(120):
        num,den,gn=vals(cur);kap=num/den;grad=gn-kap*np.r_[.5,np.ones(B-1)];grad[0]=0
        mod.setObjective((gn if direct else grad)@q,GRB.MAXIMIZE)
        for refine in range(10):
            mod.optimize();assert mod.SolCount
            cand=q.X.copy();sym=Fine@cand
            bad=np.flatnonzero((sym[1:-1]<sym[:-2])&(sym[1:-1]<sym[2:])&(sym[1:-1]<-1e-8))+1
            if not len(bad):break
            mod.addConstr(Fine[bad]@q>=0)
        nnum,nden,_=vals(cand)
        if (it>0 and nnum<num+1e-10 if direct else nnum/nden<kap+1e-11):break
        cur=cand
    num,den,_=vals(cur);I1=den/B;IF=num/B;phi=min(1.,R/(2*I1))*.99999 if direct else min(.999,R/(2*I1))*.999
    # Independent quadrature for p and all fixed-scale windows.
    pts,ww=np.polynomial.legendre.leggauss(40)
    def integrate(th,which):
        total=0.
        for i in range(B):
            lo=phi*i/B;hi=min(phi*(i+1)/B,th)
            if hi<=lo:break
            ts=(lo+hi)/2+(hi-lo)*pts/2;rr=ts*B/phi-i
            qq=(1-rr)*cur[i]+rr*(cur[i+1] if i+1<B else 0.)
            v=qq/4 if which=='energy' else (1-np.sqrt(np.maximum(0,1-qq)))/2
            total+=(ww*((1-ts/th)**2)*v).sum()*(hi-lo)/2
        return total
    d=phi*IF/2;b=phi*I1/4
    ths=np.unique(np.r_[np.geomspace(1e-7,1,800),np.linspace(.001,1,800)])
    wins={}
    for name,total in [('density',d),('energy',b)]:
        sl=np.array([R*(1+th)*integrate(th,name)/th-(2/3)*total for th in ths])
        wins[name]=dict(min_slack=float(sl.min()),theta=float(ths[sl.argmin()]))
    sym=Fine@cur
    row=dict(B=B,start=start,kappa=num/den,C_zero_window=4/(R*num/den),C_witness=1/d,d=d,a=.5,phi=phi,q=cur.tolist(),iterations=it,symbol_min=float(sym.min()),windows=wins,seed=2026101909+B)
    row['direct_density']=direct
    OUT.joinpath(f'{"full" if direct else "energy"}_B{B}_{start}.json').write_text(json.dumps(row,indent=2))
    print('PROFILE',json.dumps({k:v for k,v in row.items() if k!='q'}),flush=True)
    return row
if __name__=='__main__':
    args=sys.argv[1:];direct='full' in args;args=[v for v in args if v!='full']
    for B in map(int,args or ['40','80','160']):
        for start in ['half_sine','triangle','random']:optimize(B,start,direct)
