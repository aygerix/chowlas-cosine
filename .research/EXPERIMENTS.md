# Experiments (exact tests, seeds, outputs)

## 2026-10-21 — L25, scalar caps and integrated GPU projected proposals

[Derivation, exact scopes and reproduction commands](notes/cstar_l25_gpu_cycle_2026-10-21.md).
Data: experiments/l25_2026-10-21/{probe,scalar_barrier,scalar_singer,projected_cpu,
projected_cpu_verification,projected_gpu,projected_gpu_verification,projected_pod_cpu}.json.
Sources: src/cstar_l25_probe.py, cstar_scalar_moment_barrier.py,
cstar_gpu_projected.py and cstar_projected_verify.py. All ordinary research
and exact certification ran on Dirichlet. One RunPodL4 worker, now DELETED,
ran CPU/GPU proposals with seed20261021. All jobs terminal.

The n496/8128 Singer inputs have exact full-degree4 caps13.7233/31.3755
and escaped exact M lower15.091991495/58.53525904, with exact square-identity
M upper16/64. Scalar moments are independently recounted through9 on
these inputs; older plateau recount only through7. Broader witness moments
have a separate signed packed-integer square check. Arb global L1 brackets
certify L25 on both; the large interval has small L1 but fails the low-M
hypothesis. Other Singer trend values are numerical only. No universal
convergence, matrix optimum or Chowla conclusion is inferred.

Follow-on source cstar_inverse_residual.py brackets OP140 by a rational CG
proposal's rigorously enclosed residual; FLINT2Cw matches independent Python
products. inverse_residual.json covers singleton/p31/p127. The selected
p509 high-triple test (tau780.35>552,n129795) exited0/PASS, J/sqrt(n) in
[0.157044006,0.157044015]. Full record is inverse_high_triples.json.gz,
retrieved explicitly after exceeding the wrapper's20MB limit. Reproduce:
`src/dirun.sh -c 2 -m 8 -t 180 python src/cstar_inverse_residual.py --primes 509 --output .research/experiments/l25_2026-10-21/inverse_high_triples.json`.
Weighted Fejer X120000 rigorously fails the coefficient-relaxed OP140;
it is labeled Boolean=false. No new GPU run, no universal conclusion.

## 2026-10-20 — arbitrary-support prefix spaces and fixed coupling

[Definitions, controls and limitations](notes/cstar_arbitrary_coupling_2026-10-20.md). Data: `experiments/ordered_prefix_2026-10-20/`, results.json, extra.json, verification.json, coupling.json, coupling_verification.json. Run `src/dirun.sh -c 2 -m 8 -t 480 python src/cstar_ordered_prefix.py` (also --extra), cstar_ordered_prefix_verify.py, cstar_coupling_ball.py and cstar_coupling_ball_verify.py. Sparse seed20261023; other inputs explicit/saved. Both verifiers exited0/PASS; all jobs terminal.

Fifty scalar Rayleigh witnesses cover19 Boolean sets and six weighted controls in two spaces. Twenty fixed-coupling witnesses independently have a=n,Q<=25n,H<0. Eight exact interval checks and three rational period-five control checks pass. Nearest binary controls are progressions with n7,14,28,max A35,70,140,M>7n/33 and trivial all-circle M<=n. Weighted controls are not Chowla sets. An extra-suite checkpoint TypeError from variable shadowing was repaired after confirmed termination; final data are checked. No numerical optimality, exact Gram-rank, universal theorem or exponent gain is asserted.

## 2026-10-20 — frozen references, profile mismatch and sharp ruling counts

[Paper results and exact limitations](notes/cstar_sidon_deterministic_2026-10-20.md). Data: `experiments/sidon_cutoff_2026-10-20/`. All computations on Dirichlet. Sources `cstar_sidon_cutoff.py`/`_verify.py`, `cstar_cyclic_sidon_probe.py`, `cstar_sidon_profile_probe.py`/`_verify.py`, `cstar_sidon_partial.py`, `cstar_ruling_triples.py`, `cstar_ruling_count_verify.py`. Run via `src/dirun.sh -c 2 -m 8 -t 480 python src/<script>`; profile arc adds `--arc`, windowed construction adds `--window`. All jobs terminal.

- Frozen references at (X,cutoff squared)=(64,2),(256,2),(256,4),(1024,4) keep actual hashes/n unchanged and certify ratios>0.2364/0.2516/0.2134/0.2453. At X64 the independent four-coordinate count gives H66498, including520 from frozen actual targets. Larger cubics have exact correlation/algebra checks, not independent complete recounts. Their finite cutoffs and sizes do not meet the conservative asymptotic sufficient condition.
- Exact profile-cost probes at p31/61/127/251/509: half-interval actual fibers with isotropic references have certified conditional H/p^3 lower bounds about0.0511/0.1206/0.2214/0.4327/0.8744. Matched horizontal references reduce the front defect; on quadratic-arc selections that projection alone fails. p31 mean-cubics are independently counted directly, all variances/lower inequalities rechecked, and p7 reference laws summed directly by a separate program. These costs are NOT Chowla counterexample ratios.
- Concrete Boolean partial/windowed sets use base385, n874/394, max A2342103225/1199584925. Full four-coordinate cubic recounts give (a,Q,H)=(712,1424,10918)/(434,868,5070), global M lower1541990599/200000000 and241942561/40000000, square-identity global upper76/55. Frequencies: `partial_A.txt`, `windowed_A.txt`, hashes and bounds in `profile_verification.json`. Window-cardinality trimming/padding is independently reconstructed.
- Complete normalized cyclic-Sidon searches p3/5/7 yield totals72/600/2352 (finite-only classification). Ruling weights computed exactly/with192-bit balls for U2..16; D(U)/U^2 is about8.6049 at U16. Direct FOUR-coordinate controls give ordered off-left counts432/3840/16848 at (X,U)=(4,2),(6,3),(8,4), matching the primitive-relation formula.451 independent-vector lattice cases pass the area bound. The uniform U^2 log U theorem is proved analytically, not inferred from data.
- Four proof/Lean review launches failed with the unavailable configured model. All finite certificate statuses and incomplete-independent-recount scopes are preserved in the JSON; no unrestricted theorem or novelty claim.

## 2026-10-20 — Boolean Sidon fibers, exact mixed cubics and conditional populations

[Definitions, proof and scope](notes/cstar_sidon_mixed_2026-10-20.md); data in `experiments/sidon_fibers_2026-10-20/`. All jobs use `src/dirun.sh -c 2 -m 8 -t 480 python src/<script>.py`: `cstar_sidon_fibers`, `cstar_sidon_mixed`, `cstar_sidon_verify`, `cstar_sidon_population`, `cstar_sidon_lemmas_verify`. Population extra: `cstar_sidon_population.py 11`; independent extra recount: `cstar_sidon_lemmas_verify.py --extra`. Seeds are saved per case (20261021+X+rotated for realizations; 20261031+X+rotated for references).

Rotated cases X64/256/1024, U=floor(X^(1/3)), have n3952/81794/1585878 and certified negative-point ratios>1.7533/1.9602/1.8541. The additional unrotated X256 control has a stronger content defect. Reverse-parameter endpoint reconstruction matches all hashes/cardinalities/max frequencies, independently reconstructs every modulus2..128 average by Mobius inversion, and directly rechecks scalar sums with192-bit Arb. Right-plane FFT points remain numerical minima; selected positive Fejer plane lower certificates are rigorous, no global right-plane upper bounds.

Three integer mixed cubics (X64 rotated, X256 unrotated/rotated) give (a,Q,H)=(4558,9116,162998),(92916,185832,14878870),(92032,184064,12940846). Exact rational polynomial negativity yields global M/sqrt(n)>0.31518/0.31328/0.31857. X64 has an independent four-coordinate recount; X256 does not claim that extra recount. The finite probes use U=X^(1/3), wider than the asymptotic theorem, and do not test its conservative threshold.

Exhaustive p3/5/7 affine-parabola populations contain72/600/2352 sets; separate implicit-graph enumeration and sparse convolution recount ALL conditional costs/certificates. Max conditional H/p^3=118/243,11212/9375,83159/67228. The p11 extra contains14520 sets with max1643756/805255 and also has a full independent sparse recount. Thus C=2 is REFUTED by the saved p11 maximizer, with exact gap33246/605 above2p^3. These are finite maxima, not an all-prime bound. Data: `population*.json`, `lemmas*_verification.json`, plus `results.json`, `mixed.json`, `verification.json`. One proof/Lean-agent launch failed with the unavailable configured model. All research computations were on Dirichlet; all jobs terminal.

## 2026-10-20 — widened means, changed center laws, and short-factor residue checks

[Full definitions and limits](notes/cstar_wide_parity_2026-10-20.md); data in `experiments/wide_mean_2026-10-20/`. All computation on Dirichlet. Commands: `src/dirun.sh -c 2 -m 8 -t 480 python src/cstar_wide_mean.py`, then `cstar_parity_mean.py`, `cstar_wide_mean_verify.py`, `cstar_center_law_lp.py`, `cstar_residue_mean_verify.py`; `cstar_short_factor_probe.py` uses timeout240. These are deterministic probes with no random seeds. All jobs terminal and checks pass.

- Six widened profiles X=256,1024,4096, sigma in{1,3/4,1/2}: cyclic and per-fiber heat-maximizing radii. Independent Gaussian/192-bit checks give M(mean) lower bounds; parity ratios at X4096 exceed28.878 and38.118. Three near-linear, parity-resistant radius assignments give mean ratios>12.125,25.772,89.788. These are fractional profiles, NOT Boolean sets. Two sources share disk statistics; the verifier imports neither and uses independent row counts/alternating sums. A negative-exponent integer-power issue in the initial verifier produced floats; it was corrected to integer parity signs before the passing run.
- Three Gurobi center laws R=8,16,32, D4 orbits, exact expected masses4758/197,79054/797,1285672/3209: all parity values become nonnegative. Endpoint-pair reconstruction confirms rational laws/mass and Arb negative-point M(mean)>0.4871,0.4888,0.4535. A561-point grid objective is NOT an all-phase upper bound; numerical LP optimality is not promoted to an exact optimum claim.
- Exact GL2 histograms at p=2,3,5,7,11 check rank-one average -1/(p^2-1), positive zero/rank-two countercontrols and the scalar-transfer constant. Two deliberately incomplete-fiber Boolean sets at X16,64 have n592,15320, max A415831654172258 and490283659859416061612, with two scalar evaluation conventions and certified point ratios>3.8315,3.9424. Frequencies exceed the practical Epoch verifier range; these are mechanism probes, not submissions.
- Saved certificates: `verification.json`, `residue_verification.json`, `boolean_residue.json`; raw assignments/laws: `results.json`, `parity.json`, `center_law.json`. The two configured reviewer launches failed; no independent-agent/Lean audit completed.

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
- Final (2400 s each, status 9 = time limit):
  - k = 6, Mt = 1.15·M(D): |E| = 2 ({64, 80}), bound 69;
  - k = 7, Mt = 1.05·M(D): E = ∅, bound 94;
  - k = 7, Mt = 1.15·M(D): |E| = 1 ({157}).
  Stacking a second Bu step buys at most 1–2 elements even at 15% slack.
- E65 completed: q = 19, λ = 2: 1.80. q = 23: 1.72 / 1.75 / 1.80 / 1.84. The penalty for λ > 1 keeps growing with q,
  and every λ > 1 has R >= 0.98 (q = 19, 23).

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

## E75 (2026-10-19) Adversarial annealing against per-t RT2 (src/e75_runtop_sa.c, src/e75_batch.sh; examples/e75/e75.jsonl)
- Objective: MAXIMISE Q(A) = max_t |B_t(A')| / K_grid² over A ⊂ [1, X], |A| = n, by swap annealing (200k moves, 3
  restarts per (X, n), seeds in the batch file). Grid λ on 8X + 1 points: UNCERTIFIED, HEURISTIC search.
- Results (best Q per (X, n); R_grid of that set):
| X | n | best Q | R_grid |
|---|---|---|---|
| 60 | 20 | 0.389 | 0.76 |
| 120 | 30 | 0.230 | 0.93 |
| 120 | 60 | 0.348 | 0.76 |
| 200 | 40 | 0.224 | 0.94 |
| 200 | 100 | 0.361 | 0.74 |
| 300 | 60 | 0.171 | 1.06 |
| 400 | 80 | 0.144 | 1.12 |
- Reading: no RT2 violation. The annealer does WORSE than the small-N optima of E74 (max 0.65), so maximising |B_t|
  pushes K up faster than |B_t|. Q falls with X at density 1/5. Weak evidence only (search-limited).

## E76 (2026-10-19) Fourier anatomy of run-tops: is Bu et al.'s per-t split saturated? (src/e76_q1q2.py;
## examples/e76/e76.jsonl, 23 sets)
- Per t <= 2X: g = 1̂_{B_t} on a 16(2X+1)-point grid, u = F + K >= 0 (mean K), proxy split Q1 = min(|g|, 3u),
  Q2 = (|g| − 3u)₊ (a clipping proxy for Lemma 9.3, NOT its exact split). Averages over t. NUMERICAL.
