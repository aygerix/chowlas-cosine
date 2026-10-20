r"""E119e: exact K for a finished one-rep SA run whose driver died in true_min (G = 2^15 grid exceeds the memory cap).
Rebuilds the lift from fd_in/fd_out, scans a G×G grid with rfft2 (f is even, so the half-plane suffices), refines the
lowest grid cells with BFGS. NUMERICAL (not interval-certified). Usage: python src/e119e_trueK.py <tag> G1 [G2 ...]
"""
import sys, json, math
import numpy as np
from scipy.optimize import minimize
sys.path.insert(0, "src")
from e116_jl_taper import Fval

tag = sys.argv[1]
lines = open(f"examples/e116/fd_in_{tag}.txt").read().split("\n")
reps = []
for ln in lines[1:]:
    t = ln.split()
    if not t:
        continue
    k = int(t[0]); xs = list(map(int, t[1:1 + 2 * k]))
    reps.append([(xs[2 * i], xs[2 * i + 1]) for i in range(k)])
out = open(f"examples/e116/fd_out_{tag}.txt").read().split("\n")
idx = [int(t) for t in out[1].split()]
pairs = np.array([reps[c][i] for c, i in enumerate(idx)], dtype=np.int64)
w = np.ones(len(pairs))
res = {"tag": tag, "pairs": len(pairs), "D": 2 * len(pairs), "sa_gridK": float(out[0]), "L": int(np.abs(pairs).max())}
best = (np.inf, None)
for G in map(int, sys.argv[2:]):
    A = np.zeros((G, G))
    np.add.at(A, (pairs[:, 0] % G, pairs[:, 1] % G), 1.0)
    np.add.at(A, ((-pairs[:, 0]) % G, (-pairs[:, 1]) % G), 1.0)
    V = np.fft.rfft2(A).real; del A
    cand = np.argpartition(V, 400, axis=None)[:400]
    cand = cand[np.argsort(V.flat[cand])]
    gmin = float(V.flat[cand[0]])
    seen = []
    for c in cand:
        x0 = np.array(np.unravel_index(c, V.shape), dtype=float) / G
        if any(np.max(np.abs(((x0 - s + 0.5) % 1) - 0.5)) < 2.0 / G for s in seen):
            continue
        seen.append(x0)
        r = minimize(lambda x: Fval(pairs, w, x), x0, jac=True, method="BFGS", options={"gtol": 1e-10})
        if r.fun < best[0]:
            best = (float(r.fun), (r.x % 1).tolist())
        if len(seen) >= 48:
            break
    del V
    res[f"grid_min_G{G}"] = gmin
    res[f"refined_min_after_G{G}"] = best[0]
res["K_true"] = -best[0]; res["xi"] = best[1]
res["ratio"] = res["D"] / best[0] ** 2
res["R1D_upper"] = -best[0] / math.sqrt(res["D"])
print(json.dumps(res), flush=True)
