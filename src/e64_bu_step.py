"""E64: one Bu step with D fixed — can E beat |E| = |D| at Bu's minimum?

Setting (NOTEBOOK "Bu as a map; triangle geometry"): A = 3D ∪ E, E ∩ 3Z = ∅. With P(x) = f_D(3x) + M and
Z = Ẽ₁ + conj(Ẽ₂), f_A >= −M at x, x ± 2π/3 iff Z(x) lies in the equilateral triangle of inradius P. Bu's E (sums
|3(s + s') + 1|, s < s' in a Sidon set S; D = positive differences of S) has |Z| = P: Z on the INCIRCLE. Approximate
vertex-locking would allow |E| up to the pinch ceiling 2|D| + 2M. lambda = |E|/|D| > 1 at M(A) <= M_Bu would beat
½ when iterated: R(A)² = R(D)²/(1 + lambda).

Model (Gurobi): binaries z_e for 1 <= e <= XE, 3 ∤ e; maximise Σ z_e subject to f_{3D}(x) + Σ z_e cos(e x) >= −Mt at
cut points (initial grid + LAZY cuts at the true minimiser of every incumbent, box_minlam.true_min). Mt = (1 + eps)·M_Bu
with S shifted to the best Bu shift. Every cut is valid, so ObjBound is a valid upper bound on |E| for this (D, Mt, XE)
up to float evaluation. Status: NUMERICAL-EXACT class optimum (not interval-certified).
Usage: python src/e64_bu_step.py k [--eps e] [--mt bu|d] [--D-file f.json] [--xe-factor f] [--tl s] [--threads t]
       [--out f.jsonl]
"""
from __future__ import annotations
import argparse, json, math, sys, time
import numpy as np
import gurobipy as gp
from gurobipy import GRB
sys.path.insert(0, "src")
from box_minlam import true_min

GOLOMB = {6: [0, 1, 4, 10, 12, 17], 7: [0, 1, 4, 10, 18, 23, 25], 8: [0, 1, 4, 9, 15, 22, 32, 34],
          9: [0, 1, 5, 12, 25, 27, 35, 41, 44], 10: [0, 1, 6, 10, 23, 26, 34, 41, 53, 55],
          11: [0, 1, 4, 13, 28, 33, 47, 54, 64, 70, 72], 12: [0, 2, 6, 24, 29, 40, 43, 55, 68, 75, 76, 85],
          13: [0, 2, 5, 25, 37, 43, 59, 70, 85, 89, 98, 99, 106],
          14: [0, 4, 6, 20, 35, 52, 59, 77, 78, 86, 89, 99, 122, 127]}


def bu_parts(S):
    D = sorted({b - a for a in S for b in S if b > a})
    E = sorted({abs(3 * (a + b) + 1) for i, a in enumerate(S) for b in S[i + 1:]})
    return D, E


def best_shift(G):
    best = None
    for c in range(-max(G) - 1, 1):
        S = [g + c for g in G]
        D, E = bu_parts(S)
        A = sorted(set(3 * d for d in D) | set(E))
        assert len(A) == len(D) + len(E)
        (fm, xm), _, _ = true_min(A)
        if best is None or -fm < best[0]:
            best = (-fm, c, S, D, E, A)
    return best


