import ChowlaCosine.P31.Averaging
import ChowlaCosine.P31.Fejer

/-!
# P31 with its spectral-factorization dependency explicit

`p31_of_factorization` assumes actual analytic factors for all real window
centres. This is an explicitly CONDITIONAL version of T3, not a proof of
finite Fejér–Riesz. All circle moment and averaging identities are proved.
-/

open Real MeasureTheory
open scoped BigOperators

namespace ChowlaCosine.P31

theorem circleMean_fejerKernel_shift (w : ℕ) (y : ℝ) :
    circleMean (fun x => fejerKernel w (x - y)) = 1 := by
  rw [circleMean_periodic_sub (fejerKernel_periodic w), circleMean_fejerKernel]

theorem circleMean_fejerKernel_mul_cos (w : ℕ) {a : ℕ} (ha : 0 < a) (y : ℝ) :
    circleMean (fun x => fejerKernel w (x - y) * Real.cos ((a : ℝ) * x)) =
      kappa w a * Real.cos ((a : ℝ) * y) := by
  have hexp : (fun x => fejerKernel w (x - y) * Real.cos ((a : ℝ) * x)) =
      (fun x => Real.cos ((a : ℝ) * x) + 2 * ∑ k ∈ windowFreq w,
        kappa w k * (Real.cos ((k : ℝ) * (x - y)) * Real.cos ((a : ℝ) * x))) := by
    funext x
    simp only [fejerKernel, weightedCos, add_mul, one_mul, Finset.sum_mul]
    congr 1
    rw [mul_assoc]
    congr 1
    rw [Finset.sum_mul]
    apply Finset.sum_congr rfl
    intro k hk
    ring
  rw [hexp, circleMean_add (by fun_prop) (by fun_prop)]
  have hm : circleMean (fun x => Real.cos ((a : ℝ) * x)) = 0 := by
    simp [circleMean, integral_cos_nat_mul ha]
  rw [hm, zero_add, circleMean_const_mul,
    circleMean_sum (windowFreq w) _ (by intro k hk; fun_prop)]
  have hi : ∀ k ∈ windowFreq w, circleMean (fun x => kappa w k *
      (Real.cos ((k : ℝ) * (x - y)) * Real.cos ((a : ℝ) * x))) =
        if k = a then kappa w a * Real.cos ((a : ℝ) * y) / 2 else 0 := by
    intro k hk
    rw [circleMean_const_mul,
      circleMean_cos_shift_mul_cos (windowFreq_pos w k hk) ha]
    split_ifs with hka
    · subst k
      ring
    · ring
  rw [Finset.sum_congr rfl hi]
  by_cases haw : a ≤ w
  · have ham : a ∈ windowFreq w := Finset.mem_Icc.mpr ⟨ha, haw⟩
    simp [ham]
    ring
  · have hz := kappa_eq_zero (Nat.lt_of_not_ge haw)
    simp [hz]

theorem circleMean_window (w : ℕ) (A : Finset ℕ) (M y : ℝ)
    (hA : ∀ a ∈ A, 0 < a) :
    circleMean (fun x => fejerKernel w (x - y) * (cosSum A x + M)) =
      M + weightedCos A (kappa w) y := by
  have hexp : (fun x => fejerKernel w (x - y) * (cosSum A x + M)) =
      (fun x => (∑ a ∈ A, fejerKernel w (x - y) * Real.cos ((a : ℝ) * x)) +
        fejerKernel w (x - y) * M) := by
    funext x
    simp [cosSum, mul_add, Finset.mul_sum]
  rw [hexp, circleMean_add (by fun_prop) (by fun_prop),
    circleMean_sum A _ (by intro a ha; fun_prop), circleMean_mul_const,
    circleMean_fejerKernel_shift, one_mul]
  rw [Finset.sum_congr rfl (fun a ha => circleMean_fejerKernel_mul_cos w (hA a ha) y)]
  exact add_comm _ _

