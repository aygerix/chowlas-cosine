import ChowlaCosine.DiffSet
import ChowlaCosine.Star

/-!
# P16: the half-integer square structure of Bu et al.'s sets

Let `S ⊆ ℤ` be finite, `b_s = 3 s + 1/2`, and

* `A(S) = {3 (t - s) : s < t in S} ∪ {|3 (s + t) + 1| : s < t in S}` (as a `Finset ℕ`),
* `P(x) = ∑_{s ∈ S} cos (b_s x)`,
* `C(x) = ∑_{s ∈ S} cos ((6 s + 1) x)`.

## M1 (identity)
`2 cos (b_s x) cos (b_t x) = cos (3 (t - s) x) + cos ((3 (s + t) + 1) x)`,
`cos² (b_s x) = (1 + cos ((6 s + 1) x)) / 2`, hence when the two pair-to-frequency maps are
injective, `f_{A(S)}(x) = P(x)² - |S|/2 - C(x)/2` for every real `x`. The Sidon property
implies both injectivity hypotheses, so `|A(S)| = |S| (|S| - 1)`.

## M2 (fourth moment)
For a Sidon set `S` with `|S| = k`: `(1/2π) ∫_0^{2π} C⁴ = 3k²/4 - 3k/8`.

## M3 (triangle kernel / visit lemma)
`∫_{c-h}^{c+h} cos (b x) φ_{c,h}(x) dx = cos (b c) sinc² (b h / 2)`, and if
`|∑_s cos (b_s x)| ≥ δ` on `[c - h, c + h]` then `δ ≤ ∑_s sinc² (b_s h / 2)`.

## M4 (Chebyshev + counting)
The P16 contradiction argument: under the explicit numerical condition
`2 r n > 24 π / (η⁴ k²)` there is a real `x` with `f_{A(S)}(x) < -(1/2 - η) k`.
-/

open Real

namespace ChowlaCosine

/-! ### M1: definitions and the identity -/

/-- Sidon property of a finite set of integers: every additive quadruple is trivial
(repeated elements allowed). -/
def IsSidon (S : Finset ℤ) : Prop :=
  ∀ a ∈ S, ∀ b ∈ S, ∀ c ∈ S, ∀ d ∈ S, a + b = c + d → (a = c ∧ b = d) ∨ (a = d ∧ b = c)

/-- Bu et al.'s set `A(S) = {3 (t - s)} ∪ {|3 (s + t) + 1|}` over pairs `s < t` in `S`. -/
def buSet (S : Finset ℤ) : Finset ℕ :=
  (ltPairs S).image (fun p => (3 * (p.2 - p.1)).toNat) ∪
    (ltPairs S).image (fun p => (3 * (p.1 + p.2) + 1).natAbs)

/-- `P(x) = ∑_{s ∈ S} cos ((3 s + 1/2) x)`. -/
noncomputable def halfP (S : Finset ℤ) (x : ℝ) : ℝ :=
  ∑ s ∈ S, Real.cos ((3 * (s : ℝ) + 1 / 2) * x)

/-- `C(x) = ∑_{s ∈ S} cos ((6 s + 1) x)`. -/
noncomputable def halfC (S : Finset ℤ) (x : ℝ) : ℝ :=
  ∑ s ∈ S, Real.cos (((6 * s + 1 : ℤ) : ℝ) * x)

theorem continuous_halfP (S : Finset ℤ) : Continuous (halfP S) := by
  unfold halfP
  fun_prop

theorem continuous_halfC (S : Finset ℤ) : Continuous (halfC S) := by
  unfold halfC
  fun_prop

/-- `2 cos (b_s x) cos (b_t x) = cos (3 (t - s) x) + cos ((3 (s + t) + 1) x)`. -/
theorem two_cos_half_mul (s t : ℤ) (x : ℝ) :
    2 * (Real.cos ((3 * (s : ℝ) + 1 / 2) * x) * Real.cos ((3 * (t : ℝ) + 1 / 2) * x)) =
      Real.cos (((3 * (t - s) : ℤ) : ℝ) * x) + Real.cos (((3 * (s + t) + 1 : ℤ) : ℝ) * x) := by
  have e1 : ((3 * (t - s) : ℤ) : ℝ) * x =
      (3 * (t : ℝ) + 1 / 2) * x - (3 * (s : ℝ) + 1 / 2) * x := by push_cast; ring
  have e2 : ((3 * (s + t) + 1 : ℤ) : ℝ) * x =
      (3 * (t : ℝ) + 1 / 2) * x + (3 * (s : ℝ) + 1 / 2) * x := by push_cast; ring
  rw [e1, e2, Real.cos_sub, Real.cos_add]
  ring

/-- `cos² (b_s x) = 1/2 + cos ((6 s + 1) x) / 2`. -/
theorem cos_half_sq (s : ℤ) (x : ℝ) :
    Real.cos ((3 * (s : ℝ) + 1 / 2) * x) ^ 2 =
      1 / 2 + Real.cos (((6 * s + 1 : ℤ) : ℝ) * x) / 2 := by
  have e : ((6 * s + 1 : ℤ) : ℝ) * x = 2 * ((3 * (s : ℝ) + 1 / 2) * x) := by push_cast; ring
  rw [e, Real.cos_two_mul]
  ring

/-- **M1, pair form.** `2 ∑_{s<t} cos (b_s x) cos (b_t x) = ∑_{s<t} (cos (3(t-s)x) + cos ((3(s+t)+1)x))`. -/
theorem two_sum_pairs_half (S : Finset ℤ) (x : ℝ) :
    2 * ∑ p ∈ ltPairs S, Real.cos ((3 * (p.1 : ℝ) + 1 / 2) * x) *
        Real.cos ((3 * (p.2 : ℝ) + 1 / 2) * x) =
      ∑ p ∈ ltPairs S, (Real.cos (((3 * (p.2 - p.1) : ℤ) : ℝ) * x) +
        Real.cos (((3 * (p.1 + p.2) + 1 : ℤ) : ℝ) * x)) := by
  rw [Finset.mul_sum]
  exact Finset.sum_congr rfl (fun p _ => two_cos_half_mul p.1 p.2 x)

/-- **M1, square form.** `P(x)² - ∑_s cos² (b_s x) = ∑_{s<t} (cos (3(t-s)x) + cos ((3(s+t)+1)x))`. -/
theorem halfP_sq_sub_sum_sq (S : Finset ℤ) (x : ℝ) :
    halfP S x ^ 2 - ∑ s ∈ S, Real.cos ((3 * (s : ℝ) + 1 / 2) * x) ^ 2 =
      ∑ p ∈ ltPairs S, (Real.cos (((3 * (p.2 - p.1) : ℤ) : ℝ) * x) +
        Real.cos (((3 * (p.1 + p.2) + 1 : ℤ) : ℝ) * x)) := by
  rw [← two_sum_pairs_half]
  have h := sum_product_symm S (fun p => Real.cos ((3 * (p.1 : ℝ) + 1 / 2) * x) *
      Real.cos ((3 * (p.2 : ℝ) + 1 / 2) * x)) (fun u v => by simp only; ring)
  simp only at h
  have hsq : halfP S x ^ 2 = ∑ p ∈ S ×ˢ S, Real.cos ((3 * (p.1 : ℝ) + 1 / 2) * x) *
      Real.cos ((3 * (p.2 : ℝ) + 1 / 2) * x) := by
    rw [halfP, sq, Finset.sum_mul_sum, Finset.sum_product]
  rw [hsq, h]
  have : ∀ b ∈ S, Real.cos ((3 * (b : ℝ) + 1 / 2) * x) * Real.cos ((3 * (b : ℝ) + 1 / 2) * x) =
      Real.cos ((3 * (b : ℝ) + 1 / 2) * x) ^ 2 := fun b _ => (sq _).symm
  rw [Finset.sum_congr rfl this]
  ring

