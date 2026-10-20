"""Exact checks for the global four-wise selector argument and its 3-wise limit.

Standard library only; run through dirun.sh. The finite checks corroborate
the accompanying all-size paper derivations; they do not replace them.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import json
import socket


def fourth(frequencies, z):
    coefficients = {s: v for a, v in zip(frequencies, z) if v for s in [-a, a]}
    square = defaultdict(F)
    for a, u in coefficients.items():
        for b, v in coefficients.items():
            square[a + b] += u * v
    return sum(v * v for v in square.values())


def independent_check(p):
    a = [1, 2, 4, 7]
    expected = F(0)
    for bits in product([0, 1], repeat=len(p)):
        mass = F(1)
        for bit, prob in zip(bits, p):
            mass *= prob if bit else 1 - prob
        z = [(bit - prob) / (1 - prob) for bit, prob in zip(bits, p)]
        expected += mass * fourth(a, z)
    variance = [prob / (1 - prob) for prob in p]
    fourth_marginal = [prob + prob ** 4 / (1 - prob) ** 3 for prob in p]
    formula = 6 * sum(fourth_marginal) + 24 * sum(variance[i] * variance[j] for i, j in combinations(range(len(p)), 2))
    assert expected == formula
    return dict(p=list(map(str, p)), expected_fourth=str(expected), formula=str(formula))


def parity_check(m):
    a = list(range(1, m + 1))
    rows = [bits for bits in product([0, 1], repeat=m) if sum(bits) % 2 == 0]
    for k in range(1, m):
        for ids in combinations(range(m), k):
            assert sum((-1) ** sum(bits[i] for i in ids) for bits in rows) == 0
    expected = sum(fourth(a, [F((-1) ** bit) for bit in bits]) for bits in rows) / len(rows)
    baseline = 12 * m * m - 6 * m
    if m == 5:
        assert expected == baseline
    elif m == 4:
        assert expected == baseline + 48
    return dict(m=m, independence_order=m-1, expected_fourth=str(expected), fourwise_formula=baseline)


def cube_check(d):
    m = 2 ** d
    Q = 5 ** d
    a = [Q + sum(((b >> i) & 1) * 5 ** i for i in range(d)) for b in range(m)]
    assert 4 * max(a) < 5 * Q
    labels = [m + b for b in range(m)]
    for ids in combinations(range(m), 2):
        assert labels[ids[0]] ^ labels[ids[1]]
    for ids in combinations(range(m), 3):
        assert labels[ids[0]] ^ labels[ids[1]] ^ labels[ids[2]]
    for y in range(2 * m):
        z = [F((-1) ** ((label & y).bit_count() % 2)) for label in labels]
        assert fourth(a, z) == 6 * 6 ** d
    return dict(d=d, ambient_positive_frequencies=m, outcomes=2*m,
                fourth_every_outcome=6*6**d,
                fourwise_baseline=12*m*m-6*m,
                fourth_over_m_squared=str(F(6*6**d, m*m)),
                frequencies=a,
                qualification='3-wise selector countercontrol, with a separate linear global lower bound')


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Run on dirichlet through src/dirun.sh')
    success = 1 - F(4, 64) - (48 + F(12, 64)) / 128
    assert success == F(1149, 2048) > F(1, 2)
    # 8*sqrt(2)*(sqrt(2)/20)*(1+sqrt(2)/20)
    # = 4/5+sqrt(2)/25 < 22/25 < 1.
    assert F(22, 25) < 1
    out = dict(status='exact finite moment checks; general result uses the paper proof',
               independent=[independent_check([F(1,2)]*4), independent_check([F(1,3),F(1,5),F(1,2),F(2,5)])],
               parity=[parity_check(4), parity_check(5)],
               cubes=[cube_check(d) for d in range(1, 6)],
               probability_lower_at_mu64=str(success))
    path = Path('.research/experiments/global_l4_2026-10-20/fourwise_checks.json')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
