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
## E19 (2026-10-18) Bu-class checks for P15/P16 (src/bu_halfsquare.py on F4; src/p16_constants.py)
   Identity f_{A(S)} = P^2 − k/2 − C/2 holds to 4e−8 on all certified Bu sets; E[C^4] = 3k^2/4 − 3k/8 EXACTLY (k=12..80);
   visit lemma: every window of the P16 size contains |P| < δ (100% of windows, η = .3, .5). Bu minima sit at near-zeros
   of P with C ≈ +2√k..2.7√k (excess = C/2 − P^2 ≈ 1.0–1.37√k; mean of C over zeros of P ≈ −0.1√k).
   E9 update (Bu-class SA, examples/bu_class/runs.jsonl): k=24 R=0.6829, k=32 0.6796, k=40 0.6787 (excess 0.83–1.08√k).
