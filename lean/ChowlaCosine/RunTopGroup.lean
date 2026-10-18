/-
P21 (PROOFS.md): full cosets are not needed for |B_t| ≍ K³ in finite abelian groups.

STATEMENT FILE (lead, 2026-10-18); proofs by the Lean agent (2026-10-18). The five theorems at the end of the file
are the exact intended statements (unchanged); everything before them is auxiliary.

Setting: p an odd prime, d ∈ ZMod p a non-square, Γ = Fin 4 → ZMod p (coordinates x 0, x 1, x 2, x 3 correspond to
x1, x2, x3, x4 of the paper), t = e_0, and
    A = {x : x 1 ≠ 0 ∧ x 0 * x 1 + x 2 ^ 2 - d * x 3 ^ 2 ≠ 0} ∪ {x : x 1 = 0 ∧ x 0 ≠ x 2 * x 3 ^ 2}.
Characters of Γ are x ↦ ψ (∑ i, c i * x i) for c : Γ, with ψ a primitive additive character of ZMod p.
Claims: A = −A, 0 ∉ A, every line x + ⟨t⟩ meets A in exactly p − 1 points, every nontrivial character sum is real and
≥ −3p, and the run-top set B_t = {m ∈ A : m − t ∈ A, m + t ∉ A} has exactly p³ elements.

Proof outline (formalized below).
* `mem_runSet_iff`: x ∈ A ↔ x 0 ≠ τ(x 1, x 2, x 3), where τ(b, c, e) = c e² if b = 0 and −(c² − d e²)/b otherwise.
  So A is the complement of the graph of τ, and each line x + ⟨t⟩ misses exactly the point with x 0 = τ.
