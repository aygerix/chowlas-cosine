"""Exact J0 annulus sign and arbitrary-angular-subset CRT point tests."""
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import socket
import flint
import numpy as np
import sympy as sp
from cstar_integer_cone import cone_pairs


def sign_certificate():
    u=sp.symbols('u');n=20
    coefficients=[F((-1)**k,math.factorial(k)**2) for k in range(n+1)]
    coefficients[0]+=F(1,10)
    polynomial=sp.Poly(sum(sp.Rational(a.numerator,a.denominator)*u**k
                           for k,a in enumerate(coefficients)),u)
    lo,hi=F(9,4),F(25,4)
    assert hi<(n+1)**2
    roots=int(polynomial.count_roots(sp.Rational(9,4),sp.Rational(25,4)))
    assert roots==0 and polynomial.eval(sp.Rational(9,4))<0
    # Independent rational Bernstein test; no SymPy in the conversion.
    partitions=[]
    def bernstein(a,b,depth=0):
        power=[sum((coefficients[k]*math.comb(k,j)*a**(k-j)*(b-a)**j
                    for k in range(j,n+1)),F(0)) for j in range(n+1)]
        controls=[sum((power[j]*F(math.comb(i,j),math.comb(n,j))
                       for j in range(i+1)),F(0)) for i in range(n+1)]
        if max(controls)<0:
            partitions.append(dict(interval=[str(a),str(b)],
                                   maximum_control=str(max(controls))));return
        assert depth<8
        mid=(a+b)/2;bernstein(a,mid,depth+1);bernstein(mid,b,depth+1)
    bernstein(lo,hi)
    assert F(1,10)-F(44,7000)>F(1,12)
    return dict(J0_interval=['3','5'],strict_upper='-1/10',order=n,
                coefficients_low_to_high=[str(a) for a in coefficients],
                sturm_root_count=roots,bernstein_partitions=partitions,verified=True)


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Run through src/dirun.sh')
    flint.ctx.prec=128
    rng=np.random.default_rng(20261023)
    root=Path('.research/experiments/cone_confinement_2026-10-20')
    root.mkdir(parents=True,exist_ok=True)
    out=dict(qualification='Paper annular-subset obstruction for phase-rich CRT encoding; '
             'finite points are rigorous lower bounds, not global minima.',seed=20261023,
             sign=sign_certificate(),cases=[])
    for X in [24,64]:
        raw=[z for z in cone_pairs(X) if 25*(z[0]**2+z[1]**2)*(z[2]**2+z[3]**2)>=9*X*X]
        raw_hash=hashlib.sha256((' '.join(','.join(map(str,z)) for z in raw)).encode()).hexdigest()
        raw_matrices=[(a*c,a*d,b*c,b*d) for a,b,c,d in raw]
        raw_index={M:i for i,M in enumerate(raw_matrices)}
        h=[1500*X+i for i in [1,3,5,7]];P=math.prod(h);C=[P//z for z in h]
        assert min(h)>=1000*X
        assert all(math.gcd(a,b)==1 for i,a in enumerate(h) for b in h[i+1:])
        masks={name:[] for name in ['full_annulus','two_ruling_threshold','coupled_modular','seeded_even']}
        for z in raw:
            a,b,c,d=z;M=(a*c,a*d,b*c,b*d)
            masks['full_annulus'].append(M)
            if a*a*(c*c+d*d)+c*c*(a*a+b*b)>=(a*a+b*b)*(c*c+d*d):
                masks['two_ruling_threshold'].append(M)
            if (M[0]+M[3])%7 in [0,1,6]:masks['coupled_modular'].append(M)
            if rng.random()<.5:masks['seeded_even'].append(M)
        for name,matrices in masks.items():
            arr=np.array(matrices,dtype=np.int64);n=len(arr)
            angles=np.arange(64)*(2*np.pi/64)
            sums=np.cos((5/X)*((arr[:,0]+arr[:,3])[:,None]*np.cos(angles)
                                  +(arr[:,2]-arr[:,1])[:,None]*np.sin(angles))).sum(axis=0)
            index=int(sums.argmin())
            phi=2*flint.arb.pi()*index/64
            Y=[5*phi.cos(),-5*phi.sin(),5*phi.sin(),5*phi.cos()]
            k=[round(float((y*m/(2*flint.arb.pi()*X)).mid())) for y,m in zip(Y,h)]
            assert all(abs(2*flint.arb.pi()*X*z/m-y)<flint.arb.pi()*X/m
                       for z,m,y in zip(k,h,Y))
            j=sum(z*(P//m)*pow(P//m,-1,m) for z,m in zip(k,h))%P
            assert all(j%m==z%m for z,m in zip(k,h))
            A=sorted(abs(sum(c*z for c,z in zip(C,M))) for M in matrices)
            assert A and A[0]>0 and len(set(A))==n
            counts=Counter()
            for a in A:
                r=j*a%P;counts[min(r,P-r)]+=1
            value=sum((count*flint.arb.cos_pi_fmpq(flint.fmpq(2*r,P))
                       for r,count in counts.items()),flint.arb(0))
            scale=10**7;upper=F(math.ceil(float(value.mid())/n*scale)+1,scale)
            assert value<flint.arb(upper.numerator)*n/upper.denominator
            assert upper<-F(1,12)
            row=dict(X=X,pattern=name,n=n,moduli=h,C=C,orientation_index=index,
                     orientation_denominator=64,phase_residues=k,root_of_unity=dict(j=j,q=P),
                     f_over_n_upper_rational=str(upper),M_lower_rational=str(-n*upper),
                     R_lower_float=float(-n*upper)/math.sqrt(n),
                     raw_factor_sha256=raw_hash,
                     selection_mask_hex=hex(sum(1 << raw_index[M] for M in matrices)),
                     encoded_set_sha256=hashlib.sha256((' '.join(map(str,A))).encode()).hexdigest(),
                     arb_precision=flint.ctx.prec,verified=True)
            out['cases'].append(row)
            print(json.dumps({z:row[z] for z in ['X','pattern','n','orientation_index',
                             'f_over_n_upper_rational','R_lower_float']}),flush=True)
    (root/'rotation.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
