r"""E36b: is the order-4 obstruction (Theorem O4) also an obstruction for the A-AVERAGED run-top count used in
Shankar's chain, (1/|A|) sum_{t in A} |B_t| <= C K^beta ?  Reuses the O4 set of e36_o4_check.py (same construction,
rebuilt here), then counts |B_t| for every t in A (each t of A has order 2 or 4).
Usage: python src/e36b_o4_avg.py a"""
import sys, itertools, runpy
import numpy as np
a = int(sys.argv[1])
sys.argv = ["e36_o4_check.py", str(a)]
g = runpy.run_path("src/e36_o4_check.py")
ind, K = g["ind"], int(g["K"])
pts = np.argwhere(ind)
tot = 0; mx = 0; hist = {}
for t in pts:
    sh = tuple(int(x) for x in t)
    m_minus = np.roll(ind, sh, axis=tuple(range(a + 1)))            # m - t in A
    m_plus = np.roll(ind, tuple(-x for x in sh), axis=tuple(range(a + 1)))  # m + t in A
    b = int((ind & m_minus & ~m_plus).sum())
    tot += b; mx = max(mx, b)
    o = 2 if all((2 * x) % 4 == 0 for x in sh) else 4
    hist.setdefault((o, b), 0); hist[(o, b)] += 1
n = len(pts)
print(f"a={a}: |A|={n} K={K} avg_t|B_t|={tot / n:.2f} max={mx} avg/K^3={tot / n / K**3:.3f} avg/K^4={tot / n / K**4:.4f}")
print("  (order, |B_t|): count  ->", dict(sorted(hist.items())))
