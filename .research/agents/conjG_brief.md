# Brief: Conjecture G (run-tops vs K²) in the finite-field model Z_3 × H

## Exact statement
Γ finite abelian, A = −A ⊂ Γ \ {0}, F(χ) = Σ_{a∈A} χ(a) >= −K for all characters χ, t ∈ Γ,
B_t = {m ∈ A : m − t ∈ A, m + t ∉ A}.  CONJECTURE G: |B_t| <= C·K² with an absolute C (Paley sets give C >= 1/2).
Why it matters (verified): upper bounds valid in all Z_N transfer to Z (embed A ⊂ [−X,X] in Z_N, N > 4X + 4|t|); in Z
Shankar (arXiv 2609.05338) gives Σ_{t∈A}|B_t| = 6Q − 4I >= T/3 and Roth gives T >= n²/K − nK, so some t has |B_t| >= n/(3K) − K/3.
Hence G (even only for cyclic groups) ⇒ Chowla K >> n^{1/3} in Z (current record n^{1/5}).

## What is known here (read .research/PROOFS.md P19, Conjecture G; .research/NOTEBOOK.md last entries; EXPERIMENTS E30)
- Bedert's Prop 7.3 gives |B_t| << K^4 in every finite abelian group. P19 (agent, proved): no argument using F >= −K only
  through finitely many A-independent degree-r Fourier/convolution inequalities can beat K^{2r}; any proof of G must use
  pointwise positivity at all characters STRUCTURALLY (additive combinatorics / coset structure), not via averaged
  polynomial identities.
- Slice form in Γ = Z_3 × H, t = (1,0): fibres A_h ⊂ Z_3; c(h) = |A_h|; u(h) = Σ_{i∈A_h} ω^i ∈ μ_6 ∪ {0}, u(−h) = conj u(h).
  F at characters (j, ψ): j = 0 gives ĉ(ψ), j = 1 gives û(ψ), j = 2 gives û(ψ^{-1}). u ∈ −μ_3 exactly on 2-point fibres
  D (|B_t| = |D|), u ∈ μ_3 on singleton fibres E, u = 0 on empty/full fibres; u³ = 1_E − 1_D. Proved: if u(0) = 0 then
  |D| <= |E| + K³ (threefold convolution of û + K >= 0). Equivalent slice sets: S_i = {h : i ∈ A_h}, S_2 = −S_1,
  a = 1̂_{S_0}, z = 1̂_{S_1}: constraints a + 2Re(ω^j z) >= −K for all ψ, j; consequences |z| <= a + K, |S_1| <= |S_0| + K,
  Σ_{ψ≠1}|z(ψ)| <= K|H| (spectral norm of 1_{S_1} <= K + 1).
- Failed construction (lead): u = ζ_6^{λ(h)} for a homomorphism λ makes û >= 0 but forces D to be an index-2 coset,
  and then ĉ = −|H|/2 (K grows like |H|).
- Numerics (E30): simulated annealing over Z_m^d, cyclic Z_N: max |B_t|/K² <= 1/2; Paley sets are local maxima.

## Task (computations allowed but small: use `src/localrun.sh -m 2 -t 1800 python ...` from the repo root, ONE job at a
## time, each < 30 min; nothing else heavy runs on the laptop now)
Pursue BOTH, report honestly:
(1) FALSIFICATION: a structured search for |B_t| >> K² (or ratio > 1/2 growing with the group) in Z_3 × F_3^k and in
    Z_9 × ..., Z_p: e.g. A = signed/ symmetric unions of a few cosets of subgroups, quadrics {Q(x) = c}, Paley-like
    cyclotomic sets, and local-search moves that add/remove whole cosets or lines (not single points). Record the best
    ratios with exact K (characters enumerated; verify any claimed record with exact arithmetic where cheap).
(2) PROOF: try to prove G (or |D| <= CK^{2+ε}, or K³ — anything below K^4) in Z_3 × H using the slice form plus genuine
    structure (e.g. spectral norm of 1_{S_1} <= K + 1 ⇒ coset structure with POLYNOMIAL losses in this special
    situation? large-spectrum / Chang-type arguments? a weighted version of |D| <= |E| + K³ that kills |E|?). Or prove G
    for a natural subclass (e.g. A ∪ {0} a union of cosets; |H| ≤ K^C; S_0 = ∅ or S_0 a subgroup).
Deliverable: .research/agents/conjG_report.md with statements labelled PROVED / CONDITIONAL / NUMERICAL / FAILED,
complete proofs, exact search spaces and best examples (sets written out), and the most promising next lemma. Do not
edit other .research files, do not commit. Keep quantifiers exact (∀ characters, sets not multisets, A = −A, 0 ∉ A).
