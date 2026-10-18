# Experiments (exact tests, seeds, outputs)

## E0 (2026-10-17) Baseline evaluators and Sidon differences
- Code: src/chowla.py (E1 float FFT+Newton; E2 rigorous arb DFT + 4th-order Taylor remainder; E3 exact PARI polsturm).
- Sanity: A={1}: -1; {1,2}: -1.125 exact (2c^2+c-1 at c=-1/4); {1,2,3}: -1.3155651547; {1,3,5}: -3 (x=pi). E1/E2 agree.
- Erdős–Turán Sidon B_p={2pk+(k^2 mod p)}, A=(B-B)^+: p=5..31, est min ≈ -p/2, certified lower bounds within 2e-3
  of -p/2; R = 0.79 (p=5) ... 0.719 (p=31). PARI Sturm (exact) confirms f_A >= -5/2 for p=5 and brackets the min.
## E0b (2026-10-17) Simulated annealing probe (src/search.py), seeds 0,1, 150k iters, grid objective
- N=10..80, L in {3N,6N,12N}: best R 0.65 (N=10), 0.71 (20), 0.84 (30), 0.82 (40), 0.92 (60), 0.96 (80).
- Conclusion: plain SA is far weaker than algebraic constructions for N>=30; not informative about mechanisms.
  Data: examples/sa_best_v1.json. UNCERTIFIED.

## E1 (2026-10-17) Cube-framework ILP (src/cube_ilp.py) — see NOTEBOOK. Optimum R_cube = 0.8165 for k <= 8.
## E2 (2026-10-17) Boundary sets |B_t| (src/boundary.py): max_t|B_t|/K^2 <= 0.47 on all families (uninformative; see caveat).
## E3 (2026-10-17) Q-flat(m) local search (src/qflat.py, 3 seeds x 60k iters): F_2 = 0.909 (n=12), 0.933 (n=16) symmetric;
   F_3 = 0.682 (12), 0.650 (16), 0.600 (20); F_4 = 0.667 (12), 0.600 (16), 0.725 (n=24 sym; product ±(S+{0,32})).
## E4 (2026-10-17) Bu et al. reproduction (src/singer.py, src/bu.py; best of 40 Singer shifts, seed 0, r = ceil(3 sqrt q))
   CERTIFIED by E4 identity certifier (src/cert_identity.py; arb cos table, 2nd-order Taylor, L = 2^ceil(log2(32 max A))):
   | q | k | n | max A | est min | certified min >= | R_cert <= |
   | 61 | 12 | 132 | 8201 | -9.5006 | -9.5008 | 0.8269 |
   | 101 | 20 | 380 | 19050 | -14.8943 | -14.8974 | 0.7642 |
   | 199 | 40 | 1560 | 97738 | -27.7233 | -27.7559 | 0.7027 |
   | 311 | 60 | 3540 | 248407 | -40.3428 | -40.4277 | 0.6795 |
   | 401 | 80 | 6320 | 432979 | -52.2459 | -52.2550 | 0.6573 |
   Data: examples/bu_reproduction_certified.json (S, shift, theta). E2 (arb DFT) and E4 agree on q=61,101 (E4 looser by <5e-3).
   Paper (uncertified, seed 0): 0.839, 0.805, 0.725, 0.708, 0.674 — shift selection explains our slightly smaller values.
## E5 (2026-10-17/18) Local improvement from Bu seeds (src/improve.py; add/remove/swap SA on grid, cap = max A)
   61_12 s0: 0.8269 -> 0.8269; 101_20 s0,s1: 0.7642 -> 0.7641; 199_40 s0 (450 s): 0.7027 -> 0.7013 (grid; = cert/grid gap).
   Bu sets are strict local optima under single-element moves. Data: examples/improve_*.json.
## E6 (2026-10-17) Dense-regime SA (src/dense_sa.py X iters seed random; 4e5 iters; free N; grid G = 2^ceil(log2 16X))
   arb-certified (E2) R <= : X=30: 0.6011 (N=20, s1), 0.6073 (s0); X=50: 0.6043 (N=34, s0), 0.6348; X=80: 0.6403 (N=54),
   0.6527; X=120: 0.6730 (N=73), 0.6791; X=180: 0.6942 (N=122), 0.7473; X=260: 0.7459 (N=150), 0.8165.
   Error-diffused Fejér profiles (no SA): R = 0.96–2.37 (X = 20..1280) — bad. Data: examples/dense_runs/.
