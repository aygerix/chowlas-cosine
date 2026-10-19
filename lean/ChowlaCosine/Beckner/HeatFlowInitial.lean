import ChowlaCosine.Beckner.HeatFlowProductLimit

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
