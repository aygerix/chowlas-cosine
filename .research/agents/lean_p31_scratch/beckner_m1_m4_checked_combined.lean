-- SOURCE ChowlaCosine/Beckner/Young.lean
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

-- SOURCE ChowlaCosine/Beckner/YoungSpecial.lean

/-!
# The project exponent triple for non-sharp Young

This is the constant-one specialization of M1. It is not Beckner's
sharp constant; no shortcut to that constant is asserted here.
-/

open MeasureTheory
open scoped ENNReal NNReal

namespace ChowlaCosine.Beckner

/-- Young at the project exponents, with the M1 constant one. -/
theorem young_four_thirds {f g : ℝ → ℂ}
    (hf : MemLp f (ENNReal.ofReal (4 / 3 : ℝ)))
    (hg : MemLp g (ENNReal.ofReal (4 / 3 : ℝ))) :
    MemLp (convolution f g) 2 ∧
      eLpNorm (convolution f g) 2 ≤
        eLpNorm f (ENNReal.ofReal (4 / 3 : ℝ)) *
          eLpNorm g (ENNReal.ofReal (4 / 3 : ℝ)) := by
  have H := young_finite (4 / 3) (4 / 3) 2 (by norm_num) (by norm_num)
    (by norm_num) (by norm_num) f g hf hg
  simpa only [ENNReal.ofReal_ofNat] using H

end ChowlaCosine.Beckner

-- SOURCE ChowlaCosine/Beckner/Gaussian.lean

/-!
# Gaussian norm and convolution computations for sharp Young

The parameter `a` in `gaussian a x` is the positive quadratic coefficient:
`exp (-a*x²)`. Integrals use Lebesgue measure on the actual real line.
-/

open MeasureTheory Real
open scoped ENNReal NNReal

namespace ChowlaCosine.Beckner

set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

noncomputable def gaussian (a x : ℝ) : ℝ := Real.exp (-a * x ^ 2)
noncomputable def complexGaussian (a x : ℝ) : ℂ := (gaussian a x : ℂ)

@[simp] theorem gaussian_pos (a x : ℝ) : 0 < gaussian a x := Real.exp_pos _

@[simp] theorem norm_complexGaussian (a x : ℝ) : ‖complexGaussian a x‖ = gaussian a x := by
  simp only [complexGaussian, Complex.norm_real, Real.norm_of_nonneg (gaussian_pos a x).le]

theorem gaussian_rpow (a x p : ℝ) : gaussian a x ^ p = gaussian (p * a) x := by
  unfold gaussian
  rw [← Real.exp_mul]
  congr 1
  ring

theorem integrable_gaussian {a : ℝ} (ha : 0 < a) : Integrable (gaussian a) :=
  integrable_exp_neg_mul_sq ha

theorem integral_gaussian_exact (a : ℝ) : (∫ x : ℝ, gaussian a x) = Real.sqrt (Real.pi / a) :=
  integral_gaussian a

/-- Exact finite-p Gaussian moment, for arbitrary positive p. -/
theorem integral_gaussian_rpow (a p : ℝ) :
    (∫ x : ℝ, gaussian a x ^ p) = Real.sqrt (Real.pi / (p * a)) := by
  simp_rw [gaussian_rpow]
  exact integral_gaussian_exact _

/-- Pointwise completion of the square; no sampled-angle surrogate. -/
theorem gaussian_mul_completed_square {a b : ℝ} (hab : a + b ≠ 0) (x y : ℝ) :
    gaussian a y * gaussian b (x - y) =
      gaussian (a * b / (a + b)) x * gaussian (a + b) (y - b * x / (a + b)) := by
  unfold gaussian
  rw [← Real.exp_add, ← Real.exp_add]
  congr 1
  field_simp
  <;> ring

