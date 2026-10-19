"""E62c: structure of the best phase-relaxed configuration on the dense N50 support (E62: R 0.498 < 1/2).
10 random starts; saves the best phases and reports how close they are to {0, pi} (signs), to a linear phase (pure
shift), and the location/height of the global minimum. UNCERTIFIED (32x grid)."""
import json, math, sys
import numpy as np
sys.path.insert(0, "src")
from e51_transfer import sets
from e62_phase_relax import optimise, final_R
A = np.asarray(sorted(sets()["dense_N50"])); n = len(A); rng = np.random.default_rng(5); res = []
for s in range(10):
    th = optimise(A, rng.uniform(0, 2 * np.pi, n), betas=[2 / math.sqrt(n), 8 / math.sqrt(n), 32 / math.sqrt(n), 128 / math.sqrt(n), 512 / math.sqrt(n)], iters=500)
    res.append((final_R(A, th), th))
res.sort(key=lambda t: t[0]); R, th = res[0]
# remove the best linear phase (shift invariance x -> x + c gives theta_a -> theta_a - a c) and global sign: fit c
best = None
for c in np.linspace(0, 2 * np.pi, 4001):
    r = np.angle(np.exp(1j * (th + A * c)))
    v = float(np.mean(np.minimum(np.abs(r), np.pi - np.abs(r))))     # distance to {0, pi}
    if best is None or v < best[0]: best = (v, c, r)
print(json.dumps(dict(R_values=[round(r[0], 4) for r in res], best_R=round(R, 4),
                      mean_dist_to_signs_after_shift=round(best[0], 4), shift=round(best[1], 4),
                      phases_after_shift=[round(float(x), 3) for x in best[2]], A=A.tolist())))
