r"""E33: all-(p−1)-point fibres in F_p^4 — a counterexample candidate to Conjecture G_noFull (lead, 2026-10-18).

A = {x : x2 ≠ 0, x1 ≠ −N(x3,x4)/x2} ∪ {x : x2 = 0, x1 ≠ τ2(x3,x4)},  N(x3,x4) = x3² − d x4² (anisotropic), t = e1,
τ2 : F_p² → F_p odd (τ2(−v) = −τ2(v), so A = −A and 0 ∉ A).  Every ⟨t⟩-coset meets A in exactly p − 1 points (one
cyclic run, one top): no full cosets, no singletons (p >= 5), |B_t| = p³.  Predicted: F(0,·) = 0 off the trivial
character; F(j,k,c) = (E31 bulk value ∈ {−p, p(p−1)}) − ĝ_j(c), ĝ_j(c) = Σ_{v∈F_p²} e_p(jτ2(v) + c·v); so
K <= p + max_{j≠0,c} ĝ_j(c).  τ2 = homogeneous cubic a x3³ + b x3²x4 + c x3x4² + e x4³ (p >= 5; Deligne: |ĝ| <= 4p for
a nonsingular form) or exhaustive odd τ2 (p = 3).  Spectrum over all p^4 characters by FFT (float, error ~1e-9; NUMERICAL).
Usage: python src/e33_alld_nofull.py p [trials]
"""
import sys, itertools
import numpy as np
p = int(sys.argv[1]); trials = int(sys.argv[2]) if len(sys.argv) > 2 else 200
rng = np.random.default_rng(1)
d = next(v for v in range(2, p) if pow(v, (p - 1) // 2, p) == p - 1)
X = np.indices((p,) * 4).reshape(4, -1).T
x1, x2, x3, x4 = X.T
Nf = (x3 * x3 - d * x4 * x4) % p
inv = np.array([0] + [pow(v, p - 2, p) for v in range(1, p)])
bulk = (x2 != 0) & (x1 != (-Nf * inv[x2]) % p)

def build(tau2):                                   # tau2: array over (x3,x4) of shape (p,p)
    ind = bulk | ((x2 == 0) & (x1 != tau2[x3, x4]))
    return ind.reshape((p,) * 4)

def evaluate(ind):
    J = ind
    for ax in range(4): J = np.take(J, [(-i) % p for i in range(p)], axis=ax)
    assert (J == ind).all() and not ind[0, 0, 0, 0]
    F = np.fft.fftn(ind.astype(float)); assert np.abs(F.imag).max() < 1e-6
    v = F.real.copy(); v[0, 0, 0, 0] = 0            # real algebraic integers of Q(ζ_p)^+ (integers only for p = 3)
    K = -v.min()
    B = int((ind & np.roll(ind, 1, 0) & ~np.roll(ind, -1, 0)).sum())
    lines = ind.sum(0)                             # points per t-line
    return K, B, int(lines.max()), int(lines.min()), sorted(set(np.round(v, 6).ravel().tolist()))

def ghat_max(tau2):
    g = np.exp(2j * np.pi * tau2 / p)
    best = -1e9
    for j in range(1, p):
        G = np.fft.fft2(np.exp(2j * np.pi * j * tau2 / p)).real
        best = max(best, G.max())
    return best

cands = []
if p == 3:
    reps = [(a, b) for a in range(3) for b in range(3) if (a, b) != (0, 0) and (a, b) < ((-a) % 3, (-b) % 3)]
    for vals in itertools.product(range(3), repeat=len(reps)):
        t2 = np.zeros((3, 3), int)
        for (a, b), s in zip(reps, vals): t2[a, b] = s; t2[(-a) % 3, (-b) % 3] = (-s) % 3
        cands.append(t2)
else:
    a3, a4 = np.indices((p, p))
    for _ in range(trials):
        cf = rng.integers(0, p, 4)
        cands.append((cf[0] * a3 ** 3 + cf[1] * a3 ** 2 * a4 + cf[2] * a3 * a4 ** 2 + cf[3] * a4 ** 3) % p)
if len(sys.argv) > 3 and sys.argv[3] == 'x3x4sq':      # the elementary choice of P21: tau2 = x3*x4^2, max ghat = 2p
    a3, a4 = np.indices((p, p)); t2 = (a3 * a4 * a4) % p
else:
    t2 = sorted(cands, key=ghat_max)[0]
K, B, lmax, lmin, spec = evaluate(build(t2))
print(f"p={p}: best max ĝ = {ghat_max(t2):.3f}; K = {K:.4f}, |B_t| = {B} (p³ = {p ** 3}), points per t-line in "
      f"[{lmin},{lmax}] (p−1 = {p - 1}), |B_t|/K² = {B / K ** 2:.3f}, |B_t|/K³ = {B / K ** 3:.3f}, "
      f"#distinct F values = {len(spec)}, min..max = {spec[0]}..{spec[-1]}", flush=True)
