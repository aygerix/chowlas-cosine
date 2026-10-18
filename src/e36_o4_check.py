r"""E36: lead's independent check of Theorem O4 (agent g3): order-4 run-tops with |B_t| = K^4/4 - K^2/2.
Independent choices: GR(4,a) = Z_4[x]/(f) with f the NAIVE 0/1 lift of an irreducible f in F_2[x] (any monic lift of an
irreducible is a Galois ring); Teichmueller set T = {z : z^(2^a) = z} found by brute force (no Lemma T used);
characters via the DOT-PRODUCT pairing i^{lambda . y} on Z_4^a (any nondegenerate pairing works in the proof);
spectrum by numpy FFT over Z_4^(1+a) (values must be integers), run-tops counted directly.
Usage: python src/e36_o4_check.py a   (a odd)"""
import sys, itertools
import numpy as np
a = int(sys.argv[1]); F2 = {3: [1, 1, 0, 1], 5: [1, 0, 1, 0, 0, 1], 7: [1, 1, 0, 0, 0, 0, 0, 1], 9: [1, 0, 0, 0, 1, 0, 0, 0, 0, 1]}[a]
f = np.array(F2)                       # f[0] + f[1] x + ... + x^a, irreducible over F_2
def mul(u, v):
    r = np.zeros(2 * a, dtype=np.int64)
    for i in range(a):
        if u[i]: r[i:i + a] += u[i] * v
    for d in range(2 * a - 1, a - 1, -1):    # reduce mod f (monic)
        c = r[d] % 4
        if c: r[d - a:d + 1] -= c * f
    return r[:a] % 4
elems = [np.array(e) for e in itertools.product(range(4), repeat=a)]
def power(z, n):
    out = np.zeros(a, dtype=np.int64); out[0] = 1; b = z.copy()
    while n:
        if n & 1: out = mul(out, b)
        b = mul(b, b); n >>= 1
    return out
T = [z for z in elems if (power(z, 2 ** a) == z).all()]
assert len(T) == 2 ** a, len(T)
Tm = np.array(T)
# relative difference set check: every y with an odd coordinate is exactly one difference, no nonzero even y is one
diffs = {}
for x in T:
    for xp in T:
        d = tuple((x - xp) % 4); diffs[d] = diffs.get(d, 0) + 1
odd = [e for e in elems if (e % 2).any()]
assert all(diffs.get(tuple(e), 0) == 1 for e in odd)
assert all(diffs.get(tuple(e), 0) == 0 for e in elems if not (e % 2).any() and e.any())
# S(y) = sum_{x in T} i^{x.y}; k(y) from conj S(y) = 2^{(a-1)/2} (1+i) i^{k}
c0 = 2 ** ((a - 1) // 2)
k = {}
for y in odd:
    S = np.sum(1j ** ((Tm @ y) % 4))
    w = np.conj(S) / (c0 * (1 + 1j))
    kk = [q for q in range(4) if abs(w - 1j ** q) < 1e-9]
    assert len(kk) == 1, (y, S)
    k[tuple(y)] = kk[0]
# F0 = {2u : ubar in W \ 0}, W = hyperplane {u in F_2^a : u_0 = 0}
F0 = [tuple(2 * np.array(u)) for u in itertools.product(range(2), repeat=a) if any(u) and u[0] == 0]
ind = np.zeros((4,) + (4,) * a, dtype=bool)
for y, kk in k.items():
    ind[(kk,) + y] = True; ind[((kk + 1) % 4,) + y] = True
for y in F0:
    ind[(slice(None),) + y] = True
neg = ind
for ax in range(a + 1): neg = np.take(neg, [(-i) % 4 for i in range(4)], axis=ax)
assert (neg == ind).all() and not ind[(0,) * (a + 1)]
Fv = np.fft.fftn(ind.astype(float))
assert np.abs(Fv.imag).max() < 1e-6 and np.abs(Fv.real - np.round(Fv.real)).max() < 1e-6
v = np.round(Fv.real).astype(np.int64); v[(0,) * (a + 1)] = 10 ** 9
K = -v.min()
B = int((ind & np.roll(ind, 1, 0) & ~np.roll(ind, -1, 0)).sum())
vals, cnt = np.unique(v[v < 10 ** 9], return_counts=True)
print(f"a={a}: |T|={len(T)} RDS ok, |A|={int(ind.sum())}, K={K}, |B_t|={B}, K^4/4-K^2/2={K**4 // 4 - K**2 // 2}, "
      f"|B_t|/K^3={B / K**3:.3f}; spectrum {dict(zip(vals.tolist(), cnt.tolist()))}", flush=True)
