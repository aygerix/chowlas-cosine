"""VM-only PWL profile escape. All quadratic optimization uses Gurobi.

p is even, piecewise linear at nodes i/B, supported in [-1,1]. Positive
definiteness is equivalent to positivity of its finite cosine interpolation
symbol; enforce on a finite grid, then independently refine/check the symbol.
The resulting search is still a finite necessary-condition relaxation.
"""
import sys,json,math
from pathlib import Path
import numpy as np
import gurobipy as gp
from gurobipy import GRB
OUT=Path('.research/agents/tdense7_scratch')

def weights(B,theta):
    # Three-point Gauss rule is exact for weight(deg2)*p^2(deg2).
    pts,ww=np.polynomial.legendre.leggauss(3)
    lin=np.zeros(B+1);sq=np.zeros(B+1);cross=np.zeros(B)
    for i in range(B):
        lo=i/B;hi=min((i+1)/B,theta)
        if hi<=lo:break
        ts=(lo+hi)/2+(hi-lo)*pts/2
        vals=ww*(hi-lo)/2*(1-ts/theta)**2
        rr=ts*B-i;ll=1-rr
        lin[i]+=sum(vals*ll);lin[i+1]+=sum(vals*rr)
        sq[i]+=sum(vals*ll*ll);sq[i+1]+=sum(vals*rr*rr)
        cross[i]+=sum(vals*2*ll*rr)
    return lin,sq,cross

def solve(B,rho,tl,mode,emin):
    m=gp.Model('tdense7_pwl_'+mode)
    m.Params.Threads=2;m.Params.NonConvex=2;m.Params.TimeLimit=tl;m.Params.MIPGap=.001
    m.Params.FeasibilityTol=1e-8;m.Params.OptimalityTol=1e-8;m.Params.Seed=1907
    p=m.addVars(B+1,lb=0,ub=1,name='p');u=m.addVars(B+1,lb=0,ub=1,name='u');v=m.addVars(B,lb=0,ub=1,name='v')
    for i in range(B+1):m.addQConstr(u[i]==p[i]*p[i])
    for i in range(B):m.addQConstr(v[i]==p[i]*p[i+1])
    m.addConstr(p[B]==0);m.addConstr(p[B-1]>=1e-5)
    d=(p[0]/2+gp.quicksum(p[i] for i in range(1,B)))/B
    b=d-gp.quicksum(u[i]+v[i]+u[i+1] for i in range(B))/(3*B)
    m.addConstr(b>=emin)
    m.addConstr(p[0]>=2*d/rho);m.addConstr(p[0]-u[0]>=2*b/rho)
    ths=sorted(set(np.r_[np.geomspace(1/(10*B),1,48),np.arange(1,B+1)/B].tolist()))
    for th in ths:
        lin,sq,cross=weights(B,th)
        dens=gp.quicksum(lin[i]*p[i] for i in range(B+1))
        energy=dens-gp.quicksum(sq[i]*u[i] for i in range(B+1))-gp.quicksum(cross[i]*v[i] for i in range(B))
        m.addConstr(rho*(1+th)*dens>=2*th*d/3)
        m.addConstr(rho*(1+th)*energy>=2*th*b/3)
    if mode in ('pd','envelope'):
        for ang in np.linspace(0,math.pi,1025 if B==24 else 4097):
            m.addConstr(p[0]+2*gp.quicksum(math.cos(i*ang)*p[i] for i in range(1,B))>=1e-6)
    if mode=='envelope':
        for i in range(1,B):
            m.addConstr(p[i]<=math.cos(math.pi/(math.floor(B/i)+2))*p[0])
    # A small nonzero support endpoint makes the scale normalization explicit.
    # Warm start from the previous coarser-grid solution when available.
    old=OUT/f'pwl_{mode}_B24_r{rho:.6f}_e{emin:.3f}.json'
    if B>24 and old.exists():
        base=json.loads(old.read_text())
        if 'p' in base:
            pp=np.interp(np.arange(B+1)/B,np.arange(len(base['p']))/(len(base['p'])-1),base['p'])
            for i in range(B+1):p[i].Start=pp[i];u[i].Start=pp[i]**2
            for i in range(B):v[i].Start=pp[i]*pp[i+1]
    m.setObjective(d,GRB.MAXIMIZE)
    m.optimize()
    rec=dict(B=B,rho=rho,mode=mode,emin=emin,status=int(m.Status),solcount=m.SolCount,
             runtime=m.Runtime,objbound=float(m.ObjBound) if m.Status not in (3,4) else None,
             windows=ths)
    if m.SolCount:
        pp=np.array([p[i].X for i in range(B+1)])
        dd=float((pp[0]/2+sum(pp[1:-1]))/B)
        bb=dd-float(sum(pp[:-1]**2+pp[:-1]*pp[1:]+pp[1:]**2)/(3*B))
        fine=np.r_[np.geomspace(1e-7,1,4000),np.arange(1,B+1)/B]
        ds=[];es=[]
        for th in fine:
            lin,sq,cross=weights(B,th)
            dens=float(lin@pp);energy=dens-float(sq@(pp*pp)+cross@(pp[:-1]*pp[1:]))
            ds.append((rho*(1+th)*dens-2*th*dd/3)/th)
            es.append((rho*(1+th)*energy-2*th*bb/3)/th)
        gg=1<<19;cc=np.zeros(gg);cc[0]=pp[0];cc[1:B]=pp[1:B];cc[-B+1:]=pp[1:B][::-1]
        symbol=np.fft.rfft(cc).real
        rec.update(p=pp.tolist(),density=dd,C=1/dd,energy=bb,
                   density_min_slack=float(min(ds)),energy_min_slack=float(min(es)),
                   density_bad_theta=float(fine[int(np.argmin(ds))]),energy_bad_theta=float(fine[int(np.argmin(es))]),
                   symbol_min_grid=float(min(symbol)),symbol_grid=gg,
                   symbol_Lipschitz=2*sum(i*pp[i] for i in range(1,B)),
                   max_eq_error=max(abs(u[i].X-pp[i]**2) for i in range(B+1)))
    name=f'pwl_{mode}_B{B}_r{rho:.6f}_e{emin:.3f}.json'
    OUT.joinpath(name).write_text(json.dumps(rec,indent=2))
    print('PWL_RESULT',json.dumps({k:v for k,v in rec.items() if k not in ('p','windows')}),flush=True)

if __name__=='__main__':
    mode=sys.argv[1];B=int(sys.argv[2]);tl=float(sys.argv[3]);rho=float(sys.argv[4]) if len(sys.argv)>4 else .7698
    emin=float(sys.argv[5]) if len(sys.argv)>5 else .01
    solve(B,rho,tl,mode,emin)
