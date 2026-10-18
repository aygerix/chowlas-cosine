"""E46: Kronecker/Bohr sets with ball shape as a construction probe.
A(d, α, X, r) = {1 <= a <= X : |(2a/X − 1, ‖aα_1‖/r, …, ‖aα_d‖/r)|_2 <= 1}   (‖·‖ = distance to nearest integer).
Heuristic: the Fourier transform of a (d+1)-ball has first negative lobe ≈ (2/e)^{(d+1)/2} of its peak, so the
"Gibbs" part of f_A is tiny for large d; the question is whether the sharp-boundary (lattice-point) noise keeps
R = M/√|A| large. Also the cube shape (sup-norm) for contrast. UNCERTIFIED (FFT + Newton).
Usage: python src/e46_bohr_ball.py   (seed 20261019)
"""
import json, math, sys
import numpy as np
sys.path.insert(0, "src")
from chowla import min_estimate_fft

rng = np.random.default_rng(20261019)


def bohr(d, alpha, X, r, norm):
    a = np.arange(1, X + 1)
    u = 2 * a / X - 1
    v = (np.outer(a, alpha) + 0.5) % 1 - 0.5                 # signed distance to nearest integer
    if norm == "ball":
        q = u ** 2 + (v ** 2).sum(1) / r ** 2
    else:
        q = np.maximum(u ** 2, (np.abs(v).max(1) / r) ** 2)
    return a[q <= 1].tolist()


for norm in ("ball", "cube"):
    for d in (0, 1, 2, 3, 4, 6, 8):
        for target in (400, 1600):
            alpha = rng.random(d)
            # choose r so that the expected density ≈ 1/4, then X so that n ≈ target
            vol_ball = math.pi ** ((d + 1) / 2) / math.gamma((d + 1) / 2 + 1)
            rows = []
            for rep in range(3):
                alpha = rng.random(d)
                dens_unit = (vol_ball / 2 if norm == "ball" else 1.0)  # u ∈ [−1,1] has length 2
                r = min(0.5, (0.25 / dens_unit) ** (1 / d)) if d > 0 else 0.5
                dens = dens_unit * (r ** d if d > 0 else 1)
                X = max(50, int(target / max(dens, 1e-9)))
                A = bohr(d, alpha, X, r, norm)
                if len(A) < 20:
                    continue
                M = -min_estimate_fft(A, oversample=16).fmin
                rows.append(M / math.sqrt(len(A)))
                last = (len(A), X, r)
            if rows:
                print(json.dumps(dict(norm=norm, d=d, target=target, n=last[0], X=last[1], r=round(last[2], 4),
                                      R_min=round(min(rows), 4), R_mean=round(float(np.mean(rows)), 4))), flush=True)