theorem circleMean_window_mean_sq (w : ℕ) (A : Finset ℕ) (M : ℝ)
    (hA : ∀ a ∈ A, 0 < a) :
    circleMean (fun y => circleMean
      (fun x => fejerKernel w (x - y) * (cosSum A x + M)) ^ 2) =
        M ^ 2 + windowEnergy w A / 2 := by
  simp_rw [circleMean_window w A M _ hA]
  exact circleMean_shifted_weightedCos_sq A (kappa w) M hA

/-- Exact P31 averaging reduction. The additional hypothesis is the
square/mean inequality for every translated window. -/
theorem p31_of_window_bound (w : ℕ) (A : Finset ℕ) (M C : ℝ)
    (hA : ∀ a ∈ A, 0 < a)
    (hbound : ∀ y : ℝ,
      circleMean (fun x => (fejerKernel w (x - y) * (cosSum A x + M)) ^ 2) ≤
        C * circleMean (fun x => fejerKernel w (x - y) * (cosSum A x + M)) ^ 2) :
    windowMass w * ((A.card : ℝ) / 2 + M ^ 2) ≤
      C * (M ^ 2 + windowEnergy w A / 2) := by
  have h := averaged_window_bound C (continuous_fejerKernel w)
    ((continuous_cosSum A).add continuous_const)
    (fejerKernel_periodic w) hbound
  simp only [Pi.add_apply] at h
  rwa [circleMean_fejerKernel_sq, circleMean_cosSum_add_sq A M hA,
    circleMean_window_mean_sq w A M hA] at h

noncomputable def analyticValue {L : ℕ} (u : Fin (L + 1) → ℂ) (x : ℝ) : ℂ :=
  ∑ j, u j * Complex.exp ((j.val : ℂ) * (x : ℂ) * Complex.I)

/-- The analytic degree-at-most-`L` hypothesis in T3, in normalized
fourth/second-moment form. It quantifies over every complex coefficient vector. -/
def AnalyticNikolskii (L : ℕ) (C : ℝ) : Prop :=
  ∀ u : Fin (L + 1) → ℂ,
    circleMean (fun x => ‖analyticValue u x‖ ^ 4) ≤
      C * circleMean (fun x => ‖analyticValue u x‖ ^ 2) ^ 2

/-- The exact missing window-specific consequence of Fejér–Riesz,
with analytic degree at most `L`. Centres and angles are arbitrary reals. -/
def WindowFactorization (L w : ℕ) (A : Finset ℕ) (M : ℝ) : Prop :=
  ∀ y : ℝ, ∃ u : Fin (L + 1) → ℂ, ∀ x : ℝ,
    fejerKernel w (x - y) * (cosSum A x + M) = ‖analyticValue u x‖ ^ 2

/-- CONDITIONAL T3. `hfactor` is an additional, unproved mathematical
hypothesis and is not hidden in the Nikolskii constant. -/
theorem p31_of_factorization (L w : ℕ) (A : Finset ℕ) (M C : ℝ)
    (hA : ∀ a ∈ A, 0 < a) (hnik : AnalyticNikolskii L C)
    (hfactor : WindowFactorization L w A M) :
    windowMass w * ((A.card : ℝ) / 2 + M ^ 2) ≤
      C * (M ^ 2 + windowEnergy w A / 2) := by
  apply p31_of_window_bound w A M C hA
  intro y
  obtain ⟨u, hu⟩ := hfactor y
  have h := hnik u
  have hpow : ∀ x : ℝ, (fejerKernel w (x - y) * (cosSum A x + M)) ^ 2 =
      ‖analyticValue u x‖ ^ 4 := by
    intro x
    rw [hu x, ← pow_mul]
  simpa only [hu, ← pow_mul] using h

end ChowlaCosine.P31

/-! ## Degree control and the universal factorization assumption

The span representation is a finite complex trigonometric polynomial, not
a relaxation of the `Finset` of positive frequencies in the theorem.
-/

namespace ChowlaCosine.P31

noncomputable def circleCharacter (k : ℤ) (x : ℝ) : ℂ :=
  Complex.exp ((k : ℂ) * (x : ℂ) * Complex.I)

noncomputable def trigBand (L : ℕ) : Submodule ℂ (ℝ → ℂ) :=
  Submodule.span ℂ {f | ∃ k : ℤ, |k| ≤ (L : ℤ) ∧ f = circleCharacter k}

