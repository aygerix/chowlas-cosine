"""E78 — sharp constant of the doubly-positive L2/L1 gap (round-7 lemma R7-D; NOTEBOOK cont. 10).

J(q) = int q^2 / (q(0) int q) over even q >= 0 with nonnegative Fourier transform (doubly positive).
Round 7 proved J <= v* = (1+sqrt 17)/(4 sqrt 2) = 0.90565, giving T-dense(C) for C < (2/r)(1+sqrt(1-v*))^2 = 4.4393.
The same argument with the sharp J* gives C < (2/r)(1+sqrt(1-J*))^2. Known values: Gaussian 1/sqrt2 = 0.7071,
triangle 2/3, half-sine autocorrelation pi^2/24 + 5/16 = 0.72369 (=> C = 6.047).
J is Fourier-invariant (Plancherel), so q and its transform are both admissible.
(a) Autocorrelation subclass q = g * g~ with g >= 0 on N grid points (L-BFGS on g = exp(theta), many starts).
(b) General doubly-positive piecewise-linear q (nodes c_i = q(i/B), c_0 = 1, c_i >= 0; PD <=> cosine symbol
    c_0 + 2 sum c_i cos(i th) >= 0, sampled on 16B points): Dinkelbach iterations with Gurobi NonConvex = 2.
NUMERICAL. Usage: python src/e78_doubly_positive.py -> examples/e78/e78.jsonl
"""
import json
import math
import os

import numpy as np
from scipy.optimize import minimize

OUT = "examples/e78/e78.jsonl"


def J_seq_pwl(c):
    """J for the even piecewise-linear function with nodes c_0..c_{K-1} at spacing 1 (c_K = 0)."""
    c = np.append(np.asarray(c, float), 0.0)
    I1 = c[0] / 2 + c[1:].sum()
    I2 = ((c[:-1] ** 2 + c[:-1] * c[1:] + c[1:] ** 2) / 3).sum()
    return I2 / (c[0] * I1)


def autocorr_J(g):
    q = np.correlate(g, g, mode="full")[len(g) - 1:]  # q_k, k >= 0
    return J_seq_pwl(q / q[0])


def part_a(fh, N=200, starts=24, seed=1):
    rng = np.random.default_rng(seed)
    x = (np.arange(N) + 0.5) / N
    inits = {"half_sine": np.sin(np.pi * x), "flat": np.ones(N), "gauss": np.exp(-((x - 0.5) / 0.2) ** 2),
             "parabola": x * (1 - x), "sin^2": np.sin(np.pi * x) ** 2}
    for s in range(starts):
        inits[f"rand{s}"] = rng.random(N) + 0.1
    best = None
    for name, g0 in inits.items():
        th0 = np.log(np.maximum(g0, 1e-6))

        def obj(th):
            g = np.exp(th)
            return -autocorr_J(g)

        res = minimize(obj, th0, method="L-BFGS-B", options={"maxiter": 3000})
        val = -res.fun
        row = {"part": "a_autocorr", "N": N, "start": name, "J_start": autocorr_J(np.exp(th0)), "J": val}
        fh.write(json.dumps(row) + "\n")
        fh.flush()
        print(json.dumps(row), flush=True)
        if best is None or val > best[0]:
            best = (val, np.exp(res.x))
    g = best[1]
    row = {"part": "a_best", "N": N, "J": best[0], "g_normalized": (g / g.max()).round(5).tolist()}
    fh.write(json.dumps(row) + "\n")
    fh.flush()
    print(json.dumps({k: v for k, v in row.items() if k != "g_normalized"}), flush=True)


def part_b(fh, B=40, tlim=600):
    import gurobipy as gp
    from gurobipy import GRB
    th = np.linspace(0, np.pi, 16 * B + 1)
    lam = 0.70
    for it in range(8):
        m = gp.Model()
        m.Params.OutputFlag = 0
        m.Params.NonConvex = 2
        m.Params.TimeLimit = tlim
        m.Params.Threads = 2
        c = m.addVars(B, lb=0.0, ub=1.0, name="c")
        m.addConstr(c[0] == 1)
        for t in th:
            m.addConstr(c[0] + 2 * gp.quicksum(c[i] * math.cos(i * t) for i in range(1, B)) >= 0)
        cc = [c[i] for i in range(B)] + [0.0]
        I1 = 0.5 * c[0] + gp.quicksum(c[i] for i in range(1, B))
        I2 = gp.quicksum((cc[i] * cc[i] + cc[i] * cc[i + 1] + cc[i + 1] * cc[i + 1]) / 3.0 for i in range(B))
        m.setObjective(I2 - lam * I1, GRB.MAXIMIZE)
        m.optimize()
        cv = np.array([c[i].X for i in range(B)])
        J = J_seq_pwl(cv)
        sym = cv[0] + 2 * (cv[1:, None] * np.cos(np.outer(np.arange(1, B), np.linspace(0, np.pi, 200 * B)))).sum(0)
        row = {"part": "b_gurobi", "B": B, "iter": it, "lambda": lam, "status": int(m.Status), "obj": m.ObjVal,
               "bound": m.ObjBound, "J": J, "symbol_min_fine": float(sym.min()), "c": cv.round(6).tolist()}
        fh.write(json.dumps(row) + "\n")
        fh.flush()
        print(json.dumps({k: v for k, v in row.items() if k != "c"}), flush=True)
        if abs(J - lam) < 1e-7:
            break
        lam = J


def main():
    os.makedirs("examples/e78", exist_ok=True)
    with open(OUT, "w") as fh:
        hs = np.linspace(0, 1, 2001)
        qh = (1 - hs) * np.cos(np.pi * hs) + np.sin(np.pi * hs) / np.pi
        ref = {"part": "reference", "half_sine_J_numeric": J_seq_pwl(qh) , "half_sine_J_exact": math.pi ** 2 / 24 + 5 / 16,
               "gauss": 1 / math.sqrt(2), "triangle": 2 / 3, "v_star": (1 + math.sqrt(17)) / (4 * math.sqrt(2))}
        fh.write(json.dumps(ref) + "\n")
        print(json.dumps(ref), flush=True)
        part_a(fh)
        for B in (24, 40):
            part_b(fh, B=B)


if __name__ == "__main__":
    main()