## E7 (2026-10-18) Exact box MILP (src/box_ilp.py X lams timelimit; HiGHS via scipy.milp; cutting planes at violating x)
   X=30, lam=2.7: optimal N=20 (the E6 set, R=0.6011). X=40, lam=2.4: optimal N=14, M=2.3664 (R=0.6324); 532 s.
   X=40/50/60 scans over lam ∈ {2.4,...,4.5} running (examples/box_ilp/X*.jsonl). Feasibility of the final A is checked
   numerically (64X grid + Newton), so N is the true box optimum for that lam up to that (uncertified) check.
## E8 (2026-10-18) Sidon lower-flatness (scratchpad sidon_flat.py; 3 seeds x 4000 SA moves; D ⊂ [0, 1.5k^2])
   max min_x|F_D|^2/k = 0.103 (k=5), 0.096 (6), 0.034 (8), 0.020 (10), 0.0041 (12), 0.0017 (16). Threshold for
   R(D−D) < 1/2 is 0.293. Singer (q <= 101, multipliers 1,2,3,5): <= 0.008.
## E9 (2026-10-18) Bu-class SA over Sidon S ⊂ [−L, L] (src/bu_class_sa.py k L iters seed; grid objective, UNCERTIFIED)
   30k iters: excess (M − k/2)/sqrt k = 0.37 (k=6), 0.49 (8), 0.59 (10), 0.65 (12), 0.68 (16); R = 0.69–0.72. Longer runs
   in examples/bu_class/runs.jsonl. No negative excess found (P12 proves excess >= −o(k) under dissociation).
## E10 (2026-10-18) FINITE analog in Z_p (src/cyclo_finite.py): H = index-m subgroup of Z_p^* (−1 ∈ H), ratio on the
   p-grid only, R_p = (−min_{θ≠0} η(θ)/2)/sqrt(|H|/2). Best over primes p < 2e4 (m<=4) / 6e4 (m>=5):
   m=2 (Paley) 0.5035; m=3 0.4158 (p=18367); m=4 0.3684 (p=14177); m=5 0.3789; m=6 0.3129 (p=51637); m=8 0.3905;
   m=10 0.4402; m=12 0.5328 (medians 0.51–1.20). Theory: if all Gauss sums of order-m characters are ≈ +√p, the
   periods are ((m−1)√p, −√p, ..., −√p)/m and R_p -> 1/sqrt(2m) -> 0. So 1/2 is NOT a barrier for abelian Cayley graphs
   of prime order (no subgroups); C½, if true, depends on Z's continuity (goodness at ALL moduli simultaneously).
## E11 (2026-10-18) Z-lifts of the E10 finite winners and model sets (src/lift_tests.py; FFT estimates, UNCERTIFIED)
   Aligned cyclotomic classes lifted as integer sets A = H ∩ [1,(p−1)/2]: R on the circle = 12.5 (m=3,p=18367),
   11.1 (m=3,p=15259), 8.3 (m=4,p=14177), 14.6 (m=6,p=51637) vs 0.42/0.42/0.37/0.31 on the p-grid. Model sets
   {n <= X: ||nφ|| < w(n/X)/2}, φ golden, w ∈ {flat, linear, quadratic taper}, w0 ∈ {.3,.5,.7}: R = 1.3–2.6 (X=200),
   2.2–5.2 (X=800), 4.1–10.3 (X=3200), growing ~sqrt X (bumps of size X/m at x = 2πmφ). Both routes KILLED as stated.
## E12 (2026-10-18) Exhaustive Sidon (Golomb ruler) search, max c = min_x|F_D|^2/k (src/sidon_exhaustive.py; 64L grid)
   k=4, L<=20 (802 rulers): c = 0.0913 ({0,8,18,20}); k=5, L<=30 (12178): 0.1031 ({0,2,5,11,19}); k=6, L<=40 (132914):
   0.1206 ({0,9,12,19,23,25}); k=7, L<=50 (923614): 0.1156 ({0,6,10,13,18,38,39}). Threshold for R(D−D) < 1/2: 0.293.
   C½ for Sidon differences holds with margin in these boxes (R(D−D) >= 0.6755); SNZ (c -> 0) not decided by small k.
