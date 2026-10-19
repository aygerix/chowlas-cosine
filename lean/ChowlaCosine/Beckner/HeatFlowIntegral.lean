import ChowlaCosine.Beckner.HeatFlowUniform

/-! # Concrete domination and time differentiation of the planar heat-product integral -/

open MeasureTheory Real
open scoped BigOperators Topology RealInnerProductSpace

namespace ChowlaCosine.Beckner
set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

@[fun_prop] theorem continuous_heatFlow_space {f : ℝ → ℝ} (hf : Integrable f)
    {t : ℝ} (ht : 0 < t) : Continuous (heatFlow f t) :=
  continuous_iff_continuousAt.mpr (fun x => (hasDerivAt_heatFlow_space hf ht x).continuousAt)

@[fun_prop] theorem continuous_heatSpaceMoment_space {f : ℝ → ℝ} (hf : Integrable f)
    {t : ℝ} (ht : 0 < t) : Continuous (heatSpaceMoment f t) :=
  continuous_iff_continuousAt.mpr (fun x => (hasDerivAt_heatFlow_space_slope hf ht x).continuousAt)

/-- Measurability of the actual second/time moment follows from its spatial derivative. -/
theorem measurable_heatTimeMoment {f : ℝ → ℝ} (hf : Integrable f)
    {t : ℝ} (ht : 0 < t) : Measurable (heatTimeMoment f t) := by
  have heq : heatTimeMoment f t = deriv (heatSpaceMoment f t) := by
    funext x
    exact (hasDerivAt_heatFlow_space_slope hf ht x).deriv.symm
  rw [heq]
  exact measurable_deriv _

theorem measurable_heatTimeScore {f : ℝ → ℝ} (hf : Integrable f)
    {t : ℝ} (ht : 0 < t) : Measurable (heatTimeScore f t) :=
  (measurable_heatTimeMoment hf ht).div (continuous_heatFlow_space hf ht).measurable

/-- Gaussian-polynomial integrability on the actual unbounded coordinate plane. -/
theorem integrable_plane_polynomial_gaussian {d : ℝ} (hd : 0 < d) :
    Integrable (fun z : ℝ × ℝ => (1 + (z.1^2 + z.2^2)) *
      exp (-d * (z.1^2 + z.2^2))) (volume.prod volume) := by
  have hg := integrable_exp_neg_mul_sq hd
  have hq : Integrable (fun x : ℝ => x^2 * exp (-d*x^2)) := by
    simpa only [rpow_two] using
      integrable_rpow_mul_exp_neg_mul_sq hd (show (-1 : ℝ) < 2 by norm_num)
  have H := ((hg.mul_prod hg).add (hq.mul_prod hg)).add (hg.mul_prod hq)
  apply H.congr
  exact Filter.Eventually.of_forall (fun z => by
    simp only [Pi.add_apply]
    rw [show -d*(z.1^2+z.2^2) = -d*z.1^2 + -d*z.2^2 by ring, exp_add]
    ring)

/-- A concrete quadratic score envelope with coefficients independent of position. -/
theorem heat_score_polynomial_bound (a R r : ℝ) (ha : 0 < a) :
    (r+R)^2/(4*a^2) + 1/(2*a) ≤
      ((1+R^2)/(2*a^2) + 1/(2*a)) * (1+r^2) := by
  have hsq : (r+R)^2 ≤ 2*(1+R^2)*(1+r^2) := by
    nlinarith [sq_nonneg (r-R), mul_nonneg (sq_nonneg R) (sq_nonneg r)]
  have H := div_le_div_of_nonneg_right hsq (by positivity : 0 ≤ 4*a^2)
  have he : (2*(1+R^2)*(1+r^2))/(4*a^2) = (1+R^2)/(2*a^2)*(1+r^2) := by ring
  rw [he] at H
  have hp : 0 ≤ 1/(2*a) := by positivity
  nlinarith [mul_nonneg hp (sq_nonneg r)]

