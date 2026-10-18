"""E26: free-phase analogue — how small can max_t Σ_{j=1}^n cos(j t − θ_j) be?  (Erdélyi 2607.21877 claims >= n^{1/3}/60;
its proof has a gap, LITERATURE.md.)  Minimise a soft-max over a grid of 16n points by Adam on θ, anneal β, then report
the true max (FFT 64n + Newton).  c := max T / sqrt(n/2).  UNCERTIFIED; mechanism probe (most freedom: unit moduli,
arbitrary phases, full support — strictly more freedom than ±1 (E24) and than 0/1 dense roundings).
Usage: python src/freephase_opt.py n iters seed
"""
import sys, math, time
import numpy as np


def true_max(theta):
    n = len(theta); G = 1 << math.ceil(math.log2(64 * n))
    c = np.zeros(G, complex); c[1:n + 1] = np.exp(-1j * theta)
    v = np.real(np.fft.ifft(c)) * G                      # Σ cos(j t_k − θ_j) at t_k = 2πk/G
    k = int(np.argmax(v)); t = 2 * np.pi * k / G; j = np.arange(1, n + 1)
    for _ in range(30):
        d1 = -(j * np.sin(j * t - theta)).sum(); d2 = -(j * j * np.cos(j * t - theta)).sum()
        if d2 >= 0: break
        t -= d1 / d2
    return max(float(v[k]), float(np.cos(j * t - theta).sum()))


if __name__ == "__main__":
    n, iters, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    rng = np.random.default_rng(seed)
    G = 16 * n; ts = 2 * np.pi * np.arange(G) / G; j = np.arange(1, n + 1)
    th = rng.uniform(0, 2 * np.pi, n)
    m = np.zeros(n); v2 = np.zeros(n); lr = 0.05; t0 = time.time(); best = (1e9, th.copy())
    for it in range(iters):
        beta = 2.0 * (1 + 20 * it / iters) / math.sqrt(n)
        ph = np.outer(ts, j) - th                            # G x n
        T = np.cos(ph).sum(1)
        w = np.exp(beta * (T - T.max())); w /= w.sum()
        g = -(w[:, None] * np.sin(ph)).sum(0) * (-1)         # d/dθ_j of Σ w_t T(t) = Σ w_t sin(j t − θ_j)
        m = 0.9 * m + 0.1 * g; v2 = 0.999 * v2 + 0.001 * g * g
        th -= lr * m / (np.sqrt(v2) + 1e-9)
        if it % 50 == 0:
            cur = T.max()
            if cur < best[0]: best = (cur, th.copy())
    Mx = true_max(best[1])
    print(f"n={n} seed={seed} iters={iters} grid c={best[0]/math.sqrt(n/2):.4f} true c={Mx/math.sqrt(n/2):.4f} "
          f"t={time.time()-t0:.0f}s", flush=True)