## E13 (2026-10-18) Fixed-size exact box MILP (src/box_minlam.py X n0 tl warm; highspy 1.x, mip_rel_gap 1e-6, cuts)
   X=40, n0=24: kOptimal after 875 s, K_[1,40](24) ∈ [2.826302 (dual), 2.826305 (feasible)], optimum = the agent's set
   [1,3..12,14..20,22,23,27,28,34,37], R = 0.57692. So no 24-subset of [1,40] has R < 0.5769 (HiGHS numerics, not
   interval-certified). X=45, n0=27: time limit 2400 s, best M = 3 (R = 1/√3, min at x = π), dual bound 2.4223 (gap open).
## E14 (2026-10-18) Small-N agent (src/smallN_search.py; C kernel; exhaustive DFS with certified pruning threshold)
   Exhaustive box optima, certified R (arb E2; PARI Sturm brackets for N <= 40): N=4..17 in [1,40..100]: 0.76→0.614;
   N=18 0.5980, 21 0.5931, 24 0.5769, 27 0.5774, 29 0.5767, 34 0.5741, 35 0.5677, **36 0.56481** ([1,52]; A = [1..11,
   13..23, 25..31, 34, 35, 37, 44, 45, 48, 50], max 50; lead re-certified: min f >= −3.3887702, Sturm M ∈
   [3.3887696, 3.3887699]), 37 0.5758, 40 0.5842. Edge-touching optima (max = L) at N=29,30,34,38–40. Fit over N=20–36:
   R ≈ 0.49 + 0.54/√N (finite-N only). SA for N=45–100: 0.612–0.665 (search-limited). Structure: tapered dense sets,
   E(A)/N^3 ≈ 0.5, not Sidon-difference sets. Data: examples/smallN_best.json, examples/smallN_runs/.
   ADDENDUM 2026-10-18 (laptop, src/localrun.sh, 1 core): N=41, box [1,57], complete in 1247 s (3.97e10 nodes): optimum
   A = [1..33, 38, 39, 43, 44, 46, 48, 52, 55], M_est = 3.675475, certified M <= 3.675636, R = 0.57404, x* = 1.0761,
   unique (second best M = 3.68887). Box optima N = 34..41: 0.5741, 0.5677, 0.5648, 0.5758, 0.5818, 0.5816, 0.5842, 0.5740
   (boxes L = 52, 52, 52, 52, 52, 54, 55, 57). The fit R ≈ 0.49 + 0.54/√N (N = 20–36) predicts 0.574 at N = 41 — matched;
   N = 38–40 sit above it but their optima touch the box edge (max A = L), so those boxes were too tight. Conclusion:
   N=42, box [1,58], complete in 1652 s (4.47e10 nodes): A = [1..17, 19..32, 34, 35, 36, 41, 42, 44, 47, 51, 55, 56, 58],
   certified M <= 3.752118, R = 0.57896 (fit: 0.5733); edge-touching (max A = L = 58). Rerun in [1,60]: SAME optimum,
   complete in 9619 s (3.02e11 nodes, no overflow) — so N = 42's value is not a box artefact and the fit 0.49 + 0.54/√N
   FAILS at N = 42 (0.579 vs 0.573). Box optima since the N = 36 minimum (0.5648) are all >= 0.574.
   UPDATE after the [1,60] rerun: the descending fit is contradicted at N = 42; the data now lean toward the anatomy
   prediction (ρ -> ρ*, c_E rising ⇒ dense optima rise past N ≈ 36), i.e. toward C½ in the dense regime (still finite-N
   evidence only, not a proof).
## E15 (2026-10-18) Sidon lower-flatness SA (src/sidon_flat_sa.py k L 60000 seed; 32L grid, UNCERTIFIED)
   best c = min|F_D|^2/k: k=8 0.019, 10 0.012, 12 0.0031, 16 0.00083, 20 0.00051 — far below the 0.293 needed for
   R(D−D) < 1/2 and below E12's exhaustive k <= 7 optima; supports SNZ. Data: examples/sidon_flat_sa.jsonl.
## E16 (2026-10-18) Doubly-positive profile problem (src/profile_opt.py; L-BFGS on w = h⋆h, h >= 0 or signed + penalty)
   sup ρ(w) = ∫w^2/(w(0)∫w) over w >= 0, ŵ >= 0: ρ* = 0.72388 (n = 200/800/1600 grid, all inits; signed class no better);
   triangle 2/3, Gaussian 1/√2. Optimal h ≈ a smooth arch (h ≈ 0, .25, .53, .77, .93, 1, .95, .80, .57, .30, 0).
   Dense heuristic R ≈ c_E sqrt((1−ρ)/2): ultraflat symmetric rounding (c_E = √2) gives R ≈ √(1−ρ*) = 0.5255 > 1/2.