/-- Closed convolution formula for two arbitrary positive Gaussian widths. -/
theorem gaussian_convolution {a b : ℝ} (ha : 0 < a) (hb : 0 < b) (x : ℝ) :
    (∫ y : ℝ, gaussian a y * gaussian b (x - y)) =
      Real.sqrt (Real.pi / (a + b)) * gaussian (a * b / (a + b)) x := by
  have hab : 0 < a + b := add_pos ha hb
  simp_rw [gaussian_mul_completed_square hab.ne' x]
  rw [integral_const_mul, integral_sub_right_eq_self, integral_gaussian_exact]
  ring


/-- Gaussian finite-p norm in closed form, in the actual eLpNorm notation. -/
theorem eLpNorm_complexGaussian {a p : ℝ} (ha : 0 < a) (hp : 0 < p) :
    eLpNorm (complexGaussian a) (ENNReal.ofReal p) =
      ENNReal.ofReal (Real.sqrt (Real.pi / (p * a))) ^ (1 / p) := by
  rw [eLpNorm_eq_lintegral_rpow_enorm_toReal (ENNReal.ofReal_ne_zero_iff.mpr hp)
    ENNReal.ofReal_ne_top, ENNReal.toReal_ofReal hp.le]
  simp_rw [← ofReal_norm, norm_complexGaussian,
    ENNReal.ofReal_rpow_of_pos (gaussian_pos _ _), gaussian_rpow]
  rw [← ofReal_integral_eq_lintegral_ofReal (integrable_gaussian (mul_pos hp ha))
    (Filter.Eventually.of_forall (fun x => (gaussian_pos (p * a) x).le)),
    integral_gaussian_exact]

/-- All positive finite Gaussian norms are finite; not only integer moments. -/
theorem memLp_complexGaussian {a p : ℝ} (ha : 0 < a) (hp : 0 < p) :
    MemLp (complexGaussian a) (ENNReal.ofReal p) := by
  refine ⟨?_, ?_⟩
  · have hc : Continuous (complexGaussian a) := by
      unfold complexGaussian gaussian
      fun_prop
    exact hc.aestronglyMeasurable
  · rw [eLpNorm_complexGaussian ha hp]
    exact ENNReal.rpow_lt_top_of_nonneg (by positivity) ENNReal.ofReal_ne_top

/-- The Gaussian convolution formula also holds for the complex convolution
used throughout Young's inequality. -/
theorem complexGaussian_convolution {a b : ℝ} (ha : 0 < a) (hb : 0 < b) (x : ℝ) :
    convolution (complexGaussian a) (complexGaussian b) x =
      (Real.sqrt (Real.pi / (a + b)) : ℂ) * complexGaussian (a * b / (a + b)) x := by
  unfold convolution complexGaussian
  simp_rw [← Complex.ofReal_mul]
  rw [integral_complex_ofReal, gaussian_convolution ha hb]


/-- Exact finite-r norm of convolution of positive-width Gaussians. -/
theorem eLpNorm_complexGaussian_convolution {a b r : ℝ}
    (ha : 0 < a) (hb : 0 < b) (hr : 0 < r) :
    eLpNorm (convolution (complexGaussian a) (complexGaussian b)) (ENNReal.ofReal r) =
      ENNReal.ofReal (Real.sqrt (Real.pi / (a + b))) *
        ENNReal.ofReal (Real.sqrt (Real.pi / (r * (a * b / (a + b))))) ^ (1 / r) := by
  have hfun : convolution (complexGaussian a) (complexGaussian b) =
      (Real.sqrt (Real.pi / (a + b)) : ℂ) • complexGaussian (a * b / (a + b)) := by
    funext x
    exact complexGaussian_convolution ha hb x
  rw [hfun, eLpNorm_const_smul, ← ofReal_norm, Complex.norm_real,
    Real.norm_of_nonneg (Real.sqrt_nonneg _),
    eLpNorm_complexGaussian (div_pos (mul_pos ha hb) (add_pos ha hb)) hr]

noncomputable def sharpBeta : ℝ := 4 / (3 * Real.sqrt 3)

theorem sharpBeta_pos : 0 < sharpBeta := by unfold sharpBeta; positivity

/-- The exact sharp factor, not its rounded decimal, is attained by a
Gaussian at the project exponents. This is a lower bound on any proposed
universal constant; it does not prove the sharp upper inequality. -/
theorem gaussian_attains_project_constant :
    eLpNorm (convolution (complexGaussian 1) (complexGaussian 1)) 2 ^ 2 =
      ENNReal.ofReal sharpBeta *
        eLpNorm (complexGaussian 1) (ENNReal.ofReal (4 / 3 : ℝ)) ^ 4 := by
  have hn := eLpNorm_complexGaussian_convolution (a := 1) (b := 1) (r := 2)
    (by norm_num) (by norm_num) (by norm_num)
  norm_num at hn
  rw [hn, eLpNorm_complexGaussian (a := 1) (by norm_num) (by norm_num)]
  rw [mul_pow]
  have e2 : (ENNReal.ofReal (Real.sqrt Real.pi) ^ (1 / 2 : ℝ)) ^ 2 =
      ENNReal.ofReal (Real.sqrt Real.pi) := by
    rw [← ENNReal.rpow_natCast, ← ENNReal.rpow_mul]
    norm_num
  have e4 : (ENNReal.ofReal (Real.sqrt (Real.pi / (4 / 3 : ℝ))) ^ (1 / (4 / 3) : ℝ)) ^ 4 =
      ENNReal.ofReal (Real.sqrt (Real.pi / (4 / 3 : ℝ))) ^ 3 := by
    rw [← ENNReal.rpow_natCast, ← ENNReal.rpow_mul]
    norm_num
  norm_num only [one_mul, mul_one] at *
  rw [e2, e4]
  rw [← ENNReal.ofReal_pow (by positivity : 0 ≤ Real.sqrt Real.pi / Real.sqrt 2),
    ← ENNReal.ofReal_pow (Real.sqrt_nonneg (Real.pi / (4 / 3 : ℝ))),
    ← ENNReal.ofReal_mul (by positivity : 0 ≤ (Real.sqrt Real.pi / Real.sqrt 2) ^ 2),
    ← ENNReal.ofReal_mul sharpBeta_pos.le]
  congr 1
  have hs : Real.sqrt (Real.pi / (4 / 3 : ℝ)) = Real.sqrt 3 * Real.sqrt Real.pi / 2 := by
    have ee : Real.pi / (4 / 3 : ℝ) = 3 * Real.pi / 4 := by ring
    rw [ee, Real.sqrt_div (by positivity), Real.sqrt_mul (by positivity)]
    norm_num
  rw [div_pow, Real.sq_sqrt Real.pi_pos.le,
    Real.sq_sqrt (by norm_num : (0 : ℝ) ≤ 2), hs]
  unfold sharpBeta
  have h3 : Real.sqrt 3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)
  have hpi : Real.sqrt Real.pi ^ 2 = Real.pi := Real.sq_sqrt Real.pi_pos.le
  have h3p : Real.sqrt 3 ≠ 0 := (Real.sqrt_pos.mpr (by norm_num)).ne'
  field_simp
  nlinarith [h3, hpi]


