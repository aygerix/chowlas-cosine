"""E74 — run-top (boundary) counts against K^2 and K^3 mu on the project's sets (alternative lower-bound mechanism,
NOTEBOOK 2026-10-19 night cont. 8; Bu et al. 2610.17160 Prop. 9.1/9.7).

A' = A u (-A), N = |A'| = 2n, B_t = {a in A' : a - t in A', a + t notin A'} (t >= 1),
K = 2 lambda (lambda = M(A) from the grid), mu = ||F||_1 = 2||f_A||_1 (normalized measure, grid).
Bu et al.: |B_t| <= C1 K^3 mu for every t; sum_{t>=1} |B_t| = (N^2 - N - 2 T3)/2... (we report the exact sum and N^2/2).
Reports: max_t |B_t| / K^2, mean_{t <= 2X} |B_t| / K^2, max_t |B_t| / (K^3 mu), sum_t |B_t| / (2X K^2), lambda/sqrt(n).
T-dense would follow from mean_{t<=2X} |B_t| <= c K^2 uniformly (Lemma 9.6 gives sum_t |B_t| >= N^2/4 over t >= 1).
NUMERICAL (grid minimum, uncertified). Usage: python src/e74_runtops.py  -> examples/e74/e74.jsonl
"""
import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, "src")
from e67_zoo import bu  # noqa: E402
from singer import singer  # noqa: E402

OUT = "examples/e74/e74.jsonl"


def grid(A):
    X = max(A)
    G = 1 << math.ceil(math.log2(64 * X))
    c = np.zeros(G)
    c[np.array(A)] = 1
    f = np.fft.rfft(c).real
    w = np.ones(len(f))
    w[0] = w[-1] = 0.5
    lam = float(-f.min())
    l1 = float((w * np.abs(f)).sum() / (w.sum()))
    return lam, l1


def runtops(A):
    A = np.array(sorted(A))
    X = int(A.max())
    ind = np.zeros(4 * X + 3, dtype=bool)
    off = 2 * X + 1
    ind[A + off] = True
    ind[-A + off] = True
    pos = np.nonzero(ind)[0]
    cnt = np.zeros(2 * X + 1, dtype=np.int64)
    for t in range(1, 2 * X + 1):
        lo = pos - t
        hi = pos + t
        ok_lo = (lo >= 0) & ind[np.clip(lo, 0, len(ind) - 1)]
        ok_hi = (hi < len(ind)) & ind[np.clip(hi, 0, len(ind) - 1)]
        cnt[t] = int((ok_lo & ~ok_hi).sum())
    return cnt


def rec(name, A, fh):
    A = sorted(set(int(a) for a in A))
    n = len(A)
    X = max(A)
    lam, l1 = grid(A)
    K = 2 * lam
    mu = 2 * l1
    cnt = runtops(A)
    N = 2 * n
    r = {"family": name, "n": n, "X": X, "C": X / n, "R": lam / math.sqrt(n),
         "max_Bt_over_K2": float(cnt.max() / K ** 2), "mean_Bt_over_K2": float(cnt[1:].mean() / K ** 2),
         "max_Bt_over_K3mu": float(cnt.max() / (K ** 3 * mu)), "sumBt_over_N2": float(cnt.sum() / N ** 2),
         "argmax_t": int(cnt.argmax()), "max_Bt": int(cnt.max()), "mu_over_K": mu / K}
    print(json.dumps(r), flush=True)
    fh.write(json.dumps(r) + "\n")
    fh.flush()


def main():
    os.makedirs("examples/e74", exist_ok=True)
    rng = np.random.default_rng(20261019)
    with open(OUT, "w") as fh:
        for q in (7, 11, 13, 19, 23, 31, 43):
            A, _ = bu(q)
            rec(f"bu_q{q}", A, fh)
        for q in (13, 23, 43, 61):
            S, v = singer(q)
            D = sorted({b - a for a in S for b in S if b > a})
            rec(f"singer_diff_q{q}", D, fh)
        sb = json.load(open("examples/smallN_best.json"))
        for k in ("24", "30", "36"):
            if k in sb:
                rec(f"smallN_{k}", sb[k]["A"], fh)
        for C in (1.5, 2, 4, 8):
            for n in (256, 1024, 4096):
                X = int(C * n)
                A = (rng.permutation(X)[:n] + 1).tolist()
                rec(f"random_C{C}", A, fh)
        for n in (256, 1024, 4096):
            rec("interval", list(range(1, n + 1)), fh)
        for fn, tag in (("examples/e68/e68.jsonl", "e68"), ("examples/e72/e72c_n128_C6.jsonl", "e72c_C6"),
                        ("examples/e72/e72c_n128_C10.jsonl", "e72c_C10"), ("examples/e72/e72c_n512_C3.jsonl", "e72c_C3")):
            if os.path.exists(fn):
                for i, line in enumerate(open(fn)):
                    if i >= 6:
                        break
                    rec(f"{tag}_{i}", json.loads(line)["A"], fh)


if __name__ == "__main__":
    main()
