"""Gurobi-only finite completion search for a planted Sidon clique; VM only."""
import json
import math
from pathlib import Path
import sys
import time

import gurobipy as gp
from gurobipy import GRB
import numpy as np

sys.path.insert(0,'src')
from singer import singer
from chowla import min_estimate_fft, certify_lower_bound

ROOT=Path('.research/agents/tdense17_scratch')


def main():
    out=[]
    for q in (3,5,7):
        C,_=singer(q)
        C=sorted(C)
        forced={b-a for a in C for b in C if b>a}
        assert len(forced)==len(C)*(len(C)-1)//2
        X=3*max(forced)
        a=np.arange(1,X+1)
        model=gp.Model('round17_sidon_completion')
        model.Params.Threads=4
        model.Params.TimeLimit=25
        model.Params.OutputFlag=0
        model.Params.Seed=17
        y=model.addVars(range(1,X+1),vtype=GRB.BINARY)
        z=model.addVar(lb=0)
        for v in forced: y[v].LB=1
        model.setObjective(z,GRB.MINIMIZE)
        for x in np.linspace(0,math.pi,4*X+1):
            co=np.cos(a*x)
            model.addConstr(gp.quicksum(float(c)*y[int(v)] for v,c in zip(a,co))+z>=0)
        for step in range(4):
            model.optimize()
            if model.SolCount==0: break
            A=[v for v in range(1,X+1) if y[v].X>0.5]
            est=min_estimate_fft(A,oversample=64,polish=32)
            if -est.fmin<=z.X+1e-5 or step==3: break
            for x in est.xmin+np.linspace(-2,2,9)/X:
                co=np.cos(a*x)
                model.addConstr(gp.quicksum(float(c)*y[int(v)] for v,c in zip(a,co))+z>=0)
        if model.SolCount==0: continue
        A=[v for v in range(1,X+1) if y[v].X>0.5]
        est=min_estimate_fft(A,oversample=64,polish=32)
        cert=certify_lower_bound(A,oversample=32,prec=110)
        rec=dict(q=q,C=C,A=A,cap=X,n=len(A),K_est=-2*est.fmin,
                 omega_over_K_est=len(C)/(-2*est.fmin),
                 certified_M_upper=-cert.lower_bound,
                 certified_omega_over_K_lower=len(C)/(-2*cert.lower_bound),
                 grid_objective=float(z.X), solver_status=int(model.Status),
                 solver_bound=float(model.ObjBound), version=gp.gurobi.version())
        out.append(rec)
        print(json.dumps(rec),flush=True)
    (ROOT/'sidon_completion.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__': main()
