"""Simulated-annealing probe: minimise M(A) over A subset [1, L], |A| = N.

UNCERTIFIED search tool (objective is the min over a fine grid, which is an
upper bound for the true min... i.e. grid-M <= true M).  Best sets are
re-evaluated by chowla.min_estimate_fft and chowla.certify_lower_bound.
"""
from __future__ import annotations

import math
import sys

import numpy as np


def anneal(N, L, iters=200000, T0=0.5, T1=0.01, seed=0, grid_mult=8, init=None):
    rng = np.random.default_rng(seed)
    G = 1 << math.ceil(math.log2(grid_mult * L))
    j = np.arange(G // 2 + 1)
    # cos table rows computed on the fly: cos(2 pi a j / G)
    def row(a):
        return np.cos(2 * np.pi * ((a * j) % G) / G)
    if init is None:
        A = list(rng.choice(np.arange(1, L + 1), size=N, replace=False))
    else:
        A = list(init)
    inA = np.zeros(L + 1, bool); inA[A] = True
    g = np.zeros(G // 2 + 1)
    for a in A:
        g += row(a)
    cur = -g.min()
    best = cur; bestA = sorted(A)
    for it in range(iters):
        T = T0 * (T1 / T0) ** (it / iters)
        i = rng.integers(N)
        a_old = A[i]
        # propose: local move (nearby) or global move
        if rng.random() < 0.5:
            a_new = a_old + int(rng.integers(-3, 4))
        else:
            a_new = int(rng.integers(1, L + 1))
        if a_new < 1 or a_new > L or inA[a_new]:
            continue
        g2 = g - row(a_old) + row(a_new)
        new = -g2.min()
        if new <= cur or rng.random() < math.exp(-(new - cur) / T):
            g = g2; cur = new
            inA[a_old] = False; inA[a_new] = True; A[i] = a_new
            if cur < best:
                best = cur; bestA = sorted(A)
    return best, bestA


if __name__ == "__main__":
    N = int(sys.argv[1]); L = int(sys.argv[2]); seed = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    best, A = anneal(N, L, seed=seed)
    print(N, L, best, best / math.sqrt(N), A)
