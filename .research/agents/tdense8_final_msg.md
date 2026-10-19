Completed Tasks 1, 2 and the optional Task 3. The proofs, computations and handoff are in [tdense8_report.md](/Users/jmercedes/Desktop/Projects/Research/chowla-cosine/.research/agents/tdense8_report.md).

- **PROVED on paper — Task 1:** `rho* <= 203819/250000 = 0.815276`. A four-point Gram constraint and a monotone polynomial potential improve P17(a)’s 0.90565. The rational certificate passed both exact Bernstein verification and independent Sturm checks. Combined with P58 alone, it gives **T-dense(5.311)**.

- **PROVED on paper — Task 2:** **T-dense(6.156)**, exceeding the requested 6.054 threshold. The new ingredient is the product-window constraint: the limiting residual energy `e = p(1-p)` must itself be positive definite. This forces `p(0) <= 1/2` and excludes the round 7 witness. The resulting sufficient range is `C < 4(2-rho*)/r`. The constant at C=6.156 remains ineffective.

- **PROVED on paper — Task 3:** An explicit bound **`c(3) = 10^(-6,000,005)`**, using a finite geometric family of Gaussian smoothing widths and elementary P31-E. The constant is extremely small, but the argument removes compactness from this C=3 result.

- **NUMERICAL:** The best observed autocorrelation value was **0.7238796373** at 800 points. The general PWL search showed no advantage at the common tested resolution; equality of the two suprema remains unresolved.

The [independent verification results](/Users/jmercedes/Desktop/Projects/Research/chowla-cosine/.research/agents/tdense8_scratch/independent_verification.json) and [artifact manifest](/Users/jmercedes/Desktop/Projects/Research/chowla-cosine/.research/agents/tdense8_scratch/manifest.json) are saved. All mathematical computation ran on the specified VM with two cores, and optimization used Gurobi. No root `.research/*.md` files were edited, no commits were made, and no subagents were launched. These are paper proofs with exact computational certificates where stated; no new Lean kernel verification is claimed.