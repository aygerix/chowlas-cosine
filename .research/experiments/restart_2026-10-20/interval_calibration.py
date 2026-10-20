"""Exact interval obstruction and explicit repair; no universal Chowla claim.

Uses only the Python standard library. Checks both direct Laurent constant
terms and closed formulas, and writes a compact JSON receipt beside the script.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json


def coefficients(n):
    q = {s: F(1) for a in range(1, n + 1) for s in [-a, a]}
    for k in range(1, n + 1):
        c = -F(1, 2) + F(15, 2 * n) * (k - F(n + 1, 2))
        q[n + k] = q[-n - k] = c
    return q


def direct(n):
    q = coefficients(n)
    S = [s for a in range(1, n + 1) for s in [-a, a]]
    norm = sum(c * c for c in q.values())
    energy = sum(c * q.get(w + s, 0) for w, c in q.items() for s in S)
    return norm, energy


def formulas(n):
    return F(95 * n, 8) - F(75, 8 * n), -F(111 * n, 8) + F(5, 2) + F(75, 8 * n)


def verify_saved_witnesses(path):
    """Rebuild Laurent constant terms without importing the optimizer/matrices."""
    data = json.loads(path.read_text())
    C = F(data['summary']['constant'])
    passed = 0
    for row in data['cases']:
        w = row['exact_witness']
        q = dict(w['nonzero_coefficients'])
        denominator = w['denominator']
        S = {s for a in row['A'] for s in [-a, a]}
        allowed = (S | {a + b for a in S for b in S}) - {0}
        assert set(q) <= allowed
        assert all(q[s] == denominator for s in S)
        norm = sum(v * v for v in q.values())
        energy = sum(v * q.get(i + s, 0) for i, v in q.items() for s in S)
        assert norm == w['norm_numerator'] and energy == w['energy_numerator']
        assert w['norm_bound_verified'] == (norm <= C * len(S) * denominator ** 2)
        assert w['energy_bound_verified'] == (energy <= 0 or energy ** 2 <= C ** 2 * len(S) ** 3 * denominator ** 4)
        passed += w['norm_bound_verified'] and w['energy_bound_verified']
    return dict(file=path.name, count=len(data['cases']), exact_feasible_witnesses=passed)


def main():
    checked = []
    for n in list(range(1, 25)) + [32, 64, 128]:
        norm, energy = direct(n)
        assert (norm, energy) == formulas(n)
        assert norm <= F(95, 16) * (2 * n)
        assert energy < 0
        checked.append(n)
    # For n=128, B_E is two complete graphs, hence B_E >= -I.
    # h=3n(n-1), ||g||²=2 sum j². Exterior norm² <= N=256.
    n = 128
    h = 3 * n * (n - 1)
    g_squared = n * (n + 1) * (2 * n + 1) // 3
    radicand = 2 * n * g_squared
    ceiling = isqrt(radicand) + 1
    assert (ceiling - 1) ** 2 < radicand < ceiling ** 2
    lower_bound = h - 2 * n - 2 * ceiling
    assert isqrt(2 * n) ** 2 == 2 * n
    target = 2 * (2 * n) * isqrt(2 * n)
    assert lower_bound > target
    out = dict(status='exact integer/rational identity checks, accompanying paper argument required',
               direct_formula_checks=checked,
               interval_128_C2_obstruction=dict(N=2*n, h=h, cross_vector_norm_squared=g_squared,
                  radicand=radicand, square_root_upper_bound=ceiling,
                  strict_energy_lower_bound=lower_bound, proposed_energy_upper_bound=target),
               explicit_all_interval_repair=dict(norm_ratio_upper_bound='95/16',
                  norm_formula='95*n/8 - 75/(8*n)',
                  energy_formula='-111*n/8 + 5/2 + 75/(8*n)'),
               saved_witness_verification=[verify_saved_witnesses(p) for p in
                  sorted(Path(__file__).parent.glob('fixed_interior_C*.json'))])
    Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