theorem character_mem_trigBand {L : ℕ} {k : ℤ} (hk : |k| ≤ (L : ℤ)) :
    circleCharacter k ∈ trigBand L :=
  Submodule.subset_span ⟨k, hk, rfl⟩

private theorem character_mul (k m : ℤ) :
    circleCharacter k * circleCharacter m = circleCharacter (k + m) := by
  funext x
  simp only [Pi.mul_apply, circleCharacter, ← Complex.exp_add]
  congr 1
  push_cast
  ring

theorem trigBand_mul {L K : ℕ} {f g : ℝ → ℂ}
    (hf : f ∈ trigBand L) (hg : g ∈ trigBand K) :
    f * g ∈ trigBand (L + K) := by
  induction hf using Submodule.span_induction with
  | mem f hf =>
    obtain ⟨k, hk, rfl⟩ := hf
    induction hg using Submodule.span_induction with
    | mem g hg =>
      obtain ⟨m, hm, rfl⟩ := hg
      rw [character_mul]
      apply character_mem_trigBand
      have hab := abs_add_le k m
      push_cast
      omega
    | zero => simpa using (trigBand (L + K)).zero_mem
    | add f g hf hg ihf ihg =>
      simpa only [mul_add] using (trigBand (L + K)).add_mem ihf ihg
    | smul c f hf ih =>
      simpa only [mul_smul_comm] using (trigBand (L + K)).smul_mem c ih
  | zero => simpa using (trigBand (L + K)).zero_mem
  | add f h hf hh ihf ihh =>
    simpa only [add_mul] using (trigBand (L + K)).add_mem ihf ihh
  | smul c f hf ih =>
    simpa only [smul_mul_assoc] using (trigBand (L + K)).smul_mem c ih

theorem const_mem_trigBand (L : ℕ) (c : ℂ) : (fun _ : ℝ => c) ∈ trigBand L := by
  have h := (trigBand L).smul_mem c
    (character_mem_trigBand (L := L) (k := 0) (by simp))
  convert h using 1
  funext x
  simp [circleCharacter]

/-- A shifted cosine has precisely the same frequency bound. -/
theorem cos_shift_mem_trigBand {L a : ℕ} (ha : a ≤ L) (y : ℝ) :
    (fun x : ℝ => (Real.cos ((a : ℝ) * (x - y)) : ℂ)) ∈ trigBand L := by
  have hp := (trigBand L).smul_mem
    (Complex.exp (-(a : ℂ) * (y : ℂ) * Complex.I) / 2)
    (character_mem_trigBand (L := L) (k := (a : ℤ)) (by
      simpa using (show (a : ℤ) ≤ L by exact_mod_cast ha)))
  have hn := (trigBand L).smul_mem
    (Complex.exp ((a : ℂ) * (y : ℂ) * Complex.I) / 2)
    (character_mem_trigBand (L := L) (k := -(a : ℤ)) (by
      simpa using (show (a : ℤ) ≤ L by exact_mod_cast ha)))
  convert (trigBand L).add_mem hp hn using 1
  funext x
  simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul, circleCharacter]
  rw [Complex.ofReal_cos, Complex.cos]
  push_cast
  have he1 : Complex.exp (-(a : ℂ) * (y : ℂ) * Complex.I) *
      Complex.exp ((a : ℂ) * (x : ℂ) * Complex.I) =
      Complex.exp (((a : ℂ) * ((x : ℂ) - (y : ℂ))) * Complex.I) := by
    rw [← Complex.exp_add]
    congr 1
    ring
  have he2 : Complex.exp ((a : ℂ) * (y : ℂ) * Complex.I) *
      Complex.exp (-(a : ℂ) * (x : ℂ) * Complex.I) =
      Complex.exp (-((a : ℂ) * ((x : ℂ) - (y : ℂ))) * Complex.I) := by
    rw [← Complex.exp_add]
    congr 1
    ring
  linear_combination -(1 / 2 : ℂ) * he1 - (1 / 2 : ℂ) * he2

