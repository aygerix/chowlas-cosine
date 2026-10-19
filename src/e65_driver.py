"""E65 driver: one Bu step at larger k (Singer sets) by annealing (src/e65_bustep_sa.c).
For each prime q: S = Singer set mod v = q^2+q+1 (k = q+1, Sidon in Z), integer shift c near the centre chosen to
minimise M of Bu's set A = 3D ∪ E_Bu (D = positive differences, E_Bu = {|3(s+s')+1| : s < s'}). Then for each lambda,
anneal E (|E| = round(lambda·|D|), started from E_Bu padded at random) and record the grid M of 3D ∪ E (refined by
box_minlam.true_min). Compare with M_Bu: Bu is lambda = 1. HEURISTIC (grid + Newton minimum, not certified).
Usage: python src/e65_driver.py q [q ...] [--iters N] [--restarts r] [--lams l1,l2,...]
"""
from __future__ import annotations
import argparse, json, math, os, subprocess, sys
sys.path.insert(0, "src")
from singer import singer
from box_minlam import true_min

BIN = "src/.build/e65_bustep_sa"


def bu_parts(S):
    D = sorted({b - a for a in S for b in S if b > a})
    E = sorted({abs(3 * (a + b) + 1) for i, a in enumerate(S) for b in S[i + 1:]})
    return D, E


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("qs", type=int, nargs="+")
    ap.add_argument("--iters", type=int, default=20_000_000); ap.add_argument("--restarts", type=int, default=2)
    ap.add_argument("--lams", default="1.0,1.25,1.5,1.75,2.0"); ap.add_argument("--out", default="examples/e65/e65.jsonl")
    a = ap.parse_args()
    os.makedirs("src/.build", exist_ok=True); os.makedirs(os.path.dirname(a.out), exist_ok=True)
    subprocess.run(["cc", "-O3", "-march=native", "-o", BIN, "src/e65_bustep_sa.c", "-lm"], check=True)
    for q in a.qs:
        S0, v = singer(q)
        best = None
        mid = -(max(S0) // 2)
        for c in range(mid - 40, mid + 41):
            S = [s + c for s in S0]
            D, E = bu_parts(S)
            A = sorted(set(3 * d for d in D) | set(E))
            (fm, _), _, _ = true_min(A)
            if best is None or -fm < best[0]:
                best = (-fm, c, S, D, E)
        MBu, c, S, D, EBu = best
        MD = -true_min(D)[0][0]
        XE = int(1.25 * max(max(EBu), 3 * max(D)))
        print(json.dumps(dict(event="setup", q=q, k=len(S), shift=c, nD=len(D), M_Bu=MBu,
                              R_Bu=MBu / math.sqrt(2 * len(D)), M_D=MD, XE=XE)), flush=True)
        for lam in [float(x) for x in a.lams.split(",")]:
            m = round(lam * len(D))
            fn = f"examples/e65/in_q{q}.txt"
            with open(fn, "w") as fh:
                fh.write(f"{len(D)} {' '.join(map(str, D))}\n{len(EBu)} {' '.join(map(str, EBu))}\n{XE}\n")
            r = subprocess.run([BIN, fn, str(m), str(a.iters), str(a.restarts), str(1000 * q + int(100 * lam))],
                               capture_output=True, text=True, check=True)
            d = json.loads(r.stdout)
            A = sorted(set(3 * x for x in D) | set(d["E"]))
            (fm, xm), _, _ = true_min(A)
            rec = dict(event="result", q=q, k=len(S), nD=len(D), lam=lam, nE=len(d["E"]), M_D=MD, M_Bu=MBu,
                       R_Bu=MBu / math.sqrt(2 * len(D)), grid_M=d["grid_M"], M=-fm, R=-fm / math.sqrt(len(A)),
                       ratio_M_over_MBu=-fm / MBu, xmin=xm, iters=a.iters, restarts=a.restarts, E=d["E"])
            print(json.dumps({k: v for k, v in rec.items() if k != "E"}), flush=True)
            with open(a.out, "a") as fh:
                fh.write(json.dumps(rec) + "\n")


if __name__ == "__main__":
    main()
