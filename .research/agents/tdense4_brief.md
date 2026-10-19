# Math brief (codex research agent), round 4: verify P47/P53, then the descent below macroscopic scale

You are a research mathematician working on Chowla's cosine problem in /Users/jmercedes/Desktop/Projects/Research/chowla-cosine.
- Read CLAUDE.md first: conventions, honesty labels, and the rule that numerics are not proofs.
- Conventions: f_A = Σ_{a∈A} cos(ax), M(A) = −min f_A, n = |A|, X = max A.
- Rules (unchanged):
  - Do NOT edit .research/*.md. Do not commit. Do not launch subagents. No LaTeX; markdown only.
  - Report: `.research/agents/tdense4_report.md` (keep it current). Scratch: `.research/agents/tdense4_scratch/`.
  - Computation ONLY on the VM via `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 ...` (at most 2 cores).
  - Gurobi (gurobipy) for any LP/MILP.
  - Label every claim PROVED / NUMERICAL / HEURISTIC / CONJECTURED, with exact quantifiers.

## Target
T-dense: for every C >= 1 there is c(C) > 0 with M(A) >= c(C)√n for all A ⊂ [1, Cn], |A| = n.
Read PROOFS P38–P53 and the NOTEBOOK entries dated 2026-10-19 (night) first. Your round-3 results are recorded as
P48–P51.

## Task 1 (first, mandatory): adversarial verification of the lead's two new proofs
Try hard to break them. Check every quantifier, normalization and edge case. Report each as CONFIRMED,
CONFIRMED-WITH-FIX (give the fix) or BROKEN (give a counterexample or the exact failing step).
- P47 (PROOFS "P47"): smoothing-defect filter H = 1 − K_h/(h+1) plus the P31 window. Check in particular:
  - the Abel bound |(κ̃ ∗ β̄)_j| <= 4D₀/(h+1) for the even extension;
  - the U bound π²h(h+2)Q₂/96 (sign conventions; Φ = P̄_0 + 2f_P with P̄_0 := P_1);
  - the mean term γ_0 and the use of m' = m + γ_0/2 >= 0 in the P31 chain;
  - the energy pinning Σβ² = Σp(1−p) + Σβ(1−2p) with its Abel error;
  - the asymptotic corollary (choice of h, Γ(θ), the claimed D₀ range up to X^{3/4}).
  - Numerical audit already done: E69b, examples/e69/e69_p47_audit.jsonl. Add an exact-arithmetic or interval check
    of the finite inequality on small cases.
- P53 (PROOFS "P53", macro-SB): joint positive-definiteness of the local pattern density g on [0,1] × K. Check:
  - existence of the limit density g <= 1 (nondegeneracy of Γ; metrizability; subsequences);
  - that P48 really applies at every θ ∈ Γ, including X-dependent angle sequences;
  - the Følner/Gaussian integrability argument (step 3) and Fourier inversion on R × K;
  - the conclusion ∫∫g(1−g) > 0 and the claimed corollaries (TD10, Bohr-window sets, residue patterns have LINEAR M).
  - Numerically test the Bohr-window corollary: A = {m <= X : {mα} ∈ E(m/X)} for α = golden ratio, E(t) = [0, p(t))
    and centred windows, p(t) = c(1 − t)^k. M/X should stay bounded below as X grows.

## Task 2: the descent below macroscopic scale (main research task)
P53 shows that a counterexample (M <= ε√n, hence M = o(X)) must keep a positive part of its local spectral mass
outside every countable family of macroscopic atoms. That part lives in spikes of height o(X) or in the bulk. P40 says
the bulk is O(√ε)n, so it lives in MESOSCOPIC spikes of height H with √(n/ε) <= H << X.
- (QD) Make P53 quantitative. Fix a finite-X notion of "local spectral energy carried by structure of height >= δX"
  (suggestion: the largest local twisted energy captured by at most 1/δ² frequency windows of width K/X, localized in
  t). Prove: for every C there are δ, c > 0 such that every A ⊂ [1, Cn] with M(A) <= δX has at least cX of energy
  outside such windows. Compactness is fine; say whether the constants are effective.
- (MP48) A mesoscopic P48. For spikes of height H with √n << H << X, normalize by H instead of X.
  - Show that the COHERENT part of the twisted profile (amplitude H/X) must be positive-definite in the limit, with
    incoherent noise O(√X/H) → 0. Or find the exact obstruction.
  - Then find where the 0/1 constraint re-enters. Candidate: local Bessel Σ_atoms|q|² <= ∫g² <= ∫g at the finest
    scale, propagated through the scales.
- (D) If QD and MP48 hold, attempt the descent. At each level the energy must move to lower heights, and a summable or
  logarithmic count of levels must contradict P40 at height √(n/ε). Identify the single missing inequality if it does
  not close.
- Falsification first. Test every candidate lemma on:
  - Bu/Singer sets (src/e67_zoo.py bu(q));
  - P42's random Fejér mixtures;
  - E68 sets (examples/e68/);
  - smooth Bohr profiles (TD12 family);
  - random sets.
  Bu sets are the critical test. Their energy sits in chi-square-like structure of height ≈ √n log n, so any descent
  that "proves too much" will fail on them.

## Deliverable
For Task 1, a verdict per proof. For Task 2, a proof of T-dense, a precise single missing lemma with evidence, or a
rigorous obstruction. Say exactly what is new versus quoted.
