# Math brief (codex research agent), round 11: push the certificate toward 8; attack the fourth-moment (approximate-binarity) layer

You are a research mathematician working on Chowla's cosine problem in /Users/jmercedes/Desktop/Projects/Research/chowla-cosine.
- Read CLAUDE.md first: conventions, honesty labels, and the rule that numerics are not proofs.
- Conventions: f_A = Σ_{a∈A} cos(ax), M(A) = −min f_A, n = |A|, X = max A.
- Rules (unchanged):
  - Do NOT edit .research/*.md. Do not commit. Do not launch subagents. No LaTeX; markdown only.
  - Report: `.research/agents/tdense11_report.md` (keep it current). Scratch: `.research/agents/tdense11_scratch/`.
  - Computation ONLY on the VM via `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 ...` (at most 4 cores).
  - Gurobi for every LP/MILP/QP.
  - Label every claim PROVED / NUMERICAL / HEURISTIC / CONJECTURED, with exact quantifiers.
  - Grep PROOFS.md before any novelty claim.

## State (read PROOFS P58–P62, NOTEBOOK cont. 12–14, EXPERIMENTS E82–E84, and your round-10 report)
- Your round 10 (lead-verified as P62; the lead re-checked the certificate independently in Arb, E84):
  - D <= 1333/10000, so T-dense(C) for every C < 7.5019;
  - the P61 audit and repair;
  - three binary moment profiles are free (sparse gadgets).
- Numerical truth of the second-order theory: 1/D ≈ 8.5708 (E82; the optimiser G* is in examples/e82/e82.jsonl).
- Lead's new observations (NOTEBOOK cont. 14). Test them; do not take them on trust.
  - DC BARRIER. Binarity beyond second order enters only anchored sums Σ_k τ(k)ĥ(k)^j, with ĥ(0) = m and
    ĥ(k) = r_k/2. A positive x-space integrand (h^{*j} tested against τ̌) needs a doubly positive τ, so τ(0) >= 1/ℓ.
    The DC term τ(0)m^j then swamps the k ≠ 0 signal unless M << n^{1/j}. Claimed consequence: in the √n regime only
    second-order positivity is effective. Any proof beyond 1/D must apply SECOND-ORDER positivity to binary-derived
    objects, or use arithmetic structure.
  - SUBGROUP RESTRICTIONS. A_q = (A ∩ qZ)/q is again a dense counterexample (f_{A∩qZ} = q⁻¹Σ_j f_A(x + 2πj/q)), so
    P59/P61 apply to it. In the limit: a + Σ_{j≠0}W_{2πj/q}(0) <= ½ (rational macroscopic atoms), and ∫p_q <= D. If
    a = ½, all rational atoms vanish.
  - KURTOSIS. Binary local kurtosis is 1/e − 3 (< 3 iff e > 1/6; = 1 at e = ¼). Positive-amplitude cosine structures
    have kurtosis >= 1.5 unless subgroup atoms are present; Gaussian packets have 3. But the anchored fourth moment is
    DC-swamped, so this is only a heuristic.
  - CYCLIC ANALOGUE. Binary ⟺ the spike measure is a weighted partial difference set (h ⋆ h = c₁ + c₂h off 0).
    Sparse PDS give two-valued sequences with small min on Z_K; in Z_p nontrivial PDS are essentially Paley (Ma).

## Task 1 (bounded): push the rigorous constant toward 8
Improve D₁ = 0.1333 toward 0.1167. Each exact improvement gives T-dense(1/D₁). Ideas: a third dilation (B(3t, ·)
terms with the identity ∫B(3t, w(3t)) = ⅓∫B), two-variable potentials, the long Chebyshev supporting lines of round 9
applied to w, adaptive t-cells, a better Schur function (piecewise or higher degree), finer CF caps. Deliver an exact
certificate with an independent re-verification, as in round 10. Target C >= 8. Cap this task at about a third of your
effort.

## Task 2 (main): the fourth-moment / approximate-binarity layer
Four matching raw profiles (a, a², a³, a⁴ → p) are equivalent to normalized L² proximity to {0, 1}. Decide which of
these holds.
- (A) CONSTRUCTION. A weighted escape (min >= −o(√X)) with the first FOUR binary raw-moment profiles, at some density
  d close to D. Then quantify its rounding cost: is the non-binarity energy o(X/log X), and can rounding be done so that
  the min stays −o(√X)? That would be a dense Chowla counterexample.
  - Ingredients available: random packets (Gaussian, kurtosis 3); sparse gadgets (raise the fourth moment, any third);
    macroscopic irrational atoms (PD profiles); rational atoms (subject to the A_q constraints); structured (weighted
    PDS / Bohr-type) spike configurations.
  - The hard region is e > 1/6 (p ∈ (0.211, 0.5]), where binary needs kurtosis < 3, i.e. platykurtic, two-valued-like
    residuals.
- (B) OBSTRUCTION. An inequality "positivity + approximate binarity ⇒ d <= D₄ < D" (or a <= a₄ < ½, which already
  gives d <= 4a₄(1 − a₄)·D).
  - Preferred mechanism, consistent with the DC barrier: second-order positivity applied to binary-derived positive
    objects. Candidates:
    - A_q (subgroup restrictions);
    - the "rounding correction" δ = binary − escape, whose energy must itself be packet-structured (P40);
    - other operations that map dense counterexamples to dense counterexamples.
  - Also decide whether the kurtosis heuristic can be made rigorous on the excess over the random DC background.
- (C) TEST the DC-barrier meta-statement. Prove a precise version: e.g., every inequality obtained by testing
  h^{*j} (j >= 3) against doubly positive weights is satisfied by a weighted escape with matched j-th moments once
  M >> n^{1/j}. Or refute it with a counterexample inequality.
Either (A) or (B) is a major result. Preserve every failed construction with numbers. Test candidate constructions on
the VM, with FFT minimum plus an Arb point or interval certificate for the best.

## Task 3 (short, capped): literature check
Is Chowla's problem for Z_p (the smallest eigenvalue of symmetric Cayley graphs Cay(Z_p, B) versus √|B|) known? What
do Ma's theorems on partial difference sets in cyclic groups say precisely? Is the dense integer problem beyond 1/D
reducible to, or related to, a cyclic statement? Quote exact theorems with versions. Cap at a short search.

## Deliverable
- Task 1: rigorous D₁ with certificate.
- Task 2: the four-moment escape or an obstruction inequality, with exact quantifiers, plus the DC-barrier verdict.
- Task 3: the precise literature facts.
Say exactly what is new versus quoted.
