import ChowlaCosine.Beckner.HeatFlowDerivative

/-!
# Relative heat-flow derivative bounds

Interval support is an explicit hypothesis in these auxiliary estimates.
It is not a restriction on the M1 theorem or a claimed sharp-Young result.
-/

open MeasureTheory Real
open scoped ENNReal NNReal Topology

namespace ChowlaCosine.Beckner
set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

/-- Integrating a pointwise envelope for a signed real integrand. -/
theorem abs_integral_le_scaled_integral {α : Type*} [MeasurableSpace α] (μ : Measure α)
    {F G : α → ℝ} (hF : Integrable F μ) (hG : Integrable G μ) (C : ℝ)
    (hbound : ∀ y, |G y| ≤ C * F y) :
    |∫ y, G y ∂μ| ≤ C * ∫ y, F y ∂μ := by
  calc
    _ ≤ ∫ y, |G y| ∂μ := norm_integral_le_integral_norm G
    _ ≤ ∫ y, C * F y ∂μ := integral_mono hG.norm (hF.const_mul C) hbound
    _ = _ := integral_const_mul _ _

theorem integrable_heatSpaceSlope_integrand {f : ℝ → ℝ} (hf : Integrable f)
    {t : ℝ} (ht : 0 < t) (x : ℝ) : Integrable (fun y => f y * heatSpaceSlope t (x - y)) := by
  have hc : Continuous (fun y : ℝ => heatSpaceSlope t (x - y)) := by
    unfold heatSpaceSlope
    exact (by fun_prop : Continuous (fun y : ℝ => -(x - y) / (2 * t))).mul
      ((continuous_heatKernel t).comp (continuous_const.sub continuous_id))
  exact hf.mul_bdd hc.aestronglyMeasurable
    (Filter.Eventually.of_forall (fun y => heatKernel_space_slope_bound ht _))

theorem integrable_heatTimeSlope_integrand {f : ℝ → ℝ} (hf : Integrable f)
    {t : ℝ} (ht : 0 < t) (x : ℝ) : Integrable (fun y => f y * heatTimeSlope t (x - y)) := by
  have hc : Continuous (fun y : ℝ => heatTimeSlope t (x - y)) := by
    unfold heatTimeSlope
    exact (by fun_prop : Continuous (fun y : ℝ => (x - y) ^ 2 / (4 * t ^ 2) - 1 / (2 * t))).mul
      ((continuous_heatKernel t).comp (continuous_const.sub continuous_id))
  exact hf.mul_bdd hc.aestronglyMeasurable
    (Filter.Eventually.of_forall (fun y => heatKernel_time_slope_bound ht _))

/-- Relative first-derivative envelope before dividing by the positive flow. -/
theorem heatFlow_space_moment_bound {f : ℝ → ℝ} (hf : Integrable f)
    (hn : ∀ y, 0 ≤ f y) (R : ℝ) (hR : 0 ≤ R)
    (hsupport : ∀ y, f y ≠ 0 → |y| ≤ R) {t : ℝ} (ht : 0 < t) (x : ℝ) :
    |∫ y : ℝ, f y * heatSpaceSlope t (x - y)| ≤
      ((|x| + R) / (2 * t)) * heatFlow f t x := by
  apply abs_integral_le_scaled_integral volume
    (integrable_heatFlow_integrand hf ht x) (integrable_heatSpaceSlope_integrand hf ht x)
  intro y
  by_cases hy : f y = 0
  · simp [hy]
  have hyR := hsupport y hy
  have hxy : |x - y| ≤ |x| + R := (abs_sub x y).trans (by linarith)
  have hfy : 0 ≤ f y := hn y
  have hKy : 0 ≤ heatKernel t (x - y) := (heatKernel_pos ht _).le
  unfold heatSpaceSlope
  rw [abs_mul, abs_of_nonneg (hn y), abs_mul, abs_of_nonneg (heatKernel_pos ht _).le,
    abs_div, abs_neg, abs_of_pos (by positivity : 0 < 2 * t)]
  calc
    _ ≤ f y * (((|x| + R) / (2 * t)) * heatKernel t (x - y)) := by gcongr
    _ = _ := by ring

