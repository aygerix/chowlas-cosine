import Mathlib

/-! Unnormalized Fourier and convolution identities for sign functions on `ZMod p`. -/

namespace ChowlaCosine.HalfSet

open Finset
open scoped ComplexConjugate
attribute [local instance] Classical.propDecidable

section Convolution

variable {G R : Type*} [AddCommGroup G] [Fintype G] [CommRing R]

noncomputable def conv (f g : G → R) (x : G) : R := ∑ y, f y * g (x - y)

lemma conv_comm (f g : G → R) : conv f g = conv g f := by
  funext x
  unfold conv
  apply Fintype.sum_equiv (Equiv.subLeft x)
  intro y
  simp [mul_comm]

lemma sum_sub (f : G → R) (x : G) : (∑ y, f (x - y)) = ∑ y, f y := by
  exact Fintype.sum_equiv (Equiv.subLeft x) _ _ (fun y => rfl)

lemma conv_add_left (f g h : G → R) :
    conv (fun x => f x + g x) h = fun x => conv f h x + conv g h x := by
  funext x
  simp [conv, add_mul, sum_add_distrib]

lemma conv_add_right (f g h : G → R) :
    conv f (fun x => g x + h x) = fun x => conv f g x + conv f h x := by
  funext x
  simp [conv, mul_add, sum_add_distrib]

lemma conv_sub_left (f g h : G → R) :
    conv (fun x => f x - g x) h = fun x => conv f h x - conv g h x := by
  funext x
  simp [conv, sub_mul, sum_sub_distrib]

lemma conv_sub_right (f g h : G → R) :
    conv f (fun x => g x - h x) = fun x => conv f g x - conv f h x := by
  funext x
  simp [conv, mul_sub, sum_sub_distrib]

/-- A point mass, kept bundled to make repeated convolution expansions explicit. -/
noncomputable def atom (a : G) (c : R) (x : G) : R := if x = a then c else 0

lemma conv_atom_left (f : G → R) (a : G) (c : R) :
    conv (atom a c) f = fun x => c * f (x - a) := by
  funext x
  simp [conv, atom, ite_mul]

lemma conv_atom_right (f : G → R) (a : G) (c : R) :
    conv f (atom a c) = fun x => c * f (x - a) := by
  rw [conv_comm, conv_atom_left]

lemma conv_const_right (f : G → R) (c : R) :
    conv f (fun _ => c) = fun _ => (∑ y, f y) * c := by
  funext x
  simp [conv, sum_mul]

lemma conv_const_left (f : G → R) (c : R) :
    conv (fun _ => c) f = fun _ => c * ∑ y, f y := by
  rw [conv_comm, conv_const_right]
  simp only [mul_comm]

lemma conv_delta_left (f : G → R) (a : G) (c : R) :
    conv (fun y => if y = a then c else 0) f = fun x => c * f (x - a) := by
  funext x
  simp [conv, ite_mul]

lemma conv_delta_right (f : G → R) (a : G) (c : R) :
    conv f (fun y => if y = a then c else 0) = fun x => c * f (x - a) := by
  rw [conv_comm, conv_delta_left]

lemma conv_assoc (f g h : G → R) : conv (conv f g) h = conv f (conv g h) := by
  funext x
  simp only [conv, sum_mul, mul_sum]
  rw [sum_comm]
  apply sum_congr rfl
  intro y _
  apply Fintype.sum_equiv (Equiv.addLeft (-y))
  intro z
  simp [sub_eq_add_neg, add_assoc, add_comm, add_left_comm, mul_assoc]

end Convolution

variable {p : ℕ} [NeZero p]

/-- The exact sign-function hypothesis; no evenness or balance is imposed in (a)--(c). -/
def IsSign (g : ZMod p → ℝ) : Prop := ∀ x, g x = 1 ∨ g x = -1

/-- `ĝ(γ) = ∑ x, g(x) exp(-2π i xγ/p)`, with no normalization. -/
noncomputable def hat (g : ZMod p → ℝ) : ZMod p → ℂ :=
  ZMod.dft (fun x => (g x : ℂ))

