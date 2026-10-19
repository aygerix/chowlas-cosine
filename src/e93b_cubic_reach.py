"""E93b — numerical reach of "second order + cubic front cap + cubic profile PD" (NOTEBOOK cont. 17.9).
maximise ∫_0^1 φ(σ w²) over step-function G >= 0 (N steps; w = G⋆G̃ normalised) and σ ∈ (0, 2/3],
subject to FT[g(p)](ξ) >= 0 on a grid ξ ∈ [0, 120], p = φ(σ w²), g(u) = u(1−u)(1−2u). Penalty method, L-BFGS-B with
finite-difference gradients, warm-started from the E82 λ = 2/3 optimiser. NUMERICAL (an approximation of a sup).
Output: examples/e93/e93b.json
"""
import json, os
import numpy as np
from scipy.optimize import minimize

def phi(x):
    return (1 - np.sqrt(np.clip(1 - x, 0, None))) / 2

M = 1200
t = np.linspace(0, 1, M + 1)
wts = np.full_like(t, t[1] - t[0]); wts[0] /= 2; wts[-1] /= 2
xis = np.linspace(0, 120, 1201)
COS = 2 * np.cos(np.outer(xis, t)) * wts

def w_of(G):
    N = len(G)
    c = np.correlate(G, G, "full")[N - 1:] / max(G @ G, 1e-300)
    c = np.append(c, 0.0)
    return np.interp(t, np.arange(N + 1) / N, c)

def unpack(x):
    G = np.abs(x[:-1]); sig = (2 / 3) / (1 + np.exp(-x[-1]))  # σ ∈ (0, 2/3)
    return G, sig

def obj(x, mu):
    G, sig = unpack(x)
    w = w_of(G); p = phi(sig * w * w)
    d = float(wts @ p)
    s = p * (1 - p) * (1 - 2 * p)
    F = COS @ s
    pen = float(np.sum(np.minimum(F, 0) ** 2))
    return -d + mu * pen, d, float(F.min())

def main():
    os.makedirs("examples/e93", exist_ok=True)
    rows = [json.loads(l) for l in open("examples/e82/e82_lam0.6666666667.jsonl")]
    r = max((x for x in rows if x["N"] == 80), key=lambda x: x["D"])
    G0 = np.array(r["g"], float)
    x = np.append(G0, 6.0)
    hist = []
    for mu in (1e2, 1e3, 1e4, 1e5, 1e6):
        res = minimize(lambda z: obj(z, mu)[0], x, method="L-BFGS-B", options={"maxiter": 400, "maxfun": 200000})
        x = res.x
        _, d, fmin = obj(x, mu)
        G, sig = unpack(x)
        hist.append({"mu": mu, "d": d, "C": 1 / d, "min_ft_s": fmin, "sigma": sig, "a": float(phi(sig)), "nit": int(res.nit)})
        print(hist[-1], flush=True)
    json.dump({"hist": hist, "G": list(map(float, unpack(x)[0]))}, open("examples/e93/e93b.json", "w"), indent=1)

if __name__ == "__main__":
    main()
