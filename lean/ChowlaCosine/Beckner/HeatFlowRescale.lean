import ChowlaCosine.Beckner.HeatFlowMonotone

/-! # Scalar large-time rescaling for every real L1 datum -/

open MeasureTheory Real
open scoped BigOperators Topology

namespace ChowlaCosine.Beckner
set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

/-- The normalized scalar flow after moving the spatial dilation into the datum. -/
noncomputable def rescaledHeatFlow (f : ℝ → ℝ) (ε x : ℝ) : ℝ :=
  ∫ y : ℝ, f y * heatKernel 1 (x-ε*y)

/-- Dominated convergence in the rescaling parameter; no support or sign restriction. -/
theorem tendsto_rescaledHeatFlow {f : ℝ → ℝ} (hf : Integrable f) (x : ℝ) :
    Filter.Tendsto (fun ε : ℝ => rescaledHeatFlow f ε x) (𝓝 0)
      (𝓝 ((∫ y : ℝ, f y) * heatKernel 1 x)) := by
  let F : ℝ → ℝ → ℝ := fun ε y => f y * heatKernel 1 (x-ε*y)
  let bound := fun y : ℝ => |f y| * (1/sqrt (4*π*1))
  have hmeas : ∀ᶠ ε : ℝ in 𝓝 0, AEStronglyMeasurable (F ε) := by
    apply Filter.Eventually.of_forall
    intro ε
    exact hf.aestronglyMeasurable.mul
      ((continuous_heatKernel 1).comp (by fun_prop : Continuous (fun y : ℝ => x-ε*y))).aestronglyMeasurable
  have hbound : ∀ᶠ ε : ℝ in 𝓝 0, ∀ᵐ y : ℝ, ‖F ε y‖ ≤ bound y := by
    apply Filter.Eventually.of_forall
    intro ε
    apply Filter.Eventually.of_forall
    intro y
    dsimp [F, bound]
    rw [abs_mul, abs_of_pos (heatKernel_pos (by norm_num : (0:ℝ)<1) _)]
    exact mul_le_mul_of_nonneg_left (heatKernel_le (by norm_num : (0:ℝ)<1) _) (abs_nonneg _)
  have hlim : ∀ᵐ y : ℝ, Filter.Tendsto (fun ε => F ε y) (𝓝 0) (𝓝 (f y*heatKernel 1 x)) := by
    apply Filter.Eventually.of_forall
    intro y
    have hc : Continuous (fun ε : ℝ => heatKernel 1 (x-ε*y)) :=
      (continuous_heatKernel 1).comp (by fun_prop)
    simpa only [F, zero_mul, sub_zero] using (hc.tendsto (0 : ℝ)).const_mul (f y)
  have H := tendsto_integral_filter_of_dominated_convergence bound hmeas hbound
    (hf.norm.mul_const _) hlim
  simpa only [rescaledHeatFlow, F, integral_mul_const] using H

/-- Exact scalar heat-kernel dilation, with its normalization factor retained. -/
theorem heatKernel_rescale {s : ℝ} (hs : 0 < s) (x y : ℝ) :
    heatKernel (s^2) (s*x-y) = s⁻¹ * heatKernel 1 (x-s⁻¹*y) := by
  unfold heatKernel gaussian
  rw [sqrt_mul (by positivity : 0 ≤ 4*π), sqrt_sq_eq_abs, abs_of_pos hs]
  have he : -(1/(4*s^2))*(s*x-y)^2 = -(1/(4*1))*(x-s⁻¹*y)^2 := by
    field_simp
    <;> ring
  rw [he]
  simp only [mul_one]
  ring

/-- The rescaled scalar integral is exactly the original heat flow, not a surrogate. -/
theorem rescaledHeatFlow_eq_heatFlow (f : ℝ → ℝ) {s : ℝ} (hs : 0 < s) (x : ℝ) :
    rescaledHeatFlow f s⁻¹ x = s * heatFlow f (s^2) (s*x) := by
  unfold rescaledHeatFlow heatFlow
  simp_rw [heatKernel_rescale hs, show ∀ y : ℝ,
    f y*(s⁻¹*heatKernel 1 (x-s⁻¹*y)) = s⁻¹*(f y*heatKernel 1 (x-s⁻¹*y)) by intro y; ring]
  rw [integral_const_mul, ← mul_assoc, mul_inv_cancel₀ hs.ne', one_mul]

/-- Actual large-time Gaussian asymptotic along the square-time scaling t=s².
It holds for arbitrary signed real L1 data on the whole line. -/
theorem tendsto_heatFlow_large_time {f : ℝ → ℝ} (hf : Integrable f) (x : ℝ) :
    Filter.Tendsto (fun s : ℝ => s * heatFlow f (s^2) (s*x)) Filter.atTop
      (𝓝 ((∫ y : ℝ, f y) * heatKernel 1 x)) := by
  have H := (tendsto_rescaledHeatFlow hf x).comp tendsto_inv_atTop_zero
  apply H.congr'
  filter_upwards [Filter.eventually_gt_atTop (0 : ℝ)] with s hs
  exact rescaledHeatFlow_eq_heatFlow f hs x

/-- The same actual Gaussian asymptotic in the original time variable. -/
theorem tendsto_sqrt_mul_heatFlow {f : ℝ → ℝ} (hf : Integrable f) (x : ℝ) :
    Filter.Tendsto (fun t : ℝ => sqrt t * heatFlow f t (sqrt t*x)) Filter.atTop
      (𝓝 ((∫ y : ℝ, f y) * heatKernel 1 x)) := by
  have H := (tendsto_heatFlow_large_time hf x).comp Real.tendsto_sqrt_atTop
  apply H.congr'
  filter_upwards [Filter.eventually_ge_atTop (0 : ℝ)] with t ht
  change sqrt t * heatFlow f ((sqrt t)^2) (sqrt t*x) = sqrt t * heatFlow f t (sqrt t*x)
  rw [sq_sqrt ht]

end ChowlaCosine.Beckner