lemma hat_apply (g : ZMod p → ℝ) (γ : ZMod p) :
    hat g γ = ∑ x, (g x : ℂ) * ZMod.stdAddChar (-(γ * x)) := by
  simp only [hat, ZMod.dft_apply, smul_eq_mul, mul_comm]

lemma dft_inversion_sum (f : ZMod p → ℂ) (y : ZMod p) :
    (∑ γ, ZMod.dft f γ * ZMod.stdAddChar (γ * y)) = (p : ℂ) * f y := by
  have he := congrFun (ZMod.dft_dft f) (-y)
  simpa only [ZMod.dft_apply, smul_eq_mul, mul_neg, neg_neg, mul_comm] using he

/-- Multiplication-to-convolution identity with the exact unnormalized factor. -/
theorem conv_dft (f k : ZMod p → ℂ) (δ : ZMod p) :
    conv (ZMod.dft f) (ZMod.dft k) δ =
      (p : ℂ) * ZMod.dft (fun x => f x * k x) δ := by
  change (∑ γ, ZMod.dft f γ * (∑ y, ZMod.stdAddChar (-(y * (δ - γ))) * k y)) = _
  simp_rw [mul_sum]
  rw [sum_comm]
  calc
    _ = ∑ y, (ZMod.stdAddChar (-(y * δ)) * k y) *
        (∑ γ, ZMod.dft f γ * ZMod.stdAddChar (γ * y)) := by
      apply sum_congr rfl
      intro y _
      rw [mul_sum]
      apply sum_congr rfl
      intro γ _
      have he : -(y * (δ - γ)) = -(y * δ) + γ * y := by ring
      rw [he, AddChar.map_add_eq_mul]
      ring
    _ = _ := by
      simp_rw [dft_inversion_sum]
      simp only [ZMod.dft_apply, smul_eq_mul, mul_sum]
      apply sum_congr rfl
      intro y _
      ring

lemma sum_hat (g : ZMod p → ℝ) : ∑ γ, hat g γ = (p : ℂ) * g 0 := by
  simpa only [hat, mul_zero, AddChar.map_zero_eq_one, mul_one] using
    dft_inversion_sum (fun x => (g x : ℂ)) (0 : ZMod p)

lemma hat_zero (g : ZMod p → ℝ) : hat g 0 = (∑ x, g x : ℝ) := by
  simp [hat, ZMod.dft_apply_zero]

/-- **T3(a)**: Booleanity gives the exact convolution square. -/
theorem hat_conv_hat (g : ZMod p → ℝ) (hg : IsSign g) (δ : ZMod p) :
    conv (hat g) (hat g) δ = if δ = 0 then (p : ℂ) ^ 2 else 0 := by
  have hg2 : (fun x => (g x : ℂ) * (g x : ℂ)) = fun _ => (1 : ℂ) := by
    funext x
    rcases hg x with hx | hx <;> simp [hx]
  rw [hat, conv_dft, hg2]
  have he : ZMod.dft (fun _ : ZMod p => (1 : ℂ)) δ =
      if δ = 0 then (p : ℂ) else 0 := by
    simp only [ZMod.dft_apply, smul_eq_mul, mul_one]
    have orth := AddChar.sum_mulShift (-δ) (ZMod.isPrimitive_stdAddChar p)
    simpa [AddChar.mulShift_apply, mul_neg, ZMod.card] using orth
  rw [he]
  split_ifs <;> simp [pow_two]

noncomputable def shiftedHat (g : ZMod p → ℝ) (lam : ℝ) (γ : ZMod p) : ℂ :=
  hat g γ + lam

