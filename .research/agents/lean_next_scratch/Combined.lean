-- SOURCE ChowlaCosine/Beckner/HeatFlowUniform.lean
import ChowlaCosine.Beckner.GeometricHeat

/-! # Uniform Gaussian bounds on positive compact time intervals

These estimates discharge concrete domination obligations in M4. They do
not assert the remaining integrated monotonicity or limit/density passage.
-/

open MeasureTheory Real
open scoped BigOperators Topology RealInnerProductSpace

namespace ChowlaCosine.Beckner
set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

/-- A single explicit tail constant valid throughout a positive time interval. -/
noncomputable def heatTailConstant (f : ℝ → ℝ) (R a : ℝ) : ℝ :=
  (∫ y : ℝ, f y) * exp (R^2 / (4*a)) / sqrt (4*π*a)

theorem heatTailConstant_nonneg {f : ℝ → ℝ} (hn : ∀ y, 0 ≤ f y) (R a : ℝ) :
    0 ≤ heatTailConstant f R a := by
  unfold heatTailConstant
  exact div_nonneg (mul_nonneg (integral_nonneg hn) (exp_pos _).le) (sqrt_nonneg _)

theorem heatFlow_gaussian_bound_interval {f : ℝ → ℝ} (hf : Integrable f)
    (hn : ∀ y, 0 ≤ f y) (R : ℝ) (hR : 0 ≤ R)
    (hsupport : ∀ y, f y ≠ 0 → |y| ≤ R)
    {a b t : ℝ} (ha : 0 < a) (hat : a ≤ t) (htb : t ≤ b) (x : ℝ) :
    heatFlow f t x ≤ heatTailConstant f R a * gaussian (1/(8*b)) x := by
  have ht : 0 < t := ha.trans_le hat
  have hb : 0 < b := ht.trans_le htb
  have hm : 0 ≤ ∫ y : ℝ, f y := integral_nonneg hn
  have hcoef : heatTailConstant f R t ≤ heatTailConstant f R a := by
    unfold heatTailConstant
    apply div_le_div₀
    · exact mul_nonneg hm (exp_pos _).le
    · apply mul_le_mul_of_nonneg_left _ hm
      apply exp_le_exp.mpr
      exact div_le_div_of_nonneg_left (sq_nonneg R) (by positivity) (by linarith)
    · exact sqrt_pos.mpr (by positivity)
    · apply sqrt_le_sqrt
      nlinarith [pi_pos]
  have hg : gaussian (1/(8*t)) x ≤ gaussian (1/(8*b)) x := by
    unfold gaussian
    apply exp_le_exp.mpr
    have hi : 1/(8*b) ≤ 1/(8*t) :=
      div_le_div_of_nonneg_left (by norm_num) (by positivity) (by linarith)
    nlinarith [mul_le_mul_of_nonneg_right hi (sq_nonneg x)]
  exact (heatFlow_gaussian_bound hf hn R hR hsupport ht x).trans
    (mul_le_mul hcoef hg (gaussian_pos _ _).le (by unfold heatTailConstant; positivity))

section
variable {ι E : Type*} [Fintype ι] [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- Concrete all-space product domination uniform on a whole positive time interval. -/
theorem geometricHeatProduct_gaussian_bound_interval
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hc : ∀ i, 0 ≤ c i) (hframe : IsWeightedFrame c u)
    (R : ℝ) (hR : 0 ≤ R) (hsupport : ∀ i y, f i y ≠ 0 → |y| ≤ R)
    {a b t : ℝ} (ha : 0 < a) (hat : a ≤ t) (htb : t ≤ b) (x : E) :
    geometricHeatProduct f c u t x ≤
      (∏ i, heatTailConstant (f i) R a ^ c i) * exp (-(1/(8*b)) * ‖x‖^2) := by
  exact frame_product_gaussian_bound c u hframe hc (fun i => heatFlow (f i) t)
    (fun i => heatTailConstant (f i) R a)
    (fun i => heatTailConstant_nonneg (hn i) R a)
    (1/(8*b)) (fun i y => heatFlow_nonneg (hn i) (ha.trans_le hat) y)
    (fun i y => heatFlow_gaussian_bound_interval (hf i) (hn i) R hR (hsupport i) ha hat htb y) x

