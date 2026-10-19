# Lean brief (codex verification agent): formalize P73 (robust few-spike lemma, Z version)

You are formalizing ONE elementary theorem in Lean 4 / mathlib in /Users/jmercedes/Desktop/Projects/Research/chowla-cosine/lean.
- Read CLAUDE.md (section "Lean 4 formalization") and .research/PROOFS.md section P73.
- Rules:
  - Do NOT edit .research/*.md. Do not commit. Do not launch subagents.
  - Report: `.research/agents/lean_p73_report.md` (keep it current). Scratch: `.research/agents/lean_p73_scratch/`.
  - New file: `lean/ChowlaCosine/FewSpike.lean`, imported from `lean/ChowlaCosine.lean`.
  - Build with `lake build` in `lean/` (the laptop is fine for Lean builds).
  - No `sorry`, no new axioms, no `native_decide`. Report `#print axioms` for the main theorem; it must use only
    propext, Classical.choice, Quot.sound.
  - Do NOT weaken the statement. If you must change a hypothesis, say so explicitly in the report.

## Definitions
- φ : ℤ → ℂ is positive definite (PD) if for every Finset W ⊂ ℤ and every c : ℤ → ℂ,
      0 <= Re Σ_{k∈W} Σ_{l∈W} c k * conj (c l) * φ (k − l)
  and also φ(−k) = conj φ(k) for all k. Use this finite-sum definition (no GNS construction needed).
- ψ(k) := Re φ(0) − Re φ(k).

## Statements to formalize (exact)
Let S : Finset ℤ be nonempty, φ PD, m₀ := Re φ 0, δ : ℝ with 0 < δ < 1/2, and m₀ < (4 − 5δ)/3.
Write ind k := if k ∈ S then (1 : ℂ) else 0.
- (Core) Let Bad := ((S ∪ (S + S)).filter fun k => δ < ‖φ k − ind k‖). Then (Bad.card : ℝ) >= ((S.card : ℝ) − 1)/3.
  (S + S is the Finset sumset, pointwise addition.)
- (Main) If E : ℝ satisfies Σ_{k∈F} ‖φ k − ind k‖² <= E for every Finset F ⊂ ℤ, then E >= δ²((S.card : ℝ) − 1)/3.
  (Apply Core with F = Bad: each element contributes more than δ².)
Both are the exact content of P73 (Z). Do not restrict S, δ or φ further.

## Proof (checked by the lead)
1. 3-point PSD. For k, l ∈ ℤ, the 3×3 Hermitian matrix [φ(i − j)] over the points {0, k, k + l} is PSD (the PD
   definition with W = {0, k, k + l} and suitable c). From it derive the subadditivity
       √ψ(k + l) <= √ψ(k) + √ψ(l)
   (ψ >= 0 follows from the 2-point case). Equivalently, use the seminorm ‖e_x − e_y‖² = 2ψ(x − y) on the span.
   A direct route: for real a, b, the vector c = (−a − b, a·(stuff)...) — choose any proof; the standard argument is
   that d(x, y) = √(2ψ(x − y)) is a pseudometric because it is the distance in the GNS space. A purely algebraic proof
   from 3×3 PSD is acceptable.
2. G := {k : ‖φ k − 1_S k‖ <= δ}. For k, l ∈ S ∩ G with k + l ∈ G and k + l ∉ S: ψ(k), ψ(l) <= m₀ − 1 + δ (since
   Re φ(k) >= 1 − δ), and ψ(k + l) >= m₀ − δ (since Re φ(k + l) <= δ). Subadditivity gives
   √(m₀ − δ) <= 2√(m₀ − 1 + δ), i.e. 3m₀ >= 4 − 5δ. Contradiction. So (S∩G) + (S∩G) ⊂ S ∪ Gᶜ.
   (Note m₀ − 1 + δ >= 0 because Re φ(k) <= m₀ for PD φ; prove it.)
3. Cauchy–Davenport in ℤ (mathlib: Mathlib/Combinatorics/Additive/CauchyDavenport.lean, the linearly ordered
   cancellative version): #(T + T) >= 2#T − 1 for nonempty finite T. With T = S ∩ G:
   2#(S∩G) − 1 <= #S + #(Gᶜ ∩ (T + T)), and #(S∩G) >= #S − #(S \ G). Conclude #(Gᶜ ∩ ((T + T) ∪ S)) >= (#S − 1)/3.
   If S ∩ G is empty then #(S \ G) = #S >= (#S − 1)/3 directly.
4. Chebyshev: each k ∉ G contributes > δ² to E, so δ² · #(any finite subset of Gᶜ) <= E.
