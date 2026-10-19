import ChowlaCosine.Beckner.HeatFlowRescale
import Mathlib.MeasureTheory.Measure.Haar.NormedSpace

/-! # The large-time limit of the actual planar geometric heat integral

The finite-product normalization and the planar dilation Jacobian are kept
explicit. Compact support is an intermediate domination hypothesis here.
-/

open MeasureTheory Real
open scoped BigOperators Topology RealInnerProductSpace

namespace ChowlaCosine.Beckner
set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

section
variable {ι E : Type*} [Fintype ι] [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- Trace of the weighted rank-one identity in an arbitrary finite orthonormal basis. -/
theorem weightedFrame_sum_weights {κ : Type*} [Fintype κ]
    (c : ι → ℝ) (u : ι → E) (hu : ∀ i, ‖u i‖ = 1)
    (hframe : IsWeightedFrame c u) (b : OrthonormalBasis κ ℝ E) :
    (∑ i, c i) = Fintype.card κ := by
  calc
    (∑ i, c i) = ∑ i, c i * ∑ j, ⟪u i, b j⟫^2 := by
      simp_rw [b.sum_sq_inner_left, hu, one_pow, mul_one]
    _ = ∑ j, ∑ i, c i * (⟪u i, b j⟫ * ⟪u i, b j⟫) := by
      simp_rw [Finset.mul_sum, pow_two]
      exact Finset.sum_comm
    _ = ∑ j, ⟪b j, b j⟫ := Finset.sum_congr rfl (fun j _ => hframe (b j) (b j))
    _ = _ := by simp [b.norm_eq_one]

/-- Exact normalization of a finite weighted product in dimension two. -/
theorem geometricHeatProduct_rescale (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hn : ∀ i y, 0 ≤ f i y) (hu : ∀ i, ‖u i‖ = 1)
    (hframe : IsWeightedFrame c u) (b : OrthonormalBasis (Fin 2) ℝ E)
    {s : ℝ} (hs : 0 < s) (x : E) :
    (∏ i, (s * heatFlow (f i) (s^2) (s*⟪u i,x⟫)) ^ c i) =
      s^2 * geometricHeatProduct f c u (s^2) (s • x) := by
  have hsum : (∑ i, c i) = 2 := by
    simpa using weightedFrame_sum_weights c u hu hframe b
  simp_rw [mul_rpow hs.le (heatFlow_nonneg (hn _) (sq_pos_of_pos hs) _)]
  rw [Finset.prod_mul_distrib, ← rpow_sum_of_pos hs, hsum, rpow_two]
  simp only [geometricHeatProduct, real_inner_smul_right]

end

/-- Uniform scalar Gaussian envelope after square-time rescaling, for every s ≥ 1. -/
theorem rescaled_heatFlow_gaussian_bound {f : ℝ → ℝ} (hf : Integrable f)
    (hn : ∀ y, 0 ≤ f y) (R : ℝ) (hR : 0 ≤ R)
    (hsupport : ∀ y, f y ≠ 0 → |y| ≤ R)
    {s : ℝ} (hs : 1 ≤ s) (x : ℝ) :
    s * heatFlow f (s^2) (s*x) ≤ heatTailConstant f R 1 * gaussian (1/8) x := by
  have hs0 : 0 < s := by linarith
  have hs2 : 1 ≤ s^2 := by nlinarith
  have H := mul_le_mul_of_nonneg_left
    (heatFlow_gaussian_bound hf hn R hR hsupport (sq_pos_of_pos hs0) (s*x)) hs0.le
  have hcoef : s * heatTailConstant f R (s^2) ≤ heatTailConstant f R 1 := by
    unfold heatTailConstant
    rw [sqrt_mul (by positivity : 0 ≤ 4*π), sqrt_sq_eq_abs, abs_of_pos hs0]
    have he : exp (R^2/(4*s^2)) ≤ exp (R^2/(4*1)) := by
      apply exp_le_exp.mpr
      exact div_le_div_of_nonneg_left (sq_nonneg R) (by norm_num) (by nlinarith)
    have hm : 0 ≤ ∫ y : ℝ, f y := integral_nonneg hn
    have H' := mul_le_mul_of_nonneg_left he hm
    have H'' := div_le_div_of_nonneg_right H' (sqrt_nonneg (4*π))
    convert H'' using 1 <;> (try rfl) <;> field_simp
  have hg : gaussian (1/(8*s^2)) (s*x) = gaussian (1/8) x := by
    unfold gaussian
    congr 1
    field_simp
  change s * heatFlow f (s^2) (s*x) ≤ _
  calc
    _ ≤ (s * heatTailConstant f R (s^2)) * gaussian (1/(8*s^2)) (s*x) := by
      simpa only [heatTailConstant, mul_assoc] using H
    _ ≤ _ := by rw [hg]; exact mul_le_mul_of_nonneg_right hcoef (gaussian_pos _ _).le

/-- Integrability of the Gaussian on the whole coordinate plane. -/
theorem integrable_plane_gaussian {d : ℝ} (hd : 0 < d) :
    Integrable (fun z : ℝ × ℝ => exp (-d*(z.1^2+z.2^2))) (volume.prod volume) := by
  exact ((integrable_gaussian hd).mul_prod (integrable_gaussian hd)).congr
    (Filter.Eventually.of_forall (fun z => by
      dsimp [gaussian]
      rw [← exp_add]
      congr 1
      ring))

/-- Exact two-dimensional Gaussian integral, with the full-plane measure. -/
theorem integral_plane_gaussian {d : ℝ} (hd : 0 < d) :
    (∫ z : ℝ × ℝ, exp (-d*(z.1^2+z.2^2)) ∂volume.prod volume) = π/d := by
  have he : (fun z : ℝ × ℝ => exp (-d*(z.1^2+z.2^2))) =
      (fun z : ℝ × ℝ => gaussian d z.1 * gaussian d z.2) := by
    funext z
    unfold gaussian
    rw [← exp_add]
    congr 1
    ring
  rw [he, integral_prod_mul, integral_gaussian_exact, ← pow_two, sq_sqrt (by positivity)]

/-- The planar dilation contributes exactly the inverse square of the dilation. -/
theorem integral_plane_dilate (F : ℝ × ℝ → ℝ) {s : ℝ} (hs : 0 < s) :
    (∫ z : ℝ × ℝ, s^2 * F (s • z) ∂volume.prod volume) =
      ∫ z : ℝ × ℝ, F z ∂volume.prod volume := by
  rw [integral_const_mul,
    Measure.integral_comp_smul_of_nonneg (volume.prod volume) F s (hR := hs.le)]
  simp only [Module.finrank_prod, Module.finrank_self, smul_eq_mul]
  field_simp

section
variable {ι E : Type*} [Fintype ι] [NormedAddCommGroup E] [InnerProductSpace ℝ E]

theorem planePoint_smul (b : OrthonormalBasis (Fin 2) ℝ E) (s : ℝ) (z : ℝ × ℝ) :
    planePoint b (s • z) = s • planePoint b z := by
  simp only [planePoint, Prod.smul_fst, Prod.smul_snd, smul_add, smul_smul, smul_eq_mul]

/-- The exact probability-normalized Gaussian product determined by a planar frame. -/
theorem frame_heatKernel_product (c : ι → ℝ) (u : ι → E)
    (hu : ∀ i, ‖u i‖ = 1) (hframe : IsWeightedFrame c u)
    (b : OrthonormalBasis (Fin 2) ℝ E) (x : E) :
    (∏ i, heatKernel 1 ⟪u i,x⟫ ^ c i) = exp (-(1/4)*‖x‖^2)/(4*π) := by
  have hsum : (∑ i, c i) = 2 := by simpa using weightedFrame_sum_weights c u hu hframe b
  simp only [heatKernel, mul_one]
  simp_rw [div_rpow (gaussian_pos _ _).le (sqrt_nonneg _)]
  rw [Finset.prod_div_distrib, ← rpow_sum_of_pos (sqrt_pos.mpr (by positivity : 0 < 4*π)),
    hsum, rpow_two, sq_sqrt (by positivity : 0 ≤ 4*π), frame_gaussian_identity c u hframe]

/-- Integrating the limiting Gaussian product gives exactly the product of the masses. -/
theorem integral_frame_heatKernel_product (m c : ι → ℝ) (u : ι → E)
    (hm : ∀ i, 0 ≤ m i) (hu : ∀ i, ‖u i‖ = 1) (hframe : IsWeightedFrame c u)
    (b : OrthonormalBasis (Fin 2) ℝ E) :
    (∫ z : ℝ × ℝ, ∏ i, (m i * heatKernel 1 ⟪u i,planePoint b z⟫) ^ c i
      ∂volume.prod volume) = ∏ i, m i ^ c i := by
  simp_rw [mul_rpow (hm _) (heatKernel_pos (by norm_num : (0:ℝ)<1) _).le,
    Finset.prod_mul_distrib, frame_heatKernel_product c u hu hframe b, norm_planePoint_sq]
  rw [integral_const_mul, integral_div, integral_plane_gaussian (by norm_num : (0:ℝ)<1/4)]
  have hp : π ≠ 0 := pi_ne_zero
  field_simp

/-- Dominated convergence of the normalized product, including zero-mass data.
The restriction to interval-supported nonnegative L1 data is only an intermediate
step toward the unrestricted sharp Young theorem. -/
theorem tendsto_integral_rescaled_geometricHeatProduct
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hc : ∀ i, 0 ≤ c i) (hu : ∀ i, ‖u i‖ = 1) (hframe : IsWeightedFrame c u)
    (R : ℝ) (hR : 0 ≤ R) (hsupport : ∀ i y, f i y ≠ 0 → |y| ≤ R)
    (b : OrthonormalBasis (Fin 2) ℝ E) :
    Filter.Tendsto (fun s : ℝ => ∫ z : ℝ × ℝ,
      s^2 * geometricHeatProduct f c u (s^2) (s • planePoint b z) ∂volume.prod volume)
      Filter.atTop (𝓝 (∏ i, (∫ y : ℝ, f i y) ^ c i)) := by
  let F : ℝ → ℝ × ℝ → ℝ := fun s z =>
    ∏ i, (s * heatFlow (f i) (s^2) (s*⟪u i,planePoint b z⟫)) ^ c i
  let K : ℝ := ∏ i, heatTailConstant (f i) R 1 ^ c i
  let bound : ℝ × ℝ → ℝ := fun z => K * exp (-(1/8)*(z.1^2+z.2^2))
  have hmeas : ∀ᶠ s : ℝ in Filter.atTop, AEStronglyMeasurable (F s) (volume.prod volume) := by
    filter_upwards [Filter.eventually_gt_atTop (0 : ℝ)] with s hs
    apply Continuous.aestronglyMeasurable
    apply continuous_finsetProd
    intro i _
    apply (continuous_rpow_const (hc i)).comp
    exact continuous_const.mul ((continuous_heatFlow_space (hf i) (sq_pos_of_pos hs)).comp
      (continuous_const.mul (continuous_const.inner (continuous_planePoint b))))
  have hbound : ∀ᶠ s : ℝ in Filter.atTop, ∀ᵐ z : ℝ × ℝ ∂volume.prod volume,
      ‖F s z‖ ≤ bound z := by
    filter_upwards [Filter.eventually_ge_atTop (1 : ℝ)] with s hs
    apply Filter.Eventually.of_forall
    intro z
    have hs0 : 0 < s := by linarith
    have H := frame_product_gaussian_bound c u hframe hc
      (fun i x => s * heatFlow (f i) (s^2) (s*x))
      (fun i => heatTailConstant (f i) R 1)
      (fun i => heatTailConstant_nonneg (hn i) R 1) (1/8)
      (fun i x => mul_nonneg hs0.le (heatFlow_nonneg (hn i) (sq_pos_of_pos hs0) _))
      (fun i x => rescaled_heatFlow_gaussian_bound (hf i) (hn i) R hR (hsupport i) hs x)
      (planePoint b z)
    rw [norm_planePoint_sq] at H
    rw [Real.norm_of_nonneg (Finset.prod_nonneg (fun i _ => rpow_nonneg
      (mul_nonneg hs0.le (heatFlow_nonneg (hn i) (sq_pos_of_pos hs0) _)) _))]
    exact H
  have hlim : ∀ᵐ z : ℝ × ℝ ∂volume.prod volume,
      Filter.Tendsto (fun s => F s z) Filter.atTop
        (𝓝 (∏ i, ((∫ y : ℝ, f i y) * heatKernel 1 ⟪u i,planePoint b z⟫) ^ c i)) := by
    apply Filter.Eventually.of_forall
    intro z
    exact tendsto_finsetProd _ (fun i _ =>
      (tendsto_heatFlow_large_time (hf i) ⟪u i,planePoint b z⟫).rpow_const (Or.inr (hc i)))
  have H := tendsto_integral_filter_of_dominated_convergence bound hmeas hbound
    ((integrable_plane_gaussian (by norm_num : (0:ℝ)<1/8)).const_mul K) hlim
  rw [integral_frame_heatKernel_product _ c u (fun i => integral_nonneg (hn i)) hu hframe b] at H
  apply H.congr'
  filter_upwards [Filter.eventually_gt_atTop (0 : ℝ)] with s hs
  apply integral_congr_ae
  exact Filter.Eventually.of_forall (fun z => geometricHeatProduct_rescale f c u hn hu hframe b hs _)

