import ChowlaCosine.P31.Main
import ChowlaCosine.Star
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

noncomputable def elementaryC (L : ℕ) : ℝ := (811 / 1000 : ℝ) * (L + 1) + 71 / 300

theorem p31_elementary (w : ℕ) (A : Finset ℕ) (M : ℝ)
    (hA : ∀ a ∈ A, 0 < a) (hM : ∀ x : ℝ, -M ≤ cosSum A x) :
    windowMass w * ((A.card : ℝ) / 2 + M ^ 2) ≤
      elementaryC (A.sup id + w) * (M ^ 2 + windowEnergy w A / 2) :=
  p31_main w A M _ hA hM (elementary_analyticNikolskii _)

theorem windowEnergy_nonneg (w : ℕ) (A : Finset ℕ) : 0 ≤ windowEnergy w A :=
  Finset.sum_nonneg (fun a ha => sq_nonneg _)

/-- The positive-frequency set occupies at most the positive half of W. -/
theorem two_windowEnergy_le (w : ℕ) (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a) :
    2 * windowEnergy w A ≤ windowMass w - 1 := by
  let B := A.filter (fun a => a ≤ w)
  have hs : windowEnergy w A = ∑ a ∈ B, kappa w a ^ 2 := by
    unfold windowEnergy
    symm
    apply Finset.sum_subset (Finset.filter_subset _ _)
    intro a ha hnot
    have haw : w < a := by simp only [B, Finset.mem_filter, ha, true_and] at hnot; omega
    rw [kappa_eq_zero haw, zero_pow (by decide : (2 : ℕ) ≠ 0)]
  have hsub : B ⊆ windowFreq w := by
    intro a ha
    have ha' := Finset.mem_filter.mp ha
    exact Finset.mem_Icc.mpr ⟨hA a ha'.1, ha'.2⟩
  have hle : (∑ a ∈ B, kappa w a ^ 2) ≤ ∑ a ∈ windowFreq w, kappa w a ^ 2 :=
    Finset.sum_le_sum_of_subset_of_nonneg hsub (fun a ha hnot => sq_nonneg _)
  rw [hs]
  unfold windowMass
  linarith

theorem card_le_max_frequency (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a) :
    A.card ≤ A.sup id := by
  have hsub : A ⊆ Finset.Icc 1 (A.sup id) := by
    intro a ha
    exact Finset.mem_Icc.mpr ⟨hA a ha, Finset.le_sup (f := id) ha⟩
  have h := Finset.card_le_card hsub
  simpa using h

/-- The uniform finite-size fallback, from the already checked singleton star bound. -/
theorem half_le_of_nonempty (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a) (hne : A.Nonempty)
    (M : ℝ) (hM : ∀ x : ℝ, -M ≤ cosSum A x) : (1 / 2 : ℝ) ≤ M := by
  obtain ⟨a, ha⟩ := hne
  have hI : ∀ i ∈ ({(a : ℤ)} : Finset ℤ), i.natAbs ∈ A := by
    intro i hi
    simp only [Finset.mem_singleton] at hi
    subst i
    simpa using ha
  have hind : ∀ i ∈ ({(a : ℤ)} : Finset ℤ), ∀ j ∈ ({(a : ℤ)} : Finset ℤ),
      i ≠ j → (i - j).natAbs ∉ A := by
    intro i hi j hj hij
    simp only [Finset.mem_singleton] at hi hj
    exact False.elim (hij (hi.trans hj.symm))
  have h := star_bound A hA M hM {(a : ℤ)} hI hind
  simpa using h

private theorem elementaryC_window_upper (X : ℕ) (hX : 2000 ≤ X) :
    elementaryC (X + X / 200) ≤ (102 / 125 : ℝ) * X := by
  have hw : (X / 200 : ℕ) * 200 ≤ X := Nat.div_mul_le_self _ _
  have hwr : ((X / 200 : ℕ) : ℝ) * 200 ≤ X := by exact_mod_cast hw
  have hXr : (2000 : ℝ) ≤ X := by exact_mod_cast hX
  unfold elementaryC
  push_cast
  nlinarith

private theorem windowMass_floor_lower (X : ℕ) :
    (X : ℝ) / 300 ≤ windowMass (X / 200) := by
  have hw : X ≤ 200 * (X / 200 + 1) := by omega
  have hwr : (X : ℝ) ≤ 200 * (((X / 200 : ℕ) : ℝ) + 1) := by exact_mod_cast hw
  rw [windowMass_eq]
  have hnonneg : (0 : ℝ) ≤ 1 / (3 * (((X / 200 : ℕ) : ℝ) + 1)) := by positivity
  nlinarith

