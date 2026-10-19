# Lean brief (next slot after P34): P36, P33, dilation pinch, then resume Beckner M4

You are the Lean 4 formalization agent for /Users/jmercedes/Desktop/Projects/Research/chowla-cosine (Lean project in
`lean/`).
- Build locally with `lake build`.
- No `sorry`, no new `axiom`, no `native_decide`, no unchecked external solvers.
- Extend `lean/AxiomCheck.lean` with every new headline theorem and report the `#print axioms` output. Only propext,
  Classical.choice and Quot.sound are acceptable.
- Do not edit `.research/*.md`. Do not commit. Do not launch subagents.
- Report: `.research/agents/lean_next_report.md`, kept current as milestones are checked.
- Do not weaken statements: ∀ x : ℝ stays ∀ x : ℝ; A is a genuine `Finset ℕ` of positive integers; every n and D is
  covered, or an exclusion is announced explicitly.
Reuse: `ChowlaCosine/P31/*` (cosSum, circleMean, fejerKernel, Fejér–Riesz, Nikolskii) and `ChowlaCosine/P34/*` (complex
coefficients), once checked.

## Target 1 — P36 (truncation at gaps). Paper proof: .research/PROOFS.md, section "P36".
For finite A ⊂ ℕ_{>0}, an integer D >= 1, and M with ∀ x, −M <= cosSum A x:
    ∀ x, −(M + (1 − cos(π/(D+2)))·Σ_{a∈A, a<=D} a²) <= cosSum (A.filter (· <= D)) x.
Ingredients:
- (i) A nonnegative trigonometric polynomial J of degree D with mean 1 and first coefficient cos(π/(D+2)).
  - Explicit choice: J = |U|² with U(x) = c·Σ_{k=0}^{D} sin(π(k+1)/(D+2)) e^{ikx}, normalized to mean 1. Its first
    autocorrelation coefficient is cos(π/(D+2)).
  - Proving this identity is a finite trigonometric sum computation.
  - Acceptable fallback: ANY explicit nonnegative J of degree D with 1 − Ĵ(1) <= c/D², c an explicit constant.
    Announce the constant. For example, the normalized square of the Fejér kernel of degree ⌊D/2⌋ gives an explicit c.
- (ii) PD increment inequality: 1 − Ĵ(a) <= a²(1 − Ĵ(1)), from 1 − cos(aθ) <= a²(1 − cos θ) and J >= 0.
- (iii) cosSum A ∗ J = Σ_{a<=D} Ĵ(a) cos(a·) >= −M, since J >= 0 has mean 1 and kills frequencies > D.
- (iv) Conclude.
Also state the gap corollary: if A ∩ (Y, D] = ∅, then the error is <= (1 − Ĵ(1))·Y²·|A ∩ [1, Y]|.

## Target 2 — P33 ratio lemma. Paper proof: .research/PROOFS.md, section "P33".
A finite nonempty, all elements positive, m = min A, X = max A, ∀ x, −M <= cosSum A x  ⇒  M >= |A|·m/X.
(A simpler sufficient route: the measure on N-th roots of unity in PROOFS P33, or any correct proof.)

## Target 3 — Dilation pinch.
For q >= 1: Σ_{j=0}^{q−1} cosSum A (2πj/q) = q·|A.filter (q ∣ ·)|. Hence, if ∀ x, −M <= cosSum A x, then
    |A.filter (q ∣ ·)| >= |A|/q − (1 − 1/q)·M.

## Target 4 — Resume Beckner M4 (previous report: .research/agents/lean_p31_report.md, "T5 M4").
- 51 audited declarations are already in `lean/ChowlaCosine/Beckner/`.
- Continue the geometric heat-flow Brascamp–Lieb argument: apply the global integration bridge to the concrete
  geometric product, then the rescaling limit, the initial-time limit and the density passage. Then the 2×2 frame
  change of variables, giving the sharp Young constant A_p A_q A_{r'}.
- Then M5: the sharp autocorrelation bound ‖u ∗ ũ‖₂² <= (4/(3√3))·‖u‖_{4/3}⁴ style statement as in the original
  brief .research/agents/lean_p31_brief.md, and P31-N.
- Partial progress is valuable. Report exactly what is checked.
