"""VM-only independent all-set checks, exact lower certificates, numerical minima."""
import sys,json,math,hashlib,platform
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.optimize import minimize_scalar
OUT=Path('.research/agents/tdense7_scratch')

def minimum(A):
    aa=np.array(A,float);X=max(A);G=1<<math.ceil(math.log2(128*X))
    c=np.zeros(G);c[A]=1;v=np.fft.rfft(c).real
    inds=np.flatnonzero((v[1:-1]<=v[:-2])&(v[1:-1]<=v[2:]))+1
    inds=inds[np.argsort(v[inds])[:24]]
    best=(float(v.min()),2*math.pi*int(v.argmin())/G)
    for j in inds:
        res=minimize_scalar(lambda x:float(np.cos(aa*x).sum()),bounds=(2*math.pi*(j-1)/G,2*math.pi*(j+1)/G),
                            method='bounded',options={'xatol':1e-16})
        if res.fun<best[0]:best=(float(res.fun),float(res.x))
    # Independent direct evaluation at refined angle and exact endpoints.
    direct=float(np.cos(aa*best[1]).sum())
    return dict(M_estimate=-min(best[0],direct),angle=best[1],FFT_M=-float(v.min()),G=G,
                direct_difference=abs(best[0]-direct),certificate='NUMERICAL, not whole-circle certified')

def family(A):
    X=max(A);n=len(A)
    hs=sorted(set([0]+[int(round(2**(j/3))) for j in range(0,int(3*math.log2(max(2,X//2)))+1)]))
    ws=np.unique(np.maximum(1,np.round(X*np.r_[np.geomspace(1/X,1,70),np.linspace(.01,1,60)]).astype(int)))
    bests={k:dict(bound=0) for k in ('elem','beckner','numerical_rho')}
    NN=1<<math.ceil(math.log2(2*(X+max(hs))+4))
    a=np.zeros(NN);a[A]=1;a[(-np.array(A))%NN]=1;fa=np.fft.fft(a)
    for h in hs:
        if h:
            kk=np.arange(-h,h+1);ker=np.zeros(NN);ker[kk%NN]=(h+1-abs(kk))/(h+1)**2
            rr=a-np.fft.ifft(fa*np.fft.fft(ker)).real
        else:rr=a
        rp=rr[1:X+h+1];jj=np.arange(1,len(rp)+1,dtype=float);vv=rp*rp
        pp=[np.r_[0,np.cumsum(vv*jj**i)] for i in range(3)]
        E=float(sum(vv));S=pp[0][ws]-2*pp[1][ws]/(ws+1)+pp[2][ws]/(ws+1)**2
        W=2*(ws+1)/3+1/(3*(ws+1));L=X+h+ws
        for kind in bests:
            C=(.811*(L+1)+.2367 if kind=='elem' else
               4/(3*math.sqrt(3))*(1+2/np.sqrt(L+1))**3*(L+1) if kind=='beckner' else .687*(L+1))
            bb=np.sqrt(np.maximum(0,(W*E-C*S)/(2*(C-W))))+abs(rr[0])/2
            j=int(np.argmax(bb))
            if bb[j]>bests[kind]['bound']:
                bests[kind]=dict(bound=float(bb[j]),h=h,w=int(ws[j]),over_sqrtn=float(bb[j]/math.sqrt(n)))
    return bests

def exact_lower(A,h,w):
    X=max(A);d=h+1
    # Integer convolution checked independently of the FFT family.
    r=[0]*(X+h+1)
    for a in A:r[a]+=d*d
    if h:
        for a in A:
            for u in (a,-a):
                for j in range(max(0,u-h),u+h+1):r[j]-=d-abs(j-u)
    E=F(sum(v*v for v in r[1:]),d**4)
    S=F(sum((w+1-j)**2*r[j]**2 for j in range(1,min(w,len(r)-1)+1)),d**4*(w+1)**2)
    W=F(2*(w+1),3)+F(1,3*(w+1));C=F(811,1000)*(X+h+w+1)+F(2367,10000)
    z=max(F(0),(W*E-C*S)/(2*(C-W)))
    scale=10**8;v=math.isqrt(z.numerator*scale*scale//z.denominator)
    root=F(v,scale)
    assert root*root<=z
    lb=root-F(r[0],2*d*d)
    return dict(h=h,w=w,lower=str(lb),lower_float=float(lb),bound_over_sqrtn=float(lb)/math.sqrt(len(A)),
                square_radicand=str(z),status='PROVED exact rational P31/P47 lower bound, not a minimum certificate')

def p29(A):
    X=max(A);n=len(A);counts=np.zeros(X+1);sums=np.zeros(X+1)
    counts[A]=1;sums[A]=A;counts=np.cumsum(counts);sums=np.cumsum(sums)
    hs=np.arange(1,X+1,dtype=float);ss=counts[:-1]-sums[:-1]/hs
    bb=(hs*n-(X+hs)*ss)/X;j=int(np.argmax(bb))
    return dict(bound=float(bb[j]),h=j+1,over_sqrtn=float(bb[j]/math.sqrt(n)))

def check(A,name):
    assert len(A)==len(set(A)) and min(A)>0;A=sorted(A);n=len(A);X=max(A)
    mm=minimum(A);ff=family(A);ef=ff['elem'];ex=exact_lower(A,ef['h'],ef['w'])
    # Prefix P29 plus the rigorous removal inequality M(A)>=M(front)-|tail|.
    cuts=sorted(set([int(n*x) for x in [.1,.2,.3,.4,.5,.6,.7,.8,.9,.95,1]]))
    corebest=dict(bound=0)
    for cut in cuts:
        if cut<1:continue
        pp=p29(A[:cut]);val=pp['bound']-(n-cut)
        if val>corebest['bound']:corebest=dict(bound=val,cut=cut,Y=A[cut-1],tail=n-cut)
    # P36 on a bounded list of largest ratio gaps, with a certified core bound.
    gaps=sorted(range(1,n),key=lambda i:A[i]/A[i-1],reverse=True)[:4]
    gapbest=dict(bound=0)
    for cut in gaps:
        if cut<2:continue
        Y=A[cut-1];D=A[cut]-1
        cf=family(A[:cut])['elem'];lower=exact_lower(A[:cut],cf['h'],cf['w'])['lower_float']
        error=(math.pi**2/2)*sum(a*a for a in A[:cut])/(D+2)**2
        if lower-error>gapbest['bound']:gapbest=dict(bound=lower-error,cut=cut,Y=Y,D=D,error=error)
    rec=dict(name=name,n=n,X=X,C=X/n,R_estimate=mm['M_estimate']/math.sqrt(n),minimum=mm,
             family=ff,exact_elementary=ex,P29=p29(A),prefix_dip=corebest,P36=gapbest)
    print('SET_CHECK',json.dumps({k:v for k,v in rec.items() if k not in ('family','exact_elementary')}),flush=True)
    return rec

if __name__=='__main__':
    mode=sys.argv[1]
    if mode=='search':
        sets={}
        for n in (128,512):
            for i,line in enumerate(OUT.joinpath(f'adversarial_{n}.jsonl').read_text().splitlines()):
                rr=json.loads(line);sets[f'n{n}_mu{rr["mu"]}_row{i}']=rr['A']
        checks=[check(A,name) for name,A in sets.items()]
        OUT.joinpath('adversarial_checks.json').write_text(json.dumps(checks,indent=2))
        OUT.joinpath('adversarial_sets.json').write_text(json.dumps(sets,indent=2))
