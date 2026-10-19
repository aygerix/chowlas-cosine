import ChowlaCosine.P31.Averaging
import ChowlaCosine.P31.Fejer

/-!
# P31 with its spectral-factorization dependency explicit

`p31_of_factorization` assumes actual analytic factors for all real window
centres. This is an explicitly CONDITIONAL version of T3, not a proof of
finite Fejér–Riesz. All circle moment and averaging identities are proved.
-/

open Real MeasureTheory
open scoped BigOperators

namespace ChowlaCosine.P31

theorem circleMean_fejerKernel_shift (w : ℕ) (y : ℝ) :
    circleMean (fun x => fejerKernel w (x - y)) = 1 := by
  rw [circleMean_periodic_sub (fejerKernel_periodic w), circleMean_fejerKernel]

theorem circleMean_fejerKernel_mul_cos (w : ℕ) {a : ℕ} (ha : 0 < a) (y : ℝ) :
    circleMean (fun x => fejerKernel w (x - y) * Real.cos ((a : ℝ) * x)) =
      kappa w a * Real.cos ((a : ℝ) * y) := by
  have hexp : (fun x => fejerKernel w (x - y) * Real.cos ((a : ℝ) * x)) =
      (fun x => Real.cos ((a : ℝ) * x) + 2 * ∑ k ∈ windowFreq w,
        kappa w k * (Real.cos ((k : ℝ) * (x - y)) * Real.cos ((a : ℝ) * x))) := by
    funext x
    simp only [fejerKernel, weightedCos, add_mul, one_mul]
    congr 1
    rw [mul_assoc]
    congr 1
    rw [Finset.sum_mul]
    apply Finset.sum_congr rfl
    intro k hk
    ring
  rw [hexp, circleMean_add (by fun_prop) (by fun_prop)]
  have hm : circleMean (fun x => Real.cos ((a : ℝ) * x)) = 0 := by
    simp [circleMean, integral_cos_nat_mul ha]
  rw [hm, zero_add, circleMean_const_mul,
    circleMean_sum (windowFreq w) _ (by intro k hk; fun_prop)]
  have hi : ∀ k ∈ windowFreq w, circleMean (fun x => kappa w k *
      (Real.cos ((k : ℝ) * (x - y)) * Real.cos ((a : ℝ) * x))) =
        if k = a then kappa w a * Real.cos ((a : ℝ) * y) / 2 else 0 := by
    intro k hk
    rw [circleMean_const_mul,
      circleMean_cos_shift_mul_cos (windowFreq_pos w k hk) ha]
    split_ifs with hka
    · subst k
      ring
    · ring
  rw [Finset.sum_congr rfl hi]
  by_cases haw : a ≤ w
  · have ham : a ∈ windowFreq w := Finset.mem_Icc.mpr ⟨ha, haw⟩
    simp [ham]
    ring
  · have hz := kappa_eq_zero (Nat.lt_of_not_ge haw)
    simp [hz]

theorem circleMean_window (w : ℕ) (A : Finset ℕ) (M y : ℝ)
    (hA : ∀ a ∈ A, 0 < a) :
    circleMean (fun x => fejerKernel w (x - y) * (cosSum A x + M)) =
      M + weightedCos A (kappa w) y := by
  have hexp : (fun x => fejerKernel w (x - y) * (cosSum A x + M)) =
      (fun x => (∑ a ∈ A, fejerKernel w (x - y) * Real.cos ((a : ℝ) * x)) +
        fejerKernel w (x - y) * M) := by
    funext x
    simp [cosSum, mul_add, Finset.mul_sum]
  rw [hexp, circleMean_add (by fun_prop) (by fun_prop),
    circleMean_sum A _ (by intro a ha; fun_prop), circleMean_mul_const,
    circleMean_fejerKernel_shift, one_mul]
  rw [Finset.sum_congr rfl (fun a ha => circleMean_fejerKernel_mul_cos w (hA a ha) y)]
  exact add_comm _ _

theorem circleMean_window_mean_sq (w : ℕ) (A : Finset ℕ) (M : ℝ)
    (hA : ∀ a ∈ A, 0 < a) :
    circleMean (fun y => circleMean
      (fun x => fejerKernel w (x - y) * (cosSum A x + M)) ^ 2) =
        M ^ 2 + windowEnergy w A / 2 := by
  simp_rw [circleMean_window w A M _ hA]
  exact circleMean_shifted_weightedCos_sq A (kappa w) M hA