theorem fejer_shift_mem_trigBand (w : ℕ) (y : ℝ) :
    (fun x : ℝ => (fejerKernel w (x - y) : ℂ)) ∈ trigBand w := by
  have hs : (fun x : ℝ => (2 : ℂ) *
      ∑ a ∈ windowFreq w, (kappa w a : ℂ) *
        (Real.cos ((a : ℝ) * (x - y)) : ℂ)) ∈ trigBand w := by
    apply (trigBand w).smul_mem (2 : ℂ)
    have hsum : (∑ a ∈ windowFreq w, fun x : ℝ => (kappa w a : ℂ) *
        (Real.cos ((a : ℝ) * (x - y)) : ℂ)) ∈ trigBand w := by
      apply Submodule.sum_mem
      intro a ha
      exact (trigBand w).smul_mem (kappa w a : ℂ)
        (cos_shift_mem_trigBand (Finset.mem_Icc.mp ha).2 y)
    convert hsum using 1
    funext x
    simp only [Finset.sum_apply]
  convert (trigBand w).add_mem (const_mem_trigBand w 1) hs using 1
  funext x
  simp [fejerKernel, weightedCos]

theorem cosSum_add_mem_trigBand (A : Finset ℕ) (X : ℕ) (M : ℝ)
    (hX : ∀ a ∈ A, a ≤ X) :
    (fun x : ℝ => (cosSum A x + M : ℂ)) ∈ trigBand X := by
  have hs : (fun x : ℝ => (cosSum A x : ℂ)) ∈ trigBand X := by
    have h : (∑ a ∈ A, fun x : ℝ => (Real.cos ((a : ℝ) * x) : ℂ)) ∈ trigBand X := by
      apply Submodule.sum_mem
      intro a ha
      simpa using cos_shift_mem_trigBand (hX a ha) 0
    convert h using 1
    funext x
    simp only [cosSum, Complex.ofReal_sum, Finset.sum_apply]
  convert (trigBand X).add_mem hs (const_mem_trigBand X (M : ℂ)) using 1
  funext x
  simp only [Pi.add_apply, Complex.ofReal_add]

/-- The full finite Fejér–Riesz assertion needed here, kept as a `Prop`
so it cannot be mistaken for a proved theorem. -/
def FejerRiesz (L : ℕ) : Prop :=
  ∀ h : ℝ → ℝ, (fun x => (h x : ℂ)) ∈ trigBand L →
    (∀ x : ℝ, 0 ≤ h x) →
      ∃ u : Fin (L + 1) → ℂ, ∀ x : ℝ, h x = ‖analyticValue u x‖ ^ 2

end ChowlaCosine.P31

namespace ChowlaCosine.P31

/-- P31 with the one missing universal theorem made explicit. Here `X`
may be any upper bound for the positive finite set, and `L = X + w` exactly. -/
theorem p31_of_fejerRiesz (w X : ℕ) (A : Finset ℕ) (M C : ℝ)
    (hA : ∀ a ∈ A, 0 < a) (hX : ∀ a ∈ A, a ≤ X)
    (hM : ∀ x : ℝ, -M ≤ cosSum A x)
    (hFR : FejerRiesz (X + w)) (hnik : AnalyticNikolskii (X + w) C) :
    windowMass w * ((A.card : ℝ) / 2 + M ^ 2) ≤
      C * (M ^ 2 + windowEnergy w A / 2) := by
  apply p31_of_factorization (X + w) w A M C hA hnik
  intro y
  apply hFR (fun x => fejerKernel w (x - y) * (cosSum A x + M))
  · have hd := trigBand_mul (fejer_shift_mem_trigBand w y)
      (cosSum_add_mem_trigBand A X M hX)
    rw [Nat.add_comm] at hd
    convert hd using 1
    funext x
    simp only [Pi.mul_apply, Complex.ofReal_mul, Complex.ofReal_add]
  · intro x
    exact window_nonneg w A M hM x y

