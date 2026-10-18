# Lean agent report: P16 made unconditional (explicit constants)

Date: 2026-10-18. File: `lean/ChowlaCosine/HalfSquareExplicit.lean` (new, imported from
`lean/ChowlaCosine.lean`). `HalfSquare.lean` was not modified. No git commit was made.

## Status
- `lake build`: succeeds (8717 jobs) with no warnings, errors or `sorry`s in the new file.
- `lean/AxiomCheck.lean`: added section 10 (24 new `#check` / `#print axioms` pairs).
  `lean/AxiomCheck.out` regenerated. All 85 `#print axioms` lines in the file read
  `[propext, Classical.choice, Quot.sound]`. No `sorry`, no new axioms, no `native_decide`.
- Nothing in the task was left unproved. `IsSidon`, `buSet` and `cosSum` are unchanged. The
  conclusion is the original statement, quantified over every real `x`.

## Main theorems (Lean text)

```lean
theorem halfSquare_lower_bound_explicit (S : Finset ℤ) (hS : IsSidon S) (L : ℝ)
    (hL : ∀ s ∈ S, |(s : ℝ)| ≤ L) (hL1 : 1 ≤ L) (η : ℝ) (hη : 0 < η) (hη' : η ≤ 1 / 2)
    (hk : 1000 * (6 * L + 1) ≤ η ^ 6 * (S.card : ℝ) ^ 3) :
    ∃ x : ℝ, cosSum (buSet S) x < -((1 / 2 - η) * S.card)

theorem halfSquare_lower_bound_explicit' (S : Finset ℤ) (hS : IsSidon S) (L : ℝ)
    (hL : ∀ s ∈ S, |(s : ℝ)| ≤ L) (hL1 : 1 ≤ L) (η : ℝ) (hη : 0 < η) (hη' : η ≤ 1 / 2)
    (hk : 7000 * L ≤ η ^ 6 * (S.card : ℝ) ^ 3) :
    ∃ x : ℝ, cosSum (buSet S) x < -((1 / 2 - η) * S.card)
```

**Explicit constant:** `C = 7000` in the form `η⁶ k³ ≥ C L`. The sharper form is
`η⁶ k³ ≥ 1000 (6L + 1)`. The paper gets about 1.4e3 using Lindström's bound; we use only the
trivial Sidon count, a sum majorant that is lossy in its constants, and the crude bound `π > 3`.
Inside the proof, `h = 64 / (3 η k)`.

## Supporting theorems (Lean text)

Sidon counting (step 1):
```lean
theorem IsSidon.mono {S T : Finset ℤ} (hS : IsSidon S) (hTS : T ⊆ S) : IsSidon T
theorem injOn_sub_ltPairs_of_sidon (T : Finset ℤ) (hT : IsSidon T) :
    Set.InjOn (fun p : ℤ × ℤ => p.2 - p.1) ↑(ltPairs T)
theorem sidon_card_mul_pred_le_of_diam (T : Finset ℤ) (hT : IsSidon T) (D : ℕ)
    (hD : ∀ s ∈ T, ∀ t ∈ T, t - s ≤ (D : ℤ)) : T.card * (T.card - 1) ≤ 2 * D
theorem sidon_card_mul_pred_le_of_Ico (S : Finset ℤ) (hS : IsSidon S) (a : ℤ) (m : ℕ)
    (hm : ∀ s ∈ S, a ≤ s ∧ s < a + m) : S.card * (S.card - 1) ≤ 2 * (m - 1)
theorem le_one_add_sqrt_of_mul_pred_le {N w : ℝ} (h : N * (N - 1) ≤ w) : N ≤ 1 + Real.sqrt w
theorem sidon_card_le_one_add_sqrt_of_Ico (S : Finset ℤ) (hS : IsSidon S) (a : ℤ) (m : ℕ)
    (hm : ∀ s ∈ S, a ≤ s ∧ s < a + m) :
    (S.card : ℝ) ≤ 1 + Real.sqrt (2 * ((m : ℝ) - 1))
theorem sidon_card_mul_pred_le_real (T : Finset ℤ) (hT : IsSidon T) (w : ℝ) (hw0 : 0 ≤ w)
    (hw : ∀ s ∈ T, ∀ t ∈ T, (t : ℝ) - s ≤ w) :
    (T.card : ℝ) * ((T.card : ℝ) - 1) ≤ 2 * w
```

