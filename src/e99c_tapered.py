"""E99c: graph certificates on TAPERED random sets (NOTEBOOK cont. 19.11).

E99b showed P9 on W2 = {0} u A u (-A) certifies ~sqrt(n) on FLAT random sets at every density, via a macroscopic negative
eigenvalue: the graphon of W2 is the convolution kernel rho(|x-y|) on [-1,1], which is indefinite for the flat profile
(a boxcar is not positive definite; this is Gibbs in graph form). For a positive-definite profile (triangle) that
eigenvalue should disappear, leaving the star (~1/alpha) and the noise bulk (~2 sqrt(alpha n)): ~n^(1/3) at
alpha ~ n^(-1/3). Test: random A with P(a in A) = 2 alpha (1 - a/X) (mean density alpha) for alpha = n^(-1/2), n^(-1/3),
n^(-1/4). NUMERICAL. Usage: python src/e99c_tapered.py
"""
import json, math, os, sys
import numpy as np
sys.path.insert(0, 'src')
from chowla import min_estimate_fft
from e99_selfgraph import selfgraph

OUT = 'examples/e99/e99c.jsonl'
os.makedirs('examples/e99', exist_ok=True)
rng = np.random.default_rng(20261021)
for n in (1000, 4000, 16000):
    for ex in (0.5, 1 / 3, 0.25):
        alpha = n ** (-ex); X = int(round(n / alpha))
        a = np.arange(1, X + 1); p = np.clip(2 * alpha * (1 - a / X), 0, 1)
        A = a[rng.random(X) < p].tolist(); m = len(A)
        M = -min_estimate_fft(A, oversample=8, polish=8).fmin
        rec = dict(n=m, n_target=n, alpha_exp=round(ex, 4), alpha=alpha, X=X, profile='triangle', M=M, R=M / math.sqrt(m),
                   pred_bulk=2 * math.sqrt(alpha * m), pred_star=1 / alpha, n13=m ** (1 / 3), seed=20261021)
        for tag, W in (('W0_A', A), ('W2_0pmA', [X] + [X + b for b in A] + [X - b for b in A])):
            w, _ = selfgraph(W, A, k=4)
            rec[tag] = dict(lam_min=float(w[0]), over_sqrt_n=float(w[0] / math.sqrt(m)), over_n13=float(w[0] / m ** (1 / 3)),
                            cert_M_over_true=float(-w[0] / (2 * M)))
        print(json.dumps(rec), flush=True)
        with open(OUT, 'a') as fh: fh.write(json.dumps(rec) + '\n')
