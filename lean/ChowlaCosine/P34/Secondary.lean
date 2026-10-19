import ChowlaCosine.P31.Corollaries
import ChowlaCosine.Averaging

/-! # P33 ratio and the dilation pinch

The ratio proof uses the nonnegative Fejér weights on the (X+m)-th roots
of unity. Exact orthogonality makes their weighted cosine sum zero. The
weight at angle zero is m, and the total weight away from zero is X.
-/

open Real
open scoped BigOperators

namespace ChowlaCosine.P34

open P31

private noncomputable def rootSum (q : ℕ) (f : ℝ → ℝ) : ℝ :=
  ∑ j ∈ Finset.range q, f (2 * π * j / q)

private theorem rootSum_add (q : ℕ) (f g : ℝ → ℝ) :
    rootSum q (fun x => f x + g x) = rootSum q f + rootSum q g := by
  simp only [rootSum, Finset.sum_add_distrib]

private theorem rootSum_const_mul (q : ℕ) (c : ℝ) (f : ℝ → ℝ) :
    rootSum q (fun x => c * f x) = c * rootSum q f := by
  simp only [rootSum, Finset.mul_sum]

private theorem rootSum_sum (q : ℕ) (A : Finset ℕ) (f : ℕ → ℝ → ℝ) :
    rootSum q (fun x => ∑ k ∈ A, f k x) = ∑ k ∈ A, rootSum q (f k) := by
  exact Finset.sum_comm

private theorem rootSum_cos {q a : ℕ} (ha : 0 < a) (haq : a < q) :
    rootSum q (fun x => Real.cos ((a : ℝ) * x)) = 0 := by
  have hnot : ¬q ∣ a := by
    intro h
    have := Nat.le_of_dvd ha h
    omega
  simpa only [rootSum, zero_add, if_neg hnot] using
    sum_range_cos_shift a q (by omega) 0

private theorem rootSum_cos_mul_cos {q a k : ℕ}
    (hka : k < a) (haq : a + k < q) :
    rootSum q (fun x => Real.cos ((k : ℝ) * x) * Real.cos ((a : ℝ) * x)) = 0 := by
  have hpoint : (fun x => (2 : ℝ) *
      (Real.cos ((k : ℝ) * x) * Real.cos ((a : ℝ) * x))) =
      (fun x => Real.cos (((a + k : ℕ) : ℝ) * x) +
        Real.cos (((a - k : ℕ) : ℝ) * x)) := by
    funext x
    rw [Nat.cast_add, Nat.cast_sub (by omega : k ≤ a), add_mul, sub_mul,
      Real.cos_add, Real.cos_sub]
    ring
  have h := congrArg (rootSum q) hpoint
  rw [rootSum_const_mul, rootSum_add, rootSum_cos (by omega) haq,
    rootSum_cos (by omega) (by omega)] at h
  linarith

private theorem rootSum_fejer {q w : ℕ} (hw : w < q) :
    rootSum q (fejerKernel w) = q := by
  unfold fejerKernel weightedCos
  rw [rootSum_add, rootSum_const_mul, rootSum_sum]
  have hz : ∀ k ∈ windowFreq w, rootSum q (fun x =>
      kappa w k * Real.cos ((k : ℝ) * x)) = 0 := by
    intro k hk
    rw [rootSum_const_mul, rootSum_cos (windowFreq_pos w k hk)
      (by have := (Finset.mem_Icc.mp hk).2; omega), mul_zero]
  rw [Finset.sum_eq_zero hz]
  simp [rootSum]

private theorem rootSum_fejer_mul_cos {q w a : ℕ}
    (hwa : w < a) (haq : a + w < q) :
    rootSum q (fun x => fejerKernel w x * Real.cos ((a : ℝ) * x)) = 0 := by
  have hpoint : (fun x => fejerKernel w x * Real.cos ((a : ℝ) * x)) =
      (fun x => Real.cos ((a : ℝ) * x) + 2 * ∑ k ∈ windowFreq w,
        kappa w k * (Real.cos ((k : ℝ) * x) * Real.cos ((a : ℝ) * x))) := by
    funext x
    simp only [fejerKernel, weightedCos, add_mul, one_mul]
    congr 1
    rw [mul_assoc]
    congr 1
    rw [Finset.sum_mul]
    apply Finset.sum_congr rfl
    intro k hk
    ring
  rw [hpoint, rootSum_add, rootSum_cos (by omega) (by omega),
    rootSum_const_mul, rootSum_sum]
  have hz : ∀ k ∈ windowFreq w, rootSum q (fun x => kappa w k *
      (Real.cos ((k : ℝ) * x) * Real.cos ((a : ℝ) * x))) = 0 := by
    intro k hk
    have hkw := (Finset.mem_Icc.mp hk).2
    rw [rootSum_const_mul, rootSum_cos_mul_cos (by omega) (by omega), mul_zero]
  rw [Finset.sum_eq_zero hz]
  ring

