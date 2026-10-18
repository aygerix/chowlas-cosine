"""EXP-1: cube framework (PROOFS P7).

For a family J of nonempty subsets of [k], g_J(eps) = sum_{S in J} 2^{|S|} prod_{j in S} eps_j on {±1}^k.
R_cube(J) = -min g / sqrt(2 * sum_{S in J} 2^{|S|}) is a RIGOROUS upper bound for R(A) of any set A built from
base frequencies alpha with distinct signed sums over J (see P7).
"""
from __future__ import annotations
import math, sys
import numpy as np


def chi_matrix(k):
    # rows: eps in {±1}^k (bit i set -> eps_i = -1); cols: subsets S (bitmask)
    n = 1 << k
    e = np.arange(n)
    S = np.arange(n)
    # parity of popcount(e & S)
    x = e[:, None] & S[None, :]
    par = np.zeros_like(x)
    while x.any():
        par ^= (x & 1)
        x >>= 1
    return (1 - 2 * par).astype(np.int8)


def popcount(v):
    return bin(v).count("1")


def R_cube(Jmask, chi, k):
    w = np.array([(1 << popcount(S)) if Jmask[S] else 0 for S in range(1 << k)], dtype=np.float64)
    g = chi.astype(np.float64) @ w
    tot = w.sum()
    return -g.min() / math.sqrt(2 * tot), g


def anneal(k, iters=20000, seed=0, maxdeg=None, T0=0.3, T1=0.002):
    rng = np.random.default_rng(seed)
    n = 1 << k
    chi = chi_matrix(k).astype(np.float64)
    wts = np.array([1 << popcount(S) for S in range(n)], dtype=np.float64)
    allowed = np.array([S != 0 and (maxdeg is None or popcount(S) <= maxdeg) for S in range(n)])
    idx = np.nonzero(allowed)[0]
    J = np.zeros(n, bool)
    # start from all 2-subsets (Bu-like / e_2)
    for S in idx:
        if popcount(S) == 2:
            J[S] = True
    g = chi[:, J] @ wts[J]
    tot = wts[J].sum()
    cur = -g.min() / math.sqrt(2 * tot)
    best = cur; bestJ = J.copy()
    for it in range(iters):
        T = T0 * (T1 / T0) ** (it / iters)
        S = idx[rng.integers(len(idx))]
        sgn = -1.0 if J[S] else 1.0
        g2 = g + sgn * wts[S] * chi[:, S]
        tot2 = tot + sgn * wts[S]
        if tot2 <= 0:
            continue
        new = -g2.min() / math.sqrt(2 * tot2)
        if new <= cur or rng.random() < math.exp(-(new - cur) / T):
            J[S] = not J[S]; g = g2; tot = tot2; cur = new
            if cur < best:
                best = cur; bestJ = J.copy()
    return best, bestJ


if __name__ == "__main__":
    k = int(sys.argv[1]); seed = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    maxdeg = int(sys.argv[3]) if len(sys.argv) > 3 else None
    best, J = anneal(k, iters=40000, seed=seed, maxdeg=maxdeg)
    sets = [S for S in range(1 << k) if J[S]]
    degs = {}
    for S in sets:
        degs[popcount(S)] = degs.get(popcount(S), 0) + 1
    N = sum((1 << popcount(S)) // 2 for S in sets)
    print(f"k={k} seed={seed} maxdeg={maxdeg} R_cube={best:.4f} N={N} |J|={len(sets)} degree-hist={dict(sorted(degs.items()))}")
