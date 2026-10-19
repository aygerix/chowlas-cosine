import Mathlib

/-!
# Non-sharp Young on the real line

`young_finite` proves M1 for all finite admissible exponent triples and
arbitrary complex Lp functions on R. `young_conjugate` proves the L∞
output boundary. No boundedness, compact support, or finite-group
replacement is made.
-/

open MeasureTheory Real
open scoped ENNReal NNReal Convolution

namespace ChowlaCosine.Beckner

set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

noncomputable def convolution (f g : ℝ → ℂ) (x : ℝ) : ℂ :=
  ∫ y : ℝ, f y * g (x - y)

noncomputable def normConvolution (f g : ℝ → ℂ) (x : ℝ) : ℝ :=
  ∫ y : ℝ, ‖f y‖ * ‖g (x - y)‖

/-- Exact all-real norm domination, with the standard Bochner convention
that a nonintegrable integral is zero. -/
theorem norm_convolution_le (f g : ℝ → ℂ) (x : ℝ) :
    ‖convolution f g x‖ ≤ normConvolution f g x := by
  unfold convolution normConvolution
  have h := norm_integral_le_integral_norm (μ := volume) (fun y : ℝ => f y * g (x - y))
  simpa only [norm_mul] using h

theorem normConvolution_nonneg (f g : ℝ → ℂ) (x : ℝ) :
    0 ≤ normConvolution f g x :=
  integral_nonneg (fun y => mul_nonneg (norm_nonneg _) (norm_nonneg _))

theorem integrable_convolution {f g : ℝ → ℂ} (hf : Integrable f) (hg : Integrable g) :
    Integrable (convolution f g) := by
  have h := hf.integrable_convolution (L := ContinuousLinearMap.mul ℝ ℂ) hg
  convert h using 1
  funext x
  rfl

theorem integrable_normConvolution {f g : ℝ → ℂ} (hf : Integrable f) (hg : Integrable g) :
    Integrable (normConvolution f g) := by
  have h := hf.norm.integrable_convolution (L := ContinuousLinearMap.mul ℝ ℝ) hg.norm
  convert h using 1
  funext x
  rfl