/-- **T3(b)**, including its diagonal term for use in subsequent identities. -/
theorem shiftedHat_square (g : ZMod p → ℝ) (hg : IsSign g) (lam : ℝ) (δ : ZMod p) :
    conv (shiftedHat g lam) (shiftedHat g lam) δ =
      (if δ = 0 then (p : ℂ) ^ 2 else 0) + 2 * lam * p * g 0 + p * (lam : ℂ) ^ 2 := by
  unfold shiftedHat
  rw [conv_add_left, conv_add_right, conv_add_right]
  simp only [conv_const_left, conv_const_right, sum_hat, sum_const, card_univ, ZMod.card,
    nsmul_eq_mul, hat_conv_hat g hg]
  ring

theorem shiftedHat_square_off_zero (g : ZMod p → ℝ) (hg : IsSign g) (lam : ℝ)
    (δ : ZMod p) (hδ : δ ≠ 0) :
    conv (shiftedHat g lam) (shiftedHat g lam) δ =
      2 * lam * p * g 0 + p * (lam : ℂ) ^ 2 := by
  rw [shiftedHat_square g hg, if_neg hδ, zero_add]

/-- The general value of the cubic constant, before specializing `g(0)`. -/
noncomputable def cubicConstant (g : ZMod p → ℝ) (lam : ℝ) : ℝ :=
  (p : ℝ) ^ 2 * (2 * lam + 3 * lam ^ 2 * g 0 + lam ^ 3)

/-- **T3(c)**: the cubic identity for arbitrary sign functions and real shifts. -/
theorem shiftedHat_cube (g : ZMod p → ℝ) (hg : IsSign g) (lam : ℝ) (δ : ZMod p) :
    conv (conv (shiftedHat g lam) (shiftedHat g lam)) (shiftedHat g lam) δ =
      (p : ℂ) ^ 2 * shiftedHat g lam δ + (cubicConstant g lam : ℂ) := by
  have hs : conv (shiftedHat g lam) (shiftedHat g lam) = fun x =>
      (if x = 0 then (p : ℂ) ^ 2 else 0) +
        (2 * (lam : ℂ) * p * g 0 + p * (lam : ℂ) ^ 2) := by
    funext x
    rw [shiftedHat_square g hg]
    ring
  have hsum : ∑ γ, shiftedHat g lam γ = (p : ℂ) * (g 0 + lam) := by
    simp [shiftedHat, sum_add_distrib, sum_hat]
    ring
  rw [hs, conv_add_left]
  change conv (fun x => if x = 0 then (p : ℂ) ^ 2 else 0) (shiftedHat g lam) δ +
    conv (fun _ => 2 * (lam : ℂ) * p * g 0 + p * (lam : ℂ) ^ 2)
      (shiftedHat g lam) δ = _
  have hd : conv (fun x => if x = 0 then (p : ℂ) ^ 2 else 0) (shiftedHat g lam) δ =
      (p : ℂ) ^ 2 * shiftedHat g lam δ := by
    simp [conv, ite_mul]
  rw [hd, conv_const_left]
  dsimp only
  rw [hsum]
  simp only [shiftedHat, cubicConstant]
  push_cast
  rcases hg 0 with h0 | h0 <;> simp only [h0] <;> push_cast <;> ring

omit [NeZero p] in
theorem cubicConstant_of_neg_one (g : ZMod p → ℝ) (lam : ℝ) (h0 : g 0 = -1) :
    cubicConstant g lam = (p : ℝ) ^ 2 * lam * (lam - 1) * (lam - 2) := by
  simp only [cubicConstant, h0]
  ring

omit [NeZero p] in
theorem cubicConstant_eq_brief (g : ZMod p → ℝ) (lam : ℝ) :
    cubicConstant g lam = (p : ℝ) ^ 2 * (3 * lam + 3 * lam ^ 2 * g 0 + lam ^ 3) -
      (p : ℝ) ^ 2 * lam := by
  unfold cubicConstant
  ring

theorem shiftedHat_cube_neg_one (g : ZMod p → ℝ) (hg : IsSign g) (hzero : g 0 = -1)
    (lam : ℝ) (δ : ZMod p) :
    conv (conv (shiftedHat g lam) (shiftedHat g lam)) (shiftedHat g lam) δ =
      (p : ℂ) ^ 2 * shiftedHat g lam δ + (p : ℂ) ^ 2 * lam * (lam - 1) * (lam - 2) := by
  rw [shiftedHat_cube g hg, cubicConstant_of_neg_one g lam hzero]
  push_cast
  rfl

