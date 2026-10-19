# Math brief (codex research agent), round 2: T-dense beyond single filters

You are a research mathematician working on Chowla's cosine problem in /Users/jmercedes/Desktop/Projects/Research/chowla-cosine.
- Read CLAUDE.md first: conventions, honesty labels, and the rule that numerics are not proofs.
- Conventions: f_A = Σ_{a∈A} cos(ax), M(A) = −min f_A, n = |A|, S = A ∪ (−A).
- Rules:
  - Do NOT edit .research/*.md; the lead records results after verifying them. Do not commit. Do not launch
    subagents. Do not write LaTeX papers; markdown only.
  - Write everything to `.research/agents/tdense2_report.md` and keep it current: statements, full proofs or precise
    gaps, failed attempts with the exact reason, and code/data paths.
  - Computation ONLY on the VM via `src/dirun.sh [-c cores] [-t secs] <cmd>` (see its header). At most -c 2 (the VM is
    shared). Never compute on the laptop. Gurobi (gurobipy on the VM) is the LP/MILP solver.
  - Scratch code goes in `.research/agents/tdense2_scratch/`.
  - Label every claim PROVED / NUMERICAL / HEURISTIC / CONJECTURED. Keep all quantifiers exact.

## Target (unchanged)
T-dense: for every C >= 1 there is c(C) > 0 such that every A ⊂ [1, C·n] with |A| = n has M(A) >= c(C)·√n.
- Literature: Bu et al. 2610.17160 prove only n^{1/4} (Prop. 9.7). We have √n for C < 2.466 (kernel-checked).

## Your round-1 results, now verified and recorded by the lead
In .research/PROOFS.md:
- P38: your TD1/TD2, the denominator filters, re-derived line by line.
- P39: your TD4. Identities re-verified in exact arithmetic. Physical-space form: with g_q = 2·1_S − 1_{S+q} − 1_{S−q},
  V_q = ‖g_q‖²/16 and Δ_q = ½·Σ_{x+y+z=0} g_q(x)g_q(y)g_q(z).
- TD3: profile certificate reproduced independently.
Read P38, P39, P39-O and P40, and the NOTEBOOK entry "2026-10-19 (session 3, late)".

## The lead's new analysis you must test (P39-O, P40)
1. P39-O(ii): LM-dense with ONE filter (1 − cos qx) is very probably FALSE (HEURISTIC).
   - Family: A = union of J randomly thinned Bohr sets {m <= X : ‖mα_i‖ < ε}, ε ≈ 1/(4CJ), J ~ log X/log log X, α_i
     such that no q <= X has min_{j<=3} ‖jqα_i‖ < 3ε for more than J/2 of the i.
   - Pure (single-component) triple excesses are positive for every "inactive" component. The Pólya envelope is >= 0
     for a convex decreasing thinning profile. So W_q ≳ n²/J ≫ n^{3/2} for every q.
   - These sets still have M >= √n by other means, so this obstructs the certificate, not T-dense.
2. P40 (PROVED, Bhatia–Davis): a counterexample must be spike-dominated for every multiplier H. The third moment is only
   a computable surrogate. It fails when tall positive spikes (structure) sit on top of a Gaussian-like bulk.
3. Product filters Π_{i<=J}(1 − cos q_i x) kill all J components but lose (3/8)^{J/2} in √V.

## Tasks, in priority order
T1. Decide LM-dense rigorously at computable sizes.
  - Build the Bohr-union family explicitly (choose α_i, J, ε, thinning; justify the choices) for X up to ~2·10^5.
  - Compute EXACT triple counts c(k) = 1_S^{*3}(k): integer convolution with CRT over two NTT primes, or an exact
    alternative. Note c(k) can exceed 998244353.
  - Report min over q <= X with V_q >= n/10 of W_q/V_q^{3/2}, and its growth in X. Also report M (grid + refine; label
    as numerical).
  - Either prove that LM-dense fails for an explicit infinite family (a PROVED counterexample to the certificate, with
    M ≥ c√n proved separately if possible), or find the flaw in P39-O(ii).
T2. Find a certificate that DOES work on the Bohr-union family with a constant independent of J. Candidates:
  - (a) Stieltjes/Hankel conditions on moments of T_q up to order 5 or 7. With T + m >= 0, the shifted Hankel matrices
    must be PSD; derive the exact integer formulas, e.g. via k-fold sum counts of S.
  - (b) Spike-masking multipliers H = 1 − Σ_s (normalized Fejér bump at the Bohr points s = 2πkα_i), with H >= 0, plus
    TD4. Give exact formulas for V_H and W_H.
  - (c) Windows applied to T_H (your TD-window).
  - (d) Anything better.
  If none can work, prove the obstruction precisely: a certificate class plus a family on which it provably loses.
T3. Extend P38 from cumulative rounding to bounded local discrepancy (your round-1 line 3). Find the weakest
  rounding hypothesis under which the denominator filter plus window still gives √n. Find the first family where it
  fails.
T4. If T1–T3 point the same way, formulate the general dense theorem as an energy-increment / multiplier-selection
  lemma. Make it a precise statement of what remains, or a proof.

## Falsification first
Before investing in a lemma, test it on:
- your round-1 benchmark sets (tdense_scratch);
- Bu/Singer sets;
- the certified dense optima (examples/construct/N50_certified.json, examples/smallN_best.json);
- intervals, unions of dilated intervals, and the Bohr unions above.
The evaluator box_minlam.true_min (src/box_minlam.py) gives a grid + Newton minimum: evidence, not proof.

## Deliverable
A proof, a precise reduction with evidence, or a rigorous obstruction. Say exactly what is new versus what is quoted.
