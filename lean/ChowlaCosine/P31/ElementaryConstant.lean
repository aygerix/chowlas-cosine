import ChowlaCosine.P31.WindowMoments

/-! # Exact elementary constant for P31-E

The integral is bounded by a finite geometric sum and an explicit tail.
Every numerical inequality is proved by rational kernel arithmetic.
-/

open Real MeasureTheory
open scoped BigOperators

namespace ChowlaCosine.P31

noncomputable def elementaryWeight (A : ℝ) : ℝ :=
  (811 / 1000 : ℝ) - (71 / 100 : ℝ) * (1 - 2 * A * (1 - A))

theorem elementaryWeight_pos {A : ℝ} (hA : A ∈ Set.Icc (0 : ℝ) 1) :
    0 < elementaryWeight A := by
  unfold elementaryWeight
  nlinarith [mul_nonneg hA.1 (sub_nonneg.mpr hA.2)]

private theorem integral_centered_even_pow (m : ℕ) :
    (∫ A in (0 : ℝ)..1, (2 * A - 1) ^ (2 * m)) = 1 / (2 * m + 1 : ℝ) := by
  have heq : (fun A : ℝ => (2 * A - 1) ^ (2 * m)) =
      (fun A : ℝ => (2 * A + (-1)) ^ (2 * m)) := by
    funext A
    rw [sub_eq_add_neg]
  rw [heq, intervalIntegral.integral_comp_mul_add (fun t : ℝ => t ^ (2 * m))
    (by norm_num : (2 : ℝ) ≠ 0) (-1), integral_pow]
  simp only [mul_zero, zero_add, mul_one, add_neg_cancel, one_pow, smul_eq_mul]
  have hn : Odd (2 * m + 1) := ⟨m, by omega⟩
  rw [hn.neg_one_pow]
  push_cast
  field_simp
  ring

private theorem elementary_geometric_constant :
    (145 / 228 : ℝ) *
      ((∑ m ∈ Finset.range 32, (355 / 456 : ℝ) ^ m / (2 * m + 1 : ℝ)) +
        (355 / 456 : ℝ) ^ 32 / ((1 - 355 / 456 : ℝ) * 65)) ≤ 1 := by
  norm_num [Finset.sum_range_succ]

