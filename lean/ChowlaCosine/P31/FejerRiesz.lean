import ChowlaCosine.P31.WindowBound

/-! # Finite Fejér–Riesz via reciprocal-conjugate roots

This includes degenerate degrees, the zero polynomial, and even multiplicities
on the unit circle. The final theorem has no factorization hypothesis.
-/

open Real MeasureTheory
open scoped BigOperators

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


namespace ChowlaCosine.P31

theorem analyticValue_coeff {L : ℕ} (q : Polynomial ℂ) (hq : q.natDegree ≤ L) (x : ℝ) :
    analyticValue (fun j : Fin (L + 1) => q.coeff j.val) x =
      q.eval (Complex.exp ((x : ℂ) * Complex.I)) := by
  rw [Polynomial.eval_eq_sum_range' (Nat.lt_succ_of_le hq), ← Fin.sum_univ_eq_sum_range]
  unfold analyticValue
  apply Finset.sum_congr rfl
  intro j hj
  rw [mul_assoc, Complex.exp_nat_mul]

/-- Once the root argument has given a scalar times a polynomial norm
square on the circle, positivity fixes the scalar and supplies the exact
analytic coefficient vector. No positivity or nonvanishing is assumed for `q`. -/
theorem factorization_of_polynomial_norm (L : ℕ) (h : ℝ → ℝ)
    (q : Polynomial ℂ) (γ : ℂ) (hq : q.natDegree ≤ L)
    (hn : ∀ x : ℝ, 0 ≤ h x)
    (hidentity : ∀ x : ℝ, (h x : ℂ) =
      γ * ((‖q.eval (Complex.exp ((x : ℂ) * Complex.I))‖ ^ 2 : ℝ) : ℂ)) :
    ∃ u : Fin (L + 1) → ℂ, ∀ x : ℝ, h x = ‖analyticValue u x‖ ^ 2 := by
  by_cases hzero : ∀ x : ℝ, h x = 0
  · refine ⟨fun _ => 0, ?_⟩
    intro x
    simp [hzero x, analyticValue]
  push_neg at hzero
  obtain ⟨x₀, hx₀⟩ := hzero
  let E : ℝ → ℝ := fun x => ‖q.eval (Complex.exp ((x : ℂ) * Complex.I))‖ ^ 2
  have he0 : E x₀ ≠ 0 := by
    intro he
    have hh := hidentity x₀
    change (h x₀ : ℂ) = γ * (E x₀ : ℂ) at hh
    rw [he, Complex.ofReal_zero, mul_zero] at hh
    exact hx₀ (Complex.ofReal_injective hh)
  let r : ℝ := h x₀ / E x₀
  have hr : 0 ≤ r := div_nonneg (hn x₀) (sq_nonneg _)
  have hγ : γ = (r : ℂ) := by
    have hc : (E x₀ : ℂ) ≠ 0 := by exact_mod_cast he0
    change γ = ((h x₀ / E x₀ : ℝ) : ℂ)
    rw [Complex.ofReal_div]
    apply (eq_div_iff hc).mpr
    exact (hidentity x₀).symm
  have hreal : ∀ x : ℝ, h x = r * E x := by
    intro x
    apply Complex.ofReal_injective
    rw [hidentity x, hγ]
    simp only [E, Complex.ofReal_mul]
  refine ⟨fun j => (Real.sqrt r : ℂ) * q.coeff j.val, ?_⟩
  intro x
  have hval : analyticValue (fun j : Fin (L + 1) => (Real.sqrt r : ℂ) * q.coeff j.val) x =
      (Real.sqrt r : ℂ) * q.eval (Complex.exp ((x : ℂ) * Complex.I)) := by
    rw [← analyticValue_coeff q hq x]
    simp only [analyticValue, Finset.mul_sum, mul_assoc]
  rw [hval, norm_mul, mul_pow, hreal x]
  simp only [Complex.norm_real, Real.norm_eq_abs, sq_abs, Real.sq_sqrt hr]
  rfl

end ChowlaCosine.P31

namespace ChowlaCosine.P31

/-- Assembly from explicit paired-root data. Root symmetry and evenness
are not assumed implicitly: they must have supplied this multiset and identity. -/
theorem factorization_of_root_data (L : ℕ) (h : ℝ → ℝ) (c : ℂ) (t : Multiset ℂ)
    (ht : t.card ≤ L) (hnz : ∀ a ∈ t, a ≠ 0) (hn : ∀ x : ℝ, 0 ≤ h x)
    (hdata : ∀ x : ℝ,
      Complex.exp ((x : ℂ) * Complex.I) ^ t.card * (h x : ℂ) =
        c * (t.map (fun a =>
          (Complex.exp ((x : ℂ) * Complex.I) - a) *
          (Complex.exp ((x : ℂ) * Complex.I) - rootReflection a))).prod) :
    ∃ u : Fin (L + 1) → ℂ, ∀ x : ℝ, h x = ‖analyticValue u x‖ ^ 2 := by
  let q : Polynomial ℂ := (t.map (fun a => Polynomial.X - Polynomial.C a)).prod
  let γ : ℂ := c * (t.map (fun a => -(star a)⁻¹)).prod
  have hq : q.natDegree ≤ L := by
    simpa only [q, Polynomial.natDegree_multiset_prod_X_sub_C_eq_card] using ht
  apply factorization_of_polynomial_norm L h q γ hq hn
  intro x
  let z := Complex.exp ((x : ℂ) * Complex.I)
  have hz : ‖z‖ = 1 := by simp [z, Complex.norm_exp]
  have hzne : z ≠ 0 := Complex.exp_ne_zero _
  have hqeval : q.eval z = (t.map (fun a => z - a)).prod := by
    simp [q, Polynomial.eval_multiset_prod, Multiset.map_map]
  apply mul_left_cancel₀ (pow_ne_zero t.card hzne)
  calc
    z ^ t.card * (h x : ℂ) = c * (t.map (fun a => (z - a) * (z - rootReflection a))).prod := hdata x
    _ = z ^ t.card * (γ * ((‖q.eval z‖ ^ 2 : ℝ) : ℂ)) := by
      rw [root_product_identity t z hz hnz, hqeval]
      dsimp only [γ]
      ring

/-- The FTA/root-selection reduction of T1. This proves the complete
factorization once the shifted polynomial's root symmetry and the even
multiplicities on the circle have been established. Those facts remain
explicit hypotheses here. -/
theorem factorization_of_polynomial_root_conditions (L : ℕ) (h : ℝ → ℝ)
    (p : Polynomial ℂ) (hdegree : p.natDegree = 2 * L)
    (hstable : p.roots.map rootReflection = p.roots)
    (hnz : ∀ a ∈ p.roots, a ≠ 0)
    (heven : ∀ a : ℂ, ‖a‖ = 1 → Even (p.roots.count a))
    (hn : ∀ x : ℝ, 0 ≤ h x)
    (hrepresentation : ∀ x : ℝ, p.eval (Complex.exp ((x : ℂ) * Complex.I)) =
      Complex.exp ((x : ℂ) * Complex.I) ^ L * (h x : ℂ)) :
    ∃ u : Fin (L + 1) → ℂ, ∀ x : ℝ, h x = ‖analyticValue u x‖ ^ 2 := by
  obtain ⟨t, ht⟩ := root_partition_of_even_fixed p.roots hstable hnz heven
  have hsplit : p.Splits := IsAlgClosed.splits p
  have htcard : t.card = L := by
    have hc := hsplit.natDegree_eq_card_roots
    rw [hdegree, ht, Multiset.card_add, Multiset.card_map] at hc
    omega
  refine factorization_of_root_data L h p.leadingCoeff t htcard.le ?_ hn ?_
  · intro a ha
    apply hnz a
    rw [ht]
    exact Multiset.mem_add.mpr (Or.inl ha)
  · intro x
    rw [htcard, ← hrepresentation x, hsplit.eval_eq_prod_roots, ht,
      Multiset.map_add, Multiset.prod_add, Multiset.map_map, ← Multiset.prod_map_mul]
    simp only [Function.comp_def]

end ChowlaCosine.P31

namespace ChowlaCosine.P31

/-- A nonzero continuous local factor cannot multiply an odd real power
to give a nonnegative function on both sides of the centre. -/
theorem even_of_local_nonnegative_power (n : ℕ) (g : ℝ → ℝ) (x₀ : ℝ)
    (hg : ContinuousAt g x₀) (hg0 : g x₀ ≠ 0)
    (hn : ∀ᶠ x in nhds x₀, 0 ≤ (x - x₀) ^ n * g x) : Even n := by
  by_contra hbad
  have hodd : Odd n := Nat.not_even_iff_odd.mp hbad
  rcases lt_or_gt_of_ne hg0 with hneg | hpos
  · have hs : ∀ᶠ x in nhds x₀, g x < 0 :=
      Filter.Tendsto.eventually_lt_const hneg hg
    obtain ⟨δ, hδ, hball⟩ := Metric.eventually_nhds_iff.mp (hn.and hs)
    have hdist : dist (x₀ + δ / 2) x₀ < δ := by
      rw [Real.dist_eq, show x₀ + δ / 2 - x₀ = δ / 2 by ring,
        abs_of_pos (by positivity : 0 < δ / 2)]
      linarith
    have hv := hball hdist
    have hp : 0 < (x₀ + δ / 2 - x₀) ^ n := by
      apply pow_pos
      linarith
    exact (not_le_of_gt (mul_neg_of_pos_of_neg hp hv.2)) hv.1
  · have hs : ∀ᶠ x in nhds x₀, 0 < g x :=
      Filter.Tendsto.eventually_const_lt hpos hg
    obtain ⟨δ, hδ, hball⟩ := Metric.eventually_nhds_iff.mp (hn.and hs)
    have hdist : dist (x₀ - δ / 2) x₀ < δ := by
      rw [Real.dist_eq, show x₀ - δ / 2 - x₀ = -(δ / 2) by ring, abs_neg,
        abs_of_pos (by positivity : 0 < δ / 2)]
      linarith
    have hv := hball hdist
    have hp : (x₀ - δ / 2 - x₀) ^ n < 0 := by
      rw [show x₀ - δ / 2 - x₀ = -(δ / 2) by ring, hodd.neg_pow]
      exact neg_neg_of_pos (pow_pos (by positivity : 0 < δ / 2) n)
    exact (not_le_of_gt (mul_neg_of_neg_of_pos hp hv.2)) hv.1

/-- Finite orders of zeros of a locally nonnegative real analytic
function are even. The identically-zero germ has the conventional natural order zero. -/
theorem analyticOrderNatAt_even_of_nonneg (f : ℝ → ℝ) (x₀ : ℝ)
    (hf : AnalyticAt ℝ f x₀) (hn : ∀ᶠ x in nhds x₀, 0 ≤ f x) :
    Even (analyticOrderNatAt f x₀) := by
  by_cases ht : analyticOrderAt f x₀ = ⊤
  · simp [analyticOrderNatAt, ht]
  · obtain ⟨g, hg, hg0, heq⟩ := (hf.analyticOrderNatAt_eq_iff ht).mp rfl
    apply even_of_local_nonnegative_power _ g x₀ hg.continuousAt hg0
    filter_upwards [hn, heq] with x hnx heqx
    simpa only [smul_eq_mul, heqx] using hnx

end ChowlaCosine.P31

namespace ChowlaCosine.P31

/-- Real nonnegativity also forces even local powers when the residual
continuous factor is complex. A real linear functional reduces to the real lemma. -/
theorem even_of_local_nonnegative_complex_power (n : ℕ) (g : ℝ → ℂ)
    (h : ℝ → ℝ) (x₀ : ℝ) (hg : ContinuousAt g x₀) (hg0 : g x₀ ≠ 0)
    (hn : ∀ᶠ x in nhds x₀, 0 ≤ h x)
    (heq : ∀ᶠ x in nhds x₀, (h x : ℂ) = ((x - x₀) ^ n : ℝ) * g x) :
    Even n := by
  let G : ℝ → ℝ := fun x => (g x * star (g x₀)).re
  have hG : ContinuousAt G x₀ := by
    apply Complex.continuous_re.continuousAt.comp
    exact hg.mul continuousAt_const
  have hG0 : G x₀ ≠ 0 := by
    dsimp only [G]
    rw [Complex.star_def, Complex.mul_conj]
    simpa using (Complex.normSq_pos.mpr hg0).ne'
  have hidentity : ∀ᶠ x in nhds x₀, (x - x₀) ^ n * G x = h x * (g x₀).re := by
    filter_upwards [heq] with x hx
    have hh := congrArg (fun z : ℂ => (z * star (g x₀)).re) hx
    simpa only [G, mul_assoc, Complex.re_ofReal_mul, Complex.star_def, Complex.conj_re]
      using hh.symm
  by_cases hsign : 0 ≤ (g x₀).re
  · apply even_of_local_nonnegative_power n G x₀ hG hG0
    filter_upwards [hn, hidentity] with x hnx hix
    rw [hix]
    exact mul_nonneg hnx hsign
  · apply even_of_local_nonnegative_power n (fun x => -G x) x₀ hG.neg (neg_ne_zero.mpr hG0)
    filter_upwards [hn, hidentity] with x hnx hix
    rw [mul_neg, hix]
    exact neg_nonneg.mpr (mul_nonpos_of_nonneg_of_nonpos hnx (le_of_not_ge hsign))

/-- Zeros on the unit circle have even complex root multiplicity when
`p(exp(ix)) = exp(iLx) h(x)` and `h` is nonnegative for every real `x`.
This statement does not assume the conclusion or root-pair symmetry. -/
theorem unit_circle_rootMultiplicity_even_at_angle (p : Polynomial ℂ) (hp : p ≠ 0)
    (L : ℕ) (h : ℝ → ℝ) (hn : ∀ x : ℝ, 0 ≤ h x)
    (hrep : ∀ x : ℝ, p.eval (Complex.exp ((x : ℂ) * Complex.I)) =
      Complex.exp ((x : ℂ) * Complex.I) ^ L * (h x : ℂ)) (x₀ : ℝ) :
    Even (p.rootMultiplicity (Complex.exp ((x₀ : ℂ) * Complex.I))) := by
  let z : ℝ → ℂ := fun x => Complex.exp ((x : ℂ) * Complex.I)
  let m := p.rootMultiplicity (z x₀)
  obtain ⟨q, hpq, hq⟩ := p.exists_eq_pow_rootMultiplicity_mul_and_not_dvd hp (z x₀)
  have hq0 : q.eval (z x₀) ≠ 0 := by
    intro hzero
    exact hq (Polynomial.dvd_iff_isRoot.mpr hzero)
  have hzderiv : HasDerivAt z (z x₀ * Complex.I) x₀ := by
    simpa only [z, id_eq, Complex.ofReal_one, one_mul] using
      (((hasDerivAt_id x₀).ofReal_comp).mul_const Complex.I).cexp
  have hzc : Continuous z := by dsimp [z]; fun_prop
  let a : ℝ → ℂ := dslope z x₀
  have hac : ContinuousAt a x₀ := continuousAt_dslope_same.mpr hzderiv.differentiableAt
  have ha0 : a x₀ ≠ 0 := by
    rw [show a x₀ = deriv z x₀ from dslope_same z x₀, hzderiv.deriv]
    exact mul_ne_zero (Complex.exp_ne_zero _) Complex.I_ne_zero
  let G : ℝ → ℂ := fun x => (z x ^ L)⁻¹ * a x ^ m * q.eval (z x)
  have hGc : ContinuousAt G x₀ := by
    exact ((hzc.continuousAt.pow L).inv₀ (pow_ne_zero _ (Complex.exp_ne_zero _))).mul
      (hac.pow m) |>.mul (q.continuous.comp hzc).continuousAt
  have hG0 : G x₀ ≠ 0 := by
    exact mul_ne_zero (mul_ne_zero (inv_ne_zero (pow_ne_zero _ (Complex.exp_ne_zero _)))
      (pow_ne_zero m ha0)) hq0
  apply even_of_local_nonnegative_complex_power m G h x₀ hGc hG0
    (Filter.Eventually.of_forall hn)
  apply Filter.Eventually.of_forall
  intro x
  have hd : ((x - x₀ : ℝ) : ℂ) * a x = z x - z x₀ := by
    simpa only [a, Complex.real_smul] using sub_smul_dslope z x₀ x
  have hrepr := hrep x
  change p.eval (z x) = z x ^ L * (h x : ℂ) at hrepr
  rw [hpq, Polynomial.eval_mul, Polynomial.eval_pow, Polynomial.eval_sub,
    Polynomial.eval_X, Polynomial.eval_C, ← hd] at hrepr
  apply mul_left_cancel₀ (pow_ne_zero L (Complex.exp_ne_zero ((x : ℂ) * Complex.I)))
  rw [← hrepr]
  dsimp only [G, m, z]
  rw [mul_pow, Complex.ofReal_pow]
  field_simp [Complex.exp_ne_zero] <;> ring

end ChowlaCosine.P31

namespace ChowlaCosine.P31

/-- The angle version extends to every point on the actual unit circle. -/
theorem unit_circle_rootMultiplicity_even (p : Polynomial ℂ) (hp : p ≠ 0)
    (L : ℕ) (h : ℝ → ℝ) (hn : ∀ x : ℝ, 0 ≤ h x)
    (hrep : ∀ x : ℝ, p.eval (Complex.exp ((x : ℂ) * Complex.I)) =
      Complex.exp ((x : ℂ) * Complex.I) ^ L * (h x : ℂ))
    (a : ℂ) (ha : ‖a‖ = 1) : Even (p.rootMultiplicity a) := by
  have hexp : Complex.exp ((a.arg : ℂ) * Complex.I) = a := by
    simpa only [ha, Complex.ofReal_one, one_mul] using Complex.norm_mul_exp_arg_mul_I a
  have he := unit_circle_rootMultiplicity_even_at_angle p hp L h hn hrep a.arg
  rwa [hexp] at he

/-- Boundary parity is discharged: only the shifted polynomial data and
its root symmetry remain hypotheses of this factorization reduction. -/
theorem factorization_of_polynomial_root_symmetry (L : ℕ) (h : ℝ → ℝ)
    (p : Polynomial ℂ) (hp : p ≠ 0) (hdegree : p.natDegree = 2 * L)
    (hstable : p.roots.map rootReflection = p.roots)
    (hnz : ∀ a ∈ p.roots, a ≠ 0) (hn : ∀ x : ℝ, 0 ≤ h x)
    (hrep : ∀ x : ℝ, p.eval (Complex.exp ((x : ℂ) * Complex.I)) =
      Complex.exp ((x : ℂ) * Complex.I) ^ L * (h x : ℂ)) :
    ∃ u : Fin (L + 1) → ℂ, ∀ x : ℝ, h x = ‖analyticValue u x‖ ^ 2 := by
  apply factorization_of_polynomial_root_conditions L h p hdegree hstable hnz _ hn hrep
  intro a ha
  rw [Polynomial.count_roots]
  exact unit_circle_rootMultiplicity_even p hp L h hn hrep a ha

end ChowlaCosine.P31

namespace ChowlaCosine.P31

private theorem reflected_linear_factor (a z : ℂ) (ha : a ≠ 0) (hz : ‖z‖ = 1) :
    -(star a) * (z - rootReflection a) = z * star (z - a) := by
  have han : star a ≠ 0 := star_ne_zero.mpr ha
  have hp : z * star z = 1 := by
    simpa only [Complex.star_def, Complex.mul_conj, Complex.normSq_eq_norm_sq, hz,
      one_pow, Complex.ofReal_one]
  simp only [rootReflection, star_sub]
  field_simp [han]
  linear_combination -hp

private theorem reflected_root_product (s : Multiset ℂ) (z : ℂ) (hz : ‖z‖ = 1)
    (hnz : ∀ a ∈ s, a ≠ 0) :
    (s.map (fun a => -(star a) * (z - rootReflection a))).prod =
      z ^ s.card * star ((s.map (fun a => z - a)).prod) := by
  induction s using Multiset.induction_on with
  | empty => simp
  | @cons a s ih =>
    have ha : a ≠ 0 := hnz a (by simp)
    have hs : ∀ b ∈ s, b ≠ 0 := fun b hb => hnz b (by simp [hb])
    simp only [Multiset.map_cons, Multiset.prod_cons, Multiset.card_cons, star_mul, pow_succ]
    rw [reflected_linear_factor a z ha hz, ih hs]
    ring

private theorem polynomial_eq_of_circle_eval (p q : Polynomial ℂ)
    (heq : ∀ x : ℝ, p.eval (Complex.exp ((x : ℂ) * Complex.I)) =
      q.eval (Complex.exp ((x : ℂ) * Complex.I))) : p = q := by
  have hi : Set.InjOn (fun x : ℝ => Complex.exp ((x : ℂ) * Complex.I)) (Set.Icc 0 π) := by
    intro x hx y hy hxy
    apply Circle.exp_injOn_Icc (by linarith [Real.pi_pos] : π - 0 < 2 * π) hx hy
    apply Subtype.ext
    simpa only [Circle.coe_exp] using hxy
  apply p.eq_of_infinite_eval_eq q
  apply ((Set.Icc_infinite Real.pi_pos).image hi).mono
  rintro z ⟨x, hx, rfl⟩
  exact heq x

/-- Root symmetry follows from the full-circle real-valued representation;
it is not an extra axiom. No positivity of `h` is needed for this lemma. -/
theorem root_symmetry_of_real_circle_representation (p : Polynomial ℂ) (hp : p ≠ 0)
    (L : ℕ) (h : ℝ → ℝ) (hdegree : p.natDegree = 2 * L)
    (hnz : ∀ a ∈ p.roots, a ≠ 0)
    (hrep : ∀ x : ℝ, p.eval (Complex.exp ((x : ℂ) * Complex.I)) =
      Complex.exp ((x : ℂ) * Complex.I) ^ L * (h x : ℂ)) :
    p.roots.map rootReflection = p.roots := by
  classical
  let c : ℂ := star p.leadingCoeff * (p.roots.map (fun a => -(star a))).prod
  let q : Polynomial ℂ := Polynomial.C c *
    (p.roots.map (fun a => Polynomial.X - Polynomial.C (rootReflection a))).prod
  have hc : c ≠ 0 := by
    apply mul_ne_zero (star_ne_zero.mpr (Polynomial.leadingCoeff_ne_zero.mpr hp))
    apply Multiset.prod_ne_zero
    intro hz
    obtain ⟨b, hb, hb0⟩ := Multiset.mem_map.mp hz
    exact (neg_ne_zero.mpr (star_ne_zero.mpr (hnz b hb))) hb0
  have heval : ∀ z : ℂ, ‖z‖ = 1 → q.eval z = z ^ p.roots.card * star (p.eval z) := by
    intro z hz
    have hs : (p.roots.map (fun a => -(star a))).prod *
        (p.roots.map (fun a => z - rootReflection a)).prod =
        z ^ p.roots.card * star ((p.roots.map (fun a => z - a)).prod) := by
      rw [← Multiset.prod_map_mul]
      exact reflected_root_product p.roots z hz hnz
    simp only [q, Polynomial.eval_mul, Polynomial.eval_C, Polynomial.eval_multiset_prod,
      Multiset.map_map, Polynomial.eval_sub, Polynomial.eval_X, Polynomial.eval_C,
      Function.comp_def]
    dsimp only [c]
    rw [mul_assoc, hs, (IsAlgClosed.splits p).eval_eq_prod_roots, star_mul]
    ring
  have hpq : p = q := by
    apply polynomial_eq_of_circle_eval
    intro x
    let z := Complex.exp ((x : ℂ) * Complex.I)
    have hz : ‖z‖ = 1 := by simp [z, Complex.norm_exp]
    have hzprod : z * star z = 1 := by
      simpa only [Complex.star_def, Complex.mul_conj, Complex.normSq_eq_norm_sq, hz,
        one_pow, Complex.ofReal_one]
    have hcroots : p.roots.card = 2 * L :=
      (IsAlgClosed.splits p).natDegree_eq_card_roots.symm.trans hdegree
    have hzx : p.eval z = z ^ L * (h x : ℂ) := hrep x
    rw [heval z hz, hcroots, hzx]
    have hstar : star (h x : ℂ) = (h x : ℂ) := by simp
    simp only [star_mul, star_pow, hstar]
    have hpow : z ^ (2 * L) * star z ^ L = z ^ L := by
      rw [show 2 * L = L + L by omega, pow_add]
      calc z ^ L * z ^ L * star z ^ L = z ^ L * (z * star z) ^ L := by rw [mul_pow]; ring
           _ = z ^ L := by rw [hzprod]; simp
    linear_combination -(h x : ℂ) * hpow
  have hqroots : q.roots = p.roots.map rootReflection := by
    rw [show q = Polynomial.C c *
      ((p.roots.map rootReflection).map (fun a => Polynomial.X - Polynomial.C a)).prod by
        simp only [q, Multiset.map_map, Function.comp_def],
      Polynomial.roots_C_mul _ hc, Polynomial.roots_multiset_prod_X_sub_C]
  rw [← hqroots, ← hpq]

end ChowlaCosine.P31

namespace ChowlaCosine.P31

/-- Finite frequency-band membership gives a genuine shifted ordinary
polynomial, with degree at most `2L`, uniformly for every real angle. -/
theorem exists_shifted_polynomial {L : ℕ} {f : ℝ → ℂ} (hf : f ∈ trigBand L) :
    ∃ p : Polynomial ℂ, p.natDegree ≤ 2 * L ∧ ∀ x : ℝ,
      p.eval (Complex.exp ((x : ℂ) * Complex.I)) =
        Complex.exp ((x : ℂ) * Complex.I) ^ L * f x := by
  induction hf using Submodule.span_induction with
  | mem f hf =>
    obtain ⟨k, hk, rfl⟩ := hf
    let m : ℕ := ((L : ℤ) + k).toNat
    have hklo : -(L : ℤ) ≤ k := (abs_le.mp hk).1
    have hkhi : k ≤ (L : ℤ) := (abs_le.mp hk).2
    have hm : (m : ℤ) = (L : ℤ) + k := Int.toNat_of_nonneg (by omega)
    have hmle : m ≤ 2 * L := by omega
    refine ⟨Polynomial.X ^ m, by simpa using hmle, ?_⟩
    intro x
    simp only [Polynomial.eval_pow, Polynomial.eval_X, circleCharacter]
    rw [← Complex.exp_nat_mul, ← Complex.exp_nat_mul, ← Complex.exp_add]
    congr 1
    have hc : (m : ℂ) = (L : ℂ) + (k : ℂ) := by exact_mod_cast hm
    rw [hc]
    ring
  | zero =>
    refine ⟨0, by simp, ?_⟩
    intro x
    simp
  | add f g hf hg ihf ihg =>
    obtain ⟨p, hp, hep⟩ := ihf
    obtain ⟨q, hq, heq⟩ := ihg
    refine ⟨p + q, (Polynomial.natDegree_add_le p q).trans (max_le hp hq), ?_⟩
    intro x
    rw [Polynomial.eval_add, hep x, heq x]
    change _ = _ * (f x + g x)
    ring
  | smul c f hf ih =>
    obtain ⟨p, hp, hep⟩ := ih
    refine ⟨Polynomial.C c * p, (Polynomial.natDegree_C_mul_le c p).trans hp, ?_⟩
    intro x
    rw [Polynomial.eval_mul, Polynomial.eval_C, hep x]
    change c * (_ * f x) = _ * (c * f x)
    ring

/-- Zero extension preserves the analytic factor exactly. -/
theorem analytic_factor_mono {K L : ℕ} (hKL : K ≤ L) (h : ℝ → ℝ)
    (hf : ∃ u : Fin (K + 1) → ℂ, ∀ x : ℝ, h x = ‖analyticValue u x‖ ^ 2) :
    ∃ u : Fin (L + 1) → ℂ, ∀ x : ℝ, h x = ‖analyticValue u x‖ ^ 2 := by
  obtain ⟨u, hu⟩ := hf
  let v : ℕ → ℂ := fun n => if hn : n < K + 1 then u ⟨n, hn⟩ else 0
  refine ⟨fun j => v j.val, ?_⟩
  intro x
  have hsmall : analyticValue u x = analyticValue (fun j : Fin (K + 1) => v j.val) x := by
    unfold analyticValue
    apply Finset.sum_congr rfl
    intro j hj
    simp only [v, dif_pos j.isLt]
  have hsum : ∀ N : ℕ, analyticValue (fun j : Fin (N + 1) => v j.val) x =
      ∑ n ∈ Finset.range (N + 1), v n * Complex.exp ((n : ℂ) * (x : ℂ) * Complex.I) := by
    intro N
    unfold analyticValue
    exact Fin.sum_univ_eq_sum_range
      (fun n : ℕ => v n * Complex.exp ((n : ℂ) * (x : ℂ) * Complex.I)) (N + 1)
  rw [hu x, hsmall, hsum, hsum]
  congr 2
  apply Finset.sum_subset (Finset.range_mono (Nat.succ_le_succ hKL))
  intro n hn hnot
  have hk : ¬n < K + 1 := by simpa only [Finset.mem_range] using hnot
  simp only [v, dif_neg hk, zero_mul]

end ChowlaCosine.P31

namespace ChowlaCosine.P31

/-- Padded conjugate-reflection symmetry follows from reality on the full circle. -/
theorem shifted_polynomial_reflection (L : ℕ) (h : ℝ → ℝ) (p : Polynomial ℂ)
    (hp : p.natDegree ≤ 2 * L)
    (hrep : ∀ x : ℝ, p.eval (Complex.exp ((x : ℂ) * Complex.I)) =
      Complex.exp ((x : ℂ) * Complex.I) ^ L * (h x : ℂ)) :
    p = (p.reflect (2 * L)).map (starRingEnd ℂ) := by
  apply polynomial_eq_of_circle_eval
  intro x
  let z := Complex.exp ((x : ℂ) * Complex.I)
  have hz : ‖z‖ = 1 := by simp [z, Complex.norm_exp]
  have hzprod : z * star z = 1 := by
    simpa only [Complex.star_def, Complex.mul_conj, Complex.normSq_eq_norm_sq, hz,
      one_pow, Complex.ofReal_one]
  have hinv : (star z)⁻¹ = z := inv_eq_of_mul_eq_one_left hzprod
  letI : Invertible (star z) := invertibleOfNonzero (star_ne_zero.mpr (Complex.exp_ne_zero _))
  have H := Polynomial.eval₂_reflect_mul_pow (starRingEnd ℂ) (star z) (2 * L) p hp
  simp only [invOf_eq_inv, hinv] at H
  have Heval := Polynomial.eval₂_at_apply (p := p) (starRingEnd ℂ) z
  simp only [starRingEnd_apply] at Heval
  rw [Heval] at H
  rw [← Polynomial.eval_map] at H
  have hzz : star z ^ (2 * L) * z ^ (2 * L) = 1 := by
    rw [← mul_pow, mul_comm (star z) z, hzprod, one_pow]
  have hreflect : ((p.reflect (2 * L)).map (starRingEnd ℂ)).eval z =
      z ^ (2 * L) * star (p.eval z) := by
    calc
      _ = (((p.reflect (2 * L)).map (starRingEnd ℂ)).eval z * star z ^ (2 * L)) *
          z ^ (2 * L) := by rw [mul_assoc, hzz, mul_one]
      _ = _ := by rw [H]; ring
  have hrepr : p.eval z = z ^ L * (h x : ℂ) := hrep x
  change p.eval z = _
  rw [hreflect, hrepr]
  have hstar : star (h x : ℂ) = (h x : ℂ) := by simp
  simp only [star_mul, star_pow, hstar]
  have hpow : z ^ (2 * L) * star z ^ L = z ^ L := by
    rw [show 2 * L = L + L by omega, pow_add]
    calc z ^ L * z ^ L * star z ^ L = z ^ L * (z * star z) ^ L := by rw [mul_pow]; ring
         _ = z ^ L := by rw [hzprod]; simp
  linear_combination -(h x : ℂ) * hpow

/-- Coefficient version of the padded symmetry; no positivity is needed. -/
theorem shifted_polynomial_coeff_symmetry (L : ℕ) (h : ℝ → ℝ) (p : Polynomial ℂ)
    (hp : p.natDegree ≤ 2 * L)
    (hrep : ∀ x : ℝ, p.eval (Complex.exp ((x : ℂ) * Complex.I)) =
      Complex.exp ((x : ℂ) * Complex.I) ^ L * (h x : ℂ))
    (i : ℕ) (hi : i ≤ 2 * L) : p.coeff i = star (p.coeff (2 * L - i)) := by
  have heq := congrArg (fun q : Polynomial ℂ => q.coeff i)
    (shifted_polynomial_reflection L h p hp hrep)
  simpa only [Polynomial.coeff_map, Polynomial.coeff_reflect, Polynomial.revAt_le hi, starRingEnd_apply] using heq

end ChowlaCosine.P31

namespace ChowlaCosine.P31

/-- Finite Fejér–Riesz, with analytic support `0,...,L`, allowing every
zero configuration and including the identically zero polynomial. -/
theorem finite_fejerRiesz (L : ℕ) : FejerRiesz L := by
  intro h hh hn
  by_cases hzero : ∀ x : ℝ, h x = 0
  · refine ⟨fun _ => 0, ?_⟩
    intro x
    simp [hzero x, analyticValue]
  obtain ⟨p, hpdeg, hrep⟩ := exists_shifted_polynomial hh
  have hp0 : p ≠ 0 := by
    intro heq
    apply hzero
    intro x
    have hx := hrep x
    rw [heq, Polynomial.eval_zero] at hx
    have hhx : (h x : ℂ) = 0 := (mul_eq_zero.mp hx.symm).resolve_left
      (pow_ne_zero L (Complex.exp_ne_zero _))
    exact_mod_cast hhx
  let d := p.natDegree
  let a := 2 * L - d
  have had : a + d = 2 * L := Nat.sub_add_cancel hpdeg
  have haN : a ≤ 2 * L := Nat.sub_le _ _
  have haindex : 2 * L - a = d := by omega
  have hca : p.coeff a ≠ 0 := by
    rw [shifted_polynomial_coeff_symmetry L h p hpdeg hrep a haN, haindex]
    exact star_ne_zero.mpr (Polynomial.leadingCoeff_ne_zero.mpr hp0)
  have hadle : a ≤ d := Polynomial.le_natDegree_of_ne_zero hca
  have haL : a ≤ L := by omega
  have hdiv : Polynomial.X ^ a ∣ p := by
    apply Polynomial.X_pow_dvd_iff.mpr
    intro i hi
    rw [shifted_polynomial_coeff_symmetry L h p hpdeg hrep i (by omega)]
    have hdi : p.natDegree < 2 * L - i := by omega
    rw [Polynomial.coeff_eq_zero_of_natDegree_lt hdi, star_zero]
  obtain ⟨q, hpq⟩ := hdiv
  have hq0 : q ≠ 0 := by
    intro hq
    apply hp0
    rw [hpq, hq, mul_zero]
  have hcoeff : p.coeff a = q.coeff 0 := by
    rw [hpq]
    simpa only [zero_add] using Polynomial.coeff_X_pow_mul q a 0
  have hqa0 : q.coeff 0 ≠ 0 := by rwa [hcoeff] at hca
  have hdegpq : p.natDegree = a + q.natDegree := by
    rw [hpq, Polynomial.natDegree_mul (pow_ne_zero a Polynomial.X_ne_zero) hq0,
      Polynomial.natDegree_X_pow]
  have hqdegree : q.natDegree = 2 * (L - a) := by omega
  have hqnz : ∀ b ∈ q.roots, b ≠ 0 := by
    intro b hb hb0
    subst b
    have hr := (Polynomial.mem_roots hq0).mp hb
    apply hqa0
    rw [Polynomial.coeff_zero_eq_eval_zero]
    exact hr
  have hqrep : ∀ x : ℝ, q.eval (Complex.exp ((x : ℂ) * Complex.I)) =
      Complex.exp ((x : ℂ) * Complex.I) ^ (L - a) * (h x : ℂ) := by
    intro x
    have hx := hrep x
    rw [hpq, Polynomial.eval_mul, Polynomial.eval_pow, Polynomial.eval_X,
      show L = a + (L - a) by omega, pow_add, mul_assoc] at hx
    exact mul_left_cancel₀ (pow_ne_zero a (Complex.exp_ne_zero _)) hx
  have hqsym := root_symmetry_of_real_circle_representation q hq0 (L - a) h hqdegree hqnz hqrep
  apply analytic_factor_mono (Nat.sub_le L a) h
  exact factorization_of_polynomial_root_symmetry (L - a) h q hq0 hqdegree hqsym hqnz hn hqrep


end ChowlaCosine.P31

namespace ChowlaCosine.P31

/-- T1 in explicit finite Fourier-coefficient form. `h` is real-valued,
its equality to the complex Fourier sum holds for every real angle, and
nonnegativity is likewise on the entire real line. -/
theorem finite_fejerRiesz_of_coefficients (L : ℕ) (c : ℤ → ℂ) (h : ℝ → ℝ)
    (heq : ∀ x : ℝ, (h x : ℂ) =
      ∑ k ∈ Finset.Icc (-(L : ℤ)) (L : ℤ), c k * circleCharacter k x)
    (hn : ∀ x : ℝ, 0 ≤ h x) :
    ∃ u : Fin (L + 1) → ℂ, ∀ x : ℝ, h x = ‖analyticValue u x‖ ^ 2 := by
  apply finite_fejerRiesz L h _ hn
  have hb : (∑ k ∈ Finset.Icc (-(L : ℤ)) (L : ℤ), c k • circleCharacter k) ∈ trigBand L := by
    apply Submodule.sum_mem
    intro k hk
    apply (trigBand L).smul_mem
    apply character_mem_trigBand
    exact abs_le.mpr (Finset.mem_Icc.mp hk)
  convert hb using 1
  funext x
  rw [heq]
  simp only [Finset.sum_apply, Pi.smul_apply, smul_eq_mul]

end ChowlaCosine.P31
