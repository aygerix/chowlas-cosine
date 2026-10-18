import ChowlaCosine.Star

/-!
# Multiplicity bound for square certificates (P8), integer-frequency version

Let `A` be a finite set of positive naturals. Suppose that for **every** real `x`

  `λ + f_A(x) = |Q(x)|² - h(x)`,   `Q(x) = ∑_{β ∈ B} q_β e^{iβx}`,
  `h(x) = ∑_{g ∈ G} c_g cos (g x)`,

where `B, G ⊆ ℤ` are finite, `q : ℤ → ℂ`, `c : ℤ → ℝ`, and every `g ∈ G` satisfies
`g ≠ 0` and `|g| ∉ A` (`h` has no constant term and no frequency in `±A`; no sign condition
on `h` is assumed). If `m` bounds the representation counts
`#{β ∈ B : β - g ∈ B} ≤ m` for every `g` with `|g| ∈ A` (in particular if it bounds them for
every `g ≠ 0`), then

  `|A| ≤ 2 m λ²`.

Proof outline (all real-variable; `R(β,β') = Re (q_β conj q_β')`):
* `|Q(x)|² = ∑_{β,β'} (R(β,β') cos ((β-β')x) + S(β,β') sin ((β-β')x))`;
* integrating the identity against `1` gives `λ = ∑_β |q_β|²`;
* integrating against `cos (a x)`, `a ∈ A`, gives `∑_{|β-β'| = a} R(β,β') = 1`;
* `R(β,β') ≤ |q_β| |q_β'|`, Cauchy–Schwarz, and `#{(β,β') ∈ B² : |β-β'| = a} ≤ 2m` give
  `1 ≤ 2m ∑_{|β-β'| = a} |q_β|² |q_β'|²`;
* summing over `a ∈ A` (the pair sets are disjoint) gives `|A| ≤ 2m (∑ |q_β|²)² = 2m λ²`.
-/

open Real

namespace ChowlaCosine

