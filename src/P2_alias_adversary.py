"""One finite-alias adversary for the full two-direction P2 determinant.

All admissible supports have an exact difference-square M<=17/2
certificate. FFTs propose determinant signs only. A possible falsifier
is checked by exact finite recurrences and an infinite inverse residual.
"""
from collections import Counter
from fractions import Fraction as F
import json
import math
from pathlib import Path
import platform
import socket
import time


def differences(points):
    raw = [b-a for i, a in enumerate(points) for b in points[i+1:]]
    assert all(a > 0 for a in raw) and len(raw) == len(set(raw))
    return sorted(raw)


def evaluate(A, grid):
    import numpy as np
    n = len(A)
    spectral = np.zeros(grid, dtype=np.complex128)
    spectral[A] = 1
    values = np.fft.ifft(spectral, norm='forward')
    lam = 2*math.sqrt(n)
    reciprocal = 1/(lam+values)
    q = reciprocal.imag
    H = float(np.mean(2*values.real*q*q))
    Q = float(np.mean(q*q))
    C2 = float(np.mean(values*values*reciprocal.conjugate()).real)
    C2_cross = float(-4*np.mean(values.real*values.imag**2/abs(lam+values)**2))
    sums = Counter(a+b for a in A for b in A)
    t = sum(sums[a] for a in A)
    phi = 2*t*H-C2*C2
    scale = 2*t*abs(H)+C2*C2
    assert t > 0 and Q > 0 and scale > 0
    return dict(grid=grid, t_exact=t, H_grid=H, Q_grid=Q,
                C2_grid=C2, C2_cross_grid=C2_cross,
                cross_identity_discrepancy=abs(C2-C2_cross),
                P2_violation_grid=phi,
                scaled_P2_violation_grid=phi/scale,
                normalized_reciprocal_energy_grid=H/(Q*math.sqrt(n)))


def certify_possible_falsifier(A, label):
    import flint
    from cstar_zero_reciprocal import one, ball, bracket
    flint.ctx.prec = 384
    exact = one(A, F(17, 2), label, band_multiple=32)
    n, X = len(A), max(A)
    lam = 2*flint.arb(n).sqrt()
    coef = [1/lam]
    for j in range(1, 2*X+1):
        coef.append(-sum((coef[j-a] for a in A if a <= j), flint.arb(0))/lam)
    sums = Counter(a+b for a in A for b in A)
    t = sum(sums[a] for a in A)
    C1 = sum((coef[a] for a in A), flint.arb(0))
    C2 = sum((count*coef[j] for j, count in sums.items()), flint.arb(0))
    remainder = Counter(a+b-c for a in A for b in A for c in A
                        if c != a and c != b and a+b > c)
    RA = sum((count*coef[j] for j, count in remainder.items()), flint.arb(0))
    identity_error = lam*C2+t/lam+(2*n-1)*C1+RA
    assert abs(identity_error) < flint.arb('1e-70')
    Hlo, Hhi = map(F, exact['H_bracket'])
    lower_expression = 2*t*ball(Hlo)-C2*C2
    upper_expression = 2*t*ball(Hhi)-C2*C2
    return dict(reciprocal=exact, t_exact=t,
                C1_ball=str(C1), C2_ball=str(C2), signed_residual_ball=str(RA),
                Boolean_recurrence_error_ball=str(identity_error),
                P2_violation_bracket=bracket(lower_expression, upper_expression),
                P2_refuted=bool(lower_expression > 0),
                S0_refuted=bool(ball(Hlo) > 0),
                certificate_status='exact coefficient counts, rigorous balls and infinite inverse residual')


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    import numpy as np
    from singer import singer, is_perfect_difference_set
    started = time.monotonic()
    U, modulus = singer(11)
    assert is_perfect_difference_set(U, modulus)
    U = sorted(U)
    V = [0, 1, 4, 9, 11]
    DA, DB = differences(U), differences(V)
    assert len(U) == 12 and len(V) == 5 and len(DA) == 66 and len(DB) == 10
    rows, excluded = [], []
    for dilation in range(1, 129):
        second = [dilation*a for a in DB]
        if set(DA) & set(second):
            excluded.append(dilation)
            continue
        A = sorted(DA+second)
        assert len(A) == len(set(A)) == 76
        assert F(17, 2)**2 < len(A)
        row = dict(L=dilation, A=A, n=len(A), X=max(A),
                   M_upper_exact='17/2', lambda_exact='2sqrt(76)',
                   actual_lowM_proved_by_two_difference_squares=True)
        row.update(evaluate(A, 1 << 16))
        rows.append(row)
    assert rows
    best_det = max(rows, key=lambda r: r['scaled_P2_violation_grid'])
    best_H = max(rows, key=lambda r: r['normalized_reciprocal_energy_grid'])
    selected = {row['L']: row for row in (best_det, best_H)}
    checks, certified = [], []
    for dilation, row in selected.items():
        refined = evaluate(row['A'], 1 << 17)
        checks.append(dict(L=dilation, refined=refined,
                           determinant_change=refined['P2_violation_grid']-row['P2_violation_grid'],
                           H_change=refined['H_grid']-row['H_grid']))
        # A possible falsifier gets a global infinite-reciprocal check.
        # Robustly negative proposals are not promoted to finite exclusions.
        if (refined['P2_violation_grid'] >= -1e-6
                or refined['normalized_reciprocal_energy_grid'] >= -1e-6):
            certified.append(dict(L=dilation, result=certify_possible_falsifier(
                row['A'], f'P2_alias_L{dilation}')))
    out = dict(status='PASS', host=socket.gethostname(), python=platform.python_version(),
        numpy=np.__version__, elapsed_seconds=time.monotonic()-started,
        fixed_family=dict(Singer_prime=11, Singer_modulus=modulus, U=U, V=V,
                          U_differences=DA, V_differences=DB,
                          L_inclusive=[1,128], only_disjoint_unions=True,
                          cardinality=76, exact_M_upper='17/2'),
        evaluated_cases=rows, excluded_for_overlap=excluded,
        best_grid_determinant_L=best_det['L'], best_grid_H_L=best_H['L'],
        independent_grid_refinements=checks, possible_falsifier_certificates=certified,
        P2_refuted=any(c['result']['P2_refuted'] for c in certified),
        S0_refuted=any(c['result']['S0_refuted'] for c in certified),
        qualification=('One bounded adversarial family; FFTs only propose signs. '
            'All supports have exact all-circle lowM certificates, but robustly negative '
            'grid values are not a universal or finite-class determinant proof. '
            'No enlarged search or GPU deployment follows from a failed pilot.'))
    dest = Path('.research/experiments/P2_alias_2026-10-23/results.json')
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(dict(status='PASS', cases=len(rows), overlap_exclusions=len(excluded),
        best_L=best_det['L'], best_P2_grid=best_det['P2_violation_grid'],
        best_scaled_P2_grid=best_det['scaled_P2_violation_grid'],
        best_H_L=best_H['L'], best_normalized_H_grid=best_H['normalized_reciprocal_energy_grid'],
        P2_refuted=out['P2_refuted'], S0_refuted=out['S0_refuted'], artifact=str(dest))), flush=True)


if __name__ == '__main__':
    main()
