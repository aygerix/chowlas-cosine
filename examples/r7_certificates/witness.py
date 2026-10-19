"""VM-only rational PD/window repair, exact certificates, and actual roundings."""
import os
os.environ['SYMPY_GROUND_TYPES']='flint'
import json,sys,math,time
from pathlib import Path
from fractions import Fraction as F
from math import comb
import numpy as np
import sympy as sp
from evaluate import check
OUT=Path('.research/agents/tdense7_scratch')

def peval(poly,x):
    s=F(0)
    for c in poly[::-1]:s=s*x+c
    return s
def bernstein(poly,lo,hi):
    deg=len(poly)-1
    q=[sum(poly[j]*comb(j,k)*lo**(j-k)*(hi-lo)**k for j in range(k,deg+1)) for k in range(deg+1)]
    return [sum(q[j]*F(comb(k,j),comb(deg,j)) for j in range(k+1)) for k in range(deg+1)]
def certpoly(poly,lo,hi,depth=0):
    bb=bernstein(poly,lo,hi)
    if min(bb)>=0:return dict(ok=True,leaves=1,min_bernstein=float(min(bb)),depth=depth)
    if peval(poly,(lo+hi)/2)<0:return dict(ok=False,negative_at=str((lo+hi)/2))
    if depth>=30:return dict(ok=False,reason='unresolved Bernstein depth')
    mid=(lo+hi)/2;a=certpoly(poly,lo,mid,depth+1);b=certpoly(poly,mid,hi,depth+1)
    return dict(ok=a['ok'] and b['ok'],leaves=a.get('leaves',0)+b.get('leaves',0),
                depth=max(a.get('depth',0),b.get('depth',0)),min_bernstein=min(a.get('min_bernstein',0),b.get('min_bernstein',0)))

def allwindows(pp,rho):
    B=len(pp)-1
    ppolys=[[pp[i]-i*(pp[i+1]-pp[i]),B*(pp[i+1]-pp[i])] for i in range(B)]
    epolys=[[c[0]-c[0]*c[0],c[1]-2*c[0]*c[1],-c[1]*c[1]] for c in ppolys]
    recs={}
    for name,polys in [('density',ppolys),('energy',epolys)]:
        moments=[F(0)]*3
        for i,v in enumerate(polys):
            lo=F(i,B);hi=F(i+1,B)
            for ell in range(3):moments[ell]+=sum(c*(hi**(k+ell+1)-lo**(k+ell+1))/F(k+ell+1) for k,c in enumerate(v))
        total=moments[0];prev=[F(0)]*3;checks=[]
        for i,v in enumerate(polys):
            lo=F(i,B);hi=F(i+1,B);J=[F(0)]*6
            J[0]=prev[2];J[1]=-2*prev[1];J[2]=prev[0]
            for k,c in enumerate(v):
                J[k+3]+=2*c/F((k+1)*(k+2)*(k+3))
                J[2]-=c*lo**(k+1)/F(k+1)
                J[1]+=2*c*lo**(k+2)/F(k+2)
                J[0]-=c*lo**(k+3)/F(k+3)
            R=[F(0)]*7
            for j,c in enumerate(J):R[j]+=rho*c;R[j+1]+=rho*c
            R[3]-=F(2,3)*total
            if i==0:
                assert R[:3]==[0,0,0]
                R=R[3:]
            cc=certpoly(R,lo,hi);cc.update(cell=i);checks.append(cc)
            for ell in range(3):prev[ell]+=sum(c*(hi**(k+ell+1)-lo**(k+ell+1))/F(k+ell+1) for k,c in enumerate(v))
        recs[name]=dict(total=str(total),ok=all(c['ok'] for c in checks),checks=checks)
    return recs

