"""Elementary (Lean-friendly) bound on rho_L: for v >= 0, ||v||=1 on N = L+1 points,
   (E1) ||v*v||^2 <= N - 2 sum_{j<L} a_j(1-a_j),  a_j = sum_{i<=j} v_i^2   (C-S per s + Abel summation)
   (E2) ||v*v||^2 <= (sum v)^2                                             (max_s (v*v)_s <= 1)
So rho_L <= sup_v min(E1, E2)/N.  This script estimates that sup (and checks E1, E2 against the true ||v*v||^2)."""
import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(1)
def parts(z):
    v = z * z; v = v / np.sqrt((v * v).sum()); a = np.cumsum(v * v)
    N = len(v); e1 = N - 2 * (a[:-1] * (1 - a[:-1])).sum(); e2 = v.sum() ** 2
    c = np.convolve(v, v); return v, e1, e2, c @ c
def obj(z, N, t):   # smooth max of min(E1,E2) via soft-min
    _, e1, e2, _ = parts(z)
    return -(-t * np.log(np.exp(-e1 / t) + np.exp(-e2 / t)))
for N in (5, 20, 60, 150):
    best = 0; worst_check = 1e9
    for trial in range(40):
        z0 = rng.random(N) ** (1 + 3 * rng.random())
        r = minimize(obj, z0, args=(N, 0.01 * N), method="L-BFGS-B", options={"maxiter": 3000})
        v, e1, e2, true = parts(r.x)
        best = max(best, min(e1, e2) / N); worst_check = min(worst_check, min(e1, e2) - true)
    print(N, "sup min(E1,E2)/N ~", round(best, 4), " min slack vs true ||v*v||^2:", round(worst_check, 6), flush=True)
