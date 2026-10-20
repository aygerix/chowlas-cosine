r"""E117 (lead, cont. 31): centroid-lemma inputs for Jedwab–Li sets D ⊂ Z_n².
lambda_odd = top eigenvalue of the concentration operator f ↦ 1_D·P_{N}(f) on ODD real functions on D, where
N = Z_n² ∖ B, B = {χ : D̂(χ) <= −r'} (r' = K_G: the background). φ_B(z) <= lambda_odd for EVERY lift z (each
coordinate of the centroid field is an odd function on D). Also reports φ_B for the canonical (centred) lift and
for lifts read from a jsonl (fd 'reps').
Usage: python src/e117_concentration.py p a j [jsonl idx ...]
"""
import sys, json, math
import numpy as np
sys.path.insert(0, "src")
from e114_cp_group import jl_set

p, a, j = (int(t) for t in sys.argv[1:4])
D, n = jl_set(p, a, j)
Dl = sorted(D)
A = np.zeros((n, n)); 
for (x, y) in Dl: A[x, y] = 1
Dh = np.fft.fft2(A).real
r = -Dh[np.unravel_index(np.argmin(np.where(np.arange(n*n).reshape(n,n)==0, np.inf, Dh)), Dh.shape)]
B = np.isclose(Dh, -r); B[0, 0] = False
N = ~B  # includes 0 and the spikes
chis = np.argwhere(N)
G = np.array(Dl)
# odd basis: one g per ±pair
idx = {g: i for i, g in enumerate(Dl)}
half = [g for g in Dl if g < ((-g[0]) % n, (-g[1]) % n)]
# C[g,g'] = (1/n²) Σ_{χ∈N} cos(2π χ·(g−g')/n); on odd functions (e_g − e_{−g}) the restricted matrix is
# Codd[g,h] = C[g,h] − C[g,−h]  (for g,h in 'half')
Hh = np.array(half)
cN = np.fft.fft2(N.astype(float)).real / n ** 2   # c(h) = (1/n²) Σ_{χ∈N} cos(2π χ·h/n)  (N = −N)
def Cmat(X, Y):
    d = (X[:, None, :] - Y[None, :, :]) % n
    return cN[d[..., 0], d[..., 1]]
Codd = Cmat(Hh, Hh) - Cmat(Hh, (-Hh) % n)
ev = np.linalg.eigvalsh(Codd)
out = {"p": p, "a": a, "j": j, "n": n, "D": len(D), "r": float(r), "N_size": int(N.sum()), "N_frac": float(N.mean()),
       "lambda_odd_top": float(ev[-1]), "lambda_odd_top5": [float(v) for v in ev[-5:]],
       "trace_frac": float(ev.sum() / len(ev))}
def phi(Z):
    # centroid field z (one rep per class) -> fraction of Σ|W|² outside B
    W = np.zeros((n, n, 2))
    for g, z in Z.items():
        ph = 2 * np.pi * (np.arange(n)[:, None] * g[0] + np.arange(n)[None, :] * g[1]) / n
        W += np.sin(ph)[..., None] * np.array(z, dtype=float)[None, None, :]
    tot = (W ** 2).sum(); return float((W[N] ** 2).sum() / tot), float(tot)
cen = {g: (((g[0] + n // 2) % n) - n // 2, ((g[1] + n // 2) % n) - n // 2) for g in Dl}
out["phi_centred"], out["W2_centred"] = phi(cen)
for spec in sys.argv[4:]:
    f, i = spec.rsplit(":", 1)
    d = json.loads(open(f).read().splitlines()[int(i)])
    Z = {}
    for z in d["reps"]:
        g = (z[0] % n, z[1] % n); Z[g] = tuple(z); Z[((-g[0]) % n, (-g[1]) % n)] = (-z[0], -z[1])
    out["phi_" + spec] = phi(Z)
print(json.dumps(out), flush=True)
