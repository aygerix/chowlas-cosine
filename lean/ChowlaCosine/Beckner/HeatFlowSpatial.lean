import ChowlaCosine.Beckner.HeatFlowIntegral

/-! # Concrete spatial derivative bounds for the geometric heat product -/

open MeasureTheory Real
open scoped BigOperators Topology RealInnerProductSpace

namespace ChowlaCosine.Beckner
set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

section Scores
variable {ι : Type*} [Fintype ι]

/-- A finite weighted directional score, with all coefficients controlled. -/
theorem abs_weighted_directional_score_le (c θ v : ι → ℝ) (hc : ∀ i, 0 ≤ c i)
    (hθ : ∀ i, |θ i| ≤ 1) (B : ℝ) (hB : 0 ≤ B) (hv : ∀ i, |v i| ≤ B) :
    |∑ i, c i * θ i * v i| ≤ (∑ i, c i) * B := by
  calc
    _ ≤ ∑ i, |c i * θ i * v i| := Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ i, c i * B := by
      apply Finset.sum_le_sum
      intro i _
      rw [abs_mul, abs_mul, abs_of_nonneg (hc i)]
      have H := mul_le_mul (hθ i) (hv i) (abs_nonneg _) (by norm_num : (0 : ℝ) ≤ 1)
      nlinarith [mul_le_mul_of_nonneg_left H (hc i)]
    _ = _ := by rw [Finset.sum_mul]

/-- The actual second directional product formula has a quadratic score bound. -/
theorem abs_weighted_second_score_le (c θ v w : ι → ℝ) (hc : ∀ i, 0 ≤ c i)
    (hθ : ∀ i, |θ i| ≤ 1) (B T : ℝ) (hB : 0 ≤ B) (hT : 0 ≤ T)
    (hv : ∀ i, |v i| ≤ B) (hw : ∀ i, |w i| ≤ T) :
    |(∑ i, c i * θ i * v i)^2 + ∑ i, c i * θ i^2 * (w i - v i^2)| ≤
      (∑ i, c i)^2 * B^2 + (∑ i, c i) * (T+B^2) := by
  have hS : 0 ≤ ∑ i, c i := Finset.sum_nonneg (fun i _ => hc i)
  have hfirst : (∑ i, c i * θ i * v i)^2 ≤ (∑ i, c i)^2 * B^2 := by
    have H := (sq_le_sq₀ (abs_nonneg _) (mul_nonneg hS hB)).mpr
      (abs_weighted_directional_score_le c θ v hc hθ B hB hv)
    simpa only [sq_abs, mul_pow] using H
  have hsecond : |∑ i, c i * θ i^2 * (w i-v i^2)| ≤ (∑ i, c i)*(T+B^2) := by
    calc
      _ ≤ ∑ i, |c i * θ i^2 * (w i-v i^2)| := Finset.abs_sum_le_sum_abs _ _
      _ ≤ ∑ i, c i*(T+B^2) := by
        apply Finset.sum_le_sum
        intro i _
        have hθsq : θ i^2 ≤ 1 := by
          simpa only [sq_abs, one_pow] using (sq_le_sq₀ (abs_nonneg _) (by norm_num : (0:ℝ) ≤ 1)).mpr (hθ i)
        have hvsq : v i^2 ≤ B^2 := by
          simpa only [sq_abs] using (sq_le_sq₀ (abs_nonneg _) hB).mpr (hv i)
        have hdiff : |w i-v i^2| ≤ T+B^2 := by
          have H := abs_sub (w i) (v i^2)
          rw [abs_of_nonneg (sq_nonneg (v i))] at H
          linarith [hw i]
        rw [abs_mul, abs_of_nonneg (mul_nonneg (hc i) (sq_nonneg _))]
        have HH := mul_le_mul hθsq hdiff (abs_nonneg _) (by norm_num : (0:ℝ) ≤ 1)
        nlinarith [mul_le_mul_of_nonneg_left HH (hc i)]
      _ = _ := by rw [Finset.sum_mul]
  exact (abs_add_le _ _).trans (by rw [abs_of_nonneg (sq_nonneg _)]; linarith)
end Scores

section
variable {ι E : Type*} [Fintype ι] [NormedAddCommGroup E] [InnerProductSpace ℝ E]

