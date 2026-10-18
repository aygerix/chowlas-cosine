"""Box MILP, fixed size: min lam s.t. A ⊂ [1,X], |A| = n0, f_A(x) + lam >= 0 at constraint points (cutting planes).
HiGHS via highspy, optional warm start (an initial set).  Returns (lam*, A, status, gap).  lam* is a LOWER bound on
the true box optimum K_X(n0) whenever HiGHS proves optimality for the relaxed constraint set (every true constraint
set is a superset), and the returned A is a feasible point of the true problem up to the numerical min check, so
K_X(n0) ∈ [lam*_relaxed, M(A)]. UNCERTIFIED numerics; certify A separately.
Usage: python src/box_minlam.py X n0 timelimit [warmstart.json]
"""
from __future__ import annotations
import sys, math, json, time
import numpy as np
import highspy


def true_min(A, over=64):
    X = max(A); G = 1 << math.ceil(math.log2(over * X))
    c = np.zeros(2 * G); c[A] = 1
    v = np.fft.rfft(c).real[: G + 1]
    Aa = np.asarray(A, float); best = (v.min(), math.pi * int(v.argmin()) / G)
    for j in np.argsort(v)[:10]:
        x = math.pi * j / G
        for _ in range(40):
            d1 = -(Aa * np.sin(Aa * x)).sum(); d2 = -(Aa * Aa * np.cos(Aa * x)).sum()
            if d2 <= 0: break
            x -= d1 / d2
        fx = float(np.cos(Aa * x).sum())
        if fx < best[0]: best = (fx, x)
    return best, v, G


def solve(X, n0, tl, warm=None, verbose=True):
    h = highspy.Highs(); h.setOptionValue("output_flag", False)
    h.setOptionValue("mip_rel_gap", 1e-6)
    inf = highspy.kHighsInf
    for n in range(1, X + 1):
        h.addVar(0, 1)
    h.addVar(0, inf)                       # lam, index X
    h.changeColsIntegrality(X, np.arange(X, dtype=np.int32), np.array([highspy.HighsVarType.kInteger] * X))
    cost = np.zeros(X + 1); cost[X] = 1.0
    h.changeColsCost(X + 1, np.arange(X + 1, dtype=np.int32), cost)
    h.addRow(n0, n0, X, np.arange(X, dtype=np.int32), np.ones(X))
    nn = np.arange(1, X + 1)
    def add_points(xs):
        for x in xs:
            coef = np.append(np.cos(nn * x), 1.0)
            h.addRow(0, inf, X + 1, np.arange(X + 1, dtype=np.int32), coef)
    add_points(np.pi * np.arange(4 * X + 1) / (4 * X))
    if warm is not None:
        (fm, xm), v, G = true_min(warm)
        loc = [math.pi * j / G for j in range(1, G) if v[j] <= v[j - 1] and v[j] <= v[j + 1] and v[j] < 0.7 * fm]
        add_points(loc[:300] + [xm])
    t0 = time.time(); best_feasible = None
    sol_vals = None
    for rnd in range(200):
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
        if best_feasible is None or -fm < best_feasible[0]:
            best_feasible = (-fm, A)
        if verbose:
            print(f"  rnd {rnd}: lam_relaxed={lam:.5f} bound={info.mip_dual_bound:.5f} N={len(A)} true M={-fm:.5f} "
                  f"status={st} t={time.time()-t0:.0f}s", flush=True)
        if -fm <= lam + 1e-7 or time.time() - t0 > tl:
            return dict(X=X, n0=n0, lam_relaxed=float(lam), dual_bound=float(info.mip_dual_bound),
                        status=str(st), best_M=best_feasible[0], A=best_feasible[1],
                        R=best_feasible[0] / math.sqrt(n0), secs=time.time() - t0, rounds=rnd + 1)
        bad = np.flatnonzero(v < -lam)
        add = {xm}
        for j in bad:
            if (j == 0 or v[j] <= v[j - 1]) and (j == G or v[j] <= v[j + 1]):
                add.add(math.pi * j / G)
        add_points(sorted(add)[:200])
    return None


if __name__ == "__main__":
    X, n0, tl = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
    warm = json.load(open(sys.argv[4]))["A"] if len(sys.argv) > 4 else None
    if warm is not None and (len(warm) != n0 or max(warm) > X): warm = None
    r = solve(X, n0, tl, warm)
    print(json.dumps(r), flush=True)
