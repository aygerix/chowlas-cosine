import ChowlaCosine.P31.Corollaries

/-! # Exact moments for arbitrary complex coefficients

The positive frequencies are a finite set. All angles and phases are real;
there is no discretization in these identities.
-/

open Real MeasureTheory
open scoped BigOperators

namespace ChowlaCosine.P34

open P31

noncomputable def trigSum (A : Finset ℕ) (b : ℕ → ℂ) (x : ℝ) : ℝ :=
  ∑ j ∈ A, (b j * circleCharacter (j : ℤ) x).re

noncomputable def energy (A : Finset ℕ) (b : ℕ → ℂ) : ℝ :=
  ∑ j ∈ A, ‖b j‖ ^ 2

noncomputable def windowEnergy (w : ℕ) (A : Finset ℕ) (b : ℕ → ℂ) : ℝ :=
  ∑ j ∈ A, kappa w j ^ 2 * ‖b j‖ ^ 2

@[fun_prop] theorem continuous_trigSum (A : Finset ℕ) (b : ℕ → ℂ) :
    Continuous (trigSum A b) := by
  unfold trigSum
  fun_prop

theorem circleMean_trigSum (A : Finset ℕ) (b : ℕ → ℂ)
    (hA : ∀ j ∈ A, 0 < j) : circleMean (trigSum A b) = 0 := by
  unfold trigSum
  rw [circleMean_sum A _ (by intro j hj; fun_prop)]
  apply Finset.sum_eq_zero
  intro j hj
  rw [circleMean_re_mul_character, if_neg (by have := hA j hj; omega)]

theorem re_mul_re (z v : ℂ) :
    z.re * v.re = ((z * v).re + (z * star v).re) / 2 := by
  simp only [Complex.mul_re, Complex.star_def, Complex.conj_re, Complex.conj_im]
  ring

theorem circleMean_re_character_mul {j k : ℕ} (hj : 0 < j) (hk : 0 < k)
    (b c : ℂ) :
    circleMean (fun x => (b * circleCharacter (j : ℤ) x).re *
      (c * circleCharacter (k : ℤ) x).re) =
        if j = k then (b * star c).re / 2 else 0 := by
  have hexp : (fun x => (b * circleCharacter (j : ℤ) x).re *
      (c * circleCharacter (k : ℤ) x).re) =
      (fun x => (1 / 2 : ℝ) * (((b * c) * circleCharacter ((j : ℤ) + k) x).re +
        ((b * star c) * circleCharacter ((j : ℤ) - k) x).re)) := by
    funext x
    rw [re_mul_re, star_mul, circleCharacter_star, sub_eq_add_neg,
      circleCharacter_add, circleCharacter_add]
    simp only [mul_assoc, mul_left_comm, mul_comm]
    ring
  rw [hexp, circleMean_const_mul, circleMean_add (by fun_prop) (by fun_prop),
    circleMean_re_mul_character, circleMean_re_mul_character,
    if_neg (by omega : (j : ℤ) + k ≠ 0)]
  by_cases he : j = k
  · subst k
    simp
    ring
  · rw [if_neg (by omega : (j : ℤ) - k ≠ 0), if_neg he]
    ring

theorem circleMean_trigSum_mul (A : Finset ℕ) (b c : ℕ → ℂ)
    (hA : ∀ j ∈ A, 0 < j) :
    circleMean (fun x => trigSum A b x * trigSum A c x) =
      (∑ j ∈ A, (b j * star (c j)).re) / 2 := by
  have hexp : (fun x => trigSum A b x * trigSum A c x) =
      (fun x => ∑ j ∈ A, ∑ k ∈ A,
        (b j * circleCharacter (j : ℤ) x).re *
          (c k * circleCharacter (k : ℤ) x).re) := by
    funext x
    simp only [trigSum, Finset.sum_mul_sum]
  rw [hexp, circleMean_sum A _ (by intro j hj; fun_prop)]
  have hi : ∀ j ∈ A, circleMean (fun x => ∑ k ∈ A,
      (b j * circleCharacter (j : ℤ) x).re *
        (c k * circleCharacter (k : ℤ) x).re) = (b j * star (c j)).re / 2 := by
    intro j hj
    rw [circleMean_sum A _ (by intro k hk; fun_prop)]
    rw [Finset.sum_congr rfl (fun k hk => circleMean_re_character_mul
      (hA j hj) (hA k hk) (b j) (c k))]
    simp [hj]
  rw [Finset.sum_congr rfl hi, Finset.sum_div]

theorem circleMean_trigSum_add_sq (A : Finset ℕ) (b : ℕ → ℂ) (M : ℝ)
    (hA : ∀ j ∈ A, 0 < j) :
    circleMean (fun x => (trigSum A b x + M) ^ 2) = M ^ 2 + energy A b / 2 := by
  have hexp : (fun x => (trigSum A b x + M) ^ 2) =
      (fun x => (M ^ 2 + (2 * M) * trigSum A b x) +
        trigSum A b x * trigSum A b x) := by funext x; ring
  rw [hexp, circleMean_add (by fun_prop) (by fun_prop),
    circleMean_add (by fun_prop) (by fun_prop), circleMean_const,
    circleMean_const_mul, circleMean_trigSum A b hA,
    circleMean_trigSum_mul A b b hA]
  simp [energy, Complex.mul_conj, Complex.normSq_eq_norm_sq,
    -Complex.ofReal_pow]

