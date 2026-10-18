"""Structured exact MILP for dense sets: A ⊂ [1, X], |A| = n0, the core [1, Y] has at most H holes, tail (Y, X] free.
min lam s.t. f_A(x) + lam >= 0 at cut points (lazy cuts at true minimisers), Σ_{a<=Y} z_a >= Y − H.
Optimal value = exact optimum of the RESTRICTED box problem (HiGHS numerics, not interval-certified); certify A separately.
The restriction is motivated by the exhaustive optima N <= 40 (E14): core [1, ~0.6X] with 1–3 holes, X ≈ 1.38N.
Usage: python src/box_core_milp.py X n0 Y H timelimit [threads] [warm.json]
"""
from __future__ import annotations
import sys, math, json, time
import numpy as np
import highspy
sys.path.insert(0, 'src')
from box_minlam import true_min


def solve(X, n0, Y, H, tl, threads=2, warm=None, verbose=True):
    h = highspy.Highs(); h.setOptionValue("output_flag", False)
    h.setOptionValue("mip_rel_gap", 1e-6); h.setOptionValue("threads", threads)
    inf = highspy.kHighsInf
    for n in range(1, X + 1):
        h.addVar(0, 1)
    h.addVar(0, inf)                                         # lam, column X
    h.changeColsIntegrality(X, np.arange(X, dtype=np.int32), np.array([highspy.HighsVarType.kInteger] * X))
    cost = np.zeros(X + 1); cost[X] = 1.0
    h.changeColsCost(X + 1, np.arange(X + 1, dtype=np.int32), cost)
    h.addRow(n0, n0, X, np.arange(X, dtype=np.int32), np.ones(X))
    h.addRow(Y - H, inf, Y, np.arange(Y, dtype=np.int32), np.ones(Y))
    nn = np.arange(1, X + 1)
    def add_points(xs):
        for x in xs:
            h.addRow(0, inf, X + 1, np.arange(X + 1, dtype=np.int32), np.append(np.cos(nn * x), 1.0))
    add_points(np.pi * np.arange(4 * X + 1) / (4 * X))
    if warm is not None:
        (fm, xm), v, G = true_min(warm)
        loc = [math.pi * j / G for j in range(1, G) if v[j] <= v[j - 1] and v[j] <= v[j + 1] and v[j] < 0.7 * fm]
        add_points(loc[:300] + [xm])
    t0 = time.time(); best = None
    for rnd in range(300):
        if warm is not None and rnd == 0:
            ws = np.zeros(X + 1); ws[np.array(warm) - 1] = 1; ws[X] = -true_min(warm)[0][0] + 1e-9
            sol = highspy.HighsSolution(); sol.col_value = list(ws); sol.value_valid = True
            h.setSolution(sol)
        h.setOptionValue("time_limit", max(5.0, tl - (time.time() - t0)))
        h.run()
        st = h.getModelStatus(); info = h.getInfo()
        x = np.array(h.getSolution().col_value)
        if len(x) < X + 1: return dict(status=str(st), fail=True)
        A = [int(n) for n in nn[x[:X] > 0.5]]; lam = x[X]
        (fm, xm), v, G = true_min(A)
        if best is None or -fm < best[0]: best = (-fm, A)
        if verbose:
            print(f"  rnd {rnd}: lam_relaxed={lam:.5f} bound={info.mip_dual_bound:.5f} true M={-fm:.5f} status={st} "
                  f"t={time.time()-t0:.0f}s", flush=True)
        if -fm <= lam + 1e-7 or time.time() - t0 > tl:
            return dict(X=X, n0=n0, Y=Y, H=H, lam_relaxed=float(lam), dual_bound=float(info.mip_dual_bound),
                        status=str(st), best_M=best[0], A=best[1], R=best[0] / math.sqrt(n0),
                        secs=time.time() - t0, rounds=rnd + 1)
        add = {xm}
        for j in np.flatnonzero(v < -lam):
            if 0 < j < G and v[j] <= v[j - 1] and v[j] <= v[j + 1]: add.add(math.pi * j / G)
        add_points(sorted(add)[:200])


if __name__ == "__main__":
    X, n0, Y, H = map(int, sys.argv[1:5]); tl = float(sys.argv[5])
    threads = int(sys.argv[6]) if len(sys.argv) > 6 else 2
    warm = json.load(open(sys.argv[7]))["A"] if len(sys.argv) > 7 else None
    print(json.dumps(solve(X, n0, Y, H, tl, threads, warm)), flush=True)
