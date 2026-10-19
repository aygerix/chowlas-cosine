"""E100b: falsification search for the positivity-resolution lemma PR(r=1) (NOTEBOOK cont. 20.3).
Window Omega = -Omega in T = R/Z, a union of J disjoint symmetric arc pairs [a_i, b_i] u [-b_i, -a_i] (plus optionally
[-b0, b0]). hat(k) = sum over arcs of (sin 2 pi k b - sin 2 pi k a)/(pi k). Minimize the unresolved fraction
delta_L = 1 - sum_{|k|<=L} hat(k)^2 / |Omega| subject to hat(k) >= 0 for 1 <= k <= L and |Omega| <= 1/2.
SLSQP from random starts. NUMERICAL heuristic search: a value below 0.0972 would refute PR's conjectured constant."""
import json, sys
import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(20261022)
L = int(sys.argv[1]) if len(sys.argv) > 1 else 16
K = np.arange(1, L + 1)

def parts(z, central):
    z = np.sort(np.clip(z, 0, 0.5))
    pairs = z.reshape(-1, 2)
    meas = 2 * (pairs[:, 1] - pairs[:, 0]).sum()
    hk = (2 * (np.sin(2 * np.pi * np.outer(K, pairs[:, 1])) - np.sin(2 * np.pi * np.outer(K, pairs[:, 0]))).sum(1)) / (2 * np.pi * K) * 2
    if central:   # first pair starts at 0: arc [-b, b]
        pass
    return meas, hk

def hat(z):
    z = np.sort(np.clip(z, 0, 0.5)); pairs = z.reshape(-1, 2)
    meas = 2 * (pairs[:, 1] - pairs[:, 0]).sum()
    hk = 2 * (np.sin(2 * np.pi * np.outer(K, pairs[:, 1])) - np.sin(2 * np.pi * np.outer(K, pairs[:, 0]))).sum(1) / (2 * np.pi * K)
    return meas, hk          # Omega's coefficient at +-k (real, even)

def delta(z):
    meas, hk = hat(z)
    if meas <= 1e-9: return 1.0
    return 1 - (meas ** 2 + 2 * (hk ** 2).sum()) / meas

best = (1.0, None)
for J in range(1, 7):
    for trial in range(300):
        z0 = np.sort(rng.random(2 * J) * 0.5)
        if rng.random() < 0.5: z0[0] = 0.0
        cons = [{'type': 'ineq', 'fun': lambda z: hat(z)[1]},
                {'type': 'ineq', 'fun': lambda z: 0.5 - hat(z)[0]},
                {'type': 'ineq', 'fun': lambda z: hat(z)[0] - 1e-4}]
        r = minimize(delta, z0, method='SLSQP', bounds=[(0, 0.5)] * (2 * J), constraints=cons,
                     options={'maxiter': 500, 'ftol': 1e-12})
        z = r.x; meas, hk = hat(z)
        if hk.min() >= -1e-9 and 1e-4 <= meas <= 0.5 + 1e-9:
            d = delta(z)
            if d < best[0]: best = (d, (J, np.sort(z).round(6).tolist(), float(meas)))
    print(json.dumps({'L': L, 'J_max': J, 'best_delta': best[0], 'witness': best[1]}), flush=True)
