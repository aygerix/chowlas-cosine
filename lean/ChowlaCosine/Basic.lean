import Mathlib

/-!
# Basic definitions for Chowla's cosine problem

Convention (fixed throughout the project): for a finite set `A` of natural numbers,

  `f_A(x) = ∑_{a ∈ A} cos (a * x)`,   `x : ℝ`.

Positivity of the frequencies is *not* built into the definition; it is stated as an
explicit hypothesis `∀ a ∈ A, 0 < a` wherever it is needed.

This file also contains the elementary orthogonality integrals over `[0, 2π]` used by
the mean-zero / Parseval identities and by the intersection lemma.
-/

open Real

namespace ChowlaCosine

/-- `cosSum A x = f_A(x) = ∑_{a ∈ A} cos (a * x)`. -/
noncomputable def cosSum (A : Finset ℕ) (x : ℝ) : ℝ := ∑ a ∈ A, Real.cos ((a : ℝ) * x)

theorem continuous_cosSum (A : Finset ℕ) : Continuous (cosSum A) := by
  unfold cosSum
  fun_prop

/-- `∫_0^{2π} cos (k x) dx = 0` for a nonzero integer `k`. -/
theorem integral_cos_int_mul {k : ℤ} (hk : k ≠ 0) :
    ∫ x in (0 : ℝ)..2 * π, Real.cos ((k : ℝ) * x) = 0 := by
  have hk' : (k : ℝ) ≠ 0 := by exact_mod_cast hk
  rw [intervalIntegral.integral_comp_mul_left (fun x => Real.cos x) hk', integral_cos]
  have h : Real.sin ((k : ℝ) * (2 * π)) = 0 := by
    have := Real.sin_int_mul_pi (2 * k)
    rw [← this]
    congr 1
    push_cast
    ring
  simp [h]

/-- `∫_0^{2π} sin (k x) dx = 0` for every integer `k`. -/
theorem integral_sin_int_mul (k : ℤ) :
    ∫ x in (0 : ℝ)..2 * π, Real.sin ((k : ℝ) * x) = 0 := by
  by_cases hk : k = 0
  · subst hk
    simp
  have hk' : (k : ℝ) ≠ 0 := by exact_mod_cast hk
  rw [intervalIntegral.integral_comp_mul_left (fun x => Real.sin x) hk', integral_sin]
  have h : Real.cos ((k : ℝ) * (2 * π)) = 1 := Real.cos_int_mul_two_pi k
  simp [h]

/-- `∫_0^{2π} cos (k y + φ) dy = 2π cos φ` if `k = 0`, and `0` for every other integer `k`. -/
theorem integral_cos_int_mul_add (k : ℤ) (φ : ℝ) :
    ∫ y in (0 : ℝ)..2 * π, Real.cos ((k : ℝ) * y + φ) =
      if k = 0 then 2 * π * Real.cos φ else 0 := by
  split_ifs with hk
  · subst hk
    simp
  · simp_rw [Real.cos_add]
    rw [intervalIntegral.integral_sub, intervalIntegral.integral_mul_const,
      intervalIntegral.integral_mul_const, integral_cos_int_mul hk, integral_sin_int_mul k]
    · ring
    · exact (by fun_prop : Continuous fun y => Real.cos ((k : ℝ) * y) * Real.cos φ).intervalIntegrable _ _
    · exact (by fun_prop : Continuous fun y => Real.sin ((k : ℝ) * y) * Real.sin φ).intervalIntegrable _ _

/-- Product-to-sum orthogonality over a full period, with integer frequencies and phases. -/
theorem integral_cos_mul_cos (m n : ℤ) (φ ψ : ℝ) :
    ∫ y in (0 : ℝ)..2 * π, Real.cos ((m : ℝ) * y + φ) * Real.cos ((n : ℝ) * y + ψ) =
      (if m - n = 0 then π * Real.cos (φ - ψ) else 0) +
        (if m + n = 0 then π * Real.cos (φ + ψ) else 0) := by
  have hpt : ∀ y : ℝ, Real.cos ((m : ℝ) * y + φ) * Real.cos ((n : ℝ) * y + ψ) =
      (1 / 2 : ℝ) * Real.cos (((m - n : ℤ) : ℝ) * y + (φ - ψ)) +
        (1 / 2 : ℝ) * Real.cos (((m + n : ℤ) : ℝ) * y + (φ + ψ)) := by
    intro y
    have e1 : ((m - n : ℤ) : ℝ) * y + (φ - ψ) = ((m : ℝ) * y + φ) - ((n : ℝ) * y + ψ) := by
      push_cast; ring
    have e2 : ((m + n : ℤ) : ℝ) * y + (φ + ψ) = ((m : ℝ) * y + φ) + ((n : ℝ) * y + ψ) := by
      push_cast; ring
    rw [e1, e2, Real.cos_sub ((m : ℝ) * y + φ) ((n : ℝ) * y + ψ),
      Real.cos_add ((m : ℝ) * y + φ) ((n : ℝ) * y + ψ)]
    ring
  simp_rw [hpt]
  rw [intervalIntegral.integral_add, intervalIntegral.integral_const_mul,
    intervalIntegral.integral_const_mul, integral_cos_int_mul_add, integral_cos_int_mul_add]
  · split_ifs <;> ring
  · exact (by fun_prop : Continuous fun y : ℝ =>
      (1 / 2 : ℝ) * Real.cos (((m - n : ℤ) : ℝ) * y + (φ - ψ))).intervalIntegrable _ _
  · exact (by fun_prop : Continuous fun y : ℝ =>
      (1 / 2 : ℝ) * Real.cos (((m + n : ℤ) : ℝ) * y + (φ + ψ))).intervalIntegrable _ _

end ChowlaCosine
