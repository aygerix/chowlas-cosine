"""EXP-1 exact: for the cube framework (PROOFS P7) solve
   maximize W = sum_S 2^{|S|} x_S  s.t.  C0 + sum_S 2^{|S|} chi_S(eps) x_S >= 0  for all eps in {±1}^k,
   x_S in {0,1} (S nonempty).  Then R_cube = C0/sqrt(2W) is optimal for that (k, C0).
Uses scipy.optimize.milp (HiGHS).  Results are exact optima of the ILP (up to solver tolerance; verified by
recomputing min g in exact integer arithmetic)."""
import sys, math, numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
sys.path.insert(0, 'src')
from cube import chi_matrix, popcount

def solve(k, C0, time_limit=600, sym_break=False):
    n = 1 << k
    chi = chi_matrix(k).astype(np.float64)[:, 1:]          # drop S = empty
    w = np.array([1 << popcount(S) for S in range(1, n)], float)
    Acon = chi * w[None, :]
    cons = [LinearConstraint(Acon, lb=-C0, ub=np.inf)]
    res = milp(c=-w, constraints=cons, integrality=np.ones(n - 1), bounds=Bounds(0, 1),
               options={"time_limit": time_limit, "disp": False})
    if res.x is None:
        return None
    x = np.round(res.x).astype(int)
    g = (chi.astype(np.int64) * w.astype(np.int64)[None, :]) @ x
    W = int(w @ x)
    sets = [S for S in range(1, n) if x[S - 1]]
    return dict(k=k, C0=C0, W=W, ming=int(g.min()), R=(-g.min()) / math.sqrt(2 * W) if W else None,
                status=res.status, sets=sets)

if __name__ == "__main__":
    k = int(sys.argv[1])
    for C0 in [int(c) for c in sys.argv[2].split(',')]:
        r = solve(k, C0)
        if r is None:
            print(k, C0, "infeasible/none"); continue
        hist = {}
        for S in r['sets']:
            hist[popcount(S)] = hist.get(popcount(S), 0) + 1
        print(f"k={k} C0={C0} W={r['W']} min_g={r['ming']} R={r['R']:.4f} status={r['status']} hist={dict(sorted(hist.items()))}")
        if k <= 6:
            print("   sets:", [bin(S)[2:].zfill(k)[::-1] for S in r['sets']])