/-- Large-time limit of the actual unnormalized whole-plane heat-product integral.
The rescaling factors cancel by the two-dimensional change of variables. -/
theorem tendsto_integral_geometricHeatProduct_sq
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hc : ∀ i, 0 ≤ c i) (hu : ∀ i, ‖u i‖ = 1) (hframe : IsWeightedFrame c u)
    (R : ℝ) (hR : 0 ≤ R) (hsupport : ∀ i y, f i y ≠ 0 → |y| ≤ R)
    (b : OrthonormalBasis (Fin 2) ℝ E) :
    Filter.Tendsto (fun s : ℝ => ∫ z : ℝ × ℝ,
      geometricHeatProduct f c u (s^2) (planePoint b z) ∂volume.prod volume)
      Filter.atTop (𝓝 (∏ i, (∫ y : ℝ, f i y) ^ c i)) := by
  apply (tendsto_integral_rescaled_geometricHeatProduct f c u hf hn hc hu hframe R hR hsupport b).congr'
  filter_upwards [Filter.eventually_gt_atTop (0 : ℝ)] with s hs
  simpa only [planePoint_smul] using
    integral_plane_dilate (fun z => geometricHeatProduct f c u (s^2) (planePoint b z)) hs

/-- The same whole-plane limit in the original time variable. -/
theorem tendsto_integral_geometricHeatProduct
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hc : ∀ i, 0 ≤ c i) (hu : ∀ i, ‖u i‖ = 1) (hframe : IsWeightedFrame c u)
    (R : ℝ) (hR : 0 ≤ R) (hsupport : ∀ i y, f i y ≠ 0 → |y| ≤ R)
    (b : OrthonormalBasis (Fin 2) ℝ E) :
    Filter.Tendsto (fun t : ℝ => ∫ z : ℝ × ℝ,
      geometricHeatProduct f c u t (planePoint b z) ∂volume.prod volume)
      Filter.atTop (𝓝 (∏ i, (∫ y : ℝ, f i y) ^ c i)) := by
  have H := (tendsto_integral_geometricHeatProduct_sq f c u hf hn hc hu hframe R hR hsupport b).comp
    Real.tendsto_sqrt_atTop
  apply H.congr'
  filter_upwards [Filter.eventually_ge_atTop (0 : ℝ)] with t ht
  simp only [Function.comp_def, sq_sqrt ht]

