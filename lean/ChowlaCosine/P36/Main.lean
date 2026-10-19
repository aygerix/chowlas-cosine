import ChowlaCosine.P36.SineKernel

/-! # P36: truncation at gaps with the exact cosine error -/

open Real
open scoped BigOperators

namespace ChowlaCosine.P36
open P31

/-- P36 for every finite set of positive frequencies, every D≥1 and every real angle.
The kernel has the exact first coefficient cos(pi/(D+2)); no fallback constant is used. -/
theorem p36_truncation (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a)
    (D : ℕ) (hD : 1 ≤ D) (M : ℝ) (hM : ∀ x : ℝ, -M ≤ cosSum A x) :
    ∀ x : ℝ, -(M + (1 - cos (π / ((D : ℝ)+2))) *
      ∑ a ∈ A.filter (fun a => a ≤ D), (a : ℝ)^2) ≤
        cosSum (A.filter (fun a => a ≤ D)) x := by
  intro x
  have H := truncation_of_kernel A D M hM (sineKernel D)
    (continuous_sineKernel D) (sineKernel_nonneg D) (circleMean_sineKernel D)
    (kernelCoeff_sineKernel_eq_zero D) (circleMean_sineKernel_mul_shift D) x
  rwa [kernelCoeff_sineKernel_one] at H

/-- The gap corollary with the same exact kernel constant, including an empty core. -/
theorem p36_gap (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a)
    (Y D : ℕ) (hD : 1 ≤ D) (hYD : Y ≤ D)
    (hgap : ∀ a ∈ A, Y < a → D < a)
    (M : ℝ) (hM : ∀ x : ℝ, -M ≤ cosSum A x) :
    ∀ x : ℝ, -(M + (1 - cos (π / ((D : ℝ)+2))) *
      (Y : ℝ)^2 * (A.filter (fun a => a ≤ Y)).card) ≤
        cosSum (A.filter (fun a => a ≤ Y)) x := by
  have heq : A.filter (fun a => a ≤ D) = A.filter (fun a => a ≤ Y) := by
    ext a
    simp only [Finset.mem_filter]
    constructor
    · rintro ⟨ha, had⟩
      exact ⟨ha, by by_contra h; have := hgap a ha (by omega); omega⟩
    · rintro ⟨ha, hay⟩
      exact ⟨ha, hay.trans hYD⟩
  have hs : (∑ a ∈ A.filter (fun a => a ≤ Y), (a : ℝ)^2) ≤
      (Y : ℝ)^2 * (A.filter (fun a => a ≤ Y)).card := by
    calc
      _ ≤ ∑ _a ∈ A.filter (fun a => a ≤ Y), (Y : ℝ)^2 := by
        apply Finset.sum_le_sum
        intro a ha
        have haY : (a : ℝ) ≤ Y := by exact_mod_cast (Finset.mem_filter.mp ha).2
        exact (sq_le_sq₀ (Nat.cast_nonneg _) (Nat.cast_nonneg _)).mpr haY
      _ = _ := by simp [mul_comm]
  intro x
  have H := p36_truncation A hA D hD M hM x
  rw [heq] at H
  have hc : 0 ≤ 1 - cos (π / ((D : ℝ)+2)) := sub_nonneg.mpr (cos_le_one _)
  nlinarith [mul_le_mul_of_nonneg_left hs hc]

/-- The paper's explicit quadratic gap-ratio bound with constant pi²/2. -/
theorem p36_gap_pi (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a)
    (Y D : ℕ) (hD : 1 ≤ D) (hYD : Y ≤ D)
    (hgap : ∀ a ∈ A, Y < a → D < a)
    (M : ℝ) (hM : ∀ x : ℝ, -M ≤ cosSum A x) :
    ∀ x : ℝ, -(M + (π^2/2) * ((Y : ℝ)/((D : ℝ)+2))^2 *
      (A.filter (fun a => a ≤ Y)).card) ≤
        cosSum (A.filter (fun a => a ≤ Y)) x := by
  intro x
  have H := p36_gap A hA Y D hD hYD hgap M hM x
  have hc : 1 - cos (π / ((D : ℝ)+2)) ≤ (π / ((D : ℝ)+2))^2 / 2 := by
    linarith [one_sub_sq_div_two_le_cos (x := π / ((D : ℝ)+2))]
  have he : (π / ((D : ℝ)+2))^2 / 2 * (Y : ℝ)^2 =
      (π^2/2) * ((Y : ℝ)/((D : ℝ)+2))^2 := by ring
  have hh := mul_le_mul_of_nonneg_right hc (sq_nonneg (Y : ℝ))
  rw [he] at hh
  have hh' := mul_le_mul_of_nonneg_right hh
    (show (0 : ℝ) ≤ (A.filter (fun a => a ≤ Y)).card by positivity)
  linarith

end ChowlaCosine.P36
