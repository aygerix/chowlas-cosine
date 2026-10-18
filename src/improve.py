"""Local improvement of a seed set A (e.g. a Bu set): minimise R = M/sqrt(N) by add / remove / swap moves.

Objective evaluated on a fixed grid x_j = pi j / G (j = 0..G) — UNCERTIFIED (grid min >= true min); final sets are
re-certified separately.  Moves are targeted: with probability p_t the move uses the current argmin x* (remove an
element with cos(a x*) < 0, or add a candidate with cos(a x*) > 0), otherwise random.
"""
from __future__ import annotations
import math, sys, json, time
import numpy as np


def improve(A, cap, iters=20000, seed=0, G=None, T0=0.02, T1=0.0005, p_target=0.7, log_every=2000):
    rng = np.random.default_rng(seed)
    A = sorted(set(A))
    if G is None:
        G = 1 << math.ceil(math.log2(8 * cap))
    j = np.arange(G + 1, dtype=np.int64)
    def row(a):
        return np.cos(np.pi * ((a * j) % (2 * G)) / G)
    inA = set(A)
    g = np.zeros(G + 1)
    for a in A:
        g += row(a)
    N = len(A)
    def score(gv, n):
        return -gv.min() / math.sqrt(n)
    cur = score(g, N); best = cur; bestA = list(A)
    hist = []
    for it in range(iters):
        T = T0 * (T1 / T0) ** (it / iters)
        jstar = int(np.argmin(g)); xs = math.pi * jstar / G
        mv = rng.random()
        if mv < 0.34:      # remove
            Al = list(inA)
            if rng.random() < p_target:
                cand = [a for a in rng.choice(Al, size=min(64, len(Al)), replace=False) if math.cos(a * xs) < 0]
                if not cand:
                    continue
                a = int(min(cand, key=lambda a: math.cos(a * xs)))
            else:
                a = int(rng.choice(Al))
            g2 = g - row(a); n2 = N - 1
            new = score(g2, n2)
            if new <= cur or rng.random() < math.exp(-(new - cur) / T):
                g = g2; N = n2; inA.discard(a); cur = new
        elif mv < 0.67:    # add
            if rng.random() < p_target:
                cand = rng.integers(1, cap + 1, size=256)
                cand = [int(c) for c in cand if c not in inA and math.cos(c * xs) > 0.5]
                if not cand:
                    continue
                a = cand[0]
            else:
                a = int(rng.integers(1, cap + 1))
                if a in inA:
                    continue
            g2 = g + row(a); n2 = N + 1
            new = score(g2, n2)
            if new <= cur or rng.random() < math.exp(-(new - cur) / T):
                g = g2; N = n2; inA.add(a); cur = new
        else:              # swap
            Al = list(inA)
            a = int(rng.choice(Al))
            b = int(a + rng.integers(-50, 51)) if rng.random() < 0.5 else int(rng.integers(1, cap + 1))
            if b < 1 or b > cap or b in inA:
                continue
            g2 = g - row(a) + row(b)
            new = score(g2, N)
            if new <= cur or rng.random() < math.exp(-(new - cur) / T):
                g = g2; inA.discard(a); inA.add(b); cur = new
        if cur < best:
            best = cur; bestA = sorted(inA)
        if log_every and it % log_every == 0:
            hist.append((it, cur, best, N))
    return best, bestA, hist


if __name__ == "__main__":
    key = sys.argv[1]; seed = int(sys.argv[2]); iters = int(sys.argv[3])
    sys.path.insert(0, 'src')
    from bu import A_of_S
    d = json.load(open('examples/bu_reproduction_certified.json'))
    S = d[key]['S']; A = A_of_S(S)
    cap = int(max(A) * 1.0)
    t = time.time()
    best, bestA, hist = improve(A, cap, iters=iters, seed=seed)
    out = dict(key=key, seed=seed, iters=iters, start_R=d[key]['R_cert'], best_R_grid=best, N=len(bestA), max=max(bestA), A=bestA, hist=hist, secs=time.time() - t)
    json.dump(out, open(f'examples/improve_{key}_s{seed}.json', 'w'))
    print(f"{key} seed={seed}: start R_cert={d[key]['R_cert']:.4f} -> grid R={best:.4f} N={len(bestA)} ({time.time()-t:.0f}s)")
