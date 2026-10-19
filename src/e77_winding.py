"""E77 — the zero-set reformulation S(A) <= M(A) (NOTEBOOK 2026-10-19 cont. 9).

G(z) = sum_{a in A} z^a.  Since Re G >= -M on the circle, G(D) lies in {Re w > -M}, so mu + G is zero-free in the open
disk for mu >= M.  Define S(A) = sup{mu > 0 : mu + G has a zero in |z| < 1} = sup{mu : -mu in G(D)} <= M(A).
By the argument principle, #zeros of mu + G in D = winding number W(mu) of the curve x -> G(e^{ix}) around -mu, and
W(mu) = sum over crossings of the ray (-inf, -mu) (points with Im G = 0, Re G < -mu) of the crossing sign.
"Chowla-S": S(A) >= c sqrt|A| for all A would imply Chowla.  This script measures S/sqrt(n) and S/M.
W(mu) by the argument principle on a 64X-point FFT sample of the curve (angle sum); S by a 600-point mu-scan from M
down, then bisection (assumes no finer transitions).
Cross-check for small X: numpy.roots of mu + G at mu = 0.98 S and 1.02 S.
NUMERICAL (uncertified).  Usage: python src/e77_winding.py -> examples/e77/e77.jsonl
"""
import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, "src")
from e67_zoo import bu  # noqa: E402
from singer import singer  # noqa: E402

OUT = "examples/e77/e77.jsonl"


def analyse(name, A, fh):
    A = sorted(set(int(a) for a in A))
    n, X = len(A), max(A)
    Gs = 1 << math.ceil(math.log2(64 * X))
    c = np.zeros(Gs, dtype=complex)
    c[np.array(A)] = 1
    Gv = np.fft.ifft(c) * Gs  # G(e^{i 2 pi k / Gs})
    M = float(-Gv.real.min())

    def wind(mu):  # argument principle on the sampled curve: number of zeros of mu + G in the open disk
        w = Gv + mu
        return int(round(float(np.angle(np.roll(w, -1) / w).sum()) / (2 * np.pi)))

    grid = np.linspace(M * 1.001, M * 1e-3, 600)
    S, below = 0.0, None
    for i, mu in enumerate(grid):
        if wind(mu) != 0:
            lo, hi = mu, (grid[i - 1] if i else M * 1.001)  # wind(lo) != 0, wind(hi) == 0
            for _ in range(40):
                mid = 0.5 * (lo + hi)
                if wind(mid) != 0:
                    lo = mid
                else:
                    hi = mid
            S = lo
            break
    out = {"family": name, "n": n, "X": X, "M_grid": M, "R": M / math.sqrt(n), "S": S, "S_over_sqrt_n": S / math.sqrt(n),
           "S_over_M": S / M if M > 0 else None, "W_small_mu": wind(1e-6)}
    if X <= 120 and S > 0:
        chk = []
        for mu in (0.98 * S, 1.02 * S):
            coeffs = np.zeros(X + 1)
            coeffs[np.array(A)] = 1
            coeffs[0] = mu
            r = np.roots(coeffs[::-1])
            chk.append(int((np.abs(r) < 1 - 1e-9).sum()))
        out["roots_inside_at_0.98S_1.02S"] = chk
    print(json.dumps(out), flush=True)
    fh.write(json.dumps(out) + "\n")
    fh.flush()


def main():
    os.makedirs("examples/e77", exist_ok=True)
    rng = np.random.default_rng(20261019)
    with open(OUT, "w") as fh:
        sb = json.load(open("examples/smallN_best.json"))
        for k in sorted(sb, key=int):
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
        for C in (1.5, 3, 10):
            for n in (64, 256, 1024):
                X = int(C * n)
                analyse(f"random_C{C}_n{n}", (rng.permutation(X)[:n] + 1).tolist(), fh)
        for n in (64, 256):
            analyse(f"interval_{n}", list(range(1, n + 1)), fh)
            analyse(f"interval_far_{n}", list(range(5 * n, 6 * n)), fh)
            analyse(f"lacunary_like_{n}", sorted({int(1.02 ** j) + j for j in range(n)}), fh)
            analyse(f"evens_odd1_{n}", [1] + list(range(2, 2 * n, 2)), fh)


if __name__ == "__main__":
    main()
