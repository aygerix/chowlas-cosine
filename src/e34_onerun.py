r"""E34: one t-run per residue class in Z — probe of Lemma OR (NOTEBOOK 2026-10-18 late; HEURISTIC prediction
M >~ 0.16·ℓ·√t, i.e. R = M/√|A| >~ 0.16·√ℓ).
A = {y + t·k : 0 <= y < t, τ(y) + 1 <= k <= τ(y) + ℓ} ⊂ Z_{>0}, |A| = ℓt, every residue class mod t is ONE t-run of
length ℓ (so |B_t| = t run-tops).  f_A(x) = Σ cos(ax) = Re[D_ℓ(tx)-twisted F_S(x)] with S = run starts.
Run positions τ: random, linear c·y mod t, quadratic c·y² mod t, inverse c/y mod t (the P20/P21 'bent' phase), τ = 0.
Minimum by FFT grid + Newton polish (chowla.min_estimate_fft): NUMERICAL, UNCERTIFIED.
Usage: python src/e34_onerun.py t1,t2,.. l1,l2,.. [cmax]
"""
import sys, math
import numpy as np
sys.path.insert(0, 'src')
from chowla import min_estimate_fft
ts = [int(v) for v in sys.argv[1].split(',')]; ls = [int(v) for v in sys.argv[2].split(',')]
cmax = int(sys.argv[3]) if len(sys.argv) > 3 else 12
rng = np.random.default_rng(7)
def build(t, l, tau):
    return sorted(y + t * k for y in range(t) for k in range(tau[y] + 1, tau[y] + l + 1))
def R(A):
    return min_estimate_fft(A, oversample=8, polish=6).R
for t in ts:
    inv = [0] + [pow(y, -1, t) if math.gcd(y, t) == 1 else 0 for y in range(1, t)]
    for l in ls:
        fam = {'zero': [[0] * t]}
        fam['random'] = [list(rng.integers(0, t, t)) for _ in range(cmax)]
        fam['linear'] = [[(c * y) % t for y in range(t)] for c in range(1, cmax + 1)]
        fam['quadratic'] = [[(c * y * y) % t for y in range(t)] for c in range(1, cmax + 1)]
        fam['inverse'] = [[(c * inv[y]) % t for y in range(t)] for c in range(1, cmax + 1)]
        out = []
        for name, taus in fam.items():
            vals = [R(build(t, l, tau)) for tau in taus]
            out.append(f"{name} {min(vals):.3f}")
        print(f"t={t} l={l} |A|={l * t}  best R by family: " + ", ".join(out) +
              f"   [Lemma OR heuristic floor ~ {0.16 * math.sqrt(l):.3f}]", flush=True)
