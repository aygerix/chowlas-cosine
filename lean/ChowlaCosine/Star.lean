import ChowlaCosine.Moments

/-!
# The induced-subgraph / star lemma (P9)

Let `A` be a finite set of positive naturals and `M : ℝ` with `-M ≤ f_A(x)` for **every**
real `x`. For every finite `W ⊆ ℤ` and every real weight `v : ℤ → ℝ`,

  `∑_{u,w ∈ W} v_u v_w [|u - w| ∈ A] ≥ -2 M ∑_{u ∈ W} v_u²`.

Proof: with `P(x) = ∑_{u,w ∈ W} v_u v_w cos ((u - w) x) = |∑_u v_u e^{iux}|² ≥ 0`,
`∫_0^{2π} f_A P = π · LHS` and `∫_0^{2π} P = 2π ∑ v_u²`, so
`0 ≤ ∫_0^{2π} (f_A + M) P = π · LHS + 2π M ∑ v_u²`.

**Star corollary.** If `I ⊆ ℤ` is finite, `|i| ∈ A` for every `i ∈ I`, and `|i - j| ∉ A`
for distinct `i, j ∈ I` (i.e. `I` is an independent set in the Cayley graph
`Cay(ℤ, ±A)` contained in the neighbourhood of `0`), then `√|I| / 2 ≤ M`.
(Take `W = {0} ∪ I`, `v_0 = √|I|`, `v_i = -1` on `I`.)
-/

open Real

namespace ChowlaCosine

/-- `∫_0^{2π} cos (a x) cos (m x) dx = π [|m| = a]` for a positive natural `a`, integer `m`. -/
theorem integral_cos_nat_mul_cos_int {a : ℕ} (ha : 0 < a) (m : ℤ) :
    ∫ x in (0 : ℝ)..2 * π, Real.cos ((a : ℝ) * x) * Real.cos ((m : ℝ) * x) =
      if m.natAbs = a then π else 0 := by
  have h := integral_cos_mul_cos (a : ℤ) m 0 0
  simp only [add_zero, sub_zero, Real.cos_zero, mul_one, Int.cast_natCast] at h
  rw [h]
  by_cases hm : m.natAbs = a
  · rw [if_pos hm]
    rcases Int.natAbs_eq m with h1 | h1
    · rw [if_pos (by omega), if_neg (by omega), add_zero]
    · rw [if_neg (by omega), if_pos (by omega), zero_add]
  · rw [if_neg hm, if_neg (by omega), if_neg (by omega), add_zero]

/-- `∫_0^{2π} cos (k x) dx = 2π [k = 0]` for an integer `k`. -/
theorem integral_cos_int_mul' (k : ℤ) :
    ∫ x in (0 : ℝ)..2 * π, Real.cos ((k : ℝ) * x) = if k = 0 then 2 * π else 0 := by
  have h := integral_cos_int_mul_add k 0
  simp only [add_zero, Real.cos_zero, mul_one] at h
  exact h

/-- The real quadratic trigonometric form `P(x) = ∑_{u,w ∈ W} v_u v_w cos ((u - w) x)`,
which equals `|∑_{u ∈ W} v_u e^{iux}|²`. -/
noncomputable def quadTrig (W : Finset ℤ) (v : ℤ → ℝ) (x : ℝ) : ℝ :=
  ∑ u ∈ W, ∑ w ∈ W, v u * v w * Real.cos (((u - w : ℤ) : ℝ) * x)