* Run-tops: m ∈ B_t ↔ m 0 = τ − 1 (uses 1 ≠ 0 and 2 ≠ 0 in ZMod p), a graph over (m 1, m 2, m 3): p³ points.
* Realness: A = −A and ψ(−y) = conj ψ(y).
* Lower bound: F(c) = Σ_{b,c',e} (ψ(L)·p[c 0 = 0] − ψ(c 0·τ + L)) with L = c 1 b + c 2 c' + c 3 e.
  If c 0 = 0, F = (p − 1)·Σ ψ(L) = 0. If j = c 0 ≠ 0, F = −Σ_b H(b) with
  H(0) = p Σ_{e : j e² + c 2 = 0} ψ(c 3 e) (Re ≤ 2p, at most two roots) and, for b ≠ 0, completing squares and the
  quadratic Gauss sum (g² = η(−1) p, η(d) = −1) give H(b) = −p ψ(κ b); so Σ_{b ≠ 0} H(b) = p − p²[κ = 0] (Re ≤ p).
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

/-! ### Auxiliary definitions and lemmas -/

/-- The unique point `τ(b, c, e)` of the line `{(s, b, c, e)}` that is missing from the set. -/
def tau (d b c e : ZMod p) : ZMod p :=
  if b = 0 then c * e ^ 2 else -(c ^ 2 - d * e ^ 2) / b

lemma mem_runSet_iff (d : ZMod p) (x : Γ p) :
    x ∈ runSet p d ↔ x 0 ≠ tau p d (x 1) (x 2) (x 3) := by
  simp only [runSet, mem_filter, mem_univ, true_and, tau]
  by_cases h : x 1 = 0
  · rw [if_pos h]
    constructor
    · rintro (⟨h1, _⟩ | ⟨_, h2⟩)
      · exact absurd h h1
      · exact h2
    · intro h2
      exact Or.inr ⟨h, h2⟩
  · rw [if_neg h]
    have key : x 0 * x 1 + x 2 ^ 2 - d * x 3 ^ 2 = 0 ↔ x 0 = -(x 2 ^ 2 - d * x 3 ^ 2) / x 1 := by
      rw [eq_div_iff h]
      constructor <;> intro h' <;> linear_combination h'
    have key' : x 0 ≠ -(x 2 ^ 2 - d * x 3 ^ 2) / x 1 ↔ x 0 * x 1 + x 2 ^ 2 - d * x 3 ^ 2 ≠ 0 :=
      (not_congr key).symm
    rw [key']
    constructor
    · rintro (⟨_, h2⟩ | ⟨h1, _⟩)
      · exact h2
      · exact absurd h1 h
    · intro h2
      exact Or.inl ⟨h, h2⟩

lemma runSet_eq_filter (d : ZMod p) :
    runSet p d = univ.filter fun x : Γ p => x 0 ≠ tau p d (x 1) (x 2) (x 3) := by
  ext x
  rw [mem_runSet_iff]
  simp

lemma tVec_zero : tVec p 0 = 1 := by simp [tVec]

lemma tVec_of_ne {i : Fin 4} (hi : i ≠ 0) : tVec p i = 0 := by simp [tVec, hi]

lemma ringChar_ne_two (hp : p ≠ 2) : ringChar (ZMod p) ≠ 2 := by
  rwa [ZMod.ringChar_zmod_n]

lemma two_ne_zero_zmod (hp : p ≠ 2) : (2 : ZMod p) ≠ 0 :=
  Ring.two_ne_zero (ringChar_ne_two p hp)

/-- Every line has exactly `p − 1` points: the explicit description. -/
lemma line_mem_iff (d : ZMod p) (x : Γ p) (s : ZMod p) :
    x + s • tVec p ∈ runSet p d ↔ x 0 + s ≠ tau p d (x 1) (x 2) (x 3) := by
  rw [mem_runSet_iff]
  simp [tVec_zero, tVec_of_ne]

lemma mem_runTops_iff (hp : p ≠ 2) (d : ZMod p) (m : Γ p) :
    m ∈ runTops p (runSet p d) (tVec p) ↔ m 0 = tau p d (m 1) (m 2) (m 3) - 1 := by
  have h2 := two_ne_zero_zmod p hp
  have hsub : m - tVec p = m + (-1 : ZMod p) • tVec p := by
    rw [neg_one_smul, sub_eq_add_neg]
  have hadd : m + tVec p = m + (1 : ZMod p) • tVec p := by rw [one_smul]
  simp only [runTops, mem_filter]
  rw [hsub, hadd, line_mem_iff, line_mem_iff, mem_runSet_iff]
  constructor
  · rintro ⟨_, _, h⟩
    rw [ne_eq, not_not] at h
    linear_combination h
  · intro h
    refine ⟨?_, ?_, ?_⟩
    · intro h'
      exact one_ne_zero (by linear_combination h - h' : (1 : ZMod p) = 0)
    · intro h'
      exact h2 (by linear_combination h - h')
    · rw [ne_eq, not_not]
      linear_combination h

/-- Coordinates `(b, c, e, a) ↦ ![a, b, c, e]`. -/
def e4 : ZMod p × ZMod p × ZMod p × ZMod p ≃ Γ p where
  toFun q := ![q.2.2.2, q.1, q.2.1, q.2.2.1]
  invFun x := (x 1, x 2, x 3, x 0)
  left_inv q := by rcases q with ⟨b, c, e, a⟩; rfl
  right_inv x := by ext i; fin_cases i <;> rfl

lemma sum_Γ (f : Γ p → ℂ) :
    ∑ x, f x = ∑ b, ∑ c, ∑ e, ∑ a, f ![a, b, c, e] := by
  rw [← (e4 p).sum_comp]
  simp only [Fintype.sum_prod_type]
  rfl

section Characters

variable {p}

lemma sum_lin {ψ : AddChar (ZMod p) ℂ} (hψ : ψ.IsPrimitive) (a : ZMod p) :
    ∑ x : ZMod p, ψ (a * x) = if a = 0 then (p : ℂ) else 0 := by
  simp_rw [mul_comm a]
  rw [AddChar.sum_mulShift a hψ, ZMod.card]
  split_ifs <;> simp

/-- The quadratic character of `ZMod p`, valued in `ℂ`. -/
noncomputable def qchar (p : ℕ) [Fact p.Prime] : MulChar (ZMod p) ℂ :=
  (quadraticChar (ZMod p)).ringHomComp (Int.castRingHom ℂ)

lemma qchar_apply (a : ZMod p) : qchar p a = ((quadraticChar (ZMod p) a : ℤ) : ℂ) := by
  simp [qchar]

lemma qchar_isQuadratic : (qchar p).IsQuadratic :=
  (quadraticChar_isQuadratic (ZMod p)).comp _

lemma qchar_ne_one (hp : p ≠ 2) : qchar p ≠ 1 :=
  (MulChar.ringHomComp_ne_one_iff (Int.castRingHom ℂ).injective_int).mpr
    (quadraticChar_ne_one (ringChar_ne_two p hp))

lemma gauss_sq (hp : p ≠ 2) {ψ : AddChar (ZMod p) ℂ} (hψ : ψ.IsPrimitive) :
    gaussSum (qchar p) ψ ^ 2 = qchar p (-1) * p := by
  have := gaussSum_sq (qchar_ne_one hp) qchar_isQuadratic hψ
  rwa [ZMod.card] at this

/-- `Σ_u ψ(a u²) = η(a) g` for `a ≠ 0`. -/
lemma sum_sq_eq (hp : p ≠ 2) {ψ : AddChar (ZMod p) ℂ} (hψ : ψ.IsPrimitive) {a : ZMod p}
    (ha : a ≠ 0) :
    ∑ u : ZMod p, ψ (a * u ^ 2) = qchar p a * gaussSum (qchar p) ψ := by
  have h1 : ∑ u : ZMod p, ψ (a * u ^ 2) =
      ∑ w : ZMod p, (qchar p w + 1) * ψ (a * w) := by
    rw [← Finset.sum_fiberwise univ (fun u : ZMod p => u ^ 2)]
    refine Finset.sum_congr rfl fun w _ => ?_
    rw [Finset.sum_congr rfl (g := fun _ => ψ (a * w)) (fun u hu => by rw [(mem_filter.mp hu).2])]
    rw [sum_const, nsmul_eq_mul]
    congr 1
    have := quadraticChar_card_sqrts (ringChar_ne_two p hp) w
    rw [Set.toFinset_ofPred] at this
    rw [qchar_apply]
    exact_mod_cast this
  rw [h1]
  simp_rw [add_mul, one_mul]
  rw [sum_add_distrib, sum_lin hψ, if_neg ha, add_zero]
  have h2 : ∑ w : ZMod p, qchar p w * ψ (a * w) = gaussSum (qchar p) (ψ.mulShift a) := by
    simp [gaussSum, AddChar.mulShift_apply]
  have h3 := gaussSum_mulShift_eq (qchar p) ψ (Units.mk0 a ha)
  rw [Units.val_mk0, qchar_isQuadratic.inv] at h3
  rw [h2, h3]

/-- The two-variable quadratic sum: `Σ_u ψ(α u²) · Σ_v ψ(−α d v²) = −p` for `d` a non-square. -/
lemma prod_two (hp : p ≠ 2) {ψ : AddChar (ZMod p) ℂ} (hψ : ψ.IsPrimitive) {d : ZMod p}
    (hd : ¬ IsSquare d) {α : ZMod p} (hα : α ≠ 0) :
    (∑ u : ZMod p, ψ (α * u ^ 2)) * (∑ v : ZMod p, ψ (-(α * d) * v ^ 2)) = -(p : ℂ) := by
  have hd0 : d ≠ 0 := by rintro rfl; exact hd ⟨0, by ring⟩
  have hαd : -(α * d) ≠ 0 := neg_ne_zero.mpr (mul_ne_zero hα hd0)
  rw [sum_sq_eq hp hψ hα, sum_sq_eq hp hψ hαd]
  have key : qchar p α * qchar p (-(α * d)) * qchar p (-1) = -1 := by
    rw [← map_mul, ← map_mul, show α * -(α * d) * -1 = α ^ 2 * d by ring, map_mul, qchar_apply,
      qchar_apply, quadraticChar_sq_one' hα, quadraticChar_neg_one_iff_not_isSquare.mpr hd]
    simp
  calc qchar p α * gaussSum (qchar p) ψ * (qchar p (-(α * d)) * gaussSum (qchar p) ψ)
      = qchar p α * qchar p (-(α * d)) * gaussSum (qchar p) ψ ^ 2 := by ring
    _ = qchar p α * qchar p (-(α * d)) * qchar p (-1) * p := by rw [gauss_sq hp hψ]; ring
    _ = -(p : ℂ) := by rw [key]; ring

/-- Completing the square. -/
lemma complete_sq (hp : p ≠ 2) (ψ : AddChar (ZMod p) ℂ) {a : ZMod p} (ha : a ≠ 0) (b : ZMod p) :
    ∑ u : ZMod p, ψ (a * u ^ 2 + b * u) = ψ (-(b ^ 2 / (4 * a))) * ∑ u : ZMod p, ψ (a * u ^ 2) := by
  have h2 := two_ne_zero_zmod p hp
  have h4 : (4 : ZMod p) ≠ 0 := by
    rw [show (4 : ZMod p) = 2 * 2 by norm_num]; exact mul_ne_zero h2 h2
  calc ∑ u : ZMod p, ψ (a * u ^ 2 + b * u)
      = ∑ u : ZMod p, ψ (a * (u - b / (2 * a)) ^ 2 + b * (u - b / (2 * a))) :=
        ((Equiv.subRight (b / (2 * a))).sum_comp (fun u => ψ (a * u ^ 2 + b * u))).symm
    _ = ∑ u : ZMod p, ψ (-(b ^ 2 / (4 * a))) * ψ (a * u ^ 2) := by
        refine Finset.sum_congr rfl fun u _ => ?_
        rw [← AddChar.map_add_eq_mul]
        congr 1
        field_simp
        ring
    _ = _ := (Finset.mul_sum _ _ _).symm

lemma two_var (hp : p ≠ 2) {ψ : AddChar (ZMod p) ℂ} (hψ : ψ.IsPrimitive) {d : ZMod p}
    (hd : ¬ IsSquare d) {α : ZMod p} (hα : α ≠ 0) (c2 c3 : ZMod p) :
    (∑ u : ZMod p, ψ (α * u ^ 2 + c2 * u)) * (∑ v : ZMod p, ψ (-(α * d) * v ^ 2 + c3 * v)) =
      -(p : ℂ) * ψ (-(c2 ^ 2 / (4 * α)) + -(c3 ^ 2 / (4 * -(α * d)))) := by
  have hd0 : d ≠ 0 := by rintro rfl; exact hd ⟨0, by ring⟩
  have hαd : -(α * d) ≠ 0 := neg_ne_zero.mpr (mul_ne_zero hα hd0)
  rw [complete_sq hp ψ hα, complete_sq hp ψ hαd, AddChar.map_add_eq_mul, ← prod_two hp hψ hd hα]
  ring

/-- `Σ_{a ≠ t} ψ(j a + L) = ψ(L) · p[j = 0] − ψ(j t + L)`. -/
lemma inner_sum {ψ : AddChar (ZMod p) ℂ} (hψ : ψ.IsPrimitive) (t L j : ZMod p) :
    ∑ a : ZMod p, (if a ≠ t then ψ (j * a + L) else 0) =
      ψ L * (if j = 0 then (p : ℂ) else 0) - ψ (j * t + L) := by
  rw [← Finset.sum_filter, Finset.filter_ne' univ t, Finset.sum_erase_eq_sub (mem_univ t)]
  congr 1
  simp_rw [AddChar.map_add_eq_mul, ← Finset.sum_mul, sum_lin hψ]
  ring

lemma triple_zero {ψ : AddChar (ZMod p) ℂ} (hψ : ψ.IsPrimitive) (c1 c2 c3 : ZMod p)
    (h : ¬ (c1 = 0 ∧ c2 = 0 ∧ c3 = 0)) :
    ∑ b : ZMod p, ∑ c : ZMod p, ∑ e : ZMod p, ψ (c1 * b + c2 * c + c3 * e) = 0 := by
  simp only [AddChar.map_add_eq_mul, ← Finset.mul_sum, ← Finset.sum_mul, sum_lin hψ]
  by_cases h1 : c1 = 0 <;> by_cases h2 : c2 = 0 <;> by_cases h3 : c3 = 0 <;> simp_all

lemma card_quad_le_two (hp : p ≠ 2) {j : ZMod p} (hj : j ≠ 0) (c2 : ZMod p) :
    (univ.filter fun e : ZMod p => j * e ^ 2 + c2 = 0).card ≤ 2 := by
  have h1 := quadraticChar_card_sqrts (ringChar_ne_two p hp) (-c2 / j)
  rw [Set.toFinset_ofPred] at h1
  have hfilt : (univ.filter fun e : ZMod p => j * e ^ 2 + c2 = 0) =
      univ.filter fun e : ZMod p => e ^ 2 = -c2 / j := by
    ext e
    simp only [mem_filter, mem_univ, true_and]
    rw [eq_div_iff hj]
    constructor <;> intro h <;> linear_combination h
  rw [hfilt]
  have h2 : quadraticChar (ZMod p) (-c2 / j) ≤ 1 := by
    rcases quadraticChar_isQuadratic (ZMod p) (-c2 / j) with h | h | h <;> rw [h] <;> norm_num
  omega

/-- The `b = 0` slice. -/
lemma H_zero {ψ : AddChar (ZMod p) ℂ} (hψ : ψ.IsPrimitive) (d j c1 c2 c3 : ZMod p) :
    ∑ c : ZMod p, ∑ e : ZMod p, ψ (j * tau p d 0 c e + (c1 * 0 + c2 * c + c3 * e)) =
      ∑ e : ZMod p, ψ (c3 * e) * (if j * e ^ 2 + c2 = 0 then (p : ℂ) else 0) := by
  simp only [tau, ↓reduceIte]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun e _ => ?_
  rw [← sum_lin hψ (j * e ^ 2 + c2), Finset.mul_sum]
  refine Finset.sum_congr rfl fun c _ => ?_
  rw [← AddChar.map_add_eq_mul]
  congr 1
  ring

lemma re_H_zero_le (hp : p ≠ 2) {ψ : AddChar (ZMod p) ℂ} {j : ZMod p} (hj : j ≠ 0)
    (c2 c3 : ZMod p) :
    (∑ e : ZMod p, ψ (c3 * e) * (if j * e ^ 2 + c2 = 0 then (p : ℂ) else 0)).re ≤ 2 * p := by
  rw [Complex.re_sum]
  calc ∑ e : ZMod p, (ψ (c3 * e) * (if j * e ^ 2 + c2 = 0 then (p : ℂ) else 0)).re
      ≤ ∑ e : ZMod p, (p : ℝ) * (if j * e ^ 2 + c2 = 0 then (1 : ℝ) else 0) := by
        refine Finset.sum_le_sum fun e _ => ?_
        split_ifs
        · have hre : (ψ (c3 * e)).re ≤ 1 := by
            have := Complex.re_le_norm (ψ (c3 * e))
            rwa [AddChar.norm_apply] at this
          have hp0 : (0 : ℝ) ≤ p := Nat.cast_nonneg p
          simp only [Complex.mul_re, Complex.natCast_re, Complex.natCast_im, mul_zero, sub_zero,
            mul_one]
          nlinarith
        · simp
    _ = (p : ℝ) * (univ.filter fun e : ZMod p => j * e ^ 2 + c2 = 0).card := by
        rw [← Finset.mul_sum, Finset.sum_boole]
    _ ≤ (p : ℝ) * 2 := by
        gcongr
        exact_mod_cast card_quad_le_two hp hj c2
    _ = 2 * p := by ring

/-- The `b ≠ 0` slices. -/
lemma H_ne (hp : p ≠ 2) {ψ : AddChar (ZMod p) ℂ} (hψ : ψ.IsPrimitive) {d : ZMod p}
    (hd : ¬ IsSquare d) {j : ZMod p} (hj : j ≠ 0) (c1 c2 c3 : ZMod p) {b : ZMod p} (hb : b ≠ 0) :
    ∑ c : ZMod p, ∑ e : ZMod p, ψ (j * tau p d b c e + (c1 * b + c2 * c + c3 * e)) =
      -(p : ℂ) * ψ ((c1 + c2 ^ 2 / (4 * j) - c3 ^ 2 / (4 * j * d)) * b) := by
  have hd0 : d ≠ 0 := by rintro rfl; exact hd ⟨0, by ring⟩
  have h2 := two_ne_zero_zmod p hp
  have h4 : (4 : ZMod p) ≠ 0 := by
    rw [show (4 : ZMod p) = 2 * 2 by norm_num]; exact mul_ne_zero h2 h2
  have hα : -(j / b) ≠ 0 := neg_ne_zero.mpr (div_ne_zero hj hb)
  calc ∑ c : ZMod p, ∑ e : ZMod p, ψ (j * tau p d b c e + (c1 * b + c2 * c + c3 * e))
      = ∑ c : ZMod p, ∑ e : ZMod p, ψ (c1 * b) * (ψ (-(j / b) * c ^ 2 + c2 * c) *
          ψ (-(-(j / b) * d) * e ^ 2 + c3 * e)) := by
        refine Finset.sum_congr rfl fun c _ => Finset.sum_congr rfl fun e _ => ?_
        rw [← AddChar.map_add_eq_mul, ← AddChar.map_add_eq_mul]
        congr 1
        simp only [tau, if_neg hb]
        field_simp
        ring
    _ = ψ (c1 * b) * ((∑ c : ZMod p, ψ (-(j / b) * c ^ 2 + c2 * c)) *
          (∑ e : ZMod p, ψ (-(-(j / b) * d) * e ^ 2 + c3 * e))) := by
        rw [Finset.sum_mul, Finset.mul_sum]
        refine Finset.sum_congr rfl fun c _ => ?_
        rw [Finset.mul_sum, Finset.mul_sum]
    _ = ψ (c1 * b) * (-(p : ℂ) * ψ (-(c2 ^ 2 / (4 * -(j / b))) +
          -(c3 ^ 2 / (4 * -(-(j / b) * d))))) := by
        rw [two_var hp hψ hd hα]
    _ = _ := by
        rw [mul_left_comm (ψ (c1 * b)), ← AddChar.map_add_eq_mul]
        congr 2
        field_simp
        ring

/-- Explicit form of the character sum. -/
lemma charSum_eq {ψ : AddChar (ZMod p) ℂ} (hψ : ψ.IsPrimitive) (d : ZMod p) (c : Γ p) :
    charSum p ψ (runSet p d) c =
      ∑ b : ZMod p, ∑ c' : ZMod p, ∑ e : ZMod p,
        (ψ (c 1 * b + c 2 * c' + c 3 * e) * (if c 0 = 0 then (p : ℂ) else 0) -
          ψ (c 0 * tau p d b c' e + (c 1 * b + c 2 * c' + c 3 * e))) := by
  rw [charSum, runSet_eq_filter, Finset.sum_filter, sum_Γ]
  refine Finset.sum_congr rfl fun b _ => Finset.sum_congr rfl fun c' _ =>
    Finset.sum_congr rfl fun e _ => ?_
  rw [← inner_sum hψ]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [Fin.sum_univ_four]
  show (if a ≠ tau p d b c' e then ψ (c 0 * a + c 1 * b + c 2 * c' + c 3 * e) else 0) = _
  rw [show c 0 * a + c 1 * b + c 2 * c' + c 3 * e = c 0 * a + (c 1 * b + c 2 * c' + c 3 * e) by ring]

end Characters

/-! ### The five P21 statements -/

-- The hypothesis `p ≠ 2` is not needed for the symmetry; it is kept to preserve the stated form.
set_option linter.unusedVariables false in
theorem runSet_neg (hp : p ≠ 2) (d : ZMod p) (x : Γ p) :
    -x ∈ runSet p d ↔ x ∈ runSet p d := by
  have e1 : (-x) 0 * (-x) 1 + (-x) 2 ^ 2 - d * (-x) 3 ^ 2 = x 0 * x 1 + x 2 ^ 2 - d * x 3 ^ 2 := by
    simp only [Pi.neg_apply]; ring
  have e2 : (-x) 0 = (-x) 2 * (-x) 3 ^ 2 ↔ x 0 = x 2 * x 3 ^ 2 := by
    simp only [Pi.neg_apply]
    constructor <;> intro h <;> linear_combination -h
  have e3 : (-x) 1 = 0 ↔ x 1 = 0 := by simp
  simp only [runSet, mem_filter, mem_univ, true_and, ne_eq]
  rw [e1, e2, e3]

theorem zero_not_mem_runSet (d : ZMod p) : (0 : Γ p) ∉ runSet p d := by
  rw [mem_runSet_iff]
  simp [tau]

/-- Every line `x + ⟨t⟩` meets the set in exactly `p − 1` points. -/
theorem card_line_inter (d : ZMod p) (x : Γ p) :
    ((univ : Finset (ZMod p)).filter fun s => x + s • tVec p ∈ runSet p d).card = p - 1 := by
  have : ((univ : Finset (ZMod p)).filter fun s => x + s • tVec p ∈ runSet p d) =
      univ.erase (tau p d (x 1) (x 2) (x 3) - x 0) := by
    ext s
    rw [mem_filter, line_mem_iff, mem_erase]
    simp only [mem_univ, and_true, true_and]
    constructor <;> intro h h' <;> apply h <;> linear_combination h'
  rw [this, card_erase_of_mem (mem_univ _), card_univ, ZMod.card]

/-- |B_t| = p³. -/
theorem card_runTops (hp : p ≠ 2) (d : ZMod p) :
    (runTops p (runSet p d) (tVec p)).card = p ^ 3 := by
  have : runTops p (runSet p d) (tVec p) =
      (univ : Finset (ZMod p × ZMod p × ZMod p)).image
        (fun q => ![tau p d q.1 q.2.1 q.2.2 - 1, q.1, q.2.1, q.2.2]) := by
    ext m
    rw [mem_runTops_iff p hp, mem_image]
    constructor
    · intro h
      refine ⟨(m 1, m 2, m 3), mem_univ _, ?_⟩
      ext i
      fin_cases i <;> simp [h]
    · rintro ⟨q, -, rfl⟩
      simp
  rw [this, card_image_of_injective, card_univ, Fintype.card_prod, Fintype.card_prod, ZMod.card]
  · ring
  · intro q q' h
    have h1 := congrFun h 1
    have h2 := congrFun h 2
    have h3 := congrFun h 3
    simp only [Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons,
      Matrix.tail_cons] at h1 h2 h3
    exact Prod.ext h1 (Prod.ext h2 h3)

/-- Every nontrivial character sum is real and at least −3p (so K ≤ 3p and |B_t| = p³ ≥ K³/27). -/
theorem charSum_lower (hp : p ≠ 2) (d : ZMod p) (hd : ¬ IsSquare d)
    (ψ : AddChar (ZMod p) ℂ) (hψ : ψ.IsPrimitive) (c : Γ p) (hc : c ≠ 0) :
    (charSum p ψ (runSet p d) c).im = 0 ∧ -(3 * (p : ℝ)) ≤ (charSum p ψ (runSet p d) c).re := by
  constructor
  · -- realness from `A = −A`
    rw [← Complex.conj_eq_iff_im]
    unfold charSum
    rw [map_sum]
    refine Finset.sum_nbij' (fun x => -x) (fun x => -x) ?_ ?_ ?_ ?_ ?_
    · intro x hx; exact (runSet_neg p hp d x).mpr hx
    · intro x hx; exact (runSet_neg p hp d x).mpr hx
    · intro x _; simp
    · intro x _; simp
    · intro x _
      rw [← AddChar.map_neg_eq_conj]
      congr 1
      simp [Finset.sum_neg_distrib]
  · rw [charSum_eq hψ]
    by_cases hj : c 0 = 0
    · -- `c 0 = 0`: the sum vanishes
      have hc' : ¬ (c 1 = 0 ∧ c 2 = 0 ∧ c 3 = 0) := by
        rintro ⟨h1, h2, h3⟩
        apply hc
        ext i
        fin_cases i <;> simp [hj, h1, h2, h3]
      have : ∑ b : ZMod p, ∑ c' : ZMod p, ∑ e : ZMod p,
          (ψ (c 1 * b + c 2 * c' + c 3 * e) * (if c 0 = 0 then (p : ℂ) else 0) -
            ψ (c 0 * tau p d b c' e + (c 1 * b + c 2 * c' + c 3 * e))) =
          ((p : ℂ) - 1) * ∑ b : ZMod p, ∑ c' : ZMod p, ∑ e : ZMod p,
            ψ (c 1 * b + c 2 * c' + c 3 * e) := by
        simp only [hj, ↓reduceIte, zero_mul, zero_add, Finset.mul_sum]
        refine Finset.sum_congr rfl fun b _ => Finset.sum_congr rfl fun c' _ =>
          Finset.sum_congr rfl fun e _ => ?_
        ring
      rw [this, triple_zero hψ _ _ _ hc', mul_zero, Complex.zero_re]
      have : (0 : ℝ) ≤ p := Nat.cast_nonneg p
      linarith
    · -- `c 0 = j ≠ 0`
      have hsplit : ∑ b : ZMod p, ∑ c' : ZMod p, ∑ e : ZMod p,
          (ψ (c 1 * b + c 2 * c' + c 3 * e) * (if c 0 = 0 then (p : ℂ) else 0) -
            ψ (c 0 * tau p d b c' e + (c 1 * b + c 2 * c' + c 3 * e))) =
          -(∑ e : ZMod p, ψ (c 3 * e) * (if c 0 * e ^ 2 + c 2 = 0 then (p : ℂ) else 0) +
            -(p : ℂ) * ((if (c 1 + c 2 ^ 2 / (4 * c 0) - c 3 ^ 2 / (4 * c 0 * d)) = 0
              then (p : ℂ) else 0) - 1)) := by
        simp only [hj, ↓reduceIte, mul_zero, zero_sub, Finset.sum_neg_distrib]
        congr 1
        rw [← Finset.add_sum_erase univ _ (mem_univ 0), H_zero hψ]
        congr 1
        rw [Finset.sum_congr rfl fun b hb => H_ne hp hψ hd hj (c 1) (c 2) (c 3) (ne_of_mem_erase hb),
          ← Finset.mul_sum, Finset.sum_erase_eq_sub (mem_univ 0), sum_lin hψ, mul_zero,
          AddChar.map_zero_eq_one]
      rw [hsplit, Complex.neg_re, Complex.add_re]
      have h0 := re_H_zero_le hp (ψ := ψ) hj (c 2) (c 3)
      have h1 : (-(p : ℂ) * ((if (c 1 + c 2 ^ 2 / (4 * c 0) - c 3 ^ 2 / (4 * c 0 * d)) = 0
              then (p : ℂ) else 0) - 1)).re ≤ p := by
        have hp0 : (0 : ℝ) ≤ p := Nat.cast_nonneg p
        split_ifs
        · simp only [Complex.mul_re, Complex.neg_re, Complex.natCast_re, Complex.sub_re,
            Complex.one_re, Complex.neg_im, Complex.natCast_im, Complex.sub_im, Complex.one_im]
          nlinarith
        · simp
      linarith

end ChowlaCosine.RunTopGroup
