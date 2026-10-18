import ChowlaCosine.HalfSquare

/-!
# P16, unconditional explicit form

`halfSquare_lower_bound_min` (in `HalfSquare.lean`) needs the numerical hypothesis
`∑_{s ∈ S} min (1, 4 / ((3s + 1/2) h)²) < √(η |S| / 2)`. Here we remove it with an elementary
Sidon counting argument and an explicit choice of `h`.

## Sidon counting
* `sidon_card_mul_pred_le_of_diam`: if `S` is Sidon and `t - s ≤ D` for all `s, t ∈ S`,
  then `|S| (|S| - 1) ≤ 2 D` (the positive differences are pairwise distinct and lie in `[1, D]`).
* `sidon_card_mul_pred_le_of_Ico`, `sidon_card_le_one_add_sqrt_of_Ico`: the interval forms
  `|S| (|S| - 1) / 2 ≤ m - 1` and `|S| ≤ 1 + √(2 (m - 1))` for `S ⊆ [a, a + m)`.
* `card_filter_abs_half_le`, `card_filter_abs_half_le_sqrt`: for `u ≥ 0`, the number `N` of
  `s ∈ S` with `|3 s + 1/2| ≤ u` satisfies `N (N - 1) ≤ 4u/3`, hence `N ≤ 1 + √(4u/3)`.

## Majorant sum (rank argument, no integrals)
Order `S` by `|b_s|`, `b_s = 3 s + 1/2` (the values `|b_s|` are pairwise distinct). If `s` has
rank `ρ` (number of `t ∈ S` with `|b_t| < |b_s|`), the counting bound applied to
`{t : |b_t| ≤ |b_s|}` gives `ρ (ρ + 1) ≤ 4 |b_s| / 3` (`rankB_bound`). Comparing with the
telescoping majorant `(a/3)(1/ρ³ - 1/(ρ+1)³) ≥ a / (ρ² (ρ+1)²)` gives, for `u₀ > 0`,
`∑_s min (1, u₀² / b_s²) ≤ 1 + (4/3) √(4 u₀ / 3)` (`sum_min_absB_le`), i.e. with `u₀ = 2/h`,
`∑_s min (1, 4 / (b_s h)²) ≤ 1 + (4/3) √(8 / (3 h))` (`sum_min_le_sidon`).

## Final theorem
With `h = 64 / (3 η |S|)`, `halfSquare_lower_bound_explicit`: if `S` is Sidon, `|s| ≤ L` on `S`,
`1 ≤ L`, `0 < η ≤ 1/2` and `1000 (6 L + 1) ≤ η⁶ |S|³`, then there is a real `x` with
`f_{A(S)}(x) < -(1/2 - η) |S|`. Corollary `halfSquare_lower_bound_explicit'`: the same under
`7000 L ≤ η⁶ |S|³`.
-/

open Real

namespace ChowlaCosine

/-! ### Sidon counting -/

/-- The Sidon property passes to subsets. -/
theorem IsSidon.mono {S T : Finset ℤ} (hS : IsSidon S) (hTS : T ⊆ S) : IsSidon T :=
  fun a ha b hb c hc d hd h => hS a (hTS ha) b (hTS hb) c (hTS hc) d (hTS hd) h

/-- For a Sidon set the difference map `(s, t) ↦ t - s` is injective on pairs `s < t`. -/
theorem injOn_sub_ltPairs_of_sidon (T : Finset ℤ) (hT : IsSidon T) :
    Set.InjOn (fun p : ℤ × ℤ => p.2 - p.1) ↑(ltPairs T) := by
  intro p hp q hq hpq
  rw [Finset.mem_coe] at hp hq
  simp only [ltPairs, Finset.mem_filter, Finset.mem_product] at hp hq
  simp only at hpq
  have h : p.2 + q.1 = q.2 + p.1 := by omega
  rcases hT p.2 hp.1.2 q.1 hq.1.1 q.2 hq.1.2 p.1 hp.1.1 h with h' | h'
  · exact Prod.ext h'.2.symm h'.1
  · exact absurd h'.1 (ne_of_gt hp.2)

