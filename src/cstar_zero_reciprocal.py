"""Validate the exceptional zero-carrier odd reciprocal Rayleigh seed.

FFT only proposes a dyadic polynomial P. An EXACT polynomial residual
(lambda+F)P-1 bounds the infinite analytic reciprocal in L2. The known
all-circle M upper bound supplies the inverse margin. No grid quadrature
is used as proof of the infinite moments or their signs.
"""
from fractions import Fraction as F
import argparse
import json
import math
from pathlib import Path
import socket

import flint
import numpy as np


def ball(x):
    x = F(x)
    return flint.arb(x.numerator)/x.denominator


def upper(x, den=1 << 100):
    middle = float(x)
    q = F(middle)+8*F(math.ulp(middle))+F(1, den)
    assert ball(q) > x
    return q


def bracket(lo, hi, den=1 << 64):
    left, right = float(lo), float(hi)
    lower = F(left)-8*F(math.ulp(left))-F(1, den)
    higher = F(right)+8*F(math.ulp(right))+F(1, den)
    assert ball(lower) < lo and ball(higher) > hi
    return [str(lower), str(higher)]


def one(A, M_upper, label, band_multiple=8):
    A = sorted(A)
    n, X = len(A), max(A)
    assert len(set(A)) == n and min(A) > 0 and M_upper*M_upper <= n
    lam = 2*flint.arb(n).sqrt()
    margin = lam-ball(M_upper)
    assert margin > 0
    assert band_multiple >= 8
    B = band_multiple*X
    grid = 1 << (8*(B+1)).bit_length()
    spectral = np.zeros(grid, dtype=np.complex128)
    spectral[A] = 1
    values = np.fft.ifft(spectral, norm='forward')
    reciprocal = 1/(2*math.sqrt(n)+values)
    coeff = (np.fft.fft(reciprocal)/grid)[:B+1].real
    den = 1 << 64
    nums = [int(round(float(c)*den)) for c in coeff]
    P = flint.fmpz_poly(nums)
    freq = [int(j in set(A)) for j in range(X+1)]
    product = flint.fmpz_poly(freq)*P
    U = [int(product[j])-(den if j == 0 else 0) for j in range(B+X+1)]
    # Residual coefficients are (U_j+lambda*V_j)/den exactly.
    v2 = sum(z*z for z in nums)
    u2 = sum(z*z for z in U)
    uv = sum(U[j]*nums[j] for j in range(B+1))
    residual2 = (flint.arb(u2+4*n*v2)+2*lam*uv)/(den*den)
    assert residual2 > 0
    epsilon = upper(residual2.sqrt()/margin)
    S_P = F(v2, den*den)
    S_error = upper(2*ball(S_P).sqrt()*ball(epsilon)+ball(epsilon)**2)
    square = P*P
    T_P = F(sum(int(square[a]) for a in A), den*den)
    # ||p²-P²||2 <= (||p||inf+||P||inf)||p-P||2.
    T_error = upper(flint.arb(n).sqrt()*ball(epsilon)*
                    (1/margin+ball(F(sum(abs(z) for z in nums), den))))
    Slo, Shi = ball(S_P-S_error), ball(S_P+S_error)
    Qlo, Qhi = (Slo-ball(F(1, 4*n)))/2, (Shi-ball(F(1, 4*n)))/2
    assert Qlo > 0
    Hlo = 1/lam-lam*Shi-ball(T_P+T_error)/2
    Hhi = 1/lam-lam*Slo-ball(T_P-T_error)/2
    corners = [Hlo/Qlo, Hlo/Qhi, Hhi/Qlo, Hhi/Qhi]
    low = min(corners, key=float)
    high = max(corners, key=float)
    quot = bracket(low, high)
    for c in corners:
        assert ball(quot[0]) < c and ball(quot[1]) > c
    # Independently, construct the exact FINITE sine witness Im(P).
    odd = [-z for z in nums[:0:-1]]+[0]+nums[1:]
    squared_odd = flint.fmpz_poly(odd)**2
    Q_finite = F(sum(z*z for z in nums[1:]), 2*den*den)
    H_finite = F(-sum(int(squared_odd[2*B+a]) for a in A), 2*den*den)
    independent = sum(sum(nums[j]*nums[j+a] for j in range(1, B-a+1))
                      for a in A)
    independent -= F(sum(sum(nums[j]*nums[a-j] for j in range(1, a))
                         for a in A), 2)
    assert H_finite == independent/(den*den)
    Q_finite_error = upper(2*ball(Q_finite).sqrt()*ball(epsilon)+ball(epsilon)**2)
    H_finite_error = 2*n*Q_finite_error
    assert Hlo < ball(H_finite+H_finite_error)
    assert Hhi > ball(H_finite-H_finite_error)
    return dict(label=label, A=A, n=n, X=X, band=B, proposal_grid=grid,
        lambda_exact='2sqrt(n)', M_upper=str(M_upper),
        residual_squared_ball=str(residual2), L2_error_upper=str(epsilon),
        S_P_exact=str(S_P), S_error_upper=str(S_error),
        T_P_exact=str(T_P), T_error_upper=str(T_error),
        Q_bracket=bracket(Qlo, Qhi), H_bracket=bracket(Hlo, Hhi),
        infinite_Rayleigh_bracket=quot,
        infinite_Rayleigh_normalized_bracket=bracket(low/flint.arb(n).sqrt(),
                                                     high/flint.arb(n).sqrt()),
        infinite_energy_negative=bool(Hhi < 0),
        infinite_energy_positive=bool(Hlo > 0),
        finite_sine_numerators=nums[1:], finite_denominator=den,
        finite_Q_exact=str(Q_finite), finite_H_exact=str(H_finite),
        finite_to_infinite_Q_error_upper=str(Q_finite_error),
        finite_to_infinite_H_error_upper=str(H_finite_error),
        finite_Rayleigh_exact=str(H_finite/Q_finite),
        exact_finite_signed_moments_independently_matched=True,
        qualification='Finite tests of this explicit seed, not a universal Boolean bound.')


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    flint.ctx.prec = 384
    parser = argparse.ArgumentParser()
    parser.add_argument('--prefix', action='store_true',
                        help='Single predeclared coherent-prefix adversarial input, not a sweep')
    args = parser.parse_args()
    if args.prefix:
        saved = json.loads(Path('.research/experiments/forced_plateau_2026-10-20/results.json').read_text())
        row = next(r for r in saved['cases'] if r['t'] == 3)
        assert row['n'] == 337 and row['b'] == 243 and row['certificate']['verified']
        inputs = [(row['A'], F(row['certificate']['M_upper_rational']), 'forced_prefix_n337')]
    else:
        data = json.loads(Path('.research/experiments/boolean_projection_2026-10-21/results.json').read_text())
        inputs = [(row['A'], F(row['candidate_certificate']['M_upper']), f"projection_n{row['n']}")
                  for row in data['cases']]
    output = dict(host=socket.gethostname(), precision=flint.ctx.prec,
                  residual_method='Exact integer polynomial product; analytic inverse margin', cases=[])
    name = 'prefix' if args.prefix else 'results'
    path = Path(f'.research/experiments/zero_reciprocal_2026-10-21/{name}.json')
    path.parent.mkdir(parents=True, exist_ok=True)
    for A, upper_bound, label in inputs:
        result = one(A, upper_bound, label)
        output['cases'].append(result)
        path.write_text(json.dumps(output, indent=2)+'\n')
        print(json.dumps({k: result[k] for k in ('label', 'n', 'band',
            'infinite_Rayleigh_normalized_bracket', 'infinite_energy_negative',
            'infinite_energy_positive')}), flush=True)
    print(json.dumps(dict(status='PASS', output=str(path))), flush=True)


if __name__ == '__main__':
    main()