lemma hat_even (g : ZMod p → ℝ) (heven : ∀ x, g (-x) = g x) :
    ∀ γ, hat g (-γ) = hat g γ := by
  apply ZMod.dft_even_iff.mpr
  intro x
  simp [heven x]

lemma hat_im_eq_zero (g : ZMod p → ℝ) (heven : ∀ x, g (-x) = g x) (γ : ZMod p) :
    (hat g γ).im = 0 := by
  rw [← Complex.conj_eq_iff_im, hat_apply, map_sum]
  apply Fintype.sum_equiv (Equiv.neg (ZMod p))
  intro x
  simp [AddChar.map_neg_eq_conj, heven, mul_neg]

/-- In the even case the complex shifted transform is represented by this real function. -/
noncomputable def realShiftedHat (g : ZMod p → ℝ) (lam : ℝ) (γ : ZMod p) : ℝ :=
  (hat g γ).re + lam

lemma realShiftedHat_cast (g : ZMod p → ℝ) (heven : ∀ x, g (-x) = g x)
    (lam : ℝ) (γ : ZMod p) :
    (realShiftedHat g lam γ : ℂ) = shiftedHat g lam γ := by
  apply Complex.ext <;> simp [realShiftedHat, shiftedHat, hat_im_eq_zero g heven]

lemma realShiftedHat_even (g : ZMod p → ℝ) (heven : ∀ x, g (-x) = g x) (lam : ℝ) :
    ∀ γ, realShiftedHat g lam (-γ) = realShiftedHat g lam γ := by
  intro γ
  simp [realShiftedHat, hat_even g heven γ]

lemma conv_ofReal {G : Type*} [AddCommGroup G] [Fintype G] (f k : G → ℝ) (x : G) :
    ((conv f k x : ℝ) : ℂ) = conv (fun y => (f y : ℂ)) (fun y => (k y : ℂ)) x := by
  simp [conv]

lemma realShiftedHat_square (g : ZMod p → ℝ) (hg : IsSign g)
    (heven : ∀ x, g (-x) = g x) (lam : ℝ) (δ : ZMod p) :
    conv (realShiftedHat g lam) (realShiftedHat g lam) δ =
      (if δ = 0 then (p : ℝ) ^ 2 else 0) + 2 * lam * p * g 0 + p * lam ^ 2 := by
  apply Complex.ofReal_injective
  rw [conv_ofReal]
  simp_rw [realShiftedHat_cast g heven]
  rw [shiftedHat_square g hg]
  push_cast
  split_ifs <;> push_cast <;> rfl

lemma realShiftedHat_cube (g : ZMod p → ℝ) (hg : IsSign g)
    (heven : ∀ x, g (-x) = g x) (lam : ℝ) (δ : ZMod p) :
    conv (conv (realShiftedHat g lam) (realShiftedHat g lam)) (realShiftedHat g lam) δ =
      (p : ℝ) ^ 2 * realShiftedHat g lam δ + cubicConstant g lam := by
  apply Complex.ofReal_injective
  rw [conv_ofReal]
  simp_rw [conv_ofReal, realShiftedHat_cast g heven]
  rw [shiftedHat_cube g hg]
  push_cast
  rw [realShiftedHat_cast g heven]

/-- Balance supplies positivity at frequency zero; the spectral hypothesis supplies it elsewhere. -/
theorem realShiftedHat_nonneg (g : ZMod p → ℝ)
    (hbal : (∑ x, g x) = 1 ∨ (∑ x, g x) = -1) (lam : ℝ) (hlam : 1 ≤ lam)
    (hlower : ∀ γ : ZMod p, γ ≠ 0 → -lam ≤ (hat g γ).re) :
    ∀ γ, 0 ≤ realShiftedHat g lam γ := by
  intro γ
  by_cases hγ : γ = 0
  · subst γ
    simp only [realShiftedHat, hat_zero, Complex.ofReal_re]
    rcases hbal with hbal | hbal <;> rw [hbal] <;> linarith
  · unfold realShiftedHat
    linarith [hlower γ hγ]

