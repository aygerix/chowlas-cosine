# Proposition P3 (ord t = 3): explicit set in Gamma = F_3 x F_9 x F_9, t = (1,0,0), F_9 = F_3[i], i^2 = -1.
#   A = {(s,a,b) : [b square != 0 and s = Tr(a^2/b)] or [b non-square and s != Tr(a^2/b)] or [b = 0, a != 0]}
# Claim: A = -A, 0 notin A, K = 3, |B_t| = 36, spectrum {-3: 220, 24: 22}.  Two evaluators: FFT and exact level counts.
import itertools
import numpy as np
F9 = [(u, v) for u in range(3) for v in range(3)]
mul = lambda x, y: ((x[0] * y[0] - x[1] * y[1]) % 3, (x[0] * y[1] + x[1] * y[0]) % 3)
inv = lambda x: next(y for y in F9 if mul(x, y) == (1, 0))
tr = lambda z: (2 * z[0]) % 3                      # z + z^3 = (u+vi) + (u-vi)
sq = {mul(x, x) for x in F9 if x != (0, 0)}
I = np.zeros((3,) * 5, bool)
for s, a, b in itertools.product(range(3), F9, F9):
    if b == (0, 0):
        val = a != (0, 0)
    else:
        tau = tr(mul(mul(a, a), inv(b)))
        val = (s == tau) if b in sq else (s != tau)
    I[(s,) + a + b] = val
neg = I
for ax in range(5): neg = np.take(neg, [0, 2, 1], axis=ax)
assert (neg == I).all() and not I[0, 0, 0, 0, 0]
F = np.fft.fftn(I.astype(float)).real; F[0, 0, 0, 0, 0] = np.inf
B = int((I & np.roll(I, 1, 0) & ~np.roll(I, -1, 0)).sum())
pts = np.argwhere(I); Kx = 0
for xi in itertools.product(range(3), repeat=5):
    if any(xi):
        lev = (pts @ np.array(xi)) % 3; n = np.bincount(lev, minlength=3); assert n[1] == n[2]
        Kx = max(Kx, -(int(n[0]) - int(n[1])))
vals, cnt = np.unique(np.round(F[np.isfinite(F)], 6), return_counts=True)
print(f"|A|={len(pts)} |B_t|={B} K_fft={-F.min():.9f} K_exact={Kx} spectrum={dict(zip(vals.tolist(), cnt.tolist()))}")
