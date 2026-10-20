-- SOURCE ../.research/agents/lean_m4_scratch/DensityHeader.lean
import ChowlaCosine.Beckner.HeatFlowRescale
import Mathlib.MeasureTheory.Measure.Haar.NormedSpace
import Mathlib.MeasureTheory.Function.ContinuousMapDense
import Mathlib.MeasureTheory.Function.ConvergenceInMeasure

-- SOURCE ChowlaCosine/Beckner/HeatFlowProductLimit.lean

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

-- SOURCE ChowlaCosine/Beckner/HeatFlowInitial.lean

/-! # Initial-time passage for bounded continuous data

Boundedness and continuity are intermediate assumptions. The density passage
to arbitrary nonnegative L1 data is a separate obligation.
-/

open MeasureTheory Real
open scoped BigOperators Topology RealInnerProductSpace

namespace ChowlaCosine.Beckner
set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

/-- Move the small-time heat-kernel dilation into the initial datum exactly. -/
theorem heatFlow_initial_rescale (f : ℝ → ℝ) {s : ℝ} (hs : 0 < s) (x : ℝ) :
    (∫ y : ℝ, heatKernel 1 y * f (x-s*y)) = heatFlow f (s^2) x := by
  have hk : ∀ y : ℝ, heatKernel 1 y = s * heatKernel (s^2) (s*y) := by
    intro y
    rw [show s*y = s*y-0 by ring, heatKernel_rescale hs]
    simp [hs.ne']
  simp_rw [hk, mul_assoc]
  rw [integral_const_mul,
    Measure.integral_comp_mul_left (fun y : ℝ => heatKernel (s^2) y * f (x-y)) s,
    abs_of_pos (inv_pos.mpr hs), smul_eq_mul, ← mul_assoc, mul_inv_cancel₀ hs.ne', one_mul]
  have H := integral_sub_left_eq_self (fun y : ℝ => f y * heatKernel (s^2) (x-y)) volume x
  simpa only [sub_sub_cancel, mul_comm, heatFlow] using H

/-- Approximate identity for the actual heat flow at every continuity point of
a bounded measurable datum. The normalization integral is exactly one. -/
theorem tendsto_heatFlow_initial_sq {f : ℝ → ℝ} (hf : Measurable f)
    (B : ℝ) (hB : ∀ y, |f y| ≤ B) {x : ℝ} (hx : ContinuousAt f x) :
    Filter.Tendsto (fun s : ℝ => heatFlow f (s^2) x) (𝓝[>] (0:ℝ)) (𝓝 (f x)) := by
  let F : ℝ → ℝ → ℝ := fun s y => heatKernel 1 y * f (x-s*y)
  let bound : ℝ → ℝ := fun y => heatKernel 1 y * B
  have hmeas : ∀ᶠ s : ℝ in 𝓝 (0:ℝ), AEStronglyMeasurable (F s) := by
    apply Filter.Eventually.of_forall
    intro s
    exact (continuous_heatKernel 1).aestronglyMeasurable.mul
      (hf.comp (by fun_prop : Measurable (fun y : ℝ => x-s*y))).aestronglyMeasurable
  have hbound : ∀ᶠ s : ℝ in 𝓝 (0:ℝ), ∀ᵐ y : ℝ, ‖F s y‖ ≤ bound y := by
    apply Filter.Eventually.of_forall
    intro s
    apply Filter.Eventually.of_forall
    intro y
    dsimp [F, bound]
    rw [abs_mul, abs_of_pos (heatKernel_pos (by norm_num : (0:ℝ)<1) _)]
    exact mul_le_mul_of_nonneg_left (hB _) (heatKernel_pos (by norm_num : (0:ℝ)<1) _).le
  have hlim : ∀ᵐ y : ℝ, Filter.Tendsto (fun s => F s y) (𝓝 (0:ℝ))
      (𝓝 (heatKernel 1 y * f x)) := by
    apply Filter.Eventually.of_forall
    intro y
    have H : Filter.Tendsto (fun s : ℝ => x-s*y) (𝓝 (0:ℝ)) (𝓝 x) := by
      simpa only [zero_mul, sub_zero] using
        (by fun_prop : Continuous (fun s : ℝ => x-s*y)).tendsto (0:ℝ)
    exact (hx.tendsto.comp H).const_mul _
  have H := tendsto_integral_filter_of_dominated_convergence bound hmeas hbound
    ((integrable_heatKernel (by norm_num : (0:ℝ)<1)).mul_const B) hlim
  rw [integral_mul_const, integral_heatKernel (by norm_num : (0:ℝ)<1), one_mul] at H
  apply (H.mono_left nhdsWithin_le_nhds).congr'
  filter_upwards [self_mem_nhdsWithin] with s hs
  exact heatFlow_initial_rescale f hs x

/-- Fatou passage for nonnegative real integrals, including finiteness of the
limiting integral. This is applied on the whole unbounded plane below. -/
theorem integrable_and_integral_le_of_nonneg_limit
    {α : Type*} [MeasurableSpace α] (μ : Measure α)
    (F : ℕ → α → ℝ) (g : α → ℝ) (C : ℝ)
    (hF : ∀ n, Integrable (F n) μ) (hFn : ∀ n x, 0 ≤ F n x)
    (hg : AEStronglyMeasurable g μ) (hgn : ∀ x, 0 ≤ g x)
    (hlim : ∀ᵐ x ∂μ, Filter.Tendsto (fun n => F n x) Filter.atTop (𝓝 (g x)))
    (hbound : ∀ n, (∫ x, F n x ∂μ) ≤ C) :
    Integrable g μ ∧ (∫ x, g x ∂μ) ≤ C := by
  have H : (∫⁻ x, ENNReal.ofReal (g x) ∂μ) ≤ ENNReal.ofReal C := by
    calc
      _ = ∫⁻ x, Filter.liminf (fun n => ENNReal.ofReal (F n x)) Filter.atTop ∂μ := by
        apply lintegral_congr_ae
        filter_upwards [hlim] with x hx
        exact ((ENNReal.continuous_ofReal.tendsto _).comp hx).liminf_eq.symm
      _ ≤ Filter.liminf (fun n => ∫⁻ x, ENNReal.ofReal (F n x) ∂μ) Filter.atTop :=
        lintegral_liminf_le' (fun n => (hF n).aestronglyMeasurable.aemeasurable.ennreal_ofReal)
      _ ≤ _ := by
        apply Filter.liminf_le_of_frequently_le'
        apply Filter.Eventually.frequently
        apply Filter.Eventually.of_forall
        intro n
        rw [← ofReal_integral_eq_lintegral_ofReal (hF n) (Filter.Eventually.of_forall (hFn n))]
        exact ENNReal.ofReal_le_ofReal (hbound n)
  have hgi : Integrable g μ := ⟨hg, (hasFiniteIntegral_iff_ofReal
    (Filter.Eventually.of_forall hgn)).mpr (H.trans_lt ENNReal.ofReal_lt_top)⟩
  refine ⟨hgi, ?_⟩
  have hC : 0 ≤ C := (integral_nonneg (hFn 0)).trans (hbound 0)
  rw [← ofReal_integral_eq_lintegral_ofReal hgi (Filter.Eventually.of_forall hgn)] at H
  exact (ENNReal.ofReal_le_ofReal_iff hC).mp H

section
variable {ι E : Type*} [Fintype ι] [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- Initial-time limit of the actual geometric product for bounded continuous
data. No positive-mass or support hypothesis is needed for this pointwise step. -/
theorem tendsto_geometricHeatProduct_initial_sq
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Continuous (f i)) (hc : ∀ i, 0 ≤ c i)
    (B : ι → ℝ) (hB : ∀ i y, |f i y| ≤ B i) (x : E) :
    Filter.Tendsto (fun s : ℝ => geometricHeatProduct f c u (s^2) x) (𝓝[>] (0:ℝ))
      (𝓝 (∏ i, f i ⟪u i,x⟫ ^ c i)) := by
  exact tendsto_finsetProd _ (fun i _ =>
    (tendsto_heatFlow_initial_sq (hf i).measurable (B i) (hB i) (hf i).continuousAt).rpow_const
      (Or.inr (hc i)))

/-- Geometric Brascamp–Lieb on the whole plane for bounded continuous,
interval-supported, nonnegative data of positive mass. These are explicitly
intermediate data hypotheses; arbitrary L1 density is not asserted here. -/
theorem geometric_brascamp_lieb_bounded_continuous
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hcont : ∀ i, Continuous (f i))
    (hn : ∀ i y, 0 ≤ f i y) (hm : ∀ i, 0 < ∫ y : ℝ, f i y)
    (hc : ∀ i, 0 ≤ c i) (hu : ∀ i, ‖u i‖ = 1) (hframe : IsWeightedFrame c u)
    (R : ℝ) (hR : 0 ≤ R) (hsupport : ∀ i y, f i y ≠ 0 → |y| ≤ R)
    (B : ι → ℝ) (hB : ∀ i y, |f i y| ≤ B i)
    (b : OrthonormalBasis (Fin 2) ℝ E) :
    Integrable (fun z : ℝ × ℝ => ∏ i, f i ⟪u i,planePoint b z⟫ ^ c i) (volume.prod volume) ∧
    (∫ z : ℝ × ℝ, ∏ i, f i ⟪u i,planePoint b z⟫ ^ c i ∂volume.prod volume) ≤
      ∏ i, (∫ y : ℝ, f i y) ^ c i := by
  let s : ℕ → ℝ := fun n => ((n:ℝ)+1)⁻¹
  have hs : ∀ n, 0 < s n := fun n => by dsimp [s]; positivity
  have hslim : Filter.Tendsto s Filter.atTop (𝓝[>] (0:ℝ)) := by
    apply tendsto_nhdsWithin_iff.mpr
    exact ⟨tendsto_inv_atTop_zero.comp
      (Filter.tendsto_atTop_add_const_right _ _ tendsto_natCast_atTop_atTop),
      Filter.Eventually.of_forall hs⟩
  let F : ℕ → ℝ × ℝ → ℝ := fun n z => geometricHeatProduct f c u ((s n)^2) (planePoint b z)
  let g : ℝ × ℝ → ℝ := fun z => ∏ i, f i ⟪u i,planePoint b z⟫ ^ c i
  have hg : Continuous g := by
    apply continuous_finsetProd
    intro i _
    exact (continuous_rpow_const (hc i)).comp ((hcont i).comp
      (continuous_const.inner (continuous_planePoint b)))
  apply integrable_and_integral_le_of_nonneg_limit (volume.prod volume) F g _
  · intro n
    exact integrable_geometricHeatProduct_plane f c u hf hn hm hc hframe R hR hsupport b
      (sq_pos_of_pos (hs n))
  · intro n z
    exact Finset.prod_nonneg (fun i _ => rpow_nonneg
      (heatFlow_nonneg (hn i) (sq_pos_of_pos (hs n)) _) _)
  · exact hg.aestronglyMeasurable
  · intro z
    exact Finset.prod_nonneg (fun i _ => rpow_nonneg (hn i _) _)
  · apply Filter.Eventually.of_forall
    intro z
    exact (tendsto_geometricHeatProduct_initial_sq f c u hcont hc B hB (planePoint b z)).comp hslim
  · intro n
    exact integral_geometricHeatProduct_le_mass f c u hf hn hm hc hu hframe R hR hsupport b
      (sq_pos_of_pos (hs n))

/-- Interval support and continuity supply the boundedness used in the
approximate-identity proof; it is not an extra data restriction. -/
theorem geometric_brascamp_lieb_continuous_compact
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hcont : ∀ i, Continuous (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hm : ∀ i, 0 < ∫ y : ℝ, f i y)
    (hc : ∀ i, 0 ≤ c i) (hu : ∀ i, ‖u i‖ = 1) (hframe : IsWeightedFrame c u)
    (R : ℝ) (hR : 0 ≤ R) (hsupport : ∀ i y, f i y ≠ 0 → |y| ≤ R)
    (b : OrthonormalBasis (Fin 2) ℝ E) :
    Integrable (fun z : ℝ × ℝ => ∏ i, f i ⟪u i,planePoint b z⟫ ^ c i) (volume.prod volume) ∧
    (∫ z : ℝ × ℝ, ∏ i, f i ⟪u i,planePoint b z⟫ ^ c i ∂volume.prod volume) ≤
      ∏ i, (∫ y : ℝ, f i y) ^ c i := by
  have hcompact : ∀ i, HasCompactSupport (f i) := by
    intro i
    apply HasCompactSupport.of_support_subset_isCompact isCompact_Icc
    intro y hy
    exact abs_le.mp (hsupport i y hy)
  choose B hB using fun i => (hcompact i).exists_bound_of_continuous (hcont i)
  exact geometric_brascamp_lieb_bounded_continuous f c u
    (fun i => (hcont i).integrable_of_hasCompactSupport (hcompact i)) hcont hn hm hc hu hframe
    R hR hsupport B hB b

end
end ChowlaCosine.Beckner

-- SOURCE ChowlaCosine/Beckner/HeatFlowDensity.lean

/-! # Null-set pullback and nonnegative compact approximation for planar frames -/

open MeasureTheory Real
open scoped BigOperators Topology RealInnerProductSpace

namespace ChowlaCosine.Beckner
set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 400000

/-- Null sets pull back to planar null sets along every nonzero linear form,
including forms with one vanishing coefficient. The predicate need not itself
be measurable: a measurable null hull is used before Fubini. -/
theorem ae_plane_linear {P : ℝ → Prop} (hP : ∀ᵐ x : ℝ, P x)
    (a b : ℝ) (hab : a ≠ 0 ∨ b ≠ 0) :
    ∀ᵐ z : ℝ × ℝ ∂volume.prod volume, P (a*z.1+b*z.2) := by
  obtain ⟨N, hN, hNm, hNzero⟩ := exists_measurable_superset_of_null (ae_iff.mp hP)
  have hNae : ∀ᵐ x : ℝ, x ∉ N := by
    rw [ae_iff]
    simpa using hNzero
  have hright : ∀ a b : ℝ, b ≠ 0 →
      ∀ᵐ z : ℝ × ℝ ∂volume.prod volume, a*z.1+b*z.2 ∉ N := by
    intro a b hb
    have hmeas : Measurable (fun z : ℝ × ℝ => a*z.1+b*z.2) := by fun_prop
    apply (Measure.ae_prod_iff_ae_ae (hNm.compl.preimage hmeas)).mpr
    apply Filter.Eventually.of_forall
    intro x
    simpa only [Function.comp_def, smul_eq_mul, Set.mem_compl_iff] using
      ((quasiMeasurePreserving_add_left volume (a*x)).comp
        (Measure.quasiMeasurePreserving_smul volume hb)).ae hNae
  have H : ∀ᵐ z : ℝ × ℝ ∂volume.prod volume, a*z.1+b*z.2 ∉ N := by
    rcases hab with ha | hb
    · have H := (Measure.measurePreserving_swap (μ := (volume : Measure ℝ))
        (ν := (volume : Measure ℝ))).quasiMeasurePreserving.ae
        (hright b a ha)
      simpa only [Prod.fst_swap, Prod.snd_swap, add_comm] using H
    · exact hright a b hb
  filter_upwards [H] with z hz
  by_contra h
  exact hz (hN h)

/-- The planar linear form of every nonzero vector respects almost-everywhere
statements. No assertion about an arbitrary measurable pullback is assumed. -/
theorem ae_plane_inner {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    (b : OrthonormalBasis (Fin 2) ℝ E) (u : E) (hu : u ≠ 0)
    {P : ℝ → Prop} (hP : ∀ᵐ x : ℝ, P x) :
    ∀ᵐ z : ℝ × ℝ ∂volume.prod volume, P ⟪u,planePoint b z⟫ := by
  have hab : ⟪u,b 0⟫ ≠ 0 ∨ ⟪u,b 1⟫ ≠ 0 := by
    by_contra h
    push Not at h
    have H := b.sum_sq_inner_left u
    simp only [Fin.sum_univ_two, h.1, h.2, zero_pow (by decide : 2 ≠ 0), zero_add] at H
    exact hu (norm_eq_zero.mp (sq_eq_zero_iff.mp H.symm))
  have H := ae_plane_linear hP ⟪u,b 0⟫ ⟪u,b 1⟫ hab
  simpa only [planePoint, inner_add_right, real_inner_smul_right, mul_comm] using H

/-- A fixed nonnegative continuous compact datum of strictly positive mass. -/
theorem exists_positive_compact_datum :
    ∃ φ : ℝ → ℝ, Continuous φ ∧ HasCompactSupport φ ∧ (∀ x, 0 ≤ φ x) ∧
      0 < ∫ x : ℝ, φ x := by
  let φ : ℝ → ℝ := fun x => max (1-|x|) 0
  have hcont : Continuous φ := by dsimp [φ]; fun_prop
  have hcompact : HasCompactSupport φ := by
    apply HasCompactSupport.intro (K := Set.Icc (-1) 1) isCompact_Icc
    intro x hx
    dsimp [φ]
    rw [max_eq_right]
    have H : 1 ≤ |x| := by
      by_contra h
      exact hx (abs_le.mp (le_of_lt (lt_of_not_ge h)))
    linarith
  have hn : ∀ x, 0 ≤ φ x := fun x => le_max_right _ _
  refine ⟨φ, hcont, hcompact, hn, ?_⟩
  exact hcont.integral_pos_of_hasCompactSupport_nonneg_nonzero hcompact hn (x := 0)
    (by norm_num [φ])

/-- Approximate every nonnegative L1 datum, including the zero datum, by
nonnegative continuous compact data of strictly positive mass. -/
theorem exists_positive_compact_approximation {f : ℝ → ℝ} (hf : Integrable f)
    (hn : ∀ y, 0 ≤ f y) {ε : ℝ} (hε : 0 < ε) :
    ∃ g : ℝ → ℝ, Continuous g ∧ HasCompactSupport g ∧ (∀ y, 0 ≤ g y) ∧
      0 < ∫ y : ℝ, g y ∧ (∫ y : ℝ, ‖f y-g y‖) ≤ ε := by
  obtain ⟨φ,hφc,hφs,hφn,hφm⟩ := exists_positive_compact_datum
  have hφi : Integrable φ := hφc.integrable_of_hasCompactSupport hφs
  obtain ⟨g,hgs,herr,hgc,hgi⟩ := hf.exists_hasCompactSupport_integral_sub_le (half_pos hε)
  let δ : ℝ := ε/(2*((∫ y : ℝ, φ y)+1))
  have hδ : 0 < δ := by dsimp [δ]; positivity
  let G : ℝ → ℝ := fun y => |g y|+δ*φ y
  have hGc : Continuous G := hgc.abs.add (continuous_const.mul hφc)
  have hGs : HasCompactSupport G := hgs.abs.add (hφs.mul_left (f := fun _ => δ))
  have hGi : Integrable G := hGc.integrable_of_hasCompactSupport hGs
  have hGn : ∀ y, 0 ≤ G y := fun y => add_nonneg (abs_nonneg _) (mul_nonneg hδ.le (hφn y))
  have hGm : 0 < ∫ y : ℝ, G y := by
    have he : (∫ y : ℝ, G y) = (∫ y : ℝ, |g y|)+(∫ y : ℝ, δ*φ y) :=
      integral_add (show Integrable (fun y => |g y|) from hgi.norm) (hφi.const_mul δ)
    rw [he, integral_const_mul]
    exact add_pos_of_nonneg_of_pos (integral_nonneg (fun _ => abs_nonneg _)) (mul_pos hδ hφm)
  refine ⟨G,hGc,hGs,hGn,hGm,?_⟩
  have hp : ∀ y, ‖f y-G y‖ ≤ ‖f y-g y‖+δ*φ y := by
    intro y
    change abs (f y-(abs (g y)+δ*φ y)) ≤ |f y-g y|+δ*φ y
    calc
      _ = abs ((f y-abs (g y))-δ*φ y) := congrArg abs (by ring)
      _ ≤ abs (f y-abs (g y))+|δ*φ y| := abs_sub _ _
      _ ≤ |f y-g y|+δ*φ y := by
        rw [abs_of_nonneg (mul_nonneg hδ.le (hφn y))]
        have hd : abs (f y-abs (g y)) ≤ |f y-g y| := by
          simpa only [abs_of_nonneg (hn y)] using abs_abs_sub_abs_le_abs_sub (f y) (g y)
        exact add_le_add hd le_rfl
  have H := integral_mono (hf.sub hGi).norm ((hf.sub hgi).norm.add (hφi.const_mul δ)) hp
  have he : (∫ y : ℝ, ‖f y-g y‖+δ*φ y) =
      (∫ y : ℝ, ‖f y-g y‖)+(∫ y : ℝ, δ*φ y) :=
    integral_add (show Integrable (fun y => ‖f y-g y‖) from (hf.sub hgi).norm) (hφi.const_mul δ)
  change (∫ y : ℝ, ‖f y-G y‖) ≤ ∫ y : ℝ, ‖f y-g y‖+δ*φ y at H
  rw [he, integral_const_mul] at H
  apply H.trans
  have hd : δ*(∫ y : ℝ, φ y) ≤ ε/2 := by
    dsimp [δ]
    rw [div_mul_eq_mul_div]
    apply (div_le_iff₀ (by positivity : 0 < 2*((∫ y : ℝ, φ y)+1))).mpr
    nlinarith only [hε.le]
  linarith only [H, herr, hd]

/-- Positive compact continuous approximation with both almost-everywhere
convergence and convergence of the actual masses. No positive target mass is
assumed, so the zero-mass case is included. -/
theorem exists_positive_compact_approximation_seq {f : ℝ → ℝ} (hf : Integrable f)
    (hn : ∀ y, 0 ≤ f y) :
    ∃ g : ℕ → ℝ → ℝ,
      (∀ n, Continuous (g n)) ∧ (∀ n, HasCompactSupport (g n)) ∧
      (∀ n y, 0 ≤ g n y) ∧ (∀ n, 0 < ∫ y : ℝ, g n y) ∧
      (∀ᵐ y : ℝ, Filter.Tendsto (fun n => g n y) Filter.atTop (𝓝 (f y))) ∧
      Filter.Tendsto (fun n => ∫ y : ℝ, g n y) Filter.atTop (𝓝 (∫ y : ℝ, f y)) := by
  choose g hgc hgs hgn hgm hgerr using fun n : ℕ =>
    exists_positive_compact_approximation hf hn
      (by positivity : 0 < ((n:ℝ)+1)⁻¹)
  have hgi : ∀ n, Integrable (g n) := fun n => (hgc n).integrable_of_hasCompactSupport (hgs n)
  have hreal : Filter.Tendsto (fun n => ∫ y : ℝ, ‖g n y-f y‖) Filter.atTop (𝓝 (0:ℝ)) := by
    apply squeeze_zero (fun n => integral_nonneg (fun _ => norm_nonneg _))
      (fun n => by simpa only [norm_sub_rev] using hgerr n)
    exact tendsto_inv_atTop_zero.comp
      (Filter.tendsto_atTop_add_const_right _ _ tendsto_natCast_atTop_atTop)
  have hLp : Filter.Tendsto (fun n => eLpNorm (g n-f) 1) Filter.atTop (𝓝 0) := by
    have H := ENNReal.continuous_ofReal.tendsto (0:ℝ) |>.comp hreal
    simp only [ENNReal.ofReal_zero] at H
    convert H using 1
    funext n
    rw [eLpNorm_one_eq_lintegral_enorm]
    exact (ofReal_integral_norm_eq_lintegral_enorm ((hgi n).sub hf)).symm
  have hinmeasure := tendstoInMeasure_of_tendsto_eLpNorm (by norm_num : (1:ENNReal) ≠ 0)
    (fun n => (hgi n).aestronglyMeasurable) hf.aestronglyMeasurable hLp
  obtain ⟨ns,hns,hlim⟩ := hinmeasure.exists_seq_tendsto_ae
  refine ⟨fun n => g (ns n), (fun n => hgc (ns n)), (fun n => hgs (ns n)),
    (fun n => hgn (ns n)), (fun n => hgm (ns n)), hlim, ?_⟩
  exact (tendsto_integral_of_L1' f hf.aestronglyMeasurable
    (Filter.Eventually.of_forall hgi) hLp).comp hns.tendsto_atTop

/-- A common finite support radius for any finite family of compact data. -/
theorem exists_common_support_radius {ι : Type*} [Fintype ι]
    (g : ι → ℝ → ℝ) (hg : ∀ i, HasCompactSupport (g i)) :
    ∃ R : ℝ, 0 ≤ R ∧ ∀ i y, g i y ≠ 0 → |y| ≤ R := by
  choose r hr using fun i => (hg i).isBounded.exists_norm_le
  refine ⟨∑ i, |r i|, Finset.sum_nonneg (fun _ _ => abs_nonneg _), ?_⟩
  intro i y hy
  exact (hr i y (subset_tsupport (g i) hy)).trans
    ((le_abs_self _).trans (Finset.single_le_sum (fun j _ => abs_nonneg (r j)) (Finset.mem_univ i)))

/-- Fatou with converging upper bounds, retaining finiteness of the limiting
integral. The upper bounds may tend to zero. -/
theorem integrable_and_integral_le_of_nonneg_limit_bounds
    {α : Type*} [MeasurableSpace α] (μ : Measure α)
    (F : ℕ → α → ℝ) (g : α → ℝ) (C : ℕ → ℝ) (L : ℝ)
    (hF : ∀ n, Integrable (F n) μ) (hFn : ∀ n x, 0 ≤ F n x)
    (hg : AEStronglyMeasurable g μ) (hgn : ∀ x, 0 ≤ g x)
    (hlim : ∀ᵐ x ∂μ, Filter.Tendsto (fun n => F n x) Filter.atTop (𝓝 (g x)))
    (hbound : ∀ n, (∫ x, F n x ∂μ) ≤ C n)
    (hC : Filter.Tendsto C Filter.atTop (𝓝 L)) :
    Integrable g μ ∧ (∫ x, g x ∂μ) ≤ L := by
  have H : (∫⁻ x, ENNReal.ofReal (g x) ∂μ) ≤ ENNReal.ofReal L := by
    calc
      _ = ∫⁻ x, Filter.liminf (fun n => ENNReal.ofReal (F n x)) Filter.atTop ∂μ := by
        apply lintegral_congr_ae
        filter_upwards [hlim] with x hx
        exact ((ENNReal.continuous_ofReal.tendsto _).comp hx).liminf_eq.symm
      _ ≤ Filter.liminf (fun n => ∫⁻ x, ENNReal.ofReal (F n x) ∂μ) Filter.atTop :=
        lintegral_liminf_le' (fun n => (hF n).aestronglyMeasurable.aemeasurable.ennreal_ofReal)
      _ ≤ Filter.liminf (fun n => ENNReal.ofReal (C n)) Filter.atTop := by
        have Hn : ∀ n, (∫⁻ x, ENNReal.ofReal (F n x) ∂μ) ≤ ENNReal.ofReal (C n) := by
          intro n
          rw [← ofReal_integral_eq_lintegral_ofReal (hF n) (Filter.Eventually.of_forall (hFn n))]
          exact ENNReal.ofReal_le_ofReal (hbound n)
        exact Filter.liminf_le_liminf (Filter.Eventually.of_forall Hn)
      _ = _ := ((ENNReal.continuous_ofReal.tendsto _).comp hC).liminf_eq
  have hgi : Integrable g μ := ⟨hg, (hasFiniteIntegral_iff_ofReal
    (Filter.Eventually.of_forall hgn)).mpr (H.trans_lt ENNReal.ofReal_lt_top)⟩
  refine ⟨hgi, ?_⟩
  have hL : 0 ≤ L := ge_of_tendsto hC
    (Filter.Eventually.of_forall (fun n => (integral_nonneg (hFn n)).trans (hbound n)))
  rw [← ofReal_integral_eq_lintegral_ofReal hgi (Filter.Eventually.of_forall hgn)] at H
  exact (ENNReal.ofReal_le_ofReal_iff hL).mp H

section
variable {ι E : Type*} [Fintype ι] [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- Geometric Brascamp–Lieb on the whole plane for arbitrary nonnegative L1
data. Compact support, continuity, boundedness and positive mass are all removed;
zero masses and zero weights are included with the usual real-power convention. -/
theorem geometric_brascamp_lieb
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hc : ∀ i, 0 ≤ c i) (hu : ∀ i, ‖u i‖ = 1) (hframe : IsWeightedFrame c u)
    (b : OrthonormalBasis (Fin 2) ℝ E) :
    Integrable (fun z : ℝ × ℝ => ∏ i, f i ⟪u i,planePoint b z⟫ ^ c i) (volume.prod volume) ∧
    (∫ z : ℝ × ℝ, ∏ i, f i ⟪u i,planePoint b z⟫ ^ c i ∂volume.prod volume) ≤
      ∏ i, (∫ y : ℝ, f i y) ^ c i := by
  choose g hgc hgs hgn hgm hglim hgmass using fun i =>
    exists_positive_compact_approximation_seq (hf i) (hn i)
  let F : ℕ → ℝ × ℝ → ℝ := fun n z => ∏ i, g i n ⟪u i,planePoint b z⟫ ^ c i
  let G : ℝ × ℝ → ℝ := fun z => ∏ i, f i ⟪u i,planePoint b z⟫ ^ c i
  let C : ℕ → ℝ := fun n => ∏ i, (∫ y : ℝ, g i n y) ^ c i
  have hFc : ∀ n, Continuous (F n) := by
    intro n
    apply continuous_finsetProd
    intro i _
    exact (continuous_rpow_const (hc i)).comp ((hgc i n).comp
      (continuous_const.inner (continuous_planePoint b)))
  have hFbound : ∀ n, Integrable (F n) (volume.prod volume) ∧
      (∫ z : ℝ × ℝ, F n z ∂volume.prod volume) ≤ C n := by
    intro n
    obtain ⟨R,hR,hRs⟩ := exists_common_support_radius (fun i => g i n) (fun i => hgs i n)
    exact geometric_brascamp_lieb_continuous_compact (fun i => g i n) c u (fun i => hgc i n)
      (fun i => hgn i n) (fun i => hgm i n) hc hu hframe R hR hRs b
  have hlim : ∀ᵐ z : ℝ × ℝ ∂volume.prod volume,
      Filter.Tendsto (fun n => F n z) Filter.atTop (𝓝 (G z)) := by
    have H : ∀ᵐ z : ℝ × ℝ ∂volume.prod volume, ∀ i,
        Filter.Tendsto (fun n => g i n ⟪u i,planePoint b z⟫) Filter.atTop
          (𝓝 (f i ⟪u i,planePoint b z⟫)) := by
      rw [ae_all_iff]
      intro i
      exact ae_plane_inner b (u i) (by intro hi; simpa [hi] using hu i) (hglim i)
    filter_upwards [H] with z hz
    exact tendsto_finsetProd _ (fun i _ => (hz i).rpow_const (Or.inr (hc i)))
  have hGmeas : AEStronglyMeasurable G (volume.prod volume) :=
    aestronglyMeasurable_of_tendsto_ae _ (fun n => (hFc n).aestronglyMeasurable) hlim
  exact integrable_and_integral_le_of_nonneg_limit_bounds (volume.prod volume) F G C _
    (fun n => (hFbound n).1)
    (fun n z => Finset.prod_nonneg (fun i _ => rpow_nonneg (hgn i n _) _))
    hGmeas (fun z => Finset.prod_nonneg (fun i _ => rpow_nonneg (hn i _) _)) hlim
    (fun n => (hFbound n).2)
    (tendsto_finsetProd _ (fun i _ => (hgmass i).rpow_const (Or.inr (hc i))))

end
end ChowlaCosine.Beckner


/-! # An explicit two-dimensional frame for the interior Young exponents

The parameters are the three positive complementary weights, of sum one.
This module constructs the frame; the sharp-factor and Lp reduction are separate.
-/

open MeasureTheory Real
open scoped BigOperators Topology RealInnerProductSpace

namespace ChowlaCosine.Beckner
set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

section
variable {ι E : Type*} [Fintype ι] [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- The three scalar entries of a symmetric 2×2 matrix verify the full
bilinear weighted-frame identity, not just its diagonal specialization. -/
theorem isWeightedFrame_plane_of_coefficients
    (b : OrthonormalBasis (Fin 2) ℝ E) (c A B : ι → ℝ)
    (hA : (∑ i, c i * A i ^ 2) = 1) (hB : (∑ i, c i * B i ^ 2) = 1)
    (hAB : (∑ i, c i * (A i * B i)) = 0) :
    IsWeightedFrame c (fun i => planePoint b (A i,B i)) := by
  intro x y
  have he : ∀ i, c i * (⟪planePoint b (A i,B i),x⟫ * ⟪planePoint b (A i,B i),y⟫) =
      (c i*A i^2)*(⟪b 0,x⟫*⟪b 0,y⟫) +
      (c i*B i^2)*(⟪b 1,x⟫*⟪b 1,y⟫) +
      (c i*(A i*B i))*(⟪b 0,x⟫*⟪b 1,y⟫+⟪b 1,x⟫*⟪b 0,y⟫) := by
    intro i
    simp only [planePoint, inner_add_left, real_inner_smul_left]
    ring
  simp_rw [he, Finset.sum_add_distrib, ← Finset.sum_mul, hA, hB, hAB,
    one_mul, zero_mul, add_zero]
  simpa only [Fin.sum_univ_two, real_inner_comm x (b 0), real_inner_comm x (b 1)] using
    b.sum_inner_mul_inner x y

end

/-- Weights cᵢ=1-dᵢ for complementary weights d=(a,b,d), a+b+d=1. -/
def youngFrameWeights (a b d : ℝ) : Fin 3 → ℝ := ![b+d,a+d,a+b]

def youngFrameComplement (a b d : ℝ) : Fin 3 → ℝ := ![a,b,d]

noncomputable def youngFrameFirst (a b d : ℝ) : Fin 3 → ℝ :=
  ![sqrt b/(sqrt (a+b)*sqrt (b+d)), -sqrt a/(sqrt (a+b)*sqrt (a+d)), 0]

noncomputable def youngFrameSecond (a b d : ℝ) : Fin 3 → ℝ :=
  ![sqrt a*sqrt d/(sqrt (a+b)*sqrt (b+d)),
    sqrt b*sqrt d/(sqrt (a+b)*sqrt (a+d)), -1]

/-- Scales relating the three frame forms to x, y and -(x+y). -/
noncomputable def youngFrameScale (a b d : ℝ) : Fin 3 → ℝ :=
  ![sqrt a*sqrt (b+d),sqrt b*sqrt (a+d),sqrt d*sqrt (a+b)]

/-- The actual 2×2 map from frame coordinates to the first two scaled forms. -/
noncomputable def youngFrameMatrix (a b d : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![youngFrameScale a b d 0 * youngFrameFirst a b d 0,
      youngFrameScale a b d 0 * youngFrameSecond a b d 0;
     youngFrameScale a b d 1 * youngFrameFirst a b d 1,
      youngFrameScale a b d 1 * youngFrameSecond a b d 1]

/-- The determinant keeps all scaling factors and has the exact positive value. -/
theorem youngFrameMatrix_det (a b d : ℝ) (ha : 0 < a) (hb : 0 < b) (hd : 0 < d) :
    (youngFrameMatrix a b d).det = sqrt a*sqrt b*sqrt d := by
  have hab : 0 < a+b := add_pos ha hb
  have had : 0 < a+d := add_pos ha hd
  have hbd : 0 < b+d := add_pos hb hd
  have hsnab := (sqrt_pos.mpr hab).ne'
  have hsnad := (sqrt_pos.mpr had).ne'
  have hsnbd := (sqrt_pos.mpr hbd).ne'
  simp [youngFrameMatrix, Matrix.det_fin_two, youngFrameScale, youngFrameFirst, youngFrameSecond]
  field_simp
  simp only [sq_sqrt ha.le, sq_sqrt hb.le, sq_sqrt hd.le,
    sq_sqrt hab.le, sq_sqrt had.le, sq_sqrt hbd.le]
  ring

/-- Exact dependence of the three scaled coordinate forms. -/
theorem youngFrame_coordinate_relation (a b d : ℝ) (ha : 0 < a) (hb : 0 < b) (hd : 0 < d) :
    (∑ i, youngFrameScale a b d i * youngFrameFirst a b d i) = 0 ∧
    (∑ i, youngFrameScale a b d i * youngFrameSecond a b d i) = 0 := by
  have hab : 0 < a+b := add_pos ha hb
  have had : 0 < a+d := add_pos ha hd
  have hbd : 0 < b+d := add_pos hb hd
  have hsnab := (sqrt_pos.mpr hab).ne'
  have hsnad := (sqrt_pos.mpr had).ne'
  have hsnbd := (sqrt_pos.mpr hbd).ne'
  simp [Fin.sum_univ_three, youngFrameScale, youngFrameFirst, youngFrameSecond]
  constructor
  · field_simp
    ring
  · field_simp
    simp only [sq_sqrt ha.le, sq_sqrt hb.le, sq_sqrt hd.le,
      sq_sqrt hab.le, sq_sqrt had.le, sq_sqrt hbd.le]
    ring

/-- One scalar factor in the determinant/Lp cancellation, with both
complementary weights displayed explicitly. -/
theorem young_scalar_factor {c d : ℝ} (hc : 0 < c) (hd : 0 < d) (hsum : c+d=1) :
    sqrt d / (sqrt d*sqrt c)^c = d^(d/2) / c^(c/2) := by
  rw [sqrt_eq_rpow, sqrt_eq_rpow, mul_rpow (rpow_pos_of_pos hd _).le (rpow_pos_of_pos hc _).le,
    ← rpow_mul hd.le, ← rpow_mul hc.le]
  calc
    _ = (d^(1/2:ℝ) / d^((1/2:ℝ)*c)) / c^((1/2:ℝ)*c) := by
      rw [div_div]
    _ = d^((1/2:ℝ)-(1/2:ℝ)*c) / c^((1/2:ℝ)*c) := by rw [← rpow_sub hd]
    _ = _ := by
      congr 1
      · congr 1
        linarith only [hsum]
      · congr 1
        ring

/-- In exponent notation p=1/c and p'=1/d, this is precisely Beckner's A_p. -/
theorem young_scalar_factor_beckner {c d : ℝ} (hc : 0 < c) (hd : 0 < d) (hsum : c+d=1) :
    sqrt d / (sqrt d*sqrt c)^c = sqrt ((1/c)^c / (1/d)^d) := by
  rw [young_scalar_factor hc hd hsum]
  rw [one_div, one_div, inv_rpow hc.le, inv_rpow hd.le, inv_div_inv,
    sqrt_eq_rpow, div_rpow (rpow_pos_of_pos hd _).le (rpow_pos_of_pos hc _).le,
    ← rpow_mul hd.le, ← rpow_mul hc.le]
  congr 1 <;> congr 1 <;> ring

/-- The exact determinant divided by all three dilation factors is Beckner's
product A_p A_q A_{r'}, with pᵢ=1/cᵢ and pᵢ'=1/dᵢ. -/
theorem youngFrame_sharp_factor (a b d : ℝ) (ha : 0 < a) (hb : 0 < b) (hd : 0 < d)
    (hsum : a+b+d=1) :
    (youngFrameMatrix a b d).det /
      (∏ i, youngFrameScale a b d i ^ youngFrameWeights a b d i) =
    ∏ i, sqrt ((1/youngFrameWeights a b d i)^youngFrameWeights a b d i /
      (1/youngFrameComplement a b d i)^youngFrameComplement a b d i) := by
  have hci : ∀ i, 0 < youngFrameWeights a b d i := by
    intro i
    fin_cases i <;> simp [youngFrameWeights] <;> positivity
  have hdi : ∀ i, 0 < youngFrameComplement a b d i := by
    intro i
    fin_cases i <;> simp [youngFrameComplement] <;> assumption
  have hsum' : ∀ i, youngFrameWeights a b d i + youngFrameComplement a b d i = 1 := by
    intro i
    fin_cases i <;> simp [youngFrameWeights, youngFrameComplement] <;> linarith only [hsum]
  have hscale : ∀ i, youngFrameScale a b d i =
      sqrt (youngFrameComplement a b d i) * sqrt (youngFrameWeights a b d i) := by
    intro i
    fin_cases i <;> rfl
  calc
    _ = ∏ i, sqrt (youngFrameComplement a b d i) /
        youngFrameScale a b d i ^ youngFrameWeights a b d i := by
      rw [Finset.prod_div_distrib, youngFrameMatrix_det a b d ha hb hd]
      congr 1
      simp [Fin.prod_univ_three, youngFrameComplement]
    _ = _ := by
      apply Finset.prod_congr rfl
      intro i _
      rw [hscale]
      exact young_scalar_factor_beckner (hci i) (hdi i) (hsum' i)

/-- The exact 2×2 coefficient identities for all interior Young triples. -/
theorem youngFrame_matrix (a b d : ℝ) (ha : 0 < a) (hb : 0 < b) (hd : 0 < d)
    (hsum : a+b+d=1) :
    (∑ i, youngFrameWeights a b d i * youngFrameFirst a b d i ^ 2) = 1 ∧
    (∑ i, youngFrameWeights a b d i * youngFrameSecond a b d i ^ 2) = 1 ∧
    (∑ i, youngFrameWeights a b d i *
      (youngFrameFirst a b d i * youngFrameSecond a b d i)) = 0 := by
  have hab : 0 < a+b := add_pos ha hb
  have had : 0 < a+d := add_pos ha hd
  have hbd : 0 < b+d := add_pos hb hd
  have hsab := sq_sqrt hab.le
  have hsad := sq_sqrt had.le
  have hsbd := sq_sqrt hbd.le
  have hsa := sq_sqrt ha.le
  have hsb := sq_sqrt hb.le
  have hsd := sq_sqrt hd.le
  have hsnab := (sqrt_pos.mpr hab).ne'
  have hsnad := (sqrt_pos.mpr had).ne'
  have hsnbd := (sqrt_pos.mpr hbd).ne'
  simp [Fin.sum_univ_three, youngFrameWeights, youngFrameFirst, youngFrameSecond,
    Matrix.vecHead, Matrix.vecTail, Function.comp_def]
  constructor
  · field_simp
    simp only [hsab, hsad, hsbd, hsa, hsb]
    ring
  constructor
  · field_simp
    simp only [hsab, hsad, hsbd, hsa, hsb, hsd]
    rw [show d=1-a-b by linarith only [hsum]]
    ring
  · field_simp
    simp only [hsab, hsad, hsbd]
    ring

section
variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

noncomputable def youngFrame (basis : OrthonormalBasis (Fin 2) ℝ E) (a b d : ℝ) : Fin 3 → E :=
  fun i => planePoint basis (youngFrameFirst a b d i, youngFrameSecond a b d i)

/-- The explicit vectors satisfy the whole-space bilinear frame identity. -/
theorem youngFrame_isWeightedFrame (basis : OrthonormalBasis (Fin 2) ℝ E)
    (a b d : ℝ) (ha : 0 < a) (hb : 0 < b) (hd : 0 < d) (hsum : a+b+d=1) :
    IsWeightedFrame (youngFrameWeights a b d) (youngFrame basis a b d) := by
  obtain ⟨hA,hB,hAB⟩ := youngFrame_matrix a b d ha hb hd hsum
  exact isWeightedFrame_plane_of_coefficients basis _ _ _ hA hB hAB

/-- Every one of the three explicit vectors is a unit vector. -/
theorem youngFrame_unit (basis : OrthonormalBasis (Fin 2) ℝ E)
    (a b d : ℝ) (ha : 0 < a) (hb : 0 < b) (hd : 0 < d) (hsum : a+b+d=1) :
    ∀ i, ‖youngFrame basis a b d i‖ = 1 := by
  have hab : 0 < a+b := add_pos ha hb
  have had : 0 < a+d := add_pos ha hd
  have hbd : 0 < b+d := add_pos hb hd
  have hcoords : ∀ i, youngFrameFirst a b d i ^ 2 + youngFrameSecond a b d i ^ 2 = 1 := by
    intro i
    fin_cases i <;>
      simp [youngFrameFirst, youngFrameSecond, div_pow, mul_pow,
        sq_sqrt ha.le, sq_sqrt hb.le, sq_sqrt hd.le, sq_sqrt hab.le, sq_sqrt had.le, sq_sqrt hbd.le]
    all_goals
      field_simp
      rw [show d=1-a-b by linarith only [hsum]]
      ring
  intro i
  have H := norm_planePoint_sq basis (youngFrameFirst a b d i,youngFrameSecond a b d i)
  rw [hcoords i] at H
  change ‖youngFrame basis a b d i‖^2 = 1 at H
  nlinarith only [H, norm_nonneg (youngFrame basis a b d i)]

/-- The scaled frame vectors have exactly the dependence required for the
convolution trilinear form. -/
theorem youngFrame_relation (basis : OrthonormalBasis (Fin 2) ℝ E)
    (a b d : ℝ) (ha : 0 < a) (hb : 0 < b) (hd : 0 < d) :
    (∑ i, youngFrameScale a b d i • youngFrame basis a b d i) = 0 := by
  obtain ⟨hA,hB⟩ := youngFrame_coordinate_relation a b d ha hb hd
  simp only [youngFrame, planePoint, smul_add, smul_smul, Finset.sum_add_distrib,
    ← Finset.sum_smul, smul_eq_mul, hA, hB, zero_smul, zero_add]

/-- Applying the unrestricted geometric theorem to this concrete Young frame.
This is a geometric integral theorem; Lp and sharp-factor cancellation are not
implicit in its conclusion. -/
theorem geometric_brascamp_lieb_youngFrame
    (basis : OrthonormalBasis (Fin 2) ℝ E) (a b d : ℝ)
    (ha : 0 < a) (hb : 0 < b) (hd : 0 < d) (hsum : a+b+d=1)
    (f : Fin 3 → ℝ → ℝ) (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y) :
    Integrable (fun z : ℝ × ℝ => ∏ i,
      f i ⟪youngFrame basis a b d i,planePoint basis z⟫ ^ youngFrameWeights a b d i)
      (volume.prod volume) ∧
    (∫ z : ℝ × ℝ, ∏ i,
      f i ⟪youngFrame basis a b d i,planePoint basis z⟫ ^ youngFrameWeights a b d i
      ∂volume.prod volume) ≤ ∏ i, (∫ y : ℝ, f i y) ^ youngFrameWeights a b d i := by
  apply geometric_brascamp_lieb f (youngFrameWeights a b d) (youngFrame basis a b d) hf hn
  · intro i
    fin_cases i <;> simp [youngFrameWeights] <;> positivity
  · exact youngFrame_unit basis a b d ha hb hd hsum
  · exact youngFrame_isWeightedFrame basis a b d ha hb hd hsum

end
end ChowlaCosine.Beckner
#print axioms ChowlaCosine.Beckner.weightedFrame_sum_weights
#print axioms ChowlaCosine.Beckner.geometricHeatProduct_rescale
#print axioms ChowlaCosine.Beckner.rescaled_heatFlow_gaussian_bound
#print axioms ChowlaCosine.Beckner.integrable_plane_gaussian
#print axioms ChowlaCosine.Beckner.integral_plane_gaussian
#print axioms ChowlaCosine.Beckner.integral_plane_dilate
#print axioms ChowlaCosine.Beckner.planePoint_smul
#print axioms ChowlaCosine.Beckner.frame_heatKernel_product
#print axioms ChowlaCosine.Beckner.integral_frame_heatKernel_product
#print axioms ChowlaCosine.Beckner.tendsto_integral_rescaled_geometricHeatProduct
#print axioms ChowlaCosine.Beckner.tendsto_integral_geometricHeatProduct_sq
#print axioms ChowlaCosine.Beckner.tendsto_integral_geometricHeatProduct
#print axioms ChowlaCosine.Beckner.integral_geometricHeatProduct_le_mass
#print axioms ChowlaCosine.Beckner.heatFlow_initial_rescale
#print axioms ChowlaCosine.Beckner.tendsto_heatFlow_initial_sq
#print axioms ChowlaCosine.Beckner.integrable_and_integral_le_of_nonneg_limit
#print axioms ChowlaCosine.Beckner.tendsto_geometricHeatProduct_initial_sq
#print axioms ChowlaCosine.Beckner.geometric_brascamp_lieb_bounded_continuous
#print axioms ChowlaCosine.Beckner.geometric_brascamp_lieb_continuous_compact
#print axioms ChowlaCosine.Beckner.ae_plane_linear
#print axioms ChowlaCosine.Beckner.ae_plane_inner
#print axioms ChowlaCosine.Beckner.exists_positive_compact_datum
#print axioms ChowlaCosine.Beckner.exists_positive_compact_approximation
#print axioms ChowlaCosine.Beckner.exists_positive_compact_approximation_seq
#print axioms ChowlaCosine.Beckner.exists_common_support_radius
#print axioms ChowlaCosine.Beckner.integrable_and_integral_le_of_nonneg_limit_bounds
#print axioms ChowlaCosine.Beckner.geometric_brascamp_lieb
#print axioms ChowlaCosine.Beckner.isWeightedFrame_plane_of_coefficients
#print axioms ChowlaCosine.Beckner.youngFrameMatrix_det
#print axioms ChowlaCosine.Beckner.youngFrame_coordinate_relation
#print axioms ChowlaCosine.Beckner.young_scalar_factor
#print axioms ChowlaCosine.Beckner.young_scalar_factor_beckner
#print axioms ChowlaCosine.Beckner.youngFrame_sharp_factor
#print axioms ChowlaCosine.Beckner.youngFrame_matrix
#print axioms ChowlaCosine.Beckner.youngFrame_isWeightedFrame
#print axioms ChowlaCosine.Beckner.youngFrame_unit
#print axioms ChowlaCosine.Beckner.youngFrame_relation
#print axioms ChowlaCosine.Beckner.geometric_brascamp_lieb_youngFrame
#check @ChowlaCosine.Beckner.tendsto_integral_geometricHeatProduct
#check @ChowlaCosine.Beckner.geometric_brascamp_lieb
#check @ChowlaCosine.Beckner.youngFrame_sharp_factor
