import ChowlaCosine.Beckner.YoungSharp

/-! # M5: sharp autocorrelation and interval-supported convolution bounds -/

set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

namespace ChowlaCosine.Beckner
open Real
/-- The project Beckner constant is exact, without decimal rounding. -/
theorem becknerFactor_three_quarters_fourth :
    becknerFactor (3/4) ^ 4 = 4/(3*sqrt 3) := by
  have hsq : becknerFactor (3/4) ^ 2 = (4/3:ℝ)^(3/4:ℝ)/(4:ℝ)^(1/4:ℝ) := by
    rw [becknerFactor, sq_sqrt (by positivity)]
    norm_num
  have h8 : becknerFactor (3/4) ^ 8 = (16/27:ℝ) := by
    calc
      _ = (becknerFactor (3/4)^2)^4 := by ring
      _ = ((4/3:ℝ)^(3/4:ℝ)/(4:ℝ)^(1/4:ℝ))^4 := congrArg (fun x : ℝ => x^4) hsq
      _ = _ := by
        rw [div_pow, ← rpow_mul_natCast (by norm_num : (0:ℝ) ≤ 4/3),
          ← rpow_mul_natCast (by norm_num : (0:ℝ) ≤ 4)]
        norm_num
  have h3 : sqrt 3 ^ 2 = (3:ℝ) := sq_sqrt (by norm_num)
  have hβ : (4/(3*sqrt 3))^2 = (16/27:ℝ) := by
    rw [div_pow, mul_pow, h3]
    norm_num
  have hn : 0 ≤ becknerFactor (3/4) ^ 4 := pow_nonneg (sqrt_nonneg _) _
  have hβn : 0 ≤ 4/(3*sqrt 3) := by positivity
  nlinarith only [h8,hβ,hn,hβn, sq_nonneg (becknerFactor (3/4)^4-4/(3*sqrt 3))]

end ChowlaCosine.Beckner
namespace ChowlaCosine.Beckner
open MeasureTheory Real
open scoped ENNReal NNReal
@[simp] theorem becknerFactor_half : becknerFactor (1/2) = 1 := by
  norm_num [becknerFactor]

/-- The sharp project inequality, with its exact squared constant. -/
theorem sharp_young_four_thirds_sq {f g : ℝ → ℂ}
    (hf : MemLp f (ENNReal.ofReal (4/3:ℝ)))
    (hg : MemLp g (ENNReal.ofReal (4/3:ℝ))) :
    MemLp (convolution f g) 2 ∧
    eLpNorm (convolution f g) 2 ^ 2 ≤ ENNReal.ofReal (4/(3*sqrt 3)) *
      eLpNorm f (ENNReal.ofReal (4/3:ℝ)) ^ 2 * eLpNorm g (ENNReal.ofReal (4/3:ℝ)) ^ 2 := by
  obtain ⟨hi,H⟩ := sharp_young_finite (p := 4/3) (q := 4/3) (r := 2)
    (by norm_num) (by norm_num) (by norm_num) (by norm_num) hf hg
  have H' : eLpNorm (convolution f g) 2 ≤ ENNReal.ofReal (becknerFactor (3/4)^2) *
      eLpNorm f (ENNReal.ofReal (4/3:ℝ)) * eLpNorm g (ENNReal.ofReal (4/3:ℝ)) := by
    simpa only [show (1/(4/3):ℝ)=3/4 by norm_num, show (1-1/2:ℝ)=1/2 by norm_num,
      becknerFactor_half, mul_one, ← pow_two, ENNReal.ofReal_ofNat] using H
  have he : ENNReal.ofReal (becknerFactor (3/4)^2)^2 = ENNReal.ofReal (4/(3*sqrt 3)) := by
    rw [← ENNReal.ofReal_pow (sq_nonneg _), ← pow_mul,
      show (2*2:ℕ)=4 from rfl, becknerFactor_three_quarters_fourth]
  refine ⟨by simpa only [ENNReal.ofReal_ofNat] using hi, ?_⟩
  simpa only [mul_pow, he] using pow_le_pow_left' H' 2

noncomputable def reflectConj (h : ℝ → ℂ) : ℝ → ℂ := fun x => star (h (-x))

/-- Reflection and complex conjugation preserve every Lp space. -/
theorem memLp_reflectConj {h : ℝ → ℂ} {p : ℝ≥0∞} (hh : MemLp h p) :
    MemLp (reflectConj h) p := by
  have H := hh.comp_measurePreserving (Measure.measurePreserving_neg volume)
  refine H.congr_norm ?_ (Filter.Eventually.of_forall (fun x => by simp [reflectConj]))
  exact continuous_star.comp_aestronglyMeasurable H.1

/-- The exact seminorm identity holds for every exponent, including endpoints. -/
theorem eLpNorm_reflectConj (h : ℝ → ℂ) (p : ℝ≥0∞) (hh : AEStronglyMeasurable h) :
    eLpNorm (reflectConj h) p = eLpNorm h p := by
  calc
    _ = eLpNorm (h ∘ Neg.neg) p volume := eLpNorm_congr_norm_ae
      (Filter.Eventually.of_forall (fun x => by simp [reflectConj]))
    _ = _ := eLpNorm_comp_measurePreserving hh (Measure.measurePreserving_neg volume)

