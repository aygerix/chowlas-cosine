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
   N=43, box [1,60] (src/exh2.c via exh2_driver.py on dirichlet, 4 threads; certified pruning threshold 4.168221):
   COMPLETE in 7647 s (2.44e11 nodes, 36895 survivors). Optimum
   A = [1..14, 16..34, 38, 41, 43, 44, 47, 50, 51, 52, 55, 57] (max 57 < L, so not edge-touching).
   Its value: M = 3.796328 (Newton estimate), arb certificate M <= 3.796574, so R(43) <= 0.578972.
   Second best M = 3.796371: almost tied, equiripple. Data: examples/smallN_runs/exh2_43_60.out.
   Exact box optima N = 41, 42, 43: 0.5740, 0.5790, 0.5789.
   Structured-class optima (E42, exact only inside their class, not full boxes): N = 45 0.5718, 50 0.5701, 55 <= 0.5671.
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

## E34 (2026-10-18) One t-run per residue class in Z (src/e34_onerun.py; FFT + Newton, UNCERTIFIED) — UNINFORMATIVE
A = {y + tk : 0 <= y < t, τ(y) < k <= τ(y) + ℓ}, |A| = ℓt, t ∈ {31, 101, 307}, ℓ ∈ {2,3,4,8}, τ ∈ {0, random, c·y,
c·y², c/y mod t} (12 choices each). Best R: 1.9–4.4 (t = 31), 3.0–7.0 (t = 101), 4.0–10 (t = 307); τ = 0 and linear τ
give intervals/GAPs (R ≈ 0.22√n). Every family is dominated by the macroscopic Gibbs lobe of the run-start set S
(uniform on [0, t²] with a sharp cutoff: M ≈ 0.22·|A|·const), so the experiment does not test the run mechanism of
Lemma OR at all. A meaningful test needs S with a tapered positive-definite profile and algebraic (not random) fine
structure. Kept as a failed probe.

## E35 (2026-10-18) λ-fold ruler search (src/lambda_ruler_sa.c, src/e35_batch.sh, src/e35_eval.py; GCP VM dirichlet)
SA (5e7 single-point moves × 4 restarts, seed 1) maximising φ = share of pairs of D ⊂ [0,L] (|D| = k, endpoints 0, L)
whose difference has multiplicity exactly λ; grid λ ∈ {2,3,4}, k ∈ {8,…,30}, L = (k²/(2λ))·{1, 1.5, 2.5, 4}.
HEURISTIC (search lower bounds on the best φ). Data: examples/lambda_ruler/e35_grid.txt.
   λ = 2 (validation): best φ = 1 − 1/(k−1) EXACTLY for k = 8…21 (Bu-type coherent structure found); 0.935/0.938 at
         k = 24/30 (optimum 0.957/0.966: slightly search-limited).
   λ = 3: best φ = 0.75 (k=8), 0.80 (10), 0.77 (12), 0.77 (15), 0.69 (18), 0.67 (21), 0.62 (24), 0.57 (30) — DECREASING.
   λ = 4: 0.71, 0.71, 0.79, 0.72, 0.65, 0.67, 0.59, 0.52 (k = 8…30) — decreasing.
Actual R(A) (A = multiplicity-λ differences; FFT + Newton, uncertified): λ = 2 candidates 0.71–1.03, λ = 3: 0.68–1.96,
λ = 4: 0.71–2.33 — none near 1/2. The defect sum E (weight W ≈ k–14k) peaks where |F_D|² is small, so the naive
R ≈ 1/√(2λφ) badly underestimates. CORRECTION (2026-10-18 night, E39 / agent lambda): the SA was search-limited. Exact optima give φ = 0.818 at k = 12
(SA 0.773), and tabu gives φ ≈ 0.835 at k = 30 (SA 0.57). "φ decreases with k" is an ARTEFACT; the true best φ for
λ = 3 is about 0.8, flat in k, with W/k growing. The conclusion "no route to R < 1/2" stands (every candidate R >= 0.68).
Original reading, kept for the record: no coherent multiplicity-3 or -4 structure appears (φ decays toward the
generic level), while λ = 2 structure is found immediately — consistent with P4 (symmetry gives at most 2). Not a
proof; candidates beyond SA reach: homometric triples (NOTEBOOK evening entry). Runtime ≈ 12 min on 4 vCPUs.

## E36 (2026-10-18) Independent check of Theorem O4 (src/e36_o4_check.py, src/e36b_o4_avg.py; GCP VM dirichlet)
Lead's own implementation, independent of the agent's code: GR(4,a) = Z_4[x]/(f) with f the NAIVE 0/1 lift of an
F_2-irreducible (x³+x+1, x⁵+x²+1, x⁷+x+1, x⁹+x⁴+1; any monic lift of an irreducible gives a Galois ring), Teichmüller set
by brute force {z : z^{2^a} = z}, characters via the DOT-PRODUCT pairing on Z_4^a (not the trace form), W̄ = {u_0 = 0},
spectrum by numpy FFT over Z_4^{1+a} (integrality asserted), run-tops counted directly; RDS property checked exhaustively.
   a   |A|     K    |B_t|   K⁴/4 − K²/2   spectrum (value: multiplicity)
   3   124     4    56      56            −4:167, 0:64, 12:8, 28:16
   5   2044    8    992     992           −8:1984, −4:991, 0:1024, 60:32, 248:64
   7   32764   16   16256   16256         −16:32512, −4:16255, 0:16384, 252:128, 2032:256
Identical to the agent's table (different lift/pairing). E36b, A-averaged run-tops: avg_{t∈A}|B_t| = 30.97 / 511 / 8191
(K⁴/8 = 32 / 512 / 8192); distribution in PROOFS P22. Runtime < 1 min.

## E37 (2026-10-18 night) Exact ILP max |B_t| in cyclic / coprime / higher-rank groups (src/group_bt_ilp.py from agent g3;
## src/e37_batch.sh, e37b, e37c; HiGHS, 900 s per instance; data examples/cyclic_ilp/*.jsonl)
NUMERICAL-EXACT where "opt" (solver-certified optimum); otherwise a lower bound (best found) with the dual bound.
   K0 = 3, ord t = 3:  F_3^4 18 (agent, opt) | Z_9² 6 opt | Z_3×Z_27 5 opt (t ∈ Z_3), 6 opt (t = (0,9)) | Z_81: 3 / 4 / 5 opt
                       for t of order 3 / 9 / 81 | Z_3×F_2^5 6 opt | Z_3×F_5² 4 opt | Z_3×Z_25 4 opt | Z_3×Z_4²×Z_2 12 opt
                       (A ⊂ Z_3×Z_4²: full cosets on {y1+y2 ≡ 0}, 2-point cosets elsewhere; Lemma-3 type, coprime H) |
                       Z_243 >=3 (bound 81) | Z_240 >=3 | Z_231 >=6 | Z_3×Z_81 >=5 | Z_3×Z_32 >=6 (bound 19) | Z_3×Z_7² >=6.
   K0 = 4:             Z_64: 11 opt (t of order 4), 14 opt (t = 1) | Z_4³ 16 opt | Z_8²: 15 opt (both t) | Z_125 (t = 25) >=5.
Reading (NOTEBOOK night entry, corrected): only the elementary abelian F_3^4 (bent mechanism) stands out; cyclic Z_81 is
the most restrictive; coprimality alone does not keep |B_t| small (Z_3×Z_4² gives 12). At K <= 4 exponents cannot be
read off. e37b (rank dependence at order 243, K0 = 3, all hit 900 s, dual bounds 77–81, so lower bounds only):
   Z_9×Z_27 >=6 | Z_3²×Z_27 >=6 | Z_3×Z_9² >=6 | Z_3³×Z_9 >=18 (3-rank 4: contains the F_3^4 bent configuration).
   Primal values track the 3-rank (rank <= 3: 3–6; rank 4: 18), consistent with the reading above; not certified.
   e37 final instances (900 s; 'opt' = solver-certified, else best found with dual bound):
   - K0 = 4: F_5³ 25 opt | Z_4^4 (t = e1) >=55 (bound 62), consistent with Theorem O4's exact 56 at a = 3
     (Z_4 × GR(4,3) ≅ Z_4^4) | Z_256: >=7 (t = 64), >=4 (t = 1) | Z_125 (t = 1) >=4 (bound 39) | Z_121 (t = 11) >=4 |
     Z_105 (t = 1) >=13 (bound 30).
   - K0 = 3: Z_105 (t = 35) >=4.
   Order 256 at K0 = 4: rank 4 (Z_4^4) >= 55 against cyclic >= 7. Cyclic groups stay the most restrictive throughout.

## E38 (2026-10-18 night) The O4-shaped class in Z: A = S ∪ (S+t) vs unrestricted sets (src/pair_sa.c, src/e38_batch.sh;
## data examples/pair_sa/e38.txt) — HEURISTIC (SA, grid minimum over 4096 points of [0,π], seed 1, 3e6 moves × 4 restarts)
Same N, same span, same search effort; "free" = unrestricted subsets of [1, span].
   N = 36 (span 50):   pair best 0.655 (t = 2; 0.66–0.68 for t <= span/8; 0.99 at t = 25)  | free 0.611 (exhaustive truth 0.5648)
   N = 60 (span 85):   pair best 0.693 (t = 3; 0.69–0.70 for t <= span/4; 1.23 at t = 42) | free 0.649
   N = 100 (span 150): pair best 0.732 (t = 18; 0.73–0.77 for t <= span/4; 1.46 at t = 75) | free 0.657
   (span 170 for N = 60: both modes search-limited, pair 0.76–0.96, free 0.83.)
