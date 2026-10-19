"""Support-sensitive lower lines for w(2t), obtained from nonnegative symbols.
All LPs Gurobi; exact rational reconstruction. VM only.
"""
import json
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
import gurobipy as gp
OUT=Path('.research/agents/tdense11_scratch')
def cheb(z,k):
    r=[Q(1),z]
    for n in range(2,k+1):r.append(2*z*r[-1]-r[-2])
    return r
def run():
    zz=np.linspace(-1,1,1001); zq=[Q(i,500) for i in range(-500,501)]
    records={}
    for k in range(2,17):
        A=np.polynomial.chebyshev.chebvander(zz,k)
        model=gp.Model();model.Params.OutputFlag=0;model.Params.Threads=4
        model.Params.FeasibilityTol=1e-9;model.Params.OptimalityTol=1e-9
        weights=model.addMVar(len(zz),lb=0)
        model.addConstr(2*A[:,2]@weights==1)
        if k>=3:model.addConstr(2*A[:,3:].T@weights<=0)
        rr=[]
        for x0 in np.r_[np.arange(.35,.96,.05),.97,.99]:
            model.setObjective((1+2*x0*zz)@weights,gp.GRB.MINIMIZE);model.optimize()
            if not model.SolCount:continue
            aq=[Q(round(v*10**12),10**12) for v in weights.X]
            nz=[(z,a) for z,a in zip(zq,aq) if a>0]
            moments=[sum((2*a*cheb(z,k)[n] for z,a in nz),Q(0)) for n in range(k+1)]
            if moments[2]<=0:continue
            err=sum((max(Q(0),v) for v in moments[3:]),Q(0))
            slope=-moments[1]/moments[2];intercept=-(sum((a for z,a in nz),Q(0))+err)/moments[2]
            row=dict(k=k,x0=float(x0),m=str(slope),b=str(intercept),nodes=[[str(z),str(a)] for z,a in nz],positive_moment_repair=str(err),normalization=str(moments[2]))
            rr.append(row)
        records[str(k)]=rr
        print('SUPPORT_LINES',k,'count',len(rr),'at_0.6',max(float(Q(r['m']))*.6+float(Q(r['b'])) for r in rr),flush=True)
    OUT.joinpath('support_lines.json').write_text(json.dumps(records,indent=2))
if __name__=='__main__':run()
