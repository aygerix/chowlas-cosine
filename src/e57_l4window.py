"""E57: L^4 window inequality (nonlinear upgrade of P31) vs P31.
Nikolskii L^4/L^1 for nonneg trig polys of degree L:  ||h||_4^4 <= C4(L) (L+1)^3 ||h||_1^4,
  C4(L) = sup_{u>=0} ||u*u*u*u||_2^2 / ((L+1)^3 ||u||_2^8)   (h = |U|^2, ||h||_4^4 = ||U^4||_2^2, ||h||_1 = ||u||^2).
Window step (as in P31, h = F_w(x - x0)(f + M) >= 0, degree X + w), integrated over x0:
  mean(F^4) * mean((f+M)^4) <= C4 (L+1)^3 * mean((M+g)^4),   g = f * F_w.
mean((f+M)^4) = M^4 + 3M^2 n + 4M*(3/4)T + (3/8)E + (1/2)T3 involves Schur triples / additive energy: NONLINEAR in 1_A.
For each set and w we compute the least M >= 0 for which the L^4 inequality holds (the L^4 lower bound) and the same for
P31 (L^2), using exact grid means (grid > 4 deg). C4 from part 1 (L-BFGS over u >= 0, several starts).
Usage: python src/e57_l4window.py > examples/e57/e57.jsonl
"""
import json, math, sys
import numpy as np
from scipy.optimize import minimize
sys.path.insert(0, "src")

def c4_of(L, starts=8, seed=0):
    rng = np.random.default_rng(seed); best = 0.0
    N = L + 1; G = 1 << math.ceil(math.log2(4 * N + 1))
    def neg(z):
        u = z * z; U = np.fft.rfft(u, G); U4 = U ** 4; q = np.fft.irfft(U4, G)
        num = float((q ** 2).sum()); den = float((u ** 2).sum()) ** 4 * N ** 3
        # gradient via autodiff-free finite structure: d num/du = 8 * (q corr u^3-conv); use numeric-free formula
        U3 = U ** 3; c = np.fft.irfft(np.fft.rfft(q, G) * np.conj(U3), G)[:N]
        gnum = 8 * c; s2 = float((u ** 2).sum()); gden = 8 * s2 ** 3 * u * N ** 3
        val = num / den; g = (gnum * den - num * gden) / den ** 2
        return -val, -g * 2 * z
    for s in range(starts):
        z0 = np.sqrt(np.abs(np.sin(np.pi * (np.arange(N) + 0.5) / N)) ** (rng.uniform(0, 1.5)) + 0.05 * rng.random(N))
        r = minimize(neg, z0, jac=True, method="L-BFGS-B", options={"maxiter": 3000})
        best = max(best, -r.fun)
    return best

def grid_vals(coef, G):
    c = np.zeros(G); c[:len(coef)] = coef; return np.fft.fft(c).real

def least_M(lhs_fn, rhs_fn, hi):
    lo = 0.0
    if lhs_fn(0.0) <= rhs_fn(0.0): return 0.0
    while lhs_fn(hi) > rhs_fn(hi): hi *= 2
    for _ in range(80):
        mid = (lo + hi) / 2
        if lhs_fn(mid) > rhs_fn(mid): lo = mid
        else: hi = mid
    return hi

if __name__ == "__main__":
    out = sys.stdout
    Ls = (8, 16, 32, 64, 128, 256)
    c4 = {L: c4_of(L) for L in Ls}
    print(json.dumps({"C4": {str(L): round(v, 5) for L, v in c4.items()}}), file=out, flush=True)
    C4inf = max(c4.values())            # conservative: use the largest observed value for all L
    from e51_transfer import sets
    S = sets()
    for name in ("bu_101_20", "bu_199_40", "singer_diff_q31", "singer_diff_q61", "dense_N50", "e49_p1_n299_6",
                 "e49_p3_n300_8", "e50_a0.5_n299_10", "e50_a0.7_n300_12", "taper_random_X4000"):
        A = np.asarray(sorted(S[name])); X = int(A.max()); n = len(A)
        G = 1 << math.ceil(math.log2(8 * X + 8))
        coef = np.zeros(X + 1); coef[A] = 1
        f = grid_vals(coef, G); Mtrue = -f.min()
        rec = dict(set=name, n=n, X=X, R=round(Mtrue / math.sqrt(n), 4), rows=[])
        for wf in (0.05, 0.1, 0.2, 0.35, 0.5, 0.75, 1.0):
            w = max(1, int(round(wf * X)))
            kap = np.clip(1 - np.arange(X + 1) / (w + 1), 0, None)
            g = grid_vals(coef * kap, G)
            Fk = np.zeros(G); Fk[:w + 1] = kap[:w + 1]; Fk[G - w:] = kap[1:w + 1][::-1]
            F = np.fft.fft(Fk).real                       # Fejér kernel with mean 1
            mF4 = float((F ** 4).mean()); W = float((F ** 2).mean())
            L = X + w
            l4 = least_M(lambda M: mF4 * float(((f + M) ** 4).mean()),
                         lambda M: C4inf * (L + 1) ** 3 * float(((M + g) ** 4).mean()), max(1.0, Mtrue))
            rhoL = 0.7698
            l2 = least_M(lambda M: W * (n / 2 + M * M), lambda M: rhoL * (L + 1) * float(((M + g) ** 2).mean()), max(1.0, Mtrue))
            rec["rows"].append(dict(w_over_X=wf, L4_LB_R=round(l4 / math.sqrt(n), 4), L2_LB_R=round(l2 / math.sqrt(n), 4)))
        print(json.dumps(rec), file=out, flush=True)
