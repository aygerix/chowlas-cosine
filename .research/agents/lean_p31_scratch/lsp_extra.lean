
/-!
# Pointwise geometric heat-flow differential inequality

This file concerns the actual differentiated heat product. Integrating its
Laplacian and proving the large-time/density passages are separate steps.
-/

open MeasureTheory Real
open scoped Topology RealInnerProductSpace

namespace ChowlaCosine.Beckner
set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

noncomputable def heatSpaceMoment (f : ℝ → ℝ) (t x : ℝ) : ℝ :=
  ∫ y : ℝ, f y * heatSpaceSlope t (x - y)

noncomputable def heatTimeMoment (f : ℝ → ℝ) (t x : ℝ) : ℝ :=
  ∫ y : ℝ, f y * heatTimeSlope t (x - y)

noncomputable def heatSpaceScore (f : ℝ → ℝ) (t x : ℝ) : ℝ :=
  heatSpaceMoment f t x / heatFlow f t x

noncomputable def heatTimeScore (f : ℝ → ℝ) (t x : ℝ) : ℝ :=
  heatTimeMoment f t x / heatFlow f t x

theorem hasDerivAt_heatFlow_affine {f : ℝ → ℝ} (hf : Integrable f)
    {t : ℝ} (ht : 0 < t) (a b r : ℝ) :
    HasDerivAt (fun s => heatFlow f t (a + s * b)) (b * heatSpaceMoment f t (a + r * b)) r := by
  have H := (hasDerivAt_heatFlow_space hf ht (a + r * b)).comp r
    (((hasDerivAt_id r).mul_const b).const_add a)
  simpa only [Function.comp_def, id_eq, one_mul, mul_one, heatSpaceMoment, mul_comm] using! H

theorem hasDerivAt_heatSpaceMoment_affine {f : ℝ → ℝ} (hf : Integrable f)
    {t : ℝ} (ht : 0 < t) (a b r : ℝ) :
    HasDerivAt (fun s => heatSpaceMoment f t (a + s * b))
      (b * heatTimeMoment f t (a + r * b)) r := by
  have H := (hasDerivAt_heatFlow_space_slope hf ht (a + r * b)).comp r
    (((hasDerivAt_id r).mul_const b).const_add a)
  simpa only [Function.comp_def, id_eq, one_mul, mul_one, heatSpaceMoment, heatTimeMoment, mul_comm] using! H

section
variable {ι E : Type*} [Fintype ι] [NormedAddCommGroup E] [InnerProductSpace ℝ E]

noncomputable def geometricHeatProduct (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E) (t : ℝ) (x : E) : ℝ :=
  ∏ i, heatFlow (f i) t ⟪u i, x⟫ ^ c i

