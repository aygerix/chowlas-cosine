"""E47: spike share. For K in KS, the fraction of ||f_A||_2^2 carried on {f_A > K·M(A)}, with M = -min f_A.
Elementary (NOTEBOOK 2026-10-19): (1/2π)∫_{f > λ√n} f² >= (n/2)(1 − 2R² − 2λR), so R -> 0 forces the share above
K·M to tend to 1 for every fixed K; Chowla is equivalent to a uniform cap ρ_* < 1 on it (P30, conjectural).
FFT grid of size 16·2^ceil(log2(maxA)) points; UNCERTIFIED quadrature (shares, not minima, are what is measured).
Usage: python src/e47_spike_share.py
"""
import json, math, sys
import numpy as np
sys.path.insert(0, "src")
from chowla import min_estimate_fft
KS = (0.5, 1, 2, 3, 4, 6, 8, 12)

def shares(A):
    A = np.asarray(sorted(set(A))); X = int(A.max()); n = len(A)
    G = 16 << math.ceil(math.log2(X))
    c = np.zeros(G); c[A] = 1.0
    f = np.fft.fft(c).real
    M = -min_estimate_fft(A.tolist(), oversample=16).fmin
    tot = (f * f).sum()
    return n, X, M, {K: float((f[f > K * M] ** 2).sum() / tot) for K in KS}, float(f.max() / M)

sets = {}
d = json.load(open("examples/construct/N50_certified.json")); sets["dense_N50"] = d["N50_x72"]["A"]
sets["dense_N45"] = json.load(open("examples/milp/N45_best.json"))["A"]
sb = json.load(open("examples/singer_bu/certified.json"))
for k in sorted(sb, key=lambda s: int(s) if s.isdigit() else 0):
    if not k.isdigit(): continue
    S = sb[k]["S"]
    sets["singer_bu_q" + k] = sorted({3 * abs(a - b) for i, a in enumerate(S) for b in S[:i]} |
                                     {abs(3 * (a + b) + 1) for i, a in enumerate(S) for b in S[:i]})
rng = np.random.default_rng(20261019)
sets["interval_500"] = list(range(1, 501))
sets["random_d0.5_X4000"] = [a for a in range(1, 4001) if rng.random() < 0.5]
sets["taper_random_X4000"] = [a for a in range(1, 4001) if rng.random() < 1 - a / 4000]
B = sorted(rng.choice(np.arange(1, 20000), 60, replace=False))
sets["diffs_random60"] = sorted({abs(int(x) - int(y)) for i, x in enumerate(B) for y in B[:i]})
for name, A in sets.items():
    n, X, M, sh, top = shares(A)
    print(json.dumps(dict(set=name, n=n, maxA=X, R=round(M / math.sqrt(n), 4), max_over_M=round(top, 1),
                          share_above_KM={str(K): round(v, 3) for K, v in sh.items()})), flush=True)
