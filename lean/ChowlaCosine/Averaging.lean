import ChowlaCosine.Basic

/-!
# Averaging over the `q`-th roots of unity

For a finite `A ⊆ ℕ`, a positive natural `q` and every real `x`,

  `(1/q) ∑_{j<q} f_A(x + 2πj/q) = f_{A_q}(x)`,   `A_q = {a ∈ A : q ∣ a}`,

because `∑_{j<q} cos (a (x + 2πj/q)) = q cos (a x)` if `q ∣ a` and `= 0` otherwise
(a geometric sum of `q`-th roots of unity).

Consequences, for a uniform lower bound `-M ≤ f_A(x)` (all real `x`):
* restriction to multiples: `-M ≤ f_{A_q}(x)` for all real `x` (any `q : ℕ`, including `0`);
* for `q ≥ 2`: `|A| - q |A_q| ≤ (q - 1) M`; in particular `|A| ≤ (q - 1) M` when no element
  of `A` is divisible by `q`.

No positivity hypothesis on `A` is needed for any of these statements.
-/

open Real

namespace ChowlaCosine

/-- `∑_{j<q} cos (a (x + 2πj/q)) = q cos (a x)` if `q ∣ a`, and `0` otherwise (`q > 0`). -/
theorem sum_range_cos_shift (a q : ℕ) (hq : 0 < q) (x : ℝ) :
    ∑ j ∈ Finset.range q, Real.cos ((a : ℝ) * (x + 2 * π * j / q)) =
      if q ∣ a then (q : ℝ) * Real.cos ((a : ℝ) * x) else 0 := by
  have hq' : (q : ℝ) ≠ 0 := by exact_mod_cast hq.ne'
  split_ifs with hdiv
  · obtain ⟨k, rfl⟩ := hdiv
    have hterm : ∀ j ∈ Finset.range q, Real.cos (((q * k : ℕ) : ℝ) * (x + 2 * π * j / q)) =
        Real.cos (((q * k : ℕ) : ℝ) * x) := by
      intro j _
      have : ((q * k : ℕ) : ℝ) * (x + 2 * π * j / q) =
          ((q * k : ℕ) : ℝ) * x + ((k * j : ℕ) : ℝ) * (2 * π) := by
        push_cast
        field_simp
      rw [this, Real.cos_add_nat_mul_two_pi]
    rw [Finset.sum_congr rfl hterm, Finset.sum_const, Finset.card_range, nsmul_eq_mul]
  · set ζ : ℂ := Complex.exp (((2 * π * a / q : ℝ) : ℂ) * Complex.I) with hζ_def
    have hζq : ζ ^ q = 1 := by
      rw [hζ_def, ← Complex.exp_nat_mul]
      have : (q : ℂ) * (((2 * π * a / q : ℝ) : ℂ) * Complex.I) =
          (a : ℂ) * (2 * π * Complex.I) := by
        have hqc : (q : ℂ) ≠ 0 := by exact_mod_cast hq.ne'
        push_cast
        field_simp
      rw [this, Complex.exp_nat_mul_two_pi_mul_I]
    have hζ1 : ζ ≠ 1 := by
      intro h
      rw [hζ_def, Complex.exp_eq_one_iff] at h
      obtain ⟨n, hn⟩ := h
      have h2 := congrArg Complex.im hn
      simp only [Complex.mul_im, Complex.ofReal_re, Complex.ofReal_im, Complex.I_re,
        Complex.I_im, Complex.intCast_re, Complex.intCast_im, Complex.mul_re, mul_one, mul_zero,
        sub_zero, add_zero, zero_mul, Complex.re_ofNat, Complex.im_ofNat] at h2
      have h3 : (a : ℝ) = (n : ℝ) * q := by
        field_simp at h2
        nlinarith [Real.pi_pos]
      have h4 : (a : ℤ) = n * q := by exact_mod_cast h3
      apply hdiv
      have : (q : ℤ) ∣ (a : ℤ) := ⟨n, by rw [h4]; ring⟩
      exact_mod_cast this
    have hgeom : ∑ j ∈ Finset.range q, ζ ^ j = 0 := by
      rw [geom_sum_eq hζ1, hζq, sub_self, zero_div]
    have hterm : ∀ j ∈ Finset.range q, Real.cos ((a : ℝ) * (x + 2 * π * j / q)) =
        (Complex.exp ((((a : ℝ) * x : ℝ) : ℂ) * Complex.I) * ζ ^ j).re := by
      intro j _
      rw [hζ_def, ← Complex.exp_nat_mul, ← Complex.exp_add,
        ← Complex.exp_ofReal_mul_I_re ((a : ℝ) * (x + 2 * π * j / q))]
      congr 3
      push_cast
      ring
    rw [Finset.sum_congr rfl hterm, ← Complex.re_sum, ← Finset.mul_sum, hgeom, mul_zero,
      Complex.zero_re]