/-- Every universal squared project-exponent constant is at least beta.
This is sharpness from a concrete Gaussian, independent of the unproved
sharp upper inequality. -/
theorem project_constant_lower_bound (C : ℝ≥0∞)
    (hC : ∀ f : ℝ → ℂ, MemLp f (ENNReal.ofReal (4 / 3 : ℝ)) volume →
      eLpNorm (convolution f f) 2 volume ^ 2 ≤
        C * eLpNorm f (ENNReal.ofReal (4 / 3 : ℝ)) volume ^ 4) :
    ENNReal.ofReal sharpBeta ≤ C := by
  have hm : MemLp (complexGaussian 1) (ENNReal.ofReal (4 / 3 : ℝ)) volume :=
    memLp_complexGaussian (a := 1) (p := 4 / 3) (by norm_num) (by norm_num)
  have H : ENNReal.ofReal sharpBeta *
      eLpNorm (complexGaussian 1) (ENNReal.ofReal (4 / 3 : ℝ)) volume ^ 4 ≤
      C * eLpNorm (complexGaussian 1) (ENNReal.ofReal (4 / 3 : ℝ)) volume ^ 4 := by
    rw [← gaussian_attains_project_constant]
    exact hC (complexGaussian 1) hm
  have h0 : eLpNorm (complexGaussian 1) (ENNReal.ofReal (4 / 3 : ℝ)) volume ^ 4 ≠ 0 := by
    rw [eLpNorm_complexGaussian (a := 1) (p := 4 / 3) (by norm_num) (by norm_num)]
    positivity
  have ht : eLpNorm (complexGaussian 1) (ENNReal.ofReal (4 / 3 : ℝ)) volume ^ 4 ≠ ∞ :=
    (ENNReal.pow_lt_top hm.eLpNorm_lt_top).ne
  exact (ENNReal.mul_le_mul_iff_left h0 ht).mp H

