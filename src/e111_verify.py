"""E111 lead verification of a flat-block CP certificate (independent of the agent's code).
Primal: check Σ_B w_B m_B(k) = 1_A(k) for k = 1..X EXACTLY (rationals from the stored weights, then the cost).
Dual:   given duals y (k in A), the flat-class LP lower bound is Σ_k y_k provided every clique B satisfies
        Σ_{b<b' in B} y_{b'-b} <= |B|. We re-solve max_B [Σ_{pairs} y − |B|] over cliques with Gurobi (binary x_b,
        pair products linearised only on admissible pairs) to confirm max <= 0 (+ tolerance), i.e. y is dual-feasible.
Usage: python src/e111_verify.py examples/e111/N50_x72_certificate.json
"""
import sys, json
from fractions import Fraction
import gurobipy as gp

def main():
    r = json.load(open(sys.argv[1])); A = sorted(r["A"]); X = max(A); S = set(A)
    cert = r["certificate"]
    blocks = cert["blocks"] if isinstance(cert, dict) and "blocks" in cert else cert
    cov = [Fraction(0)] * (X + 1); cost = Fraction(0)
    for b in blocks:
        B = list(b["B"]); w = Fraction(str(b.get("weight", b.get("w"))))
        lev = [Fraction(v) for v in b.get("levels", [1] * len(B))]
        P = sorted(zip(B, lev))
        assert all((y - x) in S for i, (x, _) in enumerate(P) for (y, _) in P[i + 1:]), "block is not a clique"
        cost += w * sum(l * l for _, l in P)
        for i, (x, lx) in enumerate(P):
            for (y, ly) in P[i + 1:]: cov[y - x] += w * lx * ly
    bad = [k for k in range(1, X + 1) if cov[k] != (1 if k in S else 0)]
    print("primal exact identity:", "OK" if not bad else f"FAILS at {bad[:10]}", " cost =", float(cost),
          " R_CP =", float(cost) / (2 * len(A) ** 0.5))
    y = r.get("last_master_duals")
    if y is None: print("no duals stored"); return
    if isinstance(y, dict): y = {int(k): float(v) for k, v in y.items()}
    else: y = {k: float(v) for k, v in zip(A, y)}
    m = gp.Model(); m.Params.OutputFlag = 0; m.Params.TimeLimit = 1800
    x = m.addVars(X + 1, vtype=gp.GRB.BINARY)
    m.addConstr(x[0] == 1)                      # translation: min B = 0
    obj = -gp.quicksum(x[b] for b in range(X + 1)); z = {}
    for b in range(X + 1):
        for c in range(b + 1, X + 1):
            if (c - b) in S:
                z[b, c] = m.addVar(lb=0, ub=1)
                m.addConstr(z[b, c] <= x[b]); m.addConstr(z[b, c] <= x[c]); m.addConstr(z[b, c] >= x[b] + x[c] - 1)
                obj += y.get(c - b, 0.0) * z[b, c]
            else:
                m.addConstr(x[b] + x[c] <= 1)
    m.setObjective(obj, gp.GRB.MAXIMIZE); m.optimize()
    print("dual value Σy =", sum(y.get(k, 0.0) for k in A), " max reduced cost over cliques =", m.ObjVal,
          " bound =", m.ObjBound, " status =", m.Status)

if __name__ == "__main__":
    main()