/-- **Sidon counting, diameter form.** If `T` is Sidon and `t - s ≤ D` for all `s, t ∈ T`,
then `|T| (|T| - 1) ≤ 2 D`. -/
theorem sidon_card_mul_pred_le_of_diam (T : Finset ℤ) (hT : IsSidon T) (D : ℕ)
    (hD : ∀ s ∈ T, ∀ t ∈ T, t - s ≤ (D : ℤ)) : T.card * (T.card - 1) ≤ 2 * D := by
  rw [← two_mul_card_ltPairs]
  have hsub : (ltPairs T).image (fun p : ℤ × ℤ => p.2 - p.1) ⊆ Finset.Icc 1 (D : ℤ) := by
    intro d hd
    simp only [Finset.mem_image, ltPairs, Finset.mem_filter, Finset.mem_product] at hd
    obtain ⟨p, ⟨⟨h1, h2⟩, hlt⟩, rfl⟩ := hd
    have := hD p.1 h1 p.2 h2
    rw [Finset.mem_Icc]
    constructor <;> omega
  have hc := Finset.card_le_card hsub
  rw [Finset.card_image_of_injOn (injOn_sub_ltPairs_of_sidon T hT), Int.card_Icc] at hc
  omega

/-- **Sidon counting, interval form.** If `S` is Sidon and `S ⊆ [a, a + m)`, then
`|S| (|S| - 1) ≤ 2 (m - 1)`. -/
theorem sidon_card_mul_pred_le_of_Ico (S : Finset ℤ) (hS : IsSidon S) (a : ℤ) (m : ℕ)
    (hm : ∀ s ∈ S, a ≤ s ∧ s < a + m) : S.card * (S.card - 1) ≤ 2 * (m - 1) := by
  apply sidon_card_mul_pred_le_of_diam S hS (m - 1)
  intro s hs t ht
  have h1 := hm s hs
  have h2 := hm t ht
  omega

/-- `N (N - 1) ≤ w` implies `N ≤ 1 + √w`. -/
theorem le_one_add_sqrt_of_mul_pred_le {N w : ℝ} (h : N * (N - 1) ≤ w) : N ≤ 1 + Real.sqrt w := by
  rcases le_or_gt N 1 with h1 | h1
  · linarith [Real.sqrt_nonneg w]
  · have hsq : (N - 1) ^ 2 ≤ w := by nlinarith
    have := Real.sqrt_le_sqrt hsq
    rw [Real.sqrt_sq (by linarith)] at this
    linarith

/-- **Sidon counting, interval form with square root.** If `S` is Sidon and `S ⊆ [a, a + m)`,
then `|S| ≤ 1 + √(2 (m - 1))`. -/
theorem sidon_card_le_one_add_sqrt_of_Ico (S : Finset ℤ) (hS : IsSidon S) (a : ℤ) (m : ℕ)
    (hm : ∀ s ∈ S, a ≤ s ∧ s < a + m) :
    (S.card : ℝ) ≤ 1 + Real.sqrt (2 * ((m : ℝ) - 1)) := by
  have h := sidon_card_mul_pred_le_of_Ico S hS a m hm
  rcases Nat.eq_zero_or_pos S.card with h0 | hpos
  · rw [h0]
    simp only [Nat.cast_zero]
    linarith [Real.sqrt_nonneg (2 * ((m : ℝ) - 1))]
  · have hm1 : 1 ≤ m := by
      obtain ⟨s, hs⟩ := Finset.card_pos.mp hpos
      have := hm s hs
      omega
    have hcast : ((S.card * (S.card - 1) : ℕ) : ℝ) ≤ ((2 * (m - 1) : ℕ) : ℝ) := by
      exact_mod_cast h
    push_cast [Nat.cast_sub (show 1 ≤ S.card from hpos), Nat.cast_sub hm1] at hcast
    exact le_one_add_sqrt_of_mul_pred_le hcast

/-- **Sidon counting, real diameter form.** If `T` is Sidon, `0 ≤ w` and `t - s ≤ w` for all
`s, t ∈ T`, then `|T| (|T| - 1) ≤ 2 w`. -/
theorem sidon_card_mul_pred_le_real (T : Finset ℤ) (hT : IsSidon T) (w : ℝ) (hw0 : 0 ≤ w)
    (hw : ∀ s ∈ T, ∀ t ∈ T, (t : ℝ) - s ≤ w) :
    (T.card : ℝ) * ((T.card : ℝ) - 1) ≤ 2 * w := by
  have hD : ∀ s ∈ T, ∀ t ∈ T, t - s ≤ ((⌊w⌋₊ : ℕ) : ℤ) := by
    intro s hs t ht
    rcases le_or_gt (t - s) 0 with h0 | h0
    · omega
    · have h1 : (((t - s).toNat : ℕ) : ℝ) ≤ w := by
        have e : (((t - s).toNat : ℕ) : ℤ) = t - s := Int.toNat_of_nonneg h0.le
        have h2 : (((t - s).toNat : ℕ) : ℝ) = ((t - s : ℤ) : ℝ) := by exact_mod_cast e
        rw [h2]
        push_cast
        exact hw s hs t ht
      have := Nat.le_floor h1
      omega
  have hn := sidon_card_mul_pred_le_of_diam T hT _ hD
  have hfl : (⌊w⌋₊ : ℝ) ≤ w := Nat.floor_le hw0
  rcases Nat.eq_zero_or_pos T.card with h0 | hpos
  · rw [h0]
    simp only [Nat.cast_zero, zero_mul]
    linarith
  · have hcast : ((T.card * (T.card - 1) : ℕ) : ℝ) ≤ ((2 * ⌊w⌋₊ : ℕ) : ℝ) := by exact_mod_cast hn
    push_cast [Nat.cast_sub (show 1 ≤ T.card from hpos)] at hcast
    linarith

