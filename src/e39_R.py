"""E39: lead's check of R(A) for the agent's best λ = 3 set, A = {d > 0 : r_D(d) = 3}; dense grid + golden refinement
(uncertified), plus the T2 parity count for reflection-symmetric sets."""
import numpy as np
from collections import Counter
D = [0, 2, 4, 5, 10, 11, 13, 14, 18, 24]
r = Counter(u - v for u in D for v in D if u > v)
A = sorted(d for d, c in r.items() if c == 3)
dfct = sum(c for d, c in r.items() if c != 3)
x = np.linspace(0, np.pi, 400001)
f = np.cos(np.outer(x, A)).sum(1)
i = f.argmin(); a, b = x[max(i - 1, 0)], x[min(i + 1, len(x) - 1)]
g = lambda t: np.cos(t * np.array(A)).sum()
for _ in range(80):
    m1, m2 = a + (b - a) * 0.382, a + (b - a) * 0.618
    if g(m1) < g(m2): b = m2
    else: a = m1
M = -g((a + b) / 2)
print(f"k=10 set: |A|={len(A)} def={dfct} M={M:.6f} R={M/np.sqrt(len(A)):.4f} argmin x={(a+b)/2:.5f}")
# T2: reflection-symmetric D has exactly floor(k/2) odd-multiplicity classes
rng = np.random.default_rng(1)
for trial in range(5):
    k = int(rng.integers(5, 15)); c = 60
    half = rng.choice(np.arange(1, 30), size=k // 2, replace=False)
    Dsym = sorted(set(list(c // 2 + half) + list(c - (c // 2 + half)) + ([c // 2] if k % 2 else [])))
    rr = Counter(u - v for u in Dsym for v in Dsym if u > v)
    print(f"  T2 check k={len(Dsym)}: odd classes={sum(1 for v in rr.values() if v % 2)} floor(k/2)={len(Dsym)//2}")
