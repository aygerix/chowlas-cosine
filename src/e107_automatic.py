"""E107: Chowla ratio of b-AUTOMATIC sets (CSTAR A2, design class "transfer-matrix / b-adic hierarchy").

A deterministic automaton reads the L base-b digits of k (most significant first, leading zeros included).
delta[s][d] in {-1 (reject), 0..S-1}; initial state 0 with delta[0][0] = 0, so A_{L-1} is the front of A_L
(nested family). A_L = {1 <= k < b^L : the digit string of k is accepted (never rejected)}.
f(x) = sum_{a in A_L} cos(2 pi a x); F(x) = sum e(a x) is a matrix Riesz product u^T M(b^{L-1}x)...M(x) 1.
Spikes sit at b-adic rationals of every depth k; their heights ~ lambda^{L-k} |Phi_k| are mesoscopic for
1 << k < L/2. A fixed automaton with R_L = M_L/sqrt(n_L) -> 0 would be an explicit Chowla counterexample family.

Modes:
  screen b S L1 L2 [limit]   enumerate all automata with S reachable states (delta[0][0] = 0), keep
                             1.05 < lambda < b (sparse), print JSON rows with R at L1 and L2 and the
                             b-adic depth <= 3 diagnostic. (Grid minima; UNCERTIFIED, M underestimated.)
  follow file Lmax           for each automaton (JSON rows with key "delta") compute R_L for L up to Lmax,
                             with golden-section refinement of the 24 lowest grid minima.
"""
import sys, json, math, itertools
import numpy as np
from multiprocessing import Pool
import os

def reach(delta):
    S = len(delta); seen = {0}; st = [0]
    while st:
        s = st.pop()
        for t in delta[s]:
            if t >= 0 and t not in seen:
                seen.add(t); st.append(t)
    return seen

def lam(delta, b):
    S = len(delta); C = np.zeros((S, S))
    for s in range(S):
        for d in range(b):
            t = delta[s][d]
            if t >= 0: C[s, t] += 1
    ev = np.linalg.eigvals(C)
    return float(max(abs(ev)))

def gen(delta, b, L):
    vals = np.zeros(1, dtype=np.int64); st = np.zeros(1, dtype=np.int64)
    D = np.array(delta, dtype=np.int64)
    for _ in range(L):
        nv = []; ns = []
        for d in range(b):
            t = D[st, d]; ok = t >= 0
            nv.append(vals[ok] * b + d); ns.append(t[ok])
        vals = np.concatenate(nv); st = np.concatenate(ns)
        if vals.size == 0: break
    vals = vals[vals > 0]
    return np.sort(vals)

def fgrid(A, G):
    ind = np.zeros(G); ind[A % G] += 1.0
    return np.fft.rfft(ind).real   # f(j/G), j = 0..G/2 (f is even)

def fval(A, x):
    return float(np.cos(2 * np.pi * A * x).sum())

def refine(A, x0, h):
    # golden section on [x0-h, x0+h] for the minimum of f
    a, c = x0 - h, x0 + h; g = (math.sqrt(5) - 1) / 2
    x1 = c - g * (c - a); x2 = a + g * (c - a); f1 = fval(A, x1); f2 = fval(A, x2)
    for _ in range(40):
        if f1 < f2: c, x2, f2 = x2, x1, f1; x1 = c - g * (c - a); f1 = fval(A, x1)
        else: a, x1, f1 = x1, x2, f2; x2 = a + g * (c - a); f2 = fval(A, x2)
    return min(f1, f2), (x1 if f1 < f2 else x2)

def stats(A, b, L, over=8, nref=0):
    n = A.size
    if n < 4: return None
    X = int(b ** L); G = over * X
    f = fgrid(A, G)
    j = int(np.argmin(f)); M = -float(f[j]); xm = j / G
    if nref:
        idx = np.argpartition(f, nref)[:nref]
        for jj in idx:
            v, xx = refine(A, jj / G, 1.0 / G)
            if -v > M: M, xm = -v, xx
    # b-adic diagnostic: min f/n over x = j/b^k, k <= 3, j coprime-ish (all j)
    bad = 1e9
    for k in range(1, 4):
        q = b ** k
        for jj in range(1, q):
            if jj % b == 0: continue
            v = fval(A, jj / q) / n
            bad = min(bad, v)
    return dict(n=int(n), X=X, M=M, R=M / math.sqrt(n), xmin=xm, badic_min=bad)

def automata(b, S):
    choices = list(range(-1, S))
    cells = [(s, d) for s in range(S) for d in range(b) if not (s == 0 and d == 0)]
    for combo in itertools.product(choices, repeat=len(cells)):
        delta = [[-1] * b for _ in range(S)]; delta[0][0] = 0
        for (s, d), t in zip(cells, combo): delta[s][d] = t
        if len(reach(delta)) != S: continue
        # canonical-ish: states 1..S-1 first reached in increasing order (cheap symmetry cut)
        order = []
        for s in range(S):
            for d in range(b):
                t = delta[s][d]
                if t > 0 and t not in order: order.append(t)
        if order != sorted(order): continue
        yield delta

def screen_one(args):
    delta, b, L1, L2 = args
    l = lam(delta, b)
    if not (1.05 < l < b - 1e-9): return None
    out = dict(b=b, delta=delta, lam=l)
    for L in (L1, L2):
        A = gen(delta, b, L); st = stats(A, b, L)
        if st is None: return None
        out[f"L{L}"] = st
    return out

def main():
    mode = sys.argv[1]
    W = int(os.environ.get("CHOWLA_WORKERS", "4"))
    if mode == "screen":
        b, S, L1, L2 = map(int, sys.argv[2:6])
        lim = int(sys.argv[6]) if len(sys.argv) > 6 else 0
        jobs = ((d, b, L1, L2) for d in automata(b, S))
        if lim: jobs = itertools.islice(jobs, lim)
        with Pool(W) as P:
            for r in P.imap_unordered(screen_one, jobs, chunksize=64):
                if r is not None: print(json.dumps(r), flush=True)
    elif mode == "follow":
        fn, Lmax = sys.argv[2], int(sys.argv[3])
        rows = [json.loads(l) for l in open(fn)]
        for r in rows:
            b, delta = r["b"], r["delta"]
            res = []
            for L in range(4, Lmax + 1):
                if b ** L > 2 ** 21: break
                A = gen(delta, b, L); st = stats(A, b, L, over=16, nref=24)
                if st: st["L"] = L; res.append(st)
            print(json.dumps(dict(b=b, delta=delta, lam=lam(delta, b), series=res)), flush=True)

if __name__ == "__main__":
    main()
