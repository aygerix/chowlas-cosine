"""(E4) Rigorous certifier for Bu-type sets via the exact identity
      f_A(x) = rho(x)^2 - k/2 - g(x)/2,   rho = sum_j cos(alpha_j x), alpha_j = 3 s_j + 1/2,  g = sum_j cos(beta_j x), beta_j = 6 s_j + 1,
valid whenever A = A(S) is a genuine set of size k(k-1) (checked by bu.A_of_S; the identity is then exact algebra:
rho^2 = k/2 + g/2 + sum_{i<j} [cos(3(s_i-s_j)x) + cos((3(s_i+s_j)+1)x)]).

f is even and 2pi-periodic, so it suffices to treat x in [0, pi].  Grid x_j = pi j / L (j = 0..L), cell |s| <= h/2,
h = pi/L.  All angles alpha x_j = pi (6s+1) j / (2L) are exact rational multiples of pi: values come from a table
T[m] = cos(pi m / (2L)), m in [0, L], whose entries are FLINT/arb enclosures rounded to double (|err| <= 2^-52 each).
Second-order Taylor on each cell with third-derivative remainder |rho'''| <= sum alpha^3, |g'''| <= sum beta^3.
On each cell: rho ∈ [rlo, rhi], g <= ghi  =>  f >= dist(0,[rlo,rhi])^2 - k/2 - ghi/2.
Float accumulation errors are bounded explicitly (gamma_k * sum of |terms|) and added to the radii.
"""
from __future__ import annotations
import math
import numpy as np

U = 2.0 ** -53


def cos_table(L):
    import flint
    flint.ctx.prec = 80
    T = np.empty(L + 1)
    for m in range(L + 1):
        T[m] = float(flint.arb.cos_pi_fmpq(flint.fmpq(m, 2 * L)).mid())
    return T  # each entry within ~1.2e-16 of the true value (arb mid at 80 bits, then rounded)


def _lookup(T, L, m):
    """cos(pi m/(2L)) for integer array m, via quadrant symmetry (exact index arithmetic)."""
    m = np.mod(m, 4 * L)
    m = np.where(m > 2 * L, 4 * L - m, m)            # cos symmetric about pi
    neg = m > L
    m = np.where(neg, 2 * L - m, m)                  # cos(pi - y) = -cos y
    v = T[m]
    return np.where(neg, -v, v)


def certify_bu(S, L, T=None, chunk=1 << 16, return_profile=False):
    S = np.asarray(S, dtype=np.int64)
    k = len(S)
    a_num = 6 * S + 1          # alpha = a_num / 2
    b_num = 2 * (6 * S + 1)    # beta  = b_num / 2   (beta = 6s+1)
    alpha = a_num / 2.0
    beta = (6 * S + 1).astype(float)
    if T is None:
        T = cos_table(L)
    h2 = math.pi / (2 * L)     # half cell width
    # derivative bounds
    A3 = float(np.sum(np.abs(alpha) ** 3)); B3 = float(np.sum(np.abs(beta) ** 3))
    R3r = A3 * h2 ** 3 / 6.0; R3g = B3 * h2 ** 3 / 6.0
    eps_tab = 2.5e-16
    best = math.inf; best_j = -1
    gk = k * U / (1 - k * U) * 4
    prof = []
    for j0 in range(0, L + 1, chunk):
        j = np.arange(j0, min(L + 1, j0 + chunk), dtype=np.int64)
        ma = np.outer(j, a_num)            # angle = pi * ma / (2L)
        mb = np.outer(j, b_num)
        ca = _lookup(T, L, ma); sa = _lookup(T, L, ma - L)     # sin y = cos(y - pi/2)
        cb = _lookup(T, L, mb); sb = _lookup(T, L, mb - L)
        r0 = ca.sum(1); r1 = -(sa * alpha).sum(1); r2 = -(ca * alpha ** 2).sum(1)
        g0 = cb.sum(1); g1 = -(sb * beta).sum(1); g2 = -(cb * beta ** 2).sum(1)
        # error radii from table + summation
        e_r0 = k * eps_tab + gk * k; e_r1 = (eps_tab + gk) * np.abs(alpha).sum(); e_r2 = (eps_tab + gk) * (alpha ** 2).sum()
        e_g0 = k * eps_tab + gk * k; e_g1 = (eps_tab + gk) * np.abs(beta).sum(); e_g2 = (eps_tab + gk) * (beta ** 2).sum()
        # rho range on cell: quadratic q(s) = r0 + r1 s + r2 s^2/2, |s|<=h2
        def qrange(c0, c1, c2):
            e1 = c0 - c1 * h2 + c2 * h2 * h2 / 2; e2 = c0 + c1 * h2 + c2 * h2 * h2 / 2
            lo = np.minimum(e1, e2); hi = np.maximum(e1, e2)
            with np.errstate(divide="ignore", invalid="ignore"):
                sv = np.where(c2 != 0, -c1 / c2, 0.0)
            inside = (np.abs(sv) < h2) & (c2 != 0)
            vv = c0 + c1 * sv + c2 * sv * sv / 2
            lo = np.where(inside, np.minimum(lo, vv), lo)
            hi = np.where(inside, np.maximum(hi, vv), hi)
            return lo, hi
        rlo, rhi = qrange(r0, r1, r2)
        rad_r = e_r0 + e_r1 * h2 + e_r2 * h2 * h2 / 2 + R3r
        rlo -= rad_r; rhi += rad_r
        glo, ghi = qrange(g0, g1, g2)
        ghi += e_g0 + e_g1 * h2 + e_g2 * h2 * h2 / 2 + R3g
        dist = np.where((rlo <= 0) & (rhi >= 0), 0.0, np.minimum(np.abs(rlo), np.abs(rhi)))
        low = dist * dist - k / 2.0 - ghi / 2.0
        # pad for the handful of float ops in this combination
        low -= 1e-12 * (1 + np.abs(r0) ** 2 + np.abs(g0))
        i = int(np.argmin(low))
        if low[i] < best:
            best = float(low[i]); best_j = int(j[i])
        if return_profile:
            prof.append(low)
    out = dict(lower_bound=best, L=L, x_worst=math.pi * best_j / L, R3r=R3r, R3g=R3g, k=k)
    if return_profile:
        out["profile"] = np.concatenate(prof)
    return out
