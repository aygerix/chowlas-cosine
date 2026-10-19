import ChowlaCosine.P34.Moments

open Real MeasureTheory
open scoped BigOperators

namespace ChowlaCosine.P34

open P31

theorem re_character_mem_trigBand {n j : ℕ} (hj : j ≤ n) (b : ℂ) :
    (fun x : ℝ => ((b * circleCharacter (j : ℤ) x).re : ℂ)) ∈ trigBand n := by
  have hp := (trigBand n).smul_mem (b / 2)
    (character_mem_trigBand (L := n) (k := (j : ℤ)) (by
      simpa using (show (j : ℤ) ≤ n by exact_mod_cast hj)))
  have hn := (trigBand n).smul_mem (star b / 2)
    (character_mem_trigBand (L := n) (k := -(j : ℤ)) (by
      simpa using (show (j : ℤ) ≤ n by exact_mod_cast hj)))
  convert (trigBand n).add_mem hp hn using 1
  funext x
  rw [Complex.re_eq_add_conj]
  simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul]
  rw [← Complex.star_def, star_mul, circleCharacter_star]
  ring

theorem trigSum_add_mem_trigBand (A : Finset ℕ) (b : ℕ → ℂ) (n : ℕ) (M : ℝ)
    (hn : ∀ j ∈ A, j ≤ n) :
    (fun x : ℝ => (trigSum A b x + M : ℂ)) ∈ trigBand n := by
  have hs : (∑ j ∈ A, fun x : ℝ => ((b j * circleCharacter (j : ℤ) x).re : ℂ)) ∈
      trigBand n := by
    apply Submodule.sum_mem
    intro j hj
    exact re_character_mem_trigBand (hn j hj) (b j)
  convert (trigBand n).add_mem hs (const_mem_trigBand n (M : ℂ)) using 1
  funext x
  simp [trigSum, Complex.ofReal_sum, Finset.sum_apply]

/-- P34-main, exact window energy, for arbitrary finite complex coefficients.
The all-real lower bound and the analytic hypotheses are explicit. -/
theorem p34_main (w n : ℕ) (A : Finset ℕ) (b : ℕ → ℂ) (M C : ℝ)
    (hA : ∀ j ∈ A, 0 < j) (hn : ∀ j ∈ A, j ≤ n)
    (hM : ∀ x : ℝ, -M ≤ trigSum A b x)
    (hFR : FejerRiesz (n + w)) (hnik : AnalyticNikolskii (n + w) C) :
    windowMass w * (M ^ 2 + energy A b / 2) ≤
      C * (M ^ 2 + windowEnergy w A b / 2) := by
  have hbound : ∀ y : ℝ,
      circleMean (fun x => (fejerKernel w (x - y) * (trigSum A b x + M)) ^ 2) ≤
        C * circleMean (fun x => fejerKernel w (x - y) * (trigSum A b x + M)) ^ 2 := by
    intro y
    obtain ⟨u, hu⟩ := hFR (fun x => fejerKernel w (x - y) * (trigSum A b x + M))
      (by
        have hd := trigBand_mul (fejer_shift_mem_trigBand w y)
          (trigSum_add_mem_trigBand A b n M hn)
        rw [Nat.add_comm] at hd
        convert hd using 1
        funext x
        simp only [Pi.mul_apply, Complex.ofReal_mul, Complex.ofReal_add])
      (fun x => mul_nonneg (fejerKernel_nonneg w (x - y)) (by linarith [hM x]))
    simpa only [hu, ← pow_mul] using hnik u
  have h := averaged_window_bound C (continuous_fejerKernel w)
    ((continuous_trigSum A b).add continuous_const) (fejerKernel_periodic w) hbound
  simp only [Pi.add_apply] at h
  rwa [circleMean_fejerKernel_sq, circleMean_trigSum_add_sq A b M hA,
    circleMean_window_mean_sq w A b M hA] at h

