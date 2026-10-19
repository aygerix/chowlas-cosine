# Lean brief (codex verification agent): formalize P71.2, linear M for periodic triangular Bohr tapers

You are formalizing ONE mature theorem in Lean 4 / mathlib, in /Users/jmercedes/Desktop/Projects/Research/chowla-cosine/lean.
- Read CLAUDE.md (section "Lean 4 formalization") and .research/PROOFS.md section P71, item 2.
- Rules:
  - Do NOT edit .research/*.md. Do not commit. Do not launch subagents.
  - Report: `.research/agents/lean_p71_report.md` (keep it current). Scratch: `.research/agents/lean_p71_scratch/`.
  - New file: `lean/ChowlaCosine/BohrTaper.lean`, imported from `lean/ChowlaCosine.lean`.
  - Build with `lake build` in `lean/` (the laptop is fine for Lean builds).
  - No `sorry`, no new axioms, no `native_decide`. Report `#print axioms` for the main theorems; they must use only
    propext, Classical.choice, Quot.sound.
  - Do NOT weaken the statement: no restriction to particular L, q, P; no replacing "∀ real x" by a grid; no
    replacing the set by a multiset. If you must change a hypothesis, say so explicitly in the report.

## Available (already kernel-checked)
`ChowlaCosine/Star.lean`, theorem `star_lemma`. If −M <= cosSum A x for all real x (A a Finset ℕ of positive
naturals), then for every finite W ⊂ ℤ and v : ℤ → ℝ:
    Σ_{u,w∈W} v u * v w * [|u − w| ∈ A] >= −2M Σ_{u∈W} (v u)².
Read the file for the exact Lean signature (`cosSum`, the indicator form, etc.) and reuse it.

## Statement to formalize (exact)
Parameters: naturals L, P, q with 20 ∣ L, L >= 20, P >= 100, q >= 4L + 1.
- Centred residue: for a ∈ ℕ, r(a) ∈ ℤ is the unique integer with r ≡ a (mod q) and −q < 2r <= q.
- The set:
      A = {a ∈ ℕ : 1 <= a <= P·q  and  |r(a)|·(P·q) <= L·(P·q − a)}.
  This is the division-free form of |r(a)| <= L(1 − a/(Pq)). It is a Finset of positive naturals.
- Packets, with h = L/20 and J = ⌊P/8⌋ (both naturals):
      U = {j·q + r : 1 <= j <= J, −16h <= r < −14h},
      V = {j·q + r : 1 <= j <= J,  −h <= r < h},
      W = {j·q + r : 1 <= j <= J,  14h <= r < 16h},
  each of size m = 2hJ, viewed as subsets of ℤ.

Theorem (main). If −M <= cosSum A x for every real x, then M >= 7m/34 + 1/2.
Corollary. Also M >= 7·|A|/6290 + 1/2. This needs |A| <= (2L+1)·P and m >= L·P/90.

## Proof (checked by the lead; formalize it)
1. Membership: U, V, W ⊂ A.
   - Every element a = jq + r has 1 <= a, since q >= 4L + 1 > 0.8L >= |r|.
   - a <= Jq + 16h <= Pq/8 + 0.8L, so a/(Pq) <= 0.127.
   - |r(a)| = |r| <= 16h = 0.8L <= 0.873L <= L(1 − a/(Pq)).
   - No wrap: |r| < q/2.
2. Adjacency. For distinct u, w in the union, d = u − w = (j − j')q + (r − r'), with |d| <= Jq + 32h <= 0.129Pq.
   - Its centred residue is r − r', since |r − r'| <= 32h = 1.6L < q/2.
   - The allowed radius at |d| is L(1 − |d|/(Pq)) >= 0.871L.
   - |r − r'| < 0.85L inside each packet, across U–V and across V–W, so |d| ∈ A: edge. Note d ≠ 0 for distinct
     elements, and the case r = r', j ≠ j' gives residue 0, which is allowed.
   - |r − r'| >= 28h = 1.4L > L across U–W, so |d| ∉ A: no edge.
3. The quadratic form with v = 2 on U, −3 on V, 2 on W (0 elsewhere). The diagonal terms vanish since 0 ∉ A.
       4m(m−1) + 9m(m−1) + 4m(m−1) − 2·6·m² − 2·6·m² + 0 = −7m² − 17m,
   and Σv² = 17m. star_lemma gives −7m² − 17m >= −34Mm, hence M >= 7m/34 + 1/2.
4. Counting: m = 2hJ >= (L/10)(P/9), since J >= P/9 for P >= 72. |A| <= (2L+1)P <= (41/20)LP for L >= 20.
   Combine.

## Deliverable
- `BohrTaper.lean`, building with no sorry.
- The report: the exact Lean statements, any deviation from the statement above, the axioms printout, and the build
  log tail.
