import ChowlaCosine.Beckner.Gaussian

/-!
# Finite-frame variance and the real heat kernel

These are ingredients of the paper heat-flow proof in the report. They do
not assert the missing dominated-differentiation, density, or sharp-Young
steps.
-/

open MeasureTheory Real
open scoped ENNReal NNReal RealInnerProductSpace

namespace ChowlaCosine.Beckner

set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

section Frame
variable {ι E : Type*} [Fintype ι] [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- The weighted rank-one frame identity, explicitly quantified over the
whole real inner product space. This is a datum, not an asserted existence. -/
def IsWeightedFrame (c : ι → ℝ) (u : ι → E) : Prop :=
  ∀ x y : E, (∑ i, c i * (⟪u i, x⟫ * ⟪u i, y⟫)) = ⟪x, y⟫

noncomputable def frameVector (c v : ι → ℝ) (u : ι → E) : E :=
  ∑ i, (c i * v i) • u i

/-- Exact sum of squares behind geometric Brascamp–Lieb heat flow. -/
theorem frame_variance_identity (c v : ι → ℝ) (u : ι → E) (hframe : IsWeightedFrame c u) :
    (∑ i, c i * (v i - ⟪u i, frameVector c v u⟫) ^ 2) =
      (∑ i, c i * v i ^ 2) - ‖frameVector c v u‖ ^ 2 := by
  let V := frameVector c v u
  have hcross : (∑ i, (c i * v i) * ⟪u i, V⟫) = ‖V‖ ^ 2 := by
    rw [← real_inner_self_eq_norm_sq]
    change (∑ i, (c i * v i) * ⟪u i, V⟫) = ⟪∑ i, (c i * v i) • u i, V⟫
    rw [sum_inner]
    simp only [real_inner_smul_left]
  have hdiag : (∑ i, c i * ⟪u i, V⟫ ^ 2) = ‖V‖ ^ 2 := by
    simpa only [pow_two, real_inner_self_eq_norm_sq] using hframe V V
  change (∑ i, c i * (v i - ⟪u i, V⟫) ^ 2) = _
  calc
    _ = (∑ i, c i * v i ^ 2) - 2 * (∑ i, (c i * v i) * ⟪u i, V⟫) +
        (∑ i, c i * ⟪u i, V⟫ ^ 2) := by
      have he : ∀ i, c i * (v i - ⟪u i, V⟫) ^ 2 =
          c i * v i ^ 2 - 2 * ((c i * v i) * ⟪u i, V⟫) + c i * ⟪u i, V⟫ ^ 2 := by
        intro i
        ring
      simp_rw [he, Finset.sum_add_distrib, Finset.sum_sub_distrib, ← Finset.mul_sum]
    _ = _ := by rw [hcross, hdiag]; dsimp [V]; ring

/-- The nonnegative heat-flow defect for every weighted geometric frame. -/
theorem frame_variance_nonneg (c v : ι → ℝ) (u : ι → E)
    (hc : ∀ i, 0 ≤ c i) (hframe : IsWeightedFrame c u) :
    ‖frameVector c v u‖ ^ 2 ≤ ∑ i, c i * v i ^ 2 := by
  have H : 0 ≤ ∑ i, c i * (v i - ⟪u i, frameVector c v u⟫) ^ 2 :=
    Finset.sum_nonneg (fun i _ => mul_nonneg (hc i) (sq_nonneg _))
  rw [frame_variance_identity c v u hframe] at H
  linarith
end Frame

noncomputable def heatKernel (t x : ℝ) : ℝ :=
  gaussian (1 / (4 * t)) x / Real.sqrt (4 * Real.pi * t)

theorem heatKernel_pos {t : ℝ} (ht : 0 < t) (x : ℝ) : 0 < heatKernel t x := by
  unfold heatKernel
  exact div_pos (gaussian_pos _ _) (Real.sqrt_pos.mpr (by positivity))

theorem integrable_heatKernel {t : ℝ} (ht : 0 < t) : Integrable (heatKernel t) :=
  (integrable_gaussian (by positivity : 0 < 1 / (4 * t))).div_const _

/-- Exact probability normalization at every positive time. -/
theorem integral_heatKernel {t : ℝ} (ht : 0 < t) : (∫ x : ℝ, heatKernel t x) = 1 := by
  unfold heatKernel
  rw [integral_div, integral_gaussian_exact]
  have he : Real.pi / (1 / (4 * t)) = 4 * Real.pi * t := by field_simp
  rw [he]
  exact div_self (Real.sqrt_pos.mpr (by positivity)).ne'

/-- Spatial derivative of an arbitrary-width Gaussian. -/
theorem hasDerivAt_gaussian (a x : ℝ) :
    HasDerivAt (gaussian a) ((-2 * a * x) * gaussian a x) x := by
  have H := (((hasDerivAt_id x).pow 2).const_mul (-a)).exp
  dsimp [id_eq, Pi.pow_apply] at H
  convert H using 1 <;> unfold gaussian <;> ring


/-- First spatial heat-kernel derivative. -/
theorem hasDerivAt_heatKernel_space {t : ℝ} (ht : 0 < t) (x : ℝ) :
    HasDerivAt (heatKernel t) ((-x / (2 * t)) * heatKernel t x) x := by
  have H := (hasDerivAt_gaussian (1 / (4 * t)) x).div_const (Real.sqrt (4 * Real.pi * t))
  change HasDerivAt (heatKernel t) _ x at H
  apply H.congr_deriv
  unfold heatKernel
  field_simp
  <;> ring

/-- Second Gaussian derivative in a form usable without a derivative operator. -/
theorem hasDerivAt_gaussian_slope (a x : ℝ) :
    HasDerivAt (fun y => (-2 * a * y) * gaussian a y)
      ((4 * a ^ 2 * x ^ 2 - 2 * a) * gaussian a x) x := by
  have H := ((hasDerivAt_id x).const_mul (-2 * a)).mul (hasDerivAt_gaussian a x)
  dsimp [id_eq, Pi.mul_apply] at H
  exact H.congr_deriv (by ring)

/-- Explicit scalar heat-kernel expression for differentiation in time. -/
theorem heatKernel_eq (t x : ℝ) :
    heatKernel t x = Real.exp (-(x ^ 2) / (4 * t)) / Real.sqrt (4 * Real.pi * t) := by
  unfold heatKernel gaussian
  congr 2
  ring

/-- The spatial derivative itself has the expected second derivative. -/
theorem hasDerivAt_heatKernel_slope {t : ℝ} (ht : 0 < t) (x : ℝ) :
    HasDerivAt (fun y => (-y / (2 * t)) * heatKernel t y)
      ((x ^ 2 / (4 * t ^ 2) - 1 / (2 * t)) * heatKernel t x) x := by
  have H := ((hasDerivAt_id x).neg.div_const (2 * t)).mul (hasDerivAt_heatKernel_space ht x)
  dsimp [id_eq, Pi.mul_apply, Pi.neg_apply] at H
  change HasDerivAt (fun y => (-y / (2 * t)) * heatKernel t y) _ x at H
  apply H.congr_deriv
  field_simp
  <;> ring

/-- Exact time derivative; together with the previous theorem this is the
one-dimensional heat equation for every positive time and real x. -/
theorem hasDerivAt_heatKernel_time {t : ℝ} (ht : 0 < t) (x : ℝ) :
    HasDerivAt (fun s => heatKernel s x)
      ((x ^ 2 / (4 * t ^ 2) - 1 / (2 * t)) * heatKernel t x) t := by
  have hden := (hasDerivAt_id t).const_mul (4 : ℝ)
  have hnum := ((hasDerivAt_const t (-(x ^ 2))).div hden (by positivity : 4 * t ≠ 0)).exp
  have hroot := ((hasDerivAt_id t).const_mul (4 * Real.pi)).sqrt (by positivity : 4 * Real.pi * t ≠ 0)
  have H := hnum.div hroot (Real.sqrt_pos.mpr (by positivity)).ne'
  have hfun : (fun s : ℝ => Real.exp (-(x ^ 2) / (4 * s)) / Real.sqrt (4 * Real.pi * s)) =
      (fun s : ℝ => heatKernel s x) := by funext s; exact (heatKernel_eq s x).symm
  change HasDerivAt (fun s : ℝ => Real.exp (-(x ^ 2) / (4 * s)) / Real.sqrt (4 * Real.pi * s)) _ t at H
  rw [hfun] at H
  apply H.congr_deriv
  rw [heatKernel_eq]
  have hs : Real.sqrt (4 * Real.pi * t) ^ 2 = 4 * Real.pi * t := Real.sq_sqrt (by positivity)
  have hsn : Real.sqrt (4 * Real.pi * t) ≠ 0 := (Real.sqrt_pos.mpr (by positivity)).ne'
  dsimp
  field_simp
  have hst : Real.sqrt (4 * t * Real.pi) ^ 2 = 4 * t * Real.pi := Real.sq_sqrt (by positivity)
  rw [hst]
  ring


/-- Gaussian convolution gives the heat semigroup at all positive times. -/
theorem heatKernel_semigroup {s t : ℝ} (hs : 0 < s) (ht : 0 < t) (x : ℝ) :
    (∫ y : ℝ, heatKernel s y * heatKernel t (x - y)) = heatKernel (s + t) x := by
  have ha : 0 < 1 / (4 * s) := by positivity
  have hb : 0 < 1 / (4 * t) := by positivity
  have hw : (1 / (4 * s)) * (1 / (4 * t)) / (1 / (4 * s) + 1 / (4 * t)) =
      1 / (4 * (s + t)) := by field_simp; ring
  unfold heatKernel
  simp_rw [div_mul_div_comm]
  rw [integral_div, gaussian_convolution ha hb, hw]
  have hcoef : Real.sqrt (Real.pi / (1 / (4 * s) + 1 / (4 * t))) /
      (Real.sqrt (4 * Real.pi * s) * Real.sqrt (4 * Real.pi * t)) =
      1 / Real.sqrt (4 * Real.pi * (s + t)) := by
    rw [← Real.sqrt_mul (by positivity : 0 ≤ 4 * Real.pi * s),
      ← Real.sqrt_div (by positivity : 0 ≤ Real.pi / (1 / (4 * s) + 1 / (4 * t)))]
    have he : (Real.pi / (1 / (4 * s) + 1 / (4 * t))) / ((4 * Real.pi * s) * (4 * Real.pi * t)) =
        1 / (4 * Real.pi * (s + t)) := by field_simp; ring
    rw [he, Real.sqrt_div (by norm_num : (0 : ℝ) ≤ 1), Real.sqrt_one]
  calc
    _ = (Real.sqrt (Real.pi / (1 / (4 * s) + 1 / (4 * t))) /
        (Real.sqrt (4 * Real.pi * s) * Real.sqrt (4 * Real.pi * t))) *
        gaussian (1 / (4 * (s + t))) x := by ring
    _ = _ := by rw [hcoef]; ring

noncomputable def heatFlow (f : ℝ → ℝ) (t x : ℝ) : ℝ :=
  ∫ y : ℝ, f y * heatKernel t (x - y)

/-- Positivity preservation for arbitrary nonnegative initial functions.
The statement uses the standard real Bochner integral convention. -/
theorem heatFlow_nonneg {f : ℝ → ℝ} (hf : ∀ x, 0 ≤ f x) {t : ℝ} (ht : 0 < t) (x : ℝ) :
    0 ≤ heatFlow f t x :=
  integral_nonneg (fun y => mul_nonneg (hf y) (heatKernel_pos ht _).le)

/-- Exact mass preservation for arbitrary integrable initial data. -/
theorem integral_heatFlow {f : ℝ → ℝ} (hf : Integrable f) {t : ℝ} (ht : 0 < t) :
    (∫ x : ℝ, heatFlow f t x) = ∫ x : ℝ, f x := by
  have H := integral_convolution (ContinuousLinearMap.mul ℝ ℝ) hf (integrable_heatKernel ht)
  simpa only [MeasureTheory.convolution_mul, ContinuousLinearMap.mul_apply',
    heatFlow, integral_heatKernel ht, mul_one] using H


/-- Uniform spatial upper bound of the positive heat kernel. -/
theorem heatKernel_le {t : ℝ} (ht : 0 < t) (x : ℝ) :
    heatKernel t x ≤ 1 / Real.sqrt (4 * Real.pi * t) := by
  unfold heatKernel gaussian
  apply div_le_div_of_nonneg_right _ (Real.sqrt_nonneg _)
  exact Real.exp_le_one_iff.mpr (mul_nonpos_of_nonpos_of_nonneg
    (neg_nonpos.mpr (by positivity)) (sq_nonneg x))

theorem continuous_heatKernel (t : ℝ) : Continuous (heatKernel t) := by
  unfold heatKernel gaussian
  fun_prop

/-- Pointwise integrability of the heat convolution for every L1 datum. -/
theorem integrable_heatFlow_integrand {f : ℝ → ℝ} (hf : Integrable f)
    {t : ℝ} (ht : 0 < t) (x : ℝ) : Integrable (fun y : ℝ => f y * heatKernel t (x - y)) := by
  have hmeas : AEStronglyMeasurable (fun y : ℝ => heatKernel t (x - y)) :=
    ((continuous_heatKernel t).comp (continuous_const.sub continuous_id)).aestronglyMeasurable
  apply hf.mul_bdd (c := 1 / Real.sqrt (4 * Real.pi * t)) hmeas
  exact Filter.Eventually.of_forall (fun y => by
    rw [Real.norm_of_nonneg (heatKernel_pos ht _).le]
    exact heatKernel_le ht _)

/-- Strict positivity from positive initial mass, without requiring the
initial datum itself to be everywhere positive or continuous. -/
theorem heatFlow_pos {f : ℝ → ℝ} (hf : Integrable f) (hn : ∀ x, 0 ≤ f x)
    (hm : 0 < ∫ x : ℝ, f x) {t : ℝ} (ht : 0 < t) (x : ℝ) : 0 < heatFlow f t x := by
  unfold heatFlow
  apply (integral_pos_iff_support_of_nonneg (fun y => mul_nonneg (hn y) (heatKernel_pos ht _).le)
    (integrable_heatFlow_integrand hf ht x)).mpr
  have hs : Function.support (fun y : ℝ => f y * heatKernel t (x - y)) = Function.support f := by
    ext y
    simp only [Function.mem_support, ne_eq, mul_eq_zero, not_or, (heatKernel_pos ht _).ne',
      not_false_eq_true, and_true]
  rw [hs]
  exact (integral_pos_iff_support_of_nonneg hn hf).mp hm

/-- The elementary Gaussian shift bound used to obtain global domination. -/
theorem gaussian_shift_le (a x y : ℝ) (ha : 0 ≤ a) :
    gaussian a (x - y) ≤ Real.exp (a * y ^ 2) * gaussian (a / 2) x := by
  unfold gaussian
  rw [← Real.exp_add]
  apply Real.exp_le_exp.mpr
  nlinarith [mul_nonneg ha (sq_nonneg (x - 2 * y))]

/-- Actual Gaussian tail domination for heat flow with an interval-supported
L1 datum. The bound is global in x, not a compact-domain restriction. -/
theorem heatFlow_gaussian_bound {f : ℝ → ℝ} (hf : Integrable f)
    (hn : ∀ y, 0 ≤ f y) (R : ℝ) (hR : 0 ≤ R)
    (hsupport : ∀ y, f y ≠ 0 → |y| ≤ R) {t : ℝ} (ht : 0 < t) (x : ℝ) :
    heatFlow f t x ≤
      ((∫ y : ℝ, f y) * Real.exp (R ^ 2 / (4 * t)) / Real.sqrt (4 * Real.pi * t)) *
        gaussian (1 / (8 * t)) x := by
  have ht4 : 0 < 4 * t := by positivity
  have hpoint : ∀ y, f y * heatKernel t (x - y) ≤
      f y * (Real.exp (R ^ 2 / (4 * t)) / Real.sqrt (4 * Real.pi * t) *
        gaussian (1 / (8 * t)) x) := by
    intro y
    by_cases hy : f y = 0
    · simp [hy]
    have hyR := hsupport y hy
    have hysq : y ^ 2 ≤ R ^ 2 := by
      simpa only [sq_abs] using (sq_le_sq₀ (abs_nonneg y) hR).mpr hyR
    have H := gaussian_shift_le (1 / (4 * t)) x y (by positivity)
    have he : Real.exp ((1 / (4 * t)) * y ^ 2) ≤ Real.exp (R ^ 2 / (4 * t)) := by
      apply Real.exp_le_exp.mpr
      simpa only [one_div_mul_eq_div] using (div_le_div_of_nonneg_right hysq ht4.le)
    have hg : gaussian (1 / (4 * t)) (x - y) ≤
        Real.exp (R ^ 2 / (4 * t)) * gaussian (1 / (8 * t)) x := by
      have ee : (1 / (4 * t)) / 2 = 1 / (8 * t) := by ring
      exact (H.trans (mul_le_mul_of_nonneg_right he (gaussian_pos _ _).le)).trans_eq (by rw [ee])
    unfold heatKernel
    calc
      _ ≤ f y * ((Real.exp (R ^ 2 / (4 * t)) * gaussian (1 / (8 * t)) x) /
          Real.sqrt (4 * Real.pi * t)) := mul_le_mul_of_nonneg_left
            (div_le_div_of_nonneg_right hg (Real.sqrt_nonneg _)) (hn y)
      _ = _ := by ring
  have H := integral_mono (integrable_heatFlow_integrand hf ht x)
    (hf.mul_const _) hpoint
  simpa only [heatFlow, integral_mul_const, mul_div_assoc, mul_assoc] using H


section FrameGaussian
variable {ι E : Type*} [Fintype ι] [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- Frame geometry turns the product of one-dimensional Gaussian tails
into the Gaussian of the full Euclidean norm. -/
theorem frame_gaussian_identity (c : ι → ℝ) (u : ι → E) (hframe : IsWeightedFrame c u)
    (a : ℝ) (x : E) :
    (∏ i, gaussian a ⟪u i, x⟫ ^ c i) = Real.exp (-a * ‖x‖ ^ 2) := by
  unfold gaussian
  simp_rw [← Real.exp_mul]
  rw [← Real.exp_sum]
  congr 1
  have H : (∑ i, c i * ⟪u i, x⟫ ^ 2) = ‖x‖ ^ 2 := by
    simpa only [pow_two, real_inner_self_eq_norm_sq] using hframe x x
  calc
    _ = -a * ∑ i, c i * ⟪u i, x⟫ ^ 2 := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro i _
      ring
    _ = _ := by rw [H]

/-- Product Gaussian domination for arbitrary nonnegative functions on a
weighted frame. This is an actual all-space bound. -/
theorem frame_product_gaussian_bound (c : ι → ℝ) (u : ι → E) (hframe : IsWeightedFrame c u)
    (hc : ∀ i, 0 ≤ c i) (F : ι → ℝ → ℝ) (K : ι → ℝ) (hK : ∀ i, 0 ≤ K i)
    (a : ℝ) (hF : ∀ i y, 0 ≤ F i y) (hbound : ∀ i y, F i y ≤ K i * gaussian a y) (x : E) :
    (∏ i, F i ⟪u i, x⟫ ^ c i) ≤ (∏ i, K i ^ c i) * Real.exp (-a * ‖x‖ ^ 2) := by
  calc
    _ ≤ ∏ i, (K i * gaussian a ⟪u i, x⟫) ^ c i := by
      apply Finset.prod_le_prod
      · intro i _
        exact Real.rpow_nonneg (hF i _) _
      · intro i _
        exact Real.rpow_le_rpow (hF i _) (hbound i _) (hc i)
    _ = (∏ i, K i ^ c i) * ∏ i, gaussian a ⟪u i, x⟫ ^ c i := by
      simp_rw [Real.mul_rpow (hK _) (gaussian_pos _ _).le, Finset.prod_mul_distrib]
    _ = _ := by rw [frame_gaussian_identity c u hframe]

/-- Conditional scalar monotonicity reduction. The central analytic
hypothesis is stated explicitly: the differentiated integral identity.
This theorem does not assert that heat flow satisfies that hypothesis. -/
theorem monotone_of_heat_defect_identity {α : Type*} [MeasurableSpace α] (μ : Measure α)
    (c : ι → ℝ) (u : ι → E) (hc : ∀ i, 0 ≤ c i) (hframe : IsWeightedFrame c u)
    (P : ℝ → α → ℝ) (v : ℝ → α → ι → ℝ) (Φ : ℝ → ℝ)
    (hP : ∀ t > 0, ∀ x, 0 ≤ P t x)
    (hderiv : ∀ t > 0, HasDerivAt Φ
      (∫ x, P t x * ((∑ i, c i * v t x i ^ 2) - ‖frameVector c (v t x) u‖ ^ 2) ∂μ) t) :
    MonotoneOn Φ (Set.Ioi 0) := by
  apply monotoneOn_of_hasDerivWithinAt_nonneg (convex_Ioi (0 : ℝ))
  · exact fun t ht => (hderiv t ht).continuousAt.continuousWithinAt
  · intro t ht
    exact (hderiv t ((interior_subset ht) : t ∈ Set.Ioi 0)).hasDerivWithinAt
  · intro t ht
    apply integral_nonneg
    intro x
    exact mul_nonneg (hP t (interior_subset ht) x)
      (sub_nonneg.mpr (frame_variance_nonneg c (v t x) u hc hframe))
end FrameGaussian


/-- A global polynomial-times-Gaussian bound, used for dominated
parameter differentiation without a compact-support assumption. -/
theorem gaussian_quadratic_le {a : ℝ} (ha : 0 < a) (x : ℝ) :
    x ^ 2 * gaussian a x ≤ 1 / a := by
  have H := Real.mul_exp_neg_le_exp_neg_one (a * x ^ 2)
  have he : Real.exp (-1) ≤ 1 := Real.exp_le_one_iff.mpr (by norm_num)
  have HH : (a * x ^ 2) * gaussian a x ≤ 1 := by
    simpa only [gaussian, neg_mul] using H.trans he
  apply (le_div_iff₀ ha).mpr
  nlinarith [HH]

/-- Uniform spatial bound on the time/second-spatial derivative of the
heat kernel. -/
theorem heatKernel_time_slope_bound {t : ℝ} (ht : 0 < t) (x : ℝ) :
    |(x ^ 2 / (4 * t ^ 2) - 1 / (2 * t)) * heatKernel t x| ≤
      3 / (2 * t * Real.sqrt (4 * Real.pi * t)) := by
  have hs : 0 < Real.sqrt (4 * Real.pi * t) := Real.sqrt_pos.mpr (by positivity)
  have hgauss : gaussian (1 / (4 * t)) x ≤ 1 := by
    unfold gaussian
    apply Real.exp_le_one_iff.mpr
    exact mul_nonpos_of_nonpos_of_nonneg (neg_nonpos.mpr (by positivity)) (sq_nonneg _)
  have hquad : x ^ 2 * gaussian (1 / (4 * t)) x ≤ 4 * t := by
    simpa only [one_div_one_div] using gaussian_quadratic_le (by positivity : 0 < 1 / (4 * t)) x
  calc
    _ ≤ (x ^ 2 / (4 * t ^ 2) + 1 / (2 * t)) * heatKernel t x := by
      rw [abs_mul, abs_of_nonneg (heatKernel_pos ht x).le]
      apply mul_le_mul_of_nonneg_right _ (heatKernel_pos ht x).le
      exact (abs_sub _ _).trans (by rw [abs_of_nonneg (by positivity), abs_of_nonneg (by positivity)])
    _ = ((x ^ 2 * gaussian (1 / (4 * t)) x) / (4 * t ^ 2) +
        gaussian (1 / (4 * t)) x / (2 * t)) / Real.sqrt (4 * Real.pi * t) := by
      unfold heatKernel
      ring
    _ ≤ ((4 * t) / (4 * t ^ 2) + 1 / (2 * t)) / Real.sqrt (4 * Real.pi * t) := by
      gcongr
    _ = _ := by field_simp; ring

/-- Monotonicity of the explicit derivative envelope in positive time. -/
theorem heatKernel_time_envelope_le {a t : ℝ} (ha : 0 < a) (hat : a ≤ t) :
    3 / (2 * t * Real.sqrt (4 * Real.pi * t)) ≤
      3 / (2 * a * Real.sqrt (4 * Real.pi * a)) := by
  have ht : 0 < t := ha.trans_le hat
  apply div_le_div_of_nonneg_left (by norm_num) (by positivity)
  apply mul_le_mul
  · linarith
  · exact Real.sqrt_le_sqrt (mul_le_mul_of_nonneg_left hat (by positivity))
  · positivity
  · positivity

end ChowlaCosine.Beckner
