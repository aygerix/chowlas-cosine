"""Gurobi adversarial design of symmetric nested schedules, VM only."""
from pathlib import Path
import json, time, math
import numpy as np
import gurobipy as gp
from gurobipy import GRB

ROOT=Path(__file__).resolve().parent
def solve(n,B,count):
    reps=np.arange(1,(n+1)//2);times=(np.arange(B)+.5)/B
    xis=np.unique(np.r_[np.linspace(0,60,121),np.linspace(.1,4,20)])
    model=gp.Model('round12_schedule');model.Params.Threads=4;model.Params.TimeLimit=55
    model.Params.Seed=1912;model.Params.OutputFlag=0
    a=model.addVars(len(reps),B,vtype=GRB.BINARY,name='assign')
    mu=model.addVar(lb=0,name='mu')
    for c in range(len(reps)):model.addConstr(gp.quicksum(a[c,j] for j in range(B))<=1)
    for j in range(B):model.addConstr(gp.quicksum(a[c,j] for c in range(len(reps)))==count)
    for s in range((n+1)//2):
        cos=2*np.cos(2*np.pi*s*reps/n)/n
        for xi in xis:
            v=times*np.sinc(xi*times/np.pi)
            model.addConstr(gp.quicksum(float(cos[c]*v[j])*a[c,j] for c in range(len(reps)) for j in range(B))+mu>=0)
    model.setObjective(mu,GRB.MINIMIZE);model.optimize()
    result=dict(N=n,B=B,count=count,status=int(model.Status),runtime=model.Runtime,
        bound=model.ObjBound,solutions=model.SolCount,solver=gp.gurobi.version())
    if model.SolCount:
        u=np.zeros(n)
        for c,r in enumerate(reps):
            for j in range(B):
                if a[c,j].X>.5:u[r]=u[-r]=times[j]
        from roughness_probe import analyze
        result.update(objective=model.ObjVal,probe=analyze(n,'gurobi_nested',u))
    (ROOT/f'milp_N{n}.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result|{'probe':{k:v for k,v in result.get('probe',{}).items() if k!='u'}}),flush=True)

if __name__=='__main__':
    solve(29,7,1)
    solve(61,5,3)
