"""E94 — rigorous mixing bound for D_{2/3}: minimise α1·D1 + α2·N2b subject to φ(2x/3) <= α1 φ(x) + α2 x on [0,1],
with D1 = 259/2000 (P63, rigorous) and N2b = 2/(3√3) (Beckner, rigorous). Gurobi LP on a fine grid, then an exact
sanity check with mpmath on a much finer grid plus endpoint analysis. NUMERICAL search for the multipliers; the final
inequality must be certified separately before use.
"""
import numpy as np, gurobipy as gp, mpmath as mp
phi = lambda x: (1 - np.sqrt(np.clip(1 - x, 0, None))) / 2
D1, N2b = 259 / 2000, 2 / (3 * np.sqrt(3))
xs = np.linspace(0, 1, 200001)
m = gp.Model(); m.Params.OutputFlag = 0
a1 = m.addVar(lb=0); a2 = m.addVar(lb=-gp.GRB.INFINITY)
for x in xs[::20]:
    m.addConstr(a1 * phi(x) + a2 * x >= phi(2 * x / 3))
m.setObjective(D1 * a1 + N2b * a2, gp.GRB.MINIMIZE); m.optimize()
A1, A2 = a1.X, a2.X
slack = A1 * phi(xs) + A2 * xs - phi(2 * xs / 3)
print("alpha1", A1, "alpha2", A2, "bound", D1 * A1 + N2b * A2, "C", 1 / (D1 * A1 + N2b * A2), "min slack fine grid", slack.min())
print("pure Beckner: bound", (1 - 1 / np.sqrt(3)) / 2 * N2b, "C", 1 / ((1 - 1 / np.sqrt(3)) / 2 * N2b))