/-- **Counting the frequencies `b_s = 3 s + 1/2`.** For a Sidon set `S` and `u ≥ 0`, the number
`N` of `s ∈ S` with `|3 s + 1/2| ≤ u` satisfies `N (N - 1) ≤ 4 u / 3`. -/
theorem card_filter_abs_half_le (S : Finset ℤ) (hS : IsSidon S) (u : ℝ) (hu : 0 ≤ u) :
    ((S.filter (fun s : ℤ => |3 * (s : ℝ) + 1 / 2| ≤ u)).card : ℝ) *
      (((S.filter (fun s : ℤ => |3 * (s : ℝ) + 1 / 2| ≤ u)).card : ℝ) - 1) ≤ 4 * u / 3 := by
  have := sidon_card_mul_pred_le_real (S.filter (fun s : ℤ => |3 * (s : ℝ) + 1 / 2| ≤ u))
    (hS.mono (Finset.filter_subset _ _)) (2 * u / 3) (by positivity) (by
      intro s hs t ht
      simp only [Finset.mem_filter] at hs ht
      have h1 := abs_le.mp hs.2
      have h2 := abs_le.mp ht.2
      linarith [h1.1, h2.2])
  linarith

/-- **Counting the frequencies, square-root form.** For a Sidon set `S` and `u ≥ 0`,
`#{s ∈ S : |3 s + 1/2| ≤ u} ≤ 1 + √(4 u / 3)`. -/
theorem card_filter_abs_half_le_sqrt (S : Finset ℤ) (hS : IsSidon S) (u : ℝ) (hu : 0 ≤ u) :
    ((S.filter (fun s : ℤ => |3 * (s : ℝ) + 1 / 2| ≤ u)).card : ℝ) ≤ 1 + Real.sqrt (4 * u / 3) :=
  le_one_add_sqrt_of_mul_pred_le (card_filter_abs_half_le S hS u hu)

/-! ### Ranks of the frequencies -/

/-- `|b_s| = |3 s + 1/2|`. -/
noncomputable def absB (s : ℤ) : ℝ := |3 * (s : ℝ) + 1 / 2|

theorem absB_injective : Function.Injective absB := by
  intro s t h
  unfold absB at h
  rcases abs_eq_abs.mp h with h' | h'
  · have : (s : ℝ) = t := by linarith
    exact_mod_cast this
  · have h6 : ((3 * (s + t) + 1 : ℤ) : ℝ) = 0 := by push_cast; linarith
    have : (3 * (s + t) + 1 : ℤ) = 0 := by exact_mod_cast h6
    omega

theorem absB_pos (s : ℤ) : 0 < absB s := by
  unfold absB
  apply abs_pos.mpr
  intro h0
  have h6 : ((6 * s + 1 : ℤ) : ℝ) = 0 := by push_cast; linarith
  have : (6 * s + 1 : ℤ) = 0 := by exact_mod_cast h6
  omega

/-- The rank of `s` in `S` with respect to `|b_t|`: `#{t ∈ S : |b_t| < |b_s|}`. -/
noncomputable def rankB (S : Finset ℤ) (s : ℤ) : ℕ := (S.filter (fun t => absB t < absB s)).card

theorem rankB_lt_rankB (S : Finset ℤ) {s t : ℤ} (hs : s ∈ S) (hst : absB s < absB t) :
    rankB S s < rankB S t := by
  unfold rankB
  apply Finset.card_lt_card
  rw [Finset.ssubset_iff_of_subset]
  · exact ⟨s, Finset.mem_filter.mpr ⟨hs, hst⟩, fun h => lt_irrefl _ (Finset.mem_filter.mp h).2⟩
  · intro x hx
    rw [Finset.mem_filter] at hx ⊢
    exact ⟨hx.1, hx.2.trans hst⟩

theorem rankB_injOn (S : Finset ℤ) : Set.InjOn (rankB S) ↑S := by
  intro s hs t ht hst
  by_contra hne
  rcases lt_or_gt_of_ne (fun h => hne (absB_injective h)) with h | h
  · exact absurd hst (rankB_lt_rankB S hs h).ne
  · exact absurd hst (rankB_lt_rankB S ht h).ne'

