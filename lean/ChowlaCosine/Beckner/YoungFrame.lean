import ChowlaCosine.Beckner.HeatFlowDensity

/-! # An explicit two-dimensional frame for the interior Young exponents

The parameters are the three positive complementary weights, of sum one.
This module constructs the frame; the sharp-factor and Lp reduction are separate.
-/

open MeasureTheory Real
open scoped BigOperators Topology RealInnerProductSpace

namespace ChowlaCosine.Beckner
set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

section
variable {ι E : Type*} [Fintype ι] [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- The three scalar entries of a symmetric 2×2 matrix verify the full
bilinear weighted-frame identity, not just its diagonal specialization. -/
theorem isWeightedFrame_plane_of_coefficients
    (b : OrthonormalBasis (Fin 2) ℝ E) (c A B : ι → ℝ)
    (hA : (∑ i, c i * A i ^ 2) = 1) (hB : (∑ i, c i * B i ^ 2) = 1)
    (hAB : (∑ i, c i * (A i * B i)) = 0) :
    IsWeightedFrame c (fun i => planePoint b (A i,B i)) := by
  intro x y
  have he : ∀ i, c i * (⟪planePoint b (A i,B i),x⟫ * ⟪planePoint b (A i,B i),y⟫) =
      (c i*A i^2)*(⟪b 0,x⟫*⟪b 0,y⟫) +
      (c i*B i^2)*(⟪b 1,x⟫*⟪b 1,y⟫) +
      (c i*(A i*B i))*(⟪b 0,x⟫*⟪b 1,y⟫+⟪b 1,x⟫*⟪b 0,y⟫) := by
    intro i
    simp only [planePoint, inner_add_left, real_inner_smul_left]
    ring
  simp_rw [he, Finset.sum_add_distrib, ← Finset.sum_mul, hA, hB, hAB,
    one_mul, zero_mul, add_zero]
  simpa only [Fin.sum_univ_two, real_inner_comm x (b 0), real_inner_comm x (b 1)] using
    b.sum_inner_mul_inner x y

end

/-- Weights cᵢ=1-dᵢ for complementary weights d=(a,b,d), a+b+d=1. -/
def youngFrameWeights (a b d : ℝ) : Fin 3 → ℝ := ![b+d,a+d,a+b]

def youngFrameComplement (a b d : ℝ) : Fin 3 → ℝ := ![a,b,d]

noncomputable def youngFrameFirst (a b d : ℝ) : Fin 3 → ℝ :=
  ![sqrt b/(sqrt (a+b)*sqrt (b+d)), -sqrt a/(sqrt (a+b)*sqrt (a+d)), 0]

noncomputable def youngFrameSecond (a b d : ℝ) : Fin 3 → ℝ :=
  ![sqrt a*sqrt d/(sqrt (a+b)*sqrt (b+d)),
    sqrt b*sqrt d/(sqrt (a+b)*sqrt (a+d)), -1]

/-- Scales relating the three frame forms to x, y and -(x+y). -/
noncomputable def youngFrameScale (a b d : ℝ) : Fin 3 → ℝ :=
  ![sqrt a*sqrt (b+d),sqrt b*sqrt (a+d),sqrt d*sqrt (a+b)]

/-- The actual 2×2 map from frame coordinates to the first two scaled forms. -/
noncomputable def youngFrameMatrix (a b d : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![youngFrameScale a b d 0 * youngFrameFirst a b d 0,
      youngFrameScale a b d 0 * youngFrameSecond a b d 0;
     youngFrameScale a b d 1 * youngFrameFirst a b d 1,
      youngFrameScale a b d 1 * youngFrameSecond a b d 1]

/-- The determinant keeps all scaling factors and has the exact positive value. -/
theorem youngFrameMatrix_det (a b d : ℝ) (ha : 0 < a) (hb : 0 < b) (hd : 0 < d) :
    (youngFrameMatrix a b d).det = sqrt a*sqrt b*sqrt d := by
  have hab : 0 < a+b := add_pos ha hb
  have had : 0 < a+d := add_pos ha hd
  have hbd : 0 < b+d := add_pos hb hd
  have hsnab := (sqrt_pos.mpr hab).ne'
  have hsnad := (sqrt_pos.mpr had).ne'
  have hsnbd := (sqrt_pos.mpr hbd).ne'
  simp [youngFrameMatrix, Matrix.det_fin_two, youngFrameScale, youngFrameFirst, youngFrameSecond]
  field_simp
  simp only [sq_sqrt ha.le, sq_sqrt hb.le, sq_sqrt hd.le,
    sq_sqrt hab.le, sq_sqrt had.le, sq_sqrt hbd.le]
  ring

/-- Exact dependence of the three scaled coordinate forms. -/
theorem youngFrame_coordinate_relation (a b d : ℝ) (ha : 0 < a) (hb : 0 < b) (hd : 0 < d) :
    (∑ i, youngFrameScale a b d i * youngFrameFirst a b d i) = 0 ∧
    (∑ i, youngFrameScale a b d i * youngFrameSecond a b d i) = 0 := by
  have hab : 0 < a+b := add_pos ha hb
  have had : 0 < a+d := add_pos ha hd
  have hbd : 0 < b+d := add_pos hb hd
  have hsnab := (sqrt_pos.mpr hab).ne'
  have hsnad := (sqrt_pos.mpr had).ne'
  have hsnbd := (sqrt_pos.mpr hbd).ne'
  simp [Fin.sum_univ_three, youngFrameScale, youngFrameFirst, youngFrameSecond]
  constructor
  · field_simp
    ring
  · field_simp
    simp only [sq_sqrt ha.le, sq_sqrt hb.le, sq_sqrt hd.le,
      sq_sqrt hab.le, sq_sqrt had.le, sq_sqrt hbd.le]
    ring

/-- One scalar factor in the determinant/Lp cancellation, with both
complementary weights displayed explicitly. -/
theorem young_scalar_factor {c d : ℝ} (hc : 0 < c) (hd : 0 < d) (hsum : c+d=1) :
    sqrt d / (sqrt d*sqrt c)^c = d^(d/2) / c^(c/2) := by
  rw [sqrt_eq_rpow, sqrt_eq_rpow, mul_rpow (rpow_pos_of_pos hd _).le (rpow_pos_of_pos hc _).le,
    ← rpow_mul hd.le, ← rpow_mul hc.le]
  calc
    _ = (d^(1/2:ℝ) / d^((1/2:ℝ)*c)) / c^((1/2:ℝ)*c) := by
      rw [div_div]
    _ = d^((1/2:ℝ)-(1/2:ℝ)*c) / c^((1/2:ℝ)*c) := by rw [← rpow_sub hd]
    _ = _ := by
      congr 1
      · congr 1
        linarith only [hsum]
      · congr 1
        ring

/-- In exponent notation p=1/c and p'=1/d, this is precisely Beckner's A_p. -/
theorem young_scalar_factor_beckner {c d : ℝ} (hc : 0 < c) (hd : 0 < d) (hsum : c+d=1) :
    sqrt d / (sqrt d*sqrt c)^c = sqrt ((1/c)^c / (1/d)^d) := by
  rw [young_scalar_factor hc hd hsum]
  rw [one_div, one_div, inv_rpow hc.le, inv_rpow hd.le, inv_div_inv,
    sqrt_eq_rpow, div_rpow (rpow_pos_of_pos hd _).le (rpow_pos_of_pos hc _).le,
    ← rpow_mul hd.le, ← rpow_mul hc.le]
  congr 1 <;> congr 1 <;> ring

/-- The exact determinant divided by all three dilation factors is Beckner's
product A_p A_q A_{r'}, with pᵢ=1/cᵢ and pᵢ'=1/dᵢ. -/
theorem youngFrame_sharp_factor (a b d : ℝ) (ha : 0 < a) (hb : 0 < b) (hd : 0 < d)
    (hsum : a+b+d=1) :
    (youngFrameMatrix a b d).det /
      (∏ i, youngFrameScale a b d i ^ youngFrameWeights a b d i) =
    ∏ i, sqrt ((1/youngFrameWeights a b d i)^youngFrameWeights a b d i /
      (1/youngFrameComplement a b d i)^youngFrameComplement a b d i) := by
  have hci : ∀ i, 0 < youngFrameWeights a b d i := by
    intro i
    fin_cases i <;> simp [youngFrameWeights] <;> positivity
  have hdi : ∀ i, 0 < youngFrameComplement a b d i := by
    intro i
    fin_cases i <;> simp [youngFrameComplement] <;> assumption
  have hsum' : ∀ i, youngFrameWeights a b d i + youngFrameComplement a b d i = 1 := by
    intro i
    fin_cases i <;> simp [youngFrameWeights, youngFrameComplement] <;> linarith only [hsum]
  have hscale : ∀ i, youngFrameScale a b d i =
      sqrt (youngFrameComplement a b d i) * sqrt (youngFrameWeights a b d i) := by
    intro i
    fin_cases i <;> rfl
  calc
    _ = ∏ i, sqrt (youngFrameComplement a b d i) /
        youngFrameScale a b d i ^ youngFrameWeights a b d i := by
      rw [Finset.prod_div_distrib, youngFrameMatrix_det a b d ha hb hd]
      congr 1
      simp [Fin.prod_univ_three, youngFrameComplement]
    _ = _ := by
      apply Finset.prod_congr rfl
      intro i _
      rw [hscale]
      exact young_scalar_factor_beckner (hci i) (hdi i) (hsum' i)

/-- The exact 2×2 coefficient identities for all interior Young triples. -/
theorem youngFrame_matrix (a b d : ℝ) (ha : 0 < a) (hb : 0 < b) (hd : 0 < d)
    (hsum : a+b+d=1) :
    (∑ i, youngFrameWeights a b d i * youngFrameFirst a b d i ^ 2) = 1 ∧
    (∑ i, youngFrameWeights a b d i * youngFrameSecond a b d i ^ 2) = 1 ∧
    (∑ i, youngFrameWeights a b d i *
      (youngFrameFirst a b d i * youngFrameSecond a b d i)) = 0 := by
  have hab : 0 < a+b := add_pos ha hb
  have had : 0 < a+d := add_pos ha hd
  have hbd : 0 < b+d := add_pos hb hd
  have hsab := sq_sqrt hab.le
  have hsad := sq_sqrt had.le
  have hsbd := sq_sqrt hbd.le
  have hsa := sq_sqrt ha.le
  have hsb := sq_sqrt hb.le
  have hsd := sq_sqrt hd.le
  have hsnab := (sqrt_pos.mpr hab).ne'
  have hsnad := (sqrt_pos.mpr had).ne'
  have hsnbd := (sqrt_pos.mpr hbd).ne'
  simp [Fin.sum_univ_three, youngFrameWeights, youngFrameFirst, youngFrameSecond,
    Matrix.vecHead, Matrix.vecTail, Function.comp_def]
  constructor
  · field_simp
    simp only [hsab, hsad, hsbd, hsa, hsb]
    ring
  constructor
  · field_simp
    simp only [hsab, hsad, hsbd, hsa, hsb, hsd]
    rw [show d=1-a-b by linarith only [hsum]]
    ring
  · field_simp
    simp only [hsab, hsad, hsbd]
    ring

section
variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

noncomputable def youngFrame (basis : OrthonormalBasis (Fin 2) ℝ E) (a b d : ℝ) : Fin 3 → E :=
  fun i => planePoint basis (youngFrameFirst a b d i, youngFrameSecond a b d i)

/-- The explicit vectors satisfy the whole-space bilinear frame identity. -/
theorem youngFrame_isWeightedFrame (basis : OrthonormalBasis (Fin 2) ℝ E)
    (a b d : ℝ) (ha : 0 < a) (hb : 0 < b) (hd : 0 < d) (hsum : a+b+d=1) :
    IsWeightedFrame (youngFrameWeights a b d) (youngFrame basis a b d) := by
  obtain ⟨hA,hB,hAB⟩ := youngFrame_matrix a b d ha hb hd hsum
  exact isWeightedFrame_plane_of_coefficients basis _ _ _ hA hB hAB

/-- Every one of the three explicit vectors is a unit vector. -/
theorem youngFrame_unit (basis : OrthonormalBasis (Fin 2) ℝ E)
    (a b d : ℝ) (ha : 0 < a) (hb : 0 < b) (hd : 0 < d) (hsum : a+b+d=1) :
    ∀ i, ‖youngFrame basis a b d i‖ = 1 := by
  have hab : 0 < a+b := add_pos ha hb
  have had : 0 < a+d := add_pos ha hd
  have hbd : 0 < b+d := add_pos hb hd
  have hcoords : ∀ i, youngFrameFirst a b d i ^ 2 + youngFrameSecond a b d i ^ 2 = 1 := by
    intro i
    fin_cases i <;>
      simp [youngFrameFirst, youngFrameSecond, div_pow, mul_pow,
        sq_sqrt ha.le, sq_sqrt hb.le, sq_sqrt hd.le, sq_sqrt hab.le, sq_sqrt had.le, sq_sqrt hbd.le]
    all_goals
      field_simp
      rw [show d=1-a-b by linarith only [hsum]]
      ring
  intro i
  have H := norm_planePoint_sq basis (youngFrameFirst a b d i,youngFrameSecond a b d i)
  rw [hcoords i] at H
  change ‖youngFrame basis a b d i‖^2 = 1 at H
  nlinarith only [H, norm_nonneg (youngFrame basis a b d i)]

/-- The scaled frame vectors have exactly the dependence required for the
convolution trilinear form. -/
theorem youngFrame_relation (basis : OrthonormalBasis (Fin 2) ℝ E)
    (a b d : ℝ) (ha : 0 < a) (hb : 0 < b) (hd : 0 < d) :
    (∑ i, youngFrameScale a b d i • youngFrame basis a b d i) = 0 := by
  obtain ⟨hA,hB⟩ := youngFrame_coordinate_relation a b d ha hb hd
  simp only [youngFrame, planePoint, smul_add, smul_smul, Finset.sum_add_distrib,
    ← Finset.sum_smul, smul_eq_mul, hA, hB, zero_smul, zero_add]

/-- Applying the unrestricted geometric theorem to this concrete Young frame.
This is a geometric integral theorem; Lp and sharp-factor cancellation are not
implicit in its conclusion. -/
theorem geometric_brascamp_lieb_youngFrame
    (basis : OrthonormalBasis (Fin 2) ℝ E) (a b d : ℝ)
    (ha : 0 < a) (hb : 0 < b) (hd : 0 < d) (hsum : a+b+d=1)
    (f : Fin 3 → ℝ → ℝ) (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y) :
    Integrable (fun z : ℝ × ℝ => ∏ i,
      f i ⟪youngFrame basis a b d i,planePoint basis z⟫ ^ youngFrameWeights a b d i)
      (volume.prod volume) ∧
    (∫ z : ℝ × ℝ, ∏ i,
      f i ⟪youngFrame basis a b d i,planePoint basis z⟫ ^ youngFrameWeights a b d i
      ∂volume.prod volume) ≤ ∏ i, (∫ y : ℝ, f i y) ^ youngFrameWeights a b d i := by
  apply geometric_brascamp_lieb f (youngFrameWeights a b d) (youngFrame basis a b d) hf hn
  · intro i
    fin_cases i <;> simp [youngFrameWeights] <;> positivity
  · exact youngFrame_unit basis a b d ha hb hd hsum
  · exact youngFrame_isWeightedFrame basis a b d ha hb hd hsum

end
end ChowlaCosine.Beckner