end ChowlaCosine.Beckner

-- SOURCE ChowlaCosine/Beckner/HeatFlow.lean

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

-- SOURCE ChowlaCosine/Beckner/HeatFlowDerivative.lean

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

-- SOURCE ChowlaCosine/Beckner/HeatFlowRelative.lean

/-!
# Relative heat-flow derivative bounds

Interval support is an explicit hypothesis in these auxiliary estimates.
It is not a restriction on the M1 theorem or a claimed sharp-Young result.
-/

open MeasureTheory Real
open scoped ENNReal NNReal Topology

namespace ChowlaCosine.Beckner
set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

/-- Integrating a pointwise envelope for a signed real integrand. -/
theorem abs_integral_le_scaled_integral {α : Type*} [MeasurableSpace α] (μ : Measure α)
    {F G : α → ℝ} (hF : Integrable F μ) (hG : Integrable G μ) (C : ℝ)
    (hbound : ∀ y, |G y| ≤ C * F y) :
    |∫ y, G y ∂μ| ≤ C * ∫ y, F y ∂μ := by
  calc
    _ ≤ ∫ y, |G y| ∂μ := norm_integral_le_integral_norm G
    _ ≤ ∫ y, C * F y ∂μ := integral_mono hG.norm (hF.const_mul C) hbound
    _ = _ := integral_const_mul _ _

theorem integrable_heatSpaceSlope_integrand {f : ℝ → ℝ} (hf : Integrable f)
    {t : ℝ} (ht : 0 < t) (x : ℝ) : Integrable (fun y => f y * heatSpaceSlope t (x - y)) := by
  have hc : Continuous (fun y : ℝ => heatSpaceSlope t (x - y)) := by
    unfold heatSpaceSlope
    exact (by fun_prop : Continuous (fun y : ℝ => -(x - y) / (2 * t))).mul
      ((continuous_heatKernel t).comp (continuous_const.sub continuous_id))
  exact hf.mul_bdd hc.aestronglyMeasurable
    (Filter.Eventually.of_forall (fun y => heatKernel_space_slope_bound ht _))

theorem integrable_heatTimeSlope_integrand {f : ℝ → ℝ} (hf : Integrable f)
    {t : ℝ} (ht : 0 < t) (x : ℝ) : Integrable (fun y => f y * heatTimeSlope t (x - y)) := by
  have hc : Continuous (fun y : ℝ => heatTimeSlope t (x - y)) := by
    unfold heatTimeSlope
    exact (by fun_prop : Continuous (fun y : ℝ => (x - y) ^ 2 / (4 * t ^ 2) - 1 / (2 * t))).mul
      ((continuous_heatKernel t).comp (continuous_const.sub continuous_id))
  exact hf.mul_bdd hc.aestronglyMeasurable
    (Filter.Eventually.of_forall (fun y => heatKernel_time_slope_bound ht _))

/-- Relative first-derivative envelope before dividing by the positive flow. -/
theorem heatFlow_space_moment_bound {f : ℝ → ℝ} (hf : Integrable f)
    (hn : ∀ y, 0 ≤ f y) (R : ℝ) (hR : 0 ≤ R)
    (hsupport : ∀ y, f y ≠ 0 → |y| ≤ R) {t : ℝ} (ht : 0 < t) (x : ℝ) :
    |∫ y : ℝ, f y * heatSpaceSlope t (x - y)| ≤
      ((|x| + R) / (2 * t)) * heatFlow f t x := by
  apply abs_integral_le_scaled_integral volume
    (integrable_heatFlow_integrand hf ht x) (integrable_heatSpaceSlope_integrand hf ht x)
  intro y
  by_cases hy : f y = 0
  · simp [hy]
  have hyR := hsupport y hy
  have hxy : |x - y| ≤ |x| + R := (abs_sub x y).trans (by linarith)
  have hfy : 0 ≤ f y := hn y
  have hKy : 0 ≤ heatKernel t (x - y) := (heatKernel_pos ht _).le
  unfold heatSpaceSlope
  rw [abs_mul, abs_of_nonneg (hn y), abs_mul, abs_of_nonneg (heatKernel_pos ht _).le,
    abs_div, abs_neg, abs_of_pos (by positivity : 0 < 2 * t)]
  calc
    _ ≤ f y * (((|x| + R) / (2 * t)) * heatKernel t (x - y)) := by gcongr
    _ = _ := by ring

