#!/usr/bin/env python
"""Coherent lifts of cyclic (v,k,lam) difference sets.
For a cyclic difference set B ⊂ Z_v (every nonzero residue is a difference exactly lam times), every multiplier
m ∈ Z_v^* and shift c, put D = {(m*b + c) mod v : b ∈ B} ⊂ [0, v).  Aperiodically r(d) + r(v-d) = lam (1 <= d < v).
Coherent class: r(d) ∈ {0, lam}.  Report the best number of good classes G = #{d : r(d) = lam} and
phi = lam*G / C(k,2), plus the full multiplicity profile of the best lift.
Difference sets: generated (Singer PG(n,q) for small q via explicit field arithmetic, QR, biquadratic, twin prime),
and verified to be (v,k,lam) difference sets before use.  Complements are included.
"""
import sys, itertools
from math import gcd
from collections import Counter


def is_ds(B, v):
    c = Counter((a - b) % v for a in B for b in B if a != b)
    vals = set(c[d] for d in range(1, v))
    return len(vals) == 1, (vals.pop() if len(vals) == 1 else None)


def primes_upto(n):
    s = [True] * (n + 1); s[0] = s[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i): s[j] = False
    return [i for i in range(n + 1) if s[i]]


# --- finite field GF(p^n) via a primitive polynomial found by brute force (p prime, small) ---
def polymulmod(a, b, f, p):
    n = len(f) - 1
    res = [0] * (2 * n)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                res[i + j] = (res[i + j] + x * y) % p
    for i in range(len(res) - 1, n - 1, -1):
        c = res[i]
        if c:
            for j in range(n + 1):
                res[i - n + j] = (res[i - n + j] - c * f[j]) % p
    return res[:n]


def find_primitive(p, n):
    order = p ** n - 1
    fac = [q for q in primes_upto(order) if order % q == 0] if order < 10 ** 6 else None
    for coeffs in itertools.product(range(p), repeat=n):
        f = list(coeffs) + [1]   # monic, f[0] + f[1] x + ... + x^n
        if f[0] == 0: continue
        # x has order exactly p^n - 1 ?
        def xpow(e):
            r = [1] + [0] * (n - 1); b = [0, 1] + [0] * (n - 2) if n > 1 else [0]
            if n == 1: b = [(-f[0]) % p]
            while e:
                if e & 1: r = polymulmod(r, b, f, p)
                b = polymulmod(b, b, f, p); e >>= 1
            return r
        one = [1] + [0] * (n - 1)
        if xpow(order) != one: continue
        if all(xpow(order // q) != one for q in fac):
            return f
    return None


def singer(q, n):
    """Singer difference set of PG(n, q) (q prime here): v = (q^{n+1}-1)/(q-1), k = (q^n-1)/(q-1)."""
    p = q
    N = n + 1
    f = find_primitive(p, N)
    v = (q ** N - 1) // (q - 1)
    # powers x^i, i < v; take i with trace-like condition: coefficient of x^{N-1}... use hyperplane {coord_{N-1} = 0}
    B = []
    r = [1] + [0] * (N - 1)
    xx = [0, 1] + [0] * (N - 2)
    for i in range(v):
        if r[N - 1] == 0: B.append(i)
        r = polymulmod(r, xx, f, p)
    return B, v


def qr(p):
    return sorted(set((x * x) % p for x in range(1, p))), p


def biquad(p):
    return sorted(set(pow(x, 4, p) for x in range(1, p))), p


def twin(p):
    q = p + 2; v = p * q
    def chi(a, m):
        a %= m
        if a == 0: return 0
        return 1 if pow(a, (m - 1) // 2, m) == 1 else -1
    B = [x for x in range(v) if (x % q == 0 and True) or (x % p and x % q and chi(x, p) * chi(x, q) == 1)]
    return sorted(B), v


def lifts(B, v, lam):
    k = len(B)
    best = None
    P = k * (k - 1) // 2
    res = Counter()
    for m in range(1, v):
        if gcd(m, v) != 1: continue
        Bm = [(m * b) % v for b in B]
        for c in range(v):
            D = sorted((b + c) % v for b in Bm)
            r = Counter(D[i] - D[j] for i in range(k) for j in range(i))
            G = sum(1 for d, x in r.items() if x == lam)
            res[G] += 1
            if best is None or G > best[0]:
                best = (G, m, c, D, r)
    return best, res, P


def main():
    cands = []
    for (q, n) in [(2, 2), (3, 2), (2, 3), (3, 3), (5, 3), (2, 4), (7, 3)]:
        try:
            B, v = singer(q, n); cands.append((f"Singer PG({n},{q})", B, v))
        except Exception as e:
            print("singer fail", q, n, e)
    for p in [7, 11, 19, 23, 31, 43]:
        B, v = qr(p); cands.append((f"QR({p})", B, v))
    for p in [37, 101]:
        B, v = biquad(p); cands.append((f"biquad({p})", B, v))
    for p in [3, 5]:
        B, v = twin(p); cands.append((f"twin({p},{p+2})", B, v))
    out = []
    for name, B, v in cands:
        for comp in (False, True):
            BB = sorted(set(range(v)) - set(B)) if comp else B
            ok, lam = is_ds(BB, v)
            if not ok:
                print(f"{name}{' compl' if comp else ''}: NOT a difference set (v={v}, k={len(BB)})"); continue
            if lam < 2 or len(BB) > 60 or v > 200:
                continue
            best, res, P = lifts(BB, v, lam)
            G, m, c, D, r = best
            k = len(BB)
            prof = Counter(r.values())
            def_pairs = P - lam * G
            print(f"{name}{' compl' if comp else ''}: (v,k,lam)=({v},{k},{lam}) best G={G} of {(v-1)//2 if lam*(v-1)//2==P else '?'}"
                  f"  phi={lam*G/P:.4f} defpairs={def_pairs} W/k={2*def_pairs/k:.3f}  m={m} c={c}"
                  f"  r-profile={dict(sorted(prof.items()))}  D={','.join(map(str,D))}", flush=True)
            top = sorted(res.items(), reverse=True)[:4]
            print(f"     distribution of G over all (m,c): top {top}", flush=True)


if __name__ == "__main__":
    main()
