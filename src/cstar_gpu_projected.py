"""General-seed, device-resident Fourier trust-region proposals.

This is a discovery solver. Integer reconstruction on Dirichlet is a
separate step. It optimizes a=n, Q<=24n in a growing subspace of the
full Fourier band, without asserting global optimality or an inverse theorem.
"""
import argparse
import json
import math
from pathlib import Path
import platform
import socket
import time

import numpy as np
from cstar_gpu_kernel import FourierCost, controls, synchronize, to_cpu


def small_ball_minimum(C, b, radius):
    """Minimize u'C u+2b'u in a small Euclidean ball, numerically."""
    vals,U=np.linalg.eigh((C+C.T)/2);d=U.T@b
    lo=max(0.,-vals[0]);tol=1e-11*max(1.,np.max(np.abs(vals)))
    gap=vals+lo;regular=gap>tol;u=np.zeros_like(d)
    u[regular]=-d[regular]/gap[regular]
    if np.linalg.norm(d[~regular])<tol and u@u<=radius*radius:
        if lo>0:u[np.argmin(vals)]=math.sqrt(max(0.,radius*radius-u@u))
        return U@u
    left=lo+tol;right=max(left+1.,2*left)
    while np.sum((d/(vals+right))**2)>radius*radius:right=2*right+1
    for _ in range(90):
        mid=(left+right)/2
        if np.sum((d/(vals+mid))**2)>radius*radius:left=mid
        else:right=mid
    return U@(-d/(vals+right))


def optimize(row,xp,band_factor=2,steps=4,random_count=16):
    A=row['A'];n=len(A);X=max(A);B=band_factor*X
    started=time.perf_counter();operator=FourierCost(A,list(range(1,B+1)),xp)
    center=xp.zeros(B,dtype=xp.float64);center[xp.asarray(A)-1]=1
    def tangent(rows):return rows-(rows@center)[:,None]*center[None,:]/n
    # Resolvent warm starts have unrestricted scalar complexity. Independent
    # random Fourier seeds make this more than a D-only polynomial Krylov space.
    Kgrid=-float(to_cpu(xp,xp.min(operator.D)))
    gaps=np.geomspace(1e-4,2.,12)
    lambdas=xp.asarray(Kgrid*(1+gaps))[:,None]
    h=1/(lambdas+operator.D[None,:]);means=xp.mean(h,axis=1)[:,None]
    values=n*(means-h)/(lambdas*means-1)
    seeds=2*xp.fft.rfft(values,axis=1,norm='forward')[:,1:B+1].real
    del values,h
    # V=2F_(2X)-F_X reproduces D exactly, is an L2 contraction, and
    # ||V||1<=3. This adds a quantitatively justified band<2X sign seed.
    Lgrid=float(to_cpu(xp,xp.mean(xp.abs(operator.D))))
    frequencies=xp.arange(1,B+1)
    taper=xp.maximum(0.,xp.minimum(1.,2.-frequencies/X))
    sign_seed=2*n/Lgrid*taper*xp.fft.rfft(xp.sign(operator.D),norm='forward')[1:B+1].real
    baseline=dict(a=float(to_cpu(xp,sign_seed@center)),
                  Q_over_n=float(to_cpu(xp,sign_seed@sign_seed))/(2*n),
                  H_over_n32=float(to_cpu(xp,sign_seed@operator.apply(sign_seed)[0]))/n**1.5)
    seeds=xp.concatenate([seeds,sign_seed[None,:]],axis=0)
    rng=np.random.default_rng(20261021)
    seeds=xp.concatenate([seeds,xp.asarray(rng.normal(size=(random_count,B)))],axis=0)
    Ccenter=operator.apply(center)[0]
    seeds=xp.concatenate([seeds,Ccenter[None,:]],axis=0)
    W=xp.zeros((0,B),dtype=xp.float64);CW=xp.zeros_like(W)
    trace=[];best=None
    for step in range(steps):
        block=tangent(seeds)
        for _ in range(2):
            if len(W):block-= (block@W.T)@W
            block=tangent(block)
        norms=xp.sqrt(xp.sum(block*block,axis=1))
        block=block[norms>1e-10]/norms[norms>1e-10,None]
        if not len(block):break
        gram=block@block.T;vals,U=xp.linalg.eigh((gram+gram.T)/2)
        keep=vals>1e-9*xp.max(vals)
        block=(U[:,keep]/xp.sqrt(vals[keep])[None,:]).T@block
        if not len(block):break
        Cblock=operator.apply(block)
        W=xp.concatenate([W,block],axis=0);CW=xp.concatenate([CW,Cblock],axis=0)
        Csmall=to_cpu(xp,W@CW.T);bsmall=to_cpu(xp,W@Ccenter)
        u=small_ball_minimum(Csmall,bsmall,math.sqrt(47*n))
        vector=center+xp.asarray(u)@W
        Q=float(to_cpu(xp,xp.sum(vector*vector)))/2
        H=float(to_cpu(xp,vector@operator.apply(vector)[0]))
        a=float(to_cpu(xp,vector@center))
        K=2*n*n/(H+math.sqrt(H*H+4*Q*n*n)) if H>=0 else (-H+math.sqrt(H*H+4*Q*n*n))/(2*Q)
        orth_error=float(to_cpu(xp,xp.max(xp.abs(W@W.T-xp.eye(len(W))))))
        assert abs(a-n)<1e-7*n and Q<=24.00001*n and orth_error<1e-5
        result=dict(step=step,dimension=len(W),a=a,Q_over_n=Q/n,H_over_n32=H/n**1.5,
                    proposed_M_lower=K/2,orthogonality_error=orth_error)
        trace.append(result)
        print(json.dumps(dict(label=row['label'],**result)),flush=True)
        if best is None or H<best[0]:best=(H,to_cpu(xp,vector).tolist())
        seeds=Cblock
    synchronize(xp)
    return dict(label=row['label'],A=A,n=n,band=B,fft_length=operator.length,
                beta_target=24,sign_baseline=baseline,trace=trace,cosine_coefficients=best[1],
                seconds=time.perf_counter()-started,
                qualification='Floating proposal only; subspace optimization is not a global optimum certificate.')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--backend',choices=['numpy','cupy'],default='numpy')
    parser.add_argument('--input',default='.research/experiments/l25_2026-10-21/probe.json')
    parser.add_argument('--labels',default='singer_integer_differences_p31')
    parser.add_argument('--band-factor',type=int,default=2)
    parser.add_argument('--steps',type=int,default=4)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    if platform.system()=='Darwin':raise SystemExit('Run research on Dirichlet or the authorized GPU worker.')
    xp=np
    if args.backend=='cupy':
        import cupy as xp
    labels=set(args.labels.split(','));source=json.loads(Path(args.input).read_text())
    rows=[r for r in source['cases'] if r['label'] in labels]
    assert len(rows)==len(labels)
    output=dict(host=socket.gethostname(),backend=args.backend,backend_version=xp.__version__,
                controls=controls(xp),seed=20261021,cases=[])
    path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True)
    for row in rows:
        output['cases'].append(optimize(row,xp,args.band_factor,args.steps))
        path.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',output=str(path))),flush=True)


if __name__=='__main__':main()
