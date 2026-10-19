"""Lead's independent check of TD4 (tdense_report): for T_q = (1-cos qx) f_A + a_q/2,
V_q = mean T^2, W_q = mean T^3 computed by exact rational Fourier convolution (no FFT, no triple-count formula),
compared with the report's closed form W = Delta_q/32 + (3a_q/2)V + a_q/8, Delta = 10c(0)-15c(q)+6c(2q)-c(3q).
Also checks V^2 <= m^2 V + m W with m = 2M - a_q/2 using a grid estimate of M (sanity only)."""
from fractions import Fraction as F
import random, math
import numpy as np

def coeffs_T(A, q):
    # complex Fourier coefficients of T (dict k -> Fraction), f_A = sum_a (e^{iax}+e^{-iax})/2
    f = {}
    for a in A:
        f[a] = f.get(a, 0) + F(1, 2); f[-a] = f.get(-a, 0) + F(1, 2)
    T = {}
    for k, v in f.items():
        T[k] = T.get(k, 0) + v
        T[k + q] = T.get(k + q, 0) - v / 2
        T[k - q] = T.get(k - q, 0) - v / 2
    aq = 1 if q in A else 0
    T[0] = T.get(0, 0) + F(aq, 2)
    return {k: v for k, v in T.items() if v != 0}, aq

def moments(T):
    V = sum(v * T.get(-k, 0) for k, v in T.items())
    # mean T^3 = sum_{k1+k2+k3=0} T_k1 T_k2 T_k3
    P = {}
    for k1, v1 in T.items():
        for k2, v2 in T.items():
            P[k1 + k2] = P.get(k1 + k2, 0) + v1 * v2
    W = sum(v * T.get(-k, 0) for k, v in P.items())
    return V, W

def closed_form(A, q, V, aq):
    S = list(A) + [-a for a in A]
    from collections import Counter
    r = Counter(s1 + s2 for s1 in S for s2 in S)
    c = lambda k: sum(r[k - s] for s in S)
    D = 10 * c(0) - 15 * c(q) + 6 * c(2 * q) - c(3 * q)
    return F(D, 32) + F(3 * aq, 2) * V + F(aq, 8)

def gridM(A, G=1 << 16):
    x = 2 * np.pi * np.arange(G) / G
    return -np.cos(np.outer(np.asarray(sorted(A)), x)).sum(0).min()

random.seed(1)
bad = 0; worst = 1e9
for trial in range(300):
    X = random.randint(3, 30); n = random.randint(1, X)
    A = set(random.sample(range(1, X + 1), n))
    for q in range(1, X + 1):
        T, aq = coeffs_T(A, q)
        V, W = moments(T)
        W2 = closed_form(A, q, V, aq)
        if W != W2: bad += 1
        M = gridM(A); m = 2 * M - aq / 2
        slack = m * m * float(V) + m * float(W) - float(V) ** 2
        worst = min(worst, slack)
print("closed-form mismatches:", bad, " min slack of V^2<=m^2V+mW (grid M, should be >= ~0):", worst)
