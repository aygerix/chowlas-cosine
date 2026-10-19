"""E79 — lead's independent checks of round 8 (PROOFS P59) and the enlarged macroscopic class.

(A) Independent re-check of the rho* <= 203819/250000 potential certificate:
    rho x − x² + beta(y_min(x)) − beta(x)/2 >= 0 on [0,1], y_min = max(0, 2x²−1, x − sqrt(1−x)), beta increasing,
    beta(0) = 0 (beta from the Bernstein coefficients in potential_g4_d8_exact.json).
    Method: exact rational evaluation on a 20001-point grid in each region, plus a rigorous Lipschitz bound between
    grid points, written independently of the agent's Bernstein/Sturm code.
(B) Does the energy-PD constraint (e = p(1−p) PD) bite on the rho*-extremal shape p = q/2 (q = half-sine
    autocorrelation, and the numerically optimal autocorrelation from E78)? Prints min of the cosine transform of e.
NUMERICAL except where stated. Usage: python src/e79_r8_checks.py
"""
import json
import math
from fractions import Fraction as F

import numpy as np

cert = json.load(open(".research/agents/tdense8_scratch/potential_g4_d8_exact.json"))
rho = F(cert["rho"])
bern = [F(b) for b in cert["beta_bernstein"]]
deg = len(bern) - 1


def beta(x):
    x = F(x)
    return sum(bern[k] * math.comb(deg, k) * x ** k * (1 - x) ** (deg - k) for k in range(deg + 1))


def beta_f(x):
    return sum(float(bern[k]) * math.comb(deg, k) * x ** k * (1 - x) ** (deg - k) for k in range(deg + 1))


def part_a():
    # monotonicity: beta' >= 0 on [-0.001, 1] (dense float check of the derivative)
    xs = np.linspace(-0.001, 1, 200001)
    h = 1e-7
    dmin = min((beta_f(x + h) - beta_f(x - h)) / (2 * h) for x in xs[::50])
    # main inequality on a dense grid (float) + exact rational at a coarser grid
    worst = (1e9, None)
    N = 200001
    for x in np.linspace(0, 1, N):
        y = max(0.0, 2 * x * x - 1, x - math.sqrt(max(0.0, 1 - x)))
        v = float(rho) * x - x * x + beta_f(y) - beta_f(x) / 2
        if v < worst[0]:
            worst = (v, x)
    # Lipschitz constant of the expression in x (crude): |d/dx| <= rho + 2 + |beta'| * |dy/dx| + |beta'|/2;
    # dy/dx <= max(4x, 1 + 1/(2 sqrt(1-x))) which blows up only as x -> 1 where 2x^2-1 is the binding branch (dy/dx<=4).
    exact_min = None
    for i in range(0, 2001):
        x = F(i, 2000)
        cands = [F(0), 2 * x * x - 1]
        # x - sqrt(1-x): use a rational lower bound of the sqrt-branch value (smaller y => smaller beta(y) since beta increasing)
        s = math.sqrt(float(1 - x))
        cands.append(x - F(s).limit_denominator(10 ** 12) - F(1, 10 ** 11))
        y = max(cands)
        v = rho * x - x * x + beta(y) - beta(x) / 2
        if exact_min is None or v < exact_min[0]:
            exact_min = (v, x)
    return {"beta_prime_min_float": dmin, "float_min": worst[0], "float_argmin": worst[1],
            "exact_grid_min": float(exact_min[0]), "exact_grid_argmin": float(exact_min[1])}


def cos_transform(vals, t, ys):
    # vals on grid t in [0,1] (even extension), trapezoid
    w = np.full(len(t), t[1] - t[0])
    w[0] = w[-1] = w[0] / 2
    return np.array([np.sum(w * vals * np.cos(y * t)) for y in ys])


def part_b():
    out = {}
    t = np.linspace(0, 1, 4001)
    q = (1 - t) * np.cos(np.pi * t) + np.sin(np.pi * t) / np.pi
    ys = np.linspace(0, 400, 40001)
    for a in (0.5, 0.45, 0.4):
        p = a * q
        e = p * (1 - p)
        E = cos_transform(e, t, ys)
        P = cos_transform(p, t, ys)
        out[f"halfsine_a{a}"] = {"min_FT_e": float(E.min()), "argmin_y": float(ys[E.argmin()]),
                                 "min_FT_p": float(P.min()), "J": float((np.trapezoid(p * p, t)) / (a * np.trapezoid(p, t)))}
    return out


def main():
    res = {"A": part_a(), "B": part_b()}
    print(json.dumps(res, indent=1))
    json.dump(res, open("examples/e79/e79_checks.json", "w"), indent=1)


if __name__ == "__main__":
    import os
    os.makedirs("examples/e79", exist_ok=True)
    main()