/-- Exact maximum-frequency specialization. The additional `hFR`
hypothesis must be discharged by T1 before this is the requested T3. -/
theorem p31_main_of_fejerRiesz (w : ℕ) (A : Finset ℕ) (M C : ℝ)
    (hA : ∀ a ∈ A, 0 < a) (hM : ∀ x : ℝ, -M ≤ cosSum A x)
    (hFR : FejerRiesz (A.sup id + w))
    (hnik : AnalyticNikolskii (A.sup id + w) C) :
    windowMass w * ((A.card : ℝ) / 2 + M ^ 2) ≤
      C * (M ^ 2 + windowEnergy w A / 2) :=
  p31_of_fejerRiesz w (A.sup id) A M C hA
    (fun a ha => Finset.le_sup (f := id) ha) hM hFR hnik

end ChowlaCosine.P31

-- BEGIN T1 DEVELOPMENT
namespace ChowlaCosine.P31

/-- Degree-zero base case, including the identically zero polynomial. -/
theorem fejerRiesz_zero : FejerRiesz 0 := by
  intro h hh hn
  have hconst : ∀ f : ℝ → ℂ, f ∈ trigBand 0 → ∀ x : ℝ, f x = f 0 := by
    intro f hf
    induction hf using Submodule.span_induction with
    | mem f hf =>
      obtain ⟨k, hk, rfl⟩ := hf
      have hk0 : k = 0 := by simpa using hk
      subst k
      simp [circleCharacter]
    | zero => simp
    | add f g hf hg ihf ihg =>
      intro x
      simp only [Pi.add_apply, ihf x, ihg x]
    | smul c f hf ih =>
      intro x
      simp only [Pi.smul_apply, ih x]
  have hx : ∀ x : ℝ, h x = h 0 := by
    intro x
    exact Complex.ofReal_injective (hconst _ hh x)
  refine ⟨fun _ => (Real.sqrt (h 0) : ℂ), ?_⟩
  intro x
  rw [hx]
  simp [analyticValue, Complex.norm_real, Real.norm_eq_abs,
    abs_of_nonneg (Real.sqrt_nonneg (h 0)), Real.sq_sqrt (hn 0)]

/-- Reciprocal conjugation is the root symmetry of a Hermitian Laurent polynomial. -/
noncomputable def rootReflection (a : ℂ) : ℂ := (star a)⁻¹

@[simp] theorem rootReflection_rootReflection (a : ℂ) :
    rootReflection (rootReflection a) = a := by
  simp [rootReflection]

/-- The local algebraic identity for a reciprocal-conjugate root pair.
It includes roots on the circle; parity of their multiplicity is a separate obligation. -/
theorem root_pair_identity (a z : ℂ) (ha : a ≠ 0) (hz : ‖z‖ = 1) :
    (z - a) * (z - rootReflection a) =
      -(z / star a) * (‖z - a‖ ^ 2 : ℂ) := by
  have hznorm : Complex.normSq z = 1 := by rw [Complex.normSq_eq_norm_sq, hz]; norm_num
  have hzprod : z * star z = 1 := by
    simpa only [Complex.star_def, Complex.mul_conj, hznorm, Complex.ofReal_one]
  have han : star a ≠ 0 := star_ne_zero.mpr ha
  rw [← Complex.ofReal_pow, Complex.sq_norm, Complex.normSq_eq_conj_mul_self]
  simp only [map_sub]
  change (z - a) * (z - (star a)⁻¹) =
    -(z / star a) * ((star z - star a) * (z - a))
  field_simp [han]
  linear_combination (z - a) * hzprod

end ChowlaCosine.P31

namespace ChowlaCosine.P31