Counting the frequencies `b_s = 3s + 1/2` (step 2):
```lean
theorem card_filter_abs_half_le (S : Finset ℤ) (hS : IsSidon S) (u : ℝ) (hu : 0 ≤ u) :
    ((S.filter (fun s : ℤ => |3 * (s : ℝ) + 1 / 2| ≤ u)).card : ℝ) *
      (((S.filter (fun s : ℤ => |3 * (s : ℝ) + 1 / 2| ≤ u)).card : ℝ) - 1) ≤ 4 * u / 3
theorem card_filter_abs_half_le_sqrt (S : Finset ℤ) (hS : IsSidon S) (u : ℝ) (hu : 0 ≤ u) :
    ((S.filter (fun s : ℤ => |3 * (s : ℝ) + 1 / 2| ≤ u)).card : ℝ) ≤ 1 + Real.sqrt (4 * u / 3)
```

Majorant sum (step 3). Definitions:
- `absB s = |3s + 1/2|`
- `rankB S s = #{t ∈ S : absB t < absB s}`
- `telG R a ρ = if ρ < R then 1 else a/3 · (1/ρ³ − 1/(ρ+1)³)`

```lean
theorem absB_injective : Function.Injective absB
theorem absB_pos (s : ℤ) : 0 < absB s
theorem rankB_lt_rankB (S : Finset ℤ) {s t : ℤ} (hs : s ∈ S) (hst : absB s < absB t) :
    rankB S s < rankB S t
theorem rankB_injOn (S : Finset ℤ) : Set.InjOn (rankB S) ↑S
theorem rankB_lt_card (S : Finset ℤ) {s : ℤ} (hs : s ∈ S) : rankB S s < S.card
theorem rankB_bound (S : Finset ℤ) (hS : IsSidon S) {s : ℤ} (hs : s ∈ S) :
    (rankB S s : ℝ) * ((rankB S s : ℝ) + 1) ≤ 4 * absB s / 3
theorem one_div_sq_sq_le (ρ : ℝ) (hρ : 0 < ρ) :
    1 / (ρ ^ 2 * (ρ + 1) ^ 2) ≤ (1 / ρ ^ 3 - 1 / (ρ + 1) ^ 3) / 3
theorem telG_nonneg (R : ℕ) (hR : 1 ≤ R) (a : ℝ) (ha : 0 ≤ a) (ρ : ℕ) : 0 ≤ telG R a ρ
theorem sum_range_telG_le (R : ℕ) (hR : 1 ≤ R) (a : ℝ) (ha : 0 ≤ a) (n : ℕ) :
    ∑ ρ ∈ Finset.range n, telG R a ρ ≤ R + a / (3 * (R : ℝ) ^ 3)
theorem min_le_telG (S : Finset ℤ) (hS : IsSidon S) {s : ℤ} (hs : s ∈ S) (u0 : ℝ)
    (R : ℕ) (hR : 1 ≤ R) :
    min 1 (u0 ^ 2 / absB s ^ 2) ≤ telG R (16 * u0 ^ 2 / 9) (rankB S s)
theorem sum_min_absB_le (S : Finset ℤ) (hS : IsSidon S) (u0 : ℝ) (hu0 : 0 < u0) :
    ∑ s ∈ S, min 1 (u0 ^ 2 / absB s ^ 2) ≤ 1 + 4 / 3 * Real.sqrt (4 * u0 / 3)
theorem sum_min_le_sidon (S : Finset ℤ) (hS : IsSidon S) (h : ℝ) (hh : 0 < h) :
    ∑ s ∈ S, min 1 (4 / ((3 * (s : ℝ) + 1 / 2) * h) ^ 2) ≤
      1 + 4 / 3 * Real.sqrt (8 / (3 * h))
```

