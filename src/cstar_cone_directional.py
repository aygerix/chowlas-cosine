"""Arb point certificates for arbitrary-direction, complete radial fibers.

This tests the one-ruling integer lift suggested by exact finite-field
confinement. Computation only on Dirichlet; no global upper bound is claimed.
"""
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import socket
import flint
from cstar_integer_cone import cone_pairs


def selected(name,u1,u2,X):
    d=u1*u1+u2*u2
    if d<X:return False
    if name=='annular':return True
    if name=='wedge_annular':return 0<=u2<=u1
    if name=='scale_changing':return (u2>=0)==(d.bit_length()%2==0)
    raise ValueError(name)


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Run through src/dirun.sh')
    flint.ctx.prec=112
    assert F(2)*F(157,50)*72/F(3*72//2+5)>4
    root=Path('.research/experiments/cone_confinement_2026-10-20')
    root.mkdir(parents=True,exist_ok=True)
    out=dict(qualification='Certified lower witnesses at a fixed CRT phase; '
             'not global minima or a universal Chowla theorem.',cases=[],
             paper_bound='D(theta)<=-N/50+308 X^2 for all directional subsets, X>=72 divisible by four')
    for X in [96,128]:
        pairs=cone_pairs(X)
        h=[3*X//2+i for i in [1,3,5,7]];P=math.prod(h);C=[P//z for z in h]
        assert all(math.gcd(a,b)==1 for i,a in enumerate(h) for b in h[i+1:])
        assert min(h)**2>2*X*X
        residues=[0,1,-1,0]
        j=sum(r*(P//m)*pow(P//m,-1,m) for r,m in zip(residues,h))%P
        assert all(j%m==r%m for r,m in zip(residues,h))
        for denominator in h[1:3]:
            radius=2*flint.arb.pi()*X/denominator
            assert radius>4 and radius<flint.arb(44)/7
        for name in ['annular','wedge_annular','scale_changing']:
            subset=[row for row in pairs if selected(name,row[0],row[1],X)]
            A=sorted(abs(C[0]*u1*w1+C[1]*u1*w2+C[2]*u2*w1+C[3]*u2*w2)
                     for u1,u2,w1,w2 in subset)
            assert A and A[0]>0 and len(A)==len(set(A))
            counts=Counter()
            for a in A:
                r=j*a%P;counts[min(r,P-r)]+=1
            value=sum((multiplicity*flint.arb.cos_pi_fmpq(flint.fmpq(2*r,P))
                       for r,multiplicity in counts.items()),flint.arb(0))
            n=len(A);scale=10**7
            upper=F(math.ceil(float(value.mid())/n*scale)+1,scale)
            assert value<flint.arb(upper.numerator)*n/upper.denominator and upper<0
            lower=-n*upper
            # A second finite check: independently sum the lattice-error upper
            # bounds fiber by fiber, using Arb only to enclose irrational r.
            directions=Counter((a,b) for a,b,c,d in subset)
            radial_sum=sum((flint.arb(X)/flint.arb(a*a+b*b).sqrt()
                            for a,b in directions),flint.arb(0))
            assert radial_sum<=4*X*X
            assert 2*value<=-flint.arb(2*n)/50+77*radial_sum
            row=dict(X=X,pattern=name,n=n,directions=len(directions),
                     min_direction_squared=min(a*a+b*b for a,b in directions),
                     C=C,moduli=h,root_of_unity=dict(j=j,q=P),
                     f_over_n_upper_rational=str(upper),M_lower_rational=str(lower),
                     R_lower_float=float(lower)/math.sqrt(n),
                     encoded_set_sha256=hashlib.sha256((' '.join(map(str,A))).encode()).hexdigest(),
                     arb_precision=flint.ctx.prec,verified=True)
            out['cases'].append(row);print(json.dumps(row),flush=True)
    (root/'directional.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