theorem nikolskii_constant_one_le (L : ℕ) (C : ℝ)
    (hFR : FejerRiesz L) (hnik : AnalyticNikolskii L C) : 1 ≤ C := by
  obtain ⟨u, hu⟩ := hFR (fun _ => 1) (const_mem_trigBand L 1) (by intro x; norm_num)
  have h := hnik u
  have hfour : (fun x => ‖analyticValue u x‖ ^ 4) = fun _ => (1 : ℝ) := by
    funext x
    rw [show (4 : ℕ) = 2 * 2 by rfl, pow_mul, ← hu x]
    norm_num
  simp_rw [← hu] at h
  simpa only [hfour, circleMean_const, one_pow, mul_one] using h

theorem windowEnergy_le (w : ℕ) (A : Finset ℕ) (b : ℕ → ℂ)
    (hA : ∀ j ∈ A, 0 < j) (hb : ∀ j ∈ A, ‖b j‖ ^ 2 ≤ 1) :
    windowEnergy w A b ≤ ∑ j ∈ windowFreq w, kappa w j ^ 2 := by
  have hle : windowEnergy w A b ≤ P31.windowEnergy w A := by
    apply Finset.sum_le_sum
    intro j hj
    simpa using mul_le_mul_of_nonneg_left (hb j hj) (sq_nonneg (kappa w j))
  have h := two_windowEnergy_le w A hA
  unfold windowMass at h
  linarith

/-- P34-main with the coefficient bound, without any restriction on phases. -/
theorem p34_main_bounded (w n : ℕ) (A : Finset ℕ) (b : ℕ → ℂ) (M C : ℝ)
    (hA : ∀ j ∈ A, 0 < j) (hn : ∀ j ∈ A, j ≤ n)
    (hb : ∀ j ∈ A, ‖b j‖ ^ 2 ≤ 1) (hM : ∀ x : ℝ, -M ≤ trigSum A b x)
    (hFR : FejerRiesz (n + w)) (hnik : AnalyticNikolskii (n + w) C) :
    windowMass w * (M ^ 2 + energy A b / 2) ≤
      C * (M ^ 2 + (∑ j ∈ windowFreq w, kappa w j ^ 2) / 2) := by
  have hC : 0 ≤ C := le_trans (by norm_num) (nikolskii_constant_one_le _ C hFR hnik)
  exact (p34_main w n A b M C hA hn hM hFR hnik).trans
    (mul_le_mul_of_nonneg_left (by linarith [windowEnergy_le w A b hA hb]) hC)

/-- P34 with both analytic dependencies discharged by the P31 proofs. -/
theorem p34_elementary (w n : ℕ) (A : Finset ℕ) (b : ℕ → ℂ) (M : ℝ)
    (hA : ∀ j ∈ A, 0 < j) (hn : ∀ j ∈ A, j ≤ n)
    (hb : ∀ j ∈ A, ‖b j‖ ^ 2 ≤ 1) (hM : ∀ x : ℝ, -M ≤ trigSum A b x) :
    windowMass w * (M ^ 2 + energy A b / 2) ≤
      elementaryC (n + w) * (M ^ 2 + (windowMass w - 1) / 4) := by
  have h := p34_main_bounded w n A b M (elementaryC (n + w)) hA hn hb hM
    (finite_fejerRiesz _) (elementary_analyticNikolskii _)
  unfold windowMass at h ⊢
  convert h using 1
  ring

theorem nonneg_of_trigSum_ge (A : Finset ℕ) (b : ℕ → ℂ) (M : ℝ)
    (hA : ∀ j ∈ A, 0 < j) (hM : ∀ x : ℝ, -M ≤ trigSum A b x) : 0 ≤ M := by
  have h := circleMean_mono (f := fun _ => -M) continuous_const
    (continuous_trigSum A b) hM
  rw [circleMean_const, circleMean_trigSum A b hA] at h
  linarith

end ChowlaCosine.P34
