Completed **all targets T0–T3**, including T1’s run-top corollaries and T3(d)–(e). They are **kernel-checked**: the full build passed, and all 33 audited declarations show exactly `[propext, Classical.choice, Quot.sound]`, with no `sorry`, new axioms, or `native_decide`.

The [report](/Users/jmercedes/Desktop/Projects/Research/chowla-cosine/.research/agents/lean_o4plus_report.md) contains the exact formal statements, Lean names, and complete verification output.

- [FibreSchur.lean](/Users/jmercedes/Desktop/Projects/Research/chowla-cosine/lean/ChowlaCosine/FibreSchur.lean): T0–T2, actual quotient fibres, zero-fibre classifications, and run-top bounds.
- [HalfSet.lean](/Users/jmercedes/Desktop/Projects/Research/chowla-cosine/lean/ChowlaCosine/HalfSet.lean): T3(a)–(e).
- [AxiomCheck.lean](/Users/jmercedes/Desktop/Projects/Research/chowla-cosine/lean/ChowlaCosine/AxiomCheck.lean): axiom audit.

No false statement or missing hypothesis was found. T3(c)’s general constant is
\[
c_1=p^2(2\lambda+3\lambda^2g(0)+\lambda^3),
\]
which agrees with the brief and specializes to \(p^2\lambda(\lambda-1)(\lambda-2)\).

All Lean builds ran on `dirichlet` through `src/dirun.sh`. The lead’s jobs were left untouched, `fejer` was untouched, and no commit was made.