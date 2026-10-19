"""E99: does the SELF-DIFFERENCE graph of a near-extremal set certify its minimum? (NOTEBOOK cont. 19.7)

P9: for any finite W ⊂ Z, M(A) >= -lambda_min(Cay(Z, ±A)[W]) / 2, i.e. K = 2M >= -lambda_min(W).
Vertex sets tested: W0 = A (edges a~a' iff |a-a'| in A), W1 = {0} ∪ A (adds the star at 0).
Random-matrix heuristic (lead): if Cay[A] looks like a density-alpha random graph, its bottom edge is the semicircle edge
-2 sqrt(alpha(1-alpha) n); at alpha = 1/2 this is -sqrt(n), i.e. exactly the C½ value M = sqrt(n)/2.
We report rho_W = -lambda_min(W)/K (fraction of K certified), alpha = 2T3/(n(n-1)), the RMT prediction, the bottom of the
spectrum (soft-edge clustering vs an isolated outlier), and eigenvector anatomy (weight at 0, overlap with 1_A, IPR).
NUMERICAL: M is an FFT+Newton estimate (uncertified); eigenvalues by LAPACK (n <= 3000) or Lanczos with FFT matvec.
Usage: python src/e99_selfgraph.py            (writes examples/e99/e99.jsonl)
"""
import json, math, os, sys, time
import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh
sys.path.insert(0, 'src')
from chowla import min_estimate_fft
from bu import A_of_S
from singer import singer

OUT = 'examples/e99/e99.jsonl'


def t3(A):
    """T3 = #{(a < a') : a' - a in A}, exact integer via FFT autocorrelation (rounded)."""
    X = max(A); L = 1 << math.ceil(math.log2(2 * X + 2))
    c = np.zeros(L); c[A] = 1.0
    F = np.fft.rfft(c); r = np.rint(np.fft.irfft(F * np.conj(F), L)).astype(np.int64)   # r[d] = #{a'-a = d}
    return int(r[np.array(A)].sum())


def selfgraph(W, A, k=8):
    """k smallest eigenpairs of Cay(Z, ±A) induced on the sorted vertex list W (nonnegative integers)."""
    W = np.array(sorted(W), dtype=np.int64); m = len(W); X = int(max(A)); top = int(W.max())
    if m <= 3000:
        D = np.abs(W[:, None] - W[None, :]); inA = np.zeros(max(top, X) + 1, bool); inA[A] = True
        B = inA[D].astype(float); np.fill_diagonal(B, 0.0)
        w, V = np.linalg.eigh(B); return w[:k], V[:, :k]
    L = 1 << math.ceil(math.log2(top + X + 2))
    s = np.zeros(L); s[A] = 1.0; s[(-np.array(A)) % L] = 1.0          # 1_{±A} on Z_L (no wraparound: L > top + X)
    Fs = np.fft.rfft(s)

    def mv(v):
        e = np.zeros(L); e[W] = np.ravel(v)
        return np.fft.irfft(np.fft.rfft(e) * Fs, L)[W]
    op = LinearOperator((m, m), matvec=mv, dtype=float)
    w, V = eigsh(op, k=k, which='SA', tol=1e-9, ncv=max(4 * k, 40))
    o = np.argsort(w); return w[o], V[:, o]


def analyse(name, A, **meta):
    t0 = time.time(); A = sorted(set(int(a) for a in A)); n = len(A)
    M = -min_estimate_fft(A, oversample=16, polish=16).fmin; K = 2 * M
    T3 = t3(A); alpha = 2 * T3 / (n * (n - 1)); pred = 2 * math.sqrt(alpha * (1 - alpha) * n)
    rec = dict(family=name, n=n, X=max(A), C=max(A) / n, M=M, R=M / math.sqrt(n), T3=T3, T3_rel=T3 / n ** 1.5,
               alpha=alpha, rmt_pred_over_K=pred / K, schur_bound_over_M=(math.sqrt(n) / 2 - T3 / (2 * n)) / M) | meta
    for tag, W in (('W0', A), ('W1', [0] + A)):
        w, V = selfgraph(W, A); v = V[:, 0]
        ones = np.ones(len(W)); ones[0 if tag == 'W1' else -1] = ones[0 if tag == 'W1' else -1]
        oA = (v[1:] if tag == 'W1' else v)
        rec[tag] = dict(lam_min=float(w[0]), rho=float(-w[0] / K), bottom=[float(x) for x in w[:8]],
                        w0=float(v[0] ** 2) if tag == 'W1' else None,
                        overlap_1A=float(oA.sum() ** 2 / n), ipr=float((v ** 4).sum() * len(W)))
    rec['secs'] = round(time.time() - t0, 1)
    print(json.dumps(rec), flush=True)
    with open(OUT, 'a') as fh: fh.write(json.dumps(rec) + '\n')


if __name__ == '__main__':
    os.makedirs('examples/e99', exist_ok=True)
    rng = np.random.default_rng(20261019)
    sm = json.load(open('examples/smallN_best.json'))
    for N in ('36', '50', '64', '80', '100'):
        if N in sm: analyse('smallN_best', sm[N]['A'], R_cert=sm[N].get('R_cert'))
    sb = json.load(open('examples/singer_bu/certified.json'))
    for q in ('61', '101', '151', '199'):
        analyse('singer_bu', A_of_S(sb[q]['S']), q=int(q), R_cert=sb[q]['R_cert'])
    for q in (31, 61):                                                    # plain Sidon differences (R -> 1/sqrt2)
        D, v = singer(q); D = sorted(D)
        analyse('sidon_diff', sorted({b - a for a in D for b in D if b > a}), q=q)
    for n in (500, 2000):
        analyse('random_dense_half', (rng.choice(2 * n, n, replace=False) + 1).tolist(), seed=20261019)
        X = int(n ** 1.5); analyse('random_sparse_n1.5', (rng.choice(X, n, replace=False) + 1).tolist(), seed=20261019)
        analyse('sumfree_odd', list(range(n + 1 - (n % 2 == 0), 3 * n, 2))[:n])
        analyse('AP', list(range(1, n + 1)))
