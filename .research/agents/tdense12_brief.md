# Math brief (codex research agent), round 12: the coupled front problem (FRONT-½), Parseval roughness, cyclic half-sets

You are a research mathematician working on Chowla's cosine problem in /Users/jmercedes/Desktop/Projects/Research/chowla-cosine.
- Read CLAUDE.md first: conventions, honesty labels, and the rule that numerics are not proofs.
- Conventions: f_A = Σ_{a∈A} cos(ax), M(A) = −min f_A, n = |A|, X = max A.
- Rules (unchanged):
  - Do NOT edit .research/*.md. Do not commit. Do not launch subagents. No LaTeX; markdown only.
  - Report: `.research/agents/tdense12_report.md` (keep it current). Scratch: `.research/agents/tdense12_scratch/`.
  - Computation ONLY on the VM via `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 ...` (at most 4 cores).
  - Gurobi for every LP/MILP/QP.
  - Label every claim PROVED / NUMERICAL / HEURISTIC / CONJECTURED, with exact quantifiers.
  - Grep PROOFS.md before any novelty claim.

## State (read PROOFS P58–P63, NOTEBOOK cont. 12–16, and your round-11 report)
- T-dense(C) is PROVED for every C < 2000/259 = 7.722 (P63). The exact second-order reach is 1/D ≈ 8.571 (P61). The
  dilation/support-line certificate family saturates near D ≈ 0.129, so do NOT spend time on certificates this round.
- Your round 11 (P63):
  - the DC-barrier theorem;
  - the repair-energy lemma;
  - the torsion budget Σ_{rational θ≠0} W_θ(0) <= ½ − a;
  - full-Haar kurtosis >= 3/2;
  - the Paley boundary.
- Lead's new observations (NOTEBOOK cont. 15–16). Test them; do not take them on trust.
  1. FRONT-½. P61 step 9 gives d <= 4a(1 − a)D, where a = p(0). So a universal a* < ½ with a <= a* in every dense
     binary counterexample limit gives T-dense(C) for C < 1/sup_w ∫_0^1 φ(4a*(1 − a*)w²), BEYOND 1/D.
  2. Front object. At a = ½, for fixed small ε and Y = εX, s_k = 2·1_A(k) − 1:
         S(x) = Σ_{k<=Y}(1 − k/Y)s_k cos kx >= −4m − o(√Y)   on Y^{−1/2} <= |x| <= π.
     This is the Fejér low-pass of h = g + m >= 0. The torsion budget removes all macroscopic rational atoms.
     So FRONT-½ ⟸ TBS: every locally balanced sign sequence on [1, Y] without macroscopic rational atoms has
     min_{|x| >= Y^{−1/2}} S(x) <= −c√Y. Untapered, this is P34 (kernel-checked). The taper admits s ≡ 1 and
     s = (−1)^k.
  3. CYCLIC BARRIER: TBS ⇒ √-strength cyclic half-set Chowla, which is open (Sanders 0807.5104v2 Thm 1.2 has exponent
     1/3).
     - Let S ⊂ Z_q (q prime) be a symmetric half-set with λ_γ >= −K (γ ≠ 0), and s_c = 2·1_S(c) − 1.
     - For L periods (Y = Lq): S(x) = (1/(2q))Σ_γ λ_γ F_Y(x − 2πγ/q) − s_0/2 >= −O(KL) − O(1).
     - Stronger (lead, to verify): for ANY Y <= q (a partial period) with Fejér taper τ, Σ_γ F_τ(x + 2πγ/q) = q.
       Hence S(x) >= −K/2 − O(1).
     - So a front-only proof of FRONT-½ would prove the cyclic conjecture. A proof must use the TAPER COUPLING.
  4. Taper coupling.
     - All local patterns share one spike set, with PD envelopes, so |m_θ(t)| <= 1 (Fourier domination by the front
       pattern).
     - In the exact macroscopic model: a PD indicator is a subgroup, so there is no taper (cont. 15.2).
  5. Parseval roughness (cont. 16.4).
     - Model: locally N-periodic binary families with E_t ⊂ Z_N nested, N << window << X. Then exactly
           Σ_{s≠0}|∫1̂_{E_t}(s)e^{iξt}dt|² = ∫(−p')·4sin²(ξu/2)/ξ² − |p̂(ξ)|² ≈ 2p(0)/ξ².
       So spike envelopes are forced to be Hölder-½ rough.
     - This gives M >~ X p(0)/(N d ξ²) (lead, sketch) and heuristically M >~ X√(p(0)/N). That would exclude periodic
       fronts with N << X.

## Task 1 (main): FRONT-½ through the coupling
- Verify or refute items 2 and 3 above (especially the partial-period identity and its use) with exact quantifiers.
- Then decide one of the following:
  - (A) PROVE a <= a* < ½ (an ineffective constant is fine) using information beyond the front: the taper region,
    Fourier domination, energy-PD, the torsion budget, Parseval roughness, P53-type rigidity. State the resulting
    T-dense range.
  - (B) Prove that FRONT-½ (or any binary statement improving 1/D through the front) is EQUIVALENT to, or implied by, a
    precisely stated cyclic or coupled statement. Identify the weakest such statement that would suffice. Example: a
    cyclic half-set lemma restricted to sets that admit a PD-envelope continuation to density 0.
  - (C) Exhibit an obstruction: a coupled object satisfying every proved constraint, with a = ½ and binary two-point
    local laws on a macroscopic front, conditional on an explicitly named cyclic hypothesis.
- Whatever you prove, preserve every failed step with its counterexample.

## Task 2 (bounded): the rigorous Parseval-roughness theorem
- Formalize a model of locally N-periodic binary sets: A ∩ window = {k : k mod N ∈ E_t} on windows of length L with
  N << L << X; E_t need not be nested, so state what replaces |E_t ∩ E_t'|.
- Prove the best lower bound you can for M in terms of X, N, p(0) and d, with exact quantifiers. Is M >~ X/N
  provable? Is X√(p(0)/N) provable?
- Search adversarially, on the VM, for structured removal schedules (coset removals, multiplicative cosets, Bohr
  slices) that concentrate the roughness on few characters with POSITIVE spikes and so evade X√(p/N).
- State precisely which mesoscopic structures this excludes. This is a quantitative P53.

## Task 3 (exploratory, capped at about a third): the cyclic half-set exponent
- Target: symmetric half-sets S ⊂ Z_p (p prime): −λ_min >= c p^θ with θ > 1/3 (Sanders), ideally ½.
- Available tools:
  - P26 (half-sets ⟺ symmetric weighted near-planar difference sets);
  - line-D identities (h⋆h = const, h^{⋆3} = p²h + p²λ(λ − 1)(λ − 2) for h = ĝ + λ, g = 2·1_S − 1);
  - the spectral gap ĝ(γ) <= λ³/2;
  - the elementary p^{1/4} in the project record;
  - E41 exact optima (p <= 89: dilates of near-intervals; sub-Paley for p >= 37).
- Any rigorous exponent improvement, or a conditional one with an explicitly named missing lemma, is valuable. If you
  find the exact obstruction to improving 1/3 in these methods, record it as a barrier with a precise example.
- Short literature check: any 2024–2026 work on half-sets / dense Chowla in Z_p beyond Sanders? Quote exact theorems
  and versions.

## Deliverable
- Task 1: (A), (B) or (C) with full proofs and quantifiers, plus verification of the lead's reductions.
- Task 2: the theorem, the adversarial search results and the excluded structures.
- Task 3: the exponent result or a precise barrier, plus literature facts.
Say exactly what is new versus quoted.
