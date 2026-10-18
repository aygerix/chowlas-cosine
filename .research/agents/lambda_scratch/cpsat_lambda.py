#!/usr/bin/env python
"""Exact maximum of G = #{d >= 1 : r_D(d) = lam} over D ⊂ [0, L] with 0, L ∈ D (span exactly L), |D| = k.
r_D(d) = #{(u, v) ∈ D^2 : u - v = d}.  phi = lam*G / C(k,2);  defect pairs = C(k,2) - lam*G;  W = 2*(defect pairs).
CP-SAT (OR-tools) model: x_i bool, p_{i,d} = x_i AND x_{i+d}, r_d = sum_i p_{i,d}, g_d => r_d == lam, maximize sum g_d.
Symmetry breaking (valid): D and L - D give the same r; require #(D ∩ [0, L/2)) >= #(D ∩ (L/2, L]).
Usage: cpsat_lambda.py lam k Lmin Lmax [time_per_L] [workers]
Prints one line per L: status (OPTIMAL = solver-certified), G, phi, defect pairs, D.
"""
import sys, time
from ortools.sat.python import cp_model


def r_of(D):
    D = sorted(D)
    r = {}
    for i in range(len(D)):
        for j in range(i):
            d = D[i] - D[j]
            r[d] = r.get(d, 0) + 1
    return r


def solve(lam, k, L, tlim, workers, hintD=None, lb=None):
    m = cp_model.CpModel()
    x = [m.NewBoolVar(f"x{i}") for i in range(L + 1)]
    m.Add(x[0] == 1)
    m.Add(x[L] == 1)
    m.Add(sum(x) == k)
    # symmetry breaking
    left = [x[i] for i in range(L + 1) if 2 * i < L]
    right = [x[i] for i in range(L + 1) if 2 * i > L]
    m.Add(sum(left) >= sum(right))
    g = {}
    rsum = []
    for d in range(1, L + 1):
        ps = []
        for i in range(0, L - d + 1):
            p = m.NewBoolVar("")
            m.AddBoolOr([x[i].Not(), x[i + d].Not(), p])
            m.AddImplication(p, x[i])
            m.AddImplication(p, x[i + d])
            ps.append(p)
        rd = sum(ps)
        rsum.append(rd)
        if d == L:
            continue  # r(L) = 1 always (span exactly L)
        if L - d + 1 < lam:
            continue
        gd = m.NewBoolVar(f"g{d}")
        m.Add(rd == lam).OnlyEnforceIf(gd)
        g[d] = gd
    m.Add(sum(rsum) == k * (k - 1) // 2)
    m.Add(lam * sum(g.values()) <= k * (k - 1) // 2 - 1)
    if lb is not None:
        m.Add(sum(g.values()) >= lb)
    m.Maximize(sum(g.values()))
    if hintD is not None:
        hs = set(hintD)
        for i in range(L + 1):
            m.AddHint(x[i], 1 if i in hs else 0)
    s = cp_model.CpSolver()
    s.parameters.max_time_in_seconds = tlim
    s.parameters.num_search_workers = workers
    t0 = time.time()
    st = s.Solve(m)
    dt = time.time() - t0
    if st in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        D = [i for i in range(L + 1) if s.Value(x[i])]
        r = r_of(D)
        G = sum(1 for d, c in r.items() if c == lam)
        return s.StatusName(st), G, int(s.BestObjectiveBound()), D, dt
    return s.StatusName(st), None, int(s.BestObjectiveBound()) if st != cp_model.INFEASIBLE else None, None, dt


if __name__ == "__main__":
    lam, k, Lmin, Lmax = map(int, sys.argv[1:5])
    tlim = float(sys.argv[5]) if len(sys.argv) > 5 else 600
    workers = int(sys.argv[6]) if len(sys.argv) > 6 else 4
    P = k * (k - 1) // 2
    for L in range(Lmin, Lmax + 1):
        st, G, ub, D, dt = solve(lam, k, L, tlim, workers)
        if G is None:
            print(f"lam={lam} k={k} L={L} status={st} G=None ub={ub} t={dt:.1f}", flush=True)
            continue
        print(f"lam={lam} k={k} L={L} status={st} G={G} ub={ub} phi={lam*G/P:.4f} defpairs={P-lam*G} t={dt:.1f} D={','.join(map(str,D))}", flush=True)
