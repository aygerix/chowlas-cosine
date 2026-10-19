Completed the brief. The full proofs, computations, limitations, and reproduction commands are in [tdense2_report.md](/Users/jmercedes/Desktop/Projects/Research/chowla-cosine/.research/agents/tdense2_report.md).

The main result is a **complete paper proof that LM-dense fails**, already at \(C=16\). An effective infinite family has \(W_q/V_q^{3/2}\to\infty\) uniformly over every allowed \(q\), while separately satisfying \(M(A)\ge\sqrt n/128\). The construction uses positive Fejér mixtures; its threshold and search complexity are enormous.

The report also contains:

- A reciprocal spike-mask certificate with a constant independent of the number of components on that mixture family.
- Exact Bohr-union audits through ambient size \(200{,}000\). Seventh-moment rational witnesses prove \(M(A)\ge\sqrt n\) for all four samples with \(J=32,35,37,40\).
- An extension of P38 using bounded discrepancy plus averaged local overshoot, and an obstruction showing why prefix discrepancy alone does not suffice for the fixed \(q=2\) window.
- A precise multiplier-selection lemma sufficient for T-dense, with its remaining gap identified.
- A correction to P39: \(V_q=(\|g_q\|_2^2-4a_q)/16\).

Verification passed: **210 rational witnesses**, independent integer checks of over **1.7 million cubic coefficients**, all **23 benchmark criteria**, and **94,242 local-variation checks**.

These are paper proofs and exact finite certificates, not kernel-checked results. Full T-dense and the original sharp Bohr-union asymptotics remain unproved. All computation ran through the requested VM with at most two cores; all jobs finished. No commits or subagents were used.