section
variable {ι E : Type*} [Fintype ι] [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- The ordinary coordinate plane associated with a two-vector orthonormal basis. -/
noncomputable def planePoint (b : OrthonormalBasis (Fin 2) ℝ E) (z : ℝ × ℝ) : E :=
  z.1 • b 0 + z.2 • b 1

@[fun_prop] theorem continuous_planePoint (b : OrthonormalBasis (Fin 2) ℝ E) :
    Continuous (planePoint b) := by unfold planePoint; fun_prop

theorem norm_planePoint_sq (b : OrthonormalBasis (Fin 2) ℝ E) (z : ℝ × ℝ) :
    ‖planePoint b z‖^2 = z.1^2 + z.2^2 := by
  unfold planePoint
  rw [norm_add_sq_real]
  simp [norm_smul, b.norm_eq_one, real_inner_smul_left, real_inner_smul_right,
    b.inner_eq_zero (by decide : (0 : Fin 2) ≠ 1)]

@[fun_prop] theorem continuous_geometricHeatProduct_space
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hm : ∀ i, 0 < ∫ y : ℝ, f i y) {t : ℝ} (ht : 0 < t) :
    Continuous (geometricHeatProduct f c u t) := by
  unfold geometricHeatProduct
  apply continuous_finsetProd
  intro i _
  exact ((continuous_heatFlow_space (hf i) ht).comp (continuous_const.inner continuous_id)).rpow_const
    (fun x => Or.inl (heatFlow_pos (hf i) (hn i) (hm i) ht _).ne')

/-- The explicit time slope used in dominated differentiation, with measurable factors. -/
noncomputable def geometricHeatTimeSlope (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (t : ℝ) (x : E) : ℝ :=
  geometricHeatProduct f c u t x * ∑ i, c i * heatTimeScore (f i) t ⟪u i,x⟫

theorem measurable_geometricHeatTimeSlope_plane
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hm : ∀ i, 0 < ∫ y : ℝ, f i y) (b : OrthonormalBasis (Fin 2) ℝ E)
    {t : ℝ} (ht : 0 < t) :
    Measurable (fun z : ℝ × ℝ => geometricHeatTimeSlope f c u t (planePoint b z)) := by
  apply Measurable.mul
  · exact ((continuous_geometricHeatProduct_space f c u hf hn hm ht).comp
      (continuous_planePoint b)).measurable
  · apply Finset.measurable_sum
    intro i _
    exact measurable_const.mul ((measurable_heatTimeScore (hf i) ht).comp
      (continuous_const.inner (continuous_planePoint b)).measurable)

/-- Explicit integrable domination for the time slope, uniform on [a,b]. -/
theorem geometricHeatTimeSlope_plane_bound_interval
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hm : ∀ i, 0 < ∫ y : ℝ, f i y)
    (hc : ∀ i, 0 ≤ c i) (hu : ∀ i, ‖u i‖ = 1) (hframe : IsWeightedFrame c u)
    (R : ℝ) (hR : 0 ≤ R) (hsupport : ∀ i y, f i y ≠ 0 → |y| ≤ R)
    (basis : OrthonormalBasis (Fin 2) ℝ E)
    {a b t : ℝ} (ha : 0 < a) (hat : a ≤ t) (htb : t ≤ b) (z : ℝ × ℝ) :
    |geometricHeatTimeSlope f c u t (planePoint basis z)| ≤
      ((∏ i, heatTailConstant (f i) R a ^ c i) * (∑ i, c i) *
        ((1+R^2)/(2*a^2) + 1/(2*a))) *
      ((1+(z.1^2+z.2^2)) * exp (-(1/(8*b)) * (z.1^2+z.2^2))) := by
  have ht : 0 < t := ha.trans_le hat
  have H := geometricHeatProduct_time_derivative_bound_interval f c u hf hn hm hc hu hframe
    R hR hsupport ha hat htb (planePoint basis z)
  rw [(hasDerivAt_geometricHeatProduct_time f c u hf hn hm ht _).deriv] at H
  change |geometricHeatTimeSlope f c u t (planePoint basis z)| ≤ _ at H
  apply H.trans
  have hp : 0 ≤ (∏ i, heatTailConstant (f i) R a ^ c i) *
      exp (-(1/(8*b)) * ‖planePoint basis z‖^2) * ∑ i, c i := by
    apply mul_nonneg
    · exact mul_nonneg (Finset.prod_nonneg (fun i _ => rpow_nonneg
        (heatTailConstant_nonneg (hn i) R a) _)) (exp_pos _).le
    · exact Finset.sum_nonneg (fun i _ => hc i)
  have HH := mul_le_mul_of_nonneg_left
    (heat_score_polynomial_bound a R ‖planePoint basis z‖ ha) hp
  rw [norm_planePoint_sq] at HH
  rw [norm_planePoint_sq]
  convert HH using 1 <;> ring

