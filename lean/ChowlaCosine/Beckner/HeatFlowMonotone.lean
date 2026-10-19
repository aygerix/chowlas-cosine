import ChowlaCosine.Beckner.HeatFlowSpatial

/-! # Monotonicity of the concrete geometric heat-product integral on R² -/

open MeasureTheory Real
open scoped BigOperators Topology RealInnerProductSpace

namespace ChowlaCosine.Beckner
set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

section
variable {ι E : Type*} [Fintype ι] [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- Application of the global parabolic integration bridge to the actual geometric
heat product. All unbounded-domain hypotheses are supplied for interval-supported
nonnegative L1 data, with no extra domination or boundary assumptions. -/
theorem geometricHeatProduct_integral_derivative_nonneg
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hm : ∀ i, 0 < ∫ y : ℝ, f i y)
    (hc : ∀ i, 0 ≤ c i) (hu : ∀ i, ‖u i‖ = 1) (hframe : IsWeightedFrame c u)
    (R : ℝ) (hR : 0 ≤ R) (hsupport : ∀ i y, f i y ≠ 0 → |y| ≤ R)
    (basis : OrthonormalBasis (Fin 2) ℝ E) {t : ℝ} (ht : 0 < t) :
    HasDerivAt (fun s => ∫ z : ℝ × ℝ, geometricHeatProduct f c u s (planePoint basis z)
      ∂volume.prod volume)
      (∫ z : ℝ × ℝ, geometricHeatTimeSlope f c u t (planePoint basis z) ∂volume.prod volume) t ∧
      0 ≤ ∫ z : ℝ × ℝ, geometricHeatTimeSlope f c u t (planePoint basis z) ∂volume.prod volume := by
  let F := fun s (z : ℝ × ℝ) => geometricHeatProduct f c u s (planePoint basis z)
  let Ft := fun s (z : ℝ × ℝ) => geometricHeatTimeSlope f c u s (planePoint basis z)
  let Px := fun z : ℝ × ℝ => geometricHeatSpaceSlope f c u (basis 0) t (planePoint basis z)
  let Py := fun z : ℝ × ℝ => geometricHeatSpaceSlope f c u (basis 1) t (planePoint basis z)
  let Qx := fun z : ℝ × ℝ => geometricHeatSecondSlope f c u (basis 0) t (planePoint basis z)
  let Qy := fun z : ℝ × ℝ => geometricHeatSecondSlope f c u (basis 1) t (planePoint basis z)
  obtain ⟨hPx,hQx⟩ := integrable_geometricHeat_spatial_slopes_plane f c u hf hn hm hc hu hframe
    R hR hsupport basis ht (basis 0) (basis.norm_eq_one 0)
  obtain ⟨hPy,hQy⟩ := integrable_geometricHeat_spatial_slopes_plane f c u hf hn hm hc hu hframe
    R hR hsupport basis ht (basis 1) (basis.norm_eq_one 1)
  have hdx : ∀ x y : ℝ, HasDerivAt (fun r => Px (r,y)) (Qx (x,y)) x := by
    intro x y
    have H := hasDerivAt_geometricHeatSpaceSlope_line f c u hf hn hm ht (y • basis 1) (basis 0) x
    simpa only [Px, Qx, planePoint, add_comm] using! H
  have hdy : ∀ x y : ℝ, HasDerivAt (fun r => Py (x,r)) (Qy (x,y)) y := by
    intro x y
    exact hasDerivAt_geometricHeatSpaceSlope_line f c u hf hn hm ht (x • basis 0) (basis 1) y
  have hparabolic : ∀ z, Qx z + Qy z ≤ Ft t z := by
    intro z
    have H := geometricHeat_defect_nonneg f c u hf hn hm hc hu hframe basis ht (planePoint basis z)
    rw [(hasDerivAt_geometricHeatProduct_time f c u hf hn hm ht _).deriv] at H
    simp only [Fin.sum_univ_two, geometricHeatPath_second_derivative f c u hf hn hm ht] at H
    change 0 ≤ Ft t z - (Qx z + Qy z) at H
    linarith
  let a := t/2
  let b := 2*t
  have ha : 0 < a := by dsimp [a]; positivity
  have hb : 0 < b := by dsimp [b]; positivity
  have hs : Set.Ioo a b ∈ 𝓝 t := Ioo_mem_nhds (by dsimp [a]; linarith) (by dsimp [b]; linarith)
  let C := (∏ i, heatTailConstant (f i) R a ^ c i) * (∑ i, c i) *
    ((1+R^2)/(2*a^2) + 1/(2*a))
  let bound := fun z : ℝ × ℝ => C *
    ((1+(z.1^2+z.2^2))*exp (-(1/(8*b))*(z.1^2+z.2^2)))
  have hFmeas : ∀ᶠ s in 𝓝 t, AEStronglyMeasurable (F s) (volume.prod volume) := by
    filter_upwards [Ioi_mem_nhds ht] with s hs
    exact ((continuous_geometricHeatProduct_space f c u hf hn hm hs).comp
      (continuous_planePoint basis)).aestronglyMeasurable
  have hbound : ∀ᵐ z : ℝ × ℝ ∂volume.prod volume, ∀ s ∈ Set.Ioo a b, ‖Ft s z‖ ≤ bound z := by
    apply Filter.Eventually.of_forall
    intro z s hs
    exact geometricHeatTimeSlope_plane_bound_interval f c u hf hn hm hc hu hframe R hR hsupport
      basis ha hs.1.le hs.2.le z
  have hdt : ∀ᵐ z : ℝ × ℝ ∂volume.prod volume, ∀ s ∈ Set.Ioo a b,
      HasDerivAt (fun r => F r z) (Ft s z) s := by
    apply Filter.Eventually.of_forall
    intro z s hs
    exact hasDerivAt_geometricHeatProduct_time f c u hf hn hm (ha.trans hs.1) _
  exact parabolic_integral_derivative_nonneg F Ft Px Py Qx Qy t (Set.Ioo a b) bound hs hFmeas
    (integrable_geometricHeatProduct_plane f c u hf hn hm hc hframe R hR hsupport basis ht)
    (measurable_geometricHeatTimeSlope_plane f c u hf hn hm basis ht).aestronglyMeasurable
    hbound ((integrable_plane_polynomial_gaussian (by positivity : 0 < 1/(8*b))).const_mul C) hdt
    hPx hPy hQx hQy hdx hdy hparabolic