Reading: under equal search effort, forcing every t-run to be a 2-run costs 0.04–0.08 in R, and the gap grows with N
(0.044, 0.044, 0.075). This is the opposite of the group picture (O4: this shape is EXTREMAL in Z_4 × GR(4,a)), and
it is mild evidence for Lemma OR(2) (Chowla for the O4-shaped class in Z). Not a proof; the SA is search-limited.

## E39 (2026-10-18 night) Lead's independent check of the λ-ruler exact optima (src/e39_lam_exact.c, src/e39_batch.sh,
## src/e39_R.py; GCP VM dirichlet; data examples/lambda_verify/)
Plain DFS over D ⊂ [0, L] with 0, L ∈ D (span exactly L), incremental r(d), prune only on over-full weight Σ_{r>λ} r,
reflection broken by x₁ <= L − x_{k−2}. Independent of the agent's bb_lambda.c, whose bounds are stronger.
   λ = 3:  k = 6: min def 3 (L <= 40) | 7: 6 (L <= 40) | 8: 7 (L <= 40) | 9: 9 (L <= 36) | 10: 9 (L <= 30) | 11: 10 (L <= 30)
   — identical to the agent's table for every k (same argmin spans where the ranges overlap).
The agent's best set D = {0,2,4,5,10,11,13,14,18,24}: |A| = 12, def = 9, M = 2.35706, R = 0.6804 (grid 4e5 + golden-section
refinement, uncertified; agent 0.680). T2 parity count checked on 5 random reflection-symmetric sets.
## E40 (2026-10-18 late night) Branch-2 dichotomy test on transversal 2-run sets A = S ∪ (S+t), s_y = y + t·k_y
## (src/e40_transversal.py; dense FFT grid on [0, 2π) + golden-section refinement: UNCERTIFIED; rng seed 12345)
Columns: level range L, M, R = M/sqrt(2t), M/sqrt t, M·L/t, fraction of pairs (y1,y2) with |defect| <= 1.
   t = 1024:  constant 445.5 (M/t 0.435) | linear k = ⌊2y/√t⌋ (L = 64) 446.5 | quadratic ⌊y²/t⌋ (L = 1023) 1292 |
              random uniform levels L = 4 / 32 / 128: 744 / 498 / 447 | random tapered (min of two uniforms)
              L = 4 / 32 / 124: 385 / 161 / 198 (M/√t = 12.0 / 5.0 / 6.2) | Z_4 digit quadratic (O4-like) 582.
   t = 64, 256 behave the same way (table in the run log reproduced by the script).
Reading:
   - Uniform level profiles give M ≈ 0.44·t regardless of L. That is the Gibbs lobe of the flat macroscopic profile
     (density 1/L on [0, tL)), so the heuristic "case (a): M >~ t/L" is only a lower bound that the best (tapered)
     profiles approach. Tapered random levels drop to the fluctuation scale M ≈ 5–6·√t.
   - The O4-like Z_4 quadratic levels have nothing special in Z: M grows linearly in t (L = 4, sharp profile).
   - The small-defect fraction is high only for AP-like (linear, constant) levels, which all have M ~ t.
     Large-L random levels have small-defect fraction 1–7% and M ~ 5√t: consistent with dichotomy case (b).
## E41 (2026-10-18 late night) Dense finite model: exact min M_p over symmetric half-sets of Z_p (Sanders' question)
## (src/zp_half.c exact branch and bound, multiplicative symmetry broken by 1 ∈ P; src/zp_sa.c heuristic; dirichlet)
Objective: P = k pairs {a,−a} ⊂ Z_p^*, k = (p−1)/4 or (p+1)/4, M_p = max_{γ≠0} −2Σ_{a∈P}cos(2πaγ/p). Grid-R in Z
normalization: M_p/(2√k) ≈ M_p/√p. Paley (quadratic residues, p ≡ 1 mod 4): (1+√p)/2.
NUMERICAL-EXACT (double precision; the minimizing P is unique in every case, the reported value is 1e−9 accurate):
   p:      11    13    17    19    23    29    31    37    41    43    47    53    59    61    67    71    73    79    83    89
   M_p/√p .723  .639  .621  .584  .636  .593  .614  .554  .562  .546  .519  .543  .541  .523  .508  .493  .508  .491  .483  .491
   - The optima are Paley for p = 13, 17, 29.
   - From p = 37 on they are dilates of near-intervals with a tail, the anatomy of the dense Z optima.
     For example p = 79: P = [1,16] ∪ {18,19,25,27} after dilation by 16.
   - Spectrum: one giant profile coefficient (≈ 0.27p) and a nearly flat negative floor at the minimum.
   - The optima are below Paley for p >= 37 and below grid-R 1/2 for p = 71, 79, 83, 89.
   - p = 89: M_p = 4.630071582 after 3.3e10 nodes (examples/zp_half/e41_mid.txt).
HEURISTIC (zp_sa.c; calibrated: it reproduces the exact optima at p = 47, 53, 79):
   - Unrestricted SA is sub-Paley at p = 101 (0.516) and worse than Paley from p = 149 (search-limited).
   - Core-plus-tail SA (pairs 1..L forced; E41c) gives p = 149: 0.4825, 197: 0.523, 293: 0.528 (≈ Paley 0.529),
     401: 0.541, 601: 0.577, 797: 0.578. Search-limited from about p = 300, so the large-p trend is undetermined.
