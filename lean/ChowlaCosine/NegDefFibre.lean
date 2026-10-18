/-
P21 diagnosis (PROOFS.md): the negative-definite fibre lemma (Lean agent, 2026-10-18).

Statement. Let ℓ ≥ 1 and let I ⊆ ZMod ℓ be nonempty with 0 ∉ I and I = −I. Suppose that for every j ≠ 0,
    Σ_{s ∈ I} cos(2π j s / ℓ) ≤ 0.
Then ℓ ≤ 2|I|.

Here cos(2π j s/ℓ) is written with the representatives `j.val, s.val ∈ {0, …, ℓ − 1}`; the value does not depend
on the choice of representatives.

Proof (a direct form of "|I|/ℓ − 1_I is positive definite"). Let χ be the standard character of ZMod ℓ,
C_j = Σ_{s∈I} χ(j s), c_j = Re C_j = Σ_{s∈I} cos(2π j s/ℓ) and r_j = Re χ(j s₀) for a fixed s₀ ∈ I.
* Σ_j c_j = 0 by orthogonality, since 0 ∉ I.
* Σ_j C_j χ(j s₀) = ℓ (uses −s₀ ∈ I) and Σ_j C_j conj χ(j s₀) = ℓ (uses s₀ ∈ I); adding, Σ_j c_j r_j = ℓ.
* c_0 = |I|, r_0 = 1, and for j ≠ 0: c_j ≤ 0 and r_j ≥ −1, so c_j r_j ≤ −c_j.
Hence ℓ ≤ |I| − Σ_{j≠0} c_j = |I| + c_0 = 2|I|.
-/
import Mathlib

namespace ChowlaCosine.NegDefFibre

open Finset

/-- `cos(2π j s/ℓ)` is the real part of the standard additive character at `j * s`. -/
lemma cos_eq_re (ℓ : ℕ) [NeZero ℓ] (j s : ZMod ℓ) :
    Real.cos (2 * Real.pi * ((j.val : ℝ) * (s.val : ℝ)) / ℓ) = (ZMod.stdAddChar (j * s)).re := by
  have hjs : j * s = ((j.val * s.val : ℕ) : ZMod ℓ) := by
    rw [Nat.cast_mul, ZMod.natCast_zmod_val, ZMod.natCast_zmod_val]
  rw [hjs, ZMod.stdAddChar_apply, ZMod.toCircle_natCast, ← Complex.exp_ofReal_mul_I_re]
  congr 2
  push_cast
  ring

