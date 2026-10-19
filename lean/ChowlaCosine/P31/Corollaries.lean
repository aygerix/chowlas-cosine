import ChowlaCosine.P31.AnalyticNikolskii
import ChowlaCosine.Star

/-! # Explicit elementary dense corollary of P31 -/

open Real MeasureTheory
open scoped BigOperators

namespace ChowlaCosine.P31

noncomputable def elementaryC (L : ℕ) : ℝ := (811 / 1000 : ℝ) * (L + 1) + 71 / 300

theorem p31_elementary (w : ℕ) (A : Finset ℕ) (M : ℝ)
    (hA : ∀ a ∈ A, 0 < a) (hM : ∀ x : ℝ, -M ≤ cosSum A x) :
    windowMass w * ((A.card : ℝ) / 2 + M ^ 2) ≤
      elementaryC (A.sup id + w) * (M ^ 2 + windowEnergy w A / 2) :=
  p31_main w A M _ hA hM (elementary_analyticNikolskii _)

theorem windowEnergy_nonneg (w : ℕ) (A : Finset ℕ) : 0 ≤ windowEnergy w A :=
  Finset.sum_nonneg (fun a ha => sq_nonneg _)

/-- The positive-frequency set occupies at most the positive half of W. -/
theorem two_windowEnergy_le (w : ℕ) (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a) :
    2 * windowEnergy w A ≤ windowMass w - 1 := by
  let B := A.filter (fun a => a ≤ w)
  have hs : windowEnergy w A = ∑ a ∈ B, kappa w a ^ 2 := by
    unfold windowEnergy
    symm
    apply Finset.sum_subset (Finset.filter_subset _ _)
    intro a ha hnot
    have haw : w < a := by simp only [B, Finset.mem_filter, ha, true_and] at hnot; omega
    rw [kappa_eq_zero haw, zero_pow (by decide : (2 : ℕ) ≠ 0)]
  have hsub : B ⊆ windowFreq w := by
    intro a ha
    have ha' := Finset.mem_filter.mp ha
    exact Finset.mem_Icc.mpr ⟨hA a ha'.1, ha'.2⟩
  have hle : (∑ a ∈ B, kappa w a ^ 2) ≤ ∑ a ∈ windowFreq w, kappa w a ^ 2 :=
    Finset.sum_le_sum_of_subset_of_nonneg hsub (fun a ha hnot => sq_nonneg _)
  rw [hs]
  unfold windowMass
  linarith

theorem card_le_max_frequency (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a) :
    A.card ≤ A.sup id := by
  have hsub : A ⊆ Finset.Icc 1 (A.sup id) := by
    intro a ha
    exact Finset.mem_Icc.mpr ⟨hA a ha, Finset.le_sup (f := id) ha⟩
  have h := Finset.card_le_card hsub
  simpa using h

/-- The uniform finite-size fallback, from the already checked singleton star bound. -/
theorem half_le_of_nonempty (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a) (hne : A.Nonempty)
    (M : ℝ) (hM : ∀ x : ℝ, -M ≤ cosSum A x) : (1 / 2 : ℝ) ≤ M := by
  obtain ⟨a, ha⟩ := hne
  have hI : ∀ i ∈ ({(a : ℤ)} : Finset ℤ), i.natAbs ∈ A := by
    intro i hi
    simp only [Finset.mem_singleton] at hi
    subst i
    simpa using ha
  have hind : ∀ i ∈ ({(a : ℤ)} : Finset ℤ), ∀ j ∈ ({(a : ℤ)} : Finset ℤ),
      i ≠ j → (i - j).natAbs ∉ A := by
    intro i hi j hj hij
    simp only [Finset.mem_singleton] at hi hj
    exact False.elim (hij (hi.trans hj.symm))
  have h := star_bound A hA M hM {(a : ℤ)} hI hind
  simpa using h

private theorem elementaryC_window_upper (X : ℕ) (hX : 2000 ≤ X) :
    elementaryC (X + X / 200) ≤ (102 / 125 : ℝ) * X := by
  have hw : (X / 200 : ℕ) * 200 ≤ X := Nat.div_mul_le_self _ _
  have hwr : ((X / 200 : ℕ) : ℝ) * 200 ≤ X := by exact_mod_cast hw
  have hXr : (2000 : ℝ) ≤ X := by exact_mod_cast hX
  unfold elementaryC
  push_cast
  nlinarith