theorem rankB_lt_card (S : Finset ℤ) {s : ℤ} (hs : s ∈ S) : rankB S s < S.card := by
  unfold rankB
  apply Finset.card_lt_card
  rw [Finset.ssubset_iff_of_subset (Finset.filter_subset _ _)]
  exact ⟨s, hs, fun h => lt_irrefl _ (Finset.mem_filter.mp h).2⟩

/-- **Rank bound.** For a Sidon set `S` and `s ∈ S` of rank `ρ`, `ρ (ρ + 1) ≤ 4 |b_s| / 3`. -/
theorem rankB_bound (S : Finset ℤ) (hS : IsSidon S) {s : ℤ} (hs : s ∈ S) :
    (rankB S s : ℝ) * ((rankB S s : ℝ) + 1) ≤ 4 * absB s / 3 := by
  set T := S.filter (fun t => absB t ≤ absB s) with hT
  have hTcard : rankB S s + 1 ≤ T.card := by
    have hsub : insert s (S.filter (fun t => absB t < absB s)) ⊆ T := by
      intro x hx
      rw [Finset.mem_insert] at hx
      rw [hT, Finset.mem_filter]
      rcases hx with rfl | hx
      · exact ⟨hs, le_rfl⟩
      · rw [Finset.mem_filter] at hx
        exact ⟨hx.1, hx.2.le⟩
    have hns : s ∉ S.filter (fun t => absB t < absB s) :=
      fun h => lt_irrefl _ (Finset.mem_filter.mp h).2
    have := Finset.card_le_card hsub
    rw [Finset.card_insert_of_notMem hns] at this
    exact this
  have hTS : IsSidon T := hS.mono (Finset.filter_subset _ _)
  have hv := absB_pos s
  have h := sidon_card_mul_pred_le_real T hTS (2 * absB s / 3) (by positivity) (by
    intro x hx y hy
    rw [hT, Finset.mem_filter] at hx hy
    unfold absB at hx hy ⊢
    have h1 := le_abs_self (3 * (y : ℝ) + 1 / 2)
    have h2 := neg_abs_le (3 * (x : ℝ) + 1 / 2)
    linarith [hx.2, hy.2])
  have hc : ((rankB S s : ℝ) + 1) ≤ T.card := by exact_mod_cast hTcard
  have hr0 : (0 : ℝ) ≤ rankB S s := Nat.cast_nonneg _
  nlinarith [mul_nonneg (sub_nonneg.mpr hc) (by positivity : (0 : ℝ) ≤ T.card + rankB S s)]

/-! ### The telescoping majorant -/

/-- `G_{R,a}(ρ) = 1` for `ρ < R` and `G_{R,a}(ρ) = (a/3) (1/ρ³ - 1/(ρ+1)³)` for `ρ ≥ R`. -/
noncomputable def telG (R : ℕ) (a : ℝ) (ρ : ℕ) : ℝ :=
  if ρ < R then 1 else a / 3 * (1 / (ρ : ℝ) ^ 3 - 1 / ((ρ : ℝ) + 1) ^ 3)

theorem one_div_sq_sq_le (ρ : ℝ) (hρ : 0 < ρ) :
    1 / (ρ ^ 2 * (ρ + 1) ^ 2) ≤ (1 / ρ ^ 3 - 1 / (ρ + 1) ^ 3) / 3 := by
  have key : 1 / ρ ^ 3 - 1 / (ρ + 1) ^ 3 =
      3 / (ρ ^ 2 * (ρ + 1) ^ 2) + 1 / (ρ ^ 3 * (ρ + 1) ^ 3) := by
    field_simp
    ring
  rw [key]
  have : 0 ≤ 1 / (ρ ^ 3 * (ρ + 1) ^ 3) := by positivity
  have e : 3 / (ρ ^ 2 * (ρ + 1) ^ 2) = 3 * (1 / (ρ ^ 2 * (ρ + 1) ^ 2)) := by ring
  rw [e]
  linarith

theorem telG_nonneg (R : ℕ) (hR : 1 ≤ R) (a : ℝ) (ha : 0 ≤ a) (ρ : ℕ) : 0 ≤ telG R a ρ := by
  unfold telG
  split_ifs with h
  · norm_num
  · push Not at h
    have hρ : (0 : ℝ) < ρ := by exact_mod_cast (lt_of_lt_of_le Nat.zero_lt_one (le_trans hR h))
    have h1 : 1 / ((ρ : ℝ) + 1) ^ 3 ≤ 1 / (ρ : ℝ) ^ 3 :=
      one_div_le_one_div_of_le (by positivity) (pow_le_pow_left₀ hρ.le (by linarith) 3)
    have h2 : 0 ≤ 1 / (ρ : ℝ) ^ 3 - 1 / ((ρ : ℝ) + 1) ^ 3 := by linarith
    exact mul_nonneg (by positivity) h2

