"""E63 post-processing: for each SA optimum (examples/e63/e63_raw.jsonl) report n, X, C = X/n, R (16x grid), the front
ratio fr(t) = s_A(tX)*3X/(n(tX+1)) at t = 0.05, 0.2, 1, and the best P31 lower bound on R (E55 method, three constants)."""
import json, math
import numpy as np
for l in open("examples/e63/e63_raw.jsonl"):
    r = json.loads(l); A = np.asarray(r["A"]); n = len(A); X = int(A.max())
    G = 16 << math.ceil(math.log2(X)); c = np.zeros(G); c[A] = 1; M = -np.fft.fft(c).real.min()
    fr = {f"{t:g}": round(float((np.clip(1 - A / (int(t * X) + 1), 0, None) ** 2).sum()) * 3 * X / (n * (int(t * X) + 1)), 3) for t in (0.05, 0.2, 1.0)}
    lb = {}
    for rho, lab in ((0.7698, "beckner"), (None, "elem"), (0.687, "num")):
        b = 0.0
        for w in range(1, X + 1):
            s = float((np.clip(1 - A / (w + 1), 0, None) ** 2).sum()); W = 2 * (w + 1) / 3 + 1 / (3 * (w + 1))
            C = (0.811 * (X + w + 1) + 0.2367) if rho is None else rho * (X + w + 1)
            b = max(b, (W * n - C * s) / (2 * (C - W)))
        lb[lab] = round(math.sqrt(max(b, 0) / n), 4)
    print(json.dumps(dict(X_box=r["X"], C_target=round(r["X"] / r["n"], 2), n=n, X=X, R=round(M / math.sqrt(n), 4),
                          front_ratio=fr, P31_LB_R=lb, A=A.tolist())), flush=True)
