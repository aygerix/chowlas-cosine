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

## C-SB (2026-10-18): Bu sums on full Singer sets (E25), examples/singer_bu/certified.json (S, shift, N, max, bound)
Method: src/chowla.certify_lower_bound(A, oversample=16) — arb ball DFT of f, f', f'', f''' on L = 2^⌈log2(16 max A)⌉
points + 4th-order Taylor remainder (rigorous lower bound on min over ALL real x). One method only (no Sturm check: degree
~1.9e5 is beyond the exact route); status INTERVAL-CERTIFIED (single method).
   q = 61: N = 3782, max 10707, min f >= −37.1485, R <= 0.60406
   q = 101: N = 10302, max 30575, min f >= −59.7566, R <= 0.58874
   q = 151: N = 22952, R <= 0.57770;  q = 199: N = 39800, R <= 0.56630;  q = 251: N = 63252, max 189688, R <= 0.56272
   q = 307: N = 94556, max 278751, min f >= −171.2117, R <= 0.55679;  q = 401: N = 161202, max 483272, R <= 0.55476
   (q = 307, 401 certified 2026-10-18 on the laptop with chowla.certify_lower_bound_blocked(A, oversample=16, blocks=64):
   same arb-DFT + Taylor certificate computed in 64 decimated residue blocks; validated bit-identical to the unblocked
   certifier on q = 61, 101 and N = 45. q = 401: grid estimate 0.55358, certificate loses 0.0012 to the Taylor remainder
   at oversample 16 — rerun at oversample 32 to tighten.)
   Tightened 2026-10-18 (certify_lower_bound_blocked, oversample 32, 128 blocks, L = 2^24, ~220 s each):
   q = 307: min f >= −171.184725, R <= 0.556699;  q = 401: min f >= −222.292595, **R <= 0.553656** (N = 161202).

## C-N45 (2026-10-18): N = 45, max 61 (E27; examples/milp/N45_best.json)
A = [1..13, 15..35, 37, 39, 40, 41, 45, 50, 52, 57, 58, 60, 61].
Certificate 1: chowla.certify_lower_bound(A, oversample=64) ⇒ min_x f_A >= −3.8360448 (arb ball DFT + Taylor).
Certificate 2: chowla.sturm_certify(A, 38360448, 10^7): PARI/GP Sturm count, Σ T_a(y) + 3.8360448 has no root in [−1,1]
  (True, 0); with 3.8360432 it has 2 roots. Hence M(A) ∈ [3.8360432, 3.8360448], R(A) <= 0.571844.
Status: INTERVAL-CERTIFIED finite case, two independent methods.

## C-N50 (2026-10-18 night): N = 50 structured-class records (E42; examples/construct/N50_certified.json)
A72 = [1..26, 28..40, 43, 44, 47, 49, 50, 52, 54, 60, 68, 69, 72] (max 72).
A68 = [1..18, 20..37, 39..42, 47, 48, 50, 52, 57, 61, 62, 64, 65, 68] (max 68).
Certificate 1: chowla.certify_lower_bound(A, oversample=64):
  - A72: min f >= −4.0309358;
  - A68: min f >= −4.0483108.
Certificate 2: chowla.sturm_certify(A, B, 10^7), PARI/GP 2.15.4 on dirichlet:
  - A72: Σ T_a + 4.0309358 has no root in [−1,1]; with 4.0309354 it has 2 roots.
  - A68: Σ T_a + 4.0483108 has no root in [−1,1]; with 4.0483104 it has 2 roots.
Hence M(A72) ∈ [4.0309354, 4.0309358] and **R <= 0.5700604**; M(A68) ∈ [4.0483104, 4.0483108] and R <= 0.5725176.
Status: INTERVAL-CERTIFIED finite case, two independent methods.
Reproduce with `src/dirun.sh -c 1 python .research/agents/construct_scratch/cert_n50.py`.
