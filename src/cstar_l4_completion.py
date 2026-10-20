"""Global Fourier L4 completion probes; execute on dirichlet via dirun.sh.

The convex QCP integrates a degree-B polynomial's fourth power exactly by
using an odd grid L>4B. Boolean primal witnesses are rounded and verified
by integer Laurent convolution. Dual L^(4/3) norms are numerical diagnostics.
This script does not claim a uniform theorem from finite tests.
"""
from __future__ import annotations

import argparse
import json
import math
import os
from pathlib import Path
import socket
import sys
import time

import gurobipy as gp
from gurobipy import GRB
import numpy as np
from scipy.fft import next_fast_len
from scipy.sparse import csr_matrix, hstack, eye


def exact_boolean_certificate(A, coefficients):
    denominator = 2 ** 16
    B = len(coefficients)
    positive = [int(round(float(x) * denominator)) for x in coefficients]
    for a in A:
        positive[a - 1] = denominator
    z = np.array(positive[::-1] + [0] + positive, dtype=np.int64)
    bound = sum(abs(int(t)) for t in z) ** 2
    conv = np.convolve(z, z) if bound < 2 ** 63 else np.convolve(z.astype(object), z.astype(object))
    Qnum = sum(int(t) ** 2 for t in z)
    fourth_num = sum(int(t) ** 2 for t in conv)
    N = 2 * len(A)
    Hnum = 0
    for a in A:
        Hnum += 2 * sum(int(t) * int(u) for t, u in zip(z[a:], z[:-a]))
    Q, H = Qnum / denominator ** 2, Hnum / denominator ** 2
    coupling = N
    discriminant = math.hypot(H, 2 * math.sqrt(Q) * coupling)
    kfloat = (2 * coupling ** 2 / (discriminant + H)
              if discriminant + H > 0 else (discriminant - H) / (2 * Q))
    scale = 10 ** 6
    knum = max(1, math.floor(kfloat * scale))
    determinant = (knum * Hnum * scale + knum ** 2 * Qnum
                   - coupling ** 2 * denominator ** 2 * scale ** 2)
    assert determinant < 0
    return dict(denominator=denominator, positive_coefficients=positive,
                norm_squared_numerator=Qnum, fourth_power_numerator=fourth_num,
                energy_numerator=Hnum,
                fourth_power_over_N2=float(fourth_num / (denominator ** 4 * N ** 2)),
                K_lower_rational=[knum, scale], determinant_numerator=determinant,
                R_lower_float=knum / scale / math.sqrt(2 * N),
                verification='integer Laurent convolution and rational negative determinant')


