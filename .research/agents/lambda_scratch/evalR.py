#!/usr/bin/env python
"""Numerical (UNCERTIFIED) evaluation of R(A) = M(A)/sqrt|A| for A = {d > 0 : r_D(d) = lam},
plus the anatomy of the identity 2*lam*f_A = |F_D|^2 - k - E.
M(A) = -min_x f_A(x): dense FFT grid (>= 64*max(A) points) + Newton refinement of the 20 lowest grid minima.
Also reports: naive bound (k+W)/(2 lam), E at the minimiser, |F_D|^2 at the minimiser, and the correlation between
E and |F_D|^2 on the grid (how much E sits where F_D is small).
Usage: evalR.py lam D (comma-separated) [lam D ...]   or   evalR.py --file FILE  (lines 'lam=.. ... D=a,b,c')
"""
import sys, re
import numpy as np


def rprofile(D, S=None):
    """signed autocorrelation c(g) = sum_{u-v=g} eps_u eps_v (S = signs; None = all +)"""
    idx = sorted(range(len(D)), key=lambda i: D[i])
    D = [D[i] for i in idx]; S = [1] * len(D) if S is None else [S[i] for i in idx]
    r = {}
    for i in range(len(D)):
        for j in range(i):
            d = D[i] - D[j]
            r[d] = r.get(d, 0) + S[i] * S[j]
    return r


def fmin(A):
    A = np.array(sorted(A), dtype=float)
    amax = int(A.max())
    n = 1 << int(np.ceil(np.log2(64 * amax + 64)))
    coef = np.zeros(n)
    coef[A.astype(int)] = 1.0
    vals = np.fft.rfft(coef)  # sum exp(-i a x_j), real part = sum cos
    f = np.concatenate([vals.real, vals.real[-2:0:-1]])
    xs = 2 * np.pi * np.arange(n) / n
    idx = np.argsort(f)[:20]
    best = (f[idx[0]], xs[idx[0]])
    for i in idx:
        x = xs[i]
        for _ in range(30):
            s = np.sin(A * x); c = np.cos(A * x)
            g = -(A * s).sum(); h = -(A * A * c).sum()
            if h <= 0: break
            x -= g / h
        v = np.cos(A * x).sum()
        if v < best[0]: best = (v, x)
    return best, xs, f


def analyse(lam, D, S=None):
    if S is None: S = [1] * len(D)
    order = sorted(range(len(D)), key=lambda i: D[i]); D = [D[i] for i in order]; S = [S[i] for i in order]
    k = len(D)
    r = rprofile(D, S)
    A = [d for d, c in r.items() if c == lam]
    Delta = {d: c for d, c in r.items() if c not in (0, lam)}
    W = sum(2 * abs(c) for c in Delta.values())
    (mn, x0), xs, f = fmin(A)
    M = -mn
    N = len(A)
    FD = (np.array(S) * np.exp(1j * np.array(D, float) * x0)).sum()
    F2 = abs(FD) ** 2
    E0 = sum(2 * c * np.cos(d * x0) for d, c in Delta.items())
    # identity check at x0
    lhs = 2 * lam * mn
    rhs = F2 - k - E0
    # grid correlation between E and |F_D|^2 (coarser grid)
    xg = np.linspace(0, 2 * np.pi, 4096, endpoint=False)
    Dv = np.array(D, float)
    F2g = np.abs((np.exp(1j * np.outer(xg, Dv)) * np.array(S)[None, :]).sum(1)) ** 2
    dd = np.array(list(Delta.keys()), float); cc = np.array(list(Delta.values()), float)
    Eg = (2 * cc[None, :] * np.cos(np.outer(xg, dd))).sum(1)
    low = F2g < np.quantile(F2g, 0.25)
    P = k * (k - 1) // 2
    neg = sum(1 for x in S if x < 0)
    print(f"lam={lam} k={k} neg={neg} L={D[-1]-D[0]} |A|={N} phi={lam*N/P:.4f} W={W} W/k={W/k:.3f} "
          f"M={M:.4f} R={M/np.sqrt(N):.4f} naiveM=(k+W)/2lam={(k+W)/(2*lam):.3f} naiveR={(k+W)/(2*lam)/np.sqrt(N):.4f} "
          f"x*={x0:.5f} |F_D(x*)|^2={F2:.3f} E(x*)={E0:.3f} idcheck={lhs-rhs:.1e} "
          f"mean E on lowest-quartile |F|^2 = {Eg[low].mean():.3f} (overall mean {Eg.mean():.3f}, max {Eg.max():.3f}) "
          f"corr(E,|F|^2)={np.corrcoef(Eg, F2g)[0,1]:.3f}")
    # E on the near-zero set of F_D: local minima of |F_D|^2 below 0.1 k on the grid
    nz = [i for i in range(len(xg)) if F2g[i] < 0.1 * k and F2g[i] <= F2g[i - 1] and F2g[i] <= F2g[(i + 1) % len(xg)]]
    if nz:
        Ez = Eg[nz]
        print(f"   near-zeros of F_D (|F|^2<0.1k): {len(nz)} local minima; E there: min {Ez.min():.2f} mean {Ez.mean():.2f} max {Ez.max():.2f}"
              f" (k={k}); lower bound from identity: M >= (k + max E - |F|^2)/(2 lam) = {(k + max(Eg[i]-F2g[i] for i in nz))/(2*lam):.3f};"
              f" 'ideal' R if E=0 there: {(k - F2g[nz].min())/(2*lam)/np.sqrt(N):.4f}")
    defects = sorted(Delta.items())
    print("   defects d:r(d) =", " ".join(f"{d}:{c}" for d, c in defects))
    return M / np.sqrt(N)


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--file":
        for line in open(args[1]):
            m = re.search(r"lam=(\d+).*D=([-\d,]+)", line)
            if m:
                toks = m.group(2).split(",")
                analyse(int(m.group(1)), [abs(int(t)) for t in toks], [(-1 if t.startswith("-") else 1) for t in toks])
    else:
        for i in range(0, len(args), 2):
            analyse(int(args[i]), [int(t) for t in args[i + 1].split(",")])
