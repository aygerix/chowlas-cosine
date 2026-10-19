"""E71: torus level-1 inequality (TL1) numerics. theta*(p) = sup_L Lambda_p(L)^2 / (||L||^2 p(1-p)),
L = sum_s b_s cos(U_s) (U_s iid uniform; phases irrelevant), Lambda_p(L) = E[L 1{L > q_p}] (best set of measure p).
Exact grid quadrature on T^S (S=1: 2^20 pts; S=2: 2048^2; S=3: 256^3) plus the Gaussian limit phi(z_p)^2/(p(1-p)).
NUMERICAL. Usage: python src/e71_tl1.py"""
import math, json
import numpy as np
from math import erf, sqrt, exp, pi
ps = [0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5]
def lam(vals, p):
    v = np.sort(vals)[::-1]; k = int(round(p * len(v))); return v[:k].sum() / len(v), float((vals ** 2).mean())
def ratio(vals, p):
    l, var = lam(vals, p); return l * l / (var * p * (1 - p))
out = {}
u = 2 * np.pi * (np.arange(1 << 20) + 0.5) / (1 << 20); c1 = np.cos(u)
out["S1"] = {p: ratio(c1, p) for p in ps}
g = 2048; u = 2 * np.pi * (np.arange(g) + 0.5) / g; C = np.cos(u)
best2 = {p: (0, None) for p in ps}
for th in np.linspace(0, np.pi / 4, 33):
    vals = (np.cos(th) * C[:, None] + np.sin(th) * C[None, :]).ravel()
    for p in ps:
        r = ratio(vals, p)
        if r > best2[p][0]: best2[p] = (r, float(th))
out["S2"] = best2
g = 256; u = 2 * np.pi * (np.arange(g) + 0.5) / g; C = np.cos(u)
best3 = {p: (0, None) for p in ps}
for a in np.linspace(0, np.pi / 2, 9):
    for b in np.linspace(0, np.pi / 2, 9):
        w = np.array([np.cos(a), np.sin(a) * np.cos(b), np.sin(a) * np.sin(b)])
        vals = (w[0] * C[:, None, None] + w[1] * C[None, :, None] + w[2] * C[None, None, :]).ravel()
        for p in ps:
            r = ratio(vals, p)
            if r > best3[p][0]: best3[p] = (r, [round(float(x), 3) for x in w])
out["S3"] = best3
def zq(p):
    lo, hi = -10, 10
    for _ in range(200):
        m = (lo + hi) / 2
        if 0.5 * (1 - erf(m / sqrt(2))) > p: lo = m
        else: hi = m
    return lo
out["gauss"] = {p: (exp(-zq(p) ** 2 / 2) / sqrt(2 * pi)) ** 2 / (p * (1 - p)) for p in ps}
print(json.dumps({k: {str(p): v for p, v in d.items()} for k, d in out.items()}, indent=1))
print("8/pi^2 =", 8 / pi ** 2)
