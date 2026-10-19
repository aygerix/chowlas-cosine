"""Continuum elementary bound: rho <= min_{0<lam<1} mu(lam), where mu(lam) = top eigenvalue of
T = lam*Mult(1-2A(1-A)) + (1-lam)*(1 x 1) on L^2[0,1]; mu solves 1 = (1-lam) * int_0^1 dA / (mu - lam*(1-2A(1-A))),
mu > lam.  (From E1, E2 after the substitution g = 1/V(A).)"""
import numpy as np
from scipy.optimize import brentq, minimize_scalar
from scipy.integrate import quad
def mu(lam):
    f = lambda m: (1 - lam) * quad(lambda A: 1 / (m - lam * (1 - 2 * A * (1 - A))), 0, 1, limit=200)[0] - 1
    return brentq(f, lam + 1e-12, 2.0)
r = minimize_scalar(mu, bounds=(1e-6, 1 - 1e-6), method="bounded", options={"xatol": 1e-10})
print("min_lam mu =", r.fun, "at lam =", r.x)
