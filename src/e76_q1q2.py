"""E76 — averaged run-top quantities (Bu et al. 2610.17160 Lemma 9.3 / Prop. 9.1; round-6 report "Task 3").

For A' = A u (-A), F = F_{A'} = 2 f_A, K = 2 lambda, u = F + K >= 0 (mean K), B_t = right endpoints of maximal
t-progressions in A'. Proxy for Lemma 9.3's split g = 1hat_{B_t} = Q1 + Q2 with |Q1| <= 3u: the clipping
Q1 = g min(1, 3u/|g|), Q2 = g - Q1 (|Q2| = (|g| - 3u)_+). Per t we record |B_t|, ||g||_1, ||Q1||_1, ||Q2||_2^2.
Averaged over 1 <= t <= 2X we report
  s1 = mean_t ||Q1_t||_1^2 / K^2   (Bu et al. use ||Q1||_1 <= 3K, i.e. s1 <= 9),
  s2 = mean_t ||Q2_t||_2^2 / (K^3 mu),
  r  = mean_t |B_t| / (K mu mean_t ||Q1_t||_1^2 + mean_t ||Q2_t||_2^2),
i.e. how much of the per-shift budget the actual sets use. An averaged saving (round 6) needs s1 << 1 on average.
NUMERICAL (grid G = 16X power of two; clipping is a proxy for, not a reproduction of, Lemma 9.3's exact split).
Usage: python src/e76_q1q2.py -> examples/e76/e76.jsonl
"""
import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, "src")
from e67_zoo import bu  # noqa: E402
from singer import singer  # noqa: E402

OUT = "examples/e76/e76.jsonl"


def analyse(name, A, fh, tmax=None):
    A = sorted(set(int(a) for a in A))
    n = len(A)
    X = max(A)
    G = 1 << math.ceil(math.log2(16 * (2 * X + 1)))
    ind = np.zeros(G)
    for a in A:
        ind[a % G] = 1
        ind[(-a) % G] = 1
    F = np.fft.fft(ind).real  # F(2 pi k/G) = sum_{a in A'} e^{-i a x}, real since A' symmetric
    K = float(-F.min())
    mu = float(np.abs(F).mean())
    u = F + K
    pos = np.array(sorted(set(A) | {-a for a in A}))
    S = set(pos.tolist())
    T = tmax or 2 * X
    rows = []
    for t in range(1, T + 1):
        Bt = [a for a in pos if (a - t) in S and (a + t) not in S]
        if not Bt:
            rows.append((0, 0.0, 0.0, 0.0))
            continue
        b = np.zeros(G)
        for a in Bt:
            b[a % G] = 1
        g = np.fft.fft(b)
        ag = np.abs(g)
        q1 = np.minimum(ag, 3 * u)
        q2 = np.maximum(ag - 3 * u, 0)
        rows.append((len(Bt), float(ag.mean()), float(q1.mean()), float((q2 ** 2).mean())))
    R = np.array(rows)
    nb, g1, q1, q2 = R[:, 0], R[:, 1], R[:, 2], R[:, 3]
    out = {"family": name, "n": n, "X": X, "C": X / n, "R": K / 2 / math.sqrt(n), "K": K, "mu": mu,
           "mean_Bt": float(nb.mean()), "mean_Bt_over_K2": float(nb.mean() / K ** 2),
           "mean_g1_over_K": float(g1.mean() / K), "mean_q1_over_K": float(q1.mean() / K),
           "s1": float((q1 ** 2).mean() / K ** 2), "s2": float(q2.mean() / (K ** 3 * mu)),
           "budget_use": float(nb.mean() / (K * mu * (q1 ** 2).mean() + q2.mean() + 1e-300)),
           "max_q1_over_K": float(q1.max() / K)}
    print(json.dumps(out), flush=True)
    fh.write(json.dumps(out) + "\n")
    fh.flush()


def main():
    os.makedirs("examples/e76", exist_ok=True)
    rng = np.random.default_rng(20261019)
    with open(OUT, "w") as fh:
        sb = json.load(open("examples/smallN_best.json"))
        for k in ("24", "36"):
            analyse(f"smallN_{k}", sb[k]["A"], fh)
        for q in (7, 11, 13, 19, 23, 31):
            A, _ = bu(q)
            analyse(f"bu_q{q}", A, fh)
        for q in (13, 23, 43):
            S, v = singer(q)
            analyse(f"singer_diff_q{q}", sorted({b - a for a in S for b in S if b > a}), fh)
        for fn, tag in (("examples/e68/e68.jsonl", "e68"), ("examples/e72/e72c_n128_C6.jsonl", "e72c_C6"),
                        ("examples/e72/e72c_n512_C3.jsonl", "e72c_C3")):
            for i, line in enumerate(open(fn)):
                if i >= 3:
                    break
                analyse(f"{tag}_{i}", json.loads(line)["A"], fh)
        for n in (128, 512):  # tapered random (front-loaded profile, sqrt(n log n)-type M)
            X = 3 * n
            m = np.arange(1, X + 1)
            p = 2 * n / X * (1 - m / (X + 1)) * 1.0
            A = m[rng.random(X) < p].tolist()
            analyse(f"tapered_random_{n}", A, fh)
        for n in (128, 512):
            analyse(f"interval_{n}", list(range(1, n + 1)), fh)


if __name__ == "__main__":
    main()