noncomputable def geometricHeatSpaceSlope (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (e : E) (t : ℝ) (x : E) : ℝ :=
  geometricHeatProduct f c u t x * ∑ i, c i * ⟪u i,e⟫ * heatSpaceScore (f i) t ⟪u i,x⟫

noncomputable def geometricHeatSecondSlope (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (e : E) (t : ℝ) (x : E) : ℝ :=
  geometricHeatProduct f c u t x *
    ((∑ i, c i * ⟪u i,e⟫ * heatSpaceScore (f i) t ⟪u i,x⟫)^2 +
      ∑ i, c i * ⟪u i,e⟫^2 * (heatTimeScore (f i) t ⟪u i,x⟫ - heatSpaceScore (f i) t ⟪u i,x⟫^2))

/-- Actual derivative of the first spatial slope on every affine line. -/
theorem hasDerivAt_geometricHeatSpaceSlope_line
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hm : ∀ i, 0 < ∫ y : ℝ, f i y) {t : ℝ} (ht : 0 < t) (x e : E) (r : ℝ) :
    HasDerivAt (fun s => geometricHeatSpaceSlope f c u e t (x+s • e))
      (geometricHeatSecondSlope f c u e t (x+r • e)) r := by
  let F : ι → ℝ → ℝ := fun i s => heatFlow (f i) t (⟪u i,x⟫ + s * ⟪u i,e⟫)
  let G : ι → ℝ → ℝ := fun i s => ⟪u i,e⟫ * heatSpaceMoment (f i) t (⟪u i,x⟫ + s * ⟪u i,e⟫)
  let K : ι → ℝ := fun i => ⟪u i,e⟫^2 * heatTimeMoment (f i) t (⟪u i,x⟫ + r * ⟪u i,e⟫)
  have hpos : ∀ i, 0 < F i r := fun i => heatFlow_pos (hf i) (hn i) (hm i) ht _
  have hF : ∀ i, HasDerivAt (F i) (G i r) r := fun i => hasDerivAt_heatFlow_affine (hf i) ht _ _ _
  have hG : ∀ i, HasDerivAt (G i) (K i) r := by
    intro i
    have H := (hasDerivAt_heatSpaceMoment_affine (hf i) ht ⟪u i,x⟫ ⟪u i,e⟫ r).const_mul ⟪u i,e⟫
    simpa only [G, K, pow_two, mul_assoc] using! H
  have H := hasDerivAt_weighted_product_slope c F G K r hpos hF hG
  simpa only [F, G, K, geometricHeatSpaceSlope, geometricHeatSecondSlope, geometricHeatProduct,
    heatSpaceScore, heatTimeScore, inner_add_right, real_inner_smul_right,
    mul_div_assoc, mul_pow, mul_sub, mul_assoc] using! H

/-- Integrable polynomial envelope for the first and second directional scores. -/
theorem geometricHeat_spatial_envelopes
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hm : ∀ i, 0 < ∫ y : ℝ, f i y)
    (hc : ∀ i, 0 ≤ c i) (hu : ∀ i, ‖u i‖ = 1) (hframe : IsWeightedFrame c u)
    (R : ℝ) (hR : 0 ≤ R) (hsupport : ∀ i y, f i y ≠ 0 → |y| ≤ R)
    (basis : OrthonormalBasis (Fin 2) ℝ E) {t : ℝ} (ht : 0 < t)
    (e : E) (he : ‖e‖ = 1) :
    ∃ C₁ C₂ : ℝ, ∀ z : ℝ × ℝ,
      |geometricHeatSpaceSlope f c u e t (planePoint basis z)| ≤
        C₁ * ((1+(z.1^2+z.2^2))*exp (-(1/(8*t))*(z.1^2+z.2^2))) ∧
      |geometricHeatSecondSlope f c u e t (planePoint basis z)| ≤
        C₂ * ((1+(z.1^2+z.2^2))*exp (-(1/(8*t))*(z.1^2+z.2^2))) := by
  let S := ∑ i, c i
  let K := ∏ i, heatTailConstant (f i) R t ^ c i
  let C := (1+R^2)/(2*t^2) + 1/(2*t)
  have hS : 0 ≤ S := Finset.sum_nonneg (fun i _ => hc i)
  have hK : 0 ≤ K := Finset.prod_nonneg (fun i _ => rpow_nonneg (heatTailConstant_nonneg (hn i) R t) _)
  have hC : 0 ≤ C := by dsimp [C]; positivity
  have hθ : ∀ i, |⟪u i,e⟫| ≤ 1 := fun i => by simpa only [hu, he, mul_one] using abs_real_inner_le_norm (u i) e
  refine ⟨K*S*(1+C), K*(S^2+2*S)*C, ?_⟩
  intro z
  let x := planePoint basis z
  let B := (‖x‖+R)/(2*t)
  let T := (‖x‖+R)^2/(4*t^2) + 1/(2*t)
  let V := 1+‖x‖^2
  let P := geometricHeatProduct f c u t x
  let E₀ := exp (-(1/(8*t))*‖x‖^2)
  have hP : 0 ≤ P := Finset.prod_nonneg (fun i _ => rpow_nonneg (heatFlow_nonneg (hn i) ht _) _)
  have hPB : P ≤ K*E₀ := geometricHeatProduct_gaussian_bound_interval f c u hf hn hc hframe R hR hsupport ht le_rfl le_rfl x
  have hB : 0 ≤ B := by dsimp [B]; positivity
  have hT : 0 ≤ T := by dsimp [T]; positivity
  have hV : 0 ≤ V := by dsimp [V]; positivity
  have hE : 0 ≤ E₀ := (exp_pos _).le
  have hv : ∀ i, |heatSpaceScore (f i) t ⟪u i,x⟫| ≤ B := fun i =>
    heatSpaceScore_bound_interval (hf i) (hn i) (hm i) R hR (hsupport i) ht le_rfl (u i) x (hu i)
  have hw : ∀ i, |heatTimeScore (f i) t ⟪u i,x⟫| ≤ T := fun i =>
    heatTimeScore_bound_interval (hf i) (hn i) (hm i) R hR (hsupport i) ht le_rfl (u i) x (hu i)
  have hTB : T ≤ C*V := heat_score_polynomial_bound t R ‖x‖ ht
  have hBsq : B^2 ≤ C*V := by
    have heq : B^2 = (‖x‖+R)^2/(4*t^2) := by dsimp [B]; ring
    rw [heq]
    dsimp [T] at hTB
    linarith [show 0 ≤ 1/(2*t) by positivity]
  have hBpoly : B ≤ (1+C)*V := by
    have hvone : 1 ≤ V := by dsimp [V]; nlinarith [sq_nonneg ‖x‖]
    nlinarith [sq_nonneg (B-1/2)]
  have h₁ := abs_weighted_directional_score_le c (fun i => ⟪u i,e⟫)
    (fun i => heatSpaceScore (f i) t ⟪u i,x⟫) hc hθ B hB hv
  have h₂ := abs_weighted_second_score_le c (fun i => ⟪u i,e⟫)
    (fun i => heatSpaceScore (f i) t ⟪u i,x⟫) (fun i => heatTimeScore (f i) t ⟪u i,x⟫)
    hc hθ B T hB hT hv hw
  have hsecond : S^2*B^2+S*(T+B^2) ≤ (S^2+2*S)*C*V := by
    nlinarith [mul_le_mul_of_nonneg_left hBsq (sq_nonneg S),
      mul_le_mul_of_nonneg_left hBsq hS, mul_le_mul_of_nonneg_left hTB hS]
  have hfirst : |geometricHeatSpaceSlope f c u e t x| ≤ K*S*(1+C)*(V*E₀) := by
    rw [geometricHeatSpaceSlope, abs_mul, abs_of_nonneg hP]
    have H := mul_le_mul_of_nonneg_left (h₁.trans (mul_le_mul_of_nonneg_left hBpoly hS)) hP
    have HH := mul_le_mul_of_nonneg_right hPB (mul_nonneg hS (mul_nonneg (by positivity : 0 ≤ 1+C) hV))
    nlinarith [H, HH]
  have hsecond' : |geometricHeatSecondSlope f c u e t x| ≤ K*(S^2+2*S)*C*(V*E₀) := by
    rw [geometricHeatSecondSlope, abs_mul, abs_of_nonneg hP]
    have H := mul_le_mul_of_nonneg_left (h₂.trans hsecond) hP
    have HH := mul_le_mul_of_nonneg_right hPB
      (mul_nonneg (mul_nonneg (by nlinarith : 0 ≤ S^2+2*S) hC) hV)
    nlinarith [H, HH]
  simpa only [x, V, E₀, norm_planePoint_sq] using And.intro hfirst hsecond'

