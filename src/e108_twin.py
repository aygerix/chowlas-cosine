"""E108c: LOCAL TWINS of 0 for the stationary Parry measure (T-A2 twin criterion, lead 2026-10-19).

tau_v := the state map s -> delta(s, v) (reject = -1), composed letter by letter. Cylinders [v], [v'] of equal length
with tau_v = tau_{v'} carry translate-equal restrictions of the stationary Parry measure mu (mu([v x]) = lam^{-|vx|}
sum_s pi_s r_{delta(s, v x)}). A twin of 0 is u = m/b^p (1 <= m < b^p, gcd(m, b) = 1) such that, for some N >= 0:
  tau_{w 0^N} = tau_{0^{p+N}},  tau_{w^- (b-1)^N} = tau_{(b-1)^{p+N}}      (w, w^- = p-digit expansions of m, m - 1)
and the same for -u (m' = b^p - m).  Then sigma|B(u, b^{-p-N}) is a translate of sigma|B(0, b^{-p-N}).
THEOREM (paper, lead): a twin forces Re mu^(j) < 0 for some j, so M(A_L) >= c|A_L| (linear M).
Usage: python src/e108_twin.py rows.jsonl pmax out.jsonl
"""
import sys, json, os
from math import gcd
from multiprocessing import Pool

NSTAB = 40

def tau(delta, word):
    S = len(delta); m = list(range(S))
    for d in word:
        m = [(delta[x][d] if x >= 0 else -1) for x in m]
    return tuple(m)

def digits(m, b, p):
    out = []
    for _ in range(p):
        out.append(m % b); m //= b
    return out[::-1]

def is_twin(delta, b, p, m):
    z, top = [0] * NSTAB, [b - 1] * NSTAB
    def ok(mm):
        w, wm = digits(mm, b, p), digits(mm - 1, b, p)
        return tau(delta, w + z) == tau(delta, [0] * p + z) and tau(delta, wm + top) == tau(delta, [b - 1] * p + top)
    return ok(m) and ok(b ** p - m)

def one(args):
    row, pmax = args
    b, delta = row["b"], row["delta"]
    for p in range(1, pmax + 1):
        for m in range(1, b ** p):
            if gcd(m, b) != 1: continue
            if is_twin(delta, b, p, m):
                return dict(b=b, delta=delta, twin=True, p=p, m=m)
    return dict(b=b, delta=delta, twin=False)

def main():
    fn, pmax, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    rows = [json.loads(l) for l in open(fn)]
    with Pool(int(os.environ.get("CHOWLA_WORKERS", "4"))) as P, open(out, "w") as o:
        for r in P.imap_unordered(one, ((r, pmax) for r in rows), chunksize=64):
            o.write(json.dumps(r) + "\n")

if __name__ == "__main__":
    main()