Reading: in Z_p the profile is constrained only at the critically sampled frequencies γ ∈ Z_p, so near-interval
profiles with tuned tails beat Paley at small p. This is the Z_p version of the loose positive-definiteness tolerance
that makes dense Z optima good at small N. Whether min M_p/√p -> 0 (towards Sanders' p^{1/3}) or levels off is the
same open question as the dense Z regime.

## E42 (2026-10-18 night) Structured-class branch and bound C(X,N,Y,h) — construct agent (interim) + lead certification
Class C(X,N,Y,h) = {A ⊂ [1,X]: |A| = N, at most h holes in the core [1,Y], free tail in (Y,X]}.
Code: .research/agents/construct_scratch/coretail_omp.c (OpenMP, one shared threshold).
Method:
- complete DFS over tails with the valid grid prune g_S(x_j) + U_j(k,i) < −thr (grid values are true values of f);
- leaves are Newton-polished, so the result is NUMERICAL-EXACT class optimum, not interval-certified.
Calibration: recovers the exhaustive optima N = 36, 41, 42 in 2–13 s (full exhaustive: hours).
Results (dirichlet, 4 threads):
- N = 45: class optimum R = 0.5718436 (X = 64, Y ∈ {36, 38}, h = 3). This is the E27/C-N45 set.
- N = 50, X = 71, Y = 40, h = 3: COMPLETE, class optimum M = 4.0483107, R = 0.5725176 (3.2e10 nodes, 975 s).
- N = 50, X = 72, Y = 38, h = 2: interrupted by a session restart after finding M = 4.0309356, R = 0.5700604
  (holes {27}). Rerun 2026-10-18 night: COMPLETE, class optimum M = 4.0309356, R = 0.5700604 (1.6e10 nodes, 619 s,
  runs/ct/o50y38x72.txt). The partial pre-restart log is runs/ct/o50y38x72_partial_interrupted.txt.
- N = 55 classes C(79/81, 55, 42/44, 2) queued (batch_n55.sh).
Certification by the lead (.research/agents/construct_scratch/cert_n50.py; examples/construct/N50_certified.json).
Both sets are certified by E2 (arb DFT + Taylor, oversample 64) AND E3 (PARI 2.15.4 Sturm):
- max 72: M ∈ [4.0309354, 4.0309358], **R(50) <= 0.5700604**.
- max 68: M ∈ [4.0483104, 4.0483108], R(50) <= 0.5725176.
Both replace the E27 addendum's 0.584181. A, the minimizer and its ripple are in the json.
Reading: the dense records N = 36, 45, 50 are 0.5648, 0.5718, 0.5701. That is flat at ≈ 0.57: no downward trend, and
nowhere near 1/2. Single-swap tabu is inadequate in this regime (N = 36 optimum: 7 dips within 0.08; basin test fails
2 of 4 runs).

## E43 (2026-10-18 night) Gurobi 13.0.3 ports: validation (pip gurobipy, size-limited licence <= 2000 rows/cols)
src/grb_dense.py is the box problem (min M over A ⊂ [1,X], |A| = n0, optional core/holes):
- Gurobi binary model with LAZY cuts in a MIPSOL callback at the true minimiser and at the grid local minima;
- initial cuts on the grid πj/(4X).
src/grb_group_bt.py is the E37 model (max |B_t|), unchanged logic, with an optional cutoff.
Validation, X = 40, n0 = 24 (E13 exact value M = 2.826302–2.826305):
- Gurobi, cold, 2 threads, dirichlet oversubscribed (~10 threads on 8 vCPUs): OPTIMAL in 1116 s, 2.26e6 nodes,
  249 lazy cuts, bound = obj = 2.8263048. The set is E13's [1,3..12,14..20,22,23,27,28,34,37]; found at t = 97 s.
- So the model is correct, but there is NO speedup over HiGHS on this instance (E13: 875 s, conditions not recorded).
- Fair comparison, 2 threads each, same load:
  - Gurobi WARM (optimum given as start): OPTIMAL in 219 s (1.02e6 nodes), i.e. ~4x faster than E13's 875 s.
  - HiGHS COLD (box_minlam.py): round 0 alone took 1309 s, slower than Gurobi cold (1116 s total). Its final time is
    still running.
  - Reading: ~4x, not the 10–100x hoped for, on this weak-LP model.
- N = 55 class C(79,55,42,2) (still running): incumbent M = 4.2053961, R = 0.5670555 (holes {24}; uncertified).
Note: the LP relaxation of this model is weak by nature. A fractional tapered profile with a positive-definite cosine
transform makes lam ≈ 0, so the proof is all branching. Expect no miracle on the full-box dense problem; Gurobi's value
is in structured or warm-started instances.

## E44 (2026-10-18 late night) Gurobi full-box dense optima (src/e44_grb_dense.sh → src/grb_dense.py)
User directive (2026-10-18): Gurobi replaces the C/HiGHS dense searches from now on.
- Licence: the user installed it at /opt/gurobi1303/gurobi.lic (LicenseID 2655336). dirun.sh passes it as
  GRB_LICENSE_FILE. gurobipy now solves a 3000-variable model, so the size limit is gone.
- Stopped:
  - the C class search C(79,55,42,2), with incumbent M = 4.2053961, R = 0.5670555, uncertified
    (warm start: examples/gurobi/warm_N55.json);
  - the HiGHS cold comparison at X = 40.
- Queue: N = 45 in [1,64], N = 50 in [1,72], N = 55 in [1,79]; 5 threads, 4 h each, warm starts from the best sets.
  Output: examples/gurobi/e44.jsonl, with progress lines every 5 min, and dense_N*_X*.json.
- E37g: the Z_4^4 instance crashed (Bus error) at 22:28, when the licence/library files were installed. RERUN NEEDED.
- VM stop for a resize attempt killed all runs. c2d-standard-56 failed: global CPUS_ALL_REGIONS quota is 16.
- A/B test, X = 40, n0 = 24, cold, 4 threads each, concurrent:
  - OLD (grid 4X, lazy cuts only): OPTIMAL in 639 s, 2.86e6 nodes.
  - NEW (grid 8X plus MIPNODE user cuts at fractional minima): bound 2.53 at 600 s with 0.70e6 nodes, killed.
  - The Python node callback cuts node throughput ~4x, and the tighter node LPs do not pay for it. Defaults reverted
    to OLD.
- Relaunched 2026-10-18 ~23:50 UTC: e44 dense (6 threads); e37g group batch without cutoff hints (2 threads).
  The other instances continue.

## E45 (2026-10-19) How much of M does the P28 bound recover? (src/p28_test.py on dirichlet; UNCERTIFIED quadrature)
B = max over H ∈ {X/64, …, X} of (1/4π)∫ sup_m |Σ_a F̂_H(a − m)e^{iax}| dx, with window centres on a grid of spacing H/4.
   set                    n      max A   M/√n    B/√n    B/M
   dense N=50 (C-N50)     50     72      0.570   0.218   0.38
   dense N=45 (C-N45)     45     61      0.572   0.225   0.39
   Singer–Bu q=61         3782   10707   0.604   0.209   0.35
   Singer–Bu q=101        10302  30575   0.589   0.207   0.35
   random diffs (k=40)    676    3876    1.203   0.248   0.21
   random d=0.5           1017   1999    7.19    0.234   0.03
   random d=0.05          1973   39989   8.92    0.308   0.03
   interval [1,200]       200    200     3.12    0.085   0.03
Reading:
- P28 gives ≈ 0.21–0.31·√n on every set with local randomness, including all near-extremal ones, where it recovers
  35–39% of M.
- It fails only for the deterministic interval, where it gives ~log n and M is carried by Gibbs.
- This supports the dichotomy behind P28: "B_P28 small at every scale ⇒ deterministic spectrum ⇒ Gibbs lobes
  (non-positive-definite twisted profiles at the spikes)". A quantitative version of that implication would give
  Chowla.
- Tried and failed (NOTEBOOK): descending spikes through scales with P25 and the triangle inequality loses a factor
  5 per scale (g_H <= 5g_{H/4} + 4M), the same as P24(b) shell growth. The phase information must be used.

## E46 (2026-10-19) KILLED: ball-shaped Kronecker/Bohr sets as a construction (src/e46_bohr_ball.py, seed 20261019)
A = {a <= X : |(2a/X − 1, ‖aα₁‖/r, …, ‖aα_d‖/r)|₂ <= 1}, density ≈ 1/4 in the lift, 3 random α per row
(the cube variant crashed at d = 0, a script bug; irrelevant).
R = M/√n (min over 3 α):
   d:       0      1      2      3      4      6      8
   n≈400   4.38   6.49   7.93   9.02   10.41  11.65  12.39
   n≈1600  8.70   12.85  15.91  18.39  20.26  23.46  25.53
R ∝ √n at every d, so M is linear in n, and R grows with d. Mechanism (the motivation was that a (d+1)-ball's Fourier
transform has a first negative lobe exponentially small in d):
- (i) The ball transform still has real negative values at lattice frequencies k (Λ₁ min ≈ −0.13 for the disk).
  Each Kronecker spike x ≈ −2πk·α carries a twisted profile with such a value, so there is a Gibbs lobe linear in n.
- (ii) In high dimension almost all of the ball's volume lies in a boundary layer, so the 0/1 set is a sum of very many
  small spikes (lattice-point discrepancy) and behaves like noise, giving M ~ √(n log X) or worse. For d >= 4 the
  r = 0.5 cap also clips the ball in T^d.
A 0/1 set cannot have both a smooth shape (small Gibbs) and no boundary noise. This is the same tension P28 isolates.

## E47 (2026-10-19) Spike share: fraction of ‖f_A‖₂² on {f_A > K·M} (src/e47_spike_share.py on dirichlet; FFT grid 16·2^⌈log2 X⌉)
Motivation (NOTEBOOK 2026-10-19 item 2). Share_{>KM} >= 1 − 2(1 + K)R², so R -> 0 forces share -> 1 for every fixed
K. P30 conjectures a uniform cap ρ < 1.
   set                 n       R      max f/M  K=1    K=2    K=4    K=8    K=12
   dense N50           50      0.570  12.4     0.820  0.800  0.783  0.657  0.239
   dense N45           45      0.572  11.7     0.819  0.783  0.772  0.635  0.0
   Singer–Bu q=61      3782    0.604  101.8    0.780  0.660  0.557  0.547  0.544
   Singer–Bu q=151     22952   0.578  262.3    0.786  0.674  0.537  0.507  0.506
   Singer–Bu q=401     161202  0.554  725.3    0.792  0.685  0.544  0.506  0.505
   interval [1,500]    500     4.88   4.6      0.895  0.869  0.554  0      0
   random d=0.5        2043    10.14  4.5      0.455  0.443  0.283  0      0
   taper random        1988    1.69   26.4     0.661  0.657  0.656  0.646  0.612
   random diffs k=60   1649    1.33   30.6     0.531  0.264  0.117  0.106  0.104
Reading:
- At large K the share is the central (density-profile) peak: ≈ 0.5 for Bu, ≈ 2/3 for triangle profiles (theory
  ∫φ²/∫φ = 2/3), 0.64–0.78 for the dense records.
- No set puts noise mass into secondary spikes above 4M.
- A construction with R -> 0 needs >= 1 − ρ* of the mass in secondary spikes far above M. This is the quantitative
  target for the construction track.

## E44 closed (2026-10-19): Gurobi full-box N=45, X=64, warm-started at 3.836.
- After 3600 s: bound 3.358, 2.4e7 nodes, no better incumbent.
- Stopped by the lead. Low value after P29: the dense small-N sets are pre-asymptotic (density 0.7 cannot persist).
  N=50/55 stages were not run.

## E48 (2026-10-19) ρ_L = sup_{v>=0 on L+1 points} ‖v∗v‖²/((L+1)‖v‖⁴) (src/scratch/rhoL.py, L-BFGS, 12 starts, dirichlet)
   L+1:    2      3        5        10       20       50       120
   ρ_L:    0.75   0.71429  0.69669  0.68940  0.68758  0.68708  0.68700
   const:  0.75   0.7037   0.68     0.67     0.6675   0.6668   0.66669
- The optimizer is dome-shaped: ends at ≈ 0.62 of the peak.
- Limit ≈ 0.687 < Beckner–Hölder 4/(3√3)≈0.76980. This is the constant in P31.

## E49 (2026-10-19) Does steep front-loading help? Profile-constrained SA (src/profile_sa.c, src/e49_batch.sh; dirichlet)
Setup:
- [1, X] in blocks of 10, each block's count fixed by c(1 − a/X)^p with c = 1 (density 1 at 0, d/δ = p + 1).
- Swaps only within blocks; mode 1 = free swaps from the same start.
- 3e6 iterations × 6 restarts × 2 seeds; grid objective (G = 8X + 1 on [0, π]).
- HEURISTIC and search-limited: absolute values are far above the records (calibration: at N = 36 random-start SA
  reaches 0.60 vs the 0.565 optimum).
Results (best grid R over seeds; examples/profile_sa/e49.jsonl):
   n     triangle p=1 (X=2n)   p=2 (X=3n)   p=3 (X=4n)   free, X=2n   free, X=3n
   150   0.754                 0.801        0.875        0.762        0.916
   300   0.781                 0.886        0.922        0.843        1.014
Reading:
- At equal effort, R increases with steepness p. Steep profiles, which form P31's escape class, are WORSE
  constructions than the triangle (P31-covered) at n = 150–300.
- The profile constraint helps the search (free < constrained at the same span).
- Consistent with the heuristic that front-loading only adds Gibbs-like cost.
- Not a proof, and not a certified minimum. The next probe is power-law and Bohr-type locally deterministic profiles
  (filter 3).

## E50 (2026-10-19) Power-law profiles: front-loaded at EVERY scale (src/profile_sa.c, p < 0; src/e50_batch.sh; dirichlet)
Setup:
- Density min(1, c(a/X)^{−α}), i.e. front-loaded at every scale: P31's full escape class.
- Same SA as E49 (3e6 iterations × 6 restarts × 2 seeds, block-constrained, grid objective). HEURISTIC.
Results (best grid R over 2 seeds; examples/profile_sa/e50.jsonl):
   α      c      X      n     R        front density (a <= X/10) / avg
   0.5    0.2    417    150   0.927    0.88 / 0.36
   0.5    0.2    833    299   1.001    0.88 / 0.36
   0.7    0.1    610    150   1.018    0.79 / 0.25
   0.7    0.1    1220   300   1.096    0.80 / 0.25
   0.85   0.05   900    149   1.079    0.69 / 0.17
Reading:
- Every power-law profile is worse than the triangle at equal n (0.754 / 0.781).
- R grows with α and with n (0.93 -> 1.00 for α = 0.5; 1.02 -> 1.10 for α = 0.7).
- The escape class is empirically the worst region for constructions: the obstruction is not just P31.
- Supports the self-reducibility picture (NOTEBOOK 2026-10-19): sets that evade P31 through front-loading pay through
  Gibbs/rotation cost. HEURISTIC; not certified.

## E51 (2026-10-19) R3 noise-transfer ratio and secondary-spike anatomy (src/e51_transfer.py; dirichlet; examples/e51/e51.jsonl)
Setup:
- g = f ∗ F_w with w ∈ {X/4, X/2, X}.
- S = {f > 2M, |x| >= 4/w} (secondary spikes); E = S + c/w with c ∈ {3, 4, 6}.
- τ = (1/2π)∫_E (M + g)² / (M² + s_A/2).
- B = Λ·m_g(E)/(n/2), the P32 bound on f's secondary mass, normalised. B < 1 would be a nontrivial bound.
- FFT grid; UNCERTIFIED quadrature.
Results (w = X, c = 4 unless noted):
   set              n     R      sec.share_f   τ      m_f/m_g   Λ      B
   Bu q101          380   0.764  0.405         0.52   0.99      3.05   2.7   (c=3, w=X/4: B=9.6)
   Bu q199          1560  0.701  0.476         0.58   1.06      3.05   2.7
   Bu q401          6320  0.657  0.521         0.63   1.09      3.05   2.7
   Singer diff q31  496   0.718  0.088         0.39   0.31      3.05   1.8
   Singer diff q61  1891  0.713  0.078         0.37   0.28      3.05   1.7
   E49/E50 SA sets  300   0.78–1.1  0.00–0.05  0.1–0.3  0.01–0.4  3.05   1.1–1.9
Spike anatomy:
- Bu: the tallest secondary spikes sit at x/2π = 1/3 and 1/6, height 10–20√n, i.e. ≈ n/4.
  - This is the mod-3 dilation: A ∩ 3Z = 3D with D the Sidon differences; the sums lie in 1 + 3Z.
  - Further spikes of height ≈ 7–9√n sit at other rationals (1/8, 22/59, …).
  - The secondary share GROWS with n (0.40 -> 0.52) as R falls.
- Singer differences: no secondary spike above 3√n.
- SA sets: essentially no secondary spikes. Their L² mass sits at moderate heights, consistent with R ≈ 1.
Reading:
1. P32 is far from contracting: B >= 1.7 on every test set and B ≈ 2.7 on Bu at every n.
   - The realised m_f/m_g (≈ 1) is 3× below Λ.
   - τ ≈ 0.5–0.6 on Bu: g's mass DOES sit on f's secondary spikes.
   - So the noise-transfer route (R3 recursion) is KILLED as stated (see NOTEBOOK).
2. Bu exactly saturates the dilation inequality. Averaging over cube roots of unity gives M(A ∩ 3Z) <= M(A), with
   |A ∩ 3Z| = n/2. So R(D) <= √2·R(A), and asymptotically 1/√2 = √2·(1/2). Equality.

## E53 (2026-10-19) Realised P31 efficiency for f and along the low-pass recursion (src/e53_efficiency.py; examples/e53/e53.jsonl)
Definitions:
- eff_f(w) = W(n/2 + M²)/((X + w + 1)(M² + s_A/2)). P31 says eff_f <= ρ_L.
- eff_g(w, θ) is the same quantity for G = g_w at window θw.
Results:
- eff_f(X) = 0.37–0.51 on every set (Bu 0.42–0.44, Singer 0.45, dense N50 0.51, SA 0.38–0.44).
- eff_f(X/16) = 0.05–0.11.
- eff_g ranges 0.06–0.31 over all (w, θ).
Reading:
- Every realised value is far below ρ ≈ 0.687, but only because M² ~ n here.
- For hypothetical R -> 0 sets the M² terms vanish and eff becomes a pure profile quantity. Then:
  - triangle profile: eff_f(X) -> 2/3;
  - flat front: eff_g(w, θ) -> (2/3)/(1 + θ), exactly the recursion's borderline (NOTEBOOK 2026-10-19 late).
- Not evidence for or against Chowla. It locates where the slack is not.

## E55 (2026-10-19) What P31 alone proves for actual families (src/scratch/p31_family_lb.py; dirichlet)
Method: the best P31 lower bound on R over w ∈ (0, X]: M² >= (Wn − C·s_A)/(2(C − W)).
Columns: C from Beckner (0.7698(L + 1)), elementary P31-E, and numerical ρ = 0.687 (unproved).
   set              n     true R   P31 LB (Beckner / elem / num)    best w/X
   Bu q101          380   0.764    0.077 / 0.064 / 0.114             0.10–0.19
   Bu q199          1560  0.701    0.086 / 0.068 / 0.126             0.13–0.20
   Bu q401          6320  0.657    0.060 / 0.042 / 0.105             0.08–0.19
   Singer diff q61  1891  0.713    0.137 / 0.113 / 0.198             0.25–0.46
   dense N50        50    0.569    0.209 / 0.186 / 0.266             0.33–0.53
   E49 triangle     299   0.784    0.126 / 0.102 / 0.186
   E50 α=0.5        299   1.003    0.022 / 0.015 / 0.109             (escape class: P31 nearly vacuous)
Reading:
- P31 depends only on the density profile s_A(·).
- Every known family's profile lies OUTSIDE the escape class (front/average ratio ≈ 2 < 2/ρ). So P31 already proves
  that any family with the Bu, Singer or triangle profile has R >= c(profile) > 0 (about 0.04–0.2).
- Constructions must change the profile class, not tune parameters.

## E52 (2026-10-19) Two-level front-loaded profiles: escape-class probe (src/e52_batch.sh; examples/profile_sa/e52.jsonl)
Profile: density d1 on [1, εX], a linear ramp over 0.05X, then d2. Same SA as E49 (3e6 iterations × 6 restarts ×
2 seeds). HEURISTIC.
   config (δ, d1, ε)           escape?   n≈150 R   n≈300 R
   δ=0.30, d1=0.90, ε=0.15     yes       0.970     1.362
   δ=0.25, d1=0.75, ε=0.20     yes       1.100     1.789
   δ=0.15, d1=0.45, ε=0.25     yes       1.659     2.613
   δ=0.25, d1=0.50, ε=0.20     no (2δ)   1.073     1.232
   (E49 triangle: 0.754 / 0.781)
Reading:
- Everything is far worse than the triangle, and R grows like √n, i.e. M is LINEAR.
- Cause: the kinks of the ramp. The smooth part P(x) = Σ p(a)cos(ax) has dips of size about (d1 − d2)·(ramp width)
  ∝ X at x ~ 1/(ramp width), via the cosine transform of p' jumps.
- Lesson: escape-class probes must use C¹-smooth profiles. E49's (1 − t)^p, p = 2, 3 are smooth and in the escape
  class; there R ≈ 0.8–0.9, growing slowly.
- Within the escape class, nothing beats the triangle so far (E49, E50, E52).

## E56 (2026-10-19) Multiplicative self-similar sets: smooth numbers (src/e56_multiplicative.py; examples/e56/e56.jsonl)
Motivation: y-smooth numbers are front-loaded at every scale and dilation-self-similar (S ∩ pZ = p·S(X/p, y) for p <= y),
the structure the SR picture predicts.
Results (X = 2^12 … 2^18, UNCERTIFIED grid minima):
- smooth(y) for y = 3 … 61: R grows with X (e.g. y = 19: 1.40 -> 3.34). The minimum is at x/2π = a/p with p the first
  prime > y.
- odd smooth: M = n, minimum at x = π.
- smooth with y = √X: R = 1.4 -> 22.5, minimum near x = 0: the Dickman profile has a kink at a = y (E52 lesson).
- rough numbers: M ~ n, all odd.
Mechanism, PROVED: the dilation pinch (NOTEBOOK). y-smooth numbers avoid pZ for every prime p > y. Averaging f over the
p-th roots of unity gives M >= n/(p − 1), which is LINEAR. So multiplicative self-similarity is not enough: a
counterexample must keep its fair share in EVERY qZ with q <~ n/M, not only for small primes.

## E57 (2026-10-19) L⁴ window inequality vs P31 (src/e57_l4window.py; examples/e57/e57.jsonl)
- L⁴/L¹ Nikolskii constant for nonneg polynomials: C₄(L) = sup ‖u∗u∗u∗u‖²/((L + 1)³‖u‖⁸).
  - Values: 0.48872 (L = 8), 0.48688, 0.48636, 0.48622, 0.48618, 0.48617 (L = 256). Decreasing in L.
  - Fejér gives 151/315 = 0.47937. Same pattern as ρ (0.687 vs 2/3).
- Window step at L⁴, integrated over x₀: mean(F⁴)·mean((f + M)⁴) <= C₄(L + 1)³·mean((M + g)⁴).
  The left side contains Schur triples and additive energy, so it is NONLINEAR in 1_A.
- Least M allowed (as R), best over w:
   set              true R   L⁴ LB    L² (P31) LB
   dense N50        0.565    0.257    0.208      <- L⁴ beats P31
   Singer q61       0.713    0.125    0.136
   Singer q31       0.718    0.106    0.155
   E49 triangle     0.779    0.037    0.122
   Bu q101/q199     0.76/0.70  0      0.08
   E49 p=3, E50     0.93–1.1  0       0          (escape class: both vacuous)
- Reading:
  - The nonlinear window helps only for small dense sets.
  - On random-like and escape-class sets the L⁴ front condition is WEAKER than P31's: the front must carry
    (energy ratio)^{1/4} instead of the density ratio.
  - Not a route to the escape class as is.

## E54 (2026-10-19) Adversarial test of P31-C(a) on DYADIC sets (src/e54_batch.sh; examples/profile_sa/e54.jsonl)
SA over A ⊂ (X/2, X] (density 0 below X/2, then a 0.05X ramp up to d2). Results:
   X     d2    n     best grid R
   526   0.6   150   10.33
   1052  0.6   300   14.68
   1052  0.3   150   10.36
   2104  0.3   300   14.69
So M ≈ 0.85n: LINEAR. This exposed the error in claiming P31-C(a) as content.
- Sets in (X/2, X] satisfy M >= 0.373n by averaging f(θπ/X) over θ ∈ [1, 3/2] (PROOFS P31-C correction).
- The √n statement was true but void.

## E58 (2026-10-19) Best linear test for sets without small elements (src/e58_ratio_lp.py; Gurobi LP; examples/e58/e58.jsonl)
LP: maximize c over probability measures μ on [0, π] (grid G = 16KY) subject to μ̂(a) <= −c for all a ∈ [Y, KY].
Results (Y = 40 and 80 agree):
   K     1.5     2       2.5     3        4       6       8       12      20
   c     0.807   0.499   0.431   0.3333   0.2497  0.1665  0.1249  0.0833  0.0500
   cK    1.21    0.998   1.08    1.000    0.999   0.999   0.999   0.999   0.999
- c(K) = 1/K for K >= 2. PROOFS P33 proves the matching bound M(A) >= (min A/max A)|A| by an explicit Fejér measure
  on the (Y + Z)-th roots of unity.
- The optimal atoms sit near multiples of 2π/((K + 1)Y), matching P33's construction.

## E60 (2026-10-19) The escape class contains near-½ sets: Bu + far outliers (src/e60_bu_frontloaded.py; examples/e60/e60.jsonl)
Bu's identity f = ρ² − k/2 − g/2 holds for EVERY Sidon S. Take Bu's certified S (q = 199, k = 40; q = 401, k = 80) and add
k_out = 2–4 far elements ±(T·L + 7m), keeping S Sidon.
Core differences and sums stay near 0 while X grows by a factor ≈ T.
M is a grid minimum: 16× oversampled, capped at 2^28 points (≥ 6× for the largest X). UNCERTIFIED.
   base     T   k_out  n     X          R (grid)  front ratio (w/X = 0.001 / 0.01 / 0.1 / 1)  P31 LB (all constants)
   199_40   0   0      1560  97738      0.701     1.7 / 2.4 / 2.0 / 1.65                        0.068–0.126
   199_40   8   2      1722  833247     0.727     20.5 / 15.5 / 13.5 / 2.6                      0
   199_40   96  4      1892  9998376    0.727     177 / 139 / 23 / 2.6                          0
   401_80   0   0      6320  432979     0.657     1.7 / 2.4 / 2.2 / 1.67                        0.042–0.105
   401_80   32  4      6972  14612712   0.673     71 / 64 / 23 / 2.7                            0
   401_80   96  4      6972  43837800   0.673     201 / 153 / 26 / 2.8                          0
Reading:
- Front-loading by a factor up to 200 costs Bu only +0.016 to +0.026 in R.
- The escape class is NOT "empty of good sets": it contains sets within 0.03 of Bu's R at the same size (Bu + outliers; P16 still applies to them). R -> ½ is PROVED in P37 (modulo Bu et al.'s theorem) for k_o = o(√k) outliers. The cross term 2ρ_Sρ_O costs only k_o√(2k).
- P31's front-loading barrier is a method limitation, not evidence that front-loaded sets have large M.
- Any lower-bound proof must handle front-loaded Bu sets. Profile-only arguments cannot reach Chowla.
- (E50/E52 SA found R ~ 1–1.8 for smooth front-loaded profiles. That was search difficulty, not structure.)

