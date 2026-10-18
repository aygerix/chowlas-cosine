"""Doubly-positive profile problem (dense-regime heuristic, NOTEBOOK 2026-10-18).
rho(w) = ∫w^2 / (w(0) ∫w) over w >= 0 with ŵ >= 0.  Subclass w = h ⋆ h with h >= 0 (always doubly positive),
and the general class w = h ⋆ h (any real h) with a penalty forcing w >= 0.  Dense heuristic: R ≈ c_E sqrt((1-rho)/2),
ultraflat rounding c_E = sqrt2 => R ≈ sqrt(1-rho).  R < 1/2 needs rho > 3/4."""
import numpy as np, sys
from scipy.optimize import minimize
n = 400
def rho_of(h):
    w = np.correlate(h, h, 'full')            # w(t) on t = -(n-1)..(n-1), w(0) = ||h||^2
    return (w ** 2).sum() / (w[n - 1] * w.sum()), w
def neg(p, signed):
    h = p if signed else p ** 2
    r, w = rho_of(h)
    pen = 0.0 if not signed else 50 * ((np.minimum(w, 0) / w[n - 1]) ** 2).sum()
    return -r + pen
t = np.linspace(-3, 3, n)
inits = {'box': np.ones(n), 'gauss': np.exp(-t ** 2 / 2), 'rand': np.random.default_rng(0).random(n)}
for signed in (False, True):
    for name, h0 in inits.items():
        p0 = h0 if signed else np.sqrt(h0)
        res = minimize(neg, p0, args=(signed,), method='L-BFGS-B', options=dict(maxiter=3000))
        h = res.x if signed else res.x ** 2
        r, w = rho_of(h)
        print(f"signed={signed} init={name:5s} rho={r:.5f} min(w)/w0={w.min()/w[n-1]:+.2e} => sqrt(1-rho)={np.sqrt(1-r):.4f}", flush=True)
print("reference: triangle 2/3 -> 0.5774 ; gaussian 1/sqrt2=0.70711 -> 0.5412")