| family | n | R | mean|B_t|/K² | mean‖g‖₁/K | s1 = mean‖Q1‖₁²/K² | budget use |
|---|---|---|---|---|---|---|
| small-N 24 / 36 | 24 / 36 | 0.58 / 0.57 | 0.29 / 0.32 | 0.39 / 0.41 | 0.161 / 0.161 | 0.077 / 0.063 |
| Bu q = 7…31 | 56…992 | 0.80…0.66 | 0.10…0.15 | 0.22…0.26 | 0.062…0.085 | 0.019 → 0.0016 |
| Singer diff q = 13/23/43 | 91…946 | 0.73…0.72 | 0.162 | 0.27 | 0.080…0.088 | 0.018 → 0.0022 |
| E68 rows | 64 | 1.17–1.26 | 0.06–0.07 | 0.12–0.14 | 0.015–0.022 | 0.034–0.049 |
| E72c rows (C ≈ 2.4–5) | 128/512 | 0.94–0.99 | 0.04–0.08 | 0.12–0.18 | 0.025–0.043 | 0.002–0.007 |
| tapered random | 128/518 | 1.51/1.71 | 0.027/0.023 | 0.11/0.10 | 0.017/0.014 | 0.005/0.001 |
| interval | 128/512 | 2.5/4.9 | 0.020/0.005 | 0.048/0.015 | 0.002/0.0002 | 0.047/0.028 |
- s2 = mean‖Q2‖₂²/(K³μ) <= 5·10⁻⁴ everywhere: Q2 is negligible, Q1 ≈ g.
- Reading:
  - ‖1̂_{B_t}‖₁ ≈ 0.24K ≈ 0.7·√|B_t| on Bu sets: 1̂_{B_t} is NOT concentrated (a Gaussian-like spread would give 0.89).
  - Hence Σ_t Kμ‖Q1_t‖₁² ≈ 0.45·nK³μ on Bu sets (q = 7…31), with no decay in K. The round-6 "averaged sufficient
    inequality" Σ_t[‖Q2_t‖² + Kμ‖Q1_t‖₁²] <= D n K^{3−η}μ is FALSE for this split on the sets nearest the conjectured
    extremum.
  - Actual |B_t| uses 0.2%–8% of the per-t budget Kμ‖Q1‖₁² + ‖Q2‖², falling like 1/(Kμ). The loss sits in the
    per-t inequality itself (the factor Kμ), not in a lack of averaging.

## E77 (2026-10-19) Zero-set strengthening S(A) = sup{μ : μ + Σ_{a∈A} z^a has a zero in |z| < 1} (src/e77_winding.py;
## examples/e77/e77.jsonl)
- S <= M always (G(D) ⊂ {Re w > −M}). W(μ) is computed by the argument principle on a 64X-point sample of
  G(e^{ix}); S by a 600-point μ-scan from M down, then bisection. NUMERICAL.
  - Cross-check for X <= 120: numpy.roots at 0.98S / 1.02S gives (zeros inside > 0, 0) on every row.
  - A first version based on crossing bookkeeping was WRONG: grid points landed on exact zeros of G for intervals.
    It was replaced, and the results below are from the corrected run.
| family | S/√n | S/M |
|---|---|---|
| small-N optima N = 10…100 | 0.55–0.66 | 0.82–1.00 (mostly >= 0.95) |
| Bu q = 7…31; Singer diff q = 13/23/43 | 0.63–0.80; 0.72–0.73 | 0.95–1.00; 0.995–1.000 |
| E68, E72c (C = 3, 6) | 0.91–1.26 | 0.90–1.00 |
| random C = 1.5 / 3 / 10 (n = 64…1024) | 1.4–2.7 | 0.22–0.98 (falls with n) |
| interval [1, n] (n = 64, 256) | 1/√n exactly (S = 1.000) | 0.069, 0.018 |
| evens ∪ {1} (n = 64, 256) | 0.32, 0.16 (S ≈ 2.6) | 0.17, 0.05 |
| interval far [5n, 6n) | 7.9, 15.8 | 1.000 |
- Reading:
  - Chowla-S (S >= c√n) is FALSE: exactly for intervals (Re G = −1 at every nontrivial zero of Im G).
  - On every near-extremal set S ≈ M: the global minimum sits at a crossing of the negative real axis by G(e^{ix}).

## E78 (2026-10-19) The doubly-positive constant ρ* = sup ∫q²/(q(0)∫q) (src/e78_doubly_positive.py; examples/e78/e78.jsonl)
- Why: T-dense(C) holds for C < (2/r)(1 + √(1 − ρ*))² (PROOFS P58). Proved ρ* <= 0.90565 (P17(a)); E16 (session 2)
  estimated 0.7239 (h >= 0) and 0.7245 (signed).
- NUMERICAL:
  - Reference values: Gaussian 0.70711, triangle 0.66667, half-sine autocorrelation π²/24 + 5/16 = 0.723734 (quadrature
    0.723733).
  - (a) Autocorrelation class q = g ∗ g̃, g >= 0 on 200 points, L-BFGS: all 29 starts (half-sine, flat, Gaussian,
    parabola, sin², 24 random) converge to J = 0.72386–0.72387. Best 0.7238707.
  - (b) General piecewise-linear doubly-positive q (PD sampled on 16B points), Dinkelbach + Gurobi NonConvex:
    B = 24 gives 0.722967 (converged, gap 6e-6); B = 40 gives 0.723189 after one step. The sampled symbol dips to
    −0.0014, so (b) is a slight relaxation.
  - So the general class does not beat the autocorrelation class at these resolutions.
- Reading: ρ* ≈ 0.7239, so the sharp macroscopic reach is C ≈ 2.598·(1 + √0.2761)² ≈ 6.046. That matches the round-7
  exact witness at 6.0539.

## E79 (2026-10-19) Lead's independent checks of round 8 (src/e79_r8_checks.py; examples/e79/e79_checks.json)
- (A) ρ* potential certificate (P59.4), re-evaluated independently of the agent's code: the inequality holds on a
  200001-point float grid and on a 2001-point exact-rational grid (min = 0 at x = 0); β' >= 0.304 on [−0.001, 1].
- (B) Energy-PD on the ρ*-extremal shape p = a·q (q = half-sine autocorrelation, support [0,1]): min_y ∫_0^1 e(t)cos(ty)dt
  = −0.0094 (a = ½), −0.0073 (a = 0.45), −0.0055 (a = 0.4), all near y ≈ 8. So the doubly-positive extremiser is NOT
  admissible in the enlarged class {p PD, p(1 − p) PD}, and that class's reach exceeds 4(2 − ρ*)/r ≈ 6.63.

## E80 (2026-10-19) Two-profile ("enlarged") class reach by SLSQP (src/e80_enlarged_reach.py; examples/e80/e80.jsonl)
- Setup: maximize d over p = a·q(t/φ) with q the autocorrelation of g = exp(z) (NG = 30 cells). Constraints:
  e = p(1 − p) PD (cosine transform sampled at 1600 y ∈ [0.05, 160]); windows on p and e at 43 θ ∈ (0, 1];
  r = 4/(3√3).
- PARTIAL. Seeds 0, 1, 2 finished (SLSQP "success" false each time; constraints satisfied to sampling accuracy):
  - seed 0: d = 0.138658 (C = 7.212), a = 0.4968, min FT_e = −8e−11;
  - seed 1: C = 7.894;
  - seed 2: C = 8.608.
  Then the run CRASHED (overflow in exp(z)). Not rerun.
- Reading: seed 0 suggests the two-profile reach may be ≈ 7.21, below round 9's 7.2674 local optimum (P60.5). It is
  unverified (sampled constraints). SUPERSEDED: the two-profile class is a relaxation of the exact second-order class
  (P61, E82).

## E81 (2026-10-19) Lead's independent re-check of round 9 (src/e81_r9_verify.py; examples/e81/e81_verify.json)
- Method: exact-rational Taylor models with interval subdivision. This differs from the agent's Bernstein + SymPy
  Sturm.
- (A) All 18 supporting-line polynomials are > 0 on [−1, 1] (14–52 leaves each); λ_n >= 0.
- (B) Degree-24 scalar certificate (κ = 749089/10⁶):
  - all 29 leaves pass; the u = 1 leaf is divided by (1 − u);
  - β' > 0 on [−10⁻⁵, 1] (13 leaves);
  - Bernstein form equals power form exactly;
  - branches 3–20 are exactly the 18 lines;
  - leaves cover [0,1]; branch arguments are >= −10⁻⁵.
  (The first run flagged L <= 1 on [0, 1/16]: my checker demanded strict inequality where L(0) = 1. Only the lower
  range is needed.)
- (C) C = 4·10¹²/576649461289 exactly; r² > 16/27; the rational 6.9366 is OK; elementary r = 0.811 gives 6.58424.
- (D) 160-cell witness: q_i recomputed from the integer factor (exact match). d = 0.137600814820021222977… by
  closed-form cell integrals in mpmath (60 digits), so 1/d = 7.26739882542104 < 7.267398825422.
- (E) Horn form of the CP-obstruction profile: −0.00118031835777388 (mpmath).

## E82 (2026-10-19) The exact second-order constant D (src/e82_cp_reach.py; examples/e82/e82*.jsonl)
- Setup: maximize ∫_0^1 φ(w²), φ(x) = (1 − √(1 − x))/2, over w = G ⋆ G̃. G >= 0 is a step function on N cells of
  [0,1] with ∫G² = 1, so w is the exact PWL interpolation of the discrete autocorrelation (a genuine member of 𝒲).
  The objective uses 16-point Gauss–Legendre per cell. L-BFGS-B. Starts: constant, half-sine, centre-peaked, 2 random.
- NUMERICAL (all starts agree at each N):
  | N | D | 1/D | ∫_0^1 w² |
  | --- | --- | --- | --- |
  | 20 | 0.1163413 | 8.5954 | 0.3407 |
  | 40 | 0.1165803 | 8.5778 | 0.3402 |
  | 80 | 0.1166500 | 8.5727 | 0.3401 |
  | 160 | 0.1166694 | 8.5712 | 0.34005 |
  | 320 | 0.1166747 | 8.5708 | 0.34004 |
- Windows (sanity, r = 4/(3√3)): every P31 density and energy window holds on the optimiser, as they must, since
  escapes are genuine.
- Triangle check: (1 − π/4)/2 = 0.1073009 reproduced to 2e−9.
- Shape: G* is a symmetric bump with G*(0)/G*(½) = 0.381 and ∫G* = 0.9777.
- Companion modes (E82_MODE):
  - N2 = sup ∫_0^1 w²: 0.343456 (N = 40), 0.343482 (80), 0.343488 (160). Beckner's rigorous bound is 0.384900.
  - ratio κ_w = sup ∫φ(w²)/∫w²: 0.354845 (40), 0.355525 (80), 0.355747 (160), still rising; the maximiser's ∫w²
    shrinks (0.268 → 0.255).

## E83 (2026-10-19) Binarising the second-order extremal escape (src/e83_escape_binarise.py, src/e83_sa.c; examples/e83/e83.jsonl)
- Question: do binary sets seeded from the D-extremal weighted escape (PROOFS P61(b)) keep any of its positivity?
- Setup:
  - Profile p = φ(w*²) from the E82 optimiser (C = 1/D ≈ 8.57). Weighted escape with J = X^{0.6} random packets.
  - Binary seeds with identical block counts round(Σp) per block of 16:
    - "escape": the top values of p + r in each block;
    - "random": uniform within each block.
  - Block-preserving SA: 4·10⁶ moves × 3 restarts (2·10⁶ at X = 4096), T0 = 0.3, grid G = 8X + 1.
  - HEURISTIC (grid minima).
  - Run 1 (rows without the "seeding" key) used clipped-Bernoulli seeds that inflated the escape density (C ≈ 5.5–6.2).
    It is confounded and kept only for the record.
- Run 2 (fair; C = 8.57–8.61):
  | X | n | weighted escape R | escape seed: R_init → R_best | random seed: R_init → R_best |
  | --- | --- | --- | --- | --- |
  | 1024 | 119 | 0.261 / 0.285 | 1.82 → 1.103, 1.78 → 1.126 | 1.88 → 1.133, 1.95 → 1.125 |
  | 2048 | 239 | 0.243 / 0.243 | 1.91 → 1.194, 1.53 → 1.189 | 2.08 → 1.217, 2.47 → 1.207 |
  | 4096 | 478 | 0.208 / 0.208 | 1.85 → 1.338, 1.85 → 1.302 | 2.33 → 1.318, 2.15 → 1.315 |
- Reading:
  - Escape seeds start lower but end at the SAME R as random seeds.
  - R_best rises with X (search-limited, like E59), while the weighted escape falls (0.26 → 0.21).
  - This matches NOTEBOOK cont. 13.5: rounding random-centre packets costs O(1) non-binarity per coefficient, i.e. bulk
    energy, so P40 applies.
  - Binarisation needs weighted-PDS structure in the spike positions, not random packets.

## E84 (2026-10-19) Lead's independent re-check of the round-10 certificate D <= 1333/10000 (src/e84_r10_verify.py; examples/e84/e84_verify.json)
- Method:
  - Arb ball arithmetic (200 bits) directly in x, on [0, cap_jj] for each of the 128 half-cells; cap = cos(π/(k + 2))
    enclosed in Arb.
  - F(x) = a_j x + β_child(L) − β_j(x)/2 − φ(x²) >= 0, with L the max over the valid branches 0, 2x² − 1, x − √(1 − x)
    (each used only where it lies in [0, 1]).
  - Mean-value enclosures with adaptive bisection. On [0, 0.6] the check is on F(x)/x, since F(0) = 0.
  - Schur: my own exact piecewise-cubic integration of (T_a U)(x) for U = 1 + (4/5)x(1 − x), checked by exact rational
    Taylor models.
- Result:
  - betas monotone with β(0) = 0; a_j >= 0; power form equals Bernstein form;
  - 2475 pointwise leaves, 0 failures;
  - all 64 Schur cells pass with λ = 1333/5000.
  - So D <= 1333/10000 is confirmed, and T-dense(C < 7.5019) follows from P61(a).
## E85 (2026-10-19) Lead's independent re-check of the round-11 certificate D <= 259/2000 (src/e85_r11_verify.py; examples/e85/e85_verify.json)
- Method: E84's Arb-in-x pointwise check (200 bits; mean-value enclosures; adaptive bisection; F/x on [0, 0.6]), but
  with a branch set I derive myself rather than reading the certificate's per-cell branch list:
  - 0, Gram 2x² − 1, x − √(1 − x);
  - the 18 round-9 long lines (verified in E81);
  - support lines recomputed from the stored nodes and weights (A_n via exact Chebyshev recurrence, R-repair), each
    allowed only on half-cells with k >= k_jj = ⌈1/t_lo⌉ − 1.
  - Dominated lines are pruned. On each sub-interval the 6 branches highest at the midpoint are tried.
