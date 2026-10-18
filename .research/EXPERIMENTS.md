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
