# Gurobi port of src/group_bt_ilp.py (E37): maximize |B_t| over symmetric A ⊂ Γ\{0} with F(χ) >= −K0 for every
# nontrivial χ, Γ = Z_{n1} × ... × Z_{nr}, B_t = {m ∈ A : m − t ∈ A, m + t ∉ A}. Same model, same exact FFT recheck.
# Usage: python src/grb_group_bt.py "4,4,4,4" "1,0,0,0" K0 timelimit [threads] [out.json] [hint]
#   hint (optional): an integer lower bound on |B_t| known from an earlier run (added as a cutoff, not a constraint).
# Status of results: exact up to Gurobi tolerances (character constraints in floating point; the solution's K is
# rechecked exactly by FFT and reported). Fits the size-limited pip licence (<= 2000 rows/cols) for |Γ| <= ~400.
import sys, itertools, time, json
import numpy as np
import gurobipy as gp
from gurobipy import GRB

dims = tuple(int(v) for v in sys.argv[1].split(','))
t = tuple(int(v) for v in sys.argv[2].split(','))
K0 = float(sys.argv[3]); tl = float(sys.argv[4]) if len(sys.argv) > 4 else 600
threads = int(sys.argv[5]) if len(sys.argv) > 5 else 4
extra = sys.argv[6] if len(sys.argv) > 6 else ""
hint = int(sys.argv[7]) if len(sys.argv) > 7 else None
els = list(itertools.product(*[range(n) for n in dims]))
idx = {e: i for i, e in enumerate(els)}
neg = lambda e: tuple((-x) % n for x, n in zip(e, dims))
addv = lambda e, f: tuple((x + y) % n for x, y, n in zip(e, f, dims))
subv = lambda e, f: tuple((x - y) % n for x, y, n in zip(e, f, dims))
zero = tuple(0 for _ in dims)
orbits = []; orb_of = {}
for e in els:
    if e == zero or e in orb_of: continue
    o = sorted({e, neg(e)}); k = len(orbits); orbits.append(o)
    for f in o: orb_of[f] = k
nx = len(orbits); G = len(els)
m = gp.Model("bt"); m.Params.OutputFlag = 0; m.Params.TimeLimit = tl; m.Params.Threads = threads
m.Params.MIPGap = 0.0; m.Params.FeasibilityTol = 1e-9; m.Params.IntFeasTol = 1e-9
x = m.addVars(nx, vtype=GRB.BINARY, name="x")
z = m.addVars(G, lb=0.0, ub=1.0, name="z")
m.setObjective(z.sum(), GRB.MAXIMIZE)
Xo = lambda e: orb_of[e] if e != zero else None
for mm in els:
    zm = z[idx[mm]]
    for e, sgn in ((mm, 1), (subv(mm, t), 1), (addv(mm, t), -1)):
        xe = Xo(e)
        if xe is None:
            if sgn == 1: m.addConstr(zm <= 0)
            continue
        if sgn == 1: m.addConstr(zm <= x[xe])
        else: m.addConstr(zm + x[xe] <= 1)
seen = set(); ncons = 0
for chi in els:
    if chi == zero or chi in seen: continue
    seen.add(chi); seen.add(neg(chi))
    ph = sum((np.array([o[0][i] for o in orbits]) * chi[i]) / dims[i] for i in range(len(dims)))
    coef = np.array([len(o) * np.cos(2 * np.pi * pv) for o, pv in zip(orbits, ph)])
    nz = np.nonzero(np.abs(coef) > 1e-12)[0]
    m.addConstr(gp.quicksum(float(coef[k]) * x[int(k)] for k in nz) >= -K0); ncons += 1
if hint is not None:
    m.Params.Cutoff = hint - 0.5
t0 = time.time(); m.optimize(); dt = time.time() - t0
if m.SolCount == 0:
    print(json.dumps({"dims": dims, "t": t, "K0": K0, "status": m.Status, "time": round(dt, 1), "bound": m.ObjBound,
                      "note": "no feasible solution found (cutoff or time)"}))
    sys.exit(0)
xs = np.array([int(round(x[k].X)) for k in range(nx)])
A = [e for k, o in enumerate(orbits) if xs[k] for e in o]
S = set(A)
B = sum(1 for mm in els if mm in S and subv(mm, t) in S and addv(mm, t) not in S)
I = np.zeros(dims)
for e in A: I[e] = 1
F = np.fft.fftn(I).real; F[zero] = np.inf; K = -F.min()
print(json.dumps({"dims": dims, "t": t, "K0": K0, "status": m.Status, "optimal": m.Status == GRB.OPTIMAL,
                  "time": round(dt, 1), "obj": m.ObjVal, "bound": m.ObjBound, "gap": m.MIPGap, "B_t": B,
                  "K": round(K, 9), "|A|": len(A), "ratio_B_K3": B / K ** 3 if K > 0 else None,
                  "nodes": m.NodeCount, "gurobi": ".".join(map(str, gp.gurobi.version()))}))
if extra:
    with open(extra, "w") as fh: json.dump({"dims": dims, "t": t, "A": A}, fh)
