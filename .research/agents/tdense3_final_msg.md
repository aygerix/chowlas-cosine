Completed the research round and wrote the full [tdense3 report](/Users/jmercedes/Desktop/Projects/Research/chowla-cosine/.research/agents/tdense3_report.md).

The main results are:

- **PROVED, paper proof:** every fixed nonzero finite staircase profile—including irrational Sturmian slopes—has M ≥ c(p)X under cumulative rounding, uniformly in the rounding phase.
- **PROVED, paper proof:** P41+ for fixed flat/curved profiles, excluding flat energy from the adverse-energy budget.
- **PROVED, paper proof:** P41-B for fixed smooth Diophantine Bohr profiles. For fixed finite Fourier profiles, the argument removes the Diophantine assumption under the stated orbit-average curvature hypotheses.
- **PROVED obstruction:** positivity and spatial localization alone do not force monotone Fourier decay. The report also gives an exact Vandermonde obstruction for common Fejér-bump representations.

All computations used the specified VM through `src/dirun.sh -c 2`. The audit covered **121 zoo sets, including 40 E68 rows, plus 45 extension examples**. Arb certified all **516,096 Bohr floor decisions**; minima and bulk integrals remain numerical. No audited set had both β₁ < 0.13 and R < 0.60.

The full **T-dense conjecture remains open**. The report separates the proved classes from the unresolved need to control arbitrary binary spectra at the square-root scale.

Reproducible code and results are in [audit.py](/Users/jmercedes/Desktop/Projects/Research/chowla-cosine/.research/agents/tdense3_scratch/audit.py) and [summary.json](/Users/jmercedes/Desktop/Projects/Research/chowla-cosine/.research/agents/tdense3_scratch/summary.json). No commits or subagents were used.