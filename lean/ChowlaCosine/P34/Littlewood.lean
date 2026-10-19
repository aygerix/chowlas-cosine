import ChowlaCosine.P34.RealForm

open Real
open scoped BigOperators

namespace ChowlaCosine.P34

open P31

theorem trigSum_periodic (A : Finset ℕ) (b : ℕ → ℂ) :
    Function.Periodic (trigSum A b) (2 * π) := by
  intro x
  unfold trigSum
  apply Finset.sum_congr rfl
  intro j hj
  simp only [Complex.mul_re, circleCharacter_re, circleCharacter_im, Int.cast_natCast,
    mul_add, Real.cos_add_nat_mul_two_pi, Real.sin_add_nat_mul_two_pi]

theorem trigSum_exists_min (A : Finset ℕ) (b : ℕ → ℂ) :
    ∃ x : ℝ, ∀ y : ℝ, trigSum A b x ≤ trigSum A b y := by
  obtain ⟨x, hx, hmin⟩ := isCompact_Icc.exists_isMinOn
    (s := Set.Icc (0 : ℝ) (2 * π)) (f := trigSum A b)
    (by exact ⟨0, by constructor <;> positivity⟩) (continuous_trigSum A b).continuousOn
  refine ⟨x, fun y => ?_⟩
  obtain ⟨z, hz, he⟩ := (trigSum_periodic A b).exists_mem_Ico₀ (by positivity) y
  rw [he]
  exact hmin ⟨hz.1, hz.2.le⟩

theorem trigSum_neg (A : Finset ℕ) (b : ℕ → ℂ) (x : ℝ) :
    trigSum A (fun j => -b j) x = -trigSum A b x := by
  simp [trigSum]

/-- The actual negative excursion exists, including equality at the minimum. -/
theorem p34_A_exists_le (n : ℕ) (hn : 1 ≤ n) (b : ℕ → ℂ)
    (hb : ∀ j ∈ windowFreq n, ‖b j‖ ^ 2 = 1) :
    ∃ x : ℝ, trigSum (windowFreq n) b x ≤ -Real.sqrt n / 4 := by
  obtain ⟨x, hx⟩ := trigSum_exists_min (windowFreq n) b
  have h := p34_A n hn b (-trigSum (windowFreq n) b x) hb (by
    intro y
    simpa using hx y)
  exact ⟨x, by linarith⟩

theorem p34_A_exists_ge (n : ℕ) (hn : 1 ≤ n) (b : ℕ → ℂ)
    (hb : ∀ j ∈ windowFreq n, ‖b j‖ ^ 2 = 1) :
    ∃ x : ℝ, Real.sqrt n / 4 ≤ trigSum (windowFreq n) b x := by
  obtain ⟨x, hx⟩ := p34_A_exists_le n hn (fun j => -b j) (by simpa using hb)
  rw [trigSum_neg] at hx
  exact ⟨x, by linarith⟩

noncomputable def littlewoodSum (n : ℕ) (ε : ℕ → ℝ) (x : ℝ) : ℝ :=
  ∑ j ∈ Finset.range (n + 1), ε j * Real.cos ((j : ℝ) * x)

theorem littlewoodSum_eq (n : ℕ) (ε : ℕ → ℝ) (x : ℝ) :
    littlewoodSum n ε x = ε 0 + trigSum (windowFreq n) (fun j => (ε j : ℂ)) x := by
  have hs : Finset.range (n + 1) = insert 0 (windowFreq n) := by
    ext j
    simp only [Finset.mem_range, Finset.mem_insert, windowFreq, Finset.mem_Icc]
    omega
  have hz : (0 : ℕ) ∉ windowFreq n := by simp [windowFreq]
  simp only [littlewoodSum, hs, Finset.sum_insert hz, Nat.cast_zero, zero_mul,
    Real.cos_zero, mul_one, trigSum, Complex.mul_re, Complex.ofReal_re,
    Complex.ofReal_im, zero_mul, sub_zero, circleCharacter_re, Int.cast_natCast]

/-- P34-B: both one-sided bounds for every ±1 Littlewood cosine polynomial,
including the constant coefficient and every n ≥ 1. -/
theorem p34_B (n : ℕ) (hn : 1 ≤ n) (ε : ℕ → ℝ)
    (hε : ∀ j : ℕ, ε j = -1 ∨ ε j = 1) :
    (∃ x : ℝ, littlewoodSum n ε x ≤ 1 - Real.sqrt n / 4) ∧
      (∃ x : ℝ, Real.sqrt n / 4 - 1 ≤ littlewoodSum n ε x) := by
  have hb : ∀ j ∈ windowFreq n, ‖(ε j : ℂ)‖ ^ 2 = 1 := by
    intro j hj
    rcases hε j with hj | hj <;> simp [hj]
  have hzero_up : ε 0 ≤ 1 := by rcases hε 0 with h | h <;> linarith
  have hzero_low : -1 ≤ ε 0 := by rcases hε 0 with h | h <;> linarith
  constructor
  · obtain ⟨x, hx⟩ := p34_A_exists_le n hn (fun j => (ε j : ℂ)) hb
    refine ⟨x, ?_⟩
    rw [littlewoodSum_eq]
    linarith
  · obtain ⟨x, hx⟩ := p34_A_exists_ge n hn (fun j => (ε j : ℂ)) hb
    refine ⟨x, ?_⟩
    rw [littlewoodSum_eq]
    linarith

end ChowlaCosine.P34
