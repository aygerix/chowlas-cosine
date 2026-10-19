import ChowlaCosine.Beckner.YoungSpecial

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
