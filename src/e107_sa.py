"""E107c: simulated annealing over LARGER automata, minimising the b-adic sector violation D (src/e107_sector.py).
D > 0 forces linear M (M_L >= (D - o(1)) n_L); D = 0 is NECESSARY for bounded R. Question: can D -> 0 at all?
Coarse s-grid during the search (SMAX = 60, ds = 0.04, depth K); finalists are re-scored with the fine grid.
Usage: python src/e107_sa.py b S K iters seed   -> JSON lines (improvements + final, fine-grid rescored)
"""
import sys, json, math, os, random
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
import e107_sector as E
from e107_automatic import reach

def score(delta, b, K, fine=False):
    if len(reach(delta)) != len(delta): return None
    if fine: E.SMAX, E.DS = 200.0, 0.02
    else: E.SMAX, E.DS = 60.0, 0.04
    try: r = E.analyse((delta, b, K))
    except Exception: return None
    return r

def main():
    b, S, K, iters, seed = map(int, sys.argv[1:6])
    rng = random.Random(seed)
    def rand_delta():
        d = [[rng.choice([-1] + list(range(S))) for _ in range(b)] for _ in range(S)]
        d[0][0] = 0
        return d
    cur, cs = None, None
    while cs is None:
        cur = rand_delta(); r = score(cur, b, K); cs = r and r["D"]
    best, bs = [row[:] for row in cur], cs
    T0 = 0.05
    for it in range(iters):
        T = T0 * (1 - it / iters) + 1e-4
        nd = [row[:] for row in cur]
        for _ in range(rng.choice([1, 1, 1, 2, 3])):
            s, d = rng.randrange(S), rng.randrange(b)
            if s == 0 and d == 0: continue
            nd[s][d] = rng.choice([-1] + list(range(S)))
        r = score(nd, b, K)
        if r is None: continue
        ns = r["D"]
        if ns <= cs or rng.random() < math.exp(-(ns - cs) / T):
            cur, cs = nd, ns
            if cs < bs - 1e-9:
                best, bs = [row[:] for row in cur], cs
                print(json.dumps(dict(it=it, D=bs, lam=r["lam"], kD=r["kD"], h0=r["h0"], delta=best)), flush=True)
    rf = score(best, b, K, fine=True)
    print(json.dumps(dict(final=True, b=b, S=S, K=K, seed=seed, D_fine=rf and rf["D"], kD=rf and rf["kD"],
                          h0=rf and rf["h0"], lam=rf and rf["lam"], delta=best)), flush=True)

if __name__ == "__main__":
    main()
