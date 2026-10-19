Updated [tdense17_report.md](/Users/jmercedes/Desktop/Projects/Research/chowla-cosine/.research/agents/tdense17_report.md), preserving the previous proofs and shifted-interval obstruction.

- **T1 remains open**, but there is a new proved result: for independent tapered roundings, P28 certifies M(A) >= sqrt(|A|)/(8 sqrt(21)) with probability at least 1−169/μ for sufficiently large expected cardinality μ. Thus typical independent tapering cannot defeat the four-way cover.
- **T2 now includes a rigorous sufficient boundary condition:** M(A) >= (2/(3π)−1/8)k−D_d(k), where D_d(k) measures missing progression differences and weighted occupancy beyond their endpoint. The smooth-prefix counterexamples fail this sharpness condition, as they should.
- Added the joint necessary conditions with explicit ε dependence. Also checked that unrestricted P29(b) already recovers M(A) exactly at h=1, L=2; the numerical search therefore explicitly restricts its Gibbs certificate to L=X+h.
- Tested **58 adversarial sets and 4,000 swap proposals**, minimizing the maximum of the certificates. No asymptotic family defeating all four was found. The best finite audited objective was approximately 0.428184.
- Added an independent, entirely Arb-based certificate proving **M <= 76.8874** for the existing CLIQUE-S instance. It gives clique/K >= 6.66559150 globally and >= 6.65908849 for a clique contained in ±A.

All mathematical computation ran on the VM through `src/dirun.sh`, using at most four cores. Writes stayed within the agent report and scratch directory; no commits or subagents were used.