/-- The concrete geometric product is integrable on the entire coordinate plane. -/
theorem integrable_geometricHeatProduct_plane
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hm : ∀ i, 0 < ∫ y : ℝ, f i y)
    (hc : ∀ i, 0 ≤ c i) (hframe : IsWeightedFrame c u)
    (R : ℝ) (hR : 0 ≤ R) (hsupport : ∀ i y, f i y ≠ 0 → |y| ≤ R)
    (basis : OrthonormalBasis (Fin 2) ℝ E) {t : ℝ} (ht : 0 < t) :
    Integrable (fun z : ℝ × ℝ => geometricHeatProduct f c u t (planePoint basis z))
      (volume.prod volume) := by
  let K := ∏ i, heatTailConstant (f i) R t ^ c i
  have hK : 0 ≤ K := Finset.prod_nonneg (fun i _ => rpow_nonneg
    (heatTailConstant_nonneg (hn i) R t) _)
  apply ((integrable_plane_polynomial_gaussian (by positivity : 0 < 1/(8*t))).const_mul K).mono'
  · exact ((continuous_geometricHeatProduct_space f c u hf hn hm ht).comp
      (continuous_planePoint basis)).aestronglyMeasurable
  · apply Filter.Eventually.of_forall
    intro z
    rw [Real.norm_eq_abs, abs_of_nonneg (show 0 ≤ geometricHeatProduct f c u t (planePoint basis z) from
      Finset.prod_nonneg (fun i _ => rpow_nonneg (heatFlow_nonneg (hn i) ht _) _))]
    have H := geometricHeatProduct_gaussian_bound_interval f c u hf hn hc hframe R hR hsupport
      ht (le_refl t) (le_refl t) (planePoint basis z)
    rw [norm_planePoint_sq] at H
    apply H.trans
    change K * _ ≤ K * _
    have hq : 0 ≤ z.1^2+z.2^2 := add_nonneg (sq_nonneg _) (sq_nonneg _)
    have he : 0 ≤ exp (-(1/(8*t))*(z.1^2+z.2^2)) := (exp_pos _).le
    nlinarith [mul_nonneg hK (mul_nonneg hq he)]

/-- Dominated differentiation for the actual geometric heat-product integral on R².
All measurability, integrability and uniform domination hypotheses are discharged
for nonnegative interval-supported L1 data of positive mass. -/
theorem hasDerivAt_integral_geometricHeatProduct_plane
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hm : ∀ i, 0 < ∫ y : ℝ, f i y)
    (hc : ∀ i, 0 ≤ c i) (hu : ∀ i, ‖u i‖ = 1) (hframe : IsWeightedFrame c u)
    (R : ℝ) (hR : 0 ≤ R) (hsupport : ∀ i y, f i y ≠ 0 → |y| ≤ R)
    (basis : OrthonormalBasis (Fin 2) ℝ E) {t : ℝ} (ht : 0 < t) :
    HasDerivAt (fun s => ∫ z : ℝ × ℝ, geometricHeatProduct f c u s (planePoint basis z)
      ∂volume.prod volume)
      (∫ z : ℝ × ℝ, geometricHeatTimeSlope f c u t (planePoint basis z) ∂volume.prod volume) t := by
  let a := t/2
  let b := 2*t
  have ha : 0 < a := by dsimp [a]; positivity
  have hb : 0 < b := by dsimp [b]; positivity
  have hs : Set.Ioo a b ∈ 𝓝 t := Ioo_mem_nhds (by dsimp [a]; linarith) (by dsimp [b]; linarith)
  let C := (∏ i, heatTailConstant (f i) R a ^ c i) * (∑ i, c i) *
    ((1+R^2)/(2*a^2) + 1/(2*a))
  let bound : ℝ × ℝ → ℝ := fun z => C *
    ((1+(z.1^2+z.2^2)) * exp (-(1/(8*b)) * (z.1^2+z.2^2)))
  have hFmeas : ∀ᶠ s in 𝓝 t, AEStronglyMeasurable
      (fun z : ℝ × ℝ => geometricHeatProduct f c u s (planePoint basis z)) (volume.prod volume) := by
    filter_upwards [Ioi_mem_nhds ht] with s hs
    exact ((continuous_geometricHeatProduct_space f c u hf hn hm hs).comp
      (continuous_planePoint basis)).aestronglyMeasurable
  have hbound : ∀ᵐ z : ℝ × ℝ ∂volume.prod volume, ∀ s ∈ Set.Ioo a b,
      ‖geometricHeatTimeSlope f c u s (planePoint basis z)‖ ≤ bound z := by
    apply Filter.Eventually.of_forall
    intro z s hs
    exact geometricHeatTimeSlope_plane_bound_interval f c u hf hn hm hc hu hframe R hR hsupport
      basis ha hs.1.le hs.2.le z
  have hdt : ∀ᵐ z : ℝ × ℝ ∂volume.prod volume, ∀ s ∈ Set.Ioo a b,
      HasDerivAt (fun r => geometricHeatProduct f c u r (planePoint basis z))
        (geometricHeatTimeSlope f c u s (planePoint basis z)) s := by
    apply Filter.Eventually.of_forall
    intro z s hs
    exact hasDerivAt_geometricHeatProduct_time f c u hf hn hm (ha.trans hs.1) _
  exact (hasDerivAt_integral_of_dominated_loc_of_deriv_le (μ := volume.prod volume)
    hs hFmeas (integrable_geometricHeatProduct_plane f c u hf hn hm hc hframe R hR hsupport basis ht)
    (measurable_geometricHeatTimeSlope_plane f c u hf hn hm basis ht).aestronglyMeasurable
    hbound ((integrable_plane_polynomial_gaussian (by positivity : 0 < 1/(8*b))).const_mul C) hdt).2

end
end ChowlaCosine.Beckner
