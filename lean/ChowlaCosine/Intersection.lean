import ChowlaCosine.Moments

/-!
# The intersection lemma

If `f_{A₁} ≥ -M₁` and `f_{A₂} ≥ -M₂` on all of `ℝ` (`A₁, A₂` finite sets of positive
naturals), then `f_{A₁ ∩ A₂} ≥ -2 M₁ M₂` on all of `ℝ`.

Proof: for fixed `x`,
`0 ≤ ∫_0^{2π} (f_{A₁}(y) + M₁)(f_{A₂}(x - y) + M₂) dy = π f_{A₁∩A₂}(x) + 2π M₁ M₂`,
using `∫_0^{2π} cos (a y) cos (b (x - y)) dy = π cos (a x) [a = b]` for positive `a, b`
and mean zero for the cross terms.

The hypotheses `0 ≤ M₁`, `0 ≤ M₂` are **not needed** for the main statement
(`cosSum_inter_ge`); a version carrying them (`cosSum_inter_ge'`) is included for
fidelity with the paper statement.
-/

open Real

namespace ChowlaCosine

/-- `∫_0^{2π} cos (a y) cos (b (x - y)) dy = π cos (a x) [a = b]` for positive naturals. -/
theorem integral_cos_mul_cos_sub {a b : ℕ} (ha : 0 < a) (hb : 0 < b) (x : ℝ) :
    ∫ y in (0 : ℝ)..2 * π, Real.cos ((a : ℝ) * y) * Real.cos ((b : ℝ) * (x - y)) =
      if a = b then π * Real.cos ((a : ℝ) * x) else 0 := by
  have h := integral_cos_mul_cos (a : ℤ) (-(b : ℤ)) 0 ((b : ℝ) * x)
  have hpt : ∀ y : ℝ, Real.cos ((a : ℝ) * y) * Real.cos ((b : ℝ) * (x - y)) =
      Real.cos ((((a : ℤ)) : ℝ) * y + 0) * Real.cos (((-(b : ℤ) : ℤ) : ℝ) * y + (b : ℝ) * x) := by
    intro y
    congr 2
    · push_cast; ring
    · push_cast; ring
  simp_rw [hpt]
  rw [h]
  have h1 : (a : ℤ) - -(b : ℤ) ≠ 0 := by omega
  rw [if_neg h1, zero_add]
  by_cases hab : a = b
  · have h2 : (a : ℤ) + -(b : ℤ) = 0 := by omega
    rw [if_pos h2, if_pos hab, zero_add, hab]
  · have h2 : (a : ℤ) + -(b : ℤ) ≠ 0 := by omega
    rw [if_neg h2, if_neg hab]

/-- `∫_0^{2π} f_A(x - y) dy = 0` for `A` with positive elements. -/
theorem integral_cosSum_sub (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a) (x : ℝ) :
    ∫ y in (0 : ℝ)..2 * π, cosSum A (x - y) = 0 := by
  unfold cosSum
  rw [intervalIntegral.integral_finsetSum (fun (b : ℕ) _ =>
    (by fun_prop : Continuous fun y : ℝ => Real.cos ((b : ℝ) * (x - y))).intervalIntegrable _ _)]
  refine Finset.sum_eq_zero (fun b hb => ?_)
  have h := integral_cos_int_mul_add (-(b : ℤ)) ((b : ℝ) * x)
  have hb0 : -(b : ℤ) ≠ 0 := by have := hA b hb; omega
  rw [if_neg hb0] at h
  rw [← h]
  congr 1
  ext y
  congr 1
  push_cast
  ring

/-- The convolution integral `∫_0^{2π} f_{A₁}(y) f_{A₂}(x - y) dy = π f_{A₁ ∩ A₂}(x)`. -/
theorem integral_cosSum_mul_cosSum_sub (A₁ A₂ : Finset ℕ) (h₁ : ∀ a ∈ A₁, 0 < a)
    (h₂ : ∀ a ∈ A₂, 0 < a) (x : ℝ) :
    ∫ y in (0 : ℝ)..2 * π, cosSum A₁ y * cosSum A₂ (x - y) = π * cosSum (A₁ ∩ A₂) x := by
  have hexp : ∀ y, cosSum A₁ y * cosSum A₂ (x - y) =
      ∑ a ∈ A₁, ∑ b ∈ A₂, Real.cos ((a : ℝ) * y) * Real.cos ((b : ℝ) * (x - y)) := by
    intro y
    rw [cosSum, cosSum, Finset.sum_mul_sum]
  simp_rw [hexp]
  rw [intervalIntegral.integral_finsetSum (fun (a : ℕ) _ =>
    (by fun_prop : Continuous fun y : ℝ => ∑ b ∈ A₂,
      Real.cos ((a : ℝ) * y) * Real.cos ((b : ℝ) * (x - y))).intervalIntegrable _ _)]
  calc ∑ a ∈ A₁, ∫ y in (0 : ℝ)..2 * π, ∑ b ∈ A₂,
        Real.cos ((a : ℝ) * y) * Real.cos ((b : ℝ) * (x - y))
      = ∑ a ∈ A₁, ∑ b ∈ A₂, (if a = b then π * Real.cos ((a : ℝ) * x) else 0) := by
        refine Finset.sum_congr rfl (fun a ha => ?_)
        rw [intervalIntegral.integral_finsetSum (fun (b : ℕ) _ =>
          (by fun_prop : Continuous fun y : ℝ =>
            Real.cos ((a : ℝ) * y) * Real.cos ((b : ℝ) * (x - y))).intervalIntegrable _ _)]
        exact Finset.sum_congr rfl (fun b hb => integral_cos_mul_cos_sub (h₁ a ha) (h₂ b hb) x)
    _ = ∑ a ∈ A₁, (if a ∈ A₂ then π * Real.cos ((a : ℝ) * x) else 0) := by
        refine Finset.sum_congr rfl (fun a _ => ?_)
        exact Finset.sum_ite_eq A₂ a (fun a => π * Real.cos ((a : ℝ) * x))
    _ = ∑ a ∈ A₁ ∩ A₂, π * Real.cos ((a : ℝ) * x) := by
        rw [Finset.sum_ite_mem]
    _ = π * cosSum (A₁ ∩ A₂) x := by
        rw [cosSum, Finset.mul_sum]