/-- Relative second/time-derivative envelope before division. -/
theorem heatFlow_time_moment_bound {f : ℝ → ℝ} (hf : Integrable f)
    (hn : ∀ y, 0 ≤ f y) (R : ℝ) (hR : 0 ≤ R)
    (hsupport : ∀ y, f y ≠ 0 → |y| ≤ R) {t : ℝ} (ht : 0 < t) (x : ℝ) :
    |∫ y : ℝ, f y * heatTimeSlope t (x - y)| ≤
      (((|x| + R) ^ 2 / (4 * t ^ 2) + 1 / (2 * t))) * heatFlow f t x := by
  apply abs_integral_le_scaled_integral volume
    (integrable_heatFlow_integrand hf ht x) (integrable_heatTimeSlope_integrand hf ht x)
  intro y
  by_cases hy : f y = 0
  · simp [hy]
  have hxy : |x - y| ≤ |x| + R := (abs_sub x y).trans (by linarith [hsupport y hy])
  have hsq : (x - y) ^ 2 ≤ (|x| + R) ^ 2 := by
    simpa only [sq_abs] using (sq_le_sq₀ (abs_nonneg (x - y)) (by positivity)).mpr hxy
  have hA : (x - y) ^ 2 / (4 * t ^ 2) ≤ (|x| + R) ^ 2 / (4 * t ^ 2) := by gcongr
  have hcoef : |(x - y) ^ 2 / (4 * t ^ 2) - 1 / (2 * t)| ≤
      (|x| + R) ^ 2 / (4 * t ^ 2) + 1 / (2 * t) := by
    apply abs_le.mpr
    constructor <;> nlinarith [show 0 ≤ (x - y) ^ 2 / (4 * t ^ 2) by positivity,
      show 0 ≤ (|x| + R) ^ 2 / (4 * t ^ 2) by positivity,
      show 0 ≤ 1 / (2 * t) by positivity]
  have hfy : 0 ≤ f y := hn y
  have hKy : 0 ≤ heatKernel t (x - y) := (heatKernel_pos ht _).le
  unfold heatTimeSlope
  rw [abs_mul, abs_of_nonneg (hn y), abs_mul, abs_of_nonneg (heatKernel_pos ht _).le]
  calc
    _ ≤ f y * ((((|x| + R) ^ 2 / (4 * t ^ 2) + 1 / (2 * t))) * heatKernel t (x - y)) := by gcongr
    _ = _ := by ring

/-- Uniform polynomial envelope for the spatial logarithmic derivative. -/
theorem heatFlow_space_score_bound {f : ℝ → ℝ} (hf : Integrable f)
    (hn : ∀ y, 0 ≤ f y) (hm : 0 < ∫ y : ℝ, f y) (R : ℝ) (hR : 0 ≤ R)
    (hsupport : ∀ y, f y ≠ 0 → |y| ≤ R) {t : ℝ} (ht : 0 < t) (x : ℝ) :
    |(∫ y : ℝ, f y * heatSpaceSlope t (x - y)) / heatFlow f t x| ≤ (|x| + R) / (2 * t) := by
  rw [abs_div, abs_of_pos (heatFlow_pos hf hn hm ht x)]
  exact (div_le_iff₀ (heatFlow_pos hf hn hm ht x)).mpr
    (heatFlow_space_moment_bound hf hn R hR hsupport ht x)

