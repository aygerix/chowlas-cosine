import ChowlaCosine.P31.AnalyticNikolskii
import ChowlaCosine.Beckner.YoungSharpSpecial

/-! # Exact sinc interpolation for P31-N

The lemmas here concern the actual finite sinc sum on the real line and
integration over the full modulation circle.
-/

open MeasureTheory Real
open scoped BigOperators Topology

namespace ChowlaCosine.P31
set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

/-- The cardinal sinc kernel, with Fourier band `[-π,π]`. -/
noncomputable def cardinalSinc (t : ℝ) : ℝ := sinc (π*t)

/-- The exact modulated sinc interpolant, with no spatial truncation. -/
noncomputable def sincInterpolate {N : ℕ} (u : Fin N → ℂ) (θ t : ℝ) : ℂ :=
  ∑ j : Fin N, (u j * (cardinalSinc (t-j.val) : ℂ)) * circleCharacter (j.val : ℤ) θ

@[fun_prop] theorem continuous_cardinalSinc : Continuous cardinalSinc := by
  unfold cardinalSinc
  fun_prop

@[fun_prop] theorem continuous_sincInterpolate {N : ℕ} (u : Fin N → ℂ) :
    Continuous (Function.uncurry (sincInterpolate u)) := by
  unfold sincInterpolate
  fun_prop

/-- Exact modulation orthogonality for arbitrary vectors, including N=0. -/
theorem circleMean_sincInterpolate_sq {N : ℕ} (u : Fin N → ℂ) (t : ℝ) :
    circleMean (fun θ => ‖sincInterpolate u θ t‖^2) =
      ∑ j : Fin N, ‖u j‖^2 * cardinalSinc (t-j.val)^2 := by
  change circleMean (fun θ => ‖∑ j : Fin N,
    (u j * (cardinalSinc (t-j.val) : ℂ)) * circleCharacter (j.val : ℤ) θ‖^2) = _
  rw [circleMean_norm_sq_sum]
  apply Finset.sum_congr rfl
  intro i hi
  have hiff : ∀ j : Fin N, ((i.val:ℤ)=(j.val:ℤ)) ↔ i=j := by
    intro j
    constructor
    · intro h
      apply Fin.ext
      exact_mod_cast h
    · rintro rfl
      rfl
  simp_rw [hiff]
  simp only [Finset.sum_ite_eq, Finset.mem_univ, ↓reduceIte]
  rw [Complex.star_def, Complex.mul_conj, Complex.ofReal_re, Complex.normSq_eq_norm_sq,
    norm_mul, mul_pow, Complex.norm_real, Real.norm_eq_abs, sq_abs]

/-- The pointwise inverse-distance envelope retains the factor π exactly. -/
theorem abs_cardinalSinc_le {t : ℝ} (ht : t ≠ 0) :
    |cardinalSinc t| ≤ 1/(π*|t|) := by
  rw [cardinalSinc, sinc_of_ne_zero (mul_ne_zero pi_ne_zero ht), abs_div,
    abs_mul, abs_of_pos pi_pos]
  exact div_le_div_of_nonneg_right (abs_sin_le_one _) (by positivity)

/-- The scalar squared tail bound at any positive lower distance. -/
theorem cardinalSinc_sq_le {t δ : ℝ} (hδ : 0 < δ) (ht : δ ≤ |t|) :
    cardinalSinc t ^ 2 ≤ 1/(π^2*δ^2) := by
  have ht0 : t ≠ 0 := by intro h; simp only [h, abs_zero] at ht; linarith
  have hb : |cardinalSinc t| ≤ 1/(π*δ) :=
    (abs_cardinalSinc_le ht0).trans (by gcongr)
  have hs := (sq_le_sq₀ (abs_nonneg (cardinalSinc t)) (by positivity : 0 ≤ 1/(π*δ))).mpr hb
  simpa only [sq_abs, div_pow, one_pow, mul_pow] using hs

