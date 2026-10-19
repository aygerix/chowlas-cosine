"""E58: linear lower bounds for sets without small elements. For A ⊂ [Y, KY]:
    M(A) >= c(K)·|A|,   c(K) = max { c : exists probability mu on [0, pi] with mu^(a) = ∫cos(ax)dmu <= -c  ∀ a ∈ [Y, KY] }
(take M >= -∫ f_A dmu = -Σ_a mu^(a)). Gurobi LP over a fine grid of atoms x_i = pi*i/G. Also records the c needed by
P31-C(b)'s sqrt bound for comparison. Usage: python src/e58_ratio_lp.py > examples/e58/e58.jsonl
"""
import json, math, sys
import numpy as np
import gurobipy as gp
from gurobipy import GRB

def c_of(Y, K, G):
    xs = np.pi * np.arange(G + 1) / G
    a = np.arange(Y, K * Y + 1)
    Cm = np.cos(np.outer(a, xs))
    m = gp.Model(); m.Params.OutputFlag = 0; m.Params.Threads = 2
    mu = m.addMVar(G + 1, lb=0.0); c = m.addVar(lb=-1.0, ub=1.0)
    m.addConstr(mu.sum() == 1)
    m.addConstr(Cm @ mu + c <= 0)
    m.setObjective(c, GRB.MAXIMIZE); m.optimize()
    support = [(round(float(xs[i] * Y / np.pi), 4), round(float(mu.X[i]), 4)) for i in range(G + 1) if mu.X[i] > 1e-6]
    return c.X, support

if __name__ == "__main__":
    for K in (1.5, 2, 2.5, 3, 4, 6, 8, 12, 20, 40):
        for Y in (40, 80):
            Kint = K
            G = int(16 * K * Y)
            c, sup = c_of(Y, int(round(K * Y)) // Y if float(K).is_integer() else 1, G) if False else (None, None)
            xs = np.pi * np.arange(G + 1) / G
            a = np.arange(Y, int(round(K * Y)) + 1)
            Cm = np.cos(np.outer(a, xs))
            m = gp.Model(); m.Params.OutputFlag = 0; m.Params.Threads = 2
            mu = m.addMVar(G + 1, lb=0.0); cv = m.addVar(lb=-1.0, ub=1.0)
            m.addConstr(mu.sum() == 1); m.addConstr(Cm @ mu + cv <= 0)
            m.setObjective(cv, GRB.MAXIMIZE); m.optimize()
            supp = [(round(float(xs[i] * Y / np.pi), 4), round(float(mu.X[i]), 4)) for i in range(G + 1) if mu.X[i] > 1e-6]
            print(json.dumps(dict(K=K, Y=Y, c=round(cv.X, 6), cK=round(cv.X * K, 4), atoms_xY_over_pi=supp[:12], n_atoms=len(supp))), flush=True)
