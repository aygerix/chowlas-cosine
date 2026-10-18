# Certificates

## Method E2 (src/chowla.py: certify_lower_bound)
g(t) = f_A(2 pi t). Grid t_j = j/L (L power of 2 >= 16 max A). FLINT acb.dft (ball arithmetic, prec 96) encloses
g, g', g'', g''' at all grid points. For |s| <= 1/(2L): g(t_j+s) >= cubic Taylor polynomial - S4 (1/(2L))^4/24,
S4 = (2pi)^4 sum a^4. Cubic minimized exactly on the cell (endpoints + stable critical points); ball radii and a
1e-14 relative + 1e-12 absolute float pad subtracted. Output: rigorous lower bound for min f_A (modulo correctness of
FLINT and of the float-padding argument, which is documented inline).
## Method E3 (sturm_certify): exact integer polynomial P(y) = B_den sum T_a(y) + B_num, PARI polsturm on [-1,1].

## Dense-regime sets (2026-10-18) — examples/dense_certified.json
Method E2 (src/chowla.py certify_lower_bound: arb ball DFT of a^0..a^3 weights on 2L-grid, cubic Taylor per cell,
4th-order remainder S4 (π/2L)^4/24, float pads). Best: X30_s1 N=20 max 30, f_A >= −2.68817 for all real x, R <= 0.6011;
X50_s0 N=34 max 49, f_A >= −3.52350, R <= 0.6043. Re-verify: `.venv/bin/python -c "import sys,json;sys.path.insert(0,'src');
from chowla import certify_lower_bound as c;d=json.load(open('examples/dense_certified.json'));print(c(d['X50_s0']['A']))"`.

## C-N36 (2026-10-18): best finite set known to us, R(A) <= 0.564795
A = [1..11, 13..23, 25..31, 34, 35, 37, 44, 45, 48, 50]  (N = 36, max 50; examples/smallN_best.json key "36";
exhaustive optimum of the box [1,52], small-N agent).
Certificate 1 (lead): src/chowla.certify_lower_bound(A, oversample=64): arb ball-arithmetic DFT on L = 4096 points +
  4th-order Taylor remainder 4.3e−7 ⇒ min_x f_A(x) >= −3.3887702 ⇒ M(A) <= 3.3887702, R <= 0.564795.
Certificate 2 (agent): PARI/GP Sturm sequences on Σ T_a(t) + B over t ∈ [−1,1] bracket M(A) ∈ [3.3887696, 3.3887699].
Status: INTERVAL-CERTIFIED finite case (two independent methods). Says nothing about any limit.
Also certified (same method): N=35 (max 48) R <= 0.567674; N=34 (max 48) R <= 0.574135.
