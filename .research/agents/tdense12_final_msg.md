Round 12 is complete, and the [report is current](/Users/jmercedes/Desktop/Projects/Research/chowla-cosine/.research/agents/tdense12_report.md).

The main results are:

- **PROVED:** Every nested residue-removal model with n elements and r occupied classes modulo N satisfies  
  `M(A) ≥ n / ((3π + 2)r)`.  
  This excludes positive-density counterexamples with N=o(√X), regardless of removal order.
- **PROVED:** The partial-period Fejér identity is correct. A new cyclic homogenization argument supplies the local balance and rational-atom conditions needed to prove that TBS would imply the cyclic half-set square-root bound.
- **Task 1 alternative (B):** A precise cyclic support-gap statement, **CSFG(20)**, implies a uniform front gap and a T-dense range strictly beyond 1/D. CSFG remains **CONJECTURED**; the implication has a full proof.
- **PROVED corrections and obstructions:** The smooth-limit complex roughness coefficient is `2p₀−p₀²`; real cosine energy requires a separate identity. Arbitrary nonnested schedules refute both proposed X/N and X√(p₀/N) bounds, even for N=2.
- **Task 3:** A precise scalar-relaxation barrier and a conditional exponent improvement from a named missing peak lemma. No unconditional exponent above 1/3 was established.

All computation used the prescribed VM wrapper with four cores. The [verification record](/Users/jmercedes/Desktop/Projects/Research/chowla-cosine/.research/agents/tdense12_scratch/final_audit.json) includes 980 exact count checks, 64 Arb progression checks, six certified finite-set negative points, and the structured/Gurobi searches.

The unconditional T-dense endpoint remains C<2000/259. No commits, subagents, root research-record edits, or LaTeX artifacts were made.