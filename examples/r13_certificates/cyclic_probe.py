"""Round 13 cyclic trade-offs and profile rounding. Run only via dirun -c 4."""
from pathlib import Path
import json, math, re, platform, time
import numpy as np
import gurobipy as gp
from gurobipy import GRB
from flint import arb, ctx
ctx.prec=180
ROOT=Path(__file__).resolve().parent

def balls(q, pairs):
    values=[]
    for g in range(1,(q+1)//2):
        v=arb(0)
        for a in pairs:v+=2*(2*arb.pi()*((g*a)%q)/q).cos()
        values.append(v)
    lo=min(float(v.lower()) for v in values);hi=min(float(v.upper()) for v in values)
    llo=max(float(v.lower()) for v in values);lhi=max(float(v.upper()) for v in values)
    imin=min(range(len(values)),key=lambda i:float(values[i].mid()))
    imax=max(range(len(values)),key=lambda i:float(values[i].mid()))
    return dict(K_interval=[float(np.nextafter(-hi,-np.inf)),float(np.nextafter(-lo,np.inf))],
                Lambda_interval=[float(np.nextafter(llo,-np.inf)),float(np.nextafter(lhi,np.inf))],
                K_ball=str(-values[imin]),Lambda_ball=str(values[imax]),arb_bits=ctx.prec)

def tradeoffs():
    known={}
    for fn in ('e41_small.txt','e41_mid.txt'):
        for line in (Path('examples/zp_half')/fn).read_text().splitlines():
            mm=re.search(r'p=(\d+).*minM=([\d.]+).*P=([\d ]+)',line)
            if mm:known[int(mm[1])]=(float(mm[2]),[int(x) for x in mm[3].split()])
    out=[]
    for q in (17,37,61,89,101,109):
        h=(q-1)//2;m=(q-1)//4
        C=2*np.cos(2*np.pi*np.outer(np.arange(1,h+1),np.arange(1,h+1))/q)
        if q in known:kmin,seed=known[q];kmin_status='E41 double-precision enumeration, quoted'
        else:
            model=gp.Model();model.Params.OutputFlag=0;model.Params.Threads=4;model.Params.TimeLimit=8
            model.Params.Seed=1913
            b=model.addMVar(h,vtype=GRB.BINARY);kk=model.addVar(lb=0)
            model.addConstr(b.sum()==m);model.addConstr(C@b+kk>=0)
            model.setObjective(kk);model.optimize()
            seed=(np.flatnonzero(b.X>.5)+1).tolist();kmin=float(kk.X)
            kmin_status=f'Gurobi status {model.Status}, bound {model.ObjBound}'
        seedarr=np.zeros(q);seedarr[seed]=1;seedarr[[-x for x in seed]]=1
        F=np.fft.fft(seedarr).real;g=int(np.argmax(F[1:])+1)
        seed=sorted(set(min((g*a)%q,q-(g*a)%q) for a in seed))
        kbase=balls(q,seed)['K_interval'][1]
        for factor in (1,1.025,1.075,1.15,1.35,1.7):
            kap=kbase*factor+2e-8
            model=gp.Model();model.Params.OutputFlag=0;model.Params.Threads=4
            model.Params.TimeLimit=5 if q<=61 else 8
            model.Params.MIPGap=0;model.Params.FeasibilityTol=1e-9;model.Params.IntFeasTol=1e-9
            model.Params.Seed=1913
            b=model.addMVar(h,vtype=GRB.BINARY,name='pair')
            b.Start=np.isin(np.arange(1,h+1),seed).astype(float)
            model.addConstr(b.sum()==m);model.addConstr(C@b>=-kap)
            model.setObjective(C[0]@b,GRB.MAXIMIZE);model.optimize()
            row=dict(q=q,kappa=kap,factor=factor,K_min_input=kbase,K_min_status=kmin_status,
                     status=int(model.Status),runtime=model.Runtime,bound=model.ObjBound,
                     solver=gp.gurobi.version(),solutions=model.SolCount)
            if model.SolCount:
                pairs=(np.flatnonzero(b.X>.5)+1).tolist()
                row.update(pairs=pairs,objective=model.ObjVal,certificate=balls(q,pairs))
            out.append(row)
            (ROOT/'cyclic_tradeoffs.json').write_text(json.dumps(out,indent=2))
            print(json.dumps({k:v for k,v in row.items() if k!='pairs'}),flush=True)
    return out

def profiles():
    rows=[]
    for q in (257,1021,4093,16381,65537):
        rng=np.random.default_rng(1913000+q);h=(q-1)//2;m=(q-1)//4
        a=np.arange(1,h+1);p=.5+.2*np.cos(2*np.pi*a/q)
        bits=rng.random(h)<p
        if bits.sum()>m:bits[rng.choice(np.flatnonzero(bits),int(bits.sum()-m),replace=False)]=False
        elif bits.sum()<m:bits[rng.choice(np.flatnonzero(~bits),int(m-bits.sum()),replace=False)]=True
        pairs=(np.flatnonzero(bits)+1).tolist();b=np.zeros(q);b[pairs]=1;b[[-a for a in pairs]]=1
        F=np.fft.fft(b).real
        row=dict(q=q,epsilon=.2,seed=1913000+q,n=int(b.sum()),K=float(-F[1:].min()),
                 Lambda=float(F[1:].max()),lambda1=float(F[1]),pairs=pairs)
        if q<=1021:row['certificate']=balls(q,pairs)
        rows.append(row)
        (ROOT/'cyclic_profiles.json').write_text(json.dumps(rows,indent=2))
        print('PROFILE',json.dumps({k:v for k,v in row.items() if k!='pairs'}),flush=True)
    return rows

if __name__=='__main__':
    print(platform.python_version(),np.__version__,gp.gurobi.version(),flush=True)
    profiles();tradeoffs()
