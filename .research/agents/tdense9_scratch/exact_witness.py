"""VM exact PD and all-scale window witness. q=PWL, e=q/4, p=F(q)/2.
Rational coefficients, Sturm for q symbol, rational Bernstein for every theta.
"""
import os
os.environ['SYMPY_GROUND_TYPES']='flint'
import sys,json,math,time
from pathlib import Path
from fractions import Fraction as F
from math import comb,isqrt
import sympy as sp
OUT=Path('.research/agents/tdense9_scratch')
sys.path.insert(0,str(Path('.research/agents/tdense8_scratch').resolve()))
from potential import add,mul,compose,certify,peval

def sqrtbounds(x,bits=100):
    D=1<<bits;v=isqrt(x.numerator*D*D//x.denominator)
    lo=F(v,D);hi=lo if lo*lo==x else F(v+1,D)
    return lo,hi

def density_bounds(q,phi):
    lo=F(0);hi=F(0);B=len(q)-1
    for a,b in zip(q[:-1],q[1:]):
        # Mean sqrt(1-q) = 2/3*(u+sqrt(uv)+v)/(sqrt(u)+sqrt(v)).
        u=1-a;v=1-b
        if u==v:L=U=sqrtbounds(u)[0] if u==0 else None
        if u==v:
            L,U=sqrtbounds(u)
        else:
            al,au=sqrtbounds(u);bl,bu=sqrtbounds(v);cl,cu=sqrtbounds(u*v)
            L=F(2,3)*(u+cl+v)/(au+bu);U=F(2,3)*(u+cu+v)/(al+bl)
        lo+=(1-U)/2;hi+=(1-L)/2
        # Keep directed rational bounds, without multiplying unrelated denominators.
        D=1<<100
        lo=F((lo*D).__floor__(),D);hi=F((hi*D).__ceil__(),D)
    return phi*lo/B,phi*hi/B

def window_cert(polys,edges,total,r):
    prev=[F(0)]*3;checks=[]
    for i,v in enumerate(polys):
        lo=edges[i];hi=edges[i+1];J=[F(0)]*(len(v)+3)
        J[0]=prev[2];J[1]=-2*prev[1];J[2]=prev[0]
        for k,c in enumerate(v):
            J[k+3]+=2*c/F((k+1)*(k+2)*(k+3))
            J[2]-=c*lo**(k+1)/F(k+1);J[1]+=2*c*lo**(k+2)/F(k+2);J[0]-=c*lo**(k+3)/F(k+3)
        R=[F(0)]*(len(J)+1)
        for j,c in enumerate(J):R[j]+=r*c;R[j+1]+=r*c
        R[3]-=F(2,3)*total
        if lo==0:
            assert R[:3]==[0,0,0];R=R[3:]
        cc=certify(R,lo,hi);cc.update(cell=i);checks.append(cc)
        if not cc['ok']:return dict(ok=False,checks=checks)
        for ell in range(3):prev[ell]+=sum(c*(hi**(k+ell+1)-lo**(k+ell+1))/F(k+ell+1) for k,c in enumerate(v))
    # theta>=1, put u=1/theta. Inputs vanish beyond 1.
    A=mul([r,r],[prev[0],-2*prev[1],prev[2]]);A[0]-=F(2,3)*total
    cc=certify(A,F(0),F(1));cc['theta']='[1,infinity)';checks.append(cc)
    return dict(ok=all(c['ok'] for c in checks),checks=checks,moments=list(map(str,prev)))

def run(B=40,prefix='energy',method='sturm'):
    rec=json.loads(OUT.joinpath(f'{prefix}_B{B}_half_sine.json').read_text());raw=rec['q']
    gg=None
    if method=='factor':
        import numpy as np
        from scipy.signal import minimum_phase
        hh=np.r_[raw[:0:-1],raw]
        fac=minimum_phase(hh,method='homomorphic',n_fft=1<<20,half=True)
        gg=[round(float(v)*10**10) for v in fac]
        norm=sum(v*v for v in gg)
        q=[F(sum(gg[j]*gg[j+i] for j in range(B-i)),norm) for i in range(B)]+[F(0)]
    else:
        eps=F(1,10**6);q=[F(round(v*10**10),10**10)/(1+eps) for v in raw];q[0]=F(1);q.append(F(0))
    assert all(0<=v<=1 for v in q)
    # This adds eps to the unnormalized diagonal and then divides by 1+eps.
    t0=time.time()
    if method=='factor':
        roots=None;pdok=True;positive_at_one=sum(gg)!=0
    else:
        z=sp.Symbol('z');S=sp.Poly(1,z,domain=sp.QQ)
        for i in range(1,B):S+=sp.Poly(2*sp.Rational(q[i].numerator,q[i].denominator)*sp.chebyshevt(i,z),z,domain=sp.QQ)
        roots=int(S.count_roots(-1,1));pdok=roots==0 and S.eval(1)>0;positive_at_one=bool(S.eval(1)>0)
    r=F(7698,10000) # strictly below the actual Beckner r; stronger witness windows.
    Iq=(q[0]/2+sum(q[1:-1]))/B
    phi=min(F(1),r/(2*Iq))*F(99999,100000)
    # Quantize the support width downward for manageable rational cell endpoints.
    phi=F((phi.numerator*10**8)//phi.denominator,10**8)
    dl,du=density_bounds(q,phi);dupper=F(math.ceil(du*10**12),10**12)
    edges=[phi*F(i,B) for i in range(B+1)]+[F(1)]
    qpoly=[]
    for i in range(B):qpoly.append([q[i]-i*(q[i+1]-q[i]),B*(q[i+1]-q[i])/phi])
    qpoly.append([F(0)])
    epoly=[[v/4 for v in p] for p in qpoly]
    energy=window_cert(epoly,edges,phi*Iq/4,r)
    density=None
    for N in (8,12,16,24):
        # p=1/2*(1-sqrt(1-q)), truncated power series is a pointwise lower bound.
        coeff=[F(0)]+[F(comb(2*k-2,k-1),k*4**k) for k in range(1,N+1)]
        ppoly=[compose(coeff,p) for p in qpoly]
        density=window_cert(ppoly,edges,dupper,r)
        if density['ok']:break
    out=dict(status='PROVED' if pdok and energy['ok'] and density['ok'] else 'FAILED',B=B,q=list(map(str,q)),phi=str(phi),r=str(r),a='1/2',density_lower=str(dl),density_upper=str(du),density_upper_window=str(dupper),density_float=float((dl+du)/2),C_upper=float(1/dl),symbol_sturm_roots=roots,symbol_at_one_positive=positive_at_one,sturm_seconds=time.time()-t0,energy=energy,density=density,density_lower_series_N=N,method=method,factor_integers=gg)
    OUT.joinpath(f'witness_B{B}_{prefix}{"_factor" if method=="factor" else ""}.json').write_text(json.dumps(out,indent=2))
    print('WITNESS',json.dumps({k:v for k,v in out.items() if k not in ('q','energy','density','density_lower','density_upper','factor_integers')}),flush=True)
    assert out['status']=='PROVED'
if __name__=='__main__':run(int(sys.argv[1]) if len(sys.argv)>1 else 40,sys.argv[2] if len(sys.argv)>2 else 'energy',sys.argv[3] if len(sys.argv)>3 else 'sturm')