/-- **M1, diagonal.** `∑_s cos² (b_s x) = |S|/2 + C(x)/2`. -/
theorem sum_cos_half_sq (S : Finset ℤ) (x : ℝ) :
    ∑ s ∈ S, Real.cos ((3 * (s : ℝ) + 1 / 2) * x) ^ 2 = (S.card : ℝ) / 2 + halfC S x / 2 := by
  simp_rw [cos_half_sq]
  rw [Finset.sum_add_distrib, halfC, Finset.sum_div, Finset.sum_const, nsmul_eq_mul]
  ring

/-- `cos (|m| x) = cos (m x)` for an integer `m`. -/
theorem cos_natAbs_mul (m : ℤ) (x : ℝ) :
    Real.cos (((m.natAbs : ℕ) : ℝ) * x) = Real.cos ((m : ℝ) * x) := by
  rw [Nat.cast_natAbs, Int.cast_abs]
  rcases abs_choice (m : ℝ) with h | h
  · rw [h]
  · rw [h, neg_mul, Real.cos_neg]

/-- The two families in `buSet` are disjoint (residues `0` and `±1` mod `3`). -/
theorem disjoint_buSet_parts (S : Finset ℤ) :
    Disjoint ((ltPairs S).image (fun p => (3 * (p.2 - p.1)).toNat))
      ((ltPairs S).image (fun p => (3 * (p.1 + p.2) + 1).natAbs)) := by
  rw [Finset.disjoint_left]
  intro a ha hb
  simp only [Finset.mem_image] at ha hb
  obtain ⟨p, _, rfl⟩ := ha
  obtain ⟨q, _, hq⟩ := hb
  omega

