# Lean P21 report (Lean agent, 2026-10-18)

Brief: `.research/agents/lean_p21_brief.md`. Files: `lean/ChowlaCosine/RunTopGroup.lean` (468 lines),
`lean/ChowlaCosine/NegDefFibre.lean` (134 lines, optional task 5). Nothing committed.

## 1. Status

| theorem (`ChowlaCosine.RunTopGroup.`) | status |
|---|---|
| `runSet_neg` (A = −A) | proved, kernel-checked |
| `zero_not_mem_runSet` (0 ∉ A) | proved, kernel-checked |
| `card_line_inter` (every t-line has p − 1 points) | proved, kernel-checked |
| `card_runTops` (\|B_t\| = p³) | proved, kernel-checked |
| `charSum_lower` (Im F = 0 and Re F ≥ −3p for c ≠ 0) | proved, kernel-checked |
| optional: `ChowlaCosine.NegDefFibre.le_two_mul_card_of_negDef` | proved, kernel-checked |

- The definitions `Γ`, `tVec`, `runSet`, `runTops`, `charSum` and the five theorem headers are byte-identical to
  HEAD. This was checked by a script that compares every declaration header against `git show HEAD:…`.
- The only edits around the statements:
  - the file's top comment, which said "NOT imported", was rewritten and now carries a proof outline;
  - `set_option linter.unusedVariables false in` was put in front of `runSet_neg` (see §4).
- No `sorry`, no `axiom`, no `native_decide`, no `decide`. `fin_cases` is used only for 4-way case splits on `Fin 4`.
- Both files elaborate with **zero warnings** (`lake env lean`, on dirichlet).
- `lake build` succeeds with both files imported from `lean/ChowlaCosine.lean` (8720 jobs).

## 2. Axiom check

- `lean/AxiomCheck.lean` has two new sections:
  - §12: the five P21 theorems;
  - §13: the fibre lemma.
- `lean/AxiomCheck.out` was regenerated on dirichlet with `lake env lean AxiomCheck.lean`. It has **109** `depends on axioms`
  lines: the 103 existing ones, plus 5 for P21 and 1 for the fibre lemma.
- **All 109** read exactly `[propext, Classical.choice, Quot.sound]`.
- The output has no errors, warnings or `sorryAx`.

## 3. Proof structure and helper lemmas

**Key reformulation (`mem_runSet_iff`).** x ∈ A ↔ x 0 ≠ τ(x 1, x 2, x 3), where

    τ(b, c, e) = c·e²               if b = 0
    τ(b, c, e) = −(c² − d·e²)/b     if b ≠ 0.

So A is the complement of the graph of τ along t = e_0. Everything else follows from this:
- `line_mem_iff`: x + s•t ∈ A ↔ x 0 + s ≠ τ. This gives `card_line_inter`, because the line's set is `univ.erase (τ − x 0)`.
- `mem_runTops_iff`: m ∈ B_t ↔ m 0 = τ − 1. This uses 1 ≠ 0 and 2 ≠ 0 in ZMod p, from `Ring.two_ne_zero` and
  `ZMod.ringChar_zmod_n`.
- `card_runTops`: B_t is the image of the injective map (b, c, e) ↦ ![τ − 1, b, c, e].

**Realness.** Reindex by x ↦ −x (`Finset.sum_nbij'`), using `runSet_neg` and ψ(−y) = conj ψ(y)
(`AddChar.map_neg_eq_conj`, Mathlib/Analysis/RCLike/Basic.lean). Then apply `Complex.conj_eq_iff_im`.

**Lower bound.** Three steps.

