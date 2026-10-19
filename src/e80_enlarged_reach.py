"""E80 — numerical reach of the ENLARGED macroscopic class (PROOFS P59): maximise d = ∫_0^1 p over profiles with
  p PD (parametrised as a·q(t/φ), q = normalised autocorrelation of g >= 0 on [0, 1/2], so q(0) = 1, supp q = [0,1]),
  e = p(1 − p) PD (cosine transform sampled on y ∈ [0, Ymax]),
  density and energy windows (2θ/3)∫v <= r(1+θ)∫_0^θ(1 − t/θ)²v for v = p, e at every sampled θ ∈ (0, 1].
The reach is C = 1/d_max for this class (an UPPER bound on the true reach of "p, e PD + windows": the class is the
autocorrelation subclass and constraints are sampled). P59 proves T-dense(C) for C < 4(2 − ρ)/r (6.156 with
ρ = 0.815276); the ρ*-extremal shape violates e-PD (E79), so the class's true reach exceeds 4(2 − ρ*)/r ≈ 6.63.
NUMERICAL. Usage: python src/e80_enlarged_reach.py -> examples/e80/e80.jsonl
"""
import json
import math
import os

import numpy as np
from scipy.optimize import minimize

R = 4 / (3 * math.sqrt(3))
NG = 30
TT = np.linspace(0, 1, 801)
YS = np.linspace(0.05, 160, 1600)
THETAS = np.concatenate([np.linspace(0.005, 0.1, 20), np.linspace(0.12, 1.0, 23)])
OUT = "examples/e80/e80.jsonl"


def trap(v, t):
    return np.trapezoid(v, t)


def profile(z):
    g = np.exp(z[:NG])
    a = 1 / (1 + math.exp(-z[NG]))
    phi = 0.05 + 0.95 / (1 + math.exp(-z[NG + 1]))
    c = np.correlate(g, g, mode="full")[NG - 1:]
    c = c / c[0]
    s = TT / phi * NG  # position in autocorrelation index units
    q = np.interp(s, np.arange(NG), c, right=0.0)
    q[s > NG - 1] = 0.0
    return a * q, a, phi


def cosft(v):
    return np.array([trap(v * np.cos(y * TT), TT) for y in YS])


def windows(v):
    tot = trap(v, TT)
    out = []
    for th in THETAS:
        m = TT <= th
        rhs = R * (1 + th) * trap(((1 - TT[m] / th) ** 2) * v[m], TT[m])
        out.append(rhs - (2 * th / 3) * tot)
    return np.array(out)


def run(seed, fh):
    rng = np.random.default_rng(seed)
    z0 = np.concatenate([np.log(np.sin(np.pi * (np.arange(NG) + 0.5) / NG) + 0.05 * rng.random(NG)), [0.0, 0.5]])
    if seed > 0:
        z0[:NG] += 0.5 * rng.standard_normal(NG)
        z0[NG] = rng.normal(0, 1)
        z0[NG + 1] = rng.normal(0, 1)

    def obj(z):
        p, a, phi = profile(z)
        return -trap(p, TT)

    cons = [{"type": "ineq", "fun": lambda z: cosft(profile(z)[0] * (1 - profile(z)[0])) * 50},
            {"type": "ineq", "fun": lambda z: windows(profile(z)[0]) * 50},
            {"type": "ineq", "fun": lambda z: windows(profile(z)[0] * (1 - profile(z)[0])) * 50}]
    res = minimize(obj, z0, method="SLSQP", constraints=cons, options={"maxiter": 400, "ftol": 1e-10})
    p, a, phi = profile(res.x)
    e = p * (1 - p)
    d = trap(p, TT)
    row = {"seed": seed, "success": bool(res.success), "d": d, "C": 1 / d if d > 0 else None, "a": a, "phi": phi,
           "min_FT_e": float(cosft(e).min()), "min_win_p": float(windows(p).min()), "min_win_e": float(windows(e).min()),
           "J_p": float(trap(p * p, TT) / (a * d)), "g": np.exp(res.x[:NG]).round(5).tolist()}
    fh.write(json.dumps(row) + "\n")
    fh.flush()
    print(json.dumps({k: v for k, v in row.items() if k != "g"}), flush=True)


def main():
    os.makedirs("examples/e80", exist_ok=True)
    with open(OUT, "w") as fh:
        for seed in range(12):
            run(seed, fh)


if __name__ == "__main__":
    main()
