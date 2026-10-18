# Lean O4⁺ / line D formalization report

Date: 2026-10-18. Brief: `.research/agents/lean_o4plus_brief.md`.

**Status: T0, T1 (including both run-top corollaries), T2, and T3(a)–(e) are kernel-checked.** The full remote build succeeded, and all 33 audited declarations show exactly `[propext, Classical.choice, Quot.sound]`.

The implementation covers T0, all of T1 including its run-top corollary, T2, and T3(a)–(e). No statement was refuted, no hypothesis was added to repair a statement, and no statement was weakened. The general cubic constant in T3(c) agrees with the brief.

## Files and execution scope

- `lean/ChowlaCosine/FibreSchur.lean`: T0–T2, quotient and Fourier bridges, zero-fibre classifications, run-top corollaries.
- `lean/ChowlaCosine/HalfSet.lean`: T3(a)–(e) and finite convolution algebra.
- `lean/ChowlaCosine.lean`: imports both new modules.
- `lean/ChowlaCosine/AxiomCheck.lean`: the requested audit file. The pre-existing `lean/AxiomCheck.lean` is unchanged.
- This report.

Every Lean invocation ran on **dirichlet**, through `src/dirun.sh -c 4 -m 16`. No Lean build ran on the laptop. No command targeted fejer. No other process was killed, signalled, or modified; the lead's `exh2` and `coretail_omp` jobs were left alone. No commit was made. Existing unrelated worktree changes were preserved.

The local operations were source inspection and edits to the files above. The required runner performs its usual synchronization and retrieval of VM build artifacts.

## Definitions and exact correspondence

All names in the first three target sections have namespace `ChowlaCosine.FibreSchur`.

`fourier P ψ = ∑ y, P y * conj (ψ y)`, with **no normalization**. `PositiveDefinite P` means that for every character the transform has imaginary part zero and nonnegative real part, exactly the brief's definition.

`setFourier A χ = ∑ x ∈ A, χ x`. A hypothesis `∀ x ∈ A, -x ∈ A` is equivalent to `A = -A`, since negation is an involution. The additive character `0` is the trivial character (the constant function `1`), so `η ≠ 0` is exactly the nontrivial-character hypothesis.

`Cosets t` is the actual quotient `G ⧸ AddSubgroup.zmultiples t`, and `projection t` is its quotient homomorphism. `fibreSet A t y` is `A` intersected with that coset. `fibre (projection t) A χ y` sums the actual values `χ x` over this intersection; it is not a sum over an assumed transversal. `singleCosets`, `doubleCosets`, and `tripleCosets` exclude the zero coset and count actual fibres of cardinality 1, 2, and 3.

`omega = Complex.exp (2 * Real.pi * Complex.I / 3)`; `omega_primitive` verifies its exact order. `quotientPower t χ r` is the descended character `ρ`, and `quotientPower_apply` proves `ρ(projection t x) = χ(x)^r`. Its construction proves that it descends; the main bounds do not assume that fact.

The bounds write the real number `u₀` as `(fibre (projection t) A χ 0).re`. `fibre_zero_im_eq_zero` proves this fibre is real; `order_three_zero_fibre` and `order_four_zero_fibre` prove its stronger complex-valued classification `U(0) = 0 ∨ U(0) = -1`. Thus this is exactly the `u₀` in the brief.

`twoRunCosets` initially uses cyclic coordinates in the actual coset. Crucially, `mem_twoRunCosets_iff` proves this is **exactly** the set of nonzero cosets whose actual fibre is `{x, x+t}`. Opposite pairs are excluded. No assumption about the coordinate choice is needed in the final theorem.

## T0: finite Fourier Schur product and natural powers

`fourier_inversion` proves Fourier inversion multiplied by the group order, and `fourier_mul_card` proves

`|H| * Fourier(PQ)(ψ) = ∑ χ, Fourier(P)(χ) * Fourier(Q)(ψ / χ)`.

Since a finite group has positive cardinality, this is precisely the product-to-convolution formula with factor `1/|H|`. The Schur theorem uses this identity, not a different definition of positive definiteness. All groups are arbitrary finite additive commutative groups, represented by `[AddCommGroup H] [Fintype H]`.

```lean
theorem PositiveDefinite.mul {P Q : H → ℂ} (hP : PositiveDefinite P)
    (hQ : PositiveDefinite Q) : PositiveDefinite (fun y => P y * Q y)
```

```lean
theorem PositiveDefinite.pow {P : H → ℂ} (hP : PositiveDefinite P) (r : ℕ) :
    PositiveDefinite (fun y => P y ^ r)
```

## T1: exact order-three quotient and run-top inequalities

