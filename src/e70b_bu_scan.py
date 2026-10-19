"""E70b: P47 high-pass window family on Bu/Singer sets for growing q (does best/sqrt(n) stay bounded below?).
Uses e67_zoo.bu(q) (best shift by grid M) and e70_p47_scan.p47_family. NUMERICAL (rho = 0.687; true M grid+Newton).
Usage: python src/e70b_bu_scan.py [--rig] q1 q2 ...   (--rig: rigorous rho_L = 4/(3 sqrt 3)(1+2/sqrt(L+1))^3)"""
import json, math, sys
sys.path.insert(0, "src")
from e67_zoo import bu
from e70_p47_scan import p47_family
from box_minlam import true_min
RIG = "--rig" in sys.argv
for q in [int(a) for a in sys.argv[1:] if not a.startswith("--")]:
    A, r = bu(q); n = len(A)
    (fm, xm), _, _ = true_min(A, over=16); M = -fm
    (b, h, th), Es = p47_family(A, RIG)
    print(json.dumps(dict(q=q, n=n, X=max(A), M=round(M, 3), R=round(M / math.sqrt(n), 4), best=round(b, 3),
                          best_over_sqrtn=round(b / math.sqrt(n), 4), best_over_M=round(b / M, 4), h=h, theta=th, rig=RIG,
                          E_by_h={str(k): round(e / n, 4) for k, e in Es})), flush=True)