theorem sum_range_telG_le (R : ℕ) (hR : 1 ≤ R) (a : ℝ) (ha : 0 ≤ a) (n : ℕ) :
    ∑ ρ ∈ Finset.range n, telG R a ρ ≤ R + a / (3 * (R : ℝ) ^ 3) := by
  have hR0 : (0 : ℝ) < R := by exact_mod_cast hR
  have key : ∀ n, R ≤ n → ∑ ρ ∈ Finset.range n, telG R a ρ =
      R + a / 3 * (1 / (R : ℝ) ^ 3 - 1 / (n : ℝ) ^ 3) := by
    intro n hn
    induction n, hn using Nat.le_induction with
    | base =>
      have : ∑ ρ ∈ Finset.range R, telG R a ρ = R := by
        rw [Finset.sum_congr rfl (fun ρ hρ => by
          unfold telG
          rw [if_pos (Finset.mem_range.mp hρ)])]
        simp
      rw [this]
      ring
    | succ n hn ih =>
      rw [Finset.sum_range_succ, ih]
      unfold telG
      rw [if_neg (not_lt.mpr hn)]
      push_cast
      ring
  rcases le_or_gt R n with hn | hn
  · rw [key n hn]
    have h1 : 0 ≤ a / 3 * (1 / (n : ℝ) ^ 3) := by positivity
    have e : a / 3 * (1 / (R : ℝ) ^ 3) = a / (3 * (R : ℝ) ^ 3) := by field_simp
    nlinarith
  · have : ∑ ρ ∈ Finset.range n, telG R a ρ = n := by
      rw [Finset.sum_congr rfl (fun ρ hρ => by
        unfold telG
        rw [if_pos (lt_trans (Finset.mem_range.mp hρ) hn)])]
      simp
    rw [this]
    have h1 : (n : ℝ) ≤ R := by exact_mod_cast hn.le
    have h2 : 0 ≤ a / (3 * (R : ℝ) ^ 3) := by positivity
    linarith

/-- Pointwise majorant: `min (1, u₀² / b_s²) ≤ G_{R, 16 u₀²/9}(rank s)` for `R ≥ 1`. -/
theorem min_le_telG (S : Finset ℤ) (hS : IsSidon S) {s : ℤ} (hs : s ∈ S) (u0 : ℝ)
    (R : ℕ) (hR : 1 ≤ R) :
    min 1 (u0 ^ 2 / absB s ^ 2) ≤ telG R (16 * u0 ^ 2 / 9) (rankB S s) := by
  unfold telG
  split_ifs with hρ
  · exact min_le_left _ _
  · push Not at hρ
    have hρ1 : (1 : ℝ) ≤ (rankB S s : ℝ) := by
      have : 1 ≤ rankB S s := le_trans hR hρ
      exact_mod_cast this
    have hb := rankB_bound S hS hs
    have hv := absB_pos s
    set ρ : ℝ := (rankB S s : ℝ) with hρdef
    refine le_trans (min_le_right _ _) ?_
    have h0 : 0 ≤ ρ * (ρ + 1) := by positivity
    have hv2 : 9 * (ρ ^ 2 * (ρ + 1) ^ 2) ≤ 16 * absB s ^ 2 := by
      have := pow_le_pow_left₀ h0 hb 2
      nlinarith
    have step1 : u0 ^ 2 / absB s ^ 2 ≤ 16 * u0 ^ 2 / 9 * (1 / (ρ ^ 2 * (ρ + 1) ^ 2)) := by
      rw [mul_one_div, div_div, div_le_div_iff₀ (by positivity) (by positivity)]
      nlinarith [sq_nonneg u0]
    have step2 := one_div_sq_sq_le ρ (by linarith)
    calc u0 ^ 2 / absB s ^ 2 ≤ 16 * u0 ^ 2 / 9 * (1 / (ρ ^ 2 * (ρ + 1) ^ 2)) := step1
      _ ≤ 16 * u0 ^ 2 / 9 * ((1 / ρ ^ 3 - 1 / (ρ + 1) ^ 3) / 3) :=
          mul_le_mul_of_nonneg_left step2 (by positivity)
      _ = 16 * u0 ^ 2 / 9 / 3 * (1 / ρ ^ 3 - 1 / (ρ + 1) ^ 3) := by ring

