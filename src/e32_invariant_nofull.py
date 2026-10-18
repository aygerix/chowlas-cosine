r"""E32: Conjecture G_noFull probe — exhaustive search over all Stab(t)-invariant symmetric sets in F_p^n.

Setting (NOTEBOOK 2026-10-18 late, PROOFS P20).  Γ = F_p^n (p odd), Q(x) = Σ d_i x_i², polar form B(x,y) = Q(x+y)−Q(x)−Q(y),
t ∈ F_p^n \ {0}.  By Witt's extension theorem the orbits of Stab_{O(Q)}(t) on F_p^n \ span(t) are the classes
C(q,b) = {x ∉ span(t) : Q(x) = q, B(x,t) = b}; each point kt of span(t) is fixed.  So every invariant set is
A = ∪_{(q,b)∈S} C(q,b) ∪ {kt : k ∈ T}.  We require A = −A (−C(q,b) = C(q,−b)), 0 ∉ A.
t-lines act on classes by φ(q,b) = (q + b + Q(t), b + 2Q(t)) (a permutation of F_p²), so
    |B_t| = Σ_{β∈S} |C_β|·[φ^{-1}β ∈ S]·[φβ ∉ S]  +  (run-tops of A ∩ span(t)),
and A contains a full t-coset iff some φ-cycle lies inside S (span(t) is never full: 0 ∉ A).
F(c) = Σ_{x∈A} e_p(c·x) is computed exactly over ALL p^n characters by FFT of each class indicator (values are
real algebraic integers of Q(ζ_p)^+), then columns are de-duplicated (rounded to 1e-7).
Output: for every set, K = −min_{c≠0} F(c), |B_t|, nofull flag; the frontier max|B_t| at each K, separately for all
sets and for no-full sets.  NUMERICAL (float FFT; exact integers for p = 3), exhaustive over the
invariant class (which contains P20 Theorem 1 for a = 1: A = {Q ≠ 0}, t isotropic).
Usage: python src/e32_invariant_nofull.py p n d1,...,dn t1,...,tn
"""
import sys, itertools, json
import numpy as np

p, n = int(sys.argv[1]), int(sys.argv[2])
d = np.array([int(v) for v in sys.argv[3].split(',')]); t = np.array([int(v) for v in sys.argv[4].split(',')])
assert len(d) == n and len(t) == n and (d % p != 0).all() and (t % p).any()
X = np.indices((p,) * n).reshape(n, -1).T                      # all points, C-order (matches fftn layout)
Qx = (X ** 2 * d).sum(1) % p
Bx = (2 * X * d * t).sum(1) % p                                # B(x,t) = 2 Σ d_i x_i t_i
Qt = int((t * t * d).sum() % p)
idx = lambda v: int(np.ravel_multi_index(tuple(v % p), (p,) * n))
span_idx = {k: idx(k * t) for k in range(p)}
in_span = np.zeros(len(X), bool); in_span[list(span_idx.values())] = True

phi = lambda q, b: ((q + b + Qt) % p, (b + 2 * Qt) % p)
classes = [(q, b) for q in range(p) for b in range(p)]
size = {cb: int(((Qx == cb[0]) & (Bx == cb[1]) & ~in_span).sum()) for cb in classes}
classes = [cb for cb in classes if size[cb] > 0]
# symmetric units: b = 0 classes alone, {(q,b),(q,-b)} pairs, span pairs {kt, -kt}
units = []
for cb in classes:
    q, b = cb
    if b == 0: units.append(('C', [cb]))
    elif b < (p - b) % p or (p - b) % p not in [c[1] for c in classes if c[0] == q]:
        units.append(('C', sorted({cb, (q, (-b) % p)} & set(classes))))
