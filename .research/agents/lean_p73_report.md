# P73 Lean formalization report

Status: **COMPLETE — both exact P73 (ℤ) statements are kernel-checked; full project build and axiom audit pass** (2026-10-19).

Scope: the exact integer version in `lean_p73_brief.md`: finite-sum positive definiteness plus Hermitian symmetry; arbitrary nonempty `S : Finset ℤ`; `0 < δ < 1/2`; and `Re (φ 0) < (4 - 5δ)/3`. No additional hypotheses, no commits, and no subagents. Only this report, the designated scratch directory, `lean/ChowlaCosine/FewSpike.lean`, and its import in `lean/ChowlaCosine.lean` are authorized outputs.

Read: `CLAUDE.md` (including the Lean formalization rules), `.research/PROOFS.md` P73, the brief, and the Number Theory research skill. Existing unrelated workspace changes are left alone.

Proof implementation: derive the quadratic inequality

`ψ(k+l) ≤ 2 ψ(k) + 2 ψ(l)`

directly from the three-point PSD test with coefficients `(1, -2, 1)` at `(0, k, k+l)`. Its quadratic form is `6m₀ - 4 Re φ(k) - 4 Re φ(l) + 2 Re φ(k+l) ≥ 0`. This supplies the squared triangle estimate needed in P73 and yields exactly the same `3 m₀ ≥ 4 - 5δ` contradiction. It avoids constructing a GNS space or formalizing square roots. All repeated-point cases (`k = 0`, `l = 0`, or `k+l = 0`) are handled explicitly using the two-point estimate. The proof then uses the integer Cauchy–Davenport bound and sums the squared errors over the exact finite bad set. The empty-good-set case is included.

Implementation now contains the finite-sum PD definition, the two-point nonnegativity lemma, the three-point estimate (with all repeated-point cases), the good-sum closure lemma, the finite Cauchy–Davenport counting argument, and the exact core and main statements. The umbrella import has been added.

Verification:

- `lake env lean ChowlaCosine/FewSpike.lean`: **PASS**, exit 0, no diagnostics. Log: `lean_p73_scratch/full_check.log`.
- `lake build` in `lean/`: **PASS**, exit 0, `Build completed successfully (8761 jobs).` Log: `lean_p73_scratch/lake_build.log`.
- `lake env lean ../.research/agents/lean_p73_scratch/AxiomCheck.lean`: **PASS**, exit 0. This also checks wrapper theorems with the finite-sum PD hypothesis, indicator, and bad set written out exactly as in the brief. Log: `lean_p73_scratch/axioms.log`.

The requested `#print axioms` output is:

```text
'ChowlaCosine.FewSpike.fewSpike_core' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.FewSpike.fewSpike' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The two-point and three-point helper lemmas have the same axiom list. The source has no `sorry`, `admit`, `native_decide`, or new axioms. The full project build built both `ChowlaCosine.FewSpike` and the umbrella module successfully. It replayed existing warnings from other modules; the new module has no diagnostics. `git diff --check` passed for the Lean changes.

No statement changes have been made. Both requested statements retain exactly the hypotheses in the brief. The core proof happens not to need nonemptiness or the stated δ interval, but the public core theorem still takes these hypotheses; the main proof uses positivity of δ.

Deliverables:

- `lean/ChowlaCosine/FewSpike.lean`: `PositiveDefinite` is the exact finite-sum/Hermitian definition, `ind` is the complex indicator, and `badSet` is the specified filtered `S ∪ (S + S)`.
- `ChowlaCosine.FewSpike.fewSpike_core`: `((S.card : ℝ) - 1) / 3 ≤ (badSet S φ δ).card`.
- `ChowlaCosine.FewSpike.fewSpike`: `δ ^ 2 * ((S.card : ℝ) - 1) / 3 ≤ E`, assuming the squared-error bound on every finite subset of `ℤ`.
- `lean/ChowlaCosine.lean`: imports `ChowlaCosine.FewSpike`.
- `lean_p73_scratch/AxiomCheck.lean`: reproducible axiom audit and exact-statement wrappers; logs are retained in the same scratch directory.

No remaining gap or required follow-up for this brief. No commits were made, no subagents were launched, and no top-level `.research/*.md` files were edited.
