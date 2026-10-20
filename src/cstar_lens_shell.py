"""Exact Boolean radial-profile realization and mesoscopic certificates.

Rational Halton centers assign symmetric lens windows to dyadic u-shells.
Membership uses only integer comparisons. All computation on Dirichlet.
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
from scipy.optimize import minimize


def inverse_digits(k,base):
    result=F(0);denominator=base
    while k:
        k,r=divmod(k,base);result+=F(r,denominator);denominator*=base
    return result


def center(k):
    x=2*inverse_digits(k,2)-1;y=2*inverse_digits(k,3)-1
    q=math.lcm(x.denominator,y.denominator)
    return (int(x*q),int(y*q),q)


def in_lens(X,d,w1,w2,T):
    a,b,q=T;Z=X*X*(q*q-a*a-b*b)-d*(w1*w1+w2*w2)*q*q
    return Z>=0 and Z*Z>=4*X*X*q*q*d*(a*w1+b*w2)**2


def generate(L):
    X=2**L;k0=(L+3)//4;k1=3*L//4-1
    centers={k:center(k) for k in range(k0,k1+1)}
    pairs=[];shells=Counter();bound=2**(k1+1)
    for u1 in range(bound+1):
        for u2 in range(-bound,bound+1):
            if u1==0 and u2<=0:continue
            d=u1*u1+u2*u2
            if not d or math.gcd(u1,abs(u2))!=1:continue
            k=(d.bit_length()-1)//2
            if k not in centers:continue
            a,b,q=centers[k]
            if a*a+b*b>=q*q:continue
            radius=math.isqrt(X*X//d)
            for w1 in range(radius+1):
                for w2 in range(-radius,radius+1):
                    if w1==0 and w2<=0:continue
                    if not (w1 or w2):continue
                    if in_lens(X,d,w1,w2,centers[k]):
                        assert d*(w1*w1+w2*w2)<=X*X
                        pairs.append((u1,u2,w1,w2));shells[k]+=1
    return pairs,centers,shells


def fejer(X,C,pairs,centers):
    candidates=[k for k,(a,b,q) in centers.items() if 9*(a*a+b*b)<=4*q*q]
    assert candidates
    k=min(candidates);u=(2**k,1);d=u[0]**2+1;R=flint.arb(X)/flint.arb(d).sqrt()
    a,b,q=centers[k];t=flint.arb(a*a+b*b).sqrt()/q
    perpendicular=2*flint.arb.pi()/(1-t*t).sqrt()
    if a or b:
        norm=flint.arb(a*a+b*b).sqrt()
        alpha=[-perpendicular*b/norm/R,perpendicular*a/norm/R]
    else:alpha=[flint.arb(0),2*flint.arb.pi()/R]
    m=math.isqrt((1024*X)**2//d)+1
    h=[6*X**3+i for i in [1,3,5,7]]
    assert (min(h)-X)**2>2*m*m*d
    selected=[(c,e) for a0,b0,c,e in pairs if (a0,b0)==u]
    assert selected
    H=2*sum(((m+1-abs(c))*(m+1-abs(e))*(alpha[0]*c+alpha[1]*e).cos()
             for c,e in selected),flint.arb(0))/(m+1)**2
    assert H<0
    lower=F(max(0,math.floor(float((-H/2).mid())*10**6)-1),10**6)
    assert H+2*flint.arb(lower.numerator)/lower.denominator<0
    return dict(shell=k,u=list(u),center=list(centers[k]),fiber_pairs=len(selected),
                m=m,mean='1',aliases='0',H_ball=str(H),M_lower_rational=str(lower),
                isolation_squared_margin=(min(h)-X)**2-2*m*m*d,verified=True)


def point(X,C,h,P,matrices,rng):
    arr=np.array(matrices,dtype=np.float64);n=len(arr)
    phases=[]
    for scale in [4,8,16,32,64,128,256,512]:
        if scale>4*X:continue
        for j in range(16):
            c=math.cos(2*math.pi*j/16);s=math.sin(2*math.pi*j/16)
            phases.append(np.array([c,-s,s,c])*scale/X)
    phases.extend(rng.uniform(-math.pi,math.pi,size=(192,4)))
    phases=np.array(phases);scores=[]
    for chunk in np.array_split(phases,math.ceil(len(phases)/32)):
        scores.extend(np.cos(arr@chunk.T).mean(axis=0))
    def objective(v):
        theta=arr@v
        return float(np.cos(theta).mean()),-(np.sin(theta)@arr)/n
    starts=np.argsort(scores)[:3];best=(math.inf,None)
    for index in starts:
        result=minimize(objective,phases[index],jac=True,method='L-BFGS-B',
                        options={'maxiter':70,'ftol':1e-12})
        if result.fun<best[0]:best=(result.fun,result.x)
    phi=(best[1]+np.pi)%(2*np.pi)-np.pi
    residues=[round(float(y)*modulus/(2*math.pi)) for y,modulus in zip(phi,h)]
    j=sum(z*(P//modulus)*pow(P//modulus,-1,modulus) for z,modulus in zip(residues,h))%P
    counts=Counter()
    for M in matrices:
        r=j*sum(c*z for c,z in zip(C,M))%P;counts[min(r,P-r)]+=1
    value=sum((count*flint.arb.cos_pi_fmpq(flint.fmpq(2*r,P))
               for r,count in counts.items()),flint.arb(0))
    upper=F(math.ceil(float(value.mid())/n*10**7)+1,10**7)
    assert value<flint.arb(upper.numerator)*n/upper.denominator and upper<0
    return dict(j=j,q=P,residues=residues,f_over_n_upper_rational=str(upper),
                M_lower_rational=str(-n*upper),R_lower_float=float(-n*upper)/math.sqrt(n),
                certificate='128-bit Arb point LOWER bound for M; not a global minimum',verified=True)


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Run through src/dirun.sh')
    flint.ctx.prec=128;rng=np.random.default_rng(20261025)
    root=Path('.research/experiments/radial_boolean_2026-10-20');root.mkdir(parents=True,exist_ok=True)
    out=dict(qualification='Genuine Boolean profile realization and finite lower witnesses; '
             'no counterexample or global upper bound.',seed=20261025,cases=[])
    for L in [6,7,8]:
        X=2**L;pairs,centers,shells=generate(L)
        h=[6*X**3+i for i in [1,3,5,7]];P=math.prod(h);C=[P//z for z in h]
        assert all(math.gcd(a,b)==1 for i,a in enumerate(h) for b in h[i+1:])
        matrices=[(a*c,a*d,b*c,b*d) for a,b,c,d in pairs]
        A=sorted(abs(sum(c*z for c,z in zip(C,M))) for M in matrices)
        assert A and A[0]>0 and len(set(A))==len(A)
        certificate=fejer(X,C,pairs,centers)
        row=dict(L=L,X=X,n=len(A),C=C,moduli=h,
                 centers={str(k):list(z) for k,z in centers.items()},shell_counts=dict(shells),
                 encoded_set_sha256=hashlib.sha256((' '.join(map(str,A))).encode()).hexdigest(),
                 max_A=A[-1],fejer=certificate,
                 point=point(X,C,h,P,matrices,rng),
                 count_over_asymptotic_float=len(A)/((3*math.pi/32)*X*X*math.log(X)),verified=True)
        row['fejer']['R_lower_float']=float(F(certificate['M_lower_rational']))/math.sqrt(len(A))
        out['cases'].append(row);(root/'lens.json').write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps({z:row[z] for z in ['L','X','n','shell_counts','fejer','point']}),flush=True)


if __name__=='__main__':main()
