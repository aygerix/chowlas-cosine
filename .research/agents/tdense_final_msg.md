Updated [`.research/agents/tdense_report.md`](/Users/jmercedes/Desktop/Projects/Research/chowla-cosine/.research/agents/tdense_report.md) with full proofs, failed approaches, reproducible checks, and the remaining gap.

The main results are:

- **PROVED on paper:** A denominator-filter theorem for cumulative rounding of decreasing profiles with rational starting density. For the explicit quadratic family \(p_j=\tfrac12(1-j/X)^2\), it gives
  \[
  M(A_X)\ge \frac{\sqrt{|A_X|}}{1000}.
  \]
  These front-loaded sets have no adjacent members, refuting the suggested implication from front-loading to long consecutive runs.

- **PROVED on paper:** Independently rounded quartic profiles obstruct every bounded-degree nonnegative multiplier followed by the Fejér-window P31 certificate, even with optimal Nikolskii constants. The report states the precise limits of this obstruction.

- **PROVED reduction to one missing lemma:** For
  \[
  T_q=(1-\cos qx)f_A+\tfrac12\,1_A(q),
  \]
  it suffices to find \(q\le\max A\) with variance \(V_q\ge\eta(C)n\) and third moment \(W_q\le B(C)V_q^{3/2}\). I derived its exact integer triple-count formula. **This lemma remains conjectured.**

Exact arithmetic verified the concrete conditions \(V_q\ge n/10\), \(W_q\le2V_q^{3/2}\) on all 21 benchmark examples and exhaustively on **262,135 sets** with \(\max A\le18\) and \(\max A\le10|A|\).

T-dense remains unproved for arbitrary dense sets; there is no new universal hull threshold or kernel verification. All computations ran through `src/dirun.sh -c 2`. I made no commits, launched no subagents, and edited no root `.research/*.md` files.