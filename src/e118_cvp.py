r"""E118 (lead, cont. 31): does pushing the centroid field onto the spikes lower K? (P77 test for deep JL sets.)
For one-rep lifts z(g) = ḡ + n·t(g), ḡ ∈ [0, n)², t(g) ∈ {−1, 0}² (reps in [−n, n)²), odd (z(−g) = −z(g)).
First-order background energy A2 = Σ_{χ∈B}|W(χ)|² = Σ_{k=1,2} f_kᵀ M f_k, M = n²(I − C) on odd functions (C = the
concentration operator onto N = Z_n² ∖ B). Coordinates are independent; each is a binary QP in t_k, minimised by
SA with exact incremental updates. Reports φ, A2, Σ|z|², and K of the resulting lift (true_min, NUMERICAL), against the
centred lift. Usage: python src/e118_cvp.py p a j sweeps seed
"""
import sys, json, math
import numpy as np
sys.path.insert(0, "src")
from e114_cp_group import jl_set
from e116_jl_taper import true_min

p, a, j, sweeps, seed = (int(t) for t in sys.argv[1:6])
rng = np.random.default_rng(seed)
D, n = jl_set(p, a, j)
Dl = sorted(D)
A = np.zeros((n, n))
for (x, y) in Dl: A[x, y] = 1
Dh = np.fft.fft2(A).real
mask = np.ones((n, n), bool); mask[0, 0] = False
r = -Dh[mask].min()
B = np.isclose(Dh, -r) & mask
N = ~B
cN = np.fft.fft2(N.astype(float)).real / n ** 2
half = np.array([g for g in Dl if g < ((-g[0]) % n, (-g[1]) % n)])
def Cmat(X, Y):
    d = (X[:, None, :] - Y[None, :, :]) % n
    return cN[d[..., 0], d[..., 1]]
C = Cmat(half, half) - Cmat(half, (-half) % n)        # concentration operator on odd functions (half basis)
Mq = np.eye(len(half)) - C                              # A2 = n²·2·Σ_k f_kᵀ(I − C)f_k over the half basis (scale irrelevant)
lam = float(np.linalg.eigvalsh(C)[-1])

def solve_coord(gk):
    # minimise q(t) = (g + n t)ᵀ Mq (g + n t), t ∈ {−1, 0}; start from the centred choice
    t = np.where(gk > n / 2, -1.0, 0.0)
    z = gk + n * t
    v = Mq @ z
    q = z @ v
    best = (q, t.copy())
    T0 = 0.05 * abs(q) / len(z); steps = sweeps * len(z)
    for s in range(steps):
        temp = T0 * (1e-3) ** (s / steps)
        i = rng.integers(len(z))
        dz = n * ((-1.0 - t[i]) if t[i] == 0 else (1.0))   # flip t_i between 0 and −1
        dq = 2 * dz * v[i] + dz * dz * Mq[i, i]
        if dq <= 0 or rng.random() < math.exp(-dq / temp):
            t[i] = -1.0 - t[i]; z[i] += dz; v += dz * Mq[:, i]; q += dq
            if q < best[0]: best = (q, t.copy())
    return best

def lift_stats(T1, T2):
    Z = np.stack([half[:, 0] + n * T1, half[:, 1] + n * T2], axis=1)
    z2 = (Z ** 2).sum(1)
    q = sum(f @ Mq @ f for f in (Z[:, 0], Z[:, 1]))
    phi = 1 - q / z2.sum()
    L = int(np.abs(Z).max())
    fmin, _, _, _ = true_min(Z.astype(np.int64), np.ones(len(Z)), L, G=1 << int(math.ceil(math.log2(16 * (2 * L + 1)))), nstart=16)
    return {"phi": float(phi), "sum_z2": float(2 * z2.sum()), "K": float(-fmin), "ratio": 2 * len(Z) / fmin ** 2,
            "spread": float(2 * z2.sum() / math.sqrt(2 * (z2 ** 2).sum()))}

cen1 = np.where(half[:, 0] > n / 2, -1.0, 0.0); cen2 = np.where(half[:, 1] > n / 2, -1.0, 0.0)
out = {"p": p, "a": a, "j": j, "n": n, "D": len(D), "r": float(r), "lambda_odd": lam, "centred": lift_stats(cen1, cen2)}
b1 = solve_coord(half[:, 0].astype(float)); b2 = solve_coord(half[:, 1].astype(float))
out["cvp"] = lift_stats(b1[1], b2[1])
out["P77_bound_cvp"] = r + (1 - out["cvp"]["phi"]) / 8 * out["cvp"]["spread"]
print(json.dumps(out), flush=True)
