"""P28 test: the averaged local-maximal lower bound
    M(A) >= B_H(A) := (1/4π) ∫_0^{2π} sup_{m>=H} |Σ_a F̂_H(a−m) e^{iax}| dx,   F̂_H(k) = (1 − |k|/H)_+,
valid for every H >= 1 (PROOFS P28). The sup is taken over window centres m on the grid {H, H + s, H + 2s, ...},
s = max(1, H // 4), a subset of all m >= H, so the computed value is still a valid lower bound up to quadrature.
The x-integral uses an FFT grid of size G >= 16·(max A + H). UNCERTIFIED numerics; ratios to M are what matter.
Usage: python src/p28_test.py   (runs the built-in test sets and prints B_H/√n against M/√n)
"""
import json, math, sys
import numpy as np
sys.path.insert(0, "src")
from chowla import min_estimate_fft


def B_H(A, H):
    A = np.asarray(sorted(A)); X = int(A.max())
    G = 1 << math.ceil(math.log2(16 * (X + H)))
    best = np.zeros(G)
    s = max(1, H // 4)
    for m in range(H, X + H, s):
        w = 1.0 - np.abs(A - m) / H
        sel = w > 0
        if not sel.any():
            continue
        c = np.zeros(G); c[A[sel]] = w[sel]
        best = np.maximum(best, np.abs(np.fft.fft(c)))
    return best.mean() / 2.0                      # (1/4π)∫ = (1/2)·mean over the full circle


def report(name, A):
    A = sorted(set(int(a) for a in A)); n = len(A); X = max(A)
    M = -min_estimate_fft(A, oversample=16).fmin
    Hs = sorted({max(1, X // d) for d in (64, 32, 16, 8, 4, 2, 1)})     # <= ~4·64 windows per H
    vals = [(H, B_H(A, H)) for H in Hs]
    Hb, b = max(vals, key=lambda t: t[1])
    print(json.dumps(dict(set=name, n=n, maxA=X, M_over_sqrtn=round(M / math.sqrt(n), 4),
                          best_B_over_sqrtn=round(b / math.sqrt(n), 4), best_H=Hb, ratio_B_over_M=round(b / M, 3),
                          profile={H: round(v / math.sqrt(n), 3) for H, v in vals})), flush=True)


if __name__ == "__main__":
    rng = np.random.default_rng(20261019)
    sets = {}
    d = json.load(open("examples/construct/N50_certified.json")); sets["dense_N50"] = d["N50_x72"]["A"]
    sets["dense_N45"] = json.load(open("examples/milp/N45_best.json"))["A"]
    try:
        sb = json.load(open("examples/singer_bu/certified.json"))
        for k in ("61", "101"):                       # A(S) = {3|s-t|} ∪ {|3(s+t)+1|} (src/bu.py convention)
            S = sb[k]["S"]
            sets["singer_bu_q" + k] = sorted({3 * abs(a - b) for i, a in enumerate(S) for b in S[:i]} |
                                             {abs(3 * (a + b) + 1) for i, a in enumerate(S) for b in S[:i]})
    except Exception as e:
        print("singer_bu load:", e)
    sets["interval_200"] = list(range(1, 201))
    sets["random_d0.5_X2000"] = [a for a in range(1, 2001) if rng.random() < 0.5]
    sets["random_d0.05_X40000"] = [a for a in range(1, 40001) if rng.random() < 0.05]
    B = sorted(rng.choice(np.arange(1, 4000), 40, replace=False))
    sets["diffs_random40"] = sorted({abs(int(x) - int(y)) for i, x in enumerate(B) for y in B[:i]})
    for name, A in sets.items():
        report(name, A)
