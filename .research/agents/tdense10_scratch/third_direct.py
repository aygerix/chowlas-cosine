"""Direct arbitrary cubic-profile correction, VM only. Analytic/ball certificates
are separated from FFT evidence. Saves failed rounded binary candidates verbatim.
"""
import json,math
from pathlib import Path
import numpy as np
from flint import arb,ctx
OUT=Path('.research/agents/tdense10_scratch');SEED=2026101910

def fft(a):
    N=1<<int(math.ceil(math.log2(8*(len(a)+1))));c=np.zeros(N);c[1:len(a)+1]=a/2;c[-len(a):]=a[::-1]/2
    values=np.fft.ifft(c).real*N;j=int(np.argmin(values));return dict(min=float(values[j]),index=j,grid=N,angle=float(2*np.pi*j/N),status='NUMERICAL')

def row(X):
    k=np.arange(1,X+1);t=k/X;w=1-t;p=(1-np.sqrt(np.maximum(0,1-w*w)))/2;e=w*w/4;s=e*(1-2*p);v=np.cbrt(s)
    L=int(X**.8);B=L**(1/3);sel=k%L==0;z=np.zeros(X);z[sel]=B*v[sel]
    r=dict(X=X,L=L,B=B,nonzero=int(sel.sum()),first=float(np.mean(z)),second=float(np.mean(z*z)),third=float(np.mean(z**3)),third_target=math.pi/64,fourth=float(np.mean(z**4)),l1=float(np.sum(np.abs(z))),fft=fft(z))
    ctx.prec=180;A=arb(L)**(arb(1)/3);sumv=arb(0)
    for kk in k[sel]:
        ww=1-arb(int(kk))/X;ss=ww*ww*(1-ww*ww).sqrt()/4
        sumv+=ss**(arb(1)/3) if ss else arb(0)
    l1=A*sumv;r['l1_ball']=str(l1);r['global_certificate']='For all real x, Z(x)>=-L^(1/3)*sum_n cbrt(s(nL/X)); exact triangle inequality.'
    return r,(p,e,s,z)

def point_certificate(A,ff,tag):
    ctx.prec=180;x=2*arb.pi()*ff['index']/ff['grid'];val=sum(((int(k)*x).cos() for k in A),arb(0))
    n=len(A);R_lower=math.floor((-ff['min']/math.sqrt(n)-.000001)*1000)/1000
    numerator=int(round(R_lower*1000));assert val<-(arb(n).sqrt()*numerator/1000)
    path=OUT/f'rounded_{tag}.txt';path.write_text('\n'.join(str(int(k)) for k in A)+'\n')
    return dict(status='PROVED_POINT_DIP',A_file=path.name,n=n,X=int(A[-1]),angle_exact=f'2*pi*{ff["index"]}/{ff["grid"]}',value_ball=str(val),R_strict_lower=f'{numerator}/1000',scope='Rigorous lower bound on M/sqrt(n), not a global minimum enclosure.')

def main():
    rows=[];demo=None
    for X in (4096,65536,1048576):
        rr,arr=row(X);rows.append(rr);print(json.dumps(rr),flush=True)
        if X==65536:demo=arr
    X=65536;p,e,s,z=demo;k=np.arange(1,X+1);w=1-k/X;rng=np.random.default_rng(SEED);J=int(X**.9);N=1<<int(math.ceil(math.log2(64*X)))
    counts=np.bincount(rng.integers(0,N,J),minlength=N);r=4/np.sqrt(32*J)*w*np.fft.fft(counts).real[1:X+1];base=p+r
    demos=[]
    for name,a in [('base',base),('direct_cubic',base+z)]:
        ff=fft(a);b=(a>=.5).astype(float);A=np.flatnonzero(b)+1;bf=fft(b)
        d=dict(name=name,X=X,J=J,first=float(np.mean(a)),second=float(np.mean(a*a)),third=float(np.mean(a**3)),fourth=float(np.mean(a**4)),raw_target=float(np.mean(p)),residual_cube=float(np.mean((a-p)**3)),residual_cube_target=float(np.mean(s)),fraction_outside_0_1=float(np.mean((a<0)|(a>1))),fft=ff,ideal_global_bound_formula='-sqrt(J/8)-1/4' + ('-sum_abs_z' if name=='direct_cubic' else ''),rounding_energy=float(np.mean((a-b)**2)),rounded_fft=bf,rounded_R=-bf['min']/math.sqrt(len(A)),point_certificate=point_certificate(A,bf,name))
        # Rigorous all-circle lower bound for the exact ideal weighted polynomial.
        bound=-(arb(J)/8).sqrt()-arb(1)/4
        if name=='direct_cubic':bound-=arb(rows[1]['l1_ball'])
        d['ideal_global_lower_ball']=str(bound);demos.append(d);print(json.dumps(d),flush=True)
    OUT.joinpath('third_direct.json').write_text(json.dumps(dict(seed=SEED,gadgets=rows,demos=demos),indent=2))
if __name__=='__main__':main()
