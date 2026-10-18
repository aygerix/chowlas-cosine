"""Mechanism test M-B: multi-residue (arithmetic x macroscopic) doubly-positive profiles.

A dense set with residue-dependent profile has density v_r(n/X) on n = r (mod q).  Main term near x = 2 pi j/q + y is
(X/q) * hat(phi_j)(X y) with phi_j(t) = sum_r v_r(t) cos(2 pi j r / q)  (v_{-r} = v_r, symmetric in t), so Gibbs-freeness
requires EVERY phi_j to be positive definite (j = 0..q-1), and 0 <= v_r <= 1.  The profile absorbs the L^2 fraction
    rho_q = sum_r int v_r^2 / sum_r int v_r      (max v <= 1),
and the dense heuristic is R ~ c_E sqrt((1 - rho)/2).  q = 1 is the doubly-positive constant rho* ~ 0.724 (E16, P17).
Question: does sup rho_q exceed rho* for some q >= 2?  (Residue structure = sublattice spikes at 2 pi j/q, all positive.)

Parametrisation: phi_j = h_j * h_j~ (autocorrelation, so p.d. exactly), h_j in R^K signed; v_r = (1/q) sum_j cos(2pi jr/q) phi_j
(phi_j = phi_{q-j} enforced by using one h per orbit {j, q-j}).  Penalties for v_r < 0 and v_r > 1.  L-BFGS, analytic grad.
"""
import sys, json
import numpy as np
from scipy.optimize import minimize

def setup(q):
    orbits = sorted({min(j, (q - j) % q) for j in range(q)})
    # C[r, o] = (1/q) * sum_{j in orbit o} cos(2 pi j r / q)
    C = np.zeros((q, len(orbits)))
    for r in range(q):
        for oi, o in enumerate(orbits):
            js = {o, (q - o) % q}
            C[r, oi] = sum(np.cos(2 * np.pi * j * r / q) for j in js) / q
    return orbits, C

def unpack(p, K, no):
    return p.reshape(no, K)

def q_mass(C):
    return C.shape[0]

def objective(p, K, C, mu):
    no = C.shape[1]; H = unpack(p, K, no)
    phis = np.array([np.correlate(h, h, 'full') for h in H])          # (no, 2K-1)
    V = C @ phis                                                     # (q, 2K-1) profiles v_r
    S1 = V.sum(); S2 = (V ** 2).sum()
    neg = np.minimum(V, 0.0); over = np.maximum(V - 1.0, 0.0)
    # width constraint (excludes narrow delta-like profiles, for which rho -> 1 trivially on a grid):
    # mass-weighted mean |t| >= 0.2 K  (the arch profile on [-K, K] has mean |t| ~ 0.3 K)
    at = np.abs(np.arange(-(K - 1), K)).astype(float)
    mt = (V.sum(0) * at).sum() / S1
    short = max(0.0, 0.2 * K - mt)
    L = -S2 / S1 + mu * ((neg ** 2).sum() + (over ** 2).sum()) + mu * short ** 2
    dV = -(2 * V * S1 - S2) / S1 ** 2 + mu * (2 * neg + 2 * over) - mu * 2 * short * (at[None, :] - mt) / S1   # dL/dV
    dphi = C.T @ dV                                                  # (no, 2K-1)
    grad = np.zeros_like(H)
    for o in range(no):
        G = dphi[o]; G = 0.5 * (G + G[::-1])
        hp = np.concatenate([np.zeros(K - 1), H[o], np.zeros(K - 1)])
        grad[o] = 2 * np.correlate(hp, G, 'valid')
    return L, grad.ravel()

def evaluate(p, K, C):
    no = C.shape[1]; H = unpack(p, K, no)
    phis = np.array([np.correlate(h, h, 'full') for h in H])
    V = C @ phis
    Vc = np.clip(V, 0, None); m = Vc.max()
    Vc = Vc / m
    rho = (Vc ** 2).sum() / Vc.sum()
    # p.d. check of each phi_j after clipping (clipping changes them slightly): min of transform / max
    pdmin = []
    for j in range(C.shape[0]):
        ph = np.array([sum(Vc[r] * np.cos(2 * np.pi * j * r / C.shape[0]) for r in range(C.shape[0]))])[0]
        F = np.fft.rfft(np.concatenate([ph[K - 1:], np.zeros(8 * K), ph[:K - 1]])).real
        pdmin.append(F.min() / max(F.max(), 1e-12))
    at = np.abs(np.arange(-(K - 1), K)).astype(float)
    global LAST_WIDTH; LAST_WIDTH = float((Vc.sum(0) * at).sum() / Vc.sum() / K)
    return rho, V.min() / V.max(), min(pdmin), Vc

if __name__ == "__main__":
    K = int(sys.argv[1]) if len(sys.argv) > 1 else 120
    qs = [int(s) for s in sys.argv[2].split(',')] if len(sys.argv) > 2 else [1, 2, 3, 4, 6]
    ntr = int(sys.argv[3]) if len(sys.argv) > 3 else 12
    rng = np.random.default_rng(1)
    t = np.linspace(0, 1, K)
    for q in qs:
        orbits, C = setup(q); no = len(orbits)
        best = (-1, None)
        for trial in range(ntr):
            # inits: arch for orbit 0; smaller random/arch for others with random amplitude
            H0 = []
            for o in range(no):
                if o == 0 or trial % 3 == 0:
                    h = np.sin(np.pi * t) ** (0.5 + rng.random()) * (1 if o == 0 else rng.random())
                else:
                    h = rng.standard_normal(K) * 0.3 * rng.random()
                H0.append(h + 0.05 * rng.standard_normal(K))
            p = np.array(H0).ravel()
            p /= np.sqrt(np.abs(np.correlate(p[:K], p[:K], 'full')).max())
            for mu in (10.0, 100.0, 1000.0, 1e4):
                res = minimize(objective, p, args=(K, C, mu), jac=True, method='L-BFGS-B', options=dict(maxiter=4000))
                p = res.x
            rho, vmin, pdm, Vc = evaluate(p, K, C)
            if pdm > -1e-3 and rho > best[0]:
                best = (rho, Vc, vmin, pdm)
            print(json.dumps(dict(q=q, trial=trial, rho=round(rho, 5), vmin_rel=round(vmin, 5), pd_min=round(pdm, 6), width=round(LAST_WIDTH, 3))), flush=True)
        rho, Vc, vmin, pdm = best
        means = [round(float(Vc[r].sum() / Vc.sum()), 4) for r in range(q)]
        print(json.dumps(dict(q=q, K=K, best_rho=round(rho, 5), class_mass=means, R_sym=round(float(np.sqrt(1 - rho)), 4))), flush=True)
