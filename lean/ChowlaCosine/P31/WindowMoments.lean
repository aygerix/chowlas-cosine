import ChowlaCosine.Moments

/-!
# Exact circle moments used in P31

All means use `dx/(2π)`. Frequencies form a `Finset ℕ`, with strict
positivity supplied explicitly. No factorization or Nikolskii bound is
assumed in this file.
-/

open Real MeasureTheory
open scoped BigOperators

namespace ChowlaCosine.P31

noncomputable def circleMean (f : ℝ → ℝ) : ℝ :=
  (2 * π)⁻¹ * ∫ x in (0 : ℝ)..2 * π, f x

@[simp] theorem circleMean_const (c : ℝ) : circleMean (fun _ => c) = c := by
  simp [circleMean, mul_assoc, Real.pi_ne_zero]

theorem circleMean_add {f g : ℝ → ℝ} (hf : Continuous f) (hg : Continuous g) :
    circleMean (fun x => f x + g x) = circleMean f + circleMean g := by
  simp only [circleMean, intervalIntegral.integral_add (hf.intervalIntegrable _ _)
    (hg.intervalIntegrable _ _), mul_add]

theorem circleMean_mul_const (f : ℝ → ℝ) (c : ℝ) :
    circleMean (fun x => f x * c) = circleMean f * c := by
  simp only [circleMean, intervalIntegral.integral_mul_const, mul_assoc]

theorem circleMean_const_mul (f : ℝ → ℝ) (c : ℝ) :
    circleMean (fun x => c * f x) = c * circleMean f := by
  simp only [circleMean, intervalIntegral.integral_const_mul]
  ring

theorem circleMean_sum {ι : Type*} (s : Finset ι) (f : ι → ℝ → ℝ)
    (hf : ∀ i ∈ s, Continuous (f i)) :
    circleMean (fun x => ∑ i ∈ s, f i x) = ∑ i ∈ s, circleMean (f i) := by
  simp only [circleMean, intervalIntegral.integral_finsetSum
    (fun i hi => (hf i hi).intervalIntegrable _ _), Finset.mul_sum]

theorem circleMean_mono {f g : ℝ → ℝ} (hf : Continuous f) (hg : Continuous g)
    (hfg : ∀ x, f x ≤ g x) : circleMean f ≤ circleMean g := by
  apply mul_le_mul_of_nonneg_left _ (by positivity)
  exact intervalIntegral.integral_mono (by positivity) (hf.intervalIntegrable _ _)
    (hg.intervalIntegrable _ _) hfg

noncomputable def weightedCos (A : Finset ℕ) (b : ℕ → ℝ) (x : ℝ) : ℝ :=
  ∑ a ∈ A, b a * Real.cos ((a : ℝ) * x)

@[fun_prop] theorem continuous_weightedCos (A : Finset ℕ) (b : ℕ → ℝ) :
    Continuous (weightedCos A b) := by
  unfold weightedCos
  fun_prop

theorem circleMean_weightedCos (A : Finset ℕ) (b : ℕ → ℝ)
    (hA : ∀ a ∈ A, 0 < a) : circleMean (weightedCos A b) = 0 := by
  unfold weightedCos
  rw [circleMean_sum A _ (by intro a ha; fun_prop)]
  apply Finset.sum_eq_zero
  intro a ha
  rw [circleMean_const_mul]
  simp [circleMean, integral_cos_nat_mul (hA a ha)]

theorem circleMean_cos_mul_cos {a b : ℕ} (ha : 0 < a) (hb : 0 < b) :
    circleMean (fun x => Real.cos ((a : ℝ) * x) * Real.cos ((b : ℝ) * x)) =
      if a = b then 1 / 2 else 0 := by
  unfold circleMean
  rw [integral_cos_mul_cos_nat ha hb]
  split_ifs <;> simp <;> field_simp