/-- M5: the sharp autocorrelation inequality for arbitrary complex L4/3 data. -/
theorem sharp_autocorrelation {h : ℝ → ℂ} (hh : MemLp h (ENNReal.ofReal (4/3:ℝ))) :
    MemLp (convolution h (reflectConj h)) 2 ∧
    eLpNorm (convolution h (reflectConj h)) 2 ^ 2 ≤
      ENNReal.ofReal (4/(3*sqrt 3)) * eLpNorm h (ENNReal.ofReal (4/3:ℝ)) volume ^ 4 := by
  obtain ⟨hi,H⟩ := sharp_young_four_thirds_sq hh (memLp_reflectConj hh)
  refine ⟨hi, ?_⟩
  rw [eLpNorm_reflectConj h _ hh.1] at H
  simpa only [mul_assoc, ← pow_add, show (2+2:ℕ)=4 from rfl] using H

end ChowlaCosine.Beckner
namespace ChowlaCosine.Beckner
open MeasureTheory Real
open scoped ENNReal NNReal
/-- The finite-measure Hölder estimate with the exact interval length. -/
theorem interval_four_thirds_le_two {h : ℝ → ℂ} {a b : ℝ}
    (hh : MemLp h 2) (hs : Function.support h ⊆ Set.Icc a b) :
    MemLp h (ENNReal.ofReal (4/3:ℝ)) ∧
    eLpNorm h (ENNReal.ofReal (4/3:ℝ)) volume ^ 4 ≤
      ENNReal.ofReal (b-a) * eLpNorm h 2 volume ^ 4 := by
  have H := eLpNorm_le_eLpNorm_mul_rpow_measure_univ
    (μ := volume.restrict (Set.Icc a b)) (p := ENNReal.ofReal (4/3:ℝ)) (q := 2)
    (by norm_num) hh.1.restrict
  rw [eLpNorm_restrict_eq_of_support_subset hs,
    eLpNorm_restrict_eq_of_support_subset hs] at H
  have H' : eLpNorm h (ENNReal.ofReal (4/3:ℝ)) volume ≤
      eLpNorm h 2 volume * ENNReal.ofReal (b-a) ^ (1/4:ℝ) := by
    convert H using 1 <;> norm_num
  have h43 : MemLp h (ENNReal.ofReal (4/3:ℝ)) := by
    refine ⟨hh.1, H'.trans_lt (ENNReal.mul_lt_top hh.2 ?_)⟩
    exact ENNReal.rpow_lt_top_of_nonneg (by norm_num) ENNReal.ofReal_ne_top
  have he : (ENNReal.ofReal (b-a) ^ (1/4:ℝ)) ^ 4 = ENNReal.ofReal (b-a) := by
    rw [← ENNReal.rpow_natCast, ← ENNReal.rpow_mul]
    norm_num
  refine ⟨h43, ?_⟩
  simpa only [mul_pow, he, mul_comm] using pow_le_pow_left' H' 4

/-- M5: sharp Young followed by interval Hölder, for arbitrary complex L2
functions supported in an interval. The exact sharp factor is retained. -/
theorem sharp_interval_selfConvolution {h : ℝ → ℂ} {a b : ℝ}
    (hh : MemLp h 2) (hs : Function.support h ⊆ Set.Icc a b) :
    MemLp (convolution h h) 2 ∧
    eLpNorm (convolution h h) 2 ^ 2 ≤
      ENNReal.ofReal (4/(3*sqrt 3)) * ENNReal.ofReal (b-a) * eLpNorm h 2 volume ^ 4 := by
  obtain ⟨h43,H43⟩ := interval_four_thirds_le_two hh hs
  obtain ⟨hi,H⟩ := sharp_young_four_thirds_sq h43 h43
  refine ⟨hi, ?_⟩
  calc
    _ ≤ ENNReal.ofReal (4/(3*sqrt 3)) * eLpNorm h (ENNReal.ofReal (4/3:ℝ)) volume ^ 4 := by
      simpa only [mul_assoc, ← pow_add, show (2+2:ℕ)=4 from rfl] using H
    _ ≤ ENNReal.ofReal (4/(3*sqrt 3)) * (ENNReal.ofReal (b-a) * eLpNorm h 2 volume ^ 4) :=
      mul_le_mul' le_rfl H43
    _ = _ := (mul_assoc _ _ _).symm

/-- The interval-supported autocorrelation version of M5. -/
theorem sharp_interval_autocorrelation {h : ℝ → ℂ} {a b : ℝ}
    (hh : MemLp h 2) (hs : Function.support h ⊆ Set.Icc a b) :
    MemLp (convolution h (reflectConj h)) 2 ∧
    eLpNorm (convolution h (reflectConj h)) 2 ^ 2 ≤
      ENNReal.ofReal (4/(3*sqrt 3)) * ENNReal.ofReal (b-a) * eLpNorm h 2 volume ^ 4 := by
  obtain ⟨h43,H43⟩ := interval_four_thirds_le_two hh hs
  obtain ⟨hi,H⟩ := sharp_autocorrelation h43
  refine ⟨hi, H.trans ?_⟩
  simpa only [mul_assoc] using mul_le_mul' (le_refl (ENNReal.ofReal (4/(3*sqrt 3)))) H43
end ChowlaCosine.Beckner
