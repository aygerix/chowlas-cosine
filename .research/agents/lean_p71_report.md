# P71.2 Lean formalization report

Status (2026-10-19): COMPLETE — exact main theorem and corollary kernel-checked; full build and axiom audit passed.

## Scope and statement fidelity

Implemented `lean/ChowlaCosine/BohrTaper.lean` and added its import to
`lean/ChowlaCosine.lean`. No subagents were launched and no commits were made.
No project-level `.research/*.md` files were changed.

**No changes to the theorem or its hypotheses.** `L`, `q`, and `P` are arbitrary
naturals satisfying precisely `20 ∣ L`, `20 ≤ L`, `100 ≤ P`, and
`4 * L + 1 ≤ q`. `M` is an arbitrary real. The cosine hypothesis quantifies
over every real `x`. Frequencies form a `Finset ℕ`, with positivity proved by
`taper_pos`. The set is not replaced by a multiset or an angle grid.

All declarations below are in namespace `ChowlaCosine.BohrTaper`.

## Exact definitions

```lean
def centered (q : ℕ) (a : ℤ) : ℤ :=
  if 2 * (a % (q : ℤ)) ≤ q then a % (q : ℤ) else a % (q : ℤ) - q

def taper (L q P : ℕ) : Finset ℕ :=
  (Icc 1 (P * q)).filter fun a =>
    (centered q a).natAbs * (P * q) ≤ L * (P * q - a)

noncomputable def packet (q h J : ℕ) (b : ℤ) : Finset ℤ :=
  ((Icc (1 : ℤ) J) ×ˢ (Ico (b * h) ((b + 2) * h))).image
    (fun p : ℤ × ℤ => p.1 * q + p.2)
```

`centered_bounds`, `centered_mod`, and `centered_unique` prove the exact
`-q < 2r ≤ q` convention, congruence, and uniqueness for `q > 0`. Natural
subtraction in `taper` is exact on its filtered interval, because `a ≤ Pq`.

The brief's packets are exactly `packet q (L/20) (P/8) (-16)`,
`packet q (L/20) (P/8) (-1)`, and `packet q (L/20) (P/8) 14`.
`packet_card` proves each has cardinality `2hJ`; `packets_disjoint` proves
pairwise disjointness. `packet_subset_taper` proves positivity and membership
via `natAbs`, identifying these positive integers with natural frequencies.
`packet_edge` and `packet_nonedge` establish the required induced graph.

## Exact Lean theorem statements

```lean
theorem lower_bound {L q P : ℕ} (hL : 20 ∣ L) (hL0 : 20 ≤ L)
    (hP : 100 ≤ P) (hq : 4 * L + 1 ≤ q) (M : ℝ)
    (hM : ∀ x : ℝ, -M ≤ cosSum (taper L q P) x) :
    7 * (2 * (L / 20) * (P / 8) : ℕ) / 34 + 1 / 2 ≤ M

theorem lower_bound_card {L q P : ℕ} (hL : 20 ∣ L) (hL0 : 20 ≤ L)
    (hP : 100 ≤ P) (hq : 4 * L + 1 ≤ q) (M : ℝ)
    (hM : ∀ x : ℝ, -M ≤ cosSum (taper L q P) x) :
    7 * ((taper L q P).card : ℝ) / 6290 + 1 / 2 ≤ M

theorem card_taper_le (L q P : ℕ) (hq : 0 < q) (hP : 0 < P) :
    (taper L q P).card ≤ (2 * L + 1) * P

theorem packet_size_lower {L P : ℕ} (hL : 20 ∣ L) (hP : 100 ≤ P) :
    (L : ℝ) * P / 90 ≤ (2 * (L / 20) * (P / 8) : ℕ)
```

The explicit casts to `ℝ` in the cardinality statements, and the coercions in
`lower_bound`, express real inequalities. `/ 20` and `/ 8` inside the
annotated natural expression are natural division; `/ 34`, `/ 2`, and
`/ 6290` in the conclusions are real division.

## Proof and verification

The only analytic input is the existing `ChowlaCosine.star_lemma`.
`three_clique_bound` expands all nine blocks of the weighted adjacency form
for weights `(2, -3, 2)`, obtaining exactly `-7m² - 17m` and norm square `17m`.
It applies `star_lemma` to the union of the three finite integer sets.

The proof uses the exact integer margin `20|d| ≤ 3Pq`, proved by
`short_longitudinal`, which leaves transverse radius at least `17h`.
This replaces the paper proof's decimal estimates only; it does not alter any
statement or hypothesis. The auxiliary proof first uses `L = 20h`, and
`lower_bound` recovers exactly the original arbitrary-divisible-`L` statement.

For counting, the injection `a ↦ ((a-1)/q, centered q a)` maps the taper into
`range P ×ˢ Icc (-L) L`. Using `(a-1)/q` accounts for the endpoint `a = Pq`.
Together with `m ≥ LP/90` and `L ≥ 20`, this gives the requested constant 6290.

Lean LSP source version 7 completed with zero diagnostics. A source scan found
no `sorry`, new axiom declaration, or `native_decide`. The baseline full
`lake build` succeeded (8759 jobs). The new full `lake build` succeeded with the module imported (8760 jobs):
`BohrTaper` built in 67 seconds and the root module built in 51 seconds.
The audit command also exited successfully. Both main theorems, the graph
certificate, residue uniqueness, and counting lemmas depend only on the three
permitted axioms shown below. No source changes were made after this build.

## Axiom audit

Commands (working directory `lean/`), both with exit status 0:

```sh
lake build > ../.research/agents/lean_p71_scratch/final_build.log 2>&1
lake env lean ../.research/agents/lean_p71_scratch/Audit.lean > ../.research/agents/lean_p71_scratch/final_axioms.log 2>&1
```

Exact `#print axioms` output:

```text
'ChowlaCosine.BohrTaper.lower_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.BohrTaper.lower_bound_card' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.BohrTaper.three_clique_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.BohrTaper.card_taper_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.BohrTaper.packet_size_lower' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.BohrTaper.centered_unique' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.BohrTaper.packet_card' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.BohrTaper.packet_subset_taper' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The complete elaborated signatures and axiom output are preserved in
`.research/agents/lean_p71_scratch/final_axioms.log`; the audit source is
`.research/agents/lean_p71_scratch/Audit.lean`.

## Full build log tail

```text

Note: This linter can be disabled with `set_option linter.style.haveILetI false`
⚠ [8757/8760] Replayed ChowlaCosine.Beckner.YoungSharpSpecial
warning: ChowlaCosine/Beckner/YoungSharpSpecial.lean:102:22: Used `tac1 <;> tac2` where `(tac1; tac2)` would suffice

Note: This linter can be disabled with `set_option linter.unnecessarySeqFocus false`
✔ [8758/8760] Built ChowlaCosine.BohrTaper (67s)
✔ [8759/8760] Built ChowlaCosine (51s)
Build completed successfully (8760 jobs).
```

The replayed warnings are in existing Beckner files. The new `BohrTaper` module
built without warnings. The complete log is
`.research/agents/lean_p71_scratch/final_build.log`.

## Source identity and remaining work

Verified SHA-256 of `lean/ChowlaCosine/BohrTaper.lean`:

```text
749641df19bbbe358acd0065a8adf51631888d6d721e28b46b95d1e6257e93fa
```

No remaining formalization work or proof gaps for the assigned P71.2 theorem.
No statement deviations, added hypotheses, `sorry`, new axioms, or
`native_decide`. No commit was made.