## E17 (2026-10-18) Anatomy of the best dense sets (scratchpad dense_anat.py; Gaussian smoothing bw 3/5 of 1_A)
   N=24..40: main(x*) ∈ [−1.5, −0.4] (finite-size, non-p.d. at the O(1) level), E(x*) ≈ −(0.43–0.50)√N, c_E (far from 0)
   = 1.43–1.87 (above √2: rounding errors are NOT skewed), empirical ρ = 0.67–0.82 (exceeds ρ* only through finite-size
   non-p.d. tolerance ~1/√X). Prediction: dense optima rise toward >= 0.53 as N grows unless skewed rounding errors exist.
## E18 (2026-10-18) LNS with exact window MILPs (src/lns_milp.py X n0 steps seed start win=24; highspy; UNCERTIFIED objective)
   400 steps each: N=45 (X=70, from SA 0.6162) → 0.5948; N=50 (X=72) → 0.6051 (SA start), 0.6036 (scaled-36 start);
   N=60 (X=92, from 0.6308) → 0.6243; N=80 (X=115, scaled-36) → 0.6630. Sanity: N=36 box optimum is a fixed point.
   R increases with N beyond 36 in every method so far (consistent with E16/E17; not a proof). Data: examples/lns/.
   Certified (E2, arb): N=45 R <= 0.59476, N=50 0.60356, N=60 0.62427, N=80 0.66303 (examples/lns/certified.json).
## E19 (2026-10-18) Bu-class checks for P15/P16 (src/bu_halfsquare.py on F4; src/p16_constants.py)
   Identity f_{A(S)} = P^2 − k/2 − C/2 holds to 4e−8 on all certified Bu sets; E[C^4] = 3k^2/4 − 3k/8 EXACTLY (k=12..80);
   visit lemma: every window of the P16 size contains |P| < δ (100% of windows, η = .3, .5). Bu minima sit at near-zeros
   of P with C ≈ +2√k..2.7√k (excess = C/2 − P^2 ≈ 1.0–1.37√k; mean of C over zeros of P ≈ −0.1√k).
   E9 update (Bu-class SA, examples/bu_class/runs.jsonl): k=24 R=0.6829, k=32 0.6796, k=40 0.6787 (excess 0.83–1.08√k).
## E20 (2026-10-18) Singer sets: distribution of u = |F_D|^2/k on shifted grids x = 2π(j+θ)/v, j = 1..v−1 (exact sums)
   q=23/47/73 (k = 24/48/74): θ=0: var 0 (exactly flat, u = q/k); θ=0.1: var 0.06–0.08, min 0.04–0.32; θ=0.25: var
   0.34–0.42, P(u<0.29) ≈ 0.09–0.12; θ=0.5: var 0.82–0.90, min 1e−4..1e−3, P(u<0.29) = 0.26/0.21/0.25 (exponential law:
   var 1, 0.252). Every shifted grid has E u^2 = 2 − 1/k exactly (Sidon mod v). So SNZ-weak for Singer sets holds at ~1/4
   of the midpoints; a proof needs the half-shifted Hilbert transform H(l) = Σ_n G(l−n)/(n+1/2) of the Singer Gauss sums
   G(l) (|G| = √q) to be small for one l — e.g. from joint equidistribution of consecutive Gauss sums (Katz-type).
## E21 (2026-10-18) Skewness of the rounding error E = f_A − main (Gaussian-smoothed profile bw 4; bulk x > 8/X; inline
   script, 2^14 grid; random roundings = 200 Bernoulli(w) sets per profile)
   N:      24     29     34     35     36     40
   c_E:    1.45   1.43   1.63   1.73   1.77   1.79     (random roundings: median 2.50–2.59)
   skew:  +0.70  +1.18  +0.78  +0.55  +0.37  +0.19    (random: −0.05..+0.01, 5–95% within ±0.5)
   The exhaustive optima exploit positive skew (the only mechanism that can beat 1/2, E16), but the skew FADES and c_E
   RISES with N over 29–40; extrapolated, c_E stays above the 1.35 needed for R_∞ < 1/2. Small-N evidence only.