/-- Exact P31 averaging reduction. The additional hypothesis is the
square/mean inequality for every translated window. -/
theorem p31_of_window_bound (w : ℕ) (A : Finset ℕ) (M C : ℝ)
    (hA : ∀ a ∈ A, 0 < a)
    (hbound : ∀ y : ℝ,
      circleMean (fun x => (fejerKernel w (x - y) * (cosSum A x + M)) ^ 2) ≤
        C * circleMean (fun x => fejerKernel w (x - y) * (cosSum A x + M)) ^ 2) :
    windowMass w * ((A.card : ℝ) / 2 + M ^ 2) ≤
      C * (M ^ 2 + windowEnergy w A / 2) := by
  have h := averaged_window_bound C (continuous_fejerKernel w)
    ((continuous_cosSum A).add continuous_const)
    (fejerKernel_periodic w) hbound
  simp only [Pi.add_apply] at h
  rwa [circleMean_fejerKernel_sq, circleMean_cosSum_add_sq A M hA,
    circleMean_window_mean_sq w A M hA] at h

noncomputable def analyticValue {L : ℕ} (u : Fin (L + 1) → ℂ) (x : ℝ) : ℂ :=
  ∑ j, u j * Complex.exp ((j.val : ℂ) * (x : ℂ) * Complex.I)

/-- The analytic degree-at-most-`L` hypothesis in T3, in normalized
fourth/second-moment form. It quantifies over every complex coefficient vector. -/
def AnalyticNikolskii (L : ℕ) (C : ℝ) : Prop :=
  ∀ u : Fin (L + 1) → ℂ,
    circleMean (fun x => ‖analyticValue u x‖ ^ 4) ≤
      C * circleMean (fun x => ‖analyticValue u x‖ ^ 2) ^ 2

/-- The exact missing window-specific consequence of Fejér–Riesz,
with analytic degree at most `L`. Centres and angles are arbitrary reals. -/
def WindowFactorization (L w : ℕ) (A : Finset ℕ) (M : ℝ) : Prop :=
  ∀ y : ℝ, ∃ u : Fin (L + 1) → ℂ, ∀ x : ℝ,
    fejerKernel w (x - y) * (cosSum A x + M) = ‖analyticValue u x‖ ^ 2

/-- CONDITIONAL T3. `hfactor` is an additional, unproved mathematical
hypothesis and is not hidden in the Nikolskii constant. -/
theorem p31_of_factorization (L w : ℕ) (A : Finset ℕ) (M C : ℝ)
    (hA : ∀ a ∈ A, 0 < a) (hnik : AnalyticNikolskii L C)
    (hfactor : WindowFactorization L w A M) :
    windowMass w * ((A.card : ℝ) / 2 + M ^ 2) ≤
      C * (M ^ 2 + windowEnergy w A / 2) := by
  apply p31_of_window_bound w A M C hA
  intro y
  obtain ⟨u, hu⟩ := hfactor y
  have h := hnik u
  have hpow : ∀ x : ℝ, (fejerKernel w (x - y) * (cosSum A x + M)) ^ 2 =
      ‖analyticValue u x‖ ^ 4 := by
    intro x
    rw [hu x, ← pow_mul]
  simpa only [hu, ← pow_mul] using h

end ChowlaCosine.P31

/-! ## Degree control and the universal factorization assumption

The span representation is a finite complex trigonometric polynomial, not
a relaxation of the `Finset` of positive frequencies in the theorem.
-/

namespace ChowlaCosine.P31

noncomputable def circleCharacter (k : ℤ) (x : ℝ) : ℂ :=
  Complex.exp ((k : ℂ) * (x : ℂ) * Complex.I)

noncomputable def trigBand (L : ℕ) : Submodule ℂ (ℝ → ℂ) :=
  Submodule.span ℂ {f | ∃ k : ℤ, |k| ≤ (L : ℤ) ∧ f = circleCharacter k}

theorem character_mem_trigBand {L : ℕ} {k : ℤ} (hk : |k| ≤ (L : ℤ)) :
    circleCharacter k ∈ trigBand L :=
  Submodule.subset_span ⟨k, hk, rfl⟩

