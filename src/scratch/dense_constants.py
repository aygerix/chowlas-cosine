# Explicit dense constants from M^2 >= (w+1)(n/(3 C_w) - 1/6), C_w = 0.811(X+w+1) + 0.2367 (P31 + P31-E), n = delta X.
import math
for delta in (0.42, 0.45, 0.5, 0.6, 0.75, 1.0):
    for X in (10**3, 10**5, 10**7):
        n = delta * X; best = (0, 0)
        for w in range(0, X + 1, max(1, X // 4000)):
            C = 0.811 * (X + w + 1) + 0.2367
            v = (w + 1) * (n / (3 * C) - 1 / 6)
            if v > best[0]: best = (v, w / X)
        print(f"delta={delta} X={X}: M >= {math.sqrt(max(best[0],0)/n):.4f} sqrt(n)  (w/X={best[1]:.3f})")
