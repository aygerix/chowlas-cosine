# The half constant is sharp for Bu et al.'s square construction

Status: **PROVED on paper** (lead, 2026-10-18; independently reviewed, `.research/agents/p16_review.md`) and
**KERNEL-CHECKED** in Lean 4 + mathlib (axioms `propext`, `Classical.choice`, `Quot.sound` only; no `sorry`), files
`lean/ChowlaCosine/HalfSquare.lean`, `HalfSquareExplicit.lean`, `HalfSquareSieve.lean`. Nothing here concerns Epoch's
`solution(c, n)`: this is a lower bound for a construction class, not a construction.

## 1. Setting

For a finite set `A` of positive integers, `f_A(x) = Σ_{a∈A} cos(ax)`, `M(A) = −min_x f_A(x)`, `R(A) = M(A)/√|A|`.

Bu, Khan, Yi, Jha, Vajpeyi, Chandupatla, Nagpal (arXiv:2610.17160v1, 12 Oct 2026) take a Sidon set `S ⊂ Z`, `|S| = k`,
and

    A(S) = {3(t − s) : s < t in S} ∪ {|3(s + t) + 1| : s < t in S},

a set of `k(k−1)` positive integers whenever `S` is Sidon in the strong sense (every additive quadruple
`a + b = c + d` in `S`, repetitions allowed, is trivial — Lean `IsSidon`, `card_buSet`). Choosing `S` from thinned,
shifted Singer sets they prove `min_x f_{A(S)} ≥ −√n/2 − O(n^{1/4}√log n)` with `n = k(k−1)`, i.e. `R(A(S)) ≤ 1/2 + o(1)`,
and remark that they do not prove sharpness.

## 2. Theorem (kernel-checked)

**Theorem.** Let `S ⊂ Z` be Sidon (strong sense), `k = |S|`, and `L ≥ 1` with `|s| ≤ L` for all `s ∈ S`. Let
`0 < η ≤ 1/2`. If

    η^5 k^3 ≥ 600 (6L + 1)                 (in particular if η^5 k^3 ≥ 4200 L),

then there is a real `x` with `f_{A(S)}(x) < −(1/2 − η) k`. Consequently `R(A(S)) > (1/2 − η)·k/√(k(k−1)) > 1/2 − η`.