private theorem windowMass_floor_lower (X : ℕ) :
    (X : ℝ) / 300 ≤ windowMass (X / 200) := by
  have hw : X ≤ 200 * (X / 200 + 1) := by omega
  have hwr : (X : ℝ) ≤ 200 * (((X / 200 : ℕ) : ℝ) + 1) := by exact_mod_cast hw
  rw [windowMass_eq]
  have hnonneg : (0 : ℝ) ≤ 1 / (3 * (((X / 200 : ℕ) : ℝ) + 1)) := by positivity
  nlinarith

/-- Explicit large-X dense corollary, with ε=1/200 and X₀=2000. -/
theorem dense_large_sq (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a)
    (M : ℝ) (hM : ∀ x : ℝ, -M ≤ cosSum A x)
    (hX : 2000 ≤ A.sup id)
    (hdensity : (41 / 100 : ℝ) * A.sup id ≤ A.card) :
    (A.card : ℝ) / 1000000 ≤ M ^ 2 := by
  let X := A.sup id
  let w := X / 200
  let W := windowMass w
  let C := elementaryC (X + w)
  have hXpos : (0 : ℝ) < X := by have : 2000 ≤ X := hX; exact_mod_cast (by omega : 0 < X)
  have hW : 0 < W := windowMass_pos w
  have hC : 0 ≤ C := by unfold C elementaryC; positivity
  have hCup : C ≤ (102 / 125 : ℝ) * X := elementaryC_window_upper X hX
  have hWlow : (X : ℝ) / 300 ≤ W := windowMass_floor_lower X
  have hcard : (A.card : ℝ) ≤ X := by exact_mod_cast card_le_max_frequency A hA
  have hn : (0 : ℝ) ≤ A.card := Nat.cast_nonneg _
  have hS : windowEnergy w A ≤ W / 2 := by have := two_windowEnergy_le w A hA; linarith
  have hmain := p31_elementary w A M hA hM
  change W * ((A.card : ℝ) / 2 + M ^ 2) ≤ C * (M ^ 2 + windowEnergy w A / 2) at hmain
  have hCS := mul_le_mul_of_nonneg_left hS hC
  have hWsq : 0 ≤ W * M ^ 2 := mul_nonneg hW.le (sq_nonneg M)
  have hineq : W * ((A.card : ℝ) - C / 2) ≤ 2 * C * M ^ 2 := by
    nlinarith [hmain, hCS, hWsq]
  have hgap : (A.card : ℝ) / 500 ≤ (A.card : ℝ) - C / 2 := by
    change (41 / 100 : ℝ) * X ≤ A.card at hdensity
    linarith
  have hgain := (mul_le_mul_of_nonneg_left hgap hW.le).trans hineq
  have hlo := mul_le_mul_of_nonneg_right hWlow (div_nonneg hn (by norm_num : (0 : ℝ) ≤ 500))
  have hhi := mul_le_mul_of_nonneg_right hCup (by positivity : 0 ≤ 2 * M ^ 2)
  have hscaled : (X : ℝ) * ((A.card : ℝ) / 150000) ≤
      (X : ℝ) * ((204 / 125 : ℝ) * M ^ 2) := by
    nlinarith [hgain, hlo, hhi]
  have hcancel := (mul_le_mul_iff_right₀ hXpos).mp hscaled
  nlinarith [hcancel]

/-- T4: every finite positive-frequency set of density at least 41/100
satisfies the explicit square-root bound, at all sizes. -/
theorem dense_elementary (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a)
    (M : ℝ) (hM : ∀ x : ℝ, -M ≤ cosSum A x)
    (hdensity : (41 / 100 : ℝ) * A.sup id ≤ A.card) :
    Real.sqrt A.card / 1000 ≤ M := by
  have hM0 := nonneg_of_cosSum_ge A hA M hM
  have hsq : (A.card : ℝ) ≤ (M * 1000) ^ 2 := by
    by_cases hX : 2000 ≤ A.sup id
    · have h := dense_large_sq A hA M hM hX hdensity
      nlinarith
    · by_cases hne : A.Nonempty
      · have hh := half_le_of_nonempty A hA hne M hM
        have hc := card_le_max_frequency A hA
        have hcard : (A.card : ℝ) ≤ 2000 := by exact_mod_cast (by omega : A.card ≤ 2000)
        nlinarith [sq_nonneg (M - 1 / 2)]
      · have he : A = ∅ := Finset.not_nonempty_iff_eq_empty.mp hne
        simp only [he, Finset.card_empty, Nat.cast_zero]
        positivity
  apply (div_le_iff₀ (by norm_num : (0 : ℝ) < 1000)).mpr
  apply Real.sqrt_le_iff.mpr
  exact ⟨by positivity, hsq⟩

end ChowlaCosine.P31
