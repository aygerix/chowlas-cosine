import ChowlaCosine.Beckner.HeatFlowInitial
import Mathlib.MeasureTheory.Function.ContinuousMapDense
import Mathlib.MeasureTheory.Function.ConvergenceInMeasure

/-! # Null-set pullback and nonnegative compact approximation for planar frames -/

open MeasureTheory Real
open scoped BigOperators Topology RealInnerProductSpace

namespace ChowlaCosine.Beckner
set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 400000

/-- Null sets pull back to planar null sets along every nonzero linear form,
including forms with one vanishing coefficient. The predicate need not itself
be measurable: a measurable null hull is used before Fubini. -/
theorem ae_plane_linear {P : ℝ → Prop} (hP : ∀ᵐ x : ℝ, P x)
    (a b : ℝ) (hab : a ≠ 0 ∨ b ≠ 0) :
    ∀ᵐ z : ℝ × ℝ ∂volume.prod volume, P (a*z.1+b*z.2) := by
  obtain ⟨N, hN, hNm, hNzero⟩ := exists_measurable_superset_of_null (ae_iff.mp hP)
  have hNae : ∀ᵐ x : ℝ, x ∉ N := by
    rw [ae_iff]
    simpa using hNzero
  have hright : ∀ a b : ℝ, b ≠ 0 →
      ∀ᵐ z : ℝ × ℝ ∂volume.prod volume, a*z.1+b*z.2 ∉ N := by
    intro a b hb
    have hmeas : Measurable (fun z : ℝ × ℝ => a*z.1+b*z.2) := by fun_prop
    apply (Measure.ae_prod_iff_ae_ae (hNm.compl.preimage hmeas)).mpr
    apply Filter.Eventually.of_forall
    intro x
    simpa only [Function.comp_def, smul_eq_mul, Set.mem_compl_iff] using
      ((quasiMeasurePreserving_add_left volume (a*x)).comp
        (Measure.quasiMeasurePreserving_smul volume hb)).ae hNae
  have H : ∀ᵐ z : ℝ × ℝ ∂volume.prod volume, a*z.1+b*z.2 ∉ N := by
    rcases hab with ha | hb
    · have H := (Measure.measurePreserving_swap (μ := (volume : Measure ℝ))
        (ν := (volume : Measure ℝ))).quasiMeasurePreserving.ae
        (hright b a ha)
      simpa only [Prod.fst_swap, Prod.snd_swap, add_comm] using H
    · exact hright a b hb
  filter_upwards [H] with z hz
  by_contra h
  exact hz (hN h)

