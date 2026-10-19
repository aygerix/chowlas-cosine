import ChowlaCosine.Beckner.Young

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