## E61 (2026-10-19) Adversarial test of P34 (one-sided Littlewood) (src/e61_littlewood.py; examples/e61/e61.jsonl)
Maximize min_x T over (a) all phases θ_j (annealed soft-min L-BFGS, 3–6 restarts) and (b) ±1 signs (SA, 2e5–4e5
iterations). Refine the minimum on a 64n grid with Newton. HEURISTIC search; the bound is the theorem.
   n     phases −min T/√n   signs −min T/√n   P34 bound (P31-E)
   8     0.647              0.730             0.350
   16    0.624              0.749             0.317
   32    0.610              0.864             0.300
   64    0.609              0.979             0.291
   128   0.607              1.040             0.286
Reading:
- Consistent with P34: no optimum gets near the bound.
- The optimal unit-amplitude constant looks like ≈ 0.6, stable in n.
- Sign-only search is much harder: it is SA-limited, and the values rise with n.
E61 addendum: n = 256 gives phases 0.6072 and signs 1.155 (bound 0.284).
E61b (src/e61b_littlewood_large.py; examples/e61/e61b.jsonl). Baselines, −min T/√n:
   n      chirp θ_j = πj²/n   Rudin–Shapiro   random (median)
   256    1.188               1.414           2.31
   512    1.168               1.412           2.64
   1024   1.172               1.414           2.65
   2048   1.166               1.411           2.72
