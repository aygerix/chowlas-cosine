"""Independent checks of the corrected round-17 derivations. VM ONLY."""
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
import sys

import flint
import numpy as np
from scipy.linalg import eigvalsh

sys.path.insert(0,'src')
sys.path.insert(0,'.research/agents/tdense17_scratch')
from chowla import certify_lower_bound
from fourway import metrics

ROOT=Path('.research/agents/tdense17_scratch')


def main():
    count=0
    max_bulk_slack=-1e100
    for bits in range(1,1<<9):
        A=[a for a in range(1,10) if bits>>(a-1)&1]
        aset=set(A); n=len(A); S=A+[-a for a in A]
        e=sum(b-a in aset for i,a in enumerate(A) for b in A[i+1:])
        ordered_sums=sum(a+b in aset for a in A for b in A)
        TS=sum(s-t in set(S) for s in S for t in S)
        assert ordered_sums==e and TS==6*e
        H=np.array([[int(abs(a-b) in aset) for b in A] for a in A])
        assert int(np.trace(H@H))==2*e
        w=eigvalsh(H.astype(float)); K=max(0.,-float(w[0]))
        for gamma in (.125,.5,1.,2.):
            tau=gamma*math.sqrt(n)
            beta=float(np.sum(w[np.abs(w)<=tau]**2))
            rhs=n*K*max(tau,K)
            assert beta<=rhs+1e-7
            max_bulk_slack=max(max_bulk_slack,beta-rhs)
        # Exact coefficient form of the L=2,h=1 identity, independent of theta.
        assert all(1-2*int(a%2==0)==-(-1)**a for a in A)
        count+=1
    # Exact sparse-triangle/window identity, not a quadrature experiment.
    triangle=[]
    for H in range(1,65):
        alpha=Fraction(1,7)
        X=2*H
        ps=[2*alpha*(1-Fraction(a,X)) for a in range(1,X+1)]
        ws=[1-Fraction(abs(a-H),H) for a in range(1,X+1)]
        S=sum(p*w*w for p,w in zip(ps,ws))
        mu=sum(ps); v=sum(p*(1-p)*w*w for p,w in zip(ps,ws))
        assert S==alpha*Fraction(2*H*H+1,3*H)
        assert S>=mu/3 and v>=mu/6
        if H in (1,4,16,64): triangle.append(dict(H=H,mu=str(mu),v=str(v),weighted_energy=str(S)))
    # Arb checks of the actual smoothed witness; the proof is analytic.
    flint.ctx.prec=120
    boundary=[]
    rng=np.random.default_rng(171703)
    for k in (1,2,4,16,64):
        for d in (1,3):
            A=set(range(d, d*k+1,d))
            A|=set(map(int,rng.integers(1,20*d*k+1,size=2*k)))
            Ad={a//d for a in A if a%d==0}
            D=Fraction(sum(b not in Ad for b in range(1,k+1)))
            D+=sum((1-Fraction(b,4*k) for b in Ad if k<b<4*k),Fraction())
            x=3*flint.arb.pi()/(2*k+1)
            g=sum((flint.arb(4*k-b)/(4*k)*(b*x).cos() for b in Ad if b<4*k),flint.arb(0))
            bound=flint.arb(D.numerator)/D.denominator-flint.arb(23*k)/264
            assert g<bound
            boundary.append(dict(k=k,d=d,defect=str(D),g=str(g),upper=str(bound)))
    # Re-certify the existing tight finite CLIQUE-S instance from the saved A.
    A=np.load(ROOT/'spline_L4096_s17_p5_6.npz')['A'].tolist()
    aset=set(A)
    assert all(a in aset for a in range(1,1025))
    cert=certify_lower_bound(A,oversample=16,prec=120)
    assert -cert.lower_bound<77
    finite=dict(n=len(A),X=max(A),M_upper=-cert.lower_bound,
        clique_global=1025,clique_in_S=1024,
        global_ratio_lower=1025/(-2*cert.lower_bound),
        in_S_ratio_lower=1024/(-2*cert.lower_bound),grid=cert.L,
        sha256_A=hashlib.sha256(np.array(A,dtype='<i8').tobytes()).hexdigest())
    print(json.dumps(dict(finite_clique=finite)),flush=True)
    # Exact rational ambient defects of saved smooth-profile instances.
    smooth=[]
    for L,k in ((4096,1024),(262144,32768)):
        A=np.load(ROOT/f'spline_L{L}_s17_p5_6.npz')['A']
        aset=set(A.tolist())
        assert all(a in aset for a in range(1,k+1))
        numer=sum(4*k-int(a) for a in A if k<a<4*k)
        D=Fraction(numer,4*k)
        smooth.append(dict(L=L,k=k,defect=str(D),defect_over_k=float(D/k)))
    # Finite check of the convex variance lemma: enumerate all selector vectors.
    p=np.array([.09,.23,.37,.51,.65,.79,.93])
    w=np.array([.25,.5,.75,1.,.75,.5,.25])
    vals=[]; probs=[]; G=8192
    for bits in range(1<<7):
        x=np.array([bits>>j&1 for j in range(7)])
        prob=float(np.prod(np.where(x,p,1-p)))
        c=np.zeros(G); c[np.arange(1,8)]=w*x
        vals.append(float(np.abs(np.fft.fft(c)).mean()/2)); probs.append(prob)
    vals=np.array(vals); probs=np.array(probs)
    mean=float(probs@vals); var=float(probs@((vals-mean)**2))
    v=float(np.sum(p*(1-p)*w*w)); b=v/(2*math.sqrt(6*v+1))
    assert mean>=b and var<=.25
    enum=dict(variables=7,subsets=128,G=G,mean=mean,var=var,v=v,mean_lower=b)
    # Monte Carlo assesses scale, not the proof of probability one minus O(1/n).
    mc=[]
    rng=np.random.default_rng(171704)
    for X in (1024,4096,16384):
        alpha=X**(-.25); a=np.arange(1,X+1); H=X//2
        p=2*alpha*(1-a/X); w=np.maximum(1-np.abs(a-H)/H,0)
        G=8*X; samples=[]; sizes=[]
        for _ in range(128):
            keep=rng.random(X)<p; c=np.zeros(G); c[a]=w*keep
            samples.append(float(np.abs(np.fft.fft(c)).mean()/2)); sizes.append(int(keep.sum()))
        v=float(np.sum(p*(1-p)*w*w)); mu=float(p.sum())
        mc.append(dict(X=X,alpha=alpha,mu=mu,v=v,trials=128,
            B_mean=float(np.mean(samples)),B_var=float(np.var(samples,ddof=1)),
            B_min_over_sqrtn=float(np.min(np.array(samples)/np.sqrt(sizes))),
            mean_lower=v/(2*math.sqrt(6*v+1))))
    result=dict(exact_star_cases=count,bulk_numerical_cases=4*count,
        max_bulk_slack=max_bulk_slack,triangle_exact_checks=64,triangle_examples=triangle,
        boundary_arb=boundary,finite_clique=finite,smooth_defects=smooth,
        variance_enumeration=enum,rounding_MC=mc,flint_version=flint.__version__)
    (ROOT/'fourway_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)


if __name__=='__main__':main()
