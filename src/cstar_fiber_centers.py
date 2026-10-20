"""Independent whole-fiber centers after removing all large fibers.

All computation on Dirichlet. Statistical diagnostics are numerical;
saved negative point certificates use Arb at exact CRT roots.
"""
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import socket
import flint
import numpy as np
from scipy.special import jn_zeros


def disk_certificate():
    def partial(t,n):
        return sum((F((-1)**k,math.factorial(k)*math.factorial(k+1))*(t*t/4)**k
                    for k in range(n+1)),F(0))
    left,right=F(19,5),F(39,10)
    assert partial(left,21)>0 and partial(right,20)<0
    # A lower alternating partial sum is >1/100 at every doubled root.
    lo,hi=F(361,25),F(1521,100);n=21
    coefficients=[F((-1)**k,math.factorial(k)*math.factorial(k+1)) for k in range(n+1)]
    coefficients[0]-=F(1,100)
    powers=[sum((coefficients[k]*math.comb(k,j)*lo**(k-j)*(hi-lo)**j
                 for k in range(j,n+1)),F(0)) for j in range(n+1)]
    controls=[sum((powers[j]*F(math.comb(i,j),math.comb(n,j))
                   for j in range(i+1)),F(0)) for i in range(n+1)]
    assert min(controls)>0 and hi<22*23
    return dict(root_interval=[str(left),str(right)],left_lower=str(partial(left,21)),
                right_upper=str(partial(right,20)),doubled_root_disk_lower='1/100',
                bernstein_minimum=str(min(controls)),bernstein_interval=list(map(str,[lo,hi])),
                lower_order=n,verified=True)


def geometry(X):
    bound=math.isqrt(math.isqrt(math.isqrt(X**5)))
    cache={};fibers=[]
    for u1 in range(bound+1):
        for u2 in range(-bound,bound+1):
            if u1==0 and u2<=0:continue
            d=u1*u1+u2*u2
            if d<X or d**4>X**5 or math.gcd(u1,abs(u2))!=1:continue
            q=X*X//d
            if q not in cache:
                r=math.isqrt(q)
                B=np.array([(a,b) for a in range(-r,r+1) for b in range(-r,r+1)
                            if a*a+b*b<=q],dtype=np.int64)
                W=np.array([(a,b) for a,b in B if a>0 or (a==0 and b>0)],dtype=np.int64)
                plus=B[:,None,:]+W[None,:,:];minus=B[:,None,:]-W[None,:,:]
                incidence=((plus*plus).sum(axis=2)<=q)&((minus*minus).sum(axis=2)<=q)
                cache[q]=dict(B=B,W=W,incidence=incidence,
                              n=incidence.sum(axis=1).astype(np.int64))
            fibers.append(dict(u=(u1,u2),d=d,q=q,**cache[q]))
    return fibers


