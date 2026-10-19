import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(0)
def neg(z, N):
    v = z * z                                   # v >= 0
    c = np.convolve(v, v)
    return -(c @ c) / (N * (v @ v) ** 2)
for N in (2, 3, 5, 10, 20, 50, 120):
    best = (0, None)
    for trial in range(12):
        z0 = rng.random(N) + (0.5 if trial == 0 else 0)
        if trial == 1: z0 = np.ones(N)
        r = minimize(neg, z0, args=(N,), method="L-BFGS-B", options={"maxiter": 5000})
        if -r.fun > best[0]: best = (-r.fun, r.x ** 2)
    v = best[1] / best[1].max()
    print(N, round(best[0], 5), "const:", round(-neg(np.ones(N), N), 5), "shape:", np.round(v[:: max(1, N // 10)], 2))