/-- Uniform polynomial envelope for the relative time/second derivative. -/
theorem heatFlow_time_score_bound {f : ℝ → ℝ} (hf : Integrable f)
    (hn : ∀ y, 0 ≤ f y) (hm : 0 < ∫ y : ℝ, f y) (R : ℝ) (hR : 0 ≤ R)
    (hsupport : ∀ y, f y ≠ 0 → |y| ≤ R) {t : ℝ} (ht : 0 < t) (x : ℝ) :
    |(∫ y : ℝ, f y * heatTimeSlope t (x - y)) / heatFlow f t x| ≤
      (|x| + R) ^ 2 / (4 * t ^ 2) + 1 / (2 * t) := by
  rw [abs_div, abs_of_pos (heatFlow_pos hf hn hm ht x)]
  exact (div_le_iff₀ (heatFlow_pos hf hn hm ht x)).mpr
    (heatFlow_time_moment_bound hf hn R hR hsupport ht x)

end ChowlaCosine.Beckner


/-!
# Differentiating positive weighted products

The finite product is differentiated on a genuine real neighborhood;
positivity only at the base point suffices by continuity and finiteness.
-/

open MeasureTheory Real
open scoped Topology

namespace ChowlaCosine.Beckner
set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

section
variable {ι : Type*} [Fintype ι]

/-- Logarithmic form of a finite positive weighted product. -/
theorem weighted_product_eq_exp (c : ι → ℝ) (F : ι → ℝ) (hF : ∀ i, 0 < F i) :
    (∏ i, F i ^ c i) = Real.exp (∑ i, c i * Real.log (F i)) := by
  rw [Real.exp_sum]
  apply Finset.prod_congr rfl
  intro i _
  rw [Real.rpow_def_of_pos (hF i)]
  congr 1
  ring

