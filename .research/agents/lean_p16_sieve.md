# Lean agent report: P16′ (exponent 1/5 via Gallagher large sieve)

Date: 2026-10-18. File: `lean/ChowlaCosine/HalfSquareSieve.lean` (new, about 600 lines), imported from
`lean/ChowlaCosine.lean`. No existing statement was modified. Nothing committed to git.

## Status
- `lake build`: succeeds (8718 jobs). No errors, no warnings, no `sorry`, no new axioms, no `native_decide`.
- `lean/AxiomCheck.lean`: added section 11 (18 new `#check` / `#print axioms` pairs). Regenerated
  `lean/AxiomCheck.out`: all 103 `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`.
- Status: **kernel-checked** (same definitions `cosSum`, `buSet`, `IsSidon`, `halfC`, `halfP` as before;
  the conclusion is about a real `x` with a strict inequality; no grids anywhere).

## Main theorem (constant C0 = 600)
```lean
theorem halfSquare_lower_bound_sieve (S : Finset ℤ) (hS : IsSidon S) (L : ℝ)
    (hL : ∀ s ∈ S, |(s : ℝ)| ≤ L) (hL1 : 1 ≤ L) (η : ℝ) (hη : 0 < η) (hη' : η ≤ 1 / 2)
    (hk : 600 * (6 * L + 1) ≤ η ^ 5 * (S.card : ℝ) ^ 3) :
    ∃ x : ℝ, cosSum (buSet S) x < -((1 / 2 - η) * S.card)

theorem halfSquare_lower_bound_sieve' ... (hk : 4200 * L ≤ η ^ 5 * (S.card : ℝ) ^ 3) :
    ∃ x : ℝ, cosSum (buSet S) x < -((1 / 2 - η) * S.card)
```
No extra side conditions. The method also needs `η⁴ k² ≥ const`. Without it a 4th-moment argument cannot see
depth `ηk` below the typical size `√k` of `C`. In the proof this follows from the Sidon counting bound
`k(k-1) ≤ 4L` (`sidon_card_mul_pred_le_real`), which gives `k² ≤ 2(6L+1)` and then `η⁵k ≥ 300`, `ηk ≥ 4800`,
`η⁴k² ≥ 600` (`sieve_numerics`).

## Gallagher's inequality (separately named)
```lean
theorem gallagher_local {φ φ' : ℝ → ℝ} (hφ : ∀ x, HasDerivAt φ (φ' x) x) (hφ' : Continuous φ')
    {a b y : ℝ} (hab : a ≤ b) (hy : y ∈ Set.Icc a b) :
    (b - a) * φ y ≤ (∫ x in a..b, φ x) + (b - a) * ∫ x in a..b, |φ' x|

theorem gallagher_sum {φ φ' : ℝ → ℝ} (hφ : ∀ x, HasDerivAt φ (φ' x) x) (hφ' : Continuous φ')
    (hφ0 : ∀ x, 0 ≤ φ x) {T : ℝ} (hT : 0 ≤ T) (hφT : Function.Periodic φ T)
    (hφ'T : Function.Periodic φ' T) {δ0 : ℝ} (hδ0 : 0 < δ0) (c0 : ℝ) (y : ℕ → ℝ) (m : ℕ)
    (hgap : ∀ j, j + 1 < m → y j + δ0 ≤ y (j + 1))
    (hlo : ∀ j < m, c0 ≤ y j - δ0 / 2) (hhi : ∀ j < m, y j + δ0 / 2 ≤ c0 + T) :
    ∑ j ∈ Finset.range m, φ (y j) ≤ 1 / δ0 * (∫ x in (0 : ℝ)..T, φ x) + ∫ x in (0 : ℝ)..T, |φ' x|
```
Note on the paper statement. The lead's version lets the intervals `I_j` lie in a window of length `2π + δ0`
and then folds by periodicity. That would double-count the overlap. The formal version requires
`[y_j - δ0/2, y_j + δ0/2] ⊆ [c0, c0 + T]`. Step D satisfies this exactly: the windows are centred at `4hj`,
`δ0 = 2h`, `c0 = -2h`, and `4hm ≤ 2π`.

