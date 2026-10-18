"""P16' (large sieve form, found by the review agent; re-derived and re-computed by the lead 2026-10-18).
If m (2(1-θ)ηk)^4 >= (4D + π/h)(3k^2/4 - 3k/8), with δ = sqrt(θηk), Σbar(h) < δ, h <= π/2, m = floor(π/(2h)),
D = 6L+1, then M(A(S)) > (1/2 - η)k.   Σbar as in src/p16_constants.py (Lindström counting)."""
import math
from p16_constants import sigbar, hstar
def holds(k, L, eta, theta):
    delta = math.sqrt(theta * eta * k); h = hstar(delta)
    if h is None or h > math.pi / 2: return False
    m = math.floor(math.pi / (2 * h)); D = 6 * L + 1
    return m * (2 * (1 - theta) * eta * k) ** 4 >= (4 * D + math.pi / h) * (0.75 * k * k - 0.375 * k) * (1 + 1e-9)
def best_eta(k, L):
    best = None
    for theta in [i / 100 for i in range(5, 60)]:
        if not holds(k, L, 0.5, theta): continue
        lo, hi = 1e-12, 0.5
        for _ in range(100):
            mid = (lo + hi) / 2
            lo, hi = (lo, mid) if holds(k, L, mid, theta) else (mid, hi)
        if best is None or hi < best[0]: best = (hi, theta)
    return best
if __name__ == "__main__":
    print("k       L=k^2/2           L=12.5k^2         L=32k^2")
    for k in (10**3, 2 * 10**3, 10**4, 10**5, 10**6, 10**8, 10**12):
        row = []
        for c in (0.5, 12.5, 32):
            b = best_eta(k, int(c * k * k))
            row.append("none" if b is None else f"R>={0.5-b[0]:.4f} (θ={b[1]:.2f})")
        print(f"{k:.0e}  " + "  ".join(row), flush=True)