private theorem character_mul (k m : ℤ) :
    circleCharacter k * circleCharacter m = circleCharacter (k + m) := by
  funext x
  simp only [Pi.mul_apply, circleCharacter, ← Complex.exp_add]
  congr 1
  push_cast
  ring

theorem trigBand_mul {L K : ℕ} {f g : ℝ → ℂ}
    (hf : f ∈ trigBand L) (hg : g ∈ trigBand K) :
    f * g ∈ trigBand (L + K) := by
  induction hf using Submodule.span_induction with
  | mem f hf =>
    obtain ⟨k, hk, rfl⟩ := hf
    induction hg using Submodule.span_induction with
    | mem g hg =>
      obtain ⟨m, hm, rfl⟩ := hg
      rw [character_mul]
      apply character_mem_trigBand
      have hab := abs_add_le k m
      push_cast
      omega
    | zero => simpa using (trigBand (L + K)).zero_mem
    | add f g hf hg ihf ihg =>
      simpa only [mul_add] using (trigBand (L + K)).add_mem ihf ihg
    | smul c f hf ih =>
      simpa only [mul_smul_comm] using (trigBand (L + K)).smul_mem c ih
  | zero => simpa using (trigBand (L + K)).zero_mem
  | add f h hf hh ihf ihh =>
    simpa only [add_mul] using (trigBand (L + K)).add_mem ihf ihh
  | smul c f hf ih =>
    simpa only [smul_mul_assoc] using (trigBand (L + K)).smul_mem c ih

theorem const_mem_trigBand (L : ℕ) (c : ℂ) : (fun _ : ℝ => c) ∈ trigBand L := by
  have h := (trigBand L).smul_mem c
    (character_mem_trigBand (L := L) (k := 0) (by simp))
  convert h using 1
  funext x
  simp [circleCharacter]

/-- A shifted cosine has precisely the same frequency bound. -/
theorem cos_shift_mem_trigBand {L a : ℕ} (ha : a ≤ L) (y : ℝ) :
    (fun x : ℝ => (Real.cos ((a : ℝ) * (x - y)) : ℂ)) ∈ trigBand L := by
  have hp := (trigBand L).smul_mem
    (Complex.exp (-(a : ℂ) * (y : ℂ) * Complex.I) / 2)
    (character_mem_trigBand (L := L) (k := (a : ℤ)) (by
      simpa using (show (a : ℤ) ≤ L by exact_mod_cast ha)))
  have hn := (trigBand L).smul_mem
    (Complex.exp ((a : ℂ) * (y : ℂ) * Complex.I) / 2)
    (character_mem_trigBand (L := L) (k := -(a : ℤ)) (by
      simpa using (show (a : ℤ) ≤ L by exact_mod_cast ha)))
  convert (trigBand L).add_mem hp hn using 1
  funext x
  simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul, circleCharacter]
  rw [Complex.ofReal_cos, Complex.cos]
  push_cast
  have he1 : Complex.exp (-(a : ℂ) * (y : ℂ) * Complex.I) *
      Complex.exp ((a : ℂ) * (x : ℂ) * Complex.I) =
      Complex.exp (((a : ℂ) * ((x : ℂ) - (y : ℂ))) * Complex.I) := by
    rw [← Complex.exp_add]
    congr 1
    ring
  have he2 : Complex.exp ((a : ℂ) * (y : ℂ) * Complex.I) *
      Complex.exp (-(a : ℂ) * (x : ℂ) * Complex.I) =
      Complex.exp (-((a : ℂ) * ((x : ℂ) - (y : ℂ))) * Complex.I) := by
    rw [← Complex.exp_add]
    congr 1
    ring
  linear_combination -(1 / 2 : ℂ) * he1 - (1 / 2 : ℂ) * he2

