"""E100: positivity vs resolution for a window arc (NOTEBOOK cont. 20.3). Omega = [-rho, rho] in T = R/Z has
hat(k) = sin(2 pi k rho)/(pi k), hat(0) = 2 rho. All hat(k) >= 0 for 1 <= k <= L iff rho <= 1/(2L). For rho = c/(2L),
compute the fraction of ||1_Omega||^2 = 2 rho carried by |k| > L (exact series, mpmath). NUMERICAL (convergent series)."""
import mpmath as mp
mp.mp.dps = 30
for L in (10, 100, 1000, 10000):
    for c in (1.0, 0.5, 0.25):
        rho = mp.mpf(c) / (2 * L)
        tot = 2 * rho
        low = rho * rho * 4 + 2 * mp.fsum(mp.sin(2 * mp.pi * k * rho) ** 2 / (mp.pi * k) ** 2 for k in range(1, L + 1))
        # 4 rho^2 is hat(0)^2; Parseval: sum_k hat(k)^2 = 2 rho
        print(f"L={L} c={c} delta_L = {float((tot - low) / tot):.5f}")
