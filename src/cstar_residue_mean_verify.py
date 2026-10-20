"""Exact GL2 residue test and independent nonuniform-center reconstruction.

Run on Dirichlet. No grid is used to certify an all-phase upper bound.
"""
from collections import Counter,defaultdict
from fractions import Fraction as F
import itertools
import json
import math
from pathlib import Path
import socket
import flint


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    flint.ctx.prec=192
    root=Path('.research/experiments/wide_mean_2026-10-20')
    checked=[]
    for p in [2,3,5,7,11]:
        G=[A for A in itertools.product(range(p),repeat=4) if (A[0]*A[3]-A[1]*A[2])%p]
        assert len(G)==(p*p-1)*(p*p-p)
        for u,w in [((1,0),(1,0)),((1,1),(1,1)),((0,1),(1,0)),((1,2),(2,1))]:
            u=tuple(x%p for x in u);w=tuple(x%p for x in w)
            if not any(u) or not any(w):continue
            M=(u[0]*w[0],u[0]*w[1],u[1]*w[0],u[1]*w[1])
            counts=Counter(sum(a*m for a,m in zip(A,M))%p for A in G)
            assert len(set(counts[t] for t in range(1,p)))==1
            assert F(counts[0]-counts[1],len(G))==-F(1,p*p-1)
        # Essential exclusions: zero residue averages +1; rank two also
        # averages positively, so neither can be silently included.
        counts=Counter((A[0]+A[3])%p for A in G)
        assert F(counts[0]-counts[1],len(G))==F(1,(p*p-1)*(p-1))
        checked.append(dict(p=p,group_size=len(G),rank_one_average=str(-F(1,p*p-1)),
                            rank_two_average=str(F(1,(p*p-1)*(p-1))),zero_average=1))
    laws=json.loads((root/'center_law.json').read_text());law_checks=[]
    for row in laws['cases']:
        R=row['R'];disk={(a,b) for a in range(-R,R+1) for b in range(-R,R+1) if a*a+b*b<=R*R}
        weights={}
        for (a,b),size,prob in zip(row['center_representatives'],row['orbit_sizes'],row['probabilities']):
            orbit={(x,y) for x,y in itertools.product({a,-a},{b,-b})}
            orbit|={(y,x) for x,y in list(orbit)}
            assert len(orbit)==size and orbit<=disk
            for T in orbit:
                assert T not in weights
                weights[T]=F(prob)/size
        assert set(weights)==disk and sum(weights.values())==1 and min(weights.values())>=0
        coeff=defaultdict(F)
        for (a,b),prob in weights.items():
            if prob==0:continue
            for x,y in disk:
                w=(x-a,y-b)
                if w!=(0,0) and (2*a-x,2*b-y) in disk:coeff[w]+=prob
        assert all(coeff[w]==coeff[-w[0],-w[1]] for w in list(coeff))
        mass=sum(coeff.values())/2
        assert mass==F(row['expected_n'])
        pv=[sum(c*(1-2*((w[0]*v[0]+w[1]*v[1])%2)) for w,c in coeff.items())
            for v in [(1,0),(0,1),(1,1)]]
        assert pv==list(map(F,row['repaired_parity_D'])) and min(pv)>=0
        q=list(map(F,row['adversarial_phase_rationals']));value=flint.arb(0)
        for (a,b),c in coeff.items():
            angle=a*q[0]+b*q[1]
            value+=(flint.arb(angle.numerator)/angle.denominator).cos()*c.numerator/c.denominator
        lower=F(row['point_M_lower_rational'])
        assert value+2*flint.arb(lower.numerator)/lower.denominator<0
        law_checks.append(dict(R=R,expected_n=str(mass),parity_nonnegative=True,
                               point_lower=str(lower),endpoint_reconstruction=True,passed=True))
    # For X>=1 and B<=X, hmin>6000 X^3 makes the f-transfer
    # error <=(44/42000)n/X^2 < n/(8 B^2).
    assert F(44,42000)<F(1,8)
    out=dict(status='PASS',host=socket.gethostname(),precision_bits=192,
             finite_GL2_tests=checked,center_law_checks=law_checks,
             theorem='M(A)>=n/(8B^2) for encoded rank-one supports with primitive left factor and right factor norm<=B, '
                     'B<=X, h=6000X^3+(1,3,5,7); not arbitrary integer supports.')
    (root/'residue_verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out),flush=True)


if __name__=='__main__':main()
