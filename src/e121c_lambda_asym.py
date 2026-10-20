r"""E121c: λ_odd(D_{2,1}) = max over primitive odd ψ mod p² of ‖M_ψ‖²/p² (P79 reduction) for larger p, plus σ₁(H)²/p².
NUMERICAL (numpy SVD). Usage: python src/e121c_lambda_asym.py p [j]"""
import sys, json, math, cmath
import numpy as np
p = int(sys.argv[1]); j = int(sys.argv[2]) if len(sys.argv) > 2 else 1
n = p * p; order = p * (p - 1)
units = [u for u in range(1, n) if u % p]
pf = {q for q in range(2, order + 1) if order % q == 0 and all(q % d for d in range(2, int(q ** 0.5) + 1))}
gen = next(g for g in units if all(pow(g, order // q, n) != 1 for q in pf))
dlog = np.zeros(n, dtype=np.int64); x = 1
for e in range(order): dlog[x] = e; x = x * gen % n
s = np.arange(p); diff = (s[None, :] - s[:, None]) % n          # s − s0
jinv = pow(j, -1, p)
arg_phi = (1 - p * jinv * s) % n
best = 0.0; bestH = 0.0
for k in range(order):
    if (k * dlog[n - 1]) % order != order // 2:                 # need ψ(−1) = −1
        continue
    if all((k * dlog[(1 + p * t) % n]) % order == 0 for t in range(1, p)):
        continue                                                 # conductor p
    ph = lambda a: np.exp(-2j * np.pi * k * dlog[a] / order)     # ψ̄
    H = ph(diff); np.fill_diagonal(H, 0)
    phi = ph(arg_phi)
    M = np.zeros((p + 1, p + 1), complex); M[:p, :p] = H; M[:p, p] = ph(np.array([j % n]))[0] * phi; M[p, :p] = phi
    best = max(best, np.linalg.svd(M, compute_uv=False)[0] ** 2 / p ** 2)
    bestH = max(bestH, np.linalg.svd(H, compute_uv=False)[0] ** 2 / p ** 2)
Lam = ((p + 3) + math.sqrt((p + 7) * (p - 1))) / (4 * p)
print(json.dumps({"p": p, "j": j, "lambda_odd": best, "H_top": bestH, "Lambda": Lam,
                  "lam_sqrtp": best * math.sqrt(p), "lam_p_over_logp": best * p / math.log(p)}), flush=True)