/-- The planar linear form of every nonzero vector respects almost-everywhere
statements. No assertion about an arbitrary measurable pullback is assumed. -/
theorem ae_plane_inner {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    (b : OrthonormalBasis (Fin 2) ℝ E) (u : E) (hu : u ≠ 0)
    {P : ℝ → Prop} (hP : ∀ᵐ x : ℝ, P x) :
    ∀ᵐ z : ℝ × ℝ ∂volume.prod volume, P ⟪u,planePoint b z⟫ := by
  have hab : ⟪u,b 0⟫ ≠ 0 ∨ ⟪u,b 1⟫ ≠ 0 := by
    by_contra h
    push Not at h
    have H := b.sum_sq_inner_left u
    simp only [Fin.sum_univ_two, h.1, h.2, zero_pow (by decide : 2 ≠ 0), zero_add] at H
    exact hu (norm_eq_zero.mp (sq_eq_zero_iff.mp H.symm))
  have H := ae_plane_linear hP ⟪u,b 0⟫ ⟪u,b 1⟫ hab
  simpa only [planePoint, inner_add_right, real_inner_smul_right, mul_comm] using H

/-- A fixed nonnegative continuous compact datum of strictly positive mass. -/
theorem exists_positive_compact_datum :
    ∃ φ : ℝ → ℝ, Continuous φ ∧ HasCompactSupport φ ∧ (∀ x, 0 ≤ φ x) ∧
      0 < ∫ x : ℝ, φ x := by
  let φ : ℝ → ℝ := fun x => max (1-|x|) 0
  have hcont : Continuous φ := by dsimp [φ]; fun_prop
  have hcompact : HasCompactSupport φ := by
    apply HasCompactSupport.intro (K := Set.Icc (-1) 1) isCompact_Icc
    intro x hx
    dsimp [φ]
    rw [max_eq_right]
    have H : 1 ≤ |x| := by
      by_contra h
      exact hx (abs_le.mp (le_of_lt (lt_of_not_ge h)))
    linarith
  have hn : ∀ x, 0 ≤ φ x := fun x => le_max_right _ _
  refine ⟨φ, hcont, hcompact, hn, ?_⟩
  exact hcont.integral_pos_of_hasCompactSupport_nonneg_nonzero hcompact hn (x := 0)
    (by norm_num [φ])

/-- Approximate every nonnegative L1 datum, including the zero datum, by
nonnegative continuous compact data of strictly positive mass. -/
theorem exists_positive_compact_approximation {f : ℝ → ℝ} (hf : Integrable f)
    (hn : ∀ y, 0 ≤ f y) {ε : ℝ} (hε : 0 < ε) :
    ∃ g : ℝ → ℝ, Continuous g ∧ HasCompactSupport g ∧ (∀ y, 0 ≤ g y) ∧
      0 < ∫ y : ℝ, g y ∧ (∫ y : ℝ, ‖f y-g y‖) ≤ ε := by
  obtain ⟨φ,hφc,hφs,hφn,hφm⟩ := exists_positive_compact_datum
  have hφi : Integrable φ := hφc.integrable_of_hasCompactSupport hφs
  obtain ⟨g,hgs,herr,hgc,hgi⟩ := hf.exists_hasCompactSupport_integral_sub_le (half_pos hε)
  let δ : ℝ := ε/(2*((∫ y : ℝ, φ y)+1))
  have hδ : 0 < δ := by dsimp [δ]; positivity
  let G : ℝ → ℝ := fun y => |g y|+δ*φ y
  have hGc : Continuous G := hgc.abs.add (continuous_const.mul hφc)
  have hGs : HasCompactSupport G := hgs.abs.add (hφs.mul_left (f := fun _ => δ))
  have hGi : Integrable G := hGc.integrable_of_hasCompactSupport hGs
  have hGn : ∀ y, 0 ≤ G y := fun y => add_nonneg (abs_nonneg _) (mul_nonneg hδ.le (hφn y))
  have hGm : 0 < ∫ y : ℝ, G y := by
    have he : (∫ y : ℝ, G y) = (∫ y : ℝ, |g y|)+(∫ y : ℝ, δ*φ y) :=
      integral_add (show Integrable (fun y => |g y|) from hgi.norm) (hφi.const_mul δ)
    rw [he, integral_const_mul]
    exact add_pos_of_nonneg_of_pos (integral_nonneg (fun _ => abs_nonneg _)) (mul_pos hδ hφm)
  refine ⟨G,hGc,hGs,hGn,hGm,?_⟩
  have hp : ∀ y, ‖f y-G y‖ ≤ ‖f y-g y‖+δ*φ y := by
    intro y
    change abs (f y-(abs (g y)+δ*φ y)) ≤ |f y-g y|+δ*φ y
    calc
      _ = abs ((f y-abs (g y))-δ*φ y) := congrArg abs (by ring)
      _ ≤ abs (f y-abs (g y))+|δ*φ y| := abs_sub _ _
      _ ≤ |f y-g y|+δ*φ y := by
        rw [abs_of_nonneg (mul_nonneg hδ.le (hφn y))]
        have hd : abs (f y-abs (g y)) ≤ |f y-g y| := by
          simpa only [abs_of_nonneg (hn y)] using abs_abs_sub_abs_le_abs_sub (f y) (g y)
        exact add_le_add hd le_rfl
  have H := integral_mono (hf.sub hGi).norm ((hf.sub hgi).norm.add (hφi.const_mul δ)) hp
  have he : (∫ y : ℝ, ‖f y-g y‖+δ*φ y) =
      (∫ y : ℝ, ‖f y-g y‖)+(∫ y : ℝ, δ*φ y) :=
    integral_add (show Integrable (fun y => ‖f y-g y‖) from (hf.sub hgi).norm) (hφi.const_mul δ)
  change (∫ y : ℝ, ‖f y-G y‖) ≤ ∫ y : ℝ, ‖f y-g y‖+δ*φ y at H
  rw [he, integral_const_mul] at H
  apply H.trans
  have hd : δ*(∫ y : ℝ, φ y) ≤ ε/2 := by
    dsimp [δ]
    rw [div_mul_eq_mul_div]
    apply (div_le_iff₀ (by positivity : 0 < 2*((∫ y : ℝ, φ y)+1))).mpr
    nlinarith only [hε.le]
  linarith only [H, herr, hd]

/-- Positive compact continuous approximation with both almost-everywhere
convergence and convergence of the actual masses. No positive target mass is
assumed, so the zero-mass case is included. -/
theorem exists_positive_compact_approximation_seq {f : ℝ → ℝ} (hf : Integrable f)
    (hn : ∀ y, 0 ≤ f y) :
    ∃ g : ℕ → ℝ → ℝ,
      (∀ n, Continuous (g n)) ∧ (∀ n, HasCompactSupport (g n)) ∧
      (∀ n y, 0 ≤ g n y) ∧ (∀ n, 0 < ∫ y : ℝ, g n y) ∧
      (∀ᵐ y : ℝ, Filter.Tendsto (fun n => g n y) Filter.atTop (𝓝 (f y))) ∧
      Filter.Tendsto (fun n => ∫ y : ℝ, g n y) Filter.atTop (𝓝 (∫ y : ℝ, f y)) := by
  choose g hgc hgs hgn hgm hgerr using fun n : ℕ =>
    exists_positive_compact_approximation hf hn
      (by positivity : 0 < ((n:ℝ)+1)⁻¹)
  have hgi : ∀ n, Integrable (g n) := fun n => (hgc n).integrable_of_hasCompactSupport (hgs n)
  have hreal : Filter.Tendsto (fun n => ∫ y : ℝ, ‖g n y-f y‖) Filter.atTop (𝓝 (0:ℝ)) := by
    apply squeeze_zero (fun n => integral_nonneg (fun _ => norm_nonneg _))
      (fun n => by simpa only [norm_sub_rev] using hgerr n)
    exact tendsto_inv_atTop_zero.comp
      (Filter.tendsto_atTop_add_const_right _ _ tendsto_natCast_atTop_atTop)
  have hLp : Filter.Tendsto (fun n => eLpNorm (g n-f) 1) Filter.atTop (𝓝 0) := by
    have H := ENNReal.continuous_ofReal.tendsto (0:ℝ) |>.comp hreal
    simp only [ENNReal.ofReal_zero] at H
    convert H using 1
    funext n
    rw [eLpNorm_one_eq_lintegral_enorm]
    exact (ofReal_integral_norm_eq_lintegral_enorm ((hgi n).sub hf)).symm
  have hinmeasure := tendstoInMeasure_of_tendsto_eLpNorm (by norm_num : (1:ENNReal) ≠ 0)
    (fun n => (hgi n).aestronglyMeasurable) hf.aestronglyMeasurable hLp
  obtain ⟨ns,hns,hlim⟩ := hinmeasure.exists_seq_tendsto_ae
  refine ⟨fun n => g (ns n), (fun n => hgc (ns n)), (fun n => hgs (ns n)),
    (fun n => hgn (ns n)), (fun n => hgm (ns n)), hlim, ?_⟩
  exact (tendsto_integral_of_L1' f hf.aestronglyMeasurable
    (Filter.Eventually.of_forall hgi) hLp).comp hns.tendsto_atTop

/-- A common finite support radius for any finite family of compact data. -/
theorem exists_common_support_radius {ι : Type*} [Fintype ι]
    (g : ι → ℝ → ℝ) (hg : ∀ i, HasCompactSupport (g i)) :
    ∃ R : ℝ, 0 ≤ R ∧ ∀ i y, g i y ≠ 0 → |y| ≤ R := by
  choose r hr using fun i => (hg i).isBounded.exists_norm_le
  refine ⟨∑ i, |r i|, Finset.sum_nonneg (fun _ _ => abs_nonneg _), ?_⟩
  intro i y hy
  exact (hr i y (subset_tsupport (g i) hy)).trans
    ((le_abs_self _).trans (Finset.single_le_sum (fun j _ => abs_nonneg (r j)) (Finset.mem_univ i)))

/-- Fatou with converging upper bounds, retaining finiteness of the limiting
integral. The upper bounds may tend to zero. -/
theorem integrable_and_integral_le_of_nonneg_limit_bounds
    {α : Type*} [MeasurableSpace α] (μ : Measure α)
    (F : ℕ → α → ℝ) (g : α → ℝ) (C : ℕ → ℝ) (L : ℝ)
    (hF : ∀ n, Integrable (F n) μ) (hFn : ∀ n x, 0 ≤ F n x)
    (hg : AEStronglyMeasurable g μ) (hgn : ∀ x, 0 ≤ g x)
    (hlim : ∀ᵐ x ∂μ, Filter.Tendsto (fun n => F n x) Filter.atTop (𝓝 (g x)))
    (hbound : ∀ n, (∫ x, F n x ∂μ) ≤ C n)
    (hC : Filter.Tendsto C Filter.atTop (𝓝 L)) :
    Integrable g μ ∧ (∫ x, g x ∂μ) ≤ L := by
  have H : (∫⁻ x, ENNReal.ofReal (g x) ∂μ) ≤ ENNReal.ofReal L := by
    calc
      _ = ∫⁻ x, Filter.liminf (fun n => ENNReal.ofReal (F n x)) Filter.atTop ∂μ := by
        apply lintegral_congr_ae
        filter_upwards [hlim] with x hx
        exact ((ENNReal.continuous_ofReal.tendsto _).comp hx).liminf_eq.symm
      _ ≤ Filter.liminf (fun n => ∫⁻ x, ENNReal.ofReal (F n x) ∂μ) Filter.atTop :=
        lintegral_liminf_le' (fun n => (hF n).aestronglyMeasurable.aemeasurable.ennreal_ofReal)
      _ ≤ Filter.liminf (fun n => ENNReal.ofReal (C n)) Filter.atTop := by
        have Hn : ∀ n, (∫⁻ x, ENNReal.ofReal (F n x) ∂μ) ≤ ENNReal.ofReal (C n) := by
          intro n
          rw [← ofReal_integral_eq_lintegral_ofReal (hF n) (Filter.Eventually.of_forall (hFn n))]
          exact ENNReal.ofReal_le_ofReal (hbound n)
        exact Filter.liminf_le_liminf (Filter.Eventually.of_forall Hn)
      _ = _ := ((ENNReal.continuous_ofReal.tendsto _).comp hC).liminf_eq
  have hgi : Integrable g μ := ⟨hg, (hasFiniteIntegral_iff_ofReal
    (Filter.Eventually.of_forall hgn)).mpr (H.trans_lt ENNReal.ofReal_lt_top)⟩
  refine ⟨hgi, ?_⟩
  have hL : 0 ≤ L := ge_of_tendsto hC
    (Filter.Eventually.of_forall (fun n => (integral_nonneg (hFn n)).trans (hbound n)))
  rw [← ofReal_integral_eq_lintegral_ofReal hgi (Filter.Eventually.of_forall hgn)] at H
  exact (ENNReal.ofReal_le_ofReal_iff hL).mp H

section
variable {ι E : Type*} [Fintype ι] [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- Geometric Brascamp–Lieb on the whole plane for arbitrary nonnegative L1
data. Compact support, continuity, boundedness and positive mass are all removed;
zero masses and zero weights are included with the usual real-power convention. -/
theorem geometric_brascamp_lieb
    (f : ι → ℝ → ℝ) (c : ι → ℝ) (u : ι → E)
    (hf : ∀ i, Integrable (f i)) (hn : ∀ i y, 0 ≤ f i y)
    (hc : ∀ i, 0 ≤ c i) (hu : ∀ i, ‖u i‖ = 1) (hframe : IsWeightedFrame c u)
    (b : OrthonormalBasis (Fin 2) ℝ E) :
    Integrable (fun z : ℝ × ℝ => ∏ i, f i ⟪u i,planePoint b z⟫ ^ c i) (volume.prod volume) ∧
    (∫ z : ℝ × ℝ, ∏ i, f i ⟪u i,planePoint b z⟫ ^ c i ∂volume.prod volume) ≤
      ∏ i, (∫ y : ℝ, f i y) ^ c i := by
  choose g hgc hgs hgn hgm hglim hgmass using fun i =>
    exists_positive_compact_approximation_seq (hf i) (hn i)
  let F : ℕ → ℝ × ℝ → ℝ := fun n z => ∏ i, g i n ⟪u i,planePoint b z⟫ ^ c i
  let G : ℝ × ℝ → ℝ := fun z => ∏ i, f i ⟪u i,planePoint b z⟫ ^ c i
  let C : ℕ → ℝ := fun n => ∏ i, (∫ y : ℝ, g i n y) ^ c i
  have hFc : ∀ n, Continuous (F n) := by
    intro n
    apply continuous_finsetProd
    intro i _
    exact (continuous_rpow_const (hc i)).comp ((hgc i n).comp
      (continuous_const.inner (continuous_planePoint b)))
  have hFbound : ∀ n, Integrable (F n) (volume.prod volume) ∧
      (∫ z : ℝ × ℝ, F n z ∂volume.prod volume) ≤ C n := by
    intro n
    obtain ⟨R,hR,hRs⟩ := exists_common_support_radius (fun i => g i n) (fun i => hgs i n)
    exact geometric_brascamp_lieb_continuous_compact (fun i => g i n) c u (fun i => hgc i n)
      (fun i => hgn i n) (fun i => hgm i n) hc hu hframe R hR hRs b
  have hlim : ∀ᵐ z : ℝ × ℝ ∂volume.prod volume,
      Filter.Tendsto (fun n => F n z) Filter.atTop (𝓝 (G z)) := by
    have H : ∀ᵐ z : ℝ × ℝ ∂volume.prod volume, ∀ i,
        Filter.Tendsto (fun n => g i n ⟪u i,planePoint b z⟫) Filter.atTop
          (𝓝 (f i ⟪u i,planePoint b z⟫)) := by
      rw [ae_all_iff]
      intro i
      exact ae_plane_inner b (u i) (by intro hi; simpa [hi] using hu i) (hglim i)
    filter_upwards [H] with z hz
    exact tendsto_finsetProd _ (fun i _ => (hz i).rpow_const (Or.inr (hc i)))
  have hGmeas : AEStronglyMeasurable G (volume.prod volume) :=
    aestronglyMeasurable_of_tendsto_ae _ (fun n => (hFc n).aestronglyMeasurable) hlim
  exact integrable_and_integral_le_of_nonneg_limit_bounds (volume.prod volume) F G C _
    (fun n => (hFbound n).1)
    (fun n z => Finset.prod_nonneg (fun i _ => rpow_nonneg (hgn i n _) _))
    hGmeas (fun z => Finset.prod_nonneg (fun i _ => rpow_nonneg (hn i _) _)) hlim
    (fun n => (hFbound n).2)
    (tendsto_finsetProd _ (fun i _ => (hgmass i).rpow_const (Or.inr (hc i))))

end
end ChowlaCosine.Beckner
