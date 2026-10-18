import sys, math, numpy as np
sys.path.insert(0, 'src')
from chowla import min_estimate_fft
from sympy import primitive_root
# (1) Z-lift of aligned cubic / quartic residue classes
for (m, p) in [(3, 18367), (3, 15259), (4, 14177), (6, 51637)]:
    g = primitive_root(p)
    H = sorted({pow(g, m * i, p) for i in range((p - 1) // m)})
    A = [h for h in H if h <= (p - 1) // 2]
    e = min_estimate_fft(A, oversample=8)
    # restrict to grid 2*pi*j/p only (finite analog) for comparison
    c = np.zeros(p); c[A] = 1
    fg = np.fft.fft(c).real
    print(f"m={m} p={p}: N={len(A)} R_circle={e.R:.3f}  R_on_p_grid={(-fg[1:].min())/math.sqrt(len(A)):.3f}", flush=True)
# (2) model sets with tapered symmetric windows
phi = (math.sqrt(5) - 1) / 2
for X in [200, 800, 3200]:
    for w0 in [0.3, 0.5, 0.7]:
        for shape in ["flat", "lin", "fejer2"]:
            A = []
            for n in range(1, X + 1):
                t = n / X
                w = w0 * (1 if shape == "flat" else (1 - t) if shape == "lin" else (1 - t) ** 2)
                fr = (n * phi) % 1.0
                if min(fr, 1 - fr) < w / 2: A.append(n)
            e = min_estimate_fft(A, oversample=16)
            print(f"model X={X} w0={w0} {shape}: N={len(A)} R={e.R:.3f}", flush=True)