/-- `∑_{j<q} f_A(x + 2πj/q) = q f_{A_q}(x)` for `q > 0`, `A_q = {a ∈ A : q ∣ a}`. -/
theorem sum_cosSum_shift (A : Finset ℕ) (q : ℕ) (hq : 0 < q) (x : ℝ) :
    ∑ j ∈ Finset.range q, cosSum A (x + 2 * π * j / q) =
      q * cosSum (A.filter (fun a => q ∣ a)) x := by
  simp only [cosSum]
  rw [Finset.sum_comm, Finset.sum_congr rfl (fun a _ => sum_range_cos_shift a q hq x),
    Finset.sum_filter, Finset.mul_sum]
  refine Finset.sum_congr rfl (fun a _ => ?_)
  split_ifs <;> simp

/-- **Averaging identity.** For `A : Finset ℕ`, `0 < q` and every real `x`,
`(1/q) ∑_{j<q} f_A(x + 2πj/q) = f_{A ∩ qℕ}(x)`. -/
theorem averaging_identity (A : Finset ℕ) (q : ℕ) (hq : 0 < q) (x : ℝ) :
    (1 / (q : ℝ)) * ∑ j ∈ Finset.range q, cosSum A (x + 2 * π * j / q) =
      cosSum (A.filter (fun a => q ∣ a)) x := by
  rw [sum_cosSum_shift A q hq x]
  have : (q : ℝ) ≠ 0 := by exact_mod_cast hq.ne'
  field_simp

