import numpy as np
from scipy.special import gamma
from mpmath import mp, quadosc, quad, cos, pi, mpf, inf
# min over s of C(s) = int_0^1 u^(a-1) cos(2 pi s u) du, normalised by C(0) = 1/a. Substitute u = v^(1/a): int_0^1 cos(2 pi s v^{1/a}) dv / a
def C(a, s):
    v = np.linspace(0, 1, 40001)
    y = np.cos(2*np.pi*s*v**(1.0/a))
    return np.trapezoid(y, v)  # = a * int u^(a-1) cos
for a in [0.3,0.4,0.5,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0]:
    ss = np.linspace(0.01, 30, 1500)
    vals = np.array([C(a,s) for s in ss])
    print(f"alpha={a:.2f} min_s C/C0 = {vals.min():+.5f} at s={ss[vals.argmin()]:.2f}")