/-- Uniform relative time-score bound in Euclidean radius for every unit direction. -/
theorem heatTimeScore_bound_interval {f : ℝ → ℝ} (hf : Integrable f)
    (hn : ∀ y, 0 ≤ f y) (hm : 0 < ∫ y : ℝ, f y)
    (R : ℝ) (hR : 0 ≤ R) (hsupport : ∀ y, f y ≠ 0 → |y| ≤ R)
    {a t : ℝ} (ha : 0 < a) (hat : a ≤ t) (u x : E) (hu : ‖u‖ = 1) :
    |heatTimeScore f t ⟪u,x⟫| ≤ (‖x‖+R)^2/(4*a^2) + 1/(2*a) := by
  have ht : 0 < t := ha.trans_le hat
  have hi : |⟪u,x⟫| ≤ ‖x‖ := by simpa only [hu, one_mul] using abs_real_inner_le_norm u x
  have hsq : (|⟪u,x⟫|+R)^2 ≤ (‖x‖+R)^2 := by
    apply (sq_le_sq₀ (by positivity) (by positivity)).mpr
    linarith
  have H := heatFlow_time_score_bound hf hn hm R hR hsupport ht ⟪u,x⟫
  change |heatTimeScore f t ⟪u,x⟫| ≤ _ at H
  apply H.trans
  apply add_le_add
  · apply div_le_div₀ (by positivity) hsq (by positivity)
    nlinarith [sq_nonneg (t-a)]
  · exact div_le_div_of_nonneg_left (by norm_num) (by positivity) (by linarith)

/-- Uniform relative spatial-score bound in Euclidean radius. -/
theorem heatSpaceScore_bound_interval {f : ℝ → ℝ} (hf : Integrable f)
    (hn : ∀ y, 0 ≤ f y) (hm : 0 < ∫ y : ℝ, f y)
    (R : ℝ) (hR : 0 ≤ R) (hsupport : ∀ y, f y ≠ 0 → |y| ≤ R)
    {a t : ℝ} (ha : 0 < a) (hat : a ≤ t) (u x : E) (hu : ‖u‖ = 1) :
    |heatSpaceScore f t ⟪u,x⟫| ≤ (‖x‖+R)/(2*a) := by
  have ht : 0 < t := ha.trans_le hat
  have hi : |⟪u,x⟫| ≤ ‖x‖ := by simpa only [hu, one_mul] using abs_real_inner_le_norm u x
  have H := heatFlow_space_score_bound hf hn hm R hR hsupport ht ⟪u,x⟫
  change |heatSpaceScore f t ⟪u,x⟫| ≤ _ at H
  exact H.trans (div_le_div₀ (by positivity) (by linarith) (by positivity) (by linarith))

/-- Actual time derivative has a uniform Gaussian-polynomial envelope. -/
theorem geometricHeatProduct_time_derivative_bound_interval
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hm : ∀ i, 0 < ∫ y : ℝ, f i y)
    (hc : ∀ i, 0 ≤ c i) (hu : ∀ i, ‖u i‖ = 1) (hframe : IsWeightedFrame c u)
    (R : ℝ) (hR : 0 ≤ R) (hsupport : ∀ i y, f i y ≠ 0 → |y| ≤ R)
    {a b t : ℝ} (ha : 0 < a) (hat : a ≤ t) (htb : t ≤ b) (x : E) :
    |deriv (fun s => geometricHeatProduct f c u s x) t| ≤
      ((∏ i, heatTailConstant (f i) R a ^ c i) * exp (-(1/(8*b)) * ‖x‖^2)) *
        (∑ i, c i) * ((‖x‖+R)^2/(4*a^2) + 1/(2*a)) := by
  have ht : 0 < t := ha.trans_le hat
  have hP : 0 ≤ geometricHeatProduct f c u t x :=
    Finset.prod_nonneg (fun i _ => rpow_nonneg (heatFlow_nonneg (hn i) ht _) _)
  have hsum : |∑ i, c i * heatTimeScore (f i) t ⟪u i,x⟫| ≤
      (∑ i, c i) * ((‖x‖+R)^2/(4*a^2) + 1/(2*a)) := by
    calc
      _ ≤ ∑ i, |c i * heatTimeScore (f i) t ⟪u i,x⟫| := Finset.abs_sum_le_sum_abs _ _
      _ ≤ ∑ i, c i * ((‖x‖+R)^2/(4*a^2) + 1/(2*a)) := by
        apply Finset.sum_le_sum
        intro i _
        rw [abs_mul, abs_of_nonneg (hc i)]
        exact mul_le_mul_of_nonneg_left
          (heatTimeScore_bound_interval (hf i) (hn i) (hm i) R hR (hsupport i) ha hat (u i) x (hu i)) (hc i)
      _ = _ := by rw [Finset.sum_mul]
  rw [(hasDerivAt_geometricHeatProduct_time f c u hf hn hm ht x).deriv,
    abs_mul, abs_of_nonneg hP]
  calc
    _ ≤ geometricHeatProduct f c u t x *
        ((∑ i, c i) * ((‖x‖+R)^2/(4*a^2) + 1/(2*a))) :=
      mul_le_mul_of_nonneg_left hsum hP
    _ ≤ _ := by
      have H := geometricHeatProduct_gaussian_bound_interval f c u hf hn hc hframe R hR hsupport ha hat htb x
      have hs : 0 ≤ ∑ i, c i := Finset.sum_nonneg (fun i _ => hc i)
      have HB := mul_le_mul_of_nonneg_right H (mul_nonneg hs (by positivity :
        0 ≤ (‖x‖+R)^2/(4*a^2) + 1/(2*a)))
      simpa only [mul_assoc] using HB

