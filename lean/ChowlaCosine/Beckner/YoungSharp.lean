import ChowlaCosine.Beckner.YoungFrame
import ChowlaCosine.Beckner.Young

/-! # Sharp Young from the explicit geometric Brascamp–Lieb frame -/

open MeasureTheory Real
open scoped BigOperators Topology RealInnerProductSpace ENNReal NNReal

namespace ChowlaCosine.Beckner
set_option backward.isDefEq.respectTransparency.types false
set_option maxHeartbeats 1000000

/-- The physical two-coordinate map used in the Young substitution. -/
noncomputable def youngFrameMap (a b d : ℝ) : (ℝ × ℝ) →ₗ[ℝ] (ℝ × ℝ) :=
  Matrix.toLin (Module.Basis.finTwoProd ℝ) (Module.Basis.finTwoProd ℝ) (youngFrameMatrix a b d)

/-- The linear map has exactly the already computed matrix determinant. -/
theorem youngFrameMap_det (a b d : ℝ) :
    LinearMap.det (youngFrameMap a b d) = (youngFrameMatrix a b d).det :=
  LinearMap.det_toLin _ _

/-- Invertible planar substitution preserves integrability and keeps the exact
Jacobian in the ordinary Bochner integral, without extra measurability assumptions. -/
theorem plane_linear_change (L : (ℝ × ℝ) →ₗ[ℝ] (ℝ × ℝ))
    (hL : 0 < LinearMap.det L) (H : ℝ × ℝ → ℝ) :
    (Integrable (fun z => H (L z)) (volume.prod volume) ↔
      Integrable H (volume.prod volume)) ∧
    (∫ z, H (L z) ∂volume.prod volume) =
      (LinearMap.det L)⁻¹ * (∫ z, H z ∂volume.prod volume) := by
  let μ : Measure (ℝ × ℝ) := volume.prod volume
  let e := (L.equivOfDetNeZero hL.ne').toContinuousLinearEquiv.toHomeomorph.toMeasurableEquiv
  have hm : Measure.map e μ = ENNReal.ofReal (LinearMap.det L)⁻¹ • μ := by
    change Measure.map L μ = _
    rw [Measure.map_linearMap_addHaar_eq_smul_addHaar μ hL.ne', abs_of_pos (inv_pos.mpr hL)]
  constructor
  · have hi := integrable_map_equiv (μ := μ) e H
    rw [hm, integrable_smul_measure (by positivity) ENNReal.ofReal_ne_top] at hi
    exact hi.symm
  · have hi := (integral_map_equiv (μ := μ) e H).symm
    rw [hm, integral_smul_measure, ENNReal.toReal_ofReal (by positivity)] at hi
    exact hi

/-- The first two scaled frame forms are exactly the physical map coordinates. -/
theorem youngFrameMap_apply {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    (basis : OrthonormalBasis (Fin 2) ℝ E) (a b d : ℝ) (z : ℝ × ℝ) :
    youngFrameMap a b d z =
      (youngFrameScale a b d 0 * ⟪youngFrame basis a b d 0,planePoint basis z⟫,
       youngFrameScale a b d 1 * ⟪youngFrame basis a b d 1,planePoint basis z⟫) := by
  rw [youngFrameMap, youngFrameMatrix, Matrix.toLin_finTwoProd_apply]
  simp only [youngFrame, planePoint, inner_add_left, inner_add_right,
    real_inner_smul_left, real_inner_smul_right, basis.inner_eq_ite]
  norm_num
  constructor <;> ring

/-- The third physical argument is minus the sum of the first two. -/
theorem youngFrameMap_third {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    (basis : OrthonormalBasis (Fin 2) ℝ E) (a b d : ℝ)
    (ha : 0 < a) (hb : 0 < b) (hd : 0 < d) (z : ℝ × ℝ) :
    youngFrameScale a b d 2 * ⟪youngFrame basis a b d 2,planePoint basis z⟫ =
      -((youngFrameMap a b d z).1+(youngFrameMap a b d z).2) := by
  have h := congrArg (fun v => ⟪v,planePoint basis z⟫) (youngFrame_relation basis a b d ha hb hd)
  simp only [Fin.sum_univ_three, inner_add_left, real_inner_smul_left, inner_zero_left] at h
  rw [youngFrameMap_apply basis]
  dsimp only
  linarith only [h]

/-- Sharp trilinear Young for arbitrary nonnegative data at every interior
triple, in integral-power form. Integrability of the physical product is part
of the conclusion; no support, boundedness, or positive-mass assumption occurs. -/
theorem young_trilinear_complement (a b d : ℝ)
    (ha : 0 < a) (hb : 0 < b) (hd : 0 < d) (hsum : a+b+d=1)
    (g : Fin 3 → ℝ → ℝ) (hn : ∀ i x, 0 ≤ g i x)
    (hg : ∀ i, Integrable (fun x => g i x ^ (1/youngFrameWeights a b d i))) :
    Integrable (fun z : ℝ × ℝ => g 0 z.1*g 1 z.2*g 2 (-(z.1+z.2)))
      (volume.prod volume) ∧
    (∫ z : ℝ × ℝ, g 0 z.1*g 1 z.2*g 2 (-(z.1+z.2)) ∂volume.prod volume) ≤
      (∏ i, sqrt ((1/youngFrameWeights a b d i)^youngFrameWeights a b d i /
        (1/youngFrameComplement a b d i)^youngFrameComplement a b d i)) *
      ∏ i, (∫ x : ℝ, g i x ^ (1/youngFrameWeights a b d i)) ^
        youngFrameWeights a b d i := by
  let basis := EuclideanSpace.basisFun (Fin 2) ℝ
  let c := youngFrameWeights a b d
  let α := youngFrameScale a b d
  let L := youngFrameMap a b d
  let H : ℝ × ℝ → ℝ := fun z => g 0 z.1*g 1 z.2*g 2 (-(z.1+z.2))
  have hc : ∀ i, 0 < c i := by
    intro i
    fin_cases i <;> simp [c, youngFrameWeights] <;> positivity
  have hα : ∀ i, 0 < α i := by
    intro i
    fin_cases i <;> simp [α, youngFrameScale] <;> positivity
  have hL : 0 < LinearMap.det L := by
    dsimp [L]
    rw [youngFrameMap_det, youngFrameMatrix_det a b d ha hb hd]
    positivity
  let F : Fin 3 → ℝ → ℝ := fun i s => g i (α i*s) ^ (1/c i)
  have hFi : ∀ i, Integrable (F i) := fun i => (hg i).comp_mul_left' (hα i).ne'
  have hFn : ∀ i s, 0 ≤ F i s := fun i s => rpow_nonneg (hn i _) _
  obtain ⟨hprod,hbound⟩ := geometric_brascamp_lieb_youngFrame basis a b d ha hb hd hsum F hFi hFn
  have hpoint : ∀ z : ℝ × ℝ,
      (∏ i, F i ⟪youngFrame basis a b d i,planePoint basis z⟫ ^ c i) = H (L z) := by
    intro z
    have he : ∀ i, F i ⟪youngFrame basis a b d i,planePoint basis z⟫ ^ c i =
        g i (α i * ⟪youngFrame basis a b d i,planePoint basis z⟫) := by
      intro i
      dsimp [F]
      rw [← rpow_mul (hn i _), one_div_mul_cancel (hc i).ne', rpow_one]
    rw [Finset.prod_congr rfl (fun i _ => he i), Fin.prod_univ_three]
    dsimp only [H, L]
    rw [← youngFrameMap_third basis a b d ha hb hd]
    rw [youngFrameMap_apply basis]
  change Integrable (fun z => ∏ i,
    F i ⟪youngFrame basis a b d i,planePoint basis z⟫ ^ c i) (volume.prod volume) at hprod
  change (∫ z, ∏ i, F i ⟪youngFrame basis a b d i,planePoint basis z⟫ ^ c i
    ∂volume.prod volume) ≤ ∏ i, (∫ s, F i s)^c i at hbound
  have hpull : Integrable (fun z => H (L z)) (volume.prod volume) := by
    simpa only [hpoint] using hprod
  obtain ⟨hiff,hchange⟩ := plane_linear_change L hL H
  refine ⟨hiff.mp hpull, ?_⟩
  have hmass : ∀ i, (∫ s : ℝ, F i s) =
      (α i)⁻¹ * (∫ x : ℝ, g i x ^ (1/c i)) := by
    intro i
    simpa only [abs_of_pos (inv_pos.mpr (hα i)), smul_eq_mul] using
      Measure.integral_comp_mul_left (fun x => g i x ^ (1/c i)) (α i)
  have hrhs : (∏ i, (∫ s : ℝ, F i s)^c i) =
      (∏ i, α i ^ c i)⁻¹ * ∏ i, (∫ x : ℝ, g i x ^ (1/c i))^c i := by
    simp_rw [hmass, mul_rpow (inv_nonneg.mpr (hα _).le)
      (integral_nonneg (fun x => rpow_nonneg (hn _ x) _)), inv_rpow (hα _).le]
    rw [Finset.prod_mul_distrib, Finset.prod_inv_distrib]
  have hbound' : (LinearMap.det L)⁻¹ * (∫ z, H z ∂volume.prod volume) ≤
      (∏ i, α i ^ c i)⁻¹ * ∏ i, (∫ x : ℝ, g i x ^ (1/c i))^c i := by
    rw [← hchange, ← hrhs]
    simpa only [hpoint] using hbound
  have hm := mul_le_mul_of_nonneg_left hbound' hL.le
  rw [← mul_assoc, mul_inv_cancel₀ hL.ne', one_mul] at hm
  change (∫ z, H z ∂volume.prod volume) ≤ _
  calc
    _ ≤ (LinearMap.det L * (∏ i, α i ^ c i)⁻¹) *
        ∏ i, (∫ x : ℝ, g i x ^ (1/c i))^c i := by simpa only [mul_assoc] using hm
    _ = _ := by
      rw [← div_eq_mul_inv, show LinearMap.det L = (youngFrameMatrix a b d).det from
        youngFrameMap_det a b d, youngFrame_sharp_factor a b d ha hb hd hsum]

/-- Beckner's `A_p`, parametrized by the reciprocal exponent `c=1/p`.
This definition includes `p=∞` (`c=0`) and `p=1` (`c=1`). -/
noncomputable def becknerFactor (c : ℝ) : ℝ :=
  sqrt ((1/c)^c / (1/(1-c))^(1-c))

/-- Sharp trilinear Young expressed in actual Lp norms. -/
theorem young_trilinear_interior (c₀ c₁ c₂ : ℝ)
    (h₀ : 0 < c₀) (h₁ : 0 < c₁) (h₂ : 0 < c₂)
    (h₀' : c₀ < 1) (h₁' : c₁ < 1) (h₂' : c₂ < 1) (hsum : c₀+c₁+c₂=2)
    (g : Fin 3 → ℝ → ℝ) (hn : ∀ i x, 0 ≤ g i x)
    (hg : ∀ i, MemLp (g i) (ENNReal.ofReal (1/(![c₀,c₁,c₂] i)))) :
    Integrable (fun z : ℝ × ℝ => g 0 z.1*g 1 z.2*g 2 (-(z.1+z.2)))
      (volume.prod volume) ∧
    (∫ z : ℝ × ℝ, g 0 z.1*g 1 z.2*g 2 (-(z.1+z.2)) ∂volume.prod volume) ≤
      (becknerFactor c₀ * becknerFactor c₁ * becknerFactor c₂) *
      (lpNorm (g 0) (ENNReal.ofReal (1/c₀)) volume *
        lpNorm (g 1) (ENNReal.ofReal (1/c₁)) volume * lpNorm (g 2) (ENNReal.ofReal (1/c₂)) volume) := by
  let c : Fin 3 → ℝ := ![c₀,c₁,c₂]
  have hc : ∀ i, 0 < c i := by intro i; fin_cases i <;> assumption
  have hweights : youngFrameWeights (1-c₀) (1-c₁) (1-c₂) = c := by
    ext i
    fin_cases i <;> simp [youngFrameWeights, c] <;> linarith only [hsum]
  have hcomplement : ∀ i, youngFrameComplement (1-c₀) (1-c₁) (1-c₂) i = 1-c i := by
    intro i
    fin_cases i <;> rfl
  have hpower : ∀ i, Integrable (fun x => g i x ^ (1/c i)) := by
    intro i
    have hgi : MemLp (g i) (ENNReal.ofReal (1/c i)) := hg i
    have H := hgi.integrable_norm_rpow (ENNReal.ofReal_ne_zero_iff.mpr (one_div_pos.mpr (hc i)))
      ENNReal.ofReal_ne_top
    simpa only [ENNReal.toReal_ofReal ((one_div_pos.mpr (hc i)).le : 0 ≤ 1/c i),
      Real.norm_of_nonneg (hn i _)] using H
  obtain ⟨hi,hbound⟩ := young_trilinear_complement (1-c₀) (1-c₁) (1-c₂)
    (by linarith) (by linarith) (by linarith) (by linarith) g hn (by simpa only [hweights] using hpower)
  refine ⟨hi, ?_⟩
  have hnorm : ∀ i, (∫ x : ℝ, g i x ^ (1/c i)) ^ c i =
      lpNorm (g i) (ENNReal.ofReal (1/c i)) volume := by
    intro i
    rw [lpNorm_eq_integral_norm_rpow_toReal (ENNReal.ofReal_ne_zero_iff.mpr (one_div_pos.mpr (hc i)) : ENNReal.ofReal (1/c i) ≠ 0)
      ENNReal.ofReal_ne_top (hg i).aestronglyMeasurable]
    rw [ENNReal.toReal_ofReal (one_div_pos.mpr (hc i)).le]
    simp only [one_div, inv_inv, Real.norm_of_nonneg (hn i _)]
  simp only [hweights, hcomplement] at hbound
  simp_rw [hnorm] at hbound
  simpa [becknerFactor, Fin.prod_univ_three, c] using hbound

/-- The convolution of norms belongs to Lr under the full finite Young
hypotheses. This uses only the already established constant-one inequality. -/
theorem memLp_normConvolution {p q r : ℝ}
    (hp : 1 ≤ p) (hq : 1 ≤ q) (hr : 1 ≤ r)
    (hexp : 1/p+1/q=1+1/r) {f g : ℝ → ℂ}
    (hf : MemLp f (ENNReal.ofReal p)) (hg : MemLp g (ENNReal.ofReal q)) :
    MemLp (normConvolution f g) (ENNReal.ofReal r) := by
  let F : ℝ → ℂ := fun x => (‖f x‖ : ℂ)
  let G : ℝ → ℂ := fun x => (‖g x‖ : ℂ)
  have hF : MemLp F (ENNReal.ofReal p) :=
    hf.congr_norm (Complex.continuous_ofReal.comp_aestronglyMeasurable hf.1.norm)
      (Filter.Eventually.of_forall (fun x => by simp [F]))
  have hG : MemLp G (ENNReal.ofReal q) :=
    hg.congr_norm (Complex.continuous_ofReal.comp_aestronglyMeasurable hg.1.norm)
      (Filter.Eventually.of_forall (fun x => by simp [G]))
  have he : ∀ x, convolution F G x = (normConvolution f g x : ℂ) := by
    intro x
    simp only [convolution, F, G, ← Complex.ofReal_mul, integral_complex_ofReal, normConvolution]
  have hC : AEStronglyMeasurable (normConvolution f g) := by
    have H := (hf.1.norm.convolution_integrand (ContinuousLinearMap.mul ℝ ℝ) hg.1.norm).integral_prod_right'
    simpa only [ContinuousLinearMap.mul_apply', normConvolution, Prod.fst, Prod.snd] using! H
  exact (young_finite p q r hp hq hr hexp F G hF hG).1.congr_norm hC
    (Filter.Eventually.of_forall (fun x => by rw [he]; exact Complex.norm_real _))

/-- Recover the rth root after testing a nonnegative Lr function against its
(r-1) power. Zero mass is included. -/
theorem young_power_cancel {T K r : ℝ} (hT : 0 ≤ T) (hK : 0 ≤ K) (hr : 0 < r)
    (h : T ≤ K*T^(1-1/r)) : T^(1/r) ≤ K := by
  rcases hT.eq_or_lt with hT | hT
  · subst T
    simpa only [zero_rpow (one_div_pos.mpr hr).ne'] using hK
  · have he : T^(1/r)*T^(1-1/r) = T := by
      rw [← rpow_add hT, show 1/r+(1-1/r)=1 by ring, rpow_one]
    apply (mul_le_mul_iff_left₀ (rpow_pos_of_pos hT (1-1/r))).mp
    rwa [he]

/-- Sharp interior Young for the convolution of norms. The non-sharp
inequality supplies membership; the exact trilinear inequality supplies the
Beckner constant, including the zero-norm cases. -/
theorem sharp_young_normConvolution_interior {p q r : ℝ}
    (hp : 1 < p) (hq : 1 < q) (hr : 1 < r)
    (hexp : 1/p+1/q=1+1/r) {f g : ℝ → ℂ}
    (hf : MemLp f (ENNReal.ofReal p)) (hg : MemLp g (ENNReal.ofReal q)) :
    lpNorm (normConvolution f g) (ENNReal.ofReal r) volume ≤
      (becknerFactor (1/p)*becknerFactor (1/q)*becknerFactor (1-1/r)) *
      (lpNorm f (ENNReal.ofReal p) volume * lpNorm g (ENNReal.ofReal q) volume) := by
  have hp0 : 0 < p := by linarith
  have hq0 : 0 < q := by linarith
  have hr0 : 0 < r := by linarith
  have hc₂ : 0 < 1-1/r := sub_pos.mpr ((div_lt_one hr0).mpr hr)
  have hC := memLp_normConvolution hp.le hq.le hr.le hexp hf hg
  let C := normConvolution f g
  let T : ℝ := ∫ x : ℝ, C x ^ r
  let s : ℝ := 1/(1-1/r)
  let H : ℝ → ℝ := fun x => C (-x) ^ (r-1)
  have hCn : ∀ x, 0 ≤ C x := normConvolution_nonneg f g
  have hT : 0 ≤ T := integral_nonneg (fun x => rpow_nonneg (hCn x) _)
  have hCi : Integrable (fun x => C x ^ r) := by
    have hi := hC.integrable_norm_rpow (ENNReal.ofReal_ne_zero_iff.mpr hr0) ENNReal.ofReal_ne_top
    change Integrable (fun x => ‖C x‖ ^ (ENNReal.ofReal r).toReal) at hi
    simpa only [ENNReal.toReal_ofReal hr0.le, Real.norm_of_nonneg (hCn _)] using hi
  have hs : 0 < s := one_div_pos.mpr hc₂
  have hex : (r-1)*s=r := by
    dsimp [s]
    rw [mul_one_div, div_eq_iff hc₂.ne']
    field_simp
  have hHn : ∀ x, 0 ≤ H x := fun x => rpow_nonneg (hCn _) _
  have hHp : ∀ x, H x ^ s = C (-x)^r := by
    intro x
    dsimp [H]
    rw [← rpow_mul (hCn _), hex]
  have hHm : AEStronglyMeasurable H :=
    (((hC.1.comp_measurePreserving (Measure.measurePreserving_neg volume)).aemeasurable).pow_const
      (r-1)).aestronglyMeasurable
  have hHi : Integrable (fun x => H x ^ s) := by
    simpa only [hHp] using hCi.comp_neg
  have hH : MemLp H (ENNReal.ofReal s) := by
    apply (integrable_norm_rpow_iff hHm (ENNReal.ofReal_ne_zero_iff.mpr hs) ENNReal.ofReal_ne_top).mp
    simpa only [ENNReal.toReal_ofReal hs.le, Real.norm_of_nonneg (hHn _)] using hHi
  have hHnorm : lpNorm H (ENNReal.ofReal s) volume = T^(1-1/r) := by
    rw [lpNorm_eq_integral_norm_rpow_toReal (ENNReal.ofReal_ne_zero_iff.mpr hs)
      ENNReal.ofReal_ne_top hHm, ENNReal.toReal_ofReal hs.le]
    simp_rw [Real.norm_of_nonneg (hHn _), hHp]
    rw [integral_neg_eq_self (fun x => C x ^ r)]
    congr 1
    dsimp [s]
    simp
  let k : Fin 3 → ℝ → ℝ := ![fun x => ‖f x‖, fun x => ‖g x‖, H]
  have hkn : ∀ i x, 0 ≤ k i x := by
    intro i x
    fin_cases i <;> simp only [k, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two]
    · exact norm_nonneg _
    · exact norm_nonneg _
    · exact hHn x
  have hki : ∀ i, MemLp (k i) (ENNReal.ofReal (1/(![1/p,1/q,1-1/r] i))) := by
    intro i
    fin_cases i
    · simpa [k] using hf.norm
    · simpa [k] using hg.norm
    · simpa [k, s] using hH
  obtain ⟨hprod,hbound⟩ := young_trilinear_interior (1/p) (1/q) (1-1/r)
    (by positivity) (by positivity) hc₂ ((div_lt_one hp0).mpr hp)
    ((div_lt_one hq0).mpr hq) (by have := one_div_pos.mpr hr0; linarith)
    (by linarith only [hexp]) k hkn hki
  let P : ℝ × ℝ → ℝ := fun z => ‖f z.1‖*‖g z.2‖*C (z.1+z.2)^(r-1)
  have hPi : Integrable P (volume.prod volume) := by
    simpa [P, k, H] using hprod
  let e : ℝ × ℝ → ℝ × ℝ := fun z => (z.2,z.1-z.2)
  have he : MeasurePreserving e (volume.prod volume) (volume.prod volume) :=
    measurePreserving_prod_sub_swap volume volume
  have hPe : Integrable (P ∘ e) (volume.prod volume) := he.integrable_comp_of_integrable hPi
  have hchange : (∫ z, P (e z) ∂volume.prod volume) = ∫ z, P z ∂volume.prod volume := by
    apply he.integral_comp
    exact ((MeasurableEquiv.prodComm : ℝ × ℝ ≃ᵐ ℝ × ℝ).trans (MeasurableEquiv.shearSubRight ℝ)).measurableEmbedding
  have htest : (∫ z, P z ∂volume.prod volume) = T := by
    rw [← hchange]
    change (∫ z, (P ∘ e) z ∂volume.prod volume) = T
    rw [integral_prod _ hPe]
    have hinner : ∀ x, (∫ y, P (e (x,y))) = C x ^ r := by
      intro x
      simp only [P, e, add_sub_cancel_left]
      simp_rw [show ∀ y : ℝ, y+(x-y)=x from fun y => by ring]
      rw [integral_mul_const]
      change C x * C x ^ (r-1) = C x ^ r
      calc
        C x * C x ^ (r-1) = C x ^ ((1:ℝ)+(r-1)) := by
          rw [rpow_add' (hCn x) (by linarith : (1:ℝ)+(r-1) ≠ 0), rpow_one]
        _ = _ := by congr 1; ring
    simp only [Function.comp_apply, hinner]
    rfl
  have htestbound : T ≤
      ((becknerFactor (1/p)*becknerFactor (1/q)*becknerFactor (1-1/r)) *
        (lpNorm f (ENNReal.ofReal p) volume * lpNorm g (ENNReal.ofReal q) volume)) * T^(1-1/r) := by
    simp only [show k 0 = (fun x => ‖f x‖) from rfl,
      show k 1 = (fun x => ‖g x‖) from rfl, show k 2 = H from rfl,
      one_div, inv_inv] at hbound
    have hHnorm' : lpNorm H (ENNReal.ofReal ((1-r⁻¹)⁻¹)) volume = T^(1-1/r) := by
      simpa only [s, one_div] using hHnorm
    rw [hHnorm', lpNorm_norm hf.1, lpNorm_norm hg.1] at hbound
    have heq : (fun z : ℝ × ℝ => ‖f z.1‖*‖g z.2‖*H (-(z.1+z.2))) = P := by
      ext z
      simp only [H, neg_neg, P]
    rw [heq, htest] at hbound
    simpa only [mul_assoc, one_div] using hbound
  have hK : 0 ≤ (becknerFactor (1/p)*becknerFactor (1/q)*becknerFactor (1-1/r)) *
      (lpNorm f (ENNReal.ofReal p) volume * lpNorm g (ENNReal.ofReal q) volume) :=
    mul_nonneg (by unfold becknerFactor; positivity) (mul_nonneg lpNorm_nonneg lpNorm_nonneg)
  have hout := young_power_cancel hT hK hr0 htestbound
  change lpNorm C (ENNReal.ofReal r) volume ≤ _
  rw [lpNorm_eq_integral_norm_rpow_toReal (f := C) (ENNReal.ofReal_ne_zero_iff.mpr hr0)
    ENNReal.ofReal_ne_top hC.1, ENNReal.toReal_ofReal hr0.le]
  simpa only [Real.norm_of_nonneg (hCn _), one_div] using hout

@[simp] theorem becknerFactor_zero : becknerFactor 0 = 1 := by norm_num [becknerFactor]
@[simp] theorem becknerFactor_one : becknerFactor 1 = 1 := by norm_num [becknerFactor]

/-- Conjugate exponents have reciprocal Beckner factors, including both
boundary exponents. -/
theorem becknerFactor_mul_complement {c : ℝ} (hc : 0 ≤ c) (hc1 : c ≤ 1) :
    becknerFactor c * becknerFactor (1-c) = 1 := by
  rcases hc.eq_or_lt with hc | hc
  · subst c
    simp
  rcases hc1.eq_or_lt with hc1 | hc1
  · subst c
    simp
  have hd : 0 < 1-c := sub_pos.mpr hc1
  have hX : 0 < (1/c)^c := rpow_pos_of_pos (one_div_pos.mpr hc) _
  have hY : 0 < (1/(1-c))^(1-c) := rpow_pos_of_pos (one_div_pos.mpr hd) _
  unfold becknerFactor
  rw [show 1-(1-c)=c by ring, ← sqrt_mul (div_pos hX hY).le,
    div_mul_div_cancel₀ hY.ne', div_self hX.ne', sqrt_one]

/-- Sharp Young on R for every interior finite triple, arbitrary complex Lp
functions, in the actual extended Lp seminorm. -/
theorem sharp_young_finite_interior {p q r : ℝ}
    (hp : 1 < p) (hq : 1 < q) (hr : 1 < r)
    (hexp : 1/p+1/q=1+1/r) {f g : ℝ → ℂ}
    (hf : MemLp f (ENNReal.ofReal p)) (hg : MemLp g (ENNReal.ofReal q)) :
    MemLp (convolution f g) (ENNReal.ofReal r) ∧
    eLpNorm (convolution f g) (ENNReal.ofReal r) ≤
      ENNReal.ofReal (becknerFactor (1/p)*becknerFactor (1/q)*becknerFactor (1-1/r)) *
      eLpNorm f (ENNReal.ofReal p) * eLpNorm g (ENNReal.ofReal q) := by
  refine ⟨(young_finite p q r hp.le hq.le hr.le hexp f g hf hg).1, ?_⟩
  have hC := memLp_normConvolution hp.le hq.le hr.le hexp hf hg
  calc
    _ ≤ eLpNorm (normConvolution f g) (ENNReal.ofReal r) volume :=
      eLpNorm_convolution_le_normConvolution f g (ENNReal.ofReal r)
    _ = ENNReal.ofReal (lpNorm (normConvolution f g) (ENNReal.ofReal r) volume) :=
      (ofReal_lpNorm hC).symm
    _ ≤ ENNReal.ofReal ((becknerFactor (1/p)*becknerFactor (1/q)*becknerFactor (1-1/r)) *
        (lpNorm f (ENNReal.ofReal p) volume * lpNorm g (ENNReal.ofReal q) volume)) :=
      ENNReal.ofReal_le_ofReal (sharp_young_normConvolution_interior hp hq hr hexp hf hg)
    _ = _ := by
      have hK : 0 ≤ becknerFactor (1/p)*becknerFactor (1/q)*becknerFactor (1-1/r) := by
        unfold becknerFactor
        positivity
      have hF : 0 ≤ lpNorm f (ENNReal.ofReal p) volume := lpNorm_nonneg
      calc
        _ = ENNReal.ofReal (becknerFactor (1/p)*becknerFactor (1/q)*becknerFactor (1-1/r)) *
            ENNReal.ofReal (lpNorm f (ENNReal.ofReal p) volume * lpNorm g (ENNReal.ofReal q) volume) :=
          ENNReal.ofReal_mul hK
        _ = _ := by
          exact (congrArg (fun t => ENNReal.ofReal
            (becknerFactor (1/p)*becknerFactor (1/q)*becknerFactor (1-1/r)) * t)
            ((ENNReal.ofReal_mul hF).trans (congrArg₂ (fun x y : ℝ≥0∞ => x*y)
              (ofReal_lpNorm hf) (ofReal_lpNorm hg)))).trans (mul_assoc _ _ _).symm

/-- Sharp Young on R for all finite admissible exponent triples, including
L1 input and output endpoints. -/
theorem sharp_young_finite {p q r : ℝ}
    (hp : 1 ≤ p) (hq : 1 ≤ q) (hr : 1 ≤ r)
    (hexp : 1/p+1/q=1+1/r) {f g : ℝ → ℂ}
    (hf : MemLp f (ENNReal.ofReal p)) (hg : MemLp g (ENNReal.ofReal q)) :
    MemLp (convolution f g) (ENNReal.ofReal r) ∧
    eLpNorm (convolution f g) (ENNReal.ofReal r) ≤
      ENNReal.ofReal (becknerFactor (1/p)*becknerFactor (1/q)*becknerFactor (1-1/r)) *
      eLpNorm f (ENNReal.ofReal p) * eLpNorm g (ENNReal.ofReal q) := by
  have hp0 : 0 < p := by linarith
  have hq0 : 0 < q := by linarith
  have hr0 : 0 < r := by linarith
  by_cases hp1 : p = 1
  · have hqr : q = r := by
      have hi : 1/q=1/r := by simp only [hp1, div_one] at hexp; linarith only [hexp]
      field_simp at hi
      linarith only [hi]
    subst p
    subst r
    have he : becknerFactor (1/q)*becknerFactor (1-1/q)=1 :=
      becknerFactor_mul_complement (by positivity) ((div_le_one₀ hq0).mpr hq)
    simpa only [div_one, becknerFactor_one, one_mul, he, ENNReal.ofReal_one] using
      young_finite 1 q q (by rfl) hq hq (by simp) f g hf hg
  by_cases hq1 : q = 1
  · have hpr : p = r := by
      have hi : 1/p=1/r := by simp only [hq1, div_one] at hexp; linarith only [hexp]
      field_simp at hi
      linarith only [hi]
    subst q
    subst r
    have he : becknerFactor (1/p)*becknerFactor (1-1/p)=1 :=
      becknerFactor_mul_complement (by positivity) ((div_le_one₀ hp0).mpr hp)
    simpa only [div_one, becknerFactor_one, mul_one, he, ENNReal.ofReal_one, one_mul] using
      young_finite p 1 p hp (by rfl) hp (by simp [add_comm]) f g hf hg
  have hpp : 1 < p := lt_of_le_of_ne hp (Ne.symm hp1)
  have hqp : 1 < q := lt_of_le_of_ne hq (Ne.symm hq1)
  have hrp : 1 < r := by
    have hi : 1/r < 1 := by
      have := (div_lt_one hp0).mpr hpp
      have := (div_lt_one hq0).mpr hqp
      linarith only [hexp, this, ‹1/p < 1›]
    exact (div_lt_one hr0).mp hi
  exact sharp_young_finite_interior hpp hqp hrp hexp hf hg

/-- Beckner's factor for an extended exponent, with `A₁=A∞=1`. -/
noncomputable def becknerA (p : ℝ≥0∞) : ℝ := becknerFactor p⁻¹.toReal

/-- The full extended-exponent inequality, including every infinity endpoint. -/
theorem sharp_young_ennreal {p q r : ℝ≥0∞}
    (hp : 1 ≤ p) (hq : 1 ≤ q) (hr : 1 ≤ r)
    (hexp : p⁻¹+q⁻¹=1+r⁻¹) {f g : ℝ → ℂ}
    (hf : MemLp f p) (hg : MemLp g q) :
    MemLp (convolution f g) r ∧
    eLpNorm (convolution f g) r ≤
      ENNReal.ofReal (becknerFactor p⁻¹.toReal * becknerFactor q⁻¹.toReal *
        becknerFactor (1-r⁻¹.toReal)) * eLpNorm f p * eLpNorm g q := by
  have hp0 : p ≠ 0 := ne_of_gt (lt_of_lt_of_le (by norm_num) hp)
  have hq0 : q ≠ 0 := ne_of_gt (lt_of_lt_of_le (by norm_num) hq)
  have hr0 : r ≠ 0 := ne_of_gt (lt_of_lt_of_le (by norm_num) hr)
  have hpi : p⁻¹ ≠ ∞ := ENNReal.inv_ne_top.mpr hp0
  have hqi : q⁻¹ ≠ ∞ := ENNReal.inv_ne_top.mpr hq0
  have hri : r⁻¹ ≠ ∞ := ENNReal.inv_ne_top.mpr hr0
  have hcp : p⁻¹.toReal ≤ 1 := by
    simpa only [ENNReal.toReal_one] using
      ENNReal.toReal_mono ENNReal.one_ne_top (ENNReal.inv_le_one.mpr hp)
  have hcq : q⁻¹.toReal ≤ 1 := by
    simpa only [ENNReal.toReal_one] using
      ENNReal.toReal_mono ENNReal.one_ne_top (ENNReal.inv_le_one.mpr hq)
  have he : p⁻¹.toReal + q⁻¹.toReal = 1+r⁻¹.toReal := by
    have H := congrArg ENNReal.toReal hexp
    simpa only [ENNReal.toReal_add hpi hqi, ENNReal.toReal_add ENNReal.one_ne_top hri,
      ENNReal.toReal_one] using H
  by_cases hrt : r = ∞
  · subst r
    have hconj : p⁻¹+q⁻¹=(1:ℝ≥0∞)⁻¹ := by simpa using hexp
    letI : ENNReal.HolderTriple p q 1 := ⟨hconj⟩
    have hc : q⁻¹.toReal = 1-p⁻¹.toReal := by simp only [ENNReal.inv_top, ENNReal.toReal_zero] at he; linarith
    have hfactor : becknerFactor p⁻¹.toReal * becknerFactor q⁻¹.toReal *
        becknerFactor (1-(∞:ℝ≥0∞)⁻¹.toReal) = 1 := by
      rw [hc, becknerFactor_mul_complement ENNReal.toReal_nonneg hcp]
      simp
    simpa only [hfactor, ENNReal.ofReal_one, one_mul] using young_conjugate hf hg
  have hcr : 0 < r⁻¹.toReal := ENNReal.toReal_pos (ENNReal.inv_ne_zero.mpr hrt) hri
  have hpt : p ≠ ∞ := by
    intro h
    simp only [h, ENNReal.inv_top, ENNReal.toReal_zero, zero_add] at he
    linarith only [he, hcq, hcr]
  have hqt : q ≠ ∞ := by
    intro h
    simp only [h, ENNReal.inv_top, ENNReal.toReal_zero, add_zero] at he
    linarith only [he, hcp, hcr]
  have hpR : 1 ≤ p.toReal := by simpa using ENNReal.toReal_mono hpt hp
  have hqR : 1 ≤ q.toReal := by simpa using ENNReal.toReal_mono hqt hq
  have hrR : 1 ≤ r.toReal := by simpa using ENNReal.toReal_mono hrt hr
  have hexpR : 1/p.toReal+1/q.toReal=1+1/r.toReal := by
    simpa only [one_div, ENNReal.toReal_inv] using he
  have H := sharp_young_finite hpR hqR hrR hexpR
    (by simpa only [ENNReal.ofReal_toReal hpt] using hf)
    (by simpa only [ENNReal.ofReal_toReal hqt] using hg)
  simpa only [ENNReal.ofReal_toReal hpt, ENNReal.ofReal_toReal hqt,
    ENNReal.ofReal_toReal hrt, ENNReal.toReal_inv, one_div] using H

/-- Beckner's sharp Young inequality on the real line, for all admissible
extended exponents and arbitrary complex Lp functions. The conjugate output
exponent is `(1-r⁻¹)⁻¹`; all endpoint factors have their exact value one. -/
theorem sharp_young {p q r : ℝ≥0∞}
    (hp : 1 ≤ p) (hq : 1 ≤ q) (hr : 1 ≤ r)
    (hexp : p⁻¹+q⁻¹=1+r⁻¹) {f g : ℝ → ℂ}
    (hf : MemLp f p) (hg : MemLp g q) :
    MemLp (convolution f g) r ∧
    eLpNorm (convolution f g) r ≤
      ENNReal.ofReal (becknerA p * becknerA q * becknerA ((1-r⁻¹)⁻¹)) *
        eLpNorm f p * eLpNorm g q := by
  have he : ((1-r⁻¹)⁻¹)⁻¹.toReal = 1-r⁻¹.toReal := by
    rw [inv_inv, ENNReal.toReal_sub_of_le (ENNReal.inv_le_one.mpr hr) ENNReal.one_ne_top,
      ENNReal.toReal_one]
  simpa only [becknerA, he] using sharp_young_ennreal hp hq hr hexp hf hg

end ChowlaCosine.Beckner