/-- **Intersection lemma.** Let `A₁, A₂` be finite sets of positive naturals and
`M₁, M₂ : ℝ`. If `-M₁ ≤ f_{A₁}(x)` and `-M₂ ≤ f_{A₂}(x)` for all real `x`, then
`-(2 M₁ M₂) ≤ f_{A₁ ∩ A₂}(x)` for all real `x`. (No sign hypothesis on `M₁, M₂` is needed.) -/
theorem cosSum_inter_ge (A₁ A₂ : Finset ℕ) (h₁ : ∀ a ∈ A₁, 0 < a) (h₂ : ∀ a ∈ A₂, 0 < a)
    (M₁ M₂ : ℝ) (hM₁ : ∀ x : ℝ, -M₁ ≤ cosSum A₁ x) (hM₂ : ∀ x : ℝ, -M₂ ≤ cosSum A₂ x) :
    ∀ x : ℝ, -(2 * M₁ * M₂) ≤ cosSum (A₁ ∩ A₂) x := by
  intro x
  have hc₁ := continuous_cosSum A₁
  have hc₂ := continuous_cosSum A₂
  have hc₂' : Continuous fun y : ℝ => cosSum A₂ (x - y) := hc₂.comp (by fun_prop)
  have hnn : 0 ≤ ∫ y in (0 : ℝ)..2 * π, (cosSum A₁ y + M₁) * (cosSum A₂ (x - y) + M₂) := by
    apply intervalIntegral.integral_nonneg (by positivity)
    intro y _
    exact mul_nonneg (by linarith [hM₁ y]) (by linarith [hM₂ (x - y)])
  have hF : ∀ y, (cosSum A₁ y + M₁) * (cosSum A₂ (x - y) + M₂) =
      ((cosSum A₁ y * cosSum A₂ (x - y) + M₂ * cosSum A₁ y) + M₁ * cosSum A₂ (x - y)) + M₁ * M₂ := by
    intro y
    ring
  simp_rw [hF] at hnn
  rw [intervalIntegral.integral_add, intervalIntegral.integral_add,
    intervalIntegral.integral_add] at hnn
  · simp only [intervalIntegral.integral_const_mul, intervalIntegral.integral_const,
      integral_cosSum_mul_cosSum_sub A₁ A₂ h₁ h₂ x, integral_cosSum A₁ h₁,
      integral_cosSum_sub A₂ h₂ x, sub_zero, smul_eq_mul, mul_zero, add_zero] at hnn
    have hπ := Real.pi_pos
    nlinarith
  all_goals first
    | exact (hc₁.mul hc₂').intervalIntegrable _ _
    | exact ((hc₁.mul hc₂').add (continuous_const.mul hc₁)).intervalIntegrable _ _
    | exact (((hc₁.mul hc₂').add (continuous_const.mul hc₁)).add
        (continuous_const.mul hc₂')).intervalIntegrable _ _
    | exact (continuous_const.mul hc₁).intervalIntegrable _ _
    | exact (continuous_const.mul hc₂').intervalIntegrable _ _
    | exact continuous_const.intervalIntegrable _ _
    | (apply Continuous.intervalIntegrable; fun_prop)

/-- The intersection lemma with the (redundant) hypotheses `0 ≤ M₁`, `0 ≤ M₂`, exactly as in
the paper statement. -/
theorem cosSum_inter_ge' (A₁ A₂ : Finset ℕ) (h₁ : ∀ a ∈ A₁, 0 < a) (h₂ : ∀ a ∈ A₂, 0 < a)
    (M₁ M₂ : ℝ) (_hM₁0 : 0 ≤ M₁) (_hM₂0 : 0 ≤ M₂)
    (hM₁ : ∀ x : ℝ, cosSum A₁ x ≥ -M₁) (hM₂ : ∀ x : ℝ, cosSum A₂ x ≥ -M₂) :
    ∀ x : ℝ, cosSum (A₁ ∩ A₂) x ≥ -2 * M₁ * M₂ := by
  intro x
  have := cosSum_inter_ge A₁ A₂ h₁ h₂ M₁ M₂ hM₁ hM₂ x
  linarith

end ChowlaCosine
