Completed round 13 and kept [tdense13_report.md](/Users/jmercedes/Desktop/Projects/Research/chowla-cosine/.research/agents/tdense13_report.md) current throughout. Task 1 is delivered through the permitted **precise-barrier alternative**.

- **PROVED:** Universal PK is false. Genuine symmetric half-sets can have Λ of order q while K=O(√(q log q)).
- **PROVED:** An explicit relaxation preserves exact convolution at every frequency ±1,…,±J, with the peak at 1, for any J=o(q^(1/3)), while retaining K=q^(1/3)/2. An omitted equation detects a defect of order q², making the relaxation’s limitation explicit.
- **PROVED:** The literal R12 fake fails cubic count integrality. A replacement construction nevertheless satisfies any fixed number of scalar moment, integer-count and Newton-congruence constraints.
- **VERIFIED:** Completed 36 Gurobi trade-off models, certified the full curves at q=17 and 37 by exhaustive interval-enclosed enumeration, and tested 20 binary constructions through X=2²⁰. Every retained construction has an independently checked 220-bit Arb dip proving R>0.6.

The audit caught and corrected a block-size mismatch in the small rounding MILPs; the failed versions are preserved. It also flagged a discrepancy between the supplied q=89 E41 pair list and its printed K value.

All final checks passed; details are in [final_summary.json](/Users/jmercedes/Desktop/Projects/Research/chowla-cosine/.research/agents/tdense13_scratch/final_summary.json). No unconditional exponent above 1/3 or binary escape below R=0.56 was established. All computation used the prescribed VM with at most four cores; no subagents, commits, or top-level research-note edits were made.