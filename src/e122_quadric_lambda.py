r"""E122 (lead, cont. 31): P77 inputs for the second advisor model, the quadric cone A = {x ∈ F_p^4 ∖ 0 : Q(x) = 0}
(CSTAR O6). Computes the spectrum of A on Z_p^4 (FFT), r = −min_{χ≠0}Â, B = {Â = −r}, N = complement, and
λ_odd = top eigenvalue of 1_A P_N 1_A on odd functions (E117 method). Also the centred one-rep lift's K on T^4 and its
φ, and the P77(b) increment. Q ∈ {hyp: x1x2 + x3x4, ell: x1x2 + x3² − εx4² (ε non-residue)}. NUMERICAL.
Usage: python src/e122_quadric_lambda.py p form
"""
import sys, json, math, itertools
import numpy as np
from scipy.optimize import minimize

p, form = int(sys.argv[1]), sys.argv[2]
eps = next(e for e in range(2, p) if pow(e, (p - 1) // 2, p) == p - 1)
def Q(x):
    if form == "hyp": return (x[0] * x[1] + x[2] * x[3]) % p
    return (x[0] * x[1] + x[2] * x[2] - eps * x[3] * x[3]) % p
A = [x for x in itertools.product(range(p), repeat=4) if any(x) and Q(x) == 0]
ind = np.zeros((p,) * 4)
for x in A: ind[x] = 1
Ah = np.fft.fftn(ind).real
mask = np.ones((p,) * 4, bool); mask[0, 0, 0, 0] = False
vals = np.round(Ah[mask], 6)
r = -Ah[mask].min()
B = np.isclose(Ah, -r) & mask
cN = np.fft.fftn((~B).astype(float)).real / p ** 4
neg = lambda x: tuple((-np.array(x)) % p)
half = np.array([x for x in A if x < neg(x)])
dm = (half[:, None, :] - half[None, :, :]) % p; dp = (half[:, None, :] + half[None, :, :]) % p
C = cN[dm[..., 0], dm[..., 1], dm[..., 2], dm[..., 3]] - cN[dp[..., 0], dp[..., 1], dp[..., 2], dp[..., 3]]
lam = float(np.linalg.eigvalsh(C)[-1])
Z = ((half + p // 2) % p) - p // 2           # centred one-rep lift
z2 = (Z ** 2).sum(1)
phi = float(sum(Z[:, k] @ C @ Z[:, k] for k in range(4)) / z2.sum())
# K of the centred lift on T^4: grid + BFGS
G = 8 * p
grid = np.stack(np.meshgrid(*[np.arange(G) / G] * 4, indexing="ij"), -1).reshape(-1, 4)
F = np.zeros(len(grid))
for z in Z: F += 2 * np.cos(2 * np.pi * grid @ z)
idx = np.argsort(F)[:20]
def fv(x):
    ph = 2 * np.pi * (Z @ x)
    return 2 * np.cos(ph).sum(), -4 * np.pi * (np.sin(ph) @ Z)
best = F[idx[0]]
for i in idx:
    rr = minimize(fv, grid[i], jac=True, method="BFGS")
    best = min(best, rr.fun)
K = -best
spread = 2 * z2.sum() / math.sqrt(2 * (z2 ** 2).sum())
print(json.dumps({"p": p, "form": form, "A": len(A), "spectrum": sorted(set(vals.tolist())), "r": float(r),
                  "ratio_G": len(A) / r ** 2, "B_frac": float(B.sum()) / p ** 4, "lambda_odd": lam,
                  "phi_centred": phi, "K_centred_lift": K, "ratio_centred_lift": len(A) / K ** 2,
                  "P77b_increment": (1 - lam) / 8 * spread}), flush=True)