theorem integral_normConvolution {f g : ℝ → ℂ} (hf : Integrable f) (hg : Integrable g) :
    (∫ x : ℝ, normConvolution f g x) = (∫ x : ℝ, ‖f x‖) * (∫ x : ℝ, ‖g x‖) := by
  have h := integral_convolution (ContinuousLinearMap.mul ℝ ℝ) hf.norm hg.norm
  simpa only [MeasureTheory.convolution_mul, ContinuousLinearMap.mul_apply', normConvolution] using h

/-- Non-sharp Young for the full L¹(R) endpoint, complex-valued functions. -/
theorem young_L1_integral {f g : ℝ → ℂ} (hf : Integrable f) (hg : Integrable g) :
    (∫ x : ℝ, ‖convolution f g x‖) ≤ (∫ x : ℝ, ‖f x‖) * (∫ x : ℝ, ‖g x‖) := by
  calc
    _ ≤ ∫ x : ℝ, normConvolution f g x := integral_mono
      (integrable_convolution hf hg).norm (integrable_normConvolution hf hg)
      (fun x => norm_convolution_le f g x)
    _ = _ := integral_normConvolution hf hg

/-- The same endpoint in actual extended Lp seminorm notation. -/
theorem young_L1 {f g : ℝ → ℂ} (hf : MemLp f 1) (hg : MemLp g 1) :
    eLpNorm (convolution f g) 1 ≤ eLpNorm f 1 * eLpNorm g 1 := by
  have hfi : Integrable f := memLp_one_iff_integrable.mp hf
  have hgi : Integrable g := memLp_one_iff_integrable.mp hg
  have hci := integrable_convolution hfi hgi
  simp only [eLpNorm_one_eq_lintegral_enorm,
    ← ofReal_integral_norm_eq_lintegral_enorm hfi,
    ← ofReal_integral_norm_eq_lintegral_enorm hgi,
    ← ofReal_integral_norm_eq_lintegral_enorm hci]
  rw [← ENNReal.ofReal_mul (by positivity)]
  exact ENNReal.ofReal_le_ofReal (young_L1_integral hfi hgi)

/-- Domination reduces the general exponent problem to convolution of norms. -/
theorem eLpNorm_convolution_le_normConvolution (f g : ℝ → ℂ) (r : ℝ≥0∞) :
    eLpNorm (convolution f g) r ≤ eLpNorm (normConvolution f g) r := by
  apply eLpNorm_mono
  intro x
  rw [Real.norm_of_nonneg (normConvolution_nonneg f g x)]
  exact norm_convolution_le f g x

/-- The full M1 assertion. This definition asserts no theorem and contributes no axiom. -/
def YoungFinite : Prop :=
  ∀ p q r : ℝ, 1 ≤ p → 1 ≤ q → 1 ≤ r → 1 / p + 1 / q = 1 + 1 / r →
    ∀ f g : ℝ → ℂ, MemLp f (ENNReal.ofReal p) → MemLp g (ENNReal.ofReal q) →
      MemLp (convolution f g) (ENNReal.ofReal r) ∧
        eLpNorm (convolution f g) (ENNReal.ofReal r) ≤
          eLpNorm f (ENNReal.ofReal p) * eLpNorm g (ENNReal.ofReal q)

/-- Convolution is ae strongly measurable for arbitrary ae strongly
measurable factors; no L¹ or compact-support hypothesis is inserted. -/
theorem aestronglyMeasurable_convolution {f g : ℝ → ℂ}
    (hf : AEStronglyMeasurable f) (hg : AEStronglyMeasurable g) :
    AEStronglyMeasurable (convolution f g) := by
  have h := (hf.convolution_integrand (ContinuousLinearMap.mul ℝ ℂ) hg).integral_prod_right'
  simpa only [ContinuousLinearMap.mul_apply', convolution, Prod.fst, Prod.snd] using! h

/-- Hölder's conjugate-exponent boundary of Young, pointwise on all of R. -/
theorem young_conjugate_pointwise {p q : ℝ≥0∞} [ENNReal.HolderTriple p q 1]
    {f g : ℝ → ℂ} (hf : MemLp f p) (hg : MemLp g q) (x : ℝ) :
    ‖convolution f g x‖ₑ ≤ eLpNorm f p * eLpNorm g q := by
  have hmp : MeasurePreserving (fun y : ℝ => x - y) volume volume :=
    volume.measurePreserving_sub_left x
  have hgt : MemLp (g ∘ fun y : ℝ => x - y) q := hg.comp_measurePreserving hmp
  have hholder := eLpNorm_smul_le_mul_eLpNorm (p := p) (q := q) (r := 1)
    (φ := f) (f := g ∘ fun y : ℝ => x - y)
    hgt.aestronglyMeasurable hf.aestronglyMeasurable
  simp only [Pi.smul_apply, smul_eq_mul] at hholder
  rw [eLpNorm_comp_measurePreserving hg.aestronglyMeasurable hmp] at hholder
  have hInt : ‖convolution f g x‖ₑ ≤
      eLpNorm (fun y : ℝ => f y * g (x - y)) 1 volume := by
    unfold convolution
    rw [eLpNorm_one_eq_lintegral_enorm]
    exact enorm_integral_le_lintegral_enorm (μ := volume) (fun y : ℝ => f y * g (x - y))
  exact hInt.trans hholder

/-- Complete conjugate-exponent boundary `Lp * Lq -> L∞`, including
membership of the convolution in the actual function space. -/
theorem young_conjugate {p q : ℝ≥0∞} [ENNReal.HolderTriple p q 1]
    {f g : ℝ → ℂ} (hf : MemLp f p) (hg : MemLp g q) :
    MemLp (convolution f g) ∞ ∧ eLpNorm (convolution f g) ∞ ≤ eLpNorm f p * eLpNorm g q := by
  have hbound : eLpNorm (convolution f g) ∞ ≤ eLpNorm f p * eLpNorm g q := by
    rw [eLpNorm_exponent_top]
    exact eLpNormEssSup_le_of_ae_enorm_bound (Filter.Eventually.of_forall
      (young_conjugate_pointwise hf hg))
  refine ⟨⟨aestronglyMeasurable_convolution hf.aestronglyMeasurable hg.aestronglyMeasurable,
    hbound.trans_lt (ENNReal.mul_lt_top hf.eLpNorm_lt_top hg.eLpNorm_lt_top)⟩, hbound⟩

/-- Three-factor weighted Hölder in extended integrals. This is the
pointwise mechanism for the finite-exponent part of Young. -/
theorem lintegral_weighted_three {α : Type*} [MeasurableSpace α] (μ : Measure α)
    (f g h : α → ℝ≥0∞) (hf : AEMeasurable f μ) (hg : AEMeasurable g μ) (hh : AEMeasurable h μ)
    (a b c : ℝ) (ha : 0 < a) (hb : 0 < b) (hc : 0 < c) (hsum : a + b + c = 1) :
    (∫⁻ x, f x ^ a * g x ^ b * h x ^ c ∂μ) ≤
      (∫⁻ x, f x ∂μ) ^ a * (∫⁻ x, g x ∂μ) ^ b * (∫⁻ x, h x ∂μ) ^ c := by
  have ha1 : 0 < 1 - a := by linarith
  have hconj1 : (1 / a).HolderConjugate (1 / (1 - a)) := by
    apply Real.holderConjugate_iff.mpr
    constructor
    · simpa only [one_div] using (one_lt_inv₀ ha).mpr (by linarith : a < 1)
    · field_simp
      ring
  have hconj2 : ((1 - a) / b).HolderConjugate ((1 - a) / c) := by
    apply Real.holderConjugate_iff.mpr
    constructor
    · apply (lt_div_iff₀ hb).mpr
      linarith
    · field_simp
      nlinarith
  have eA : a * (1 / a) = 1 := by field_simp
  have eB : (b / (1 - a)) * ((1 - a) / b) = 1 := by field_simp
  have eC : (c / (1 - a)) * ((1 - a) / c) = 1 := by field_simp
  have eQ : 1 / (1 / a) = a := by simp
  have eR : 1 / (1 / (1 - a)) = 1 - a := by simp
  have eP2 : 1 / ((1 - a) / b) = b / (1 - a) := by field_simp
  have eQ2 : 1 / ((1 - a) / c) = c / (1 - a) := by field_simp
  have H2 := ENNReal.lintegral_mul_le_Lp_mul_Lq μ hconj2
    (hg.pow_const (b / (1 - a))) (hh.pow_const (c / (1 - a)))
  simp only [Pi.mul_apply, ← ENNReal.rpow_mul, eB, eC, ENNReal.rpow_one, eP2, eQ2] at H2
  have H1 := ENNReal.lintegral_mul_le_Lp_mul_Lq μ hconj1
    (hf.pow_const a) ((hg.pow_const b).mul (hh.pow_const c))
  have epb : b * (1 / (1 - a)) = b / (1 - a) := by ring
  have epc : c * (1 / (1 - a)) = c / (1 - a) := by ring
  simp only [Pi.mul_apply, ENNReal.mul_rpow_of_nonneg _ _ (by positivity : 0 ≤ 1 / (1 - a)),
    ← ENNReal.rpow_mul, eA, epb, epc, ENNReal.rpow_one, eQ, eR] at H1
  have H2pow := ENNReal.rpow_le_rpow H2 ha1.le
  have eb : (b / (1 - a)) * (1 - a) = b := by field_simp
  have ec : (c / (1 - a)) * (1 - a) = c := by field_simp
  simp only [ENNReal.mul_rpow_of_nonneg _ _ ha1.le, ← ENNReal.rpow_mul, eb, ec] at H2pow
  have H := H1.trans (mul_le_mul_right H2pow ((∫⁻ x, f x ∂μ) ^ a))
  simpa only [mul_assoc] using H

theorem lintegral_weighted_two {α : Type*} [MeasurableSpace α] (μ : Measure α)
    (f g : α → ℝ≥0∞) (hf : AEMeasurable f μ) (hg : AEMeasurable g μ)
    (a b : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b) (hsum : a + b = 1) :
    (∫⁻ x, f x ^ a * g x ^ b ∂μ) ≤ (∫⁻ x, f x ∂μ) ^ a * (∫⁻ x, g x ∂μ) ^ b := by
  by_cases ha0 : a = 0
  · have hb1 : b = 1 := by linarith
    simp [ha0, hb1]
  by_cases hb0 : b = 0
  · have ha1 : a = 1 := by linarith
    simp [hb0, ha1]
  have hap : 0 < a := lt_of_le_of_ne ha (Ne.symm ha0)
  have hbp : 0 < b := lt_of_le_of_ne hb (Ne.symm hb0)
  have hpq : (1 / a).HolderConjugate (1 / b) := by
    apply Real.holderConjugate_iff.mpr
    constructor
    · simpa only [one_div] using (one_lt_inv₀ hap).mpr (by linarith : a < 1)
    · simp only [one_div, inv_inv]
      exact hsum
  have ea : a * (1 / a) = 1 := by field_simp
  have eb : b * (1 / b) = 1 := by field_simp
  have H := ENNReal.lintegral_mul_le_Lp_mul_Lq μ hpq (hf.pow_const a) (hg.pow_const b)
  simpa only [Pi.mul_apply, ← ENNReal.rpow_mul, ea, eb, ENNReal.rpow_one, show 1 / (1 / a) = a by simp,
    show 1 / (1 / b) = b by simp] using H

theorem lintegral_weighted_three_nonneg {α : Type*} [MeasurableSpace α] (μ : Measure α)
    (f g h : α → ℝ≥0∞) (hf : AEMeasurable f μ) (hg : AEMeasurable g μ) (hh : AEMeasurable h μ)
    (a b c : ℝ) (ha : 0 < a) (hb : 0 ≤ b) (hc : 0 ≤ c) (hsum : a + b + c = 1) :
    (∫⁻ x, f x ^ a * g x ^ b * h x ^ c ∂μ) ≤
      (∫⁻ x, f x ∂μ) ^ a * (∫⁻ x, g x ∂μ) ^ b * (∫⁻ x, h x ∂μ) ^ c := by
  by_cases hb0 : b = 0
  · simpa only [hb0, ENNReal.rpow_zero, mul_one] using
      lintegral_weighted_two μ f h hf hh a c ha.le hc (by linarith)
  by_cases hc0 : c = 0
  · simpa only [hc0, ENNReal.rpow_zero, mul_one] using
      lintegral_weighted_two μ f g hf hg a b ha.le hb (by linarith)
  exact lintegral_weighted_three μ f g h hf hg hh a b c ha
    (lt_of_le_of_ne hb (Ne.symm hb0)) (lt_of_le_of_ne hc (Ne.symm hc0)) hsum

/-- Three-factor Hölder gives the pointwise finite-exponent Young bound.
The powers may be zero at the p=1 or q=1 endpoints. -/
theorem young_pointwise_power {α : Type*} [MeasurableSpace α] (μ : Measure α)
    (f g : α → ℝ≥0∞) (hf : AEMeasurable f μ) (hg : AEMeasurable g μ)
    (p q r : ℝ) (hp : 1 ≤ p) (hq : 1 ≤ q) (hr : 1 < r)
    (hexp : 1 / p + 1 / q = 1 + 1 / r) :
    (∫⁻ x, f x * g x ∂μ) ^ r ≤
      (∫⁻ x, f x ^ p * g x ^ q ∂μ) *
        (∫⁻ x, f x ^ p ∂μ) ^ ((1 - 1 / q) * r) *
        (∫⁻ x, g x ^ q ∂μ) ^ ((1 - 1 / p) * r) := by
  have hpp : 0 < p := by linarith
  have hqp : 0 < q := by linarith
  have hrp : 0 < r := by linarith
  have hA : 0 < 1 / r := by positivity
  have hB : 0 ≤ 1 - 1 / q := by
    have h := (div_le_one₀ hqp).mpr hq
    linarith
  have hC : 0 ≤ 1 - 1 / p := by
    have h := (div_le_one₀ hpp).mpr hp
    linarith
  have hsum : 1 / r + (1 - 1 / q) + (1 - 1 / p) = 1 := by linarith
  have eF : p * (1 / r) + p * (1 - 1 / q) = 1 := by
    field_simp [hpp.ne', hqp.ne', hrp.ne'] at hexp ⊢
    nlinarith [hexp]
  have eG : q * (1 / r) + q * (1 - 1 / p) = 1 := by
    field_simp [hpp.ne', hqp.ne', hrp.ne'] at hexp ⊢
    nlinarith [hexp]
  have H := lintegral_weighted_three_nonneg μ
    (fun x => f x ^ p * g x ^ q) (fun x => f x ^ p) (fun x => g x ^ q)
    ((hf.pow_const p).mul (hg.pow_const q)) (hf.pow_const p) (hg.pow_const q)
    (1 / r) (1 - 1 / q) (1 - 1 / p) hA hB hC hsum
  have hpoint : ∀ x, (f x ^ p * g x ^ q) ^ (1 / r) * (f x ^ p) ^ (1 - 1 / q) *
      (g x ^ q) ^ (1 - 1 / p) = f x * g x := by
    intro x
    rw [ENNReal.mul_rpow_of_nonneg _ _ hA.le]
    simp only [← ENNReal.rpow_mul]
    calc
      _ = (f x ^ (p * (1 / r)) * f x ^ (p * (1 - 1 / q))) *
          (g x ^ (q * (1 / r)) * g x ^ (q * (1 - 1 / p))) := by ring
      _ = f x * g x := by
        rw [← ENNReal.rpow_add_of_nonneg _ _ (mul_nonneg hpp.le hA.le) (mul_nonneg hpp.le hB),
          ← ENNReal.rpow_add_of_nonneg _ _ (mul_nonneg hqp.le hA.le) (mul_nonneg hqp.le hC),
          eF, eG, ENNReal.rpow_one, ENNReal.rpow_one]
  simp_rw [hpoint] at H
  have Hpow := ENNReal.rpow_le_rpow H hrp.le
  have ear : (1 / r) * r = 1 := by field_simp
  simpa only [ENNReal.mul_rpow_of_nonneg _ _ hrp.le, ← ENNReal.rpow_mul,
    ear, ENNReal.rpow_one] using Hpow


/-- Tonelli and translation invariance for a nonnegative convolution. -/
theorem lintegral_convolution_ennreal (f g : ℝ → ℝ≥0∞)
    (hf : AEMeasurable f) (hg : AEMeasurable g) :
    (∫⁻ x : ℝ, ∫⁻ y : ℝ, f y * g (x - y)) = (∫⁻ y : ℝ, f y) * ∫⁻ y : ℝ, g y := by
  have hsub : AEMeasurable (fun z : ℝ × ℝ => g (z.1 - z.2)) (volume.prod volume) :=
    hg.comp_quasiMeasurePreserving (quasiMeasurePreserving_sub_of_right_invariant volume volume)
  have hprod : AEMeasurable (fun z : ℝ × ℝ => f z.2 * g (z.1 - z.2))
      (volume.prod volume) := hf.comp_snd.mul hsub
  rw [lintegral_lintegral_swap hprod]
  have hinner : ∀ y : ℝ, (∫⁻ x : ℝ, f y * g (x - y)) = f y * ∫⁻ x : ℝ, g x := by
    intro y
    have hgy : AEMeasurable (fun x : ℝ => g (x - y)) := by
      simpa only [Function.comp_def] using hg.comp_quasiMeasurePreserving
        (measurePreserving_sub_right volume y).quasiMeasurePreserving
    rw [lintegral_const_mul'' _ hgy]
    rw [lintegral_sub_right_eq_self]
  simp_rw [hinner]
  exact lintegral_mul_const'' _ hf

/-- The complete powered integral estimate underlying finite-exponent Young. -/
theorem young_lintegral_power (f g : ℝ → ℝ≥0∞)
    (hf : AEMeasurable f) (hg : AEMeasurable g)
    (p q r : ℝ) (hp : 1 ≤ p) (hq : 1 ≤ q) (hr : 1 < r)
    (hexp : 1 / p + 1 / q = 1 + 1 / r) :
    (∫⁻ x : ℝ, (∫⁻ y : ℝ, f y * g (x - y)) ^ r) ≤
      (∫⁻ y : ℝ, f y ^ p) ^ (r / p) * (∫⁻ y : ℝ, g y ^ q) ^ (r / q) := by
  have hpp : 0 < p := by linarith
  have hqp : 0 < q := by linarith
  have hrp : 0 < r := by linarith
  have hB : 0 ≤ (1 - 1 / q) * r := mul_nonneg
    (sub_nonneg.mpr ((div_le_one₀ hqp).mpr hq)) hrp.le
  have hC : 0 ≤ (1 - 1 / p) * r := mul_nonneg
    (sub_nonneg.mpr ((div_le_one₀ hpp).mpr hp)) hrp.le
  have hcross : AEMeasurable (fun x : ℝ => ∫⁻ y : ℝ, f y ^ p * g (x - y) ^ q) := by
    have hsub := (hg.pow_const q).comp_quasiMeasurePreserving
      (quasiMeasurePreserving_sub_of_right_invariant volume volume)
    exact ((hf.pow_const p).comp_snd.mul hsub).lintegral_prod_right'
  have hpoint : ∀ x : ℝ, (∫⁻ y : ℝ, f y * g (x - y)) ^ r ≤
      (∫⁻ y : ℝ, f y ^ p * g (x - y) ^ q) *
        (∫⁻ y : ℝ, f y ^ p) ^ ((1 - 1 / q) * r) *
        (∫⁻ y : ℝ, g y ^ q) ^ ((1 - 1 / p) * r) := by
    intro x
    have H := young_pointwise_power volume f (fun y : ℝ => g (x - y)) hf
      (hg.comp_quasiMeasurePreserving (volume.measurePreserving_sub_left x).quasiMeasurePreserving) p q r hp hq hr hexp
    rw [show (∫⁻ y : ℝ, g (x - y) ^ q) = ∫⁻ y : ℝ, g y ^ q from
      lintegral_sub_left_eq_self (fun y => g y ^ q) x] at H
    exact H
  have H := lintegral_mono (μ := volume) hpoint
  rw [lintegral_mul_const'' _ (hcross.mul_const _), lintegral_mul_const'' _ hcross,
    lintegral_convolution_ennreal (fun y => f y ^ p) (fun y => g y ^ q)
      (hf.pow_const p) (hg.pow_const q)] at H
  have eF : 1 + (1 - 1 / q) * r = r / p := by
    field_simp [hpp.ne', hqp.ne', hrp.ne'] at hexp ⊢
    nlinarith [hexp]
  have eG : 1 + (1 - 1 / p) * r = r / q := by
    field_simp [hpp.ne', hqp.ne', hrp.ne'] at hexp ⊢
    nlinarith [hexp]
  calc
    _ ≤ ((∫⁻ y : ℝ, f y ^ p) * (∫⁻ y : ℝ, g y ^ q)) *
        (∫⁻ y : ℝ, f y ^ p) ^ ((1 - 1 / q) * r) *
        (∫⁻ y : ℝ, g y ^ q) ^ ((1 - 1 / p) * r) := H
    _ = ((∫⁻ y : ℝ, f y ^ p) ^ (1 : ℝ) * (∫⁻ y : ℝ, f y ^ p) ^ ((1 - 1 / q) * r)) *
        ((∫⁻ y : ℝ, g y ^ q) ^ (1 : ℝ) * (∫⁻ y : ℝ, g y ^ q) ^ ((1 - 1 / p) * r)) := by
      simp only [ENNReal.rpow_one]
      <;> ring
    _ = _ := by
      have hF := ENNReal.rpow_add_of_nonneg (x := ∫⁻ y : ℝ, f y ^ p)
        1 ((1 - 1 / q) * r) (by norm_num) hB
      have hG := ENNReal.rpow_add_of_nonneg (x := ∫⁻ y : ℝ, g y ^ q)
        1 ((1 - 1 / p) * r) (by norm_num) hC
      rw [eF] at hF
      rw [eG] at hG
      rw [← hF, ← hG]


/-- Non-sharp Young for every finite exponent with r>1, for arbitrary
complex Lp functions on the real line. -/
theorem young_finite_gt_one {p q r : ℝ} (hp : 1 ≤ p) (hq : 1 ≤ q) (hr : 1 < r)
    (hexp : 1 / p + 1 / q = 1 + 1 / r) {f g : ℝ → ℂ}
    (hf : MemLp f (ENNReal.ofReal p)) (hg : MemLp g (ENNReal.ofReal q)) :
    MemLp (convolution f g) (ENNReal.ofReal r) ∧
      eLpNorm (convolution f g) (ENNReal.ofReal r) ≤
        eLpNorm f (ENNReal.ofReal p) * eLpNorm g (ENNReal.ofReal q) := by
  have hpp : 0 < p := by linarith
  have hqp : 0 < q := by linarith
  have hrp : 0 < r := by linarith
  have hnorm : ∀ x : ℝ, ‖convolution f g x‖ₑ ≤
      ∫⁻ y : ℝ, ‖f y‖ₑ * ‖g (x - y)‖ₑ := by
    intro x
    have H := enorm_integral_le_lintegral_enorm (μ := volume)
      (fun y : ℝ => f y * g (x - y))
    simpa only [convolution, enorm_mul] using H
  have H := young_lintegral_power (fun x => ‖f x‖ₑ) (fun x => ‖g x‖ₑ)
    hf.aestronglyMeasurable.enorm hg.aestronglyMeasurable.enorm p q r hp hq hr hexp
  have Hint : (∫⁻ x : ℝ, ‖convolution f g x‖ₑ ^ r) ≤
      (∫⁻ y : ℝ, ‖f y‖ₑ ^ p) ^ (r / p) * (∫⁻ y : ℝ, ‖g y‖ₑ ^ q) ^ (r / q) :=
    (lintegral_mono (fun x => ENNReal.rpow_le_rpow (hnorm x) hrp.le)).trans H
  have Hroot := ENNReal.rpow_le_rpow Hint (by positivity : 0 ≤ 1 / r)
  have ep : (r / p) * (1 / r) = 1 / p := by field_simp
  have eq : (r / q) * (1 / r) = 1 / q := by field_simp
  have hbound : eLpNorm (convolution f g) (ENNReal.ofReal r) ≤
      eLpNorm f (ENNReal.ofReal p) * eLpNorm g (ENNReal.ofReal q) := by
    simp only [eLpNorm_eq_lintegral_rpow_enorm_toReal (ENNReal.ofReal_ne_zero_iff.mpr hrp)
        ENNReal.ofReal_ne_top,
      eLpNorm_eq_lintegral_rpow_enorm_toReal (ENNReal.ofReal_ne_zero_iff.mpr hpp)
        ENNReal.ofReal_ne_top,
      eLpNorm_eq_lintegral_rpow_enorm_toReal (ENNReal.ofReal_ne_zero_iff.mpr hqp)
        ENNReal.ofReal_ne_top,
      ENNReal.toReal_ofReal hrp.le, ENNReal.toReal_ofReal hpp.le, ENNReal.toReal_ofReal hqp.le]
    simpa only [ENNReal.mul_rpow_of_nonneg _ _ (by positivity : 0 ≤ 1 / r),
      ← ENNReal.rpow_mul, ep, eq] using Hroot
  exact ⟨⟨aestronglyMeasurable_convolution hf.aestronglyMeasurable hg.aestronglyMeasurable,
    hbound.trans_lt (ENNReal.mul_lt_top hf.eLpNorm_lt_top hg.eLpNorm_lt_top)⟩, hbound⟩

/-- M1: non-sharp Young, constant one, for every finite admissible triple.
No support, boundedness, or nonnegativity restrictions are imposed. -/
theorem young_finite : YoungFinite := by
  intro p q r hp hq hr hexp f g hf hg
  by_cases hr1 : r = 1
  · have hp0 : 0 < p := by linarith
    have hq0 : 0 < q := by linarith
    have hpinv : 1 / p ≤ 1 := (div_le_one₀ hp0).mpr hp
    have hqinv : 1 / q ≤ 1 := (div_le_one₀ hq0).mpr hq
    have hp1 : p = 1 := by
      have hi : 1 / p = 1 := by simp only [hr1, div_one] at hexp; linarith
      exact (div_eq_one_iff_eq hp0.ne').mp hi |>.symm
    have hq1 : q = 1 := by
      have hi : 1 / q = 1 := by simp only [hr1, div_one] at hexp; linarith
      exact (div_eq_one_iff_eq hq0.ne').mp hi |>.symm
    subst p; subst q; subst r
    simp only [ENNReal.ofReal_one] at hf hg ⊢
    exact ⟨memLp_one_iff_integrable.mpr (integrable_convolution
      (memLp_one_iff_integrable.mp hf) (memLp_one_iff_integrable.mp hg)), young_L1 hf hg⟩
  · exact young_finite_gt_one hp hq (lt_of_le_of_ne hr (Ne.symm hr1)) hexp hf hg

end ChowlaCosine.Beckner