- Schur: my own exact piecewise-cubic integration (as E84), with λ = 2D₁ = 259/1000 and U = 1 + (4/5)x(1 − x).
- Result (VM, about 6 minutes):
  - all 188 support records re-derive (none bad; every stored line is implied);
  - β_j monotone with β(0) = 0; a_j >= 0; power form equals Bernstein form;
  - 22615 pointwise leaves, 0 failures. Branch use: 15256 lines, 131 √-branch, 87 Gram, 7141 zero;
  - support_k agrees with the certificate;
  - all 192 Schur cells pass.
- So D <= 259/2000 is confirmed, and T-dense(C < 2000/259 = 7.7220) follows from P61(a).
## E86 (2026-10-19, round-11 agent, VM) Fourth-moment and Paley probes (examples/r11_certificates/fourth_probe.*)
- Setup: E82 N = 320 factor rounded to integers (packet_factor.json); seed 2026101911; FFT grid >= 32(X + 1); Paley
  moduli 61 and 257.
- Results at X = 65536:
  - random packets (J = 776): fourth moment 0.0879 vs binary 0.1167; nearest-rounding energy 0.0508; FFT minimum −10.1;
  - positive Paley (q = 257): fourth 1.162, energy 0.0656, minimum −3.07 (Arb-bracketed);
  - Paley with the DC class deleted: fourth 0.058, minimum −977.2 (Arb).
- Residual cubes: random −0.00006 and Paley 0.187, against the required 0.0427.
- Nearest roundings of the random family (saved sets) give R > 1.7995 (X = 4096) and R > 1.9944 (X = 65536), with Arb
  point certificates.
- Reading: no tested weighted family has four binary profiles with a bounded fourth moment. Positive Paley
  overconcentrates on qZ; deletion loses both the lower bound and the cubic skew.
## E87 (2026-10-19) Where the round-11 certificate loses (src/e87_slack.py; examples/e87/e87.json)
- NUMERICAL. At the E82 optimiser w* (N = 320; ∫φ(w*²) = 0.1166747), the certificate's λ/2 = 0.1295 splits as follows:
  - Schur slack λ/2 − ∫a w* = 0.0030 (23%);
  - pointwise slack ∫(a w* − φ(w*²)) = 0.0098 (77%), after the potentials telescope.
- Per quarter of t, the linear term a·w* − φ(w*²) is −0.0064, +0.0063, +0.0073, +0.0026. The potentials move slack from
  t >= ¼ to the front, as designed, but the net loss is spread over t ∈ [¼, 1).
- The certificate's own worst case is the top eigenfunction G_a of T_a: ∫a w_a = 0.12938 ≈ λ/2, but ∫φ(w_a²) is only
  0.11118.
- Reading:
  - The bound is limited by the per-t LINEARIZATION of the convex φ(x²) under per-t constraints (caps and lattice
    lines), not by the Schur step.
  - Reaching 1/D ≈ 8.57 rigorously needs constraints coupling non-commensurable t (non-lattice Gram triples). The
    dilation family cannot supply them.
## E88 (2026-10-19) What FRONT-½ would buy: reach under a front cap p(0) <= a* (src/e82_cp_reach.py, E82_MODE=lam; src/e82_lam_batch.sh)
- NUMERICAL. Computes sup_w ∫_0^1 φ(λw²) with λ = 4a*(1 − a*), by E82's L-BFGS-B over step factors G (N = 80, 160).
  This is the second-order reach when the front density is capped (NOTEBOOK cont. 16.1). N = 160 values sit about 0.3%
  above the N -> ∞ limit, as for E82.
| a* | λ | sup ∫φ(λw²) | reach C |
|---|---|---|---|
| ½ (P61) | 1 | 0.11667 | 8.571 |
| 0.45 | 0.99 | 0.11418 | 8.758 |
| 0.40 | 0.96 | 0.10804 | 9.256 |
| 1/3 | 8/9 | 0.09598 | 10.419 |
| 0.30 | 0.84 | 0.08869 | 11.276 |
| 0.25 | 0.75 | 0.07648 | 13.075 |
| 0.2113 (Gaussian-kurtosis threshold) | 2/3 | 0.06617 | 15.114 |
- Reading:
  - A front cap is cheap to state and buys a lot: a* = 1/3 (the full-Haar kurtosis-3/2 threshold) gives T-dense(10.4).
  - The front is exactly where the cyclic barrier sits (cont. 16.3, 16.7).
## E89 (2026-10-19) Round 12: lead's falsification test of R12-N, plus the agent's probes (src/e89_r12n_check.py; examples/e89/e89.json; examples/r12_certificates/)
- Lead (NUMERICAL, falsification only; seed 2026101989). The test checks M(A) >= n/((3π + 2)r), or 2n/((3π + 2)r) for
  symmetric counts, when A ∩ NZ is an initial progression. Grid minima (FFT oversample 16, then golden-section
  refinement) only under-estimate M.
  - 538 cases: random nested and offset schedules (N = 3 … 101), adversarial l0 at the proof's balance point
    (symmetric and not), and l0 scans.
  - 0 violations. Worst ratio M_grid/bound = 1.262: a single class, i.e. a pure progression, where M ≈ 0.22n against the
    bound 0.175n. The balance-point families sit higher.
- Agent (VM; reproduction commands in the report):
  - roughness_probe.py (seed 2026101912): 36 structured removal schedules (coset, multiplicative, Bohr, random,
    Paley-front) at N = 29 … 257. Sampled μ√N runs 0.25–0.64. All keep square-root-sized dips.
  - schedule_milp.py (Gurobi 13.0.3, seed 1912): N = 29 optimal at 0.046092; N = 61 incumbent 0.033427, with lower
    bound 0.013233 at the 55 s limit.
  - Arb point certificates (220 bits) of actual dips: −5474 (N = 29, n = 28671), −8351 (61), −10139 (64),
    −32574 (257, n = 264192).
  - R12-U probe (seed 2026101913): M/H = 0.0730, 0.0360, 0.0342 at H = 2^16, 2^18, 2^20. Uncertified upper estimates.
  - independent_check.py: 980 exact second-moment count checks; 4 scalar-fake (R12-S) arithmetic checks.
## E90 (2026-10-19) Large-q search for symmetric half-sets of Z_q with small K (src/e90_zp_tabu.c; src/e90_calib*.sh, src/e90_prod.sh; examples/e90/)
- HEURISTIC (upper bounds on min K only). Same objective as E41: K = max_γ −λ(γ) over symmetric half-sets.
  - Method: tabu search with a soft-max surrogate at inverse temperature β/√q, best of 48 sampled swaps per step,
    200000 steps.
  - Seeds 2026101990+i.
  - Calibration: it reproduces the exact E41 optima at q = 79 (0.49064), 83 (0.48267) and 89 (K = 4.630072, β = 3).
  - CORRECTION to E41's printed q = 89 value 4.630071582: the pair list evaluates to 4.6300723 (the round-13 agent's
    Arb enclosure, 4.630072322; E90 agrees). The E41 file is unchanged.
- Production best K/√q, with Paley (1 + √q)/(2√q) in brackets:
  - 149: 0.5131 [0.5410]; 151: 0.5163; 197: 0.5296 [0.5356];
  - 293: 0.5524 [0.5292]; 401: 0.5756 [0.5250]; 601: 0.5774; 797: 0.5933; 1009: 0.6228;
  - 1201: 0.6289; 1601: 0.6122; 2003: 0.6575.
- Reading:
  - The search is weaker than E41c's core-plus-tail SA, which reached 0.4825 at q = 149. It finds nothing better than
    Paley for q >= 293.
  - Its sets have the profiled anatomy (Λ/q ≈ 0.25) with K/√q drifting up, like R13-PK's random profile rounding
    (K ~ √(q log q)). Paley's structured texture wins at large q.
  - INCONCLUSIVE about the asymptotics of min K/√q. Not continued.
  - Bug note: production runs did not record the seed state itself, so mode-2 rows show the best set after leaving
    Paley. This is fixed in the source.
## E91 (2026-10-19, round-13 agent, VM) Cyclic trade-off curves and binary-escape probes (examples/r13_certificates/)
- Reproduction: cyclic_probe.py, binary_probe.py, finalize.py (commands in the report). Gurobi seed 1913, 4 threads.
- Cyclic trade-offs Λ_max(κ) at q = 17, 37: exact staircases, by interval-enclosed enumeration of all 70 and 48620
  symmetric half-sets.
- Gurobi scans at q = 61, 89, 101, 109 (floating coefficients; q = 101 and 109 thresholds are incumbents only).
- R13-PK illustration, profile rounding with ε = 0.2. (K, Λ):
  - q = 257: (20.1, 28.8); 1021: (56.3, 77.8) — Arb-enclosed;
  - 4093: (138.7, 372.9); 16381: (252.4, 1626.2); 65537: (521.3, 6489.0) — FFT only.
- Binary escapes following the E82 profile, X up to 2^20: all R > 0.6 and increasing; each dip has a 220-bit Arb
  point certificate.
  - At X = 2^20, R ≈ 51.6 (Paley θ = ½), 18.6 (θ = ⅔), 2.93 (θ = 1), 43.1 / 141.6 (near-interval θ = ½ / 1),
    176 (spectral diffusion).
  - Gurobi rounding at X = 128, 256: R ≈ 0.90, 1.18.
  - The smooth profile contributes only −0.25 … −0.20 at each dip; the residual carries the whole dip.
- No new record. The constructive track's best certified R is unchanged (0.5537, E25).
## E92–E93 (2026-10-19) Third-order profiles and the cubic front cap (src/e92_third_profile_pd.py, src/e93_cubic_cap.py, src/e93b_cubic_reach.py; examples/e92, e93)
- E92 (NUMERICAL). At the P61 optimiser (E82, N = 320) the third-profile defect s = e(1 − 2p) is NOT PD: min FT −0.0195
  at ξ = 8.25, relative −0.23. The triangle gives −0.0123.
  - So PD gadgets (NOTEBOOK cont. 17.8) cannot supply it. p, e and p³ + 3pe are PD.
- E93 (NUMERICAL). At the D_{2/3} optimiser (E82 λ = 2/3, N = 160; a = 0.211325 = u*), the cubic profile
  g(p) = p(1 − p)(1 − 2p) has min FT −0.0022 at ξ = 9.1, against FT(0) = 0.084. So P66's cubic PD constraint binds
  beyond the front cap.
- E93b (NUMERICAL). Maximise ∫φ(σw²) over step G (N = 80) and σ <= 2/3, subject to FT[g(p)] >= 0 on ξ ∈ [0, 120], by a
  penalty method (μ = 1e2 … 1e6, L-BFGS-B, warm start from the E82 λ = 2/3 row).
  - Result: d = 0.064013, i.e. C = 15.62, with residual FT violation −7e−7.
  - The optimum keeps σ = 2/3 (a = u*).
  - Reading: the exponent-1/3 reach of "second order + cubic profile PD" is ≈ 15.6 numerically. The rigorous value
    is C < 12.294 (P66, Beckner).
## E94 (2026-10-19) Rigorous D_{2/3} by mixing the P63 and Beckner bounds (src/e94_mix_bound.py, src/e94b_mix_certify.py)
- E94 (Gurobi LP; numerical). Minimise α1(259/2000) + α2(2√3/9) subject to φ(2x/3) <= α1φ(x) + α2x on a grid of
  10⁴ points in [0, 1].
  - Optimum α1 = 0.233809, α2 = 0.117342, giving bound 0.075443 and C = 13.255.
  - The fine-grid slack is −7e−7, so the multipliers were bumped for the certificate.
- E94b (RIGOROUS, exact rationals). With α1 = 233809/10⁶ and α2 = 117344/10⁶:
  - G(x) = F(x)/x > 0 on [0, 1], certified on 910 bisection cells (minimum lower bound 4.9e−10);
  - D_{2/3} <= 0.07544399, so P66 holds for C < 13.254866.
- Rerun: `src/dirun.sh -c 1 python src/e94b_mix_certify.py` (pure Python, < 1 min).
## E95 (2026-10-19) D_σ discovery LP at σ = 2/3 (src/e95_discover_sigma.py, src/e95_run*.sh; examples/e95/)
- Code: P63's support-coupled Schur-test LP (examples/r11_certificates/discover.py) with φ(x²) replaced by φ(σx²).
  Only val, the output path and the σ argument change. Gurobi, 4 threads, about 11 s (K = 64) and 36 s (K = 192).
- σ = 1 reproduces P63's discovery value 0.1299369 exactly (K = 64, degree 10, shape 0.2).
- σ = 2/3 (NUMERICAL, discovery LP, not a certificate):

| K | degree | shape | D_{2/3} bound | C |
|---|---|---|---|---|
| 64 | 10 | 0.0 | 0.073256 | 13.65 |
| 64 | 10 | 0.05 | 0.072810 | 13.73 |
| 64 | 10 | 0.1 | 0.072516 | 13.79 |
| 64 | 10 | 0.2 | 0.073073 | 13.69 |
| 64 | 10 | 0.3 | 0.075394 | 13.26 |
| 64 | 10 | 0.5 | 0.083055 | 12.04 |
| 192 | 12 | 0.1 | 0.072338 | 13.82 |

- Reading:
  - The certificate family saturates near 0.0723 (C ≈ 13.8), against the true D_{2/3} ≈ 0.0662 (C ≈ 15.1, E82).
    The overshoot ratio is 1.09, comparable to σ = 1 (0.1292 against 0.1167).
  - Certifying it (porting certify.py) would move P66's rigorous range only from 13.25 (E94b) to about 13.8.
  - Not done. Low value per effort; it is a candidate mechanical task for an agent.
## E96 (2026-10-19) Degree-3 ("level 1.5") SOS / Sherali–Adams lower bound for cyclic half-sets (src/e96_sos15_halfset.py)
- Relaxation. Pseudo-moments up to degree 3, made dilation-invariant by averaging over G = Z_q^*/{±1} (legitimate: the
  problem is G-invariant and the relaxation is convex). Constraints:
  - Boolean reduction;
  - cardinality times every monomial of degree <= 2;
  - Sherali–Adams nonnegativity of all degree-3 products of x and 1 − x;
  - the degree-<=1 moment matrix is PSD;
  - ONE localizing matrix Ẽ[(λ(1) + K)·s·t] (s, t ∈ {1, x_j}) is PSD; the other γ follow by G-invariance.
