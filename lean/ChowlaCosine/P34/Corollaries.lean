import ChowlaCosine.P34.Main

open Real MeasureTheory
open scoped BigOperators

namespace ChowlaCosine.P34

open P31

theorem energy_eq_card (A : Finset ℕ) (b : ℕ → ℂ)
    (hb : ∀ j ∈ A, ‖b j‖ ^ 2 = 1) : energy A b = A.card := by
  unfold energy
  rw [Finset.sum_congr rfl hb]
  simp

theorem windowMass_le_succ (w : ℕ) : windowMass w ≤ (w : ℝ) + 1 := by
  rw [windowMass_eq]
  have hw : (0 : ℝ) < w + 1 := by positivity
  apply (mul_le_mul_iff_left₀ (show (0 : ℝ) < 3 * (w + 1) by positivity)).mp
  field_simp
  nlinarith [sq_nonneg (w : ℝ)]

private theorem unit_window_arithmetic (n : ℕ) (hn : 1 ≤ n) :
    let W := windowMass (n / 2)
    let C := elementaryC (n + n / 2)
    0 ≤ C - W ∧ C * (n / 16 + (W - 1) / 4) < W * (n / 16 + (n : ℝ) / 2) := by
  dsimp only
  have hw := windowMass_le_succ (n / 2)
  have hhalf : (2 : ℝ) * (n / 2 : ℕ) ≤ n := by
    exact_mod_cast (show 2 * (n / 2) ≤ n by omega)
  have hnr : (1 : ℝ) ≤ n := by exact_mod_cast hn
  constructor
  · unfold elementaryC
    push_cast
    linarith
  · let w := n / 2
    have hn_cases : n = 2 * w ∨ n = 2 * w + 1 := by omega
    have hw0 : (0 : ℝ) ≤ w := Nat.cast_nonneg _
    have hw1 : (0 : ℝ) < w + 1 := by positivity
    have hw3 : (0 : ℝ) ≤ (w : ℝ) ^ 3 := by positivity
    change elementaryC (n + w) * ((n : ℝ) / 16 + (windowMass w - 1) / 4) <
      windowMass w * ((n : ℝ) / 16 + (n : ℝ) / 2)
    rcases hn_cases with hn_even | hn_odd
    · rw [hn_even, windowMass_eq]
      have hwpos : (1 : ℝ) ≤ w := by exact_mod_cast (show 1 ≤ w by omega)
      unfold elementaryC
      push_cast
      apply (mul_lt_mul_iff_right₀ hw1).mp
      field_simp
      nlinarith [sq_nonneg (w : ℝ)]
    · rw [hn_odd, windowMass_eq]
      unfold elementaryC
      push_cast
      apply (mul_lt_mul_iff_right₀ hw1).mp
      field_simp
      nlinarith [sq_nonneg (w : ℝ)]

/-- P34-A: unit amplitudes on every frequency 1,...,n, all n ≥ 1.
No condition is imposed on the arguments of the complex coefficients. -/
theorem p34_A (n : ℕ) (hn : 1 ≤ n) (b : ℕ → ℂ) (M : ℝ)
    (hb : ∀ j ∈ windowFreq n, ‖b j‖ ^ 2 = 1)
    (hM : ∀ x : ℝ, -M ≤ trigSum (windowFreq n) b x) :
    Real.sqrt n / 4 ≤ M := by
  have hM0 := nonneg_of_trigSum_ge _ b M (windowFreq_pos n) hM
  have h := p34_elementary (n / 2) n (windowFreq n) b M (windowFreq_pos n)
    (fun j hj => (Finset.mem_Icc.mp hj).2) (fun j hj => (hb j hj).le) hM
  rw [energy_eq_card _ b hb] at h
  have hcard : (windowFreq n).card = n := by simp [windowFreq]
  rw [hcard] at h
  obtain ⟨hCW, hgap⟩ := unit_window_arithmetic n hn
  have hsq : (n : ℝ) / 16 ≤ M ^ 2 := by
    by_contra hnot
    have hprod := mul_le_mul_of_nonneg_left (le_of_lt (lt_of_not_ge hnot)) hCW
    nlinarith [h, hgap, hprod]
  apply (div_le_iff₀ (by norm_num : (0 : ℝ) < 4)).mpr
  apply Real.sqrt_le_iff.mpr
  exact ⟨by positivity, by nlinarith⟩

theorem circleCharacter_norm (k : ℤ) (x : ℝ) : ‖circleCharacter k x‖ = 1 := by
  simp [circleCharacter, Complex.norm_exp]

theorem trigSum_le_card (A : Finset ℕ) (b : ℕ → ℂ)
    (hb : ∀ j ∈ A, ‖b j‖ ^ 2 ≤ 1) (x : ℝ) : trigSum A b x ≤ A.card := by
  have h : trigSum A b x ≤ ∑ _j ∈ A, (1 : ℝ) := by
    apply Finset.sum_le_sum
    intro j hj
    have hnorm : ‖b j‖ ≤ 1 := by nlinarith [hb j hj, norm_nonneg (b j)]
    exact (Complex.re_le_norm _).trans (by simpa [norm_mul, circleCharacter_norm] using hnorm)
  simpa using h

