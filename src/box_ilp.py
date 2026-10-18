"""Exact box-restricted optimisation via MILP with cutting planes (HiGHS through scipy.optimize.milp).

maximise |A|  s.t.  A ⊂ [1, X],  f_A(x) >= -lam  for all x in [0, pi]  (constraints added lazily at violating x).
Termination: the returned A satisfies the constraint at every point of a 64X-point grid + Newton polish (UNCERTIFIED);
re-certify with chowla.certify_lower_bound.  Optimality of |A| is exact w.r.t. the constraints actually added
(a relaxation of the true problem), hence N_max(X, lam) <= returned value is NOT implied; the returned N is an
UPPER bound on the true box optimum only if every true constraint is implied — it is a relaxation, so
returned N >= true optimum, and if the final A is feasible (certified) it IS the true optimum.
"""
from __future__ import annotations
import sys, math, json, time
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds


def true_min(A, X, over=64):
    G = 1 << math.ceil(math.log2(over * X))
    c = np.zeros(2 * G); c[A] = 1
    v = np.fft.rfft(c).real[: G + 1]                     # f at x = pi j / G, j=0..G
    js = np.argsort(v)[:8]
    best = (v[js[0]], math.pi * js[0] / G)
    Aa = np.asarray(A, float)
    for j in js:
        x = math.pi * j / G
        for _ in range(30):
            d1 = -(Aa * np.sin(Aa * x)).sum(); d2 = -(Aa * Aa * np.cos(Aa * x)).sum()
            if d2 <= 0: break
            x -= d1 / d2
        fx = np.cos(Aa * x).sum()
        if fx < best[0]: best = (fx, x)
    return best, v, G


def solve(X, lam, G0=None, max_rounds=60, time_limit=600, verbose=False):
    n = np.arange(1, X + 1)
    if G0 is None: G0 = 4 * X
    xs = list(np.pi * np.arange(G0 + 1) / G0)
    t0 = time.time()
    for rnd in range(max_rounds):
        Cm = np.cos(np.outer(xs, n))
        cons = LinearConstraint(Cm, lb=-lam * np.ones(len(xs)), ub=np.inf)
        res = milp(c=-np.ones(X), constraints=[cons], integrality=np.ones(X), bounds=Bounds(0, 1),
                   options=dict(time_limit=max(10, time_limit - (time.time() - t0)), disp=False))
        if res.x is None:
            return None
        A = [int(k) for k in n[res.x > 0.5]]
        (fm, xm), v, G = true_min(A, X)
        if verbose:
            print(f"round {rnd}: N={len(A)} min={fm:.5f} (lam {lam}) cons={len(xs)} status={res.status} t={time.time()-t0:.0f}s", flush=True)
        if fm >= -lam - 1e-9:
            return dict(A=A, N=len(A), min=fm, xmin=xm, rounds=rnd + 1, status=int(res.status),
                        mip_gap=float(getattr(res, 'mip_gap', np.nan) or 0), secs=time.time() - t0)
        # add the violating points: polished argmin + all grid local minima below -lam
        bad = np.flatnonzero(v < -lam)
        add = {xm}
        for j in bad:
            if (j == 0 or v[j] <= v[j - 1]) and (j == G or v[j] <= v[j + 1]):
                add.add(math.pi * j / G)
        xs.extend(sorted(add))
    return None


if __name__ == "__main__":
    X = int(sys.argv[1]); lams = [float(s) for s in sys.argv[2].split(",")]
    tl = float(sys.argv[3]) if len(sys.argv) > 3 else 600
    for lam in lams:
        r = solve(X, lam, time_limit=tl)
        if r is None:
            print(json.dumps(dict(X=X, lam=lam, fail=True))); continue
        r.update(X=X, lam=lam, R=lam / math.sqrt(r["N"]), R_actual=-r["min"] / math.sqrt(r["N"]))
        print(json.dumps(r), flush=True)