- K multiplies pseudo-moments, so it is bisected over feasibility SDPs (Clarabel 0.11.1, cvxpy 1.9.3; NUMERICAL,
  tolerance 1e−3, not a certificate).
- Results. K_1.5(q) = 1.997, 1.757, 1.739, 1.714 for q = 13, 17, 29, 37. Exact K_min (E41) is 2.30 at q = 13 and
  2.56 at q = 17.
- Reading: the level-1.5 bound is O(1).
  - Mechanism (lead, paper): the product measure is excluded, since localizing with s = λ(1) − c forces K >= σ ≈ √q/2.
  - But a two-point pseudo-marginal for each λ(γ), with values {−K, ≈ cq} and mass ≈ 2K/(cq) on the top, matches the
    first two moments (variance q/4) for K ≈ 1/(4c) = O(1). The bound λ <= q/π needs high-degree Booleanity.
  - Pairwise products (λ(β) + K)(λ(β') + K) >= 0, summed symmetrically over γ, give only K² − K >= ¼. The real
    second-order argument needs the PEAK γ, i.e. a non-symmetric (max) step; in SOS form that means weighting by λ,
    which is third moments (the R12-S world).
- Conclusion: low-degree, symmetric SOS certificates cannot give growth. Do not use them as a Chowla route.
## E97 (2026-10-19) Round-15 certificate re-run by the lead (src/r15_rerun_lead.sh; examples/r15_certificates/)
- On the VM:
  - mixing_sturm.py: Sturm certificate for E94b reproduced;
  - certify_sigma.py (E95 K = 64, degree 10, shape 0.1 input): PROVED, D_{2/3} <= 73/1000, minimum Schur margin
    1704250072843/1966080000000000, 43 s;
  - verify_sigma.py (independent reconstruction): PROVED, 767 leaves, 127 caps, 64 Schur cells, 55 s.
- So P66 holds for C < 1000/73 = 13.6986 (P68.3).

## E99 (2026-10-19) Self-difference graph of near-extremal sets: a √n soft spectral edge (src/e99_selfgraph.py; examples/e99/e99.jsonl; VM, 4 cores)
NUMERICAL. M: FFT + Newton estimate (uncertified; it matches the stored certificates to ~1e-4). H = Cay(Z, ±A)[A]: vertices A, a ~ a' iff
|a − a'| ∈ A. P9 gives K = 2M >= −λ_min(H). Eigenvalues: LAPACK for n <= 3000, else Lanczos with an exact FFT matvec.
| family | n | max A/n | R | α (edge density of H) | λ_min(H)/√n | ρ = −λ_min(H)/K | IPR·n of bottom vector |
|---|---|---|---|---|---|---|---|
| small-N optimum | 36 / 50 / 80 / 100 | 1.4–1.5 | 0.565–0.665 | 0.79–0.90 | −0.58 … −0.72 | 0.47–0.61 | 2.2–4.0 |
| Singer–Bu (q = 61, 101, 151, 199) | 3782 → 39800 | 2.8–3.0 | 0.604 → 0.566 | 0.51–0.56 | −0.739, −0.732, −0.712, −0.721 | 0.611, 0.622, 0.616, 0.637 | 3.8–4.1 |
| Sidon differences (q = 31, 61) | 496 / 1891 | 2.0 | 0.718 / 0.713 | 0.66–0.69 | −0.623 / −0.613 | 0.434 / 0.430 | 2.8–2.9 |
| random, density ½ | 500 / 2000 | 2.0 | 4.0 / 9.0 (Gibbs) | 0.51 | −1.37 / −1.28 | 0.17 / 0.07 | 2.3 |
| random sparse, X = n^1.5 | 500 / 2000 | 22 / 45 | 4.3 / 8.7 | 0.04 / 0.02 | −0.43 / −0.30 | 0.05 / 0.02 | 4.0 |
| AP [1, n] | 500 / 2000 | 1 | 4.9 / 9.7 | 1 | −0.045 / −0.022 (H = J − I) | 0.005 | localized |
- (The row labelled `sumfree_odd` in the jsonl is a BUG: the list is the step-2 AP of EVEN numbers. Ignore it.)
Reading:
- On EVERY near-extremal set, the self-difference graph alone has a bottom edge ≈ −0.72√n (stable from n = 36 to 39800).
  - The bottom spectrum is a soft cluster (gaps 0.1–0.4), not an isolated outlier.
  - Its eigenvectors are delocalized (IPR·n ≈ 3–4, Gaussian-like) and orthogonal to 1_A (overlap ~1e-8).
  - So Cay[A] alone certifies ≈ 0.6K, i.e. M >= 0.36√n, on these sets.
  - This is a random-matrix SEMICIRCLE EDGE. The naive RMT prediction 2√(α(1−α)n) over-predicts by a factor ≈ 0.72/1.0
    for Singer–Bu, and is accurate (±15%) on the small-N optima.
- The star (vertex 0) adds nothing on near-extremal sets (w0 = 0). It dominates only for sparse random sets.
- The AP is the clique case: H = J − I has λ_min = −1, so its large M (Gibbs) is invisible to Cay[A]. This is the
  structured alternative.

## E99b / E99c (2026-10-19) Graph certificates on random sets of density α: flat versus PD-tapered profiles (src/e99b_sparse_gap.py, src/e99c_tapered.py; examples/e99/e99b.jsonl, e99c.jsonl; VM)
NUMERICAL. Random A of density α = n^{−e} in [1, X]. E99b uses a flat profile; E99c uses P(a ∈ A) = 2α(1 − a/X), a
triangle profile, which is PD. λ_min is computed on W0 = A and W2 = {0} ∪ ±A (P9: 2M >= −λ_min).
| profile | e | n ≈ 1000 / 4000 / 16000: λ_min(W2)/√n | λ_min(W2)/n^{1/3} | true R |
|---|---|---|---|---|
| flat | 1/2 | −0.89 / −0.89 / −0.88 | −2.8 / −3.6 / −4.4 | 6 / 15 / 28 |
| flat | 1/3 | −0.93 / −0.98 / −1.20 | −3.0 / −3.9 / −6.0 | 8 / 14 / 28 |
| flat | 1/4 | −1.52 / −1.75 / −2.56 | −4.8 / −7.0 / −12.8 | 7 / 14 / 28 |
| triangle | 1/2 | −0.74 / −0.75 / −0.74 | −2.4 / −3.0 / −3.7 | 2.7 / 3.0 / 3.6 |
| triangle | 1/3 | −1.04 / −0.78 / −0.62 | **−3.30 / −3.09 / −3.09** | 2.6 / 3.1 / 3.2 |
| triangle | 1/4 | −1.36 / −1.19 / −0.94 | −4.3 / −4.8 / −4.7 | 2.3 / 2.8 / 3.1 |
Reading:
- On flat sets, W2 certifies >~ √n at every density. A macroscopic negative eigenvalue (boundary/Gibbs) grows like αn.
- On PD-tapered sets at α = n^{−1/3}, the certificate is ≈ 3.1n^{1/3}: constant in units of n^{1/3}, decaying like
  n^{−1/6} in units of √n. This is the "intermediate region" of the external review, confirmed with exponent 1/3.
- These sets are not counterexamples: R ≈ 3, from random fluctuations (P28).
- On W0 = A the certificate tracks the noise bulk ≈ 2√(αn) on flat sets (E99b: 0.62√n at n = 1000, e = 1/3).

## E100 / E100b (2026-10-19) Positivity versus resolution for window arcs (src/e100_arc_resolution.py, src/e100b_pr_search.py; VM)
NUMERICAL.
- E100 (exact mpmath series): an arc of radius ρ = c/(2L) with all coefficients >= 0 up to L (true iff c <= 1) leaves
  a fraction δ_L of its ℓ² mass above frequency L:
  - c = 1: 0.09717 (L = 10), then 0.09718 for L = 100, 1000, 10⁴;
  - c = ½: 0.207 → 0.226;
  - c = ¼: 0.513 → 0.533.
- E100b: SLSQP, 300 random starts for each J = 1 … 6 symmetric arc pairs, L = 16, constraints 1̂(k) >= 0 for
  k <= 16 and |Ω| <= ½.
  - Minimum δ = 0.09713 at J = 2 (arcs at 0 and ½, a dilate of one arc).
  - Minimum δ = 0.0947 at J = 6 (period 1/11 with half density, i.e. the dilate of the L' = 1 problem:
    δ = ½ − 4/π²).
  - No window below 0.0947 was found. This supports PR(1) with c* = ½ − 4/π² (NOTEBOOK cont. 20.3).

## E103 (2026-10-19) Near-Boolean weight robustness (Ruzsa's [0.99, 1.01] question) (src/e103_weight_robust.py; VM; Gurobi)
NUMERICAL. The minimum is FFT + Newton (grid 2^⌈log₂ 32X⌉), not interval-certified. Gurobi LP with cutting planes, iterated
until LP value = true minimum to 1e-6 relative.
- Quantity. For fixed support A: M_τ = min over w ∈ [1−τ, 1+τ]^A of max_x −Σ w_a cos(ax). Normalization R_τ = M_τ/√(Σw²).
- Output: examples/e103/e103.jsonl (all rows; the first run's partial rows are kept too).
- Table of R_τ/R_0:

| family | n | X | R_0 | τ = 0.01 | τ = 0.1 | τ = 0.3 |
|---|---|---|---|---|---|---|
| Singer diff q = 13 | 91 | 181 | 0.734 | 0.969 | 0.842 | 0.770 |
| q = 19 | 190 | 379 | 0.726 | 0.972 | 0.865 | 0.736 |
| q = 23 | 276 | 551 | 0.722 | 0.969 | 0.856 | 0.735 |
| q = 31 | 496 | 991 | 0.718 | 0.972 | 0.845 | 0.701 |
| q = 43 | 946 | 1891 | 0.715 | 0.972 | 0.849 | 0.702 |
| Bu q = 61, k = 9 | 72 | 9468 | 0.911 | 0.958 | 0.919 | 0.919 |
| Bu q = 83, k = 20 | 380 | 16407 | 0.791 | 0.913 | 0.851 | 0.851 |
| random half, n = 100…800 | | 2n | 1.5 → 5.4 | 0.96–0.97 | 0.73 → 0.68 | 0.58 → 0.26 |
| interval [1, 200] | 200 | 200 | 3.12 | 0.973 | 0.720 | 0.236 |

- Weight pattern (Singer): about 55% of weights at 1 − τ; at the upper bound 15% (τ = 0.1) and about 2% (τ = 0.3).
- Reading.
  - On the flat algebraic families (Singer, Bu) near-Boolean weights buy only a CONSTANT factor. At τ = 0.3 the ratio
    plateaus at 0.70 (q = 31 → 43: 0.701 → 0.702). At τ = 0.1 it is 0.85 with no trend; at τ = 0.01 it is 0.97.
  - The initial slope gives min_{μ ∈ Opt₀} Σ_a |c_a(μ)| >= (M_0 − M_τ)/τ ≈ 2.1–2.4·√n on Singer (P72(c)). The optimal
    dual measures are A-spread: a point mass would give ≈ (2/π)n.
  - Random and interval sets drop a lot because their M_0 is boundary Gibbs (linear) and the weights partly taper it.
    In the continuum limit this is still linear for every τ < 1 (P72(e)).
  - The regime that matters for C* (spiky sets with M << √n) cannot be probed: no such sets are known.
- E103c (Singer q = 61, 83) was not run: the τ = 0.3 plateau was already flat from q = 31 to q = 43.

## E104 (2026-10-19) Do near-extremizers drift into the spiky (C*) regime? (src/e104_spikiness_trend.py; VM; examples/e104/e104.jsonl)
NUMERICAL (FFT grid 2^⌈log₂ 64X⌉, Newton-polished minimum). Quantities:
- β_K = ∫_{f<=K√n} f²/∫f² (SB);
- λ_half = |{f <= −M/2}|, the bimodality / flatness of the negative region;
- η = (∫|f|)²/∫f², the effective support.
Families: all stored small-N optima (n = 4…100), dense_certified (n = 20–150), Singer differences q = 7…61
(n = 28–1891), Bu q = 61, 83, 101.

| family | n range | R | β₁ | β₂ | λ_half | η |
|---|---|---|---|---|---|---|
| small-N optima | 20 → 100 | 0.60 → 0.565 (n = 36) → 0.665 | 0.20–0.30, no trend | 0.21–0.37 | 0.39 → 0.27 | 0.38 → 0.24–0.27 |
| dense_certified | 20 → 150 | 0.60 → 0.82 | 0.21–0.34 | 0.24–0.43 | 0.39 → 0.23 | 0.27–0.38 |
| Singer diff | 28 → 1891 | 0.756 → 0.713 | 0.31 → 0.24 | 0.35–0.43 | 0.25 → 0.20 | 0.355 → 0.205 |
| Bu | 72 → 506 | 0.91 → 0.79 | 0.31–0.34 | 0.55–0.59 | 0.23–0.32 | 0.47–0.50 |

Reading:
- No known near-extremizer drifts toward β -> 0. The bulk fraction stays at 0.2–0.6.
- Every known near-extremizer is FLAT: f <= −M/2 on 20–40% of the circle. P72(b) and P28 apply to all of them, and their
  √n is "flat" √n.
- The large top-1% share on dense sets (up to 0.75) is the CENTRAL spike (f(0) = n at width 1/X), not mesoscopic
  spikes.
- Singer's λ_half (0.25 -> 0.20) and η (0.36 -> 0.21) drift down slowly with q. Its |F_B|²/k value distribution is not
  converging fast to Exp(1), which would give λ_half = 0.39 and η = 0.54. Watch at larger q; R is unaffected.
- So the C* regime (spiky, M << √n) is empty of examples at every scale we can reach, consistent with SB and with
  Chowla being true.

## E105 (2026-10-19) PR(1) large-peak test (src/e105_pr_largepeak.py, src/e105_batch.sh; VM; examples/e105/e105.jsonl)
NUMERICAL, heuristic search: SLSQP over symmetric unions of J <= 8 arc pairs, 150 random starts per J.
- Minimize the unresolved fraction δ_L = U/|Ω| subject to: 1̂_Ω(k) >= 0 for 1 <= k <= L; |Ω| <= ½; peak g(0) >= γ,
  where g = P_L1_Ω.
- This is the case P73 does not cover.

| L | γ = 1.25 | γ = 4/3 | γ = 1.5 | γ = 2 |
|---|---|---|---|---|
| 8 | 0.0971 | 0.1037 | 0.1506 | no feasible point |
| 16 | 0.1179 | 0.1568 | 0.1552 | no feasible point |
| 32 | no feasible point | no feasible point | no feasible point | no feasible point |

Reading:
- In the large-peak regime the unresolved fraction is LARGER than the conjectured c* = ½ − 4/π² = 0.0947 and grows with
  γ. So the large-peak case is not where PR(1) could fail.
- γ = 2 was never reached. The witnesses at L = 8 are dilated half-density square waves (period ≈ 1/8, |Ω| = ½) whose
  fundamental sits at k ≈ L. That matches the cont. 24 analysis: a large peak needs structure at scale 1/L, which puts
  energy just above L.
- L = 32 found no feasible point at all. That is a SEARCH failure with <= 8 arcs, since peak >= 1.25 at L = 32 needs
  many arcs; it is inconclusive, not evidence.
- Next: a paper proof of the large-peak case. Route: Bernstein (a peak >= 4/3 forces |g − 1_Ω| >= 1/6 on an arc of
  length ~1/L) plus the identity ∫g(1 − g) = U. This closes the case when |Ω| <~ 1/L. For |Ω| >> 1/L, show a peak >= 4/3
  needs scale-1/L structure whose energy straddles k = L.

## E106 (2026-10-19) Sparse Pareto search β_K + μR (src/e106_batch.sh, src/e68_pareto_sa.c; analysis src/e106_anal.py; examples/e106/e106.jsonl, 24 rows)
- Boxes: n = 64 at X = 1280 (K = 1, 2) and X = 3200 (K = 2); n = 128 at X = 2560 (K = 2). μ ∈ {0.1, 0.2, 0.5}, 6e6 SA iterations, 2 restarts. Grid M (UNCERTIFIED).
- Result: every low-β set is a BEATTY DILATE of a dense near-interval, with one macroscopic spike pair of 0.85–0.98·n at an irrational-looking x₀ (e.g. A ≈ round(j/0.0916)). β = 0.24–0.42 with R = 0.85–1.06. The only R < 0.85 row is gcd(A) = 2, a dilated dense set (R = 0.635, β = 0.20, spike at ½).
- The sparse front (min R ≈ 0.85) is WORSE than the dense one (E68: β ≈ 0.18 at R ≈ 0.65). No mesoscopic spikes appear anywhere.
- Reading: the annealer reaches spikiness only through ONE macroscopic real dilation (bounded frame, F4). At n <= 128 there is no room for mesoscopic heights (√n = 8–11, n = 64–128), so E106 cannot probe C*. The kill test passed vacuously. Mesoscopic probes need structured families with large n → E107 (automatic sets).

## E107 (2026-10-19) Automatic sets: R screen and exact sector violation (src/e107_automatic.py, e107_sector.py, e107_batch.sh, e107_sector_batch.sh; examples/e107/)
- Class (CSTAR A2): A_L = {1 <= k < b^L : the base-b digits of k (MSB first, leading zeros allowed) are accepted by a
  deterministic automaton}, with δ(0,0) = 0 (nested family) and 1.05 < λ < b (sparse, n = X^α).
- R screen (grid minima, UNCERTIFIED; R at two depths L1 < L2):
  - Coverage: all automata with b = 2 (S <= 4), b = 3 (S <= 3), b = 4 (S = 2; S = 3 partial, ~100k), b = 5 (S = 2).
    168,226 sparse automata in total.
  - Result: NO automaton has R decreasing from L1 to L2. Best R(L2) ≈ 2.8 at n ≈ 150, and every R grows (linear M).
  - Fibbinary (no "11"): minimum at x ≈ 0.2506, next to the depth-2 spike ¼.
- Exact sector scan (asymptotic, no grid in x). D = max over (main profile, b-adic spikes of depth <= K) of
  −min_s Re[μ̂_k(j)ν̂(s)], and M_L >= (D − o(1))n_L.
  - Validation: Cantor D = 0.300 vs measured M/n = 0.299; Fibbinary D = 0.203 vs 0.21.
  - 11,868 automata, b <= 5, S <= 3 or 4.
  - min D = 0.102 overall:
    | class | min D |
    |---|---|
    | b=2, S=4 | 0.111 |
    | b=3, S=3 | 0.102 |
    | b=4, S=2 | 0.111 |
    | b=5, S=2 | 0.233 |
  - The binding constraint is almost always the MAIN profile h₀ = −min Re ν̂ >= 0.085. The front (top-digit Parry
    measure ν) is never PD. The best rows have λ close to b (b = 3, λ = 2.618).
- Reading: in small automata the FRONT already forces linear M. The b-adic sector conditions are not yet binding.
  E107c anneals larger automata (S = 4–10) to test whether D → 0 is reachable at all.

## E108 (2026-10-19) Finite-prefix certificates and the T-A2 tests for automatic sets (src/e108_fpc.py, e108_mu.py, e108_twin.py, e108_dom.py, e108_sum.py, e108_margin.py; examples/e108/ on dirichlet, NOT committed, 9–13 MB each)
- Input: examples/e107/sector_all.jsonl, 71,840 automata (b = 3: 213, b = 4: 58,377, b = 5: 13,250; S <= 3).
- E108a, FPC (advisor; python-flint arb/acb at 128 bits; λ is a rigorous root of charpoly(C), r from arb_mat solve).
  t is proposed by a float scan s ∈ [0.02, 20) and rounded to k/50, with h chosen so that 2π|t|/b^h <= |Re|/4.
  - Result: 71,840 / 71,840 CERTIFIED, Re ν̂(t) < bound_upper <= −0.0843 (worst: b = 5, t = 241/25, h = 5).
  - Fibbinary check: the advisor's −0.03182448 (t = 1, h = 8) is reproduced; h = 24 gives < −0.0578943.
  - Status: interval-certified (the float search only proposes t).
- E108b, stationary μ̂(j), j <= J (float). min_j Re μ̂(j) < 0 for ALL 71,840; the largest such minimum is −0.0106.
  The margin shrinks as α → 1.
- E108c, exact twins (equal state maps τ, gcd(m, b) = 1, p <= 4): 3,560 / 71,840.
- E108d, P75 domination-or-twin (float G, p <= 4, N = 40, twins combined by b | lcm of reduced denominators):
  - covered: 20,476 (dom 15,829, twin 4,647);
  - uncovered: 51,364 (b = 4: 43,435, mostly a single tie at u = 1/2; b = 5: 7,726 and b = 3: 203 with G < 0
    strictly, e.g. b = 3, δ = [[0,−1,1],[0,1,0]], λ = 1+√2, Gmax = −0.38).
- Reading: the finite class has NO survivor, rigorously. The general T-A2 needs a base-2 descent for the b = 4 ties
  and a >= 3-point Gram test for the strictly-dominated cases. A2 is closed as a design class (CSTAR A2 (viii)).

## E109 (2026-10-19) Residue-staircase profile check (src/e109_residue_taper.py Q X seed; dirichlet; grid M UNCERTIFIED)
- Class: W₀ ⊂ Z_Q random symmetric (density ½); u_r ~ U[0, 1] with u_{−r} = u_r; A = ∪_{r∈W₀}{a <= X : a ≡ r (mod Q), a < u_r X}.
- Prediction f(t/Q + τ/X) ≈ (X/(2πQτ))Σ_{r∈W₀}cos(2πrt/Q)sin(2πτu_r), checked at 16 points (t, τ) per run:
  | Q | X | n | max abs error | typical values | grid M | R | √(X/Q) |
  |---|---|---|---|---|---|---|---|
  | 31 | 2·10⁴ | 7264 | 1.65 | ~100 | 2762 | 32.4 | 25.4 |
  | 101 | 4·10⁴ | 16760 | 5.27 | ~100–300 | 3210 | 24.8 | 19.9 |
- Reading: the formula holds. Random staircases have R ≈ 1.3√(X/Q): rounding noise confined to the Q rational columns
  is amplified, not diluted (CSTAR A3, design rule D8).

## E110 (2026-10-19, cont. 28) DNN vs PSD square certificates (src/e110_dnn.py; examples/e110/)
- Computes, for A ⊂ [1, X]:
  - M_PSD = min tr Q subject to Q ⪰ 0 and diagonal sums Σ_iQ_{i,i+k} = ½·1_A(k). This equals M(A) up to solver
    tolerance.
  - M_DNN = the same with Q >= 0 entrywise added.
  NUMERICAL SDP (Clarabel for X <= 130, SCS beyond), not a certificate.
- Sets in the script:
  - N50_x72 / N50_x71;
  - dense_certified rows with max <= 200;
  - Singer Sidon differences q = 5, 7, 11, 13;
  - random sets (seed 20261019);
  - intervals [1, 30] and [1, 60].
- Usage: `python src/e110_dnn.py out.jsonl [names]`.
- SMOKE (dirichlet, examples/e110/e110_smoke.jsonl). M_psd matches the FFT-grid M to 1e−6 in both rows (sanity):
| set | n | X | M | M_DNN | ratio | rank(Q_psd, Q_dnn) |
|---|---|---|---|---|---|---|
| Singer differences q = 5 | 15 | 29 | 2.90254 | 2.97287 | 1.024 | 26, 17 |
| interval [1, 30] | 30 | 30 | 7.13162 | 7.13162 | 1.000 | 29, 29 |
- FULL RUN (cont. 29, examples/e110/e110.jsonl; X = 180 rows by SCS). DNN at MINIMAL degree [0, X] against M:
| set | n | X | R | R_DNN | ratio |
|---|---|---|---|---|---|
| N50_x72 | 50 | 72 | 0.570 | 0.570 | 1.0000 |
| N50_x71 | 50 | 68 | 0.573 | 0.589 | 1.029 |
| dense X30 / X50 / X80 / X120 / X180 (2 seeds each) | 20–122 | 28–180 | 0.60–0.75 | — | 1.000–1.099 |
| Singer differences q = 5 / 7 / 11 / 13 | 15–91 | 29–181 | 0.73–0.75 | — | 1.024 / 1.000 / 1.000 / 1.000 |
| random X = 80, p = ½ | 46 | 80 | 1.414 | 1.414 | 1.000 |
- Reading:
  - With an unbounded index set, DNN = PSD (P76(a)). Even at minimal degree the gap is <= 10%, and it is ZERO for
    N50_x72.
  - Together with E111 (flat CP 1.50×M for N50_x72): the cheapest certificate of the best dense set is entrywise
    nonnegative but NOT completely positive. The required cancellation lives in the DNN \ CP gap (odd-cycle-type
    structure of the difference graph), not in negative Gram entries.

## E111 (2026-10-19, cont. 29) Flat completely-positive certificate costs (codex agent; src/e111_cp.py; examples/e111/)
- Method: flat-block CP LP (Σ_B w_B m_B = 1_A, cost Σ w_B|B|), solved by column generation with Gurobi max-weight
  clique pricing; two-level blocks optional. Brief: .research/agents/e111_cp_brief.md. Report:
  .research/agents/e111_report.md (when complete).
- LEAD VERIFICATION (src/e111_verify.py, independent code):
  - N50_x72 primal identity holds exactly in rationals, cost 12.11522.
  - Dual pricing re-solved to Gurobi optimality, max reduced cost 2.2e−16, so the flat-class optimum is 12.1152.
  - R_CP = 0.857 against R = 0.570.
- Suite (numerical; "opt" = pricing proved optimal):
| set | n | X | R | R_CP (flat) |
|---|---|---|---|---|
| N50_x72 | 50 | 72 | 0.570 | 0.857 (opt, lead-verified) |
| N50_x71 | 50 | 68 | 0.573 | <= 0.836 (time limit) |
| dense X30 s0 / s1 | 20 | 28–30 | 0.607 / 0.601 | 0.808 / 0.842 (opt) |
| dense X50 s0 / s1 | 34 / 31 | 49 / 45 | 0.604 / 0.635 | 0.842 / 0.823 (opt) |
| dense X80 s0 / s1 | 54 / 49 | 80 | 0.640 / 0.653 | <= 0.912 / 0.937 |
| dense X120 s0 / s1 | 73 | 115 / 120 | 0.673 / 0.679 | <= 1.02 / 1.03 (pricing time limit) |
| Singer q = 5 / 7 / 11 | 15 / 28 / 66 | 29 / 55 / 131 | 0.749 / 0.756 / 0.738 | 0.775 / 0.756 / 0.739 (one Sidon block) |
| interval [1, 20] | 20 | 20 | 1.110 | 1.112 |
- Adversarial local search over A ⊂ [1, X], X = 10…39 (20 s per X, seed 20271109): best R_CP 0.754 (X = 12, 13).
  The X = 23, 24 and 30 optima are single Sidon blocks.
- Reading (CORRECTED after the final report):
  - Flat CP stays above ≈ 0.74 at these sizes, consistent with flat CP½.
  - TWO-LEVEL nonnegative blocks (values {0,1,2}·√w) are far cheaper. Lead-verified exact rational certificate for
    X30_s0 (38 blocks): C = 5.857342 against flat 7.230, R_CP <= 0.6549 against R = 0.6073, i.e. C/(2M) = 1.078.
  - Agent's two-level optima: X11 0.682 (R 0.675), X12 0.690 (R 0.687), X13 0.714 (R 0.712),
    X14 0.751 (R 0.751), X30_s1 0.724 (R 0.601).
  - So "the best sets need phase cancellation" is WRONG. They need non-flat weights. Report:
    .research/agents/e111_report.md.

## E112a (2026-10-19, cont. 29) CP-efficiency in prime cyclic groups (src/e112_cpzp.py; examples/e112/e112a.jsonl)
- Setup: Z_p has no nontrivial subgroups, so it has no spreads.
  - S symmetric; K = −min_{γ≠0} Σ_{s∈S}cos(2πsγ/p); ratio |S|/K².
  - C_CP = flat completely positive certificate cost, by column generation with exact Gurobi clique pricing.
  - "opt" = pricing proved optimal; "stalled" = a degenerate dual repeated a column, so C_CP is an UPPER bound.
| set | p | ratio | C_CP/K | status |
|---|---|---|---|---|
| E41 half-set optimum | 71 / 79 / 83 / 89 | 2.08 / 2.10 / 2.17 / 2.05 | 5.45 / 5.00 / 5.25 / 2.64 | stalled (UB) |
| E41 half-set optimum | 43–73 (others) | 1.66–1.97 | 2.1–5.8 | stalled (UB) |
| Paley (QR) | 13–89 | 1.13–1.62 (→ 2) | 1.30–2.11 | opt |
- Reading:
  - Paley's CP cost equals the clique bound |S|/(ω − 1) (ω = 5 at p = 89), so its efficiency grows like √p/log p.
  - The E41 optima reach ratio 2.05–2.17 with NO subgroups and are far from CP-efficient. So ratio slightly above
    2 does not force spreads at these sizes.
  - E41's SA data put the Z_p half-set ratio at a peak of ≈ 2.15 (p = 80–150), declining for larger p
    (search-limited). This is consistent with a bounded ratio in Z_p and a spread threshold T ≈ 2.2 rather than 2.
  - No refutation of SCP(T) for any fixed T: finite data cannot test the C(T) constant.

## E113–E114 (2026-10-19, cont. 30) Finite-group probes after the Jedwab–Li literature check (lead; dirichlet)
E113 (src/e113_valclass.py, exact): valuation-class sets in Z_{p^a}² (membership by (v_p(x), v_p(y)) ∈ Ω), exhaustive
for (p, a) = (3,2), (3,3), (5,3), (7,3). Subgroup unions dominate (K = 1). Excluding them, the best is a large subgroup
minus a small valuation shell (values −p, 0, |D|): ratio p^{2a−3}, no new mechanism.
E114 (src/e114_cp_group.py, e114b_cliques.py, e114c_omega.py; exact combinatorics, networkx):
CP structure of the Jedwab–Li blocks D_{a,j} ⊂ Z_{p^a}² (exact LS_{p^{a−1}}(p^a), K = p^{a−1}, ratio ≈ p).
  | p | a | j | |D| | K | ratio | Delsarte 1+|D|/K | ω (exact) | max cliques | C_CP lower = |D|/(ω−1) | /K |
  | 3 | 2 | 0 | 24 | 3 | 2.67 | 9 | 9 | 3 subgroups | — (C_flat = 3 = K, opt) | 1 |
  | 3 | 3 | 0 | 234 | 9 | 2.89 | 27 | 27 | only the 3 subgroups ⟨(0,1)⟩, ⟨(3,1)⟩, ⟨(6,1)⟩ | — | — |
  | 3 | 3 | 1, 2 | 234 | 9 | 2.89 | 27 | 10 | 540 of size 10 | 26 | 2.89 |
  | 5 | 2 | 1 | 120 | 5 | 4.8 | 25 | 6 | — | 24 | 4.8 |
  | 5 | 3 | 1 | 3100 | 25 | 4.96 | 125 | 26 (252 s) | — | 124 | 4.96 |
- j = 0 (a = 3) is NOT geometric: the only 27-cliques are its three subgroups (78 of 234 elements covered).
- j ≠ 0: ω = K + 1 in both cases, so C_CP >= |D|/K = ratio·K. These exact two-valued sets with ratio > 2 are
  CP-INEFFICIENT by a factor equal to their ratio: genuine CANCELLATION objects (clique-poor), not spreads.
- Bug note: the first e114 pricing lacked z >= x_s + x_t − 1 (fixed before any reported number); the full column
  generation on Z_27² was too slow (killed) and replaced by the exact clique computations above.
- (3, 4, 1) (K = 27): the exact max-clique run produced no output within its wall-time limit (no
  value claimed). The ω = K + 1 pattern is verified only for (3,3), (5,2), (5,3).

## E115 (2026-10-20, cont. 31) Exact K-Chowla numbers in Z_p (Gurobi ILP; src/e115_zp_ilp.py; dirichlet)
N_p(K) = max |S| over symmetric S ⊂ Z_p^*, |S| <= (p−1)/2, D_S(j) >= −K for all j ≠ 0 (exact characters, no grid;
1 ∈ S by dilation symmetry). Z_p-Chowla (sup_p max_K N_p(K)/K² < ∞) ⇒ Z-Chowla.
- Run 1 (K = 2, 3; 57 solves, all OPTIMAL; examples/e115/np_k_run1.jsonl): N_p(2) = 2 for every p >= 83 (S = {±1});
  N_p(3) = 6–8 (ratio <= 0.89) except p = 37: |S| = 12, S = ±{1,4,5,8,9,13} (ratio 1.33). Fixed small K is
  uninformative (optimum = tiny set); stopped.
- Run 2 (STOPPED at p = 83 to free the VM for E116; 37 solves, all OPTIMAL; examples/e115/np_k_run2.jsonl):
  K = c√p, c ∈ {0.42, 0.46, 0.50}. Max ratio |S|/K² = 1.92 (p = 71, 79 at c = 0.50, |S| one pair short of a
  half-set); with the exact min of the optimal set, 38/4.362² = 2.0 at p = 79. Sub-half sets never beat the E41
  half-set optima: in Z_p the binding constraint is |S| <= p/2, and the question reduces to E41.

## E116 (2026-10-20, cont. 31) Advisor's experiment: lifting a Jedwab–Li set to Z² (≡ Z) with a jointly optimised
## Boolean taper (src/e116_jl_taper.py; dirichlet; minima NUMERICAL: FFT grid 16(2L+1) + BFGS, not certified)
Lift P_L = {z ∈ [−L, L]² : z mod n ∈ D_{a,j}}; Boolean T ⊂ P_L maps to S = {z₁ + Vz₂} ⊂ Z (V > 4L) with
ratio_1D >= |T|/K'_2D², R_1D <= K'/√(2|T|). ratio 2 ⟺ R = ½; best known integer sets of size ~100–250: ratio ≈ 1.4.
Measured (i) finite, (ii) fractional PD taper w = Λ(z₁/L)Λ(z₂/L), (iii) Boolean (box = centred representatives;
Bernoulli(w) rounding, seeds 0–3):
  | p a j | L  | |D| | K_G | ratio_G | K_frac | Σw²   | ratio_frac | box: |T|, K', ratio | Bernoulli ratio     |
  | 3 2 1 | 9  | 24  | 3   | 2.67    | 3.000  | 9.41  | 1.05       | 24, 10.28, 0.227   | 0.13–0.16           |
  | 5 2 1 | 25 | 120 | 5   | 4.80    | 5.000  | 50.93 | 2.04       | 120, 32.3, 0.115   | 0.078–0.110         |
  | 5 2 1 | 50 | 120 | 5   | 4.80    | 20.00  | 211.1 | 0.53       | 120, 32.3, 0.115   | 0.077–0.097         |
- (ii) is exact theory: with L = n the PD taper vanishes on nZ² ∖ 0, so by Poisson F_w >= −r·τ(0) = −r (observed
  K_frac = r to 1e−13). The fractional lift costs only the factor Σw²/|D| ≈ (2/3)² = 4/9 (a sinc taper would cost
  nothing: Σw² = |D|). L = 2n is worse (K scales by (L/n)² = 4, Σw² only by 4, so the ratio drops by 4). So the Gibbs penalty of the box is
  ENTIRELY avoidable for fractional weights; the whole loss is the 0/1 constraint.
- (iii) naive Booleans lose a factor ≈ 20–60 in ratio. Bernoulli matches the noise prediction
  K ≈ √(2·(5/9)|D|·ln(4n²)) (p = 5: 32 predicted, 31–38 observed).
- PREDICTION (lead, falsifiable, recorded before the MILP results): the jointly optimised Boolean T stays at ratio
  <= ~1.4 (R >= 0.6) for p = 3, 5, i.e. no better than unstructured integer optima of the same size, and the ratio
  gap ratio_frac/ratio_bool grows with p. A ratio > 2 at p = 5 would refute the Gibbs-versus-rounding dichotomy.
- MILP batch 1 (running): max |T| s.t. F_T >= −Kthr (lazy cuts at true minimisers), p = 3 (L = 9, Kthr 3–6, plus
  the unrestricted box as control) and p = 5 (L = 25, Kthr 5, 7.5, 10, 15); 1800 s each; examples/e116/milp1.jsonl.

### E116 cont. — advisor's second review (2026-10-20): energy/negativity split, CERTIFIED K, where the error lives
(src/e116_analyze.py; examples/e116/analysis1.jsonl). Ɛ = Σ_{s≠0}|a_s|² (= |T| for 0/1), ρ = Ɛ/K²,
ρ_int/ρ_G = (Ɛ_int/Ɛ_G)·(K_G/K_int)². K is CERTIFIED for the 1D integer image A = {z₁ + Vz₂} (V = 4L + 3):
upper end = −2·certify_lower_bound_blocked(A) (rigorous), lower end = −2 f_A(x*) at a definite x* (mpmath 60 digits).
Both ends agree to 3 decimals in every row, so these K are certified.
  | instance (best found)          | Ɛ   | Ɛ/Ɛ_G | K (cert.) | (K_G/K)² | ρ     | ρ_G  | K/√(Ɛ ln n²) |
  | FD lift p=3 a=2 (SA)           | 24  | 1     | 8.164     | 0.135    | 0.360 | 2.67 | 0.80          |
  | FD lift p=5 a=2 (SA)           | 120 | 1     | 23.354    | 0.046    | 0.220 | 4.80 | 0.84          |
  | FD lift p=3 a=3 (SA)           | 234 | 1     | 33.240    | 0.073    | 0.212 | 2.89 | 0.83          |
  | FD lift p=7 a=2 (SA)           | 336 | 1     | 45.137    | 0.024    | 0.165 | 6.86 | 0.88          |
  | MILP p=3, Kthr 5 (OPTIMAL)     | 20  | 0.833 | 5.000     | 0.360    | 0.800 | 2.67 | —             |
  | fractional τ-lift p=5 (theory) | 51  | 0.42  | 5 (exact) | 1        | 2.04  | 4.80 | —             |
- Split: fundamental-domain (FD) lifts keep all the energy and lose everything in K. The optimal MILP subsets trade
  some energy for K. The fractional lift keeps K and loses 58% of the energy (advisor's correction: the boundary cost is
  NOT avoided, it is moved from K into Ɛ). The "sinc taper keeps all of ρ_G" remark is RETRACTED: sinc weights are
  negative in places, so it is not a relaxation of a 0/1 set; with weights in [0,1] the best energy retention is open
  (triangle: 4/9 in 2D).
- FD scaling (p = 3, 5, 7 at a = 2): ρ = 0.360, 0.220, 0.165, DECREASING in p; K/√(Ɛ ln n²) ≈ 0.80–0.88, i.e.
  random-level negativity K ≈ 0.85√(Ɛ ln n²). Consistent with the prediction, for this class only.
- Where the error lives. Reference = fractional τ-lift of T's own class multiplicities (K_ref = K_G exactly on the
  grid). Spike region Σ+ = {F_w > 0} (measure 0.24–0.39). Fraction of ∫e² on Σ+: 0.57, 0.41, 0.47, 0.28 for the FD
  rows (1.2–1.5 × the area share) and 0.52–0.63 for the MILP optima (1.2–1.7 ×). The most negative error on the
  background (−8.0, −22.3, −32.3, −42.5) is essentially the global minimum. So the optimiser hides only a little of the
  rounding error under the spikes; the binding negativity is on the background.
- Pending: certified Gurobi bounds at p = 5 (batch 1) and p = 7 (to queue); free-subset SA at p = 5, 7.

## E117 (2026-10-20, cont. 31) Concentration eigenvalues for the centroid barrier P77 (src/e117_concentration.py;
## dirichlet; NUMERICAL eigenvalues, numpy eigvalsh, not certified)
N = Z_n² ∖ B (B = {D̂ = −r}, the background), λ_odd = top eigenvalue of 1_D P_N 1_D on odd functions; φ = fraction of
the centroid field's W-energy on N.
  | p a j | n   | |D|  | |N|/n² | λ_odd  | φ centred lift | φ SA-optimised one-rep lift (E116) |
  | 3 2 1 | 9   | 24   | 0.309  | 0.6055 | 0.133          | 0.476                              |
  | 5 2 1 | 25  | 120  | 0.194  | 0.5418 | 0.085          | 0.266                              |
  | 7 2 1 | 49  | 336  | 0.140  | 0.3897 | 0.084          | 0.110                              |
  | 11 2 1| 121 | 1320 | 0.090  | 0.3034 | 0.058          | —                                  |
  | 13 2 1| 169 | 2184 | 0.077  | 0.3532 | 0.053          | —                                  |
  | 3 3 1 | 27  | 234  | 0.322  | 0.8007 | 0.176          | —                                  |
  | 3 3 0 | 27  | 234  | 0.322  | 0.7558 | 0.317          | —                                  |
  | 3 3 1 | 27  | 234  |        | 0.8007 | 0.176          | 0.340 (E116 FD seed 1, K/√(Ɛ ln n²) = 0.83)      |
  | 3 3 2 | 27  | 234  |        | 0.756  | —              | —                                  |
  | 5 3 1 | 125 | 3000 |        | 0.672  | —              | —                                  |
  | 3 4 1 | 81  | 2160 |        | 0.935  | —              | —                                  |
  | 3 4 0 | 81  | 2160 |        | 0.863  | —              | —                                  |
DEPTH (added later, cont. 31): λ_odd GROWS with the p-adic depth a (p = 3: 0.61, 0.80, 0.94 at a = 2, 3, 4; p = 5:
0.54, 0.67 at a = 2, 3). So the P77 centroid barrier weakens for deep JL sets. The optimised a = 3 lift does NOT use the
room: φ = 0.34 against λ_odd = 0.80, and its K/√(Ɛ ln n²) = 0.83 is no better than a = 2's 0.80. Test: E118.
Reading: the optimiser does move the centroid field toward the spikes (φ 0.13 → 0.48 at p = 3) but cannot exceed
λ_odd, which stays <= 0.61 for a = 2. This is the quantitative content of "the rounding error cannot hide under the
spikes" at first order (P77).

## E118 (2026-10-20, cont. 31) Does pushing the centroid field onto the spikes lower K? (src/e118_cvp.py,
## src/e118_batch.sh; dirichlet, 1 core, ~1 min; data examples/e118/cvp.jsonl; K NUMERICAL (FFT + BFGS), not certified)
One-rep lifts z(g) = ḡ + n·t(g), t ∈ {−1, 0}², odd. "CVP" = minimise the first-order background energy A2 (equivalently
maximise φ, the share of the centroid field's W-energy on N) by SA on the binary QP in t (coordinates independent).
  | p a j | n   | |D|  | λ_odd | centred φ / K / ρ        | CVP φ / K / ρ            | best direct-K SA (E116 FD) ρ |
  | 3 2 1 | 9   | 24   | 0.605 | 0.133 / 10.3 / 0.227     | 0.476 / 10.3 / 0.225     | 0.36 (K 8.0–8.2)             |
  | 5 2 1 | 25  | 120  | 0.542 | 0.085 / 32.3 / 0.115     | 0.342 / 23.9 / 0.209     | 0.210 (K 23.9)               |
  | 7 2 1 | 49  | 336  | 0.390 | 0.084 / 86.3 / 0.045     | 0.185 / 70.2 / 0.068     | 0.161 (K 45.6, φ 0.110)      |
  | 3 3 1 | 27  | 234  | 0.801 | 0.176 / 62.1 / 0.061     | 0.532 / 34.6 / 0.196     | 0.20, 0.17 (K 34.1, 37.0)    |
  | 3 3 0 | 27  | 234  | 0.756 | 0.317 / 62.2 / 0.060     | 0.510 / 34.4 / 0.198     | —                            |
  | 5 3 1 | 125 | 3100 | 0.671 | 0.109 / 705 / 0.0062     | 0.317 / 474 / 0.0138     | —                            |
  | 3 4 1 | 81  | 2160 | 0.935 | 0.184 / 502 / 0.0086     | 0.575 / 194 / 0.0576     | E118b running                |
Readings.
- The centred lift's K is the Gibbs lobe of the box: K ≈ 0.217|D| (p = 3, a = 4: 502 vs 469). CVP smooths the box edge
  (K 502 → 194) but stays far above random level (K/√(Ɛ ln n²) = 1.40 at a = 4).
- CVP equals the direct optimum at p = 5 and p = 3, a = 3; at p = 7 the direct optimum has LOWER φ and much lower K.
  So the first-order centroid term is neither necessary nor sufficient: it is not the binding cost (P77 is true but weak).
- ρ of CVP lifts FALLS with depth at p = 3 (0.225, 0.196, 0.058 at a = 2, 3, 4) although λ_odd → 1 (0.61, 0.80, 0.94).
  The deeper JL sets do not use the room P77 leaves. Prediction (E118b): direct SA at a = 4 stays below a = 3's 0.20.

## E121 / E121b (2026-10-20, cont. 31) Character reduction of λ_odd for JL D_{2,j} (P79), and exact self-checks
src/e121_lambda_char.py, src/e121_check.py (dirichlet). λ_char (block norms ‖M_ψ‖²/p²) = λ_direct (E117 method) to 1e−15 at
(p, j) = (3,1), (3,2), (5,1), (5,2), (7,1), (7,3), (11,1), (13,1), (13,5), (17,1), (19,2). Exact integer checks for every j,
p <= 19: orbits/free action, two-valued spectrum, N ∖ 0 = N₁ ∪ N₂, β bound — all TRUE. H antisymmetric with doubled top
singular value for every primitive odd ψ. max_{j,ψ} λ: 0.605 (3), 0.542 (5), 0.469 (7), 0.348 (11), 0.353 (13), 0.287 (17),
0.306 (19) against Λ(p) = 0.873, 0.746, 0.684, 0.623, 0.606, 0.582, 0.574. σ₁(H)²/p² = 0.25–0.37 (bound (p−1)/(2p)).

## E122 / E122b (2026-10-20, cont. 31) Quadric cones in F_p^4, F_p^6: P77 inputs (src/e122_quadric_lambda.py,
## src/e122_odd_spectrum.py; dirichlet; NUMERICAL)
  | p form | |A| | spectrum   | ρ_G  | λ_odd  | φ centred | K centred lift (T^4) | ρ centred lift |
  | 3 hyp  | 32  | −4, 5      | 2.0  | 1/3    | 1/3       | 12.0                 | 0.222          |
  | 5 hyp  | 144 | −6, 19     | 4.0  | 1/5    | 1/5       | 37.3                 | 0.103          |
  | 7 hyp  | 384 | −8, 41     | 6.0  | 1/7    | 1/7       | 40.9                 | 0.230          |
  | 3,5,7 ell | 20, 104, 300 | spikes negative | 0.41, 0.24, 0.16 | 1 − 1/p | — | — | — |
Full odd spectrum (E122b): every eigenvalue = 1/p, off-diagonal <= 1e−17, for r = 4 (p = 3, 5, 7, 11) and r = 6 (p = 3, 5).
This is P81 (proved).

## E119 (2026-10-20, cont. 31) Advisor's p² law vs noise law, one-rep JL D_{2,1} lifts (src/e119_taper_random.py,
## src/e119_batch.sh; dirichlet; K NUMERICAL FFT + BFGS). Predictions were pre-registered in CSTAR A10 before the run.
Taper-random one-rep lifts (P78 construction), 4 seeds each:
  | p  | |D|  | K (seeds)                    | median K/√(|D| ln n²) | 0.92p² | registered pred | corrected pred |
  | 3  | 24   | 13.1, 12.7, 13.6, 12.8       | 1.26                  | 8.3    | 12.2            | 16.3           |
  | 5  | 120  | 38.2, 48.0, 35.6, 37.9       | 1.37                  | 23.0   | 28.2            | 37.9           |
  | 7  | 336  | 63.0, 64.9, 69.6, 67.0       | 1.29                  | 45.1   | 48.8            | 66.0           |
  | 11 | 1320 | 136.8, 150.1, 142.1, 141.3   | 1.26                  | 111.3  | 101.1           | 138.4          |
  | 13 | 2184 | 175.9, 187.0, 199.1, 182.6   | 1.23                  | 155.5  | 132.2           | 181.0          |
PRE-REGISTERED PREDICTION FAILED (lead): taper-random K at p = 11, 13 is 137–150 and 176–199, not ≈ 101, 132, and lies ABOVE
0.92p². Cause found: the Gaussian extreme value is σ√(2 ln N); the registered formula used σ√(ln N) (dropped factor √2).
With √2 restored ("corrected pred", same σ̄², no refit) the noise law matches all five p. K/√(|D| ln n²) ≈ 1.25 is flat in p,
as P78 predicts. Consequence: at p <= 13 random lifts do NOT beat the p² law; the asymptotic o(p²) (P78, a theorem) only
bites near p ≈ 25–30 (1.25·2p^{3/2}√ln p = 0.92p²). Decisive test launched: E119b (p = 17..31).
Centred / CVP (E118 method) at p = 11: K = 303 / 281 (φ 0.058 / 0.097, λ_odd 0.303); p = 13: 491 / 479. Centred K ≈ 0.22|D|
(box Gibbs lobe). SA one-rep (taper init) at p = 11, 13: running.

## E120 (2026-10-20, cont. 31) Certified sup_T |T|/K(T)² (Dinkelbach MIQP; src/e116_jl_taper.py ratio; src/e120_ratio.sh)
p = 3, a = 2, j = 1, class P_9 (48 ± pairs): round 0 at ρ = 0.8: OPTIMAL, ObjBound = 0.0 (228 lazy cuts, 404 s).
CERTIFIED: |T| <= 0.8·K(T)² + 10⁻⁴ for every symmetric T ⊂ P_9, i.e. sup ratio <= 0.8001 (K >= 1), attained by the E116
optimum T = 20, K = 5. (Cuts are valid for all truly feasible T, so the bound is rigorous up to LP tolerances; the cut
generator's numerics only affect which incumbents are accepted.) Running: full box [−9, 9]² control, p = 5 (L = 25), p = 7.
(Threshold-MILP control, full box at Kthr = 3, 1800 s: T = 6, K = 2.63, ratio 0.867 — the full box beats the D-class.)
E120 (cont.) Remaining runs. p = 3 full box [−9,9]² (180 pairs), 1800 s/round: NOT certified; incumbent T = 30, K = 6,
ρ = 0.8333 > the D-class sup 0.8; ObjBound 166 (useless). p = 5 (L = 25, ρ0 = 0.30): NO OUTPUT — no line in ratio.jsonl on
the VM or locally, no traceback in the job log; cause undiagnosed (it ended in < 10800 s, before p = 7 started). p = 7
(L = 49, 672 pairs, 10800 s): NOT certified; ObjBound 696 → 1344, incumbent a single ± pair (T = 2, K = 2, ρ = 0.5).
PRE-REGISTRATION ERROR (lead): any single ± pair {g, −g} in the class has K = 2, ρ = 2/4 = 0.5, so sup ρ >= 0.5 for every p
and the p = 5 window [0.305, 0.45] was false before the run. The free-subset SA values (0.305, 0.204, 0.160) are optima of
LARGE T, not sups. A meaningful item (3) needs a size floor (|T| >= c|D|, added as a constraint) or must ask whether
sup ρ − 0.5 grows with p. Dinkelbach MIQP with lazy cuts does not close at p >= 5 (bound gap ~10³); certification beyond
p = 3 needs a different relaxation.

## E119b (2026-10-20, cont. 31) Crossover test of the 0.92p² law (src/e119b_batch.sh; data examples/e119/taper_large.jsonl;
## dirichlet; K NUMERICAL: FFT grid (oversampling 8 for p = 17, 19; 4 for p >= 23) + BFGS from the 16 best basins)
Pre-registered (src/e119b_batch.sh header, before the run): 1.25√(|D| ln n²) ⇒ K ≈ 716 (p = 29), 799 (p = 31) < 0.92p².
  | p  | |D|   | taper-random K (3 seeds)   | K/√(|D| ln n²) | 0.92p² |
  | 17 | 4896  | 314.2, 302.6, 310.6        | 1.29–1.33      | 265.9  |
  | 19 | 6840  | 352.7, 332.4, 349.8        | 1.17–1.24      | 332.1  |
  | 23 | 12144 | 485.1, 517.6, 506.2        | 1.24–1.33      | 486.7  |
  | 29 | 24360 | 704.0, 737.7, 717.5        | 1.23–1.29      | 773.7  |
  | 31 | 29760 | 812.2, 828.3, 783.7        | 1.23–1.30      | 884.1  |
CONFIRMED: the constant 1.25 (fitted at p <= 13) holds out of sample to p = 31; random lifts cross 0.92p² at p ≈ 23 and lie
7–11% below it at p = 29, 31 (all seeds). A random taper lift is a valid one-rep lift, so the OPTIMAL one-rep K is below
0.92p² at p = 29, 31: the p² law fails for optimal lifts (as P78 proves asymptotically). The SA values at p <= 7 (0.92p²)
sit ≈ 0.65 × the random level there; whether SA stays at ≈ 0.65 × random (⇒ K ≈ 0.8p^{3/2}√ln p) is E119's SA runs.
Status: numerical, not interval-certified (a rigorous grid bound at p = 31 costs ~2700 in Hessian slack ≫ the 100 margin).

## E121c (2026-10-20) Asymptotics of λ_odd(D_{2,1}) via the P79 blocks (src/e121c_lambda_asym.py; dirichlet; NUMERICAL SVD)
  | p        | 13    | 19    | 23    | 29    | 37    | 43    | 53    | 61    | 71    | 83    | 97    |
  | λ_odd    | 0.353 | 0.268 | 0.242 | 0.199 | 0.189 | 0.168 | 0.151 | 0.175 | 0.137 | 0.122 | 0.134 |
  | λ·√p     | 1.27  | 1.17  | 1.16  | 1.07  | 1.15  | 1.10  | 1.10  | 1.37  | 1.16  | 1.11  | 1.32  |
λ_odd ≈ 1.2/√p, carried by σ₁(H)² ≈ 1.2p^{3/2} (H_top = λ to 3 digits for p >= 19: the a_* row/column is negligible).
So the first-order concentration factor relative to the area share |N|/n² ≈ 1/p is ≈ 1.2√p for JL a = 2, against EXACTLY 1
for quadric cones (P81). P79's bound (→ 1/2) is crude; a p^{−1/2+ε} bound would need Fermat-quotient/character-sum
estimates for H[s₀,s] = ψ̄(s − s₀) (sums over an interval of length p modulo p²); not needed for P80.

## E118b (2026-10-20) Direct K-minimising SA (one rep, R = 1) on deep JL p = 3, a = 4 (src/e118_deep.sh; NUMERICAL)
Seed 1 (1.5M iterations, box init): K = 136.9, ρ = 0.115, K/√(|D| ln n²) = 0.99 (|D| = 2160, λ_odd = 0.935).
Against CVP 0.058 and centred 0.0086. Pre-registered (E118): "direct SA at a = 4 stays below a = 3's 0.20" — CONFIRMED
(seed 2 running). Optimised one-rep ρ at p = 3: 0.36, 0.20, 0.115 for a = 2, 3, 4, although λ_odd → 1 (0.61, 0.80, 0.94):
the weaker first-order barrier at depth is not exploited; the cost is random-level (K/√(|D| ln n²) = 0.80, 0.83, 0.99; the
rise at a = 4 may be under-optimisation, 1400 iterations per class).

## E123 (2026-10-20) P80c 1D transfer: advisor's counterexample and the repaired bound (src/e123_freiman_transfer.py;
## dirichlet; NUMERICAL minima: dense grid/random starts + BFGS)
- Counterexample to the z₁-only bound (advisor review 4): d = 3, T = {±e₂, ±e₃}, V = 8: K₃ = 4, K₁D = 3.850015, Σz₁² = 0.
  Repaired full-coordinate loss (π²/(2V²))Σ(Σ_{k<d}|z_k|)² = 0.1542 >= 0.1500. CONFIRMED.
- 120 random odd lifts (d = 2, 3, 4; n ∈ [3, 6]; 3–8 ± pairs; V ∈ (2n, 6n]): repaired bound min margin 0.096 / 0.360 / 2.359
  (no violation); z₁-only bound violated once at d = 3 (margin −0.037).

## E124 (2026-10-20, cont. 31; advisor's commissioned experiment) Local centroid / anti-concentration test (src/e124_bac.py;
## dirichlet; NUMERICAL grid sums, L >= 32·max A; pre-registered in CSTAR)
f = Σ c_a cos(2πax); share₀ = ∫_{f<=0}f'²/∫f'²; G₀ = ∫_{f<=0}f'²/(2√2|{f<=0}|^{1/2}‖f''‖₂) (P82 at r' = 0, a valid lower bound on M).
  | family                         | n_eff  | R = M/√n | share₀ | G₀/√n  |
  | Singer–Bu q = 61/101/199/307   | 3782–94556 | 0.604/0.588/0.566/0.557 | 0.227/0.226/0.225/0.225 | 0.048/0.047/0.047/0.047 |
  | dense optima X30/X120/X260     | 20/73/150 | 0.61/0.67/0.75 | 0.30/0.24/0.26 | 0.064/0.053/0.059 |
  | JL lift images p=3,5 (a=2), 3 (a=3), 7 | 12–168 | 1.18–1.74 | 0.38–0.43 | 0.085–0.10 |
  | quadric centred lift p=5/7     | 72/192 | 2.17/1.47 | 0.42/0.36 | 0.10/0.083 |
  | random d=0.5 / d=0.1           | 2061/1624 | 9.4/8.5 | 0.35/0.48 | 0.091/0.125 |
  | interval [1,2000] / Paley 4093 | 2000/2046 | 9.7/9.5 | 0.200/0.348 | 0.043/0.091 |
  | packets FRACTIONAL X=1024/4096/16384 | 115/484/1923 | 0.765/0.687/0.639 | 0.288/0.287/0.260 | 0.053/0.054/0.050 |
  | packets Bernoulli-rounded       | 168/656/2674 | 1.79/1.99/2.08 | 0.42/0.43/0.42 | 0.090/0.087/0.085 |
(X = 65536 packets killed: X × J outer product > 10 GB; not needed.)
Pre-registered: (P1) P82 <= M — HOLDS for all 24 sets. (P2) Boolean share₀ >= 0.2 HOLDS (min 0.200, interval);
G₀/√n >= 0.05 FAILS marginally for Singer–Bu (0.047, flat in q) and interval (0.043) — a threshold miss, not a decay.
(P3) packets share₀ → 0 NOT CONFIRMED: 0.288 → 0.287 → 0.260 over 16× in X, and the fractional packets match the Bu-type
Boolean sets in both statistics. Reason: the packet advantage decays like X^{−0.05} (R 0.76 → 0.64), their background is
not flat at accessible X (floor −√(J/8) plus oscillating nonnegative tails), so separation would need X ~ 10²⁰.
NOTE: an "optimised" P82 over levels r' is dominated by the trivial term r' (ratio 0.950 = the top level scanned);
the informative quantity is G₀.
VERDICT (advisor's criterion): the local centroid inequality is weight-agnostic (P82) and Booleanity enters only through
an anti-concentration (gap) hypothesis that cannot even be calibrated against the packets at computable sizes. P77 does
NOT supply a general route. Recorded in ROUTES; P77/P79/P81 remain model exclusions.

## E125 (2026-10-20, cont. 31) Near-floor geometry: Boolean sets vs fractional P61(b) packets (src/e125_floor.py; dirichlet;
## NUMERICAL, grid L >= 64·max A, M = grid min; pre-registered in CSTAR)
N(t) = |{f <= −M(1 − t)}|, wells(t) = components, γ = slope of log N between t = 0.01 and 0.1.
  | family                      | N(0.01)            | N(0.05)          | N(0.1)          | N(0.5)        | wells(0.01)    | γ           |
  | Singer–Bu q = 61/101/199    | 8.0e-5/3.4e-5/1.4e-5 | 2.5e-3/1.9e-3/3.5e-3 | 0.024/0.026/0.041 | 0.36/0.37/0.38 | 14/16/30     | 2.48/2.88/3.45 |
  | dense optima X120/X260      | 2.7e-3/3.7e-4      | 0.017/0.0068     | 0.037/0.022     | 0.28/0.25     | 6/2            | 1.14/1.78   |
  | random d = 0.5, X = 4096    | 2.3e-5             | 5.0e-5           | 7.2e-5          | 2.2e-4        | 2              | 0.50        |
  | packets FRACTIONAL 1k/4k/16k| 0.022/0.024/0.036  | 0.13/0.17/0.20   | 0.16/0.21/0.25  | 0.31/0.36/0.39 | 62/284/1596  | 0.87/0.95/0.85 |
  | packets Bernoulli 1k/4k/16k | 2.1e-4/6.9e-5/1.3e-5 | 5e-4/3e-4/4e-5 | 7e-4/6e-4/1.4e-4 | 0.07/0.04/0.035 | 2/2/2       | 0.54/0.93/1.01 |
PRE-REGISTERED CRITERION MET: packets vs Singer–Bu differ by 270–2500× in N(0.01) (growing with X: packets up, Bu down) and by
>= 1.5 in γ. The fractional packets have a macroscopic FLAT FLOOR (the deterministic bottom −√(J/8) of nonnegative packet
tails, attained on ~0.1X shallow wells); Boolean near-extremizers reach their minimum in a few isolated deep wells, with the
near-floor measure growing steeply (γ ≈ 2.5–3.5). At half depth (N(0.5)) the two are indistinguishable. Bernoulli rounding
destroys the floor at once.
SCOPE: a model-separating statistic, not a Chowla mechanism. C* (F2) forces only E_background[p] <= 1 − c (background at
about −cM on average), not a flat floor at −M; a C* object with a half-depth background and rare deep wells would look
Boolean-like here. So FLOOR ("Boolean sets have no macroscopic near-floor plateau") would exclude the packet model only.
E119 (cont.) SA one-rep, taper init, p = 11 (1.5M iterations, ~1100 per class): K = 114.6, ρ = 0.1005, K/√(|D| ln n²) = 1.02.
0.92p² = 111.3 (law within 3%); taper-random 137–150. Pre-registered "SA <= taper-random" HOLDS. SA/random = 0.80 (vs ≈ 0.65
at p <= 7): the optimiser's advantage shrinks with size, so at p = 11 the optimised lift sits ON the p² law. The law can
only fail for optimised lifts once the random level (1.25√(|D| ln n²)) drops below it, p ≈ 23–29 (E119b), unless SA gains
more. p = 13 SA (2.5M iterations) did NOT finish: the batch hit its 30000 s wall-clock limit (exit 143) and was killed;
no p = 13 SA result and the p = 11 box seed-2 run never started.
E119d (one-rep SA, taper init, p = 17, 2.5M iterations; examples/e119/sa_p17.jsonl; NUMERICAL). The SA finished, but the
driver died in true_min (2^15 × 2^15 grid over the 8 GB cap); K recomputed by src/e119e_trueK.py (rfft2 grids 8192 and
16384 + BFGS from 48 starts each; both give the same minimum). K_true = 271.39, ρ = 0.0665, at ξ ≈ (−0.0028, 0.00006), a
low-frequency dip (ξ₁·n ≈ 0.8). PRE-REGISTERED PREDICTION FALSE: K ≈ 245 < 266 predicted; observed 271.4 >= 0.92p² = 265.9
(2% above the law). SA/random = 271/308 = 0.88 (0.65 at p <= 7, 0.80 at p = 11): the optimiser's advantage keeps shrinking
and the optimised one-rep lift stays on the p² law through p = 17.
DISCREPANCY: the SA's own objective (grid G = 4(2L+1) = 2316) reported K = 235.6, 13% below the true K; at p = 11 the gap
was 4.5% (109.7 vs 114.6). The SA partly optimises grid artefacts (dips between grid points), and the gap grows with p. So
271.4 bounds the lift this SA found, not the best one-rep lift at p = 17; an SA on a finer grid (or with true-min
re-checks) is needed before reading the law off p >= 17. p <= 11 values used true_min on the final lift and stand.
E119c (free-subset SA, p = 11, L = 121, Bernoulli-taper init, 6M iterations; examples/e119/free_p11.jsonl; NUMERICAL):
|T| = 2452 (1.86 per class), K = 123.7, ρ = 0.160 (one-rep optimum 0.100). Free-subset best ρ: 0.305 (p = 5), 0.204 (7),
0.160 (11) — still DEcreasing in p (ρ·log p ≈ 0.49, 0.40, 0.38; ρ·√p ≈ 0.68, 0.54, 0.53), consistent with the A10
prediction that the best lift ratio falls with p. Multiplicity buys a factor 1.3–1.6 over one-rep, not a trend reversal.

## Unnumbered archive supplement — completed passes, 2026-10-20

No new E identifier is assigned and earlier seeds/results remain unchanged. These are archived completed passes, not newly scheduled runs. Use N=|S|=2|A| and K=-lambda_min(B_W2); K_global=2M. Historical multiscale JSON `rho` means N/K^2, not the Perron eigenvalue.

- [Structural reproduction index](experiments/cstar_structural_2026-10-20/README.md): exact subset and sharp-W2 certificates; exhaustive/heuristic full-W2 searches; profile, alias and model diagnostics; independent product-Fejer and order-profile exact checks. Reports and captured JSON/logs are linked there. Restored repository inputs are available; two profile path assumptions were made script-relative during recovery, with manifest provenance retained.
- [Full-W2 falsification index](experiments/full_w2_falsification_2026-10-20/README.md): 84 multiscale records and text support exports, correlated lift/Singer tests, exact set checks and independent operator controls. Binary eigenvector caches were deliberately omitted. Finite curves and residuals do not certify asymptotic lower bounds or the absence of a lower eigenvalue.
- [Groundstate-repair index](experiments/groundstate_repair_2026-10-20/README.md): exact finite layer/implant/energy checks and translated-space diagnostics. The beta=.45 target-8192 translated solve was interrupted after groundstate diagnostics; no completed translated certificate is claimed there. [Archive-time validation](experiments/groundstate_repair_2026-10-20/VALIDATION.md).
- [Coupled-mode index](experiments/coupled_mode_2026-10-20/README.md): exact axis/encoding/color/compression checks; optional root-orbit and Laguerre diagnostics; seeded tapered FFT samples t=2,...,6. These samples are not the lexicographically selected theorem family, do not establish all five joint conditions, and do not compute certified full-W2 minima. [Archive-time validation](experiments/coupled_mode_2026-10-20/VALIDATION.md).

Recovery-time checks and their limits are recorded in [RECOVERY_AUDIT](RECOVERY_AUDIT.md). Run output-generating scripts in a copy to preserve captured evidence; some large scripts require substantial time and memory. No universal theorem or counterfamily is inferred from a completed finite search.

## 2026-10-20 cone-confinement continuation

[Proof and exact reproduction commands](notes/cstar_cone_confinement_2026-10-20.md). Dirichlet data: experiments/cone_confinement_2026-10-20/{results,verification,directional,directional_verification,rotation,rotation_verification}.json. Full finite-field operators p=3,5,7 have exact cubic/eigenspace checks and 15 saved Boolean masks; independent standard-library reconstruction checks every probe. Six directional-fiber supports at X=96,128 have rational point lower bounds, independently re-enumerated in reverse factor order and rechecked at 160-bit Arb. Eight arbitrary annular/angular supports at X=24,64 have 128-bit point bounds, independent 176-bit rechecks, and exact J0 interval certificates. Seeds 20261022 and 20261023; masks, hashes, cardinalities, coefficients and exact rational bounds are retained. Point witnesses prove LOWER bounds for M, never global upper bounds or counterexamples to Chowla. The all-parameter statements come from the paper arguments and retain their explicit hypotheses. No external-agent/Lean audit completed.

## 2026-10-20 Boolean radial realization

[Proof, scopes and commands](notes/cstar_radial_boolean_2026-10-20.md). Data: experiments/radial_boolean_2026-10-20/{quantization,lens,verification}.json. Seed 20261024 checks 84 rational line profiles exhaustively and 16 varying-profile cone cases at p=5,7. Seed 20261025 probes three exact Boolean supports: X=64,128,256 and n=2420,14672,95608. Arb point lower ratios exceed 6.4201,10.6327,18.6951; separate positive Fejer lower ratios exceed 0.1809,0.2960,0.4544. Independent reverse-factor enumeration matches every set hash and rechecks both certificate types at 192 bits. Seven incomplete-moment lens checks corroborate the separate all-center curvature proof. All computation ran on Dirichlet. No sampled minimum is used as a global upper bound; the macro-limit and asymptotic model exclusion are paper statements with explicit distinct quantifiers. Reviewer launch failed; no independent-agent/Lean audit completed.

## 2026-10-20 independent and correlated small-fiber centers

[Statements, proofs, bug repair and reproduction](notes/cstar_fiber_centers_2026-10-20.md). Data: experiments/fiber_centers_2026-10-20/{independent,correlated,countercontrol,verification}.json. Seed20261026 supplies full finite-population numerical moments and96 sampled center assignments at X=64,128,256; selected negative samples have rigorous point R>2.6182,3.3424,4.8221. Seed20261027/Gurobi13 fixes n=1599 and repairs8,9,10 finite phases, each with an Arb floor -10^(-6), while separate points give R>1.8052,2.1552,1.8608. Deterministic mod5 full/empty controls have positive tested zero-circle values and t=5 R>5.1019,11.3456,24.3083. An independent endpoint-pair reconstruction, exact parity coefficient comparison, separate Sturm sign check and192-bit evaluations verify the stored bounds. A mutable-list serialization bug was repaired without reoptimizing candidates; every original target-prefix floor was rechecked. Finite expectation bounds for ANY original-marginal coupling are also rigorous; finite population moments/CLT fits remain numerical. All jobs ran on Dirichlet and are terminal. No global upper bound for an individual Boolean set or external/Lean audit is claimed.
