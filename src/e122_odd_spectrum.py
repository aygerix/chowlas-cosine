r"""E122b: full odd concentration spectrum of the hyperbolic quadric cone A ⊂ F_p^r (claim P81: ≡ 1/p). NUMERICAL.
Usage: python src/e122_odd_spectrum.py p r"""
import sys, json, itertools
import numpy as np
p, r = int(sys.argv[1]), int(sys.argv[2])
Q = lambda x: sum(x[2 * i] * x[2 * i + 1] for i in range(r // 2)) % p
A = [x for x in itertools.product(range(p), repeat=r) if any(x) and Q(x) == 0]
ind = np.zeros((p,) * r)
for x in A: ind[x] = 1
Ah = np.fft.fftn(ind).real; mask = np.ones((p,) * r, bool); mask[(0,) * r] = False
rr = -Ah[mask].min(); B = np.isclose(Ah, -rr) & mask
cN = np.fft.fftn((~B).astype(float)).real / p ** r
neg = lambda x: tuple((-np.array(x)) % p)
half = np.array([x for x in A if x < neg(x)])
dm = (half[:, None, :] - half[None, :, :]) % p; dp = (half[:, None, :] + half[None, :, :]) % p
C = cN[tuple(dm[..., k] for k in range(r))] - cN[tuple(dp[..., k] for k in range(r))]
ev = np.linalg.eigvalsh(C)
print(json.dumps({"p": p, "r": r, "A": len(A), "r_floor": float(rr), "ratio_G": len(A) / rr ** 2,
                  "odd_eig_min": float(ev[0]), "odd_eig_max": float(ev[-1]), "one_over_p": 1 / p,
                  "max_offdiag": float(np.abs(C - np.diag(np.diag(C))).max())}), flush=True)
