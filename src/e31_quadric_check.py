# E31 (see .research/EXPERIMENTS.md). Run: src/localrun.sh -m 2 python src/e31_quadric_check.py
# Lead's independent check of the conjG agent's counterexample mechanism: A = {x in F_p^4 : Q(x) != 0},
# Q = x1*x2 + N(x3,x4) with N an anisotropic binary form (elliptic 4-dim quadric), t = e_1 (isotropic).
import numpy as np, itertools
def nonresidue(p):
    return next(d for d in range(2, p) if pow(d, (p - 1) // 2, p) == p - 1)
for p in (3, 5, 7, 11, 13):
    d = nonresidue(p)
    X = np.indices((p, p, p, p)).reshape(4, -1).T
    Q = (X[:, 0] * X[:, 1] + X[:, 2] ** 2 - d * X[:, 3] ** 2) % p     # x3^2 - d x4^2 anisotropic
    ind = (Q != 0).reshape(p, p, p, p)
    assert not ind[0, 0, 0, 0]
    neg = ind[(-np.arange(p)) % p][:, (-np.arange(p)) % p][:, :, (-np.arange(p)) % p][:, :, :, (-np.arange(p)) % p]
    assert (neg == ind).all()
    F = np.fft.fftn(ind.astype(float))                # sum_x 1_A(x) e(-a.x/p); real by symmetry
    assert np.abs(F.imag).max() < 1e-6
    vals = np.round(F.real).astype(int); assert np.abs(F.real - vals).max() < 1e-6
    K = -vals.min()
    plus = np.roll(ind, -1, axis=0)    # plus[m] = ind[m + t]
    minus = np.roll(ind, 1, axis=0)    # minus[m] = ind[m - t]
    B = int((ind & minus & ~plus).sum())
    print(f"p={p}: |A|={int(ind.sum())} K={K} distinct F values={sorted(set(vals.ravel().tolist()))[:6]}... |B_t|={B} "
          f"p^2(p-1)={p*p*(p-1)} |B_t|/K^2={B / K**2:.3f}  |B_t|/K^3={B / K**3:.3f}", flush=True)
