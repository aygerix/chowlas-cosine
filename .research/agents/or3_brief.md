# Brief: OR(2)-weak beyond residue strips — from Theorem C toward arbitrary 2-run sets (codex agent, Sol 6.1 xhigh)
(lead, 2026-10-18)

## Context (read first, do not re-derive)
- `.research/agents/or2_brief.md`: why OR(2)-weak is the minimal Z-specific statement behind any run-top improvement.
  **OR(2)-weak:** there are absolute c, δ > 0 with M(S ∪ (S + t)) >= c|S|^{1/4+δ} whenever S ∩ (S + jt) = ∅ for
  j = ±1, ±2. In groups the analogue is false (O4 in Z_4 × GR(4,a), PROOFS P22), so a proof must use Z.
- `.research/agents/or2_report.md`: the previous agent's proved results.
  - Theorem A (residue strip, exponent 3/8).
  - Theorem B (phase coherence at the zeros u_j = (2j+1)π/t of the pair factor).
  - Theorem C (§5), which uses the macro-profile H and the reciprocal grid Σ 1/(1 + cos v_j) = J²/2. Statement: for
    residues mod q in [0, Lt] with k classes and q >= 16BJtk, M >= √n/(32BJ²k^{3/2}), where B = L² + (L+1)² and
    J = 2L + 3.
  - Obstructions in §6 (free rotation, the {0, 3t} cancellation, signed levels).
  - The lead re-checked Theorem C. It is recorded in `.research/PROOFS.md` as P27.
- Mechanism to keep: the real coset grid (θ + 2πZ)/q separates the quotient (micro) phase from the residue (macro)
  profile. Group characters cannot do this, which is why the argument is Z-specific.

## Task (pick what you can actually push; report exactly what is proved)
1. **Remove the bounded-spread hypothesis R ⊂ [0, Lt].**
   - Theorem C's constants blow up as L grows (B ~ L², J ~ L), so residues spread over [0, q) give nothing.
   - Prove a version for S = ⋃_{r∈R} (qY_r + r) with k = |R| residues ANYWHERE mod q (q >= poly(t, k)) and a bound
     M >= c·n^{α}·k^{−β} with α > 1/4 and β independent of the spread.
   - Candidate route: localized macro-profile tests.
     - Group the residues into clusters of diameter O(t).
     - Apply the Theorem C dichotomy to each cluster with a test function that sees only that cluster (Fejér
       windows in the residue variable). P24/P25 in PROOFS.md are the localization lemmas available.
   - First falsification check: residues forming an arithmetic progression with step comparable to t (or 3t/2).
     Does the macro profile still have a dip, or can the clusters cancel each other's dips?
2. **Reduce the k^{3/2} loss** in the derivative branch by relating the fibre counts to the curvature statistic G
   (the previous agent's suggested next derivation). A bound with k^{1/2} would already give exponent > 1/4 for
   k <= n^{1/2 − ε}.
3. **General S: a structure-versus-randomness dichotomy.**
   - Either S has a large "Bohr structure" — a q with S concentrated on few residues mod q on a long stretch —
     and items 1–2 apply locally.
   - Or F_S has no large almost-periods, and then some unstructured argument (energy, the P28 averaged
     local-maximal bound, a random-phase argument at the zeros u_j) gives M >= n^{1/4+δ}.
   - State precisely which middle case is left over.
4. **Or a genuine obstruction:** a Z family of 2-run sets with M(S ∪ (S + t)) <= C|S|^{1/4+o(1)}. That would cap
   the run-top route at 1/4 in Z. Certify any such finite example rigorously (src/chowla.py certify_lower_bound or
   the arb ball DFT). A numerical minimum is not enough.

## Rules
- All computation on the GCP VM dirichlet via `src/dirun.sh` (header explains usage). Use at most `-c 2`; the lead's
  Gurobi jobs use the rest.
  - Gurobi 13.0.3 (full licence, gurobipy in the VM venv) is the solver for any ILP/LP.
  - Write C for anything heavy. Never compute on the laptop beyond trivial checks.
  - Never touch the VM fejer. Never kill or modify processes you did not start.
- Edit only `.research/agents/or3_report.md` and files under `.research/agents/or3_scratch/`. Do not edit other
  .research files. Do not commit.
- Label every claim PROVED (full proof written out, all constants), NUMERICAL (code path and seed), or CONJECTURED.
  State the exact hypotheses of any outside theorem used.
- Write the report early and overwrite it as you go, so partial progress survives.
- A failed lemma is a result: keep its smallest counterexample and pivot to a different lemma motivated by it.
