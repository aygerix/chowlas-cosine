import ChowlaCosine.HalfSquareExplicit

/-!
# P16′: the half-square lower bound with rate exponent `1/5` (Gallagher large sieve)

`halfSquare_lower_bound_explicit` (in `HalfSquareExplicit.lean`) proves, for a Sidon set `S`
with `|s| ≤ L`, that `M(A(S)) > (1/2 - η) |S|` as soon as `1000 (6L + 1) ≤ η⁶ |S|³`. Its last
step is Chebyshev on `∫ C⁴` plus a Lipschitz neighbourhood of every visit. Here the Lipschitz /
Chebyshev step is replaced by a Gallagher-type large-sieve inequality, which improves the
hypothesis to `600 (6L + 1) ≤ η⁵ |S|³`.

## Gallagher's inequality
* `gallagher_local`: if `φ` has continuous derivative `φ'` and `y ∈ [a, b]`, then
  `(b - a) φ(y) ≤ ∫_a^b φ + (b - a) ∫_a^b |φ'|`.
* `gallagher_sum`: if moreover `φ ≥ 0`, `φ, φ'` are `T`-periodic, and the intervals
  `[y_j - δ₀/2, y_j + δ₀/2]` (`j < m`) are consecutive, non-overlapping and contained in
  `[c₀, c₀ + T]`, then `∑_{j<m} φ(y_j) ≤ (1/δ₀) ∫_0^T φ + ∫_0^T |φ'|`.

## The derivative term for `φ = C⁴`
With `C' = -S'`, `S'(x) = ∑_s (6s+1) sin((6s+1)x)` (`halfS`), and `|6s + 1| ≤ D` on `S`:
* `integral_halfC_sq_mul_halfS_sq_le`: `∫_0^{2π} C² S'² ≤ D² ∫_0^{2π} C⁴` (no Sidon hypothesis:
  termwise comparison of the two fourfold expansions; frequencies `≡ 1 mod 6` kill cross terms);
* `integral_abs_halfC_cube_mul_halfS_le`: `∫_0^{2π} |C³ S'| ≤ D ∫_0^{2π} C⁴` (pointwise AM-GM);
* `sieve_halfC_pow_four`: for separated points as above with `T = 2π`,
  `∑_{j<m} C(y_j)⁴ ≤ (1/δ₀ + 4D) ∫_0^{2π} C⁴`.

## Final theorem
`halfSquare_lower_bound_sieve`: if `S` is Sidon, `|s| ≤ L` on `S`, `1 ≤ L`, `0 < η ≤ 1/2` and
`600 (6L + 1) ≤ η⁵ |S|³`, then there is a real `x` with `f_{A(S)}(x) < -(1/2 - η) |S|`.
Proof: by contradiction; with `h = 64/(3η|S|)` every window `[4hj - h, 4hj + h]` contains a visit
`y_j` with `|P(y_j)| < √(η|S|/2)` (as in `HalfSquareExplicit.lean`), where then `C(y_j) < -η|S|`;
Gallagher with `δ₀ = 2h` on `m = ⌊π/(2h)⌋` visits contradicts `∫ C⁴ ≤ 2π · 3|S|²/4`.
The Sidon counting bound `|S|(|S| - 1) ≤ 4L` supplies `η⁴|S|² ≥ 600`.
-/

open Real

namespace ChowlaCosine

/-! ### Gallagher's inequality -/

