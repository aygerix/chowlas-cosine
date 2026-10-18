# Independent adversarial check of P21 (F_p^4, t = e1).
# Two evaluators: (a) numpy FFT on the indicator; (b) exact level-count distribution n_r = #{a in A : <xi,a> = r}
# for every character xi, F = sum_r n_r cos(2 pi r/p).  Also checks the two partial sums of the proof separately.
import sys, itertools, math
import numpy as np

def nonres(p):
    sq = {(x * x) % p for x in range(1, p)}
    return min(d for d in range(1, p) if d not in sq)

def build(p):
    d = nonres(p)
    I = np.zeros((p,) * 4, bool)
    for x1, x2, x3, x4 in itertools.product(range(p), repeat=4):
        if x2 != 0:
            I[x1, x2, x3, x4] = (x1 * x2 + x3 * x3 - d * x4 * x4) % p != 0
        else:
            I[x1, x2, x3, x4] = (x1 - x3 * x4 * x4) % p != 0
    return I, d

def check(p):
    I, d = build(p)
    neg = I[np.ix_(*[[(-i) % p for i in range(p)]] * 4)]
    assert (neg == I).all(), "A != -A"
    assert not I[0, 0, 0, 0], "0 in A"
    # every t-coset (fix x2,x3,x4) has exactly p-1 points
    cs = I.sum(axis=0)
    assert (cs == p - 1).all(), "coset sizes"
    # run-tops: m in A, m - t in A, m + t notin A  (t = e1, axis 0)
    B = int((I & np.roll(I, 1, 0) & ~np.roll(I, -1, 0)).sum())
    # (a) FFT
    Fa = np.fft.fftn(I.astype(float)).real
    Fa[0, 0, 0, 0] = np.inf
    Ka = -Fa.min()
    # (b) exact level counts
    pts = np.array([x for x in itertools.product(range(p), repeat=4) if I[x]], dtype=np.int64)
    cosr = np.cos(2 * np.pi * np.arange(p) / p)
    Kb = -np.inf; imin = None; nint = 0
    for xi in itertools.product(range(p), repeat=4):
        if xi == (0, 0, 0, 0): continue
        lev = (pts @ np.array(xi)) % p
        n = np.bincount(lev, minlength=p)
        assert (n[1:] == n[1:][::-1]).all()          # realness: n_r = n_{-r}
        F = float(n @ cosr)
        if -F > Kb: Kb, imin, nmin = -F, xi, n.copy()
    # exactness of the minimum: if n_r constant for r != 0 then F = n_0 - n_1 is an integer
    exact_min = (nmin[1:] == nmin[1]).all() and (nmin[0] - nmin[1] == -3 * p)
    print(f"p={p} d={d} |A|={len(pts)} |B_t|={B} (p^3={p**3})  K_fft={Ka:.9f}  K_levels={Kb:.9f} (3p={3*p}) "
          f"argmin={imin} exact_integer_min={exact_min}")
    assert B == p ** 3 and abs(Ka - 3 * p) < 1e-7 and abs(Kb - 3 * p) < 1e-7
    # proof decomposition for j != 0: part with x2 != 0 and part with x2 = 0
    w = lambda z: np.exp(2j * np.pi * z / p)
    inv = lambda z: pow(z, p - 2, p)
    bad = 0
    for j in range(1, p):
        for k, c3, c4 in itertools.product(range(p), repeat=3):
            S1 = 0j; S0 = 0j
            for x2, x3, x4 in itertools.product(range(p), repeat=3):
                if x2:
                    tau = (-(x3 * x3 - d * x4 * x4) * inv(x2)) % p
                    S1 += -w(j * tau) * w(k * x2 + c3 * x3 + c4 * x4)
                else:
                    tau = (x3 * x4 * x4) % p
                    S0 += -w(j * tau) * w(c3 * x3 + c4 * x4)
            Nst = (c3 * c3 - c4 * c4 * inv(d)) % p
            pred1 = p * (p * ((k + Nst * inv(4 * j)) % p == 0) - 1)
            g = p * sum(w(c4 * v) for v in range(p) if (j * v * v + c3) % p == 0)
            if abs(S1 - pred1) > 1e-8 or abs(S0 + g) > 1e-8 or abs(g.imag) > 1e-8 or abs(g) > 2 * p + 1e-8:
                bad += 1
    print(f"   decomposition check (j != 0): mismatches = {bad}")

for p in map(int, sys.argv[1:]):
    check(p)
