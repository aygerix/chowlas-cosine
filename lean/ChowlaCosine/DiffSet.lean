import ChowlaCosine.Basic

/-!
# The difference-set identity and the Sidon consequence

For a finite `B ⊆ ℤ` and real `x`,

  `‖∑_{b ∈ B} exp (i b x)‖² = |B| + 2 ∑_{(u,v) ∈ B × B, u < v} cos ((v - u) x)`.

If the positive differences `v - u` (`u < v` in `B`) are pairwise distinct, they form a
genuine finite set `A ⊆ ℕ_{>0}` with `|A| = |B| (|B| - 1) / 2` and
`f_A(x) ≥ -|B| / 2` for **every** real `x`.
-/

open Real

namespace ChowlaCosine

/-- The ordered pairs `(u, v) ∈ B × B` with `u < v`. -/
def ltPairs (B : Finset ℤ) : Finset (ℤ × ℤ) := (B ×ˢ B).filter (fun p => p.1 < p.2)

/-- The set of positive differences `v - u` (`u < v` in `B`), as a `Finset ℕ`. -/
def diffSet (B : Finset ℤ) : Finset ℕ := (ltPairs B).image (fun p => (p.2 - p.1).toNat)

/-- Splitting a sum over `B × B` of a symmetric function into diagonal and twice the
strictly-ordered part. -/
theorem sum_product_symm (B : Finset ℤ) (g : ℤ × ℤ → ℝ) (hg : ∀ u v, g (u, v) = g (v, u)) :
    ∑ p ∈ B ×ˢ B, g p = ∑ b ∈ B, g (b, b) + 2 * ∑ p ∈ ltPairs B, g p := by
  have h1 : ∀ p : ℤ × ℤ, g p = ((if p.1 < p.2 then g p else 0) + (if p.1 = p.2 then g p else 0))
      + (if p.2 < p.1 then g p else 0) := by
    rintro ⟨u, v⟩
    rcases lt_trichotomy u v with h | h | h
    · simp [h, h.ne, not_lt.mpr h.le]
    · simp [h]
    · simp [h, h.ne', not_lt.mpr h.le]
  rw [Finset.sum_congr rfl (fun p _ => h1 p), Finset.sum_add_distrib, Finset.sum_add_distrib,
    ← Finset.sum_filter, ← Finset.sum_filter, ← Finset.sum_filter]
  have hdiag : ∑ p ∈ (B ×ˢ B).filter (fun p => p.1 = p.2), g p = ∑ b ∈ B, g (b, b) := by
    symm
    apply Finset.sum_nbij' (fun b => (b, b)) (fun p => p.1)
    · intro b hb
      simp [hb]
    · intro p hp
      simp only [Finset.mem_filter, Finset.mem_product] at hp
      exact hp.1.1
    · intro b _
      rfl
    · intro p hp
      simp only [Finset.mem_filter, Finset.mem_product] at hp
      exact Prod.ext rfl hp.2
    · intro b _
      rfl
  have hgt : ∑ p ∈ (B ×ˢ B).filter (fun p => p.2 < p.1), g p = ∑ p ∈ ltPairs B, g p := by
    apply Finset.sum_equiv (Equiv.prodComm ℤ ℤ)
    · intro p
      simp only [ltPairs, Finset.mem_filter, Finset.mem_product, Equiv.prodComm_apply,
        Prod.fst_swap, Prod.snd_swap]
      tauto
    · intro p _
      simp only [Equiv.prodComm_apply]
      exact hg p.1 p.2
  rw [hdiag, hgt, ltPairs]
  ring

/-- **Difference-set identity.** For every finite `B ⊆ ℤ` and every real `x`,
`‖∑_{b∈B} exp (b x i)‖² = |B| + 2 ∑_{u<v in B} cos ((v - u) x)`. -/
theorem norm_sq_sum_exp (B : Finset ℤ) (x : ℝ) :
    ‖∑ b ∈ B, Complex.exp ((b : ℂ) * (x : ℂ) * Complex.I)‖ ^ 2 =
      (B.card : ℝ) + 2 * ∑ p ∈ (B ×ˢ B).filter (fun p => p.1 < p.2),
        Real.cos (((p.2 - p.1 : ℤ) : ℝ) * x) := by
  have hpt : ∀ b : ℤ, (b : ℂ) * (x : ℂ) * Complex.I = (((b : ℝ) * x : ℝ) : ℂ) * Complex.I := by
    intro b
    push_cast
    ring
  have hre : (∑ b ∈ B, Complex.exp ((b : ℂ) * (x : ℂ) * Complex.I)).re =
      ∑ b ∈ B, Real.cos ((b : ℝ) * x) := by
    rw [Complex.re_sum]
    refine Finset.sum_congr rfl (fun b _ => ?_)
    rw [hpt, Complex.exp_ofReal_mul_I_re]
  have him : (∑ b ∈ B, Complex.exp ((b : ℂ) * (x : ℂ) * Complex.I)).im =
      ∑ b ∈ B, Real.sin ((b : ℝ) * x) := by
    rw [Complex.im_sum]
    refine Finset.sum_congr rfl (fun b _ => ?_)
    rw [hpt, Complex.exp_ofReal_mul_I_im]
  have key : (∑ b ∈ B, Real.cos ((b : ℝ) * x)) * (∑ b ∈ B, Real.cos ((b : ℝ) * x)) +
      (∑ b ∈ B, Real.sin ((b : ℝ) * x)) * (∑ b ∈ B, Real.sin ((b : ℝ) * x)) =
        ∑ p ∈ B ×ˢ B, Real.cos (((p.2 - p.1 : ℤ) : ℝ) * x) := by
    rw [Finset.sum_product, Finset.sum_mul_sum, Finset.sum_mul_sum, ← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl (fun b _ => ?_)
    rw [← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl (fun c _ => ?_)
    have : ((c - b : ℤ) : ℝ) * x = (c : ℝ) * x - (b : ℝ) * x := by
      push_cast
      ring
    simp only
    rw [this, Real.cos_sub]
    ring
  rw [Complex.sq_norm, Complex.normSq_apply, hre, him, key]
  rw [sum_product_symm B (fun p => Real.cos (((p.2 - p.1 : ℤ) : ℝ) * x))]
  · simp [ltPairs]
  · intro u v
    have : ((u - v : ℤ) : ℝ) * x = -(((v - u : ℤ) : ℝ) * x) := by
      push_cast
      ring
    simp only
    rw [this, Real.cos_neg]

/-- Number of strictly ordered pairs: `2 · #{(u,v) ∈ B×B : u < v} = |B| (|B| - 1)`. -/
theorem two_mul_card_ltPairs (B : Finset ℤ) :
    2 * (ltPairs B).card = B.card * (B.card - 1) := by
  have h := sum_product_symm B (fun _ => (1 : ℝ)) (fun _ _ => rfl)
  simp only [Finset.sum_const, Finset.card_product, nsmul_eq_mul, mul_one] at h
  have h' : B.card * B.card = B.card + 2 * (ltPairs B).card := by exact_mod_cast h
  rw [Nat.mul_sub_one]
  omega

/-- Under the Sidon-type hypothesis (the difference map is injective on `ltPairs B`),
the difference map `(u,v) ↦ (v - u).toNat` is injective on `ltPairs B`. -/
theorem injOn_toNat_of_sidon (B : Finset ℤ)
    (hB : Set.InjOn (fun p : ℤ × ℤ => p.2 - p.1) ↑(ltPairs B)) :
    Set.InjOn (fun p : ℤ × ℤ => (p.2 - p.1).toNat) ↑(ltPairs B) := by
  intro p hp q hq hpq
  have hp' := hp
  have hq' := hq
  rw [Finset.mem_coe] at hp' hq'
  simp only [ltPairs, Finset.mem_filter] at hp' hq'
  apply hB hp hq
  simp only at hpq ⊢
  have h1 : (0 : ℤ) ≤ p.2 - p.1 := by linarith [hp'.2]
  have h2 : (0 : ℤ) ≤ q.2 - q.1 := by linarith [hq'.2]
  rw [← Int.toNat_of_nonneg h1, ← Int.toNat_of_nonneg h2, hpq]

/-- All elements of `diffSet B` are positive. -/
theorem diffSet_pos (B : Finset ℤ) : ∀ a ∈ diffSet B, 0 < a := by
  intro a ha
  simp only [diffSet, ltPairs, Finset.mem_image, Finset.mem_filter, Finset.mem_product] at ha
  obtain ⟨p, ⟨_, hlt⟩, rfl⟩ := ha
  omega

/-- **Sidon consequence, cardinality.** If the differences are distinct, then
`|A| = |B| (|B| - 1) / 2` (natural-number division; exact since `|B|(|B|-1)` is even). -/
theorem card_diffSet_of_sidon (B : Finset ℤ)
    (hB : Set.InjOn (fun p : ℤ × ℤ => p.2 - p.1) ↑(ltPairs B)) :
    (diffSet B).card = B.card * (B.card - 1) / 2 := by
  rw [diffSet, Finset.card_image_of_injOn (injOn_toNat_of_sidon B hB), ← two_mul_card_ltPairs B]
  omega

/-- On `ltPairs B`, the cast of `(v - u).toNat` to `ℝ` equals the cast of `v - u`. -/
theorem cast_toNat_of_lt {p : ℤ × ℤ} (h : p.1 < p.2) :
    (((p.2 - p.1).toNat : ℕ) : ℝ) = ((p.2 - p.1 : ℤ) : ℝ) := by
  have h1 : (0 : ℤ) ≤ p.2 - p.1 := by linarith
  rw [← Int.cast_natCast, Int.toNat_of_nonneg h1]

/-- `f_A(x)` for `A = diffSet B` under the Sidon-type hypothesis, rewritten as the pair sum. -/
theorem cosSum_diffSet_of_sidon (B : Finset ℤ)
    (hB : Set.InjOn (fun p : ℤ × ℤ => p.2 - p.1) ↑(ltPairs B)) (x : ℝ) :
    cosSum (diffSet B) x = ∑ p ∈ ltPairs B, Real.cos (((p.2 - p.1 : ℤ) : ℝ) * x) := by
  rw [cosSum, diffSet, Finset.sum_image (injOn_toNat_of_sidon B hB)]
  refine Finset.sum_congr rfl (fun p hp => ?_)
  simp only [ltPairs, Finset.mem_filter] at hp
  rw [cast_toNat_of_lt hp.2]

/-- **Sidon consequence, lower bound.** If `B ⊆ ℤ` is finite and the map
`{(u,v) ∈ B × B : u < v} → ℤ, (u,v) ↦ v - u` is injective, then with
`A = {(v - u).toNat : u < v in B}` (a set of positive naturals),
`f_A(x) ≥ -|B|/2` for **every** real `x`. -/
theorem cosSum_diffSet_ge_of_sidon (B : Finset ℤ)
    (hB : Set.InjOn (fun p : ℤ × ℤ => p.2 - p.1) ↑((B ×ˢ B).filter (fun p => p.1 < p.2)))
    (x : ℝ) :
    -((B.card : ℝ) / 2) ≤
      cosSum (((B ×ˢ B).filter (fun p => p.1 < p.2)).image (fun p => (p.2 - p.1).toNat)) x := by
  have h := cosSum_diffSet_of_sidon B hB x
  rw [diffSet, ltPairs] at h
  rw [h]
  have hid := norm_sq_sum_exp B x
  have hnn : 0 ≤ ‖∑ b ∈ B, Complex.exp ((b : ℂ) * (x : ℂ) * Complex.I)‖ ^ 2 := sq_nonneg _
  linarith

end ChowlaCosine

namespace ChowlaCosine

/-- **Sidon consequence, combined statement** (fully unfolded). If the difference map
`(u,v) ↦ v - u` is injective on `{(u,v) ∈ B × B : u < v}`, then
`A := {(v - u).toNat : u < v in B}` consists of positive naturals, has
`|A| = |B| (|B| - 1) / 2`, and satisfies `f_A(x) ≥ -|B|/2` for every real `x`. -/
theorem sidon_diffSet_main (B : Finset ℤ)
    (hB : Set.InjOn (fun p : ℤ × ℤ => p.2 - p.1) ↑((B ×ˢ B).filter (fun p => p.1 < p.2))) :
    (∀ a ∈ ((B ×ˢ B).filter (fun p => p.1 < p.2)).image (fun p => (p.2 - p.1).toNat), 0 < a) ∧
    (((B ×ˢ B).filter (fun p => p.1 < p.2)).image (fun p => (p.2 - p.1).toNat)).card =
      B.card * (B.card - 1) / 2 ∧
    ∀ x : ℝ, -((B.card : ℝ) / 2) ≤
      cosSum (((B ×ˢ B).filter (fun p => p.1 < p.2)).image (fun p => (p.2 - p.1).toNat)) x :=
  ⟨diffSet_pos B, card_diffSet_of_sidon B hB, cosSum_diffSet_ge_of_sidon B hB⟩

end ChowlaCosine
