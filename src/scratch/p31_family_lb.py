import json, math, sys
import numpy as np
sys.path.insert(0, "src")
from e51_transfer import sets
S = sets()
for name in ("bu_101_20", "bu_199_40", "bu_401_80", "singer_diff_q61", "dense_N50", "e49_p1_n299_6", "e50_a0.5_n299_10"):
    A = np.asarray(sorted(S[name])); X = int(A.max()); n = len(A)
    G = 16 << math.ceil(math.log2(X)); c = np.zeros(G); c[A] = 1; M = -np.fft.fft(c).real.min()
    best = {}
    for rho, lab in ((0.7698, "beckner"), (None, "elem"), (0.687, "num")):
        b = (0, 0)
        for w in sorted(set(int(X * t) for t in np.linspace(0.01, 1, 400))):
            kw = np.clip(1 - A / (w + 1), 0, None); s = float((kw ** 2).sum())
            W = 2 * (w + 1) / 3 + 1 / (3 * (w + 1))
            C = (0.811 * (X + w + 1) + 0.2367) if rho is None else rho * (X + w + 1)
            lb2 = (W * n - C * s) / (2 * (C - W))
            if lb2 > b[0]: b = (lb2, w / X)
        best[lab] = (round(math.sqrt(max(b[0], 0)) / math.sqrt(n), 4), round(b[1], 3))
    print(name, "n", n, "true R %.4f" % (M / math.sqrt(n)), "P31 LB on R (value, w/X):", best)