for k in range(1, (p + 1) // 2): units.append(('T', [k, p - k]))
nu = len(units); assert nu <= 22, f"{nu} units: too many for plain enumeration"

# character sums of each unit, de-duplicated over characters
W = []
for kind, mem in units:
    ind = np.zeros(len(X), bool)
    if kind == 'C':
        for (q, b) in mem: ind |= (Qx == q) & (Bx == b) & ~in_span
    else:
        for k in mem: ind[span_idx[k]] = True
    F = np.fft.fftn(ind.reshape((p,) * n).astype(float)).ravel()
    assert np.abs(F.imag).max() < 1e-6
    W.append(F.real)
W = np.array(W)                                                # (units, p^n); column 0 = trivial character
Wn = np.round(W[:, 1:], 7)                                     # real algebraic integers of Q(ζ_p)^+ (integers iff p = 3)
cols = np.unique(Wn, axis=1)                                   # (units, distinct nontrivial characters)

# class-level run-top data
unit_of_class = {}
for u, (kind, mem) in enumerate(units):
    if kind == 'C':
        for cb in mem: unit_of_class[cb] = u
phiinv = {phi(*cb): cb for cb in [(q, b) for q in range(p) for b in range(p)]}
cycles, seen = [], set()
for cb in classes:
    if cb in seen: continue
    cyc, cur = [], cb
    while cur not in cyc: cyc.append(cur); cur = phi(*cur)
    seen |= set(cyc); cycles.append([unit_of_class[c] for c in cyc])

bits = ((np.arange(2 ** nu)[:, None] >> np.arange(nu)) & 1).astype(np.int64)   # (sets, units)
Fmin = (bits.astype(float) @ cols).min(1)                                    # min over nontrivial characters
K = -Fmin
B = np.zeros(2 ** nu, np.int64)
for cb in classes:
    u, um, up = unit_of_class[cb], unit_of_class[phiinv[cb]], unit_of_class[phi(*cb)]
    B += size[cb] * bits[:, u] * bits[:, um] * (1 - bits[:, up])
span_units = {k: u for u, (kind, mem) in enumerate(units) if kind == 'T' for k in mem}
sb = lambda k: bits[:, span_units[k % p]] if k % p != 0 else np.zeros(2 ** nu, np.int64)
for k in range(1, p): B += sb(k) * sb(k - 1) * (1 - sb(k + 1))
full = np.zeros(2 ** nu, bool)
for cyc in cycles: full |= bits[:, cyc].all(1)
nofull = ~full
sizeA = bits @ np.array([sum(size[cb] for cb in mem) if kind == 'C' else len(mem) for kind, mem in units])

def frontier(mask):
    out = {}
    for k_, b_, a_ in zip(K[mask], B[mask], sizeA[mask]):
        kk = round(float(k_), 3)
        if kk >= 1 and b_ > out.get(kk, (-1,))[0]: out[kk] = (int(b_), int(a_))
    return dict(sorted(out.items()))
fa, fn = frontier(np.ones(2 ** nu, bool)), frontier(nofull & (sizeA > 0))
tag = f"p={p} n={n} d={sys.argv[3]} t={sys.argv[4]} Q(t)={Qt} units={nu} classes={len(classes)} cycles={len(cycles)}"
best = lambda f: max(((b / k ** 2, k, b) for k, (b, a) in f.items()), default=(0, 0, 0))
print(tag, flush=True)
print("  ALL     frontier K:(|B_t|,|A|) ", {k: v for k, v in fa.items() if k <= 3 * p * p}, flush=True)
print("  NOFULL  frontier K:(|B_t|,|A|) ", {k: v for k, v in fn.items() if k <= 3 * p * p}, flush=True)
print(f"  best |B_t|/K^2: all {best(fa)[0]:.3f} (K={best(fa)[1]}, B={best(fa)[2]});  "
      f"nofull {best(fn)[0]:.3f} (K={best(fn)[1]}, B={best(fn)[2]})", flush=True)
json.dump(dict(p=p, n=n, d=sys.argv[3], t=sys.argv[4], Qt=Qt, units=[[k, [list(map(int, m)) if k == 'C' else m for m in mem]
          if False else str(mem)] for k, mem in units], frontier_all=fa, frontier_nofull=fn),
          open(f"examples/group_runtop/e32_p{p}_n{n}_d{sys.argv[3].replace(',', '')}_t{sys.argv[4].replace(',', '')}.json", 'w'))
