"""Independent exact mathematical audits, run only on the VM."""
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path
import sys

import flint
import numpy as np

sys.path.insert(0,'.research/agents/tdense18_scratch')
from probe18 import boundary, C_HI

ROOT=Path('.research/agents/tdense18_scratch')


def exact_boundary_bruteforce(A):
    best=Fraction(0)
    for d in range(1,max(A)+1):
        Ad={a//d for a in A if a%d==0}
        for k in range(1,2*len(A)+1):
            D=Fraction(sum(a not in Ad for a in range(1,k+1)))
            D+=sum((1-Fraction(a,4*k) for a in Ad if k<a<4*k),Fraction(0))
            best=max(best,C_HI*k-D)
    return best


def power_coeff(c,k):
    result={0:Fraction(1)}
    for _ in range(k):
        out={}
        for a,x in result.items():
            for b,y in c.items():
                out[a+b]=out.get(a+b,Fraction(0))+x*y
        result=out
    return result


def modulus_moment(c,k):
    ck=power_coeff(c,k)
    return sum(x*x for x in ck.values())


def block_moments(variable=False):
    # Three disjoint frequency blocks, exactly two points in each block.
    blocks=[[(1,2),(1,3),(2,4)],[(7,8),(7,10),(9,10)],
            [(14,15),(14,18),(16,18)]]
    if variable:
        blocks=[[(),(1,),(2,4)],[(),(7,),(9,10)],[(),(14,),(16,18)]]
    probs=[Fraction(1,6),Fraction(1,3),Fraction(1,2)]
    states=[]
    weights={a:Fraction(1)-abs(Fraction(a-10,10))
             for block in blocks for alt in block for a in alt}
    for choices in itertools.product(range(3),repeat=3):
        A=set()
        pr=Fraction(1)
        for b,j in enumerate(choices):
            A.update(blocks[b][j])
            pr*=probs[j]
        states.append((A,pr))
    marg={a:sum((pr for A,pr in states if a in A),Fraction(0)) for a in weights}
    v=sum(p*(1-p)*weights[a]**2 for a,p in marg.items())
    m2=Fraction(0)
    m4=Fraction(0)
    # Exact Parseval moments of the symmetrized random Fourier sum.
    for A,pa in states:
        for B,pb in states:
            c={a:weights[a]*(int(a in A)-int(a in B)) for a in A|B}
            m2+=pa*pb*modulus_moment(c,1)
            m4+=pa*pb*modulus_moment(c,2)
    b=2
    expected_size=sum(pr*len(A) for A,pr in states)
    C=6*b*expected_size+4*b*b
    assert m2==2*v and m4<=C*2*v
    G=16384
    means=[]
    for A,pr in states:
        c=np.zeros(G)
        for a in A:
            c[a]=float(weights[a])
        means.append((float(np.abs(np.fft.fft(c)).mean()/2),float(pr)))
    mean=sum(x*p for x,p in means)
    variance=sum(p*(x-mean)**2 for x,p in means)
    lower=float(v)/(2*math.sqrt(float(C)))
    assert mean>=lower and variance<=b/2
    return dict(blocks=blocks,probabilities=list(map(str,probs)),states=len(states),
                expected_size=str(expected_size),variable_occupancy=variable,
                v=str(v),symmetrized_L2=str(m2),symmetrized_L4=str(m4),
                fourth_upper=str(C*2*v),mean_numerical=mean,variance_numerical=variance,
                theoretical_mean_lower=lower,theoretical_variance_upper=b/2,
                numerical_quadrature_grid=G)


def packet_theorem():
    records=[]
    for L,P in ((20,100),(20,199),(40,200),(60,1000),(80,6400)):
        for q in (4*L+1,L*L):
            h=L//20
            J=P//8
            U=[j*q+r for j in range(1,J+1) for r in range(-16*h,-14*h)]
            V=[j*q+r for j in range(1,J+1) for r in range(-h,h)]
            W=[j*q+r for j in range(1,J+1) for r in range(14*h,16*h)]
            def member(a):
                if not 1<=a<=P*q:
                    return False
                residue=(a+q//2)%q-q//2
                return abs(residue)*P*q <= L*(P*q-a)
            assert all(member(a) for a in U+V+W)
            m=len(U)
            assert len(V)==len(W)==m
            groups=[U,V,W]
            pair_checks=0
            # Test every possible difference, avoiding a quadratic expansion
            # of large packets. Integer interval differences have no gaps.
            for i,aa in enumerate(groups):
                for j,bb in enumerate(groups):
                    ra=aa[:2*h]
                    rb=bb[:2*h]
                    for dj in range(-J+1,J):
                        for dr in range(min(ra)-max(rb),max(ra)-min(rb)+1):
                            diff=dj*q+dr
                            value=int(member(abs(diff)))
                            expected=int(i==j or abs(i-j)==1)-int(i==j and diff==0)
                            assert value==expected
                            pair_checks+=1
            vec=[2,-3,2]
            quadratic=sum(vec[i]*vec[j]*(m*m-int(i==j)*m)
                          for i in range(3) for j in range(3)
                          if i==j or abs(i-j)==1)
            assert quadratic==-7*m*m-17*m
            n=0
            for r in range(-L,L+1):
                lower=-((r-1)//q)  # ceil((1-r)/q)
                upper=(P*q*(L-abs(r))-L*r)//(L*q)
                n+=max(0,upper-lower+1)
            assert 185*m>=n
            records.append(dict(L=L,P=P,q=q,n=n,m=m,quadratic=quadratic,
                exact_difference_checks=pair_checks,
                norm2=17*m,P9_rational_lower=str(Fraction(7*m,34)+Fraction(1,2)),
                density=Fraction(n,P*q).__str__()))
    return records


def main():
    checks=0
    for bits in range(1,1<<8):
        A=[a+1 for a in range(8) if bits>>a&1]
        b=boundary(A)
        assert Fraction(b['upper_rational'])==exact_boundary_bruteforce(A)
        checks+=1
    reductions=0
    for A in ([1],[1,3,7],[2,5,6],[3,4,5]):
        X=max(A)
        for H in range(X,3*X+1):
            for r in range(X+1):
                left={a:Fraction(max(0,H-abs(a-H-r)),H) for a in A}
                right={a:Fraction(max(0,a-r),H) for a in A}
                assert left==right
                reductions+=1
    theorem=block_moments()
    variable=block_moments(variable=True)
    interpolations=0
    for h in range(1,33):
        for u in (Fraction(1,3),Fraction(1,2),Fraction(2,3)):
            H=h+u
            alpha=h*(h+1-H)/H
            for b in range(-h-2,h+3):
                psi=lambda R:max(Fraction(0),1-Fraction(abs(b),1)/R)
                assert psi(H)==alpha*psi(h)+(1-alpha)*psi(h+1)
                interpolations+=1
    packets=packet_theorem()
    out=dict(exhaustive_boundary_sets=checks,full_window_coefficient_checks=reductions,
             block_theorem=theorem,variable_occupancy_blocks=variable,
             fractional_H_interpolation_checks=interpolations,
             packet_theorem=packets,flint=flint.__version__)
    (ROOT/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
    if (ROOT/'manifest.json').exists():
        manifest=json.loads((ROOT/'manifest.json').read_text())
        for p in (Path(__file__),ROOT/'verification.json'):
            manifest['sha256'][str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
        (ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps(out),flush=True)


if __name__=='__main__':
    main()
