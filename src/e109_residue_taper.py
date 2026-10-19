"""E109: residue-taper (Zhat model set) profile check (lead, 2026-10-19, CSTAR A3).
A = union over r in W0 (symmetric subset of Z_Q) of the initial segment {a = r mod Q, 1 <= a < u_r X} (u_{-r} = u_r).
Continuous-u prediction: f(t/Q + tau/X) ~ (X/(2 pi Q tau)) * sum_{r in W0} cos(2 pi r t/Q) sin(2 pi tau u_r).
Usage: python src/e109_residue_taper.py Q X seed
"""
import sys, numpy as np
Q, X, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
rng = np.random.default_rng(seed)
W0 = [r for r in range(Q) if rng.random() < 0.5]
W0 = sorted(set(W0) | {(-r) % Q for r in W0})
u = {}
for r in W0:
    if r not in u: u[r] = u[(-r) % Q] = rng.random()
A = np.array(sorted(a for a in range(1, X + 1) if (a % Q) in u and a < u[a % Q] * X), dtype=float)
n = len(A)
def f(x): return np.cos(2 * np.pi * np.outer(np.atleast_1d(x), A)).sum(1)
W0a = np.array(W0, dtype=float); ua = np.array([u[r] for r in W0])
worst = 0.0
for t in [1, 2, 3, Q // 3]:
    for tau in [1.3, 2.7, 5.1, 9.9]:
        x = t / Q + tau / X
        pred = X / (2 * np.pi * Q * tau) * np.sum(np.cos(2 * np.pi * W0a * t / Q) * np.sin(2 * np.pi * tau * ua))
        val = f(x)[0]
        worst = max(worst, abs(val - pred))
        print(f"t={t:4d} tau={tau:5.1f} direct={val:10.2f} pred={pred:10.2f}")
xs = np.linspace(0, 0.5, 400001)
fv = np.concatenate([f(xs[i:i + 20000]) for i in range(0, len(xs), 20000)])
M = -fv.min()
print(f"n={n} |W0|={len(W0)} Q={Q} X={X} max|direct-pred|={worst:.2f} gridM={M:.2f} R={M/np.sqrt(n):.3f} sqrt(X/Q)={np.sqrt(X/Q):.1f}")