The following four theorems are the requested inequality, zero-fibre classification, unconditional run-top count, and spectral run-top bound. The assumptions `0 ∉ A` and `0 ≤ K` are retained in the main spectral theorem signatures; their underscore-prefixed binder names only mark that the cardinality inequality itself does not need them. The zero-fibre classification does use `0 ∉ A`.

```lean
theorem order_three_fibre_bound (A : Finset G) (hsym : ∀ x ∈ A, -x ∈ A)
    (_hzero : (0 : G) ∉ A) (K : ℝ) (_hKnonneg : 0 ≤ K)
    (hK : ∀ η : AddChar G ℂ, η ≠ 0 → -K ≤ (setFourier A η).re)
    (t : G) (ht : addOrderOf t = 3) (χ : AddChar G ℂ) (hχ : χ t = omega) :
    ((doubleCosets A t).card : ℝ) - (singleCosets A t).card ≤
      (K + (fibre (projection t) A χ 0).re) ^ 3
```

```lean
theorem order_three_zero_fibre (A : Finset G) (hsym : ∀ x ∈ A, -x ∈ A)
    (hzero : (0 : G) ∉ A) (t : G) (ht : addOrderOf t = 3)
    (χ : AddChar G ℂ) (hχ : χ t = omega) :
    fibre (projection t) A χ 0 = 0 ∨ fibre (projection t) A χ 0 = -1
```

```lean
theorem order_three_runTops_card (A : Finset G) (t : G) (ht : addOrderOf t = 3) :
    (runTops A t).card ≤ (doubleCosets A t).card + 1
```

```lean
theorem order_three_runTops_bound (A : Finset G) (hsym : ∀ x ∈ A, -x ∈ A)
    (hzero : (0 : G) ∉ A) (K : ℝ) (hKnonneg : 0 ≤ K)
    (hK : ∀ η : AddChar G ℂ, η ≠ 0 → -K ≤ (setFourier A η).re)
    (t : G) (ht : addOrderOf t = 3) (χ : AddChar G ℂ) (hχ : χ t = omega) :
    ((runTops A t).card : ℝ) ≤ (singleCosets A t).card +
      (K + (fibre (projection t) A χ 0).re) ^ 3 + 1
```

The proof establishes `fourier_fibre` with the convention `χ / ψ.compAddMonoidHom q`, proves every twist is nontrivial using its value on `t`, and proves `shifted_fibre_positiveDefinite` from the original spectral assumption. `fibre_cube_table` proves the fibre values on the actual quotient. `order_three_runTops_card` proves injectivity of the projection on run-tops and allows one extra top in the zero coset. No Fourier positivity or fibre-table identity is added as a hypothesis to these final theorems.

## T2: exact order-four / O4⁺ inequality

```lean
theorem mem_twoRunCosets_iff (A : Finset G) (t : G) (ht : addOrderOf t = 4) (y : Cosets t) :
    y ∈ twoRunCosets A t ↔ y ≠ 0 ∧ ∃ x : G, fibreSet A t y = {x, x + t}
```

```lean
theorem order_four_fibre_bound (A : Finset G) (hsym : ∀ x ∈ A, -x ∈ A)
    (_hzero : (0 : G) ∉ A) (K : ℝ) (_hKnonneg : 0 ≤ K)
    (hK : ∀ η : AddChar G ℂ, η ≠ 0 → -K ≤ (setFourier A η).re)
    (t : G) (ht : addOrderOf t = 4) (χ : AddChar G ℂ) (hχ : χ t = Complex.I) :
    4 * ((twoRunCosets A t).card : ℝ) ≤ (singleCosets A t).card + (tripleCosets A t).card +
      (K + (fibre (projection t) A χ 0).re) ^ 4
```

```lean
theorem order_four_zero_fibre (A : Finset G) (hsym : ∀ x ∈ A, -x ∈ A)
    (hzero : (0 : G) ∉ A) (t : G) (ht : addOrderOf t = 4)
    (χ : AddChar G ℂ) (hχ : χ t = Complex.I) :
    fibre (projection t) A χ 0 = 0 ∨ fibre (projection t) A χ 0 = -1
```

The local theorem `fibre_table_four` checks all 16 subsets of `Fin 4` using kernel proof-producing tactics. `fibre_fourth_table` transports it to actual quotient fibres. Its values are +1 for singleton and three-point fibres, -4 for two-runs, and 0 for opposite pairs, full fibres, and empty fibres. T0 supplies positivity of the fourth power, yielding the exact coefficient `4` in O4⁺.

## T3: half-set identities and spectral bounds

All names in this section have namespace `ChowlaCosine.HalfSet`.