private theorem reciprocal_geometric_upper (r s : ℝ) (hr : 0 ≤ r) (hr1 : r < 1)
    (hs : 0 ≤ s) (hs1 : s ≤ 1) (N : ℕ) :
    1 / (1 - r * s) ≤ (∑ m ∈ Finset.range N, r ^ m * s ^ m) +
      r ^ N * s ^ N / (1 - r) := by
  have hq : r * s ≤ r := mul_le_of_le_one_right hr hs1
  have hq1 : 0 < 1 - r * s := by linarith
  have heq : 1 / (1 - r * s) = (∑ m ∈ Finset.range N, (r * s) ^ m) +
      (r * s) ^ N / (1 - r * s) := by
    have hg := geom_sum_mul_neg (r * s) N
    field_simp [hq1.ne']
    nlinarith [hg]
  rw [heq]
  simp only [mul_pow]
  apply add_le_add_right
  exact div_le_div_of_nonneg_left (mul_nonneg (pow_nonneg hr _) (pow_nonneg hs _))
    (sub_pos.mpr hr1) (by linarith)

private noncomputable def elementaryMajorant (A : ℝ) : ℝ :=
  (125 / 57 : ℝ) * ((∑ m ∈ Finset.range 32,
    (355 / 456 : ℝ) ^ m * (2 * A - 1) ^ (2 * m)) +
      (355 / 456 : ℝ) ^ 32 / (1 - 355 / 456 : ℝ) * (2 * A - 1) ^ 64)

private theorem elementaryMajorant_bound {A : ℝ} (hA : A ∈ Set.Icc (0 : ℝ) 1) :
    1 / elementaryWeight A ≤ elementaryMajorant A := by
  have hs : (2 * A - 1) ^ 2 ≤ 1 := by
    nlinarith [mul_nonneg hA.1 (sub_nonneg.mpr hA.2)]
  have hg := reciprocal_geometric_upper (355 / 456 : ℝ) ((2 * A - 1) ^ 2)
    (by norm_num) (by norm_num) (sq_nonneg _) hs 32
  have hw : elementaryWeight A = (57 / 125 : ℝ) *
      (1 - (355 / 456 : ℝ) * (2 * A - 1) ^ 2) := by unfold elementaryWeight; ring
  have hscaled := mul_le_mul_of_nonneg_left hg (by norm_num : (0 : ℝ) ≤ 125 / 57)
  have hleft : 1 / elementaryWeight A =
      (125 / 57 : ℝ) * (1 / (1 - (355 / 456 : ℝ) * (2 * A - 1) ^ 2)) := by
    rw [hw]
    simp only [div_eq_mul_inv, one_mul, mul_inv_rev]
    norm_num
    ring
  have hright : elementaryMajorant A =
      (125 / 57 : ℝ) * ((∑ m ∈ Finset.range 32,
        (355 / 456 : ℝ) ^ m * ((2 * A - 1) ^ 2) ^ m) +
          (355 / 456 : ℝ) ^ 32 * ((2 * A - 1) ^ 2) ^ 32 / (1 - 355 / 456)) := by
    unfold elementaryMajorant
    simp only [← pow_mul]
    ring
  rw [hleft, hright]
  exact hscaled

@[fun_prop] private theorem continuous_elementaryMajorant : Continuous elementaryMajorant := by
  unfold elementaryMajorant
  fun_prop

private theorem integral_elementaryMajorant :
    (29 / 100 : ℝ) * (∫ A in (0 : ℝ)..1, elementaryMajorant A) ≤ 1 := by
  have hi : (∫ A in (0 : ℝ)..1, elementaryMajorant A) =
      (125 / 57 : ℝ) * ((∑ m ∈ Finset.range 32, (355 / 456 : ℝ) ^ m / (2 * m + 1 : ℝ)) +
        (355 / 456 : ℝ) ^ 32 / ((1 - 355 / 456 : ℝ) * 65)) := by
    unfold elementaryMajorant
    rw [intervalIntegral.integral_const_mul,
      intervalIntegral.integral_add (by apply Continuous.intervalIntegrable; fun_prop)
        (by apply Continuous.intervalIntegrable; fun_prop),
      intervalIntegral.integral_finsetSum (by intro m hm; apply Continuous.intervalIntegrable; fun_prop)]
    simp_rw [intervalIntegral.integral_const_mul, integral_centered_even_pow]
    have htail : (∫ A in (0 : ℝ)..1, (2 * A - 1) ^ 64) = (1 / 65 : ℝ) := by
      exact_mod_cast integral_centered_even_pow 32
    rw [htail]
    congr 1
    ring
  rw [hi]
  have hrat : (145 / 228 : ℝ) *
      ((∑ m ∈ Finset.range 32, (355 / 456 : ℝ) ^ m / (2 * m + 1 : ℝ)) +
        (355 / 456 : ℝ) ^ 32 / ((1 - 355 / 456 : ℝ) * 65)) ≤ 1 := by
    exact elementary_geometric_constant
  nlinarith only [hrat]

/-- The exact integral constant required by P31-E, with μ=811/1000 and
λ=71/100. No logarithm, floating point, Riemann-grid approximation, or external solver is used. -/
theorem elementary_integral_constant :
    (1 - 71 / 100 : ℝ) * (∫ A in (0 : ℝ)..1, 1 / elementaryWeight A) ≤ 1 := by
  have hcont : ContinuousOn (fun A : ℝ => 1 / elementaryWeight A) (Set.Icc (0 : ℝ) 1) := by
    apply continuousOn_const.div
      (by unfold elementaryWeight; fun_prop)
    intro A hA
    exact (elementaryWeight_pos hA).ne'
  have hle : (∫ A in (0 : ℝ)..1, 1 / elementaryWeight A) ≤
      ∫ A in (0 : ℝ)..1, elementaryMajorant A := by
    apply intervalIntegral.integral_mono_on (by norm_num)
      (hcont.intervalIntegrable_of_Icc (by norm_num))
      (continuous_elementaryMajorant.intervalIntegrable _ _)
    intro A hA
    exact elementaryMajorant_bound hA
  have hh := mul_le_mul_of_nonneg_left hle (by norm_num : (0 : ℝ) ≤ 29 / 100)
  have hresult := hh.trans integral_elementaryMajorant
  norm_num only [show (1 - 71 / 100 : ℝ) = 29 / 100 by norm_num]
  exact hresult

noncomputable def elementaryCellWeight (a b : ℝ) : ℝ :=
  (811 / 1000 - 71 / 100 : ℝ) + (71 / 100 : ℝ) * (a * (1 - a) + b * (1 - b)) +
    (71 / 300 : ℝ) * (b - a) ^ 2

theorem elementaryCellWeight_pos {a b : ℝ}
    (ha : a ∈ Set.Icc (0 : ℝ) 1) (hb : b ∈ Set.Icc (0 : ℝ) 1) :
    0 < elementaryCellWeight a b := by
  unfold elementaryCellWeight
  nlinarith [mul_nonneg ha.1 (sub_nonneg.mpr ha.2),
    mul_nonneg hb.1 (sub_nonneg.mpr hb.2), sq_nonneg (b - a)]

/-- Exact quadratic trapezoid identity, including a cell of length zero. -/
theorem integral_elementaryWeight (a b : ℝ) :
    (∫ A in a..b, elementaryWeight A) = (b - a) * elementaryCellWeight a b := by
  have heq : elementaryWeight = fun A : ℝ =>
      (101 / 1000 : ℝ) + (71 / 50 : ℝ) * A - (71 / 50 : ℝ) * A ^ 2 := by
    funext A
    unfold elementaryWeight
    ring
  rw [heq, intervalIntegral.integral_sub (by apply Continuous.intervalIntegrable; fun_prop)
      (by apply Continuous.intervalIntegrable; fun_prop),
    intervalIntegral.integral_add (by apply Continuous.intervalIntegrable; fun_prop)
        (by apply Continuous.intervalIntegrable; fun_prop)]
  rw [intervalIntegral.integral_const_mul (71 / 50 : ℝ) (fun A : ℝ => A),
    intervalIntegral.integral_const_mul (71 / 50 : ℝ) (fun A : ℝ => A ^ 2)]
  simp only [intervalIntegral.integral_const, integral_id, integral_pow, smul_eq_mul]
  unfold elementaryCellWeight
  ring

/-- Cellwise inverse-weight Cauchy–Schwarz, proved by integrating a
nonnegative square. Zero-length cells are allowed. -/
theorem elementary_cell_reciprocal_bound {a b : ℝ}
    (ha : 0 ≤ a) (hab : a ≤ b) (hb : b ≤ 1) :
    (b - a) / elementaryCellWeight a b ≤
      ∫ A in a..b, 1 / elementaryWeight A := by
  have haI : a ∈ Set.Icc (0 : ℝ) 1 := ⟨ha, hab.trans hb⟩
  have hbI : b ∈ Set.Icc (0 : ℝ) 1 := ⟨ha.trans hab, hb⟩
  let d := elementaryCellWeight a b
  have hd : 0 < d := elementaryCellWeight_pos haI hbI
  have hcont : ContinuousOn (fun A : ℝ => 1 / elementaryWeight A) (Set.Icc a b) := by
    apply continuousOn_const.div (by unfold elementaryWeight; fun_prop)
    intro A hA
    exact (elementaryWeight_pos ⟨ha.trans hA.1, hA.2.trans hb⟩).ne'
  have hint : IntervalIntegrable (fun A : ℝ => 1 / elementaryWeight A) volume a b :=
    hcont.intervalIntegrable_of_Icc hab
  have hpt : ∀ A ∈ Set.Icc a b,
      2 * d ≤ elementaryWeight A + d ^ 2 * (1 / elementaryWeight A) := by
    intro A hA
    have hD := elementaryWeight_pos ⟨ha.trans hA.1, hA.2.trans hb⟩
    apply (mul_le_mul_iff_right₀ hD).mp
    field_simp
    nlinarith [sq_nonneg (elementaryWeight A - d)]
  have hI : (∫ A in a..b, 2 * d) ≤
      ∫ A in a..b, elementaryWeight A + d ^ 2 * (1 / elementaryWeight A) := by
    exact intervalIntegral.integral_mono_on hab (by apply Continuous.intervalIntegrable; fun_prop)
      ((by unfold elementaryWeight; fun_prop : Continuous elementaryWeight).intervalIntegrable _ _ |>.add
        (hint.const_mul (d ^ 2))) hpt
  rw [intervalIntegral.integral_const, smul_eq_mul,
    intervalIntegral.integral_add
      ((by unfold elementaryWeight; fun_prop : Continuous elementaryWeight).intervalIntegrable _ _)
      (hint.const_mul (d ^ 2)), intervalIntegral.integral_const_mul,
    integral_elementaryWeight] at hI
  apply (div_le_iff₀ hd).mpr
  have hcancel : d * (b - a) ≤ d * (d * (∫ A in a..b, 1 / elementaryWeight A)) := by
    change _ ≤ _
    dsimp only [d] at hI ⊢
    nlinarith [hI]
  have hfinal := (mul_le_mul_iff_right₀ hd).mp hcancel
  simpa only [mul_comm] using hfinal

/-- Finite weighted Cauchy–Schwarz and the exact integral certificate
close the variational part of P31-E. The two convolution estimates E1/E2
remain explicit hypotheses of this intermediate theorem. -/
theorem elementary_bound_of_two_estimates (N : ℕ) (v a : ℕ → ℝ) (E : ℝ)
    (ha0 : a 0 = 0) (haN : a N = 1)
    (habounds : ∀ j ≤ N, a j ∈ Set.Icc (0 : ℝ) 1)
    (hdiff : ∀ j < N, a (j + 1) - a j = v j ^ 2)
    (hv : ∑ j ∈ Finset.range N, v j ^ 2 = 1)
    (hE1 : E ≤ (N : ℝ) - ∑ j ∈ Finset.range N,
      (a j * (1 - a j) + a (j + 1) * (1 - a (j + 1))))
    (hE2 : E ≤ (∑ j ∈ Finset.range N, v j) ^ 2) :
    E ≤ (811 / 1000 : ℝ) * N + 71 / 300 := by
  let d : ℕ → ℝ := fun j => elementaryCellWeight (a j) (a (j + 1))
  have hd : ∀ j ∈ Finset.range N, 0 < d j := by
    intro j hj
    have hjN : j < N := Finset.mem_range.mp hj
    exact elementaryCellWeight_pos (habounds j hjN.le) (habounds (j + 1) hjN)
  have hD : 0 ≤ ∑ j ∈ Finset.range N, d j := Finset.sum_nonneg (fun j hj => (hd j hj).le)
  have hcs : (∑ j ∈ Finset.range N, v j) ^ 2 ≤
      (∑ j ∈ Finset.range N, d j) * (∑ j ∈ Finset.range N, v j ^ 2 / d j) := by
    apply Finset.sum_sq_le_sum_mul_sum_of_sq_le_mul
      (Finset.range N) (r := v) (f := d) (g := fun j => v j ^ 2 / d j)
      (fun j hj => (hd j hj).le)
      (fun j hj => div_nonneg (sq_nonneg _) (hd j hj).le)
    intro j hj
    rw [mul_div_cancel₀ _ (hd j hj).ne']
  have hcells : (∑ j ∈ Finset.range N, v j ^ 2 / d j) ≤
      ∫ A in (0 : ℝ)..1, 1 / elementaryWeight A := by
    calc
      _ ≤ ∑ j ∈ Finset.range N, ∫ A in a j..a (j + 1), 1 / elementaryWeight A := by
        apply Finset.sum_le_sum
        intro j hj
        have hjN : j < N := Finset.mem_range.mp hj
        rw [← hdiff j hjN]
        apply elementary_cell_reciprocal_bound (habounds j hjN.le).1
          (by rw [← sub_nonneg, hdiff j hjN]; exact sq_nonneg _) (habounds (j + 1) hjN).2
      _ = _ := by
        rw [intervalIntegral.sum_integral_adjacent_intervals, ha0, haN]
        intro j hj
        apply ContinuousOn.intervalIntegrable_of_Icc
          (by rw [← sub_nonneg, hdiff j hj]; exact sq_nonneg _)
        apply continuousOn_const.div (by unfold elementaryWeight; fun_prop)
        intro A hA
        exact (elementaryWeight_pos
          ⟨(habounds j hj.le).1.trans hA.1, hA.2.trans (habounds (j + 1) hj).2⟩).ne'
  have hweighted : (29 / 100 : ℝ) * (∑ j ∈ Finset.range N, v j) ^ 2 ≤
      ∑ j ∈ Finset.range N, d j := by
    calc
      _ ≤ (29 / 100 : ℝ) * ((∑ j ∈ Finset.range N, d j) *
          (∑ j ∈ Finset.range N, v j ^ 2 / d j)) := mul_le_mul_of_nonneg_left hcs (by norm_num)
      _ ≤ (∑ j ∈ Finset.range N, d j) *
          ((29 / 100 : ℝ) * (∫ A in (0 : ℝ)..1, 1 / elementaryWeight A)) := by
        have hle := mul_le_mul_of_nonneg_left hcells
          (mul_nonneg (by norm_num : (0 : ℝ) ≤ 29 / 100) hD)
        nlinarith [hle]
      _ ≤ _ := by
        have hc : (29 / 100 : ℝ) * (∫ A in (0 : ℝ)..1, 1 / elementaryWeight A) ≤ 1 := by
          convert elementary_integral_constant using 1 <;> norm_num
        simpa only [mul_one] using mul_le_mul_of_nonneg_left hc hD
  have hp4 : (∑ j ∈ Finset.range N, (v j ^ 2) ^ 2) ≤ 1 := by
    calc
      _ ≤ ∑ j ∈ Finset.range N, v j ^ 2 := by
        apply Finset.sum_le_sum
        intro j hj
        have hle := Finset.single_le_sum (fun k hk => sq_nonneg (v k)) hj
        rw [hv] at hle
        nlinarith [sq_nonneg (v j)]
      _ = _ := hv
  have hdiffsq : (∑ j ∈ Finset.range N, (a (j + 1) - a j) ^ 2) =
      ∑ j ∈ Finset.range N, (v j ^ 2) ^ 2 := by
    apply Finset.sum_congr rfl
    intro j hj
    rw [hdiff j (Finset.mem_range.mp hj)]
  have hdsum : (∑ j ∈ Finset.range N, d j) =
      (101 / 1000 : ℝ) * N + (71 / 100 : ℝ) *
        (∑ j ∈ Finset.range N, (a j * (1 - a j) + a (j + 1) * (1 - a (j + 1)))) +
          (71 / 300 : ℝ) * (∑ j ∈ Finset.range N, (v j ^ 2) ^ 2) := by
    simp only [d, elementaryCellWeight, Finset.sum_add_distrib,
      Finset.sum_const, Finset.card_range, nsmul_eq_mul, ← Finset.mul_sum, hdiffsq]
    ring
  rw [hdsum] at hweighted
  nlinarith [hweighted, hE1, hE2, hp4]

end ChowlaCosine.P31
