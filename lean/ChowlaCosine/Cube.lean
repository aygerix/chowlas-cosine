import Mathlib

/-!
# The cube framework

1. **Cube identity.** For real `θ₁, …, θ_k` and a finite family `J` of subsets of `Fin k`,

   `∑_{S∈J} ∏_{j∈S} 2 cos θ_j = ∑_{S∈J} ∑_{ε : S → {±1}} cos (∑_{j∈S} ε_j θ_j)`.

   Here `{±1}` is encoded as the unit group `ℤˣ` (whose elements are exactly `1` and `-1`),
   and `ε` ranges over **all** functions `↥S → ℤˣ`. The identity holds for every subset `S`
   (for `S = ∅` both sides equal `1`), so nonemptiness of the members of `J` is not needed.

2. **Multilinear vertex lemma.** The multilinear polynomial
   `p_J(y) = ∑_{S∈J} ∏_{j∈S} y_j` attains its minimum over the box `[a,b]^k` (`a ≤ b`) at a
   vertex `{a,b}^k`; in particular over `[-2,2]^k` at a point of `{±2}^k`.

3. Consequence: `min_θ ∑_{S∈J} ∑_ε cos (∑ ε_j θ_j) = min_{v ∈ {±2}^k} p_J(v)`, attained.
-/

open Real

namespace ChowlaCosine

/-- `2 cos θ = ∑_{e ∈ {±1}} exp (i e θ)`, with `{±1} = ℤˣ`. -/
theorem two_cos_eq_sum_units (θ : ℝ) :
    ((2 * Real.cos θ : ℝ) : ℂ) =
      ∑ e : ℤˣ, Complex.exp ((((e : ℤ) : ℝ) * θ : ℝ) * Complex.I) := by
  rw [Fintype.sum_eq_add 1 (-1) (by decide) (by
    intro u hu
    rcases Int.units_eq_one_or u with h | h
    · exact absurd h hu.1
    · exact absurd h hu.2)]
  rw [Complex.ofReal_mul, Complex.ofReal_cos, Complex.ofReal_ofNat, Complex.two_cos]
  congr 2
  · push_cast; ring
  · push_cast; ring

/-- **Cube identity for one subset.** `∏_{j∈S} 2 cos θ_j = ∑_{ε : S → {±1}} cos (∑_{j∈S} ε_j θ_j)`. -/
theorem prod_two_cos_eq_sum_cos {k : ℕ} (S : Finset (Fin k)) (θ : Fin k → ℝ) :
    ∏ j ∈ S, (2 * Real.cos (θ j)) =
      ∑ ε : (S → ℤˣ), Real.cos (∑ j : S, (((ε j : ℤˣ) : ℤ) : ℝ) * θ j) := by
  have h : ((∏ j ∈ S, (2 * Real.cos (θ j)) : ℝ) : ℂ) =
      ∑ ε : (S → ℤˣ), Complex.exp
        (((∑ j : S, (((ε j : ℤˣ) : ℤ) : ℝ) * θ j : ℝ) : ℂ) * Complex.I) := by
    rw [Complex.ofReal_prod, ← Finset.prod_coe_sort S]
    simp_rw [two_cos_eq_sum_units]
    rw [Fintype.prod_sum]
    refine Fintype.sum_congr _ _ (fun ε => ?_)
    rw [Complex.ofReal_sum, Finset.sum_mul, Complex.exp_sum]
  have h2 := congrArg Complex.re h
  rw [Complex.ofReal_re, Complex.re_sum] at h2
  simp_rw [Complex.exp_ofReal_mul_I_re] at h2
  exact h2

/-- The cosine side of the cube framework: `∑_{S∈J} ∑_{ε : S → {±1}} cos (∑_{j∈S} ε_j θ_j)`. -/
noncomputable def cubeSum {k : ℕ} (J : Finset (Finset (Fin k))) (θ : Fin k → ℝ) : ℝ :=
  ∑ S ∈ J, ∑ ε : (S → ℤˣ), Real.cos (∑ j : S, (((ε j : ℤˣ) : ℤ) : ℝ) * θ j)

/-- The multilinear polynomial `p_J(y) = ∑_{S∈J} ∏_{j∈S} y_j`. -/
def multilinPoly {k : ℕ} (J : Finset (Finset (Fin k))) (y : Fin k → ℝ) : ℝ :=
  ∑ S ∈ J, ∏ j ∈ S, y j

