"""Basic families: Sidon sets and their difference sets."""
from __future__ import annotations

from itertools import combinations


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def erdos_turan_sidon(p: int) -> list[int]:
    """{2pk + (k^2 mod p) : 0<=k<p}, Sidon for odd prime p."""
    assert is_prime(p) and p > 2
    return sorted(2 * p * k + (k * k) % p for k in range(p))


def is_sidon(B) -> bool:
    B = sorted(B)
    seen = set()
    for u, v in combinations(B, 2):
        d = v - u
        if d in seen:
            return False
        seen.add(d)
    return True


def difference_multiset(B):
    """Positive differences v-u (u<v) with multiplicity, as a dict."""
    D = {}
    B = sorted(B)
    for u, v in combinations(B, 2):
        D[v - u] = D.get(v - u, 0) + 1
    return D


def difference_set(B):
    D = difference_multiset(B)
    if any(m > 1 for m in D.values()):
        raise ValueError("B is not Sidon: differences collide")
    return sorted(D)


def gf_singer(q: int):
    """Singer perfect difference set of size q+1 in Z/(q^2+q+1), q prime.

    Construction: GF(q^3) = GF(q)[x]/(irreducible cubic); a primitive element g;
    D = {i in [0, q^2+q+1) : g^i lies in a fixed 2-dim GF(q)-subspace (trace-0 plane
    spanned by 1, x)} -- we use the subspace {c0 + c1 x}.
    """
    assert is_prime(q)
    m = q * q + q + 1
    # find irreducible monic cubic x^3 + a x^2 + b x + c with a primitive root x
    def mul(u, v, poly):
        # u, v: tuples of length 3 (coeffs of 1, x, x^2); poly = (a,b,c) for x^3 = -(a x^2 + b x + c)
        a, b, c = poly
        prod = [0] * 5
        for i in range(3):
            for j in range(3):
                prod[i + j] = (prod[i + j] + u[i] * v[j]) % q
        for k in (4, 3):
            t = prod[k]
            if t:
                prod[k] = 0
                prod[k - 1] = (prod[k - 1] - a * t) % q
                prod[k - 2] = (prod[k - 2] - b * t) % q
                prod[k - 3] = (prod[k - 3] - c * t) % q
        return tuple(prod[:3])
    order = q ** 3 - 1
    for a in range(q):
        for b in range(q):
            for c in range(1, q):
                poly = (a, b, c)
                # check x has order q^3-1 (implies irreducible + primitive)
                e = (0, 1, 0); cur = (1, 0, 0)
                ok = True
                # compute powers and look for early return to 1
                seen_one_at = None
                p = (1, 0, 0)
                for i in range(1, order + 1):
                    p = mul(p, e, poly)
                    if p == (1, 0, 0):
                        seen_one_at = i
                        break
                if seen_one_at != order:
                    continue
                # build D: exponents i mod m with g^i in span{1,x} up to GF(q)^* scalars
                D = set()
                p = (1, 0, 0)
                for i in range(order):
                    if p[2] == 0:
                        D.add(i % m)
                    p = mul(p, e, poly)
                D = sorted(D)
                assert len(D) == q + 1, (len(D), q)
                return D, m
    raise RuntimeError("no primitive cubic found")
