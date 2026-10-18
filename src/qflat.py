"""Q-flat(m) probe: finite B ⊂ Z; mu(g) = |B ∩ (B+g)|.  F_m(B) = fraction of ordered pairs (b != b') whose difference
has multiplicity exactly m.  Barrier analysis (NOTEBOOK) needs F_m -> 1 with m >= 3 for any R < 1/2 mechanism with
nearly aligned FR weights.  Local search (simulated annealing) over B ⊂ [0, L], |B| = n."""
import sys, math, numpy as np

def Fm(B, m):
    B = np.asarray(sorted(B)); n = len(B)
    d = (B[:, None] - B[None, :]).ravel()
    d = d[d != 0]
    vals, cnt = np.unique(d, return_counts=True)
    good = cnt[cnt == m].sum()
    return good / (n * (n - 1))

def anneal(n, L, m, iters=60000, seed=0, sym=False):
    rng = np.random.default_rng(seed)
    if sym:   # symmetric sets B = -B (n even): choose n/2 positive elements
        half = list(rng.choice(np.arange(1, L + 1), n // 2, replace=False))
        mk = lambda h: sorted(set(h) | {-x for x in h})
        cur_set = half
    else:
        cur_set = list(rng.choice(np.arange(0, L + 1), n, replace=False))
        mk = lambda h: sorted(h)
    cur = Fm(mk(cur_set), m); best = cur; bestB = mk(cur_set)
    for it in range(iters):
        T = 0.05 * (0.002 / 0.05) ** (it / iters)
        i = rng.integers(len(cur_set)); old = cur_set[i]
        new = int(rng.integers(1 if sym else 0, L + 1))
        if new in cur_set: continue
        cur_set[i] = new
        val = Fm(mk(cur_set), m)
        if val >= cur or rng.random() < math.exp((val - cur) / T):
            cur = val
            if cur > best: best = cur; bestB = mk(cur_set)
        else:
            cur_set[i] = old
    return best, bestB

if __name__ == "__main__":
    n, L, m = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); sym = len(sys.argv) > 4 and sys.argv[4] == 'sym'
    best = None
    for s in range(3):
        b, B = anneal(n, L, m, seed=s, sym=sym)
        if best is None or b > best[0]: best = (b, B)
    print(f"n={n} L={L} m={m} sym={sym} best F_m={best[0]:.3f} B={best[1]}")
