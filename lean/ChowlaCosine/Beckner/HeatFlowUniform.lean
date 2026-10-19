import ChowlaCosine.Beckner.GeometricHeat

/-! # Uniform Gaussian bounds on positive compact time intervals

These estimates discharge concrete domination obligations in M4. They do
not assert the remaining integrated monotonicity or limit/density passage.
-/

open MeasureTheory Real
open scoped BigOperators Topology RealInnerProductSpace

namespace ChowlaCosine.Beckner
set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

/-- A single explicit tail constant valid throughout a positive time interval. -/
noncomputable def heatTailConstant (f : ℝ → ℝ) (R a : ℝ) : ℝ :=
  (∫ y : ℝ, f y) * exp (R^2 / (4*a)) / sqrt (4*π*a)

theorem heatTailConstant_nonneg {f : ℝ → ℝ} (hn : ∀ y, 0 ≤ f y) (R a : ℝ) :
    0 ≤ heatTailConstant f R a := by
  unfold heatTailConstant
  exact div_nonneg (mul_nonneg (integral_nonneg hn) (exp_pos _).le) (sqrt_nonneg _)

theorem heatFlow_gaussian_bound_interval {f : ℝ → ℝ} (hf : Integrable f)
    (hn : ∀ y, 0 ≤ f y) (R : ℝ) (hR : 0 ≤ R)
    (hsupport : ∀ y, f y ≠ 0 → |y| ≤ R)
    {a b t : ℝ} (ha : 0 < a) (hat : a ≤ t) (htb : t ≤ b) (x : ℝ) :
    heatFlow f t x ≤ heatTailConstant f R a * gaussian (1/(8*b)) x := by
  have ht : 0 < t := ha.trans_le hat
  have hb : 0 < b := ht.trans_le htb
  have hm : 0 ≤ ∫ y : ℝ, f y := integral_nonneg hn
  have hcoef : heatTailConstant f R t ≤ heatTailConstant f R a := by
    unfold heatTailConstant
    apply div_le_div₀
    · exact mul_nonneg hm (exp_pos _).le
    · apply mul_le_mul_of_nonneg_left _ hm
      apply exp_le_exp.mpr
      exact div_le_div_of_nonneg_left (sq_nonneg R) (by positivity) (by linarith)
    · exact sqrt_pos.mpr (by positivity)
    · apply sqrt_le_sqrt
      nlinarith [pi_pos]
  have hg : gaussian (1/(8*t)) x ≤ gaussian (1/(8*b)) x := by
    unfold gaussian
    apply exp_le_exp.mpr
    have hi : 1/(8*b) ≤ 1/(8*t) :=
      div_le_div_of_nonneg_left (by norm_num) (by positivity) (by linarith)
    nlinarith [mul_le_mul_of_nonneg_right hi (sq_nonneg x)]
  exact (heatFlow_gaussian_bound hf hn R hR hsupport ht x).trans
    (mul_le_mul hcoef hg (gaussian_pos _ _).le (by unfold heatTailConstant; positivity))

section
variable {ι E : Type*} [Fintype ι] [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- Concrete all-space product domination uniform on a whole positive time interval. -/
theorem geometricHeatProduct_gaussian_bound_interval
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hc : ∀ i, 0 ≤ c i) (hframe : IsWeightedFrame c u)
    (R : ℝ) (hR : 0 ≤ R) (hsupport : ∀ i y, f i y ≠ 0 → |y| ≤ R)
    {a b t : ℝ} (ha : 0 < a) (hat : a ≤ t) (htb : t ≤ b) (x : E) :
    geometricHeatProduct f c u t x ≤
      (∏ i, heatTailConstant (f i) R a ^ c i) * exp (-(1/(8*b)) * ‖x‖^2) := by
  exact frame_product_gaussian_bound c u hframe hc (fun i => heatFlow (f i) t)
    (fun i => heatTailConstant (f i) R a)
    (fun i => heatTailConstant_nonneg (hn i) R a)
    (1/(8*b)) (fun i y => heatFlow_nonneg (hn i) (ha.trans_le hat) y)
    (fun i y => heatFlow_gaussian_bound_interval (hf i) (hn i) R hR (hsupport i) ha hat htb y) x

