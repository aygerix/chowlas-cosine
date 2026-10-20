r"""E119 (lead, cont. 31; advisor's p² question). Random one-rep lifts of JL D_{2,1} ⊂ Z_n², n = p²: class pair {g, −g}
gets z = ḡ + n t, t ∈ {−1, 0}², with probability τ(z) = Λ(z₁/n)Λ(z₂/n) (Σ_{z≡g} τ = 1), and z(−g) = −z(g).
E F = F_τ (fractional PD lift, min = −r exactly). Fluctuation = sum of independent bounded terms per pair, so
K <= r + C√(|D| log n) with positive probability (Hoeffding + union bound on a grid): K_opt = O(p^{3/2}√log p) = o(p²).
This script measures K (NUMERICAL: FFT grid + BFGS) for several seeds and compares with
  advisor's law K ≈ 0.92p²  and  noise law  K ≈ r + √(σ̄²·|D|·ln(4n²)), σ̄² = mean over classes of (1 − Σ_z τ(z)²).
Usage: python src/e119_taper_random.py p seeds [oversampling, default 16]
"""
import sys, json, math
import numpy as np
sys.path.insert(0, "src")
from e114_cp_group import jl_set
from e116_jl_taper import true_min

p, seeds = int(sys.argv[1]), int(sys.argv[2])
os_ = int(sys.argv[3]) if len(sys.argv) > 3 else 16
D, n = jl_set(p, 2, 1)
half = np.array([g for g in sorted(D) if g < ((-g[0]) % n, (-g[1]) % n)])
opts = []
for g in half:
    c = [(g[0] + n * u, g[1] + n * v) for u in (-1, 0) for v in (-1, 0)]
    w = np.array([max(0.0, 1 - abs(z[0]) / n) * max(0.0, 1 - abs(z[1]) / n) for z in c])
    opts.append((np.array(c), w / w.sum()))
sig2 = float(np.mean([1 - (w ** 2).sum() for _, w in opts]))
pred_noise = p + math.sqrt(sig2 * len(D) * math.log(4 * n * n))
for s in range(1, seeds + 1):
    rng = np.random.default_rng(1000 + s)
    Z = np.array([c[rng.choice(4, p=w)] for c, w in opts], dtype=np.int64)
    L = int(np.abs(Z).max())
    fmin, xi, _, _ = true_min(Z, np.ones(len(Z)), L, G=1 << int(math.ceil(math.log2(os_ * (2 * L + 1)))), nstart=16)
    print(json.dumps({"p": p, "n": n, "D": len(D), "seed": s, "K": -fmin, "ratio": len(D) / fmin ** 2,
                      "pred_p2": 0.92 * p * p, "pred_noise_registered": pred_noise, "pred_noise_corrected": p + math.sqrt(2) * (pred_noise - p), "G": os_, "sigma2_bar": sig2,
                      "K_over_sqrt_Dlog": -fmin / math.sqrt(len(D) * math.log(n * n))}), flush=True)