section AbstractGap

variable {G : Type*} [AddCommGroup G] [Fintype G]

/-- Exact expansion after deleting one coefficient. No division or approximation is used. -/
lemma cube_delete (h : G → ℝ) (γ : G) (hne : -γ ≠ γ) :
    let a := h γ
    let u := fun x => h x - atom γ a x
    conv (conv u u) u γ = conv (conv h h) h γ -
      3 * a * conv h h 0 + 3 * a ^ 2 * h (-γ) := by
  dsimp only
  let d := atom γ (h γ)
  have h₁ : conv (conv h h) d γ = h γ * conv h h 0 := by
    simp [d, conv_atom_right]
  have h₂ : conv (conv h d) h γ = h γ * conv h h 0 := by
    rw [conv_comm h d, conv_assoc, conv_atom_left]
    simp
  have h₃ : conv (conv d h) h γ = h γ * conv h h 0 := by
    rw [conv_assoc, conv_atom_left]
    simp
  have h₄ : conv (conv h d) d γ = h γ ^ 2 * h (-γ) := by
    simp [d, conv_atom_right, pow_two, mul_assoc]
  have h₅ : conv (conv d h) d γ = h γ ^ 2 * h (-γ) := by
    rw [conv_comm d h]
    exact h₄
  have h₆ : conv (conv d d) h γ = h γ ^ 2 * h (-γ) := by
    rw [conv_assoc]
    simp [d, conv_atom_left, pow_two, mul_assoc]
  have h₇ : conv (conv d d) d γ = 0 := by
    rw [conv_assoc]
    simp [d, conv_atom_left, atom, hne]
  change conv (conv (fun x => h x - d x) (fun x => h x - d x))
    (fun x => h x - d x) γ = _
  simp only [conv_sub_left, conv_sub_right]
  rw [h₁, h₂, h₃, h₄, h₅, h₆, h₇]
  ring

theorem spectral_gap_of_cube (h : G → ℝ) (hpos : ∀ x, 0 ≤ h x)
    (heven : ∀ x, h (-x) = h x) (q c : ℝ)
    (hcube : ∀ δ, conv (conv h h) h δ = q * h δ + c)
    (γ : G) (hne : -γ ≠ γ) :
    0 ≤ 3 * h γ ^ 3 - (3 * (∑ x, h x ^ 2) - q) * h γ + c := by
  let u := fun x => h x - atom γ (h γ) x
  have hu : ∀ x, 0 ≤ u x := by
    intro x
    by_cases hx : x = γ
    · simp [u, atom, hx]
    · simpa [u, atom, hx] using hpos x
  have hconv : ∀ x, 0 ≤ conv u u x := by
    intro x
    exact sum_nonneg (fun y _ => mul_nonneg (hu y) (hu (x - y)))
  have hp : 0 ≤ conv (conv u u) u γ :=
    sum_nonneg (fun y _ => mul_nonneg (hconv y) (hu (γ - y)))
  have hs : conv h h 0 = ∑ x, h x ^ 2 := by
    simp [conv, heven, pow_two]
  have he := cube_delete h γ hne
  dsimp only at he
  change conv (conv u u) u γ = _ at he
  rw [hcube γ, hs, heven γ] at he
  linarith

end AbstractGap

section OddPrime

variable [Fact p.Prime]

omit [NeZero p] in
lemma neg_ne_of_nonzero (hp : p ≠ 2) (γ : ZMod p) (hγ : γ ≠ 0) : -γ ≠ γ := by
  intro he
  have htwo : (2 : ZMod p) ≠ 0 := by
    intro h
    have hd : p ∣ 2 := (ZMod.natCast_eq_zero_iff 2 p).mp h
    have hle := Nat.le_of_dvd (by decide : 0 < 2) hd
    have hprime : 2 ≤ p := (Fact.out : p.Prime).two_le
    omega
  have hsum : γ + γ = 0 := neg_eq_iff_add_eq_zero.mp he
  have hmul : (2 : ZMod p) * γ = 0 := by simpa [two_mul] using hsum
  exact hγ ((mul_eq_zero.mp hmul).resolve_left htwo)