/-- **Cube identity.** `∑_{S∈J} ∏_{j∈S} 2 cos θ_j = ∑_{S∈J} ∑_{ε : S → {±1}} cos (∑ ε_j θ_j)`. -/
theorem sum_prod_two_cos_eq_cubeSum {k : ℕ} (J : Finset (Finset (Fin k))) (θ : Fin k → ℝ) :
    ∑ S ∈ J, ∏ j ∈ S, (2 * Real.cos (θ j)) =
      ∑ S ∈ J, ∑ ε : (S → ℤˣ), Real.cos (∑ j : S, (((ε j : ℤˣ) : ℤ) : ℝ) * θ j) :=
  Finset.sum_congr rfl (fun S _ => prod_two_cos_eq_sum_cos S θ)

/-- In the language of `cubeSum` and `multilinPoly`: `cubeSum J θ = p_J (2 cos θ)`. -/
theorem cubeSum_eq_multilinPoly {k : ℕ} (J : Finset (Finset (Fin k))) (θ : Fin k → ℝ) :
    cubeSum J θ = multilinPoly J (fun j => 2 * Real.cos (θ j)) :=
  (sum_prod_two_cos_eq_cubeSum J θ).symm

/-- `p_J` is affine in each single coordinate. -/
theorem multilinPoly_update {k : ℕ} (J : Finset (Finset (Fin k))) (y : Fin k → ℝ) (i : Fin k)
    (t : ℝ) :
    multilinPoly J (Function.update y i t) =
      (∑ S ∈ J, if i ∈ S then 0 else ∏ j ∈ S, y j) +
        t * ∑ S ∈ J, if i ∈ S then ∏ j ∈ S \ {i}, y j else 0 := by
  rw [multilinPoly, Finset.mul_sum, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl (fun S _ => ?_)
  by_cases h : i ∈ S
  · rw [Finset.prod_update_of_mem h, if_pos h, if_pos h, zero_add]
  · rw [Finset.prod_update_of_notMem h, if_neg h, if_neg h, mul_zero, add_zero]

/-- One coordinate can be pushed to an endpoint without increasing `p_J`. -/
theorem exists_endpoint_le {k : ℕ} (J : Finset (Finset (Fin k))) (y : Fin k → ℝ) (i : Fin k)
    {a b t : ℝ} (ht : t ∈ Set.Icc a b) :
    ∃ s, (s = a ∨ s = b) ∧
      multilinPoly J (Function.update y i s) ≤ multilinPoly J (Function.update y i t) := by
  set c₀ := ∑ S ∈ J, if i ∈ S then 0 else ∏ j ∈ S, y j
  set c₁ := ∑ S ∈ J, if i ∈ S then ∏ j ∈ S \ {i}, y j else 0
  have key : ∀ s, multilinPoly J (Function.update y i s) = c₀ + s * c₁ :=
    fun s => multilinPoly_update J y i s
  by_cases hc : 0 ≤ c₁
  · refine ⟨a, Or.inl rfl, ?_⟩
    rw [key, key]
    have := mul_le_mul_of_nonneg_right ht.1 hc
    linarith
  · refine ⟨b, Or.inr rfl, ?_⟩
    rw [key, key]
    have := mul_le_mul_of_nonpos_right ht.2 (le_of_lt (not_le.mp hc))
    linarith

/-- Vertex reduction on a set `F` of coordinates, by induction on `F`. -/
theorem exists_vertex_on_le {k : ℕ} (J : Finset (Finset (Fin k))) {a b : ℝ} (hab : a ≤ b)
    (F : Finset (Fin k)) :
    ∀ y : Fin k → ℝ, (∀ j, y j ∈ Set.Icc a b) →
      ∃ v : Fin k → ℝ, (∀ j, v j ∈ Set.Icc a b) ∧ (∀ j ∈ F, v j = a ∨ v j = b) ∧
        multilinPoly J v ≤ multilinPoly J y := by
  induction F using Finset.induction_on with
  | empty =>
    intro y hy
    exact ⟨y, hy, by simp, le_rfl⟩
  | insert i F _ ih =>
    intro y hy
    obtain ⟨v, hvbox, hvF, hvle⟩ := ih y hy
    obtain ⟨s, hs, hsle⟩ := exists_endpoint_le J v i (hvbox i)
    refine ⟨Function.update v i s, ?_, ?_, ?_⟩
    · intro j
      by_cases hj : j = i
      · subst hj
        rw [Function.update_self]
        rcases hs with rfl | rfl
        · exact ⟨le_rfl, hab⟩
        · exact ⟨hab, le_rfl⟩
      · rw [Function.update_of_ne hj]
        exact hvbox j
    · intro j hj
      by_cases hji : j = i
      · subst hji
        rw [Function.update_self]
        exact hs
      · rw [Function.update_of_ne hji]
        exact hvF j ((Finset.mem_insert.mp hj).resolve_left hji)
    · rw [Function.update_eq_self] at hsle
      exact hsle.trans hvle

/-- **Multilinear vertex lemma (pointwise form).** For `a ≤ b` and `y ∈ [a,b]^k` there is a
vertex `v ∈ {a,b}^k` with `p_J(v) ≤ p_J(y)`. -/
theorem exists_vertex_le {k : ℕ} (J : Finset (Finset (Fin k))) {a b : ℝ} (hab : a ≤ b)
    (y : Fin k → ℝ) (hy : ∀ j, y j ∈ Set.Icc a b) :
    ∃ v : Fin k → ℝ, (∀ j, v j = a ∨ v j = b) ∧ multilinPoly J v ≤ multilinPoly J y := by
  obtain ⟨v, _, hvF, hle⟩ := exists_vertex_on_le J hab Finset.univ y hy
  exact ⟨v, fun j => hvF j (Finset.mem_univ j), hle⟩

/-- **Multilinear vertex lemma.** For `a ≤ b`, `p_J` attains its minimum over the box
`[a,b]^k` at a vertex: there is `v ∈ {a,b}^k` with `p_J(v) ≤ p_J(y)` for all `y ∈ [a,b]^k`.
(Since `v` itself lies in the box, `min_{box} p_J = min_{vertices} p_J`.) -/
theorem multilinPoly_min_at_vertex {k : ℕ} (J : Finset (Finset (Fin k))) {a b : ℝ}
    (hab : a ≤ b) :
    ∃ v : Fin k → ℝ, (∀ j, v j = a ∨ v j = b) ∧
      ∀ y : Fin k → ℝ, (∀ j, y j ∈ Set.Icc a b) → multilinPoly J v ≤ multilinPoly J y := by
  classical
  let V : Finset (Fin k → ℝ) := Fintype.piFinset (fun _ => ({a, b} : Finset ℝ))
  have hV : V.Nonempty := ⟨fun _ => a, by simp [V, Fintype.mem_piFinset]⟩
  obtain ⟨v, hvV, hvmin⟩ := Finset.exists_min_image V (multilinPoly J) hV
  refine ⟨v, ?_, ?_⟩
  · intro j
    have := (Fintype.mem_piFinset.mp hvV) j
    simpa using this
  · intro y hy
    obtain ⟨w, hw, hwle⟩ := exists_vertex_le J hab y hy
    have hwV : w ∈ V := by
      simp only [V, Fintype.mem_piFinset, Finset.mem_insert, Finset.mem_singleton]
      exact hw
    exact (hvmin w hwV).trans hwle

/-- The `[-2,2]` case of the vertex lemma. -/
theorem multilinPoly_min_at_vertex_two {k : ℕ} (J : Finset (Finset (Fin k))) :
    ∃ v : Fin k → ℝ, (∀ j, v j = -2 ∨ v j = 2) ∧
      ∀ y : Fin k → ℝ, (∀ j, y j ∈ Set.Icc (-2 : ℝ) 2) → multilinPoly J v ≤ multilinPoly J y :=
  multilinPoly_min_at_vertex J (by norm_num)

/-- **Cube framework, minimum.** There is a vertex `v ∈ {±2}^k` such that
`p_J(v) ≤ ∑_{S∈J} ∑_{ε} cos (∑ ε_j θ_j)` for **all** real `θ`, with equality for some `θ`
(namely `θ_j ∈ {0, π}`). Hence `min_θ cubeSum J θ = min_{v ∈ {±2}^k} p_J(v)`. -/
theorem cubeSum_min {k : ℕ} (J : Finset (Finset (Fin k))) :
    ∃ v : Fin k → ℝ, (∀ j, v j = -2 ∨ v j = 2) ∧
      (∀ θ : Fin k → ℝ, multilinPoly J v ≤ cubeSum J θ) ∧
      (∃ θ : Fin k → ℝ, cubeSum J θ = multilinPoly J v) := by
  classical
  obtain ⟨v, hv, hmin⟩ := multilinPoly_min_at_vertex_two J
  refine ⟨v, hv, ?_, ?_⟩
  · intro θ
    rw [cubeSum_eq_multilinPoly]
    apply hmin
    intro j
    constructor <;> nlinarith [Real.neg_one_le_cos (θ j), Real.cos_le_one (θ j)]
  · refine ⟨fun j => if v j = 2 then 0 else π, ?_⟩
    rw [cubeSum_eq_multilinPoly]
    congr 1
    ext j
    show 2 * Real.cos (if v j = 2 then 0 else π) = v j
    by_cases h : v j = 2
    · rw [if_pos h, Real.cos_zero, h]
      ring
    · have h' : v j = -2 := (hv j).resolve_right h
      rw [if_neg h, Real.cos_pi, h']
      ring

end ChowlaCosine