def encoding(X):
    h=[6*X**3+i for i in [1,3,5,7]];P=math.prod(h);C=[P//a for a in h]
    assert all(math.gcd(a,b)==1 for i,a in enumerate(h) for b in h[i+1:])
    return h,P,C


def residues_for_phase(phase,h):
    return [round(float(x)*m/(2*math.pi)) for x,m in zip(phase,h)]


def crt(residues,h):
    P=math.prod(h)
    return sum(z*(P//m)*pow(P//m,-1,m) for z,m in zip(residues,h))%P


def matrices_for_choices(fibers,choices):
    matrices=[]
    for fiber,index in zip(fibers,choices):
        a,b=fiber['u']
        for r,s in fiber['W'][fiber['incidence'][index]]:
            matrices.append((a*int(r),a*int(s),b*int(r),b*int(s)))
    return matrices


def point_certificate(matrices,h,C,residues):
    P=math.prod(h);j=crt(residues,h);n=len(matrices);counts=Counter()
    A=sorted(abs(sum(c*z for c,z in zip(C,M))) for M in matrices)
    assert n and A[0]>0 and len(set(A))==n
    for a in A:
        r=j*a%P;counts[min(r,P-r)]+=1
    value=sum((count*flint.arb.cos_pi_fmpq(flint.fmpq(2*r,P))
               for r,count in counts.items()),flint.arb(0))
    upper=F(math.ceil(float(value.mid())/n*10**8)+1,10**8)
    assert value<flint.arb(upper.numerator)*n/upper.denominator
    return dict(j=j,q=P,residues=list(map(int,residues)),n=n,max_A=A[-1],
                f_over_n_upper_rational=str(upper),M_lower_rational=str(max(F(0),-n*upper)),
                R_lower_float=float(max(F(0),-n*upper))/math.sqrt(n),
                encoded_set_sha256=hashlib.sha256((' '.join(map(str,A))).encode()).hexdigest(),
                qualification='Arb exact-root LOWER bound for M, not a global minimum',verified=True)


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Run through src/dirun.sh')
    flint.ctx.prec=128;rng=np.random.default_rng(20261026)
    alpha=float(jn_zeros(1,1)[0]);tau=2*alpha
    assert 3.8<alpha<3.9
    out=dict(qualification='Numerical finite distribution diagnostics; exact set and Arb point certificates. '
             'No universal or deterministic exclusion of correlated centers.',seed=20261026,
             disk_sign=disk_certificate(),alpha_float=alpha,cases=[])
    for X in [64,128,256]:
        fibers=geometry(X);h,P,C=encoding(X)
        residues=residues_for_phase([tau/X,0,0,tau/X],h)
        phase=2*np.pi*np.array(residues,dtype=float)/np.array(h,dtype=float)
        mean=0.;variance=0.;third=0.;mean_n=0.;variance_n=0.;parity_error=0.
        for fiber in fibers:
            a,b=fiber['u'];q=np.array([phase[0]*a,phase[3]*b])
            cosine=np.cos(fiber['W']@q)
            scores=2*(fiber['incidence']@cosine)
            fiber['scores']=scores
            avg=float(scores.mean());centered=scores-avg
            mean+=avg;variance+=float((centered**2).mean());third+=float((abs(centered)**3).mean())
            mean_n+=float(fiber['n'].mean());variance_n+=float(fiber['n'].var())
            parity=0.
            for r in range(2):
                for s in range(2):
                    B=fiber['B'];subset=B[(B[:,0]%2==r)&(B[:,1]%2==s)]
                    parity+=abs(np.exp(.5j*(subset@q)).sum())**2/len(B)
            parity_error=max(parity_error,abs(avg-(parity-1)))
        assert parity_error<1e-8
        samples=[];best=(math.inf,None)
        for trial in range(96):
            choices=[int(rng.integers(len(f['B']))) for f in fibers]
            n=sum(int(f['n'][i]) for f,i in zip(fibers,choices))
            D=sum(float(f['scores'][i]) for f,i in zip(fibers,choices))
            samples.append(dict(n=n,D=D))
            if D<best[0]:best=(D,choices)
        matrices=matrices_for_choices(fibers,best[1]);certificate=point_certificate(matrices,h,C,residues)
        assert F(certificate['M_lower_rational'])>0
        row=dict(X=X,fibers=len(fibers),min_direction_squared=min(f['d'] for f in fibers),
                 max_direction_squared=max(f['d'] for f in fibers),
                 expected_n=mean_n,variance_n=variance_n,
                 expected_n_over_asymptotic=mean_n/((3/32)*X*X*math.log(X)),
                 mean_D=mean,variance_D=variance,variance_D_over_X3=variance/X**3,
                 lyapunov_third_ratio=third/variance**1.5,parity_identity_max_float_error=parity_error,
                 empirical_negative_point_count=sum(s['D']<0 for s in samples),samples=samples,
                 best_choices=best[1],point=certificate,verified=True)
        out['cases'].append(row)
        print(json.dumps({k:row[k] for k in ['X','fibers','expected_n','mean_D','variance_D_over_X3',
                                            'lyapunov_third_ratio','empirical_negative_point_count','point']}),flush=True)
    root=Path('.research/experiments/fiber_centers_2026-10-20');root.mkdir(parents=True,exist_ok=True)
    (root/'independent.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