/-- Measurability of the first relative moment requires no additional regularity of the datum. -/
theorem measurable_heatSpaceScore {f : ℝ → ℝ} (hf : Integrable f)
    {t : ℝ} (ht : 0 < t) : Measurable (heatSpaceScore f t) :=
  (continuous_heatSpaceMoment_space hf ht).measurable.div (continuous_heatFlow_space hf ht).measurable

theorem measurable_geometricHeat_spatial_slopes_plane
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hm : ∀ i, 0 < ∫ y : ℝ, f i y) (basis : OrthonormalBasis (Fin 2) ℝ E)
    {t : ℝ} (ht : 0 < t) (e : E) :
    Measurable (fun z : ℝ × ℝ => geometricHeatSpaceSlope f c u e t (planePoint basis z)) ∧
    Measurable (fun z : ℝ × ℝ => geometricHeatSecondSlope f c u e t (planePoint basis z)) := by
  have hP := ((continuous_geometricHeatProduct_space f c u hf hn hm ht).comp
    (continuous_planePoint basis)).measurable
  have hv : ∀ i, Measurable (fun z : ℝ × ℝ => heatSpaceScore (f i) t ⟪u i,planePoint basis z⟫) :=
    fun i => (measurable_heatSpaceScore (hf i) ht).comp
      (continuous_const.inner (continuous_planePoint basis)).measurable
  have hw : ∀ i, Measurable (fun z : ℝ × ℝ => heatTimeScore (f i) t ⟪u i,planePoint basis z⟫) :=
    fun i => (measurable_heatTimeScore (hf i) ht).comp
      (continuous_const.inner (continuous_planePoint basis)).measurable
  have hfirst : Measurable (fun z : ℝ × ℝ => ∑ i, c i*⟪u i,e⟫*heatSpaceScore (f i) t ⟪u i,planePoint basis z⟫) := by
    apply Finset.measurable_sum
    intro i _
    exact measurable_const.mul (hv i)
  refine ⟨hP.mul hfirst, hP.mul ((hfirst.pow_const 2).add ?_)⟩
  apply Finset.measurable_sum
  intro i _
  exact measurable_const.mul ((hw i).sub ((hv i).pow_const 2))