end
end ChowlaCosine.Beckner


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
#print axioms ChowlaCosine.Beckner.heatTailConstant_nonneg
#print axioms ChowlaCosine.Beckner.heatFlow_gaussian_bound_interval
#print axioms ChowlaCosine.Beckner.geometricHeatProduct_gaussian_bound_interval
#print axioms ChowlaCosine.Beckner.heatTimeScore_bound_interval
#print axioms ChowlaCosine.Beckner.heatSpaceScore_bound_interval
#print axioms ChowlaCosine.Beckner.geometricHeatProduct_time_derivative_bound_interval
#print axioms ChowlaCosine.Beckner.continuous_heatFlow_space
#print axioms ChowlaCosine.Beckner.continuous_heatSpaceMoment_space
#print axioms ChowlaCosine.Beckner.measurable_heatTimeMoment
#print axioms ChowlaCosine.Beckner.measurable_heatTimeScore
#print axioms ChowlaCosine.Beckner.integrable_plane_polynomial_gaussian
#print axioms ChowlaCosine.Beckner.heat_score_polynomial_bound
#print axioms ChowlaCosine.Beckner.continuous_planePoint
#print axioms ChowlaCosine.Beckner.norm_planePoint_sq
#print axioms ChowlaCosine.Beckner.continuous_geometricHeatProduct_space
#print axioms ChowlaCosine.Beckner.measurable_geometricHeatTimeSlope_plane
#print axioms ChowlaCosine.Beckner.geometricHeatTimeSlope_plane_bound_interval
#print axioms ChowlaCosine.Beckner.integrable_geometricHeatProduct_plane
#print axioms ChowlaCosine.Beckner.hasDerivAt_integral_geometricHeatProduct_plane
#print axioms ChowlaCosine.Beckner.abs_weighted_directional_score_le
#print axioms ChowlaCosine.Beckner.abs_weighted_second_score_le
#print axioms ChowlaCosine.Beckner.hasDerivAt_geometricHeatSpaceSlope_line
#print axioms ChowlaCosine.Beckner.geometricHeat_spatial_envelopes
#print axioms ChowlaCosine.Beckner.measurable_heatSpaceScore
#print axioms ChowlaCosine.Beckner.measurable_geometricHeat_spatial_slopes_plane
#print axioms ChowlaCosine.Beckner.integrable_geometricHeat_spatial_slopes_plane
#print axioms ChowlaCosine.Beckner.integrable_geometricHeatTimeSlope_plane
#print axioms ChowlaCosine.Beckner.geometricHeatProduct_integral_derivative_nonneg
#print axioms ChowlaCosine.Beckner.geometricHeatProduct_integral_monotone
#print axioms ChowlaCosine.Beckner.tendsto_rescaledHeatFlow
#print axioms ChowlaCosine.Beckner.heatKernel_rescale
#print axioms ChowlaCosine.Beckner.rescaledHeatFlow_eq_heatFlow
#print axioms ChowlaCosine.Beckner.tendsto_heatFlow_large_time
#print axioms ChowlaCosine.Beckner.tendsto_sqrt_mul_heatFlow
