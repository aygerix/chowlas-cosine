"""VM numerical probes of signed cubic gadgets and one finite raw-moment matching approximation.
No sampled minimum is called a certificate. Analytic global lower bounds are recorded.
"""
import os,json,math,sys
from pathlib import Path
import numpy as np
from sympy import nextprime
OUT=Path('.research/agents/tdense10_scratch')
SEED=2026101910

def fft_min(a):
    N=1<<int(math.ceil(math.log2(8*(len(a)+1))))
    c=np.zeros(N);c[1:len(a)+1]=a/2;c[-len(a):]=a[::-1]/2
    v=np.fft.ifft(c).real*N;ix=int(np.argmin(v));return dict(min=float(v[ix]),angle=float(2*np.pi*ix/N),grid=N,certificate='NUMERICAL')

def probe(X,alpha=.8,gamma=.03,lam=0.):
    L=int(nextprime(int(X**alpha)));B=(gamma*L)**(1/3);k=np.arange(1,X+1);t=k/X
    v=(1-t)*np.cos(lam*t);z=np.zeros(X);sel=(k%L)==0;z[sel]=B*v[sel]
    rows=[]
    for sign in (1,-1):
        zz=sign*z
        row=dict(X=X,alpha=alpha,L=L,B=B,gamma=gamma,lam=lam,sign=sign,nonzero=int(sel.sum()),mean=float(zz.mean()),second=float(np.mean(zz**2)),third=float(np.mean(zz**3)),fourth=float(np.mean(zz**4)),third_target=sign*gamma/4 if lam==0 else None,analytic_global_lower=-B/2 if sign==1 else -B*X/L,fft=fft_min(zz))
        rows.append(row);print(json.dumps(row),flush=True)
    return rows

def finite_demo(X=65536):
    # Explicit cosine-series approximation on a compact subinterval, then cube recursion.
    # This is a probe of convergence, not an exact finite match of all tests.
    rng=np.random.default_rng(SEED);k=np.arange(1,X+1);t=k/X;w=1-t;p=(1-np.sqrt(np.maximum(0,1-w*w)))/2;e=w*w/4;s=e*(1-2*p)
    J=int(X**.9);c=1/np.sqrt(32*J)
    # Occupancy FFT on a fine circle grid samples uniform centres from a finite subgroup.
    N=1<<int(math.ceil(math.log2(64*X)));thetaidx=rng.integers(0,N,J);counts=np.bincount(thetaidx,minlength=N);r=4*c*w*np.fft.fft(counts).real[1:X+1]
    base=p+r
    rows=[]
    # single positive cubic correction; deliberately fails the target shape, preserve numbers.
    L=int(nextprime(int(X**.8)));gamma=float(np.mean(s))*4;B=(gamma*L)**(1/3);z=np.zeros(X);sel=k%L==0;z[sel]=B*w[sel]
    for name,a,bound in [('base',base,-math.sqrt(J/8)-.25),('one_positive_family',base+z,-math.sqrt(J/8)-.25-B/2)]:
        row=dict(name=name,X=X,J=J,L=L,gamma=gamma,seed=SEED,first=float(a.mean()),first_target=float(p.mean()),second=float(np.mean(a*a)),second_target=float(p.mean()),third=float(np.mean(a**3)),third_target=float(p.mean()),fourth=float(np.mean(a**4)),fourth_target=float(p.mean()),residual_cube=float(np.mean((a-p)**3)),residual_cube_target=float(s.mean()),fraction_outside_0_1=float(np.mean((a<0)|(a>1))),analytic_global_lower=bound,fft=fft_min(a))
        rounded=(a>=.5).astype(float);row['rounding']=dict(n=int(rounded.sum()),maxA=int(np.flatnonzero(rounded)[-1]+1),coefficient_error_energy=float(np.mean((a-rounded)**2)),fft=fft_min(rounded))
        row['rounding']['R_numerical']=-row['rounding']['fft']['min']/math.sqrt(row['rounding']['n'])
        rows.append(row);print(json.dumps(row),flush=True)
    return rows

if __name__=='__main__':
    rows=[]
    for X in (4096,65536,1048576):rows.extend(probe(X))
    rows.extend(finite_demo())
    OUT.joinpath('third_probe.json').write_text(json.dumps(dict(status='NUMERICAL',seed=SEED,rows=rows),indent=2))