/-- Concrete geometric heat-flow monotonicity on all positive times, with every
integrability and integration-by-parts condition discharged. Limit and density
passages are separate theorems, not implicit hypotheses of this one. -/
theorem geometricHeatProduct_integral_monotone
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hm : ∀ i, 0 < ∫ y : ℝ, f i y)
    (hc : ∀ i, 0 ≤ c i) (hu : ∀ i, ‖u i‖ = 1) (hframe : IsWeightedFrame c u)
    (R : ℝ) (hR : 0 ≤ R) (hsupport : ∀ i y, f i y ≠ 0 → |y| ≤ R)
    (basis : OrthonormalBasis (Fin 2) ℝ E) :
    MonotoneOn (fun t => ∫ z : ℝ × ℝ, geometricHeatProduct f c u t (planePoint basis z)
      ∂volume.prod volume) (Set.Ioi 0) := by
  have H := fun t ht => geometricHeatProduct_integral_derivative_nonneg f c u hf hn hm hc hu hframe
    R hR hsupport basis (t := t) ht
  apply monotoneOn_of_hasDerivWithinAt_nonneg (convex_Ioi (0 : ℝ))
  · exact fun t ht => (H t ht).1.continuousAt.continuousWithinAt
  · intro t ht
    exact (H t (interior_subset ht)).1.hasDerivWithinAt
  · intro t ht
    exact (H t (interior_subset ht)).2

end
end ChowlaCosine.Beckner
