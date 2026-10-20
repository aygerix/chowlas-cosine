"""Independent row-count/Arb checks of widened disk-lens mean certificates.

No imports from the producers. Run on Dirichlet. These are lower bounds
for fractional means, not upper certificates for Boolean outputs.
"""
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import socket
import flint


def stats(q):
    r=math.isqrt(q)
    rows=[(y,math.isqrt(q-y*y)) for y in range(-r,r+1)]
    B=sum(2*l+1 for y,l in rows)
    parity=[0]*4
    singles=[0,0];double=0
    for y,l in rows:
        even=2*(l//2)+1
        parity[y%2]+=even
        parity[2+y%2]+=2*l+1-even
        singles[y%2]+=1-2*((l//2)%2)
        if y%2==0:double+=1-2*((y//2+l//2)%2)
    single=sum(t*t for t in singles)-B
    both=double*double-B
    assert B>=2*r*r+2*r+1 and single<=0 and 5*both<=-B
    axis=[sum(max(0,2*(l-k)+1) for y,l in rows) for k in range(r+1)]
    return dict(B=B,r=r,axis=axis,mean=F(sum(t*t for t in parity)-B,2*B),
                budgets={(1,0):single,(0,1):single,(1,1):both})


def directions(X,V):
    # Different traversal from both producers; sort only for decoding bytes.
    return sorted((a,b,a*a+b*b) for b in range(-V,V+1) for a in range(V+1)
                  if (a>0 or b>0) and math.gcd(abs(b),a)==1 and X<=a*a+b*b<=V*V)


def ceilroot(n):
    r=math.isqrt(n)
    return r+(r*r<n)


def up(n,d,scale=10**6):
    return -((-n*scale)//d)


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    flint.ctx.prec=192
    root=Path('.research/experiments/wide_mean_2026-10-20')
    heat=json.loads((root/'results.json').read_text())
    parity=json.loads((root/'parity.json').read_text())
    matrices=[tuple(A) for A in parity['matrices']]
    assert len(set(matrices))==6 and all((a*d-b*c)%2==1 for a,b,c,d in matrices)
    for u in [(1,0),(0,1),(1,1)]:
        assert Counter(((a*u[0]+c*u[1])%2,(b*u[0]+d*u[1])%2)
                       for a,b,c,d in matrices)==Counter({(1,0):2,(0,1):2,(1,1):2})
    cache={q:stats(q) for q in range(1,4097)}
    checked=[]
    source={(r['X'],r['pattern']):r for r in heat['cases']}
    for row in parity['widened_cases']+parity['near_linear_cases']:
        X=row['X'];V=row['V'];key=(X,row['pattern']);old=source.get(key)
        assignment=bytes.fromhex((old or row)['radius_indices_hex'])
        assert hashlib.sha256(assignment).hexdigest()==(old or row)['radius_sha256']
        U=directions(X,V);assert len(U)==len(assignment)==row['fibers']
        groups=Counter();nmax=0
        H=flint.arb(0);cosines={};exps={};m=4*V
        for (a,b,d),option in zip(U,assignment):
            assert option in [0,1,2]
            q=(X*X//d,9*X*X//(16*d),X*X//(4*d))[option]
            if q not in cache:cache[q]=stats(q)
            info=cache[q];B=info['B'];groups[q,a%2,b%2]+=1;nmax+=(B-1)//2
            if old:
                for k in range(1,info['r']+1):
                    z=a*k;t=d*k*k
                    if z not in cosines:cosines[z]=(flint.arb(5*z)/V).cos()
                    if t not in exps:exps[t]=(-flint.arb(t)/(2*m*m)).exp()
                    H+=2*info['axis'][k]*exps[t]*cosines[z]/B
        mass_up=sum(up(count*cache[q]['mean'].numerator,cache[q]['mean'].denominator)
                    for (q,a,b),count in groups.items())
        mass_down=sum((count*cache[q]['mean'].numerator*10**6)//cache[q]['mean'].denominator
                      for (q,a,b),count in groups.items())
        mu_up=(mass_up+10**6-1)//10**6
        assert mu_up==row['certified_mass_upper'] and nmax==row['max_boolean_cardinality']
        means=[]
        for A in matrices:
            means.append(F(sum(up(count*cache[q]['budgets'][((A[0]*a+A[2]*b)%2,
                       (A[1]*a+A[3]*b)%2)],cache[q]['B']) for (q,a,b),count in groups.items()),10**6))
        assert means==list(map(F,row['matrix_D_upper_rationals']))
        index=min(range(6),key=lambda i:means[i]);A=matrices[index]
        assert tuple(row['best_matrix'])==A
        h=[6*X**3+i for i in (1,3,5,7)]
        assert all(math.gcd(p,q)==1 for i,p in enumerate(h) for q in h[i+1:])
        assert row['best_residues']==[(p-1)//2 if a else 0 for p,a in zip(h,A)]
        error=F(88*X*mu_up,7*min(h));lower=max(F(0),-(means[index]+error)/2)
        assert F(row['scalar_transfer_error_upper'])==error
        assert F(row['fractional_mean_M_lower_rational'])==lower
        assert F(row['fractional_mean_M_global_upper_rational'])==F(len(U),2)
        assert F(row['mean_ratio_lower_rational'])==lower/ceilroot(mu_up)
        assert F(row['any_coupling_expected_ratio_lower_rational'])==lower/ceilroot(nmax)
        if old:
            lo,hi=old['expected_mass_interval']
            assert F(mass_down,10**6)>lo and F(mass_up,10**6)<hi
            assert old['max_boolean_cardinality']==nmax
            tail=F(25*(m+1)**2,2**100)
            assert F(old['gaussian_alias_tail_upper'])==tail and (min(h)-X)**2>=400*m*m
            tb=flint.arb(tail.numerator)/tail.denominator
            bound=F(old['fractional_mean_M_lower_rational'])
            assert H+tb+2*flint.arb(bound.numerator)/bound.denominator*(1+tb)<0
            assert F(old['mean_ratio_lower_rational'])==bound/ceilroot(hi)
            assert F(old['any_coupling_expected_ratio_lower_rational'])==bound/ceilroot(nmax)
        result=dict(X=X,V=V,pattern=row['pattern'],fibers=len(U),
                    parity_lower=str(lower),mean_ratio_lower=float(lower/ceilroot(mu_up)),
                    heat_checked=bool(old),passed=True)
        checked.append(result);print(json.dumps(result),flush=True)
    eps=F(1,2000)
    assert 630*eps+860160*eps*eps<1
    out=dict(status='PASS',host=socket.gethostname(),precision_bits=192,
             independent_disk_method='row alternating sums and direct row lens intersections',
             finite_q_checks=4096,cases=checked,
             broader_sampler_constant=str(eps),qualification='Fractional means and explicitly scoped sampler laws only.')
    (root/'verification.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
