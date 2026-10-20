import Mathlib

/-! # Classical Fourier transforms of L1 ∩ L2 functions

The normalization is mathlib's `exp(-2π i t ξ)`. Thus the cardinal sinc
corresponds to the spectral interval `[-1/2,1/2]` of length one.
-/

open MeasureTheory SchwartzMap FourierTransform
open scoped ENNReal NNReal FourierTransform ComplexConjugate

namespace ChowlaCosine.P31
set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

/-- Different Lp representatives of the same function define the same
actual tempered distribution. -/
theorem lp_tempered_eq_of_ae_eq {p q : ℝ≥0∞} [Fact (1 ≤ p)] [Fact (1 ≤ q)]
    (f : Lp (α := ℝ) ℂ p volume) (g : Lp (α := ℝ) ℂ q volume)
    (h : (f : ℝ → ℂ) =ᵐ[volume] g) :
    (f : TemperedDistribution ℝ ℂ) = (g : TemperedDistribution ℝ ℂ) := by
  ext φ
  simp only [Lp.toTemperedDistribution_apply]
  apply integral_congr_ae
  filter_upwards [h] with x hx
  rw [hx]

/-- Equality of the distributions of two Lp functions implies actual
a.e. equality, even if their exponents differ. -/
theorem lp_ae_eq_of_tempered_eq {p q : ℝ≥0∞} [hp : Fact (1 ≤ p)] [hq : Fact (1 ≤ q)]
    (f : Lp (α := ℝ) ℂ p volume) (g : Lp (α := ℝ) ℂ q volume)
    (h : (f : TemperedDistribution ℝ ℂ) = (g : TemperedDistribution ℝ ℂ)) :
    (f : ℝ → ℂ) =ᵐ[volume] g := by
  apply ae_eq_of_integral_contDiff_smul_eq (Lp.memLp f |>.locallyIntegrable hp.out)
    (Lp.memLp g |>.locallyIntegrable hq.out)
  intro ψ hψc hψs
  have hφs : HasCompactSupport (Complex.ofRealCLM ∘ ψ) := hψs.comp_left rfl
  have hφc : ContDiff ℝ ∞ (Complex.ofRealCLM ∘ ψ) := by fun_prop
  let φ : 𝓢(ℝ, ℂ) := hφs.toSchwartzMap hφc
  have H := congrArg (fun T : TemperedDistribution ℝ ℂ => T φ) h
  simpa only [Lp.toTemperedDistribution_apply, φ, HasCompactSupport.toSchwartzMap_coe,
    Function.comp_apply, Complex.ofRealCLM_apply, Complex.real_smul] using H

/-- The classical Fourier transform of an L1 function is bounded and
therefore gives an L∞ representative. -/
theorem memLp_top_fourier_of_integrable {f : ℝ → ℂ} (hf : Integrable f) :
    MemLp (𝓕 f) ∞ volume := by
  have hm : AEStronglyMeasurable (𝓕 f) volume := by
    have H := VectorFourier.fourierIntegral_continuous Real.continuous_fourierChar
      (L := innerₗ ℝ) continuous_inner hf
    exact H.aestronglyMeasurable
  apply memLp_top_of_bound hm (∫ x : ℝ, ‖f x‖)
  apply Filter.Eventually.of_forall
  intro x
  exact VectorFourier.norm_fourierIntegral_le_integral_norm Real.fourierChar volume (innerₗ ℝ) f x

/-- Classical Fourier transformation and distributional transformation
agree on L1 functions, with no Schwartz assumption. -/
theorem fourier_lp_one_tempered {f : ℝ → ℂ} (hf : Integrable f) :
    (𝓕 (((memLp_one_iff_integrable.mpr hf).toLp f) : TemperedDistribution ℝ ℂ)) =
      (((memLp_top_fourier_of_integrable hf).toLp (𝓕 f)) : TemperedDistribution ℝ ℂ) := by
  ext φ
  simp only [TemperedDistribution.fourier_apply, Lp.toTemperedDistribution_apply]
  have hf1 := (memLp_one_iff_integrable.mpr hf).coeFn_toLp
  have hfF := (memLp_top_fourier_of_integrable hf).coeFn_toLp
  have hleft : (∫ x : ℝ, (𝓕 φ) x • ((memLp_one_iff_integrable.mpr hf).toLp f) x) =
      ∫ x : ℝ, (𝓕 φ) x * f x := by
    apply integral_congr_ae
    filter_upwards [hf1] with x hx
    simp only [hx, smul_eq_mul]
  have hright : (∫ x : ℝ, φ x • ((memLp_top_fourier_of_integrable hf).toLp (𝓕 f)) x) =
      ∫ x : ℝ, φ x * (𝓕 f) x := by
    apply integral_congr_ae
    filter_upwards [hfF] with x hx
    simp only [hx, smul_eq_mul]
  rw [hleft, hright]
  simpa only [Real.fourier_eq, SchwartzMap.fourier_coe, smul_eq_mul,
    LinearMap.flip_def, real_inner_comm] using
    VectorFourier.integral_fourierIntegral_smul_eq_flip (L := innerₗ ℝ)
      Real.continuous_fourierChar continuous_inner φ.integrable hf

end ChowlaCosine.P31
