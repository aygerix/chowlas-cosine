"""Lead's independent check of TD3.profile: p(t)=(1/2)(1-t)^4, e in {p(1-p), p^2}.
D(theta) = (1+theta) S(theta)/theta - E, S(theta)=int_0^theta e(t)(1-t/theta)^2 dt, E=int_0^1 e.
Check: Bernstein coefficients of D on [0,1] all > 0; for theta>=1, m1=int t e/E < 1/4 and m2 > 0."""
from fractions import Fraction as F
from math import comb
def pmul(a, b):
    r = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i + j] += x * y
    return r
one_minus_t = [F(1), F(-1)]
p = [F(1, 2)]
for _ in range(4): p = pmul(p, one_minus_t)
for name, e in [("e_v", pmul(p, [F(1) - p[0]] + [-c for c in p[1:]])), ("e_s", pmul(p, p))]:
    # S(theta)/theta = sum_k e_k theta^k * 2/((k+1)(k+2)(k+3))
    Sd = [e[k] * F(2, (k + 1) * (k + 2) * (k + 3)) for k in range(len(e))]
    E = sum(e[k] / (k + 1) for k in range(len(e)))
    D = pmul([F(1), F(1)], Sd); D[0] -= E
    d = len(D) - 1
    # power -> Bernstein: b_i = sum_{k<=i} C(i,k)/C(d,k) * D_k
    b = [sum(F(comb(i, k), comb(d, k)) * D[k] for k in range(i + 1)) for i in range(d + 1)]
    m1 = sum(e[k] / (k + 2) for k in range(len(e))) / E
    m2 = sum(e[k] / (k + 3) for k in range(len(e))) / E
    print(name, "deg", d, "min Bernstein coeff", min(b), "all>0:", all(x > 0 for x in b), " E", E, " m1", m1, "<1/4:", m1 < F(1, 4), " m2", m2)
