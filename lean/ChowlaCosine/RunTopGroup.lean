/-
P21 (PROOFS.md): full cosets are not needed for |B_t| ≍ K³ in finite abelian groups.

STATEMENT FILE (lead, 2026-10-18). The theorems below are the exact intended statements; the proofs are `sorry`
pending formalization. This file is NOT imported by `ChowlaCosine.lean`, so `AxiomCheck` is unaffected.

Setting: p an odd prime, d ∈ ZMod p a non-square, Γ = Fin 4 → ZMod p (coordinates x 0, x 1, x 2, x 3 correspond to
x1, x2, x3, x4 of the paper), t = e_0, and
    A = {x : x 1 ≠ 0 ∧ x 0 * x 1 + x 2 ^ 2 - d * x 3 ^ 2 ≠ 0} ∪ {x : x 1 = 0 ∧ x 0 ≠ x 2 * x 3 ^ 2}.
Characters of Γ are x ↦ ψ (∑ i, c i * x i) for c : Γ, with ψ a primitive additive character of ZMod p.
Claims: A = −A, 0 ∉ A, every line x + ⟨t⟩ meets A in exactly p − 1 points, every nontrivial character sum is real and
≥ −3p, and the run-top set B_t = {m ∈ A : m − t ∈ A, m + t ∉ A} has exactly p³ elements.
-/
import Mathlib

namespace ChowlaCosine.RunTopGroup

open Finset

variable (p : ℕ) [Fact p.Prime]

/-- The group Γ = (ZMod p)^4. -/
abbrev Γ := Fin 4 → ZMod p

/-- The step t = e_0. -/
def tVec : Γ p := Pi.single 0 1

/-- The P21 set. -/
def runSet (d : ZMod p) : Finset (Γ p) :=
  univ.filter fun x =>
    (x 1 ≠ 0 ∧ x 0 * x 1 + x 2 ^ 2 - d * x 3 ^ 2 ≠ 0) ∨ (x 1 = 0 ∧ x 0 ≠ x 2 * x 3 ^ 2)

/-- Run-tops of a set `A` in direction `t`. -/
def runTops (A : Finset (Γ p)) (t : Γ p) : Finset (Γ p) :=
  A.filter fun m => m - t ∈ A ∧ m + t ∉ A

/-- The character sum F(c) = ∑_{x∈A} ψ(c · x). -/
noncomputable def charSum (ψ : AddChar (ZMod p) ℂ) (A : Finset (Γ p)) (c : Γ p) : ℂ :=
  ∑ x ∈ A, ψ (∑ i, c i * x i)

theorem runSet_neg (hp : p ≠ 2) (d : ZMod p) (x : Γ p) :
    -x ∈ runSet p d ↔ x ∈ runSet p d := by
  sorry

theorem zero_not_mem_runSet (d : ZMod p) : (0 : Γ p) ∉ runSet p d := by
  sorry

/-- Every line `x + ⟨t⟩` meets the set in exactly `p − 1` points. -/
theorem card_line_inter (d : ZMod p) (x : Γ p) :
    ((univ : Finset (ZMod p)).filter fun s => x + s • tVec p ∈ runSet p d).card = p - 1 := by
  sorry

/-- |B_t| = p³. -/
theorem card_runTops (hp : p ≠ 2) (d : ZMod p) :
    (runTops p (runSet p d) (tVec p)).card = p ^ 3 := by
  sorry

/-- Every nontrivial character sum is real and at least −3p (so K ≤ 3p and |B_t| = p³ ≥ K³/27). -/
theorem charSum_lower (hp : p ≠ 2) (d : ZMod p) (hd : ¬ IsSquare d)
    (ψ : AddChar (ZMod p) ℂ) (hψ : ψ.IsPrimitive) (c : Γ p) (hc : c ≠ 0) :
    (charSum p ψ (runSet p d) c).im = 0 ∧ -(3 * (p : ℝ)) ≤ (charSum p ψ (runSet p d) c).re := by
  sorry

end ChowlaCosine.RunTopGroup
