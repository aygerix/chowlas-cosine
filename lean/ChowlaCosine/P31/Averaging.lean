import ChowlaCosine.P31.WindowMoments

/-!
# Averaging continuous windows on the full circle

These lemmas are independent of finite spectral factorization. In particular
there is no choice of factors under the integral.
-/

open Real MeasureTheory

namespace ChowlaCosine.P31

@[fun_prop] theorem continuous_circleMean_param {f : ℝ → ℝ → ℝ}
    (hf : Continuous (Function.uncurry f)) :
    Continuous (fun y => circleMean (f y)) := by
  unfold circleMean
  exact continuous_const.mul
    (intervalIntegral.continuous_parametric_intervalIntegral_of_continuous' hf _ _)

/-- Fubini on the actual square `[0,2π]²`; no finite sampling. -/
theorem circleMean_swap {f : ℝ → ℝ → ℝ}
    (hf : Continuous (Function.uncurry f)) :
    circleMean (fun y => circleMean (fun x => f y x)) =
      circleMean (fun x => circleMean (fun y => f y x)) := by
  have hT : (0 : ℝ) ≤ 2 * π := by positivity
  have hint : Integrable (Function.uncurry f)
      ((volume.restrict (Set.Ioc (0 : ℝ) (2 * π))).prod
        (volume.restrict (Set.Ioc (0 : ℝ) (2 * π)))) := by
    rw [Measure.prod_restrict]
    apply (hf.continuousOn.integrableOn_compact
      (isCompact_Icc.prod isCompact_Icc)).mono_set
    exact Set.prod_mono Set.Ioc_subset_Icc_self Set.Ioc_subset_Icc_self
  have hswap := integral_integral_swap hint
  simp only [circleMean, intervalIntegral.integral_const_mul]
  congr 1
  simp only [intervalIntegral.integral_of_le hT]
  exact congrArg (fun z : ℝ => (2 * π)⁻¹ * z) hswap

/-- Translation invariance, with the full real variable retained. -/
theorem circleMean_periodic_sub {f : ℝ → ℝ}
    (hf : Function.Periodic f (2 * π)) (y : ℝ) :
    circleMean (fun x => f (x - y)) = circleMean f := by
  unfold circleMean
  rw [intervalIntegral.integral_comp_sub_right]
  congr 1
  convert hf.intervalIntegral_add_eq (-y) 0 using 1 <;> congr 1 <;> ring

/-- Reflection followed by translation, needed when the window centre varies. -/
theorem circleMean_periodic_sub_left {f : ℝ → ℝ}
    (hf : Function.Periodic f (2 * π)) (y : ℝ) :
    circleMean (fun x => f (y - x)) = circleMean f := by
  unfold circleMean
  rw [intervalIntegral.integral_comp_sub_left]
  congr 1
  convert hf.intervalIntegral_add_eq (y - 2 * π) 0 using 1 <;> congr 1 <;> ring

/-- The averaged squared window is the product of its two exact moments. -/
theorem circleMean_window_sq {F g : ℝ → ℝ}
    (hF : Continuous F) (hg : Continuous g)
    (hperiod : Function.Periodic F (2 * π)) :
    circleMean (fun y => circleMean (fun x => (F (x - y) * g x) ^ 2)) =
      circleMean (fun x => F x ^ 2) * circleMean (fun x => g x ^ 2) := by
  rw [circleMean_swap (by fun_prop)]
  have hp : Function.Periodic (fun x => F x ^ 2) (2 * π) := by
    intro x
    change F (x + 2 * π) ^ 2 = F x ^ 2
    rw [hperiod x]
  have hinner : ∀ x, circleMean (fun y => (F (x - y) * g x) ^ 2) =
      circleMean (fun y => F y ^ 2) * g x ^ 2 := by
    intro x
    simp only [mul_pow]
    rw [circleMean_mul_const, circleMean_periodic_sub_left hp]
  simp_rw [hinner]
  exact circleMean_const_mul _ _

/-- Averaging any pointwise square/mean inequality. The hypothesis must
subsequently be obtained from spectral factorization and analytic Nikolskii. -/
theorem averaged_window_bound {F g : ℝ → ℝ} (C : ℝ)
    (hF : Continuous F) (hg : Continuous g)
    (hperiod : Function.Periodic F (2 * π))
    (hbound : ∀ y : ℝ, circleMean (fun x => (F (x - y) * g x) ^ 2) ≤
      C * circleMean (fun x => F (x - y) * g x) ^ 2) :
    circleMean (fun x => F x ^ 2) * circleMean (fun x => g x ^ 2) ≤
      C * circleMean (fun y => circleMean (fun x => F (x - y) * g x) ^ 2) := by
  rw [← circleMean_window_sq hF hg hperiod, ← circleMean_const_mul]
  apply circleMean_mono (continuous_circleMean_param (by fun_prop))
    (by fun_prop) hbound

end ChowlaCosine.P31