## E22 (2026-10-18) Complete-multipartite Bu sums (src/multipartite_bu.py; FFT grid >= 16 max A, UNCERTIFIED estimates)
S = Bu et al.'s certified Sidon sets (examples/bu_reproduction_certified.json); blocks of size b (consecutive in sorted S
or random); A = cross-block pair frequencies, f_A = P^2 − Σ_i P_i^2, N = k^2 − Σ|B_i|^2. M/k (R):
   k=40:  b=1 0.693 (0.701) | b=2 1.170/1.026 | b=4 2.04/1.60 | b=8 3.60/2.45 | b=20 7.74/4.59   (sorted/random)
   k=60:  b=1 0.671 (0.677) | b=2 1.113/0.953 | b=4 2.18/1.35 | b=8 4.16/2.10 | b=30 13.96/6.28
   k=80:  b=1 0.653 (0.657) | b=2 1.053/0.960 | b=4 2.08/1.39 | b=8 3.93/1.97 | b=40 14.97/5.44
Idealised (concentrated) prediction (k/2)/sqrt(N) = 0.503–0.707. Even b = 2 costs ≈ +0.35k: the within-block sum f_W
(k frequencies, not engineered) adds Gaussian extreme values at the zeros of P, whereas Bu's Singer/parity design
specifically keeps C small there. The one-positive-eigenvalue class beyond K_k is worse in practice. Killed as a
construction route.

## E24 (2026-10-18) One-sided skew for ±1 cosine polynomials (constant profile w = 1/2; src/signed_sa.py; UNCERTIFIED)
c := −min Σ_{n<=X} ε_n cos(nx) / sqrt(X/2) (= c_E of the constant profile). Single-flip SA, grid 8X, Newton polish:
   X:            50     100    200    400
   2e6 iters:   1.17   1.34   1.54   1.69     (two seeds, best)
   2e7 iters:    —     1.32   1.46   1.65
Baselines: Rudin–Shapiro c = 2.00 (|P| <= sqrt(2X)), Legendre/Fekete c ≈ 2.0–2.2 (two-valued ±√p on the grid, larger in
between), random ≈ sqrt(2 log X). Optimised sequences are strongly skewed at small X (c < sqrt2 = arcsine value) but c
RISES with X (also with 10x more search), crossing the 1.33 needed by the dense heuristic near X ≈ 100. Same pattern as
E21 (skew of the exhaustive 0/1 optima fades with N). Mechanism probe only: says nothing rigorous about the limit.

## E25 (2026-10-18) Bu's identity on FULL Singer sets, best cyclic shift (src/singer_bu.py; certificates C-SB below)
S = shifted, centred Singer set (k = q+1, L ≈ k^2/2, no thinning, no parity block); shift = best of ~40–60 by FFT grid;
chosen set certified by arb ball arithmetic (chowla.certify_lower_bound, oversample 16):
   q:        13     23     31     43     61      101     151     199     251     307      401
   N:       182    552    992   1892   3782   10302   22952   39800   63252   94556   161202
   R (est): .673   .644   .635   .618   .604    .588    .576    .565    .561    .5567    .5536
   R_cert:   —      —      —      —    .60406  .58874  .57770  .56630  .56272  .55670   .55366  (q=307,401: oversample 32)
   (q = 307, 401: laptop, src/localrun.sh, blocked certifier, 115 s / 133 s, peak RSS < 1 GB.) Better fit than 0.95/√k:
   (R − 1/2)·√(k/log k) = 0.403, 0.417, 0.427, 0.407, 0.423, 0.416, 0.439 (est) for k = 62..402 — consistent with Bu et
   al.'s O(n^{1/4}√log n) error (max of the C-fluctuation over ≍ L zeros of P).
Better at every size than Bu et al.'s random tent-thinned sets (E4: 0.6573 at N = 6320; their paper: 0.635 at 25440,
uncertified). Excess fits R − 1/2 ≈ 0.95/√k (i.e. M ≈ k/2 + 0.95√k: the C-fluctuation at the zeros of P), so R -> 1/2
from above like N^{-1/4}, as P16 (kernel-checked) and the heuristic predict. q = 251 gives the best certified finite R
known to us (0.56272 at N = 63252), narrowly beating the dense N = 36 optimum (0.56481). Not a step toward R -> 0.
E24 addendum — exact optima for X <= 22 (all 2^X sign patterns, grid 16X on [0, π], top-20 Newton-polished):
   X:   8      10     12     14     16     18     20     22
   c*: 1.032  1.157  1.104  1.126  1.060  1.103  1.057  1.094