def certify(B):
    base=json.loads(OUT.joinpath(f'pwl_pd_B{B}_r0.769800_e0.010.json').read_text())
    amp=F(999,1000);diag=F(1,20000) if B>=48 else F(1,1000)
    pp=[F(round(p*10**9),10**9)*amp for p in base['p']]
    pp[0]+=diag;pp[-1]=F(0)
    # Exact positivity of the interpolation symbol by Sturm root count.
    t=sp.Symbol('t');T0=sp.Poly(1,t,domain=sp.QQ);T1=sp.Poly(t,t,domain=sp.QQ)
    S=sp.Poly(sp.Rational(pp[0].numerator,pp[0].denominator),t,domain=sp.QQ)
    for i in range(1,B):
        Ti=T1 if i==1 else 2*sp.Poly(t,t)*T1-T0
        if i>1:T0,T1=T1,Ti
        S+=2*sp.Rational(pp[i].numerator,pp[i].denominator)*Ti
    t0=time.time();roots=int(S.count_roots(-1,1));val=S.eval(1);pdok=roots==0 and val>0
    windows=allwindows(pp,F(3849,5000))
    dd=(pp[0]/2+sum(pp[1:-1]))/B
    rec=dict(B=B,p=[str(p) for p in pp],density=str(dd),density_float=float(dd),C=float(1/dd),
             amplitude=str(amp),diagonal_repair=str(diag),symbol_roots_in_unit_interval=roots,
             symbol_value_at_one=str(val),PD_proved=bool(pdok),sturm_seconds=time.time()-t0,
             windows=windows,window_status='PROVED by exact rational Bernstein coefficients when ok=True',
             rho=str(F(3849,5000)))
    OUT.joinpath(f'witness_B{B}.json').write_text(json.dumps(rec,indent=2))
    print('WITNESS',json.dumps({k:v for k,v in rec.items() if k not in ('p','windows','symbol_value_at_one','density')}),flush=True)
    assert pdok and windows['density']['ok'] and windows['energy']['ok']
    return rec

def probabilities(pp,X):
    B=len(pp)-1
    nodes=np.array([float(x) for x in pp]);areas=(nodes[:-1]+nodes[1:])/(2*B);cum=np.r_[0,np.cumsum(areas)]
    ts=np.arange(X+1)/X;ii=np.minimum(B-1,np.floor(ts*B).astype(int));rr=ts-ii/B
    integral=cum[ii]+nodes[ii]*rr+(nodes[ii+1]-nodes[ii])*B*rr*rr/2
    return np.diff(integral)*X

def realize(B):
    rec=json.loads(OUT.joinpath(f'witness_B{B}.json').read_text());pp=[F(s) for s in rec['p']];d=float(F(rec['density']))
    rng=np.random.default_rng(2026101907);sets={};checks=[];construction=[]
    for n in (512,1024,2048,4096):
        X=math.ceil(n/d);prob=probabilities(pp,X);prob*=n/prob.sum()
        assert min(prob)>=-1e-10 and max(prob)<1
        for mode in ('cumulative','conditional_bernoulli'):
            if mode=='cumulative':
                bits=np.diff(np.floor(np.r_[0,np.cumsum(prob)]+.3721)).astype(int);tries=1
            else:
                for tries in range(1,10001):
                    bits=(rng.random(X)<prob).astype(int)
                    if bits.sum()==n:break
                else:raise RuntimeError('conditional Bernoulli did not hit size')
            A=(np.flatnonzero(bits)+1).tolist();forced=False
            if A[-1]!=X:
                # Single-element repair pins the true endpoint at the prescribed box.
                A.pop(0);A.append(X);forced=True
            assert len(A)==n and len(set(A))==n and max(A)==X
            name=f'profile_B{B}_{mode}_n{n}';sets[name]=A
            construction.append(dict(name=name,n=n,X=X,attempts=tries,forced_endpoint=forced,
                                     probability_rescale=n/(X*d)))
            checks.append(check(A,name))
            OUT.joinpath('realized_sets.json').write_text(json.dumps(sets))
            OUT.joinpath('realized_checks.json').write_text(json.dumps(checks,indent=2))
            OUT.joinpath('realized_construction.json').write_text(json.dumps(construction,indent=2))
    return checks

if __name__=='__main__':
    mode=sys.argv[1];B=int(sys.argv[2])
    if mode=='certify':certify(B)
    elif mode=='realize':realize(B)
