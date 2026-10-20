r"""E121 (lead, cont. 31): check of the character reduction of λ_odd for JL D_{2,j} (j ≠ 0), P79.
Claim: λ_odd = max over PRIMITIVE odd characters ψ of (Z/p²)^* of ‖M_ψ‖²/p², where M_ψ is the (p+1)×(p+1) matrix
    M = [[H, ψ̄(j)φ], [φᵀ, 0]],  H[s0, s] = ψ̄(s − s0) (s ≠ s0, s, s0 ∈ [0, p)), H[s, s] = 0,  φ_s = ψ̄(1 − p j⁻¹ s)
(conductor-p characters contribute 0), and the bound λ_odd <= [(p+3) + √((p+7)(p−1))]/(4p).
Compares with the direct eigenvalue (E117 method). NUMERICAL (numpy). Usage: python src/e121_lambda_char.py p j
"""
import sys, json, math
import numpy as np
sys.path.insert(0, "src")
from e114_cp_group import jl_set

p, j = int(sys.argv[1]), int(sys.argv[2])
n = p * p
# direct λ_odd (E117 method)
D, _ = jl_set(p, 2, j)
A = np.zeros((n, n))
for g in D: A[g] = 1
Dh = np.fft.fft2(A).real
mask = np.ones((n, n), bool); mask[0, 0] = False
r = -Dh[mask].min(); B = np.isclose(Dh, -r) & mask
cN = np.fft.fft2((~B).astype(float)).real / n ** 2
half = np.array([g for g in sorted(D) if g < ((-g[0]) % n, (-g[1]) % n)])
dm = (half[:, None, :] - half[None, :, :]) % n; dp = (half[:, None, :] + half[None, :, :]) % n
lam_direct = float(np.linalg.eigvalsh(cN[dm[..., 0], dm[..., 1]] - cN[dp[..., 0], dp[..., 1]])[-1])
# characters of (Z/p²)^*: find a generator, ψ_k(g^e) = e(k e / (p(p−1)))
order = p * (p - 1)
units = [u for u in range(1, n) if u % p]
gen = next(g for g in units if all(pow(g, order // q, n) != 1 for q in {2, p} | {f for f in range(2, p) if (p - 1) % f == 0 and all(f % d for d in range(2, f))}))
dlog = {}
x = 1
for e in range(order):
    dlog[x] = e; x = x * gen % n
res = []
for k in range(order):
    psi = lambda u, k=k: np.exp(2j * np.pi * k * dlog[u % n] / order)
    odd = abs(psi(n - 1) + 1) < 1e-9
    prim = any(abs(psi(1 + p * t) - 1) > 1e-9 for t in range(1, p))
    if not odd:
        continue
    if not prim:
        res.append((k, "cond p", 0.0)); continue
    jinv = pow(j, -1, p)
    H = np.zeros((p, p), complex)
    for s0 in range(p):
        for s in range(p):
            if s != s0: H[s0, s] = np.conj(psi(s - s0))
    phi = np.array([np.conj(psi(1 - p * jinv * s)) for s in range(p)])
    M = np.zeros((p + 1, p + 1), complex)
    M[:p, :p] = H; M[:p, p] = np.conj(psi(j)) * phi; M[p, :p] = phi
    sv = np.linalg.svd(M, compute_uv=False); svH = np.linalg.svd(H, compute_uv=False)
    res.append((k, "prim", float(sv[0] ** 2 / p ** 2), float(svH[0] ** 2), float(svH[1] ** 2)))
lam_char = max(t[2] for t in res)
bound = ((p + 3) + math.sqrt((p + 7) * (p - 1))) / (4 * p)
prim = [t for t in res if t[1] == "prim"]
print(json.dumps({"p": p, "j": j, "lambda_direct": lam_direct, "lambda_char": lam_char, "bound_P79": bound,
                  "n_odd_prim": len(prim), "n_odd_condp": len(res) - len(prim),
                  "H_top_sv2_over_p2": max(t[3] for t in prim) / p ** 2, "H_top_two_equal": all(abs(t[3] - t[4]) < 1e-8 for t in prim),
                  "H_frob_half_over_p2": (p - 1) / (2 * p)}), flush=True)