/-- A second route to the zero-on-the-circle case: uniformly bounded
analytic factors for positive perturbations have a limiting factor.
The existence and uniform coefficient bound are explicit hypotheses. -/
theorem factorization_of_bounded_approximation (L : ℕ) (h : ℝ → ℝ) (B : ℝ)
    (ε : ℕ → ℝ) (hε : Filter.Tendsto ε Filter.atTop (nhds 0))
    (happrox : ∀ n : ℕ, ∃ u : Fin (L + 1) → ℂ, ‖u‖ ≤ B ∧
      ∀ x : ℝ, h x + ε n = ‖analyticValue u x‖ ^ 2) :
    ∃ u : Fin (L + 1) → ℂ, ∀ x : ℝ, h x = ‖analyticValue u x‖ ^ 2 := by
  choose u hub hu using happrox
  have hmem : ∀ n : ℕ, u n ∈ Metric.closedBall (0 : Fin (L + 1) → ℂ) B := by
    intro n
    simpa only [Metric.mem_closedBall, dist_zero_right] using hub n
  obtain ⟨v, hv, φ, hφ, hlim⟩ := (isCompact_closedBall
    (0 : Fin (L + 1) → ℂ) B).tendsto_subseq hmem
  refine ⟨v, ?_⟩
  intro x
  have hc : Continuous (fun a : Fin (L + 1) → ℂ => ‖analyticValue a x‖ ^ 2) := by
    unfold analyticValue
    fun_prop
  have hval := (hc.tendsto v).comp hlim
  have heps := hε.comp hφ.tendsto_atTop
  have hleft : Filter.Tendsto (fun n : ℕ => h x + ε (φ n)) Filter.atTop (nhds (h x)) := by
    simpa only [Function.comp_def, add_zero] using (tendsto_const_nhds.add heps)
  have heq : (fun n : ℕ => h x + ε (φ n)) =
      (fun n : ℕ => ‖analyticValue (u (φ n)) x‖ ^ 2) := by
    funext n
    exact hu (φ n) x
  rw [heq] at hleft
  exact tendsto_nhds_unique hleft hval

end ChowlaCosine.P31

namespace ChowlaCosine.P31

/-- Off the circle, reciprocal-conjugate symmetry gives an exact partition
into the roots inside the disk and their reflected partners. This does not
assert that an arbitrary polynomial has the required root symmetry. -/
theorem root_partition_off_circle (s : Multiset ℂ)
    (hstable : s.map rootReflection = s)
    (hnz : ∀ a ∈ s, a ≠ 0) (hunit : ∀ a ∈ s, ‖a‖ ≠ 1) :
    s = s.filter (fun a => ‖a‖ < 1) +
      (s.filter (fun a => ‖a‖ < 1)).map rootReflection := by
  classical
  have hequiv : ∀ a ∈ s, (¬ ‖rootReflection a‖ < 1) ↔ ‖a‖ < 1 := by
    intro a ha
    have hp : 0 < ‖a‖ := norm_pos_iff.mpr (hnz a ha)
    have hnorm : ‖rootReflection a‖ = ‖a‖⁻¹ := by simp [rootReflection]
    rw [hnorm, not_lt]
    have hinv := inv_mul_cancel₀ hp.ne'
    constructor
    · intro h
      have hmul := mul_le_mul_of_nonneg_right h hp.le
      rw [hinv, one_mul] at hmul
      exact lt_of_le_of_ne hmul (hunit a ha)
    · intro h
      by_contra hbad
      have hb : ‖a‖⁻¹ < 1 := lt_of_not_ge hbad
      have hmul := mul_lt_mul_of_pos_right hb hp
      rw [hinv, one_mul] at hmul
      linarith
  have hmap : s.filter (fun a => ¬ ‖a‖ < 1) =
      (s.filter (fun a => ‖a‖ < 1)).map rootReflection := by
    conv_lhs => rw [← hstable]
    rw [Multiset.filter_map]
    congr 1
    apply Multiset.filter_congr
    intro a ha
    exact hequiv a ha
  rw [← hmap]
  exact (Multiset.filter_add_not (fun a : ℂ => ‖a‖ < 1) s).symm

end ChowlaCosine.P31

namespace ChowlaCosine.P31

private noncomputable def halfMultiset (s : Multiset ℂ) : Multiset ℂ :=
  Finsupp.toMultiset (s.toFinsupp.mapRange (fun n : ℕ => n / 2) (by decide))

private theorem count_halfMultiset (s : Multiset ℂ) (a : ℂ) :
    (halfMultiset s).count a = s.count a / 2 := by
  classical
  simp [halfMultiset, Finsupp.count_toMultiset, Multiset.toFinsupp_apply]

