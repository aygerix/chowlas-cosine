# P34 Lean formalization report

Status: COMPLETE — all assigned primary and secondary targets are kernel checked under the permitted standard axioms. No assigned target remains open.

## Results

| Target | Checked result | Location |
|---|---|---|
| P34-main | Exact window energy inequality, arbitrary complex coefficients; exact real cosine/sine form with the sum over 1..min(w,n); coefficient-bounded S_w consequence | `lean/ChowlaCosine/P34/Main.lean:39`, `lean/ChowlaCosine/P34/RealForm.lean:51` |
| P34-A | sqrt(n)/4 ≤ M for every n≥1 and every unit-amplitude coefficient vector; explicitly arbitrary real phases | `lean/ChowlaCosine/P34/Corollaries.lean:60`, `lean/ChowlaCosine/P34/RealForm.lean:103` |
| P34-B | Both attained Littlewood excursions, including ε₀ and every n≥1 | `lean/ChowlaCosine/P34/Littlewood.lean:66` |
| P34-C | E≥(41/100)n and squared amplitudes≤1 imply sqrt(n)/1000≤M; every n including 0 | `lean/ChowlaCosine/P34/Corollaries.lean:126`, `lean/ChowlaCosine/P34/RealForm.lean:109` |
| P33 ratio | M ≥ card(A)·m/X for arbitrary positive lower and upper frequency bounds, and the requested min/max specialization | `lean/ChowlaCosine/P34/Secondary.lean:106`, `lean/ChowlaCosine/P34/Secondary.lean:151` |
| Dilation pinch | Exact roots-of-unity sum and requested cardinality inequality for every q≥1 | `lean/ChowlaCosine/P34/Secondary.lean:160`, `lean/ChowlaCosine/P34/Secondary.lean:166` |

## Verification

Toolchain: `leanprover/lean4:v4.33.1`; existing project dependencies unchanged.

Commands run in `lean/`:

```sh
LEAN_NUM_THREADS=1 lake build
LEAN_NUM_THREADS=1 lake env lean AxiomCheck.lean
```

Both returned exit code 0. The full build ends with `Build completed successfully (8745 jobs).` All six new P34 modules and the top-level library were rebuilt. The P34 modules produced no build warnings; the build log replays pre-existing warnings elsewhere.

Logs:

- Full build: `.research/agents/lean_p34_scratch/lake_build.log`.
- Full existing-plus-new axiom check: `.research/agents/lean_p34_scratch/axioms.log`.
- Extracted literal P34 axiom output: `.research/agents/lean_p34_scratch/p34_axioms.txt`.
- Individual milestone elaboration logs: `moments.log`, `main.log`, `corollaries.log`, `real_form.log`, `littlewood.log`, and `secondary.log` in the same directory.

`lean/AxiomCheck.lean:508` begins the new headline checks. The audit covers all 49 new public theorem declarations, with no missing checks. Every one reports exactly `[propext, Classical.choice, Quot.sound]`. No `sorryAx` or other axiom occurs in the new theorem dependencies. A source scan of the six new Lean files found no `sorry`, `axiom`, or `native_decide`. `git diff --check` passed.

## Definitions and proof structure

All new results are in namespace `ChowlaCosine.P34`; `P31` is opened. The definitions are:

- `windowFreq n = Finset.Icc 1 n`, reused from P31.
- `trigSum A b x = Σ j∈A, Re(b_j * exp(i j x))`.
- `energy A b = Σ j∈A, ‖b_j‖²`.
- `windowEnergy w A b = Σ j∈A, (kappa w j)² * ‖b_j‖²`.
- `coefficients a c j = a_j - i c_j`, so `realTrigSum n a c x = Σ j=1..n (a_j cos(jx)+c_j sin(jx))` and `realEnergy n a c = Σ j=1..n (a_j²+c_j²)`.
- `littlewoodSum n ε x = Σ j=0..n ε_j cos(jx)`.
- `circleMean`, `kappa`, `windowMass`, `fejerKernel`, `FejerRiesz`, `AnalyticNikolskii`, and `elementaryC` are the existing P31 definitions. The circle mean is the exact integral with measure dx/(2π), and `elementaryC L = (811/1000)(L+1)+71/300`.

P34-main proves the new complex orthogonality and Fejér convolution identities, controls the trigonometric degree, then directly reuses P31's `averaged_window_bound`, `finite_fejerRiesz`, and `elementary_analyticNikolskii`. The exact main theorem retains its stated analytic hypotheses; `p34_elementary` discharges both hypotheses using the checked P31 theorems. No factorization, positivity, or analytic Nikolskii infrastructure is duplicated.

