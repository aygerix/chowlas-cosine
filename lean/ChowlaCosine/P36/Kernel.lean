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
  simp only [Int.cast_natCast]
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
    apply Finset.sum_congr rfl
    intro i hi
    rw [circleMean_sum _ _ (by intro j hj; fun_prop)]
    apply Finset.sum_congr rfl
    intro j hj
    simp only [mul_assoc]
    rw [circleMean_const_mul, circleMean_const_mul, mean_cos_int_mul_shift]
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
    simp only [heq]
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
  simp only [Nat.cast_one]
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
  simp only [kernelCoeff, neg_one_mul, sub_eq_add_neg]

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
  rw [mean_increment J hJ a, circleMean_const_mul] at H
  simpa only [Nat.cast_one] using H.trans_eq (congrArg (fun z => (a : ℝ)^2 * z) (by
    simpa only [Nat.cast_one] using mean_increment J hJ 1))

/-- Full-circle truncation for any explicit probability kernel of degree D.
The translated-cosine identity is exact, with no sampled angles. -/
theorem truncation_of_kernel (A : Finset ℕ) (D : ℕ) (M : ℝ)
    (hM : ∀ x : ℝ, -M ≤ cosSum A x)
    (J : ℝ → ℝ) (hJ : Continuous J) (hn : ∀ x, 0 ≤ J x)
    (hm : circleMean J = 1)
    (hkill : ∀ a, D < a → kernelCoeff J a = 0)
    (hshift : ∀ (a : ℕ) (x : ℝ), circleMean (fun y => J y * cos ((a : ℝ) * (x - y))) =
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
