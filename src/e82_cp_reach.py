"""E82 — the reach of the CP-cone (second-order) macroscopic class.

Lead's reduction (NOTEBOOK cont. 12): the limiting residual energy profile e is (1/4 x) a mixture of |w|^2, w PD with
supp w in [-1,1] (Gabor-window identity applied to h = g + m >= 0), and p = (1 - sqrt(1 - 4e))/2 (a <= 1/2). By
convexity of phi(x) = (1 - sqrt(1-x))/2 a single generator is extremal, so the second-order reach is 1/D with
    D = sup { int_0^1 phi(w(t)^2) dt :  w = G * G~ (autocorrelation), G >= 0 on [0,1], int G^2 = 1 }.
Weighted Fejer-packet escapes realise every such w (round-9 Task 3 with packet shape s, s^ = w), so 1/D is also the
EXACT limit of arguments using positivity + the two binary moment profiles. Triangle (G = 1): D >= (1 - pi/4)/2,
1/D <= 9.3196. Round-9 two-profile class (relaxation): 1/D >= 7.2674.

NUMERICAL: L-BFGS-B over step functions G (N cells), w = exact PWL interpolation of the discrete autocorrelation,
objective by 16-point Gauss-Legendre per cell. Starts: constant, half-sine, random, centre-peaked.
Output: examples/e82/e82.jsonl.  Usage: python src/e82_cp_reach.py N1 N2 ...
"""
import json
import os
import sys

import numpy as np
from scipy.optimize import minimize

GX, GW = np.polynomial.legendre.leggauss(16)
GX = (GX + 1) / 2
GW = GW / 2


def phi(x):
    return (1 - np.sqrt(np.clip(1 - x, 0, None))) / 2


def dphi(x):
    return 0.25 / np.sqrt(np.clip(1 - x, 1e-300, None))


MODE = os.environ.get("E82_MODE", "D")  # D: int phi(w^2); N2: int w^2; ratio: int phi(w^2) / int w^2


def objective(g, N):
    if MODE == "D":
        return objective_f(g, N, phi, dphi)
    if MODE == "N2":
        return objective_f(g, N, lambda x: x, lambda x: np.ones_like(x))
    F1, G1 = objective_f(g, N, phi, dphi)
    F2, G2 = objective_f(g, N, lambda x: x, lambda x: np.ones_like(x))
    return F1 / F2, (G1 * F2 - F1 * G2) / F2 ** 2


def objective_f(g, N, phi, dphi):
    S = g @ g
    c = np.correlate(g, g, mode="full")[N - 1:] / S  # c_0..c_{N-1}
    c = np.append(c, 0.0)  # c_N = 0
    a, b = c[:-1, None], c[1:, None]
    w = a + (b - a) * GX[None, :]  # N cells x 16
    w2 = w * w
    F = (phi(w2) * GW[None, :]).sum() / N
    dw = 2 * w * dphi(w2) * GW[None, :] / N  # dF/dw at nodes
    dc = np.zeros(N + 1)
    dc[:-1] += (dw * (1 - GX[None, :])).sum(1)
    dc[1:] += (dw * GX[None, :]).sum(1)
    dc[0] = 0.0  # c_0 == 1 identically
    # c_k = sum_j g_j g_{j+k} / S ; dc_k/dg_j = (g_{j+k} + g_{j-k})/S - 2 c_k g_j / S
    dcN = dc[:N]
    cc = c[:N]
    grad = np.zeros(N)
    for k in range(1, N):
        if dcN[k] == 0:
            continue
        grad[:N - k] += dcN[k] * g[k:]
        grad[k:] += dcN[k] * g[:N - k]
    grad = grad / S - 2 * (dcN @ cc) * g / S
    return F, grad


R = 4 / (3 * np.sqrt(3))


def window_check(g, N):
    """Sanity: the D-optimiser must satisfy every P31 window (they are consequences of positivity)."""
    c = np.append(np.correlate(g, g, mode="full")[N - 1:] / (g @ g), 0.0)
    t = np.linspace(0, 1, 20001)
    w = np.interp(t, np.arange(N + 1) / N, c)
    e, p = w * w / 4, phi(w * w)
    out = {}
    for name, v in (("e", e), ("p", p)):
        tot = np.trapezoid(v, t)
        worst = 1e9
        for th in np.concatenate([np.geomspace(1e-3, 1, 200), np.linspace(1, 20, 100)]):
            m = t <= th
            rhs = R * (1 + th) * np.trapezoid(((1 - t[m] / th) ** 2) * v[m], t[m])
            worst = min(worst, (rhs - (2 * th / 3) * tot) / tot)
        out["min_rel_slack_" + name] = worst
    return out


def run(N, start, seed, fh):
    rng = np.random.default_rng(seed)
    x = (np.arange(N) + 0.5) / N
    if start == "const":
        g0 = np.ones(N)
    elif start == "halfsine":
        g0 = np.sin(np.pi * x)
    elif start == "peaked":
        g0 = np.exp(-((x - 0.5) / 0.2) ** 2)
    else:
        g0 = rng.random(N) + 0.1
    res = minimize(lambda g: tuple(-v for v in objective(g, N)), g0, jac=True, method="L-BFGS-B",
                   bounds=[(0, None)] * N, options={"maxiter": 20000, "maxfun": 40000, "ftol": 1e-15, "gtol": 1e-12})
    g = res.x / np.sqrt(res.x @ res.x / N)
    D, _ = objective(g, N)
    c = np.correlate(g, g, mode="full")[N - 1:] / (g @ g)
    row = {"mode": MODE, "N": N, "start": start, "seed": seed, "D": D, "C": 1 / D, "nit": int(res.nit), "msg": str(res.message),
           "int_w2_0_1": float(((np.append(c, 0)[:-1] ** 2 + np.append(c, 0)[1:] ** 2) / 2).sum() / N),
           **window_check(g, N), "g": np.round(g, 6).tolist()}
    fh.write(json.dumps(row) + "\n")
    fh.flush()
    print(json.dumps({k: v for k, v in row.items() if k != "g"}), flush=True)


def main():
    Ns = [int(a) for a in sys.argv[1:]] or [40, 80, 160]
    os.makedirs("examples/e82", exist_ok=True)
    out = "examples/e82/e82.jsonl" if MODE == "D" else f"examples/e82/e82_{MODE}.jsonl"
    # sanity: triangle value
    N = 400
    print("triangle check", objective(np.ones(N), N)[0], (1 - np.pi / 4) / 2, flush=True)
    with open(out, "w") as fh:
        for N in Ns:
            starts = (("const", 0), ("halfsine", 0), ("peaked", 0), ("random", 1), ("random", 2)) if N <= 80 else \
                (("halfsine", 0), ("random", 1))
            for start, seed in starts:
                run(N, start, seed, fh)


if __name__ == "__main__":
    main()
