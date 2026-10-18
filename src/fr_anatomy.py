"""Anatomy of the Fejer-Riesz factor of lambda + f_A (lambda slightly above M(A)); UNCERTIFIED diagnostics.

|Q(e^{ix})|^2 = lambda + f_A(x), Q(z) = sum_{beta=0}^{X} q_beta z^beta (minimum-phase factor).
Reports: |q| profile, coherent multiplicity m_coh(g) = (sum|q q'|)^2 / sum|q q'|^2, phase coherence
phi(g) = |r(g)| / sum|q q'| on g in A and leakage on g not in A (where r(g) = 0 exactly).
"""
from __future__ import annotations
import sys, json, math
import numpy as np
import mpmath as mp


def fr_factor(A, lam, dps=60):
    X = max(A)
    mp.mp.dps = dps
    c = [mp.mpf(0)] * (2 * X + 1)
    c[X] = mp.mpf(lam)
    for a in A:
        c[X + a] += mp.mpf(1) / 2
        c[X - a] += mp.mpf(1) / 2
    roots = mp.polyroots(c[::-1], maxsteps=400, extraprec=4 * dps)   # coefficients highest degree first
    inside = [r for r in roots if abs(r) < 1]
    assert len(inside) == X, (len(inside), X)
    # Q(z) = k * prod (z - r): coefficients
    poly = [mp.mpc(1)]
    for r in inside:
        new = [mp.mpc(0)] * (len(poly) + 1)
        for i, p in enumerate(poly):
            new[i] += p * (-r)
            new[i + 1] += p
        poly = new
    q = np.array([complex(p) for p in poly])           # q[beta] coefficient of z^beta
    # normalise so that autocorrelation at lag X matches c[2X] = 1/2 (if X in A)
    r = np.correlate(q, q, mode="full")                 # r[k] = sum q[n+k-X'] conj ...
    lag0 = len(q) - 1
    scale = lam / r[lag0].real
    q = q * math.sqrt(scale)
    return q


def anatomy(A, lam):
    q = fr_factor(A, lam)
    X = len(q) - 1
    Aset = set(A)
    r = np.array([np.sum(q[g:] * np.conj(q[:X + 1 - g])) for g in range(X + 1)])
    err = max(abs(r[g] - (0.5 if g in Aset else 0.0)) for g in range(1, X + 1))
    absq = np.abs(q)
    out = []
    for g in range(1, X + 1):
        prod = absq[g:] * absq[:X + 1 - g]
        s1 = prod.sum(); s2 = (prod ** 2).sum()
        out.append((g, g in Aset, s1 * s1 / s2 if s2 > 0 else 0, abs(r[g]) / s1 if s1 > 0 else 0, s2))
    return q, err, out


if __name__ == "__main__":
    sys.path.insert(0, "src")
    from chowla import min_estimate_fft
    A = json.load(open(sys.argv[1]))["A"]
    e = min_estimate_fft(A, oversample=64)
    M = -e.fmin
    lam = M * (1 + 1e-7)
    q, err, out = anatomy(A, lam)
    N = len(A)
    print(f"N={N} X={max(A)} M={M:.5f} R={M/math.sqrt(N):.4f} recon_err={err:.2e}")
    w_in = sum(o[4] for o in out if o[1]); w_out = sum(o[4] for o in out if not o[1])
    print(f"pair-weight on A-classes {w_in:.4f}, on non-A classes {w_out:.4f} (fraction wasted {w_out/(w_in+w_out):.3f})")
    mc = np.array([o[2] for o in out if o[1]]); ph = np.array([o[3] for o in out if o[1]]); ww = np.array([o[4] for o in out if o[1]])
    print(f"A-classes: weighted mean m_coh={np.sum(mc*ww)/ww.sum():.3f}, weighted mean phi^2={np.sum(ph**2*ww)/ww.sum():.3f}")
    print("|q| profile:", np.round(np.abs(q), 3).tolist())
    print("arg q / pi:", np.round(np.angle(q) / np.pi, 3).tolist())
