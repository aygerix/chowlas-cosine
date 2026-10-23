"""One bounded adversarial search for the prescribed reciprocal R0 bound.

Maximize signed reciprocal Rayleigh energy under a sampled low-M cap;
this is NOT another minimum-M search or successful-control sweep.
All mathematical computation runs on Dirichlet. Proposal floats carry
no proof; saved all-circle and full-reciprocal certificates do.
"""
from fractions import Fraction as F
import json
import math
from pathlib import Path
import socket
import time

import flint
import numpy as np

from cstar_boolean_projection import certify
from cstar_zero_reciprocal import one


def evaluate(values, n):
    rows = np.atleast_2d(values)
    lam = 2*math.sqrt(n)
    q = -rows.imag/((lam+rows.real)**2+rows.imag**2)
    q2 = q*q
    Q = q2.mean(axis=1)
    H = (2*rows.real*q2).mean(axis=1)
    return H/(Q*math.sqrt(n)), -rows.real.min(axis=1)


def search(A, X=165, chains=4, steps=3000, grid=8192, seed=20261023):
    n = len(A)
    assert n == 56 and max(A) <= X and len(set(A)) == n
    rng = np.random.default_rng(seed)
    angles = 2*np.pi*np.arange(grid)/grid
    basis = np.exp(1j*np.arange(X+1)[:,None]*angles)
    # A={1},lambda2 has exact normalized odd reciprocal quotient -1.
    control, _ = evaluate(basis[1], 1)
    assert abs(float(control[0])+1) < 1e-12
    supports = np.zeros((chains, X+1), dtype=bool)
    supports[:,A] = True
    values = np.repeat(basis[A].sum(axis=0)[None,:], chains, axis=0)
    scores, M = evaluate(values,n)
    assert np.all(M < .98*math.sqrt(n))
    best_score, best_A, best_step = float(scores.max()), list(A), -1
    initial = best_score
    history = []
    accepted, infeasible = [0]*chains, [0]*chains
    start = time.monotonic()
    for step in range(steps):
        proposals = values.copy()
        swaps = []
        for chain in range(chains):
            count = int(rng.choice([1,2,4],p=[.65,.25,.10]))
            occupied = np.flatnonzero(supports[chain])
            empty = np.flatnonzero(~supports[chain])
            # Zero is never an admissible frequency.
            empty = empty[empty > 0]
            removed = rng.choice(occupied,count,replace=False)
            added = rng.choice(empty,count,replace=False)
            proposals[chain] += basis[added].sum(axis=0)-basis[removed].sum(axis=0)
            swaps.append((removed,added))
        proposed_scores, proposed_M = evaluate(proposals,n)
        temperature = .03*(.0005/.03)**(step/max(steps-1,1))
        feasible = proposed_M <= .98*math.sqrt(n)
        accept = feasible & (np.log(rng.random(chains)) < (proposed_scores-scores)/temperature)
        for chain in range(chains):
            infeasible[chain] += int(not feasible[chain])
            if accept[chain]:
                removed,added = swaps[chain]
                supports[chain,removed] = False
                supports[chain,added] = True
                values[chain] = proposals[chain]
                scores[chain] = proposed_scores[chain]
                accepted[chain] += 1
                if scores[chain] > best_score+1e-12:
                    best_score = float(scores[chain])
                    best_A = np.flatnonzero(supports[chain]).tolist()
                    best_step = step
        if step % 500 == 0 or best_score > .005:
            history.append(dict(step=step,best_normalized_grid_energy=best_score,
                                current_scores=scores.tolist()))
            print(json.dumps(history[-1]),flush=True)
        if best_score > .005:
            break
        if step % 200 == 199:
            # Rebuild rather than accumulate cancellation/rounding drift.
            for chain in range(chains):
                values[chain] = basis[np.flatnonzero(supports[chain])].sum(axis=0)
            scores,_ = evaluate(values,n)
    assert len(best_A) == n and min(best_A) > 0
    final_values = basis[best_A].sum(axis=0)
    final_score, final_M = evaluate(final_values,n)
    assert abs(float(final_score[0])-best_score) < 1e-9
    return dict(A=best_A,n=n,X_ambient=X,grid=grid,seed=seed,
        chains=chains,steps=step+1,proposals_at_most=chains*(step+1),
        swap_sizes=[1,2,4],initial_grid_energy=initial,
        best_grid_energy=float(final_score[0]),best_grid_M=float(final_M[0]),
        best_step=best_step,accepted=accepted,infeasible=infeasible,
        history=history,seconds=time.monotonic()-start,
        qualification='Finite heuristic adversary in one box; no universal exclusion.')


def main():
    if 'dirichlet' not in socket.gethostname():
        raise SystemExit('Use src/dirun.sh')
    source=Path('.research/experiments/boolean_projection_2026-10-21/results.json')
    seed_row=next(r for r in json.loads(source.read_text())['cases'] if r['n']==56)
    result=search(seed_row['A'])
    global_certificate=certify(result['A'])
    assert F(global_certificate['M_upper'])**2 < result['n']
    flint.ctx.prec=384
    exact=one(result['A'],F(global_certificate['M_upper']),'R0_adversarial_n56',band_multiple=32)
    low,high=map(F,exact['infinite_Rayleigh_normalized_bracket'])
    out=dict(host=socket.gethostname(),proposal=result,
        all_circle_certificate=global_certificate,cases=[exact],
        R0_refuted=(low > -F(1,100)),
        R0_holds_for_saved_candidate=(high < -F(1,100)),
        universal_sign_refuted=exact['infinite_energy_positive'],
        new_GPU_deployment_justified=False,status='PASS')
    path=Path('.research/experiments/R0_adversary_2026-10-23/results.json')
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',output=str(path),
        R0_refuted=out['R0_refuted'],normalized_reciprocal_interval=exact['infinite_Rayleigh_normalized_bracket'],
        global_M_upper=global_certificate['M_upper'])),flush=True)


if __name__=='__main__':
    main()
