"""Profile of the local B-energy E_B(x) = sum_{t in A}|1^_{B_t}(x)|^2 against the height F(x)+K.
Saturation s(x) = E_B(x) / (n (F(x)+K)^2)  (domination |Q1_t| <= 3(F+K) caps the Q1-part at s <= 9).
Prints binned averages and a log-log slope p of E_B ~ (F+K)^p.  UNCERTIFIED floats."""
import json, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, HERE)
from bedert_avg import setup, coef, grid, trunc
from bedert_avg_run import fam

def profile(S, over=8, max_t=200, seed=0):
    st = setup(S, over); N, a, F, K, n = st["N"], st["a"], st["F"], st["K"], st["n"]
    ts = sorted(st["S"])
    if len(ts) > max_t:
        ts = sorted(np.random.default_rng(seed).choice(ts, max_t, replace=False).tolist())
    EB = np.zeros(N); ell = []
    T1 = np.maximum(F, 0); tau = coef(T1, N); FK = F + K
    for t in ts:
        at, amt = np.roll(a, t), np.roll(a, -t)
        h = grid(a * at * (1 - amt), N)
        ah = np.abs(h) ** 2
        EB += ah + ah[(-np.arange(N)) % N]
    EB *= n / (2 * len(ts))
    s = EB / (n * np.maximum(FK, 1e-12))**2 * n  # = EB/(n*FK^2)
    s = EB / (n * np.maximum(FK, 1e-12) ** 2)
    edges = K * np.array([0, 0.25, 0.5, 1, 2, 4, 8, 16, 64, 1e9])
    rows = []
    for lo, hi in zip(edges[:-1], edges[1:]):
        m = (FK >= lo) & (FK < hi)
        if m.sum() == 0: continue
        rows.append(dict(FK_over_K=f"[{lo/K:g},{hi/K:g})", meas=round(m.mean(), 4),
                         Bmass=round(EB[m].sum() / EB.sum(), 3),
                         mean_s=round(float(np.mean(EB[m]) / (n * np.mean(FK[m] ** 2))), 4)))
    m = FK > 0.05 * K
    p = np.polyfit(np.log(FK[m]), np.log(EB[m] + 1e-300), 1, w=None)[0]
    # binned slope using bin means
    return dict(n=n, K=round(K, 2), slope_pointwise=round(float(p), 3), rows=rows)

if __name__ == "__main__":
    for name, S in fam():
        if any(w in name for w in sys.argv[1:]):
            print(name, json.dumps(profile(S)), flush=True)
