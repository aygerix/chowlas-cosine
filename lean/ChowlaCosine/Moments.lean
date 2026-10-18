import ChowlaCosine.Basic

/-!
# Mean zero and Parseval for `f_A`

For a finite `A ⊆ ℕ` with all elements positive:

* `∫_0^{2π} f_A(x) dx = 0`;
* `∫_0^{2π} f_A(x)² dx = π |A|`, i.e. the normalized mean square
  `(1/2π) ∫_0^{2π} f_A² = |A| / 2`.

Distinctness of the frequencies is automatic (`A` is a `Finset`); positivity is required
(for `A = {0}` both identities fail).
-/

open Real

namespace ChowlaCosine

theorem intervalIntegrable_cos_mul (c : ℝ) (a b : ℝ) :
    IntervalIntegrable (fun x => Real.cos (c * x)) MeasureTheory.volume a b :=
  (by fun_prop : Continuous fun x => Real.cos (c * x)).intervalIntegrable _ _

/-- `∫_0^{2π} cos (a x) dx = 0` for a positive natural `a`. -/
theorem integral_cos_nat_mul {a : ℕ} (ha : 0 < a) :
    ∫ x in (0 : ℝ)..2 * π, Real.cos ((a : ℝ) * x) = 0 := by
  have h := integral_cos_int_mul (k := (a : ℤ)) (by exact_mod_cast ha.ne')
  simpa using h

/-- `∫_0^{2π} cos (a x) cos (b x) dx = π [a = b]` for positive naturals `a, b`. -/
theorem integral_cos_mul_cos_nat {a b : ℕ} (ha : 0 < a) (hb : 0 < b) :
    ∫ x in (0 : ℝ)..2 * π, Real.cos ((a : ℝ) * x) * Real.cos ((b : ℝ) * x) =
      if a = b then π else 0 := by
  have h := integral_cos_mul_cos (a : ℤ) (b : ℤ) 0 0
  have hab : (a : ℤ) + b ≠ 0 := by omega
  rw [if_neg hab, add_zero] at h
  by_cases h' : a = b
  · have : (a : ℤ) - b = 0 := by omega
    rw [if_pos this] at h
    rw [if_pos h']
    simpa using h
  · have : (a : ℤ) - b ≠ 0 := by omega
    rw [if_neg this] at h
    rw [if_neg h']
    simpa using h

/-- **Mean zero.** `∫_0^{2π} f_A = 0` when every element of `A` is positive. -/
theorem integral_cosSum (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a) :
    ∫ x in (0 : ℝ)..2 * π, cosSum A x = 0 := by
  unfold cosSum
  rw [intervalIntegral.integral_finsetSum (fun a _ => intervalIntegrable_cos_mul _ _ _)]
  exact Finset.sum_eq_zero (fun a ha => integral_cos_nat_mul (hA a ha))

/-- **Parseval.** `∫_0^{2π} f_A² = π |A|` when every element of `A` is positive. -/
theorem integral_cosSum_sq (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a) :
    ∫ x in (0 : ℝ)..2 * π, (cosSum A x) ^ 2 = π * A.card := by
  have hsq : ∀ x, (cosSum A x) ^ 2 =
      ∑ a ∈ A, ∑ b ∈ A, Real.cos ((a : ℝ) * x) * Real.cos ((b : ℝ) * x) := by
    intro x
    rw [cosSum, sq, Finset.sum_mul_sum]
  simp_rw [hsq]
  have hint : ∀ a b : ℕ, IntervalIntegrable
      (fun x => Real.cos ((a : ℝ) * x) * Real.cos ((b : ℝ) * x)) MeasureTheory.volume 0 (2 * π) :=
    fun a b => (by fun_prop : Continuous fun x =>
      Real.cos ((a : ℝ) * x) * Real.cos ((b : ℝ) * x)).intervalIntegrable _ _
  rw [intervalIntegral.integral_finsetSum (fun a _ =>
    (by fun_prop : Continuous fun x => ∑ b ∈ A,
      Real.cos ((a : ℝ) * x) * Real.cos ((b : ℝ) * x)).intervalIntegrable _ _)]
  calc ∑ a ∈ A, ∫ x in (0 : ℝ)..2 * π, ∑ b ∈ A, Real.cos ((a : ℝ) * x) * Real.cos ((b : ℝ) * x)
      = ∑ a ∈ A, ∑ b ∈ A, (if a = b then π else 0) := by
        refine Finset.sum_congr rfl (fun a ha => ?_)
        rw [intervalIntegral.integral_finsetSum (fun b _ => hint a b)]
        exact Finset.sum_congr rfl (fun b hb => integral_cos_mul_cos_nat (hA a ha) (hA b hb))
    _ = ∑ a ∈ A, π := by
        refine Finset.sum_congr rfl (fun a ha => ?_)
        simp [ha]
    _ = π * A.card := by
        rw [Finset.sum_const, nsmul_eq_mul, mul_comm]

/-- Normalized form of Parseval: `(1/2π) ∫_0^{2π} f_A² = |A| / 2`. -/
theorem normalized_mean_sq (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a) :
    (1 / (2 * π)) * ∫ x in (0 : ℝ)..2 * π, (cosSum A x) ^ 2 = (A.card : ℝ) / 2 := by
  rw [integral_cosSum_sq A hA]
  have := Real.pi_pos.ne'
  field_simp

end ChowlaCosine
