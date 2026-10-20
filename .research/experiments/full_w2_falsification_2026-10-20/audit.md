# Independent audit of the focused full-W2 falsification pass

Date: 2026-10-20. This is verification of the existing pass, not a new search or a universal Chowla claim.

## Findings first

No substantive algebraic error was found in the five analytic exclusions reviewed. Two presentation issues were corrected in the sources and reported to the authors:

1. `analytic/categorical_overlap_diagnostic.md` claimed maximum residual below 5e-8, whereas `categorical_overlap_check.json` records 5.8067407347025845e-8. The appropriate bound is below 6e-8.
2. A comment in `multiscale/search.py` called the FFT rounding gap “certified.” This is only a numerical check, not interval or exact certification. The mathematical report already states this correctly.

A raw-data notation warning: the historical `rho` field in multiscale records means N/K^2, not the Perron eigenvalue denoted rho in the analytic notes. Do not use that field as a spectral radius.

Most importantly, a small computed eigenpair residual does not establish that the corresponding eigenvalue is the global minimum. A negative Rayleigh quotient supplies a lower bound on K=-lambda_min, up to numerical evaluation error. It cannot supply the upper bound on full K needed to prove a vanishing counterfamily. The computations use the full operators and a smallest-eigenvalue solver, but remain floating-point diagnostics rather than certified full-spectrum bounds.

## Analytic checks

### Heterogeneous unitized products

The exact identity I+B_* = tensor_i(I+B_i) holds on the entire rowset, not a trial space. Every factor has K_i>=sqrt(2), using an extreme three-vertex path, and rho_i>=sqrt(N_i), using a positive central-star test. Perron domination ensures that an odd number of negative tensor factors cannot improve on one most-negative factor and positive Perron factors elsewhere. Thus

    K_* = 1 + max_i (K_i-1) product_{j!=i}(1+rho_j).

The comparison constant (sqrt(2)-1)/sqrt(3) is correct: it combines (K_i-1)/K_i >= 1-1/sqrt(2) and sqrt(N_i/(N_i+1)) >= sqrt(2/3). Remaining factors have (1+rho_j)/sqrt(N_j+1)>1. This is a non-amplification theorem: vanishing product ratios require the maximum of constituent normalized ratios to vanish. It does not prove a universal positive lower bound for the constituents.

### Categorical products and isolated leaves

For H=S intersect(S+S), every vertex in S\H is isolated in the graph induced on S. Conversely a representation s=a+b with a,b in S gives an edge from s to a, so H is exactly the nonisolated subset. Consequently the induced star with leaves S^d\H^d is valid and gives

    K_W2(S^d) / N^(d/2) >= sqrt(1-(|H|/N)^d).

The stronger fixed-base dichotomy is correct: if |H|<N the liminf is at least 1; if S is contained in S+S, the exact full tensor identity yields K_d=K rho^(d-1), whose normalized value is at least the base ratio. The earlier principal T^d argument is also correct, but the isolated-leaf argument gives a simpler treatment of sum-free bases.

For heterogeneous bases the missing-overlap lower bound is sqrt(1-product_i |H_i|/N_i). Its vanishing requires the sum of the missing fractions to vanish. This is only a necessary condition. Near-contained changing bases are not excluded, and no comparison K_T>=c K_W2 has been proved in that regime.

The 18-case overlap diagnostic has the correct scope. It exactly constructs S, T and W2 before numerical spectral calculations. In particular {1,3,6} produces genuinely different T and full-W2 eigenvalues; identifying the two would be wrong. The recorded finite comparisons do not close the growing-base loophole.

### Unequal axis intervals

The three blocks start at -d,0,d with k=ceil(L/3), d=L-k+1. They lie inside [-L,L], are disjoint, have complete edges within each block and between consecutive blocks, and no edges between the outer blocks. In particular the smallest outer distance is 2L-3k+3>L for all positive integer L. Their compression is k(I+A(P3))-I.

The star compression has lower-right entry at most 2L. Optimizing max(c0 L,sqrt(L^2+N)-L), with c0=(sqrt(2)-1)/3, gives exactly

    sqrt((sqrt(2)-1)/(sqrt(2)+5)) = 0.25412093785017187.

The proof already works at W1. It must not be represented as a special gain from full W2.

