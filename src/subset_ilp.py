"""MILP subset selection from a universe U: maximise |A'| s.t. A' ⊂ U, f_{A'}(x) >= -lam ∀x (cutting planes).
UNCERTIFIED final feasibility check (grid 64*maxU + Newton); certify separately.
Usage: python src/subset_ilp.py <universe.json key|'bu:<key>'> lam1,lam2 timelimit [extra_interval_L]
"""
from __future__ import annotations
import sys, math, json, time
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds


def fmin_check(A, over=32):
    X = max(A)
    G = 1 << math.ceil(math.log2(over * X))
    c = np.zeros(2 * G); c[A] = 1
    v = np.fft.rfft(c).real[: G + 1]
    Aa = np.asarray(A, float)
    cands = np.argsort(v)[:12]
    best = (v[cands[0]], math.pi * cands[0] / G)
    for j in cands:
        x = math.pi * j / G
        for _ in range(40):
            d1 = -(Aa * np.sin(Aa * x)).sum(); d2 = -(Aa * Aa * np.cos(Aa * x)).sum()
            if d2 <= 0: break
            x -= d1 / d2
        fx = np.cos(Aa * x).sum()
        if fx < best[0]: best = (fx, x)
    return best, v, G


def solve(U, lam, time_limit=600, G0=None, verbose=True):
    U = np.array(sorted(set(U)))
    X = U.max()
    if G0 is None: G0 = 8 * len(U)
    xs = list(np.pi * np.arange(G0 + 1) / G0)
    # seed constraints at local minima of f_U as well
    t0 = time.time()
    for rnd in range(80):
        Cm = np.cos(np.outer(xs, U))
        res = milp(c=-np.ones(len(U)), constraints=[LinearConstraint(Cm, lb=-lam, ub=np.inf)],
                   integrality=np.ones(len(U)), bounds=Bounds(0, 1),
                   options=dict(time_limit=max(10, time_limit - (time.time() - t0)), disp=False))
        if res.x is None:
            return None
        A = [int(u) for u in U[res.x > 0.5]]
        (fm, xm), v, G = fmin_check(A)
        if verbose:
            print(f"  round {rnd}: N={len(A)} min={fm:.4f} cons={len(xs)} status={res.status} t={time.time()-t0:.0f}s", flush=True)
        if fm >= -lam - 1e-9:
            return dict(A=A, N=len(A), min=float(fm), status=int(res.status), rounds=rnd + 1, secs=time.time() - t0)
        bad = np.flatnonzero(v < -lam)
        add = {xm}
        for j in bad:
            if (j == 0 or v[j] <= v[j - 1]) and (j == G or v[j] <= v[j + 1]):
                add.add(math.pi * j / G)
        xs.extend(sorted(add)[:400])
        if time.time() - t0 > time_limit: return dict(A=A, N=len(A), min=float(fm), status=-1, infeasible_last=True)
    return None


if __name__ == "__main__":
    sys.path.insert(0, "src")
    spec, lams, tl = sys.argv[1], [float(s) for s in sys.argv[2].split(",")], float(sys.argv[3])
    Lx = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    if spec.startswith("bu:"):
        from bu import A_of_S
        d = json.load(open("examples/bu_reproduction_certified.json"))[spec[3:]]
        U = A_of_S(d["S"])
    else:
        U = json.load(open(spec))["A"]
    U = sorted(set(U) | set(range(1, Lx + 1)))
    print(f"universe size {len(U)}, max {max(U)}", flush=True)
    for lam in lams:
        r = solve(U, lam, tl)
        if r is None: print(json.dumps(dict(lam=lam, fail=True)), flush=True); continue
        r.update(lam=lam, R_actual=-r["min"] / math.sqrt(r["N"]))
        print(json.dumps({k: (v if k != "A" else v) for k, v in r.items()}), flush=True)
