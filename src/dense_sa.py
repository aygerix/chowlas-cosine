"""Dense-regime probe: SA over subsets of [1, X] minimising R = M/sqrt(N) (grid objective, UNCERTIFIED).

Objective on grid x_j = pi j / G, j=0..G (f even, 2pi-periodic).  Moves: toggle n in [1, X] (add/remove), swap.
Initialisation: dithered Fejer profile w_n = (1 - n/X) via 1D error diffusion, or random with prob w_n.
Usage: python src/dense_sa.py X iters seed [init]
"""
from __future__ import annotations
import sys, math, json, time
import numpy as np


def fejer_dither(X, mode="diffuse", rng=None, p=1.0):
    w = np.array([(1 - n / X) ** p for n in range(1, X + 1)])
    if mode == "diffuse":
        acc = 0.0; A = []
        for n, wn in zip(range(1, X + 1), w):
            acc += wn
            if acc >= 0.5:
                A.append(n); acc -= 1.0
        return A
    return [n for n, wn in zip(range(1, X + 1), w) if rng.random() < wn]


def sa(X, iters, seed=0, init="diffuse", T0=0.05, T1=0.0005, G=None, A0=None):
    rng = np.random.default_rng(seed)
    if G is None:
        G = 1 << math.ceil(math.log2(16 * X))
    j = np.arange(G + 1)
    C = np.cos(np.pi * np.outer(np.arange(X + 1), j) / G)  # row n = cos(n x_j)
    inA = np.zeros(X + 1, bool)
    A = A0 if A0 is not None else fejer_dither(X, init, rng)
    inA[A] = True
    g = C[inA].sum(0)
    N = int(inA.sum())
    cur = -g.min() / math.sqrt(N)
    best, bestA = cur, np.flatnonzero(inA).tolist()
    for it in range(iters):
        T = T0 * (T1 / T0) ** (it / iters)
        r = rng.random()
        if r < 0.6:
            n = int(rng.integers(1, X + 1))
            s = -1 if inA[n] else 1
            g2 = g + s * C[n]; N2 = N + s
            if N2 < 2:
                continue
            new = -g2.min() / math.sqrt(N2)
            if new <= cur or rng.random() < math.exp(-(new - cur) / T):
                g, N, cur = g2, N2, new; inA[n] = not inA[n]
        else:
            ins = np.flatnonzero(inA); outs = np.flatnonzero(~inA[1:]) + 1
            if len(outs) == 0:
                continue
            a = int(rng.choice(ins))
            b = int(a + rng.integers(-3, 4)) if rng.random() < 0.7 else int(rng.choice(outs))
            if b < 1 or b > X or inA[b]:
                continue
            g2 = g - C[a] + C[b]
            new = -g2.min() / math.sqrt(N)
            if new <= cur or rng.random() < math.exp(-(new - cur) / T):
                g, cur = g2, new; inA[a] = False; inA[b] = True
        if cur < best:
            best, bestA = cur, np.flatnonzero(inA).tolist()
    return best, bestA


if __name__ == "__main__":
    X, iters, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    init = sys.argv[4] if len(sys.argv) > 4 else "diffuse"
    t = time.time()
    best, A = sa(X, iters, seed, init)
    print(json.dumps(dict(X=X, seed=seed, init=init, iters=iters, R_grid=round(best, 5), N=len(A), max=max(A), A=A,
                          secs=round(time.time() - t, 1))))
