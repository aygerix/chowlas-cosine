#!/usr/bin/env python
"""Randomised brute-force checks of the elementary statements T1-T4 in lambda_report.md (sanity checks, not proofs).
T1: W >= 6 for lam >= 3, k >= 3 (random sets and all listed optima).
T2: reflection-symmetric D has exactly floor(k/2) classes with odd r.
T3/T4: r_{A+N B}(N m + e) = r_A(e) r_B(m) + r_A(e-N) r_B(m+1)  (A ⊂ [0,N); T3 is A = [0,N)).
"""
import random
from collections import Counter

def rp(D):
    D = sorted(D); c = Counter()
    for i in range(len(D)):
        for j in range(i):
            c[D[i] - D[j]] += 1
    return c

def rfull(D):  # ordered pairs incl. 0 and negatives
    c = Counter()
    for x in D:
        for y in D:
            c[x - y] += 1
    return c

rnd = random.Random(12345)
# T1
bad = 0
for _ in range(20000):
    k = rnd.randint(3, 14); L = rnd.randint(k, 80)
    D = [0, L] + rnd.sample(range(1, L), k - 2)
    for lam in (3, 4, 5):
        W = sum(2 * c for d, c in rp(D).items() if c != lam)
        if W < 6: bad += 1
print("T1 violations (random):", bad)
# T2
bad = 0
for _ in range(5000):
    c0 = rnd.randint(4, 60)
    half = rnd.sample(range(0, (c0 + 1) // 2), rnd.randint(1, max(1, (c0 + 1) // 2 - 1)))
    D = set(half) | set(c0 - x for x in half)
    if c0 % 2 == 0 and rnd.random() < 0.5: D.add(c0 // 2)
    D = sorted(D)
    k = len(D)
    odd = sum(1 for d, c in rp(D).items() if c % 2)
    if odd != k // 2: bad += 1
print("T2 violations:", bad)
# T3/T4
bad = 0
for _ in range(3000):
    N = rnd.randint(2, 7)
    A = sorted(rnd.sample(range(N), rnd.randint(1, N)))
    B = sorted(rnd.sample(range(-30, 30), rnd.randint(1, 8)))
    D = [a + N * b for a in A for b in B]
    rD, rA, rB = rfull(D), rfull(A), rfull(B)
    for d in range(1, N * 70):
        m, e = divmod(d, N)
        pred = rA.get(e, 0) * rB.get(m, 0) + rA.get(e - N, 0) * rB.get(m + 1, 0)
        if pred != rD.get(d, 0): bad += 1
print("T3/T4 violations:", bad)
