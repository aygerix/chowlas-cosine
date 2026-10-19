"""E105: PR(1) large-peak test (STATE handoff cont. 24-25 (f); PROOFS P73(b)).
P73 proves U >= delta^2 mu / 3 whenever g(0) <= (4 - 5 delta)/3, where g = P_L 1_Omega, U = unresolved mass.
Here: minimize the unresolved fraction delta_L = U/|Omega| over symmetric unions of J arc pairs, subject to
hat(k) >= 0 (1 <= k <= L), |Omega| <= 1/2 AND the large-peak constraint g(0) = |Omega| + 2 sum_k hat(k) >= gamma.
NUMERICAL (SLSQP, random starts). Question: how small can delta_L be in the large-peak regime gamma >= 4/3?
If it stays >= ~0.09, the large-peak case is no worse than the conjectured c* = 1/2 - 4/pi^2."""
import json, sys
import numpy as np
from scipy.optimize import minimize
L = int(sys.argv[1]); gamma = float(sys.argv[2]); trials = int(sys.argv[3]) if len(sys.argv) > 3 else 200
rng = np.random.default_rng(1000 * L + int(100 * gamma))
K = np.arange(1, L + 1)

def hat(z):
    z = np.sort(np.clip(z, 0, 0.5)); pairs = z.reshape(-1, 2)
    meas = 2 * (pairs[:, 1] - pairs[:, 0]).sum()
    hk = 2 * (np.sin(2 * np.pi * np.outer(K, pairs[:, 1])) - np.sin(2 * np.pi * np.outer(K, pairs[:, 0]))).sum(1) / (2 * np.pi * K)
    return meas, hk

def delta(z):
    meas, hk = hat(z)
    if meas <= 1e-9: return 1.0
    return 1 - (meas ** 2 + 2 * (hk ** 2).sum()) / meas

def g0(z):
    meas, hk = hat(z); return meas + 2 * hk.sum()

best = (1.0, None)
for J in range(1, 9):
    for t in range(trials):
        z0 = np.sort(rng.random(2 * J) * 0.5)
        if rng.random() < 0.7: z0[0] = 0.0
        cons = [{'type': 'ineq', 'fun': lambda z: hat(z)[1]},
                {'type': 'ineq', 'fun': lambda z: 0.5 - hat(z)[0]},
                {'type': 'ineq', 'fun': lambda z: hat(z)[0] - 1e-4},
                {'type': 'ineq', 'fun': lambda z: g0(z) - gamma}]
        r = minimize(delta, z0, method='SLSQP', bounds=[(0, 0.5)] * (2 * J), constraints=cons,
                     options={'maxiter': 800, 'ftol': 1e-12})
        z = r.x; meas, hk = hat(z)
        if hk.min() >= -1e-9 and 1e-4 <= meas <= 0.5 + 1e-9 and g0(z) >= gamma - 1e-9:
            d = delta(z)
            if d < best[0]: best = (d, (J, np.sort(z).round(6).tolist(), float(meas), float(g0(z))))
    print(json.dumps({'L': L, 'gamma': gamma, 'J_max': J, 'best_delta': best[0], 'witness': best[1]}), flush=True)
