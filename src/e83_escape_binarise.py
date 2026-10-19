"""E83 — can binary sets inherit the positivity of the second-order extremal escape (PROOFS P61(b))?

Profile: p(t) = φ(w*(t)²), w* = autocorrelation of the E82 optimiser G* (N = 320), so the box ratio is C = 1/D ≈ 8.57.
Weighted escape: P_X + g_X with J = round(X^alpha) Fejér-type packets of shape w* at random centres (P61(b)); its exact
minimum (FFT, 16X grid) is reported as the weighted benchmark R_esc = M_esc / sqrt(Σ c_k).
Binary seeds (both with the SAME block counts afterwards, enforced by e83_sa's block moves):
  "escape":  b_k ~ Bernoulli(clip(p_k + r_k, 0, 1))   (inherits the packet structure);
  "random":  b_k ~ Bernoulli(p_k).
Then block-preserving SA (src/e83_sa.c). Compare R_best(escape) vs R_best(random) at X = 1024, 2048, 4096.
HEURISTIC / NUMERICAL (grid minima). Output: examples/e83/e83.jsonl.  Usage: python src/e83_escape_binarise.py
"""
import json
import math
import os
import subprocess
import sys

import numpy as np

OUT = "examples/e83/e83.jsonl"  # run 1 rows (seed by clipped Bernoulli) carry no "seeding" key; run 2 rows have it
BIN = "src/.build/e83_sa"


def wstar():
    rows = [json.loads(l) for l in open("examples/e82/e82.jsonl")]
    r = max((x for x in rows if x["N"] == 320), key=lambda x: x["D"])
    g = np.array(r["g"])
    N = len(g)
    c = np.append(np.correlate(g, g, "full")[N - 1:] / (g @ g), 0.0)
    return lambda t: np.interp(np.abs(t), np.arange(N + 1) / N, c, right=0.0)


def phi(x):
    return (1 - np.sqrt(np.clip(1 - x, 0, None))) / 2


def escape(X, alpha, rng, w):
    k = np.arange(1, X + 1)
    t = k / X
    wk = w(t)
    p = phi(wk * wk)
    J = max(1, int(round(X ** alpha)))
    th = rng.uniform(0, 2 * np.pi, J)
    c = 1 / math.sqrt(32 * J)
    r = 4 * c * wk * np.cos(np.outer(k, th)).sum(1)
    coef = p + r
    # exact weighted minimum on a fine grid (FFT of the cosine series)
    L = 16 * X
    spec = np.zeros(L)
    spec[1:X + 1] = coef
    vals = np.real(np.fft.fft(spec))  # Σ coef_k cos(2π k j / L)
    M_esc = -vals.min()
    return p, r, coef, J, M_esc


def run_sa(X, A, b, iters, restarts, seed, T0):
    inp = " ".join(map(str, A))
    out = subprocess.run([BIN, str(X), str(b), str(iters), str(restarts), str(seed), str(T0)], input=inp,
                         capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def main():
    os.makedirs("examples/e83", exist_ok=True)
    os.makedirs("src/.build", exist_ok=True)
    subprocess.run(["cc", "-O3", "-march=native", "-o", BIN, "src/e83_sa.c", "-lm"], check=True)
    w = wstar()
    Xs = [int(a) for a in sys.argv[1:]] or [1024, 2048, 4096]
    with open(OUT, "a") as fh:
        for X in Xs:
            for seed in (1, 2):
                rng = np.random.default_rng(1000 * X + seed)
                p, r, coef, J, M_esc = escape(X, 0.6, rng, w)
                R_esc = M_esc / math.sqrt(coef.sum())
                k = np.arange(1, X + 1)
                # identical block counts round(sum p) per block of 16 (fix of run 1, whose clipped Bernoulli seed
                # inflated the density): escape seed = top values of p + r in each block; random seed = uniform.
                A_esc, A_rnd = [], []
                carry = 0.0
                for lo in range(0, X, 16):
                    blk = np.arange(lo, min(lo + 16, X))
                    tgt = p[blk].sum() + carry
                    cnt = int(round(tgt))
                    carry = tgt - cnt
                    A_esc += (k[blk][np.argsort(-coef[blk])[:cnt]]).tolist()
                    A_rnd += (k[rng.choice(blk, cnt, replace=False)]).tolist()
                for name, A in (("escape", A_esc), ("random", A_rnd)):
                    res = run_sa(X, A, 16, 4_000_000 if X <= 2048 else 2_000_000, 3, seed, 0.3)
                    row = {"seeding": "block-count", "X": X, "seed": seed, "init": name, "J": J, "alpha": 0.6, "R_esc_weighted": R_esc,
                           "n": res["n"], "C": X / res["n"], "R_init": res["R_init"], "R_best": res["R_best"],
                           "A": res["A"]}
                    fh.write(json.dumps(row) + "\n")
                    fh.flush()
                    print(json.dumps({k2: v for k2, v in row.items() if k2 != "A"}), flush=True)


if __name__ == "__main__":
    main()
