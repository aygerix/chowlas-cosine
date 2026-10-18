# Finite analog: index-m multiplicative subgroup H of Z_p^*, "Chowla ratio" on the p-grid only:
# R_p = (-min_{theta != 0} eta(theta)/2) / sqrt(|H|/2),  eta(theta) = sum_{h in H} e(h theta / p)  (H symmetric).
import numpy as np, math, sys
from sympy import primerange, primitive_root
def run(m, pmax, pmin=50):
    best = []
    for p in primerange(pmin, pmax):
        if (p - 1) % (2 * m): continue          # need -1 in H: (p-1)/m even
        g = primitive_root(p)
        H = [pow(g, m * i, p) for i in range((p - 1) // m)]
        c = np.zeros(p); c[H] = 1
        eta = np.fft.fft(c).real               # eta(theta) for theta = 0..p-1
        mn = eta[1:].min()
        R = (-mn / 2) / math.sqrt(len(H) / 2)
        best.append((R, p))
    best.sort()
    return best
for m in [2, 3, 4, 5, 6, 8, 10, 12]:
    b = run(m, 20000 if m <= 4 else 60000)
    Rs = [r for r, p in b]
    print(f"m={m}: #p={len(b)} best R={b[0][0]:.4f} at p={b[0][1]}; 2nd {b[1][0]:.4f} (p={b[1][1]}); median {np.median(Rs):.4f}; 1/sqrt(2m)={1/math.sqrt(2*m):.4f}", flush=True)