/-- Unit coefficient mass gives the uniform left-tail squared envelope. -/
theorem sinc_square_sum_left {N : ℕ} (u : Fin N → ℂ)
    (hu : (∑ j : Fin N, ‖u j‖^2)=1) {t : ℝ} (ht : t < 0) :
    (∑ j : Fin N, ‖u j‖^2 * cardinalSinc (t-j.val)^2) ≤ 1/(π^2*(-t)^2) := by
  calc
    _ ≤ ∑ j : Fin N, ‖u j‖^2 * (1/(π^2*(-t)^2)) := by
      apply Finset.sum_le_sum
      intro j hj
      apply mul_le_mul_of_nonneg_left _ (sq_nonneg _)
      apply cardinalSinc_sq_le (by linarith : 0 < -t)
      rw [abs_of_neg (by have : (0:ℝ) ≤ j.val := Nat.cast_nonneg _; linarith)]
      have : (0:ℝ) ≤ j.val := Nat.cast_nonneg _
      linarith
    _ = _ := by rw [← Finset.sum_mul, hu, one_mul]

/-- The right-tail envelope uses the exact final grid location N-1. -/
theorem sinc_square_sum_right {N : ℕ} (u : Fin N → ℂ)
    (hu : (∑ j : Fin N, ‖u j‖^2)=1) {t : ℝ} (ht : (N:ℝ)-1 < t) :
    (∑ j : Fin N, ‖u j‖^2 * cardinalSinc (t-j.val)^2) ≤
      1/(π^2*(t-((N:ℝ)-1))^2) := by
  calc
    _ ≤ ∑ j : Fin N, ‖u j‖^2 * (1/(π^2*(t-((N:ℝ)-1))^2)) := by
      apply Finset.sum_le_sum
      intro j hj
      apply mul_le_mul_of_nonneg_left _ (sq_nonneg _)
      apply cardinalSinc_sq_le (by linarith : 0 < t-((N:ℝ)-1))
      have hj : (j.val:ℝ) ≤ (N:ℝ)-1 := by
        have H : (j.val:ℝ)+1 ≤ N := by exact_mod_cast Nat.succ_le_of_lt j.isLt
        linarith only [H]
      rw [abs_of_pos (by linarith : 0 < t-j.val)]
      linarith
    _ = _ := by rw [← Finset.sum_mul, hu, one_mul]

/-- The project's circle normalization is exactly the Lebesgue set average. -/
theorem circleMean_eq_setAverage (f : ℝ → ℝ) :
    circleMean f = ⨍ x in Set.Ioc (0:ℝ) (2*π), f x := by
  rw [average_eq]
  simp only [Measure.real, Measure.restrict_apply_univ, Real.volume_Ioc, sub_zero,
    ENNReal.toReal_ofReal (by positivity : 0 ≤ 2*π), smul_eq_mul,
    circleMean, intervalIntegral.integral_of_le (by positivity : (0:ℝ) ≤ 2*π)]

/-- Concavity on the full modulation circle, with no discretization. -/
theorem circleMean_rpow_le {f : ℝ → ℝ} (hf : Continuous f) (hn : ∀ x, 0 ≤ f x)
    {p : ℝ} (hp0 : 0 ≤ p) (hp1 : p ≤ 1) :
    circleMean (fun x => f x ^ p) ≤ (circleMean f)^p := by
  have hfp : Continuous (fun x => f x ^ p) := (continuous_rpow_const hp0).comp hf
  have H := (concaveOn_rpow hp0 hp1).le_map_set_average
    (μ := volume) (t := Set.Ioc (0:ℝ) (2*π))
    (continuous_rpow_const hp0).continuousOn isClosed_Ici
    (by simp only [Real.volume_Ioc, sub_zero]; positivity)
    (by rw [Real.volume_Ioc]; exact ENNReal.ofReal_ne_top)
    (Filter.Eventually.of_forall (fun x => hn x))
    (hf.intervalIntegrable 0 (2*π) |>.1)
    (hfp.intervalIntegrable 0 (2*π) |>.1)
  simpa only [← circleMean_eq_setAverage] using H