theorem fejerKernel_zero (w : ℕ) : fejerKernel w 0 = (w : ℝ) + 1 := by
  have h := fejer_triangle_sq w 0
  simp only [mul_zero, Real.cos_zero, Real.sin_zero, Finset.sum_const,
    Finset.card_range, nsmul_eq_mul, mul_one, mul_zero, zero_pow (by decide : (2 : ℕ) ≠ 0),
    add_zero, Nat.cast_add, Nat.cast_one] at h
  have hw : (0 : ℝ) < w + 1 := by positivity
  apply mul_left_cancel₀ hw.ne'
  nlinarith

/-- P33 ratio, for any lower and upper bounds m and X for a nonempty
finite set of positive frequencies. In particular m and X can be min A and max A. -/
theorem p33_ratio (A : Finset ℕ) (hne : A.Nonempty) (m X : ℕ) (hm : 1 ≤ m)
    (hlo : ∀ a ∈ A, m ≤ a) (hhi : ∀ a ∈ A, a ≤ X)
    (M : ℝ) (hM : ∀ x : ℝ, -M ≤ cosSum A x) :
    (A.card : ℝ) * m / X ≤ M := by
  obtain ⟨a, ha⟩ := hne
  have hX : 0 < X := by have := hlo a ha; have := hhi a ha; omega
  let q := X + m
  let w := m - 1
  have hq : 0 < q := by omega
  have hwm : w + 1 = m := by omega
  have hsum : rootSum q (fun x => fejerKernel w x * cosSum A x) = 0 := by
    have heq : (fun x => fejerKernel w x * cosSum A x) =
        (fun x => ∑ a ∈ A, fejerKernel w x * Real.cos ((a : ℝ) * x)) := by
      funext x
      simp only [cosSum, Finset.mul_sum]
    rw [heq, rootSum_sum]
    apply Finset.sum_eq_zero
    intro a ha
    have := hlo a ha
    have := hhi a ha
    exact rootSum_fejer_mul_cos (by omega) (by omega)
  have hmass : rootSum q (fejerKernel w) = q := rootSum_fejer (by omega)
  have htotal : rootSum q (fun x => fejerKernel w x * (cosSum A x + M)) = M * q := by
    simp only [mul_add]
    rw [rootSum_add, hsum, zero_add]
    have heq : (fun x => fejerKernel w x * M) = (fun x => M * fejerKernel w x) := by
      funext x
      ring
    rw [heq, rootSum_const_mul, hmass]
  have hsingle := Finset.single_le_sum
    (f := fun j : ℕ => fejerKernel w (2 * π * j / q) * (cosSum A (2 * π * j / q) + M))
    (s := Finset.range q)
    (fun j hj => mul_nonneg (fejerKernel_nonneg w _) (by linarith [hM (2 * π * j / q)]))
    (a := 0) (by simpa using hq)
  change _ ≤ rootSum q (fun x => fejerKernel w x * (cosSum A x + M)) at hsingle
  rw [htotal] at hsingle
  simp only [Nat.cast_zero, mul_zero, zero_div, fejerKernel_zero, cosSum_zero] at hsingle
  have hwmr : (w : ℝ) + 1 = m := by exact_mod_cast hwm
  rw [hwmr] at hsingle
  have hqr : (q : ℝ) = X + m := by simp [q]
  rw [hqr] at hsingle
  apply (div_le_iff₀ (show (0 : ℝ) < X by exact_mod_cast hX)).mpr
  nlinarith

/-- The requested min/max specialization, with nonemptiness and positivity explicit. -/
theorem p33_ratio_min_max (A : Finset ℕ) (hne : A.Nonempty)
    (hA : ∀ a ∈ A, 0 < a) (M : ℝ) (hM : ∀ x : ℝ, -M ≤ cosSum A x) :
    (A.card : ℝ) * A.min' hne / A.max' hne ≤ M := by
  exact p33_ratio A hne (A.min' hne) (A.max' hne)
    (hA _ (Finset.min'_mem A hne))
    (fun a ha => Finset.min'_le A a ha)
    (fun a ha => Finset.le_max' A a ha) M hM

/-- Exact dilation identity at all q-th roots, including q=1. -/
theorem dilation_identity (A : Finset ℕ) (q : ℕ) (hq : 1 ≤ q) :
    (∑ j ∈ Finset.range q, cosSum A (2 * π * j / q)) =
      (q : ℝ) * (A.filter (fun a => q ∣ a)).card := by
  simpa only [zero_add, cosSum_zero] using sum_cosSum_shift A q (by omega) 0

/-- Dilation pinch in the requested division form, at every q≥1. -/
theorem dilation_pinch (A : Finset ℕ) (q : ℕ) (hq : 1 ≤ q) (M : ℝ)
    (hM : ∀ x : ℝ, -M ≤ cosSum A x) :
    (A.card : ℝ) / q - (1 - 1 / (q : ℝ)) * M ≤ (A.filter (fun a => q ∣ a)).card := by
  by_cases hq1 : q = 1
  · simp [hq1]
  · have h := card_sub_le_of_cosSum_ge A q (by omega) M hM
    have hqr : (0 : ℝ) < q := by exact_mod_cast (show 0 < q by omega)
    have h' : ((A.card : ℝ) - ((q : ℝ) - 1) * M) / q ≤
        (A.filter (fun a => q ∣ a)).card := by
      apply (div_le_iff₀ hqr).mpr
      nlinarith
    convert h' using 1
    field_simp

end ChowlaCosine.P34