P34-A uses w=floor(n/2) for all n≥1. After clearing positive denominators, the strict arithmetic gap has numerator proportional to w(2907w²+49504w+65285) for n=2w (w≥1), and (2w+1)(2907w²+47071w+64272) for n=2w+1 (w≥0). This supplies one uniform proof without a finite exception list. The arbitrary-phase wrapper uses the exact coefficients exp(-iθ_j).

P34-B uses continuity, exact periodicity and compactness to attain a global minimum, then applies P34-A to b and -b. The constant ε₀ is retained explicitly in `littlewoodSum_eq`.

P34-C reuses the P31 ε=1/200, n≥2000 arithmetic. For smaller positive n, integration of g²≤(M+n)g gives E≤2nM, hence M≥41/200 from the density hypothesis. The final bound is in sqrt(n), not sqrt(E). The n=0 case is included.

P33 uses nonnegative Fejér weights K_(m-1) on the q=X+m roots of unity. For each m≤a≤X, the weighted cosine sum is exactly zero. The total weight is q, and the zero-angle weight is m, giving m(|A|+M)≤Mq and thus |A|m≤MX. The min/max specialization is fully proved. Dilation reuses the exact averaging identity already in `ChowlaCosine/Averaging.lean` and treats q=1 explicitly.

## Scope and remaining work

No weakening of any requested statement: lower-bound hypotheses still quantify over every real x; phases are arbitrary; every n≥1 is covered; P34-B includes j=0; the dense conclusion is sqrt(n)/1000; and dilation includes q=1. There are no open assigned targets or unproved analytic hypotheses in the A/B/C corollaries. The optional improved asymptotic constant was not a required target and is not claimed here.

No commits were made and no subagents were launched. No research Markdown was modified except this explicitly requested report. The pre-existing P31 files and project dependencies were left unchanged. New source lives in the six files under `lean/ChowlaCosine/P34/`, exported by `lean/ChowlaCosine.lean`; `lean/AxiomCheck.lean` contains the checks.

## Exact Lean statements

### `circleMean_trigSum_mul`

`lean/ChowlaCosine/P34/Moments.lean:67`

```lean
theorem circleMean_trigSum_mul (A : Finset ℕ) (b c : ℕ → ℂ)
    (hA : ∀ j ∈ A, 0 < j) :
    circleMean (fun x => trigSum A b x * trigSum A c x) =
      (∑ j ∈ A, (b j * star (c j)).re) / 2
```

### `circleMean_trigSum_add_sq`

`lean/ChowlaCosine/P34/Moments.lean:88`

```lean
theorem circleMean_trigSum_add_sq (A : Finset ℕ) (b : ℕ → ℂ) (M : ℝ)
    (hA : ∀ j ∈ A, 0 < j) :
    circleMean (fun x => (trigSum A b x + M) ^ 2) = M ^ 2 + energy A b / 2
```

### `circleMean_fejer_mul_re`

`lean/ChowlaCosine/P34/Moments.lean:115`

```lean
theorem circleMean_fejer_mul_re (w : ℕ) {j : ℕ} (hj : 0 < j) (b : ℂ) (y : ℝ) :
    circleMean (fun x => fejerKernel w (x - y) *
      (b * circleCharacter (j : ℤ) x).re) =
        kappa w j * (b * circleCharacter (j : ℤ) y).re
```

### `circleMean_window_mean_sq`

`lean/ChowlaCosine/P34/Moments.lean:181`

```lean
theorem circleMean_window_mean_sq (w : ℕ) (A : Finset ℕ) (b : ℕ → ℂ) (M : ℝ)
    (hA : ∀ j ∈ A, 0 < j) :
    circleMean (fun y => circleMean
      (fun x => fejerKernel w (x - y) * (trigSum A b x + M)) ^ 2) =
        M ^ 2 + windowEnergy w A b / 2
```

### `p34_main`

`lean/ChowlaCosine/P34/Main.lean:39`

```lean
theorem p34_main (w n : ℕ) (A : Finset ℕ) (b : ℕ → ℂ) (M C : ℝ)
    (hA : ∀ j ∈ A, 0 < j) (hn : ∀ j ∈ A, j ≤ n)
    (hM : ∀ x : ℝ, -M ≤ trigSum A b x)
    (hFR : FejerRiesz (n + w)) (hnik : AnalyticNikolskii (n + w) C) :
    windowMass w * (M ^ 2 + energy A b / 2) ≤
      C * (M ^ 2 + windowEnergy w A b / 2)
```

### `p34_main_bounded`

`lean/ChowlaCosine/P34/Main.lean:88`

```lean
theorem p34_main_bounded (w n : ℕ) (A : Finset ℕ) (b : ℕ → ℂ) (M C : ℝ)
    (hA : ∀ j ∈ A, 0 < j) (hn : ∀ j ∈ A, j ≤ n)
    (hb : ∀ j ∈ A, ‖b j‖ ^ 2 ≤ 1) (hM : ∀ x : ℝ, -M ≤ trigSum A b x)
    (hFR : FejerRiesz (n + w)) (hnik : AnalyticNikolskii (n + w) C) :
    windowMass w * (M ^ 2 + energy A b / 2) ≤
      C * (M ^ 2 + (∑ j ∈ windowFreq w, kappa w j ^ 2) / 2)
```