theorem circleMean_weightedCos_mul (A : Finset ℕ) (b c : ℕ → ℝ)
    (hA : ∀ a ∈ A, 0 < a) :
    circleMean (fun x => weightedCos A b x * weightedCos A c x) =
      (∑ a ∈ A, b a * c a) / 2 := by
  have hexp : (fun x => weightedCos A b x * weightedCos A c x) =
      (fun x => ∑ a ∈ A, ∑ d ∈ A,
        (b a * c d) * (Real.cos ((a : ℝ) * x) * Real.cos ((d : ℝ) * x))) := by
    funext x
    simp only [weightedCos, Finset.sum_mul_sum]
    apply Finset.sum_congr rfl
    intro a ha
    apply Finset.sum_congr rfl
    intro d hd
    ring
  rw [hexp, circleMean_sum A _ (by intro a ha; fun_prop)]
  have hs : ∀ a ∈ A, circleMean (fun x => ∑ d ∈ A,
      (b a * c d) * (Real.cos ((a : ℝ) * x) * Real.cos ((d : ℝ) * x))) =
        b a * c a / 2 := by
    intro a ha
    rw [circleMean_sum A (fun d x => (b a * c d) *
      (Real.cos ((a : ℝ) * x) * Real.cos ((d : ℝ) * x)))
        (by intro d hd; fun_prop)]
    have hi : ∀ d ∈ A, circleMean (fun x => (b a * c d) *
        (Real.cos ((a : ℝ) * x) * Real.cos ((d : ℝ) * x))) =
          if a = d then b a * c d / 2 else 0 := by
      intro d hd
      rw [circleMean_const_mul, circleMean_cos_mul_cos (hA a ha) (hA d hd)]
      split_ifs <;> ring
    rw [Finset.sum_congr rfl hi]
    simp [ha]
  rw [Finset.sum_congr rfl hs, Finset.sum_div]

theorem circleMean_shifted_weightedCos_sq (A : Finset ℕ) (b : ℕ → ℝ) (M : ℝ)
    (hA : ∀ a ∈ A, 0 < a) :
    circleMean (fun x => (M + weightedCos A b x) ^ 2) =
      M ^ 2 + (∑ a ∈ A, (b a) ^ 2) / 2 := by
  have hexp : (fun x => (M + weightedCos A b x) ^ 2) =
      (fun x => (M ^ 2 + (2 * M) * weightedCos A b x) +
        weightedCos A b x * weightedCos A b x) := by funext x; ring
  rw [hexp, circleMean_add (by fun_prop) (by fun_prop),
    circleMean_add (by fun_prop) (by fun_prop), circleMean_const,
    circleMean_const_mul, circleMean_weightedCos A b hA,
    circleMean_weightedCos_mul A b b hA]
  simp [pow_two]

noncomputable def kappa (w a : ℕ) : ℝ := max 0 (1 - (a : ℝ) / (w + 1))

def windowFreq (w : ℕ) : Finset ℕ := Finset.Icc 1 w

theorem windowFreq_pos (w : ℕ) : ∀ a ∈ windowFreq w, 0 < a := by
  intro a ha
  simp only [windowFreq, Finset.mem_Icc] at ha
  omega

