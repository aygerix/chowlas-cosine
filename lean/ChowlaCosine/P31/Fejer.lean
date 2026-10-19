import ChowlaCosine.P31.WindowMoments

/-! # Fejér positivity on the entire real line

The proof expands the square of the finite Dirichlet sum. No division by
`sin (x/2)` is used, so the argument also covers its zeros.
-/

open Real
open scoped BigOperators

namespace ChowlaCosine.P31

private noncomputable def triangle (w : ℕ) (x : ℝ) : ℝ :=
  (w + 1) + 2 * ∑ k ∈ windowFreq w, ((w : ℝ) + 1 - k) * Real.cos ((k : ℝ) * x)

private theorem sum_reverse_cos (N : ℕ) (x : ℝ) :
    (∑ j ∈ Finset.range N, Real.cos (((N - j : ℕ) : ℝ) * x)) =
      ∑ k ∈ Finset.Icc 1 N, Real.cos ((k : ℝ) * x) := by
  have href := Finset.sum_range_reflect (fun j => Real.cos (((j + 1 : ℕ) : ℝ) * x)) N
  have hleft : (∑ j ∈ Finset.range N, Real.cos (((N - j : ℕ) : ℝ) * x)) =
      ∑ j ∈ Finset.range N, Real.cos (((N - 1 - j + 1 : ℕ) : ℝ) * x) := by
    apply Finset.sum_congr rfl
    intro j hj
    apply congrArg (fun n : ℕ => Real.cos ((n : ℝ) * x))
    simp only [Finset.mem_range] at hj
    omega
  rw [hleft, href, ← Finset.Ico_add_one_right_eq_Icc, Finset.sum_Ico_eq_sum_range]
  simp only [Nat.add_sub_cancel]
  apply Finset.sum_congr rfl
  intro j hj
  apply congrArg (fun n : ℕ => Real.cos ((n : ℝ) * x))
  omega

