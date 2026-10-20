# Bounded check of the growing-base categorical loophole

For S=+/-A, T=S+S, compare K_T=-lambda_min(B_T) with K_W2 on T union S. The categorical tensor identities need K_T, while a healthy original certificate may in principle rely on rows S\T. A vanishing missing fraction is necessary for an escape, but it does not establish a uniform comparison between these two eigenvalues.

A deterministic script examined 18 finite cases, using the complete matrices through non-wrapping FFT matrix-vector products and a smallest-eigenvalue solver. Results are floating-point diagnostics, not certified interval bounds. Maximum recorded residual is below 6e-8.

- Known eight-frequency example A={1,...,7,9}: S subset T exactly, K_T=K_W2=3.44910155.
- Known 50-frequency sharp-local-constant counterexample: S subset T exactly, K_T=K_W2=7.05699354.
- Four independent triangular taper samples (nominal sizes 64 and 256; seeds 31 and 32): S subset T exactly. Hence no missing-row mechanism exists in these samples.
- Interval cores A={1,...,m} union {5m}, m=2,4,8,16,32,64: |S\T|=2, missing fraction decreases from 1/3 to 1/65. Numerically K_T and K_W2 agree to solver accuracy throughout. Normalized K_T never falls below 1.119 in this list.
- A={1,3,6}: missing fraction 1/3; K_T=3.38244123 and K_W2=3.50181886, ratio 0.96590982. Thus the two matrices should not be conflated: a finite difference does occur.
- A={1,4,8}, {1,3,6,9}, {1,3,6,9,12}: K_T/K_W2 approximately 0.99005, 0.99664, 0.98068, respectively. None has a small normalized K_T.
- Eight-frequency example augmented by 50: missing fraction 1/9; K_T/K_W2=0.99805521.
- Fifty-frequency example augmented by 300: missing fraction 1/51; K_T/K_W2=0.99999692, while K_T/sqrt(N)=0.74943855.

Conclusion: this bounded check produces no promising growing-base gap. It does not prove a universal comparison K_T>=c K_W2 under small missing fraction, and it does not close that logical loophole. No broad new search was run.

Reproduction: categorical_overlap_check.py; complete numeric records: categorical_overlap_check.json. The script constructs S, T, and W2 exactly with integer sets. Its FFT length exceeds the largest possible difference-minus-generator magnitude, so no cyclic adjacency is introduced.
