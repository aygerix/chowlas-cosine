"""Bounded construction pilot: correlated Boolean Fourier projection.

The two projections are exact for the discrete Euclidean feasibility
problem, but Douglas--Rachford has no claimed global convergence here.
Floating shadows propose sets; Arb DFT and Taylor errors certify their
ENTIRE-circle bounds. All computation runs on Dirichlet. No GPU use.
"""
from fractions import Fraction as F
from itertools import combinations
import json
import math
from pathlib import Path
import socket
import time

import flint
import numpy as np
from singer import singer, is_perfect_difference_set
from bu import A_of_S


def values_of(A, grid):
    z = np.zeros(grid//2+1, dtype=np.complex128)
    z[np.asarray(A)] = .5
    return np.fft.irfft(z, n=grid, norm='forward')


def project_boolean(values, X, n):
    rows = np.atleast_2d(values)
    scores = np.fft.rfft(rows, axis=1, norm='forward')[:, 1:X+1].real
    indices = np.argpartition(scores, X-n, axis=1)[:, X-n:]+1
    spectrum = np.zeros((len(rows), rows.shape[1]//2+1), dtype=np.complex128)
    np.put_along_axis(spectrum, indices, .5, axis=1)
    return np.fft.irfft(spectrum, n=rows.shape[1], axis=1, norm='forward'), indices


def controls():
    rng = np.random.default_rng(20261021)
    X, n, grid = 5, 2, 128
    raw = rng.normal(size=grid)
    raw = (raw+raw[(-np.arange(grid)) % grid])/2
    projected, indices = project_boolean(raw, X, n)
    chosen = float(np.mean((projected[0]-raw)**2))
    exhaustive = min(float(np.mean((values_of(A, grid)-raw)**2))
                     for A in combinations(range(1, X+1), n))
    assert abs(chosen-exhaustive) < 1e-12
    # Differences of {0,1,4}: exact square identity gives M<=3/2.
    A = [1, 3, 4]
    v = values_of(A, grid)
    positive = np.maximum(v, -1.5)
    shadow, support = project_boolean(2*positive-v, 4, 3)
    assert sorted(support[0].tolist()) == A
    assert np.max(np.abs(shadow[0]-positive)) < 1e-12
    return dict(nearest_Boolean_exhaustive_match=True,
                exact_difference_square_fixed_point=True,
                no_global_convergence_asserted=True)


def proposal(prime, iterations=2000, batch=4):
    D, modulus = singer(prime)
    assert is_perfect_difference_set(D, modulus)
    S = sorted(d-modulus//2 for d in D)
    seed = A_of_S(S)
    X, n = max(seed), len(seed)
    assert X >= 2*n
    grid = 1 << (16*X).bit_length()
    target = 9*math.sqrt(n)/20
    rng = np.random.default_rng(20261021+prime)
    v = np.zeros((batch, grid))
    v[0] = values_of(seed, grid)
    # A scaled Fejer profile has mass n*X/(X+1) and an O(1) negative
    # floor before Boolean projection. It is an initialization only.
    fractional = 2*n/(X+1)*(1-np.arange(1, X+1)/(X+1))
    assert fractional.max() <= 1
    for j in range(1, batch):
        spectrum = np.zeros(grid//2+1, dtype=np.complex128)
        perturbation = 0 if j == 1 else rng.normal(0, .2, X)
        spectrum[1:X+1] = (fractional+perturbation)/2
        v[j] = np.fft.irfft(spectrum, n=grid, norm='forward')
    seed_grid = -float(v[0].min())
    best, best_A, best_iter, best_replica = seed_grid, seed, -1, 0
    history = []
    start = time.monotonic()
    for step in range(iterations):
        p = np.maximum(v, -target)
        shadow, supports = project_boolean(2*p-v, X, n)
        costs = -shadow.min(axis=1)
        chosen = int(np.argmin(costs))
        if costs[chosen] < best-1e-10:
            best = float(costs[chosen])
            best_A = sorted(supports[chosen].tolist())
            best_iter, best_replica = step, chosen
        residual = np.sqrt(np.mean((shadow-p)**2, axis=1))
        v += shadow-p
        assert np.all(np.isfinite(v))
        if step % 200 == 0 or best <= target:
            history.append(dict(step=step, best_grid_M=best,
                best_R_grid=best/math.sqrt(n), min_projection_residual=float(residual.min())))
        if best <= target:
            break
    return dict(prime_seed=prime, n=n, X=X, proposal_grid=grid,
        target_ratio='9/20', target_M_float=target, iterations=step+1,
        batch=batch, seed=20261021+prime, seed_A=seed, A=best_A,
        seed_grid_M=seed_grid, proposed_grid_M=best,
        best_iteration=best_iter, best_replica=best_replica,
        seconds=time.monotonic()-start, history=history,
        grid_feasible_at_target=(best <= target),
        support_free_after_initialization=True,
        status='FLOATING proposal only; global certification follows')


def ball(rational):
    rational = F(rational)
    return flint.arb(rational.numerator)/rational.denominator


def certify(A):
    n, X = len(A), max(A)
    assert len(set(A)) == n and min(A) > 0
    flint.ctx.prec = 96
    sumsq = sum(a*a for a in A)
    # Choose a grid with a rigorous second-order error below1/100.
    grid = 1
    while F(242*sumsq, 49*grid*grid) > F(1, 100) or grid <= X:
        grid *= 2
    z = [flint.acb(0)]*grid
    for a in A:
        z[a] = flint.acb(1)
    vals = flint.acb.dft(z)
    j = max(range(grid), key=lambda k: -float(vals[k].real.mid()))
    hint = F(math.ceil(-float(vals[j].real.mid())*4096)+1, 4096)
    assert all(t.real+ball(hint) > 0 for t in vals)
    remainder = F(242*sumsq, 49*grid*grid)
    upper = hint+remainder
    del z, vals
    # Independent high-precision point evaluation certifies a LOWER M.
    flint.ctx.prec = 192
    angle = 2*flint.arb.pi()*j/grid
    point = sum(((angle*a).cos() for a in A), flint.arb(0))
    lower = F(math.floor(-float(point.mid())*10**8)-1, 10**8)
    assert point+ball(lower) < 0
    assert lower <= upper
    return dict(M_lower=str(lower), M_upper=str(upper), grid=grid,
        grid_M_upper=str(hint), Taylor_remainder=str(remainder),
        independent_point_index=j, point_ball=str(point),
        verified=True, all_circle=True,
        breaks_half_constant=(upper*upper < F(n, 4)),
        proves_above_half=(lower*lower > F(n, 4)),
        meets_target=(upper*upper < F(81*n, 400)),
        rules_out_target=(lower*lower > F(81*n, 400)),
        R_upper_float=float(upper)/math.sqrt(n),
        R_lower_float=float(lower)/math.sqrt(n))


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    out = dict(host=socket.gethostname(), numpy_version=np.__version__,
        flint_version=flint.__version__, controls=controls(), cases=[],
        qualification='A bounded unrestricted-support construction pilot, not a convergence theorem or an asymptotic family.')
    path = Path('.research/experiments/boolean_projection_2026-10-21/results.json')
    path.parent.mkdir(parents=True, exist_ok=True)
    for prime in (7, 17):
        row = proposal(prime)
        row['candidate_certificate'] = certify(row['A'])
        row['seed_certificate'] = certify(row['seed_A'])
        row['strict_improvement_verified'] = (F(row['candidate_certificate']['M_upper'])
                                             < F(row['seed_certificate']['M_lower']))
        out['cases'].append(row)
        path.write_text(json.dumps(out, indent=2)+'\n')
        print(json.dumps(dict(n=row['n'], X=row['X'], iterations=row['iterations'],
            candidate_R_interval=[row['candidate_certificate']['R_lower_float'],
                                  row['candidate_certificate']['R_upper_float']],
            strict_improvement_verified=row['strict_improvement_verified'],
            target_reached=row['candidate_certificate']['meets_target'])), flush=True)
    out['status'] = 'PASS'
    out['new_GPU_deployment_justified'] = any(r['candidate_certificate']['breaks_half_constant']
                                             for r in out['cases'])
    path.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(dict(status='PASS', GPU_criterion_met=out['new_GPU_deployment_justified'],
        output=str(path))), flush=True)


if __name__ == '__main__':
    main()
