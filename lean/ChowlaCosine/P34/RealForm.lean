import ChowlaCosine.P34.Corollaries

open Real MeasureTheory
open scoped BigOperators

namespace ChowlaCosine.P34

open P31

/-- Cosine/sine coordinates, with the sign convention b = a - i c. -/
def coefficients (a c : ℕ → ℝ) (j : ℕ) : ℂ := ⟨a j, -c j⟩

noncomputable def realTrigSum (n : ℕ) (a c : ℕ → ℝ) (x : ℝ) : ℝ :=
  ∑ j ∈ windowFreq n, (a j * Real.cos ((j : ℝ) * x) + c j * Real.sin ((j : ℝ) * x))

noncomputable def realEnergy (n : ℕ) (a c : ℕ → ℝ) : ℝ :=
  ∑ j ∈ windowFreq n, (a j ^ 2 + c j ^ 2)

theorem coefficients_norm_sq (a c : ℕ → ℝ) (j : ℕ) :
    ‖coefficients a c j‖ ^ 2 = a j ^ 2 + c j ^ 2 := by
  rw [Complex.sq_norm, Complex.normSq_apply]
  simp [coefficients]
  ring

theorem trigSum_coefficients (n : ℕ) (a c : ℕ → ℝ) (x : ℝ) :
    trigSum (windowFreq n) (coefficients a c) x = realTrigSum n a c x := by
  unfold trigSum realTrigSum
  apply Finset.sum_congr rfl
  intro j hj
  simp [Complex.mul_re, coefficients, circleCharacter_re, circleCharacter_im]

theorem energy_coefficients (n : ℕ) (a c : ℕ → ℝ) :
    energy (windowFreq n) (coefficients a c) = realEnergy n a c := by
  simp [energy, realEnergy, coefficients_norm_sq]

theorem windowEnergy_interval (w n : ℕ) (b : ℕ → ℂ) :
    windowEnergy w (windowFreq n) b =
      ∑ j ∈ windowFreq (min w n), kappa w j ^ 2 * ‖b j‖ ^ 2 := by
  symm
  apply Finset.sum_subset
  · intro j hj
    simp only [windowFreq, Finset.mem_Icc, le_min_iff] at hj ⊢
    exact ⟨hj.1, hj.2.2⟩
  · intro j hj hnot
    have hjw : w < j := by
      simp only [windowFreq, Finset.mem_Icc, le_min_iff] at hj hnot
      omega
    simp [kappa_eq_zero hjw]

/-- P34-main in the exact real cosine/sine coordinates of the brief. -/
theorem p34_main_real (w n : ℕ) (a c : ℕ → ℝ) (M C : ℝ)
    (hM : ∀ x : ℝ, -M ≤ realTrigSum n a c x)
    (hFR : FejerRiesz (n + w)) (hnik : AnalyticNikolskii (n + w) C) :
    windowMass w * (M ^ 2 + realEnergy n a c / 2) ≤
      C * (M ^ 2 + (∑ j ∈ windowFreq (min w n),
        kappa w j ^ 2 * (a j ^ 2 + c j ^ 2)) / 2) := by
  have h := p34_main w n (windowFreq n) (coefficients a c) M C (windowFreq_pos n)
    (fun j hj => (Finset.mem_Icc.mp hj).2)
    (by simpa only [trigSum_coefficients] using hM) hFR hnik
  simpa only [energy_coefficients, windowEnergy_interval, coefficients_norm_sq] using h

theorem p34_main_real_bounded (w n : ℕ) (a c : ℕ → ℝ) (M C : ℝ)
    (hb : ∀ j ∈ windowFreq n, a j ^ 2 + c j ^ 2 ≤ 1)
    (hM : ∀ x : ℝ, -M ≤ realTrigSum n a c x)
    (hFR : FejerRiesz (n + w)) (hnik : AnalyticNikolskii (n + w) C) :
    windowMass w * (M ^ 2 + realEnergy n a c / 2) ≤
      C * (M ^ 2 + (∑ j ∈ windowFreq w, kappa w j ^ 2) / 2) := by
  have h := p34_main_bounded w n (windowFreq n) (coefficients a c) M C (windowFreq_pos n)
    (fun j hj => (Finset.mem_Icc.mp hj).2)
    (by simpa only [coefficients_norm_sq] using hb)
    (by simpa only [trigSum_coefficients] using hM) hFR hnik
  simpa only [energy_coefficients] using h

/-- P34-A in real coordinates, with no restriction on phases. -/
theorem p34_A_real (n : ℕ) (hn : 1 ≤ n) (a c : ℕ → ℝ) (M : ℝ)
    (hb : ∀ j ∈ windowFreq n, a j ^ 2 + c j ^ 2 = 1)
    (hM : ∀ x : ℝ, -M ≤ realTrigSum n a c x) : Real.sqrt n / 4 ≤ M := by
  apply p34_A n hn (coefficients a c) M
  · simpa only [coefficients_norm_sq] using hb
  · simpa only [trigSum_coefficients] using hM

noncomputable def phaseCoefficients (θ : ℕ → ℝ) (j : ℕ) : ℂ :=
  Complex.exp (-(θ j : ℂ) * Complex.I)

theorem phaseCoefficients_norm_sq (θ : ℕ → ℝ) (j : ℕ) :
    ‖phaseCoefficients θ j‖ ^ 2 = 1 := by
  simp [phaseCoefficients, Complex.norm_exp]

theorem trigSum_phase (n : ℕ) (θ : ℕ → ℝ) (x : ℝ) :
    trigSum (windowFreq n) (phaseCoefficients θ) x =
      ∑ j ∈ windowFreq n, Real.cos ((j : ℝ) * x - θ j) := by
  unfold trigSum
  apply Finset.sum_congr rfl
  intro j hj
  unfold phaseCoefficients circleCharacter
  simp only [Int.cast_natCast]
  rw [← Complex.exp_add]
  rw [show -(θ j : ℂ) * Complex.I + (j : ℂ) * (x : ℂ) * Complex.I =
    (((j : ℝ) * x - θ j : ℝ) : ℂ) * Complex.I by push_cast; ring,
    Complex.exp_ofReal_mul_I_re]

/-- P34-A explicitly quantified over every phase vector and every n ≥ 1. -/
theorem p34_A_phases (n : ℕ) (hn : 1 ≤ n) (θ : ℕ → ℝ) (M : ℝ)
    (hM : ∀ x : ℝ, -M ≤ ∑ j ∈ windowFreq n, Real.cos ((j : ℝ) * x - θ j)) :
    Real.sqrt n / 4 ≤ M := by
  apply p34_A n hn (phaseCoefficients θ) M (fun j hj => phaseCoefficients_norm_sq θ j)
  simpa only [trigSum_phase] using hM

theorem p34_C_real (n : ℕ) (a c : ℕ → ℝ) (M : ℝ)
    (hb : ∀ j ∈ windowFreq n, a j ^ 2 + c j ^ 2 ≤ 1)
    (hdensity : (41 / 100 : ℝ) * n ≤ realEnergy n a c)
    (hM : ∀ x : ℝ, -M ≤ realTrigSum n a c x) : Real.sqrt n / 1000 ≤ M := by
  apply p34_C n (coefficients a c) M
  · simpa only [coefficients_norm_sq] using hb
  · simpa only [energy_coefficients] using hdensity
  · simpa only [trigSum_coefficients] using hM

end ChowlaCosine.P34