def solve(D, Mt, XE, tl, threads, warmE, log=print):
    T = [3 * d for d in D]
    cand = [e for e in range(1, XE + 1) if e % 3]
    m = gp.Model("bustep"); m.Params.OutputFlag = 0
    m.Params.LazyConstraints = 1; m.Params.Threads = threads; m.Params.TimeLimit = tl
    m.Params.FeasibilityTol = 1e-8; m.Params.IntFeasTol = 1e-8; m.Params.MIPGap = 0
    z = m.addVars(cand, vtype=GRB.BINARY, name="z")
    zl = [z[e] for e in cand]
    m.setObjective(z.sum(), GRB.MAXIMIZE)
    ce = np.asarray(cand, float); Ta = np.asarray(T, float)

    def cut(x):
        return gp.LinExpr(np.cos(ce * x).tolist(), zl) >= -Mt - float(np.cos(Ta * x).sum())

    Xall = max(max(T), XE)
    for j in range(1, 4 * Xall + 1):
        m.addConstr(cut(math.pi * j / (4 * Xall)))
    W = set(warmE)
    for e in cand:
        z[e].Start = 1.0 if e in W else 0.0
    best = dict(n=len(warmE), E=sorted(warmE)); t0 = time.time(); st = dict(lazy=0, sols=0)
    last = [t0]

    def cb(model, where):
        if where == GRB.Callback.MIP and time.time() - last[0] > 300:
            last[0] = time.time()
            log(json.dumps(dict(event="progress", t=round(last[0] - t0), bound=model.cbGet(GRB.Callback.MIP_OBJBND),
                                best=best["n"], nodes=model.cbGet(GRB.Callback.MIP_NODCNT))))
            return
        if where != GRB.Callback.MIPSOL:
            return
        zv = model.cbGetSolution(zl)
        E = [e for e, v in zip(cand, zv) if v > 0.5]
        (fm, xm), v, G = true_min(sorted(T + E))
        st["sols"] += 1
        if fm < -Mt - 1e-7:
            pts = [xm] + [math.pi * j / G for j in np.flatnonzero(v < -Mt)
                          if 0 < j < G and v[j] <= v[j - 1] and v[j] <= v[j + 1]][:30]
            for x in pts:
                model.cbLazy(cut(x))
            st["lazy"] += len(pts)
        elif len(E) > best["n"]:
            best.update(n=len(E), E=E)
            log(json.dumps(dict(event="incumbent", nE=len(E), M=-fm, t=round(time.time() - t0, 1))))

    m.optimize(cb)
    return dict(status=m.Status, optimal=m.Status == GRB.OPTIMAL, bound=m.ObjBound, nE=best["n"], E=best["E"],
                nodes=m.NodeCount, secs=round(time.time() - t0, 1), ncand=len(cand), **st)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("k", type=int, help="Golomb ruler size (ignored with --D-file)")
    ap.add_argument("--eps", type=float, default=0.0)
    ap.add_argument("--mt", choices=["bu", "d"], default="bu", help="Mt = (1+eps)*M_Bu or (1+eps)*M(D)")
    ap.add_argument("--D-file", help="JSON with key A: use this D instead of Sidon differences (implies --mt d)")
    ap.add_argument("--xe-factor", type=float, default=1.25); ap.add_argument("--tl", type=float, default=3600)
    ap.add_argument("--threads", type=int, default=4); ap.add_argument("--out")
    a = ap.parse_args()
    if a.D_file:
        D = sorted(json.load(open(a.D_file))["A"]); S = None; c = None; EBu = []; MBu = None; ABu = None
        a.mt = "d"
    else:
        MBu, c, S, D, EBu, ABu = best_shift(GOLOMB[a.k])
    MD = -true_min(D)[0][0]
    Mt = (1 + a.eps) * (MBu if a.mt == "bu" else MD)
    XE = int(a.xe_factor * max(max(EBu) if EBu else 0, 3 * max(D)))
    warm = EBu if a.mt == "bu" else []
    hdr = dict(event="setup", k=None if a.D_file else a.k, D_file=a.D_file, shift=c, S=S, nD=len(D), nEBu=len(EBu),
               M_Bu=MBu, R_Bu=MBu / math.sqrt(len(ABu)) if ABu else None, M_D=MD, R_D=MD / math.sqrt(len(D)),
               mt=a.mt, Mt=Mt, eps=a.eps, XE=XE, pinch=2 * len(D) + 2 * Mt)
    print(json.dumps(hdr), flush=True)
    res = solve(D, Mt, XE, a.tl, a.threads, warm)
    A = sorted(set(3 * d for d in D) | set(res["E"]))
    (fm, xm), _, _ = true_min(A)
    out = dict(hdr, **res, lam=res["nE"] / len(D), M_A=-fm, R_A=-fm / math.sqrt(len(A)), A=A,
               gurobi=".".join(map(str, gp.gurobi.version())))
    out["event"] = "final"
    print(json.dumps(out), flush=True)
    if a.out:
        with open(a.out, "a") as fh:
            fh.write(json.dumps(out) + "\n")
