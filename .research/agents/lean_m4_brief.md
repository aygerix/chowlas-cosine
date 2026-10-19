# Lean brief: finish Beckner M4 (sharp Young on R² frames), then M5 and P31-N

Project: /Users/jmercedes/Desktop/Projects/Research/chowla-cosine, Lean in `lean/`.
- Build locally with `lake build`.
- No `sorry`, no new `axiom`, no `native_decide`.
- Extend `lean/AxiomCheck.lean` and report `#print axioms`. Only propext, Classical.choice and Quot.sound are allowed.
- Do not edit `.research/*.md`. Do not commit. Do not launch subagents.
- Report: `.research/agents/lean_m4_report.md`, kept current.
- Do not weaken statements. Intermediate hypotheses (compact support, positive mass) are fine only as stepping stones,
  and must be announced as such.
Starting point: `.research/agents/lean_next_report.md`, section "Exact remaining dependencies and next derivation",
and the 51 + 34 audited declarations in `lean/ChowlaCosine/Beckner/`. Original targets: `.research/agents/lean_p31_brief.md`
(T5: M1–M5, P31-N).
Order:
1. The large-time limit of the actual whole-plane product integral: finite-product normalization, 2-D change of
   variables, dominated product limit, Gaussian integral.
2. The initial-time Fatou/approximate-identity passage.
3. Density from compact nonnegative data, plus ae pullback by nonzero linear forms (including zero-mass cases).
   This removes the intermediate support restriction.
4. The explicit 2×2 frame, determinant/sharp-factor algebra and Lp cancellation. Headline: the sharp Young inequality
   on R with Beckner's constant (A_p A_q A_{r'}).
5. M5 (sharp autocorrelation bound as in lean_p31_brief.md), then P31-N.
Partial progress is valuable. Report exactly what is checked.
