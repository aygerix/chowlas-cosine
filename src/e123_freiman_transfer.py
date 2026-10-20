r"""E123 (lead, 2026-10-20): check of the P80c 1D-transfer, after the advisor's counterexample.
(a) Counterexample to the z₁-only bound: d = 3, T = {±e₂, ±e₃}, V = 8: K_d = 4 but K₁D < 4 although Σz₁² = 0.
(b) Repaired bound (advisor): K₁D >= K_d − (π²/(2V²))·Σ_{z∈T}(Σ_{k<d}|z_k|)², via base-V digits of x
    (coordinate d exact, coordinates k < d within 1/(2V)) and Taylor at a minimiser. Adversarial test on random odd
    one-rep lifts T ⊂ [−W·n, W·n]^d (d = 2, 3, 4) and random V > 2Wn: report min over trials of K₁D − (K_d − loss)
    (must be >= 0 up to numerical error) and of K₁D − (K_d − loss_z1only) (expected negative somewhere for d >= 3).
All minima NUMERICAL (dense grid + BFGS; d-dim grid of 24 points per unit of max degree, capped).
"""
import sys, json, math, itertools
import numpy as np
from scipy.optimize import minimize

def min1d(S, starts=64):
    S = np.asarray(S, dtype=float)
    G = 1 << int(math.ceil(math.log2(32 * (np.abs(S).max() + 1))))
    A = np.zeros(G); np.add.at(A, (S.astype(np.int64)) % G, 1.0)
    v = np.fft.fft(A).real
    best = v.min()
    for i in np.argsort(v)[:starts]:
        r = minimize(lambda t: (np.cos(2 * np.pi * S * t[0]).sum(), [-2 * np.pi * (S * np.sin(2 * np.pi * S * t[0])).sum()]),
                     [i / G], jac=True, method="BFGS")
        best = min(best, r.fun)
    return float(best)

def mind(Z, starts=40, rng=None):
    Z = np.asarray(Z, dtype=float); d = Z.shape[1]
    f = lambda x: (np.cos(2 * np.pi * Z @ x).sum(), -2 * np.pi * (np.sin(2 * np.pi * Z @ x) @ Z))
    best = 1e9
    rng = rng or np.random.default_rng(0)
    pts = rng.random((4000 * d, d))
    vals = np.array([f(x)[0] for x in pts])
    for i in np.argsort(vals)[:starts]:
        r = minimize(f, pts[i], jac=True, method="BFGS")
        best = min(best, r.fun)
    return float(best)

out = {}
# (a)
T = [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]; V = 8
S = [z[0] + V * z[1] + V * V * z[2] for z in T]
out["counterexample"] = {"K_d": 4.0, "K_1D": -min1d(S), "sum_z1_sq": 0, "repaired_loss": math.pi ** 2 / (2 * V * V) * sum((abs(z[0]) + abs(z[1])) ** 2 for z in T)}
# (b)
rng = np.random.default_rng(20261020)
rows = []
for d in (2, 3, 4):
    for trial in range(40):
        n = int(rng.integers(3, 7)); W = 1; m = int(rng.integers(3, 9))
        half = set()
        while len(half) < m:
            z = tuple(int(t) for t in rng.integers(-W * n, W * n + 1, size=d))
            if any(z) and tuple(-t for t in z) not in half: half.add(z)
        T = [z for z in half] + [tuple(-t for t in z) for z in half]
        V = int(rng.integers(2 * W * n + 1, 6 * W * n + 2))
        S = [sum(z[k] * V ** k for k in range(d)) for z in T]
        if len(set(S)) < len(S): continue
        Kd = -mind(T, rng=rng); K1 = -min1d(S)
        loss = math.pi ** 2 / (2 * V * V) * sum(sum(abs(z[k]) for k in range(d - 1)) ** 2 for z in T)
        loss1 = math.pi ** 2 / (2 * V * V) * sum(z[0] ** 2 for z in T)
        rows.append((d, K1 - (Kd - loss), K1 - (Kd - loss1)))
for d in (2, 3, 4):
    r = [x for x in rows if x[0] == d]
    out[f"d{d}"] = {"trials": len(r), "min_margin_repaired": min(x[1] for x in r), "min_margin_z1only": min(x[2] for x in r),
                    "violations_z1only": sum(x[2] < -1e-6 for x in r)}
print(json.dumps(out), flush=True)
