"""E69: NON-cumulative roundings with bounded prefix discrepancy D0 (test of P47, NOTEBOOK/PROOFS 2026-10-19).
Profiles p with p(1)=0. Roundings:
 - 'walk': randomized balanced rounding: a_m = 1 with prob p_m, forced to keep |D(m)| <= D0 (D = prefix discrepancy);
 - 'block': TD7-O-style adversarial blocks of length B: inside each block the block's quota of ones is placed as a
   2-chain at the block start (density p ~ 1/2 front gets the periodic '1100' pattern), discrepancy <= B+1.
Record R = M/sqrt(n) (grid+Newton, NUMERICAL) and the energy-profile front ratio e(0)/mean(e), e = p(1-p).
Usage: python src/e69_bdround.py"""
import json, math, os, sys
import numpy as np
sys.path.insert(0, "src")
from box_minlam import true_min
rng = np.random.default_rng(20261019)
PROF = {"half(1-t)^2": lambda t: 0.5 * (1 - t) ** 2, "(1-t)": lambda t: 1 - t, "half(1-t)^4": lambda t: 0.5 * (1 - t) ** 4,
        "0.9(1-t)^2": lambda t: 0.9 * (1 - t) ** 2}

def walk(p, D0):
    a = np.zeros(len(p), int); D = 0.0
    for m, pm in enumerate(p):
        want = rng.random() < pm
        if want and D + 1 - pm > D0: want = False
        if (not want) and D - pm < -D0: want = True
        a[m] = want; D += a[m] - pm
    return a

def block(p, B):
    X = len(p); a = np.zeros(X, int); Phi = np.cumsum(p); prev = 0
    for s in range(0, X, B):
        e = min(X, s + B); quota = int(math.floor(Phi[e - 1])) - prev; prev += quota
        if p[s] > 0.4:    # front: '1100' pattern
            pat = [1, 1, 0, 0]; k = 0; j = s
            while k < quota and j < e:
                if pat[(j - s) % 4]: a[j] = 1; k += 1
                j += 1
            j = s
            while k < quota and j < e:
                if not a[j]: a[j] = 1; k += 1
                j += 1
        else:             # later: one 2-chain at the block start
            j = s; k = 0
            while k < quota and j < e:
                a[j] = 1; k += 1; j += 2
            j = s + 1
            while k < quota and j < e:
                if not a[j]: a[j] = 1; k += 1
                j += 2
    return a

os.makedirs("examples/e69", exist_ok=True)
for name, pf in PROF.items():
    t = np.linspace(0, 1, 2001); e = pf(t) * (1 - pf(t)); ratio = float(e[0] / e.mean()) if e.mean() > 0 else float("nan")
    for lx in (12, 14, 16):
        X = 1 << lx; p = pf(np.arange(1, X + 1) / X)
        for kind, par in (("walk", 1), ("walk", 4), ("walk", 16), ("block", 16), ("block", 256)):
            a = walk(p, par) if kind == "walk" else block(p, par)
            A = (np.nonzero(a)[0] + 1).tolist(); D = np.abs(np.cumsum(a - p)).max()
            (fm, xm), _, _ = true_min(A, over=16)
            rec = dict(profile=name, e0_over_mean=round(ratio, 3), X=X, kind=kind, par=par, maxdisc=round(float(D), 2),
                       n=len(A), M=-fm, R=-fm / math.sqrt(len(A)), xmin=xm)
            print(json.dumps(rec), flush=True)
            with open("examples/e69/e69.jsonl", "a") as fh: fh.write(json.dumps(rec) + "\n")