### `p34_elementary`

`lean/ChowlaCosine/P34/Main.lean:99`

```lean
theorem p34_elementary (w n : ℕ) (A : Finset ℕ) (b : ℕ → ℂ) (M : ℝ)
    (hA : ∀ j ∈ A, 0 < j) (hn : ∀ j ∈ A, j ≤ n)
    (hb : ∀ j ∈ A, ‖b j‖ ^ 2 ≤ 1) (hM : ∀ x : ℝ, -M ≤ trigSum A b x) :
    windowMass w * (M ^ 2 + energy A b / 2) ≤
      elementaryC (n + w) * (M ^ 2 + (windowMass w - 1) / 4)
```

### `p34_main_real`

`lean/ChowlaCosine/P34/RealForm.lean:51`

```lean
theorem p34_main_real (w n : ℕ) (a c : ℕ → ℝ) (M C : ℝ)
    (hM : ∀ x : ℝ, -M ≤ realTrigSum n a c x)
    (hFR : FejerRiesz (n + w)) (hnik : AnalyticNikolskii (n + w) C) :
    windowMass w * (M ^ 2 + realEnergy n a c / 2) ≤
      C * (M ^ 2 + (∑ j ∈ windowFreq (min w n),
        kappa w j ^ 2 * (a j ^ 2 + c j ^ 2)) / 2)
```

### `p34_main_real_bounded`

`lean/ChowlaCosine/P34/RealForm.lean:62`

```lean
theorem p34_main_real_bounded (w n : ℕ) (a c : ℕ → ℝ) (M C : ℝ)
    (hb : ∀ j ∈ windowFreq n, a j ^ 2 + c j ^ 2 ≤ 1)
    (hM : ∀ x : ℝ, -M ≤ realTrigSum n a c x)
    (hFR : FejerRiesz (n + w)) (hnik : AnalyticNikolskii (n + w) C) :
    windowMass w * (M ^ 2 + realEnergy n a c / 2) ≤
      C * (M ^ 2 + (∑ j ∈ windowFreq w, kappa w j ^ 2) / 2)
```

### `p34_A`

`lean/ChowlaCosine/P34/Corollaries.lean:60`

```lean
theorem p34_A (n : ℕ) (hn : 1 ≤ n) (b : ℕ → ℂ) (M : ℝ)
    (hb : ∀ j ∈ windowFreq n, ‖b j‖ ^ 2 = 1)
    (hM : ∀ x : ℝ, -M ≤ trigSum (windowFreq n) b x) :
    Real.sqrt n / 4 ≤ M
```

### `p34_A_real`

`lean/ChowlaCosine/P34/RealForm.lean:75`

```lean
theorem p34_A_real (n : ℕ) (hn : 1 ≤ n) (a c : ℕ → ℝ) (M : ℝ)
    (hb : ∀ j ∈ windowFreq n, a j ^ 2 + c j ^ 2 = 1)
    (hM : ∀ x : ℝ, -M ≤ realTrigSum n a c x) : Real.sqrt n / 4 ≤ M
```

### `p34_A_phases`

`lean/ChowlaCosine/P34/RealForm.lean:103`

```lean
theorem p34_A_phases (n : ℕ) (hn : 1 ≤ n) (θ : ℕ → ℝ) (M : ℝ)
    (hM : ∀ x : ℝ, -M ≤ ∑ j ∈ windowFreq n, Real.cos ((j : ℝ) * x - θ j)) :
    Real.sqrt n / 4 ≤ M
```

### `p34_A_exists_le`

`lean/ChowlaCosine/P34/Littlewood.lean:34`

```lean
theorem p34_A_exists_le (n : ℕ) (hn : 1 ≤ n) (b : ℕ → ℂ)
    (hb : ∀ j ∈ windowFreq n, ‖b j‖ ^ 2 = 1) :
    ∃ x : ℝ, trigSum (windowFreq n) b x ≤ -Real.sqrt n / 4
```

### `p34_A_exists_ge`

`lean/ChowlaCosine/P34/Littlewood.lean:43`

```lean
theorem p34_A_exists_ge (n : ℕ) (hn : 1 ≤ n) (b : ℕ → ℂ)
    (hb : ∀ j ∈ windowFreq n, ‖b j‖ ^ 2 = 1) :
    ∃ x : ℝ, Real.sqrt n / 4 ≤ trigSum (windowFreq n) b x
```

### `p34_B`

`lean/ChowlaCosine/P34/Littlewood.lean:66`