Lean: `ChowlaCosine.halfSquare_lower_bound_sieve` (and `halfSquare_lower_bound_sieve'` for `4200·L`):

    theorem halfSquare_lower_bound_sieve (S : Finset ℤ) (hS : IsSidon S) (L : ℝ)
        (hL : ∀ s ∈ S, |(s : ℝ)| ≤ L) (hL1 : 1 ≤ L) (η : ℝ) (hη : 0 < η) (hη' : η ≤ 1 / 2)
        (hk : 600 * (6 * L + 1) ≤ η ^ 5 * (S.card : ℝ) ^ 3) :
        ∃ x : ℝ, cosSum (buSet S) x < -((1 / 2 - η) * S.card)

**Corollary.** Along any family with `L = o(k^3)` — in particular Bu et al.'s, where `L ≍ k^2` (their sets have
`L ≈ 8–32 k^2`) — `R(A(S)) ≥ 1/2 − O((L/k^3)^{1/5}) → 1/2`. With their upper bound, `R(A(S)) → 1/2` exactly: the
square-identity route cannot go below the constant 1/2, confirming their heuristic remark ("below 1/2 appears to require
an idea outside the square-identity paradigm") for this class. An earlier kernel-checked form with rate `(L/k^3)^{1/6}`
is `halfSquare_lower_bound_explicit` (hypothesis `η^6 k^3 ≥ 1000(6L+1)`).

## 3. Proof

Notation: `b_s = 3s + 1/2`, `P(x) = Σ_s cos(b_s x)`, `C(x) = Σ_s cos((6s+1)x)`, `D = 6L + 1`.

**Step 0 (exact identity; P15).** `2cos(b_s x)cos(b_t x) = cos(3(s−t)x) + cos((3(s+t)+1)x)` and
`cos²(b_s x) = (1 + cos((6s+1)x))/2`, so for Sidon `S`

    f_{A(S)}(x) = P(x)^2 − k/2 − C(x)/2.                         (Lean: cosSum_buSet_of_sidon)

**Step 1 (fourth moment).** `(1/2π)∫_0^{2π} C^4 = 3k^2/4 − 3k/8`. Writing a zero-sum quadruple of frequencies as
`Σ σ_i (6s_i + 1) = 0`, reduction mod 6 forces two `+` and two `−` signs, and then Sidon makes the quadruple trivial;
the count is `6(2k^2 − k)`. (Lean: `normalized_halfC_pow_four`.)

**Step 2 (visit lemma).** Let `δ > 0` and `h > 0` with `Σ_s min(1, 4/(|b_s| h)^2) < δ`. Then every interval of
half-length `h` contains `y` with `|P(y)| < δ`. Proof: if `|P| ≥ δ` on `[c−h, c+h]`, `P` has constant sign there; testing
against the triangle kernel of half-width `h` (Fourier transform `sinc^2(νh/2) ≤ min(1, 4/(νh)^2)`, nonnegative) gives
`δ ≤ Σ_s sinc^2(|b_s| h/2) < δ`. The `|b_s|` are distinct, and a Sidon set meets at most `≈ √(2t/3)` integers of
`{s : |b_s| ≤ t}`; summing gives `Σ_s min(1, 4/(|b_s|h)^2) ≤ 1 + (4/3)√(8/(3h))` (Lean: `sum_min_le_sidon`).

**Step 3 (depth at visits).** Suppose, for contradiction, `f_{A(S)} ≥ −(1/2 − η)k` everywhere. Take `δ = √(ηk/2)` and
`h = 64/(3ηk)`; Step 2 applies once `ηk > 18`. At a visit `y`, Step 0 gives
`C(y) ≤ 2P(y)^2 − 2ηk < 2δ^2 − 2ηk = −ηk`. (Lean: `halfP_visit_explicit`.)

**Step 4 (Gallagher sieve).** Put windows of half-length `h` at centres `4hj`, `0 ≤ j < m = ⌊π/(2h)⌋`; each contains
a visit `y_j` with `C(y_j)^4 > (ηk)^4`, and the windows `[y_j − h, y_j + h]` are pairwise disjoint and lie in one
period window `[−2h, −2h + 2π]`. Gallagher's inequality for the nonnegative `2π`-periodic `φ = C^4`,

    Σ_j φ(y_j) ≤ (1/δ0) ∫_0^{2π} φ + ∫_0^{2π} |φ'|,   δ0 = 2h  (windows inside ONE period window),

together with `∫|(C^4)'| = 4∫|C^3 C'| ≤ 4D ∫ C^4` (pointwise AM–GM plus `∫C^2C'^2 ≤ D^2∫C^4`, which holds because all
frequencies are `≡ 1 mod 6`) gives

    m (ηk)^4 < Σ_j C(y_j)^4 ≤ (1/(2h) + 4D) · 2π (3k^2/4 − 3k/8).

(Lean: `gallagher_local`, `gallagher_sum`, `integral_halfC_sq_mul_halfS_sq_le`, `integral_abs_halfC_cube_mul_halfS_le`,
`sieve_halfC_pow_four`.) Substituting `h = 64/(3ηk)` reduces the contradiction to `3η^5k^3 ≥ 9ηk + 1536 D`
(`sieve_arith`). That follows from `η^5k^3 ≥ 600 D`, using the Sidon count `k(k−1) ≤ 4L`, which forces `ηk ≥ 4800`
(`sieve_numerics`). ∎

*Why this is the 1/2.* `Σ_s cos²(b_s x) = k/2 + C/2` concentrates at `k/2` (fourth moment `O(k^2)`), and a real cosine
sum with no low frequencies cannot avoid small values on any window of length `≫ 1/k`. So at some near-zero of `P`,
`f ≈ −k/2`.

## 4. Remarks and limits

- **Rate.** The large-sieve version (`PROOFS.md` P16′, Montgomery–Vaughan) has better constants: `R(A(S)) ≥ 0.459`
  at `k = 10^8` for `L = k^2/2`, and `≥ 0.407` for `L = 32k^2`. The Lean constant 600 is not optimised.
- **Scope.** The same proof covers the dilate/shift family `{q|s−t|} ∪ {|q(s+t)+r|}` with `q ≥ 3`, `q ∤ 2r`
  (paper level, `PROOFS.md` G1). Every real-square identity `f = P^2 − Σcos²` with Sidon-type frequency structure is
  pinned at 1/2. Sums of several squares are worse (P15 remark; E22).
- **Not covered.** Subsets of `A(S)` (other thinnings), and Sidon sets with range `L ≫ k^3` and a dense core near 0.
  These are outside the theorem, not counterexamples to it.
- **Finite data consistent with the theorem.** Singer–Bu sets with the best shift have certified `R ≤ 0.5627` at
  `n = 63252` (`CERTIFICATES.md` C-SB), decreasing like `1/2 + 0.95/√k` toward 1/2 from above.
- **Novelty.** As of 2026-10-18, alphaXiv lists no work after 2610.17160 on this question. That is not proof of novelty.
