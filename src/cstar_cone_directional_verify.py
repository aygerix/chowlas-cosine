"""Reverse-fiber enumeration and reduced-period Arb recheck on Dirichlet."""
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import socket
import flint


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Run through src/dirun.sh')
    flint.ctx.prec=160
    root=Path('.research/experiments/cone_confinement_2026-10-20')
    source=json.loads((root/'directional.json').read_text())
    out=dict(qualification='Independent reverse-factor enumeration, integer hashes, '
             'and 160-bit reduced-period point checks; not an external paper-proof audit.',cases=[])
    for X in sorted({row['X'] for row in source['cases']}):
        cases=[row for row in source['cases'] if row['X']==X]
        values={row['pattern']:[] for row in cases}
        counts={row['pattern']:Counter() for row in cases}
        h=cases[0]['moduli'];C=cases[0]['C'];q=h[1]*h[2]
        # Enumerate w first. The ||u||^2>=X restriction bounds ||w||^2<=X.
        wb=math.isqrt(X)
        for w1 in range(wb+1):
            for w2 in range(-wb,wb+1):
                if w1==0 and w2<=0:continue
                ws=w1*w1+w2*w2
                if not ws or ws>X:continue
                ub=math.isqrt(X*X//ws)
                for u1 in range(ub+1):
                    for u2 in range(-ub,ub+1):
                        us=u1*u1+u2*u2
                        if (u1==0 and u2<=0) or us<X or us*ws>X*X:continue
                        if math.gcd(u1,abs(u2))!=1:continue
                        patterns=['annular']
                        if 0<=u2<=u1:patterns.append('wedge_annular')
                        if (u2>=0)==(us.bit_length()%2==0):patterns.append('scale_changing')
                        M=(u1*w1,u1*w2,u2*w1,u2*w2)
                        a=abs(sum(c*m for c,m in zip(C,M)))
                        # Direct off-diagonal phase, without the producer's
                        # large scalar CRT root or its residue-count period.
                        r=(M[1]*h[2]-M[2]*h[1])%q
                        r=min(r,q-r)
                        for name in patterns:
                            values[name].append(a);counts[name][r]+=1
        for row in cases:
            name=row['pattern'];A=sorted(values[name])
            assert len(A)==row['n'] and len(set(A))==len(A) and A[0]>0
            digest=hashlib.sha256((' '.join(map(str,A))).encode()).hexdigest()
            assert digest==row['encoded_set_sha256']
            value=sum((n*flint.arb.cos_pi_fmpq(flint.fmpq(2*r,q))
                       for r,n in counts[name].items()),flint.arb(0))
            upper=F(row['f_over_n_upper_rational'])
            assert value<flint.arb(upper.numerator)*len(A)/upper.denominator
            assert F(row['M_lower_rational'])==-len(A)*upper
            result=dict(X=X,pattern=name,n=len(A),reduced_phase_denominator=q,
                        set_hash_matches=True,point_bound_verified=True)
            out['cases'].append(result);print(json.dumps(result),flush=True)
    (root/'directional_verification.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
