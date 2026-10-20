import ChowlaCosine.Beckner.HeatFlowRelative

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
