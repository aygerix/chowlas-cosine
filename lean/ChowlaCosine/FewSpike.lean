import Mathlib.Analysis.Complex.Norm
import Mathlib.Combinatorics.Additive.CauchyDavenport
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# The robust few-spike lemma on the integers (P73)

Positive definiteness is expressed by finite quadratic sums, together with Hermitian
symmetry. The three-point test with coefficients `(1, -2, 1)` supplies the squared
triangle estimate needed for the sharp threshold in this lemma.
-/

namespace ChowlaCosine.FewSpike

open Finset
open scoped Pointwise ComplexConjugate

/-- Finite-sum positive definiteness, including Hermitian symmetry. -/
structure PositiveDefinite (φ : ℤ → ℂ) : Prop where
  nonneg : ∀ (W : Finset ℤ) (c : ℤ → ℂ),
    0 ≤ (∑ k ∈ W, ∑ l ∈ W, c k * conj (c l) * φ (k - l)).re
  hermitian : ∀ k, φ (-k) = conj (φ k)

/-- The real defect from the peak. -/
def psi (φ : ℤ → ℂ) (k : ℤ) : ℝ := (φ 0).re - (φ k).re

@[simp] lemma psi_zero (φ : ℤ → ℂ) : psi φ 0 = 0 := by simp [psi]

lemma PositiveDefinite.re_neg {φ : ℤ → ℂ} (hφ : PositiveDefinite φ) (k : ℤ) :
    (φ (-k)).re = (φ k).re := by rw [hφ.hermitian, Complex.conj_re]

/-- The two-point PSD test bounds the real part by its value at zero. -/
lemma PositiveDefinite.psi_nonneg {φ : ℤ → ℂ} (hφ : PositiveDefinite φ) (k : ℤ) :
    0 ≤ psi φ k := by
  classical
  by_cases hk : k = 0
  · simp [hk]
  have h := hφ.nonneg {0, k} (fun x => if x = 0 then 1 else -1)
  simp [hk, Ne.symm hk, Complex.add_re, hφ.re_neg] at h
  dsimp [psi]
  linarith

/-- A three-point PSD test. Repeated points are covered by the two-point estimate. -/
lemma PositiveDefinite.psi_add_le {φ : ℤ → ℂ} (hφ : PositiveDefinite φ) (k l : ℤ) :
    psi φ (k + l) ≤ 2 * psi φ k + 2 * psi φ l := by
  classical
  have hkψ := hφ.psi_nonneg k
  have hlψ := hφ.psi_nonneg l
  by_cases hk : k = 0
  · simp [hk]
    linarith
  by_cases hl : l = 0
  · simp [hl]
    linarith
  by_cases hkl : k + l = 0
  · rw [hkl, psi_zero]
    positivity
  have hne : k ≠ k + l := by omega
  have h := hφ.nonneg {0, k, k + l} (fun x => if x = k then -2 else 1)
  have hd : k - (k + l) = -l := by omega
  have hd' : k + l - k = l := by omega
  simp [Ne.symm hk, Ne.symm hkl, hne, Ne.symm hne, hd, hd',
    Complex.add_re, Complex.mul_re, hφ.re_neg] at h
  have hn : -l + -k = -(k + l) := by omega
  rw [hn, hφ.re_neg] at h
  dsimp [psi]
  linarith

/-- The complex indicator of the finite set. -/
def ind (S : Finset ℤ) (k : ℤ) : ℂ := if k ∈ S then 1 else 0

/-- The exact finite bad set used in P73. -/
noncomputable def badSet (S : Finset ℤ) (φ : ℤ → ℂ) (δ : ℝ) : Finset ℤ := by
  classical
  exact (S ∪ (S + S)).filter fun k => δ < ‖φ k - ind S k‖

/-- Three good points cannot have two points in `S` and their sum outside `S`. -/
lemma PositiveDefinite.add_mem_of_good {φ : ℤ → ℂ} (hφ : PositiveDefinite φ)
    (S : Finset ℤ) (δ : ℝ) (hpeak : (φ 0).re < (4 - 5 * δ) / 3)
    {k l : ℤ} (hkS : k ∈ S) (hlS : l ∈ S)
    (hk : ‖φ k - ind S k‖ ≤ δ) (hl : ‖φ l - ind S l‖ ≤ δ)
    (hkl : ‖φ (k + l) - ind S (k + l)‖ ≤ δ) : k + l ∈ S := by
  by_contra hout
  simp only [ind, if_pos hkS] at hk
  simp only [ind, if_pos hlS] at hl
  simp only [ind, if_neg hout, sub_zero] at hkl
  have hkRe := (abs_le.mp ((Complex.abs_re_le_norm (φ k - 1)).trans hk)).1
  have hlRe := (abs_le.mp ((Complex.abs_re_le_norm (φ l - 1)).trans hl)).1
  have hklRe := (Complex.re_le_norm (φ (k + l))).trans hkl
  simp only [Complex.sub_re, Complex.one_re] at hkRe hlRe
  have hmetric := hφ.psi_add_le k l
  dsimp [psi] at hmetric
  linarith

