"""Reproduction of Bu et al. (arXiv:2610.17160v1) two-sided Singer construction.

S ⊂ Z Sidon, |S| = k:  A(S) = {3|s_i - s_j| : i<j} ∪ {|3(s_i+s_j)+1| : i<j},  |A| = k(k-1),
f_A(x) = rho(x)^2 - k/2 - g(x)/2,  rho = sum cos((3 s_j + 1/2) x),  g = sum cos((6 s_j + 1) x).
S: random tent-weighted thinning of a shifted Singer set (D - c), with a block P of r odd-offset elements nearest
the centre deleted ("parity block"); |S| = k enforced by rejection.
"""
from __future__ import annotations
import math
import numpy as np
from singer import singer


def bu_set_S(q, k, r=None, seed=0, max_tries=100000, D=None, v=None, shift=0):
    if D is None:
        D, v = singer(q)
    D = sorted((d + shift) % v for d in D)
    c = (v - 1) // 2
    L = c + 1
    w = {d: 1 - abs(d - c) / L for d in D}
    if r is None:
        r = math.ceil(3 * math.sqrt(q))
    odd = sorted([d for d in D if (d - c) % 2 != 0], key=lambda d: abs(d - c))
    P = set(odd[:r])
    rest = [d for d in D if d not in P]
    M = sum(w[d] for d in rest)
    theta = k / M
    if theta > 1:
        raise ValueError("k too large for this q")
    rng = np.random.default_rng(seed)
    p = np.array([theta * w[d] for d in rest])
    for _ in range(max_tries):
        xi = rng.random(len(rest)) < p
        if xi.sum() == k:
            S = sorted(d - c for d, keep in zip(rest, xi) if keep)
            return S, dict(q=q, v=v, c=c, r=r, theta=theta, seed=seed, shift=shift)
    raise RuntimeError("rejection sampling failed")


def A_of_S(S):
    k = len(S)
    diffs = {3 * abs(S[i] - S[j]) for i in range(k) for j in range(i + 1, k)}
    sums = {abs(3 * (S[i] + S[j]) + 1) for i in range(k) for j in range(i + 1, k)}
    A = diffs | sums
    if len(A) != k * (k - 1) or len(diffs) + len(sums) != len(A) or 0 in A:
        raise ValueError("A(S) not a genuine set of size k(k-1): S not Sidon?")
    return sorted(A)


def identity_check(S, xs):
    A = A_of_S(S)
    S = np.asarray(S, float)
    Af = np.asarray(A, float)
    out = []
    for x in xs:
        lhs = np.cos(Af * x).sum()
        rho = np.cos((3 * S + 0.5) * x).sum()
        g = np.cos((6 * S + 1) * x).sum()
        out.append(lhs - (rho * rho - len(S) / 2 - g / 2))
    return max(abs(e) for e in out)
