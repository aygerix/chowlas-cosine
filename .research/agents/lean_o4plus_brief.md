# Brief: Lean 4 formalization — run-top fibre inequalities (P20 Thm 2, O4⁺) and the half-set identities (line D)
(lead, 2026-10-18 late night; for a codex agent, Sol 6.1, xhigh reasoning)

## Context
Project: Chowla's cosine problem (see CLAUDE.md, `.research/PROOFS.md` P20, P22 and NOTEBOOK "Branch 2 reassessed").
Existing Lean development: `lean/ChowlaCosine/*.lean` (Lean 4.33.1 + mathlib, built on the GCP VM dirichlet).
- RunTopGroup.lean already works with additive characters of ZMod p and finite sums; reuse its conventions.
- Build: `src/dirun.sh -c 4 -m 16 sh -c 'cd lean && ~/.elan/bin/lake build'` (about 75 s with the cached mathlib).
- Axiom check: `lean/ChowlaCosine/AxiomCheck.lean`. Run `lake env lean ChowlaCosine/AxiomCheck.lean` the same way.
- Never build on the laptop. Never touch the VM `fejer`.

## Targets (formalize exactly these statements; do not weaken them silently)
Notation: Γ is a finite additive commutative group, Γ̂ its characters (`AddChar Γ ℂ`). For A ⊂ Γ, F(χ) = Σ_{a∈A} χ(a).
A function P : H → ℂ on a finite abelian group H is positive definite (p.d.) if its Fourier transform
P̂(ψ) = Σ_y P(y)·conj(ψ(y)) is a nonnegative real for every ψ ∈ Ĥ.

**T0 (Schur, finite abelian).** If P, Q : H → ℂ are p.d., so is the pointwise product P·Q. Hence P^r is p.d. for all r.
(Proof: the transform of a product is (1/|H|)·(P̂ ⋆ Q̂), a convolution of nonnegative functions.)

**T1 (P20 Theorem 2, order 3).** Hypotheses:
- A ⊂ Γ with A = −A and 0 ∉ A;
- K ≥ 0 real with Re F(χ) ≥ −K for every nontrivial χ (F is real since A = −A);
- t ∈ Γ of order exactly 3, and χ₀ ∈ Γ̂ with χ₀(t) = ω = e^{2πi/3}.
Let H̄ = Γ/⟨t⟩. For a coset y define U(y) = Σ_{x ∈ A ∩ y} χ₀(x). Let D = {cosets y ≠ ⟨t⟩ with |A ∩ y| = 2} and
E = {cosets y ≠ ⟨t⟩ with |A ∩ y| = 1}. Let u₀ = U(⟨t⟩), a real number in {0, −1}.
Conclusion: |D| − |E| ≤ (K + u₀)³.
Proof route:
- For ψ ∈ Ĥ̄ (characters of Γ trivial on t), Û(ψ) = F(χ₀·conj ψ) up to the conjugation convention, and χ₀·conj ψ is
  nontrivial, so Û ≥ −K. Hence U + K·δ_{⟨t⟩} is p.d. on H̄.
- By T0 its cube is p.d. Evaluate its transform at ρ, where ρ(y) := χ₀(x)³ for any x ∈ y (well defined: χ₀(t)³ = 1).
- Fibre computation: U(y)³ = ρ(y) on E, −ρ(y) on D, 0 on full or empty cosets.
Also prove the run-top corollary: with B_t = {m ∈ A : m − t ∈ A, m + t ∉ A}, |B_t| ≤ |D| + 1, so |B_t| ≤ |E| + (K+u₀)³ + 1.

**T2 (O4⁺, order 4).** Same as T1 with ord t = 4, χ₀(t) = i, ρ(y) := χ₀(x)⁴. Let D₂ = cosets y ≠ ⟨t⟩ whose fibre is a
2-run {x, x+t}; D₃ = 3-point fibres; E = 1-point fibres. (A fibre {x, x+2t} contributes 0, as do full and empty fibres.)
Conclusion: 4|D₂| ≤ |E| + |D₃| + (K + u₀)⁴, with u₀ = U(⟨t⟩) ∈ {0, −1}.
Fibre table: (Σ_{s∈S} i^s)⁴ = 1 (singleton), −4 (2-run), 0 ({k, k+2}), 1 (3 points), 0 (full or empty).

**T3 (line D identities, Γ = ZMod p, p an odd prime).** Hypotheses: g : ZMod p → {±1}, and ĝ(γ) = Σ_x g(x)·e(−γx/p)
(unnormalized). Statements:
- (a) Σ_γ ĝ(γ)·ĝ(δ − γ) = p²·[δ = 0].
- (b) For every real λ, h := ĝ + λ satisfies, for all δ ≠ 0: (h ⋆ h)(δ) = 2λ·p·g(0) + pλ², with
  (h ⋆ h)(δ) = Σ_γ h(γ)h(δ−γ).
- (c) h⋆h⋆h = p²·h + c₁·1 with c₁ = p²(3λ + 3λ²g(0) + λ³) − p²λ. Check the constant against the lead's
  derivation: with g(0) = −1, h⋆³ = p²h + p²λ(λ−1)(λ−2). Derive the general-g(0) form yourself and state it.
- (d) (spectral gap) Assume moreover g is even (g(−x) = g(x)), Σ_x g(x) = ±1 (balanced), λ ≥ 1, and ĝ(γ) ≥ −λ for
  all γ ≠ 0 (ĝ is real). Then h ≥ 0 everywhere, and for every γ₀ ≠ 0, with a := h(γ₀):
      0 ≤ 3a³ − (3S₂ − p²)·a + c₁,   S₂ := Σ_γ h(γ)².
  Proof: positivity of u⋆u⋆u at γ₀ for u = h − a·δ_{γ₀} ≥ 0, expanded using (a)–(c).
- (e) (consequence) Under (d) with g(0) = −1, every nonzero coefficient satisfies ĝ(γ) ≤ λ√p.
  Proof: h(γ)² ≤ (h⋆h)(2γ).

## Rules
- Statements in Lean must match the ones above. If a hypothesis is missing or a statement is false, STOP and report the
  counterexample. Do not change the statement to make it provable.
- No `sorry`, no new axioms, no `native_decide`. Report the AxiomCheck output: it must show only
  [propext, Classical.choice, Quot.sound].
- New files go in `lean/ChowlaCosine/` (suggested: FibreSchur.lean for T0–T2, HalfSet.lean for T3). Import them in
  `lean/ChowlaCosine.lean` and add `#print axioms` lines to AxiomCheck.lean.
- Edit only those Lean files and `.research/agents/lean_o4plus_report.md`. Do not edit other `.research` files and do
  not commit.
- Priority: T0, T1, T2 first; then T3(a)–(c); then (d)–(e). Partial completion is fine; report precisely what is proved.

## Deliverable
`.research/agents/lean_o4plus_report.md` containing:
- each statement as formalized, with its Lean name;
- build and axiom-check output;
- any discrepancy found in the paper statements, with a counterexample if relevant.
