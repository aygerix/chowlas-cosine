# Brief: Lean 4 formalization of Beckner's sharp Young convolution inequality (codex agent, Sol 6.1 xhigh)
(lead, 2026-10-19; requested by the user: "it would be valuable to have math like that formalized")

## Target theorem (exact statement, do not weaken without announcing it)
For 1 <= p, q, r <= ∞ with 1/p + 1/q = 1 + 1/r, and f ∈ L^p(R), g ∈ L^q(R):

    ‖f ∗ g‖_r <= (A_p A_q A_{r'})·‖f‖_p ‖g‖_q,   A_s = (s^{1/s} / s'^{1/s'})^{1/2},  1/s + 1/s' = 1.

This is Beckner (1975) / Brascamp–Lieb (1976). The constant is sharp, with Gaussian extremizers.
- Project use: the case p = q = 4/3, r = 2 gives ‖h∗h‖₂² <= A_{4/3}⁴ ‖h‖_{4/3}⁴ with A_{4/3}⁴ = 0.76980.
  It enters PROOFS P17(b) and the sharp asymptotic constant of P31 (Lemma P31-N).
- P31 itself no longer depends on it: Lemma P31-E is elementary, with constant 0.811.
- So this is a library-quality formalization goal in its own right. It also sharpens P31's thresholds.

## Status of the local mathlib (lean/.lake/packages/mathlib, checked by the lead)
- No Young convolution inequality, not even the non-sharp ‖f∗g‖_r <= ‖f‖_p‖g‖_q. "Young" occurs only as the
  product inequality in Analysis/MeanInequalities.lean.
- Convolution exists (MeasureTheory / Analysis.Convolution), as do L^p spaces (MeasureTheory.Lp, eLpNorm) and
  Hölder. Check what else exists before building: Riesz–Thorin, Gaussian integrals, heat kernel.

## Milestones (each one kernel-checked before moving on; report after each)
- M1. Non-sharp Young convolution inequality on R, constant 1, all exponents (or at least the finite ones). Use the
  standard three-factor Hölder argument. This alone is a mathlib-worthy contribution.
- M2. The special case needed here, p = q = 4/3, r = 2, if a shortcut exists. Otherwise skip.
- M3. Gaussian computations: ‖gaussian‖_p in closed form, and convolution of Gaussians. This shows the constant is
  attained (sharpness).
- M4. The sharp inequality. Choose the most formalizable proof; recommended: heat-flow monotonicity (Carlen–Lieb–Loss;
  Bennett–Carbery–Christ–Tao for Brascamp–Lieb; also Barthe's transport proof).
  - Flow f, g by the heat equation at suitably scaled times.
  - Show the trilinear form, normalized by the norms, is monotone.
  - Identify the limit with the Gaussian value.
  - Write a paper proof first in the report, at the granularity of the Lean files. Then formalize lemma by lemma.
  A reduction to nonnegative, bounded, compactly supported (or Schwartz) functions plus density is fine, if done
  rigorously.
- M5. Corollary: ‖h ⋆ h̃‖₂² <= A_{4/3}⁴ ‖h‖_{4/3}⁴. Also the project form: for h supported on an interval of length ℓ,
  ‖h∗h‖₂² <= 0.7698·ℓ·‖h‖₂⁴ (Hölder).

## Rules
- Lean project: `lean/` (lakefile there). Put new files under `lean/ChowlaCosine/Beckner/`. Do not modify existing
  kernel-checked files. Add an AxiomCheck entry for every main theorem.
- Track and report:
  - every `sorry`;
  - any new axiom (none allowed in a claimed result);
  - any `native_decide` / unchecked external tool (none allowed).
  Only call a result KERNEL-CHECKED if `#print axioms` shows only propext, Classical.choice, Quot.sound.
- No weakening: do not replace R by a finite group, L^p by bounded functions without a density argument, or the
  sharp constant by a weaker one, without saying so explicitly in the report. A finished M1 + M3 with M4 open is an
  honest partial result. Report it as such.
- Builds may run locally (`lake build` in lean/); heavy numerics (if any) on dirichlet via src/dirun.sh. Never touch
  the VM fejer.
- Edit only files under `lean/ChowlaCosine/Beckner/`, `lean/AxiomCheck.lean` (append only), the report
  `.research/agents/lean_beckner_report.md`, and `.research/agents/lean_beckner_scratch/`. Do not commit.
- Write the report early and update it after each milestone.