/-- Exact first derivative of any finite positive weighted product. -/
theorem hasDerivAt_weighted_product (c : ι → ℝ) (F : ι → ℝ → ℝ) (d : ι → ℝ) (x : ℝ)
    (hF : ∀ i, 0 < F i x) (hd : ∀ i, HasDerivAt (F i) (d i) x) :
    HasDerivAt (fun t => ∏ i, F i t ^ c i)
      ((∏ i, F i x ^ c i) * (∑ i, c i * d i / F i x)) x := by
  have hlog : HasDerivAt (fun t => ∑ i, c i * Real.log (F i t))
      (∑ i, c i * (d i / F i x)) x :=
    HasDerivAt.fun_sum (fun i _ => ((hd i).log (hF i).ne').const_mul (c i))
  have hpos : ∀ᶠ t in 𝓝 x, ∀ i, 0 < F i t := by
    apply Filter.eventually_all.mpr
    intro i
    exact (hd i).continuousAt.eventually (Ioi_mem_nhds (hF i))
  have heq : (fun t => ∏ i, F i t ^ c i) =ᶠ[𝓝 x]
      (fun t => Real.exp (∑ i, c i * Real.log (F i t))) := by
    filter_upwards [hpos] with t ht
    exact weighted_product_eq_exp c (fun i => F i t) ht
  have H := hlog.exp.congr_of_eventuallyEq heq
  rw [← weighted_product_eq_exp c (fun i => F i x) hF] at H
  simpa only [mul_div_assoc] using! H

/-- Exact derivative of the logarithmic product slope. In applications G
and K are the first and second derivatives of the factors. -/
theorem hasDerivAt_weighted_product_slope (c : ι → ℝ)
    (F G : ι → ℝ → ℝ) (K : ι → ℝ) (x : ℝ)
    (hF : ∀ i, 0 < F i x) (hd : ∀ i, HasDerivAt (F i) (G i x) x)
    (hG : ∀ i, HasDerivAt (G i) (K i) x) :
    HasDerivAt (fun t => (∏ i, F i t ^ c i) * (∑ i, c i * (G i t / F i t)))
      ((∏ i, F i x ^ c i) * ((∑ i, c i * (G i x / F i x)) ^ 2 +
        ∑ i, c i * (K i / F i x - (G i x / F i x) ^ 2))) x := by
  have hP : HasDerivAt (fun t => ∏ i, F i t ^ c i)
      ((∏ i, F i x ^ c i) * (∑ i, c i * (G i x / F i x))) x := by
    simpa only [mul_div_assoc] using! hasDerivAt_weighted_product c F (fun i => G i x) x hF hd
  have he : ∀ i, (K i * F i x - G i x * G i x) / (F i x) ^ 2 =
      K i / F i x - (G i x / F i x) ^ 2 := by
    intro i
    field_simp
    <;> ring
  have hQ : HasDerivAt (fun t => ∑ i, c i * (G i t / F i t))
      (∑ i, c i * (K i / F i x - (G i x / F i x) ^ 2)) x := by
    have HH := HasDerivAt.fun_sum (u := Finset.univ)
      (fun i _ => ((hG i).div (hd i) (hF i).ne').const_mul (c i))
    simpa only [he] using! HH
  exact (hP.mul hQ).congr_deriv (by ring)

end
end ChowlaCosine.Beckner

open scoped RealInnerProductSpace
namespace ChowlaCosine.Beckner

section FrameLaplacian
variable {ι κ E : Type*} [Fintype ι] [Fintype κ] [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- Exact algebraic Laplacian formula for a positive weighted product,
expressed using its scalar logarithmic first and second scores. -/
theorem frame_laplacian_identity (c v w : ι → ℝ) (u : ι → E)
    (hu : ∀ i, ‖u i‖ = 1) (b : OrthonormalBasis κ ℝ E) :
    (∑ j, ((∑ i, c i * ⟪u i, b j⟫ * v i) ^ 2 +
      ∑ i, c i * ⟪u i, b j⟫ ^ 2 * (w i - v i ^ 2))) =
      ‖frameVector c v u‖ ^ 2 + (∑ i, c i * w i) - ∑ i, c i * v i ^ 2 := by
  have hcoord : ∀ j, (∑ i, c i * ⟪u i, b j⟫ * v i) = ⟪frameVector c v u, b j⟫ := by
    intro j
    unfold frameVector
    rw [sum_inner]
    simp only [real_inner_smul_left]
    apply Finset.sum_congr rfl
    intro i _
    ring
  have hfirst : (∑ j, (∑ i, c i * ⟪u i, b j⟫ * v i) ^ 2) = ‖frameVector c v u‖ ^ 2 := by
    simp_rw [hcoord]
    exact b.sum_sq_inner_left _
  have hsecond : (∑ j, ∑ i, c i * ⟪u i, b j⟫ ^ 2 * (w i - v i ^ 2)) =
      ∑ i, c i * (w i - v i ^ 2) := by
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro i _
    calc
      _ = (c i * (w i - v i ^ 2)) * ∑ j, ⟪u i, b j⟫ ^ 2 := by
        rw [Finset.mul_sum]
        apply Finset.sum_congr rfl
        intro j _
        ring
      _ = _ := by rw [b.sum_sq_inner_left, hu]; norm_num
  rw [Finset.sum_add_distrib, hfirst, hsecond]
  simp_rw [mul_sub, Finset.sum_sub_distrib]
  ring

/-- Algebraic form of the pointwise nonnegative heat-flow defect.
Actual differentiation/integration of the geometric product is a later
obligation, not a hypothesis silently discharged by this identity. -/
theorem frame_heat_defect_nonneg (c v w : ι → ℝ) (u : ι → E)
    (hc : ∀ i, 0 ≤ c i) (hu : ∀ i, ‖u i‖ = 1) (hframe : IsWeightedFrame c u)
    (b : OrthonormalBasis κ ℝ E) (P : ℝ) (hP : 0 ≤ P) :
    0 ≤ P * (∑ i, c i * w i) -
      P * ∑ j, ((∑ i, c i * ⟪u i, b j⟫ * v i) ^ 2 +
        ∑ i, c i * ⟪u i, b j⟫ ^ 2 * (w i - v i ^ 2)) := by
  rw [frame_laplacian_identity c v w u hu b]
  have H := mul_nonneg hP (sub_nonneg.mpr (frame_variance_nonneg c v u hc hframe))
  nlinarith [H]
end FrameLaplacian

end ChowlaCosine.Beckner


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