/-- **T3(d)**: nonnegativity and the coefficientwise cubic spectral gap. -/
theorem spectral_gap (hp : p ≠ 2) (g : ZMod p → ℝ) (hg : IsSign g)
    (heven : ∀ x, g (-x) = g x)
    (hbal : (∑ x, g x) = 1 ∨ (∑ x, g x) = -1) (lam : ℝ) (hlam : 1 ≤ lam)
    (hlower : ∀ γ : ZMod p, γ ≠ 0 → -lam ≤ (hat g γ).re) :
    (∀ γ, 0 ≤ realShiftedHat g lam γ) ∧
      ∀ γ : ZMod p, γ ≠ 0 →
        0 ≤ 3 * realShiftedHat g lam γ ^ 3 -
          (3 * (∑ x, realShiftedHat g lam x ^ 2) - (p : ℝ) ^ 2) *
            realShiftedHat g lam γ + cubicConstant g lam := by
  have hpos := realShiftedHat_nonneg g hbal lam hlam hlower
  refine ⟨hpos, ?_⟩
  intro γ hγ
  exact spectral_gap_of_cube (realShiftedHat g lam) hpos (realShiftedHat_even g heven lam)
    ((p : ℝ) ^ 2) (cubicConstant g lam) (realShiftedHat_cube g hg heven lam)
    γ (neg_ne_of_nonzero hp γ hγ)

/-- **T3(e)**: the stated upper bound for every nonzero Fourier coefficient. -/
theorem coefficient_upper_bound (hp : p ≠ 2) (g : ZMod p → ℝ) (hg : IsSign g)
    (heven : ∀ x, g (-x) = g x)
    (hbal : (∑ x, g x) = 1 ∨ (∑ x, g x) = -1) (hzero : g 0 = -1)
    (lam : ℝ) (hlam : 1 ≤ lam)
    (hlower : ∀ γ : ZMod p, γ ≠ 0 → -lam ≤ (hat g γ).re)
    (γ : ZMod p) (hγ : γ ≠ 0) : (hat g γ).re ≤ lam * Real.sqrt p := by
  let h := realShiftedHat g lam
  have hpos : ∀ x, 0 ≤ h x := realShiftedHat_nonneg g hbal lam hlam hlower
  have hδ : γ + γ ≠ 0 := by
    intro he
    apply neg_ne_of_nonzero hp γ hγ
    exact neg_eq_iff_add_eq_zero.mpr he
  have hs : h γ ^ 2 ≤ conv h h (γ + γ) := by
    have he := single_le_sum (f := fun y => h y * h ((γ + γ) - y))
      (fun y _ => mul_nonneg (hpos y) (hpos ((γ + γ) - y))) (mem_univ γ)
    simpa [conv, pow_two] using he
  have he := realShiftedHat_square g hg heven lam (γ + γ)
  rw [if_neg hδ, hzero] at he
  have hsq : h γ ^ 2 ≤ (p : ℝ) * lam ^ 2 := by
    change conv h h (γ + γ) = _ at he
    have hp0 : (0 : ℝ) ≤ p := Nat.cast_nonneg p
    nlinarith
  have hroot : 0 ≤ lam * Real.sqrt p := mul_nonneg (by linarith) (Real.sqrt_nonneg _)
  have hrootsq : (lam * Real.sqrt p) ^ 2 = (p : ℝ) * lam ^ 2 := by
    rw [mul_pow, Real.sq_sqrt (Nat.cast_nonneg p)]
    ring
  have hh : h γ ≤ lam * Real.sqrt p := by nlinarith [hpos γ]
  dsimp [h, realShiftedHat] at hh
  linarith

end OddPrime

end ChowlaCosine.HalfSet
