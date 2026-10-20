"""Independent exact Laurent verification; standard library only.

Run on dirichlet. Verifies feasible polynomials, not QCP optimality or the
numerical dual norm. Distinct implementation: dictionary pair convolution.
"""
from collections import defaultdict
from pathlib import Path
import argparse
import json
import socket


def verify(row):
    saved = row['exact_primal']
    denominator = saved['denominator']
    positive = saved['positive_coefficients']
    q = {s: c for i, c in enumerate(positive, start=1) if c for s in [-i, i]}
    assert 0 not in q
    assert all(q[int(a)] == denominator and q[-int(a)] == denominator for a in row['support'])
    pair = defaultdict(int)
    for i, a in q.items():
        for j, b in q.items():
            pair[i + j] += a * b
    Qnum = sum(c * c for c in q.values())
    Hnum = 2 * sum(pair[int(a)] for a in row['support'])
    fourth = sum(c * c for c in pair.values())
    assert Qnum == saved['norm_squared_numerator']
    assert Hnum == saved['energy_numerator']
    assert fourth == saved['fourth_power_numerator']
    N = 2 * len(row['support'])
    knum, kden = saved['K_lower_rational']
    determinant = knum * Hnum * kden + knum * knum * Qnum - N * N * denominator * denominator * kden * kden
    assert determinant == saved['determinant_numerator'] < 0
    return dict(tag=row['tag'], positive_frequencies=len(row['support']),
                interpolation_verified=True, fourth_power_verified=True,
                negative_determinant_verified=True,
                fourth_power_over_N2=saved['fourth_power_over_N2'],
                R_lower_float=saved['R_lower_float'])


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Run on dirichlet through src/dirun.sh')
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+', type=Path)
    parser.add_argument('--output', type=Path, default=Path('.research/experiments/global_l4_2026-10-20/verification.json'))
    args = parser.parse_args()
    checks = []
    for path in args.files:
        for row in json.loads(path.read_text())['cases']:
            if 'exact_primal' in row:
                checks.append(dict(file=str(path), **verify(row)))
    out = dict(status='exact feasible-witness checks; no universal theorem or optimality assertion', checks=checks)
    args.output.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
