Completed the report: [p31_report.md](/Users/jmercedes/Desktop/Projects/Research/chowla-cosine/.research/agents/p31_report.md).

The principal P31 inequality survives the audit. I proved P31-N rigorously by exact sinc interpolation, obtaining
\[
\rho_L\le \frac{4}{3\sqrt3}
\left(1+\frac{2}{\sqrt{L+1}}\right)^3
=0.769800\ldots+O((L+1)^{-1/2}).
\]
I also proved the elementary uniform bound \(\rho_L\le0.95\) for every \(L\ge1\), and the explicit bound \(\rho_L\le0.78\) for \(L\ge249999\).

The report identifies these corrections:

- P31(iii)’s fixed-scale threshold needs the factor \(1+\varepsilon\) in the denominator.
- The Nikolskii formulation requires analytic polynomials supported on \(0,\ldots,L\); the stated two-sided interpretation fails already at \(L=1\).
- \(\rho_0=1\), so a uniform bound below 1 cannot include degree zero.
- P29’s squared bound needs a positive part; \(A=\{12\}\) disproves its unqualified version.

The corrected argument proves square-root bounds at every fixed density \(\delta>2/(3\sqrt3)\). The report includes explicit constants, sparse-tail bounds, and a rigorous obstruction to the positive low-pass approach.

All computations ran on **dirichlet**, using at most four cores. The 23 adversarial examples passed 161 window tests. Numerical minima remain explicitly labeled estimates. The literature audit also found the relevant [Kolountzakis 1996 dense-cosine theorem](https://eigen-space.org/mk/ps/dense.pdf).

Only the report and its scratch directory were edited. No commit was made.