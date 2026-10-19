"""R11 support-coupled discovery. VM only; every optimization uses Gurobi."""
import json, sys, math, time
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import numpy as np
import gurobipy as gp
OUT=Path('.research/agents/tdense11_scratch')
LINES=json.load(open('.research/agents/tdense9_scratch/long_gram_bounds.json'))
SUPPORT=json.load(open(OUT/'support_lines.json')) if (OUT/'support_lines.json').exists() else {}
def brow(x,m):
    return np.array([comb(m,k)*x**k*(1-x)**(m-k) for k in range(m+1)])
def run(K=64,deg=10,shape=.2,triple=0):
    started=time.time(); model=gp.Model(); model.Params.Threads=4
    model.Params.FeasibilityTol=1e-9; model.Params.OptimalityTol=1e-9
    model.Params.Method=2; model.Params.Crossover=0
    aa=model.addVars(K,lb=0,ub=2); bb=model.addVars(K,deg+1,lb=0,ub=10)
    cc=model.addVars(K,deg+1,lb=0,ub=10) if triple else None
    D=model.addVar(lb=0)
    for j in range(K):
        for vv in ([bb,cc] if triple else [bb]):
            model.addConstr(vv[j,0]==0)
            for i in range(deg):model.addConstr(vv[j,i+1]>=vv[j,i])
    # Include every line/Gram branch crossover in the discovery grid.
    xs=np.unique(np.r_[np.linspace(1e-7,1,600),1-np.geomspace(1e-10,.01,40),np.geomspace(1e-9,.001,20)])
    slopes=[float(Q(r['m'])) for r in LINES]; intercepts=[float(Q(r['b'])) for r in LINES]
    for i in range(len(slopes)):
        for j in range(i):
            if slopes[i]!=slopes[j]:
                x=(intercepts[j]-intercepts[i])/(slopes[i]-slopes[j])
                if 0<x<1:xs=np.r_[xs,x]
    xs=np.unique(np.r_[xs,(math.sqrt(5)-1)/2,1/math.sqrt(2)])
    splits=6 if triple else 2
    for jj in range(splits*K):
        j=jj//splits; tlo=jj/(splits*K)
        k=math.ceil(splits*K/jj)-1 if jj else 10**9
        cap=np.cos(np.pi/(k+2)) if jj else 1.
        xx=np.unique(np.r_[xs[xs<=cap],cap])
        extra=SUPPORT.get(str(k),[])
        for rr in extra:
            mm,bc=float(Q(rr['m'])),float(Q(rr['b']))
            for m,b in zip([0]+slopes,[0]+intercepts):
                if mm!=m:
                    cross=(b-bc)/(mm-m)
                    if 0<cross<cap:xx=np.r_[xx,cross]
        for x in xx:
            y=max([0,2*x*x-1,x-math.sqrt(max(0,1-x))]+[m*x+b for m,b in zip(slopes,intercepts)]+[float(Q(r['m']))*x+float(Q(r['b'])) for r in extra])
            z=max(0,4*x**3-3*x)
            bx=brow(x,deg)/x; by=brow(y,deg)/x; bz=brow(z,deg)/x
            val=x/(2*(1+math.sqrt(max(0,1-x*x))))
            expr=aa[j]-val-gp.quicksum(float(bx[i])*(bb[j,i]/2+(cc[j,i]/3 if triple else 0)) for i in range(deg+1))
            child2=jj*2//splits; child3=jj*3//splits
            if child2<K:expr+=gp.quicksum(float(by[i])*bb[child2,i] for i in range(deg+1))
            if triple and child3<K:expr+=gp.quicksum(float(bz[i])*cc[child3,i] for i in range(deg+1))
            model.addConstr(expr>=0)
    # Exact (up to floats) row integrals of quadratic U, no quadrature error.
    U=lambda x:1+shape*4*x*(1-x)
    V=lambda x:x+2*shape*x*x-4*shape*x**3/3
    clip=lambda x:np.clip(x,0,1)
    ss=np.linspace(0,1,1001)
    weights=np.array([(V(clip(ss-j/K))-V(clip(ss-(j+1)/K))+V(clip(ss+(j+1)/K))-V(clip(ss+j/K)))/U(ss) for j in range(K)]).T
    for row in weights:model.addConstr(gp.quicksum(float(row[j])*aa[j] for j in range(K))<=2*D)
    model.setObjective(D,gp.GRB.MINIMIZE); model.optimize(); assert model.SolCount
    rec=dict(K=K,degree=deg,shape=shape,triple=triple,D=D.X,C=1/D.X,a=[aa[j].X for j in range(K)],beta=[[bb[j,i].X for i in range(deg+1)] for j in range(K)],seconds=time.time()-started)
    if triple:rec['gamma']=[[cc[j,i].X for i in range(deg+1)] for j in range(K)]
    name=f'discovery_K{K}_d{deg}_s{shape}_t{triple}'+('_support' if SUPPORT else '')+'.json'
    OUT.joinpath(name).write_text(json.dumps(rec,indent=2))
    print('DISCOVERY_RESULT',json.dumps({k:v for k,v in rec.items() if k not in ('a','beta','gamma')}),flush=True)
if __name__=='__main__':run(int(sys.argv[1]),int(sys.argv[2]),float(sys.argv[3]),int(sys.argv[4]))