The numerical condition (step 4):
```lean
theorem halfSquare_hcond_explicit (k L η : ℝ) (hL1 : 1 ≤ L) (hη : 0 < η) (hη' : η ≤ 1 / 2)
    (hk0 : 0 ≤ k) (hk : 1000 * (6 * L + 1) ≤ η ^ 6 * k ^ 3) :
    24 * π / (η ^ 4 * k ^ 2) <
      2 * (η / (2 * (6 * L + 1))) *
        (⌊2 * π / (2 * (64 / (3 * (η * k))) + 2 * (η / (2 * (6 * L + 1))))⌋₊ : ℝ)
```

## Paper proof as formalized (differs from the suggested dyadic route)

1. **Sidon counting.** The positive differences are pairwise distinct and lie in `[1, D]`, so
   `k(k−1) = 2·#ltPairs ≤ 2D`. For a real diameter `w` this gives `k(k−1) ≤ 2w`.
2. **Counting `|b_s| ≤ u`.** For such `s, t`, `3(t − s) ≤ 2u`, so `N(N−1) ≤ 4u/3`.
3. **Majorant (rank argument; no integrals and no dyadic shells).**
   - The values `|b_s|` are pairwise distinct, because `3(s+t) = −1` has no integer solution.
   - Let `ρ = rank(s)`. Applying step 1 to `{t : |b_t| ≤ |b_s|}`, which has at least `ρ+1`
     elements, gives `ρ(ρ+1) ≤ 4|b_s|/3`.
   - For `ρ ≥ 1`: `u₀²/b_s² ≤ a/(ρ²(ρ+1)²) ≤ (a/3)(1/ρ³ − 1/(ρ+1)³)`, where
     `a = 16u₀²/9 = q⁴` and `q = √(4u₀/3)`.
   - The rank map is injective into `range k`, so the sum is at most `Σ_{ρ<k} telG(ρ)`. The
     terms telescope to at most `R + a/(3R³)`.
   - With `R = ⌈q⌉`: `R + a/(3R³) ≤ (q + 1) + q/3 = 1 + (4/3)q`.
   - The constant `4/3·√(4/3)` matches what Abel summation gives with the trivial count.
4. **Choosing `h`.**
   - Write `z = η²k`. Then `z³ = η⁶k³ ≥ 7000`, so `z ≥ 19`, and `ηk ≥ 2z ≥ 38`.
   - With `h = 64/(3ηk)`: `8/(3h) = ηk/8`, so the majorant is at most
     `1 + (4/3)√(ηk/8) < 2√(ηk/8) ≤ √(ηk/2)`. This uses `√(ηk/8) ≥ 2`.
   - The floor condition:
     - `r ≤ 1/28` and `h ≤ 64/114`, so `Q = 2π/(2h+2r) ≥ 5`.
     - Hence `⌊Q⌋ > Q − 1 ≥ (4/5)Q`.
     - It then remains to show `15(h + r) ≤ rη⁴k²`. Writing `D = 6L + 1`, this is equivalent
       to `1920·D + 45z ≤ 3η⁶k³`.
     - That follows from `η⁶k³ ≥ 1000·D` and `361z ≤ z³`.

## Remarks for the lead agent
- **What this does and does not cover.** This is a rigorous lower bound on `M(A(S))` for one
  construction class only: Bu et al.'s `A(S)` with `S` Sidon. Any Sidon `S ⊆ [−L, L]` satisfies
  `k(k−1) ≤ 4L` (`sidon_card_mul_pred_le_real`), so `L ≥ k(k−1)/4`.
- **When the hypothesis applies.** It needs `L = O(η⁶k³)`. For dense Sidon sets (`L ≈ k²`) it
  holds once `k ≳ 7000/η⁶`.
- **What it gives in that regime.** `M(A(S)) > (1/2 − η)k`, where `|A(S)| = k(k−1)` by
  `card_buSet`. So `R(A(S)) > 1/2 − η`, which shows this family cannot push the ratio
  `R(A)` below `1/2`.
- **What it says nothing about.** Sets that are not of the form `buSet S`, and the full Chowla
  conjecture.
- **Tightening the constant.** `C = 7000` could likely be brought to about 4000–5000 with more
  careful numerics (e.g. `π > 3.14`, a better choice of `h`). Lindström's bound is not
  formalized here.