/-- Explicit large-X dense corollary, with ε=1/200 and X₀=2000. -/
theorem dense_large_sq (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a)
    (M : ℝ) (hM : ∀ x : ℝ, -M ≤ cosSum A x)
    (hX : 2000 ≤ A.sup id)
    (hdensity : (41 / 100 : ℝ) * A.sup id ≤ A.card) :
    (A.card : ℝ) / 1000000 ≤ M ^ 2 := by
  let X := A.sup id
  let w := X / 200
  let W := windowMass w
  let C := elementaryC (X + w)
  have hXpos : (0 : ℝ) < X := by have : 2000 ≤ X := hX; exact_mod_cast (by omega : 0 < X)
  have hW : 0 < W := windowMass_pos w
  have hC : 0 ≤ C := by unfold C elementaryC; positivity
  have hCup : C ≤ (102 / 125 : ℝ) * X := elementaryC_window_upper X hX
  have hWlow : (X : ℝ) / 300 ≤ W := windowMass_floor_lower X
  have hcard : (A.card : ℝ) ≤ X := by exact_mod_cast card_le_max_frequency A hA
  have hn : (0 : ℝ) ≤ A.card := Nat.cast_nonneg _
  have hS : windowEnergy w A ≤ W / 2 := by have := two_windowEnergy_le w A hA; linarith
  have hmain := p31_elementary w A M hA hM
  change W * ((A.card : ℝ) / 2 + M ^ 2) ≤ C * (M ^ 2 + windowEnergy w A / 2) at hmain
  have hCS := mul_le_mul_of_nonneg_left hS hC
  have hWsq : 0 ≤ W * M ^ 2 := mul_nonneg hW.le (sq_nonneg M)
  have hineq : W * ((A.card : ℝ) - C / 2) ≤ 2 * C * M ^ 2 := by
    nlinarith [hmain, hCS, hWsq]
  have hgap : (A.card : ℝ) / 500 ≤ (A.card : ℝ) - C / 2 := by
    change (41 / 100 : ℝ) * X ≤ A.card at hdensity
    linarith
  have hgain := (mul_le_mul_of_nonneg_left hgap hW.le).trans hineq
  have hlo := mul_le_mul_of_nonneg_right hWlow (div_nonneg hn (by norm_num : (0 : ℝ) ≤ 500))
  have hhi := mul_le_mul_of_nonneg_right hCup (by positivity : 0 ≤ 2 * M ^ 2)
  have hscaled : (X : ℝ) * ((A.card : ℝ) / 150000) ≤
      (X : ℝ) * ((204 / 125 : ℝ) * M ^ 2) := by
    nlinarith [hgain, hlo, hhi]
  have hcancel := (mul_le_mul_iff_right₀ hXpos).mp hscaled
  nlinarith [hcancel]

/-- T4: every finite positive-frequency set of density at least 41/100
satisfies the explicit square-root bound, at all sizes. -/
theorem dense_elementary (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a)
    (M : ℝ) (hM : ∀ x : ℝ, -M ≤ cosSum A x)
    (hdensity : (41 / 100 : ℝ) * A.sup id ≤ A.card) :
    Real.sqrt A.card / 1000 ≤ M := by
  have hM0 := nonneg_of_cosSum_ge A hA M hM
  have hsq : (A.card : ℝ) ≤ (M * 1000) ^ 2 := by
    by_cases hX : 2000 ≤ A.sup id
    · have h := dense_large_sq A hA M hM hX hdensity
      nlinarith
    · by_cases hne : A.Nonempty
      · have hh := half_le_of_nonempty A hA hne M hM
        have hc := card_le_max_frequency A hA
        have hcard : (A.card : ℝ) ≤ 2000 := by exact_mod_cast (by omega : A.card ≤ 2000)
        nlinarith [sq_nonneg (M - 1 / 2)]
      · have he : A = ∅ := Finset.not_nonempty_iff_eq_empty.mp hne
        simp only [he, Finset.card_empty, Nat.cast_zero]
        positivity
  apply (div_le_iff₀ (by norm_num : (0 : ℝ) < 1000)).mpr
  apply Real.sqrt_le_iff.mpr
  exact ⟨by positivity, hsq⟩

end ChowlaCosine.P31

-- BEGIN T4 LIVE AUDIT
#print axioms ChowlaCosine.P31.circleMean_norm_sq_sum
#print axioms ChowlaCosine.P31.circleMean_analytic_sq
#print axioms ChowlaCosine.P31.circleMean_analytic_four_le_energy
#print axioms ChowlaCosine.P31.elementary_discreteEnergy_bound_homogeneous
#print axioms ChowlaCosine.P31.elementary_analyticNikolskii
#print axioms ChowlaCosine.P31.p31_elementary
#print axioms ChowlaCosine.P31.two_windowEnergy_le
#print axioms ChowlaCosine.P31.card_le_max_frequency
#print axioms ChowlaCosine.P31.half_le_of_nonempty
#print axioms ChowlaCosine.P31.dense_large_sq
#print axioms ChowlaCosine.P31.dense_elementary