Optimized phases: n = 384: 0.6087; 512: 0.6074; 768: 0.6088 (n = 1024 running).
- The optimal unit-amplitude one-sided constant (HEURISTIC) is stable at ≈ 0.608 for n = 64..768.
- The proved P34 constant is 0.28, or 0.31 once P31-N/Beckner is complete (ρ <= 4/(3√3)≈0.76980), or 0.385 with the
  numerical ρ_∞ = 0.687. The gap to 0.608 is a constant factor ≈ 1.6–2.2.

## E62 (2026-10-19) Phase relaxation of the best 0/1 supports (src/e62_phase_relax.py; examples/e62/e62.jsonl)
Question (P34: window methods are phase-blind): is C½ a positivity phenomenon or a support phenomenon?
- Method: maximize min_x Σ_{a∈A} cos(ax − θ_a) over the phases, on fixed supports A. Annealed soft-min L-BFGS with FFT
  gradient, 2 random starts. θ = 0 is a stationary point by evenness, so that start is uninformative.
- Final value: 32× grid minimum (UNCERTIFIED).
   support            n     R (0/1)   R (best phases)
   dense N50          50    0.5696    0.4982
   Bu q101            380   0.7641    0.6815
   Bu q199            1560  0.7018    0.6431
   Singer diff q31    496   0.7184    0.5995
   E49 triangle SA    299   0.7842    0.5559
   (cf. full interval [1, n], E61: 0.607, flat in n)
Reading:
- Freeing the phases buys 0.06–0.23 at these sizes, with the most on poorly optimized 0/1 sets.
- The best phase-relaxed value seen is 0.498, on the record dense support: ½ to within search noise.
- So relaxing positivity does not produce a qualitatively sub-½ regime on these supports.
- Working conjecture recorded: phase-C½, i.e. −min Σ_{a∈A} cos(ax − θ_a) >= (½ − o(1))√|A| for all supports and phases.
  - It is weaker evidence than C½ itself: only 2 starts per support, small n.
  - If true, any C½ proof may be phase-blind except at the level of supports. But P31-type profile methods are already
    known to fail on front-loaded supports (E60).

## E59 (2026-10-19) Smooth escape profiles at n ≈ 600/1200 (src/e59_batch.sh; examples/profile_sa/e59.jsonl)
SA (profile_sa mode 0, 6e6 iterations × 4 restarts) with prescribed profiles c(1 − t)^p. HEURISTIC, grid minimum.
   p (profile)       n≈600 R    n≈1200 R
   1 (triangle)      0.828      0.885
   2 (escape)        0.920      0.980
   3 (escape)        0.970      1.015
Reading:
- Under equal effort, steeper (front-loaded) profiles are worse, and R rises with n.
- This is search-limited: Bu reaches 0.66 at n = 6320, and Bu + outliers (E60) is front-loaded with R ≈ 0.67.
- So E59 does NOT show that escape profiles are intrinsically bad. It shows SA cannot find their good members.

## E63 (2026-10-19) Are near-optimal DENSE sets front-loaded? (src/e63_batch.sh, src/e63_post.py; examples/e63/)
Free SA (profile_sa mode 1: any element can move anywhere in [1, X]) at density 1/C, C ∈ {2.5, 3, 4, 6, 8}, X box
150/300, 2 seeds, 3e6 iterations × 6 restarts. Optima are post-processed for R (16× grid, UNCERTIFIED), the front ratio
and the P31 lower bound.
Results (20 optima, n = 19–120):
- R = 0.65–1.02. Search-limited for n >= 50.
- Front ratio at w = X: 1.09–1.55. At w = 0.05X: 0.0–2.5, mostly < 1.6.
- P31 lower bound on R: 0.13–0.26 (P31-E), 0.18–0.35 (numerical ρ). It is POSITIVE for every optimum.
Reading:
- Every near-optimal dense set SA finds is NOT front-loaded, and P31 already proves R >= 0.13–0.26 for it.
- The hard case of target T-dense (front-loaded A ⊂ [1, Cn]) contains no good sets that search can find (also E52:
  R ≈ 1–1.8 there).