/-- **Gallagher's inequality, local form.** If `φ` has derivative `φ'` everywhere, `φ'` is
continuous, `a ≤ b` and `y ∈ [a, b]`, then `(b - a) φ(y) ≤ ∫_a^b φ + (b - a) ∫_a^b |φ'|`. -/
theorem gallagher_local {φ φ' : ℝ → ℝ} (hφ : ∀ x, HasDerivAt φ (φ' x) x) (hφ' : Continuous φ')
    {a b y : ℝ} (hab : a ≤ b) (hy : y ∈ Set.Icc a b) :
    (b - a) * φ y ≤ (∫ x in a..b, φ x) + (b - a) * ∫ x in a..b, |φ' x| := by
  have hφc : Continuous φ := continuous_iff_continuousAt.mpr (fun x => (hφ x).continuousAt)
  have habs : Continuous (fun x => |φ' x|) := hφ'.abs
  have hnn : ∀ c d : ℝ, 0 ≤ᵐ[MeasureTheory.volume.restrict (Set.Ioc c d)] (fun x => |φ' x|) :=
    fun c d => Filter.Eventually.of_forall (fun x => by
      show (0 : ℝ) ≤ |φ' x|
      exact abs_nonneg _)
  set V := ∫ x in a..b, |φ' x| with hV
  have key : ∀ x ∈ Set.Icc a b, φ y ≤ φ x + V := by
    intro x hx
    have hFTC : ∫ t in x..y, φ' t = φ y - φ x :=
      intervalIntegral.integral_eq_sub_of_hasDerivAt (fun t _ => hφ t) (hφ'.intervalIntegrable _ _)
    have hle : φ y - φ x ≤ V := by
      rw [← hFTC]
      rcases le_total x y with hxy | hxy
      · calc ∫ t in x..y, φ' t ≤ ∫ t in x..y, |φ' t| :=
              intervalIntegral.integral_mono_on hxy (hφ'.intervalIntegrable _ _)
                (habs.intervalIntegrable _ _) (fun t _ => le_abs_self _)
          _ ≤ V := intervalIntegral.integral_mono_interval hx.1 hxy hy.2 (hnn a b)
                (habs.intervalIntegrable _ _)
      · rw [intervalIntegral.integral_symm, ← intervalIntegral.integral_neg]
        calc ∫ t in y..x, -φ' t ≤ ∫ t in y..x, |φ' t| :=
              intervalIntegral.integral_mono_on hxy (hφ'.neg.intervalIntegrable _ _)
                (habs.intervalIntegrable _ _) (fun t _ => neg_le_abs _)
          _ ≤ V := intervalIntegral.integral_mono_interval hy.1 hxy hx.2 (hnn a b)
                (habs.intervalIntegrable _ _)
    linarith
  have hint : ∫ _ in a..b, φ y ≤ ∫ x in a..b, (φ x + V) :=
    intervalIntegral.integral_mono_on hab (continuous_const.intervalIntegrable _ _)
      ((hφc.add continuous_const).intervalIntegrable _ _) key
  rw [intervalIntegral.integral_const, intervalIntegral.integral_add (hφc.intervalIntegrable _ _)
    (continuous_const.intervalIntegrable _ _), intervalIntegral.integral_const, smul_eq_mul,
    smul_eq_mul] at hint
  linarith

/-- Integrals of a nonnegative continuous function over consecutive non-overlapping intervals
`[s_j, e_j]` (`s_j ≤ e_j ≤ s_{j+1}`) add up to at most the integral over their hull. -/
theorem sum_integral_le_of_sorted {ψ : ℝ → ℝ} (hψ : Continuous ψ) (hψ0 : ∀ x, 0 ≤ ψ x)
    (s e : ℕ → ℝ) (m : ℕ) (hse : ∀ j ≤ m, s j ≤ e j) (hes : ∀ j < m, e j ≤ s (j + 1)) :
    ∑ j ∈ Finset.range (m + 1), ∫ x in s j..e j, ψ x ≤ ∫ x in s 0..e m, ψ x := by
  induction m with
  | zero => simp
  | succ m ih =>
    rw [Finset.sum_range_succ]
    have h1 := ih (fun j hj => hse j (by omega)) (fun j hj => hes j (by omega))
    have h2 : ∫ x in s (m + 1)..e (m + 1), ψ x ≤ ∫ x in e m..e (m + 1), ψ x :=
      intervalIntegral.integral_mono_interval (hes m (by omega)) (hse (m + 1) le_rfl) le_rfl
        (Filter.Eventually.of_forall (fun x => hψ0 x)) (hψ.intervalIntegrable _ _)
    have h3 : ∫ x in s 0..e (m + 1), ψ x = (∫ x in s 0..e m, ψ x) + ∫ x in e m..e (m + 1), ψ x :=
      (intervalIntegral.integral_add_adjacent_intervals (hψ.intervalIntegrable _ _)
        (hψ.intervalIntegrable _ _)).symm
    linarith

/-- **Gallagher's inequality (large sieve, periodic form).** Let `φ ≥ 0` have continuous
derivative `φ'`, both `T`-periodic (`T ≥ 0`), and let `δ₀ > 0`. If the points `y_0, …, y_{m-1}`
satisfy `y_j + δ₀ ≤ y_{j+1}` and `[y_j - δ₀/2, y_j + δ₀/2] ⊆ [c₀, c₀ + T]`, then
`∑_{j<m} φ(y_j) ≤ (1/δ₀) ∫_0^T φ + ∫_0^T |φ'|`. -/
theorem gallagher_sum {φ φ' : ℝ → ℝ} (hφ : ∀ x, HasDerivAt φ (φ' x) x) (hφ' : Continuous φ')
    (hφ0 : ∀ x, 0 ≤ φ x) {T : ℝ} (hT : 0 ≤ T) (hφT : Function.Periodic φ T)
    (hφ'T : Function.Periodic φ' T) {δ0 : ℝ} (hδ0 : 0 < δ0) (c0 : ℝ) (y : ℕ → ℝ) (m : ℕ)
    (hgap : ∀ j, j + 1 < m → y j + δ0 ≤ y (j + 1))
    (hlo : ∀ j < m, c0 ≤ y j - δ0 / 2) (hhi : ∀ j < m, y j + δ0 / 2 ≤ c0 + T) :
    ∑ j ∈ Finset.range m, φ (y j) ≤
      1 / δ0 * (∫ x in (0 : ℝ)..T, φ x) + ∫ x in (0 : ℝ)..T, |φ' x| := by
  have hφc : Continuous φ := continuous_iff_continuousAt.mpr (fun x => (hφ x).continuousAt)
  have hc2 : Continuous (fun x => δ0 * |φ' x|) := continuous_const.mul hφ'.abs
  set ψ : ℝ → ℝ := fun x => φ x + δ0 * |φ' x| with hψ
  have hψc : Continuous ψ := hφc.add hc2
  have hψ0 : ∀ x, 0 ≤ ψ x := fun x => add_nonneg (hφ0 x) (mul_nonneg hδ0.le (abs_nonneg _))
  have hψT : Function.Periodic ψ T := fun x => by simp only [hψ, hφT x, hφ'T x]
  have hsplit : ∀ c d : ℝ, ∫ x in c..d, ψ x =
      (∫ x in c..d, φ x) + δ0 * ∫ x in c..d, |φ' x| := by
    intro c d
    rw [hψ, intervalIntegral.integral_add (hφc.intervalIntegrable _ _) (hc2.intervalIntegrable _ _),
      intervalIntegral.integral_const_mul]
  -- local step
  have hloc : ∀ j, δ0 * φ (y j) ≤ ∫ x in (y j - δ0 / 2)..(y j + δ0 / 2), ψ x := by
    intro j
    have h := gallagher_local hφ hφ' (a := y j - δ0 / 2) (b := y j + δ0 / 2) (y := y j)
      (by linarith) ⟨by linarith, by linarith⟩
    rw [show y j + δ0 / 2 - (y j - δ0 / 2) = δ0 by ring] at h
    rw [hsplit]
    exact h
  -- summing over the disjoint intervals
  have hsum : ∑ j ∈ Finset.range m, ∫ x in (y j - δ0 / 2)..(y j + δ0 / 2), ψ x ≤
      ∫ x in (0 : ℝ)..T, ψ x := by
    rcases Nat.eq_zero_or_pos m with hm | hm
    · subst hm
      simp only [Finset.range_zero, Finset.sum_empty]
      exact intervalIntegral.integral_nonneg hT (fun x _ => hψ0 x)
    · obtain ⟨m', rfl⟩ : ∃ m', m = m' + 1 := ⟨m - 1, by omega⟩
      have hmono : ∀ j, j ≤ m' → y 0 ≤ y j := by
        intro j hj
        induction j with
        | zero => exact le_rfl
        | succ j ih =>
          have h1 := hgap j (by omega)
          have h2 := ih (by omega)
          linarith
      have h1 := sum_integral_le_of_sorted hψc hψ0 (fun j => y j - δ0 / 2) (fun j => y j + δ0 / 2)
        m' (fun j _ => by linarith) (fun j hj => by
          have := hgap j (by omega)
          linarith)
      have h2 : ∫ x in (y 0 - δ0 / 2)..(y m' + δ0 / 2), ψ x ≤ ∫ x in c0..c0 + T, ψ x :=
        intervalIntegral.integral_mono_interval (hlo 0 (by omega))
          (by have := hmono m' le_rfl; linarith) (hhi m' (by omega))
          (Filter.Eventually.of_forall (fun x => hψ0 x)) (hψc.intervalIntegrable _ _)
      have h3 : ∫ x in c0..c0 + T, ψ x = ∫ x in (0 : ℝ)..T, ψ x := by
        have := hψT.intervalIntegral_add_eq c0 0
        rw [zero_add] at this
        exact this
      linarith
  have htot : δ0 * ∑ j ∈ Finset.range m, φ (y j) ≤
      (∫ x in (0 : ℝ)..T, φ x) + δ0 * ∫ x in (0 : ℝ)..T, |φ' x| := by
    rw [Finset.mul_sum, ← hsplit]
    exact (Finset.sum_le_sum (fun j _ => hloc j)).trans hsum
  have hδ0' : δ0 ≠ 0 := hδ0.ne'
  calc ∑ j ∈ Finset.range m, φ (y j) = 1 / δ0 * (δ0 * ∑ j ∈ Finset.range m, φ (y j)) := by
        field_simp
    _ ≤ 1 / δ0 * ((∫ x in (0 : ℝ)..T, φ x) + δ0 * ∫ x in (0 : ℝ)..T, |φ' x|) :=
        mul_le_mul_of_nonneg_left htot (by positivity)
    _ = 1 / δ0 * (∫ x in (0 : ℝ)..T, φ x) + ∫ x in (0 : ℝ)..T, |φ' x| := by
        field_simp

/-! ### The derivative of `C` -/

/-- `S'(x) = ∑_s (6s + 1) sin ((6s + 1) x)`; `C' = -S'`. -/
noncomputable def halfS (S : Finset ℤ) (x : ℝ) : ℝ :=
  ∑ s ∈ S, ((6 * s + 1 : ℤ) : ℝ) * Real.sin (((6 * s + 1 : ℤ) : ℝ) * x)

theorem continuous_halfS (S : Finset ℤ) : Continuous (halfS S) := by
  unfold halfS
  fun_prop

theorem halfS_periodic (S : Finset ℤ) : Function.Periodic (halfS S) (2 * π) := by
  intro x
  unfold halfS
  refine Finset.sum_congr rfl (fun s _ => ?_)
  rw [mul_add, Real.sin_add_int_mul_two_pi]

/-- `C'(x) = -S'(x)`. -/
theorem hasDerivAt_halfC (S : Finset ℤ) (x : ℝ) : HasDerivAt (halfC S) (-halfS S x) x := by
  have h : ∀ s ∈ S, HasDerivAt (fun y => Real.cos (((6 * s + 1 : ℤ) : ℝ) * y))
      (-(((6 * s + 1 : ℤ) : ℝ) * Real.sin (((6 * s + 1 : ℤ) : ℝ) * x))) x := by
    intro s _
    have := ((hasDerivAt_id' x).const_mul (((6 * s + 1 : ℤ) : ℝ))).cos
    convert this using 1
    ring
  have h2 := HasDerivAt.fun_sum h
  rw [Finset.sum_neg_distrib] at h2
  exact h2

/-! ### `∫ C² S'² ≤ D² ∫ C⁴` -/

theorem cc_nonneg (m n : ℤ) : 0 ≤ cc m n := by
  unfold cc
  have := Real.pi_pos
  split_ifs <;> linarith

theorem sin_mul_sin_int (a b : ℤ) (y : ℝ) :
    Real.sin ((a : ℝ) * y) * Real.sin ((b : ℝ) * y) =
      (Real.cos (((a - b : ℤ) : ℝ) * y) - Real.cos (((a + b : ℤ) : ℝ) * y)) / 2 := by
  have e1 : ((a - b : ℤ) : ℝ) * y = (a : ℝ) * y - (b : ℝ) * y := by push_cast; ring
  have e2 : ((a + b : ℤ) : ℝ) * y = (a : ℝ) * y + (b : ℝ) * y := by push_cast; ring
  rw [e1, e2, Real.cos_sub, Real.cos_add]
  ring

/-- `∫_0^{2π} cos (a y) cos (b y) · (c sin (c y)) (d sin (d y)) dy` for integers `a, b, c, d`. -/
theorem integral_cos_cos_mul_sin_mul_sin (a b c d : ℤ) :
    ∫ y in (0 : ℝ)..2 * π, Real.cos ((a : ℝ) * y) * (Real.cos ((b : ℝ) * y) *
        (((c : ℝ) * Real.sin ((c : ℝ) * y)) * ((d : ℝ) * Real.sin ((d : ℝ) * y)))) =
      (c : ℝ) * d *
        ((cc (a - b) (c - d) - cc (a - b) (c + d) + cc (a + b) (c - d) - cc (a + b) (c + d)) / 4) := by
  have hpt : ∀ y : ℝ, Real.cos ((a : ℝ) * y) * (Real.cos ((b : ℝ) * y) *
        (((c : ℝ) * Real.sin ((c : ℝ) * y)) * ((d : ℝ) * Real.sin ((d : ℝ) * y)))) =
      (c : ℝ) * d * ((Real.cos (((a - b : ℤ) : ℝ) * y) * Real.cos (((c - d : ℤ) : ℝ) * y) -
        Real.cos (((a - b : ℤ) : ℝ) * y) * Real.cos (((c + d : ℤ) : ℝ) * y) +
        Real.cos (((a + b : ℤ) : ℝ) * y) * Real.cos (((c - d : ℤ) : ℝ) * y) -
        Real.cos (((a + b : ℤ) : ℝ) * y) * Real.cos (((c + d : ℤ) : ℝ) * y)) / 4) := by
    intro y
    have h1 := cos_mul_cos_int a b y
    have h2 := sin_mul_sin_int c d y
    calc Real.cos ((a : ℝ) * y) * (Real.cos ((b : ℝ) * y) *
          (((c : ℝ) * Real.sin ((c : ℝ) * y)) * ((d : ℝ) * Real.sin ((d : ℝ) * y))))
        = (c : ℝ) * d * ((Real.cos ((a : ℝ) * y) * Real.cos ((b : ℝ) * y)) *
            (Real.sin ((c : ℝ) * y) * Real.sin ((d : ℝ) * y))) := by ring
      _ = _ := by rw [h1, h2]; ring
  simp_rw [hpt]
  rw [intervalIntegral.integral_const_mul, intervalIntegral.integral_div,
    intervalIntegral.integral_sub, intervalIntegral.integral_add, intervalIntegral.integral_sub]
  · simp only [integral_cos_mul_cos_int, cc]
  all_goals
    apply Continuous.intervalIntegrable
    fun_prop

/-- `(∑ f)² (∑ g)²` as a fourfold sum. -/
theorem sum_sq_mul_sum_sq {ι : Type*} (s : Finset ι) (f g : ι → ℝ) :
    (∑ i ∈ s, f i) ^ 2 * (∑ i ∈ s, g i) ^ 2 =
      ∑ a ∈ s, ∑ b ∈ s, ∑ c ∈ s, ∑ d ∈ s, f a * (f b * (g c * g d)) := by
  have e2 : (∑ i ∈ s, g i) * (∑ i ∈ s, g i) = ∑ c ∈ s, ∑ d ∈ s, g c * g d := by
    rw [Finset.sum_mul_sum]
  have e3 : (∑ i ∈ s, f i) * (∑ c ∈ s, ∑ d ∈ s, g c * g d) =
      ∑ b ∈ s, ∑ c ∈ s, ∑ d ∈ s, f b * (g c * g d) := by
    rw [Finset.sum_mul_sum]
    simp_rw [Finset.mul_sum]
  have e4 : (∑ i ∈ s, f i) * (∑ b ∈ s, ∑ c ∈ s, ∑ d ∈ s, f b * (g c * g d)) =
      ∑ a ∈ s, ∑ b ∈ s, ∑ c ∈ s, ∑ d ∈ s, f a * (f b * (g c * g d)) := by
    rw [Finset.sum_mul_sum]
    simp_rw [Finset.mul_sum]
  rw [show (∑ i ∈ s, f i) ^ 2 * (∑ i ∈ s, g i) ^ 2 = (∑ i ∈ s, f i) * ((∑ i ∈ s, f i) *
      ((∑ i ∈ s, g i) * (∑ i ∈ s, g i))) by ring, e2, e3, e4]

/-- **Bernstein-type bound.** If `|6s + 1| ≤ D` for all `s ∈ S`, then
`∫_0^{2π} C² S'² ≤ D² ∫_0^{2π} C⁴` (no Sidon hypothesis needed). -/
theorem integral_halfC_sq_mul_halfS_sq_le (S : Finset ℤ) (D : ℝ)
    (hD : ∀ s ∈ S, |((6 * s + 1 : ℤ) : ℝ)| ≤ D) :
    ∫ x in (0 : ℝ)..2 * π, halfC S x ^ 2 * halfS S x ^ 2 ≤
      D ^ 2 * ∫ x in (0 : ℝ)..2 * π, halfC S x ^ 4 := by
  have hexp1 : ∀ x, halfC S x ^ 2 * halfS S x ^ 2 = ∑ a ∈ S, ∑ b ∈ S, ∑ c ∈ S, ∑ d ∈ S,
      Real.cos (((6 * a + 1 : ℤ) : ℝ) * x) * (Real.cos (((6 * b + 1 : ℤ) : ℝ) * x) *
        ((((6 * c + 1 : ℤ) : ℝ) * Real.sin (((6 * c + 1 : ℤ) : ℝ) * x)) *
          (((6 * d + 1 : ℤ) : ℝ) * Real.sin (((6 * d + 1 : ℤ) : ℝ) * x)))) := by
    intro x
    rw [halfC, halfS, sum_sq_mul_sum_sq]
  have hexp2 : ∀ x, halfC S x ^ 4 = ∑ a ∈ S, ∑ b ∈ S, ∑ c ∈ S, ∑ d ∈ S,
      Real.cos (((6 * a + 1 : ℤ) : ℝ) * x) * (Real.cos (((6 * b + 1 : ℤ) : ℝ) * x) *
        (Real.cos (((6 * c + 1 : ℤ) : ℝ) * x) * Real.cos (((6 * d + 1 : ℤ) : ℝ) * x))) := by
    intro x
    rw [halfC, sum_pow_four]
  simp_rw [hexp1, hexp2]
  rw [integral_sum_four, integral_sum_four]
  · simp only [Finset.mul_sum]
    refine Finset.sum_le_sum (fun a _ => Finset.sum_le_sum (fun b _ =>
      Finset.sum_le_sum (fun c hc => Finset.sum_le_sum (fun d hd => ?_))))
    rw [integral_cos_cos_mul_sin_mul_sin, integral_cos_four]
    simp only [cc_diff_sum, cc_sum_diff]
    have hX := cc_nonneg (6 * a + 1 - (6 * b + 1)) (6 * c + 1 - (6 * d + 1))
    have hY := cc_nonneg (6 * a + 1 + (6 * b + 1)) (6 * c + 1 + (6 * d + 1))
    have hbc := hD c hc
    have hbd := hD d hd
    have hprod : |((6 * c + 1 : ℤ) : ℝ) * ((6 * d + 1 : ℤ) : ℝ)| ≤ D ^ 2 := by
      rw [abs_mul, sq]
      exact mul_le_mul hbc hbd (abs_nonneg _) (le_trans (abs_nonneg _) hbc)
    obtain ⟨hp1, hp2⟩ := abs_le.mp hprod
    nlinarith [mul_le_mul_of_nonneg_right hp2 hX, mul_le_mul_of_nonneg_right hp1 hY]
  · intro a b c d
    fun_prop
  · intro a b c d
    fun_prop

/-- **Derivative term.** If `|6s + 1| ≤ D` (`D > 0`) for all `s ∈ S`, then
`∫_0^{2π} |C³ S'| ≤ D ∫_0^{2π} C⁴`. -/
theorem integral_abs_halfC_cube_mul_halfS_le (S : Finset ℤ) (D : ℝ) (hDpos : 0 < D)
    (hD : ∀ s ∈ S, |((6 * s + 1 : ℤ) : ℝ)| ≤ D) :
    ∫ x in (0 : ℝ)..2 * π, |halfC S x ^ 3 * halfS S x| ≤
      D * ∫ x in (0 : ℝ)..2 * π, halfC S x ^ 4 := by
  have hpt : ∀ x, |halfC S x ^ 3 * halfS S x| ≤
      (D * halfC S x ^ 4 + 1 / D * (halfC S x ^ 2 * halfS S x ^ 2)) / 2 := by
    intro x
    set u := halfC S x
    set v := halfS S x
    have h1 : |u ^ 3 * v| = u ^ 2 * |u * v| := by
      rw [show u ^ 3 * v = u ^ 2 * (u * v) by ring, abs_mul, abs_of_nonneg (sq_nonneg u)]
    have h2 : u ^ 2 * v ^ 2 = |u * v| ^ 2 := by rw [sq_abs]; ring
    have h3 : u ^ 4 = (u ^ 2) ^ 2 := by ring
    rw [h1, h2, h3]
    set p := u ^ 2
    set q := |u * v|
    have key : (D * p ^ 2 + 1 / D * q ^ 2) / 2 - p * q = (D * p - q) ^ 2 / (2 * D) := by
      field_simp
      ring
    have : 0 ≤ (D * p - q) ^ 2 / (2 * D) := by positivity
    linarith
  have hc1 : Continuous (fun x => |halfC S x ^ 3 * halfS S x|) :=
    (((continuous_halfC S).pow 3).mul (continuous_halfS S)).abs
  have hc2 : Continuous (fun x => halfC S x ^ 4) := (continuous_halfC S).pow 4
  have hc3 : Continuous (fun x => halfC S x ^ 2 * halfS S x ^ 2) :=
    ((continuous_halfC S).pow 2).mul ((continuous_halfS S).pow 2)
  have hc4 : Continuous (fun x => (D * halfC S x ^ 4 + 1 / D * (halfC S x ^ 2 * halfS S x ^ 2)) / 2) :=
    ((continuous_const.mul hc2).add (continuous_const.mul hc3)).div_const 2
  have hmono : ∫ x in (0 : ℝ)..2 * π, |halfC S x ^ 3 * halfS S x| ≤
      ∫ x in (0 : ℝ)..2 * π, (D * halfC S x ^ 4 + 1 / D * (halfC S x ^ 2 * halfS S x ^ 2)) / 2 :=
    intervalIntegral.integral_mono_on (by positivity : (0 : ℝ) ≤ 2 * π)
      (hc1.intervalIntegrable _ _) (hc4.intervalIntegrable _ _) (fun x _ => hpt x)
  have hi2 : IntervalIntegrable (fun x => D * halfC S x ^ 4) MeasureTheory.volume 0 (2 * π) :=
    (continuous_const.mul hc2).intervalIntegrable _ _
  have hi3 : IntervalIntegrable (fun x => 1 / D * (halfC S x ^ 2 * halfS S x ^ 2))
      MeasureTheory.volume 0 (2 * π) :=
    (continuous_const.mul hc3).intervalIntegrable _ _
  rw [intervalIntegral.integral_div, intervalIntegral.integral_add hi2 hi3,
    intervalIntegral.integral_const_mul, intervalIntegral.integral_const_mul] at hmono
  have hB := integral_halfC_sq_mul_halfS_sq_le S D hD
  have hB' : 1 / D * ∫ x in (0 : ℝ)..2 * π, halfC S x ^ 2 * halfS S x ^ 2 ≤
      D * ∫ x in (0 : ℝ)..2 * π, halfC S x ^ 4 := by
    calc 1 / D * ∫ x in (0 : ℝ)..2 * π, halfC S x ^ 2 * halfS S x ^ 2
        ≤ 1 / D * (D ^ 2 * ∫ x in (0 : ℝ)..2 * π, halfC S x ^ 4) :=
          mul_le_mul_of_nonneg_left hB (by positivity)
      _ = D * ∫ x in (0 : ℝ)..2 * π, halfC S x ^ 4 := by
          field_simp
  linarith

/-- **Gallagher's inequality for `C⁴`.** If `|6s + 1| ≤ D` (`D > 0`) on `S`, `δ₀ > 0`, and the
points `y_0, …, y_{m-1}` satisfy `y_j + δ₀ ≤ y_{j+1}` and
`[y_j - δ₀/2, y_j + δ₀/2] ⊆ [c₀, c₀ + 2π]`, then
`∑_{j<m} C(y_j)⁴ ≤ (1/δ₀ + 4D) ∫_0^{2π} C⁴`. -/
theorem sieve_halfC_pow_four (S : Finset ℤ) (D : ℝ) (hDpos : 0 < D)
    (hD : ∀ s ∈ S, |((6 * s + 1 : ℤ) : ℝ)| ≤ D) {δ0 : ℝ} (hδ0 : 0 < δ0) (c0 : ℝ) (y : ℕ → ℝ)
    (m : ℕ) (hgap : ∀ j, j + 1 < m → y j + δ0 ≤ y (j + 1))
    (hlo : ∀ j < m, c0 ≤ y j - δ0 / 2) (hhi : ∀ j < m, y j + δ0 / 2 ≤ c0 + 2 * π) :
    ∑ j ∈ Finset.range m, halfC S (y j) ^ 4 ≤
      (1 / δ0 + 4 * D) * ∫ x in (0 : ℝ)..2 * π, halfC S x ^ 4 := by
  have hderiv : ∀ x, HasDerivAt (fun x => halfC S x ^ 4) (4 * halfC S x ^ 3 * -halfS S x) x := by
    intro x
    exact ((hasDerivAt_halfC S x).fun_pow 4).congr_deriv (by norm_num)
  have hcont : Continuous (fun x => 4 * halfC S x ^ 3 * -halfS S x) :=
    (continuous_const.mul ((continuous_halfC S).pow 3)).mul (continuous_halfS S).neg
  have hper : Function.Periodic (fun x => halfC S x ^ 4) (2 * π) := fun x => by
    simp only [halfC_periodic S x]
  have hper' : Function.Periodic (fun x => 4 * halfC S x ^ 3 * -halfS S x) (2 * π) := fun x => by
    simp only [halfC_periodic S x, halfS_periodic S x]
  have hG := gallagher_sum hderiv hcont (fun x => by positivity)
    (by positivity : (0 : ℝ) ≤ 2 * π) hper hper' hδ0 c0 y m hgap hlo hhi
  have habs : ∫ x in (0 : ℝ)..2 * π, |4 * halfC S x ^ 3 * -halfS S x| =
      4 * ∫ x in (0 : ℝ)..2 * π, |halfC S x ^ 3 * halfS S x| := by
    rw [← intervalIntegral.integral_const_mul]
    congr 1
    ext x
    rw [show 4 * halfC S x ^ 3 * -halfS S x = -(4 * (halfC S x ^ 3 * halfS S x)) by ring,
      abs_neg, abs_mul, abs_of_pos (by norm_num : (0 : ℝ) < 4)]
  rw [habs] at hG
  have hB := integral_abs_halfC_cube_mul_halfS_le S D hDpos hD
  have e : (1 / δ0 + 4 * D) * ∫ x in (0 : ℝ)..2 * π, halfC S x ^ 4 =
      1 / δ0 * (∫ x in (0 : ℝ)..2 * π, halfC S x ^ 4) +
        4 * (D * ∫ x in (0 : ℝ)..2 * π, halfC S x ^ 4) := by ring
  rw [e]
  linarith

/-! ### Visits and numerics -/

/-- **Visits (explicit).** For a Sidon set `S` and `η > 0` with `38 ≤ η |S|`, with
`h = 64 / (3 η |S|)`, every window `[c - h, c + h]` contains `y` with `|P(y)| < √(η |S| / 2)`. -/
theorem halfP_visit_explicit (S : Finset ℤ) (hS : IsSidon S) (η : ℝ)
    (hx : 38 ≤ η * (S.card : ℝ)) (c : ℝ) :
    ∃ y ∈ Set.Icc (c - 64 / (3 * (η * (S.card : ℝ)))) (c + 64 / (3 * (η * (S.card : ℝ)))),
      |halfP S y| < Real.sqrt (η * S.card / 2) := by
  have hxpos : 0 < η * (S.card : ℝ) := by linarith
  have hh : 0 < 64 / (3 * (η * (S.card : ℝ))) := by positivity
  have hmin : ∑ s ∈ S, min 1 (4 / ((3 * (s : ℝ) + 1 / 2) * (64 / (3 * (η * (S.card : ℝ))))) ^ 2) <
      Real.sqrt (η * S.card / 2) := by
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
  have hsinc : ∑ s ∈ S, Real.sinc ((3 * (s : ℝ) + 1 / 2) *
      (64 / (3 * (η * (S.card : ℝ)))) / 2) ^ 2 < Real.sqrt (η * S.card / 2) := by
    refine lt_of_le_of_lt (Finset.sum_le_sum ?_) hmin
    intro s _
    have hb : 3 * (s : ℝ) + 1 / 2 ≠ 0 := by
      intro h0
      have h6 : ((6 * s + 1 : ℤ) : ℝ) = 0 := by
        push_cast
        linarith
      have : (6 * s + 1 : ℤ) = 0 := by exact_mod_cast h6
      omega
    have hy : (3 * (s : ℝ) + 1 / 2) * (64 / (3 * (η * (S.card : ℝ)))) / 2 ≠ 0 :=
      div_ne_zero (mul_ne_zero hb hh.ne') two_ne_zero
    have e : 1 / ((3 * (s : ℝ) + 1 / 2) * (64 / (3 * (η * (S.card : ℝ)))) / 2) ^ 2 =
        4 / ((3 * (s : ℝ) + 1 / 2) * (64 / (3 * (η * (S.card : ℝ))))) ^ 2 := by
      field_simp
      ring
    rw [← e]
    exact sinc_sq_le_min hy
  exact exists_visit_of_sinc_sum_lt S (fun s => 3 * (s : ℝ) + 1 / 2) _ _ hh hsinc c

/-- Numerical consequences of `600 D ≤ η⁵ k³`, `k² ≤ 2D`, `1 ≤ k`, `0 < η ≤ 1/2`:
`η⁵ k ≥ 300`, `η k ≥ 4800` and `η⁴ k² ≥ 600`. -/
theorem sieve_numerics (η k D : ℝ) (hη : 0 < η) (hη' : η ≤ 1 / 2) (hk1 : 1 ≤ k)
    (hDk : k ^ 2 ≤ 2 * D) (hk : 600 * D ≤ η ^ 5 * k ^ 3) :
    300 ≤ η ^ 5 * k ∧ 4800 ≤ η * k ∧ 600 ≤ η ^ 4 * k ^ 2 := by
  have hkpos : 0 < k := by linarith
  have hE : 300 ≤ η ^ 5 * k := by
    have h1 : 300 * k ^ 2 ≤ (η ^ 5 * k) * k ^ 2 := by nlinarith
    exact le_of_mul_le_mul_right h1 (by positivity)
  have hη4 : η ^ 4 ≤ 1 / 16 := by
    have := pow_le_pow_left₀ hη.le hη' 4
    norm_num at this ⊢
    linarith
  have hxpos : 0 < η * k := by positivity
  have hx5 : η ^ 5 * k = η ^ 4 * (η * k) := by ring
  have hx : 4800 ≤ η * k := by
    have := mul_le_mul_of_nonneg_right hη4 hxpos.le
    linarith
  have hA : 600 ≤ η ^ 4 * k ^ 2 := by
    have h1 : η * (η ^ 4 * k ^ 2) = (η ^ 5 * k) * k := by ring
    have h2 : 300 * k ≤ η * (η ^ 4 * k ^ 2) := by rw [h1]; nlinarith
    have h3 : 0 ≤ η ^ 4 * k ^ 2 := by positivity
    nlinarith [mul_nonneg (sub_nonneg.mpr hη') h3]
  exact ⟨hE, hx, hA⟩

/-- **The final numerical contradiction.** With `h = 64/(3ηk)`, if `m > π/(2h) - 1` and
`m (ηk)⁴ ≤ (1/(2h) + 4D) · 2π · 3k²/4`, then `600 D ≤ η⁵ k³` (with `k² ≤ 2D`, `1 ≤ k`,
`0 < η ≤ 1/2`) is violated. -/
theorem sieve_arith (η k D : ℝ) (m : ℕ) (hη : 0 < η) (hη' : η ≤ 1 / 2) (hk1 : 1 ≤ k)
    (hDk : k ^ 2 ≤ 2 * D) (hk : 600 * D ≤ η ^ 5 * k ^ 3)
    (hm : π / (2 * (64 / (3 * (η * k)))) - 1 < m)
    (hsum : (m : ℝ) * (η * k) ^ 4 ≤
      (1 / (2 * (64 / (3 * (η * k)))) + 4 * D) * (2 * π * (3 * k ^ 2 / 4))) :
    False := by
  obtain ⟨hE, hx4800, hA⟩ := sieve_numerics η k D hη hη' hk1 hDk hk
  have hkpos : 0 < k := by linarith
  have hEx : η ^ 5 * k ^ 3 = (η * k) * (η ^ 4 * k ^ 2) := by ring
  have hx5' : (η * k) ^ 5 = (η ^ 5 * k ^ 3) * k ^ 2 := by ring
  set x := η * k with hx
  have hxpos : 0 < x := by linarith
  have hxne : x ≠ 0 := hxpos.ne'
  have hxE : 600 * x ≤ η ^ 5 * k ^ 3 := by
    rw [hEx]
    nlinarith
  have e1 : π / (2 * (64 / (3 * x))) = 3 * π * x / 128 := by
    field_simp
    ring
  have e2 : 1 / (2 * (64 / (3 * x))) = 3 * x / 128 := by
    field_simp
    ring
  rw [e1] at hm
  rw [e2] at hsum
  have hπ := Real.pi_gt_three
  have hx4pos : 0 < x ^ 4 := by positivity
  have hstep1 : (3 * π * x / 128 - 1) * x ^ 4 < (m : ℝ) * x ^ 4 :=
    mul_lt_mul_of_pos_right hm hx4pos
  have hstep2 : 3 * π / 256 * x ^ 5 ≤ (3 * π * x / 128 - 1) * x ^ 4 := by
    have h1 : 1 ≤ 3 * π * x / 256 := by nlinarith
    have e : (3 * π * x / 128 - 1) * x ^ 4 - 3 * π / 256 * x ^ 5 =
        (3 * π * x / 256 - 1) * x ^ 4 := by ring
    have : 0 ≤ (3 * π * x / 256 - 1) * x ^ 4 := mul_nonneg (by linarith) hx4pos.le
    linarith
  have hstep3 : (3 * x / 128 + 4 * D) * (2 * π * (3 * k ^ 2 / 4)) ≤ 3 * π / 256 * x ^ 5 := by
    have hlin : 9 * x + 1536 * D ≤ 3 * (η ^ 5 * k ^ 3) := by nlinarith [sq_nonneg k]
    have e3 : (3 * x / 128 + 4 * D) * (2 * π * (3 * k ^ 2 / 4)) =
        π * k ^ 2 * (9 * x + 1536 * D) / 256 := by ring
    have e4 : 3 * π / 256 * x ^ 5 = π * k ^ 2 * (3 * (η ^ 5 * k ^ 3)) / 256 := by
      rw [hx5']
      ring
    rw [e3, e4]
    have : 0 ≤ π * k ^ 2 := by positivity
    exact div_le_div_of_nonneg_right (mul_le_mul_of_nonneg_left hlin this) (by norm_num)
  linarith

/-! ### The final theorem -/

/-- **P16′ (rate exponent `1/5`, Gallagher large sieve).** Let `S` be a Sidon set of integers
with `|s| ≤ L` for all `s ∈ S`, `1 ≤ L`, and `0 < η ≤ 1/2`. If `600 (6 L + 1) ≤ η⁵ |S|³`, then
there is a real `x` with `f_{A(S)}(x) < -(1/2 - η) |S|`, i.e. `M(A(S)) > (1/2 - η) |S|`
(here `|A(S)| = |S| (|S| - 1)`). -/
theorem halfSquare_lower_bound_sieve (S : Finset ℤ) (hS : IsSidon S) (L : ℝ)
    (hL : ∀ s ∈ S, |(s : ℝ)| ≤ L) (hL1 : 1 ≤ L) (η : ℝ) (hη : 0 < η) (hη' : η ≤ 1 / 2)
    (hk : 600 * (6 * L + 1) ≤ η ^ 5 * (S.card : ℝ) ^ 3) :
    ∃ x : ℝ, cosSum (buSet S) x < -((1 / 2 - η) * S.card) := by
  have hk0 : (0 : ℝ) ≤ S.card := Nat.cast_nonneg _
  have hsid : (S.card : ℝ) * ((S.card : ℝ) - 1) ≤ 2 * (2 * L) :=
    sidon_card_mul_pred_le_real S hS (2 * L) (by linarith) (fun s hs t ht => by
      have h1 := abs_le.mp (hL s hs)
      have h2 := abs_le.mp (hL t ht)
      linarith [h1.1, h2.2])
  have hkpos : (0 : ℝ) < S.card := by
    rcases hk0.lt_or_eq with h | h
    · exact h
    · exfalso
      rw [← h] at hk
      norm_num at hk
      linarith
  have hk1 : (1 : ℝ) ≤ S.card := by
    have : 0 < S.card := by exact_mod_cast hkpos
    exact_mod_cast this
  have hDk : (S.card : ℝ) ^ 2 ≤ 2 * (6 * L + 1) := by nlinarith
  obtain ⟨-, hx4800, -⟩ := sieve_numerics η S.card (6 * L + 1) hη hη' hk1 hDk hk
  have hx38 : 38 ≤ η * (S.card : ℝ) := by linarith
  by_contra hcon
  push Not at hcon
  have hvisit := halfP_visit_explicit S hS η hx38
  set h : ℝ := 64 / (3 * (η * (S.card : ℝ))) with hh
  have hhpos : 0 < h := by positivity
  choose y hyI hyP using hvisit
  set m : ℕ := ⌊π / (2 * h)⌋₊ with hm
  have hm_le : (m : ℝ) * (2 * h) ≤ π := by
    have := Nat.floor_le (by positivity : (0 : ℝ) ≤ π / (2 * h))
    exact (le_div_iff₀ (by positivity)).mp this
  have hm_gt : π / (2 * h) - 1 < m := by
    have := Nat.lt_floor_add_one (π / (2 * h))
    linarith
  -- depth of `C` at the visits
  have hdepth : ∀ j : ℕ, (η * S.card) ^ 4 < halfC S (y (4 * h * j)) ^ 4 := by
    intro j
    have hP := hyP (4 * h * j)
    have hδsq : Real.sqrt (η * S.card / 2) ^ 2 = η * S.card / 2 := Real.sq_sqrt (by positivity)
    have hP2 : halfP S (y (4 * h * j)) ^ 2 < η * S.card / 2 := by
      rw [← hδsq, ← sq_abs]
      exact pow_lt_pow_left₀ hP (abs_nonneg _) two_ne_zero
    have hid := cosSum_buSet_of_sidon S hS (y (4 * h * j))
    have hf := hcon (y (4 * h * j))
    have h1 : η * S.card < -halfC S (y (4 * h * j)) := by linarith
    have h2 := pow_lt_pow_left₀ h1 (by positivity) (by norm_num : (4 : ℕ) ≠ 0)
    have h3 : (-halfC S (y (4 * h * j))) ^ 4 = halfC S (y (4 * h * j)) ^ 4 := by ring
    linarith
  -- Gallagher on the visits `y (4 h j)`, `j < m`, with `δ₀ = 2h`, `c₀ = -2h`
  have hDpos : (0 : ℝ) < 6 * L + 1 := by linarith
  have hDs : ∀ s ∈ S, |((6 * s + 1 : ℤ) : ℝ)| ≤ 6 * L + 1 := fun s hs => by
    have := abs_le.mp (hL s hs)
    push_cast
    exact abs_le.mpr ⟨by linarith, by linarith⟩
  have hG := sieve_halfC_pow_four S (6 * L + 1) hDpos hDs (δ0 := 2 * h) (by positivity) (-2 * h)
    (fun j => y (4 * h * j)) m
    (fun j _ => by
      have h1 := (hyI (4 * h * j)).2
      have h2 := (hyI (4 * h * ((j + 1 : ℕ) : ℝ))).1
      push_cast at h2 ⊢
      linarith)
    (fun j _ => by
      have h1 := (hyI (4 * h * j)).1
      have hj : (0 : ℝ) ≤ j := Nat.cast_nonneg j
      have : 0 ≤ h * j := mul_nonneg hhpos.le hj
      linarith)
    (fun j hj => by
      have h1 := (hyI (4 * h * j)).2
      have hj' : (j : ℝ) + 1 ≤ m := by exact_mod_cast hj
      have h2 := mul_le_mul_of_nonneg_right hj' (by positivity : (0 : ℝ) ≤ 2 * h)
      linarith)
  have hlow : (m : ℝ) * (η * S.card) ^ 4 ≤ ∑ j ∈ Finset.range m, halfC S (y (4 * h * j)) ^ 4 := by
    have := Finset.sum_le_sum (fun j (_ : j ∈ Finset.range m) => (hdepth j).le)
    rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul] at this
    exact this
  have hmom := integral_halfC_pow_four_le S hS
  have hcoef : 0 ≤ 1 / (2 * h) + 4 * (6 * L + 1) := by positivity
  have hsum : (m : ℝ) * (η * S.card) ^ 4 ≤
      (1 / (2 * h) + 4 * (6 * L + 1)) * (2 * π * (3 * (S.card : ℝ) ^ 2 / 4)) :=
    hlow.trans (hG.trans (mul_le_mul_of_nonneg_left hmom hcoef))
  exact sieve_arith η S.card (6 * L + 1) m hη hη' hk1 hDk hk hm_gt hsum

/-- **P16′, `C · L` version.** Same conclusion as `halfSquare_lower_bound_sieve` under the
hypothesis `4200 L ≤ η⁵ |S|³`. -/
theorem halfSquare_lower_bound_sieve' (S : Finset ℤ) (hS : IsSidon S) (L : ℝ)
    (hL : ∀ s ∈ S, |(s : ℝ)| ≤ L) (hL1 : 1 ≤ L) (η : ℝ) (hη : 0 < η) (hη' : η ≤ 1 / 2)
    (hk : 4200 * L ≤ η ^ 5 * (S.card : ℝ) ^ 3) :
    ∃ x : ℝ, cosSum (buSet S) x < -((1 / 2 - η) * S.card) :=
  halfSquare_lower_bound_sieve S hS L hL hL1 η hη hη' (by linarith)

end ChowlaCosine