theorem circleCharacter_re (j : ℤ) (x : ℝ) :
    (circleCharacter j x).re = Real.cos ((j : ℝ) * x) := by
  unfold circleCharacter
  rw [show (j : ℂ) * (x : ℂ) * Complex.I =
    (((j : ℝ) * x : ℝ) : ℂ) * Complex.I by push_cast; ring,
    Complex.exp_ofReal_mul_I_re]

theorem circleCharacter_im (j : ℤ) (x : ℝ) :
    (circleCharacter j x).im = Real.sin ((j : ℝ) * x) := by
  unfold circleCharacter
  rw [show (j : ℂ) * (x : ℂ) * Complex.I =
    (((j : ℝ) * x : ℝ) : ℂ) * Complex.I by push_cast; ring,
    Complex.exp_ofReal_mul_I_im]

theorem circleMean_fejer_mul_re (w : ℕ) {j : ℕ} (hj : 0 < j) (b : ℂ) (y : ℝ) :
    circleMean (fun x => fejerKernel w (x - y) *
      (b * circleCharacter (j : ℤ) x).re) =
        kappa w j * (b * circleCharacter (j : ℤ) y).re := by
  let d : ℕ → ℂ := fun k => (kappa w k : ℂ) * circleCharacter (-(k : ℤ)) y
  have hk : ∀ k x, kappa w k * Real.cos ((k : ℝ) * (x - y)) =
      (d k * circleCharacter (k : ℤ) x).re := by
    intro k x
    have he : circleCharacter (-(k : ℤ)) y * circleCharacter (k : ℤ) x =
        circleCharacter (k : ℤ) (x - y) := by
      unfold circleCharacter
      rw [← Complex.exp_add]
      congr 1
      push_cast
      ring
    simp only [d, mul_assoc, he, Complex.mul_re, Complex.ofReal_re,
      Complex.ofReal_im, zero_mul, sub_zero, circleCharacter_re, Int.cast_natCast]
  have hexp : (fun x => fejerKernel w (x - y) *
      (b * circleCharacter (j : ℤ) x).re) =
      (fun x => (b * circleCharacter (j : ℤ) x).re + 2 *
        ∑ k ∈ windowFreq w, (d k * circleCharacter (k : ℤ) x).re *
          (b * circleCharacter (j : ℤ) x).re) := by
    funext x
    simp only [fejerKernel, weightedCos, add_mul, one_mul]
    congr 1
    rw [mul_assoc]
    congr 1
    rw [Finset.sum_mul]
    apply Finset.sum_congr rfl
    intro k hk'
    rw [hk]
  rw [hexp, circleMean_add (by fun_prop) (by fun_prop),
    circleMean_re_mul_character, if_neg (by omega : (j : ℤ) ≠ 0), zero_add,
    circleMean_const_mul, circleMean_sum _ _ (by intro k hk; fun_prop)]
  rw [Finset.sum_congr rfl (fun k hk => circleMean_re_character_mul
    (windowFreq_pos w k hk) hj (d k) b)]
  by_cases hjw : j ∈ windowFreq w
  · simp only [Finset.sum_ite_eq', hjw, ↓reduceIte]
    have he : (d j * star b).re =
        kappa w j * (b * circleCharacter (j : ℤ) y).re := by
      rw [show d j * star b = (kappa w j : ℂ) *
        star (b * circleCharacter (j : ℤ) y) by
          simp only [d, star_mul, circleCharacter_star]; ring]
      simp [Complex.mul_re]
    rw [he]
    ring
  · have hjw' : w < j := by simp only [windowFreq, Finset.mem_Icc] at hjw; omega
    simp [hjw, kappa_eq_zero hjw']

theorem circleMean_window (w : ℕ) (A : Finset ℕ) (b : ℕ → ℂ) (M y : ℝ)
    (hA : ∀ j ∈ A, 0 < j) :
    circleMean (fun x => fejerKernel w (x - y) * (trigSum A b x + M)) =
      M + trigSum A (fun j => (kappa w j : ℂ) * b j) y := by
  have hexp : (fun x => fejerKernel w (x - y) * (trigSum A b x + M)) =
      (fun x => (∑ j ∈ A, fejerKernel w (x - y) *
        (b j * circleCharacter (j : ℤ) x).re) + fejerKernel w (x - y) * M) := by
    funext x
    simp only [trigSum, mul_add, Finset.mul_sum]
  rw [hexp, circleMean_add (by fun_prop) (by fun_prop),
    circleMean_sum A _ (by intro j hj; fun_prop), circleMean_mul_const,
    circleMean_fejerKernel_shift, one_mul]
  rw [Finset.sum_congr rfl (fun j hj => circleMean_fejer_mul_re w (hA j hj) (b j) y)]
  simp only [trigSum, mul_assoc, Complex.mul_re, Complex.ofReal_re, Complex.ofReal_im,
    zero_mul, sub_zero]
  ring

theorem circleMean_window_mean_sq (w : ℕ) (A : Finset ℕ) (b : ℕ → ℂ) (M : ℝ)
    (hA : ∀ j ∈ A, 0 < j) :
    circleMean (fun y => circleMean
      (fun x => fejerKernel w (x - y) * (trigSum A b x + M)) ^ 2) =
        M ^ 2 + windowEnergy w A b / 2 := by
  simp_rw [circleMean_window w A b M _ hA, add_comm M]
  rw [circleMean_trigSum_add_sq A _ M hA]
  simp [energy, windowEnergy, mul_pow, Complex.norm_real, Real.norm_eq_abs,
    sq_abs]

end ChowlaCosine.P34
