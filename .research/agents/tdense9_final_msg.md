The round 9 report is current: [tdense9_report.md](/Users/jmercedes/Desktop/Projects/Research/chowla-cosine/.research/agents/tdense9_report.md).

The main results are:

- **PROVED — T-dense(C) for every C < 6.936623145469854…**, including **T-dense(6.9366)**. The proof uses a new scalar energy-profile reduction and exact degree-24 Toeplitz/potential certificates. Independent rational Bernstein and Sturm checks passed. This is a computer-assisted paper proof; the constant on the newly added range remains ineffective, and it is not Lean-checked.

- **NUMERICAL reach near 7.267, with an exact witness.** For the specified two-profile relaxation, the rigorous bounds are  
  `6.936623145469854… ≤ C₉ < 7.267398825422`.  
  The 160-cell witness has exact integer spectral factors, satisfies `e=p−p²`, and passes both windows for **every positive scale**. Global optimality remains open.

- **PROVED — the proposed completeness reduction misses a constraint.** Residual covariance kernels must be **completely positive**. An explicit profile satisfies both PD conditions and every window but fails a rigorously certified Horn copositive test. Thus the two-profile reach must remain distinguished from the full macroscopic reach.

- **PROVED — explicit constants throughout the previous range.** The finite Gaussian argument now gives an explicit `c(C)>0` for every `C < 4(2−0.815276)/r₀`, approximately **6.156 with Beckner**, covering the entire requested `C<4/r₀` range. The report includes the formula, worked constants, and precise Lean dependencies.

- **Task 3 — a formal packet escape and its binary gap.** A weighted mesoscopic packet family satisfies positivity and the first two macroscopic coefficient identities. It fails the mandatory binary cubic moment. The report derives that deficit and states a precise sufficient cubic-resonance inequality as **CONJECTURED**.

The strongest certificate and its independent verification are saved in [long_scalar_d24_exact.json](/Users/jmercedes/Desktop/Projects/Research/chowla-cosine/.research/agents/tdense9_scratch/long_scalar_d24_exact.json) and [long_independent_verification.json](/Users/jmercedes/Desktop/Projects/Research/chowla-cosine/.research/agents/tdense9_scratch/long_independent_verification.json).

All mathematical computation used the specified VM through `src/dirun.sh -c 2`; optimization used Gurobi. Edits were confined to the report and round 9 scratch directory. No root-level research Markdown was edited, and no commits or subagents were created.