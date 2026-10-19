import ChowlaCosine.Beckner.HeatFlow

/-!
# Dominated time differentiation of real heat flow

No compact-support hypothesis is needed for this L1 smoothing lemma.
It does not yet differentiate the geometric product integral in M4.
-/

open MeasureTheory Real
open scoped ENNReal NNReal Topology

namespace ChowlaCosine.Beckner

set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

noncomputable def heatTimeSlope (t z : ℝ) : ℝ :=
  (z ^ 2 / (4 * t ^ 2) - 1 / (2 * t)) * heatKernel t z

/-- Differentiating the heat convolution in time is valid for every real
integrable initial function, on all positive times and all spatial points. -/
theorem hasDerivAt_heatFlow_time {f : ℝ → ℝ} (hf : Integrable f)
    {t : ℝ} (ht : 0 < t) (x : ℝ) :
    HasDerivAt (fun s => heatFlow f s x) (∫ y : ℝ, f y * heatTimeSlope t (x - y)) t := by
  let a := t / 2
  have ha : 0 < a := by dsimp [a]; positivity
  let C := 3 / (2 * a * Real.sqrt (4 * Real.pi * a))
  let F : ℝ → ℝ → ℝ := fun s y => f y * heatKernel s (x - y)
  let F' : ℝ → ℝ → ℝ := fun s y => f y * heatTimeSlope s (x - y)
  have hnhds : Set.Ioo a (2 * t) ∈ 𝓝 t := Ioo_mem_nhds (by dsimp [a]; linarith) (by linarith)
  have hFmeas : ∀ᶠ s in 𝓝 t, AEStronglyMeasurable (F s) := by
    apply Filter.Eventually.of_forall
    intro s
    exact hf.aestronglyMeasurable.mul
      (((continuous_heatKernel s).comp (continuous_const.sub continuous_id)).aestronglyMeasurable)
  have hFpmeas : AEStronglyMeasurable (F' t) := by
    have hc : Continuous (fun y : ℝ => heatTimeSlope t (x - y)) := by
      unfold heatTimeSlope
      exact (by fun_prop : Continuous (fun y : ℝ => (x - y) ^ 2 / (4 * t ^ 2) - 1 / (2 * t))).mul
        ((continuous_heatKernel t).comp (continuous_const.sub continuous_id))
    exact hf.aestronglyMeasurable.mul hc.aestronglyMeasurable
  have hbound : ∀ᵐ y : ℝ, ∀ s ∈ Set.Ioo a (2 * t), ‖F' s y‖ ≤ ‖f y‖ * C := by
    apply Filter.Eventually.of_forall
    intro y s hs
    have hsp : 0 < s := ha.trans hs.1
    have HB := (heatKernel_time_slope_bound hsp (x - y)).trans
      (heatKernel_time_envelope_le ha hs.1.le)
    dsimp [F', heatTimeSlope, C]
    rw [abs_mul]
    exact mul_le_mul_of_nonneg_left HB (abs_nonneg (f y))
  have hdiff : ∀ᵐ y : ℝ, ∀ s ∈ Set.Ioo a (2 * t), HasDerivAt (fun s => F s y) (F' s y) s := by
    apply Filter.Eventually.of_forall
    intro y s hs
    have hsp : 0 < s := ha.trans hs.1
    have H := (hasDerivAt_const s (f y)).mul (hasDerivAt_heatKernel_time hsp (x - y))
    simpa only [zero_mul, zero_add, F, F', heatTimeSlope] using! H
  have H := hasDerivAt_integral_of_dominated_loc_of_deriv_le (μ := volume)
    (F := F) (F' := F') (bound := fun y => ‖f y‖ * C)
    hnhds hFmeas (integrable_heatFlow_integrand hf ht x) hFpmeas hbound
    (hf.norm.mul_const C) hdiff
  exact H.2


noncomputable def heatSpaceSlope (t z : ℝ) : ℝ := (-z / (2 * t)) * heatKernel t z

/-- A finite envelope for the first spatial derivative on the whole line. -/
theorem heatKernel_space_slope_bound {t : ℝ} (ht : 0 < t) (z : ℝ) :
    |heatSpaceSlope t z| ≤ (1 + 4 * t) / (2 * t * Real.sqrt (4 * Real.pi * t)) := by
  have hq : z ^ 2 * gaussian (1 / (4 * t)) z ≤ 4 * t := by
    simpa only [one_div_one_div] using gaussian_quadratic_le (by positivity : 0 < 1 / (4 * t)) z
  have hG : gaussian (1 / (4 * t)) z ≤ 1 := by
    unfold gaussian
    apply Real.exp_le_one_iff.mpr
    exact mul_nonpos_of_nonpos_of_nonneg (neg_nonpos.mpr (by positivity)) (sq_nonneg z)
  have hab : |z| ≤ 1 + z ^ 2 := by nlinarith [sq_nonneg (|z| - 1), sq_abs z]
  have H := mul_le_mul_of_nonneg_right hab (gaussian_pos (1 / (4 * t)) z).le
  have HH : |z| * gaussian (1 / (4 * t)) z ≤ 1 + 4 * t := by nlinarith [H, hq, hG]
  calc
    _ = (|z| * gaussian (1 / (4 * t)) z) / (2 * t * Real.sqrt (4 * Real.pi * t)) := by
      unfold heatSpaceSlope
      rw [abs_mul, abs_of_nonneg (heatKernel_pos ht z).le, abs_div, abs_neg,
        abs_of_pos (by positivity : 0 < 2 * t)]
      unfold heatKernel
      ring
    _ ≤ _ := div_le_div_of_nonneg_right HH (by positivity)

/-- First spatial differentiation of heat flow for every L1 initial datum. -/
theorem hasDerivAt_heatFlow_space {f : ℝ → ℝ} (hf : Integrable f)
    {t : ℝ} (ht : 0 < t) (x : ℝ) :
    HasDerivAt (heatFlow f t) (∫ y : ℝ, f y * heatSpaceSlope t (x - y)) x := by
  let C := (1 + 4 * t) / (2 * t * Real.sqrt (4 * Real.pi * t))
  let F : ℝ → ℝ → ℝ := fun s y => f y * heatKernel t (s - y)
  let F' : ℝ → ℝ → ℝ := fun s y => f y * heatSpaceSlope t (s - y)
  have hFmeas : ∀ᶠ s in 𝓝 x, AEStronglyMeasurable (F s) := by
    exact Filter.Eventually.of_forall (fun s => hf.aestronglyMeasurable.mul
      (((continuous_heatKernel t).comp (continuous_const.sub continuous_id)).aestronglyMeasurable))
  have hFpmeas : AEStronglyMeasurable (F' x) := by
    have hc : Continuous (fun y : ℝ => heatSpaceSlope t (x - y)) := by
      unfold heatSpaceSlope
      exact (by fun_prop : Continuous (fun y : ℝ => -(x - y) / (2 * t))).mul
        ((continuous_heatKernel t).comp (continuous_const.sub continuous_id))
    exact hf.aestronglyMeasurable.mul hc.aestronglyMeasurable
  have hbound : ∀ᵐ y : ℝ, ∀ s ∈ (Set.univ : Set ℝ), ‖F' s y‖ ≤ ‖f y‖ * C := by
    exact Filter.Eventually.of_forall (fun y s _ => by
      dsimp [F', C]
      rw [abs_mul]
      exact mul_le_mul_of_nonneg_left (heatKernel_space_slope_bound ht _) (abs_nonneg (f y)))
  have hdiff : ∀ᵐ y : ℝ, ∀ s ∈ (Set.univ : Set ℝ), HasDerivAt (fun s => F s y) (F' s y) s := by
    apply Filter.Eventually.of_forall
    intro y s _
    have hk := (hasDerivAt_heatKernel_space ht (s - y)).comp s ((hasDerivAt_id s).sub_const y)
    have H := (hasDerivAt_const s (f y)).mul hk
    simpa only [F, F', heatSpaceSlope, Function.comp_def, Pi.mul_apply, id_eq, mul_one, zero_mul, zero_add] using! H
  have H := hasDerivAt_integral_of_dominated_loc_of_deriv_le (μ := volume)
    (F := F) (F' := F') (bound := fun y => ‖f y‖ * C)
    (s := Set.univ) (by simp) hFmeas (integrable_heatFlow_integrand hf ht x) hFpmeas hbound
    (hf.norm.mul_const C) hdiff
  exact H.2

/-- Second spatial differentiation, with the same integrand as time
differentiation. This is the heat equation for arbitrary L1 initial data. -/
theorem hasDerivAt_heatFlow_space_slope {f : ℝ → ℝ} (hf : Integrable f)
    {t : ℝ} (ht : 0 < t) (x : ℝ) :
    HasDerivAt (fun s => ∫ y : ℝ, f y * heatSpaceSlope t (s - y))
      (∫ y : ℝ, f y * heatTimeSlope t (x - y)) x := by
  let C := 3 / (2 * t * Real.sqrt (4 * Real.pi * t))
  let F : ℝ → ℝ → ℝ := fun s y => f y * heatSpaceSlope t (s - y)
  let F' : ℝ → ℝ → ℝ := fun s y => f y * heatTimeSlope t (s - y)
  have hc : ∀ s, Continuous (fun y : ℝ => heatSpaceSlope t (s - y)) := by
    intro s
    unfold heatSpaceSlope
    exact (by fun_prop : Continuous (fun y : ℝ => -(s - y) / (2 * t))).mul
      ((continuous_heatKernel t).comp (continuous_const.sub continuous_id))
  have hFmeas : ∀ᶠ s in 𝓝 x, AEStronglyMeasurable (F s) :=
    Filter.Eventually.of_forall (fun s => hf.aestronglyMeasurable.mul (hc s).aestronglyMeasurable)
  have hFint : Integrable (F x) := by
    apply hf.mul_bdd (c := (1 + 4 * t) / (2 * t * Real.sqrt (4 * Real.pi * t))) (hc x).aestronglyMeasurable
    exact Filter.Eventually.of_forall (fun y => heatKernel_space_slope_bound ht _)
  have hFpmeas : AEStronglyMeasurable (F' x) := by
    have hct : Continuous (fun y : ℝ => heatTimeSlope t (x - y)) := by
      unfold heatTimeSlope
      exact (by fun_prop : Continuous (fun y : ℝ => (x - y) ^ 2 / (4 * t ^ 2) - 1 / (2 * t))).mul
        ((continuous_heatKernel t).comp (continuous_const.sub continuous_id))
    exact hf.aestronglyMeasurable.mul hct.aestronglyMeasurable
  have hbound : ∀ᵐ y : ℝ, ∀ s ∈ (Set.univ : Set ℝ), ‖F' s y‖ ≤ ‖f y‖ * C := by
    exact Filter.Eventually.of_forall (fun y s _ => by
      dsimp [F', C, heatTimeSlope]
      rw [abs_mul]
      exact mul_le_mul_of_nonneg_left (heatKernel_time_slope_bound ht _) (abs_nonneg (f y)))
  have hdiff : ∀ᵐ y : ℝ, ∀ s ∈ (Set.univ : Set ℝ), HasDerivAt (fun s => F s y) (F' s y) s := by
    apply Filter.Eventually.of_forall
    intro y s _
    have hk := (hasDerivAt_heatKernel_slope ht (s - y)).comp s ((hasDerivAt_id s).sub_const y)
    have H := (hasDerivAt_const s (f y)).mul hk
    simpa only [F, F', heatSpaceSlope, heatTimeSlope, Function.comp_def, Pi.mul_apply, id_eq, mul_one, zero_mul, zero_add] using! H
  exact (hasDerivAt_integral_of_dominated_loc_of_deriv_le (μ := volume)
    (F := F) (F' := F') (bound := fun y => ‖f y‖ * C) (s := Set.univ) (by simp)
    hFmeas hFint hFpmeas hbound (hf.norm.mul_const C) hdiff).2


/-- The classical scalar heat equation for arbitrary real L1 initial data,
with the actual derivative operator on both sides. -/
theorem heatFlow_heat_equation {f : ℝ → ℝ} (hf : Integrable f)
    {t : ℝ} (ht : 0 < t) (x : ℝ) :
    deriv (fun s => heatFlow f s x) t = deriv (deriv (heatFlow f t)) x := by
  have hspace : deriv (heatFlow f t) = fun z => ∫ y : ℝ, f y * heatSpaceSlope t (z - y) := by
    funext z
    exact (hasDerivAt_heatFlow_space hf ht z).deriv
  rw [hspace, (hasDerivAt_heatFlow_time hf ht x).deriv,
    (hasDerivAt_heatFlow_space_slope hf ht x).deriv]

end ChowlaCosine.Beckner
