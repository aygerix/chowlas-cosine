# Independent evaluator for the order-4 sets: exact level counts (no FFT) and direct RDS difference count.
#   usage: python order4_check.py A.npy   (A_W.npy must sit next to it)
import sys, itertools
import numpy as np
I = np.load(sys.argv[1]); W = np.load(sys.argv[1].replace(".npy", "_W.npy"))
n = I.ndim; a = n - 1
# (1) RDS property of W in Z_4^a: every element outside 2Z_4^a is exactly one difference, none inside except 0
cnt = {}
for x in W:
    for y in W:
        d = tuple((x - y) % 4); cnt[d] = cnt.get(d, 0) + 1
outside = [d for d in itertools.product(range(4), repeat=a) if any(v % 2 for v in d)]
inside = [d for d in itertools.product(range(4), repeat=a) if not any(v % 2 for v in d) and any(d)]
assert all(cnt.get(d, 0) == 1 for d in outside) and all(cnt.get(d, 0) == 0 for d in inside) and cnt[(0,) * a] == len(W)
# (2) set axioms
pts = np.argwhere(I)
S = set(map(tuple, pts))
assert all(tuple((-p) % 4) in S for p in pts) and (0,) * n not in S
# (3) exact F at every character via level counts: F = n0 - n2, and n1 = n3 (realness)
K = -10 ** 9; Kint = None
chars = np.array(list(itertools.product(range(4), repeat=n)))
for c0 in range(0, len(chars), 512):
    C = chars[c0:c0 + 512]
    lev = (C @ pts.T) % 4                        # (#chars, |A|)
    n0 = (lev == 0).sum(1); n1 = (lev == 1).sum(1); n2 = (lev == 2).sum(1); n3 = (lev == 3).sum(1)
    assert (n1 == n3).all()
    Fv = n0 - n2
    nz = np.any(C != 0, axis=1)
    if nz.any(): K = max(K, int(-Fv[nz].min()))
# (4) run-tops along t = e_0, counted directly
B = sum(1 for p in pts if tuple(((p[0] - 1) % 4,) + tuple(p[1:])) in S and tuple(((p[0] + 1) % 4,) + tuple(p[1:])) not in S)
print(f"a={a}: RDS ok, A=-A ok, 0 notin A ok; exact integer K={K}; |B_t|={B}; |B_t|/K^3={B / K ** 3:.4f}; K^4/4-K^2/2={K**4/4-K**2/2}")
