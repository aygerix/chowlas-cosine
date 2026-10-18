import numpy as np, math, sys
def minF2(B, over=64):
    L = max(B) + 1; G = 1 << math.ceil(math.log2(over * L)); c = np.zeros(G); c[B] = 1
    v = np.abs(np.fft.fft(c)) ** 2; return v.min()
def is_sidon(B):
    s = set()
    for i, a in enumerate(B):
        for b in B[:i + 1]:
            if a + b in s: return False
            s.add(a + b)
    return True
primes = [p for p in range(5, 230) if all(p % d for d in range(2, int(p ** .5) + 1))]
for p in primes[::3]:
    best = 0
    for a in range(1, min(p, 12)):          # B_a = {2pj + (a j^2 mod p)}, also linear twist (a j^2 + j)
        for lin in (0, 1):
            B = sorted(2 * p * j + ((a * j * j + lin * j) % p) for j in range(p))
            c = minF2(B) / p; best = max(best, c)
    B0 = sorted(2 * p * j + (j * j % p) for j in range(p))
    print(f"p={p:4d} sidon={is_sidon(B0)} c(ET)={minF2(B0)/p:.4f} best over twists c={best:.4f}", flush=True)