def solve(tag, indices, values, B, tl, lower_bounds_only=False):
    start = time.time()
    indices, values = np.asarray(indices, dtype=int), np.asarray(values, dtype=float)
    # A zero data coefficient is an unused frequency, hence remains free.
    # Prescribing it to zero would restrict the primal and enlarge the dual space.
    nonzero = values != 0
    indices, values = indices[nonzero], values[nonzero]
    assert np.all(indices > 0) and len(set(indices)) == len(indices) and B >= max(indices)
    N = float(2 * (values @ values))
    normalization = math.sqrt(N)
    L = 4 * B + 1
    half = L // 2 + 1
    angles = 2 * np.pi * np.arange(half) / L
    C = 2 * np.cos(np.outer(angles, np.arange(1, B + 1)))
    weights = np.full(half, 2 / L)
    weights[0] = 1 / L
    model = gp.Model(tag)
    model.Params.OutputFlag = 0
    model.Params.Threads = int(os.environ.get('CHOWLA_WORKERS', '2'))
    model.Params.TimeLimit = tl
    model.Params.BarQCPConvTol = 1e-8
    coefficients = model.addMVar(B, lb=-GRB.INFINITY, name='coefficients')
    q = model.addMVar(half, lb=-GRB.INFINITY, name='q')
    y = model.addMVar(half, lb=0, name='q_squared')
    for a, val in zip(indices, values):
        coefficients[int(a) - 1].LB = float(val) / normalization
        if not lower_bounds_only:
            coefficients[int(a) - 1].UB = float(val) / normalization
    variables = gp.MVar.fromlist(coefficients.tolist() + q.tolist())
    model.addMConstr(hstack([csr_matrix(C), -eye(half)], format='csr'), variables, '=', np.zeros(half))
    qvars, yvars = q.tolist(), y.tolist()
    for j in range(half):
        model.addQConstr(qvars[j] * qvars[j] <= yvars[j])
    model.setObjective(gp.quicksum(float(weights[j]) * yvars[j] * yvars[j] for j in range(half)), GRB.MINIMIZE)
    model.optimize()
    row = dict(tag=tag, X=int(max(indices)), B=B, grid=L,
               status=int(model.Status), gurobi=list(gp.gurobi.version()),
               seconds=time.time() - start, sol_count=int(model.SolCount),
               constraint_kind='lower_bounds' if lower_bounds_only else 'equalities')
    if not model.SolCount:
        print(json.dumps(row), flush=True)
        return row
    c = np.asarray(coefficients.X) * normalization
    # Fourth-power quadrature is exact for the returned polynomial, up to float arithmetic.
    qvalues = C @ c
    fourth = float(np.dot(weights, qvalues ** 4))
    Q = float(2 * (c @ c))
    dense_grid = next_fast_len(max(64 * B, 256))
    z = np.zeros(dense_grid)
    z[1:B + 1] = c
    z[-B:] = c[::-1]
    qfull = np.fft.ifft(z).real * dense_grid
    cube_fourier = np.fft.fft(qfull ** 3).real / dense_grid
    # Project q^3 onto the prescribed-frequency space plus its free constant.
    dual_fourier = np.zeros(dense_grid)
    dual_fourier[0] = cube_fourier[0]
    dual_selected = cube_fourier[indices]
    if lower_bounds_only:
        # The inequality problem only permits nonnegative multipliers.
        # Clipping makes this a feasible dual polynomial even with residuals.
        dual_selected = np.maximum(dual_selected, 0)
    dual_fourier[indices] = dual_selected
    dual_fourier[-indices] = dual_selected
    dual_values = np.fft.ifft(dual_fourier).real * dense_grid
    dual_norm = float(np.mean(np.abs(dual_values) ** (4 / 3)) ** (3 / 4))
    dual_pairing = float(2 * values @ dual_selected)
    dual_lower = dual_pairing / dual_norm
    data_fourier = np.zeros(dense_grid)
    data_fourier[indices], data_fourier[-indices] = values, values
    Dvalues = np.fft.ifft(data_fourier).real * dense_grid
    Kgrid = float(-np.min(Dvalues))
    row.update(N=N, norm_squared=Q, fourth_power=fourth,
               fourth_power_over_N2=fourth / N ** 2,
               L4_over_sqrt_N=fourth ** .25 / math.sqrt(N),
               dual_L4_lower_over_sqrt_N_float=dual_lower / math.sqrt(N),
               dual_primal_ratio_float=dual_lower / fourth ** .25,
               negative_dual_support_coefficients=int(np.count_nonzero(cube_fourier[indices] < -1e-7)),
               selected_coefficient_max_slack=float(np.max(c[indices - 1] - values)),
               input_R_grid_float=Kgrid / math.sqrt(2 * N),
               support=indices.tolist(), values=values.tolist(), coefficients=c.tolist(),
               qualification='convex-QCP numerical output; dual integral and grid minima uncertified')
    if np.all(values == 1) and not lower_bounds_only:
        row['exact_primal'] = exact_boolean_certificate(indices.tolist(), c)
    print(json.dumps({k: row[k] for k in row if k not in ['support', 'values', 'coefficients', 'exact_primal']}), flush=True)
    model.dispose()
    return row


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Run on dirichlet through src/dirun.sh')
    parser = argparse.ArgumentParser()
    parser.add_argument('--tl', type=float, default=30)
    parser.add_argument('--output', type=Path, default=Path('.research/experiments/global_l4_2026-10-20/results.json'))
    parser.add_argument('--suite', choices=['smoke', 'packet', 'singer'], default='smoke')
    parser.add_argument('--case', help='Run only the named case in the suite')
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    cases = []
    if args.suite == 'smoke':
        cases += [('hereditary_8', np.array([1,2,3,4,5,6,7,9]), None)]
        for n in [16, 32, 64]:
            cases.append((f'interval_{n}', np.arange(1, n + 1), None))
        for name, record in json.loads(Path('examples/construct/N50_certified.json').read_text()).items():
            cases.append((name, np.array(record['A']), None))
        rng = np.random.default_rng(20261020)
        a = np.arange(1, 257)
        cases.append(('taper_boolean_256', a[rng.random(256) < .3 * (1 - a / 257)], None))
    elif args.suite == 'packet':
        sys.path.insert(0, 'src')
        from e83_escape_binarise import escape, wstar
        w = wstar()
        for X in [64, 128, 256, 512]:
            p, r, c, J, _ = escape(X, .6, np.random.default_rng(X), w)
            cases.append((f'fractional_packet_{X}', np.arange(1, X + 1), c))
            rng = np.random.default_rng(1000 + X)
            A = np.arange(1, X + 1)[rng.random(X) < p]
            cases.append((f'boolean_profile_{X}', A, None))
    else:
        sys.path.insert(0, 'src')
        from singer import singer
        from bu import A_of_S
        for order in [5, 7, 11]:
            D, v = singer(order)
            S = [d - (v - 1) // 2 for d in D]
            A = np.array(A_of_S(S))
            cases.append((f'full_singer_bu_q{order}', A, None))
    rows = []
    for tag, A, values in cases:
        if args.case and tag != args.case:
            continue
        if values is None:
            values = np.ones(len(A))
        B = 2 * int(max(A))
        rows.append(solve(tag, A, values, B, args.tl))
        args.output.write_text(json.dumps(dict(suite=args.suite, cases=rows), separators=(',', ':')) + '\n')
    if not rows:
        parser.error('no cases matched --case')


if __name__ == '__main__':
    main()
