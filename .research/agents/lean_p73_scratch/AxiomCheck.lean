import ChowlaCosine.FewSpike

#print axioms ChowlaCosine.FewSpike.PositiveDefinite.psi_nonneg
#print axioms ChowlaCosine.FewSpike.PositiveDefinite.psi_add_le
#print axioms ChowlaCosine.FewSpike.fewSpike_core
#print axioms ChowlaCosine.FewSpike.fewSpike

#check ChowlaCosine.FewSpike.fewSpike_core
#check ChowlaCosine.FewSpike.fewSpike

open Finset
open scoped Pointwise ComplexConjugate

/- These wrappers check the statements against the brief with all definitions expanded. -/
example (S : Finset ℤ) (hS : S.Nonempty) (φ : ℤ → ℂ)
    (hpd : (∀ (W : Finset ℤ) (c : ℤ → ℂ),
      0 ≤ (∑ k ∈ W, ∑ l ∈ W, c k * conj (c l) * φ (k - l)).re) ∧
      (∀ k, φ (-k) = conj (φ k)))
    (δ : ℝ) (hδ : 0 < δ ∧ δ < 1 / 2)
    (hpeak : (φ 0).re < (4 - 5 * δ) / 3) :
    let ind : ℤ → ℂ := fun k => if k ∈ S then 1 else 0
    let Bad := (S ∪ (S + S)).filter fun k => δ < ‖φ k - ind k‖
    ((S.card : ℝ) - 1) / 3 ≤ (Bad.card : ℝ) := by
  classical
  exact ChowlaCosine.FewSpike.fewSpike_core S hS φ ⟨hpd.1, hpd.2⟩ δ hδ hpeak

example (S : Finset ℤ) (hS : S.Nonempty) (φ : ℤ → ℂ)
    (hpd : (∀ (W : Finset ℤ) (c : ℤ → ℂ),
      0 ≤ (∑ k ∈ W, ∑ l ∈ W, c k * conj (c l) * φ (k - l)).re) ∧
      (∀ k, φ (-k) = conj (φ k)))
    (δ : ℝ) (hδ : 0 < δ ∧ δ < 1 / 2)
    (hpeak : (φ 0).re < (4 - 5 * δ) / 3) (E : ℝ)
    (hE : ∀ F : Finset ℤ,
      ∑ k ∈ F, ‖φ k - (if k ∈ S then (1 : ℂ) else 0)‖ ^ 2 ≤ E) :
    δ ^ 2 * ((S.card : ℝ) - 1) / 3 ≤ E := by
  exact ChowlaCosine.FewSpike.fewSpike S hS φ ⟨hpd.1, hpd.2⟩ δ hδ hpeak E hE