/-- `Rp q β β' = Re (q_β · conj q_β')`. -/
noncomputable def Rp (q : ℤ → ℂ) (β β' : ℤ) : ℝ := (q β).re * (q β').re + (q β).im * (q β').im

/-- `Sp q β β' = -Im (q_β · conj q_β') = Re q_β Im q_β' - Im q_β Re q_β'`. -/
noncomputable def Sp (q : ℤ → ℂ) (β β' : ℤ) : ℝ := (q β).re * (q β').im - (q β).im * (q β').re

/-- The real trigonometric form of `|∑_{β ∈ B} q_β e^{iβx}|²`. -/
noncomputable def sqTrig (B : Finset ℤ) (q : ℤ → ℂ) (x : ℝ) : ℝ :=
  ∑ β ∈ B, ∑ β' ∈ B, (Rp q β β' * Real.cos (((β - β' : ℤ) : ℝ) * x) +
    Sp q β β' * Real.sin (((β - β' : ℤ) : ℝ) * x))

/-- The error term `h(x) = ∑_{g ∈ G} c_g cos (g x)`. -/
noncomputable def hTrig (G : Finset ℤ) (c : ℤ → ℝ) (x : ℝ) : ℝ :=
  ∑ g ∈ G, c g * Real.cos ((g : ℝ) * x)

theorem continuous_sqTrig (B : Finset ℤ) (q : ℤ → ℂ) : Continuous (sqTrig B q) := by
  unfold sqTrig
  fun_prop

theorem continuous_hTrig (G : Finset ℤ) (c : ℤ → ℝ) : Continuous (hTrig G c) := by
  unfold hTrig
  fun_prop

theorem Rp_self (q : ℤ → ℂ) (β : ℤ) : Rp q β β = ‖q β‖ ^ 2 := by
  rw [Rp, Complex.sq_norm, Complex.normSq_apply]

theorem Rp_le (q : ℤ → ℂ) (β β' : ℤ) : Rp q β β' ≤ ‖q β‖ * ‖q β'‖ := by
  have h := Complex.re_le_norm (q β * (starRingEnd ℂ) (q β'))
  rw [Complex.mul_re, Complex.conj_re, Complex.conj_im, norm_mul, Complex.norm_conj] at h
  rw [Rp]
  linarith

/-- `‖∑_{β ∈ B} q_β e^{iβx}‖² = sqTrig B q x` for every real `x`. -/
theorem norm_sq_eq_sqTrig (B : Finset ℤ) (q : ℤ → ℂ) (x : ℝ) :
    ‖∑ β ∈ B, q β * Complex.exp ((β : ℂ) * (x : ℂ) * Complex.I)‖ ^ 2 = sqTrig B q x := by
  have hpt : ∀ b : ℤ, (b : ℂ) * (x : ℂ) * Complex.I = (((b : ℝ) * x : ℝ) : ℂ) * Complex.I := by
    intro b
    push_cast
    ring
  have hre : (∑ β ∈ B, q β * Complex.exp ((β : ℂ) * (x : ℂ) * Complex.I)).re =
      ∑ β ∈ B, ((q β).re * Real.cos ((β : ℝ) * x) - (q β).im * Real.sin ((β : ℝ) * x)) := by
    rw [Complex.re_sum]
    refine Finset.sum_congr rfl (fun b _ => ?_)
    rw [hpt, Complex.mul_re, Complex.exp_ofReal_mul_I_re, Complex.exp_ofReal_mul_I_im]
  have him : (∑ β ∈ B, q β * Complex.exp ((β : ℂ) * (x : ℂ) * Complex.I)).im =
      ∑ β ∈ B, ((q β).re * Real.sin ((β : ℝ) * x) + (q β).im * Real.cos ((β : ℝ) * x)) := by
    rw [Complex.im_sum]
    refine Finset.sum_congr rfl (fun b _ => ?_)
    rw [hpt, Complex.mul_im, Complex.exp_ofReal_mul_I_re, Complex.exp_ofReal_mul_I_im]
  rw [Complex.sq_norm, Complex.normSq_apply, hre, him, Finset.sum_mul_sum, Finset.sum_mul_sum,
    ← Finset.sum_add_distrib, sqTrig]
  refine Finset.sum_congr rfl (fun b _ => ?_)
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl (fun b' _ => ?_)
  have : ((b - b' : ℤ) : ℝ) * x = (b : ℝ) * x - (b' : ℝ) * x := by push_cast; ring
  rw [this, Real.cos_sub, Real.sin_sub, Rp, Sp]
  ring

/-- `∫_0^{2π} sin (k x) cos (a x) dx = 0` for all integers `k` and naturals `a`. -/
theorem integral_sin_int_mul_cos_nat (k : ℤ) (a : ℕ) :
    ∫ x in (0 : ℝ)..2 * π, Real.sin ((k : ℝ) * x) * Real.cos ((a : ℝ) * x) = 0 := by
  have h := integral_cos_mul_cos k (a : ℤ) (-(π / 2)) 0
  have hpt : ∀ y : ℝ, Real.sin ((k : ℝ) * y) * Real.cos ((a : ℝ) * y) =
      Real.cos ((k : ℝ) * y + -(π / 2)) * Real.cos (((a : ℤ) : ℝ) * y + 0) := by
    intro y
    rw [← sub_eq_add_neg, Real.cos_sub_pi_div_two, add_zero, Int.cast_natCast]
  simp_rw [hpt]
  rw [h]
  simp [Real.cos_neg, Real.cos_pi_div_two]

/-- `∫_0^{2π} |Q|² cos (a x) dx = π ∑_{(β,β') ∈ B², |β - β'| = a} Re (q_β conj q_β')`. -/
theorem integral_sqTrig_mul_cos (B : Finset ℤ) (q : ℤ → ℂ) {a : ℕ} (ha : 0 < a) :
    ∫ x in (0 : ℝ)..2 * π, sqTrig B q x * Real.cos ((a : ℝ) * x) =
      π * ∑ β ∈ B, ∑ β' ∈ B, (if (β - β').natAbs = a then Rp q β β' else 0) := by
  have hexp : ∀ x, sqTrig B q x * Real.cos ((a : ℝ) * x) = ∑ β ∈ B, ∑ β' ∈ B,
      (Rp q β β' * (Real.cos ((a : ℝ) * x) * Real.cos (((β - β' : ℤ) : ℝ) * x)) +
        Sp q β β' * (Real.sin (((β - β' : ℤ) : ℝ) * x) * Real.cos ((a : ℝ) * x))) := by
    intro x
    rw [sqTrig, Finset.sum_mul]
    refine Finset.sum_congr rfl (fun β _ => ?_)
    rw [Finset.sum_mul]
    refine Finset.sum_congr rfl (fun β' _ => ?_)
    ring
  simp_rw [hexp]
  rw [intervalIntegral.integral_finsetSum (fun (β : ℤ) _ =>
    (by fun_prop : Continuous fun x : ℝ => ∑ β' ∈ B,
      (Rp q β β' * (Real.cos ((a : ℝ) * x) * Real.cos (((β - β' : ℤ) : ℝ) * x)) +
        Sp q β β' * (Real.sin (((β - β' : ℤ) : ℝ) * x) * Real.cos ((a : ℝ) * x)))).intervalIntegrable
      _ _)]
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl (fun β _ => ?_)
  rw [intervalIntegral.integral_finsetSum (fun (β' : ℤ) _ =>
    (by fun_prop : Continuous fun x : ℝ =>
      (Rp q β β' * (Real.cos ((a : ℝ) * x) * Real.cos (((β - β' : ℤ) : ℝ) * x)) +
        Sp q β β' * (Real.sin (((β - β' : ℤ) : ℝ) * x) * Real.cos ((a : ℝ) * x)))).intervalIntegrable
      _ _)]
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl (fun β' _ => ?_)
  have hi1 : IntervalIntegrable (fun x : ℝ =>
      Rp q β β' * (Real.cos ((a : ℝ) * x) * Real.cos (((β - β' : ℤ) : ℝ) * x)))
      MeasureTheory.volume 0 (2 * π) :=
    (by fun_prop : Continuous fun x : ℝ =>
      Rp q β β' * (Real.cos ((a : ℝ) * x) * Real.cos (((β - β' : ℤ) : ℝ) * x))).intervalIntegrable
      _ _
  have hi2 : IntervalIntegrable (fun x : ℝ =>
      Sp q β β' * (Real.sin (((β - β' : ℤ) : ℝ) * x) * Real.cos ((a : ℝ) * x)))
      MeasureTheory.volume 0 (2 * π) :=
    (by fun_prop : Continuous fun x : ℝ =>
      Sp q β β' * (Real.sin (((β - β' : ℤ) : ℝ) * x) * Real.cos ((a : ℝ) * x))).intervalIntegrable
      _ _
  rw [intervalIntegral.integral_add hi1 hi2, intervalIntegral.integral_const_mul,
    intervalIntegral.integral_const_mul, integral_cos_nat_mul_cos_int ha,
    integral_sin_int_mul_cos_nat]
  split_ifs <;> ring

