"""E73 — Gaussian-threshold ("multiscale Bohr") sets: the escape class of the HBCG reduction (NOTEBOOK 2026-10-19
night, cont. 3: a counterexample must be multiscale Bohr with growing rank).

A = { m in [1, X] : Phi(m) > tau(m/X) },  Phi(m) = sqrt(2/r) * sum_{j<r} cos(2 pi alpha_j m + phi_j),
tau(t) = Phi_N^{-1}(1 - p(t)), with p(t) = p0 * (1 - t)^gam (front-loaded density profile).
alpha_j, phi_j uniform random (seeded). r = 0 means the Bernoulli baseline (independent rounding of p).

Model prediction (lead, heuristic): level-k Hermite profiles ~ He_{k-1}(tau) phi(tau) must be PD in t to avoid
sidelobes of height ~ X r^{-k/2}; PD up to level K forces tau >~ 2 sqrt(K), and then the Hermite mass sits at
degree ~ tau^2 > K, i.e. in the bulk. So R should not go below the bulk-only baseline in a way that decreases with X.

M is estimated on an oversampled FFT grid and refined by golden-section on the best grid cells (UNCERTIFIED).
Also reported: beta_K = share of ||f||_2^2 at |f| <= K sqrt(n) (bulk share), K = 3, from the same grid.
Usage: python src/e73_gauss_threshold.py X seed  (prints one JSON line per configuration)
"""
import json
import sys

import numpy as np
from scipy.special import ndtri


def make_set(X, r, p0, gam, rng):
    m = np.arange(1, X + 1, dtype=np.float64)
    t = m / X
    p = p0 * (1.0 - t) ** gam
    if r == 0:
        return m[rng.random(X) < p].astype(np.int64)
    tau = ndtri(np.clip(1.0 - p, 1e-300, 1 - 1e-16))
    al = rng.random(r)
    ph = 2 * np.pi * rng.random(r)
    Phi = np.zeros(X)
    for j in range(r):
        Phi += np.cos(2 * np.pi * al[j] * m + ph[j])
    Phi *= np.sqrt(2.0 / r)
    return m[Phi > tau].astype(np.int64)


def fvals(A, x):
    out = np.zeros_like(x)
    for chunk in np.array_split(A, max(1, len(A) // 4096)):
        out += np.cos(np.outer(x, chunk)).sum(axis=1)
    return out


def minimum(A, X, over=8):
    N = 1 << int(np.ceil(np.log2(over * X)))
    c = np.zeros(N)
    c[A % N] += 1.0
    g = np.fft.rfft(c).real  # f(2 pi k / N), k = 0..N/2
    k0 = np.argsort(g)[:8]
    best = g.min()
    h = 2 * np.pi / N
    for k in k0:
        lo, hi = (k - 1) * h, (k + 1) * h
        for _ in range(40):
            a, b = lo + 0.382 * (hi - lo), lo + 0.618 * (hi - lo)
            fa, fb = fvals(A, np.array([a, b]))
            if fa < fb:
                hi = b
            else:
                lo = a
        v = fvals(A, np.array([(lo + hi) / 2]))[0]
        best = min(best, v)
    return -best, g


def main():
    X = int(sys.argv[1])
    seed = int(sys.argv[2])
    for r in [0, 1, 2, 4, 8, 16, 32, 64, 256, 1024]:
        for p0 in [0.3, 0.5]:
            for gam in [0.0, 0.5, 1.0, 2.0]:
                rng = np.random.default_rng([seed, r, int(p0 * 10), int(gam * 10)])
                A = make_set(X, r, p0, gam, rng)
                n = len(A)
                if n < 10:
                    continue
                M, g = minimum(A, X)
                K = 3.0
                tot = (g ** 2).sum()
                bulk = (g[np.abs(g) <= K * np.sqrt(n)] ** 2).sum()
                print(json.dumps({"X": X, "seed": seed, "r": r, "p0": p0, "gam": gam, "n": n, "C": X / n,
                                  "M": round(float(M), 3), "R": round(float(M / np.sqrt(n)), 4),
                                  "beta3": round(float(bulk / tot), 4),
                                  "maxspike_over_n": round(float(g[int(3 * len(g) / X) + 1:].max() / n), 4)}),
                      flush=True)


if __name__ == "__main__":
    main()