Optima are Dirichlet-like (e.g. X = 14: all + except ε_13; X = 20: alternating = Dirichlet at π), whose c = 0.307√X
still fits under 1.33 at X <= 18. So small-X values say nothing about skew; E24's SA values at X >= 50 are the
relevant probe.

## E26 (2026-10-18) Free-phase analogue: min over θ of max_t Σ_{j<=n} cos(jt − θ_j) (src/freephase_opt.py; UNCERTIFIED)
Adam on a soft-max (grid 16n), true max by FFT 64n + Newton; c := max/sqrt(n/2):
   n = 25: 0.899 | 50: 0.894–0.895 | 100: 0.908–0.909 | 200: 0.902      (grid values ≈ 0.866–0.87 throughout)
So with FREE phases (unit moduli, full support) the one-sided ratio is ≈ 0.9 and flat in n — far below the 1.33 a dense
0/1 rounding would need, and below the arcsine value √2; whereas with real ±1 coefficients (E24) the optimised ratio
rises past 1.33 by X ≈ 100. The phase restriction to {0, π} (real two-valued coefficients) is what destroys the skew.
Side remark: consistent with max T ≍ √n for free phases (Erdélyi's claimed n^{1/3}/60 would be far from sharp).
E24b — second optimiser (src/signed_homotopy.py: a = tanh(κu), κ ↑, Adam on soft-min, round + single-flip polish),
best of 3–5 seeds: X = 50: 1.43 | 100: 1.47 | 200: 1.40–1.47 | 400: 1.51 | 800: 1.58. Worse than SA at small X,
slightly better at X >= 200; both optimisers put the achievable ±1 ratio at ≈ 1.45–1.6 for X in [200, 800], slowly rising.
(Caveat: the ±1 problem is the constant profile, ρ = 1/2, for which beating 1/2 would need c_E < 1 — even stricter.)
E25 addendum: scanning 600 shifts with 8x FFT grids picked shifts whose CERTIFIED R was worse (q=199: est 0.5625 →
cert 0.56642; q=251: est 0.5600 → cert 0.56529) than the 60-shift picks (cert 0.56630, 0.56272): 8x grids misrank by
~0.004. src/singer_bu.py now re-ranks the top 8 shifts with 16x grids + Newton before certifying (q=31: cert 0.63240).
E25b — re-signing the diagonal: SA over S' ⊂ S for A(S) ∪ {|6s+1| : s ∈ S'} (valid: no collisions, by Sidon) on the q = 101
Singer–Bu set: best grid R 0.58806 → 0.58760 using one added frequency; certified 0.5924 (worse than the base 0.58874;
8x grid misranking). The diagonal can be re-signed (f = P^2 − k/2 − ½Σσ_s cos((6s+1)x)) but no sign pattern helps,
matching the heuristic E[D_σ | P = 0] ≈ −(1/4k)Σσ_s, far smaller than the √k fluctuations at the zeros of P.

## E27 (2026-10-18) Structured exact MILP at N = 45 (src/box_core_milp.py 62 45 34 3 5400 4, on F4; examples/milp/)
Restricted box: A ⊂ [1, 62], |A| = 45, core [1, 34] with <= 3 holes. HiGHS hit the 5400 s limit in round 0: incumbent
lam = 3.80706 on the cut set, true M = 3.83604, dual bound 3.128 (so the restricted optimum is NOT certified optimal).
A = [1..13, 15..35, 37, 39, 40, 41, 45, 50, 52, 57, 58, 60, 61] (holes in [1,61]: 14, 36, 38, 42–44, 46–49, 51, 53–56, 59),
x* = 2.4548. Certified (C-N45): **R <= 0.571844**. Previous N = 45 bests: LNS 0.5948, SA 0.6162.
Anatomy (Gaussian-smoothed profile, bw 4; bulk x > 8/X; same code for all three): N=36: c_E 1.62, skew +0.38, ρ 0.81 |
N=40: c_E 1.75, skew +0.25, ρ 0.83 | N=45: c_E 1.79, skew +0.55, ρ 0.83. Box records over N = 36..45 stay in
0.565–0.584 (no monotone trend); the low R values are carried by ρ ≈ 0.83 > ρ* = 0.72 — a non-positive-definite profile
that finite size tolerates — while c_E creeps up (1.62 → 1.79). Holding c_E ≈ 1.8 with a p.d. profile would give
R_∞ ≈ 1.8·sqrt((1−ρ*)/2) ≈ 0.67. Still no evidence for a dense route below 1/2.