/-- **Majorant sum for a Sidon set.** For a Sidon set `S` and `u₀ > 0`,
`∑_{s ∈ S} min (1, u₀² / b_s²) ≤ 1 + (4/3) √(4 u₀ / 3)`, `b_s = 3 s + 1/2`. -/
theorem sum_min_absB_le (S : Finset ℤ) (hS : IsSidon S) (u0 : ℝ) (hu0 : 0 < u0) :
    ∑ s ∈ S, min 1 (u0 ^ 2 / absB s ^ 2) ≤ 1 + 4 / 3 * Real.sqrt (4 * u0 / 3) := by
  set q := Real.sqrt (4 * u0 / 3) with hq
  have hqpos : 0 < q := Real.sqrt_pos.mpr (by positivity)
  have hq2 : q ^ 2 = 4 * u0 / 3 := Real.sq_sqrt (by positivity)
  set R : ℕ := ⌈q⌉₊ with hR
  have hR1 : 1 ≤ R := Nat.one_le_iff_ne_zero.mpr (Nat.ceil_pos.mpr hqpos).ne'
  have hqR : q ≤ R := Nat.le_ceil q
  have hRq : (R : ℝ) < q + 1 := Nat.ceil_lt_add_one hqpos.le
  set a : ℝ := 16 * u0 ^ 2 / 9 with ha
  have haq : a = q ^ 4 := by
    rw [ha, show q ^ 4 = (q ^ 2) ^ 2 by ring, hq2]
    ring
  calc ∑ s ∈ S, min 1 (u0 ^ 2 / absB s ^ 2)
      ≤ ∑ s ∈ S, telG R a (rankB S s) :=
        Finset.sum_le_sum (fun s hs => min_le_telG S hS hs u0 R hR1)
    _ = ∑ ρ ∈ S.image (rankB S), telG R a ρ := (Finset.sum_image (rankB_injOn S)).symm
    _ ≤ ∑ ρ ∈ Finset.range S.card, telG R a ρ := by
        apply Finset.sum_le_sum_of_subset_of_nonneg
        · intro ρ hρ
          rw [Finset.mem_image] at hρ
          obtain ⟨s, hs, rfl⟩ := hρ
          exact Finset.mem_range.mpr (rankB_lt_card S hs)
        · intro ρ _ _
          exact telG_nonneg R hR1 a (by positivity) ρ
    _ ≤ R + a / (3 * (R : ℝ) ^ 3) := sum_range_telG_le R hR1 a (by positivity) _
    _ ≤ 1 + 4 / 3 * q := by
        have h1 : a / (3 * (R : ℝ) ^ 3) ≤ q / 3 := by
          have hR0 : (0 : ℝ) < R := lt_of_lt_of_le hqpos hqR
          rw [haq, div_le_div_iff₀ (by positivity) (by norm_num)]
          have : q ^ 3 ≤ (R : ℝ) ^ 3 := pow_le_pow_left₀ hqpos.le hqR 3
          nlinarith [mul_le_mul_of_nonneg_left this hqpos.le]
        linarith

/-- **Majorant sum, `h`-form.** For a Sidon set `S` and `h > 0`,
`∑_{s ∈ S} min (1, 4 / ((3 s + 1/2) h)²) ≤ 1 + (4/3) √(8 / (3 h))`. -/
theorem sum_min_le_sidon (S : Finset ℤ) (hS : IsSidon S) (h : ℝ) (hh : 0 < h) :
    ∑ s ∈ S, min 1 (4 / ((3 * (s : ℝ) + 1 / 2) * h) ^ 2) ≤
      1 + 4 / 3 * Real.sqrt (8 / (3 * h)) := by
  have := sum_min_absB_le S hS (2 / h) (by positivity)
  have e1 : 4 * (2 / h) / 3 = 8 / (3 * h) := by field_simp; ring
  rw [e1] at this
  refine le_trans (le_of_eq (Finset.sum_congr rfl (fun s _ => ?_))) this
  unfold absB
  rw [sq_abs]
  generalize 3 * (s : ℝ) + 1 / 2 = b
  rw [div_pow, mul_pow, div_div]
  congr 1
  ring

/-! ### The explicit final theorem -/

