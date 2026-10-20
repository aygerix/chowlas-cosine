-- SOURCE ChowlaCosine/P36/Kernel.lean
import ChowlaCosine.P31.Averaging
import ChowlaCosine.P31.Fejer

/-! # Positive finite cosine kernels and quadratic Fourier increments -/

open Real
open scoped BigOperators

namespace ChowlaCosine.P36
open P31
set_option maxHeartbeats 800000

/-- The square modulus of a finite analytic polynomial with real coefficients. -/
noncomputable def squareKernel (N : ℕ) (v : ℕ → ℝ) (x : ℝ) : ℝ :=
  (∑ i ∈ Finset.range N, v i * cos ((i : ℝ) * x)) ^ 2 +
    (∑ i ∈ Finset.range N, v i * sin ((i : ℝ) * x)) ^ 2

@[fun_prop] theorem continuous_squareKernel (N : ℕ) (v : ℕ → ℝ) :
    Continuous (squareKernel N v) := by unfold squareKernel; fun_prop

theorem squareKernel_nonneg (N : ℕ) (v : ℕ → ℝ) (x : ℝ) :
    0 ≤ squareKernel N v x := add_nonneg (sq_nonneg _) (sq_nonneg _)

theorem squareKernel_expansion (N : ℕ) (v : ℕ → ℝ) (x : ℝ) :
    squareKernel N v x = ∑ i ∈ Finset.range N, ∑ j ∈ Finset.range N,
      (v i * v j) * cos ((((i : ℤ) - j : ℤ) : ℝ) * x) := by
  unfold squareKernel
  simp only [sq, Finset.sum_mul_sum, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro i hi
  apply Finset.sum_congr rfl
  intro j hj
  push_cast
  rw [sub_mul, cos_sub]
  ring

private theorem mean_cos_int (k : ℤ) :
    circleMean (fun x => cos ((k : ℝ) * x)) = if k = 0 then 1 else 0 := by
  by_cases hk : k = 0
  · simp [hk]
  · simp [circleMean, integral_cos_int_mul hk, hk]

/-- Exact mass, without a trigonometric summation formula. -/
theorem circleMean_squareKernel (N : ℕ) (v : ℕ → ℝ) :
    circleMean (squareKernel N v) = ∑ i ∈ Finset.range N, v i ^ 2 := by
  simp_rw [funext (squareKernel_expansion N v)]
  rw [circleMean_sum _ _ (by intro i hi; fun_prop)]
  apply Finset.sum_congr rfl
  intro i hi
  rw [circleMean_sum _ _ (by intro j hj; fun_prop)]
  simp_rw [circleMean_const_mul, mean_cos_int]
  have heq : ∀ j : ℕ, ((i : ℤ) - j = 0) ↔ i = j := by intro j; omega
  simp_rw [heq]
  simp [hi, sq]

private theorem mean_cos_int_mul_shift (k : ℤ) (a : ℕ) (x : ℝ) :
    circleMean (fun y => cos ((k : ℝ) * y) * cos ((a : ℝ) * (x - y))) =
      ((if k = a then 1 else 0) + (if k = -(a : ℤ) then 1 else 0)) / 2 *
        cos ((a : ℝ) * x) := by
  have heq : (fun y => cos ((k : ℝ) * y) * cos ((a : ℝ) * (x - y))) =
      (fun y => cos ((k : ℝ) * y + 0) * cos (((-(a : ℤ)) : ℝ) * y + (a : ℝ) * x)) := by
    funext y
    congr 2 <;> push_cast <;> ring
  unfold circleMean
  rw [heq]
  have hi := integral_cos_mul_cos k (-(a : ℤ)) 0 ((a : ℝ) * x)
  simp only [Int.cast_neg, Int.cast_natCast] at hi
  rw [hi]
  have h₁ : k - -(a : ℤ) = 0 ↔ k = -(a : ℤ) := by omega
  have h₂ : k + -(a : ℤ) = 0 ↔ k = a := by omega
  simp only [h₁, h₂, zero_sub, zero_add, cos_neg]
  split_ifs <;> field_simp <;> ring

/-- The real Fourier coefficient, with no positivity assumed on coefficients. -/
noncomputable def squareCoeff (N : ℕ) (v : ℕ → ℝ) (a : ℕ) : ℝ :=
  circleMean (fun y => squareKernel N v y * cos ((a : ℝ) * y))

/-- Exact convolution against a translated cosine. -/
theorem circleMean_squareKernel_mul_shift (N : ℕ) (v : ℕ → ℝ) (a : ℕ) (x : ℝ) :
    circleMean (fun y => squareKernel N v y * cos ((a : ℝ) * (x - y))) =
      squareCoeff N v a * cos ((a : ℝ) * x) := by
  have hex : ∀ z : ℝ, circleMean (fun y => squareKernel N v y * cos ((a : ℝ) * (z - y))) =
      (∑ i ∈ Finset.range N, ∑ j ∈ Finset.range N, (v i * v j) *
        (((if (i : ℤ) - j = a then 1 else 0) +
          (if (i : ℤ) - j = -(a : ℤ) then 1 else 0)) / 2)) * cos ((a : ℝ) * z) := by
    intro z
    simp_rw [squareKernel_expansion, Finset.sum_mul]
    rw [circleMean_sum _ _ (by intro i hi; fun_prop)]
    rw [← Finset.sum_mul]
    congr 1
    apply Finset.sum_congr rfl
    intro i hi
    rw [circleMean_sum _ _ (by intro j hj; fun_prop)]
    simp_rw [mul_assoc, circleMean_const_mul, mean_cos_int_mul_shift, ← mul_assoc]
    rw [Finset.sum_mul]
  have hzero := hex 0
  simp only [sub_zero, cos_neg, mul_zero, cos_zero, mul_one] at hzero
  rw [hex, ← hzero]
  congr 1
  simp only [squareCoeff, zero_sub, mul_neg, cos_neg]

/-- Exact finite autocorrelation formula for a real coefficient vector. -/
theorem squareCoeff_pair_formula (N : ℕ) (v : ℕ → ℝ) (a : ℕ) :
    squareCoeff N v a = ∑ i ∈ Finset.range N, ∑ j ∈ Finset.range N,
      if (i : ℤ) - j = a then v i * v j else 0 := by
  have hex : squareCoeff N v a =
      (∑ i ∈ Finset.range N, ∑ j ∈ Finset.range N, (v i * v j) *
        (((if (i : ℤ) - j = a then 1 else 0) +
          (if (i : ℤ) - j = -(a : ℤ) then 1 else 0)) / 2)) := by
    have H : ∀ k : ℤ, circleMean (fun y => cos ((k : ℝ) * y) * cos ((a : ℝ) * y)) =
        ((if k = a then 1 else 0) + (if k = -(a : ℤ) then 1 else 0)) / 2 := by
      intro k
      simpa only [zero_sub, mul_neg, cos_neg, mul_zero, cos_zero, mul_one] using
        mean_cos_int_mul_shift k a 0
    unfold squareCoeff
    simp_rw [squareKernel_expansion, Finset.sum_mul]
    rw [circleMean_sum _ _ (by intro i hi; fun_prop)]
    apply Finset.sum_congr rfl
    intro i hi
    rw [circleMean_sum _ _ (by intro j hj; fun_prop)]
    apply Finset.sum_congr rfl
    intro j hj
    simp only [mul_assoc]
    rw [circleMean_const_mul, circleMean_const_mul, H]
    ring
  have hflip : (∑ i ∈ Finset.range N, ∑ j ∈ Finset.range N,
      if (i : ℤ) - j = -(a : ℤ) then v i * v j else 0) =
      ∑ i ∈ Finset.range N, ∑ j ∈ Finset.range N,
        if (i : ℤ) - j = a then v i * v j else 0 := by
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro i hi
    apply Finset.sum_congr rfl
    intro j hj
    have heq : (j : ℤ) - i = -(a : ℤ) ↔ (i : ℤ) - j = a := by omega
    rw [heq]
    split_ifs <;> ring
  rw [hex]
  have hp : ∀ i j : ℕ, v i * v j *
      (((if (i : ℤ) - j = a then 1 else 0) +
        (if (i : ℤ) - j = -(a : ℤ) then 1 else 0)) / 2) =
      ((if (i : ℤ) - j = a then v i * v j else 0) +
        (if (i : ℤ) - j = -(a : ℤ) then v i * v j else 0)) / 2 := by
    intro i j
    split_ifs <;> ring
  simp_rw [hp, ← Finset.sum_div, Finset.sum_add_distrib]
  rw [hflip]
  ring

/-- The first coefficient is the adjacent-coefficient inner product. -/
theorem squareCoeff_one (D : ℕ) (v : ℕ → ℝ) :
    squareCoeff (D+1) v 1 = ∑ j ∈ Finset.range D, v j * v (j+1) := by
  rw [squareCoeff_pair_formula, Finset.sum_comm]
  have hrow : ∀ j ∈ Finset.range (D+1),
      (∑ i ∈ Finset.range (D+1), if (i : ℤ) - j = (1 : ℤ) then v i * v j else 0) =
      if j < D then v j * v (j+1) else 0 := by
    intro j hj
    have heq : ∀ i : ℕ, (i : ℤ) - j = 1 ↔ i = j+1 := by intro i; omega
    simp_rw [heq]
    simp only [Finset.sum_ite_eq', Finset.mem_range]
    by_cases h : j < D
    · rw [if_pos (by omega), if_pos h, mul_comm]
    · rw [if_neg (by omega), if_neg h]
  rw [Finset.sum_congr rfl hrow, Finset.sum_range_succ]
  simp only [lt_self_iff_false, ↓reduceIte, add_zero]
  apply Finset.sum_congr rfl
  intro j hj
  rw [if_pos (Finset.mem_range.mp hj)]

/-- All frequencies at or above the coefficient-vector length vanish exactly. -/
theorem squareCoeff_eq_zero (N : ℕ) (v : ℕ → ℝ) {a : ℕ}
    (ha : N ≤ a) (hapos : 0 < a) : squareCoeff N v a = 0 := by
  have H := circleMean_squareKernel_mul_shift N v a 0
  have hzero : circleMean (fun y => squareKernel N v y * cos ((a : ℝ) * (0 - y))) = 0 := by
    simp_rw [squareKernel_expansion, Finset.sum_mul]
    rw [circleMean_sum _ _ (by intro i hi; fun_prop)]
    apply Finset.sum_eq_zero
    intro i hi
    rw [circleMean_sum _ _ (by intro j hj; fun_prop)]
    apply Finset.sum_eq_zero
    intro j hj
    simp only [mul_assoc]
    rw [circleMean_const_mul, circleMean_const_mul, mean_cos_int_mul_shift]
    have hi' := Finset.mem_range.mp hi
    have hj' := Finset.mem_range.mp hj
    rw [if_neg (by omega : (i : ℤ) - j ≠ (a : ℤ)),
      if_neg (by omega : (i : ℤ) - j ≠ -(a : ℤ))]
    ring
  simpa only [hzero, mul_zero, cos_zero, mul_one] using H.symm

/-- Elementary all-real multiple-angle estimate. -/
theorem abs_sin_nat_mul_le (a : ℕ) (x : ℝ) : |sin ((a : ℝ) * x)| ≤ a * |sin x| := by
  induction a with
  | zero => simp
  | succ a ih =>
    rw [Nat.cast_add, Nat.cast_one, add_mul, one_mul, sin_add]
    calc
      _ ≤ |sin ((a : ℝ) * x) * cos x| + |cos ((a : ℝ) * x) * sin x| := abs_add_le _ _
      _ ≤ |sin ((a : ℝ) * x)| + |sin x| := by
        simp only [abs_mul]
        nlinarith [abs_cos_le_one x, abs_cos_le_one ((a : ℝ) * x),
          abs_nonneg (sin ((a : ℝ) * x)), abs_nonneg (sin x)]
      _ ≤ _ := by push_cast; nlinarith

/-- Positive-definite increment inequality before integration. -/
theorem one_sub_cos_nat_mul_le (a : ℕ) (x : ℝ) :
    1 - cos ((a : ℝ) * x) ≤ (a : ℝ) ^ 2 * (1 - cos x) := by
  have h := abs_sin_nat_mul_le a (x / 2)
  have hs := (sq_le_sq₀ (abs_nonneg (sin ((a : ℝ) * (x / 2))))
    (mul_nonneg (Nat.cast_nonneg a) (abs_nonneg (sin (x / 2))))).mpr h
  have h₁ := cos_two_mul (((a : ℝ) * x) / 2)
  have h₂ := cos_two_mul (x / 2)
  have ht₁ := sin_sq_add_cos_sq (((a : ℝ) * x) / 2)
  have ht₂ := sin_sq_add_cos_sq (x / 2)
  rw [show 2 * (((a : ℝ) * x) / 2) = (a : ℝ) * x by ring] at h₁
  rw [show 2 * (x / 2) = x by ring] at h₂
  simp only [mul_pow, sq_abs] at hs
  have heq : (a : ℝ) * (x / 2) = ((a : ℝ) * x) / 2 := by ring
  rw [heq] at hs
  nlinarith [mul_nonneg (sq_nonneg (a : ℝ)) (show 0 ≤ 1 - cos x by linarith [cos_le_one x])]


/-- Fourier cosine coefficient for a continuous real kernel. -/
noncomputable def kernelCoeff (J : ℝ → ℝ) (a : ℕ) : ℝ :=
  circleMean (fun y => J y * cos ((a : ℝ) * y))

private theorem mean_increment (J : ℝ → ℝ) (hJ : Continuous J) (a : ℕ) :
    circleMean (fun y => J y * (1 - cos ((a : ℝ) * y))) =
      circleMean J - kernelCoeff J a := by
  have heq : (fun y => J y * (1 - cos ((a : ℝ) * y))) =
      (fun y => J y + (-1) * (J y * cos ((a : ℝ) * y))) := by funext y; ring
  rw [heq, circleMean_add hJ (by fun_prop), circleMean_const_mul]
  rfl

/-- Positive kernels have nonnegative Fourier increments. -/
theorem kernelCoeff_le_mass (J : ℝ → ℝ) (hJ : Continuous J)
    (hn : ∀ x, 0 ≤ J x) (a : ℕ) : kernelCoeff J a ≤ circleMean J := by
  have H := circleMean_mono (f := fun _ => 0)
    (g := fun y => J y * (1 - cos ((a : ℝ) * y))) (by fun_prop) (by fun_prop)
    (fun y => mul_nonneg (hn y) (sub_nonneg.mpr (cos_le_one _)))
  rw [circleMean_const, mean_increment J hJ a] at H
  linarith

/-- The positive-definite quadratic increment bound, for every natural frequency. -/
theorem kernelCoeff_increment_le (J : ℝ → ℝ) (hJ : Continuous J)
    (hn : ∀ x, 0 ≤ J x) (a : ℕ) :
    circleMean J - kernelCoeff J a ≤
      (a : ℝ) ^ 2 * (circleMean J - kernelCoeff J 1) := by
  have H := circleMean_mono
    (f := fun y => J y * (1 - cos ((a : ℝ) * y)))
    (g := fun y => (a : ℝ) ^ 2 * (J y * (1 - cos ((1 : ℝ) * y))))
    (by fun_prop) (by fun_prop) (fun y => by
      simpa only [one_mul, mul_left_comm] using
        mul_le_mul_of_nonneg_left (one_sub_cos_nat_mul_le a y) (hn y))
  rw [mean_increment J hJ a, circleMean_const_mul, mean_increment J hJ 1] at H
  exact H

/-- Full-circle truncation for any explicit probability kernel of degree D.
The translated-cosine identity is exact, with no sampled angles. -/
theorem truncation_of_kernel (A : Finset ℕ) (D : ℕ) (M : ℝ)
    (hM : ∀ x : ℝ, -M ≤ cosSum A x)
    (J : ℝ → ℝ) (hJ : Continuous J) (hn : ∀ x, 0 ≤ J x)
    (hm : circleMean J = 1)
    (hkill : ∀ a, D < a → kernelCoeff J a = 0)
    (hshift : ∀ a x, circleMean (fun y => J y * cos ((a : ℝ) * (x - y))) =
      kernelCoeff J a * cos ((a : ℝ) * x)) (x : ℝ) :
    -(M + (1 - kernelCoeff J 1) *
      ∑ a ∈ A.filter (fun a => a ≤ D), (a : ℝ) ^ 2) ≤
      cosSum (A.filter (fun a => a ≤ D)) x := by
  have hconv := circleMean_mono
    (f := fun y => -M * J y) (g := fun y => J y * cosSum A (x - y))
    (by fun_prop) (by unfold cosSum; fun_prop)
    (fun y => by nlinarith [mul_le_mul_of_nonneg_left (hM (x-y)) (hn y)])
  rw [circleMean_const_mul, hm, mul_one] at hconv
  have hidentity : circleMean (fun y => J y * cosSum A (x-y)) =
      ∑ a ∈ A.filter (fun a => a ≤ D), kernelCoeff J a * cos ((a : ℝ) * x) := by
    unfold cosSum
    simp only [Finset.mul_sum]
    rw [circleMean_sum _ _ (by intro a ha; fun_prop)]
    simp_rw [hshift]
    rw [Finset.sum_filter]
    apply Finset.sum_congr rfl
    intro a ha
    split_ifs with h
    · rfl
    · rw [hkill a (by omega), zero_mul]
  rw [hidentity] at hconv
  have hbound : (∑ a ∈ A.filter (fun a => a ≤ D),
      kernelCoeff J a * cos ((a : ℝ) * x)) ≤
      cosSum (A.filter (fun a => a ≤ D)) x +
        (1 - kernelCoeff J 1) * ∑ a ∈ A.filter (fun a => a ≤ D), (a : ℝ) ^ 2 := by
    unfold cosSum
    rw [Finset.mul_sum, ← Finset.sum_add_distrib]
    apply Finset.sum_le_sum
    intro a ha
    have hc := kernelCoeff_le_mass J hJ hn a
    have hi := kernelCoeff_increment_le J hJ hn a
    rw [hm] at hc hi
    have H := mul_nonneg (sub_nonneg.mpr hc) (show 0 ≤ 1 + cos ((a : ℝ) * x) by
      linarith [neg_one_le_cos ((a : ℝ) * x)])
    nlinarith
  linarith

end ChowlaCosine.P36


/-!
# Pointwise geometric heat-flow differential inequality

This file concerns the actual differentiated heat product. Integrating its
Laplacian and proving the large-time/density passages are separate steps.
-/

open MeasureTheory Real
open scoped Topology RealInnerProductSpace

namespace ChowlaCosine.Beckner
set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

noncomputable def heatSpaceMoment (f : ℝ → ℝ) (t x : ℝ) : ℝ :=
  ∫ y : ℝ, f y * heatSpaceSlope t (x - y)

noncomputable def heatTimeMoment (f : ℝ → ℝ) (t x : ℝ) : ℝ :=
  ∫ y : ℝ, f y * heatTimeSlope t (x - y)

noncomputable def heatSpaceScore (f : ℝ → ℝ) (t x : ℝ) : ℝ :=
  heatSpaceMoment f t x / heatFlow f t x

noncomputable def heatTimeScore (f : ℝ → ℝ) (t x : ℝ) : ℝ :=
  heatTimeMoment f t x / heatFlow f t x

theorem hasDerivAt_heatFlow_affine {f : ℝ → ℝ} (hf : Integrable f)
    {t : ℝ} (ht : 0 < t) (a b r : ℝ) :
    HasDerivAt (fun s => heatFlow f t (a + s * b)) (b * heatSpaceMoment f t (a + r * b)) r := by
  have H := (hasDerivAt_heatFlow_space hf ht (a + r * b)).comp r
    (((hasDerivAt_id r).mul_const b).const_add a)
  simpa only [Function.comp_def, id_eq, one_mul, mul_one, heatSpaceMoment, mul_comm] using! H

theorem hasDerivAt_heatSpaceMoment_affine {f : ℝ → ℝ} (hf : Integrable f)
    {t : ℝ} (ht : 0 < t) (a b r : ℝ) :
    HasDerivAt (fun s => heatSpaceMoment f t (a + s * b))
      (b * heatTimeMoment f t (a + r * b)) r := by
  have H := (hasDerivAt_heatFlow_space_slope hf ht (a + r * b)).comp r
    (((hasDerivAt_id r).mul_const b).const_add a)
  simpa only [Function.comp_def, id_eq, one_mul, mul_one, heatSpaceMoment, heatTimeMoment, mul_comm] using! H

section
variable {ι E : Type*} [Fintype ι] [NormedAddCommGroup E] [InnerProductSpace ℝ E]

noncomputable def geometricHeatProduct (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E) (t : ℝ) (x : E) : ℝ :=
  ∏ i, heatFlow (f i) t ⟪u i, x⟫ ^ c i

noncomputable def geometricHeatPath (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (t : ℝ) (x e : E) (r : ℝ) : ℝ :=
  ∏ i, heatFlow (f i) t (⟪u i, x⟫ + r * ⟪u i, e⟫) ^ c i

/-- Actual time derivative of the geometric heat product. -/
theorem hasDerivAt_geometricHeatProduct_time (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hm : ∀ i, 0 < ∫ y : ℝ, f i y) {t : ℝ} (ht : 0 < t) (x : E) :
    HasDerivAt (fun s => geometricHeatProduct f c u s x)
      (geometricHeatProduct f c u t x * ∑ i, c i * heatTimeScore (f i) t ⟪u i, x⟫) t := by
  have H := hasDerivAt_weighted_product c (fun i s => heatFlow (f i) s ⟪u i, x⟫)
    (fun i => heatTimeMoment (f i) t ⟪u i, x⟫) t
    (fun i => heatFlow_pos (hf i) (hn i) (hm i) ht _)
    (fun i => hasDerivAt_heatFlow_time (hf i) ht _)
  simpa only [geometricHeatProduct, heatTimeScore, mul_div_assoc] using! H

/-- The second derivative along any direction, with every scalar heat-flow
factor differentiated at actual real points. -/
theorem geometricHeatPath_second_derivative (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hm : ∀ i, 0 < ∫ y : ℝ, f i y) {t : ℝ} (ht : 0 < t) (x e : E) :
    deriv (deriv (geometricHeatPath f c u t x e)) 0 =
      geometricHeatProduct f c u t x *
        ((∑ i, c i * ⟪u i, e⟫ * heatSpaceScore (f i) t ⟪u i, x⟫) ^ 2 +
          ∑ i, c i * ⟪u i, e⟫ ^ 2 *
            (heatTimeScore (f i) t ⟪u i, x⟫ - heatSpaceScore (f i) t ⟪u i, x⟫ ^ 2)) := by
  let F : ι → ℝ → ℝ := fun i r => heatFlow (f i) t (⟪u i, x⟫ + r * ⟪u i, e⟫)
  let G : ι → ℝ → ℝ := fun i r => ⟪u i, e⟫ * heatSpaceMoment (f i) t (⟪u i, x⟫ + r * ⟪u i, e⟫)
  let K : ι → ℝ := fun i => ⟪u i, e⟫ ^ 2 * heatTimeMoment (f i) t ⟪u i, x⟫
  have hpos : ∀ i r, 0 < F i r := fun i r => heatFlow_pos (hf i) (hn i) (hm i) ht _
  have hF : ∀ i r, HasDerivAt (F i) (G i r) r := fun i r => hasDerivAt_heatFlow_affine (hf i) ht _ _ _
  have hG : ∀ i, HasDerivAt (G i) (K i) 0 := by
    intro i
    have H := (hasDerivAt_heatSpaceMoment_affine (hf i) ht ⟪u i, x⟫ ⟪u i, e⟫ 0).const_mul ⟪u i, e⟫
    dsimp [G, K]
    simpa only [zero_mul, add_zero, pow_two, mul_assoc] using! H
  have hfirst : deriv (geometricHeatPath f c u t x e) =
      (fun r => (∏ i, F i r ^ c i) * ∑ i, c i * (G i r / F i r)) := by
    funext r
    have H := hasDerivAt_weighted_product c F (fun i => G i r) r (fun i => hpos i r) (fun i => hF i r)
    simpa only [geometricHeatPath, F, mul_div_assoc] using! H.deriv
  rw [hfirst]
  have H := (hasDerivAt_weighted_product_slope c F G K 0 (fun i => hpos i 0)
    (fun i => hF i 0) hG).deriv
  rw [H]
  dsimp [F, G, K, geometricHeatProduct, heatSpaceScore, heatTimeScore]
  simp only [zero_mul, add_zero, mul_div_assoc, mul_pow]
  simp only [mul_sub, mul_assoc]

/-- Pointwise heat-flow differential inequality for the actual positive
geometric product, in every finite-dimensional frame. This theorem does
not interchange a derivative and an integral or integrate a Laplacian. -/
theorem geometricHeat_defect_nonneg {κ : Type*} [Fintype κ]
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hm : ∀ i, 0 < ∫ y : ℝ, f i y)
    (hc : ∀ i, 0 ≤ c i) (hu : ∀ i, ‖u i‖ = 1) (hframe : IsWeightedFrame c u)
    (b : OrthonormalBasis κ ℝ E) {t : ℝ} (ht : 0 < t) (x : E) :
    0 ≤ deriv (fun s => geometricHeatProduct f c u s x) t -
      ∑ j, deriv (deriv (geometricHeatPath f c u t x (b j))) 0 := by
  rw [(hasDerivAt_geometricHeatProduct_time f c u hf hn hm ht x).deriv]
  simp_rw [geometricHeatPath_second_derivative f c u hf hn hm ht]
  rw [← Finset.mul_sum]
  apply frame_heat_defect_nonneg c (fun i => heatSpaceScore (f i) t ⟪u i, x⟫)
    (fun i => heatTimeScore (f i) t ⟪u i, x⟫) u hc hu hframe b
  unfold geometricHeatProduct
  exact Finset.prod_nonneg (fun i _ => Real.rpow_nonneg (heatFlow_nonneg (hn i) ht _ ) _)

end
end ChowlaCosine.Beckner

namespace ChowlaCosine.Beckner
set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

/-- Whole-plane integration by parts in the first coordinate. Integrability
of the first and second derivatives replaces an unproved boundary claim. -/
theorem integral_partial_x_eq_zero (P Q : ℝ × ℝ → ℝ)
    (hP : Integrable P (volume.prod volume)) (hQ : Integrable Q (volume.prod volume))
    (hd : ∀ x y : ℝ, HasDerivAt (fun s => P (s, y)) (Q (x, y)) x) :
    (∫ z : ℝ × ℝ, Q z ∂volume.prod volume) = 0 := by
  rw [integral_prod_symm Q hQ]
  calc
    _ = ∫ _y : ℝ, (0 : ℝ) := by
      apply integral_congr_ae
      filter_upwards [hP.prod_left_ae, hQ.prod_left_ae] with y hpy hqy
      exact integral_eq_zero_of_hasDerivAt_of_integrable (fun x => hd x y) hqy hpy
    _ = 0 := by simp

/-- Whole-plane integration by parts in the second coordinate. -/
theorem integral_partial_y_eq_zero (P Q : ℝ × ℝ → ℝ)
    (hP : Integrable P (volume.prod volume)) (hQ : Integrable Q (volume.prod volume))
    (hd : ∀ x y : ℝ, HasDerivAt (fun s => P (x, s)) (Q (x, y)) y) :
    (∫ z : ℝ × ℝ, Q z ∂volume.prod volume) = 0 := by
  rw [integral_prod Q hQ]
  calc
    _ = ∫ _x : ℝ, (0 : ℝ) := by
      apply integral_congr_ae
      filter_upwards [hP.prod_right_ae, hQ.prod_right_ae] with x hpx hqx
      exact integral_eq_zero_of_hasDerivAt_of_integrable (fun y => hd x y) hqx hpx
    _ = 0 := by simp

/-- A fully explicit integral bridge for a parabolic supersolution on R².
The integrability hypotheses are obligations when applying this result to
the geometric product; they are not asserted implicitly. -/
theorem parabolic_integral_derivative_nonneg
    (F Ft : ℝ → ℝ × ℝ → ℝ) (Px Py Qx Qy : ℝ × ℝ → ℝ) (t : ℝ)
    (s : Set ℝ) (bound : ℝ × ℝ → ℝ) (hs : s ∈ 𝓝 t)
    (hFmeas : ∀ᶠ r in 𝓝 t, AEStronglyMeasurable (F r) (volume.prod volume))
    (hFint : Integrable (F t) (volume.prod volume))
    (hFtmeas : AEStronglyMeasurable (Ft t) (volume.prod volume))
    (hbound : ∀ᵐ z ∂volume.prod volume, ∀ r ∈ s, ‖Ft r z‖ ≤ bound z)
    (hbint : Integrable bound (volume.prod volume))
    (hdt : ∀ᵐ z ∂volume.prod volume, ∀ r ∈ s, HasDerivAt (fun r => F r z) (Ft r z) r)
    (hPx : Integrable Px (volume.prod volume)) (hPy : Integrable Py (volume.prod volume))
    (hQx : Integrable Qx (volume.prod volume)) (hQy : Integrable Qy (volume.prod volume))
    (hdx : ∀ x y, HasDerivAt (fun r => Px (r, y)) (Qx (x, y)) x)
    (hdy : ∀ x y, HasDerivAt (fun r => Py (x, r)) (Qy (x, y)) y)
    (hparabolic : ∀ z, Qx z + Qy z ≤ Ft t z) :
    HasDerivAt (fun r => ∫ z : ℝ × ℝ, F r z ∂volume.prod volume)
      (∫ z : ℝ × ℝ, Ft t z ∂volume.prod volume) t ∧
      0 ≤ ∫ z : ℝ × ℝ, Ft t z ∂volume.prod volume := by
  obtain ⟨hFtint, hderiv⟩ := hasDerivAt_integral_of_dominated_loc_of_deriv_le
    (μ := volume.prod volume) hs hFmeas hFint hFtmeas hbound hbint hdt
  refine ⟨hderiv, ?_⟩
  have H := integral_mono (hQx.add hQy) hFtint hparabolic
  simp only [Pi.add_apply] at H
  rw [integral_add hQx hQy, integral_partial_x_eq_zero Px Qx hPx hQx hdx,
    integral_partial_y_eq_zero Py Qy hPy hQy hdy, add_zero] at H
  exact H

end ChowlaCosine.Beckner
#print axioms ChowlaCosine.Beckner.abs_integral_le_scaled_integral
#print axioms ChowlaCosine.Beckner.integrable_heatSpaceSlope_integrand
#print axioms ChowlaCosine.Beckner.integrable_heatTimeSlope_integrand
#print axioms ChowlaCosine.Beckner.heatFlow_space_moment_bound
#print axioms ChowlaCosine.Beckner.heatFlow_time_moment_bound
#print axioms ChowlaCosine.Beckner.heatFlow_space_score_bound
#print axioms ChowlaCosine.Beckner.heatFlow_time_score_bound
#print axioms ChowlaCosine.Beckner.weighted_product_eq_exp
#print axioms ChowlaCosine.Beckner.hasDerivAt_weighted_product
#print axioms ChowlaCosine.Beckner.hasDerivAt_weighted_product_slope
#print axioms ChowlaCosine.Beckner.frame_laplacian_identity
#print axioms ChowlaCosine.Beckner.frame_heat_defect_nonneg
#print axioms ChowlaCosine.Beckner.hasDerivAt_heatFlow_affine
#print axioms ChowlaCosine.Beckner.hasDerivAt_heatSpaceMoment_affine
#print axioms ChowlaCosine.Beckner.hasDerivAt_geometricHeatProduct_time
#print axioms ChowlaCosine.Beckner.geometricHeatPath_second_derivative
#print axioms ChowlaCosine.Beckner.geometricHeat_defect_nonneg
#print axioms ChowlaCosine.Beckner.integral_partial_x_eq_zero
#print axioms ChowlaCosine.Beckner.integral_partial_y_eq_zero
#print axioms ChowlaCosine.Beckner.parabolic_integral_derivative_nonneg