noncomputable def geometricHeatPath (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (t : ℝ) (x e : E) (r : ℝ) : ℝ :=
  ∏ i, heatFlow (f i) t (⟪u i, x⟫ + r * ⟪u i, e⟫) ^ c i

/-- Actual time derivative of the geometric heat product. -/
theorem hasDerivAt_geometricHeatProduct_time (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hm : ∀ i, 0 < ∫ y : ℝ, f i y) {t : ℝ} (ht : 0 < t) (x : E) :
    HasDerivAt (fun s => geometricHeatProduct f c u s x)
      (geometricHeatProduct f c u t x * ∑ i, c i * heatTimeScore (f i) t ⟪u i, x⟫) t := by
  have H := hasDerivAt_weighted_product c (fun i s => heatFlow (f i) s ⟪u i, x⟫)
    (fun i => heatTimeMoment (f i) t ⟪u i, x⟫) t
    (fun i => heatFlow_pos (hf i) (hn i) (hm i) ht _)
    (fun i => hasDerivAt_heatFlow_time (hf i) ht _)
  simpa only [geometricHeatProduct, heatTimeScore, mul_div_assoc] using! H

/-- The second derivative along any direction, with every scalar heat-flow
factor differentiated at actual real points. -/
theorem geometricHeatPath_second_derivative (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hm : ∀ i, 0 < ∫ y : ℝ, f i y) {t : ℝ} (ht : 0 < t) (x e : E) :
    deriv (deriv (geometricHeatPath f c u t x e)) 0 =
      geometricHeatProduct f c u t x *
        ((∑ i, c i * ⟪u i, e⟫ * heatSpaceScore (f i) t ⟪u i, x⟫) ^ 2 +
          ∑ i, c i * ⟪u i, e⟫ ^ 2 *
            (heatTimeScore (f i) t ⟪u i, x⟫ - heatSpaceScore (f i) t ⟪u i, x⟫ ^ 2)) := by
  let F : ι → ℝ → ℝ := fun i r => heatFlow (f i) t (⟪u i, x⟫ + r * ⟪u i, e⟫)
  let G : ι → ℝ → ℝ := fun i r => ⟪u i, e⟫ * heatSpaceMoment (f i) t (⟪u i, x⟫ + r * ⟪u i, e⟫)
  let K : ι → ℝ := fun i => ⟪u i, e⟫ ^ 2 * heatTimeMoment (f i) t ⟪u i, x⟫
  have hpos : ∀ i r, 0 < F i r := fun i r => heatFlow_pos (hf i) (hn i) (hm i) ht _
  have hF : ∀ i r, HasDerivAt (F i) (G i r) r := fun i r => hasDerivAt_heatFlow_affine (hf i) ht _ _ _
  have hG : ∀ i, HasDerivAt (G i) (K i) 0 := by
    intro i
    have H := (hasDerivAt_heatSpaceMoment_affine (hf i) ht ⟪u i, x⟫ ⟪u i, e⟫ 0).const_mul ⟪u i, e⟫
    dsimp [G, K]
    simpa only [zero_mul, add_zero, pow_two, mul_assoc] using! H
  have hfirst : deriv (geometricHeatPath f c u t x e) =
      (fun r => (∏ i, F i r ^ c i) * ∑ i, c i * (G i r / F i r)) := by
    funext r
    have H := hasDerivAt_weighted_product c F (fun i => G i r) r (fun i => hpos i r) (fun i => hF i r)
    simpa only [geometricHeatPath, F, mul_div_assoc] using! H.deriv
  rw [hfirst]
  have H := (hasDerivAt_weighted_product_slope c F G K 0 (fun i => hpos i 0)
    (fun i => hF i 0) hG).deriv
  rw [H]
  dsimp [F, G, K, geometricHeatProduct, heatSpaceScore, heatTimeScore]
  simp only [zero_mul, add_zero, mul_div_assoc, mul_pow]
  simp only [mul_sub, mul_assoc]

/-- Pointwise heat-flow differential inequality for the actual positive
geometric product, in every finite-dimensional frame. This theorem does
not interchange a derivative and an integral or integrate a Laplacian. -/
theorem geometricHeat_defect_nonneg {κ : Type*} [Fintype κ]
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hm : ∀ i, 0 < ∫ y : ℝ, f i y)
    (hc : ∀ i, 0 ≤ c i) (hu : ∀ i, ‖u i‖ = 1) (hframe : IsWeightedFrame c u)
    (b : OrthonormalBasis κ ℝ E) {t : ℝ} (ht : 0 < t) (x : E) :
    0 ≤ deriv (fun s => geometricHeatProduct f c u s x) t -
      ∑ j, deriv (deriv (geometricHeatPath f c u t x (b j))) 0 := by
  rw [(hasDerivAt_geometricHeatProduct_time f c u hf hn hm ht x).deriv]
  simp_rw [geometricHeatPath_second_derivative f c u hf hn hm ht]
  rw [← Finset.mul_sum]
  apply frame_heat_defect_nonneg c (fun i => heatSpaceScore (f i) t ⟪u i, x⟫)
    (fun i => heatTimeScore (f i) t ⟪u i, x⟫) u hc hu hframe b
  unfold geometricHeatProduct
  exact Finset.prod_nonneg (fun i _ => Real.rpow_nonneg (heatFlow_nonneg (hn i) ht _ ) _)

end
end ChowlaCosine.Beckner

namespace ChowlaCosine.Beckner
set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

/-- Whole-plane integration by parts in the first coordinate. Integrability
of the first and second derivatives replaces an unproved boundary claim. -/
theorem integral_partial_x_eq_zero (P Q : ℝ × ℝ → ℝ)
    (hP : Integrable P (volume.prod volume)) (hQ : Integrable Q (volume.prod volume))
    (hd : ∀ x y : ℝ, HasDerivAt (fun s => P (s, y)) (Q (x, y)) x) :
    (∫ z : ℝ × ℝ, Q z ∂volume.prod volume) = 0 := by
  rw [integral_prod_symm Q hQ]
  calc
    _ = ∫ _y : ℝ, (0 : ℝ) := by
      apply integral_congr_ae
      filter_upwards [hP.prod_left_ae, hQ.prod_left_ae] with y hpy hqy
      exact integral_eq_zero_of_hasDerivAt_of_integrable (fun x => hd x y) hqy hpy
    _ = 0 := by simp

/-- Whole-plane integration by parts in the second coordinate. -/
theorem integral_partial_y_eq_zero (P Q : ℝ × ℝ → ℝ)
    (hP : Integrable P (volume.prod volume)) (hQ : Integrable Q (volume.prod volume))
    (hd : ∀ x y : ℝ, HasDerivAt (fun s => P (x, s)) (Q (x, y)) y) :
    (∫ z : ℝ × ℝ, Q z ∂volume.prod volume) = 0 := by
  rw [integral_prod Q hQ]
  calc
    _ = ∫ _x : ℝ, (0 : ℝ) := by
      apply integral_congr_ae
      filter_upwards [hP.prod_right_ae, hQ.prod_right_ae] with x hpx hqx
      exact integral_eq_zero_of_hasDerivAt_of_integrable (fun y => hd x y) hqx hpx
    _ = 0 := by simp

