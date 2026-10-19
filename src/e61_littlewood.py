"""E61: one-sided Littlewood problem.  T(x) = sum_{j=1}^n cos(j x - theta_j) (unit amplitudes, any phases).
Claim (P34, lead): P31 applies verbatim to any coefficients with |b_j| <= 1 and energy sum|b_j|^2 >= delta n, delta > 0.4055;
for unit amplitudes it gives  -min T >= c sqrt(n)  (c ~ 0.23-0.28 elementary).  Adversarial test: MAXIMISE min T over
(a) all phases (L-BFGS on a soft-min, annealed), (b) +-1 signs (simulated annealing), and report -min T / sqrt(n) after a
fine-grid + Newton refinement.  Also checks the P31 chain numerically for each optimum.
Usage: python src/e61_littlewood.py > examples/e61/e61.jsonl      (HEURISTIC search; the bound is the theorem)
"""
import json, math, sys
import numpy as np
from scipy.optimize import minimize

def tmin(theta, refine=64):
    n = len(theta); j = np.arange(1, n + 1); G = refine * n
    x = 2 * np.pi * np.arange(G) / G
    c = np.zeros(G, complex); c[1:n + 1] = np.exp(-1j * theta)
    T = (np.fft.ifft(c) * G).real          # sum_j cos(j x - theta_j)
    k = int(np.argmin(T)); y = x[k]
    for _ in range(30):                     # Newton polish
        d1 = -(j * np.sin(j * y - theta)).sum(); d2 = -(j * j * np.cos(j * y - theta)).sum()
        if d2 <= 0: break
        y -= d1 / d2
    return min(T.min(), np.cos(j * y - theta).sum())

def opt_phases(n, restarts, seed):
    rng = np.random.default_rng(seed); j = np.arange(1, n + 1); G = 16 * n
    x = 2 * np.pi * np.arange(G) / G; JX = np.outer(x, j)
    best = None
    for r in range(restarts):
        th = rng.uniform(0, 2 * np.pi, n)
        for beta in (2.0, 8.0, 32.0, 128.0):
            def obj(t):
                arg = JX - t; T = np.cos(arg).sum(1); z = -beta * (T - T.min()); p = np.exp(z); p /= p.sum()
                m = T.min() - np.log(np.exp(-beta * (T - T.min())).sum()) / beta
                g = (p[:, None] * np.sin(arg)).sum(0)      # d m / d theta
                return -m, -g
            th = minimize(obj, th, jac=True, method="L-BFGS-B", options={"maxiter": 400}).x
        v = tmin(th)
        if best is None or v > best[0]: best = (v, th.copy())
    return best

def sa_signs(n, iters, seed):
    rng = np.random.default_rng(seed); j = np.arange(1, n + 1); G = 8 * n
    x = 2 * np.pi * np.arange(G) / G; C = np.cos(np.outer(j, x))
    e = rng.choice([-1.0, 1.0], n); T = e @ C; m = T.min(); bm, be = m, e.copy(); T0 = 0.3 * math.sqrt(n)
    for it in range(iters):
        k = rng.integers(n); T2 = T - 2 * e[k] * C[k]; m2 = T2.min(); tmp = T0 * (1e-3) ** (it / iters)
        if m2 >= m or rng.random() < math.exp((m2 - m) / tmp):
            e[k] = -e[k]; T = T2; m = m2
            if m > bm: bm, be = m, e.copy()
    th = np.where(be > 0, 0.0, np.pi)
    return tmin(th), be

def p31_lb(n, rho=0.811):
    best = 0
    for w in range(1, n + 1):
        W = 1 + 2 * sum((1 - k / (w + 1)) ** 2 for k in range(1, w + 1)); S = (W - 1) / 2
        C = rho * (n + w + 1) + 0.2367
        best = max(best, (W * n / 2 - C * S / 2) / (C - W))
    return math.sqrt(best / n)

if __name__ == "__main__":
    for n in (8, 16, 32, 64, 128, 256):
        lb = p31_lb(n)
        v, th = opt_phases(n, restarts=6 if n <= 64 else 3, seed=n)
        print(json.dumps(dict(kind="phases", n=n, best_minT=round(v, 4), negmin_over_sqrt_n=round(-v / math.sqrt(n), 4),
                              P31_elem_LB=round(lb, 4))), flush=True)
        v2, e = sa_signs(n, iters=200000 if n <= 64 else 400000, seed=n)
        print(json.dumps(dict(kind="signs", n=n, best_minT=round(v2, 4), negmin_over_sqrt_n=round(-v2 / math.sqrt(n), 4),
                              P31_elem_LB=round(lb, 4), signs="".join("+" if s > 0 else "-" for s in e))), flush=True)