`IsSign g` is `∀ x, g x = 1 ∨ g x = -1`, an explicit real-valued representation of the codomain `{±1}`. It does not impose evenness or balance. `hat g` is mathlib's **unnormalized** `ZMod.dft` of the complex coercion of `g`. `hat_apply` proves the exact expression `∑ x, (g x : ℂ) * ZMod.stdAddChar (-(γ * x))`. `conv f k δ = ∑ γ, f γ * k (δ - γ)`. `shiftedHat g lam = hat g + lam`.

For (a)–(c), the proofs work for every nonzero modulus, so they in particular include every odd prime in the brief. The required statements are not conditional on evenness or balance. For (d)–(e), `[Fact p.Prime]` and `hp : p ≠ 2` express that `p` is an odd prime, with every other hypothesis retained.

In the even case `hat_im_eq_zero` proves realness, and `realShiftedHat_cast` identifies the real-valued `realShiftedHat` **exactly** with the complex-valued `shiftedHat`. Thus the real inequalities below are for the same `h` specified by the brief.

### T3(a)

```lean
theorem hat_conv_hat (g : ZMod p → ℝ) (hg : IsSign g) (δ : ZMod p) :
    conv (hat g) (hat g) δ = if δ = 0 then (p : ℂ) ^ 2 else 0
```

### T3(b)

`shiftedHat_square` additionally retains the diagonal term; the exact off-zero statement is:

```lean
theorem shiftedHat_square_off_zero (g : ZMod p → ℝ) (hg : IsSign g) (lam : ℝ)
    (δ : ZMod p) (hδ : δ ≠ 0) :
    conv (shiftedHat g lam) (shiftedHat g lam) δ =
      2 * lam * p * g 0 + p * (lam : ℂ) ^ 2
```

### T3(c) and audit of the constant

The implementation defines

`cubicConstant g lam = p² * (2*lam + 3*lam²*g(0) + lam³)`.

Derivation: writing `G = ĝ` and `1` for the constant function, `(G*G) = p² δ₀`, `∑G = p g(0)`, and `1*1 = p 1` give

`(G + lam 1)^{*3} = p² G + p²(3lam + 3lam² g(0) + lam³) 1`.

Substituting `G = h - lam 1` gives the displayed implementation constant. `cubicConstant_eq_brief` proves that it is exactly the brief's expression `p²(3lam + 3lam²g(0) + lam³) - p²lam`. When `g(0)=-1`, it factors as `p² lam(lam-1)(lam-2)`. There is **no discrepancy** in T3(c).

```lean
theorem shiftedHat_cube (g : ZMod p → ℝ) (hg : IsSign g) (lam : ℝ) (δ : ZMod p) :
    conv (conv (shiftedHat g lam) (shiftedHat g lam)) (shiftedHat g lam) δ =
      (p : ℂ) ^ 2 * shiftedHat g lam δ + (cubicConstant g lam : ℂ)
```

```lean
theorem cubicConstant_eq_brief (g : ZMod p → ℝ) (lam : ℝ) :
    cubicConstant g lam = (p : ℝ) ^ 2 * (3 * lam + 3 * lam ^ 2 * g 0 + lam ^ 3) -
      (p : ℝ) ^ 2 * lam
```

```lean
theorem cubicConstant_of_neg_one (g : ZMod p → ℝ) (lam : ℝ) (h0 : g 0 = -1) :
    cubicConstant g lam = (p : ℝ) ^ 2 * lam * (lam - 1) * (lam - 2)
```

```lean
theorem shiftedHat_cube_neg_one (g : ZMod p → ℝ) (hg : IsSign g) (hzero : g 0 = -1)
    (lam : ℝ) (δ : ZMod p) :
    conv (conv (shiftedHat g lam) (shiftedHat g lam)) (shiftedHat g lam) δ =
      (p : ℂ) ^ 2 * shiftedHat g lam δ + (p : ℂ) ^ 2 * lam * (lam - 1) * (lam - 2)
```

### T3(d)

```lean
theorem spectral_gap (hp : p ≠ 2) (g : ZMod p → ℝ) (hg : IsSign g)
    (heven : ∀ x, g (-x) = g x)
    (hbal : (∑ x, g x) = 1 ∨ (∑ x, g x) = -1) (lam : ℝ) (hlam : 1 ≤ lam)
    (hlower : ∀ γ : ZMod p, γ ≠ 0 → -lam ≤ (hat g γ).re) :
    (∀ γ, 0 ≤ realShiftedHat g lam γ) ∧
      ∀ γ : ZMod p, γ ≠ 0 →
        0 ≤ 3 * realShiftedHat g lam γ ^ 3 -
          (3 * (∑ x, realShiftedHat g lam x ^ 2) - (p : ℝ) ^ 2) *
            realShiftedHat g lam γ + cubicConstant g lam
```