/-- Both spatial derivatives needed for whole-plane integration by parts are integrable. -/
theorem integrable_geometricHeat_spatial_slopes_plane
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hm : ∀ i, 0 < ∫ y : ℝ, f i y)
    (hc : ∀ i, 0 ≤ c i) (hu : ∀ i, ‖u i‖ = 1) (hframe : IsWeightedFrame c u)
    (R : ℝ) (hR : 0 ≤ R) (hsupport : ∀ i y, f i y ≠ 0 → |y| ≤ R)
    (basis : OrthonormalBasis (Fin 2) ℝ E) {t : ℝ} (ht : 0 < t)
    (e : E) (he : ‖e‖ = 1) :
    Integrable (fun z : ℝ × ℝ => geometricHeatSpaceSlope f c u e t (planePoint basis z)) (volume.prod volume) ∧
    Integrable (fun z : ℝ × ℝ => geometricHeatSecondSlope f c u e t (planePoint basis z)) (volume.prod volume) := by
  obtain ⟨C₁,C₂,hbound⟩ := geometricHeat_spatial_envelopes f c u hf hn hm hc hu hframe R hR hsupport basis ht e he
  obtain ⟨hm₁,hm₂⟩ := measurable_geometricHeat_spatial_slopes_plane f c u hf hn hm basis ht e
  have henv := integrable_plane_polynomial_gaussian (by positivity : 0 < 1/(8*t))
  exact ⟨(henv.const_mul C₁).mono' hm₁.aestronglyMeasurable (Filter.Eventually.of_forall (fun z => (hbound z).1)),
    (henv.const_mul C₂).mono' hm₂.aestronglyMeasurable (Filter.Eventually.of_forall (fun z => (hbound z).2))⟩

/-- The concrete time slope is integrable, as required by the parabolic integral bridge. -/
theorem integrable_geometricHeatTimeSlope_plane
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hm : ∀ i, 0 < ∫ y : ℝ, f i y)
    (hc : ∀ i, 0 ≤ c i) (hu : ∀ i, ‖u i‖ = 1) (hframe : IsWeightedFrame c u)
    (R : ℝ) (hR : 0 ≤ R) (hsupport : ∀ i y, f i y ≠ 0 → |y| ≤ R)
    (basis : OrthonormalBasis (Fin 2) ℝ E) {t : ℝ} (ht : 0 < t) :
    Integrable (fun z : ℝ × ℝ => geometricHeatTimeSlope f c u t (planePoint basis z)) (volume.prod volume) := by
  let C := (∏ i, heatTailConstant (f i) R t ^ c i) * (∑ i, c i) *
    ((1+R^2)/(2*t^2) + 1/(2*t))
  apply ((integrable_plane_polynomial_gaussian (by positivity : 0 < 1/(8*t))).const_mul C).mono'
    (measurable_geometricHeatTimeSlope_plane f c u hf hn hm basis ht).aestronglyMeasurable
  exact Filter.Eventually.of_forall (fun z => geometricHeatTimeSlope_plane_bound_interval f c u hf hn hm hc hu hframe
    R hR hsupport basis ht le_rfl le_rfl z)

end
end ChowlaCosine.Beckner
