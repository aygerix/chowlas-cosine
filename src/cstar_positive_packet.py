"""Rigorous finite premise of the averaged positive-reference obstruction.

Analytic sine integrals and independent midpoint interval quadrature certify
two positive packets of a genuine low-K Boolean support. No optimization
or sampled global minimum is used. All research runs on Dirichlet.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import socket

import flint
from cstar_l25_probe import rational_enclosure
from singer import is_perfect_difference_set


def differences(B):
    A=sorted({b-c for b in B for c in B if b>c})
    assert len(A)==len(B)*(len(B)-1)//2
    return A


def front(B,Q):
    A=differences(B);k=len(B);pi=flint.arb.pi()
    projection=sum((pi*(flint.arb(b)/Q-flint.arb(1)/2)).cos() for b in B)
    mass=2/pi*sum((pi*a/Q).sin()/a for a in A)
    # Independent composite midpoint integral of |F_B|²-k.
    N=256;total=flint.arb(0)
    for j in range(N):
        x=(2*j+1-N)*pi/(Q*N)
        z=sum((flint.acb(0,b*x).exp() for b in B),flint.acb(0))
        total+=z.real*z.real+z.imag*z.imag-k
    approximate=total/(Q*N)
    remainder=F(4*sum(a*a for a in A),Q**3*N*N)
    error=flint.arb(remainder.numerator)/remainder.denominator
    assert mass>approximate-error and mass<approximate+error
    return A,projection,mass,dict(midpoint_count=N,remainder=str(remainder),
        normalized_midpoint_enclosure=[str(t) for t in rational_enclosure(approximate)],
        agrees_with_analytic_integral=True)


def main():
    if 'dirichlet' not in socket.gethostname():raise SystemExit('Use src/dirun.sh')
    flint.ctx.prec=160
    inputs=json.loads(Path('.research/experiments/l25_2026-10-21/probe.json').read_text())
    row=next(r for r in inputs['cases'] if r['label'].endswith('p127'))
    B=sorted(row['metadata']['B']);Q=row['metadata']['modulus'];k=len(B)
    assert Q==k*(k-1)+1 and is_perfect_difference_set(B,Q)
    sub=[b for j,b in enumerate(B) if 3*(j+1)//4>3*j//4]
    h=len(sub);assert h==3*k//4
    A1,c1,m1,quad1=front(B,Q);A2,c2,m2,quad2=front(sub,Q)
    L=Q;actual=sorted(A1+[L*a for a in A2]);n=len(actual);K=k+h
    assert len(set(actual))==n and min(actual)>0 and K*K<=4*n
    measure=F(2,Q)-F(1,Q*Q)
    # Exact overlap because the interval I spans L/Q whole periods of 1_I(Lx).
    mass_lower=m1+m2-flint.arb(K)/Q-flint.arb(2*n)/(Q*Q)
    height_lower=min(c1*c1,c2*c2)-K
    delta=mass_lower-1
    assert delta>0 and height_lower>0
    dlo,_=rational_enclosure(delta);hlo,_=rational_enclosure(height_lower)
    # For all P>=0,mean(P)=1 and q=D-P+1 with ||q||²<=4n:
    # H >= delta²*height/measure -4Kn. This finite value need not be positive.
    Hlower=dlo*dlo*hlo/measure-4*K*n
    output=dict(host=socket.gethostname(),precision_bits=160,A=actual,n=n,
        full_B=B,subset_B=sub,modulus=Q,dilation=L,block_sizes=[k,h],
        all_circle_K_upper=K,all_circle_M_upper=str(F(K,2)),low_ratio_certified=True,
        packet_measure_exact=str(measure),packet_overlap_exact=str(F(1,Q*Q)),
        packet_D_mass_lower=str(rational_enclosure(mass_lower)[0]),
        packet_D_height_lower=str(hlo),excess_mass_lower=str(dlo),
        universal_reference_H_lower=str(Hlower),
        independent_midpoint_checks=[quad1,quad2],
        qualification='Finite packet premise is rigorous. Asymptotic Omega(n²) reference-cost obstruction is a separate paper proof; no finite positive-cost or universal Chowla claim.')
    path=Path('.research/experiments/positive_packet_2026-10-21/results.json')
    path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:output[k] for k in ['n','block_sizes','all_circle_M_upper','packet_D_mass_lower',
        'packet_D_height_lower','excess_mass_lower','universal_reference_H_lower']}),flush=True)
    print(json.dumps(dict(status='PASS',output=str(path))),flush=True)


if __name__=='__main__':main()
