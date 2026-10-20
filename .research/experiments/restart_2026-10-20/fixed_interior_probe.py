"""Bounded fixed-interior test; numerical optimization, exact feasible witnesses.

Run from the repo root with .venv/bin/python. Existing archived outputs are
read-only. A failed floating optimization is not a certified counterexample.
"""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import argparse
import json
import math
from pathlib import Path
import platform
import time
from fractions import Fraction

import numpy as np
import scipy
from scipy.linalg import eigh
from scipy.optimize import brentq

ROOT = Path(__file__).resolve().parents[3]


def trust_region(H, interior, radius_squared):
    """Minimize (s+r)'H(s+r), r supported off interior, ||r||^2<=R^2.

    Eigenbasis secular equation, with the negative-eigenspace hard case.
    The dual value is a floating diagnostic only.
    """
    s = np.zeros(len(H))
    s[interior] = 1
    exterior = np.flatnonzero(~np.isin(np.arange(len(H)), interior))
    h = float(s @ H @ s)
    if not len(exterior):
        return s, h, h, 0.0
    B = H[np.ix_(exterior, exterior)]
    g = (H @ s)[exterior]
    lam, V = eigh(B)
    z = V.T @ g
    floor = max(0.0, -float(lam[0]))
    tol = 1e-10 * max(1.0, np.linalg.norm(B, 2), np.linalg.norm(g))
    den0 = lam + floor
    singular = den0 <= tol
    y0 = np.zeros(len(lam))
    y0[~singular] = -z[~singular] / den0[~singular]
    hard = np.linalg.norm(z[singular]) <= tol and y0 @ y0 <= radius_squared
    if hard:
        shift = floor
        y = y0
        if floor > tol:
            y[0] += math.sqrt(max(0.0, radius_squared - y @ y))
    else:
        def squared_norm(shift):
            return np.sum((z / (lam + shift)) ** 2)
        lo = floor + 1e-12 * max(1.0, floor)
        hi = max(lo + 1.0, 2 * np.linalg.norm(g) / math.sqrt(radius_squared) + floor)
        while squared_norm(hi) > radius_squared:
            hi *= 2
        shift = brentq(lambda t: squared_norm(t) - radius_squared, lo, hi,
                       xtol=1e-12, rtol=1e-13)
        y = -z / (lam + shift)
    q = s.copy()
    q[exterior] = V @ y
    value = float(q @ H @ q)
    active = lam + shift > tol
    dual = h - shift * radius_squared - np.sum(z[active] ** 2 / (lam[active] + shift))
    return q, value, float(dual), float(abs(value - dual))


def exact_witness(A, W, q, constant):
    """Round a slightly shortened exterior vector and check integer inequalities."""
    S = set(A) | {-a for a in A}
    N = len(S)
    denominator = 2 ** 16
    coeff = {int(w): denominator if w in S else int(round(0.999 * q[i] * denominator))
             for i, w in enumerate(W)}
    assert coeff.get(0, 0) == 0
    norm_numerator = sum(v * v for v in coeff.values())
    energy_numerator = sum(v * coeff.get(w + a, 0)
                           for w, v in coeff.items() for a in S)
    ca, cb = constant.numerator, constant.denominator
    norm_ok = cb * norm_numerator <= ca * N * denominator ** 2
    energy_ok = (energy_numerator <= 0 or
                 cb ** 2 * energy_numerator ** 2 <= ca ** 2 * N ** 3 * denominator ** 4)
    return dict(denominator=denominator, norm_numerator=norm_numerator,
                energy_numerator=energy_numerator, norm_bound_verified=norm_ok,
                energy_bound_verified=energy_ok,
                nonzero_coefficients=[[w, v] for w, v in coeff.items() if v])


def run(A, tag, constant):
    A = sorted(set(int(a) for a in A))
    S = set(A) | {-a for a in A}
    N = len(S)
    W = np.array(sorted((S | {a + b for a in S for b in S}) - {0}), dtype=int)
    H = np.isin(W[:, None] - W[None, :], list(S)).astype(float)
    interior = np.flatnonzero(np.isin(W, list(S)))
    q, value, dual, gap = trust_region(H, interior, (float(constant) - 1) * N)
    witness = exact_witness(A, W, q, constant)
    return dict(tag=tag, A=A, N=N, punctured_W2_size=len(W),
                minimum_energy_over_N32_float=value / N ** 1.5,
                dual_over_N32_float=dual / N ** 1.5,
                primal_dual_gap_over_N32_float=gap / N ** 1.5,
                exact_witness=witness)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--box', type=int, default=10)
    parser.add_argument('--constant', type=Fraction, default=Fraction(2))
    parser.add_argument('--output', type=Path, default=Path(__file__).with_suffix('.json'))
    args = parser.parse_args()
    if args.constant <= 1:
        parser.error('--constant must exceed 1')
    started = time.time()
    rows = []
    for mask in range(1, 2 ** args.box):
        rows.append(run([j + 1 for j in range(args.box) if mask >> j & 1], f'box_{mask}', args.constant))
    for n in [16, 32, 64, 128]:
        rows.append(run(range(1, n + 1), f'interval_{n}', args.constant))
    for name, record in json.loads((ROOT / 'examples/construct/N50_certified.json').read_text()).items():
        rows.append(run(record['A'], name, args.constant))
    rng = np.random.default_rng(20261020)
    for j in range(24):
        X = 24 + 3 * j
        a = np.arange(1, X + 1)
        p = 0.2 if j % 2 else 0.6 * (1 - a / (X + 1))
        A = a[rng.random(X) < p]
        if len(A):
            rows.append(run(A, f'seeded_{j}', args.constant))
    worst = sorted(rows, key=lambda r: r['minimum_energy_over_N32_float'], reverse=True)[:10]
    failures = [r['tag'] for r in rows if not (r['exact_witness']['norm_bound_verified']
                                              and r['exact_witness']['energy_bound_verified'])]
    summary = dict(status='finite tests; only passing integer witness checks establish feasibility',
                   constant=str(args.constant),
                   support_count=len(rows), exhaustive_box=args.box,
                   exact_witness_failures=failures,
                   largest_minimum_energy_over_N32_float=worst[0]['minimum_energy_over_N32_float'],
                   worst_tags=[r['tag'] for r in worst],
                   max_primal_dual_gap_over_N32_float=max(r['primal_dual_gap_over_N32_float'] for r in rows),
                   seconds=time.time() - started,
                   versions=dict(python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__))
    args.output.write_text(json.dumps(dict(summary=summary, worst_cases=worst, cases=rows), separators=(',', ':')) + '\n')
    print(json.dumps(summary, indent=2))
    print('Worst cases:', [(r['tag'], r['N'], r['minimum_energy_over_N32_float']) for r in worst])


if __name__ == '__main__':
    main()
