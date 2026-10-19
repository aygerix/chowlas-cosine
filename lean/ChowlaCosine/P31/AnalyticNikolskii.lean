import ChowlaCosine.P31.Main
import ChowlaCosine.P31.ElementaryConvolution

/-! # From the elementary coefficient bound to analytic Nikolskii

Finite Fourier orthogonality is exact, including repeated pair frequencies.
-/

open Real MeasureTheory
open scoped BigOperators

namespace ChowlaCosine.P31

@[fun_prop] theorem continuous_circleCharacter (k : ℤ) : Continuous (circleCharacter k) := by
  unfold circleCharacter
  fun_prop

theorem circleCharacter_add (k m : ℤ) (x : ℝ) :
    circleCharacter (k + m) x = circleCharacter k x * circleCharacter m x := by
  unfold circleCharacter
  rw [← Complex.exp_add]
  congr 1
  push_cast
  ring

theorem circleCharacter_star (k : ℤ) (x : ℝ) :
    star (circleCharacter k x) = circleCharacter (-k) x := by
  simp [circleCharacter, Complex.star_def, ← Complex.exp_conj]

theorem circleMean_re_mul_character (c : ℂ) (k : ℤ) :
    circleMean (fun x => (c * circleCharacter k x).re) = if k = 0 then c.re else 0 := by
  by_cases hk : k = 0
  · subst k
    simp [circleCharacter]
  · rw [if_neg hk]
    have hre : ∀ x : ℝ, (circleCharacter k x).re = Real.cos ((k : ℝ) * x) := by
      intro x
      unfold circleCharacter
      have harg : (k : ℂ) * (x : ℂ) * Complex.I = (((k : ℝ) * x : ℝ) : ℂ) * Complex.I := by
        push_cast
        ring
      rw [harg, Complex.exp_ofReal_mul_I_re]
    have him : ∀ x : ℝ, (circleCharacter k x).im = Real.sin ((k : ℝ) * x) := by
      intro x
      unfold circleCharacter
      have harg : (k : ℂ) * (x : ℂ) * Complex.I = (((k : ℝ) * x : ℝ) : ℂ) * Complex.I := by
        push_cast
        ring
      rw [harg, Complex.exp_ofReal_mul_I_im]
    unfold circleMean
    simp only [Complex.mul_re, hre, him]
    rw [intervalIntegral.integral_sub (by apply Continuous.intervalIntegrable; fun_prop)
      (by apply Continuous.intervalIntegrable; fun_prop), intervalIntegral.integral_const_mul,
      intervalIntegral.integral_const_mul, integral_cos_int_mul hk, integral_sin_int_mul]
    ring

/-- Parseval with arbitrary finite, possibly repeated, integer frequencies. -/
theorem circleMean_norm_sq_sum {ι : Type*} [Fintype ι] (u : ι → ℂ) (k : ι → ℤ) :
    circleMean (fun x => ‖∑ j : ι, u j * circleCharacter (k j) x‖ ^ 2) =
      ∑ i : ι, ∑ j : ι, if k i = k j then (u i * star (u j)).re else 0 := by
  classical
  have hpoint : ∀ x : ℝ, ‖∑ j : ι, u j * circleCharacter (k j) x‖ ^ 2 =
      ∑ i : ι, ∑ j : ι, ((u i * star (u j)) * circleCharacter (k i - k j) x).re := by
    intro x
    have hnorm : ∀ z : ℂ, ‖z‖ ^ 2 = (z * star z).re := by
      intro z
      rw [Complex.star_def, Complex.mul_conj, Complex.ofReal_re, Complex.normSq_eq_norm_sq]
    rw [hnorm, star_sum, Finset.sum_mul_sum]
    simp only [Complex.re_sum]
    apply Finset.sum_congr rfl
    intro i hi
    apply Finset.sum_congr rfl
    intro j hj
    congr 1
    rw [star_mul, circleCharacter_star, sub_eq_add_neg, circleCharacter_add]
    ring
  simp_rw [hpoint]
  rw [circleMean_sum Finset.univ _ (by intro i hi; fun_prop)]
  apply Finset.sum_congr rfl
  intro i hi
  rw [circleMean_sum Finset.univ _ (by intro j hj; fun_prop)]
  apply Finset.sum_congr rfl
  intro j hj
  rw [circleMean_re_mul_character]
  simp only [sub_eq_zero]