/-- Relative second/time-derivative envelope before division. -/
theorem heatFlow_time_moment_bound {f : ℝ → ℝ} (hf : Integrable f)
    (hn : ∀ y, 0 ≤ f y) (R : ℝ) (hR : 0 ≤ R)
    (hsupport : ∀ y, f y ≠ 0 → |y| ≤ R) {t : ℝ} (ht : 0 < t) (x : ℝ) :
    |∫ y : ℝ, f y * heatTimeSlope t (x - y)| ≤
      (((|x| + R) ^ 2 / (4 * t ^ 2) + 1 / (2 * t))) * heatFlow f t x := by
  apply abs_integral_le_scaled_integral volume
    (integrable_heatFlow_integrand hf ht x) (integrable_heatTimeSlope_integrand hf ht x)
  intro y
  by_cases hy : f y = 0
  · simp [hy]
  have hxy : |x - y| ≤ |x| + R := (abs_sub x y).trans (by linarith [hsupport y hy])
  have hsq : (x - y) ^ 2 ≤ (|x| + R) ^ 2 := by
    simpa only [sq_abs] using (sq_le_sq₀ (abs_nonneg (x - y)) (by positivity)).mpr hxy
  have hA : (x - y) ^ 2 / (4 * t ^ 2) ≤ (|x| + R) ^ 2 / (4 * t ^ 2) := by gcongr
  have hcoef : |(x - y) ^ 2 / (4 * t ^ 2) - 1 / (2 * t)| ≤
      (|x| + R) ^ 2 / (4 * t ^ 2) + 1 / (2 * t) := by
    apply abs_le.mpr
    constructor <;> nlinarith [show 0 ≤ (x - y) ^ 2 / (4 * t ^ 2) by positivity,
      show 0 ≤ (|x| + R) ^ 2 / (4 * t ^ 2) by positivity,
      show 0 ≤ 1 / (2 * t) by positivity]
  have hfy : 0 ≤ f y := hn y
  have hKy : 0 ≤ heatKernel t (x - y) := (heatKernel_pos ht _).le
  unfold heatTimeSlope
  rw [abs_mul, abs_of_nonneg (hn y), abs_mul, abs_of_nonneg (heatKernel_pos ht _).le]
  calc
    _ ≤ f y * ((((|x| + R) ^ 2 / (4 * t ^ 2) + 1 / (2 * t))) * heatKernel t (x - y)) := by gcongr
    _ = _ := by ring

/-- Uniform polynomial envelope for the spatial logarithmic derivative. -/
theorem heatFlow_space_score_bound {f : ℝ → ℝ} (hf : Integrable f)
    (hn : ∀ y, 0 ≤ f y) (hm : 0 < ∫ y : ℝ, f y) (R : ℝ) (hR : 0 ≤ R)
    (hsupport : ∀ y, f y ≠ 0 → |y| ≤ R) {t : ℝ} (ht : 0 < t) (x : ℝ) :
    |(∫ y : ℝ, f y * heatSpaceSlope t (x - y)) / heatFlow f t x| ≤ (|x| + R) / (2 * t) := by
  rw [abs_div, abs_of_pos (heatFlow_pos hf hn hm ht x)]
  exact (div_le_iff₀ (heatFlow_pos hf hn hm ht x)).mpr
    (heatFlow_space_moment_bound hf hn R hR hsupport ht x)