## Derivative term (Bernstein-type, applied to C⁴)
With `halfS S x = Σ_s (6s+1) sin((6s+1)x)` and `hasDerivAt_halfC : HasDerivAt (halfC S) (-halfS S x) x`:
```lean
theorem integral_halfC_sq_mul_halfS_sq_le (S : Finset ℤ) (D : ℝ)
    (hD : ∀ s ∈ S, |((6 * s + 1 : ℤ) : ℝ)| ≤ D) :
    ∫ x in (0:ℝ)..2*π, halfC S x ^ 2 * halfS S x ^ 2 ≤ D ^ 2 * ∫ x in (0:ℝ)..2*π, halfC S x ^ 4
theorem integral_abs_halfC_cube_mul_halfS_le (S) (D) (hDpos : 0 < D) (hD : ...) :
    ∫ x in (0:ℝ)..2*π, |halfC S x ^ 3 * halfS S x| ≤ D * ∫ x in (0:ℝ)..2*π, halfC S x ^ 4
theorem sieve_halfC_pow_four (S) (D) (hDpos : 0 < D) (hD : ...) {δ0} (hδ0 : 0 < δ0) (c0) (y : ℕ → ℝ) (m)
    (hgap ...) (hlo ...) (hhi : ∀ j < m, y j + δ0 / 2 ≤ c0 + 2 * π) :
    ∑ j ∈ Finset.range m, halfC S (y j) ^ 4 ≤ (1 / δ0 + 4 * D) * ∫ x in (0:ℝ)..2*π, halfC S x ^ 4
```
- The first bound needs **no Sidon hypothesis**. Both 4-fold expansions are compared term by term. Since all
  frequencies are `≡ 1 mod 6`, the mixed `cc(diff, sum)` terms vanish. What is left is
  `β_c β_d (X − Y)/4 ≤ D²(X + Y)/4` with `X, Y ≥ 0`.
- The second bound is pointwise AM-GM, `|C³S'| ≤ (D C⁴ + C²S'²/D)/2`, then the first bound. No Cauchy–Schwarz
  or Parseval is needed.
- So `c1 = 4`: `Σ_j C(y_j)⁴ ≤ (1/δ0 + 4D) ∫C⁴`.

## Proof parameters used
- `θ = 1/2`, i.e. `δ = √(ηk/2)`.
- `h = 64/(3ηk)`. This reuses the visit machinery of `HalfSquareExplicit.lean`: `halfP_visit_explicit` packages
  `sum_min_le_sidon`, `sinc_sq_le_min` and `exists_visit_of_sinc_sum_lt`.
- At a visit, `C(y) < -ηk`.
- Gallagher is applied with `δ0 = 2h` to `m = ⌊π/(2h)⌋` visits.
- The final arithmetic (`sieve_arith`) reduces to `3η⁵k³ ≥ 9ηk + 1536·D`. This holds when `η⁵k³ ≥ 600 D` and
  `η⁴k² ≥ 600`.

## Gaps / caveats
- No unproved parts.
- C0 = 600 is not optimized. A heuristic estimate (not formalized) suggests that `θ = 1/5`, a smaller `δ0`
  relative to the window spacing, and tighter visit constants could bring C0 down to the order of 100.
- New helper names are in namespace `ChowlaCosine`: `sum_integral_le_of_sorted`, `halfS`, `continuous_halfS`,
  `halfS_periodic`, `cc_nonneg`, `sin_mul_sin_int`, `integral_cos_cos_mul_sin_mul_sin`, `sum_sq_mul_sum_sq`,
  `sieve_numerics`, `sieve_arith`.