theorem kappa_eq_zero {w a : ℕ} (ha : w < a) : kappa w a = 0 := by
  unfold kappa
  apply max_eq_left
  have hw : (0 : ℝ) < w + 1 := by positivity
  have ha' : (w : ℝ) + 1 ≤ a := by exact_mod_cast ha
  have : (1 : ℝ) ≤ (a : ℝ) / (w + 1) :=
    (le_div_iff₀ hw).mpr (by simpa using ha')
  linarith

theorem kappa_of_mem {w a : ℕ} (ha : a ∈ windowFreq w) :
    kappa w a = 1 - (a : ℝ) / (w + 1) := by
  unfold kappa
  apply max_eq_right
  have hw : (0 : ℝ) < w + 1 := by positivity
  have ha' : (a : ℝ) ≤ w + 1 := by
    have : a ≤ w := (Finset.mem_Icc.mp ha).2
    exact_mod_cast Nat.le_succ_of_le this
  have := (div_le_one₀ hw).mpr ha'
  linarith

noncomputable def fejerKernel (w : ℕ) (x : ℝ) : ℝ :=
  1 + 2 * weightedCos (windowFreq w) (kappa w) x

noncomputable def windowMass (w : ℕ) : ℝ :=
  1 + 2 * ∑ a ∈ windowFreq w, (kappa w a) ^ 2

noncomputable def windowEnergy (w : ℕ) (A : Finset ℕ) : ℝ :=
  ∑ a ∈ A, (kappa w a) ^ 2

@[fun_prop] theorem continuous_fejerKernel (w : ℕ) : Continuous (fejerKernel w) := by
  unfold fejerKernel
  fun_prop

theorem circleMean_fejerKernel (w : ℕ) : circleMean (fejerKernel w) = 1 := by
  unfold fejerKernel
  rw [circleMean_add (by fun_prop) (by fun_prop), circleMean_const,
    circleMean_const_mul, circleMean_weightedCos _ _ (windowFreq_pos w)]
  ring

theorem circleMean_fejerKernel_sq (w : ℕ) :
    circleMean (fun x => fejerKernel w x ^ 2) = windowMass w := by
  have h : fejerKernel w = fun x =>
      1 + weightedCos (windowFreq w) (fun a => 2 * kappa w a) x := by
    funext x
    simp [fejerKernel, weightedCos, Finset.mul_sum, mul_assoc]
  rw [h, circleMean_shifted_weightedCos_sq _ _ _ (windowFreq_pos w)]
  simp only [windowMass]
  have hs : (∑ a ∈ windowFreq w, (2 * kappa w a) ^ 2) =
      4 * ∑ a ∈ windowFreq w, (kappa w a) ^ 2 := by
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro a ha
    ring
  rw [hs]
  ring

theorem circleMean_cosSum_add_sq (A : Finset ℕ) (M : ℝ)
    (hA : ∀ a ∈ A, 0 < a) :
    circleMean (fun x => (cosSum A x + M) ^ 2) = (A.card : ℝ) / 2 + M ^ 2 := by
  have heq : cosSum A = weightedCos A (fun _ => 1) := by
    funext x
    simp [cosSum, weightedCos]
  simp_rw [heq, add_comm (weightedCos _ _ _) M]
  rw [circleMean_shifted_weightedCos_sq A _ M hA]
  simp
  ring

theorem fejerKernel_periodic (w : ℕ) :
    Function.Periodic (fejerKernel w) (2 * π) := by
  intro x
  unfold fejerKernel weightedCos
  congr 2
  apply Finset.sum_congr rfl
  intro a ha
  rw [mul_add, Real.cos_add_nat_mul_two_pi]

theorem circleMean_cos_shift {a : ℕ} (ha : 0 < a) (y : ℝ) :
    circleMean (fun x => Real.cos ((a : ℝ) * (x - y))) = 0 := by
  have hi := integral_cos_int_mul_add (a : ℤ) (-(a : ℝ) * y)
  have hn : (a : ℤ) ≠ 0 := by omega
  rw [if_neg hn] at hi
  have heq : (fun x : ℝ => Real.cos ((a : ℝ) * (x - y))) =
      (fun x => Real.cos (((a : ℤ) : ℝ) * x + -(a : ℝ) * y)) := by
    funext x
    congr 1
    push_cast
    ring
  unfold circleMean
  rw [heq, hi, mul_zero]

theorem circleMean_cos_shift_mul_cos {k a : ℕ}
    (hk : 0 < k) (ha : 0 < a) (y : ℝ) :
    circleMean (fun x => Real.cos ((k : ℝ) * (x - y)) *
      Real.cos ((a : ℝ) * x)) =
        if k = a then Real.cos ((a : ℝ) * y) / 2 else 0 := by
  have hi := integral_cos_mul_cos (k : ℤ) (a : ℤ) (-(k : ℝ) * y) 0
  have hn : (k : ℤ) + a ≠ 0 := by omega
  rw [if_neg hn, add_zero] at hi
  have heq : (fun x : ℝ => Real.cos ((k : ℝ) * (x - y)) *
      Real.cos ((a : ℝ) * x)) =
      (fun x => Real.cos (((k : ℤ) : ℝ) * x + -(k : ℝ) * y) *
        Real.cos (((a : ℤ) : ℝ) * x + 0)) := by
    funext x
    congr 2 <;> push_cast <;> ring
  unfold circleMean
  rw [heq, hi]
  by_cases hka : k = a
  · subst k
    simp
    field_simp
  · have hdiff : (k : ℤ) - a ≠ 0 := by omega
    simp [hdiff, hka]

end ChowlaCosine.P31