/-- Uniform polynomial envelope for the relative time/second derivative. -/
theorem heatFlow_time_score_bound {f : ℝ → ℝ} (hf : Integrable f)
    (hn : ∀ y, 0 ≤ f y) (hm : 0 < ∫ y : ℝ, f y) (R : ℝ) (hR : 0 ≤ R)
    (hsupport : ∀ y, f y ≠ 0 → |y| ≤ R) {t : ℝ} (ht : 0 < t) (x : ℝ) :
    |(∫ y : ℝ, f y * heatTimeSlope t (x - y)) / heatFlow f t x| ≤
      (|x| + R) ^ 2 / (4 * t ^ 2) + 1 / (2 * t) := by
  rw [abs_div, abs_of_pos (heatFlow_pos hf hn hm ht x)]
  exact (div_le_iff₀ (heatFlow_pos hf hn hm ht x)).mpr
    (heatFlow_time_moment_bound hf hn R hR hsupport ht x)

end ChowlaCosine.Beckner


/-!
# Differentiating positive weighted products

The finite product is differentiated on a genuine real neighborhood;
positivity only at the base point suffices by continuity and finiteness.
-/

open MeasureTheory Real
open scoped Topology

namespace ChowlaCosine.Beckner
set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

section
variable {ι : Type*} [Fintype ι]

/-- Logarithmic form of a finite positive weighted product. -/
theorem weighted_product_eq_exp (c : ι → ℝ) (F : ι → ℝ) (hF : ∀ i, 0 < F i) :
    (∏ i, F i ^ c i) = Real.exp (∑ i, c i * Real.log (F i)) := by
  rw [Real.exp_sum]
  apply Finset.prod_congr rfl
  intro i _
  rw [Real.rpow_def_of_pos (hF i)]
  congr 1
  ring