theorem quadTrig_eq (W : Finset ℤ) (v : ℤ → ℝ) (x : ℝ) :
    quadTrig W v x = (∑ u ∈ W, v u * Real.cos ((u : ℝ) * x)) ^ 2 +
      (∑ u ∈ W, v u * Real.sin ((u : ℝ) * x)) ^ 2 := by
  rw [quadTrig, sq, sq, Finset.sum_mul_sum, Finset.sum_mul_sum, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl (fun u _ => ?_)
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl (fun w _ => ?_)
  have : ((u - w : ℤ) : ℝ) * x = (u : ℝ) * x - (w : ℝ) * x := by push_cast; ring
  rw [this, Real.cos_sub]
  ring

theorem quadTrig_nonneg (W : Finset ℤ) (v : ℤ → ℝ) (x : ℝ) : 0 ≤ quadTrig W v x := by
  rw [quadTrig_eq]
  positivity

theorem continuous_quadTrig (W : Finset ℤ) (v : ℤ → ℝ) : Continuous (quadTrig W v) := by
  unfold quadTrig
  fun_prop

/-- `∫_0^{2π} P = 2π ∑_{u ∈ W} v_u²`. -/
theorem integral_quadTrig (W : Finset ℤ) (v : ℤ → ℝ) :
    ∫ x in (0 : ℝ)..2 * π, quadTrig W v x = 2 * π * ∑ u ∈ W, (v u) ^ 2 := by
  unfold quadTrig
  rw [intervalIntegral.integral_finsetSum (fun (u : ℤ) _ =>
    (by fun_prop : Continuous fun x : ℝ => ∑ w ∈ W,
      v u * v w * Real.cos (((u - w : ℤ) : ℝ) * x)).intervalIntegrable _ _)]
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl (fun u hu => ?_)
  rw [intervalIntegral.integral_finsetSum (fun (w : ℤ) _ =>
    (by fun_prop : Continuous fun x : ℝ =>
      v u * v w * Real.cos (((u - w : ℤ) : ℝ) * x)).intervalIntegrable _ _)]
  have hterm : ∀ w ∈ W, ∫ x in (0 : ℝ)..2 * π, v u * v w * Real.cos (((u - w : ℤ) : ℝ) * x) =
      if u = w then 2 * π * (v u) ^ 2 else 0 := by
    intro w _
    rw [intervalIntegral.integral_const_mul, integral_cos_int_mul']
    by_cases huw : u = w
    · subst huw
      simp only [sub_self, if_true]
      ring
    · rw [if_neg (sub_ne_zero.mpr huw), if_neg huw, mul_zero]
  rw [Finset.sum_congr rfl hterm, Finset.sum_ite_eq, if_pos hu]

/-- `∫_0^{2π} f_A P = π ∑_{u,w ∈ W} v_u v_w [|u - w| ∈ A]` for `A` with positive elements. -/
theorem integral_cosSum_mul_quadTrig (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a)
    (W : Finset ℤ) (v : ℤ → ℝ) :
    ∫ x in (0 : ℝ)..2 * π, cosSum A x * quadTrig W v x =
      π * ∑ u ∈ W, ∑ w ∈ W, v u * v w * (if (u - w).natAbs ∈ A then 1 else 0) := by
  have hexp : ∀ x, cosSum A x * quadTrig W v x = ∑ u ∈ W, ∑ w ∈ W, ∑ a ∈ A,
      v u * v w * (Real.cos ((a : ℝ) * x) * Real.cos (((u - w : ℤ) : ℝ) * x)) := by
    intro x
    rw [cosSum, quadTrig, Finset.mul_sum]
    refine Finset.sum_congr rfl (fun u _ => ?_)
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl (fun w _ => ?_)
    rw [Finset.sum_mul]
    refine Finset.sum_congr rfl (fun a _ => ?_)
    ring
  simp_rw [hexp]
  rw [intervalIntegral.integral_finsetSum (fun (u : ℤ) _ =>
    (by fun_prop : Continuous fun x : ℝ => ∑ w ∈ W, ∑ a ∈ A,
      v u * v w * (Real.cos ((a : ℝ) * x) * Real.cos (((u - w : ℤ) : ℝ) * x))).intervalIntegrable _ _)]
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl (fun u _ => ?_)
  rw [intervalIntegral.integral_finsetSum (fun (w : ℤ) _ =>
    (by fun_prop : Continuous fun x : ℝ => ∑ a ∈ A,
      v u * v w * (Real.cos ((a : ℝ) * x) * Real.cos (((u - w : ℤ) : ℝ) * x))).intervalIntegrable _ _)]
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl (fun w _ => ?_)
  rw [intervalIntegral.integral_finsetSum (fun (a : ℕ) _ =>
    (by fun_prop : Continuous fun x : ℝ =>
      v u * v w * (Real.cos ((a : ℝ) * x) * Real.cos (((u - w : ℤ) : ℝ) * x))).intervalIntegrable _ _)]
  have hterm : ∀ a ∈ A, ∫ x in (0 : ℝ)..2 * π,
      v u * v w * (Real.cos ((a : ℝ) * x) * Real.cos (((u - w : ℤ) : ℝ) * x)) =
      if (u - w).natAbs = a then v u * v w * π else 0 := by
    intro a ha
    rw [intervalIntegral.integral_const_mul, integral_cos_nat_mul_cos_int (hA a ha)]
    split_ifs <;> ring
  rw [Finset.sum_congr rfl hterm, Finset.sum_ite_eq]
  split_ifs <;> ring

/-- **Star lemma (P9).** If `A` is a finite set of positive naturals and `-M ≤ f_A(x)` for
every real `x`, then for every finite `W ⊆ ℤ` and every `v : ℤ → ℝ`,
`∑_{u,w ∈ W} v_u v_w [|u - w| ∈ A] ≥ -2 M ∑_{u ∈ W} v_u²`. -/
theorem star_lemma (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a) (M : ℝ)
    (hM : ∀ x : ℝ, -M ≤ cosSum A x) (W : Finset ℤ) (v : ℤ → ℝ) :
    ∑ u ∈ W, ∑ w ∈ W, v u * v w * (if (u - w).natAbs ∈ A then 1 else 0) ≥
      -2 * M * ∑ u ∈ W, (v u) ^ 2 := by
  have hc := continuous_cosSum A
  have hP := continuous_quadTrig W v
  have hnn : 0 ≤ ∫ x in (0 : ℝ)..2 * π, (cosSum A x + M) * quadTrig W v x := by
    apply intervalIntegral.integral_nonneg (by positivity)
    intro x _
    exact mul_nonneg (by linarith [hM x]) (quadTrig_nonneg W v x)
  have hF : ∀ x, (cosSum A x + M) * quadTrig W v x =
      cosSum A x * quadTrig W v x + M * quadTrig W v x := fun x => by ring
  simp_rw [hF] at hnn
  have hi1 : IntervalIntegrable (fun x => cosSum A x * quadTrig W v x) MeasureTheory.volume
      0 (2 * π) := (hc.mul hP).intervalIntegrable _ _
  have hi2 : IntervalIntegrable (fun x => M * quadTrig W v x) MeasureTheory.volume
      0 (2 * π) := (continuous_const.mul hP).intervalIntegrable _ _
  rw [intervalIntegral.integral_add hi1 hi2, intervalIntegral.integral_const_mul,
    integral_cosSum_mul_quadTrig A hA, integral_quadTrig] at hnn
  have hπ := Real.pi_pos
  set S := ∑ u ∈ W, ∑ w ∈ W, v u * v w * (if (u - w).natAbs ∈ A then 1 else 0)
  set T := ∑ u ∈ W, (v u) ^ 2
  have h2 : 0 ≤ π * (S + 2 * M * T) := by linear_combination hnn
  have h3 := (mul_nonneg_iff_of_pos_left hπ).mp h2
  linarith

/-- A uniform lower-bound hypothesis forces `0 ≤ M` (take `W = {0}` in the star lemma). -/
theorem nonneg_of_cosSum_ge (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a) (M : ℝ)
    (hM : ∀ x : ℝ, -M ≤ cosSum A x) : 0 ≤ M := by
  have h0A : (0 : ℕ) ∉ A := fun h => lt_irrefl 0 (hA 0 h)
  have h := star_lemma A hA M hM {0} (fun _ => 1)
  simp only [Finset.sum_singleton, sub_self, Int.natAbs_zero, if_neg h0A, mul_zero, one_pow,
    mul_one] at h
  linarith

/-- **Star bound (Corollary of P9).** Let `A` be a finite set of positive naturals with
`-M ≤ f_A(x)` for every real `x`. If `I ⊆ ℤ` is finite, `|i| ∈ A` for all `i ∈ I`, and
`|i - j| ∉ A` for all distinct `i, j ∈ I`, then `√|I| / 2 ≤ M`. -/
theorem star_bound (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a) (M : ℝ)
    (hM : ∀ x : ℝ, -M ≤ cosSum A x) (I : Finset ℤ) (hI : ∀ i ∈ I, i.natAbs ∈ A)
    (hIind : ∀ i ∈ I, ∀ j ∈ I, i ≠ j → (i - j).natAbs ∉ A) :
    Real.sqrt I.card / 2 ≤ M := by
  have h0A : (0 : ℕ) ∉ A := fun h => lt_irrefl 0 (hA 0 h)
  have h0I : (0 : ℤ) ∉ I := fun h => h0A (by simpa using hI 0 h)
  have hM0 := nonneg_of_cosSum_ge A hA M hM
  set k : ℕ := I.card with hk_def
  set s : ℝ := Real.sqrt k with hs_def
  have hs : s ^ 2 = k := Real.sq_sqrt (Nat.cast_nonneg _)
  set v : ℤ → ℝ := fun u => if u = 0 then s else -1 with hv_def
  have hne : ∀ u ∈ I, u ≠ 0 := fun u hu h => h0I (h ▸ hu)
  have h := star_lemma A hA M hM (insert 0 I) v
  have hrow0 : ∀ w ∈ I, v 0 * v w * (if ((0 : ℤ) - w).natAbs ∈ A then 1 else 0) = -s := by
    intro w hw
    have h1 : ((0 : ℤ) - w).natAbs ∈ A := by rw [zero_sub, Int.natAbs_neg]; exact hI w hw
    simp only [hv_def, if_pos, if_neg (hne w hw), if_pos h1]
    ring
  have hrow : ∀ u ∈ I, ∑ w ∈ insert 0 I, v u * v w * (if (u - w).natAbs ∈ A then 1 else 0) =
      -s := by
    intro u hu
    rw [Finset.sum_insert h0I]
    have h1 : (u - 0).natAbs ∈ A := by rw [sub_zero]; exact hI u hu
    have h2 : ∑ w ∈ I, v u * v w * (if (u - w).natAbs ∈ A then 1 else 0) = 0 := by
      apply Finset.sum_eq_zero
      intro w hw
      by_cases huw : u = w
      · subst huw
        simp [h0A]
      · simp [hIind u hu w hw huw]
    rw [h2, if_pos h1]
    simp only [hv_def, if_pos, if_neg (hne u hu)]
    ring
  have hL : ∑ u ∈ insert 0 I, ∑ w ∈ insert 0 I, v u * v w *
      (if (u - w).natAbs ∈ A then 1 else 0) = -2 * k * s := by
    rw [Finset.sum_insert h0I, Finset.sum_insert h0I, Finset.sum_congr rfl hrow0,
      Finset.sum_congr rfl hrow]
    have h00 : ((0 : ℤ) - 0).natAbs ∉ A := by simpa using h0A
    rw [if_neg h00]
    simp only [Finset.sum_const, nsmul_eq_mul, ← hk_def]
    ring
  have hR : ∑ u ∈ insert 0 I, (v u) ^ 2 = 2 * k := by
    rw [Finset.sum_insert h0I]
    have : ∀ u ∈ I, (v u) ^ 2 = 1 := by
      intro u hu
      simp only [hv_def, if_neg (hne u hu)]
      norm_num
    rw [Finset.sum_congr rfl this]
    simp only [hv_def, if_pos, Finset.sum_const, nsmul_eq_mul, mul_one, hs, ← hk_def]
    ring
  rw [hL, hR] at h
  rcases Nat.eq_zero_or_pos k with hk | hk
  · have : s = 0 := by rw [hs_def, hk]; simp
    rw [this]
    linarith
  · have hkpos : (0 : ℝ) < k := by exact_mod_cast hk
    nlinarith

end ChowlaCosine
