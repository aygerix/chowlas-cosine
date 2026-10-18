import Mathlib

/-!
Finite Fourier positive definiteness for the run-top fibre inequalities.
The Fourier transform here is unnormalized and uses conjugated characters.
-/

namespace ChowlaCosine.FibreSchur

open Finset
open scoped ComplexConjugate
attribute [local instance] Classical.propDecidable

variable {H : Type*} [AddCommGroup H] [Fintype H]

/-- The unnormalized transform, with the convention in the formalization brief. -/
noncomputable def fourier (P : H → ℂ) (ψ : AddChar H ℂ) : ℂ :=
  ∑ y, P y * conj (ψ y)

/-- Fourier positive definiteness: every coefficient is a nonnegative real. -/
def PositiveDefinite (P : H → ℂ) : Prop :=
  ∀ ψ : AddChar H ℂ, (fourier P ψ).im = 0 ∧ 0 ≤ (fourier P ψ).re

/-- Fourier inversion without division by the group order. -/
theorem fourier_inversion (P : H → ℂ) (x : H) :
    ∑ ψ : AddChar H ℂ, fourier P ψ * ψ x = (Fintype.card H : ℂ) * P x := by
  classical
  simp only [fourier, sum_mul]
  rw [sum_comm]
  -- Express character orthogonality at the difference `x - y`.
  have hterm' : ∀ y : H,
      (∑ ψ : AddChar H ℂ, P y * conj (ψ y) * ψ x) =
        P y * (if x = y then (Fintype.card H : ℂ) else 0) := by
    intro y
    calc
      _ = P y * ∑ ψ : AddChar H ℂ, ψ (x - y) := by
        rw [mul_sum]
        apply sum_congr rfl
        intro ψ _
        rw [AddChar.map_sub_eq_div, div_eq_mul_inv, AddChar.inv_apply_eq_conj]
        ring
      _ = _ := by rw [AddChar.sum_apply_eq_ite]; simp only [sub_eq_zero]
  simp_rw [hterm']
  rw [sum_eq_single x]
  · simp [mul_comm]
  · intro y _ hy
    simp [Ne.symm hy]
  · simp

/-- The transform of a pointwise product, without division by the group order. -/
theorem fourier_mul_card (P Q : H → ℂ) (ψ : AddChar H ℂ) :
    (Fintype.card H : ℂ) * fourier (fun y => P y * Q y) ψ =
      ∑ χ : AddChar H ℂ, fourier P χ * fourier Q (ψ / χ) := by
  classical
  change (Fintype.card H : ℂ) * (∑ y, P y * Q y * conj (ψ y)) =
    ∑ χ : AddChar H ℂ, fourier P χ * ∑ y, Q y * conj ((ψ / χ) y)
  simp_rw [mul_sum]
  rw [sum_comm]
  apply sum_congr rfl
  intro y _
  have hy := fourier_inversion P y
  calc
    (Fintype.card H : ℂ) * (P y * Q y * conj (ψ y)) =
        (∑ χ : AddChar H ℂ, fourier P χ * χ y) * Q y * conj (ψ y) := by
      rw [hy]
      ring
    _ = _ := by
      simp only [sum_mul]
      apply sum_congr rfl
      intro χ _
      simp only [AddChar.div_apply, map_mul, AddChar.map_neg_eq_conj,
        starRingEnd_apply, star_star]
      ring

/-- **T0: Schur's theorem**, using the Fourier definition on any finite abelian group. -/
theorem PositiveDefinite.mul {P Q : H → ℂ} (hP : PositiveDefinite P)
    (hQ : PositiveDefinite Q) : PositiveDefinite (fun y => P y * Q y) := by
  intro ψ
  have hn : (0 : ℝ) < Fintype.card H := Nat.cast_pos.mpr Fintype.card_pos
  have he := fourier_mul_card P Q ψ
  have hi := congrArg Complex.im he
  have hr := congrArg Complex.re he
  rw [Complex.mul_im, Complex.natCast_re, Complex.natCast_im, zero_mul,
    add_zero, Complex.im_sum] at hi
  rw [Complex.mul_re, Complex.natCast_re, Complex.natCast_im, zero_mul,
    sub_zero, Complex.re_sum] at hr
  have hzi : ∑ χ : AddChar H ℂ, (fourier P χ * fourier Q (ψ / χ)).im = 0 := by
    apply sum_eq_zero
    intro χ _
    simp [Complex.mul_im, (hP χ).1, (hQ (ψ / χ)).1]
  have hzr : 0 ≤ ∑ χ : AddChar H ℂ, (fourier P χ * fourier Q (ψ / χ)).re := by
    apply sum_nonneg
    intro χ _
    simpa [Complex.mul_re, (hP χ).1, (hQ (ψ / χ)).1] using
      mul_nonneg (hP χ).2 (hQ (ψ / χ)).2
  constructor
  · rw [hzi] at hi
    exact (mul_eq_zero.mp hi).resolve_left (ne_of_gt hn)
  · nlinarith

theorem positiveDefinite_one : PositiveDefinite (fun _ : H => 1) := by
  classical
  intro ψ
  have he : fourier (fun _ : H => 1) ψ =
      if ψ = 0 then (Fintype.card H : ℂ) else 0 := by
    simp only [fourier, one_mul, ← map_sum]
    rw [AddChar.sum_eq_ite]
    split_ifs <;> simp
  rw [he]
  split_ifs <;> simp

/-- Every natural pointwise power of a Fourier positive definite function is p.d. -/
theorem PositiveDefinite.pow {P : H → ℂ} (hP : PositiveDefinite P) (r : ℕ) :
    PositiveDefinite (fun y => P y ^ r) := by
  induction r with
  | zero => simpa using (positiveDefinite_one (H := H))
  | succ r ih => simpa only [pow_succ] using ih.mul hP

/-- The sum defining a character transform of a finite set. -/
noncomputable def setFourier (A : Finset H) (χ : AddChar H ℂ) : ℂ := ∑ x ∈ A, χ x

/-- Symmetry of the set makes all its character sums real. -/
theorem setFourier_im_eq_zero (A : Finset H) (hsym : ∀ x ∈ A, -x ∈ A)
    (χ : AddChar H ℂ) : (setFourier A χ).im = 0 := by
  classical
  rw [← Complex.conj_eq_iff_im]
  unfold setFourier
  rw [map_sum]
  apply sum_nbij' (fun x => -x) (fun x => -x)
  · exact fun x hx => hsym x hx
  · exact fun x hx => hsym x hx
  · intro x _; simp
  · intro x _; simp
  · intro x _; exact (AddChar.map_neg_eq_conj χ x).symm

/-- The fibre function on a quotient, expressed using its quotient homomorphism. -/
noncomputable def fibre {G : Type*} [AddCommGroup G] [Fintype G]
    (q : G →+ H) (A : Finset G) (χ : AddChar G ℂ) (y : H) : ℂ :=
  ∑ x ∈ A with q x = y, χ x

theorem fourier_fibre {G : Type*} [AddCommGroup G] [Fintype G]
    (q : G →+ H) (A : Finset G) (χ : AddChar G ℂ) (ψ : AddChar H ℂ) :
    fourier (fibre q A χ) ψ = setFourier A (χ / ψ.compAddMonoidHom q) := by
  classical
  unfold fourier fibre setFourier
  simp only [sum_mul, sum_filter]
  rw [sum_comm]
  apply sum_congr rfl
  intro x hx
  simp [AddChar.div_apply, AddChar.map_neg_eq_conj]

omit [Fintype H] in
/-- A character nontrivial on a kernel element stays nontrivial after any quotient twist. -/
theorem twist_ne_zero {G : Type*} [AddCommGroup G]
    (q : G →+ H) (χ : AddChar G ℂ) (t : G) (ht : q t = 0) (hχ : χ t ≠ 1)
    (ψ : AddChar H ℂ) : χ / ψ.compAddMonoidHom q ≠ 0 := by
  intro he
  have he' := DFunLike.congr_fun he t
  simp [AddChar.div_apply, ht] at he'
  exact hχ he'

/-- The positive definite shifted fibre used in both T1 and T2. -/
theorem shifted_fibre_positiveDefinite {G : Type*} [AddCommGroup G] [Fintype G]
    (q : G →+ H) (A : Finset G) (hsym : ∀ x ∈ A, -x ∈ A)
    (χ : AddChar G ℂ) (t : G) (ht : q t = 0) (hχ : χ t ≠ 1)
    (K : ℝ) (hK : ∀ η : AddChar G ℂ, η ≠ 0 → -K ≤ (setFourier A η).re) :
    PositiveDefinite (fun y => fibre q A χ y + if y = 0 then (K : ℂ) else 0) := by
  classical
  intro ψ
  have he : fourier (fun y => fibre q A χ y + if y = 0 then (K : ℂ) else 0) ψ =
      setFourier A (χ / ψ.compAddMonoidHom q) + K := by
    simp only [fourier, add_mul, sum_add_distrib, ite_mul, zero_mul]
    rw [show (∑ y, fibre q A χ y * conj (ψ y)) =
      setFourier A (χ / ψ.compAddMonoidHom q) from fourier_fibre q A χ ψ]
    simp
  rw [he]
  constructor
  · simp [setFourier_im_eq_zero A hsym]
  · simp only [Complex.add_re, Complex.ofReal_re]
    linarith [hK _ (twist_ne_zero q χ t ht hχ ψ)]

/-- The final Schur-power step, separated from the coset fibre classification.
`c` records the real fibre table away from zero, and is zero at the origin. -/
theorem power_certificate_bound (U : H → ℂ) (K u₀ : ℝ) (r : ℕ)
    (ρ : AddChar H ℂ) (c : H → ℝ) (hc₀ : c 0 = 0) (hU₀ : U 0 = (u₀ : ℂ))
    (hpd : PositiveDefinite (fun y => U y + if y = 0 then (K : ℂ) else 0))
    (htable : ∀ y, y ≠ 0 → U y ^ r * conj (ρ y) = (c y : ℂ)) :
    -(∑ y, c y) ≤ (K + u₀) ^ r := by
  classical
  have hp := (hpd.pow r ρ).2
  have he : fourier (fun y => (U y + if y = 0 then (K : ℂ) else 0) ^ r) ρ =
      ((K + u₀) ^ r + ∑ y, c y : ℝ) := by
    unfold fourier
    rw [← add_sum_erase _ _ (mem_univ (0 : H))]
    simp only [hU₀, ite_true, AddChar.map_zero_eq_one, map_one, mul_one]
    have hsum : ∑ y ∈ univ.erase 0,
        (U y + if y = 0 then (K : ℂ) else 0) ^ r * conj (ρ y) =
          ∑ y ∈ univ.erase 0, (c y : ℂ) := by
      apply sum_congr rfl
      intro y hy
      simpa [ne_of_mem_erase hy] using htable y (ne_of_mem_erase hy)
    rw [hsum, sum_erase_eq_sub (mem_univ 0)]
    push_cast
    rw [hc₀]
    push_cast
    ring
  rw [he, Complex.ofReal_re] at hp
  linarith

/-- A character sum inside a fibre of size `n`, after selecting its first point. -/
noncomputable def cyclicFibreSum {n : ℕ} (z : ℂ) (S : Finset (Fin n)) : ℂ :=
  ∑ s ∈ S, z ^ s.val

/-- Exact order-three local table, for an arbitrary primitive cube root. -/
theorem fibre_table_three (z : ℂ) (hz : z ^ 2 + z + 1 = 0) (S : Finset (Fin 3)) :
    cyclicFibreSum z S ^ 3 =
      if S.card = 1 then 1 else if S.card = 2 then -1 else 0 := by
  have hz3 : z ^ 3 = 1 := by linear_combination (z - 1) * hz
  have hzsum : 1 + (z + z ^ 2) = 0 := by linear_combination hz
  have hzpow : (z ^ 2) ^ 3 = 1 := by rw [← pow_mul, mul_comm 2 3, pow_mul, hz3]; norm_num
  have hzpair : (1 + z) ^ 3 = -1 := by
    linear_combination (z + 2) * hz
  have hzpair' : (1 + z ^ 2) ^ 3 = -1 := by
    linear_combination (z ^ 4 - z ^ 3 + 3 * z ^ 2 - 2 * z + 2) * hz
  have hzpair'' : (z + z ^ 2) ^ 3 = -1 := by rw [show z + z ^ 2 = -1 by linear_combination hz]; norm_num
  fin_cases S <;>
    simp [cyclicFibreSum, hz3, hzsum, hzpair, hzpair', hzpair'', hzpow]

/-- A two-point fibre is a run precisely when it contains a cyclic adjacent pair. -/
def IsTwoRun (S : Finset (Fin 4)) : Prop :=
  S.card = 2 ∧
    ((0 ∈ S ∧ 1 ∈ S) ∨ (1 ∈ S ∧ 2 ∈ S) ∨ (2 ∈ S ∧ 3 ∈ S) ∨ (0 ∈ S ∧ 3 ∈ S))

/-- Exact order-four local table, including the opposite-pair case. -/
theorem fibre_table_four (S : Finset (Fin 4)) :
    cyclicFibreSum Complex.I S ^ 4 =
      if S.card = 1 then 1 else if IsTwoRun S then -4 else if S.card = 3 then 1 else 0 := by
  classical
  fin_cases S <;>
    norm_num [cyclicFibreSum, IsTwoRun, Fin.ext_iff,
      Complex.ext_iff, Complex.mul_re, Complex.mul_im, pow_succ]

section QuotientFibres

variable {G : Type*} [AddCommGroup G] [Fintype G]

/-- The actual quotient by the cyclic subgroup generated by `t`. -/
abbrev Cosets (t : G) := G ⧸ AddSubgroup.zmultiples t

noncomputable instance cosetsFintype (t : G) : Fintype (Cosets t) := Fintype.ofFinite _

noncomputable def projection (t : G) : G →+ Cosets t :=
  QuotientAddGroup.mk' (AddSubgroup.zmultiples t)

noncomputable def fibreSet (A : Finset G) (t : G) (y : Cosets t) : Finset G :=
  A.filter (fun x => projection t x = y)

noncomputable def fibreIndices (n : ℕ) (A : Finset G) (t x : G) : Finset (Fin n) :=
  univ.filter (fun i => x + i.val • t ∈ A)

omit [Fintype G] in
lemma coset_coordinate_injective (t x : G) (n : ℕ) (ht : addOrderOf t = n) :
    Function.Injective (fun i : Fin n => x + i.val • t) := by
  intro i j he
  apply Fin.ext
  apply nsmul_injOn_Iio_addOrderOf (x := t) (by simpa only [Set.mem_Iio, ht] using i.isLt)
    (by simpa only [Set.mem_Iio, ht] using j.isLt)
  exact add_left_cancel he

lemma fibreSet_eq_image (A : Finset G) (t x : G) (n : ℕ) (ht : addOrderOf t = n) :
    fibreSet A t (projection t x) =
      (fibreIndices n A t x).image (fun i => x + i.val • t) := by
  classical
  ext z
  simp only [fibreSet, mem_filter, mem_image, fibreIndices, mem_univ, true_and]
  constructor
  · rintro ⟨hz, hq⟩
    have hm : z - x ∈ AddSubgroup.zmultiples t := by
      exact (QuotientAddGroup.eq_iff_sub_mem).mp hq
    have hmem := (isOfFinAddOrder_of_finite t).mem_zmultiples_iff_mem_range_addOrderOf.mp hm
    obtain ⟨k, hk, he⟩ := mem_image.mp hmem
    refine ⟨⟨k, by simpa [ht] using mem_range.mp hk⟩, ?_, ?_⟩
    · have he' : x + k • t = z := by rw [he]; abel
      simpa only [he'] using hz
    · dsimp
      rw [he]; abel
  · rintro ⟨i, hi, rfl⟩
    refine ⟨hi, ?_⟩
    simp only [projection, map_add, map_nsmul]
    have ht0 : QuotientAddGroup.mk' (AddSubgroup.zmultiples t) t = 0 := by
      exact (QuotientAddGroup.eq_zero_iff t).mpr (AddSubgroup.mem_zmultiples t)
    rw [ht0, nsmul_zero, add_zero]

lemma fibreSet_card (A : Finset G) (t x : G) (n : ℕ) (ht : addOrderOf t = n) :
    (fibreSet A t (projection t x)).card = (fibreIndices n A t x).card := by
  rw [fibreSet_eq_image A t x n ht, card_image_of_injective _ (coset_coordinate_injective t x n ht)]

lemma fibre_eq_cyclicFibreSum (A : Finset G) (χ : AddChar G ℂ) (t x : G)
    (n : ℕ) (ht : addOrderOf t = n) :
    fibre (projection t) A χ (projection t x) =
      χ x * cyclicFibreSum (χ t) (fibreIndices n A t x) := by
  have hdef : fibre (projection t) A χ (projection t x) =
      ∑ z ∈ fibreSet A t (projection t x), χ z := by
    unfold fibre
    apply sum_congr
    · ext z
      simp only [fibreSet, mem_filter]
    · intro z _; rfl
  rw [hdef, fibreSet_eq_image A t x n ht, sum_image]
  · simp only [AddChar.map_add_eq_mul, AddChar.map_nsmul_eq_pow,
      cyclicFibreSum, mul_sum]
  · exact fun i _ j _ he => coset_coordinate_injective t x n ht he

/-- A power of a character which is trivial on the cyclic subgroup descends to the quotient. -/
noncomputable def quotientPower (t : G) (χ : AddChar G ℂ) (r : ℕ)
    (ht : χ t ^ r = 1) : AddChar (Cosets t) ℂ :=
  AddChar.toAddMonoidHomEquiv.symm
    (QuotientAddGroup.lift (AddSubgroup.zmultiples t) (χ ^ r).toAddMonoidHom
      (AddSubgroup.zmultiples_le.mpr (by exact ht)))

omit [Fintype G] in
lemma quotientPower_apply (t : G) (χ : AddChar G ℂ) (r : ℕ)
    (ht : χ t ^ r = 1) (x : G) :
    quotientPower t χ r ht (projection t x) = χ x ^ r := rfl

omit [Fintype G] in
lemma projection_self (t : G) : projection t t = 0 :=
  (QuotientAddGroup.eq_zero_iff t).mpr (AddSubgroup.mem_zmultiples t)

lemma fibre_zero_im_eq_zero (A : Finset G) (hsym : ∀ x ∈ A, -x ∈ A)
    (t : G) (χ : AddChar G ℂ) : (fibre (projection t) A χ 0).im = 0 := by
  rw [← Complex.conj_eq_iff_im]
  unfold fibre
  rw [map_sum]
  apply sum_nbij' (fun x => -x) (fun x => -x)
  · intro x hx
    simp only [mem_filter] at hx ⊢
    exact ⟨hsym x hx.1, by simp [hx.2]⟩
  · intro x hx
    simp only [mem_filter] at hx ⊢
    exact ⟨hsym x hx.1, by simp [hx.2]⟩
  · intro x _; simp
  · intro x _; simp
  · intro x _; exact (AddChar.map_neg_eq_conj χ x).symm

noncomputable def singleCosets (A : Finset G) (t : G) : Finset (Cosets t) :=
  univ.filter (fun y => y ≠ 0 ∧ (fibreSet A t y).card = 1)

noncomputable def doubleCosets (A : Finset G) (t : G) : Finset (Cosets t) :=
  univ.filter (fun y => y ≠ 0 ∧ (fibreSet A t y).card = 2)

noncomputable def tripleCosets (A : Finset G) (t : G) : Finset (Cosets t) :=
  univ.filter (fun y => y ≠ 0 ∧ (fibreSet A t y).card = 3)

noncomputable def omega : ℂ := Complex.exp (2 * Real.pi * Complex.I / 3)

lemma omega_primitive : IsPrimitiveRoot omega 3 := Complex.isPrimitiveRoot_exp 3 (by decide)

lemma cube_root_relation (z : ℂ) (hz : IsPrimitiveRoot z 3) : z ^ 2 + z + 1 = 0 := by
  have he := hz.geom_sum_eq_zero (by norm_num : 1 < 3)
  norm_num [sum_range_succ] at he
  linear_combination he

lemma fibre_cube_table (A : Finset G) (t : G) (ht : addOrderOf t = 3)
    (χ : AddChar G ℂ) (hz : IsPrimitiveRoot (χ t) 3) (y : Cosets t) :
    fibre (projection t) A χ y ^ 3 * conj (quotientPower t χ 3 hz.pow_eq_one y) =
      if (fibreSet A t y).card = 1 then 1
      else if (fibreSet A t y).card = 2 then -1 else 0 := by
  obtain ⟨x, rfl⟩ := QuotientAddGroup.mk'_surjective (AddSubgroup.zmultiples t) y
  change fibre (projection t) A χ (projection t x) ^ 3 *
    conj (quotientPower t χ 3 hz.pow_eq_one (projection t x)) =
      if (fibreSet A t (projection t x)).card = 1 then 1
      else if (fibreSet A t (projection t x)).card = 2 then -1 else 0
  rw [fibre_eq_cyclicFibreSum A χ t x 3 ht, mul_pow,
    fibreSet_card A t x 3 ht, quotientPower_apply]
  have hc : χ x ^ 3 * conj (χ x ^ 3) = 1 := by
    rw [map_pow]
    have h1 : χ x * conj (χ x) = 1 := by
      rw [← AddChar.map_neg_eq_conj, ← AddChar.map_add_eq_mul]
      simp
    rw [← mul_pow, h1, one_pow]
  calc
    _ = cyclicFibreSum (χ t) (fibreIndices 3 A t x) ^ 3 *
        (χ x ^ 3 * conj (χ x ^ 3)) := by ring
    _ = _ := by rw [hc, mul_one, fibre_table_three _ (cube_root_relation _ hz)]

/-- **T1's fibre inequality**, on the actual quotient, with exactly the spectral hypothesis
from the brief. The zero fibre is written as its real part; it is real by symmetry. -/
theorem order_three_fibre_bound (A : Finset G) (hsym : ∀ x ∈ A, -x ∈ A)
    (_hzero : (0 : G) ∉ A) (K : ℝ) (_hKnonneg : 0 ≤ K)
    (hK : ∀ η : AddChar G ℂ, η ≠ 0 → -K ≤ (setFourier A η).re)
    (t : G) (ht : addOrderOf t = 3) (χ : AddChar G ℂ) (hχ : χ t = omega) :
    ((doubleCosets A t).card : ℝ) - (singleCosets A t).card ≤
      (K + (fibre (projection t) A χ 0).re) ^ 3 := by
  have hz : IsPrimitiveRoot (χ t) 3 := hχ.symm ▸ omega_primitive
  let U := fibre (projection t) A χ
  let c : Cosets t → ℝ := fun y =>
    (if y ∈ singleCosets A t then 1 else 0) - (if y ∈ doubleCosets A t then 1 else 0)
  have hc₀ : c 0 = 0 := by simp [c, singleCosets, doubleCosets]
  have hU₀ : U 0 = ((U 0).re : ℂ) := by
    apply Complex.ext <;> simp [U, fibre_zero_im_eq_zero A hsym]
  have hpd := shifted_fibre_positiveDefinite (projection t) A hsym χ t
    (projection_self t) (hz.ne_one (by norm_num)) K hK
  have htable : ∀ y : Cosets t, y ≠ 0 → U y ^ 3 *
      conj (quotientPower t χ 3 hz.pow_eq_one y) = (c y : ℂ) := by
    intro y hy
    rw [fibre_cube_table A t ht χ hz]
    by_cases h1 : (fibreSet A t y).card = 1
    · have h2 : (fibreSet A t y).card ≠ 2 := by omega
      simp [c, singleCosets, doubleCosets, hy, h1]
    · by_cases h2 : (fibreSet A t y).card = 2 <;>
        simp [c, singleCosets, doubleCosets, hy, h1, h2]
  have hb := power_certificate_bound U K (U 0).re 3
    (quotientPower t χ 3 hz.pow_eq_one) c hc₀ hU₀ hpd htable
  have hsum : ∑ y, c y = ((singleCosets A t).card : ℝ) - (doubleCosets A t).card := by
    simp [c, sum_sub_distrib]
  rw [hsum] at hb
  dsimp only [U] at hb
  linarith

omit [Fintype G] in
lemma nsmul_pred_eq_neg (t : G) (n : ℕ) (ht : addOrderOf t = n + 1) : n • t = -t := by
  apply eq_neg_iff_add_eq_zero.mpr
  simpa only [ht, add_nsmul, one_nsmul] using addOrderOf_nsmul_eq_zero t

/-- The order-three zero fibre has exactly the two values stated in T1. -/
theorem order_three_zero_fibre (A : Finset G) (hsym : ∀ x ∈ A, -x ∈ A)
    (hzero : (0 : G) ∉ A) (t : G) (ht : addOrderOf t = 3)
    (χ : AddChar G ℂ) (hχ : χ t = omega) :
    fibre (projection t) A χ 0 = 0 ∨ fibre (projection t) A χ 0 = -1 := by
  have hz : χ t + χ t ^ 2 = -1 := by
    linear_combination cube_root_relation (χ t) (hχ.symm ▸ omega_primitive)
  have h0 : (0 : Fin 3) ∉ fibreIndices 3 A t 0 := by
    simp [fibreIndices, hzero]
  have h12 : (1 : Fin 3) ∈ fibreIndices 3 A t 0 ↔
      (2 : Fin 3) ∈ fibreIndices 3 A t 0 := by
    have hn := nsmul_pred_eq_neg t 2 ht
    have hmem : -t ∈ A ↔ t ∈ A :=
      ⟨fun hx => by simpa using hsym (-t) hx, hsym t⟩
    simpa [fibreIndices, hn, show (2 : Fin 3).val = 2 by rfl] using hmem.symm
  have he := fibre_eq_cyclicFibreSum A χ t 0 3 ht
  simp only [map_zero, AddChar.map_zero_eq_one, one_mul] at he
  rw [he]
  generalize hS : fibreIndices 3 A t 0 = S at h0 h12 ⊢
  fin_cases S <;> simp_all [cyclicFibreSum, Fin.ext_iff]

noncomputable def cosetRep (t : G) (y : Cosets t) : G :=
  (QuotientAddGroup.mk'_surjective (AddSubgroup.zmultiples t) y).choose

omit [Fintype G] in
lemma projection_cosetRep (t : G) (y : Cosets t) : projection t (cosetRep t y) = y :=
  (QuotientAddGroup.mk'_surjective (AddSubgroup.zmultiples t) y).choose_spec

/-- Order-four two-run fibres: their cyclic coordinates are one of the four adjacent pairs.
The coordinates enumerate the entire actual coset by `fibreSet_eq_image`. -/
noncomputable def twoRunCosets (A : Finset G) (t : G) : Finset (Cosets t) :=
  univ.filter (fun y => y ≠ 0 ∧ IsTwoRun (fibreIndices 4 A t (cosetRep t y)))

lemma pair_eq_of_card_two {α : Type*} [DecidableEq α] (S : Finset α)
    (hcard : S.card = 2) (a b : α) (ha : a ∈ S) (hb : b ∈ S) (hab : a ≠ b) :
    S = {a, b} := by
  symm
  apply eq_of_subset_of_card_le
  · intro x hx
    simp only [mem_insert, mem_singleton] at hx
    rcases hx with rfl | rfl <;> assumption
  · simp [hcard, hab]

lemma isTwoRun_iff_pair (S : Finset (Fin 4)) :
    IsTwoRun S ↔ ∃ i : Fin 4, S = {i, i + 1} := by
  constructor
  · rintro ⟨hc, h⟩
    rcases h with h | h | h | h
    · exact ⟨0, pair_eq_of_card_two S hc 0 1 h.1 h.2 (by decide)⟩
    · exact ⟨1, pair_eq_of_card_two S hc 1 2 h.1 h.2 (by decide)⟩
    · exact ⟨2, pair_eq_of_card_two S hc 2 3 h.1 h.2 (by decide)⟩
    · exact ⟨3, by simpa only [show (3 : Fin 4) + 1 = 0 by decide, pair_comm]
        using pair_eq_of_card_two S hc 0 3 h.1 h.2 (by decide)⟩
  · rintro ⟨i, rfl⟩
    fin_cases i <;> norm_num [IsTwoRun, Fin.ext_iff, Fin.add_def]

omit [Fintype G] in
lemma coset_coordinate_succ (t x : G) (ht : addOrderOf t = 4) (i : Fin 4) :
    x + (i + 1).val • t = (x + i.val • t) + t := by
  fin_cases i
  · simp
  · simp [succ_nsmul, add_assoc]
  · simp [succ_nsmul, add_assoc]
  · have ht4 : 4 • t = 0 := by simpa only [ht] using addOrderOf_nsmul_eq_zero t
    change x + 0 • t = (x + 3 • t) + t
    rw [zero_nsmul, add_zero, add_assoc, ← succ_nsmul, ht4, add_zero]

/-- The coordinate definition of `D₂` is exactly the set of nonzero cosets whose fibre is
`{x, x+t}`. In particular it does not count opposite pairs or depend on the chosen section. -/
theorem mem_twoRunCosets_iff (A : Finset G) (t : G) (ht : addOrderOf t = 4) (y : Cosets t) :
    y ∈ twoRunCosets A t ↔ y ≠ 0 ∧ ∃ x : G, fibreSet A t y = {x, x + t} := by
  let x := cosetRep t y
  let S := fibreIndices 4 A t x
  let f : Fin 4 → G := fun i => x + i.val • t
  have hf : fibreSet A t y = S.image f := by
    have hf' := fibreSet_eq_image A t x 4 ht
    have hx : projection t x = y := projection_cosetRep t y
    rw [hx] at hf'
    exact hf'
  have hsucc : ∀ i : Fin 4, f (i + 1) = f i + t := coset_coordinate_succ t x ht
  change (y ∈ univ.filter (fun y => y ≠ 0 ∧ IsTwoRun (fibreIndices 4 A t (cosetRep t y)))) ↔ _
  simp only [mem_filter, mem_univ, true_and]
  constructor
  · rintro ⟨hy, hrun⟩
    obtain ⟨i, hi⟩ := isTwoRun_iff_pair S |>.mp hrun
    refine ⟨hy, f i, ?_⟩
    rw [hf, hi]
    simp [hsucc i]
  · rintro ⟨hy, u, hu⟩
    refine ⟨hy, (isTwoRun_iff_pair S).mpr ?_⟩
    have humem : u ∈ S.image f := by rw [← hf, hu]; simp
    obtain ⟨i, hi, hui⟩ := mem_image.mp humem
    refine ⟨i, ?_⟩
    apply (image_inj (coset_coordinate_injective t x 4 ht)).mp
    rw [← hf, hu]
    simp only [image_insert, image_singleton]
    change {u, u + t} = {f i, f (i + 1)}
    rw [hsucc i, hui]

lemma fibre_fourth_table (A : Finset G) (t : G) (ht : addOrderOf t = 4)
    (χ : AddChar G ℂ) (hχ : χ t = Complex.I) (y : Cosets t) :
    fibre (projection t) A χ y ^ 4 *
      conj (quotientPower t χ 4 (by rw [hχ]; norm_num) y) =
      if (fibreSet A t y).card = 1 then 1
      else if IsTwoRun (fibreIndices 4 A t (cosetRep t y)) then -4
      else if (fibreSet A t y).card = 3 then 1 else 0 := by
  let x := cosetRep t y
  have hx : projection t x = y := projection_cosetRep t y
  have hf := fibre_eq_cyclicFibreSum A χ t x 4 ht
  have hcard := fibreSet_card A t x 4 ht
  rw [hx] at hf hcard
  rw [hf, hcard, mul_pow]
  have hr : quotientPower t χ 4 (by rw [hχ]; norm_num) y = χ x ^ 4 := by
    rw [← hx]; rfl
  rw [hr]
  have hc : χ x ^ 4 * conj (χ x ^ 4) = 1 := by
    rw [map_pow]
    have h1 : χ x * conj (χ x) = 1 := by
      rw [← AddChar.map_neg_eq_conj, ← AddChar.map_add_eq_mul]
      simp
    rw [← mul_pow, h1, one_pow]
  calc
    _ = cyclicFibreSum (χ t) (fibreIndices 4 A t x) ^ 4 *
        (χ x ^ 4 * conj (χ x ^ 4)) := by ring
    _ = _ := by rw [hc, mul_one, hχ, fibre_table_four]

/-- **T2 / O4⁺**, on the actual quotient and with the full spectral hypothesis. -/
theorem order_four_fibre_bound (A : Finset G) (hsym : ∀ x ∈ A, -x ∈ A)
    (_hzero : (0 : G) ∉ A) (K : ℝ) (_hKnonneg : 0 ≤ K)
    (hK : ∀ η : AddChar G ℂ, η ≠ 0 → -K ≤ (setFourier A η).re)
    (t : G) (ht : addOrderOf t = 4) (χ : AddChar G ℂ) (hχ : χ t = Complex.I) :
    4 * ((twoRunCosets A t).card : ℝ) ≤ (singleCosets A t).card + (tripleCosets A t).card +
      (K + (fibre (projection t) A χ 0).re) ^ 4 := by
  let U := fibre (projection t) A χ
  let c : Cosets t → ℝ := fun y =>
    (if y ∈ singleCosets A t then 1 else 0) + (if y ∈ tripleCosets A t then 1 else 0) -
      4 * (if y ∈ twoRunCosets A t then 1 else 0)
  have hc₀ : c 0 = 0 := by simp [c, singleCosets, tripleCosets, twoRunCosets]
  have hU₀ : U 0 = ((U 0).re : ℂ) := by
    apply Complex.ext <;> simp [U, fibre_zero_im_eq_zero A hsym]
  have hχne : χ t ≠ 1 := by rw [hχ]; norm_num [Complex.ext_iff]
  have hpd := shifted_fibre_positiveDefinite (projection t) A hsym χ t
    (projection_self t) hχne K hK
  have htable : ∀ y : Cosets t, y ≠ 0 → U y ^ 4 *
      conj (quotientPower t χ 4 (by rw [hχ]; norm_num) y) = (c y : ℂ) := by
    intro y hy
    rw [fibre_fourth_table A t ht χ hχ]
    have hcard : (fibreSet A t y).card = (fibreIndices 4 A t (cosetRep t y)).card := by
      simpa only [projection_cosetRep] using fibreSet_card A t (cosetRep t y) 4 ht
    have hrun : IsTwoRun (fibreIndices 4 A t (cosetRep t y)) → (fibreSet A t y).card = 2 :=
      fun h => hcard.trans h.1
    by_cases h1 : (fibreSet A t y).card = 1
    · have hn : ¬ IsTwoRun (fibreIndices 4 A t (cosetRep t y)) := by
        intro h; have := hrun h; omega
      have h3 : (fibreSet A t y).card ≠ 3 := by omega
      simp [c, singleCosets, tripleCosets, twoRunCosets, hy, h1, hn]
    · by_cases hn : IsTwoRun (fibreIndices 4 A t (cosetRep t y))
      · have h2 := hrun hn
        have h3 : (fibreSet A t y).card ≠ 3 := by omega
        simp [c, singleCosets, tripleCosets, twoRunCosets, hy, h1, h3, hn]
      · by_cases h3 : (fibreSet A t y).card = 3 <;>
          simp [c, singleCosets, tripleCosets, twoRunCosets, hy, h1, h3, hn]
  have hb := power_certificate_bound U K (U 0).re 4
    (quotientPower t χ 4 (by rw [hχ]; norm_num)) c hc₀ hU₀ hpd htable
  have hsum : ∑ y, c y = ((singleCosets A t).card : ℝ) + (tripleCosets A t).card -
      4 * (twoRunCosets A t).card := by
    simp [c, sum_sub_distrib, sum_add_distrib, mul_comm]
  rw [hsum] at hb
  dsimp only [U] at hb
  linarith

/-- The order-four zero fibre has exactly the two values stated in T2. -/
theorem order_four_zero_fibre (A : Finset G) (hsym : ∀ x ∈ A, -x ∈ A)
    (hzero : (0 : G) ∉ A) (t : G) (ht : addOrderOf t = 4)
    (χ : AddChar G ℂ) (hχ : χ t = Complex.I) :
    fibre (projection t) A χ 0 = 0 ∨ fibre (projection t) A χ 0 = -1 := by
  have h0 : (0 : Fin 4) ∉ fibreIndices 4 A t 0 := by simp [fibreIndices, hzero]
  have h13 : (1 : Fin 4) ∈ fibreIndices 4 A t 0 ↔
      (3 : Fin 4) ∈ fibreIndices 4 A t 0 := by
    have hn := nsmul_pred_eq_neg t 3 ht
    have hmem : -t ∈ A ↔ t ∈ A :=
      ⟨fun hx => by simpa using hsym (-t) hx, hsym t⟩
    simpa [fibreIndices, hn, show (3 : Fin 4).val = 3 by rfl] using hmem.symm
  have he := fibre_eq_cyclicFibreSum A χ t 0 4 ht
  simp only [map_zero, AddChar.map_zero_eq_one, one_mul] at he
  rw [he, hχ]
  generalize hS : fibreIndices 4 A t 0 = S at h0 h13 ⊢
  fin_cases S <;> simp_all [cyclicFibreSum, Fin.ext_iff, Complex.I_sq, Complex.I_pow_three]

/-- Run-tops in an arbitrary finite additive abelian group. -/
noncomputable def runTops (A : Finset G) (t : G) : Finset G :=
  A.filter (fun m => m - t ∈ A ∧ m + t ∉ A)

lemma runTop_fibre (A : Finset G) (t : G) (ht : addOrderOf t = 3)
    (m : G) (hm : m ∈ runTops A t) :
    fibreSet A t (projection t m) = {m, m - t} := by
  have hn : 2 • t = -t := nsmul_pred_eq_neg t 2 ht
  have hm' : m ∈ A ∧ m - t ∈ A ∧ m + t ∉ A := by simpa [runTops] using hm
  have hS : fibreIndices 3 A t m = {0, 2} := by
    ext i
    fin_cases i <;> simp_all [fibreIndices, Fin.ext_iff, sub_eq_add_neg]
  rw [fibreSet_eq_image A t m 3 ht, hS]
  simp [hn, sub_eq_add_neg]

/-- **T1 run-top counting corollary**, including the possible zero coset. -/
theorem order_three_runTops_card (A : Finset G) (t : G) (ht : addOrderOf t = 3) :
    (runTops A t).card ≤ (doubleCosets A t).card + 1 := by
  have htne : t ≠ 0 := by
    intro he
    simp [he] at ht
  have hinj : Set.InjOn (projection t) (runTops A t) := by
    intro m hm n hn hq
    have hfm := runTop_fibre A t ht m hm
    have hnA : n ∈ A := (mem_filter.mp hn).1
    have hnf : n ∈ fibreSet A t (projection t m) := by
      simp [fibreSet, hnA, hq]
    rw [hfm] at hnf
    simp only [mem_insert, mem_singleton] at hnf
    rcases hnf with he | he
    · exact he.symm
    · have hnprev : n - t ∈ A := (mem_filter.mp hn).2.1
      have hmnext : m + t ∉ A := (mem_filter.mp hm).2.2
      have hcycle : (m - t) - t = m + t := by
        have he' := nsmul_pred_eq_neg t 2 ht
        have he'' : t + t = -t := by simpa [two_nsmul] using he'
        calc
          (m - t) - t = m - (t + t) := by abel
          _ = m + t := by rw [he'']; simp
      rw [he, hcycle] at hnprev
      exact False.elim (hmnext hnprev)
  have hmap : (runTops A t).image (projection t) ⊆ insert 0 (doubleCosets A t) := by
    intro y hy
    obtain ⟨m, hm, rfl⟩ := mem_image.mp hy
    by_cases hq : projection t m = 0
    · simp [hq]
    · apply mem_insert_of_mem
      have hcard : (fibreSet A t (projection t m)).card = 2 := by
        rw [runTop_fibre A t ht m hm]
        have hne : m ≠ m - t := by
          intro he
          apply htne
          have : m - t = m := he.symm
          exact sub_eq_self.mp this
        simp [hne]
      simp [doubleCosets, hq, hcard]
  calc
    (runTops A t).card = ((runTops A t).image (projection t)).card :=
      (card_image_of_injOn hinj).symm
    _ ≤ (insert 0 (doubleCosets A t)).card := card_le_card hmap
    _ ≤ (doubleCosets A t).card + 1 := card_insert_le _ _

/-- The spectral run-top bound requested at the end of T1. -/
theorem order_three_runTops_bound (A : Finset G) (hsym : ∀ x ∈ A, -x ∈ A)
    (hzero : (0 : G) ∉ A) (K : ℝ) (hKnonneg : 0 ≤ K)
    (hK : ∀ η : AddChar G ℂ, η ≠ 0 → -K ≤ (setFourier A η).re)
    (t : G) (ht : addOrderOf t = 3) (χ : AddChar G ℂ) (hχ : χ t = omega) :
    ((runTops A t).card : ℝ) ≤ (singleCosets A t).card +
      (K + (fibre (projection t) A χ 0).re) ^ 3 + 1 := by
  have hb := order_three_fibre_bound A hsym hzero K hKnonneg hK t ht χ hχ
  have hc : ((runTops A t).card : ℝ) ≤ (doubleCosets A t).card + 1 := by
    exact_mod_cast order_three_runTops_card A t ht
  linarith

end QuotientFibres

end ChowlaCosine.FibreSchur