/-- The averaged L4/3 integrand is bounded by the exact squared sinc mass. -/
theorem circleMean_sincInterpolate_four_thirds_le {N : ℕ} (u : Fin N → ℂ) (t : ℝ) :
    circleMean (fun θ => ‖sincInterpolate u θ t‖^(4/3:ℝ)) ≤
      (∑ j : Fin N, ‖u j‖^2 * cardinalSinc (t-j.val)^2)^(2/3:ℝ) := by
  have hc : Continuous (fun θ => ‖sincInterpolate u θ t‖^2) := by
    have H := (continuous_sincInterpolate u).comp (continuous_id.prodMk (continuous_const : Continuous (fun _ : ℝ => t)))
    exact H.norm.pow 2
  have H := circleMean_rpow_le hc (fun θ => sq_nonneg _) (by norm_num : (0:ℝ) ≤ 2/3)
    (by norm_num : (2/3:ℝ) ≤ 1)
  rw [circleMean_sincInterpolate_sq] at H
  have he : ∀ θ, (‖sincInterpolate u θ t‖^2)^(2/3:ℝ) = ‖sincInterpolate u θ t‖^(4/3:ℝ) := by
    intro θ
    rw [← rpow_natCast, ← rpow_mul (norm_nonneg _)]
    norm_num
  simpa only [he] using H

/-- The exact real-power form of the squared inverse-distance envelope. -/
theorem sinc_envelope_rpow {δ : ℝ} (hδ : 0 < δ) :
    (1/(π^2*δ^2))^(2/3:ℝ) = π^(-4/3:ℝ)*δ^(-4/3:ℝ) := by
  rw [one_div, inv_rpow (by positivity : 0 ≤ π^2*δ^2),
    mul_rpow (sq_nonneg π) (sq_nonneg δ),
    ← rpow_natCast π 2, ← rpow_mul pi_pos.le,
    ← rpow_natCast δ 2, ← rpow_mul hδ.le]
  norm_num
  rw [rpow_neg pi_pos.le, rpow_neg hδ.le]
  ring

/-- The averaged left tail, with the exact π^(-4/3) factor. -/
theorem circleMean_sincInterpolate_left {N : ℕ} (u : Fin N → ℂ)
    (hu : (∑ j : Fin N, ‖u j‖^2)=1) {t : ℝ} (ht : t < 0) :
    circleMean (fun θ => ‖sincInterpolate u θ t‖^(4/3:ℝ)) ≤
      π^(-4/3:ℝ)*(-t)^(-4/3:ℝ) := by
  have H := circleMean_sincInterpolate_four_thirds_le u t
  have H' := rpow_le_rpow (Finset.sum_nonneg (fun j _ => mul_nonneg (sq_nonneg _) (sq_nonneg _)))
    (sinc_square_sum_left u hu ht) (by norm_num : (0:ℝ) ≤ 2/3)
  exact H.trans (H'.trans_eq (sinc_envelope_rpow (by linarith : 0 < -t)))

/-- The averaged right tail at the exact endpoint N-1. -/
theorem circleMean_sincInterpolate_right {N : ℕ} (u : Fin N → ℂ)
    (hu : (∑ j : Fin N, ‖u j‖^2)=1) {t : ℝ} (ht : (N:ℝ)-1 < t) :
    circleMean (fun θ => ‖sincInterpolate u θ t‖^(4/3:ℝ)) ≤
      π^(-4/3:ℝ)*(t-((N:ℝ)-1))^(-4/3:ℝ) := by
  have H := circleMean_sincInterpolate_four_thirds_le u t
  have H' := rpow_le_rpow (Finset.sum_nonneg (fun j _ => mul_nonneg (sq_nonneg _) (sq_nonneg _)))
    (sinc_square_sum_right u hu ht) (by norm_num : (0:ℝ) ≤ 2/3)
  exact H.trans (H'.trans_eq (sinc_envelope_rpow (by linarith : 0 < t-((N:ℝ)-1))))

/-- One tail of the comparison envelope has exactly the stated mass. -/
theorem integral_sinc_tail_envelope {R : ℝ} (hR : 0 < R) :
    (∫ t : ℝ in Set.Ioi R, π^(-4/3:ℝ)*t^(-4/3:ℝ)) =
      3*π^(-4/3:ℝ)*R^(-1/3:ℝ) := by
  rw [integral_const_mul, integral_Ioi_rpow_of_lt (by norm_num : (-4/3:ℝ) < -1) hR]
  norm_num
  ring

end ChowlaCosine.P31