/-- The actual heat-product integral at every positive time is bounded by its
large-time mass limit. All monotonicity and limiting hypotheses are discharged. -/
theorem integral_geometricHeatProduct_le_mass
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hm : ∀ i, 0 < ∫ y : ℝ, f i y)
    (hc : ∀ i, 0 ≤ c i) (hu : ∀ i, ‖u i‖ = 1) (hframe : IsWeightedFrame c u)
    (R : ℝ) (hR : 0 ≤ R) (hsupport : ∀ i y, f i y ≠ 0 → |y| ≤ R)
    (b : OrthonormalBasis (Fin 2) ℝ E) {t : ℝ} (ht : 0 < t) :
    (∫ z : ℝ × ℝ, geometricHeatProduct f c u t (planePoint b z) ∂volume.prod volume) ≤
      ∏ i, (∫ y : ℝ, f i y) ^ c i := by
  apply ge_of_tendsto (tendsto_integral_geometricHeatProduct f c u hf hn hc hu hframe R hR hsupport b)
  filter_upwards [Filter.eventually_ge_atTop t] with s hs
  exact geometricHeatProduct_integral_monotone f c u hf hn hm hc hu hframe R hR hsupport b
    ht (ht.trans_le hs) hs

end
end ChowlaCosine.Beckner