```lean
theorem p34_B (n : ℕ) (hn : 1 ≤ n) (ε : ℕ → ℝ)
    (hε : ∀ j : ℕ, ε j = -1 ∨ ε j = 1) :
    (∃ x : ℝ, littlewoodSum n ε x ≤ 1 - Real.sqrt n / 4) ∧
      (∃ x : ℝ, Real.sqrt n / 4 - 1 ≤ littlewoodSum n ε x)
```

### `p34_C`

`lean/ChowlaCosine/P34/Corollaries.lean:126`

```lean
theorem p34_C (n : ℕ) (b : ℕ → ℂ) (M : ℝ)
    (hb : ∀ j ∈ windowFreq n, ‖b j‖ ^ 2 ≤ 1)
    (hdensity : (41 / 100 : ℝ) * n ≤ energy (windowFreq n) b)
    (hM : ∀ x : ℝ, -M ≤ trigSum (windowFreq n) b x) :
    Real.sqrt n / 1000 ≤ M
```

### `p34_C_real`

`lean/ChowlaCosine/P34/RealForm.lean:109`

```lean
theorem p34_C_real (n : ℕ) (a c : ℕ → ℝ) (M : ℝ)
    (hb : ∀ j ∈ windowFreq n, a j ^ 2 + c j ^ 2 ≤ 1)
    (hdensity : (41 / 100 : ℝ) * n ≤ realEnergy n a c)
    (hM : ∀ x : ℝ, -M ≤ realTrigSum n a c x) : Real.sqrt n / 1000 ≤ M
```

### `p33_ratio`

`lean/ChowlaCosine/P34/Secondary.lean:106`

```lean
theorem p33_ratio (A : Finset ℕ) (hne : A.Nonempty) (m X : ℕ) (hm : 1 ≤ m)
    (hlo : ∀ a ∈ A, m ≤ a) (hhi : ∀ a ∈ A, a ≤ X)
    (M : ℝ) (hM : ∀ x : ℝ, -M ≤ cosSum A x) :
    (A.card : ℝ) * m / X ≤ M
```

### `p33_ratio_min_max`

`lean/ChowlaCosine/P34/Secondary.lean:151`

```lean
theorem p33_ratio_min_max (A : Finset ℕ) (hne : A.Nonempty)
    (hA : ∀ a ∈ A, 0 < a) (M : ℝ) (hM : ∀ x : ℝ, -M ≤ cosSum A x) :
    (A.card : ℝ) * A.min' hne / A.max' hne ≤ M
```

### `dilation_identity`

`lean/ChowlaCosine/P34/Secondary.lean:160`

```lean
theorem dilation_identity (A : Finset ℕ) (q : ℕ) (hq : 1 ≤ q) :
    (∑ j ∈ Finset.range q, cosSum A (2 * π * j / q)) =
      (q : ℝ) * (A.filter (fun a => q ∣ a)).card
```

### `dilation_pinch`

`lean/ChowlaCosine/P34/Secondary.lean:166`

```lean
theorem dilation_pinch (A : Finset ℕ) (q : ℕ) (hq : 1 ≤ q) (M : ℝ)
    (hM : ∀ x : ℝ, -M ≤ cosSum A x) :
    (A.card : ℝ) / q - (1 - 1 / (q : ℝ)) * M ≤ (A.filter (fun a => q ∣ a)).card
```

## Literal `#print axioms` output for every new public theorem

```text
'ChowlaCosine.P34.circleMean_trigSum_mul' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.circleMean_trigSum_add_sq' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.circleMean_fejer_mul_re' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.circleMean_window_mean_sq' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.p34_main' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.p34_main_bounded' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.p34_elementary' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.p34_main_real' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.p34_main_real_bounded' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.p34_A' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.p34_A_real' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.p34_A_phases' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.p34_A_exists_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.p34_A_exists_ge' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.p34_B' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.p34_C' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.p34_C_real' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.p33_ratio' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.p33_ratio_min_max' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.dilation_identity' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.dilation_pinch' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.energy_eq_card' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.windowMass_le_succ' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.circleCharacter_norm' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.trigSum_le_card' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.energy_le_two_card_mul' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.trigSum_periodic' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.trigSum_exists_min' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.trigSum_neg' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.littlewoodSum_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.re_character_mem_trigBand' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.trigSum_add_mem_trigBand' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.nikolskii_constant_one_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.windowEnergy_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.nonneg_of_trigSum_ge' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.continuous_trigSum' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.circleMean_trigSum' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.re_mul_re' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.circleMean_re_character_mul' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.circleCharacter_re' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.circleCharacter_im' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.circleMean_window' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.coefficients_norm_sq' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.trigSum_coefficients' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.energy_coefficients' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.windowEnergy_interval' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.phaseCoefficients_norm_sq' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.trigSum_phase' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P34.fejerKernel_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
```
