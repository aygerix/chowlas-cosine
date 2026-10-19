"""Round 17 first falsification tests. Run only through dirun.sh, <=4 cores."""
import json
import math
from pathlib import Path
import sys
import time

import numpy as np
from scipy.linalg import eigvalsh

sys.path.insert(0, 'src')
from chowla import min_estimate_fft, certify_lower_bound

ROOT = Path('.research/agents/tdense17_scratch')


def spline_prob(L):
    a = np.arange(1, 2 * L, dtype=np.int64)
    Q = L * (2 * L * L + 1) // 3
    r = np.empty_like(a)
    lo = a <= L
    b = a[lo]
    r[lo] = Q - L * b * b + (b * b * b - b) // 2
    b = 2 * L - a[~lo]
    r[~lo] = (b * b * b - b) // 6
    return a, r / Q, Q


def main():
    records = []
    for m in (16, 64, 256, 1024):
        n = 2 * m
        s = 1 / (2 * np.sin((2 * np.arange(1, m) - 1) * np.pi / (4 * m - 2)))
        w = np.r_[-s, [0., 0.], s]
        if m <= 64:
            A = np.arange(m + 1, 3 * m + 1)
            H = (np.abs(A[:, None] - A[None, :]) > m).astype(float)
            assert np.max(np.abs(eigvalsh(H) - np.sort(w))) < 1e-9
        rec = dict(test='shifted_interval', m=m, n=n, bulk_gamma1=float(np.sum(w[np.abs(w) <= math.sqrt(n)] ** 2) / n ** 2),
                   neg_energy=float(np.sum(s*s) / n**2), edge=float(s.max()/math.sqrt(n)))
        records.append(rec)
        print(json.dumps(rec), flush=True)
    for L, power in ((512, 2/3), (4096, 2/3), (32768, 2/3), (262144, 2/3),
                     (4096, 5/6), (262144, 5/6)):
        a, p, Q = spline_prob(L)
        k = round(L ** power)
        for seed in (17, 117):
            rng = np.random.default_rng(seed)
            keep = rng.random(len(a)) < p
            keep[:k] = True
            A = a[keep].tolist()
            est = min_estimate_fft(A, oversample=16, polish=16)
            rec = dict(test='forced_spline', L=L, power=power, seed=seed, n=len(A), X=max(A), forced_prefix=k,
                       omega_lower=k+1, M_est=-est.fmin, omega_over_K_est=(k+1)/(-2*est.fmin),
                       forcing_l1=float(np.sum(1-p[:k])), unforced_expected_n=float(p.sum()),
                       expected_n=float(p.sum()+np.sum(1-p[:k])), Q=Q)
            if L == 4096 and seed == 17:
                cert = certify_lower_bound(A, oversample=16, prec=100)
                rec['certified_M_upper'] = -cert.lower_bound
                rec['certified_omega_over_K_lower'] = (k+1)/(-2*cert.lower_bound)
                rec['cert_grid'] = cert.L
            suffix = '_p5_6' if power > 0.8 else ''
            np.savez_compressed(ROOT / f'spline_L{L}_s{seed}{suffix}.npz', A=np.array(A, dtype=np.int64))
            records.append(rec)
            print(json.dumps(rec), flush=True)
    (ROOT / 'probe.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