/-- Exact first derivative of any finite positive weighted product. -/
theorem hasDerivAt_weighted_product (c : ι → ℝ) (F : ι → ℝ → ℝ) (d : ι → ℝ) (x : ℝ)
    (hF : ∀ i, 0 < F i x) (hd : ∀ i, HasDerivAt (F i) (d i) x) :
    HasDerivAt (fun t => ∏ i, F i t ^ c i)
      ((∏ i, F i x ^ c i) * (∑ i, c i * d i / F i x)) x := by
  have hlog : HasDerivAt (fun t => ∑ i, c i * Real.log (F i t))
      (∑ i, c i * (d i / F i x)) x :=
    HasDerivAt.fun_sum (fun i _ => ((hd i).log (hF i).ne').const_mul (c i))
  have hpos : ∀ᶠ t in 𝓝 x, ∀ i, 0 < F i t := by
    apply Filter.eventually_all.mpr
    intro i
    exact (hd i).continuousAt.eventually (Ioi_mem_nhds (hF i))
  have heq : (fun t => ∏ i, F i t ^ c i) =ᶠ[𝓝 x]
      (fun t => Real.exp (∑ i, c i * Real.log (F i t))) := by
    filter_upwards [hpos] with t ht
    exact weighted_product_eq_exp c (fun i => F i t) ht
  have H := hlog.exp.congr_of_eventuallyEq heq
  rw [← weighted_product_eq_exp c (fun i => F i x) hF] at H
  simpa only [mul_div_assoc] using! H

/-- Exact derivative of the logarithmic product slope. In applications G
and K are the first and second derivatives of the factors. -/
theorem hasDerivAt_weighted_product_slope (c : ι → ℝ)
    (F G : ι → ℝ → ℝ) (K : ι → ℝ) (x : ℝ)
    (hF : ∀ i, 0 < F i x) (hd : ∀ i, HasDerivAt (F i) (G i x) x)
    (hG : ∀ i, HasDerivAt (G i) (K i) x) :
    HasDerivAt (fun t => (∏ i, F i t ^ c i) * (∑ i, c i * (G i t / F i t)))
      ((∏ i, F i x ^ c i) * ((∑ i, c i * (G i x / F i x)) ^ 2 +
        ∑ i, c i * (K i / F i x - (G i x / F i x) ^ 2))) x := by
  have hP : HasDerivAt (fun t => ∏ i, F i t ^ c i)
      ((∏ i, F i x ^ c i) * (∑ i, c i * (G i x / F i x))) x := by
    simpa only [mul_div_assoc] using! hasDerivAt_weighted_product c F (fun i => G i x) x hF hd
  have he : ∀ i, (K i * F i x - G i x * G i x) / (F i x) ^ 2 =
      K i / F i x - (G i x / F i x) ^ 2 := by
    intro i
    field_simp
    <;> ring
  have hQ : HasDerivAt (fun t => ∑ i, c i * (G i t / F i t))
      (∑ i, c i * (K i / F i x - (G i x / F i x) ^ 2)) x := by
    have HH := HasDerivAt.fun_sum (u := Finset.univ)
      (fun i _ => ((hG i).div (hd i) (hF i).ne').const_mul (c i))
    simpa only [he] using! HH
  exact (hP.mul hQ).congr_deriv (by ring)

end
end ChowlaCosine.Beckner

open scoped RealInnerProductSpace
namespace ChowlaCosine.Beckner

section FrameLaplacian
variable {ι κ E : Type*} [Fintype ι] [Fintype κ] [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- Exact algebraic Laplacian formula for a positive weighted product,
expressed using its scalar logarithmic first and second scores. -/
theorem frame_laplacian_identity (c v w : ι → ℝ) (u : ι → E)
    (hu : ∀ i, ‖u i‖ = 1) (b : OrthonormalBasis κ ℝ E) :
    (∑ j, ((∑ i, c i * ⟪u i, b j⟫ * v i) ^ 2 +
      ∑ i, c i * ⟪u i, b j⟫ ^ 2 * (w i - v i ^ 2))) =
      ‖frameVector c v u‖ ^ 2 + (∑ i, c i * w i) - ∑ i, c i * v i ^ 2 := by
  have hcoord : ∀ j, (∑ i, c i * ⟪u i, b j⟫ * v i) = ⟪frameVector c v u, b j⟫ := by
    intro j
    unfold frameVector
    rw [sum_inner]
    simp only [real_inner_smul_left]
    apply Finset.sum_congr rfl
    intro i _
    ring
  have hfirst : (∑ j, (∑ i, c i * ⟪u i, b j⟫ * v i) ^ 2) = ‖frameVector c v u‖ ^ 2 := by
    simp_rw [hcoord]
    exact b.sum_sq_inner_left _
  have hsecond : (∑ j, ∑ i, c i * ⟪u i, b j⟫ ^ 2 * (w i - v i ^ 2)) =
      ∑ i, c i * (w i - v i ^ 2) := by
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro i _
    calc
      _ = (c i * (w i - v i ^ 2)) * ∑ j, ⟪u i, b j⟫ ^ 2 := by
        rw [Finset.mul_sum]
        apply Finset.sum_congr rfl
        intro j _
        ring
      _ = _ := by rw [b.sum_sq_inner_left, hu]; norm_num
  rw [Finset.sum_add_distrib, hfirst, hsecond]
  simp_rw [mul_sub, Finset.sum_sub_distrib]
  ring

/-- Algebraic form of the pointwise nonnegative heat-flow defect.
Actual differentiation/integration of the geometric product is a later
obligation, not a hypothesis silently discharged by this identity. -/
theorem frame_heat_defect_nonneg (c v w : ι → ℝ) (u : ι → E)
    (hc : ∀ i, 0 ≤ c i) (hu : ∀ i, ‖u i‖ = 1) (hframe : IsWeightedFrame c u)
    (b : OrthonormalBasis κ ℝ E) (P : ℝ) (hP : 0 ≤ P) :
    0 ≤ P * (∑ i, c i * w i) -
      P * ∑ j, ((∑ i, c i * ⟪u i, b j⟫ * v i) ^ 2 +
        ∑ i, c i * ⟪u i, b j⟫ ^ 2 * (w i - v i ^ 2)) := by
  rw [frame_laplacian_identity c v w u hu b]
  have H := mul_nonneg hP (sub_nonneg.mpr (frame_variance_nonneg c v u hc hframe))
  nlinarith [H]
end FrameLaplacian

end ChowlaCosine.Beckner
