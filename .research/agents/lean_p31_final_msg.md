**T1–T4 are kernel-checked. T5 is partial, with the remaining block in M4.** The detailed deliverable is [lean_p31_report.md](/Users/jmercedes/Desktop/Projects/Research/chowla-cosine/.research/agents/lean_p31_report.md).

Completed in the requested order:

- **T1:** Full finite Fejér–Riesz, including zero polynomials, lower actual degrees, and unit-circle roots.
- **T2:** The exact convolution bound \((811/1000)(L+1)+71/300\), for every \(L\ge0\).
- **T3:** The window inequality with the requested analytic constant hypothesis. Factorization is proved and discharged internally.
- **T4:** The all-size dense theorem
  \[
  n\ge 41X/100 \;\Longrightarrow\; M\ge \sqrt n/1000,
  \]
  including the nonempty-set fallback \(M\ge1/2\).

For Beckner, **M1** is checked for every finite admissible exponent triple, plus the conjugate \(L^\infty\) boundary. **M3** includes finite Gaussian norm/convolution formulas and exact project-exponent attainment of \(4/(3\sqrt3)\). The optional sharp shortcut in M2 was skipped; its constant-one specialization is checked.

**M4 has 51 audited declarations**, including the actual pointwise geometric heat-flow differential inequality and a global integration bridge with explicit hypotheses. The remaining block is applying that bridge to the concrete geometric product, then proving the rescaling limits and density passage. Sharp Young, M5, and sinc P31-N are **not** claimed checked.

Final verification:

- `lake build`: **passed, 8739 jobs**.
- Complete `AxiomCheck.lean`: **passed, 272/272 audit entries**, using only `propext`, `Classical.choice`, and `Quot.sound`.
- **Zero** new `sorry`, axiom declarations, `native_decide`, or unchecked solvers.
- No commits were made.