/-- `∫_0^{2π} |Q|² dx = 2π ∑_{β ∈ B} Re (q_β conj q_β)`. -/
theorem integral_sqTrig (B : Finset ℤ) (q : ℤ → ℂ) :
    ∫ x in (0 : ℝ)..2 * π, sqTrig B q x = 2 * π * ∑ β ∈ B, Rp q β β := by
  unfold sqTrig
  rw [intervalIntegral.integral_finsetSum (fun (β : ℤ) _ =>
    (by fun_prop : Continuous fun x : ℝ => ∑ β' ∈ B,
      (Rp q β β' * Real.cos (((β - β' : ℤ) : ℝ) * x) +
        Sp q β β' * Real.sin (((β - β' : ℤ) : ℝ) * x))).intervalIntegrable _ _)]
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl (fun β hβ => ?_)
  rw [intervalIntegral.integral_finsetSum (fun (β' : ℤ) _ =>
    (by fun_prop : Continuous fun x : ℝ =>
      (Rp q β β' * Real.cos (((β - β' : ℤ) : ℝ) * x) +
        Sp q β β' * Real.sin (((β - β' : ℤ) : ℝ) * x))).intervalIntegrable _ _)]
  have hterm : ∀ β' ∈ B, ∫ x in (0 : ℝ)..2 * π,
      (Rp q β β' * Real.cos (((β - β' : ℤ) : ℝ) * x) +
        Sp q β β' * Real.sin (((β - β' : ℤ) : ℝ) * x)) =
      if β = β' then 2 * π * Rp q β β else 0 := by
    intro β' _
    have hi1 : IntervalIntegrable (fun x : ℝ => Rp q β β' * Real.cos (((β - β' : ℤ) : ℝ) * x))
        MeasureTheory.volume 0 (2 * π) :=
      (by fun_prop : Continuous fun x : ℝ =>
        Rp q β β' * Real.cos (((β - β' : ℤ) : ℝ) * x)).intervalIntegrable _ _
    have hi2 : IntervalIntegrable (fun x : ℝ => Sp q β β' * Real.sin (((β - β' : ℤ) : ℝ) * x))
        MeasureTheory.volume 0 (2 * π) :=
      (by fun_prop : Continuous fun x : ℝ =>
        Sp q β β' * Real.sin (((β - β' : ℤ) : ℝ) * x)).intervalIntegrable _ _
    rw [intervalIntegral.integral_add hi1 hi2, intervalIntegral.integral_const_mul,
      intervalIntegral.integral_const_mul, integral_cos_int_mul', integral_sin_int_mul]
    by_cases h : β = β'
    · subst h
      rw [if_pos (sub_self β), if_pos rfl]
      ring
    · rw [if_neg (sub_ne_zero.mpr h), if_neg h]
      ring
  rw [Finset.sum_congr rfl hterm, Finset.sum_ite_eq, if_pos hβ]

/-- `∫_0^{2π} h(x) cos (a x) dx = 0` if no frequency of `h` has absolute value `a > 0`. -/
theorem integral_hTrig_mul_cos (G : Finset ℤ) (c : ℤ → ℝ) {a : ℕ} (ha : 0 < a)
    (hG : ∀ g ∈ G, g.natAbs ≠ a) :
    ∫ x in (0 : ℝ)..2 * π, hTrig G c x * Real.cos ((a : ℝ) * x) = 0 := by
  have hexp : ∀ x, hTrig G c x * Real.cos ((a : ℝ) * x) =
      ∑ g ∈ G, c g * (Real.cos ((a : ℝ) * x) * Real.cos ((g : ℝ) * x)) := by
    intro x
    rw [hTrig, Finset.sum_mul]
    exact Finset.sum_congr rfl (fun g _ => by ring)
  simp_rw [hexp]
  rw [intervalIntegral.integral_finsetSum (fun (g : ℤ) _ =>
    (by fun_prop : Continuous fun x : ℝ =>
      c g * (Real.cos ((a : ℝ) * x) * Real.cos ((g : ℝ) * x))).intervalIntegrable _ _)]
  refine Finset.sum_eq_zero (fun g hg => ?_)
  rw [intervalIntegral.integral_const_mul, integral_cos_nat_mul_cos_int ha, if_neg (hG g hg),
    mul_zero]

/-- `∫_0^{2π} h = 0` if `h` has no constant term. -/
theorem integral_hTrig (G : Finset ℤ) (c : ℤ → ℝ) (hG : ∀ g ∈ G, g ≠ 0) :
    ∫ x in (0 : ℝ)..2 * π, hTrig G c x = 0 := by
  unfold hTrig
  rw [intervalIntegral.integral_finsetSum (fun (g : ℤ) _ =>
    (by fun_prop : Continuous fun x : ℝ => c g * Real.cos ((g : ℝ) * x)).intervalIntegrable _ _)]
  refine Finset.sum_eq_zero (fun g hg => ?_)
  rw [intervalIntegral.integral_const_mul, integral_cos_int_mul (hG g hg), mul_zero]

/-- `∫_0^{2π} f_A(x) cos (a x) dx = π` for `a ∈ A` (all elements of `A` positive). -/
theorem integral_cosSum_mul_cos (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a) {a : ℕ} (ha : a ∈ A) :
    ∫ x in (0 : ℝ)..2 * π, cosSum A x * Real.cos ((a : ℝ) * x) = π := by
  have hexp : ∀ x, cosSum A x * Real.cos ((a : ℝ) * x) =
      ∑ b ∈ A, Real.cos ((b : ℝ) * x) * Real.cos ((a : ℝ) * x) := by
    intro x
    rw [cosSum, Finset.sum_mul]
  simp_rw [hexp]
  rw [intervalIntegral.integral_finsetSum (fun (b : ℕ) _ =>
    (by fun_prop : Continuous fun x : ℝ =>
      Real.cos ((b : ℝ) * x) * Real.cos ((a : ℝ) * x)).intervalIntegrable _ _)]
  rw [Finset.sum_congr rfl (fun b hb => integral_cos_mul_cos_nat (hA b hb) (hA a ha)),
    Finset.sum_ite_eq', if_pos ha]

/-- From the certificate identity: the constant `λ` equals `∑_{β ∈ B} |q_β|²`
(in particular `λ ≥ 0`). -/
theorem lam_eq_of_sq_certificate (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a)
    (B : Finset ℤ) (q : ℤ → ℂ) (lam : ℝ) (G : Finset ℤ) (c : ℤ → ℝ)
    (hG : ∀ g ∈ G, g ≠ 0 ∧ g.natAbs ∉ A)
    (hid : ∀ x : ℝ, lam + cosSum A x =
      ‖∑ β ∈ B, q β * Complex.exp ((β : ℂ) * (x : ℂ) * Complex.I)‖ ^ 2 -
        ∑ g ∈ G, c g * Real.cos ((g : ℝ) * x)) :
    lam = ∑ β ∈ B, ‖q β‖ ^ 2 := by
  have hx : ∀ x, sqTrig B q x = lam + cosSum A x + hTrig G c x := by
    intro x
    rw [← norm_sq_eq_sqTrig, hTrig]
    linarith [hid x]
  have h1 := integral_sqTrig B q
  simp_rw [hx] at h1
  have hc := continuous_cosSum A
  have hh := continuous_hTrig G c
  have hi1 : IntervalIntegrable (fun x => lam + cosSum A x) MeasureTheory.volume 0 (2 * π) :=
    (continuous_const.add hc).intervalIntegrable _ _
  have hi2 : IntervalIntegrable (fun x => hTrig G c x) MeasureTheory.volume 0 (2 * π) :=
    hh.intervalIntegrable _ _
  have hi3 : IntervalIntegrable (fun _ : ℝ => lam) MeasureTheory.volume 0 (2 * π) :=
    continuous_const.intervalIntegrable _ _
  have hi4 : IntervalIntegrable (fun x => cosSum A x) MeasureTheory.volume 0 (2 * π) :=
    hc.intervalIntegrable _ _
  rw [intervalIntegral.integral_add hi1 hi2, intervalIntegral.integral_add hi3 hi4,
    intervalIntegral.integral_const, integral_cosSum A hA,
    integral_hTrig G c (fun g hg => (hG g hg).1)] at h1
  simp only [sub_zero, smul_eq_mul, add_zero] at h1
  have hπ : (2 * π) ≠ 0 := by positivity
  rw [Finset.sum_congr rfl (fun β _ => (Rp_self q β).symm)]
  exact mul_left_cancel₀ hπ h1

/-- From the certificate identity: for every `a ∈ A`,
`∑_{(β,β') ∈ B², |β - β'| = a} Re (q_β conj q_β') = 1`. -/
theorem coeff_eq_one_of_sq_certificate (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a)
    (B : Finset ℤ) (q : ℤ → ℂ) (lam : ℝ) (G : Finset ℤ) (c : ℤ → ℝ)
    (hG : ∀ g ∈ G, g ≠ 0 ∧ g.natAbs ∉ A)
    (hid : ∀ x : ℝ, lam + cosSum A x =
      ‖∑ β ∈ B, q β * Complex.exp ((β : ℂ) * (x : ℂ) * Complex.I)‖ ^ 2 -
        ∑ g ∈ G, c g * Real.cos ((g : ℝ) * x))
    {a : ℕ} (ha : a ∈ A) :
    ∑ β ∈ B, ∑ β' ∈ B, (if (β - β').natAbs = a then Rp q β β' else 0) = 1 := by
  have hx : ∀ x, sqTrig B q x * Real.cos ((a : ℝ) * x) =
      lam * Real.cos ((a : ℝ) * x) + cosSum A x * Real.cos ((a : ℝ) * x) +
        hTrig G c x * Real.cos ((a : ℝ) * x) := by
    intro x
    have hx' : sqTrig B q x = lam + cosSum A x + hTrig G c x := by
      rw [← norm_sq_eq_sqTrig, hTrig]
      linarith [hid x]
    rw [hx']
    ring
  have h1 := integral_sqTrig_mul_cos B q (hA a ha)
  simp_rw [hx] at h1
  have hc := continuous_cosSum A
  have hh := continuous_hTrig G c
  have hi1 : IntervalIntegrable (fun x => lam * Real.cos ((a : ℝ) * x) +
      cosSum A x * Real.cos ((a : ℝ) * x)) MeasureTheory.volume 0 (2 * π) :=
    (by fun_prop : Continuous fun x => lam * Real.cos ((a : ℝ) * x)).add
      (hc.mul (by fun_prop)) |>.intervalIntegrable _ _
  have hi2 : IntervalIntegrable (fun x => hTrig G c x * Real.cos ((a : ℝ) * x))
      MeasureTheory.volume 0 (2 * π) :=
    (hh.mul (by fun_prop)).intervalIntegrable _ _
  have hi3 : IntervalIntegrable (fun x => lam * Real.cos ((a : ℝ) * x))
      MeasureTheory.volume 0 (2 * π) :=
    (by fun_prop : Continuous fun x => lam * Real.cos ((a : ℝ) * x)).intervalIntegrable _ _
  have hi4 : IntervalIntegrable (fun x => cosSum A x * Real.cos ((a : ℝ) * x))
      MeasureTheory.volume 0 (2 * π) :=
    (hc.mul (by fun_prop)).intervalIntegrable _ _
  have hGa : ∀ g ∈ G, g.natAbs ≠ a := fun g hg h => (hG g hg).2 (h ▸ ha)
  rw [intervalIntegral.integral_add hi1 hi2, intervalIntegral.integral_add hi3 hi4,
    intervalIntegral.integral_const_mul, integral_cos_nat_mul (hA a ha),
    integral_cosSum_mul_cos A hA ha, integral_hTrig_mul_cos G c (hA a ha) hGa] at h1
  have hπ := Real.pi_pos
  have h2 : π * (∑ β ∈ B, ∑ β' ∈ B, (if (β - β').natAbs = a then Rp q β β' else 0)) =
      π * 1 := by linarith
  exact mul_left_cancel₀ hπ.ne' h2

/-- `#{(β,β') ∈ B² : β - β' = g} ≤ #{β ∈ B : β - g ∈ B}`. -/
theorem card_pairs_sub_eq_le (B : Finset ℤ) (g : ℤ) :
    ((B ×ˢ B).filter (fun p => p.1 - p.2 = g)).card ≤ (B.filter (fun β => β - g ∈ B)).card := by
  apply Finset.card_le_card_of_injOn Prod.fst
  · intro p hp
    simp only [Finset.coe_filter, Finset.mem_product, Set.mem_ofPred_eq] at hp
    simp only [Finset.coe_filter, Set.mem_ofPred_eq]
    refine ⟨hp.1.1, ?_⟩
    have : p.1 - g = p.2 := by omega
    rw [this]
    exact hp.1.2
  · intro p hp p' hp' h
    simp only [Finset.coe_filter, Finset.mem_product, Set.mem_ofPred_eq] at hp hp'
    have h' : p.1 = p'.1 := h
    have : p.2 = p'.2 := by omega
    exact Prod.ext h' this

/-- `#{(β,β') ∈ B² : |β - β'| = a} ≤ 2m` when both representation counts at `±a` are `≤ m`. -/
theorem card_pairs_natAbs_le (B : Finset ℤ) (a m : ℕ)
    (h1 : (B.filter (fun β => β - (a : ℤ) ∈ B)).card ≤ m)
    (h2 : (B.filter (fun β => β - (-(a : ℤ)) ∈ B)).card ≤ m) :
    ((B ×ˢ B).filter (fun p => (p.1 - p.2).natAbs = a)).card ≤ 2 * m := by
  have hsub : (B ×ˢ B).filter (fun p => (p.1 - p.2).natAbs = a) ⊆
      (B ×ˢ B).filter (fun p => p.1 - p.2 = (a : ℤ)) ∪
        (B ×ˢ B).filter (fun p => p.1 - p.2 = -(a : ℤ)) := by
    intro p hp
    rw [Finset.mem_filter] at hp
    obtain ⟨hpB, hpa⟩ := hp
    rw [Finset.mem_union, Finset.mem_filter, Finset.mem_filter]
    rcases Int.natAbs_eq (p.1 - p.2) with h | h
    · left
      exact ⟨hpB, by omega⟩
    · right
      exact ⟨hpB, by omega⟩
  have := (Finset.card_le_card hsub).trans (Finset.card_union_le _ _)
  have h1' := (card_pairs_sub_eq_le B (a : ℤ)).trans h1
  have h2' := (card_pairs_sub_eq_le B (-(a : ℤ))).trans h2
  omega

/-- **Multiplicity bound for square certificates (P8).** Let `A` be a finite set of positive
naturals, `B, G ⊆ ℤ` finite, `q : ℤ → ℂ`, `c : ℤ → ℝ`, `λ : ℝ`, with `g ≠ 0` and `|g| ∉ A`
for all `g ∈ G`, and suppose that for **every** real `x`
`λ + f_A(x) = ‖∑_{β ∈ B} q_β e^{iβx}‖² - ∑_{g ∈ G} c_g cos (g x)`.
If `#{β ∈ B : β - g ∈ B} ≤ m` for every integer `g` with `|g| ∈ A`, then `|A| ≤ 2 m λ²`. -/
theorem card_le_of_sq_certificate (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a)
    (B : Finset ℤ) (q : ℤ → ℂ) (lam : ℝ) (G : Finset ℤ) (c : ℤ → ℝ)
    (hG : ∀ g ∈ G, g ≠ 0 ∧ g.natAbs ∉ A)
    (hid : ∀ x : ℝ, lam + cosSum A x =
      ‖∑ β ∈ B, q β * Complex.exp ((β : ℂ) * (x : ℂ) * Complex.I)‖ ^ 2 -
        ∑ g ∈ G, c g * Real.cos ((g : ℝ) * x))
    (m : ℕ) (hm : ∀ g : ℤ, g.natAbs ∈ A → (B.filter (fun β => β - g ∈ B)).card ≤ m) :
    (A.card : ℝ) ≤ 2 * m * lam ^ 2 := by
  set F : ℤ × ℤ → ℝ := fun p => ‖q p.1‖ ^ 2 * ‖q p.2‖ ^ 2 with hF_def
  have hF0 : ∀ p, 0 ≤ F p := fun p => by positivity
  have hlam := lam_eq_of_sq_certificate A hA B q lam G c hG hid
  have htot : ∑ p ∈ B ×ˢ B, F p = lam ^ 2 := by
    rw [hlam, sq, Finset.sum_mul_sum, Finset.sum_product]
  have hper : ∀ a ∈ A,
      1 ≤ 2 * (m : ℝ) * ∑ p ∈ (B ×ˢ B).filter (fun p => (p.1 - p.2).natAbs = a), F p := by
    intro a ha
    set P := (B ×ˢ B).filter (fun p => (p.1 - p.2).natAbs = a) with hP_def
    have h1 : ∑ p ∈ P, Rp q p.1 p.2 = 1 := by
      rw [hP_def, Finset.sum_filter, Finset.sum_product]
      exact coeff_eq_one_of_sq_certificate A hA B q lam G c hG hid ha
    have h2 : 1 ≤ ∑ p ∈ P, ‖q p.1‖ * ‖q p.2‖ :=
      h1 ▸ Finset.sum_le_sum (fun p _ => Rp_le q p.1 p.2)
    have h3 : (∑ p ∈ P, ‖q p.1‖ * ‖q p.2‖) ^ 2 ≤
        P.card * ∑ p ∈ P, (‖q p.1‖ * ‖q p.2‖) ^ 2 := sq_sum_le_card_mul_sum_sq
    have h6 : ∑ p ∈ P, (‖q p.1‖ * ‖q p.2‖) ^ 2 = ∑ p ∈ P, F p :=
      Finset.sum_congr rfl (fun p _ => by rw [hF_def, mul_pow])
    rw [h6] at h3
    have h4n : P.card ≤ 2 * m := by
      have hpos : (a : ℤ).natAbs ∈ A := by simpa using ha
      have hneg : (-(a : ℤ)).natAbs ∈ A := by simpa using ha
      exact card_pairs_natAbs_le B a m (hm _ hpos) (hm _ hneg)
    have h4 : (P.card : ℝ) ≤ 2 * m := by exact_mod_cast h4n
    have h5 : 0 ≤ ∑ p ∈ P, F p := Finset.sum_nonneg (fun p _ => hF0 p)
    have h7 : 1 ≤ (∑ p ∈ P, ‖q p.1‖ * ‖q p.2‖) ^ 2 := by nlinarith
    have h8 : (P.card : ℝ) * ∑ p ∈ P, F p ≤ 2 * m * ∑ p ∈ P, F p :=
      mul_le_mul_of_nonneg_right h4 h5
    linarith
  have hsum : ∑ a ∈ A, ∑ p ∈ (B ×ˢ B).filter (fun p => (p.1 - p.2).natAbs = a), F p ≤
      ∑ p ∈ B ×ˢ B, F p := by
    simp_rw [Finset.sum_filter]
    rw [Finset.sum_comm]
    apply Finset.sum_le_sum
    intro p _
    rw [Finset.sum_ite_eq]
    split_ifs
    · exact le_rfl
    · exact hF0 p
  have hm0 : (0 : ℝ) ≤ 2 * m := by positivity
  calc (A.card : ℝ) = ∑ a ∈ A, (1 : ℝ) := by simp
    _ ≤ ∑ a ∈ A, 2 * (m : ℝ) *
          ∑ p ∈ (B ×ˢ B).filter (fun p => (p.1 - p.2).natAbs = a), F p :=
        Finset.sum_le_sum hper
    _ = 2 * (m : ℝ) *
          ∑ a ∈ A, ∑ p ∈ (B ×ˢ B).filter (fun p => (p.1 - p.2).natAbs = a), F p := by
        rw [Finset.mul_sum]
    _ ≤ 2 * (m : ℝ) * ∑ p ∈ B ×ˢ B, F p := mul_le_mul_of_nonneg_left hsum hm0
    _ = 2 * m * lam ^ 2 := by rw [htot]

/-- **P8, as originally stated**: with the representation-count bound assumed for every
nonzero integer `g` (a stronger hypothesis than in `card_le_of_sq_certificate`). -/
theorem card_le_of_sq_certificate' (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a)
    (B : Finset ℤ) (q : ℤ → ℂ) (lam : ℝ) (G : Finset ℤ) (c : ℤ → ℝ)
    (hG : ∀ g ∈ G, g ≠ 0 ∧ g.natAbs ∉ A)
    (hid : ∀ x : ℝ, lam + cosSum A x =
      ‖∑ β ∈ B, q β * Complex.exp ((β : ℂ) * (x : ℂ) * Complex.I)‖ ^ 2 -
        ∑ g ∈ G, c g * Real.cos ((g : ℝ) * x))
    (m : ℕ) (hm : ∀ g : ℤ, g ≠ 0 → (B.filter (fun β => β - g ∈ B)).card ≤ m) :
    (A.card : ℝ) ≤ 2 * m * lam ^ 2 := by
  refine card_le_of_sq_certificate A hA B q lam G c hG hid m (fun g hg => hm g ?_)
  intro h0
  rw [h0, Int.natAbs_zero] at hg
  exact lt_irrefl 0 (hA 0 hg)

end ChowlaCosine
