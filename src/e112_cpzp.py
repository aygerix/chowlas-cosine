"""E112a: CP-efficiency of Chowla-type sets in a PRIME cyclic group Z_p (no nontrivial subgroups; lead 2026-10-19).
Tests SCP(T) (CSTAR A6'): do sets with ratio |S|/K² > 2 admit completely positive certificates of cost ~K?
S ⊂ Z_p \\ {0} symmetric, K = −min_{γ≠0} Ŝ(γ). A flat CP certificate: cliques B (B − B ⊂ S ∪ {0} mod p), weights w,
    Σ_B w_B m_B(k) = 1_S(k)  (k ≠ 0 mod p),   cost C = Σ_B w_B |B|,   then Ŝ(γ) + C = Σ_B w_B |B̂(γ)|² >= 0.
So K <= C_CP. Efficiency ratio C_CP / K. Column generation: Gurobi LP master + exact Gurobi clique pricing.
Sets: E41 exact half-set optima (examples/zp_half/e41_small.txt, e41_mid.txt) and Paley sets (p ≡ 1 mod 4).
NUMERICAL LP (Gurobi tolerances); pricing is exact (MILP optimal) unless the time limit is hit (reported).
Usage: python src/e112_cpzp.py out.jsonl
"""
import sys, json, math, re
import numpy as np
import gurobipy as gp

def K_of(S, p):
    g = np.arange(1, p)
    vals = np.array([sum(math.cos(2 * math.pi * s * t / p) for s in S) for t in g])
    return float(-vals.min())

def cp_cost(S, p, tlim=600):
    S = set(x % p for x in S); half = range(1, (p - 1) // 2 + 1)
    def m_of(B):
        m = {}
        for i, b in enumerate(B):
            for c in B[i + 1:]:
                k = (c - b) % p; k = min(k, p - k); m[k] = m.get(k, 0) + 1
        return m
    cols = [[0, s] for s in sorted(S) if s <= (p - 1) // 2]
    while True:
        mst = gp.Model(); mst.Params.OutputFlag = 0
        w = [mst.addVar(lb=0) for _ in cols]
        cons = {}
        for k in half:
            expr = gp.quicksum(w[j] * m_of(B).get(k, 0) for j, B in enumerate(cols))
            cons[k] = mst.addConstr(expr == (1 if k in S else 0))
        mst.setObjective(gp.quicksum(w[j] * len(B) for j, B in enumerate(cols)), gp.GRB.MINIMIZE); mst.optimize()
        C = mst.ObjVal; y = {k: cons[k].Pi for k in half}
        pr = gp.Model(); pr.Params.OutputFlag = 0; pr.Params.TimeLimit = tlim
        x = pr.addVars(p, vtype=gp.GRB.BINARY); pr.addConstr(x[0] == 1)
        obj = -gp.quicksum(x[b] for b in range(p))
        for b in range(p):
            for c in range(b + 1, p):
                k = (c - b) % p; kk = min(k, p - k)
                if k in S:
                    z = pr.addVar(lb=0, ub=1); pr.addConstr(z <= x[b]); pr.addConstr(z <= x[c])
                    obj += y.get(kk, 0.0) * z
                else:
                    pr.addConstr(x[b] + x[c] <= 1)
        pr.setObjective(obj, gp.GRB.MAXIMIZE); pr.optimize()
        if pr.ObjVal <= 1e-7:
            return C, len(cols), ("opt" if pr.Status == 2 else "timelimit"), max(len(B) for B in cols)
        B = [b for b in range(p) if x[b].X > 0.5]
        if B in cols:
            return C, len(cols), "stalled", max(len(B) for B in cols)
        cols.append(B)

def main():
    out = sys.argv[1]; rows = []
    for fn in ("examples/zp_half/e41_small.txt", "examples/zp_half/e41_mid.txt"):
        for line in open(fn):
            mm = re.match(r"p=(\d+).*?P=([\d ]+)", line)
            if mm:
                p = int(mm.group(1)); P = [int(t) for t in mm.group(2).split()]
                rows.append(("E41", p, sorted(set([a % p for a in P] + [(-a) % p for a in P]))))
    for p in (13, 17, 29, 37, 41, 53, 61, 73, 89):
        rows.append(("Paley", p, sorted({(a * a) % p for a in range(1, p)})))
    with open(out, "w") as o:
        for kind, p, S in rows:
            K = K_of(S, p); C, ncol, st, smax = cp_cost(S, p)
            r = dict(kind=kind, p=p, size=len(S), K=K, ratio=len(S) / K ** 2, C_CP=C, eff=C / K, cols=ncol,
                     status=st, max_block=smax)
            print(json.dumps(r), flush=True); o.write(json.dumps(r) + "\n"); o.flush()

if __name__ == "__main__":
    main()