private theorem triangle_step (w : ℕ) (x : ℝ) :
    triangle (w + 1) x = triangle w x + 1 +
      2 * ∑ k ∈ Finset.Icc 1 (w + 1), Real.cos ((k : ℝ) * x) := by
  simp only [triangle, windowFreq, Nat.cast_add, Nat.cast_one]
  rw [Finset.sum_Icc_succ_top (by omega : 1 ≤ w + 1),
    Finset.sum_Icc_succ_top (by omega : 1 ≤ w + 1)]
  have hs : (∑ k ∈ Finset.Icc 1 w,
      ((w : ℝ) + 1 + 1 - k) * Real.cos ((k : ℝ) * x)) =
      (∑ k ∈ Finset.Icc 1 w, ((w : ℝ) + 1 - k) * Real.cos ((k : ℝ) * x)) +
        ∑ k ∈ Finset.Icc 1 w, Real.cos ((k : ℝ) * x) := by
    rw [← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl
    intro k hk
    ring
  rw [hs]
  push_cast
  ring

/-- The unnormalized Fejér kernel is exactly a sum of two real squares. -/
theorem fejer_triangle_sq (w : ℕ) (x : ℝ) :
    (∑ j ∈ Finset.range (w + 1), Real.cos ((j : ℝ) * x)) ^ 2 +
      (∑ j ∈ Finset.range (w + 1), Real.sin ((j : ℝ) * x)) ^ 2 =
        (w + 1) * fejerKernel w x := by
  have hid : ∀ N : ℕ,
      (∑ j ∈ Finset.range (N + 1), Real.cos ((j : ℝ) * x)) ^ 2 +
        (∑ j ∈ Finset.range (N + 1), Real.sin ((j : ℝ) * x)) ^ 2 = triangle N x := by
    intro N
    induction N with
    | zero => simp [triangle, windowFreq]
    | succ N ih =>
      rw [Finset.sum_range_succ (fun j : ℕ => Real.cos ((j : ℝ) * x)) (N + 1),
        Finset.sum_range_succ (fun j : ℕ => Real.sin ((j : ℝ) * x)) (N + 1)]
      have hc : (∑ j ∈ Finset.range (N + 1), Real.cos ((j : ℝ) * x)) *
          Real.cos (((N + 1 : ℕ) : ℝ) * x) +
          (∑ j ∈ Finset.range (N + 1), Real.sin ((j : ℝ) * x)) *
          Real.sin (((N + 1 : ℕ) : ℝ) * x) =
          ∑ j ∈ Finset.range (N + 1), Real.cos ((((N + 1 - j : ℕ) : ℝ)) * x) := by
        rw [Finset.sum_mul, Finset.sum_mul, ← Finset.sum_add_distrib]
        apply Finset.sum_congr rfl
        intro j hj
        have hjN : j ≤ N + 1 := by simp only [Finset.mem_range] at hj; omega
        rw [Nat.cast_sub hjN, sub_mul, Real.cos_sub]
        ring
      have ht := Real.cos_sq_add_sin_sq (((N + 1 : ℕ) : ℝ) * x)
      rw [sum_reverse_cos] at hc
      rw [triangle_step]
      nlinarith
  rw [hid]
  unfold triangle fejerKernel weightedCos
  rw [mul_add, mul_one]
  congr 1
  have hs : (∑ k ∈ windowFreq w, ((w : ℝ) + 1 - k) * Real.cos ((k : ℝ) * x)) =
      ((w : ℝ) + 1) * ∑ a ∈ windowFreq w, kappa w a * Real.cos ((a : ℝ) * x) := by
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro k hk
    rw [kappa_of_mem hk]
    have hw : (w : ℝ) + 1 ≠ 0 := by positivity
    field_simp
  rw [hs]
  ring

/-- The Fejér kernel is nonnegative for every real angle, including multiples of `2π`. -/
theorem fejerKernel_nonneg (w : ℕ) (x : ℝ) : 0 ≤ fejerKernel w x := by
  have hs := fejer_triangle_sq w x
  have hw : (0 : ℝ) < w + 1 := by positivity
  nlinarith [sq_nonneg (∑ j ∈ Finset.range (w + 1), Real.cos ((j : ℝ) * x)),
    sq_nonneg (∑ j ∈ Finset.range (w + 1), Real.sin ((j : ℝ) * x))]

/-- The window polynomial is nonnegative under the exact all-real lower bound. -/
theorem window_nonneg (w : ℕ) (A : Finset ℕ) (M : ℝ)
    (hM : ∀ x : ℝ, -M ≤ cosSum A x) (x y : ℝ) :
    0 ≤ fejerKernel w (x - y) * (cosSum A x + M) := by
  exact mul_nonneg (fejerKernel_nonneg w (x - y)) (by linarith [hM x])

private theorem sum_pos_squares (w : ℕ) :
    (∑ k ∈ Finset.Icc 1 w, (k : ℝ) ^ 2) = (w : ℝ) * (w + 1) * (2 * w + 1) / 6 := by
  induction w with
  | zero => simp
  | succ w ih =>
    rw [Finset.sum_Icc_succ_top (by omega : 1 ≤ w + 1), ih]
    push_cast
    ring

private theorem sum_reflected_squares (w : ℕ) :
    (∑ k ∈ Finset.Icc 1 w, ((w : ℝ) + 1 - k) ^ 2) =
      ∑ k ∈ Finset.Icc 1 w, (k : ℝ) ^ 2 := by
  apply Finset.sum_nbij' (fun k => w + 1 - k) (fun k => w + 1 - k)
  · intro k hk
    simp only [Finset.mem_Icc] at hk ⊢
    omega
  · intro k hk
    simp only [Finset.mem_Icc] at hk ⊢
    omega
  · intro k hk
    simp only [Finset.mem_Icc] at hk
    omega
  · intro k hk
    simp only [Finset.mem_Icc] at hk
    omega
  · intro k hk
    have hk' : k ≤ w + 1 := by simp only [Finset.mem_Icc] at hk; omega
    rw [Nat.cast_sub hk', Nat.cast_add, Nat.cast_one]

/-- The exact rational value of `W`, valid also at `w=0`. -/
theorem windowMass_eq (w : ℕ) :
    windowMass w = 2 * ((w : ℝ) + 1) / 3 + 1 / (3 * ((w : ℝ) + 1)) := by
  have hs : (∑ k ∈ windowFreq w, (kappa w k) ^ 2) =
      ((w : ℝ) * (w + 1) * (2 * w + 1) / 6) / ((w : ℝ) + 1) ^ 2 := by
    calc
      _ = ∑ k ∈ Finset.Icc 1 w, ((w : ℝ) + 1 - k) ^ 2 / ((w : ℝ) + 1) ^ 2 := by
        apply Finset.sum_congr rfl
        intro k hk
        rw [kappa_of_mem hk]
        have hw : (w : ℝ) + 1 ≠ 0 := by positivity
        field_simp
      _ = _ := by rw [← Finset.sum_div, sum_reflected_squares, sum_pos_squares]
  unfold windowMass
  rw [hs]
  have hw : (w : ℝ) + 1 ≠ 0 := by positivity
  field_simp
  ring

theorem windowMass_pos (w : ℕ) : 0 < windowMass w := by
  rw [windowMass_eq]
  positivity

end ChowlaCosine.P31
