"""Core evaluators and certifiers for Chowla's cosine problem.

Convention (fixed throughout the project):
    f_A(x) = sum_{a in A} cos(a x),  x in R,  period 2*pi.
Internally we often use t = x / (2*pi) in [0, 1) and g(t) = f_A(2*pi*t);
min_x f_A = min_t g, so nothing changes.

Three independent evaluators:
  (E1) min_estimate_fft      : float64 numpy FFT on a fine grid + Newton polish.
                               UNCERTIFIED estimate of min f_A and argmin.
  (E2) certify_lower_bound   : rigorous.  Ball-arithmetic DFT (FLINT/arb acb.dft)
                               gives enclosures of g, g', g'', g''' on a grid of
                               spacing h = 1/L; a 4th-order Taylor remainder with
                               |g''''| <= (2 pi)^4 sum a^4 bounds g between grid
                               points.  Returns a certified lower bound for min g.
  (E3) sturm_certify         : exact.  sum_a T_a(y) + B >= 0 on [-1,1] via PARI
                               polsturm on an integer polynomial (small max(A) only).
"""
from __future__ import annotations

import math
import re
import subprocess
from dataclasses import dataclass

import numpy as np


# ---------------------------------------------------------------------------
# Input handling
# ---------------------------------------------------------------------------

def parse_set(s: str) -> list[int]:
    """Parse an Epoch-format string; raise on any violation of the spec."""
    toks = [t for t in re.split(r"[\s,]+", s.strip()) if t]
    out = []
    for t in toks:
        if not re.fullmatch(r"[0-9]+", t):
            raise ValueError(f"not a plain positive decimal integer: {t!r}")
        v = int(t)
        if v <= 0:
            raise ValueError(f"non-positive frequency {v}")
        out.append(v)
    if len(set(out)) != len(out):
        raise ValueError("repeated frequency")
    return out


def validate(A) -> list[int]:
    A = [int(a) for a in A]
    if not A:
        raise ValueError("empty set")
    if min(A) <= 0:
        raise ValueError("non-positive frequency")
    if len(set(A)) != len(A):
        raise ValueError("repeated frequency")
    return sorted(A)


# ---------------------------------------------------------------------------
# (E1) float evaluator
# ---------------------------------------------------------------------------

