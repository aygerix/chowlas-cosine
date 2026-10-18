"""Large-neighbourhood search with exact window MILPs (HiGHS) for small R = M(A)/sqrt|A|, A ⊂ [1, X], |A| = n0 fixed.

Each step frees a window W ⊂ [1, X] (contiguous block, random positions, or positions around the current minimiser's
"wrong-sign" frequencies), keeps A \\ W fixed, and solves
    min lam  s.t.  f_{A\\W}(x) + sum_{a in W} z_a cos(a x) + lam >= 0  (x in cut set),  sum z_a = |A ∩ W|,  z binary,
adding cuts at the true minimisers until the window solution is feasible for the continuum (to FFT accuracy).
Objective values are UNCERTIFIED (FFT + Newton); final sets are certified separately (src/chowla.certify_lower_bound).
Usage: python src/lns_milp.py X n0 steps seed [start.json|scaled:<N>|core:] [win] [tail]
"""
from __future__ import annotations
import sys, math, json, time
import numpy as np
import highspy
sys.path.insert(0, 'src')
from box_minlam import true_min


def window_solve(A, W, X, cuts, tl=20.0):
    W = np.array(sorted(W)); Aset = set(A); fixed = [a for a in A if a not in set(W.tolist())]
    k = sum(1 for a in W if a in Aset)
    Fa = np.array(fixed, float)
    best = None
    for rnd in range(12):
        h = highspy.Highs(); h.setOptionValue("output_flag", False); h.setOptionValue("mip_rel_gap", 1e-4)
        h.setOptionValue("time_limit", tl)
        m = len(W); inf = highspy.kHighsInf
        for _ in range(m): h.addVar(0, 1)
        h.addVar(-inf, inf)
        h.changeColsIntegrality(m, np.arange(m, dtype=np.int32), np.array([highspy.HighsVarType.kInteger] * m))
        c = np.zeros(m + 1); c[m] = 1; h.changeColsCost(m + 1, np.arange(m + 1, dtype=np.int32), c)
        h.addRow(k, k, m, np.arange(m, dtype=np.int32), np.ones(m))
        xs = np.array(sorted(cuts))
        base = np.cos(np.outer(xs, Fa)).sum(1) if len(Fa) else np.zeros(len(xs))
        Cw = np.cos(np.outer(xs, W))
        idx = np.arange(m + 1, dtype=np.int32)
        for i in range(len(xs)):
            h.addRow(-base[i], inf, m + 1, idx, np.append(Cw[i], 1.0))
        cur = np.array([1.0 if a in Aset else 0.0 for a in W])
        sol = highspy.HighsSolution(); sol.col_value = list(np.append(cur, 1e3)); sol.value_valid = True
        h.setSolution(sol)
        h.run()
        z = np.array(h.getSolution().col_value)
        if len(z) < m + 1: return None
        newA = sorted(fixed + [int(a) for a, zz in zip(W, z[:m]) if zz > 0.5])
        (fm, xm), v, G = true_min(newA)
        lam = z[m]
        if best is None or -fm < best[0]: best = (-fm, newA)
        if -fm <= lam + 1e-7: break
        add = {xm}
        bad = np.flatnonzero(v < -lam)
        for j in bad:
            if 0 < j < G and v[j] <= v[j - 1] and v[j] <= v[j + 1]: add.add(math.pi * j / G)
        cuts.update(sorted(add)[:100])
    return best


def lns(A, X, steps, seed, win=24, log=None, tail_exact=False):
    rng = np.random.default_rng(seed)
    A = sorted(A); n0 = len(A)
    (fm, xm), v, G = true_min(A); cur = -fm
    cuts = set((np.pi * np.arange(4 * X + 1) / (4 * X)).tolist())
    for j in range(1, G):
        if v[j] <= v[j - 1] and v[j] <= v[j + 1] and v[j] < 0.6 * fm: cuts.add(math.pi * j / G)
    t0 = time.time()
    for st in range(steps):
        mode = rng.integers(4) if tail_exact else rng.integers(3)
        if mode == 3:                                   # whole tail (0.58X, X] exactly + a few core positions
            lo = int(0.58 * X)
            W = list(range(lo + 1, X + 1)) + rng.choice(np.arange(1, lo + 1), size=min(6, lo), replace=False).tolist()
        elif mode == 0:                                 # contiguous block
            s = int(rng.integers(1, max(2, X - win + 2))); W = list(range(s, min(X, s + win - 1) + 1))
        elif mode == 1:                                 # random positions
            W = rng.choice(np.arange(1, X + 1), size=min(win, X), replace=False).tolist()
        else:                                           # frequencies most responsible at the current minimiser
            (fm, xm), _, _ = true_min(A)
            score = np.cos(np.arange(1, X + 1) * xm)      # members with cos<0 hurt, non-members with cos>0 help
            inA = np.zeros(X, bool); inA[np.array(A) - 1] = True
            pri = np.where(inA, -score, score) + 0.3 * rng.random(X)
            W = (np.argsort(-pri)[:win] + 1).tolist()
        r = window_solve(A, W, X, cuts, tl=8.0 if mode == 3 else 10.0)
        if r is not None and r[0] < cur - 1e-9:
            cur, A = r
            if log: print(f"step {st} mode {mode}: M={cur:.5f} R={cur/math.sqrt(n0):.5f} t={time.time()-t0:.0f}s", file=log, flush=True)
    return cur, A


if __name__ == "__main__":
    X, n0, steps, seed = map(int, sys.argv[1:5])
    src = sys.argv[5] if len(sys.argv) > 5 else None
    win = int(sys.argv[6]) if len(sys.argv) > 6 else 24
    rng = np.random.default_rng(seed)
    if src and src.startswith('core:'):                  # interval core [1, 0.6X] + random tail of the remaining size
        lo = int(0.6 * X); core = list(range(1, min(lo, n0) + 1))
        tail = sorted(rng.choice(np.arange(lo + 1, X + 1), size=n0 - len(core), replace=False).tolist())
        A = core + tail
    elif src and src.startswith('scaled:'):                # scale the density profile of a smaller optimum
        d = json.load(open('examples/smallN_best.json'))[src.split(':')[1]]
        B = np.array(d['A']); Xb = B.max(); ind = np.zeros(Xb + 1); ind[B] = 1
        dens = np.interp(np.arange(1, X + 1) * Xb / X, np.arange(Xb + 1), np.convolve(ind, np.ones(3) / 3, 'same'))
        p = dens / dens.sum() * n0
        A = sorted((rng.choice(np.arange(1, X + 1), size=n0, replace=False, p=np.clip(p, 1e-9, None) / np.clip(p, 1e-9, None).sum())).tolist())
    elif src:
        A = json.load(open(src))['A']
    else:
        A = sorted(rng.choice(np.arange(1, X + 1), size=n0, replace=False).tolist())
    A = [int(a) for a in A if a <= X][:n0]
    while len(A) < n0:
        c = int(rng.integers(1, X + 1))
        if c not in A: A = sorted(A + [c])
    M, A = lns(A, X, steps, seed, win, log=sys.stderr, tail_exact=(len(sys.argv) > 7 and sys.argv[7] == 'tail'))
    print(json.dumps(dict(X=X, n0=n0, seed=seed, src=src, M=M, R=M / math.sqrt(n0), A=A)), flush=True)