/-- A finite-size bound independent of phases, obtained by integrating
`g² ≤ (M + |A|)g` for the nonnegative polynomial `g = M + T`. -/
theorem energy_le_two_card_mul (A : Finset ℕ) (b : ℕ → ℂ) (M : ℝ)
    (hA : ∀ j ∈ A, 0 < j) (hb : ∀ j ∈ A, ‖b j‖ ^ 2 ≤ 1)
    (hM : ∀ x : ℝ, -M ≤ trigSum A b x) : energy A b ≤ 2 * A.card * M := by
  have hm := circleMean_mono
    (f := fun x => (trigSum A b x + M) ^ 2)
    (g := fun x => (M + A.card) * (trigSum A b x + M))
    (by fun_prop) (by fun_prop) (by
      intro x
      have hpos : 0 ≤ trigSum A b x + M := by linarith [hM x]
      have hle := mul_le_mul_of_nonneg_right (trigSum_le_card A b hb x) hpos
      nlinarith)
  rw [circleMean_trigSum_add_sq A b M hA, circleMean_const_mul,
    circleMean_add (continuous_trigSum A b) continuous_const,
    circleMean_trigSum A b hA, circleMean_const] at hm
  nlinarith

private theorem dense_window_arithmetic (n : ℕ) (hn : 2000 ≤ n) :
    elementaryC (n + n / 200) ≤ (102 / 125 : ℝ) * n ∧
      (n : ℝ) / 300 ≤ windowMass (n / 200) := by
  have hw : (n / 200 : ℕ) * 200 ≤ n := Nat.div_mul_le_self _ _
  have hwr : ((n / 200 : ℕ) : ℝ) * 200 ≤ n := by exact_mod_cast hw
  have hnr : (2000 : ℝ) ≤ n := by exact_mod_cast hn
  constructor
  · unfold elementaryC
    push_cast
    nlinarith
  · have hw' : n ≤ 200 * (n / 200 + 1) := by omega
    have hwr' : (n : ℝ) ≤ 200 * (((n / 200 : ℕ) : ℝ) + 1) := by exact_mod_cast hw'
    rw [windowMass_eq]
    have hnonneg : (0 : ℝ) ≤ 1 / (3 * (((n / 200 : ℕ) : ℝ) + 1)) := by positivity
    nlinarith

/-- P34-C, including every finite size; the bound is in sqrt(n). -/
theorem p34_C (n : ℕ) (b : ℕ → ℂ) (M : ℝ)
    (hb : ∀ j ∈ windowFreq n, ‖b j‖ ^ 2 ≤ 1)
    (hdensity : (41 / 100 : ℝ) * n ≤ energy (windowFreq n) b)
    (hM : ∀ x : ℝ, -M ≤ trigSum (windowFreq n) b x) :
    Real.sqrt n / 1000 ≤ M := by
  have hM0 := nonneg_of_trigSum_ge _ b M (windowFreq_pos n) hM
  have hsq : (n : ℝ) ≤ (M * 1000) ^ 2 := by
    by_cases hn : 2000 ≤ n
    · let w := n / 200
      let W := windowMass w
      let C := elementaryC (n + w)
      have hnp : (0 : ℝ) < n := by exact_mod_cast (show 0 < n by omega)
      have hW : 0 < W := windowMass_pos w
      have hC : 0 ≤ C := by unfold C elementaryC; positivity
      obtain ⟨hCup, hWlow⟩ := dense_window_arithmetic n hn
      have hmain := p34_elementary w n (windowFreq n) b M (windowFreq_pos n)
        (fun j hj => (Finset.mem_Icc.mp hj).2) hb hM
      change W * (M ^ 2 + energy (windowFreq n) b / 2) ≤ C * (M ^ 2 + (W - 1) / 4) at hmain
      have hWsq : 0 ≤ W * M ^ 2 := mul_nonneg hW.le (sq_nonneg M)
      have hineq : W * (energy (windowFreq n) b - C / 2) ≤ 2 * C * M ^ 2 := by
        nlinarith
      have hgap : (n : ℝ) / 500 ≤ energy (windowFreq n) b - C / 2 := by
        change C ≤ (102 / 125 : ℝ) * n at hCup
        linarith
      have hgain := (mul_le_mul_of_nonneg_left hgap hW.le).trans hineq
      have hlo := mul_le_mul_of_nonneg_right hWlow (by positivity : 0 ≤ (n : ℝ) / 500)
      have hhi := mul_le_mul_of_nonneg_right hCup (by positivity : 0 ≤ 2 * M ^ 2)
      have hscaled : (n : ℝ) * ((n : ℝ) / 150000) ≤
          (n : ℝ) * ((204 / 125 : ℝ) * M ^ 2) := by
        change (n : ℝ) / 300 ≤ W at hWlow
        change C ≤ (102 / 125 : ℝ) * n at hCup
        nlinarith [hgain, hlo, hhi]
      have hcancel := (mul_le_mul_iff_right₀ hnp).mp hscaled
      nlinarith
    · by_cases hn0 : n = 0
      · simp only [hn0, Nat.cast_zero]
        positivity
      · have he := energy_le_two_card_mul (windowFreq n) b M (windowFreq_pos n) hb hM
        have hc : (windowFreq n).card = n := by simp [windowFreq]
        rw [hc] at he
        have hnp : (0 : ℝ) < n := by exact_mod_cast (Nat.pos_of_ne_zero hn0)
        have hlow : (41 / 200 : ℝ) ≤ M := by nlinarith [he, hdensity]
        have hnsmall : (n : ℝ) ≤ 2000 := by exact_mod_cast (show n ≤ 2000 by omega)
        nlinarith [sq_nonneg (M - 41 / 200)]
  apply (div_le_iff₀ (by norm_num : (0 : ℝ) < 1000)).mpr
  apply Real.sqrt_le_iff.mpr
  exact ⟨by positivity, hsq⟩

end ChowlaCosine.P34
