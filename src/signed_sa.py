"""E24: one-sided skew for full-support two-valued coefficients (mechanism probe for the dense regime).

L_ε(x) = Σ_{n=1}^{X} ε_n cos(n x), ε ∈ {±1}^X.  ||L||_2^2 = X/2, so c := −min L / sqrt(X/2) is the rounding constant c_E of
the constant profile w = 1/2 (E16: dense sets beat 1/2 only if c_E < 1/sqrt(2(1−ρ)) ≈ 1.33 at ρ ≈ ρ*).  Random signs give
c ≈ sqrt(2 log X); Rudin–Shapiro / Fekete give c ≈ sqrt2·(flatness).  Simulated annealing on single flips, objective
−min over a grid of 8X points, final minimum by FFT + Newton.  UNCERTIFIED; for mechanism discovery only.
Usage: python src/signed_sa.py X iters seed
"""
import sys, math, time
import numpy as np


def true_min_signed(eps, G=None):
    X = len(eps); G = G or (1 << math.ceil(math.log2(64 * X)))
    c = np.zeros(G); c[1:X + 1] = eps
    v = np.real(np.fft.fft(c)); j = int(np.argmin(v)); x = 2 * np.pi * j / G
    n = np.arange(1, X + 1)
    for _ in range(30):
        d1 = -(eps * n * np.sin(n * x)).sum(); d2 = -(eps * n * n * np.cos(n * x)).sum()
        if d2 <= 0: break
        x -= d1 / d2
    return min(float(v[j]), float((eps * np.cos(n * x)).sum()))


if __name__ == "__main__":
    X, iters, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    rng = np.random.default_rng(seed)
    G = 8 * X; xs = 2 * np.pi * np.arange(G) / G; n = np.arange(1, X + 1)
    C = np.cos(np.outer(n, xs))                         # X x G table
    eps = rng.choice([-1.0, 1.0], X); val = eps @ C
    cur = -val.min(); best = (cur, eps.copy()); T0 = 0.05 * math.sqrt(X); t0 = time.time()
    for it in range(iters):
        T = T0 * (1 - it / iters) + 1e-3
        i = int(rng.integers(X)); nv = val - 2 * eps[i] * C[i]; m = -nv.min()
        if m <= cur or rng.random() < math.exp((cur - m) / T):
            eps[i] = -eps[i]; val = nv; cur = m
            if cur < best[0]: best = (cur, eps.copy())
    M = -true_min_signed(best[1])
    print(f"X={X} seed={seed} iters={iters} grid c={best[0]/math.sqrt(X/2):.4f} true c={M/math.sqrt(X/2):.4f} "
          f"sum(eps)={int(best[1].sum())} t={time.time()-t0:.0f}s", flush=True)
    print("eps=" + "".join('+' if e > 0 else '-' for e in best[1]), flush=True)