/-- **Explicit numerical condition.** If `1 ≤ L`, `0 < η ≤ 1/2`, `k ≥ 0` and
`1000 (6 L + 1) ≤ η⁶ k³`, then with `h = 64 / (3 η k)` and `r = η / (2 (6 L + 1))`,
`24 π / (η⁴ k²) < 2 r ⌊2π / (2h + 2r)⌋`. -/
theorem halfSquare_hcond_explicit (k L η : ℝ) (hL1 : 1 ≤ L) (hη : 0 < η) (hη' : η ≤ 1 / 2)
    (hk0 : 0 ≤ k) (hk : 1000 * (6 * L + 1) ≤ η ^ 6 * k ^ 3) :
    24 * π / (η ^ 4 * k ^ 2) <
      2 * (η / (2 * (6 * L + 1))) *
        (⌊2 * π / (2 * (64 / (3 * (η * k))) + 2 * (η / (2 * (6 * L + 1))))⌋₊ : ℝ) := by
  have hz : 19 ≤ η ^ 2 * k := by
    by_contra hcon
    push Not at hcon
    have h0 : 0 ≤ η ^ 2 * k := by positivity
    have h1 : (η ^ 2 * k) ^ 3 < 19 ^ 3 := pow_lt_pow_left₀ hcon h0 (by norm_num)
    have h2 : (η ^ 2 * k) ^ 3 = η ^ 6 * k ^ 3 := by ring
    nlinarith
  have hx : 38 ≤ η * k := by nlinarith
  have hxpos : 0 < η * k := by linarith
  have hD7 : 7 ≤ 6 * L + 1 := by linarith
  have hDpos : 0 < 6 * L + 1 := by linarith
  set D := 6 * L + 1 with hD
  set r := η / (2 * D) with hr
  set h := 64 / (3 * (η * k)) with hh
  have hrpos : 0 < r := by positivity
  have hr28 : r ≤ 1 / 28 := by
    rw [hr, div_le_iff₀ (by positivity)]
    nlinarith
  have hhpos : 0 < h := by positivity
  have hh38 : h ≤ 64 / 114 := by
    rw [hh, div_le_div_iff₀ (by positivity) (by norm_num)]
    nlinarith
  set w := 2 * h + 2 * r with hw
  have hwpos : 0 < w := by positivity
  set Q := 2 * π / w with hQ
  have hπ := Real.pi_gt_three
  have hQ5 : 5 ≤ Q := by
    rw [hQ, le_div_iff₀ hwpos]
    nlinarith
  have hQw : Q * w = 2 * π := by
    rw [hQ]
    field_simp
  have hn : Q < (⌊Q⌋₊ : ℝ) + 1 := Nat.lt_floor_add_one Q
  -- the polynomial inequality `15 (h + r) ≤ r η⁴ k²`
  have hz3 : 361 * (η ^ 2 * k) ≤ η ^ 6 * k ^ 3 := by
    have e : η ^ 6 * k ^ 3 = (η ^ 2 * k) * (η ^ 2 * k) ^ 2 := by ring
    rw [e]
    have : (361 : ℝ) ≤ (η ^ 2 * k) ^ 2 := by nlinarith
    nlinarith
  have hpoly : 1920 * D + 45 * (η ^ 2 * k) ≤ 3 * (η ^ 6 * k ^ 3) := by nlinarith
  have hid : r * η ^ 4 * k ^ 2 - 15 * (h + r) =
      (3 * (η ^ 6 * k ^ 3) - 1920 * D - 45 * (η ^ 2 * k)) / (6 * D * (η * k)) := by
    have hD0 : D ≠ 0 := hDpos.ne'
    have hη0 : η ≠ 0 := hη.ne'
    have hk0' : k ≠ 0 := by
      intro h0
      rw [h0, mul_zero] at hxpos
      exact lt_irrefl _ hxpos
    rw [hr, hh]
    field_simp
    ring
  have hP : 15 * (h + r) ≤ r * η ^ 4 * k ^ 2 := by
    have : 0 ≤ (3 * (η ^ 6 * k ^ 3) - 1920 * D - 45 * (η ^ 2 * k)) / (6 * D * (η * k)) :=
      div_nonneg (by linarith) (by positivity)
    linarith
  set P := r * η ^ 4 * k ^ 2 with hPdef
  have hP0 : 0 ≤ P := by positivity
  have hwP : w ≤ 2 * P / 15 := by rw [hw]; linarith
  have hQ0 : 0 ≤ Q := by linarith
  have key : 24 * π ≤ 2 * r * (Q - 1) * (η ^ 4 * k ^ 2) := by
    have e1 : 2 * r * (Q - 1) * (η ^ 4 * k ^ 2) = 2 * (Q - 1) * P := by rw [hPdef]; ring
    rw [e1]
    have h1 : Q * w ≤ Q * (2 * P / 15) := mul_le_mul_of_nonneg_left hwP hQ0
    have h2 : 4 / 5 * Q * P ≤ (Q - 1) * P := mul_le_mul_of_nonneg_right (by linarith) hP0
    nlinarith
  have hkpos : 0 < k := by
    by_contra hcon
    push Not at hcon
    nlinarith
  have hden : 0 < η ^ 4 * k ^ 2 := by positivity
  rw [div_lt_iff₀ hden]
  have hlt : 2 * r * (Q - 1) * (η ^ 4 * k ^ 2) < 2 * r * (⌊Q⌋₊ : ℝ) * (η ^ 4 * k ^ 2) := by
    have h1 : Q - 1 < (⌊Q⌋₊ : ℝ) := by linarith
    have h2 := mul_lt_mul_of_pos_left h1 (by positivity : 0 < 2 * r)
    exact mul_lt_mul_of_pos_right h2 hden
  linarith

/-- **P16, unconditional explicit form.** Let `S` be a Sidon set of integers with `|s| ≤ L` for
all `s ∈ S`, `1 ≤ L`, and `0 < η ≤ 1/2`. If `1000 (6 L + 1) ≤ η⁶ |S|³`, then there is a real `x`
with `f_{A(S)}(x) < -(1/2 - η) |S|`, i.e. `M(A(S)) > (1/2 - η) |S|`
(here `|A(S)| = |S| (|S| - 1)`). The width `h = 64 / (3 η |S|)` is chosen inside the proof. -/
theorem halfSquare_lower_bound_explicit (S : Finset ℤ) (hS : IsSidon S) (L : ℝ)
    (hL : ∀ s ∈ S, |(s : ℝ)| ≤ L) (hL1 : 1 ≤ L) (η : ℝ) (hη : 0 < η) (hη' : η ≤ 1 / 2)
    (hk : 1000 * (6 * L + 1) ≤ η ^ 6 * (S.card : ℝ) ^ 3) :
    ∃ x : ℝ, cosSum (buSet S) x < -((1 / 2 - η) * S.card) := by
  have hk0 : (0 : ℝ) ≤ S.card := Nat.cast_nonneg _
  have hz : 19 ≤ η ^ 2 * (S.card : ℝ) := by
    by_contra hcon
    push Not at hcon
    have h0 : 0 ≤ η ^ 2 * (S.card : ℝ) := by positivity
    have h1 : (η ^ 2 * (S.card : ℝ)) ^ 3 < 19 ^ 3 := pow_lt_pow_left₀ hcon h0 (by norm_num)
    have h2 : (η ^ 2 * (S.card : ℝ)) ^ 3 = η ^ 6 * (S.card : ℝ) ^ 3 := by ring
    nlinarith
  have hx : 38 ≤ η * (S.card : ℝ) := by nlinarith
  have hxpos : 0 < η * (S.card : ℝ) := by linarith
  have hh : 0 < 64 / (3 * (η * (S.card : ℝ))) := by positivity
  refine halfSquare_lower_bound_min S hS L hL η hη (64 / (3 * (η * (S.card : ℝ)))) hh ?_
    (halfSquare_hcond_explicit (S.card : ℝ) L η hL1 hη hη' hk0 hk)
  refine lt_of_le_of_lt (sum_min_le_sidon S hS _ hh) ?_
  have e : 8 / (3 * (64 / (3 * (η * (S.card : ℝ))))) = η * (S.card : ℝ) / 8 := by
    field_simp
    ring
  rw [e]
  have hp2 : Real.sqrt (η * (S.card : ℝ) / 8) ^ 2 = η * (S.card : ℝ) / 8 :=
    Real.sq_sqrt (by positivity)
  have hp0 : 0 ≤ Real.sqrt (η * (S.card : ℝ) / 8) := Real.sqrt_nonneg _
  have hp : 2 ≤ Real.sqrt (η * (S.card : ℝ) / 8) := by nlinarith
  have h2p : 2 * Real.sqrt (η * (S.card : ℝ) / 8) ≤ Real.sqrt (η * (S.card : ℝ) / 2) := by
    rw [Real.le_sqrt (by positivity) (by positivity)]
    nlinarith
  linarith

/-- **P16, unconditional explicit form, `C · L` version.** Same conclusion as
`halfSquare_lower_bound_explicit` under the hypothesis `7000 L ≤ η⁶ |S|³`. -/
theorem halfSquare_lower_bound_explicit' (S : Finset ℤ) (hS : IsSidon S) (L : ℝ)
    (hL : ∀ s ∈ S, |(s : ℝ)| ≤ L) (hL1 : 1 ≤ L) (η : ℝ) (hη : 0 < η) (hη' : η ≤ 1 / 2)
    (hk : 7000 * L ≤ η ^ 6 * (S.card : ℝ) ^ 3) :
    ∃ x : ℝ, cosSum (buSet S) x < -((1 / 2 - η) * S.card) :=
  halfSquare_lower_bound_explicit S hS L hL hL1 η hη hη' (by linarith)

end ChowlaCosine
