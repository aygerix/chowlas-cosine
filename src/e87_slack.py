"""E87 — where does the round-11 certificate (D <= 259/2000, P63) lose against the true D ≈ 0.11667?
Decompose, at the E82 optimiser w* = G*⋆G̃* (N = 320 step factor):
  Schur slack     = λ/2 − ∫_0^1 a w*            (λ = 2 D1; a = certificate kernel, 192 cells)
  pointwise slack = ∫_0^1 a w* − ∫_0^1 φ(w*²)    (potentials telescope to 0)
Also: the top eigenfunction G_a of T_a (discretized), its w_a, ∫φ(w_a²) and ∫a w_a, i.e. the certificate's own worst case.
Pointwise slack profile s(t) = a(t)w*(t) − φ(w*(t)²) on the 192 cells is printed. NUMERICAL. Output: examples/e87/e87.json
Usage: src/dirun.sh -c 2 python src/e87_slack.py
"""
import json
import os
from fractions import Fraction as F

import numpy as np

cert = json.load(open(".research/agents/tdense11_scratch/certificate_td.json"))
K = cert["K"]
a = np.array([float(F(x)) for x in cert["a"]])
lam = 2 * float(F(cert["D1"]))


def phi(y):
    return (1 - np.sqrt(np.clip(1 - y, 0, None))) / 2


def w_of(g):
    N = len(g)
    c = np.correlate(g, g, "full")[N - 1:] / (g @ g)
    c = np.append(c, 0.0)
    return lambda t: np.interp(np.abs(t), np.arange(N + 1) / N, c, right=0.0)


def a_of(t):
    return a[np.minimum((np.asarray(t) * K).astype(int), K - 1)]


def integrals(w, M=200000):
    t = (np.arange(M) + 0.5) / M
    wt = w(t)
    return float(np.mean(phi(wt * wt))), float(np.mean(a_of(t) * wt)), t, wt


def main():
    os.makedirs("examples/e87", exist_ok=True)
    rows = [json.loads(l) for l in open("examples/e82/e82.jsonl")]
    r = max((x for x in rows if x["N"] == 320), key=lambda x: x["D"])
    g = np.array(r["g"], float)
    ws = w_of(g)
    Dw, Aw, t, wt = integrals(ws)
    out = {"D_E82": r["D"], "D_check": Dw, "int_a_wstar": Aw, "lambda_half": lam / 2,
           "schur_slack": lam / 2 - Aw, "pointwise_slack": Aw - Dw}
    # per-cell pointwise slack at w*
    cells = []
    for j in range(K):
        m = (t >= j / K) & (t < (j + 1) / K)
        cells.append([j, float(np.mean(wt[m])), float(np.mean(a_of(t[m]) * wt[m] - phi(wt[m] ** 2))) / K])
    out["cell_slack"] = cells
    # top eigenfunction of T_a on [0,1], T_a G(s) = ∫ a(|s-s'|) G(s') ds'  (midpoint rule, P points)
    P = 1536
    s = (np.arange(P) + 0.5) / P
    T = a_of(np.abs(s[:, None] - s[None, :])) / P
    ev, V = np.linalg.eigh(T)
    G = np.abs(V[:, -1])
    out["lambda_max_discrete"] = float(ev[-1])
    # w_a = G⋆G̃ via the step function with P steps
    wa = w_of(G)
    Da, Aa, _, _ = integrals(wa)
    out["eig"] = {"phi_int": Da, "int_a_w": Aa, "rayleigh_half": float(ev[-1]) / 2}
    json.dump(out, open("examples/e87/e87.json", "w"), indent=1)
    print(json.dumps({k: v for k, v in out.items() if k != "cell_slack"}, indent=1))
    top = sorted(cells, key=lambda c: -c[2])[:12]
    print("largest per-cell pointwise slack contributions [cell, mean w*, slack/K]:")
    for c in top:
        print("  ", c)
    tot = np.array([c[2] for c in cells])
    for lo, hi in ((0, 0.25), (0.25, 0.5), (0.5, 0.75), (0.75, 1.0)):
        print(f"  slack on t in [{lo},{hi}): {tot[int(lo*K):int(hi*K)].sum():.5f}")


if __name__ == "__main__":
    main()
