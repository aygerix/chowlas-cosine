"""Gurobi exact dense optimum: min M(A) over A ⊂ [1, X], |A| = n0 (optionally: core [1, Y] with at most H holes).
Model: binaries z_1..z_X, lam >= 0, Σ z = n0, minimise lam subject to lam + Σ_n z_n cos(n x) >= 0 at cut points x.
Cut points: the grid x = πj/(grid·X) at the start (default grid 8); USER cuts at fractional nodes (MIPNODE callback:
local minima of the relaxed f_z below −lam on the grid πj/2^⌈log2 16X⌉, up to 6 per node); LAZY cuts at every incumbent
(MIPSOL callback) the true minimiser of f_A (FFT grid + Newton, box_minlam.true_min) and the grid local minima below
−lam are added whenever f_A(x*) < −lam − tol. Every cut is valid for every A, so ObjBound is a valid lower bound for
the (restricted) box problem and the final incumbent is optimal up to Gurobi's tolerances and float evaluation of f.
Status: NUMERICAL-EXACT (not interval-certified). Certify the output set with chowla.certify_lower_bound + sturm_certify.
Usage: python src/grb_dense.py X n0 [--Y Y --H H] [--tl s] [--threads t] [--warm f.json ...] [--out f.json]
"""
from __future__ import annotations
import argparse, json, math, sys, time
import numpy as np
import gurobipy as gp
from gurobipy import GRB
sys.path.insert(0, "src")
from box_minlam import true_min


def solve(X, n0, Y=None, H=None, tl=3600.0, threads=4, warm=(), tol=1e-7, log=print, grid=4, nodecuts=False, focus=0):
    m = gp.Model("dense"); m.Params.OutputFlag = 0
    m.Params.LazyConstraints = 1; m.Params.Threads = threads; m.Params.TimeLimit = tl
    m.Params.MIPGap = 1e-7; m.Params.FeasibilityTol = 1e-8; m.Params.IntFeasTol = 1e-8
    m.Params.MIPFocus = focus
    if nodecuts:
        m.Params.PreCrush = 1                      # required for user cuts (cbCut) at fractional nodes
    z = m.addVars(range(1, X + 1), vtype=GRB.BINARY, name="z")
    lam = m.addVar(lb=0.0, name="lam")
    m.setObjective(lam, GRB.MINIMIZE)
    m.addConstr(z.sum() == n0)
    if Y is not None:
        m.addConstr(gp.quicksum(z[n] for n in range(1, Y + 1)) >= Y - H)
    nn = np.arange(1, X + 1)
    zl = [z[n] for n in range(1, X + 1)]

    def cut_expr(x):
        return gp.LinExpr(np.cos(nn * x).tolist() + [1.0], zl + [lam])

    for j in range(1, grid * X + 1):
        m.addConstr(cut_expr(math.pi * j / (grid * X)) >= 0)
    GN = 1 << math.ceil(math.log2(16 * X))           # node-cut separation grid x = πj/GN
    best = dict(M=math.inf, A=None)
    for A in warm:                                 # warm-start points: their minimisers and the best start
        A = [a for a in A if 1 <= a <= X]
        if len(A) != n0 or (Y is not None and sum(1 for a in A if a <= Y) < Y - H):
            continue
        (fm, xm), v, G = true_min(A)
        m.addConstr(cut_expr(xm) >= 0)
        if -fm < best["M"]:
            best = dict(M=-fm, A=sorted(A))
    if best["A"] is not None:
        S = set(best["A"])
        for n in range(1, X + 1):
            z[n].Start = 1.0 if n in S else 0.0
        lam.Start = best["M"] + 1e-9
    t0 = time.time(); stats = dict(lazy=0, sols=0, usercuts=0)

    last = [t0]

    def cb(model, where):
        if where == GRB.Callback.MIP and time.time() - last[0] > 300:     # progress line every 5 min
            last[0] = time.time()
            log(json.dumps(dict(event="progress", t=round(last[0] - t0), bound=model.cbGet(GRB.Callback.MIP_OBJBND),
                                best_M=best["M"], nodes=model.cbGet(GRB.Callback.MIP_NODCNT))))
            return
        if (nodecuts and where == GRB.Callback.MIPNODE
                and model.cbGet(GRB.Callback.MIPNODE_STATUS) == GRB.OPTIMAL):
            # Separation at a fractional node: f_zrel(x) + lam_rel < 0 at some x gives a violated valid cut.
            zr = np.asarray(model.cbGetNodeRel(zl)); lr = model.cbGetNodeRel(lam)
            c = np.zeros(2 * GN); c[1:X + 1] = zr
            v = np.fft.rfft(c).real[: GN + 1]
            js = [j for j in np.argsort(v)[:40] if v[j] < -lr - 1e-4 and 0 < j < GN
                  and v[j] <= v[j - 1] and v[j] <= v[j + 1]][:6]
            for j in js:
                model.cbCut(cut_expr(math.pi * j / GN) >= 0)
            stats["usercuts"] += len(js)
            return
        if where != GRB.Callback.MIPSOL:
            return
        zv = model.cbGetSolution(zl); lv = model.cbGetSolution(lam)
        A = [n for n in range(1, X + 1) if zv[n - 1] > 0.5]
        (fm, xm), v, G = true_min(A)
        stats["sols"] += 1
        if -fm < best["M"] - 1e-12:
            best.update(M=-fm, A=A)
            log(json.dumps(dict(event="incumbent", M=-fm, R=-fm / math.sqrt(n0), lam=lv, t=round(time.time() - t0, 1),
                                A=A)))
        if fm < -lv - tol:
            pts = [xm] + [math.pi * j / G for j in np.flatnonzero(v < -lv)
                          if 0 < j < G and v[j] <= v[j - 1] and v[j] <= v[j + 1]][:30]
            for x in pts:
                model.cbLazy(cut_expr(x) >= 0)
            stats["lazy"] += len(pts)

    m.optimize(cb)
    out = dict(X=X, n0=n0, Y=Y, H=H, status=m.Status, optimal=(m.Status == GRB.OPTIMAL), bound=m.ObjBound,
               obj=m.ObjVal if m.SolCount else None, best_M=best["M"], R=best["M"] / math.sqrt(n0), A=best["A"],
               R_bound=m.ObjBound / math.sqrt(n0), nodes=m.NodeCount, secs=round(time.time() - t0, 1), **stats,
               gurobi=".".join(map(str, gp.gurobi.version())))
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("X", type=int); ap.add_argument("n0", type=int)
    ap.add_argument("--Y", type=int); ap.add_argument("--H", type=int, default=0)
    ap.add_argument("--tl", type=float, default=3600); ap.add_argument("--threads", type=int, default=4)
    ap.add_argument("--warm", nargs="*", default=[]); ap.add_argument("--out")
    ap.add_argument("--grid", type=int, default=4); ap.add_argument("--nodecuts", type=int, default=0)
    ap.add_argument("--focus", type=int, default=0)
    a = ap.parse_args()
    warm = []
    for fn in a.warm:
        d = json.load(open(fn))
        for v in (d.values() if isinstance(d, dict) and "A" not in d else [d]):
            if isinstance(v, dict) and "A" in v: warm.append(v["A"])
    res = solve(a.X, a.n0, a.Y, a.H if a.Y is not None else None, a.tl, a.threads, warm,
                grid=a.grid, nodecuts=bool(a.nodecuts), focus=a.focus)
    print(json.dumps(dict(event="final", **res)), flush=True)
    if a.out:
        json.dump(res, open(a.out, "w"), indent=1)