1. `charSum_eq`: F(c) = Σ_{b,c',e} (ψ(L)·p[c 0 = 0] − ψ(c 0·τ + L)), with L = c 1 b + c 2 c' + c 3 e.
   - `sum_Γ` splits Σ over Fin 4 → ZMod p into four sums through the explicit equivalence `e4`.
   - `inner_sum`: Σ_{a≠τ} ψ(j a + L) = ψ(L)·p[j = 0] − ψ(jτ + L).
2. **c 0 = 0.** F = (p − 1)·Σ ψ(L). This is 0 by `triple_zero`, which writes the sum as a product of three
   one-variable sums, at least one of which vanishes.
3. **j = c 0 ≠ 0.** F = −(H(0) + Σ_{b≠0} H(b)).
   - `H_zero`: H(0) = Σ_e ψ(c 3 e)·p[j e² + c 2 = 0].
   - `re_H_zero_le`: Re H(0) ≤ 2p. Each term has |ψ| = 1 (`AddChar.norm_apply`), and `card_quad_le_two` bounds the
     root count: #{e : e² = a} = η(a) + 1 ≤ 2.
   - `H_ne` (b ≠ 0): H(b) = −p·ψ(κ b), with κ = c 1 + c 2²/(4j) − c 3²/(4jd). Ingredients:
     - `complete_sq`: completing the square, by the shift u ↦ u − b/(2a);
     - `two_var`: the two quadratic sums together;
     - `prod_two`: Σ_u ψ(α u²) · Σ_v ψ(−α d v²) = −p.
   - Summing over b ≠ 0 gives −p(p[κ = 0] − 1), whose real part is ≤ p.
   - Hence Re F ≥ −(2p + p).

**Gauss-sum layer.**
- `qchar p` is the ℂ-valued quadratic character, `(quadraticChar (ZMod p)).ringHomComp (Int.castRingHom ℂ)`.
- `sum_sq_eq`: Σ_u ψ(a u²) = η(a)·g for a ≠ 0, with g = `gaussSum (qchar p) ψ`. Proof: sum over the fibres of u ↦ u²
  (`Finset.sum_fiberwise`), count √w by `quadraticChar_card_sqrts`, then use `gaussSum_mulShift_eq` and
  `MulChar.IsQuadratic.inv`.
- `gauss_sq`: g² = η(−1)·p (`gaussSum_sq`).
- `prod_two`: η(α)·η(−αd)·η(−1) = η(α²d) = −1, by `quadraticChar_sq_one'` and `quadraticChar_neg_one_iff_not_isSquare`.

**Mathlib sources.**
- Mathlib/NumberTheory/GaussSum.lean: `gaussSum_sq`, `gaussSum_mulShift_eq`.
- Mathlib/NumberTheory/LegendreSymbol/QuadraticChar/Basic.lean: `quadraticChar_card_sqrts`, `quadraticChar_isQuadratic`,
  `quadraticChar_ne_one`, `quadraticChar_sq_one'`, `quadraticChar_neg_one_iff_not_isSquare`.
- Mathlib/NumberTheory/LegendreSymbol/AddCharacter.lean: `AddChar.sum_mulShift`, used for orthogonality,
  Σ_x ψ(a x) = p[a = 0].
- Mathlib/NumberTheory/MulChar/Basic.lean: `MulChar.ringHomComp_ne_one_iff`, `IsQuadratic.comp`, `IsQuadratic.inv`.
- Mathlib/Analysis/Normed/Ring/Finite.lean: `AddChar.norm_apply`.

## 4. Deviations from the paper proof, and things worth knowing

**Deviations.** The argument is the paper's (P21 / g3 §1), organized differently:
- **F as a complement sum.** F is computed from the complement-of-a-graph description, as
  Σ_lines (Σ_{whole line} − the missing point). The paper sums line by line over the points present; the content is
  the same.
- **Squares completed separately.** Each variable's square is completed on its own, and S(α)S(−αd) = −p is used.
  The paper writes this as one product formula with N*(c). Translated to the paper's indices, my κ is k + N*(c)/(4j).
- **Only Re H(0) is bounded.** I bound Re H(0) ≤ 2p and never prove that the x2 = 0 part is real; the paper also
  notes it is real.

**Statement observations.** These are not errors in the statements:
1. `runSet_neg` does not need `hp : p ≠ 2`; A = −A holds for every p. The hypothesis is kept to preserve the stated
   form, and the unused-variable linter is silenced locally.
2. `card_runTops` really needs p ≠ 2. For p = 2 each line is a singleton {τ + 1}, so B_t = ∅.
3. Realness in `charSum_lower` uses only A = −A; `hd` and `hψ` are needed only for the −3p bound.
4. **Not formalized: the bridge to "K ≤ 3p".** `charSum_lower` quantifies over pairs (ψ primitive, c ≠ 0). That these
   pairs give every nontrivial character of (ZMod p)⁴ is standard, but it is not in this file. So "K ≤ 3p over all
   characters" needs that bridge as well.
5. **Not formalized: attainment.** K = 3p exactly is on paper and numerical in the g3 report, not in Lean.

**Nothing suspicious in the mathematics.** Every step of the paper proof went through as written. The completed-square
constants match the paper's N*(c) formula.

**Workspace note, outside the task.** While I worked, `git status` showed new untracked files `src/e37_batch.sh`,
`src/e37b_batch.sh` and `src/group_bt_ilp.py`. They have local timestamps 12:55–13:00, and a new lead commit `ed7830f`
appeared. I did not create or touch them.

## 5. Optional task 5: negative-definite fibre lemma

`ChowlaCosine.NegDefFibre.le_two_mul_card_of_negDef` (kernel-checked, standard axioms) states:

    (ℓ : ℕ) (hℓ : 1 ≤ ℓ) (I : Finset (ZMod ℓ)) (hI : I.Nonempty) (h0 : 0 ∉ I) (hsym : ∀ s ∈ I, -s ∈ I)
    (hneg : ∀ j ≠ 0, ∑ s ∈ I, Real.cos (2π · j.val · s.val / ℓ) ≤ 0)  ⊢  ℓ ≤ 2 · |I|

Here cos(2πjs/ℓ) is evaluated at the representatives `val ∈ [0, ℓ)`. The value does not depend on the representative,
and `cos_eq_re` identifies it with Re `ZMod.stdAddChar (j * s)`.

**Proof.** I did not use Fourier inversion. Instead I took this direct dual form, with C_j = Σ_{s∈I} χ(js),
c_j = Re C_j and r_j = Re χ(j s₀) for a fixed s₀ ∈ I:
- Σ_j c_j = 0, since 0 ∉ I.
- Σ_j C_j χ(js₀) = ℓ (because −s₀ ∈ I) and Σ_j C_j conj χ(js₀) = ℓ (because s₀ ∈ I). Adding these gives
  Σ_j c_j r_j = ℓ.
- c_0 = |I| and r_0 = 1. For j ≠ 0, c_j ≤ 0 and r_j ≥ −1, so c_j r_j ≤ −c_j.
- Therefore ℓ ≤ |I| + c_0 = 2|I|.

This is equivalent to the brief's "|I|/ℓ − 1_I is positive definite" argument.