/-- Uniform relative time-score bound in Euclidean radius for every unit direction. -/
theorem heatTimeScore_bound_interval {f : ℝ → ℝ} (hf : Integrable f)
    (hn : ∀ y, 0 ≤ f y) (hm : 0 < ∫ y : ℝ, f y)
    (R : ℝ) (hR : 0 ≤ R) (hsupport : ∀ y, f y ≠ 0 → |y| ≤ R)
    {a t : ℝ} (ha : 0 < a) (hat : a ≤ t) (u x : E) (hu : ‖u‖ = 1) :
    |heatTimeScore f t ⟪u,x⟫| ≤ (‖x‖+R)^2/(4*a^2) + 1/(2*a) := by
  have ht : 0 < t := ha.trans_le hat
  have hi : |⟪u,x⟫| ≤ ‖x‖ := by simpa only [hu, one_mul] using abs_real_inner_le_norm u x
  have hsq : (|⟪u,x⟫|+R)^2 ≤ (‖x‖+R)^2 := by
    apply (sq_le_sq₀ (by positivity) (by positivity)).mpr
    linarith
  have H := heatFlow_time_score_bound hf hn hm R hR hsupport ht ⟪u,x⟫
  change |heatTimeScore f t ⟪u,x⟫| ≤ _ at H
  apply H.trans
  apply add_le_add
  · apply div_le_div₀ (by positivity) hsq (by positivity)
    nlinarith [sq_nonneg (t-a)]
  · exact div_le_div_of_nonneg_left (by norm_num) (by positivity) (by linarith)

/-- Uniform relative spatial-score bound in Euclidean radius. -/
theorem heatSpaceScore_bound_interval {f : ℝ → ℝ} (hf : Integrable f)
    (hn : ∀ y, 0 ≤ f y) (hm : 0 < ∫ y : ℝ, f y)
    (R : ℝ) (hR : 0 ≤ R) (hsupport : ∀ y, f y ≠ 0 → |y| ≤ R)
    {a t : ℝ} (ha : 0 < a) (hat : a ≤ t) (u x : E) (hu : ‖u‖ = 1) :
    |heatSpaceScore f t ⟪u,x⟫| ≤ (‖x‖+R)/(2*a) := by
  have ht : 0 < t := ha.trans_le hat
  have hi : |⟪u,x⟫| ≤ ‖x‖ := by simpa only [hu, one_mul] using abs_real_inner_le_norm u x
  have H := heatFlow_space_score_bound hf hn hm R hR hsupport ht ⟪u,x⟫
  change |heatSpaceScore f t ⟪u,x⟫| ≤ _ at H
  exact H.trans (div_le_div₀ (by positivity) (by linarith) (by positivity) (by linarith))

/-- Actual time derivative has a uniform Gaussian-polynomial envelope. -/
theorem geometricHeatProduct_time_derivative_bound_interval
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hm : ∀ i, 0 < ∫ y : ℝ, f i y)
    (hc : ∀ i, 0 ≤ c i) (hu : ∀ i, ‖u i‖ = 1) (hframe : IsWeightedFrame c u)
    (R : ℝ) (hR : 0 ≤ R) (hsupport : ∀ i y, f i y ≠ 0 → |y| ≤ R)
    {a b t : ℝ} (ha : 0 < a) (hat : a ≤ t) (htb : t ≤ b) (x : E) :
    |deriv (fun s => geometricHeatProduct f c u s x) t| ≤
      ((∏ i, heatTailConstant (f i) R a ^ c i) * exp (-(1/(8*b)) * ‖x‖^2)) *
        (∑ i, c i) * ((‖x‖+R)^2/(4*a^2) + 1/(2*a)) := by
  have ht : 0 < t := ha.trans_le hat
  have hP : 0 ≤ geometricHeatProduct f c u t x :=
    Finset.prod_nonneg (fun i _ => rpow_nonneg (heatFlow_nonneg (hn i) ht _) _)
  have hsum : |∑ i, c i * heatTimeScore (f i) t ⟪u i,x⟫| ≤
      (∑ i, c i) * ((‖x‖+R)^2/(4*a^2) + 1/(2*a)) := by
    calc
      _ ≤ ∑ i, |c i * heatTimeScore (f i) t ⟪u i,x⟫| := Finset.abs_sum_le_sum_abs _ _
      _ ≤ ∑ i, c i * ((‖x‖+R)^2/(4*a^2) + 1/(2*a)) := by
        apply Finset.sum_le_sum
        intro i _
        rw [abs_mul, abs_of_nonneg (hc i)]
        exact mul_le_mul_of_nonneg_left
          (heatTimeScore_bound_interval (hf i) (hn i) (hm i) R hR (hsupport i) ha hat (u i) x (hu i)) (hc i)
      _ = _ := by rw [Finset.sum_mul]
  rw [(hasDerivAt_geometricHeatProduct_time f c u hf hn hm ht x).deriv,
    abs_mul, abs_of_nonneg hP]
  calc
    _ ≤ geometricHeatProduct f c u t x *
        ((∑ i, c i) * ((‖x‖+R)^2/(4*a^2) + 1/(2*a))) :=
      mul_le_mul_of_nonneg_left hsum hP
    _ ≤ _ := by
      have H := geometricHeatProduct_gaussian_bound_interval f c u hf hn hc hframe R hR hsupport ha hat htb x
      have hs : 0 ≤ ∑ i, c i := Finset.sum_nonneg (fun i _ => hc i)
      have HB := mul_le_mul_of_nonneg_right H (mul_nonneg hs (by positivity :
        0 ≤ (‖x‖+R)^2/(4*a^2) + 1/(2*a)))
      simpa only [mul_assoc] using HB

end
end ChowlaCosine.Beckner