E27 addendum (2026-10-18, laptop, src/localrun.sh, 3 HiGHS threads): N = 50, X = 70, Y = 38, H = 3, warm start = SA best
(R 0.612), 5400 s time limit: incumbent M = 4.130782, dual bound 2.964 (gap large — search-limited, NOT optimal).
A = [1..26, 28..34, 36..39, 41, 45, 46, 48..52, 56, 58, 62, 67, 70], arb certificate (oversample 64): min f >= −4.1307824,
R(50) <= 0.584181 (examples/milp/N50_best.json). The fit 0.49 + 0.54/√N predicts 0.566 — not tested (search-limited).
Structural remark: the tail must cancel the core's Dirichlet lobe (≈ 0.217Y), so it holds ≈ 0.2Y elements (8 at N = 41):
linear, not √N; at large N the optimum must approach a p.d. macroscopic profile, so small-N fits do not extrapolate.

## E28 (2026-10-18) P18 dense min–max lemma on the records — UNINFORMATIVE (src/p18_test.py)
Profiles W = w0·(Fejér K_Y or tent autocorrelation), Y <= X+1 (genuinely p.d., degree <= X), w0 ∈ [0.3, 2.5]; Λ = max|f − Ŵ|
on a 64X grid (uncertified). Best bound B = Σn²e²/(2X²Λ) − w0/2 over the grid is <= 0.03 for every record (box N=20..55,
MILP N=45, Singer–Bu q=61,101) versus M = 2.7–60. Two reasons, both structural: (i) a p.d. degree-X profile has
ΣW <= X·W_0/2, so absorbing the spike f(0) = N needs W_0 >= 2N/X ≈ 1.4 for the dense records (N/X ≈ 0.7), and the
correction W_0/2 then exceeds the main term; with W_0 <= 1 the residual keeps the spike (Λ ≈ 0.2X). (ii) the chain
||G'||_2² <= ||G'||_∞||G'||_1 loses a factor ≈ 10 even for flat residuals. Decision: P18 stays a qualitative lemma (a
√(N/log N)-type statement for flat residuals); not a probe of finite records. Dense line continues via E16/E21 anatomy.

## E29 (2026-10-18) Erdős–Turán quadratic Sidon sets are not lower-flat — KILLED (src/et_flat.py; 64L FFT, UNCERTIFIED)
B = {2pj + ((a j² + ℓ j) mod p) : 0 <= j < p}, a < min(p,12), ℓ ∈ {0,1} (all Sidon; checked for a = 1, ℓ = 0). Motivation:
Gauss-sum flatness |F_B(2πa/p)|² = p. Result: max over twists of c = min|F_B|²/k = 0.0029 (p=5), 0.0009 (13), 1e-4 (23),
< 1e-4 for p = 37..223. Far below the 0.293 needed for R(D(B)) < 1/2. Flatness at one lattice of roots of unity
does not survive interpolation (same failure as Singer, E8/E11).

## E30 (2026-10-18) Run-tops in finite abelian groups (src/group_runtop_sa.py; SA on pair toggles, float K; laptop)
Frontier max|B_t| subject to K <= K0 (t = e_1), 200k iterations, seed 1, K0 ∈ {2,3,4,6,8,12,16}; best |B_t|/K0²:
   Z7^3 0.389 (K0=12: |B_t| = 56), Z5^4 0.333, Z9^3 0.500 (K0 = 2), Z3^6 0.500 (K0=2; 0.137 at K0 = 16), Z3^7 0.500 (K0 = 2),
   Z243 0.472 (K0=12: 68), Z729 0.333, Z2187 <= 0.125 (partial). Never above 1/2. The SA is visibly search-limited in the
   larger groups (it finds LESS in Z3^7 / Z2187 than in smaller groups), so these are lower bounds on the frontier only.
   Benchmarks: Paley/QR sets in F_p (p ≡ 1 mod 4): K = (1+√p)/2, |B_t| ≈ p/8 ⇒ |B_t|/K² -> 1/2; index-m cyclotomic classes
   give ≈ (m−1)/(m³c_m²) (≈ 0.17 for m = 3) — Paley is the best known group example. No |B_t| >> K² found.
   Paley-seeded ratio search (mode `ratio paley`, 1e5 SA steps maximising |B_t|/K² directly): p = 401: Paley K = 10.512,
   |B_t| = 51, ratio 0.4615 — SA finds nothing better; p = 1009: K = 16.382, |B_t| = 123, ratio 0.4583 — nothing better.
   Paley is a local maximum under pair toggles; its ratio -> 1/2 from below. Suggests C = 1/2 might be the group
   constant in Conjecture G (weak evidence).
   CORRECTION 2026-10-18: "never above 1/2" was a search limit. Quadric level sets give ratio exactly 1 and 2, and P20
   Theorem 1 gives |B_t| = K²(K−1) (unbounded ratio). SA started from Theorem 1 stays there; from scratch it never finds
   it (isolated local maxima). Conjecture G is REFUTED (E31, P20).