- The good sets in the escape class are SPARSE (E60: Bu + outliers).

## E62b/E62c (2026-10-19) Phase relaxation, wider supports and the N50 optimum (src/e62b_phase_relax_wide.py,
## src/scratch/e62c_n50_phases.py; examples/e62/e62b.jsonl, e62c.json)
- E62b, best of 4 starts (UNCERTIFIED grid). COMPLETE (examples/e62/e62b.jsonl, 8 rows).
   support                  n      max A    R (0/1)   R (phases)
   dense N50                50     72       0.5696    0.4983
   Singer diff q31          496    991      0.7184    0.5983
   Singer diff q61          1891   3781     0.7128    0.6329
   E49 triangle SA          299    566      0.7842    0.5499
   Bu q199 (k=40)           1560   97738    0.7018    0.6428
   Bu q401 (k=80)           6320   432979   0.6572    0.6093
   random n50, X=100        50     97       1.4953    0.7412
   random n200, X=400       200    398      2.6478    0.7228
  - Random supports gain the most (2.65 -> 0.72): phases repair a bad support down to ≈ 0.7, but not below.
  - Structured supports gain 0.05–0.17 and stay above 0.6 at n >= 1500 (local optimization from θ = 0).
- E62c: 10 starts and 5 annealing stages on the N50 support give best R = 0.4916 (values 0.4916–0.5000).
  - After removing the best linear phase (a pure shift of x), the phases are SMALL PERTURBATIONS OF 0:
    |θ| mostly < 0.7, mean distance to {0, π} 0.41. They are not a sign pattern.
