r"""E121b (lead self-check of P79/P80, codex unavailable until 2026-10-25). Exact integer checks:
 (a) D_{2,j} = orbits of g_s = (jp+s, 1), g_* = (j, p) under unit scalars, free action;
 (b) D̂ two-valued {p² − p, −p} and N ∖ 0 = N₁ ∪ N₂ exactly (sets);
 (c) β: Σ_{g∈D}|g_c|² >= (p+1)(p²−1)p²(p²−p+1)/12 and the closed form of the right side;
 (d) the character reduction λ_char = λ_direct for larger p, and max over all odd primitive ψ of ‖M_ψ‖²/p² <= Λ(p).
Usage: python src/e121_check.py p   (all j = 1..p−1)
"""
import sys, json, math, cmath
import numpy as np
sys.path.insert(0, "src")
from e114_cp_group import jl_set

p = int(sys.argv[1]); n = p * p
units = [u for u in range(1, n) if u % p]
out = {"p": p, "j": []}
for j in range(1, p):
    D, _ = jl_set(p, 2, j)
    reps = [((j * p + s) % n, 1) for s in range(p)] + [(j, p)]
    orb = [{((u * g[0]) % n, (u * g[1]) % n) for u in units} for g in reps]
    a_ok = all(len(o) == len(units) for o in orb) and set().union(*orb) == D and sum(map(len, orb)) == len(D)
    ind = np.zeros((n, n)); 
    for g in D: ind[g] = 1
    Dh = np.rint(np.fft.fft2(ind).real).astype(int)
    vals = sorted(set(Dh.flatten().tolist()) - {len(D)})
    Nset = {(a, b) for a in range(n) for b in range(n) if (a, b) != (0, 0) and Dh[a, b] == p * p - p}
    N1 = {(al, (-al * (j * p + s0)) % n) for al in units for s0 in range(p)}
    N2 = {((p * a1) % n, be) for a1 in range(1, p) for be in units if (be + a1 * j) % p == 0}
    b_ok = vals == [-p, p * p - p] and Nset == (N1 | N2) and not (N1 & N2)
    cen = lambda x: ((x + n // 2) % n) - n // 2
    S = sum(cen(x) ** 2 + cen(y) ** 2 for x, y in D)
    rhs = (p + 1) * (p * p - 1) * p * p * (p * p - p + 1) // 12
    c_ok = S >= rhs and 12 * rhs == (p + 1) * (p * p - 1) * p * p * (p * p - p + 1)
    out["j"].append({"j": j, "orbits_ok": bool(a_ok), "spectrum_N_ok": bool(b_ok), "beta_ok": bool(c_ok),
                     "beta": S / (len(D) * n * n), "beta_lower": (p ** 3 + 1) / (12 * p ** 3)})
# (d) characters
order = p * (p - 1)
pf = {q for q in range(2, order + 1) if order % q == 0 and all(q % d for d in range(2, int(q ** 0.5) + 1))}
gen = next(g for g in units if all(pow(g, order // q, n) != 1 for q in pf))
dlog = {}; x = 1
for e in range(order): dlog[x] = e; x = x * gen % n
Lam = ((p + 3) + math.sqrt((p + 7) * (p - 1))) / (4 * p)
worst = 0.0; pair_ok = True; anti_ok = True
for k in range(order):
    psi = lambda u: cmath.exp(2j * math.pi * k * dlog[u % n] / order)
    if abs(psi(n - 1) + 1) > 1e-9 or all(abs(psi(1 + p * t) - 1) < 1e-9 for t in range(1, p)):
        continue
    H = np.array([[0 if s == s0 else psi(s - s0).conjugate() for s in range(p)] for s0 in range(p)])
    anti_ok &= np.allclose(H.T, -H)
    sv = np.linalg.svd(H, compute_uv=False); pair_ok &= abs(sv[0] - sv[1]) < 1e-8
    for j in range(1, p):
        jinv = pow(j, -1, p)
        phi = np.array([psi(1 - p * jinv * s).conjugate() for s in range(p)])
        M = np.zeros((p + 1, p + 1), complex); M[:p, :p] = H; M[:p, p] = psi(j).conjugate() * phi; M[p, :p] = phi
        worst = max(worst, np.linalg.svd(M, compute_uv=False)[0] ** 2 / p ** 2)
out.update({"max_char_lambda_all_j": float(worst), "Lambda": Lam, "bound_ok": bool(worst <= Lam + 1e-12),
            "H_antisym_all": bool(anti_ok), "H_top_pair_all": bool(pair_ok)})
out["all_exact_ok"] = bool(all(d["orbits_ok"] and d["spectrum_N_ok"] and d["beta_ok"] for d in out["j"]))
out["beta_min"] = min(d["beta"] for d in out["j"]); out.pop("j") if p > 7 else None
print(json.dumps(out), flush=True)
