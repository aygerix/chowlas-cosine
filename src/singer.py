"""Fast Singer perfect difference sets D ⊂ Z/v, v = q^2+q+1, |D| = q+1 (q prime).

GF(q^3) = GF(q)[x]/(x^3 - a2 x^2 - a1 x - a0) with x primitive.  D = {i in [0,v) : coefficient of x^2 in x^i is 0}
(x^i lies in the 2-dim subspace span{1, x}); this set is invariant under GF(q)^* scaling, i.e. well defined mod v.
"""
from __future__ import annotations


def _factor(n):
    f, p = set(), 2
    while p * p <= n:
        while n % p == 0:
            f.add(p); n //= p
        p += 1
    if n > 1:
        f.add(n)
    return f


def _mul(u, w, poly, q):
    a2, a1, a0 = poly  # x^3 = a2 x^2 + a1 x + a0
    c = [0] * 5
    for i in range(3):
        if u[i]:
            for j in range(3):
                c[i + j] += u[i] * w[j]
    for k in (4, 3):
        t = c[k] % q
        if t:
            c[k - 1] += a2 * t; c[k - 2] += a1 * t; c[k - 3] += a0 * t
        c[k] = 0
    return (c[0] % q, c[1] % q, c[2] % q)


def _pow(u, e, poly, q):
    r = (1, 0, 0)
    while e:
        if e & 1:
            r = _mul(r, u, poly, q)
        u = _mul(u, u, poly, q)
        e >>= 1
    return r


def singer(q: int):
    order = q ** 3 - 1
    primes = _factor(order)
    X = (0, 1, 0)
    for a0 in range(1, q):
        for a1 in range(q):
            for a2 in range(q):
                poly = (a2, a1, a0)
                # x primitive <=> x^(order/p) != 1 for all p | order, and x^order == 1
                if _pow(X, order, poly, q) != (1, 0, 0):
                    continue
                if any(_pow(X, order // p, poly, q) == (1, 0, 0) for p in primes):
                    continue
                v = q * q + q + 1
                D, cur = [], (1, 0, 0)
                for i in range(v):
                    if cur[2] == 0:
                        D.append(i)
                    cur = _mul(cur, X, poly, q)
                assert len(D) == q + 1, (q, len(D))
                return D, v
    raise RuntimeError("no primitive polynomial")


def is_perfect_difference_set(D, v):
    seen = set()
    for a in D:
        for b in D:
            if a != b:
                r = (a - b) % v
                if r in seen:
                    return False
                seen.add(r)
    return len(seen) == v - 1