### Geometric orbits, including composite bases

The argument requires divisibility by b, not a prime valuation law. If exactly one of three signed terms in u-v=w had the least exponent, division by that power and reduction modulo b would force its primitive coefficient to be divisible by b. When precisely two terms share the least exponent, their signed sum is nonzero and has magnitude at most 2 max R. It equals b^gap times a nonzero integer, so gap<=floor(log_b(2 max R)). This remains valid for composite b, even when coefficients share prime factors with b without being divisible by b.

The degree bound and central-star compression follow. The limiting statement requires fixed R and b; a growing seed is not covered.

### Symmetric interval fibers

Under S contained in S+S and q>5h, row coordinates q w+r with |r|<=2h are unique. Any candidate edge discrepancy has digit part of magnitude at most 5h<q, so no nonzero carry can occur. The matrix equality with B tensor T_h is exact, including h=0. The constant-vector average of T_h is

    (2h+1)-h(h+1)/(4h+1).

Perron domination for both nonnegative symmetric factors gives the stated exact minimum-product formula. The containment hypothesis is essential for the full rowset identity; arbitrary varying or asymmetric fibers are not excluded by this theorem.

## Full-operator numerical methodology

Reviewed `multiscale/search.py`, `verify_sparse.py`, `blowup_exact.py`, `analytic/categorical_overlap_check.py`, `correlated/lifts.py`, and `correlated/validate.py`.

- The multiscale rowset is the full {0} union S union(S+S), obtained from convolution and explicit inclusion. The FFT matrix-vector product acts on every row.
- With support radius X, rows have radius at most 2X and difference-minus-generator magnitude at most 5X. FFT length strictly exceeding 5X prevents circular aliases. The correlated and overlap scripts use the still larger threshold 6X+1.
- The multiscale rounding tolerance and correlated threshold 0.5 are practical safeguards, not mathematical certificates of exact convolution recovery.
- The scripts request `which='SA'` from eigsh on the complete symmetric operator. This is not a fixed-profile or restricted-span optimization.
- `sparse_verification.json` records an independently assembled 21,587-row, 7,695,116-nonzero dyadic J8 matrix. Its computed K agrees with the FFT result to 1.42e-14, with first residual 7.05e-12. I inspected this validation and its source; I did not rerun this expensive case.
- The correlated dense validation constructs the matrices directly and records errors at most 1.78e-15 for its two small checks. The manually supplied second set is expressly a construction check, not a validation of the Singer set generator.
- Seven interval blowup comparisons are archived in `multiscale/blowup_verification.json`. These test the entire FFT operator against an independently diagonalized Kronecker product.

These checks give strong numerical implementation evidence, but no interval-certified upper bounds on the full K. No conclusion in this pass should claim that a finite healthy curve proves a uniform asymptotic lower bound, or that failing to find a counterfamily proves the universal conjecture.

## Independent rerun performed for this audit

`audit_checks.py`, using NumPy and SciPy, creates `audit_checks.json`. It does not import the original numerical constructors.

- Nine heterogeneous unitized products: directly assembled full matrices equal the claimed Kronecker expressions, and dense eigenvalues match the exact extremal-product formula.
- Nine categorical products: the isolated-leaf inequalities hold; fully contained cases also match exact full tensor matrices and spectral formulas.
- Axis blocks for all integer L from 1 through 100: exhaustive edge and nonedge checks match the compression proof.
- Orbit bases 2,3,4,6,8,9,10 with finite primitive seeds: exact integer graph checks obey the exponent-gap and degree bounds.
- Four interval-fiber cases h=0,1,2,3: exact integer rowsets and adjacency matrices equal the Kronecker matrices, with dense spectra agreeing to floating precision.

Reproduce with:

    OPENBLAS_NUM_THREADS=1 python audit_checks.py

Finite checks are supplementary; the proofs above provide the general subclass claims.

## Verdict

The five analytic exclusions are valid with their stated hypotheses. The current finite computations are genuinely on full W2, with useful independent checks. The correct outcome is: no vanishing full-W2 family found in this focused pass, several enlargement mechanisms rigorously excluded, and both the general full-W2 conjecture and universal Chowla remain open. The near-contained changing categorical case, growing geometric seeds, and varying fibers are not eliminated by this work.