## E31 (2026-10-18) Lead's independent check of the Conjecture G counterexample (src/e31_quadric_check.py; laptop,
## localrun.sh -m 2; numpy FFT over all p^4 characters, values integral to 1e-6 and rounded: NUMERICAL-EXACT)
A = {x ∈ F_p^4 : x1x2 + x3² − d·x4² ≠ 0}, d the least non-residue (elliptic quadric complement), t = e1 (isotropic).
Built independently of the agent's field-trace construction. Checks: A = −A, 0 ∉ A, F real, all values integers.
   p  |A|    K   F-spectrum            |B_t|   p²(p−1)   |B_t|/K²
   3  60     3   {−3, 6, |A|}          18      18        2
   5  520    5   {−5, 20, |A|}         100     100       4
   7  2100   7   {−7, 42, |A|}         294     294       6
   11 13420  11  {−11, 110, |A|}       1210    1210      10
   13 26520  13  {−13, 156, |A|}       2028    2028      12
Confirms |B_t| = K²(K−1) in rank 4 for every tested p (P20 Theorem 1, a = 1). Runtime < 10 s.

## E32 (2026-10-18) Exhaustive Stab(t)-invariant sets in F_p^n, no-full filter (src/e32_invariant_nofull.py; laptop)
All symmetric unions of Witt classes C(q,b) = {x ∉ span t : Q(x) = q, B(x,t) = b} plus points of span(t) (2^7 sets for p = 3).
p = 3, n = 4..8, Q ∈ {Σx_i², Σx_i² with last coefficient 2}, t ∈ {e1, e_n, e1+e2+e3}: best |B_t|/K² over ALL invariant
sets = 2 exactly (isotropic t, n even: P20 Thm 1 / quadric complements, K = 3, 9, 27 at n = 4, 6, 8) or 1; over NO-FULL
invariant sets = 1 exactly (anisotropic quadric level sets, K = 3^{n/2−1}). Odd n: <= 1 at K = 1 only. Log:
examples/group_runtop/e32_batch.log (p = 5 rows there failed an integrality assert — values lie in Q(ζ_5)^+; fixed,
re-run in e32_p5.log). p = 5, n = 4..6 (2^17 sets each): ALL invariant sets reach 2.6 (anisotropic t, n = 4, K = 5, B = 65),
2.92 (n = 6, K = 25, B = 1825), 4 = p − 1 (elliptic isotropic t: P20 Thm 1, K = 5 and 25), 1.64 (n = 5, isotropic, K = 17.47);
NO-FULL invariant sets: max ratio 1 in every case (only K = 1, |B_t| = 1 attains it). Reading: within the orthogonally invariant class, forbidding full cosets kills the ratio-2
mechanism — but the class is too small: P21 (non-invariant τ2 on the subspace x2 = 0) gives unbounded ratio with no
full cosets.

## E33 (2026-10-18) All-(p−1)-point fibres in F_p^4 (src/e33_alld_nofull.py; FFT over all p^4 characters, float)
A = {x2 ≠ 0, x1x2 + N(x3,x4) ≠ 0} ∪ {x2 = 0, x1 ≠ τ2(x3,x4)}, t = e1. With τ2 = x3x4² (mode x3x4sq):
   p    3   5    7    11    13    17    19    23
   K    9   15   21   33    39    51    57    69      (= 3p exactly)
   |B_t| = p³ exactly; t-lines all have p − 1 points; |B_t|/K³ = 1/27; |B_t|/K² = p/9.
Best random homogeneous cubic τ2 (300 trials) lowers K slightly: p = 5: 13.09, 7: 20.89, 11: 30.65, 13: 38.92,
17: 48.61, 19: 56.99 (K = p + max ĝ exactly in every case). Confirms P21; refutes G_noFull.
