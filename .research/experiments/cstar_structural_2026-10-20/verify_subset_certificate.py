"""Independent exact verifier of stored witnesses; no floating root proposal."""
from pathlib import Path
from itertools import combinations
import json
import sympy as s
HERE = Path(__file__).resolve().parent
A = (1, 2, 3, 4, 5, 6, 7, 9)
t = s.Symbol('t')
rows = json.loads((HERE / 'subset_certificate.json').read_text())
expected = {B for k in range(1, len(A)) for B in combinations(A, k)}
assert len(rows) == len(expected) == 254
assert {tuple(row['A']) for row in rows} == expected
P = s.Poly(2 + sum(s.chebyshevt(a, t) for a in A), t, domain=s.QQ)
Q, remainder = s.div(P, s.Poly(t + 1, t))
assert remainder.is_zero and P.eval(-1) == 0
assert Q.eval(-1) > 0 and Q.eval(0) > 0 and Q.eval(1) > 0
assert Q.count_roots(-1, 1) == 0
for row in rows:
    B = row['A']
    assert row['t_denominator'] > 0
    x = s.Rational(row['t_numerator'], row['t_denominator'])
    assert -1 <= x <= 1
    # Independent Chebyshev recurrence in exact rational arithmetic.
    T = [s.Integer(1), x]
    for k in range(2, max(B) + 1):
        T.append(2*x*T[-1] - T[-2])
    value = sum(T[a] for a in B)
    assert value < 0 and 2*value**2 > len(B)
weights = {a: s.Rational(8-a, 7) if a <= 7 else s.Integer(0) for a in A}
assert sum(weights.values()) == 4
assert all(0 <= w <= 1 for w in weights.values())
print('PASS: exact full-set Sturm certificate, all 254 proper-subset rational witnesses in [-1,1], and fractional half-mass feasibility.')
