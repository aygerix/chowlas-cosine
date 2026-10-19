"""E94b — RIGOROUS certificate (exact rationals) for the pointwise mixing inequality
      φ(2x/3) <= α1 φ(x) + α2 x     for all x ∈ [0, 1],   φ(x) = (1 − √(1 − x))/2,
with rational α1, α2 > 0. Then, for every w ∈ 𝒲 (P66 step 6, |w| <= 1):
      ∫_0^1 φ((2/3)|w|²) <= α1 ∫_0^1 φ(|w|²) + α2 ∫_0^1 |w|² <= α1·(259/2000) + α2·(2√3/9)
using P63 (D <= 259/2000) and Beckner (∫|w|² <= 2/(3√3) = 2√3/9). Hence D_{2/3} <= that bound.
Method: F(x) = x·G(x) with G(x) = α1/(2(1 + √(1−x))) + α2 − 1/(3(1 + √(1 − 2x/3))) (exact identity
1 − √(1−y) = y/(1 + √(1−y))). On a cell [lo, hi] the first term is increasing in x and the last term is decreasing,
so G >= α1/(2(1 + √(1−lo))) + α2 − 1/(3(1 + √(1 − 2hi/3))). Square roots are enclosed by integer isqrt (directed).
Bisect until every cell has a positive lower bound. G > 0 on [0, 1] ⇒ F >= 0 on [0, 1].
"""
from fractions import Fraction as Fr
from math import isqrt
S = 10**30
def sqrt_up(v):   # rational upper bound for √v, v >= 0 rational
    n = v.numerator * S * S // v.denominator + 1; r = isqrt(n); r = r if r * r >= n else r + 1
    return Fr(r, S)
def sqrt_dn(v):
    n = v.numerator * S * S // v.denominator; return Fr(isqrt(n), S)
a1, a2 = Fr(233809, 10**6), Fr(117344, 10**6)
def Glo(lo, hi):
    return a1 / (2 * (1 + sqrt_up(1 - lo))) + a2 - Fr(1, 3) / (1 + sqrt_dn(1 - Fr(2, 3) * hi))
stack, cells, minlb = [(Fr(0), Fr(1))], 0, None
while stack:
    lo, hi = stack.pop(); g = Glo(lo, hi)
    if g > 0:
        cells += 1; minlb = g if minlb is None or g < minlb else minlb
    else:
        if hi - lo < Fr(1, 2**40): raise SystemExit(f"FAIL near {float(lo)}")
        mid = (lo + hi) / 2; stack += [(lo, mid), (mid, hi)]
sqrt3_up = Fr(17320508075688773, 10**16)          # > √3
assert sqrt3_up**2 > 3
bound = a1 * Fr(259, 2000) + a2 * 2 * sqrt3_up / 9
print("certified G > 0 on [0,1]:", cells, "cells, min lower bound", float(minlb))
print("alpha1 =", a1, "alpha2 =", a2)
print("D_{2/3} <=", bound, "=", float(bound), " => T-dense exponent 1/3 for C <", float(1 / bound), "(1/bound =", 1 / bound, ")")
