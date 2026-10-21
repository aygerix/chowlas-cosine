"""Independent reconstruction of saved zero-carrier reciprocal certificates.

Rebuild the exact residual by sparse integer shifts; recompute the finite
selected Taylor coefficients of p² by analytic inversion in Arb. No FFT
proposal is repeated, and no sampled integral enters the verification.
"""
from fractions import Fraction as F
import argparse
import json
import math
from pathlib import Path
import socket

import flint


def ball(x):
    x = F(x)
    return flint.arb(x.numerator)/x.denominator


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    flint.ctx.prec = 768
    parser = argparse.ArgumentParser()
    parser.add_argument('--prefix', action='store_true')
    args = parser.parse_args()
    base = Path('.research/experiments/zero_reciprocal_2026-10-21')
    name = 'prefix' if args.prefix else 'results'
    data = json.loads((base/f'{name}.json').read_text())
    out = dict(host=socket.gethostname(), precision=flint.ctx.prec, cases=[])
    for row in data['cases']:
        A, n, B, den = row['A'], row['n'], row['band'], row['finite_denominator']
        assert n == len(A) == len(set(A)) and min(A) > 0
        z = list(map(int, row['finite_sine_numerators']))
        assert len(z) == B
        SP = F(row['S_P_exact'])
        z0_squared = SP*den*den-sum(t*t for t in z)
        assert z0_squared.denominator == 1
        z0 = math.isqrt(z0_squared.numerator)
        assert z0*z0 == z0_squared
        z = [z0]+z
        # A separate sparse multiplication rather than FLINT convolution.
        U = [0]*(B+max(A)+1)
        U[0] = -den
        for a in A:
            for j, coefficient in enumerate(z):
                U[j+a] += coefficient
        lam = 2*flint.arb(n).sqrt()
        delta = lam-ball(row['M_upper'])
        assert delta > 0
        u2 = sum(t*t for t in U)
        v2 = sum(t*t for t in z)
        uv = sum(U[j]*t for j, t in enumerate(z))
        residual2 = (flint.arb(u2+4*n*v2)+2*lam*uv)/(den*den)
        eps = ball(row['L2_error_upper'])
        assert residual2 > 0 and eps > residual2.sqrt()/delta
        SE, TE = ball(row['S_error_upper']), ball(row['T_error_upper'])
        assert SE > 2*ball(SP).sqrt()*eps+eps*eps
        assert TE > flint.arb(n).sqrt()*eps*(1/delta+ball(F(sum(map(abs,z)),den)))
        # Direct formal inverse through max(A), using no floating FFT.
        X = max(A)
        p = [flint.arb(0)]*(X+1)
        p[0] = 1/lam
        for j in range(1, X+1):
            p[j] = -sum((p[j-a] for a in A if a <= j), flint.arb(0))/lam
        T_direct = sum((sum((p[j]*p[a-j] for j in range(a+1)), flint.arb(0))
                        for a in A), flint.arb(0))
        TP = ball(row['T_P_exact'])
        assert abs(T_direct-TP) < TE
        assert T_direct < 0
        Slo, Shi = ball(SP)-SE, ball(SP)+SE
        Qlo, Qhi = (Slo-ball(F(1,4*n)))/2, (Shi-ball(F(1,4*n)))/2
        Hlo, Hhi = 1/lam-lam*Shi-T_direct/2, 1/lam-lam*Slo-T_direct/2
        assert Qlo > 0
        negative, positive = bool(Hhi < 0), bool(Hlo > 0)
        assert negative or positive
        left, right = map(ball, row['infinite_Rayleigh_bracket'])
        for corner in (Hlo/Qlo,Hlo/Qhi,Hhi/Qlo,Hhi/Qhi):
            assert left < corner and right > corner
        # Finite odd-sector energy via selected correlations.
        Q = F(sum(t*t for t in z[1:]), 2*den*den)
        raw = sum(sum(z[j]*z[j+a] for j in range(1,B-a+1)) for a in A)
        raw -= F(sum(sum(z[j]*z[a-j] for j in range(1,a)) for a in A),2)
        H = raw/(den*den)
        assert Q == F(row['finite_Q_exact'])
        assert H == F(row['finite_H_exact'])
        assert (H < 0) == negative
        result = dict(label=row['label'], residual_rebuilt_by_sparse_shifts=True,
            T0_direct_formal_inverse_ball=str(T_direct), T0_negative=True,
            infinite_quotient_interval_independently_verified=True,
            infinite_energy_negative=negative, infinite_energy_positive=positive,
            finite_exact_odd_energy_verified=True)
        out['cases'].append(result)
        print(json.dumps(result), flush=True)
    out['status'] = 'PASS'
    verified = 'prefix_verification' if args.prefix else 'verification'
    (base/f'{verified}.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__ == '__main__':
    main()
