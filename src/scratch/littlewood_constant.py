"""P34 explicit constants.  T(x) = sum_{j=1}^n Re(b_j e^{ijx}), |b_j| <= 1, sum|b_j|^2 = E >= delta*n, T >= -M.
Window inequality (P31 chain):  W_w (M^2 + E/2) <= C_L (M^2 + S_w/2),  L = n + w,
  S_w = sum_{j=1}^w (1 - j/(w+1))^2 = w(2w+1)/(6(w+1)),  W_w = 1 + 2 S_w,
  C_L = (L+1)            [trivial Nikolskii, Fejer-Riesz + Cauchy-Schwarz]
      = 0.811(L+1)+0.2367 [P31-E, kernel-checked]
=> M^2 >= (W_w E - C_L S_w)/(2(C_L - W_w)) whenever C_L > W_w.  Exact rational-free evaluation in floats (diagnostic).
Prints min over n <= N of LB/sqrt(n) for delta = 1 and the large-n constants for several delta."""
import math
def lb(n, E, rho_kind):
    best = 0.0
    for w in range(0, n + 1):
        S = w * (2 * w + 1) / (6 * (w + 1)); W = 1 + 2 * S; L = n + w
        C = (L + 1) if rho_kind == "trivial" else 0.811 * (L + 1) + 0.2367
        if C <= W: continue
        v = (W * E - C * S) / (2 * (C - W))
        if v > best: best = v
    return math.sqrt(best)
for kind in ("trivial", "elem"):
    worst = min((lb(n, n, kind) / math.sqrt(n), n) for n in range(1, 2001))
    big = {n: round(lb(n, n, kind) / math.sqrt(n), 4) for n in (10, 100, 1000, 3000)}
    print(kind, "delta=1: min_{n<=2000} LB/sqrt(n) =", round(worst[0], 4), "at n =", worst[1], "; large n:", big)
    for d in (0.45, 0.5, 0.6, 0.75, 0.9):
        print("   delta", d, "n=3000:", round(lb(3000, d * 3000, kind) / math.sqrt(3000), 4))
