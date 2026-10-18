# Order-4 construction (Galois ring / Teichmueller relative difference set).
#   Gamma = Z_4 x Z_4^a (a odd), t = (1, 0).  H = Z_4^a = additive group of GR(4,a) in the basis 1, xi, ..., xi^{a-1}.
#   p_n = Tr(xi^n) in Z_4;  W = {0} u {(p_e, ..., p_{e+a-1}) : 0 <= e < 2^a - 1}  (Teichmueller set seen through the
#   trace pairing);  S(y) = sum_{w in W} i^{w.y}.
#   Fibre over y not in 2H:  the 2-run {k, k+1} subset Z_4 with (1+i) i^k = conj(S(y)) / 2^{(a-1)/2}.
#   Fibre over y = 2u in 2H \ {0}: Z_4 if u_0 = 0 (a hyperplane of F_2^a), else empty.  Fibre over 0: empty.
# Claim: A = -A, 0 notin A, K = max(4, 2^{(a+1)/2}), |B_t| = 4^a - 2^a.
# Usage: python order4.py a
import sys, itertools
import numpy as np

a = int(sys.argv[1]); n2 = 2 ** a
def polymulmod(u, v, h, mod=4):            # polynomials as int arrays low->high, h monic of degree a
    r = np.convolve(u, v) % mod
    for k in range(len(r) - 1, a - 1, -1):
        c = r[k]
        if c: r[k - a:k + 1] = (r[k - a:k + 1] - c * h) % mod
    out = np.zeros(a, int); out[:min(a, len(r))] = r[:a]
    return out
# primitive binary polynomial f of degree a
def is_primitive2(cf):
    f = np.array(list(cf) + [1]); x = np.zeros(a, int); x[1 % a] = 1 if a > 1 else 0
    cur = np.zeros(a, int); cur[0] = 1
    for k in range(1, n2):
        cur = polymulmod(cur, np.array([0, 1]), f, 2)
        if cur[0] == 1 and not cur[1:].any(): return k == n2 - 1
    return False
for cf in itertools.product(range(2), repeat=a):
    if cf[0] and is_primitive2(cf): break
f = np.array(list(cf) + [1])
# Hensel (Graeffe) lift: h(x^2) = (-1)^a (e(x)^2 - o(x)^2) mod 4
e = f.copy(); e[1::2] = 0; o = f.copy(); o[0::2] = 0
g = (np.convolve(e, e) - np.convolve(o, o)) * (-1) ** a % 4
assert not g[1::2].any()
h = g[0::2] % 4; assert h[-1] == 1 and len(h) == a + 1
# xi = x mod h has order 2^a - 1
pw = [np.eye(1, a, 0, dtype=int)[0]]
X = np.zeros(2, int); X[1] = 1
for k in range(1, 2 * n2 + a):
    pw.append(polymulmod(pw[-1], X, h))
assert (pw[n2 - 1] == pw[0]).all() and not any((pw[k] == pw[0]).all() for k in range(1, n2 - 1))
# trace of xi^n = sum_k xi^{n 2^k}  (must be a constant polynomial)
def tr_pow(nn):
    s = np.zeros(a, int)
    for k in range(a): s = (s + pw[(nn * 2 ** k) % (n2 - 1)]) % 4
    assert not s[1:].any(), "trace not in Z_4"
    return int(s[0])
p = [tr_pow(nn) for nn in range(n2 - 1)]
W = [tuple([0] * a)] + [tuple(p[(ee + j) % (n2 - 1)] for j in range(a)) for ee in range(n2 - 1)]
assert len(set(W)) == n2
# S(y) via FFT over Z_4^a: S(y) = sum_w i^{w.y}
IW = np.zeros((4,) * a)
for w in W: IW[w] = 1
S = np.fft.ifftn(IW) * 4 ** a            # ifft uses e^{+2 pi i k.y/4} = i^{k.y}
ys = np.array(list(itertools.product(range(4), repeat=a)))
even = np.all(ys % 2 == 0, axis=1).reshape((4,) * a)
absS2 = np.abs(S) ** 2
assert np.allclose(absS2[~even], n2) and np.allclose(absS2[even & (np.arange(4 ** a).reshape((4,) * a) != 0)], 0)
# fibres
I = np.zeros((4,) + (4,) * a, bool)
units = [(1 + 1j) * 1j ** k for k in range(4)]
for idx in itertools.product(range(4), repeat=a):
    if even[idx]:
        if any(idx) and (idx[0] // 2) == 0: I[(slice(None),) + idx] = True   # full fibre, u_0 = 0
        continue
    val = np.conj(S[idx]) / 2 ** ((a - 1) / 2)
    ks = [k for k in range(4) if abs(val - units[k]) < 1e-8]
    assert len(ks) == 1, f"phase condition fails at {idx}: {val}"
    k = ks[0]; I[(k,) + idx] = True; I[((k + 1) % 4,) + idx] = True
n = a + 1
neg = I
for ax in range(n): neg = np.take(neg, [(-i) % 4 for i in range(4)], axis=ax)
assert (neg == I).all() and not I[(0,) * n]
F = np.fft.fftn(I.astype(float))
assert np.abs(F.imag).max() < 1e-6
F = F.real; F[(0,) * n] = np.inf; K = -F.min()
B = int((I & np.roll(I, 1, 0) & ~np.roll(I, -1, 0)).sum())
print(f"a={a}: |Gamma|={4 ** n} |A|={int(I.sum())} K={K:.9f} (pred {max(4, 2 ** ((a + 1) / 2)):.3f}) "
      f"|B_t|={B} (pred {4 ** a - 2 ** a})  |B_t|/K^3={B / K ** 3:.4f}  |B_t|/K^4={B / K ** 4:.4f}")
vals, cnt = np.unique(np.round(F[np.isfinite(F)], 6), return_counts=True)
print("  spectrum:", dict(zip(vals.tolist(), cnt.tolist())))
if len(sys.argv) > 2:
    np.save(sys.argv[2], I); np.save(sys.argv[2].replace(".npy", "_W.npy"), np.array(W))
