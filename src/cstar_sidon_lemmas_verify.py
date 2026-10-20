"""Independent graph enumeration and sparse population moment recount.

Also check cyclic-shift sixth moments off the finite Fourier grid.
Run on Dirichlet. No producer imports, matrix moment products, or FFT.
"""
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
import socket
import sys
from pathlib import Path
import flint


def spectrum(B):
    S={(x-u,y-v) for x,y in B for u,v in B if (x,y)!=(u,v)}
    assert len(S)==len(B)*(len(B)-1)
    return S


def square(S):
    c=Counter()
    for x,y in S:
        for u,v in S:c[x+u,y+v]+=1
    return c


def exponential(turn):
    z=2*flint.arb.pi()*turn.numerator/turn.denominator
    return z.cos(),z.sin()


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    flint.ctx.prec=192;root=Path('.research/experiments/sidon_fibers_2026-10-20')
    extra='--extra' in sys.argv
    rows=json.loads((root/('population_extra.json' if extra else 'population.json')).read_text());checked=[];moments=[]
    for row in rows:
        p=row['p'];sets=[]
        # Independent implicit-parabola parameterization. For l=(1,t),
        # use coordinates r=x+t*y, y; add the l=(0,1) case separately.
        for direction in range(p+1):
            for a in range(1,p):
                for b in range(p):
                    for c in range(p):
                        B=[]
                        for t in range(p):
                            z=(a*t*t+b*t+c)%p
                            B.append(((t-direction*z)%p,z) if direction<p else (z,t))
                        sets.append(tuple(sorted(B)))
        sets.sort();N=len(sets)
        assert len(set(sets))==N==row['distinct_affine_parabolas']
        assert hashlib.sha256(repr(sets).encode()).hexdigest()==row['enumeration_sha256']
        hist=Counter();convsum=Counter()
        for B in sets:
            S=spectrum(B);hist.update(S);convsum.update(square(S))
        amin=None;Hmax=None;Hsum=0;k=2*F(row['reference_averaged_global_M_lower'])
        for B in sets:
            S=spectrum(B);conv=square(S)
            a=N*p*(p-1)-sum(hist[s] for s in S)
            third=sum(conv[s] for s in S)
            H=N*third-2*sum(c*hist[-s[0],-s[1]] for s,c in conv.items())+sum(convsum[s] for s in S)
            amin=a if amin is None else min(amin,a);Hmax=H if Hmax is None else max(Hmax,H);Hsum+=H
            assert 2*a*N*k*k+H*N*k-a*a<0
        assert F(amin,N)==F(row['conditional_a_min'])
        assert F(Hmax,N)==F(row['conditional_H_max']) and F(Hsum,N*N)==F(row['average_H'])
        checked.append(dict(p=p,all_point_sets=N,conditional_moments_recounted=True,
                            conditional_H_max=str(F(Hmax,N)),all_certificate_inequalities=True))
        # Actual shifted exponential sums at an off-grid physical phase.
        qx,qy=F(1,3*p),F(2,5*p)
        dx=[exponential(qx*t) for t in range(p)];dy=[exponential(qy*t) for t in range(p)]
        ax=sum(z[0] for z in dx);bx=sum(z[1] for z in dx)
        ay=sum(z[0] for z in dy);by=sum(z[1] for z in dy)
        Vre=(ax*ay-bx*by)/p;Vim=(ax*by+bx*ay)/p
        mean_re=flint.arb(0);mean_im=flint.arb(0);sixth=flint.arb(0)
        for sx in range(p):
            for sy in range(p):
                re=flint.arb(0);im=flint.arb(0)
                for t in range(p):
                    er,ei=exponential(qx*((t+sx)%p)+qy*((t*t+sy)%p));re+=er;im+=ei
                re-=Vre;im-=Vim;mean_re+=re;mean_im+=im;sixth+=(re*re+im*im)**3
        assert mean_re.contains(0) and mean_im.contains(0)
        sixth/=p*p
        assert sixth<169**6*p**3
        moments.append(dict(p=p,phase_turns=[str(qx),str(qy)],
                            sixth_over_p3_ball=str(sixth/(p**3)),mean_centering_checked=True))
        print(json.dumps(checked[-1]),flush=True)
    out=dict(status='PASS',host=socket.gethostname(),precision_bits=192,
             exhaustive_population_recounts=checked,off_grid_shift_moment_checks=moments,
             qualification='Finite checks corroborate normalizations; all-prime bounds are the paper argument.')
    (root/('lemmas_extra_verification.json' if extra else 'lemmas_verification.json')).write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