/-- Exact normalized second moment of an analytic coefficient vector. -/
theorem circleMean_analytic_sq (L : ℕ) (u : Fin (L + 1) → ℂ) :
    circleMean (fun x => ‖analyticValue u x‖ ^ 2) = ∑ j : Fin (L + 1), ‖u j‖ ^ 2 := by
  have heq : analyticValue u = fun x =>
      ∑ j : Fin (L + 1), u j * circleCharacter (j.val : ℤ) x := by
    funext x
    simp [analyticValue, circleCharacter]
  rw [heq, circleMean_norm_sq_sum]
  apply Finset.sum_congr rfl
  intro i hi
  have hiff : ∀ j : Fin (L + 1), ((i.val : ℤ) = (j.val : ℤ)) ↔ i = j := by
    intro j
    constructor
    · intro h
      apply Fin.ext
      exact_mod_cast h
    · rintro rfl
      rfl
  simp_rw [hiff]
  simp only [Finset.sum_ite_eq, Finset.sum_ite_eq', Finset.mem_univ, ↓reduceIte]
  rw [Complex.star_def, Complex.mul_conj, Complex.ofReal_re, Complex.normSq_eq_norm_sq]

/-- The real four-index sum in the pair-frequency ordering is exactly
the ordered-pair energy used by P31-E. -/
theorem real_additive_quad_eq_energy (N : ℕ) (v : Fin N → ℝ) :
    (∑ p : Fin N × Fin N, ∑ q : Fin N × Fin N,
      if p.1.val + p.2.val = q.1.val + q.2.val then
        (v p.1 * v p.2) * (v q.1 * v q.2) else 0) = discreteEnergy N v := by
  unfold discreteEnergy
  simp only [Fintype.sum_prod_type]
  apply Finset.sum_congr rfl
  intro a ha
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro c hc
  apply Finset.sum_congr rfl
  intro b hb
  apply Finset.sum_congr rfl
  intro d hd
  split_ifs <;> ring

/-- The fourth circle moment is bounded by the real nonnegative coefficient energy. -/
theorem circleMean_analytic_four_le_energy (L : ℕ) (u : Fin (L + 1) → ℂ) :
    circleMean (fun x => ‖analyticValue u x‖ ^ 4) ≤
      discreteEnergy (L + 1) (fun j => ‖u j‖) := by
  have hsq : ∀ x : ℝ, analyticValue u x ^ 2 =
      ∑ p : Fin (L + 1) × Fin (L + 1), (u p.1 * u p.2) *
        circleCharacter ((p.1.val : ℤ) + p.2.val) x := by
    intro x
    rw [sq, analyticValue, Finset.sum_mul_sum, Fintype.sum_prod_type]
    apply Finset.sum_congr rfl
    intro i hi
    apply Finset.sum_congr rfl
    intro j hj
    rw [circleCharacter_add]
    simp only [circleCharacter, Int.cast_natCast]
    ring
  have hnorm : (fun x => ‖analyticValue u x‖ ^ 4) =
      (fun x => ‖∑ p : Fin (L + 1) × Fin (L + 1), (u p.1 * u p.2) *
        circleCharacter ((p.1.val : ℤ) + p.2.val) x‖ ^ 2) := by
    funext x
    rw [← hsq x, norm_pow, ← pow_mul]
  rw [hnorm, circleMean_norm_sq_sum, ← real_additive_quad_eq_energy]
  apply Finset.sum_le_sum
  intro p hp
  apply Finset.sum_le_sum
  intro q hq
  have heq : (((p.1.val : ℤ) + p.2.val = (q.1.val : ℤ) + q.2.val)) ↔
      p.1.val + p.2.val = q.1.val + q.2.val := by omega
  simp only [heq]
  split_ifs
  · have h := Complex.re_le_norm ((u p.1 * u p.2) * star (u q.1 * u q.2))
    simpa only [norm_mul, norm_star] using h
  · exact le_rfl

/-- The energy scales quartically. -/
theorem discreteEnergy_scale (N : ℕ) (v : Fin N → ℝ) (c : ℝ) :
    discreteEnergy N (fun j => c * v j) = c ^ 4 * discreteEnergy N v := by
  unfold discreteEnergy
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro p hp
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro q hq
  split_ifs <;> ring

/-- Homogeneous P31-E: no normalization hypothesis is needed. -/
theorem elementary_discreteEnergy_bound_homogeneous (N : ℕ) (v : Fin N → ℝ)
    (hv0 : ∀ j, 0 ≤ v j) :
    discreteEnergy N v ≤ ((811 / 1000 : ℝ) * N + 71 / 300) *
      (∑ j : Fin N, v j ^ 2) ^ 2 := by
  let t := ∑ j : Fin N, v j ^ 2
  have ht : 0 ≤ t := Finset.sum_nonneg (fun j hj => sq_nonneg _)
  by_cases ht0 : t = 0
  · have hvzero : ∀ j, v j = 0 := by
      intro j
      have hle := Finset.single_le_sum (fun k hk => sq_nonneg (v k)) (Finset.mem_univ j)
      change v j ^ 2 ≤ t at hle
      rw [ht0] at hle
      nlinarith [sq_nonneg (v j)]
    simp [discreteEnergy, hvzero]
  · have htp : 0 < t := lt_of_le_of_ne ht (Ne.symm ht0)
    have hs : Real.sqrt t ≠ 0 := (Real.sqrt_pos.mpr htp).ne'
    have hsq : (Real.sqrt t) ^ 2 = t := Real.sq_sqrt ht
    let w : Fin N → ℝ := fun j => (Real.sqrt t)⁻¹ * v j
    have hw0 : ∀ j, 0 ≤ w j := fun j => mul_nonneg (inv_nonneg.mpr (Real.sqrt_nonneg _)) (hv0 j)
    have hw : (∑ j : Fin N, w j ^ 2) = 1 := by
      simp only [w, mul_pow, ← Finset.mul_sum, inv_pow, hsq]
      exact inv_mul_cancel₀ ht0
    have h := elementary_discreteEnergy_bound N w hw0 hw
    rw [discreteEnergy_scale] at h
    have hinv : (Real.sqrt t)⁻¹ ^ 4 = (t ^ 2)⁻¹ := by
      rw [show (4 : ℕ) = 2 * 2 by rfl, pow_mul, inv_pow, hsq, inv_pow]
    rw [hinv] at h
    have hmul := mul_le_mul_of_nonneg_left h (sq_nonneg t)
    have hfinal : discreteEnergy N v ≤ t ^ 2 * ((811 / 1000 : ℝ) * N + 71 / 300) := by
      simpa only [← mul_assoc, mul_inv_cancel₀ (pow_ne_zero 2 ht0), one_mul] using hmul
    simpa only [t, mul_comm] using hfinal

/-- The elementary analytic Nikolskii constant, discharging T3's only
analytic inequality hypothesis without Beckner. -/
theorem elementary_analyticNikolskii (L : ℕ) :
    AnalyticNikolskii L ((811 / 1000 : ℝ) * (L + 1) + 71 / 300) := by
  intro u
  have h := (circleMean_analytic_four_le_energy L u).trans
    (elementary_discreteEnergy_bound_homogeneous (L + 1) (fun j => ‖u j‖) (fun j => norm_nonneg _))
  rw [circleMean_analytic_sq]
  simpa only [Nat.cast_add, Nat.cast_one] using h

end ChowlaCosine.P31