/-- **Negative-definite fibre lemma.** A symmetric set `I ⊆ ZMod ℓ`, `0 ∉ I`, whose cosine transform is `≤ 0` at
every nonzero frequency has at least `ℓ / 2` elements. -/
theorem le_two_mul_card_of_negDef (ℓ : ℕ) (hℓ : 1 ≤ ℓ) (I : Finset (ZMod ℓ)) (hI : I.Nonempty)
    (h0 : (0 : ZMod ℓ) ∉ I) (hsym : ∀ s ∈ I, -s ∈ I)
    (hneg : ∀ j : ZMod ℓ, j ≠ 0 →
      ∑ s ∈ I, Real.cos (2 * Real.pi * ((j.val : ℝ) * (s.val : ℝ)) / ℓ) ≤ 0) :
    ℓ ≤ 2 * I.card := by
  have : NeZero ℓ := ⟨by omega⟩
  obtain ⟨s0, hs0⟩ := hI
  have hχ : (ZMod.stdAddChar (N := ℓ)).IsPrimitive := ZMod.isPrimitive_stdAddChar ℓ
  have orth : ∀ m : ZMod ℓ,
      ∑ j : ZMod ℓ, ZMod.stdAddChar (j * m) = if m = 0 then (ℓ : ℂ) else 0 := by
    intro m
    rw [AddChar.sum_mulShift m hχ, ZMod.card]
    split_ifs <;> simp
  obtain ⟨C, hC⟩ : ∃ C : ZMod ℓ → ℂ, ∀ j, C j = ∑ s ∈ I, ZMod.stdAddChar (j * s) :=
    ⟨_, fun _ => rfl⟩
  -- the cosine transform is `Re C`
  have hc : ∀ j : ZMod ℓ,
      ∑ s ∈ I, Real.cos (2 * Real.pi * ((j.val : ℝ) * (s.val : ℝ)) / ℓ) = (C j).re := by
    intro j
    rw [hC, Complex.re_sum]
    exact Finset.sum_congr rfl fun s _ => cos_eq_re ℓ j s
  -- (A) `Σ_j c_j = 0`
  have hA : ∑ j, (C j).re = 0 := by
    rw [← Complex.re_sum]
    have : ∑ j, C j = 0 := by
      simp_rw [hC]
      rw [Finset.sum_comm]
      refine Finset.sum_eq_zero fun s hs => ?_
      rw [orth s, if_neg (by rintro rfl; exact h0 hs)]
    rw [this, Complex.zero_re]
  -- (B) `Σ_j c_j r_j = ℓ`
  have hB1 : ∑ j, C j * ZMod.stdAddChar (j * s0) = ℓ := by
    simp_rw [hC, Finset.sum_mul, ← AddChar.map_add_eq_mul, ← mul_add]
    rw [Finset.sum_comm]
    simp_rw [orth]
    rw [Finset.sum_eq_single (-s0)]
    · simp
    · intro s _ hs
      rw [if_neg]
      intro h
      exact hs (by linear_combination h)
    · intro h
      exact absurd (hsym s0 hs0) h
  have hB2 : ∑ j, C j * starRingEnd ℂ (ZMod.stdAddChar (j * s0)) = ℓ := by
    simp_rw [← AddChar.map_neg_eq_conj, hC, Finset.sum_mul, ← AddChar.map_add_eq_mul, ← mul_neg,
      ← mul_add]
    rw [Finset.sum_comm]
    simp_rw [orth]
    rw [Finset.sum_eq_single s0]
    · simp
    · intro s _ hs
      rw [if_neg]
      intro h
      exact hs (by linear_combination h)
    · intro h
      exact absurd hs0 h
  have hB : ∑ j, (C j).re * (ZMod.stdAddChar (j * s0)).re = ℓ := by
    have e : ∑ j, C j * ((2 * (ZMod.stdAddChar (j * s0)).re : ℝ) : ℂ) = 2 * ℓ := by
      simp_rw [← Complex.add_conj, mul_add, Finset.sum_add_distrib, hB1, hB2]
      ring
    have e' := congrArg Complex.re e
    have hterm : ∀ j : ZMod ℓ, (C j * ((2 * (ZMod.stdAddChar (j * s0)).re : ℝ) : ℂ)).re =
        2 * ((C j).re * (ZMod.stdAddChar (j * s0)).re) := by
      intro j
      rw [Complex.mul_re, Complex.ofReal_re, Complex.ofReal_im]
      ring
    have h2l : (2 * (ℓ : ℂ)).re = 2 * ℓ := by simp
    rw [Complex.re_sum, Finset.sum_congr rfl fun j _ => hterm j, ← Finset.mul_sum, h2l] at e'
    linarith
  -- the terms `j = 0` and `j ≠ 0`
  have hC0 : (C 0).re = I.card := by
    rw [hC]
    simp
  have hr0 : (ZMod.stdAddChar (0 * s0)).re = 1 := by simp
  have hcj : ∀ j : ZMod ℓ, j ≠ 0 → (C j).re ≤ 0 := by
    intro j hj
    rw [← hc j]
    exact hneg j hj
  have hrj : ∀ j : ZMod ℓ, -1 ≤ (ZMod.stdAddChar (j * s0)).re := by
    intro j
    have h1 := Complex.abs_re_le_norm (ZMod.stdAddChar (j * s0))
    rw [AddChar.norm_apply] at h1
    linarith [neg_abs_le (ZMod.stdAddChar (j * s0)).re]
  have key : ∑ j ∈ univ.erase 0, (C j).re * (ZMod.stdAddChar (j * s0)).re ≤
      ∑ j ∈ univ.erase 0, -(C j).re := by
    refine Finset.sum_le_sum fun j hj => ?_
    have h1 := hcj j (ne_of_mem_erase hj)
    have h2 := hrj j
    nlinarith
  have hsum : ∑ j ∈ univ.erase 0, -(C j).re = I.card := by
    rw [Finset.sum_neg_distrib, Finset.sum_erase_eq_sub (mem_univ 0), hA, hC0]
    ring
  have hsplit := Finset.add_sum_erase univ
    (fun j => (C j).re * (ZMod.stdAddChar (j * s0)).re) (mem_univ 0)
  rw [hB, hC0, hr0] at hsplit
  have : (ℓ : ℝ) ≤ 2 * I.card := by linarith
  exact_mod_cast this

end ChowlaCosine.NegDefFibre
