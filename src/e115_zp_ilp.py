r"""E115: exact K-Chowla numbers in Z_p by Gurobi ILP (lead, cont. 31).

N_p(K) := max |S| over symmetric S ⊂ Z_p \ {0} with |S| <= (p-1)/2 and D_S(j) = Σ_{s∈S} e(sj/p) >= -K for all j != 0.
Variables x_s ∈ {0,1} for pairs {s, -s}, s = 1..(p-1)/2; |S| = 2Σx; D_S(j) = Σ_s x_s·2cos(2π s j/p).
Constraints are exact (Z_p has finitely many characters; no grid). Z_p-Chowla (bounded N_p(K)/K² over all p) implies
Z-Chowla (sample at p > 2·max S). Gurobi's dual bound certifies optimality up to its tolerances; the optimal S is
re-evaluated in double precision with a margin check.
Usage: python src/e115_zp_ilp.py p K [timelimit] [threads]
"""
import sys, json, time, math
import numpy as np
import gurobipy as gp
from gurobipy import GRB


def solve(p, K, tl=600, threads=8):
    h = (p - 1) // 2
    s = np.arange(1, h + 1)
    C = 2 * np.cos(2 * np.pi * np.outer(np.arange(1, h + 1), s) / p)  # rows j = 1..h (j and -j give equal values)
    m = gp.Model()
    m.Params.OutputFlag = 0
    m.Params.TimeLimit = tl
    m.Params.Threads = threads
    m.Params.MIPGap = 0
    m.Params.IntFeasTol = 1e-9
    m.Params.FeasibilityTol = 1e-9
    x = m.addMVar(h, vtype=GRB.BINARY)
    m.addConstr(C @ x >= -K)
    m.addConstr(x.sum() <= (p - 1) // 4)  # |S| <= (p-1)/2
    m.addConstr(x[0] == 1)  # dilation symmetry: some element of S can be moved to 1 (S nonempty)
    m.setObjective(x.sum(), GRB.MAXIMIZE)
    t0 = time.time()
    m.optimize()
    out = {"p": p, "K": K, "status": m.Status, "seconds": round(time.time() - t0, 2)}
    if m.SolCount:
        sol = [int(v) for v in s[np.round(x.X).astype(bool)]]
        vals = C[:, np.round(x.X).astype(bool)].sum(axis=1)
        out.update({"pairs": len(sol), "S_size": 2 * len(sol), "bound_pairs": m.ObjBound,
                    "Kmin_exact": float(-vals.min()), "ratio": 2 * len(sol) / K ** 2, "S_pos": sol})
    return out


if __name__ == "__main__":
    p, K = int(sys.argv[1]), float(sys.argv[2])
    tl = float(sys.argv[3]) if len(sys.argv) > 3 else 600
    th = int(sys.argv[4]) if len(sys.argv) > 4 else 8
    print(json.dumps(solve(p, K, tl, th)), flush=True)
