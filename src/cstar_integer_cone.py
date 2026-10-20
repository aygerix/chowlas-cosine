"""Exact/ball tests for the integer rank-one quadric construction.

All computation must run on Dirichlet. A root-of-unity evaluation supplies
a rigorous LOWER bound on M; no grid minimum or numerical global upper is
asserted. The asymptotic exclusion requires the separate paper argument.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
import hashlib
import json
import math
from pathlib import Path
import socket
import time

import flint
import sympy as sp


def variance_identity():
    p=[F(1),F(2,3),F(1,2),F(1,5),F(0)]
    mu=sum(p);variance=sum(z*(1-z) for z in p)
    for eta in product([0,1],repeat=len(p)):
        n=sum(eta)
        Q=2*sum((bit-z)**2 for bit,z in zip(eta,p))
        coupling=2*sum(bit*(1-z) for bit,z in zip(eta,p))
        assert coupling==Q/2+variance+n-mu
    return dict(boolean_vectors_checked=2**len(p),verified=True)


def disk_sign():
    # The normalized Fourier transform of the unit disk at radius t is
    # sum_k (-1)^k (t^2/4)^k/[k!(k+1)!]. Its even partial sum is an upper
    # bound after its tail terms become decreasing.
    u=sp.symbols('u');order=20
    P=sum((-1)**k*u**k/sp.Integer(math.factorial(k)*math.factorial(k+1))
          for k in range(order+1))
    certificate=sp.Poly(P+sp.Rational(1,50),u)
    lo,hi=sp.Rational(4),sp.Rational(484,49)
    assert hi<(order+1)*(order+2)
    roots=certificate.count_roots(lo,hi)
    assert roots==0 and certificate.eval(lo)<0
    return dict(variable='u=t^2/4',t_interval=['4','44/7'],
                polynomial_order=order,coefficients_low_to_high=[str(P.expand().coeff(u,k)) for k in range(order+1)],
                sturm_root_count=int(roots),disk_transform_upper='-1/50',
                qualification='Exact Sturm certificate and alternating-series upper bound',verified=True)


def cone_pairs(X):
    # u is primitive with positive first nonzero coordinate. w has the same
    # sign convention, but need not be primitive. This parametrizes one of
    # each pair {M,-M} uniquely, with M=u w^T and ||M||_F<=X.
    pairs=[]
    for u1 in range(X+1):
        for u2 in range(-X,X+1):
            if u1==0 and u2<=0:continue
            d=u1*u1+u2*u2
            if not d or d>X*X or math.gcd(u1,abs(u2))!=1:continue
            radius=math.isqrt(X*X//d)
            for w1 in range(radius+1):
                for w2 in range(-radius,radius+1):
                    if w1==0 and w2<=0:continue
                    e=w1*w1+w2*w2
                    if e and d*e<=X*X:pairs.append((u1,u2,w1,w2))
    return pairs


def evaluate_case(X,B,pairs):
    assert B>2*X
    A=sorted(abs((u1+B*B*u2)*(w1+B*w2)) for u1,u2,w1,w2 in pairs)
    assert A and A[0]>0 and len(set(A))==len(A)
    n=len(A);N=2*n
    denominator=B*B+B+1
    j=math.floor(5*B/(2*math.pi*X)+.5)
    assert j>=2
    lam=2*flint.arb.pi()*X*j/B
    assert lam>4 and lam<flint.arb(44)/7
    counts=Counter()
    for a in A:
        r=j*a%denominator
        counts[min(r,denominator-r)]+=1
    value=flint.arb(0)
    for r,count in counts.items():
        value+=2*count*flint.arb.cos_pi_fmpq(flint.fmpq(2*r,denominator))
    scale=10**6
    upper=F(math.ceil(float(value.mid())/N*scale)+1,scale)
    assert value < flint.arb(upper.numerator)*N/upper.denominator
    lower=max(F(0),-n*upper)
    digest=hashlib.sha256((' '.join(map(str,A))).encode()).hexdigest()
    return dict(X=X,B=B,n=n,N=N,max_A=A[-1],encoded_set_sha256=digest,
                root_of_unity=dict(numerator=j,denominator=denominator),
                phase_radius_float=float(lam.mid()),
                D_over_N_upper_rational=str(upper),
                M_lower_rational=str(lower),R_lower_float=float(lower)/math.sqrt(n),
                count_over_leading_term_float=N/(6*X*X*math.log(X)),
                arb_precision=flint.ctx.prec,flint_version=flint.__version__,
                certificate='Arb enclosure at one exact root of unity',verified=True)


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Run through src/dirun.sh')
    flint.ctx.prec=96
    start=time.time()
    path=Path('.research/experiments/integer_cone_2026-10-20/results.json')
    path.parent.mkdir(parents=True,exist_ok=True)
    out=dict(qualification='Finite rigorous lower witnesses, not numerical global minima or a universal Chowla result.',
             variance_identity=variance_identity(),disk_sign=disk_sign(),cases=[])
    for X in [8,16,32,64]:
        pairs=cone_pairs(X)
        # Check the parameterization by constructing the actual matrices.
        matrices=[(u1*w1,u1*w2,u2*w1,u2*w2) for u1,u2,w1,w2 in pairs]
        assert len(set(matrices))==len(matrices)
        assert all(a*d==b*c and a*a+b*b+c*c+d*d<=X*X
                   for a,b,c,d in matrices)
        for multiplier in [2,4,16]:
            row=evaluate_case(X,multiplier*X+1,pairs)
            out['cases'].append(row)
            path.write_text(json.dumps(out,indent=2)+'\n')
            print(json.dumps({k:row[k] for k in ['X','B','n','D_over_N_upper_rational',
                  'R_lower_float','count_over_leading_term_float']}),flush=True)
    out['seconds']=time.time()-start
    path.write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
