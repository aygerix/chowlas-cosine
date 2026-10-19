"""Exact strictness witness: p,e PD and all windows, but residual covariance not CP."""
import json,sys
from fractions import Fraction as F
from pathlib import Path
from math import comb
from flint import arb,ctx
ctx.prec=160
OUT=Path('.research/agents/tdense9_scratch')
sys.path.insert(0,str(OUT.resolve()))
from exact_witness import sqrtbounds,window_cert
sys.path.insert(0,str(Path('.research/agents/tdense8_scratch').resolve()))
from potential import compose

def run():
    eps=F(1,1000);ss=F(1,2);r=F(3849,5000)
    edges=[F(0),eps,ss-eps,ss,ss+eps,F(1)]
    qp=[[F(1),-1/eps],[F(0)],[-(ss-eps)/(2*eps),1/(2*eps)],[(ss+eps)/(2*eps),-1/(2*eps)],[F(0)]]
    dl=du=F(0)
    for v,l,u in zip(qp,edges[:-1],edges[1:]):
        a=sum(c*l**i for i,c in enumerate(v));b=sum(c*u**i for i,c in enumerate(v))
        uu=1-a;vv=1-b
        if uu==vv:L,U=sqrtbounds(uu)
        else:
            al,au=sqrtbounds(uu);bl,bu=sqrtbounds(vv);cl,cu=sqrtbounds(uu*vv)
            L=F(2,3)*(uu+cl+vv)/(au+bu);U=F(2,3)*(uu+cu+vv)/(al+bl)
        dl+=(u-l)*(1-U)/2;du+=(u-l)*(1-L)/2
    dupper=F((du*10**16).__ceil__(),10**16)
    b=eps/4
    energy=window_cert([[c/4 for c in v] for v in qp],edges,b,r)
    checks=[]
    for N in (8,12,16,24):
        coeff=[F(0)]+[F(comb(2*k-2,k-1),k*4**k) for k in range(1,N+1)]
        density=window_cert([compose(coeff,v) for v in qp],edges,dupper,r)
        checks.append(dict(N=N,ok=density['ok']))
        if density['ok']:break
    pi=arb.pi();ee=arb(1)/1000;st=arb(1)/2;h=4*pi/5
    def E(y):
        z=ee*y/2
        si=arb(1) if y==0 else z.sin()/z
        return ee*si*si*(1+(st*y).cos())
    horn=arb(0)
    for i in range(5):
        for j in range(5):
            sign=1 if i==j or (i-j)%5 not in (1,4) else -1
            horn+=sign*E((i-j)*h)
    assert horn<0
    out=dict(status='PROVED' if energy['ok'] and density['ok'] else 'UNRESOLVED',eps=str(eps),s=str(ss),r=str(r),q_polynomials=[[str(c) for c in v] for v in qp],edges=list(map(str,edges)),density_lower=str(dl),density_upper=str(du),density_float=float((dl+du)/2),energy=energy,density=density,N=N,horn_ball=str(horn),horn_negative=bool(horn<0),precision=ctx.prec,series_checks=checks)
    OUT.joinpath('cp_obstruction.json').write_text(json.dumps(out,indent=2))
    print('CP_WITNESS',json.dumps({k:v for k,v in out.items() if k not in ('energy','density','density_lower','density_upper')}),flush=True)
    assert out['status']=='PROVED'
if __name__=='__main__':run()
