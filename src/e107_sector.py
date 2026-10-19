"""E107b: the b-adic SECTOR condition for automatic sets (CSTAR A2), computed exactly from the automaton.

Asymptotics (L -> inf, C primitive, C^m ~ lam^m r pi^T, pi^T r = 1):
  f_{A_L}(j/b^k + b^{-L} s) / n_L  ->  Re[ mu_k(j) * nu(s) ],
  mu_k(j) = pi^T M(j/b) ... M(j/b^k) 1 / (pi^T C^k 1),   nu(s) = e_0^T prod_{i>=1} (M(s/b^i)/lam) r / r_0,
  M(y) = sum_d C_d e(d y).
So D := max_{k <= K, j} max(0, -min_{s in R} Re[mu_k(j) nu(s)]) gives M_L >= (D - o(1)) n_L (LINEAR M).
R_L bounded forces D = 0 exactly (sector condition). Here D is computed with s in [-Smax, Smax] (step ds).
Usage: python src/e107_sector.py b S K [limit]   -> JSON rows (b, delta, lam, D, kD = depth attaining D, h0 = -min Re nu)
"""
import sys, json, math, itertools, os
import numpy as np
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(__file__))
from e107_automatic import automata, reach

SMAX, DS, NTH = 200.0, 0.02, 1440

def mats(delta, b):
    S = len(delta); Cd = np.zeros((b, S, S))
    for s in range(S):
        for d in range(b):
            t = delta[s][d]
            if t >= 0: Cd[d, s, t] = 1
    return Cd

def Mof(Cd, y):
    # y: array (P,) -> (P, S, S)
    b = Cd.shape[0]
    ph = np.exp(2j * np.pi * np.outer(y, np.arange(b)))      # (P, b)
    return np.einsum('pd,dst->pst', ph, Cd)

def analyse(args):
    delta, b, K = args
    Cd = mats(delta, b); C = Cd.sum(0); S = C.shape[0]
    w, V = np.linalg.eig(C); i = int(np.argmax(abs(w))); lam = float(w[i].real)
    if not (1.05 < lam < b - 1e-9): return None
    r = np.abs(V[:, i].real); wl, U = np.linalg.eig(C.T); il = int(np.argmax(abs(wl))); pi = np.abs(U[:, il].real)
    if r.min() <= 1e-12 * r.max() or pi.min() <= 1e-12 * pi.max():
        return None   # not primitive on all states; skip (reducible)
    pi = pi / (pi @ r)
    # nu(s) on a grid, s >= 0 (s < 0 by conjugation)
    s = np.arange(0.0, SMAX, DS); P = s.size
    m = int(math.ceil(math.log(SMAX * 1e6) / math.log(b)))
    vec = np.tile(r.astype(complex), (P, 1))                    # apply from the deepest factor outward
    for i_ in range(m, 0, -1):
        vec = np.einsum('pst,pt->ps', Mof(Cd, s / b ** i_), vec) / lam
    nu = vec[:, 0] / r[0]
    nu = np.concatenate([nu, np.conj(nu[1:])])
    th = np.linspace(-np.pi, np.pi, NTH, endpoint=False)
    hmin = np.array([np.min((np.exp(1j * t) * nu).real) for t in th])   # min_s Re(e^{it} nu(s))
    h0 = -float(hmin[NTH // 2])        # theta = 0: main profile
    D, kD = max(0.0, h0), 0
    for k in range(1, K + 1):
        q = b ** k; j = np.arange(1, q); j = j[j % b != 0]
        y = j[:, None] / (b ** np.arange(1, k + 1))[None, :]      # (J, k): j/b, j/b^2, ..., j/b^k
        vec = np.ones((j.size, S), dtype=complex)
        for col in range(k - 1, -1, -1):
            vec = np.einsum('pst,pt->ps', Mof(Cd, y[:, col]), vec)
        Phi = vec @ pi; Phi0 = pi @ np.linalg.matrix_power(C, k) @ np.ones(S)
        mu = Phi / Phi0
        idx = np.clip(np.round((np.angle(mu) + np.pi) / (2 * np.pi) * NTH).astype(int) % NTH, 0, NTH - 1)
        viol = np.abs(mu) * np.maximum(0.0, -hmin[idx])
        if viol.max() > D: D, kD = float(viol.max()), k
    return dict(b=b, delta=delta, lam=lam, D=D, kD=kD, h0=h0)

def main():
    b, S, K = map(int, sys.argv[1:4]); lim = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    W = int(os.environ.get("CHOWLA_WORKERS", "4"))
    jobs = ((d, b, K) for d in automata(b, S))
    if lim: jobs = itertools.islice(jobs, lim)
    with Pool(W) as Pl:
        for r in Pl.imap_unordered(analyse, jobs, chunksize=32):
            if r is not None: print(json.dumps(r), flush=True)

if __name__ == "__main__":
    main()
