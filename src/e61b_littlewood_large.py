"""E61b: sharp constant for the one-sided Littlewood problem at larger n (P34; E61 gave 0.607 for n <= 256).
(a) phase optimisation (E61's annealed soft-min L-BFGS) for n = 384, 512, 768, 1024, 3 restarts;
(b) baselines: chirp theta_j = pi j^2/n, Rudin-Shapiro signs (n = 2^k), random phases (median of 5).
Reports -min T/sqrt(n) (64n grid + Newton; UNCERTIFIED diagnostic).  Usage: python src/e61b_littlewood_large.py > examples/e61/e61b.jsonl"""
import json, math, sys
import numpy as np
sys.path.insert(0, "src")
from e61_littlewood import tmin, opt_phases

def rs_signs(k):
    p, q = np.array([1.0]), np.array([1.0])
    for _ in range(k): p, q = np.concatenate([p, q]), np.concatenate([p, -q])
    return p
if __name__ == "__main__":
    rng = np.random.default_rng(11)
    for n in (256, 512, 1024, 2048):
        j = np.arange(1, n + 1)
        chirp = -tmin(np.pi * j * j / n) / math.sqrt(n)
        rs = -tmin(np.where(rs_signs(int(math.log2(n))) > 0, 0.0, np.pi)) / math.sqrt(n)
        rnd = float(np.median([-tmin(rng.uniform(0, 2 * np.pi, n)) / math.sqrt(n) for _ in range(5)]))
        print(json.dumps(dict(kind="baselines", n=n, chirp=round(chirp, 4), rudin_shapiro=round(rs, 4), random_median=round(rnd, 4))), flush=True)
    for n in (384, 512, 768, 1024):
        v, th = opt_phases(n, restarts=3, seed=n)
        print(json.dumps(dict(kind="phases", n=n, negmin_over_sqrt_n=round(-v / math.sqrt(n), 4))), flush=True)
