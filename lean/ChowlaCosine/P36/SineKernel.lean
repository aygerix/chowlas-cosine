import ChowlaCosine.P36.Kernel

/-! # The exact sine-vector probability kernel of degree D -/

open Real
open scoped BigOperators

namespace ChowlaCosine.P36
open P31
set_option maxHeartbeats 800000

noncomputable def sineAngle (D : ℕ) : ℝ := π / ((D : ℝ) + 2)
noncomputable def sineWeight (D k : ℕ) : ℝ := sin (((k : ℝ) + 1) * sineAngle D)
noncomputable def sineMass (D : ℕ) : ℝ := ∑ k ∈ Finset.range (D+1), sineWeight D k ^ 2
noncomputable def sineKernel (D : ℕ) (x : ℝ) : ℝ :=
  (sineMass D)⁻¹ * squareKernel (D+1) (sineWeight D) x

theorem sineAngle_pos (D : ℕ) : 0 < sineAngle D := by unfold sineAngle; positivity

theorem sineAngle_lt_pi (D : ℕ) : sineAngle D < π := by
  unfold sineAngle
  apply (div_lt_iff₀ (by positivity : (0 : ℝ) < D+2)).mpr
  nlinarith [Nat.cast_nonneg (α := ℝ) D, pi_pos]

theorem sineWeight_last (D : ℕ) : sineWeight D (D+1) = 0 := by
  unfold sineWeight sineAngle
  have h : (D : ℝ) + 2 ≠ 0 := by positivity
  have he : (((D+1 : ℕ) : ℝ)+1) * (π / ((D : ℝ)+2)) = π := by
    push_cast
    field_simp
    <;> ring
  rw [he, sin_pi]

theorem sineMass_pos (D : ℕ) : 0 < sineMass D := by
  have hsin : 0 < sineWeight D 0 := by
    simpa [sineWeight] using sin_pos_of_pos_of_lt_pi (sineAngle_pos D) (sineAngle_lt_pi D)
  have H := Finset.single_le_sum (fun k hk => sq_nonneg (sineWeight D k))
    (show 0 ∈ Finset.range (D+1) by simp)
  change _ ≤ sineMass D at H
  exact lt_of_lt_of_le (sq_pos_of_pos hsin) H

/-- The finite Dirichlet sine vector is an exact path-graph eigenvector. -/
theorem sineWeight_recurrence (D k : ℕ) :
    sineWeight D (k+1) + sin ((k : ℝ) * sineAngle D) =
      2 * cos (sineAngle D) * sineWeight D k := by
  unfold sineWeight
  have hp := sin_add (((k : ℝ)+1) * sineAngle D) (sineAngle D)
  have hm := sin_sub (((k : ℝ)+1) * sineAngle D) (sineAngle D)
  have he₁ : (((k : ℝ)+1) * sineAngle D + sineAngle D) =
      (((k+1 : ℕ) : ℝ)+1) * sineAngle D := by push_cast; ring
  have he₂ : (((k : ℝ)+1) * sineAngle D - sineAngle D) =
      (k : ℝ) * sineAngle D := by ring
  rw [he₁] at hp
  rw [he₂] at hm
  linarith

/-- Exact first autocorrelation, including both zero boundary values. -/
theorem sine_adjacent_sum (D : ℕ) :
    (∑ k ∈ Finset.range D, sineWeight D k * sineWeight D (k+1)) =
      cos (sineAngle D) * sineMass D := by
  have hp : (∑ k ∈ Finset.range (D+1), sineWeight D k * sineWeight D (k+1)) =
      ∑ k ∈ Finset.range D, sineWeight D k * sineWeight D (k+1) := by
    rw [Finset.sum_range_succ, sineWeight_last]
    ring
  have hm : (∑ k ∈ Finset.range (D+1), sineWeight D k * sin ((k : ℝ) * sineAngle D)) =
      ∑ k ∈ Finset.range D, sineWeight D k * sineWeight D (k+1) := by
    rw [Finset.sum_range_succ']
    simp only [Nat.cast_zero, zero_mul, sin_zero, mul_zero, add_zero]
    apply Finset.sum_congr rfl
    intro k hk
    simp only [sineWeight, Nat.cast_add, Nat.cast_one]
    ring
  have H : (∑ k ∈ Finset.range (D+1),
      (sineWeight D k * sineWeight D (k+1) +
        sineWeight D k * sin ((k : ℝ) * sineAngle D))) =
      2 * cos (sineAngle D) * sineMass D := by
    unfold sineMass
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro k hk
    have HH := congrArg (fun z : ℝ => sineWeight D k * z) (sineWeight_recurrence D k)
    nlinarith [HH]
  rw [Finset.sum_add_distrib, hp, hm] at H
  linarith

@[fun_prop] theorem continuous_sineKernel (D : ℕ) : Continuous (sineKernel D) := by
  unfold sineKernel
  fun_prop

theorem sineKernel_nonneg (D : ℕ) (x : ℝ) : 0 ≤ sineKernel D x := by
  exact mul_nonneg (inv_nonneg.mpr (sineMass_pos D).le) (squareKernel_nonneg _ _ _)

theorem circleMean_sineKernel (D : ℕ) : circleMean (sineKernel D) = 1 := by
  unfold sineKernel
  rw [circleMean_const_mul, circleMean_squareKernel]
  exact inv_mul_cancel₀ (sineMass_pos D).ne'

theorem kernelCoeff_sineKernel (D a : ℕ) :
    kernelCoeff (sineKernel D) a = (sineMass D)⁻¹ * squareCoeff (D+1) (sineWeight D) a := by
  unfold kernelCoeff sineKernel squareCoeff
  simp only [mul_assoc, circleMean_const_mul]

theorem kernelCoeff_sineKernel_one (D : ℕ) :
    kernelCoeff (sineKernel D) 1 = cos (π / ((D : ℝ)+2)) := by
  rw [kernelCoeff_sineKernel, squareCoeff_one, sine_adjacent_sum]
  change (sineMass D)⁻¹ * (cos (sineAngle D) * sineMass D) = cos (sineAngle D)
  rw [mul_left_comm, inv_mul_cancel₀ (sineMass_pos D).ne', mul_one]

theorem kernelCoeff_sineKernel_eq_zero (D a : ℕ) (ha : D < a) :
    kernelCoeff (sineKernel D) a = 0 := by
  rw [kernelCoeff_sineKernel, squareCoeff_eq_zero (D+1) (sineWeight D) (by omega) (by omega), mul_zero]

theorem circleMean_sineKernel_mul_shift (D a : ℕ) (x : ℝ) :
    circleMean (fun y => sineKernel D y * cos ((a : ℝ) * (x-y))) =
      kernelCoeff (sineKernel D) a * cos ((a : ℝ) * x) := by
  rw [kernelCoeff_sineKernel]
  unfold sineKernel
  simp only [mul_assoc, circleMean_const_mul]
  rw [circleMean_squareKernel_mul_shift]

end ChowlaCosine.P36