theorem fejer_shift_mem_trigBand (w : ℕ) (y : ℝ) :
    (fun x : ℝ => (fejerKernel w (x - y) : ℂ)) ∈ trigBand w := by
  have hs : (fun x : ℝ => (2 : ℂ) *
      ∑ a ∈ windowFreq w, (kappa w a : ℂ) *
        (Real.cos ((a : ℝ) * (x - y)) : ℂ)) ∈ trigBand w := by
    apply (trigBand w).smul_mem (2 : ℂ)
    have hsum : (∑ a ∈ windowFreq w, fun x : ℝ => (kappa w a : ℂ) *
        (Real.cos ((a : ℝ) * (x - y)) : ℂ)) ∈ trigBand w := by
      apply Submodule.sum_mem
      intro a ha
      exact (trigBand w).smul_mem (kappa w a : ℂ)
        (cos_shift_mem_trigBand (Finset.mem_Icc.mp ha).2 y)
    convert hsum using 1
    funext x
    simp only [Finset.sum_apply]
  convert (trigBand w).add_mem (const_mem_trigBand w 1) hs using 1
  funext x
  simp [fejerKernel, weightedCos]

theorem cosSum_add_mem_trigBand (A : Finset ℕ) (X : ℕ) (M : ℝ)
    (hX : ∀ a ∈ A, a ≤ X) :
    (fun x : ℝ => (cosSum A x + M : ℂ)) ∈ trigBand X := by
  have hs : (fun x : ℝ => (cosSum A x : ℂ)) ∈ trigBand X := by
    have h : (∑ a ∈ A, fun x : ℝ => (Real.cos ((a : ℝ) * x) : ℂ)) ∈ trigBand X := by
      apply Submodule.sum_mem
      intro a ha
      simpa using cos_shift_mem_trigBand (hX a ha) 0
    convert h using 1
    funext x
    simp only [cosSum, Complex.ofReal_sum, Finset.sum_apply]
  convert (trigBand X).add_mem hs (const_mem_trigBand X (M : ℂ)) using 1
  funext x
  simp only [Pi.add_apply]

/-- The full finite Fejér–Riesz assertion needed here, kept as a `Prop`
so it cannot be mistaken for a proved theorem. -/
def FejerRiesz (L : ℕ) : Prop :=
  ∀ h : ℝ → ℝ, (fun x => (h x : ℂ)) ∈ trigBand L →
    (∀ x : ℝ, 0 ≤ h x) →
      ∃ u : Fin (L + 1) → ℂ, ∀ x : ℝ, h x = ‖analyticValue u x‖ ^ 2

end ChowlaCosine.P31

namespace ChowlaCosine.P31

/-- P31 with the one missing universal theorem made explicit. Here `X`
may be any upper bound for the positive finite set, and `L = X + w` exactly. -/
theorem p31_of_fejerRiesz (w X : ℕ) (A : Finset ℕ) (M C : ℝ)
    (hA : ∀ a ∈ A, 0 < a) (hX : ∀ a ∈ A, a ≤ X)
    (hM : ∀ x : ℝ, -M ≤ cosSum A x)
    (hFR : FejerRiesz (X + w)) (hnik : AnalyticNikolskii (X + w) C) :
    windowMass w * ((A.card : ℝ) / 2 + M ^ 2) ≤
      C * (M ^ 2 + windowEnergy w A / 2) := by
  apply p31_of_factorization (X + w) w A M C hA hnik
  intro y
  apply hFR (fun x => fejerKernel w (x - y) * (cosSum A x + M))
  · have hd := trigBand_mul (fejer_shift_mem_trigBand w y)
      (cosSum_add_mem_trigBand A X M hX)
    rw [Nat.add_comm] at hd
    convert hd using 1
    funext x
    simp only [Pi.mul_apply, Complex.ofReal_mul, Complex.ofReal_add]
  · intro x
    exact window_nonneg w A M hM x y

/-- Exact maximum-frequency specialization. The additional `hFR`
hypothesis must be discharged by T1 before this is the requested T3. -/
theorem p31_main_of_fejerRiesz (w : ℕ) (A : Finset ℕ) (M C : ℝ)
    (hA : ∀ a ∈ A, 0 < a) (hM : ∀ x : ℝ, -M ≤ cosSum A x)
    (hFR : FejerRiesz (A.sup id + w))
    (hnik : AnalyticNikolskii (A.sup id + w) C) :
    windowMass w * ((A.card : ℝ) / 2 + M ^ 2) ≤
      C * (M ^ 2 + windowEnergy w A / 2) :=
  p31_of_fejerRiesz w (A.sup id) A M C hA
    (fun _ ha => Finset.le_sup (f := id) ha) hM hFR hnik

end ChowlaCosine.P31