/-- **Restriction to multiples.** If `-M ≤ f_A(x)` for every real `x`, then
`-M ≤ f_{A ∩ qℕ}(x)` for every real `x`, for every `q : ℕ` (for `q = 0` the restricted set is
`A ∩ {0}`). -/
theorem cosSum_filter_dvd_ge (A : Finset ℕ) (q : ℕ) (M : ℝ)
    (hM : ∀ x : ℝ, -M ≤ cosSum A x) :
    ∀ x : ℝ, -M ≤ cosSum (A.filter (fun a => q ∣ a)) x := by
  have key : ∀ q' : ℕ, 0 < q' → ∀ x : ℝ, -M ≤ cosSum (A.filter (fun a => q' ∣ a)) x := by
    intro q' hq' x
    rw [← averaging_identity A q' hq' x]
    have hsum : ∑ _j ∈ Finset.range q', (-M) ≤
        ∑ j ∈ Finset.range q', cosSum A (x + 2 * π * j / q') :=
      Finset.sum_le_sum (fun j _ => hM _)
    rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul] at hsum
    have hq'r : (0 : ℝ) < q' := by exact_mod_cast hq'
    rw [div_mul_eq_mul_div, one_mul, le_div_iff₀ hq'r]
    linarith
  rcases Nat.eq_zero_or_pos q with h0 | hq
  · subst h0
    have hfil : A.filter (fun a => 0 ∣ a) = A.filter (fun a => (A.sup id + 1) ∣ a) := by
      apply Finset.filter_congr
      intro a ha
      have hle : a ≤ A.sup id := Finset.le_sup (f := id) ha
      constructor
      · intro h
        rw [zero_dvd_iff] at h
        rw [h]
        exact dvd_zero _
      · intro h
        rw [zero_dvd_iff]
        exact Nat.eq_zero_of_dvd_of_lt h (by omega)
    rw [hfil]
    exact key _ (by omega)
  · exact key q hq

/-- `f_B(0) = |B|`. -/
theorem cosSum_zero (B : Finset ℕ) : cosSum B 0 = B.card := by
  simp [cosSum]

/-- **Mixed bound.** If `2 ≤ q` and `-M ≤ f_A(x)` for every real `x`, then
`|A| - q · #{a ∈ A : q ∣ a} ≤ (q - 1) M`. -/
theorem card_sub_le_of_cosSum_ge (A : Finset ℕ) (q : ℕ) (hq : 2 ≤ q) (M : ℝ)
    (hM : ∀ x : ℝ, -M ≤ cosSum A x) :
    (A.card : ℝ) - q * (A.filter (fun a => q ∣ a)).card ≤ ((q : ℝ) - 1) * M := by
  have h := sum_cosSum_shift A q (by omega) 0
  rw [cosSum_zero] at h
  obtain ⟨n, rfl⟩ : ∃ n, q = n + 1 := ⟨q - 1, by omega⟩
  rw [Finset.sum_range_succ'] at h
  simp only [Nat.cast_zero, mul_zero, zero_div, add_zero, cosSum_zero] at h
  have hlow : ∀ g : ℕ → ℝ, (n : ℝ) * (-M) ≤ ∑ i ∈ Finset.range n, cosSum A (g i) := by
    intro g
    have := Finset.sum_le_sum (fun i (_ : i ∈ Finset.range n) => hM (g i))
    simpa using this
  have hl := hlow (fun i => 0 + 2 * π * ((i + 1 : ℕ) : ℝ) / ((n + 1 : ℕ) : ℝ))
  beta_reduce at hl
  push_cast at h hl ⊢
  linarith

/-- **Mixed bound, division form.** If `2 ≤ q` and `-M ≤ f_A(x)` for every real `x`, then
`M ≥ (|A| - q · #{a ∈ A : q ∣ a}) / (q - 1)`. -/
theorem le_of_cosSum_ge_mixed (A : Finset ℕ) (q : ℕ) (hq : 2 ≤ q) (M : ℝ)
    (hM : ∀ x : ℝ, -M ≤ cosSum A x) :
    ((A.card : ℝ) - q * (A.filter (fun a => q ∣ a)).card) / ((q : ℝ) - 1) ≤ M := by
  have h := card_sub_le_of_cosSum_ge A q hq M hM
  have hq1 : (0 : ℝ) < (q : ℝ) - 1 := by
    have : (2 : ℝ) ≤ q := by exact_mod_cast hq
    linarith
  rw [div_le_iff₀ hq1]
  linarith

/-- **No multiples.** If `2 ≤ q`, no element of `A` is divisible by `q`, and `-M ≤ f_A(x)` for
every real `x`, then `|A| ≤ (q - 1) M`. (Positivity of `A` is not needed: `q ∣ 0`.) -/
theorem card_le_of_no_multiples (A : Finset ℕ) (q : ℕ) (hq : 2 ≤ q)
    (hnd : ∀ a ∈ A, ¬ q ∣ a) (M : ℝ) (hM : ∀ x : ℝ, -M ≤ cosSum A x) :
    (A.card : ℝ) ≤ ((q : ℝ) - 1) * M := by
  have h := card_sub_le_of_cosSum_ge A q hq M hM
  have h0 : A.filter (fun a => q ∣ a) = ∅ := Finset.filter_eq_empty_iff.mpr hnd
  rw [h0, Finset.card_empty, Nat.cast_zero, mul_zero, sub_zero] at h
  exact h

/-- The no-multiples bound with the (redundant) positivity hypothesis, exactly as requested. -/
theorem card_le_of_no_multiples' (A : Finset ℕ) (q : ℕ) (hq : 2 ≤ q)
    (_hA : ∀ a ∈ A, 0 < a) (hnd : ∀ a ∈ A, ¬ q ∣ a) (M : ℝ)
    (hM : ∀ x : ℝ, -M ≤ cosSum A x) :
    (A.card : ℝ) ≤ ((q : ℝ) - 1) * M :=
  card_le_of_no_multiples A q hq hnd M hM

end ChowlaCosine