/-- **M1, main identity.** If the two pair-to-frequency maps are injective on the pairs
`s < t` of `S`, then for every real `x`, `f_{A(S)}(x) = P(x)² - |S|/2 - C(x)/2`. -/
theorem cosSum_buSet (S : Finset ℤ)
    (h1 : Set.InjOn (fun p : ℤ × ℤ => (3 * (p.2 - p.1)).toNat) ↑(ltPairs S))
    (h2 : Set.InjOn (fun p : ℤ × ℤ => (3 * (p.1 + p.2) + 1).natAbs) ↑(ltPairs S)) (x : ℝ) :
    cosSum (buSet S) x = halfP S x ^ 2 - (S.card : ℝ) / 2 - halfC S x / 2 := by
  have hid := halfP_sq_sub_sum_sq S x
  rw [sum_cos_half_sq] at hid
  have hA : cosSum (buSet S) x = ∑ p ∈ ltPairs S, (Real.cos (((3 * (p.2 - p.1) : ℤ) : ℝ) * x) +
      Real.cos (((3 * (p.1 + p.2) + 1 : ℤ) : ℝ) * x)) := by
    rw [cosSum, buSet, Finset.sum_union (disjoint_buSet_parts S), Finset.sum_image h1,
      Finset.sum_image h2, ← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl (fun p hp => ?_)
    simp only [ltPairs, Finset.mem_filter] at hp
    have hpos : (0 : ℤ) ≤ 3 * (p.2 - p.1) := by linarith [hp.2]
    rw [cos_natAbs_mul]
    congr 2
    rw [← Int.cast_natCast, Int.toNat_of_nonneg hpos]
  rw [hA]
  linarith

/-- Under the Sidon property the difference map `(s,t) ↦ 3 (t - s)` is injective on pairs. -/
theorem injOn_buSet_diff (S : Finset ℤ) (hS : IsSidon S) :
    Set.InjOn (fun p : ℤ × ℤ => (3 * (p.2 - p.1)).toNat) ↑(ltPairs S) := by
  intro p hp q hq hpq
  rw [Finset.mem_coe] at hp hq
  simp only [ltPairs, Finset.mem_filter, Finset.mem_product] at hp hq
  simp only at hpq
  have h : p.2 + q.1 = q.2 + p.1 := by omega
  rcases hS p.2 hp.1.2 q.1 hq.1.1 q.2 hq.1.2 p.1 hp.1.1 h with h' | h'
  · exact Prod.ext h'.2.symm h'.1
  · exact absurd h'.1 (ne_of_gt hp.2)

/-- Under the Sidon property the sum map `(s,t) ↦ |3 (s + t) + 1|` is injective on pairs. -/
theorem injOn_buSet_sum (S : Finset ℤ) (hS : IsSidon S) :
    Set.InjOn (fun p : ℤ × ℤ => (3 * (p.1 + p.2) + 1).natAbs) ↑(ltPairs S) := by
  intro p hp q hq hpq
  rw [Finset.mem_coe] at hp hq
  simp only [ltPairs, Finset.mem_filter, Finset.mem_product] at hp hq
  simp only at hpq
  have h : p.1 + p.2 = q.1 + q.2 := by omega
  rcases hS p.1 hp.1.1 p.2 hp.1.2 q.1 hq.1.1 q.2 hq.1.2 h with h' | h'
  · exact Prod.ext h'.1 h'.2
  · exfalso
    have := hp.2
    have := hq.2
    omega

/-- Every element of `A(S)` is a positive natural number. -/
theorem buSet_pos (S : Finset ℤ) : ∀ a ∈ buSet S, 0 < a := by
  intro a ha
  simp only [buSet, Finset.mem_union, Finset.mem_image, ltPairs, Finset.mem_filter,
    Finset.mem_product] at ha
  rcases ha with ⟨p, ⟨_, hlt⟩, rfl⟩ | ⟨p, _, rfl⟩ <;> omega

/-- For a Sidon set, `|A(S)| = |S| (|S| - 1)`. -/
theorem card_buSet (S : Finset ℤ) (hS : IsSidon S) :
    (buSet S).card = S.card * (S.card - 1) := by
  rw [buSet, Finset.card_union_of_disjoint (disjoint_buSet_parts S),
    Finset.card_image_of_injOn (injOn_buSet_diff S hS),
    Finset.card_image_of_injOn (injOn_buSet_sum S hS), ← two_mul_card_ltPairs]
  ring

/-- **M1 for Sidon sets.** For a Sidon set `S` and every real `x`,
`f_{A(S)}(x) = P(x)² - |S|/2 - C(x)/2`. -/
theorem cosSum_buSet_of_sidon (S : Finset ℤ) (hS : IsSidon S) (x : ℝ) :
    cosSum (buSet S) x = halfP S x ^ 2 - (S.card : ℝ) / 2 - halfC S x / 2 :=
  cosSum_buSet S (injOn_buSet_diff S hS) (injOn_buSet_sum S hS) x

/-! ### M2: the fourth moment of `C` for a Sidon set -/

/-- `∫_0^{2π} cos (m y) cos (n y) dy = π [m - n = 0] + π [m + n = 0]` for integers `m, n`. -/
theorem integral_cos_mul_cos_int (m n : ℤ) :
    ∫ y in (0 : ℝ)..2 * π, Real.cos ((m : ℝ) * y) * Real.cos ((n : ℝ) * y) =
      (if m - n = 0 then π else 0) + (if m + n = 0 then π else 0) := by
  have h := integral_cos_mul_cos m n 0 0
  simp only [add_zero, sub_zero, Real.cos_zero, mul_one] at h
  exact h

/-- The correlation `cc m n = ∫_0^{2π} cos (m y) cos (n y) dy`. -/
noncomputable def cc (m n : ℤ) : ℝ := (if m - n = 0 then π else 0) + (if m + n = 0 then π else 0)

theorem cos_mul_cos_int (a b : ℤ) (y : ℝ) :
    Real.cos ((a : ℝ) * y) * Real.cos ((b : ℝ) * y) =
      (Real.cos (((a - b : ℤ) : ℝ) * y) + Real.cos (((a + b : ℤ) : ℝ) * y)) / 2 := by
  have e1 : ((a - b : ℤ) : ℝ) * y = (a : ℝ) * y - (b : ℝ) * y := by push_cast; ring
  have e2 : ((a + b : ℤ) : ℝ) * y = (a : ℝ) * y + (b : ℝ) * y := by push_cast; ring
  rw [e1, e2, Real.cos_sub, Real.cos_add]
  ring

/-- Integral of a product of four cosines with integer frequencies. -/
theorem integral_cos_four (a b c d : ℤ) :
    ∫ y in (0 : ℝ)..2 * π, Real.cos ((a : ℝ) * y) * (Real.cos ((b : ℝ) * y) *
        (Real.cos ((c : ℝ) * y) * Real.cos ((d : ℝ) * y))) =
      (cc (a - b) (c - d) + cc (a - b) (c + d) + cc (a + b) (c - d) + cc (a + b) (c + d)) / 4 := by
  have hpt : ∀ y : ℝ, Real.cos ((a : ℝ) * y) * (Real.cos ((b : ℝ) * y) *
        (Real.cos ((c : ℝ) * y) * Real.cos ((d : ℝ) * y))) =
      (Real.cos (((a - b : ℤ) : ℝ) * y) * Real.cos (((c - d : ℤ) : ℝ) * y) +
        Real.cos (((a - b : ℤ) : ℝ) * y) * Real.cos (((c + d : ℤ) : ℝ) * y) +
        Real.cos (((a + b : ℤ) : ℝ) * y) * Real.cos (((c - d : ℤ) : ℝ) * y) +
        Real.cos (((a + b : ℤ) : ℝ) * y) * Real.cos (((c + d : ℤ) : ℝ) * y)) / 4 := by
    intro y
    rw [← mul_assoc, cos_mul_cos_int a b y, cos_mul_cos_int c d y]
    ring
  simp_rw [hpt]
  rw [intervalIntegral.integral_div, intervalIntegral.integral_add, intervalIntegral.integral_add,
    intervalIntegral.integral_add]
  · simp only [integral_cos_mul_cos_int, cc]
  all_goals
    apply Continuous.intervalIntegrable
    fun_prop

theorem cc_diff_diff (s1 s2 s3 s4 : ℤ) :
    cc (6 * s1 + 1 - (6 * s2 + 1)) (6 * s3 + 1 - (6 * s4 + 1)) =
      (if s1 + s4 = s2 + s3 then π else 0) + (if s1 + s3 = s2 + s4 then π else 0) := by
  unfold cc
  split_ifs <;> first | rfl | (exfalso; omega)

theorem cc_diff_sum (s1 s2 s3 s4 : ℤ) :
    cc (6 * s1 + 1 - (6 * s2 + 1)) (6 * s3 + 1 + (6 * s4 + 1)) = 0 := by
  unfold cc
  split_ifs <;> first | (exfalso; omega) | ring1

theorem cc_sum_diff (s1 s2 s3 s4 : ℤ) :
    cc (6 * s1 + 1 + (6 * s2 + 1)) (6 * s3 + 1 - (6 * s4 + 1)) = 0 := by
  unfold cc
  split_ifs <;> first | (exfalso; omega) | ring1

theorem cc_sum_sum (s1 s2 s3 s4 : ℤ) :
    cc (6 * s1 + 1 + (6 * s2 + 1)) (6 * s3 + 1 + (6 * s4 + 1)) =
      if s1 + s2 = s3 + s4 then π else 0 := by
  unfold cc
  split_ifs <;> first | (exfalso; omega) | ring1

/-- `∫_0^{2π} ∏_{i=1}^4 cos ((6 s_i + 1) y) dy = (π/4) ([s1+s4 = s2+s3] + [s1+s3 = s2+s4] + [s1+s2 = s3+s4])`. -/
theorem integral_cos_four_half (s1 s2 s3 s4 : ℤ) :
    ∫ y in (0 : ℝ)..2 * π, Real.cos (((6 * s1 + 1 : ℤ) : ℝ) * y) *
        (Real.cos (((6 * s2 + 1 : ℤ) : ℝ) * y) *
          (Real.cos (((6 * s3 + 1 : ℤ) : ℝ) * y) * Real.cos (((6 * s4 + 1 : ℤ) : ℝ) * y))) =
      π / 4 * ((if s1 + s4 = s2 + s3 then 1 else 0) + (if s1 + s3 = s2 + s4 then 1 else 0) +
        (if s1 + s2 = s3 + s4 then 1 else 0)) := by
  rw [integral_cos_four, cc_diff_diff, cc_diff_sum, cc_sum_diff, cc_sum_sum]
  split_ifs <;> ring

/-- `(∑ f)⁴` as a fourfold sum. -/
theorem sum_pow_four {ι : Type*} (s : Finset ι) (f : ι → ℝ) :
    (∑ i ∈ s, f i) ^ 4 = ∑ a ∈ s, ∑ b ∈ s, ∑ c ∈ s, ∑ d ∈ s, f a * (f b * (f c * f d)) := by
  have e2 : (∑ i ∈ s, f i) * (∑ i ∈ s, f i) = ∑ c ∈ s, ∑ d ∈ s, f c * f d := by
    rw [Finset.sum_mul_sum]
  have e3 : (∑ i ∈ s, f i) * (∑ c ∈ s, ∑ d ∈ s, f c * f d) =
      ∑ b ∈ s, ∑ c ∈ s, ∑ d ∈ s, f b * (f c * f d) := by
    rw [Finset.sum_mul_sum]
    simp_rw [Finset.mul_sum]
  have e4 : (∑ i ∈ s, f i) * (∑ b ∈ s, ∑ c ∈ s, ∑ d ∈ s, f b * (f c * f d)) =
      ∑ a ∈ s, ∑ b ∈ s, ∑ c ∈ s, ∑ d ∈ s, f a * (f b * (f c * f d)) := by
    rw [Finset.sum_mul_sum]
    simp_rw [Finset.mul_sum]
  rw [show (∑ i ∈ s, f i) ^ 4 = (∑ i ∈ s, f i) * ((∑ i ∈ s, f i) *
      ((∑ i ∈ s, f i) * (∑ i ∈ s, f i))) by ring, e2, e3, e4]

/-- Interchanging `∫_0^{2π}` with a fourfold finite sum of continuous functions. -/
theorem integral_sum_four {ι : Type*} (s : Finset ι) (F : ι → ι → ι → ι → ℝ → ℝ)
    (hF : ∀ a b c d, Continuous (F a b c d)) :
    ∫ x in (0 : ℝ)..2 * π, ∑ a ∈ s, ∑ b ∈ s, ∑ c ∈ s, ∑ d ∈ s, F a b c d x =
      ∑ a ∈ s, ∑ b ∈ s, ∑ c ∈ s, ∑ d ∈ s, ∫ x in (0 : ℝ)..2 * π, F a b c d x := by
  have h1 : ∀ a b c, Continuous (fun x => ∑ d ∈ s, F a b c d x) :=
    fun a b c => continuous_finsetSum _ (fun d _ => hF a b c d)
  have h2 : ∀ a b, Continuous (fun x => ∑ c ∈ s, ∑ d ∈ s, F a b c d x) :=
    fun a b => continuous_finsetSum _ (fun c _ => h1 a b c)
  have h3 : ∀ a, Continuous (fun x => ∑ b ∈ s, ∑ c ∈ s, ∑ d ∈ s, F a b c d x) :=
    fun a => continuous_finsetSum _ (fun b _ => h2 a b)
  rw [intervalIntegral.integral_finsetSum (fun a _ => (h3 a).intervalIntegrable _ _)]
  refine Finset.sum_congr rfl (fun a _ => ?_)
  rw [intervalIntegral.integral_finsetSum (fun b _ => (h2 a b).intervalIntegrable _ _)]
  refine Finset.sum_congr rfl (fun b _ => ?_)
  rw [intervalIntegral.integral_finsetSum (fun c _ => (h1 a b c).intervalIntegrable _ _)]
  refine Finset.sum_congr rfl (fun c _ => ?_)
  rw [intervalIntegral.integral_finsetSum (fun d _ => (hF a b c d).intervalIntegrable _ _)]

/-- **Sidon count.** For a Sidon set `S`, `#{(a,b,c,d) ∈ S⁴ : a + b = c + d} = 2|S|² - |S|`. -/
theorem sidon_quad_count (S : Finset ℤ) (hS : IsSidon S) :
    ∑ a ∈ S, ∑ b ∈ S, ∑ c ∈ S, ∑ d ∈ S, (if a + b = c + d then (1 : ℝ) else 0) =
      2 * (S.card : ℝ) ^ 2 - S.card := by
  have inner : ∀ a ∈ S, ∀ b ∈ S,
      ∑ c ∈ S, ∑ d ∈ S, (if a + b = c + d then (1 : ℝ) else 0) = if a = b then 1 else 2 := by
    intro a ha b hb
    have h1 : ∀ c ∈ S, ∑ d ∈ S, (if a + b = c + d then (1 : ℝ) else 0) =
        if a + b - c ∈ S then 1 else 0 := by
      intro c _
      calc ∑ d ∈ S, (if a + b = c + d then (1 : ℝ) else 0)
          = ∑ d ∈ S, (if d = a + b - c then (1 : ℝ) else 0) :=
            Finset.sum_congr rfl (fun d _ => if_congr ⟨fun h => by omega, fun h => by omega⟩ rfl rfl)
        _ = if a + b - c ∈ S then 1 else 0 := by rw [Finset.sum_ite_eq']
    rw [Finset.sum_congr rfl h1]
    by_cases hab : a = b
    · rw [if_pos hab, ← hab]
      have h2 : ∀ c ∈ S, (if a + a - c ∈ S then (1 : ℝ) else 0) = if c = a then 1 else 0 := by
        intro c hc
        by_cases hca : c = a
        · rw [if_pos hca, hca, show a + a - a = a by ring, if_pos ha]
        · have hn : a + a - c ∉ S := by
            intro hd
            rcases hS a ha a ha c hc (a + a - c) hd (by ring) with h | h
            · exact hca h.1.symm
            · exact hca h.2.symm
          rw [if_neg hn, if_neg hca]
      rw [Finset.sum_congr rfl h2, Finset.sum_ite_eq', if_pos ha]
    · have h2 : ∀ c ∈ S, (if a + b - c ∈ S then (1 : ℝ) else 0) =
          (if c = a then 1 else 0) + (if c = b then 1 else 0) := by
        intro c hc
        by_cases hca : c = a
        · rw [if_pos hca, if_neg (fun h => hab (hca.symm.trans h)), hca,
            show a + b - a = b by ring, if_pos hb]
          norm_num
        · by_cases hcb : c = b
          · rw [if_neg hca, if_pos hcb, hcb, show a + b - b = a by ring, if_pos ha]
            norm_num
          · have hn : a + b - c ∉ S := by
              intro hd
              rcases hS a ha b hb c hc (a + b - c) hd (by ring) with h | h
              · exact hca h.1.symm
              · exact hcb h.2.symm
            rw [if_neg hn, if_neg hca, if_neg hcb]
            norm_num
      rw [Finset.sum_congr rfl h2, Finset.sum_add_distrib, Finset.sum_ite_eq', Finset.sum_ite_eq',
        if_pos ha, if_pos hb, if_neg hab]
      norm_num
  rw [Finset.sum_congr rfl (fun a ha => Finset.sum_congr rfl (fun b hb => inner a ha b hb))]
  have h3 : ∀ a ∈ S, ∑ b ∈ S, (if a = b then (1 : ℝ) else 2) = 2 * S.card - 1 := by
    intro a ha
    have : ∀ b ∈ S, (if a = b then (1 : ℝ) else 2) = 2 - (if a = b then 1 else 0) := by
      intro b _
      split_ifs <;> norm_num
    rw [Finset.sum_congr rfl this, Finset.sum_sub_distrib, Finset.sum_ite_eq, if_pos ha,
      Finset.sum_const, nsmul_eq_mul]
    ring
  rw [Finset.sum_congr rfl h3, Finset.sum_const, nsmul_eq_mul]
  ring

/-- The three additive-quadruple patterns appearing in `∫ C⁴` all have the Sidon count. -/
theorem sidon_three_count (S : Finset ℤ) (hS : IsSidon S) :
    ∑ a ∈ S, ∑ b ∈ S, ∑ c ∈ S, ∑ d ∈ S, ((if a + d = b + c then (1 : ℝ) else 0) +
      (if a + c = b + d then 1 else 0) + (if a + b = c + d then 1 else 0)) =
      3 * (2 * (S.card : ℝ) ^ 2 - S.card) := by
  have T1 : ∑ a ∈ S, ∑ b ∈ S, ∑ c ∈ S, ∑ d ∈ S, (if a + d = b + c then (1 : ℝ) else 0) =
      2 * (S.card : ℝ) ^ 2 - S.card := by
    rw [← sidon_quad_count S hS]
    refine Finset.sum_congr rfl (fun a _ => ?_)
    calc ∑ b ∈ S, ∑ c ∈ S, ∑ d ∈ S, (if a + d = b + c then (1 : ℝ) else 0)
        = ∑ b ∈ S, ∑ d ∈ S, ∑ c ∈ S, (if a + d = b + c then (1 : ℝ) else 0) :=
          Finset.sum_congr rfl (fun b _ => Finset.sum_comm)
      _ = ∑ d ∈ S, ∑ b ∈ S, ∑ c ∈ S, (if a + d = b + c then (1 : ℝ) else 0) := Finset.sum_comm
  have T2 : ∑ a ∈ S, ∑ b ∈ S, ∑ c ∈ S, ∑ d ∈ S, (if a + c = b + d then (1 : ℝ) else 0) =
      2 * (S.card : ℝ) ^ 2 - S.card := by
    rw [← sidon_quad_count S hS]
    refine Finset.sum_congr rfl (fun a _ => ?_)
    exact Finset.sum_comm
  have T3 := sidon_quad_count S hS
  simp only [Finset.sum_add_distrib]
  rw [T1, T2, T3]
  ring

/-- **M2 (fourth moment, unnormalized).** For a Sidon set `S`,
`∫_0^{2π} C(x)⁴ dx = (π/4) · 3 (2|S|² - |S|)`. -/
theorem integral_halfC_pow_four (S : Finset ℤ) (hS : IsSidon S) :
    ∫ x in (0 : ℝ)..2 * π, halfC S x ^ 4 = π / 4 * (3 * (2 * (S.card : ℝ) ^ 2 - S.card)) := by
  have hexp : ∀ x, halfC S x ^ 4 = ∑ a ∈ S, ∑ b ∈ S, ∑ c ∈ S, ∑ d ∈ S,
      Real.cos (((6 * a + 1 : ℤ) : ℝ) * x) * (Real.cos (((6 * b + 1 : ℤ) : ℝ) * x) *
        (Real.cos (((6 * c + 1 : ℤ) : ℝ) * x) * Real.cos (((6 * d + 1 : ℤ) : ℝ) * x))) := by
    intro x
    rw [halfC, sum_pow_four]
  simp_rw [hexp]
  rw [integral_sum_four]
  · simp only [integral_cos_four_half]
    rw [← sidon_three_count S hS]
    simp only [Finset.mul_sum]
  · intro a b c d
    fun_prop

/-- **M2 (fourth moment).** For a Sidon set `S` with `|S| = k`,
`(1/2π) ∫_0^{2π} C(x)⁴ dx = 3k²/4 - 3k/8`. -/
theorem normalized_halfC_pow_four (S : Finset ℤ) (hS : IsSidon S) :
    (1 / (2 * π)) * ∫ x in (0 : ℝ)..2 * π, halfC S x ^ 4 =
      3 * (S.card : ℝ) ^ 2 / 4 - 3 * (S.card : ℝ) / 8 := by
  rw [integral_halfC_pow_four S hS]
  have := Real.pi_pos.ne'
  field_simp
  ring

/-- **M2 (weak form).** `∫_0^{2π} C⁴ ≤ 2π · 3k²/4`. -/
theorem integral_halfC_pow_four_le (S : Finset ℤ) (hS : IsSidon S) :
    ∫ x in (0 : ℝ)..2 * π, halfC S x ^ 4 ≤ 2 * π * (3 * (S.card : ℝ) ^ 2 / 4) := by
  rw [integral_halfC_pow_four S hS]
  have hk : (0 : ℝ) ≤ S.card := Nat.cast_nonneg _
  nlinarith [Real.pi_pos]

/-! ### M3: the triangle kernel and the visit lemma -/

/-- The triangle kernel `φ_{c,h}(x) = (1/h) · max(0, 1 - |x - c|/h)` (for `h > 0`: nonnegative,
supported on `[c - h, c + h]`, total mass `1`). -/
noncomputable def triK (c h x : ℝ) : ℝ := (1 / h) * max 0 (1 - |x - c| / h)

theorem triK_nonneg {h : ℝ} (hh : 0 < h) (c x : ℝ) : 0 ≤ triK c h x :=
  mul_nonneg (by positivity) (le_max_left _ _)

theorem continuous_triK (c h : ℝ) : Continuous (triK c h) :=
  continuous_const.mul (continuous_const.max
    (continuous_const.sub (((continuous_id.sub continuous_const).abs).div_const _)))

theorem triK_left {c h x : ℝ} (hh : 0 < h) (hx : x ∈ Set.Icc (c - h) c) :
    triK c h x = (x - c + h) / h ^ 2 := by
  obtain ⟨h1, h2⟩ := hx
  unfold triK
  rw [abs_of_nonpos (by linarith : x - c ≤ 0),
    max_eq_right (sub_nonneg.mpr ((div_le_one hh).mpr (by linarith)))]
  field_simp
  ring

theorem triK_right {c h x : ℝ} (hh : 0 < h) (hx : x ∈ Set.Icc c (c + h)) :
    triK c h x = (c + h - x) / h ^ 2 := by
  obtain ⟨h1, h2⟩ := hx
  unfold triK
  rw [abs_of_nonneg (by linarith : 0 ≤ x - c),
    max_eq_right (sub_nonneg.mpr ((div_le_one hh).mpr (by linarith)))]
  field_simp
  ring

/-- **M3, Fourier transform of the triangle kernel.** For every real frequency `b`, centre `c`
and half-width `h > 0`: `∫_{c-h}^{c+h} cos (b x) φ_{c,h}(x) dx = cos (b c) · sinc² (b h / 2)`. -/
theorem integral_cos_mul_triK (b c h : ℝ) (hh : 0 < h) :
    ∫ x in (c - h)..(c + h), Real.cos (b * x) * triK c h x =
      Real.cos (b * c) * Real.sinc (b * h / 2) ^ 2 := by
  have hcont : Continuous (fun x => Real.cos (b * x) * triK c h x) :=
    (by fun_prop : Continuous fun x => Real.cos (b * x)).mul (continuous_triK c h)
  rw [← intervalIntegral.integral_add_adjacent_intervals (b := c) (hcont.intervalIntegrable _ _)
    (hcont.intervalIntegrable _ _)]
  have hL : ∫ x in (c - h)..c, Real.cos (b * x) * triK c h x =
      ∫ x in (c - h)..c, Real.cos (b * x) * ((x - c + h) / h ^ 2) := by
    apply intervalIntegral.integral_congr
    intro x hx
    rw [Set.uIcc_of_le (by linarith)] at hx
    simp only [triK_left hh hx]
  have hR : ∫ x in c..(c + h), Real.cos (b * x) * triK c h x =
      ∫ x in c..(c + h), Real.cos (b * x) * ((c + h - x) / h ^ 2) := by
    apply intervalIntegral.integral_congr
    intro x hx
    rw [Set.uIcc_of_le (by linarith)] at hx
    simp only [triK_right hh hx]
  rw [hL, hR]
  have hh0 : h ≠ 0 := hh.ne'
  have hlin : ∀ x : ℝ, HasDerivAt (fun y => y - c + h) 1 x :=
    fun x => ((hasDerivAt_id' x).sub_const c).add_const h
  have hlin2 : ∀ x : ℝ, HasDerivAt (fun y => c + h - y) (-1) x :=
    fun x => (hasDerivAt_id' x).const_sub (c + h)
  by_cases hb : b = 0
  · subst hb
    simp only [zero_mul, Real.cos_zero, one_mul, zero_div, Real.sinc_zero, one_pow, mul_one]
    rw [intervalIntegral.integral_eq_sub_of_hasDerivAt
        (f := fun y => (y - c + h) * (y - c + h) / (2 * h ^ 2))
        (fun x _ => by
          have := ((hlin x).mul (hlin x)).div_const (2 * h ^ 2)
          exact this.congr_deriv (by field_simp; ring))
        ((by fun_prop : Continuous fun x : ℝ => (x - c + h) / h ^ 2).intervalIntegrable _ _),
      intervalIntegral.integral_eq_sub_of_hasDerivAt
        (f := fun y => -((c + h - y) * (c + h - y)) / (2 * h ^ 2))
        (fun x _ => by
          have := (((hlin2 x).mul (hlin2 x)).neg).div_const (2 * h ^ 2)
          exact this.congr_deriv (by field_simp; ring))
        ((by fun_prop : Continuous fun x : ℝ => (c + h - x) / h ^ 2).intervalIntegrable _ _)]
    field_simp
    ring
  · have hsin : ∀ x : ℝ, HasDerivAt (fun y => Real.sin (b * y)) (Real.cos (b * x) * (b * 1)) x :=
      fun x => ((hasDerivAt_id' x).const_mul b).sin
    have hcos : ∀ x : ℝ, HasDerivAt (fun y => Real.cos (b * y)) (-Real.sin (b * x) * (b * 1)) x :=
      fun x => ((hasDerivAt_id' x).const_mul b).cos
    rw [intervalIntegral.integral_eq_sub_of_hasDerivAt
        (f := fun y => ((y - c + h) * Real.sin (b * y) / b + Real.cos (b * y) / b ^ 2) / h ^ 2)
        (fun x _ => by
          have := ((((hlin x).mul (hsin x)).div_const b).add ((hcos x).div_const (b ^ 2))).div_const
            (h ^ 2)
          exact this.congr_deriv (by field_simp; ring))
        ((by fun_prop : Continuous fun x : ℝ =>
          Real.cos (b * x) * ((x - c + h) / h ^ 2)).intervalIntegrable _ _),
      intervalIntegral.integral_eq_sub_of_hasDerivAt
        (f := fun y => ((c + h - y) * Real.sin (b * y) / b - Real.cos (b * y) / b ^ 2) / h ^ 2)
        (fun x _ => by
          have := ((((hlin2 x).mul (hsin x)).div_const b).sub ((hcos x).div_const (b ^ 2))).div_const
            (h ^ 2)
          exact this.congr_deriv (by field_simp; ring))
        ((by fun_prop : Continuous fun x : ℝ =>
          Real.cos (b * x) * ((c + h - x) / h ^ 2)).intervalIntegrable _ _)]
    have hbh : b * h / 2 ≠ 0 := div_ne_zero (mul_ne_zero hb hh0) two_ne_zero
    rw [Real.sinc_of_ne_zero hbh]
    have e1 : Real.cos (b * (c - h)) =
        Real.cos (b * c) * Real.cos (b * h) + Real.sin (b * c) * Real.sin (b * h) := by
      rw [show b * (c - h) = b * c - b * h by ring, Real.cos_sub]
    have e2 : Real.cos (b * (c + h)) =
        Real.cos (b * c) * Real.cos (b * h) - Real.sin (b * c) * Real.sin (b * h) := by
      rw [show b * (c + h) = b * c + b * h by ring, Real.cos_add]
    have e3 : Real.cos (b * h) = 1 - 2 * Real.sin (b * h / 2) ^ 2 := by
      rw [show b * h = 2 * (b * h / 2) by ring, Real.cos_two_mul, Real.cos_sq']
      ring
    rw [e1, e2, e3]
    field_simp
    ring

/-- `∫ φ_{c,h} = 1`. -/
theorem integral_triK (c h : ℝ) (hh : 0 < h) : ∫ x in (c - h)..(c + h), triK c h x = 1 := by
  have := integral_cos_mul_triK 0 c h hh
  simp only [zero_mul, Real.cos_zero, one_mul, zero_div, Real.sinc_zero, one_pow, mul_one] at this
  exact this

/-- Linearity: `∫ (∑_s cos (b_s x)) φ_{c,h}(x) dx = ∑_s cos (b_s c) sinc² (b_s h / 2)`. -/
theorem integral_sum_cos_mul_triK {ι : Type*} (F : Finset ι) (b : ι → ℝ) (c h : ℝ) (hh : 0 < h) :
    ∫ x in (c - h)..(c + h), (∑ s ∈ F, Real.cos (b s * x)) * triK c h x =
      ∑ s ∈ F, Real.cos (b s * c) * Real.sinc (b s * h / 2) ^ 2 := by
  simp_rw [Finset.sum_mul]
  rw [intervalIntegral.integral_finsetSum (fun s _ =>
    (show Continuous fun x => Real.cos (b s * x) * triK c h x from
      (by fun_prop : Continuous fun x => Real.cos (b s * x)).mul
        (continuous_triK c h)).intervalIntegrable _ _)]
  exact Finset.sum_congr rfl (fun s _ => integral_cos_mul_triK (b s) c h hh)

/-- **M3, visit lemma.** Let `(b_s)_{s ∈ F}` be any finite family of real frequencies, `h > 0`.
If `|∑_s cos (b_s x)| ≥ δ` for every `x ∈ [c - h, c + h]`, then `δ ≤ ∑_s sinc² (b_s h / 2)`. -/
theorem visit_lemma {ι : Type*} (F : Finset ι) (b : ι → ℝ) (c h δ : ℝ) (hh : 0 < h)
    (hP : ∀ x ∈ Set.Icc (c - h) (c + h), δ ≤ |∑ s ∈ F, Real.cos (b s * x)|) :
    δ ≤ ∑ s ∈ F, Real.sinc (b s * h / 2) ^ 2 := by
  have hsum_nonneg : 0 ≤ ∑ s ∈ F, Real.sinc (b s * h / 2) ^ 2 :=
    Finset.sum_nonneg (fun s _ => sq_nonneg _)
  rcases le_or_gt δ 0 with hδ | hδ
  · linarith
  have hPc : Continuous (fun x => ∑ s ∈ F, Real.cos (b s * x)) := by fun_prop
  have hch : c - h ≤ c + h := by linarith
  have hint := integral_sum_cos_mul_triK F b c h hh
  have hone := integral_triK c h hh
  have hcI : Continuous (fun x => (∑ s ∈ F, Real.cos (b s * x)) * triK c h x) :=
    hPc.mul (continuous_triK c h)
  have hsign : (∀ x ∈ Set.Icc (c - h) (c + h), δ ≤ ∑ s ∈ F, Real.cos (b s * x)) ∨
      (∀ x ∈ Set.Icc (c - h) (c + h), ∑ s ∈ F, Real.cos (b s * x) ≤ -δ) := by
    by_contra hcon
    push Not at hcon
    obtain ⟨⟨x1, hx1, h1⟩, ⟨x2, hx2, h2⟩⟩ := hcon
    have h1' : ∑ s ∈ F, Real.cos (b s * x1) ≤ -δ := by
      rcases le_abs.mp (hP x1 hx1) with h' | h'
      · linarith
      · linarith
    have h2' : δ ≤ ∑ s ∈ F, Real.cos (b s * x2) := by
      rcases le_abs.mp (hP x2 hx2) with h' | h'
      · linarith
      · linarith
    have h0 : (0 : ℝ) ∈ Set.uIcc (∑ s ∈ F, Real.cos (b s * x1)) (∑ s ∈ F, Real.cos (b s * x2)) :=
      Set.mem_uIcc.mpr (Or.inl ⟨by linarith, by linarith⟩)
    obtain ⟨z, hz, hz0⟩ := intermediate_value_uIcc (a := x1) (b := x2) hPc.continuousOn h0
    have hzI : z ∈ Set.Icc (c - h) (c + h) := Set.uIcc_subset_Icc hx1 hx2 hz
    have := hP z hzI
    simp only at hz0
    rw [hz0, abs_zero] at this
    linarith
  rcases hsign with hpos | hneg
  · have hle : ∫ x in (c - h)..(c + h), δ * triK c h x ≤
        ∫ x in (c - h)..(c + h), (∑ s ∈ F, Real.cos (b s * x)) * triK c h x :=
      intervalIntegral.integral_mono_on hch
        ((continuous_const.mul (continuous_triK c h)).intervalIntegrable _ _)
        (hcI.intervalIntegrable _ _)
        (fun x hx => mul_le_mul_of_nonneg_right (hpos x hx) (triK_nonneg hh c x))
    rw [intervalIntegral.integral_const_mul, hone, mul_one, hint] at hle
    calc δ ≤ ∑ s ∈ F, Real.cos (b s * c) * Real.sinc (b s * h / 2) ^ 2 := hle
      _ ≤ ∑ s ∈ F, Real.sinc (b s * h / 2) ^ 2 := Finset.sum_le_sum (fun s _ => by
          have h1 := Real.cos_le_one (b s * c)
          have h2 := sq_nonneg (Real.sinc (b s * h / 2))
          nlinarith)
  · have hle : ∫ x in (c - h)..(c + h), (∑ s ∈ F, Real.cos (b s * x)) * triK c h x ≤
        ∫ x in (c - h)..(c + h), (-δ) * triK c h x :=
      intervalIntegral.integral_mono_on hch (hcI.intervalIntegrable _ _)
        ((continuous_const.mul (continuous_triK c h)).intervalIntegrable _ _)
        (fun x hx => mul_le_mul_of_nonneg_right (hneg x hx) (triK_nonneg hh c x))
    rw [intervalIntegral.integral_const_mul, hone, mul_one, hint] at hle
    have : -(∑ s ∈ F, Real.cos (b s * c) * Real.sinc (b s * h / 2) ^ 2) ≤
        ∑ s ∈ F, Real.sinc (b s * h / 2) ^ 2 := by
      rw [← Finset.sum_neg_distrib]
      exact Finset.sum_le_sum (fun s _ => by
        have h1 := Real.neg_one_le_cos (b s * c)
        have h2 := sq_nonneg (Real.sinc (b s * h / 2))
        nlinarith)
    linarith

/-- **M3, contrapositive form.** If `∑_s sinc² (b_s h / 2) < δ` then every window
`[c - h, c + h]` contains a point `y` with `|∑_s cos (b_s y)| < δ`. -/
theorem exists_visit_of_sinc_sum_lt {ι : Type*} (F : Finset ι) (b : ι → ℝ) (h δ : ℝ) (hh : 0 < h)
    (hsum : ∑ s ∈ F, Real.sinc (b s * h / 2) ^ 2 < δ) (c : ℝ) :
    ∃ y ∈ Set.Icc (c - h) (c + h), |∑ s ∈ F, Real.cos (b s * y)| < δ := by
  by_contra hcon
  push Not at hcon
  exact absurd (visit_lemma F b c h δ hh hcon) (not_le.mpr hsum)

/-! ### M4: Chebyshev on `C⁴` and the counting argument -/

/-- `C` is `2π`-periodic. -/
theorem halfC_periodic (S : Finset ℤ) : Function.Periodic (halfC S) (2 * π) := by
  intro x
  unfold halfC
  refine Finset.sum_congr rfl (fun s _ => ?_)
  rw [mul_add, Real.cos_add_int_mul_two_pi]

/-- Lipschitz bound: if `|s| ≤ L` on `S` then `|C(x) - C(y)| ≤ |S| (6L + 1) |x - y|`. -/
theorem abs_halfC_sub_le (S : Finset ℤ) (L : ℝ) (hL : ∀ s ∈ S, |(s : ℝ)| ≤ L) (x y : ℝ) :
    |halfC S x - halfC S y| ≤ (S.card : ℝ) * (6 * L + 1) * |x - y| := by
  unfold halfC
  rw [← Finset.sum_sub_distrib]
  calc |∑ s ∈ S, (Real.cos (((6 * s + 1 : ℤ) : ℝ) * x) - Real.cos (((6 * s + 1 : ℤ) : ℝ) * y))|
      ≤ ∑ s ∈ S, |Real.cos (((6 * s + 1 : ℤ) : ℝ) * x) - Real.cos (((6 * s + 1 : ℤ) : ℝ) * y)| :=
        Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ s ∈ S, (6 * L + 1) * |x - y| := by
        refine Finset.sum_le_sum (fun s hs => ?_)
        have hm : |((6 * s + 1 : ℤ) : ℝ)| ≤ 6 * L + 1 := by
          have := abs_le.mp (hL s hs)
          push_cast
          exact abs_le.mpr ⟨by linarith, by linarith⟩
        calc |Real.cos (((6 * s + 1 : ℤ) : ℝ) * x) - Real.cos (((6 * s + 1 : ℤ) : ℝ) * y)|
            ≤ |((6 * s + 1 : ℤ) : ℝ) * x - ((6 * s + 1 : ℤ) : ℝ) * y| := Real.abs_cos_sub_cos_le _ _
          _ = |((6 * s + 1 : ℤ) : ℝ)| * |x - y| := by rw [← mul_sub, abs_mul]
          _ ≤ (6 * L + 1) * |x - y| := mul_le_mul_of_nonneg_right hm (abs_nonneg _)
    _ = (S.card : ℝ) * (6 * L + 1) * |x - y| := by
        rw [Finset.sum_const, nsmul_eq_mul]
        ring

/-- **M4 (P16 main theorem, visit form).** Let `S` be a Sidon set with `|s| ≤ L` for `s ∈ S`,
`k = |S|`, `η > 0`, `δ = √(η k / 2)`, `r = η / (2 (6L + 1))`, `h > 0`, and
`n = ⌊2π / (2h + 2r)⌋`. Assume the *visit property*: every window `[c - h, c + h]` contains a
point `y` with `|P(y)| < δ`. If `2 r n > 24 π / (η⁴ k²)`, then there is a real `x` with
`f_{A(S)}(x) < -(1/2 - η) k`, i.e. `M(A(S)) > (1/2 - η) k`. -/
theorem halfSquare_lower_bound_of_visit (S : Finset ℤ) (hS : IsSidon S) (L : ℝ)
    (hL : ∀ s ∈ S, |(s : ℝ)| ≤ L) (η : ℝ) (hη : 0 < η) (h : ℝ) (hh : 0 < h)
    (hvisit : ∀ c : ℝ, ∃ y ∈ Set.Icc (c - h) (c + h),
      |halfP S y| < Real.sqrt (η * S.card / 2))
    (hcond : 24 * π / (η ^ 4 * (S.card : ℝ) ^ 2) <
      2 * (η / (2 * (6 * L + 1))) *
        (⌊2 * π / (2 * h + 2 * (η / (2 * (6 * L + 1))))⌋₊ : ℝ)) :
    ∃ x : ℝ, cosSum (buSet S) x < -((1 / 2 - η) * S.card) := by
  by_contra hcon
  push Not at hcon
  set r : ℝ := η / (2 * (6 * L + 1)) with hr
  set n : ℕ := ⌊2 * π / (2 * h + 2 * r)⌋₊ with hn
  set δ : ℝ := Real.sqrt (η * S.card / 2) with hδ
  -- positivity facts
  obtain ⟨y0, -, hy0⟩ := hvisit 0
  have hδpos : 0 < δ := lt_of_le_of_lt (abs_nonneg _) hy0
  have hkpos : (0 : ℝ) < S.card := by
    by_contra hk0
    push Not at hk0
    have h1 : η * S.card / 2 ≤ 0 := by nlinarith
    have h2 : δ = 0 := Real.sqrt_eq_zero'.mpr h1
    linarith
  have hSne : S.Nonempty := by
    rw [← Finset.card_pos]
    exact_mod_cast hkpos
  have hL0 : 0 ≤ L := by
    obtain ⟨s, hs⟩ := hSne
    exact le_trans (abs_nonneg _) (hL s hs)
  have hrpos : 0 < r := by positivity
  have hδsq : δ ^ 2 = η * S.card / 2 := Real.sq_sqrt (by positivity)
  have hwpos : 0 < 2 * h + 2 * r := by positivity
  -- Step 3: near every visit, `C ≤ -ηk/2` on a neighbourhood of radius `r`.
  have step3 : ∀ y, |halfP S y| < δ → ∀ x ∈ Set.Ioo (y - r) (y + r),
      halfC S x ≤ -(η * S.card / 2) := by
    intro y hy x hx
    have hP2 : halfP S y ^ 2 < η * S.card / 2 := by
      rw [← hδsq, ← sq_abs]
      exact pow_lt_pow_left₀ hy (abs_nonneg _) two_ne_zero
    have hid := cosSum_buSet_of_sidon S hS y
    have hfy := hcon y
    have hCy : halfC S y < -(η * S.card) := by linarith
    have hlip := (abs_le.mp (abs_halfC_sub_le S L hL x y)).2
    have hxy : |x - y| < r := by
      rw [abs_lt]
      constructor <;> linarith [hx.1, hx.2]
    have hk6 : 0 ≤ (S.card : ℝ) * (6 * L + 1) := by positivity
    have h1 : (S.card : ℝ) * (6 * L + 1) * |x - y| ≤ (S.card : ℝ) * (6 * L + 1) * r :=
      mul_le_mul_of_nonneg_left hxy.le hk6
    have hkr : (S.card : ℝ) * (6 * L + 1) * r = η * S.card / 2 := by
      rw [hr]
      field_simp
    linarith
  -- Step 4: disjoint neighbourhoods of visits in consecutive windows.
  choose y hyI hyP using hvisit
  obtain ⟨U, hU⟩ : ∃ U : ℕ → Set ℝ,
      U = fun j : ℕ => Set.Ioo (y ((j : ℝ) * (2 * h + 2 * r)) - r) (y ((j : ℝ) * (2 * h + 2 * r)) + r) :=
    ⟨_, rfl⟩
  have key : ∀ i j : ℕ, i < j →
      y ((i : ℝ) * (2 * h + 2 * r)) + r ≤ y ((j : ℝ) * (2 * h + 2 * r)) - r := by
    intro i j hij
    have hi := (hyI ((i : ℝ) * (2 * h + 2 * r))).2
    have hj := (hyI ((j : ℝ) * (2 * h + 2 * r))).1
    have hij' : (i : ℝ) + 1 ≤ j := by exact_mod_cast hij
    have := mul_le_mul_of_nonneg_right hij' hwpos.le
    nlinarith
  have hdisj : (↑(Finset.range n) : Set ℕ).PairwiseDisjoint U := by
    intro i _ j _ hij
    rw [Function.onFun, hU]
    rcases lt_or_gt_of_ne hij with hlt | hlt
    · exact Set.disjoint_left.mpr (fun x hx1 hx2 => by
        have := key i j hlt
        simp only [Set.mem_Ioo] at hx1 hx2
        linarith [hx1.2, hx2.1])
    · exact Set.disjoint_left.mpr (fun x hx1 hx2 => by
        have := key j i hlt
        simp only [Set.mem_Ioo] at hx1 hx2
        linarith [hx1.1, hx2.2])
  have hvolU : MeasureTheory.volume.real (⋃ j ∈ Finset.range n, U j) = n * (2 * r) := by
    rw [MeasureTheory.measureReal_biUnion_finset hdisj (fun j _ => by rw [hU]; exact measurableSet_Ioo)
      (fun j _ => by rw [hU]; simp only [Real.volume_Ioo]; exact ENNReal.ofReal_ne_top)]
    have : ∀ j ∈ Finset.range n, MeasureTheory.volume.real (U j) = 2 * r := by
      intro j _
      rw [hU]
      simp only
      rw [Real.volume_real_Ioo_of_le (by linarith)]
      ring
    rw [Finset.sum_congr rfl this, Finset.sum_const, Finset.card_range, nsmul_eq_mul]
  -- the window of length `2π`
  set a : ℝ := -h - r with ha
  have hπ := Real.pi_pos
  have hnle : (n : ℝ) * (2 * h + 2 * r) ≤ 2 * π := by
    have := Nat.floor_le (by positivity : (0 : ℝ) ≤ 2 * π / (2 * h + 2 * r))
    rw [← hn] at this
    exact (le_div_iff₀ hwpos).mp this
  set τ : ℝ := η * S.card / 2 with hτ
  have hτpos : 0 < τ := by positivity
  have hsub : (⋃ j ∈ Finset.range n, U j) ⊆
      {x | τ ^ 4 ≤ halfC S x ^ 4} ∩ Set.Ioc a (a + 2 * π) := by
    intro x hx
    simp only [Set.mem_iUnion] at hx
    obtain ⟨j, hj, hxU⟩ := hx
    rw [hU] at hxU
    simp only at hxU
    have hC := step3 _ (hyP _) x hxU
    have hjn : (j : ℝ) + 1 ≤ n := by
      have := Finset.mem_range.mp hj
      exact_mod_cast this
    have hyj := hyI ((j : ℝ) * (2 * h + 2 * r))
    have hj0 : (0 : ℝ) ≤ j := Nat.cast_nonneg j
    have h1 := mul_le_mul_of_nonneg_right hjn hwpos.le
    have h2 : 0 ≤ (j : ℝ) * (2 * h + 2 * r) := mul_nonneg hj0 hwpos.le
    refine ⟨?_, ?_, ?_⟩
    · show τ ^ 4 ≤ halfC S x ^ 4
      have h3 : τ ≤ -halfC S x := by linarith
      have h4 := pow_le_pow_left₀ hτpos.le h3 4
      have h5 : (-halfC S x) ^ 4 = halfC S x ^ 4 := by ring
      linarith
    · rw [ha]
      linarith [hxU.1, hyj.1]
    · rw [ha]
      linarith [hxU.2, hyj.2]
  -- Chebyshev / Markov on the window
  let μI := MeasureTheory.volume.restrict (Set.Ioc a (a + 2 * π))
  have hint : MeasureTheory.Integrable (fun x => halfC S x ^ 4) μI :=
    ((continuous_halfC S).pow 4).integrableOn_Ioc
  have hnn : 0 ≤ᵐ[μI] (fun x => halfC S x ^ 4) :=
    Filter.Eventually.of_forall (fun x => by
      show (0 : ℝ) ≤ halfC S x ^ 4
      positivity)
  have hmarkov := MeasureTheory.mul_meas_ge_le_integral_of_nonneg hnn hint (τ ^ 4)
  have hintI : ∫ x, halfC S x ^ 4 ∂μI = ∫ x in (0 : ℝ)..2 * π, halfC S x ^ 4 := by
    show ∫ x in Set.Ioc a (a + 2 * π), halfC S x ^ 4 = _
    rw [← intervalIntegral.integral_of_le (by linarith : a ≤ a + 2 * π)]
    have hper : Function.Periodic (fun x => halfC S x ^ 4) (2 * π) := fun x => by
      simp only [halfC_periodic S x]
    have := hper.intervalIntegral_add_eq a 0
    rw [this, zero_add]
  rw [hintI] at hmarkov
  have hmeas : (n : ℝ) * (2 * r) ≤ μI.real {x | τ ^ 4 ≤ halfC S x ^ 4} := by
    rw [← hvolU]
    have hfin : MeasureTheory.volume ({x | τ ^ 4 ≤ halfC S x ^ 4} ∩ Set.Ioc a (a + 2 * π)) ≠ ⊤ :=
      ((MeasureTheory.measure_mono Set.inter_subset_right).trans_lt measure_Ioc_lt_top).ne
    calc MeasureTheory.volume.real (⋃ j ∈ Finset.range n, U j)
        ≤ MeasureTheory.volume.real ({x | τ ^ 4 ≤ halfC S x ^ 4} ∩ Set.Ioc a (a + 2 * π)) :=
          MeasureTheory.measureReal_mono hsub hfin
      _ = μI.real {x | τ ^ 4 ≤ halfC S x ^ 4} :=
          (MeasureTheory.measureReal_restrict_apply' measurableSet_Ioc).symm
  have hmom := integral_halfC_pow_four_le S hS
  have hτ4 : 0 ≤ τ ^ 4 := by positivity
  have hchain : τ ^ 4 * ((n : ℝ) * (2 * r)) ≤ 2 * π * (3 * (S.card : ℝ) ^ 2 / 4) := by
    calc τ ^ 4 * ((n : ℝ) * (2 * r)) ≤ τ ^ 4 * μI.real {x | τ ^ 4 ≤ halfC S x ^ 4} :=
          mul_le_mul_of_nonneg_left hmeas hτ4
      _ ≤ ∫ x in (0 : ℝ)..2 * π, halfC S x ^ 4 := hmarkov
      _ ≤ 2 * π * (3 * (S.card : ℝ) ^ 2 / 4) := hmom
  -- contradiction with the numerical condition
  have hk2 : (0 : ℝ) < (S.card : ℝ) ^ 2 := by positivity
  have hden : 0 < η ^ 4 * (S.card : ℝ) ^ 2 := by positivity
  have hc2 : 24 * π < 2 * r * n * (η ^ 4 * (S.card : ℝ) ^ 2) := (div_lt_iff₀ hden).mp hcond
  have hc3 := mul_lt_mul_of_pos_right hc2 (by positivity : (0 : ℝ) < (S.card : ℝ) ^ 2 / 16)
  rw [hτ] at hchain
  nlinarith

/-- **M4 (P16 main theorem, sinc form).** Same conclusion as
`halfSquare_lower_bound_of_visit`, with the visit property replaced by the explicit numerical
hypothesis `∑_{s ∈ S} sinc² ((3s + 1/2) h / 2) < √(η k / 2)` (via the visit lemma M3).
No Sidon counting bound (Lindström) is needed for this form. -/
theorem halfSquare_lower_bound (S : Finset ℤ) (hS : IsSidon S) (L : ℝ)
    (hL : ∀ s ∈ S, |(s : ℝ)| ≤ L) (η : ℝ) (hη : 0 < η) (h : ℝ) (hh : 0 < h)
    (hsinc : ∑ s ∈ S, Real.sinc ((3 * (s : ℝ) + 1 / 2) * h / 2) ^ 2 <
      Real.sqrt (η * S.card / 2))
    (hcond : 24 * π / (η ^ 4 * (S.card : ℝ) ^ 2) <
      2 * (η / (2 * (6 * L + 1))) *
        (⌊2 * π / (2 * h + 2 * (η / (2 * (6 * L + 1))))⌋₊ : ℝ)) :
    ∃ x : ℝ, cosSum (buSet S) x < -((1 / 2 - η) * S.card) :=
  halfSquare_lower_bound_of_visit S hS L hL η hη h hh
    (fun c => exists_visit_of_sinc_sum_lt S (fun s => 3 * (s : ℝ) + 1 / 2) h _ hh hsinc c) hcond

end ChowlaCosine
