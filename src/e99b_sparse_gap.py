"""E99b: the sparse-regime gap in the graph certificates (NOTEBOOK cont. 19.10).

Prediction (lead, after the advisor's sum-free example): for a random A of density alpha in [1, X] (alpha = n/X), the
self-difference graph has bulk edge ~ -2 sqrt(alpha n), and the star at 0 gives ~ -1/alpha. So every P9 certificate on
W in {A, {0} u A, {0} u A u (-A)} is only ~ n^(1/3) at alpha ~ n^(-1/3), while the true M is ~ sqrt(n log n)
(Fourier spread, P28). Here we measure lambda_min on those three vertex sets for alpha = n^(-1/2), n^(-1/3), n^(-1/4).
NUMERICAL (M uncertified; eigenvalues by Lanczos with an exact FFT matvec). Usage: python src/e99b_sparse_gap.py
"""
import json, math, os, sys
import numpy as np
sys.path.insert(0, 'src')
from chowla import min_estimate_fft
from e99_selfgraph import selfgraph, t3

OUT = 'examples/e99/e99b.jsonl'
os.makedirs('examples/e99', exist_ok=True)
rng = np.random.default_rng(20261020)
for n in (1000, 4000, 16000):
    for ex in (0.5, 1 / 3, 0.25):
        alpha = n ** (-ex); X = int(round(n / alpha))
        A = sorted((rng.choice(X, n, replace=False) + 1).tolist())
        M = -min_estimate_fft(A, oversample=8, polish=8).fmin; T3 = t3(A)
        rec = dict(n=n, alpha_exp=round(ex, 4), alpha=alpha, X=X, M=M, R=M / math.sqrt(n), T3_rel=T3 / n ** 1.5,
                   pred_bulk=2 * math.sqrt(alpha * n), pred_star=1 / alpha, n13=n ** (1 / 3), seed=20261020)
        sets = {'W0_A': A, 'W1_0A': [0] + A, 'W2_0pmA': [X] + [X + a for a in A] + [X - a for a in A]}
        for tag, W in sets.items():
            w, _ = selfgraph(W, A, k=4)
            rec[tag] = dict(lam_min=float(w[0]), over_sqrt_n=float(w[0] / math.sqrt(n)), over_n13=float(w[0] / n ** (1 / 3)),
                            cert_M_over_true=float(-w[0] / (2 * M)))
        print(json.dumps(rec), flush=True)
        with open(OUT, 'a') as fh: fh.write(json.dumps(rec) + '\n')
