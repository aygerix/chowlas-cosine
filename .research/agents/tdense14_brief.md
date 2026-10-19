# Math brief (codex research agent), round 14: Sanders' exponent 1/3 at every density ⇒ dense Chowla exponent 1/3 for all C

You are a research mathematician working on Chowla's cosine problem in /Users/jmercedes/Desktop/Projects/Research/chowla-cosine.
- Read CLAUDE.md first: conventions, honesty labels, and the rule that numerics are not proofs.
- Conventions: f_A = Σ_{a∈A} cos(ax), M(A) = −min f_A, n = |A|, X = max A.
- Rules (unchanged):
  - Do NOT edit .research/*.md. Do not commit. Do not launch subagents. No LaTeX; markdown only.
  - Report: `.research/agents/tdense14_report.md` (keep it current). Scratch: `.research/agents/tdense14_scratch/`.
  - Computation ONLY on the VM via `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 ...` (at most 4 cores; bash, not zsh).
  - Gurobi for every LP/MILP/QP.
  - Label every claim PROVED / NUMERICAL / HEURISTIC / CONJECTURED, with exact quantifiers.
  - Grep PROOFS.md before any novelty claim.

## Why this target
- Dense integer state of the art.
  - Ours: T-dense(C), exponent ½, for every C < 2000/259 = 7.722 (P63, ineffective constant).
  - Bu et al. 2610.17160v1, Prop. 9.7: M >= ((n − 1)/(64·C·200000))^{1/4} for every A ⊂ [1, Cn]. That is exponent
    ¼ for every C.
  - Bedert and Shankar: exponent 1/5 for all sets.
  - For C > 7.722 nothing better than ¼ is known.
- Embedding (P63.6, P64.5; verify it).
  - For A ⊂ [1, X] with X <= Cn, take a prime q ∈ (2X, 4X] and B = A ∪ (−A) ⊂ Z_q.
  - B is symmetric, 0 ∉ B, |B| = 2n, so its density α = 2n/q lies in [1/(2C), 1].
  - λ_B(γ) = 2f_A(2πγ/q), so K_B := −min_{γ≠0} λ_B <= 2M(A).
- So a cyclic bound K_B >= c(α)q^θ at every FIXED density α gives M(A) >= c'(C)n^θ for all A ⊂ [1, Cn].
- Known cyclic inputs (the lead read Sanders v2 pp. 1–10; verify).
  - Sanders 0807.5104v2, Thm 1.2: half-sets, M = Ω(p^{Ω(1)}). "Through careful accounting" the exponent is 1/3.
    Thm 1.2 is derived from Thm 1.3 (in Z/pZ the only subgroups are trivial).
  - Sanders Thm 4.1 (the explicit Thm 1.3): for a symmetric A of density α and K ∈ (0, |A|/2^13], either
    ‖1_A − 1_H‖_1 <= K for a subgroup H, or 1̂_A(γ) <= −K^{α/5}/2^6.
    - So in Z_p the exponent is α/5, which DEGRADES with density.
    - The source is Lemma 3.2: M >= α·1̂_A(γ)/(16‖1_A‖_A^{2α⁻¹ + 1}). It comes from binomial positivity of
      (f − f(γ)1_{γ})^{(r)} with r = 2⌈1/α⌉; the contradiction needs rα >= 2.
    - Lemma 3.1 handles the spectrum-is-a-subgroup alternative: Spec_ε is a group, or M >= ε²α|A|/(2‖1_A‖_A), or
      there is an intermediate coefficient.
  - Jin–Milojević–Tomon–Zhang 2509.03490v2, Thm A.1: any inverse-closed set, θ = ¼ − ε.
  - Bu et al. §9.2 explicitly contrast their ¼ with Sanders' half-set 1/3.
  - So θ = 1/3 at every fixed density would give DENSE CHOWLA EXPONENT 1/3 FOR EVERY C, beating the 2026 literature.

## Task 1 (main): the cyclic exponent 1/3 at every fixed density α ∈ (0, ½]
1. Read Sanders v2 §§2–4 (Prop. 2.1, Lemmas 2.2–2.3, 3.1, 3.2, Thm 4.1, Lemma 4.2). Write the half-set proof in our
   notation, with the "careful accounting" that yields 1/3 at α = ½.
   - Reconstruct that accounting yourself; the paper only asserts it.
   - Identify exactly where the density enters: r = 2⌈1/α⌉ in Lemma 3.2, and ‖1_A‖_A <= 4M + O(1).
   - Quote statements with versions.
2. Density α. With h = 1_B − α:
       h² = (1 − 2α)h + α(1 − α),
       ĥ⋆ĥ = q(1 − 2α)ĥ + q²α(1 − α)δ_0.
   At α = ½ the linear term vanishes (an involution); for α ≠ ½ it does not.
   - Equivalently, u = h/(1 − 2α) satisfies u² = u + α(1 − α)/(1 − 2α)². So û is idempotent off zero, with the
     zero mode removed (û(0) = 0 when |B| = αq). Sanders' 1_A keeps the zero mode, and that mode is what forces
     r ~ 1/α.
   - THE TARGET: remove the 1/α in r. Run the binomial-positivity argument on a function whose spectrum has no
     zero-mode mass, e.g. u, g = 2·1_B − 1 at α = ½, or a dilation- or Bohr-boosted variant. Then a FIXED r (r = 4?)
     works at every density.
   - Prove K >= c(α)q^{1/3} for all symmetric B ⊂ Z_q, q prime, with |B| = αq (or within O(1) of it), or find the
     exact step that fails and what replaces it.
   - Even any density-independent exponent θ > ¼ (beating JMTZ's ¼ − ε and Bu's dense ¼) is a new result.
   - Track how c(α) depends on α as α -> 0. A polynomial dependence is ideal; any explicit form is valuable.
   - The trivial facts K >= α (from Σλ = −|B|) and the Parseval peak bound Λ >= (α(1 − α)q − K²)/K may help.
     Check them.
   - If 1/3 fails at general α, prove the best exponent you can that beats ¼ at every fixed α.
3. Integer corollary.
   - State and prove: for every C >= 1 there is c(C) > 0 with M(A) >= c(C)|A|^θ for every finite A ⊂ Z_{>0} with
     max A <= C|A|.
   - Make the dependence on C explicit if the cyclic proof allows. Compare with Bu et al.'s constant.
4. Novelty and adversarial checks.
   - Bounded literature check (2010–2026) for symmetric sets of Z_p at general density with exponent > ¼, and for
     dense integer exponents > ¼: Sanders' later papers, Bu et al. §9, JMTZ, Bedert, Shankar, Yip 2610.01657.
     Quote exact statements.
   - Test every lemma against the round-13 fakes: R13-PK profile roundings, R13-C, R13-M2. Make sure no step relies
     on information those fakes satisfy, unless it is a genuine Boolean identity.
   - Numerically, on the VM: check the key inequalities on exact small-q data, e.g. q <= 61 with Gurobi, at α = ¼
     and α = 1/8.

## Task 2 (bounded): explicit constants
- If Task 1 succeeds, extract an explicit c(C) for the integer corollary, at least for C ∈ {8, 16, 32}.
- Say whether it is competitive with Bu et al.'s ((n − 1)/(64·C·200000))^{1/4} at moderate n. A rough break-even n is
  enough.

## Deliverable
- Either a full proof of the cyclic 1/3, or the best exponent above ¼, at every fixed density, with the integer
  corollary; or the exact obstruction to transferring Sanders' argument, with an explicit example or a precisely
  identified missing step.
- Say exactly what is new versus quoted. Preserve every failed step with its counterexample.