/-- The finite combinatorial step, using Cauchy--Davenport in `ℤ`. -/
lemma card_le_three_mul_card_of_add_subset (S T B : Finset ℤ)
    (hcover : S ⊆ T ∪ B) (hadd : T + T ⊆ S ∪ B) :
    S.card ≤ 3 * B.card + 1 := by
  have hc : S.card ≤ T.card + B.card :=
    (card_le_card hcover).trans (card_union_le T B)
  by_cases hT : T.Nonempty
  · have hcd := cauchy_davenport_add_of_linearOrder_isCancelAdd hT hT
    have ha : (T + T).card ≤ S.card + B.card :=
      (card_le_card hadd).trans (card_union_le S B)
    have htpos := hT.card_pos
    omega
  · have htzero : T.card = 0 := card_eq_zero.mpr (not_nonempty_iff_eq_empty.mp hT)
    omega

/-- **P73, core:** at least `(card S - 1) / 3` points in the specified union are bad. -/
theorem fewSpike_core (S : Finset ℤ) (_hS : S.Nonempty) (φ : ℤ → ℂ)
    (hφ : PositiveDefinite φ) (δ : ℝ) (_hδ : 0 < δ ∧ δ < 1 / 2)
    (hpeak : (φ 0).re < (4 - 5 * δ) / 3) :
    ((S.card : ℝ) - 1) / 3 ≤ (badSet S φ δ).card := by
  classical
  let T := S.filter fun k => ‖φ k - ind S k‖ ≤ δ
  have hcover : S ⊆ T ∪ badSet S φ δ := by
    intro k hk
    by_cases hgood : ‖φ k - ind S k‖ ≤ δ
    · exact mem_union_left _ (mem_filter.mpr ⟨hk, hgood⟩)
    · exact mem_union_right _ (mem_filter.mpr
        ⟨mem_union_left _ hk, lt_of_not_ge hgood⟩)
  have hadd : T + T ⊆ S ∪ badSet S φ δ := by
    intro x hx
    obtain ⟨k, hk, l, hl, rfl⟩ := mem_add.mp hx
    obtain ⟨hkS, hkgood⟩ := mem_filter.mp hk
    obtain ⟨hlS, hlgood⟩ := mem_filter.mp hl
    by_cases hgood : ‖φ (k + l) - ind S (k + l)‖ ≤ δ
    · exact mem_union_left _ (hφ.add_mem_of_good S δ hpeak hkS hlS hkgood hlgood hgood)
    · exact mem_union_right _ (mem_filter.mpr
        ⟨mem_union_right _ (add_mem_add hkS hlS), lt_of_not_ge hgood⟩)
  have hnat := card_le_three_mul_card_of_add_subset S T (badSet S φ δ) hcover hadd
  have hreal : (S.card : ℝ) ≤ 3 * ((badSet S φ δ).card : ℝ) + 1 := by
    exact_mod_cast hnat
  linarith

/-- **P73, main:** every finite-sum bound on the squared error obeys the robust L² bound. -/
theorem fewSpike (S : Finset ℤ) (hS : S.Nonempty) (φ : ℤ → ℂ)
    (hφ : PositiveDefinite φ) (δ : ℝ) (hδ : 0 < δ ∧ δ < 1 / 2)
    (hpeak : (φ 0).re < (4 - 5 * δ) / 3) (E : ℝ)
    (hE : ∀ F : Finset ℤ, ∑ k ∈ F, ‖φ k - ind S k‖ ^ 2 ≤ E) :
    δ ^ 2 * ((S.card : ℝ) - 1) / 3 ≤ E := by
  classical
  have hcore := fewSpike_core S hS φ hφ δ hδ hpeak
  have hterm : ∀ k ∈ badSet S φ δ, δ ^ 2 ≤ ‖φ k - ind S k‖ ^ 2 := by
    intro k hk
    have hbad := (mem_filter.mp hk).2
    nlinarith [norm_nonneg (φ k - ind S k)]
  have hsum : δ ^ 2 * ((badSet S φ δ).card : ℝ) ≤ E := by
    calc
      _ = ∑ _k ∈ badSet S φ δ, δ ^ 2 := by simp [mul_comm]
      _ ≤ ∑ k ∈ badSet S φ δ, ‖φ k - ind S k‖ ^ 2 := sum_le_sum hterm
      _ ≤ E := hE (badSet S φ δ)
  have hmul := mul_le_mul_of_nonneg_left hcore (sq_nonneg δ)
  nlinarith

end ChowlaCosine.FewSpike