`realShiftedHat_nonneg` derives positivity at zero from balance and `lam ≥ 1`, and away from zero from the given spectral lower bound. `cube_delete` proves the exact deletion expansion for `u = h - h(γ₀) δ_{γ₀}`. The proof uses `-γ₀ ≠ γ₀`, derived from odd primality and `γ₀ ≠ 0`; evenness gives `(h*h)(0) = ∑ h²` and `h(-γ₀)=h(γ₀)`. Thus `spectral_gap` proves the stated polynomial inequality with the actual `S₂ = ∑ h²`.

### T3(e)

```lean
theorem coefficient_upper_bound (hp : p ≠ 2) (g : ZMod p → ℝ) (hg : IsSign g)
    (heven : ∀ x, g (-x) = g x)
    (hbal : (∑ x, g x) = 1 ∨ (∑ x, g x) = -1) (hzero : g 0 = -1)
    (lam : ℝ) (hlam : 1 ≤ lam)
    (hlower : ∀ γ : ZMod p, γ ≠ 0 → -lam ≤ (hat g γ).re)
    (γ : ZMod p) (hγ : γ ≠ 0) : (hat g γ).re ≤ lam * Real.sqrt p
```

The proof uses the single nonnegative summand at `γ` to show `h(γ)² ≤ (h*h)(2γ)`. Odd primality ensures `2γ ≠ 0`; the exact square identity and `g(0)=-1` give `h(γ)² ≤ p*lam² - 2p*lam ≤ p*lam²`. Real square-root inequalities then yield the requested upper bound for `ĝ(γ)`.

## Build and axiom-check output

Both commands below ran through the required runner on **dirichlet**, using Lean 4.33.1 and the repository's pinned mathlib. Both exited with status **0**.

```sh
src/dirun.sh -c 4 -m 16 sh -c 'cd lean && ~/.elan/bin/lake build'
```

Final full-build output (the unchanged `HalfSet` module had already built successfully and was cached):

```text
✔ [8720/8722] Built ChowlaCosine.FibreSchur (13s)
✔ [8721/8722] Built ChowlaCosine (4.8s)
Build completed successfully (8722 jobs).
```

The final source built without warnings, errors, or `sorry`. The preceding successful compilation of the final `HalfSet` source reported `✔ [8719/8722] Built ChowlaCosine.HalfSet (13s)`.

```sh
src/dirun.sh -c 4 -m 16 sh -c 'cd lean && ~/.elan/bin/lake env lean ChowlaCosine/AxiomCheck.lean'
```

Complete axiom-check output:

```text
'ChowlaCosine.FibreSchur.fourier_inversion' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.FibreSchur.fourier_mul_card' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.FibreSchur.PositiveDefinite.mul' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.FibreSchur.PositiveDefinite.pow' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.FibreSchur.fourier_fibre' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.FibreSchur.shifted_fibre_positiveDefinite' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.FibreSchur.power_certificate_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.FibreSchur.fibreSet_eq_image' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.FibreSchur.quotientPower_apply' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.FibreSchur.fibre_table_three' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.FibreSchur.fibre_cube_table' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.FibreSchur.order_three_fibre_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.FibreSchur.order_three_zero_fibre' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.FibreSchur.order_three_runTops_card' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.FibreSchur.order_three_runTops_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.FibreSchur.fibre_table_four' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.FibreSchur.mem_twoRunCosets_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.FibreSchur.fibre_fourth_table' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.FibreSchur.order_four_fibre_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.FibreSchur.order_four_zero_fibre' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.HalfSet.hat_conv_hat' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.HalfSet.shiftedHat_square' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.HalfSet.shiftedHat_square_off_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.HalfSet.shiftedHat_cube' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.HalfSet.cubicConstant_eq_brief' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.HalfSet.cubicConstant_of_neg_one' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.HalfSet.shiftedHat_cube_neg_one' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.HalfSet.hat_im_eq_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.HalfSet.realShiftedHat_cast' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.HalfSet.realShiftedHat_nonneg' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.HalfSet.cube_delete' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.HalfSet.spectral_gap' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.HalfSet.coefficient_upper_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
```

All **33** audited declarations show exactly `[propext, Classical.choice, Quot.sound]`. There is no `sorryAx`, extra axiom, or native-decide axiom in the output. A local source scan of the new Lean files also found no `sorry`, `sorryAx`, `native_decide`, or axiom declaration.

## Discrepancies, counterexamples, and remaining work

No false statement or missing hypothesis was found in T0–T3. No counterexample was required. T3(c)'s general constant agrees with both expressions in the brief. The Fourier conjugation convention is explicit in `fourier_fibre`; it changes the quotient twist to division by the pulled-back character and preserves the original spectral hypothesis.

The formalization uses neither `sorry`, new axioms, nor `native_decide`. All requested statements have proofs in the new modules and have passed the remote build and axiom audit above. No target in this brief remains unfinished.