/-- Complete combinatorial root selection, including roots on the circle.
The analytic even-multiplicity fact remains an explicit hypothesis. -/
theorem root_partition_of_even_fixed (s : Multiset ℂ)
    (hstable : s.map rootReflection = s) (hnz : ∀ a ∈ s, a ≠ 0)
    (heven : ∀ a : ℂ, ‖a‖ = 1 → Even (s.count a)) :
    ∃ t : Multiset ℂ, s = t + t.map rootReflection := by
  classical
  let t := s.filter (fun a => ‖a‖ < 1) + halfMultiset (s.filter (fun a => ‖a‖ = 1))
  have hcount : ∀ q : Multiset ℂ, ∀ a : ℂ,
      (q.map rootReflection).count a = q.count (rootReflection a) := by
    intro q a
    have hi : Function.Injective rootReflection :=
      Function.Involutive.injective rootReflection_rootReflection
    simpa using Multiset.count_map_eq_count' rootReflection q hi (rootReflection a)
  have hsym : ∀ a : ℂ, s.count (rootReflection a) = s.count a := by
    intro a
    rw [← hcount, hstable]
  have ht : ∀ a : ℂ, t.count a =
      (if ‖a‖ < 1 then s.count a else 0) + (if ‖a‖ = 1 then s.count a / 2 else 0) := by
    intro a
    simp only [t, Multiset.count_add, count_halfMultiset, Multiset.count_filter]
    split_ifs <;> simp_all
  refine ⟨t, ?_⟩
  apply Multiset.ext.mpr
  intro a
  rw [Multiset.count_add, hcount, ht, ht, hsym]
  by_cases ha : a ∈ s
  · have hp : 0 < ‖a‖ := norm_pos_iff.mpr (hnz a ha)
    have hnorm : ‖rootReflection a‖ = ‖a‖⁻¹ := by simp [rootReflection]
    rcases lt_trichotomy ‖a‖ 1 with h | h | h
    · have htau : 1 < ‖rootReflection a‖ := by
        rw [hnorm]
        exact (one_lt_inv₀ hp).mpr h
      simp [h, h.ne, not_lt.mpr htau.le, htau.ne']
    · have htau : ‖rootReflection a‖ = 1 := by rw [hnorm, h, inv_one]
      simp only [h, htau, lt_self_iff_false, ↓reduceIte, zero_add]
      obtain ⟨k, hk⟩ := heven a h
      omega
    · have htau : ‖rootReflection a‖ < 1 := by
        rw [hnorm]
        exact (inv_lt_one₀ hp).mpr h
      simp [not_lt.mpr h.le, h.ne', htau, htau.ne]
  · have hzero : s.count a = 0 := Multiset.count_eq_zero_of_notMem ha
    simp [hzero]

end ChowlaCosine.P31

namespace ChowlaCosine.P31

/-- Product version of the root-pair identity. This is the algebraic
assembly step after roots have actually been partitioned. -/
theorem root_product_identity (t : Multiset ℂ) (z : ℂ) (hz : ‖z‖ = 1)
    (hnz : ∀ a ∈ t, a ≠ 0) :
    (t.map (fun a => (z - a) * (z - rootReflection a))).prod =
      (t.map (fun a => -(star a)⁻¹)).prod * z ^ t.card *
        ((‖(t.map (fun a => z - a)).prod‖ ^ 2 : ℝ) : ℂ) := by
  induction t using Multiset.induction_on with
  | empty => simp
  | @cons a t ih =>
    have ha : a ≠ 0 := hnz a (by simp)
    have ht : ∀ b ∈ t, b ≠ 0 := by
      intro b hb
      exact hnz b (by simp [hb])
    simp only [Multiset.map_cons, Multiset.prod_cons, Multiset.card_cons,
      norm_mul, mul_pow, Complex.ofReal_mul]
    rw [root_pair_identity a z ha hz, ih ht]
    simp only [pow_succ, div_eq_mul_inv]
    push_cast
    ring

end ChowlaCosine.P31

-- BEGIN T1 LIVE AUDIT
#print axioms ChowlaCosine.P31.fejerRiesz_zero
#print axioms ChowlaCosine.P31.rootReflection_rootReflection
#print axioms ChowlaCosine.P31.root_pair_identity
#print axioms ChowlaCosine.P31.factorization_of_bounded_approximation
#print axioms ChowlaCosine.P31.root_partition_off_circle
#print axioms ChowlaCosine.P31.root_partition_of_even_fixed
#print axioms ChowlaCosine.P31.root_product_identity
