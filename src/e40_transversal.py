r"""E40: test the branch-2 dichotomy on transversal 2-run sets A = S ∪ (S+t), S = {y + t k_y : y ∈ Z_t}.
For each level function k: compute M(A) (dense FFT grid on [0, π] + local refinement; uncertified), the level range L,
the fraction of pairs (y1,y2) with small defect d = k1 + k2 − k3 + carry ∈ {−1, 0, 1}, and compare M with √t and t/L.
Families: constant, linear ⌊βy⌋, quadratic ⌊c y²/t⌋ mod L, random uniform in [0,L), random with triangular (tapered)
level distribution, and Z_4-valued 'O4-like' levels k_y = Tr-type quadratic digit form (y in base 4)."""
import sys, numpy as np
rng = np.random.default_rng(12345)
def Mval(A):
    A = np.asarray(sorted(A)); X = int(A.max()); G = 1 << int(np.ceil(np.log2(16 * X + 64)))
    c = np.zeros(G); c[A] = 1.0
    f = np.fft.rfft(c).real  # f(2π j/G) = Σ cos(2π a j / G)
    j = int(np.argmin(f)); x0 = 2 * np.pi * j / G; h = 2 * np.pi / G
    a, b = x0 - h, x0 + h
    g = lambda x: np.cos(np.outer(np.atleast_1d(x), A)).sum(1)
    for _ in range(60):
        m1, m2 = a + 0.382 * (b - a), a + 0.618 * (b - a)
        if g(m1)[0] < g(m2)[0]: b = m2
        else: a = m1
    return -g((a + b) / 2)[0]
def stats(t, k):
    k = np.asarray(k, dtype=np.int64); y = np.arange(t)
    S = y + t * k; A = np.concatenate([S, S + t]); assert len(set(A.tolist())) == 2 * t and A.min() >= 0
    A = A - A.min() + 1
    M = Mval(A); L = int(k.max() - k.min() + 1)
    Y1, Y2 = np.meshgrid(y, y, indexing="ij"); Y3 = (Y1 + Y2) % t; carry = (Y1 + Y2 >= t).astype(np.int64)
    d = k[Y1] + k[Y2] - k[Y3] + carry
    small = float(np.mean(np.abs(d) <= 1))
    return M, L, small
def digit_quad(t):  # t = 4^a: k_y = (Σ_i y_i y_{i+1} + y_0^2) mod 4 over base-4 digits — a Z_4-valued quadratic form
    a = int(round(np.log(t) / np.log(4))); out = []
    for y in range(t):
        dg = [(y >> (2 * i)) & 3 for i in range(a)]
        out.append((sum(dg[i] * dg[(i + 1) % a] for i in range(a)) + dg[0] ** 2) % 4)
    return out
print(f"{'family':28s} {'t':>5s} {'L':>5s} {'M':>8s} {'R':>7s} {'M/sqrt t':>9s} {'M*L/t':>7s} {'small-def':>9s}")
for t in (64, 256, 1024):
    fams = {"constant": [0] * t,
            "linear b=0.5/sqrt(t)": [int(0.5 * y / np.sqrt(t)) for y in range(t)],
            "linear b=2/sqrt(t)": [int(2 * y / np.sqrt(t)) for y in range(t)],
            "quadratic y^2/t": [int(y * y / t) for y in range(t)],
            "quadratic y^2 mod sqrt t": [(y * y) % max(2, int(np.sqrt(t))) for y in range(t)]}
    for L in (4, int(np.sqrt(t)), 4 * int(np.sqrt(t))):
        fams[f"random unif L={L}"] = list(rng.integers(0, L, t))
        tri = np.minimum(rng.integers(0, L, t), rng.integers(0, L, t))  # decreasing density (taper on one side)
        fams[f"random taper L={L}"] = list(tri)
    if t in (64, 256, 1024): fams["Z4 digit quadratic (O4-like)"] = digit_quad(t)
    for name, k in fams.items():
        M, L, sm = stats(t, k)
        print(f"{name:28s} {t:5d} {L:5d} {M:8.2f} {M/np.sqrt(2*t):7.3f} {M/np.sqrt(t):9.3f} {M*L/t:7.3f} {sm:9.3f}", flush=True)