def f_direct(A, x):
    """Direct float evaluation of f_A at array x (radians)."""
    A = np.asarray(A, dtype=np.float64)
    x = np.atleast_1d(np.asarray(x, dtype=np.float64))
    out = np.zeros_like(x)
    for chunk in np.array_split(A, max(1, len(A) // 256)):
        out += np.cos(np.outer(x, chunk)).sum(axis=1)
    return out


def grid_values_fft(A, L):
    """g(j/L), j=0..L-1, via real FFT (float, uncertified)."""
    c = np.zeros(L)
    for a in A:
        c[a % L] += 1.0
    return np.fft.fft(c).real  # sum_a cos(2 pi a j / L)


def _newton_polish(A, x0, iters=30):
    Af = np.asarray(A, dtype=np.float64)
    x = float(x0)
    for _ in range(iters):
        s = np.sin(Af * x); c = np.cos(Af * x)
        d1 = -(Af * s).sum(); d2 = -(Af * Af * c).sum()
        if d2 <= 0:
            break
        step = d1 / d2
        x -= step
        if abs(step) < 1e-15:
            break
    return x, float(np.cos(Af * x).sum())


@dataclass
class MinEstimate:
    fmin: float        # estimated min f_A
    xmin: float        # estimated argmin in [0, pi]
    N: int
    R: float           # -fmin / sqrt(N)


def min_estimate_fft(A, oversample=16, polish=8):
    """UNCERTIFIED: grid min via FFT then Newton-polish the best few local minima."""
    A = validate(A)
    L = 1 << max(10, math.ceil(math.log2(oversample * max(A) + 1)))
    g = grid_values_fft(A, L)
    half = g[: L // 2 + 1]
    idx = np.argsort(half)[: max(polish, 1)]
    best = (math.inf, 0.0)
    for j in idx:
        x, v = _newton_polish(A, 2 * math.pi * j / L)
        v_grid = half[j]
        if v_grid < v:
            v, x = v_grid, 2 * math.pi * j / L
        if v < best[0]:
            best = (v, x)
    x = best[1] % (2 * math.pi)
    if x > math.pi:
        x = 2 * math.pi - x
    return MinEstimate(best[0], x, len(A), -best[0] / math.sqrt(len(A)))


# ---------------------------------------------------------------------------
# (E2) rigorous certifier with ball arithmetic
# ---------------------------------------------------------------------------

@dataclass
class Certificate:
    lower_bound: float     # certified: g(t) >= lower_bound for all real t
    L: int                 # grid size
    grid_min_upper: float  # an actual value g(t_j) (upper bound for min g), enclosure mid
    remainder: float       # Taylor remainder budget used per cell
    worst_cell: int
    method: str = "arb-dft + 4th-order Taylor"


def _ball_dft(coeff_dict, L, prec):
    """Rigorous DFT: returns (mid_re, rad_re, mid_im, rad_im) numpy arrays of
    sum_k c_k exp(-2 pi i k j / L)."""
    import flint
    old = flint.ctx.prec
    flint.ctx.prec = prec
    try:
        v = [flint.acb(0)] * L
        for k, c in coeff_dict.items():
            v[k] = v[k] + flint.acb(c)
        w = flint.acb.dft(v)
        mr = np.fromiter((float(z.real.mid()) for z in w), dtype=np.float64, count=L)
        rr = np.fromiter((float(z.real.rad()) for z in w), dtype=np.float64, count=L)
        mi = np.fromiter((float(z.imag.mid()) for z in w), dtype=np.float64, count=L)
        ri = np.fromiter((float(z.imag.rad()) for z in w), dtype=np.float64, count=L)
    finally:
        flint.ctx.prec = old
    # float conversion of the midpoint loses <= 1 ulp; absorb into the radius
    rr = rr + np.abs(mr) * 2.3e-16 + 1e-300
    ri = ri + np.abs(mi) * 2.3e-16 + 1e-300
    return mr, rr, mi, ri


def certify_lower_bound(A, L=None, oversample=16, prec=96):
    """RIGOROUS lower bound for min_x f_A(x).

    With t_j = j/L, s in [-h/2, h/2], h = 1/L, Taylor:
        g(t_j + s) >= g_j + g1_j s + g2_j s^2/2 + g3_j s^3/6 - S4 (h/2)^4 / 24,
    where S4 = (2 pi)^4 sum a^4 bounds |g''''|.  The cubic is minimised exactly
    on the cell (endpoints + interior critical points) using interval-padded
    floats.  Ball radii from arb are subtracted with the appropriate |s|^k.

    Note that g(t) = sum cos(2 pi a t) is the real part of sum exp(+2 pi i a t);
    the arb DFT uses exp(-2 pi i k j/L); real parts agree and derivative signs
    are handled explicitly below (we use cos/sin directly).
    """
    A = validate(A)
    amax = max(A)
    if L is None:
        L = 1 << max(10, math.ceil(math.log2(oversample * amax + 1)))
    # g(t_j)   = sum cos(2pi a j/L)            = Re DFT(c)_j
    # g'(t_j)  = -2pi sum a sin(2pi a j/L)    ;  Im DFT(c a)_j = -sum a sin(...)  => g' = 2pi * Im DFT(a)
    # g''(t_j) = -(2pi)^2 sum a^2 cos(...)    = -(2pi)^2 Re DFT(a^2)
    # g'''(t_j)= (2pi)^3 sum a^3 sin(...)     = -(2pi)^3 Im DFT(a^3)
    def coeffs(k):
        d = {}
        for a in A:
            d[a % L] = d.get(a % L, 0) + a ** k
        return d
    m0, r0, _, _ = _ball_dft(coeffs(0), L, prec)
    _, _, m1, r1 = _ball_dft(coeffs(1), L, prec)
    m2, r2, _, _ = _ball_dft(coeffs(2), L, prec)
    _, _, m3, r3 = _ball_dft(coeffs(3), L, prec)
    tp = 2 * math.pi
    g0, e0 = m0, r0
    g1, e1 = tp * m1, tp * r1 * (1 + 1e-15)
    g2, e2 = -(tp ** 2) * m2, (tp ** 2) * r2 * (1 + 1e-15)
    g3, e3 = -(tp ** 3) * m3, (tp ** 3) * r3 * (1 + 1e-15)
    h2 = 0.5 / L
    S4 = (tp ** 4) * float(sum(a ** 4 for a in A)) * (1 + 1e-12)
    rem = S4 * h2 ** 4 / 24.0
    # cubic p(s) = g0 + g1 s + g2 s^2/2 + g3 s^3/6, minimise over s in [-h2, h2]
    cand = [np.full(L, -h2), np.full(L, h2)]
    # p'(s) = g1 + g2 s + g3 s^2/2 = 0
    # Numerically stable roots: q = -(b + sign(b) sqrt(disc))/2, roots q/a, c/q.
    # Evaluating p at a slightly perturbed critical point s*+d changes p by
    # O(|p''| d^2) since p'(s*) = 0; this is far below the 1e-12 pad.
    a_ = g3 / 2.0; b_ = g2; c_ = g1
    disc = b_ * b_ - 4 * a_ * c_
    with np.errstate(divide="ignore", invalid="ignore", over="ignore"):
        sq = np.sqrt(np.maximum(disc, 0.0))
        sb = np.where(b_ >= 0, 1.0, -1.0)
        q = -(b_ + sb * sq) / 2.0
        r_a = np.where(a_ != 0, q / a_, np.where(b_ != 0, -c_ / b_, 0.0))
        r_b = np.where(q != 0, c_ / q, 0.0)
    for r in (r_a, r_b):
        r = np.where(np.isfinite(r), np.clip(r, -h2, h2), h2)
        cand.append(r)
    pmin = np.full(L, np.inf)
    for s in cand:
        p = g0 + g1 * s + g2 * s * s / 2 + g3 * s ** 3 / 6
        pmin = np.minimum(pmin, p)
    ball = e0 + e1 * h2 + e2 * h2 ** 2 / 2 + e3 * h2 ** 3 / 6
    # float rounding in evaluating p: |terms| <= |g0|+|g1|h2+|g2|h2^2/2+|g3|h2^3/6;
    # ~10 flops each with relative error 2^-53 -> pad by 1e-14 * magnitude.
    mag = np.abs(g0) + np.abs(g1) * h2 + np.abs(g2) * h2 ** 2 / 2 + np.abs(g3) * h2 ** 3 / 6
    lower = pmin - ball - rem - 1e-14 * mag - 1e-12
    j = int(np.argmin(lower))
    return Certificate(float(lower[j]), L, float(g0.min()), rem, j)



def _ball_dft_decimated(coeff_dicts, L, B, r, prec):
    """Rigorous values y_{r+B*i}, 0 <= i < L/B, of y_j = sum_k c_k exp(-2 pi i k j / L), for each coefficient dict.
    Decimation in time: y_{r+Bi} = DFT_{L/B}(v)_i with v_{k'} = sum_{k = k' mod L/B} c_k exp(-2 pi i r k / L); the twist is
    computed in ball arithmetic (exp_pi_i of the exact dyadic -2rk/L), so the result is as rigorous as _ball_dft while
    holding only L/B balls at a time.  Returns a list of (mid_re, rad_re, mid_im, rad_im) per dict."""
    import flint
    old = flint.ctx.prec
    flint.ctx.prec = prec
    Lb = L // B
    try:
        keys = sorted(set().union(*[d.keys() for d in coeff_dicts]))
        tw = {k: flint.acb(flint.arb(-2 * r * k) / L).exp_pi_i() for k in keys} if r else None
        out = []
        for d in coeff_dicts:
            v = [flint.acb(0)] * Lb
            for k, c in d.items():
                z = flint.acb(c) if tw is None else flint.acb(c) * tw[k]
                v[k % Lb] = v[k % Lb] + z
            w = flint.acb.dft(v)
            mr = np.fromiter((float(z.real.mid()) for z in w), dtype=np.float64, count=Lb)
            rr = np.fromiter((float(z.real.rad()) for z in w), dtype=np.float64, count=Lb)
            mi = np.fromiter((float(z.imag.mid()) for z in w), dtype=np.float64, count=Lb)
            ri = np.fromiter((float(z.imag.rad()) for z in w), dtype=np.float64, count=Lb)
            out.append((mr, rr + np.abs(mr) * 2.3e-16 + 1e-300, mi, ri + np.abs(mi) * 2.3e-16 + 1e-300))
            del v, w
    finally:
        flint.ctx.prec = old
    return out


def _cell_lower(g0, e0, g1, e1, g2, e2, g3, e3, h2, rem):
    """Certified lower bound on each Taylor cell [t_j - h2, t_j + h2] (same algebra as certify_lower_bound)."""
    cand = [np.full(len(g0), -h2), np.full(len(g0), h2)]
    a_ = g3 / 2.0; b_ = g2; c_ = g1
    disc = b_ * b_ - 4 * a_ * c_
    with np.errstate(divide="ignore", invalid="ignore", over="ignore"):
        sq = np.sqrt(np.maximum(disc, 0.0))
        sb = np.where(b_ >= 0, 1.0, -1.0)
        q = -(b_ + sb * sq) / 2.0
        r_a = np.where(a_ != 0, q / a_, np.where(b_ != 0, -c_ / b_, 0.0))
        r_b = np.where(q != 0, c_ / q, 0.0)
    for rr in (r_a, r_b):
        cand.append(np.where(np.isfinite(rr), np.clip(rr, -h2, h2), h2))
    pmin = np.full(len(g0), np.inf)
    for s in cand:
        pmin = np.minimum(pmin, g0 + g1 * s + g2 * s * s / 2 + g3 * s ** 3 / 6)
    ball = e0 + e1 * h2 + e2 * h2 ** 2 / 2 + e3 * h2 ** 3 / 6
    mag = np.abs(g0) + np.abs(g1) * h2 + np.abs(g2) * h2 ** 2 / 2 + np.abs(g3) * h2 ** 3 / 6
    return pmin - ball - rem - 1e-14 * mag - 1e-12


def certify_lower_bound_blocked(A, L=None, oversample=16, prec=96, blocks=16, log=None):
    """RIGOROUS lower bound for min_x f_A(x) with bounded memory: identical certificate to certify_lower_bound (arb DFT
    of the 0th..3rd derivative sums on the grid t_j = j/L + 4th-order Taylor cells), but the grid is processed in `blocks`
    residue classes j = r (mod blocks) via _ball_dft_decimated, so peak memory is ~1/blocks of the unblocked version."""
    A = validate(A)
    amax = max(A)
    if L is None:
        L = 1 << max(10, math.ceil(math.log2(oversample * amax + 1)))
    assert L % blocks == 0
    def coeffs(k):
        d = {}
        for a in A:
            d[a % L] = d.get(a % L, 0) + a ** k
        return d
    cds = [coeffs(0), coeffs(1), coeffs(2), coeffs(3)]
    tp = 2 * math.pi
    h2 = 0.5 / L
    S4 = (tp ** 4) * float(sum(a ** 4 for a in A)) * (1 + 1e-12)
    rem = S4 * h2 ** 4 / 24.0
    best = (math.inf, -1); gmin = math.inf
    for r in range(blocks):
        (m0, r0, _, _), (_, _, m1, r1), (m2, r2, _, _), (_, _, m3, r3) = _ball_dft_decimated(cds, L, blocks, r, prec)
        g0, e0 = m0, r0
        g1, e1 = tp * m1, tp * r1 * (1 + 1e-15)
        g2, e2 = -(tp ** 2) * m2, (tp ** 2) * r2 * (1 + 1e-15)
        g3, e3 = -(tp ** 3) * m3, (tp ** 3) * r3 * (1 + 1e-15)
        lower = _cell_lower(g0, e0, g1, e1, g2, e2, g3, e3, h2, rem)
        i = int(np.argmin(lower))
        if lower[i] < best[0]:
            best = (float(lower[i]), r + blocks * i)
        gmin = min(gmin, float(g0.min()))
        if log:
            log(f"  block {r + 1}/{blocks}: running lower bound {best[0]:.6f}")
    return Certificate(best[0], L, gmin, rem, best[1], method="arb-dft (decimated, %d blocks) + 4th-order Taylor" % blocks)

# ---------------------------------------------------------------------------
# (E3) exact Sturm certificate via PARI/GP (small max(A))
# ---------------------------------------------------------------------------

def sturm_certify(A, B_num, B_den=1, timeout=600):
    """EXACT: decide whether sum_{a} T_a(y) + B >= 0 on [-1,1], B = B_num/B_den.

    Returns (ok, nroots) where nroots = number of distinct real roots of
    P(y) = B_den*sum T_a(y) + B_num in [-1,1] (polsturm counts in (a,b]).
    ok is True iff P has no root in [-1,1] and P(1) > 0 ... strictly positive.
    Weak inequality with touching roots is reported as nroots > 0 (not ok).
    """
    A = validate(A)
    terms = "+".join(f"polchebyshev({a},1,y)" for a in A)
    gp = (f"P={B_den}*({terms})+({B_num});"
          f"n=polsturm(P,[-1,1]);"
          f"print(n);print(sign(subst(P,y,1)));")
    r = subprocess.run(["gp", "-q", "-f", "-D", "parisizemax=4000000000"],
                       input=gp, capture_output=True, text=True, timeout=timeout)
    lines = r.stdout.split()
    n = int(lines[0]); sgn = int(lines[1])
    return (n == 0 and sgn > 0), n


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def R_value(fmin, N):
    return -fmin / math.sqrt(N)


def report(A, certify=True, label=""):
    A = validate(A)
    est = min_estimate_fft(A)
    line = (f"{label} N={len(A)} max={max(A)} est_min={est.fmin:.6f} "
            f"x*={est.xmin:.6f} R_est={est.R:.5f}")
    if certify:
        cert = certify_lower_bound(A)
        line += (f" | certified min >= {cert.lower_bound:.6f} "
                 f"(R <= {-cert.lower_bound/math.sqrt(len(A)):.5f}, L={cert.L}, rem={cert.remainder:.2e})")
    print(line)
    return est
