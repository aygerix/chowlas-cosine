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
