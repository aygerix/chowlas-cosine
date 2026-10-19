"""E64 anatomy: do the optimal E of the one-step class use VERTEX LOCKING (NOTEBOOK 2026-10-19, triangle geometry)?
For A = 3D ∪ E: P(x) = f_D(3x) + Mt, Z(x) = Σ_{e∈E, e≡1} e^{iex} + conj(Σ_{e≡2} e^{iex}). Z(x) lies in the triangle of
inradius P. Report, on a fine grid in x:
- the L² share of Z outside the incircle: ∫_{|Z|>P}|Z|² / ∫|Z|²;
- the max of |Z|/P;
- the mean angle to the nearest vertex direction where |Z| > P;
- the overlap of E with Bu's E.
Usage: python src/e64_anatomy.py examples/e64/e64.jsonl [examples/e64/e64_dense.jsonl ...]
"""
import json, math, sys
import numpy as np


def anatomy(D, E, Mt, G=1 << 16):
    x = 2 * np.pi * np.arange(G) / G
    P = np.cos(np.outer(3 * np.asarray(D), x)).sum(0) + Mt
    Z = np.zeros(G, complex)
    for e in E:
        Z += np.exp(1j * e * x) if e % 3 == 1 else np.exp(-1j * e * x)
    absZ = np.abs(Z); out = absZ > P
    share = float((absZ[out] ** 2).sum() / max((absZ ** 2).sum(), 1e-300))
    ang = np.angle(Z) % (2 * np.pi / 3)
    dev = np.minimum(ang, 2 * np.pi / 3 - ang)              # distance to the nearest vertex direction
    viol = float((P + np.min([np.real(Z * np.exp(2j * np.pi * j / 3)) for j in range(3)], axis=0)).min())
    return dict(share_outside_incircle=round(share, 4), max_Z_over_P=round(float((absZ / np.maximum(P, 1e-12)).max()), 3),
                mean_dev_deg_outside=round(float(np.degrees(dev[out]).mean()) if out.any() else float("nan"), 2),
                min_slack=round(viol, 4))


import os
for fn in sys.argv[1:]:
    if not os.path.exists(fn):
        continue
    for line in open(fn):
        d = json.loads(line)
        if d.get("event") != "final":
            continue
        D = sorted(set(a // 3 for a in d["A"] if a % 3 == 0))
        E = d["E"]
        S = d.get("S")
        EBu = sorted({abs(3 * (a + b) + 1) for i, a in enumerate(S) for b in S[i + 1:]}) if S else []
        rec = dict(file=fn, k=d.get("k"), D_file=d.get("D_file"), nD=len(D), nE=len(E), lam=round(d["lam"], 3),
                   R_A=round(d["R_A"], 4), R_Bu=d.get("R_Bu"), overlap_Bu=len(set(E) & set(EBu)),
                   **anatomy(D, E, d["Mt"]))
        if EBu:
            rec["Bu_anatomy"] = anatomy(D, EBu, d["Mt"])
        print(json.dumps(rec))
