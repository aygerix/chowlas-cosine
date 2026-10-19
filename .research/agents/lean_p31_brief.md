# Brief: Lean 4 formalization of P31 (window–Nikolskii inequality) and its elementary constant (codex agent, Sol 6.1 xhigh)
(lead, 2026-10-19). Verification route for this project = kernel check; no outside review.

## Read first
`.research/PROOFS.md`: sections P31, Lemma P31-N, Lemma P31-E, and the corrections recorded there.
`.research/agents/p31_report.md`: the adversarial review, with its corrected statements.

## Targets (exact statements; announce any weakening)
- T1 (Fejér–Riesz, finite). Every real trigonometric polynomial h(x) = Σ_{|k|<=L} c_k e^{ikx} with h(x) >= 0 for all
  real x equals |U(e^{ix})|² for some analytic U = Σ_{j=0}^{L} u_j e^{ijx}, u ∈ C^{L+1}.
  - Route: polynomial z^L·h(z) and its root symmetry z ↔ 1/z̄. Roots on the circle have even multiplicity since
    h >= 0. Use the fundamental theorem of algebra (in mathlib).
  - Not in the local mathlib (checked). This is a valuable standalone contribution.
  - Weaker usable form: c = u ⋆ ũ (autocorrelation) for some u ∈ C^{L+1}.
- T2 (Lemma P31-E). For every L >= 0 and v >= 0 on {0..L} with ‖v‖₂ = 1:
      ‖v ∗ v‖₂² <= μ(L + 1) + λ/3,   λ = 71/100, μ = 811/1000.
  Pieces:
  - (E1) ‖v∗v‖² <= N − 2Σ_{j<L} a_j(1 − a_j), a_j = cumulative v²; proof by Cauchy–Schwarz per index plus Abel
    summation;
  - (E2) ‖v∗v‖² <= (Σv)²;
  - the trapezoid identity for w(A) = A(1 − A);
  - weighted Cauchy–Schwarz with weight μ − λ(1 − 2w(A));
  - the constant: (1 − λ)∫_0^1 dA/(μ − λ(1 − 2A(1 − A))) <= 1.
  For Lean, certify the constant by a rational upper Riemann sum (the integrand is monotone on each half) or a
  verified log/artanh bound. No native_decide.
  - Also acceptable as an alternative or addition: the review agent's elementary ρ_L <= 19/20 for L >= 1.
- T3 (P31 main inequality). For finite A ⊂ Z_{>0}, X = max A, n = |A|, M with f_A(x) >= −M for all real x, w >= 1,
  κ(k) = (1 − |k|/(w+1))₊, W = Σ κ(k)², S_A = Σ_{a∈A} κ(a)², L = X + w, and any C with
  ‖U‖₄⁴ <= C‖U‖₂⁴ for all analytic U of degree <= L:
      W(n/2 + M²) <= C(M² + S_A/2).
  - Steps: F_{w+1} >= 0 (Fejér kernel); h = F(· − x₀)(f + M) >= 0 of degree <= L; T1; integrate over x₀ (finite sums,
    Fubini for continuous functions on a torus or square); the moment identities.
- T4 (corollaries). Combine T2 + T3: the explicit dense statement with the elementary constant. Example: for X large
  enough, |A| >= (41/100)(1 + small)·X ⇒ M² >= c·n with explicit c. Choose explicit rational ε, η and state the
  finite-X fallback M >= 1/2.

- T5 (sharp constant; same project, after T1–T4 are kernel-checked). Formalize Beckner's sharp Young inequality and
  Lemma P31-N, giving ρ_L <= β(1 + 2/√(L+1))³ with β = 4/(3√3). This upgrades the dense threshold from ≈ 0.41 to any
  δ > 2/(3√3).
  - Follow `.research/agents/lean_beckner_brief.md`, milestones M1–M5. Put those files under
    `lean/ChowlaCosine/Beckner/`; its rules apply there.
  - Then formalize the sinc-interpolation proof of P31-N from `.research/agents/p31_report.md`, section "P31-N by
    exact sinc interpolation".
  - Partial progress is fine: report exactly which milestones are kernel-checked.

## Rules
- Lean project `lean/` (lakefile there). New files under `lean/ChowlaCosine/P31/`. Do not modify existing
  kernel-checked files. Append AxiomCheck entries.
- Track every `sorry`, new axiom, `native_decide`. KERNEL-CHECKED only if `#print axioms` shows only propext,
  Classical.choice, Quot.sound.
- No silent weakening: no finite grid for "all real x", no multiset for set, no restriction of L or n. If you need a
  hypothesis (e.g. state T3 with C as a hypothesis), say so; T2 then discharges it.
- Builds local (`lake build` in lean/). Numerics, if any, on dirichlet via src/dirun.sh. Never touch the VM fejer.
- Edit only `lean/ChowlaCosine/P31/`, `lean/ChowlaCosine/Beckner/`, `lean/AxiomCheck.lean` (append), `lean/ChowlaCosine.lean` (append imports),
  `.research/agents/lean_p31_report.md`, `.research/agents/lean_p31_scratch/`. Do not commit.
- Report early, update after each target. Order: T3 with C as hypothesis, then T1, then T2, then T4, then T5 (Beckner M1–M5, then P31-N).
