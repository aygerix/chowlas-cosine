#!/usr/bin/env python
"""Family F_N(B): D = {0,1,...,N-1} + N*B with B a Sidon set (|B| = b, k = N b).
PROVED (lambda_report.md, Prop. IS): for m >= 1 and 0 <= e <= N-1,
    r_D(N m + e) = (N - e) r_B(m) + e r_B(m + 1),      r_D(e) = (N - e) b + e r_B(1)  (0 < e < N),
so every class N m (m ∈ (B-B)_+) is N-fold, every class N m + e (1 <= e < N) is N-fold iff m, m+1 ∈ (B-B)_+, and
    defect pairs = N(N-1)/2 * (b + 2 r_B(1)) ... (computed exactly below, and cross-checked by brute force).
tau(B) = #{m >= 1 : 1_{B-B}(m) != 1_{B-B}(m+1)} (run boundaries of (B-B)_+).
Sidon sets: known optimal Golomb rulers (verified Sidon here), Singer sets mod q^2+q+1 (best lift over multipliers and
shifts), Bose sets mod q^2-1.
Usage: interval_sidon.py [N ...]
"""
import sys, random
from math import gcd
from collections import Counter

GOLOMB = {
    4: [0, 1, 4, 6], 5: [0, 1, 4, 9, 11], 6: [0, 1, 4, 10, 12, 17], 7: [0, 1, 4, 10, 18, 23, 25],
    8: [0, 1, 4, 9, 15, 22, 32, 34], 9: [0, 1, 5, 12, 25, 27, 35, 41, 44], 10: [0, 1, 6, 10, 23, 26, 34, 41, 53, 55],
    11: [0, 1, 4, 13, 28, 33, 47, 54, 64, 70, 72], 12: [0, 2, 6, 24, 29, 40, 43, 55, 68, 75, 76, 85],
    13: [0, 2, 5, 25, 37, 43, 59, 70, 85, 89, 98, 99, 106], 14: [0, 4, 6, 20, 35, 52, 59, 77, 78, 86, 89, 99, 122, 127],
}


def rprof(S):
    S = sorted(S); c = Counter()
    for i in range(len(S)):
        for j in range(i):
            c[S[i] - S[j]] += 1
    return c


def is_sidon(B):
    c = rprof(B)
    return all(v == 1 for v in c.values())


def tau(B):
    import numpy as np
    B = np.asarray(sorted(B)); M = int(B[-1] - B[0])
    dif = (B[:, None] - B[None, :]).ravel()
    ind = np.zeros(M + 3, dtype=np.int8)
    ind[dif[dif > 0]] = 1
    return int(np.count_nonzero(ind[1:M + 2] != ind[2:M + 3]))


def family_stats(N, B, check=False):
    b = len(B); k = N * b
    rB = rprof(B)
    P = k * (k - 1) // 2
    # exact via formula
    good = 0
    M = max(B) - min(B)
    for m in range(0, M + 1):
        for e in range(N):
            if m == 0 and e == 0: continue
            if m == 0:
                r = (N - e) * b + e * rB.get(1, 0)
            else:
                r = (N - e) * rB.get(m, 0) + e * rB.get(m + 1, 0)
            if r == N: good += N
    if check:
        D = [a + N * x for x in B for a in range(N)]
        c = rprof(D)
        good2 = sum(v for v in c.values() if v == N)
        assert good == good2, (good, good2)
    return k, P, good, P - good


def singer_sets(q):
    """Singer Sidon set mod v = q^2+q+1 for prime q (via GF(q^3) with a primitive cubic)."""
    p = q; v = q * q + q + 1
    # find primitive cubic x^3 + a x^2 + b x + c over F_p
    def mul(a, b_, f):
        res = [0] * 5
        for i in range(3):
            for j in range(3):
                res[i + j] = (res[i + j] + a[i] * b_[j]) % p
        for i in (4, 3):
            c = res[i]
            if c:
                for j in range(4):
                    res[i - 3 + j] = (res[i - 3 + j] - c * f[j]) % p
        return res[:3]
    order = p ** 3 - 1
    fac = [r for r in range(2, order + 1) if order % r == 0 and all(r % s for s in range(2, int(r ** 0.5) + 1))]
    def powx(e, f):
        r = [1, 0, 0]; bb = [0, 1, 0]
        while e:
            if e & 1: r = mul(r, bb, f)
            bb = mul(bb, bb, f); e >>= 1
        return r
    for a in range(p):
        for b_ in range(p):
            for c in range(1, p):
                f = [c, b_, a, 1]
                if powx(order, f) != [1, 0, 0]: continue
                if all(powx(order // r, f) != [1, 0, 0] for r in fac):
                    # Singer set: exponents i < v with x^i in the plane {coeff of x^2 = 0}
                    S = []; r = [1, 0, 0]; xx = [0, 1, 0]
                    for i in range(v):
                        if r[2] == 0: S.append(i)
                        r = mul(r, xx, f)
                    return S, v
    return None


def best_lift(S, v, N, tries=None, seed=1):
    """min tau over lifts {(m s + c) mod v}; returns (tau, defect pairs, B)."""
    rnd = random.Random(seed)
    mults = [m for m in range(1, v) if gcd(m, v) == 1]
    if tries is not None and len(mults) * v > tries:
        cand = [(rnd.choice(mults), rnd.randrange(v)) for _ in range(tries)]
    else:
        cand = [(m, c) for m in mults for c in range(v)]
    best = None; ts = []
    for m, c in cand:
        B = sorted((m * s + c) % v for s in S)
        t = tau(B); ts.append(t)
        if best is None or t < best[0]:
            best = (t, B)
    t, B = best
    ts.sort(); global MEDIAN; MEDIAN = ts[len(ts) // 2]
    k, P, good, dp = family_stats(N, B)
    return t, dp, B


if __name__ == "__main__":
    Ns = [int(a) for a in sys.argv[1:]] or [3]
    for N in Ns:
        print(f"=== N = lambda = {N}: D = [0,{N}) + {N}*B")
        for b, B in sorted(GOLOMB.items()):
            assert is_sidon(B), b
            k, P, good, dp = family_stats(N, B, check=(b <= 10))
            t = tau(B)
            print(f"Golomb b={b} len={max(B)} tau={t} k={k} defpairs={dp} phi={good/P:.4f} W/k={2*dp/k:.2f} tau/b^2={t/b/b:.3f}", flush=True)
        for q in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]:
            S, v = singer_sets(q)
            tries = None if v * v < 400_000 else 20000
            t, dp, B = best_lift(S, v, N, tries=tries)
            b = len(S); k = N * b; P = k * (k - 1) // 2
            assert is_sidon(B)
            print(f"Singer q={q} v={v} b={b} best-lift tau={t} tau/b^2={t/b/b:.3f} k={k} defpairs={dp} phi={1-dp/P:.4f} W/k={2*dp/k:.2f}"
                  f"{' (sampled lifts)' if tries else ''}", flush=True)
