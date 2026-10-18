"""E24b: ±1 cosine sums by continuous homotopy (second optimiser for E24).  a_j = tanh(κ u_j), κ increasing so that a -> ±1;
minimise a soft-min penalty −softmin_t Σ a_j cos(j t) / ||a|| with Adam, then round to sign(u) and polish by single-flip
descent on the exact grid objective.  c := −min L / sqrt(X/2).  UNCERTIFIED.
Usage: python src/signed_homotopy.py X iters seed
"""
import sys, math, time
import numpy as np
sys.path.insert(0, 'src')
from signed_sa import true_min_signed

X, iters, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
rng = np.random.default_rng(seed)
G = 8 * X; ts = np.pi * np.arange(G + 1) / G; j = np.arange(1, X + 1)
Cm = np.cos(np.outer(ts, j))                              # (G+1) x X
u = rng.normal(0, 0.1, X); m = np.zeros(X); v = np.zeros(X); t0 = time.time()
for it in range(iters):
    kap = 1.0 + 30.0 * it / iters
    a = np.tanh(kap * u); nrm = math.sqrt((a * a).sum() / 2) + 1e-12
    L = Cm @ a / nrm
    beta = 4.0
    w = np.exp(-beta * (L - L.min())); w /= w.sum()
    # objective J = -softmin(L) ≈ -Σ w L ; gradient wrt a (treating w fixed, standard soft-min gradient)
    gL = -w
    ga = Cm.T @ gL / nrm - ((w * L).sum() * -1) * a / (2 * nrm * nrm) * 0  # norm term dropped (a -> ±1 makes nrm const)
    g = ga * kap * (1 - a * a)
    m = 0.9 * m + 0.1 * g; v = 0.999 * v + 0.001 * g * g
    u -= 0.02 * m / (np.sqrt(v) + 1e-9)
eps = np.where(u >= 0, 1.0, -1.0); val = Cm @ eps; cur = -val.min()
improved = True
while improved:                                           # single-flip steepest descent polish
    improved = False
    for i in rng.permutation(X):
        nv = val - 2 * eps[i] * Cm[:, i]
        if -nv.min() < cur - 1e-12:
            eps[i] = -eps[i]; val = nv; cur = -nv.min(); improved = True
M = -true_min_signed(eps)
print(f"X={X} seed={seed} iters={iters} c={M / math.sqrt(X / 2):.4f} t={time.time() - t0:.0f}s", flush=True)
