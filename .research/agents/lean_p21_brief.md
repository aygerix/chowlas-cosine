# Brief: Lean formalization of P21 (lead, 2026-10-18 night)

## Task
Prove, in Lean 4 + mathlib, the five theorems in `lean/ChowlaCosine/RunTopGroup.lean` **exactly as stated**. Each
currently ends in `sorry`. They formalize P21 in `.research/PROOFS.md`; the paper proof and its independent check are
also in `.research/agents/g3_report.md` §1. Read both before starting.

The aim is to kernel-check that group-agnostic run-top bounds cannot beat K³. This is a barrier result for lower-bound
proofs of Chowla's cosine problem; context is in `.research/notes/runtop_barriers.md`.

## The mathematics (paper proof, P21)
Let p be an odd prime and d a non-square in F_p. Take Γ = F_p^4 and t = e_0 (in Lean, coordinate 0 is the paper's x1).
Write N(v) = v3² − d v4². The set is

    A = {x : x2 ≠ 0, x1x2 + N(x3,x4) ≠ 0} ∪ {x : x2 = 0, x1 ≠ x3·x4²}.

1. **Symmetry and 0 ∉ A.** Both defining conditions are invariant under x ↦ −x: N is even, and x1 − x3x4² is odd, so
   "≠" is preserved. The point x = 0 has x2 = 0 and x1 = 0 = x3x4².
2. **Lines.** The line {x + s·t} with x2 ≠ 0 misses exactly s with x1 + s = −N/x2. A line with x2 = 0 misses exactly
   x1 + s = x3x4². So every line has p − 1 points.
3. **Run-tops.** On a line, A is F_p \ {τ}. The tops m ∈ A with m − t ∈ A and m + t ∉ A are exactly m = τ − 1. This
   needs p ≥ 3, so that τ − 2 ≠ τ. There is one top per line and p³ lines, so |B_t| = p³.
4. **Characters.** Take c = (j, k, c3, c4) ≠ 0 and F(c) = Σ_{x∈A} ψ(j x1 + k x2 + c3x3 + c4x4).
   - **Realness.** A = −A gives F(c) = conj F(c), so Im F = 0.
   - **j = 0.** Every line carries p − 1 points, so F = (p−1)·Σ_{x2,x3,x4} ψ(k x2 + c3x3 + c4x4) = 0.
   - **j ≠ 0, x2 ≠ 0 lines.** On such a line, Σ_{x1 ∉ {τ}} ψ(j x1) = −ψ(jτ). These lines contribute
     −Σ_{x2≠0} ψ(k x2) Σ_{x3,x4} ψ(−j N(x3,x4)/x2 + c3x3 + c4x4).
     The inner sum is a product of two one-variable quadratic Gauss sums. Its value is
     η(α)η(−αd)·g²·ψ(−N*(c)/(4α)) with α = −j/x2, where g² = η(−1)p, η is the Legendre symbol and
     N*(c) = c3² − c4²/d. Using η(α)² = 1 and η(d) = −1, the product is −p·ψ(N*(c)x2/(4j)).
     So this part equals p·(p·[k + N*(c)/(4j) = 0] − 1) ∈ {−p, p(p − 1)}.
   - **j ≠ 0, x2 = 0 lines.** These contribute −ĝ_j(c), where ĝ_j(c) = Σ_{x3,x4} ψ(j x3x4² + c3x3 + c4x4).
     Summing over x3 first gives p·Σ_{x4 : j x4² = −c3} ψ(c4x4). That sum has at most two terms, so |ĝ_j(c)| ≤ 2p.
   - **Conclusion.** Re F ≥ −p − 2p = −3p.

You may restructure the argument; you may not change the statements.

## Rules (non-negotiable)
- Do **not** weaken, specialize or edit the five theorem statements or the definitions `Γ`, `tVec`, `runSet`, `runTops`
  and `charSum`. Helper lemmas and extra definitions are fine.
- If you believe a statement is false as written, stop and report the exact problem with a counterexample. Check this
  numerically if useful, on the VM. Do not "fix" the statement.
- No new `axiom`, no `sorry` in the final file, no `native_decide`, no `decide` on large search spaces that hide
  computation. A bounded `decide` for a single small fact is fine if you say where you used it.
- **Compute:** all Lean elaboration and builds run on the GCP VM dirichlet, never on the laptop. Lean 4.33.1, elan
  and the mathlib cache are installed there. Use for example:
      src/dirun.sh -c 4 -m 16 -t 3600 sh -c 'cd lean && ~/.elan/bin/lake env lean ChowlaCosine/RunTopGroup.lean'
      src/dirun.sh -c 4 -m 16 -t 3600 sh -c 'cd lean && ~/.elan/bin/lake build'
  dirun.sh copies the repo up (local edits win) and changed files back. A full build takes about 75 s. Never touch the
  VM `fejer`.
- Edit only files under `lean/` and your report `.research/agents/lean_p21_report.md`. Do not edit other `.research`
  files. Do not commit.

## When finished
1. Import `ChowlaCosine.RunTopGroup` from `lean/ChowlaCosine.lean` and confirm `lake build` succeeds.
2. Add `#check` / `#print axioms` lines for the five theorems to `lean/AxiomCheck.lean` as a new section.
3. Regenerate `lean/AxiomCheck.out` on the VM, for example:
       sh -c 'cd lean && ~/.elan/bin/lake env lean AxiomCheck.lean > AxiomCheck.out 2>&1'
   Then report how many lines read exactly `[propext, Classical.choice, Quot.sound]`.
4. Write `.research/agents/lean_p21_report.md`. Include the status of each theorem, the main helper lemmas (Gauss-sum
   facts and their mathlib sources), any deviation from the paper proof, and anything you found suspicious.
5. Optional, only if all of the above is done. Prove the negative-definite fibre lemma from P21's diagnosis in a new
   file:
   - Let ℓ ≥ 1 and I ⊂ ZMod ℓ nonempty, with 0 ∉ I and I = −I.
   - Suppose that for every j ≠ 0, Σ_{s∈I} cos(2π j s/ℓ) ≤ 0.
   - Then 2|I| ≥ ℓ.
   - (Paper proof: |I|/ℓ − 1_I has nonnegative Fourier transform, so its value at 0 dominates its value at any s ∈ I.)
