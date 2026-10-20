"""VM-only local Gurobi LP ascent, general DP PWL vs nonnegative autocorrelations.

All reported maxima are NUMERICAL local results. No global optimality claim.
"""
import os,json,math,time,sys
from pathlib import Path
import numpy as np
import gurobipy as gp
from gurobipy import GRB
OUT=Path('.research/agents/tdense8_scratch')

def integrals(c):
    v=np.r_[c,0.]
    return .5*v[0]+v[1:].sum(),sum((v[:-1]**2+v[:-1]*v[1:]+v[1:]**2)/3)
def autocorr(g):
    v=np.correlate(g,g,'full')[len(g)-1:]
    return v/v[0]
def obj(g):
    c=autocorr(g);a,b=integrals(c)
    return b/a

def optimize_autocorr(N,g0,steps=400,method='prox'):
    # Nonnegative g, ||g||_2=1. Linearize quartic correlation energy and use
    # a Gurobi proximal QP, or the initial unit-ball QCP, plus line search.
    g=g0/np.linalg.norm(g0)
    for it in range(steps):
        # Analytic gradient of J for the PWL autocorrelation.
        q=np.correlate(g,g,'full')[N-1:];I1,I2=integrals(q);lam=I2/I1
        gradq=np.zeros(N)
        v=np.r_[q,0.]
        gradq[:]=(4*q+np.r_[0,q[:-1]]+np.r_[q[1:],0])/3
        gradq[0]-=2*q[0]/3
        gradq-=lam*np.r_[.5,np.ones(N-1)]
        # q0 is fixed under unit-norm normalization; account for its J denominator.
        gradq[0]-=lam*I1
        grad=2*gradq[0]*g
        for k in range(1,N):
            grad[:-k]+=gradq[k]*g[k:];grad[k:]+=gradq[k]*g[:-k]
        mod=gp.Model();mod.Params.OutputFlag=0;mod.Params.Threads=2;mod.Params.NonConvex=2
        z=mod.addVars(N,lb=0)
        if method=='legacy':
            mod.addQConstr(gp.quicksum(z[j]*z[j] for j in range(N))<=1)
            mod.setObjective(gp.quicksum(float(grad[j])*z[j] for j in range(N)),GRB.MAXIMIZE)
        else:
            grad/=I1
            mod.setObjective(gp.quicksum(float(grad[j])*(z[j]-float(g[j]))-(z[j]-float(g[j]))*(z[j]-float(g[j]))/(20*N) for j in range(N)),GRB.MAXIMIZE)
        mod.optimize()
        if mod.SolCount==0:break
        target=np.array([z[j].X for j in range(N)])
        if np.linalg.norm(target)<1e-10:break
        best=(obj(g),g)
        for alpha in (2.**(-j) for j in range(22)):
            new=(1-alpha)*g+alpha*target;new/=np.linalg.norm(new)
            cand=obj(new)
            if cand>best[0]:best=(cand,new)
        if best[0]<=obj(g)+1e-12:break
        g=best[1]
    return g,it,obj(g)

def general(B,c0,steps=120):
    th=np.linspace(0,np.pi,32*B+1)
    C=np.cos(np.outer(th,np.arange(B)))
    model=gp.Model();model.Params.OutputFlag=0;model.Params.Threads=2
    model.Params.FeasibilityTol=1e-9;model.Params.OptimalityTol=1e-9
    c=model.addMVar(B,lb=0,ub=1);model.addConstr(c[0]==1)
    A=2*C;A[:,0]=1
    model.addConstr(A@c>=0)
    fine=np.linspace(0,np.pi,512*B+1)
    Fine=np.cos(np.outer(fine,np.arange(1,B)))
    cur=c0.copy()
    for it in range(steps):
        I1,I2=integrals(cur);lam=I2/I1
        grad=(4*cur+np.r_[0,cur[:-1]]+np.r_[cur[1:],0])/3;grad[0]-=2*cur[0]/3
        grad-=lam*np.r_[.5,np.ones(B-1)]
        model.setObjective(grad@c,GRB.MAXIMIZE)
        for refine in range(12):
            model.optimize()
            if model.SolCount==0:break
            candidate=c.X.copy();symbol=candidate[0]+2*Fine@candidate[1:]
            bad=np.flatnonzero((symbol[1:-1]<symbol[:-2])&(symbol[1:-1]<symbol[2:])&(symbol[1:-1]<-1e-8))+1
            if not len(bad):break
            for j in bad:model.addConstr(c[0]+2*Fine[j]@c[1:]>=0)
        if model.SolCount==0:break
        nxt=c.X.copy();nI1,nI2=integrals(nxt)
        if nI2/nI1<=lam+1e-10:break
        cur=nxt
    symbol=cur[0]+2*Fine@cur[1:]
    # A numerical diagonal repair guarantees only a sampled/floating bound here.
    repair=max(0.,-float(symbol.min()))+1e-8
    repaired=cur.copy();repaired[0]+=repair;repaired/=repaired[0]
    I1,I2=integrals(cur);rI1,rI2=integrals(repaired)
    return dict(J=I2/I1,J_repaired_numeric=rI2/rI1,min_symbol_fine=float(symbol.min()),
                repair=repair,iterations=it,c=cur.tolist())

def run():
    rows=[];rng=np.random.default_rng(2026101908)
    for B in (40,80,160):
        grid=(np.arange(B)+.5)/B
        starts=[('half_sine',np.sin(np.pi*grid)),('random',rng.random(B)+.1)]
        for name,g0 in starts:
            t=time.time();g,it,J=optimize_autocorr(B,g0,method='legacy')
            row=dict(class_name='autocorrelation',B=B,start=name,J=J,iterations=it,seconds=time.time()-t,g=g.tolist())
            rows.append(row);print(json.dumps({k:v for k,v in row.items() if k!='g'}),flush=True)
            t=time.time();rec=general(B,autocorr(g))
            row=dict(class_name='general_pwl',B=B,start=name,seconds=time.time()-t,**rec)
            rows.append(row);print(json.dumps({k:v for k,v in row.items() if k!='c'}),flush=True)
            OUT.joinpath('profile_numeric.json').write_text(json.dumps(rows,indent=2))
    print('DONE',flush=True)

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='auto':
        rows=[]
        for B in (160,400,800):
            grid=(np.arange(B)+.5)/B
            g,it,J=optimize_autocorr(B,np.sin(np.pi*grid))
            row=dict(B=B,start='half_sine',J=J,iterations=it,g=g.tolist())
            rows.append(row);print(json.dumps({k:v for k,v in row.items() if k!='g'}),flush=True)
        OUT.joinpath('autocorrelation_refined.json').write_text(json.dumps(rows,indent=2))
    else:run()
