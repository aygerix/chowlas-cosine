"""EXP-3: Bedert/Shankar boundary sets.

For finite A ⊂ N let A' = A ∪ (-A) (symmetric), K = -min F_{A'} = 2 M(A).
B_t = {a in A' : a - t in A', a + t not in A'} (t != 0).
Bedert v3 Prop 7.3: |B_t| <= C0 K^4.  Shankar: sum_{t in A'} |B_t| = 6Q - 4I >= T/3, T >= n^2/(2K) (n=|A'|).
Question tested here: is max_t |B_t| <= C K^2 on all available families?  (Would give K >> n^{1/3}.)
"""
import numpy as np


def boundary_sizes(A, ts=None):
    A = sorted(set(A))
    Ap = set(A) | {-a for a in A}
    if ts is None:
        ts = sorted({abs(a - b) for a in A for b in Ap if a != b})
    out = {}
    arr = np.array(sorted(Ap))
    S = set(Ap)
    for t in ts:
        c = 0
        for a in arr:
            if (a - t) in S and (a + t) not in S:
                c += 1
        out[t] = c
    return out