/-- A fully explicit integral bridge for a parabolic supersolution on R².
The integrability hypotheses are obligations when applying this result to
the geometric product; they are not asserted implicitly. -/
theorem parabolic_integral_derivative_nonneg
    (F Ft : ℝ → ℝ × ℝ → ℝ) (Px Py Qx Qy : ℝ × ℝ → ℝ) (t : ℝ)
    (s : Set ℝ) (bound : ℝ × ℝ → ℝ) (hs : s ∈ 𝓝 t)
    (hFmeas : ∀ᶠ r in 𝓝 t, AEStronglyMeasurable (F r) (volume.prod volume))
    (hFint : Integrable (F t) (volume.prod volume))
    (hFtmeas : AEStronglyMeasurable (Ft t) (volume.prod volume))
    (hbound : ∀ᵐ z ∂volume.prod volume, ∀ r ∈ s, ‖Ft r z‖ ≤ bound z)
    (hbint : Integrable bound (volume.prod volume))
    (hdt : ∀ᵐ z ∂volume.prod volume, ∀ r ∈ s, HasDerivAt (fun r => F r z) (Ft r z) r)
    (hPx : Integrable Px (volume.prod volume)) (hPy : Integrable Py (volume.prod volume))
    (hQx : Integrable Qx (volume.prod volume)) (hQy : Integrable Qy (volume.prod volume))
    (hdx : ∀ x y, HasDerivAt (fun r => Px (r, y)) (Qx (x, y)) x)
    (hdy : ∀ x y, HasDerivAt (fun r => Py (x, r)) (Qy (x, y)) y)
    (hparabolic : ∀ z, Qx z + Qy z ≤ Ft t z) :
    HasDerivAt (fun r => ∫ z : ℝ × ℝ, F r z ∂volume.prod volume)
      (∫ z : ℝ × ℝ, Ft t z ∂volume.prod volume) t ∧
      0 ≤ ∫ z : ℝ × ℝ, Ft t z ∂volume.prod volume := by
  obtain ⟨hFtint, hderiv⟩ := hasDerivAt_integral_of_dominated_loc_of_deriv_le
    (μ := volume.prod volume) hs hFmeas hFint hFtmeas hbound hbint hdt
  refine ⟨hderiv, ?_⟩
  have H := integral_mono (hQx.add hQy) hFtint hparabolic
  simp only [Pi.add_apply] at H
  rw [integral_add hQx hQy, integral_partial_x_eq_zero Px Qx hPx hQx hdx,
    integral_partial_y_eq_zero Py Qy hPy hQy hdy, add_zero] at H
  exact H

end ChowlaCosine.Beckner
#print axioms ChowlaCosine.Beckner.abs_integral_le_scaled_integral
#print axioms ChowlaCosine.Beckner.integrable_heatSpaceSlope_integrand
#print axioms ChowlaCosine.Beckner.integrable_heatTimeSlope_integrand
#print axioms ChowlaCosine.Beckner.heatFlow_space_moment_bound
#print axioms ChowlaCosine.Beckner.heatFlow_time_moment_bound
#print axioms ChowlaCosine.Beckner.heatFlow_space_score_bound
#print axioms ChowlaCosine.Beckner.heatFlow_time_score_bound
#print axioms ChowlaCosine.Beckner.weighted_product_eq_exp
#print axioms ChowlaCosine.Beckner.hasDerivAt_weighted_product
#print axioms ChowlaCosine.Beckner.hasDerivAt_weighted_product_slope
#print axioms ChowlaCosine.Beckner.frame_laplacian_identity
#print axioms ChowlaCosine.Beckner.frame_heat_defect_nonneg
#print axioms ChowlaCosine.Beckner.hasDerivAt_heatFlow_affine
#print axioms ChowlaCosine.Beckner.hasDerivAt_heatSpaceMoment_affine
#print axioms ChowlaCosine.Beckner.hasDerivAt_geometricHeatProduct_time
#print axioms ChowlaCosine.Beckner.geometricHeatPath_second_derivative
#print axioms ChowlaCosine.Beckner.geometricHeat_defect_nonneg
#print axioms ChowlaCosine.Beckner.integral_partial_x_eq_zero
#print axioms ChowlaCosine.Beckner.integral_partial_y_eq_zero
#print axioms ChowlaCosine.Beckner.parabolic_integral_derivative_nonneg