- Reading:
  - Phase-relaxed C½ fails at n = 50 by 0.008 on the best dense support.
  - Unimodular coefficients are not admissible for Chowla/Epoch (coefficients must be +1).
  - The relaxation buys ≈ 0.08 at n = 50 and less on larger structured supports (q61: 0.71 -> 0.63, against the
    0/1 sub-family's 0.5 + O(n^{-1/4})).
  - Evidence that positivity of coefficients costs only a small constant. No qualitative sub-½ regime appears.

## E64 (2026-10-19) One Bu step with D fixed: exact class optima (src/e64_bu_step.py, Gurobi; examples/e64/)
Class: A = 3D ∪ E with D fixed and E ⊂ {1 <= e <= XE : 3 ∤ e}, XE = 1.25·max(3·max D, max E_Bu). Maximise |E| subject
to f_A >= −Mt, with grid cuts plus lazy cuts at the true minimiser of every incumbent (box_minlam.true_min).
ObjBound is a valid upper bound up to float evaluation: NUMERICAL-EXACT class optimum, not interval-certified.
Theory: NOTEBOOK "One Bu step with D fixed" (T1–T8). The pinch is λ <= 2 + 2Mt/|D|.
Dense D (the certified N24 optimum, M(D) = 2.82630, R = 0.5769):
- Mt = M(D): E = ∅, OPTIMAL (76 s).
- Mt = 1.05·M(D) (slack 0.141): E = ∅, OPTIMAL (1188 s).
- So equioscillating optima admit NO one-step extension at small slack: W must vanish at every near-minimiser (T5).
  A single element needs slack >= ½, since the three coset cosines sum to 0.
Sidon D (optimal Golomb rulers, best Bu shift), Mt = M_Bu, so Bu's E (λ = 1) is feasible (tl 1800 s, 2 threads):
   k   |D|  M(D)    M_Bu    |E| (bound)   λ      R(A)    R_Bu    Z-energy outside incircle (central / bulk)
   6   15   3.000   3.995   32 (35)       2.13   0.583   0.730   (test run, killed at 300 s; anatomy not run)
   7   21   3.477   4.737   35 (46)       1.67   0.614   0.731   83% (75% / 7%), max|Z|/P 1.84, dev 8.3°
   8   28   3.946   5.410   35 (67)       1.25   0.681   0.723   59% (43% / 16%), max|Z|/P 1.37, dev 13°
   (Bu itself: 8.7% / 3.6% outside the incircle, dev 18–23°, with the junk pushing it past the incircle.)
Anatomy (src/e64_anatomy.py, src/e64_anatomy2.py): the optima USE VERTEX LOCKING, mostly in the CENTRAL SPIKE
(|y| < 2π/span(W), y = 3x). Here W is DENSE (k = 7: 35 terms in a span of 52), so the central spike carries most of
the energy. That is the dense-set mechanism (T8), and it is natural at small k.
The phase-blind cap ∫P² = Mt² + |D|/2 is inflated at small k by the slack (k = 8: 43 > |E| = 35).
The asymptotic question (T9: can the tails of an inflated central spike be kept under P at large k?) is open. See
k = 9–12 below and E65.
E64 continued (Mt = M_Bu; tl 1800 s; none proved optimal):
   k   |D|  M(D)    M_Bu    |E| (bound)   λ      R(A)    R_Bu    outside incircle (central / bulk)
   9   36   4.499   6.120   40 (85)       1.11   0.698   0.721   22% (0% / 22%)
   10  45   5.000   7.500   88 (106)      1.96   0.648   0.791   79% (72% / 7%); |E| close to the pinch (105)
- R(A)/R_Bu = 0.80, 0.84, 0.94, 0.97, 0.82 for k = 6..10. This is NOT monotone. It tracks Bu's relative slack
  M_Bu/M(D) (1.50 at k = 10), which the optimum spends on central-spike locking.
- A clean asymptotic test must fix the relative slack: E65 measures M(λ)/M(D) at fixed λ.
Dense D = N36 optimum, Mt = M(D): no nonempty E found in 1500 s (bound 64, not closed). The ε = 0.05 run is running.

E64 results through k = 12 (Gurobi status 9 = time limit, so the optima are NOT proven except where status = 2).
| k | nD | R_Bu | R_opt (class) | λ = nE/nD | R_opt/R_Bu |
|---|---|---|---|---|---|
| 7 | 21 | 0.7309 | 0.6143 | 1.67 | 0.840 |
| 8 | 28 | 0.7229 | 0.6808 | 1.25 | 0.942 |
| 9 | 36 | 0.7212 | 0.6982 | 1.11 | 0.968 |
| 10 | 45 | 0.7906 | 0.6475 | 1.96 | 0.819 (Bu's k = 10 Golomb shift is poor) |
| 11 | 55 | 0.6993 | 0.6862 | 1.07 | 0.981 |
| 12 | 66 | 0.6866 | 0.6866 | 1.00 | 1.000 |
Dense D (N24 status 2; N36, N50 status 9): E = ∅ at eps 0 and 0.05.
E65 (annealing, src/e65_driver.py, Singer q = 11, k = 12, nD = 66; grid M refined by true_min):
- λ = 1 reproduces Bu, M = 8.13.
- λ = 1.25, 1.5, 1.75, 2.0 give M = 11.03, 10.98, 11.67, 11.69 (ratio 1.35–1.44).
Conclusion (HEURISTIC, supports T9/T10): the one-Bu-step class closes onto Bu as k grows; λ -> 1.

E65 extended (q = 13, 17, 19; 2·10^7 iterations, 2 restarts). M(λ)/M_Bu at λ = 1.25 / 1.5 / 1.75 / 2.0:
- q = 11: 1.36 / 1.35 / 1.44 / 1.44
- q = 13: 1.39 / 1.42 / 1.45 / 1.52
- q = 17: 1.51 / 1.64 / 1.68 / 1.73
- q = 19: 1.63 / 1.70 / 1.71 (λ = 2 pending)
The penalty for λ > 1 GROWS with q. Every λ > 1 has R >= 0.83 against R_Bu ≈ 0.67–0.72. This is stronger evidence for
T9/T10: the one-step class closes onto Bu.
E64 second level (D = a Bu set itself, k = 6, |D| = 30, M(D) = 4.0045, R(D) = 0.7311; Mt = 1.05·M(D); 2400 s):
- No nonempty E is feasible in the time limit (bound 68, not closed). k = 7 (|D| = 42) is running, with no E found
  after 600 s.
- Bu sets behave like equioscillating optima: no Bu step can be stacked on them at small slack.

## E66 (2026-10-19) Cumulative rounding of profiles: R = M/√n vs X (src/e66_cumround.py; examples/e66/e66.jsonl)
NUMERICAL (box_minlam.true_min, over = 16: grid + Newton; not certified). Phases σ ∈ {0, 0.37, 0.71}; entries are
min/max of R over σ. g = (√5 − 1)/2.
| profile | 2^10 | 2^12 | 2^14 | 2^16 (n) |
|---|---|---|---|---|
| a: g(1−t) [irrational start, curved] | 2.14/2.42 | 2.36/2.92 | 2.72/2.92 | 2.72/2.97 (20251) |
| b: g(1−t)² | 2.13/2.49 | 2.14/2.54 | 2.61/2.63 | 2.83/3.05 (13500) |
| c: ½(1−t)² [TD2] | 2.27/2.40 | 2.18/2.60 | 2.53/2.71 | 2.49/2.76 (10922) |
| g: 1−t [starts with long runs] | 1.40/1.52 | 1.42/1.60 | 1.61/1.76 | 1.77/1.79 (32767) |
| d: g flat on [0,½], then quadratic decay | 3.2/7.0 | 6.4/14.2 | 12.8/28.6 | 25.6/56.5 |
| e: ½ flat on [0,½], then quadratic decay | 3.2/13.8 | 6.0/28.4 | 12.1/55.9 | 24.4/110.9 |
| f: 0.35 + 0.25 cos 5πt [oscillating] | 4.4 | 8.8 | 17.5 | 35.0 |
Reading:
- Curved profiles (P41's class, including irrational start density, outside P38) stay at R ≈ 1.4–3.0, rising
  slowly, perhaps ~√log X. This is consistent with P41's M >= c√n.
- Non-convex profiles (a flat-to-curved kink; oscillation) have LINEAR M (R ∝ √n), as in E52.
- No cumulative rounding comes near R = ½. The best is the linear profile from density 1 (R ≈ 1.4–1.8).

## E67 (2026-10-19) Bulk fraction β_K = ∫_{f<=K√n} f² / ∫f² (Conjecture SB) (src/e67_zoo.py, src/e67_bulk_sa.c;
## examples/e67/)
NUMERICAL (FFT grid integrals). SB says β_K >= c > 0 for every A, and implies Chowla via P40.
| family | n | β1 | β2 | β3 | R |
|---|---|---|---|---|---|
| interval | 256 / 1024 / 4096 | 0.083 / 0.074 / 0.070 | 0.097 / 0.080 / 0.073 | 0.104 / 0.085 / 0.076 | 3.5 / 7.0 / 13.9 |
| random density 1/3 | 256–4096 | ≈0.56 | ≈0.69 | ≈0.69 | 2.9–13.8 |
| random density 1/50 | 256–4096 | ≈0.70 | ≈0.96 | ≈0.98 | |
| cumround ½(1−t)² | 256–4096 | ≈0.53 | ≈0.70 | ≈0.70 | 2.3–2.7 |
| cumround 1−t | 256–4096 | ≈0.30 | ≈0.335 | ≈0.34 | 1.57–1.68 |
| multidilate (8 primes) | 234 / 898 / 3576 | 0.28 / 0.20 / 0.18 | 0.71 / 0.26 / 0.19 | | 1.1 / 1.6 / 3.0 |
| Bu/Singer q = 7..31 | 56–992 | 0.29–0.33 | 0.44–0.53 | 0.53–0.60 | 0.66–0.80 |
| smallN_best (certified-type optima) | 20–35 | 0.19–0.30 | 0.23–0.41 | 0.30–0.48 | 0.57–0.60 |
SA minimising β_K over A ⊂ [1, X], |A| = n (4·10^6 swaps, 3 restarts):
- (X, n) = (256, 64), (512, 64): min β1 = 0.110, min β2 = 0.112–0.118. The minimiser is the interval [1, 64]
  (R = 1.81).
- (1024, 128): min β1 = 0.091, again interval-like (R = 2.51); β2 runs reach 0.215–0.227.
- (4096, 64): pending at the time of writing.
Reading:
- No SB violator was found. β is minimised by intervals (bulk = negative sidelobes ≈ 5–10%, decreasing slowly towards
  ≈ 0.05).
- The SB-extremal sets have huge M, far from the Chowla extremisers (Bu: β2 ≈ 0.45; small optima: β2 ≈ 0.25–0.4).
- B–D (P40) is far from binding at the current R: it only requires β_K <= 2(K + R)R + 2R².
E67 quantitative law (lead, 2026-10-19). The bulk fraction β_K matches the ROUNDING-ENERGY share 1 − Σρ²/Σρ (ρ = local
density profile) wherever the rounding is unstructured:
- cumulative rounding of 1−t: predicted 1/3, observed β2 = 0.335.
- cumulative rounding of ½(1−t)²: predicted 1 − (1/20)/(1/6) = 0.70, observed β2 = 0.69–0.70.
- random density δ: predicted 1 − δ, observed 0.69 (δ = 1/3) and 0.96–0.98 (δ = 1/50).
So for curved cumulative roundings ALL rounding energy is bulk (P41's mechanism) and the central spike carries exactly
Σρ²/Σρ.
Intervals (share 0): β = sidelobe energy ≈ 0.05–0.1. Bu/Singer (share ≈ 0.67): β2 ≈ 0.45, so part of Bu's rounding is
structured (spiky). Small optima: 0.23–0.41.
Heuristic form of SB: β_K >= c·[rounding share] + [negative-sidelobe energy].

## E68 (2026-10-19) Pareto search β_K + μ·R on dense boxes X = 3n (src/e68_pareto_sa.c, src/e68_batch.sh; examples/e68/)
NUMERICAL (grid; 3·10^6 swaps, 2 restarts). Question: can a dense set be spike-dominated (β small) AND have small R?
| n | μ = 0.05 | 0.1 | 0.2 | 0.5 |
|---|---|---|---|---|
| 64 (K=1) | β .13–.14, R 1.16–1.26 | β .18, R .66–.67 | β .18, R .63–.64 | β .25–.28, R .67–.78 |
| 64 (K=2) | β .19, R 1.17–1.20 | β .21–.22, R .89–.98 | β .19–.25, R .65–.79 | β .20–.27, R .61–.73 |
| 128 (K=1) | β .17, R .76–.77 | β .19–.20, R .68–.72 | β .19, R .67 | (pending) |
| 128 (K=2) | β .17, R .89–1.54 | β .19, R .66–.70 | β .26, R .79 | (pending) |
Reading:
- The Pareto front has min β rising as R falls: ≈ 0.11 at R 1.8 (interval), ≈ 0.13 at R 1.2, ≈ 0.18 at R ≈ 0.65.
  No drift towards β -> 0 from n = 64 to 128.
- The low-(β, R) sets are very dense and front-heavy (max A ≈ 86–93 at n = 64, density ≈ 0.7). Their spike energy is
  mostly the central spike; they are not a new structural regime.
- Consistent with SB; small R costs bulk.
E68 anatomy (n = 64, K = 1, β = 0.176, R = 0.670): A = [1, 52] ∪ {56, 58, 63, 65, 69, 72, 76, 80, 81, 82, 85}.
- A full interval plus a sparse tail that fills the Dirichlet sidelobes. The interval alone has R ≈ 1.4.
- The only spike is the central one, carrying 82.5% of the energy. The tail's rounding is the bulk.
- This is the front-full cumulative-rounding shape (P41's class). E66's 1−t profile shows such shapes drift to
  R ≈ 1.4–1.8 at large n, so they are small-n optima only.

## E69 (2026-10-19) Bounded-discrepancy (non-cumulative) roundings; P47 audit (src/e69_bdround.py,
## src/e69_p47_audit.py; examples/e69/)
- E69. Profiles ½(1−t)², (1−t), ½(1−t)⁴, 0.9(1−t)². X = 2^12, 2^14, 2^16.
  - 'walk': randomized rounding forced to keep prefix discrepancy <= D0 ∈ {1, 4, 16}. Every case has
    R ∈ [1.6, 3.0], slowly varying in X.
  - 'block': adversarial TD7-O blocks (B = 16, 256; discrepancy 2–32). Linear M (R = 10–77, minimum at π or π/2).
  - NUMERICAL (grid + Newton). No small-R bounded-discrepancy rounding was found.
- E69b. P47 audit on walk roundings. X = 4096, 16384; D0 ∈ {1, 4, 16}; h ∈ {2D0+2, 8D0}; θ ∈ {0.1, 0.3, 0.6};
  profiles (1−t), 0.9(1−t)², ½(1−t)², flat 0.3. 144 rows.
  - Every P47 lower bound (rigorous ρ_L and numerical ρ = 0.687) is below the true M.
  - The numerical U = sup H f_P is <= its P47 bound in every row. Some rows were flagged only because U ≈ 0.001 against
    a bound rounded to 0.00.
  - Bound/√X is constant in X (0.06–0.17 with numerical ρ): the √X scaling holds.
  - The retained energy E/Σe is 0.85–0.99.
  - Energy pinning Σβ² vs Σp(1−p): differences <= ~4 out of 500–3500, within D0(1 + 2V).
  - ½(1−t)² (e0/ē = 2.143) gives a positive bound only with numerical ρ at these sizes. The rigorous ρ_L(1 + 2/√L)³ is
    too large below X ~ 10^6.
- Round-3 agent T3 audit (.research/agents/tdense3_scratch/summary.json): 121 zoo sets plus 45 flat/curved and Bohr
  extensions. No set has both β₁ < 0.13 and R < 0.60. The refined R of E68's best row (n = 64) is 0.60619.

## E71 (2026-10-19) Torus level-1 inequality TL1 (src/e71_tl1.py; NUMERICAL, exact grid quadrature)
θ*(p) = sup over level-1 L = Σ_s b_s cos U_s of Λ_p(L)²/(‖L‖²p(1−p)), where Λ_p(L) = E[L·1{L > q_p}]
(= sup over E ⊂ T^S with |E| = p of the level-1 Fourier mass of 1_E, divided by p(1−p)).
| p | S=1 | S=2 (best b) | S=3 (best b) | Gaussian (S→∞) |
|---|---|---|---|---|
| 0.02 | 0.041 | 0.077 | 0.098 | 0.120 |
| 0.1 | 0.215 | 0.322 | 0.336 | 0.342 |
| 0.3 | 0.632 | 0.632 | 0.632 | 0.576 |
| 0.5 | 0.8106 | 0.8106 | 0.8106 | 0.637 |
- Maximum 8/π² = 0.81057, at S = 1, p = ½.
- Small p favours many coordinates, but every value stays below the Gaussian limit and below 8/π².
- Conjecture TL1 (NOTEBOOK): W¹(1_E) <= (8/π²)|E|(1 − |E|) for every measurable E ⊂ T^S, S <= ∞.
  For p = ½ it is equivalent to the Khintchine-type bound E|Σb_s cos U_s| <= (2√2/π)‖Σb_s cos U_s‖₂.

## E70/E70b (2026-10-19) The P47 high-pass window family on the zoo and on Bu/Singer sets (src/e70_p47_scan.py,
## src/e70b_bu_scan.py; examples/e70/). NUMERICAL (ρ = 0.687; true M by grid + Newton)
- For each set: max over h ∈ {0,1,2,…,512} (h = 0 is P31) and θ ∈ {0.02,…,1} of the P47 window bound.
- E70 (159 sets: tdense3 zoo, E68, E68b):
  - best/√n >= 0.106 everywhere; the minimum is the curved quadratic rounding.
  - Near-optimal sets (R = 0.57–0.70): best/M = 0.33–0.52.
  - Intervals and random sets: P31 (h = 0) is optimal. Roundings and Bu: h > 0 wins.
- E70b, Bu/Singer with best shift (n = q(q+1)):
| q | n | R | best/√n | best/M | best h |
|---|---|---|---|---|---|
| 37 | 1406 | 0.649 | 0.230 | 0.355 | 48 |
| 53 | 2862 | 0.758 | 0.228 | 0.301 | 96 |
| 73 | 5402 | 0.607 | 0.230 | 0.378 | 96 |
| 89 | 8010 | 0.692 | 0.224 | 0.324 | 128 |
| 113 | 12882 | 0.593 | 0.226 | 0.382 | 128 |
| 127 | 16256 | 0.586 | 0.225 | 0.384 | 192 |
- best/√n levels off at ≈ 0.225 (0.29 at q = 7, 0.237 at q = 31, then flat; q = 101 gives 0.202). The best h grows
  like ~1.5q ∝ √n.
- Reading: the extremal known family is NOT in the P47 escape class. Numerically, high-pass windows certify
  M >= 0.22√n on Bu sets uniformly in q, about 38% of the true M.

## E70b (cont.) and E72 (2026-10-19)
E70b, larger Bu (numerical ρ = 0.687): best/√n = 0.205 (q = 199, n = 39800, best h = 256) and 0.211 (q = 251,
n = 63252, best h = 384). It levels off at ≈ 0.21. The best h tracks ~1.5q.
E70b with RIGOROUS ρ_L = (4/(3√3))(1 + 2/√(L+1))³: best/√n = 0.157 (q = 31), 0.166 (q = 61), 0.171 (q = 127).
- The values RISE with q as ρ_L → ρ_∞, so the high-pass window family gives M >= 0.17√n on Bu q = 127 with the proved
  Nikolskii constant. E and S are floating sums of rational quantities; making this a certificate needs exact
  arithmetic.
- E_h/n for Bu: 0.22 (h = 1), rising to ≈ 0.55–0.60 at h >= 128.
E72, Pareto search over A ⊂ [1, 3n] minimizing B/√n + μR (src/e72_p47_pareto.c, 10^7 swaps, 2 restarts). B is the
best P47-family window bound (numerical ρ):
| n | μ = 0.1 (B/√n, R) | μ = 0.3 | μ = 1 |
|---|---|---|---|
| 64 | 0.105–0.106, R 0.96–0.98 | 0.142–0.144, R 0.73–0.75 | 0.178–0.181, R 0.70–0.72 |
| 128 | 0.122–0.127, R 0.93–0.98 | 0.156–0.164, R 0.80–0.82 | 0.186–0.204, R 0.79–0.82 |
| 256 | 0.142–0.144, R 0.87–0.94 | 0.176–0.179, R 0.87–0.88 | 0.240–0.244, R 0.95–1.00 |
Reading (NUMERICAL):
- CAVEAT (lead, same night): the optima SHRINK max A, to max A/n ≈ 1.6–1.8 (n = 64) and 2.2–2.9 (n = 128, 256). They
  mostly sit inside P31's dense range (2.466). So E72 does NOT test C = 3 escape; E72c (box ratios 4, 6, 10) does.
- Within the explored range the minimal B/√n rises with n (0.105 → 0.122 → 0.142). The best h is usually > 0: the
  high-pass windows beat P31.
- Lowering R costs window bound, as in E68. The μ = 1 runs at n = 256 did not reach low R (the search is harder).
- The question whether P31 + P47 close T-dense beyond C = 2.466 is OPEN. See E72c.

## E72c (2026-10-19) P47-escape Pareto at box ratios C = 4, 6, 10 (n = 128) and C = 3 (n = 512) (src/e72c_batch.sh)
NUMERICAL (SA, 10^7 swaps, 2 restarts per μ; B = max over the P31/P47 window family with numerical ρ = 0.687;
R on the 8X grid).
| n, C | μ | max A/n | B/√n | grid R |
|---|---|---|---|---|
| 128, 10 | 0.1 / 0.3 | 9.7–9.98 | 0.014–0.017 | 1.27–1.29 |
| 128, 6 | 0.1 / 0.3 | 4.65–4.95 | 0.020–0.025 | 0.92–0.99 |
| 128, 4 | 0.1 / 0.3 | 1.95–2.79 | 0.030–0.099 | 0.85–0.93 |
| 512, 3 | 0.1 | 2.41–2.73 | 0.159 | 0.95–0.96 |
Reading:
- At C = 6 and 10 the optimiser keeps max A ≈ 4.8n and 9.8n: these are genuine box-filling sets, and the whole window
  family certifies only ≈ 0.02√n.
- Yet R ≈ 0.9–1.3: escape from the window family is cheap, but small R is not.
- C₁ (the reach of P31 + P47) is between 2.466 and ≈ 4.8. This matches the explicit escape set (NOTEBOOK cont. 6,
  C ≈ 4–7).
- At C = 4 the optimiser shrinks max A back into P31's range, so C = 4 is not decided.

## E73 (2026-10-19) Gaussian-threshold ("multiscale Bohr") sets (src/e73_gauss_threshold.py, src/e73_batch.sh;
## examples/e73/e73.jsonl, 480 rows)
- Construction: A = {m <= X : Φ(m) > τ(m/X)}, with Φ = √(2/r)Σ_{j<r} cos(2πα_j m + φ_j) (random α, φ) and front-loaded
  density p(t) = p0(1 − t)^γ. r = 0 is independent Bernoulli rounding of p.
- Grid: X = 2^14, 2^16, 2^18; seeds 1–2; r ∈ {0, 1, …, 1024}; p0 ∈ {0.3, 0.5}; γ ∈ {0, 0.5, 1, 2}.
- M is from the 8X FFT grid plus golden-section refinement (UNCERTIFIED).
| r (γ >= 1) | R at X = 2^14 → 2^16 → 2^18 | β₃ (bulk share at <= 3√n) |
|---|---|---|
| 0 (Bernoulli) | 2.3–2.8 → 2.5–2.8 → 2.9–3.0 | 0.63–0.80 |
| 1 | 17–51 → doubles → doubles (linear M) | 0.03–0.10 |
| 4 | 20–25 → ×2 → ×2 | 0.13–0.30 |
| 64 | 6–8 → 11–14 → 22–26 | 0.30–0.57 |
| 1024 | 3.1–3.9 → 4.7–6.0 → 8–11 | 0.35–0.80 |
Reading:
- Every fixed rank gives linear M: R ∝ √X, as P53 predicts for macroscopic non-PD profiles. Front-loading the
  density τ(t) makes level 1 PD but not the higher Hermite levels. Those levels' sidelobes have height ~X·r^{−k/2}.
- High rank approaches the Bernoulli baseline from above and never beats it.
- Spike domination (small β₃) comes only with linear M.
- So the simplest member of the reduction's escape class (multiscale Bohr, growing rank) is NOT a construction
  route. This matches the heuristic PD/Hermite tension: PD up to level K needs τ >~ 2√K, which puts the variance at
  degree ~τ² > K, i.e. in the bulk.
- Best rows at X = 2^18 are all Bernoulli (r = 0, γ = 1–2): R = 2.72–3.10.

## E74 (2026-10-19) Run-top counts against K² (src/e74_runtops.py; examples/e74/e74.jsonl, 45 sets)
- Definitions: A' = A ∪ −A, B_t = right endpoints of maximal t-progressions in A' (Bu et al. Prop. 9.1),
  K = 2λ (λ from the grid), μ = ‖F‖₁.
- Purpose: test the alternative mechanism. For dense sets, T-dense ⟺ mean_{t<=2X}|B_t| <~ K², because
  Σ_t|B_t| >= N²/4 (Lemma 9.6). Bu et al. bound each |B_t| by C₁K³μ.
- NUMERICAL (grid λ):
| family | mean_t|B_t|/K² | max_t|B_t|/K² |
|---|---|---|
| Bu q = 7…43 | 0.11–0.15 | 0.24–0.33 (stable in q) |
| Singer differences q = 13…61 | 0.158–0.163 | 0.33–0.34 |
| small-N optima N = 24, 30, 36 | 0.28–0.32 | 0.60–0.65 |
| E68 rows | 0.06–0.22 | 0.13–0.50 |
| E72c rows (C = 2.4–10) | 0.014–0.08 | 0.05–0.18 |
| intervals / uniform random (linear M) | <= 0.01 | <= 0.02 |
- max|B_t|/(K³μ) <= 0.027 everywhere (Bu et al.'s constant is C₁ = 2·10⁵).
- Reading:
  - On every near-optimal set, even the PER-t run-top count stays below 0.65K².
  - A Z-specific per-t bound |B_t| <~ K² would give exponent 1/3 for all A (Shankar's averaging) and √n for dense A.
    But it contains the open OR(2) two-run problem (A = S ∪ (S + t)), and P22 shows its group analogue is false
    (K⁴).
  - Consistent with T-dense; no new obstruction.
  - Uniform random subsets have LINEAR M (flat profile ⇒ Dirichlet sidelobes; R = 0.217√n), so their small ratios
    carry no information.
