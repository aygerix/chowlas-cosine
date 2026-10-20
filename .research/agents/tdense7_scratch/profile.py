"""VM-only Gurobi profile escape, piecewise constant finite relaxation.

Modes raw: sampled P31 and energy-P47 conditions; pd: additionally sampled
nonnegative cosine transform; envelope: sharp pointwise Caratheodory-Fejer bound.
Each is an explicitly finite necessary-condition relaxation, not all models.
"""
import sys, json, math, time
from pathlib import Path
import numpy as np
import gurobipy as gp
from gurobipy import GRB

OUT=Path('.research/agents/tdense7_scratch')
def solve(B,mode,rho,timelimit, emin=.01, gap=.001):
    m=gp.Model('tdense7_'+mode)
    m.Params.Threads=2; m.Params.NonConvex=2; m.Params.TimeLimit=timelimit
    m.Params.MIPGap=gap; m.Params.FeasibilityTol=1e-8; m.Params.OptimalityTol=1e-8
    m.Params.Seed=2026101907
    p=m.addVars(B,lb=0,ub=1,name='p'); e=m.addVars(B,lb=0,ub=.25,name='e')
    d=gp.quicksum(p[i] for i in range(B))/B; b=gp.quicksum(e[i] for i in range(B))/B
    for i in range(B):m.addQConstr(e[i]==p[i]-p[i]*p[i])
    m.addConstr(b>=emin)
    m.addConstr(p[B-1]>=1e-4) # support reaches 1, numerical version
    m.addConstr(p[0]>=2*d/rho); m.addConstr(e[0]>=2*b/rho)
    ths=sorted(set(np.r_[np.geomspace(1/B,1,24),np.arange(1,B+1)/B].tolist()))
    for th in ths:
        w=[]
        for i in range(B):
            lo=i/B; hi=min((i+1)/B,th)
            w.append(0 if hi<=lo else ((1-lo/th)**3-(1-hi/th)**3)*th/3)
        m.addConstr(2*th*d/3<=rho*(1+th)*gp.quicksum(w[i]*p[i] for i in range(B)))
        m.addConstr(2*th*b/3<=rho*(1+th)*gp.quicksum(w[i]*e[i] for i in range(B)))
    # Piecewise constant fixed profiles with nonzero jumps cannot have globally
    # nonnegative FT. Finite quadrature below is only a relaxation; interpolation
    # and exact transform reevaluation are performed separately.
    if mode in ('pd','envelope'):
        yy=np.r_[np.linspace(.25,20,100),np.linspace(20.5,100,160),np.linspace(102,300,100)]
        for y in yy:
            ft=[(math.sin(y*(i+1)/B)-math.sin(y*i/B))/y for i in range(B)]
            m.addConstr(gp.quicksum(ft[i]*p[i] for i in range(B))>=-1e-7)
    if mode=='envelope':
        for i in range(1,B):
            # Valid for a continuous limiting profile at t=i/B. The discretized
            # profile itself is a cell-average proxy, so use the left endpoint.
            u=math.cos(math.pi/(math.floor(B/i)+2))
            m.addConstr(p[i]<=u*p[0])
    m.setObjective(d,GRB.MAXIMIZE)
    m.optimize()
    rec=dict(status=int(m.Status),B=B,mode=mode,rho=rho,emin=emin,seconds=m.Runtime,
             objbound=float(m.ObjBound) if m.Status not in (3,4) else None,
             solcount=m.SolCount,grid_theta=ths)
    if m.SolCount:
        pp=[p[i].X for i in range(B)];ee=[e[i].X for i in range(B)]
        dd=sum(pp)/B;bb=sum(ee)/B
        th=np.r_[np.geomspace(1e-6,1,3000),np.arange(1,B+1)/B]
        def slack(v,total):
            vals=[]
            for tt in th:
                integ=sum(v[i]*max(0,((1-i/B/tt)**3-(1-min((i+1)/B,tt)/tt)**3)*tt/3)
                          for i in range(B) if i/B<tt)
                vals.append(rho*(1+tt)*integ-2*tt*total/3)
            j=int(np.argmin(vals));return dict(min=float(vals[j]),theta=float(th[j]))
        rec.update(p=pp,e=ee,density=dd,C=1/dd,energy=bb,
                   max_eq_error=max(abs(ee[i]-pp[i]*(1-pp[i])) for i in range(B)),
                   density_window=slack(pp,dd),energy_window=slack(ee,bb))
    name=f'profile_{mode}_B{B}_r{rho:.6f}_e{emin:.3f}.json'
    OUT.joinpath(name).write_text(json.dumps(rec,indent=2))
    print('PROFILE_RESULT',json.dumps({k:v for k,v in rec.items() if k not in ('p','e','grid_theta')}),flush=True)
    return rec

if __name__=='__main__':
    mode=sys.argv[1]; B=int(sys.argv[2]);tl=float(sys.argv[3]);rho=float(sys.argv[4]) if len(sys.argv)>4 else 4/(3*math.sqrt(3))
    emin=float(sys.argv[5]) if len(sys.argv)>5 else .01
    solve(B,mode,rho,tl,emin)
