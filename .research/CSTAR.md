# CSTAR — THE problem. Read this first, every session.

**Rule (user, 2026-10-19).** C* is the problem. Every route in ROUTES.md reduces to it. Work that does not advance C*
is a side lemma. A side lemma is recorded in one line (PROOFS + the index at the bottom of this file) and is never
the goal of a session. "C* needs a new idea" is not a diagnosis and not a stopping point. The math must be made here.

Every work item must name the C* step it serves: OBJECT (§1), DESIGN (§3, construction), CHAIN (§4, proof) or
ATTACK LOG (§5). If it serves none of them, do not do it.

## 1. The object (fixed formulation; do not re-derive)
Conventions: T = R/Z, e(x) = e^{2πix}, A ⊂ [1, X], |A| = n, f = Σ_{a∈A} cos(2πax), M = −min f, ε = M/√n.
S = A ∪ (−A), D_S = Σ_{s∈S} e(sx) = 2f, K := 2M.

(O1) Density form. p := 1 + D_S/K = 1 + f/M is a probability density. p̂(k) = 1/K for k ∈ S and 0 for k ∉ S ∪ {0}.
     ∫p² = 1 + |S|/K² = 1 + 1/(2ε²).
     **Chowla ⇔ every such p (S finite) has ∫p² <= 1 + C.  A counterexample ⇔ a family with ∫p² → ∞.**
(O2) Idempotent form. D_S is an idempotent trigonometric polynomial (coefficients in {0, 1}), D_S >= −K, and
     ‖D_S‖₁ = 2∫(D_S)_− <= 2K. Chowla ⇔ |S| <= C·K². (Littlewood/MPS gives only ‖D_S‖₁ >~ log|S|. Cohen and
     Green–Sanders structure costs exp(exp(K^4)), which is useless here.)
(O3) Exact mixing ⇔ two-valuedness (identity). p ⋆ p = (1 − 1/K) + p/K holds iff p̂(k)² = p̂(k)/K for all k ≠ 0, i.e.
     iff p̂ ∈ {0, 1/K}. Probabilistically: if Y₁, Y₂ are iid ~ p, then Y₁ + Y₂ ~ (1 − 1/K)·Unif + (1/K)·p, and an r-fold
     sum is uniform except with weight K^{1−r}. This is not an extra constraint; it IS Booleanity.
(O4) Factor form (P1, day 1). By Fejér–Riesz, p = |Q|² with Q of degree X. Q's aperiodic autocorrelation is two-valued,
     {0, 1/K}, off 0, and the kurtosis is ‖Q‖₄⁴/‖Q‖₂⁴ = 1 + 1/(2ε²). Chowla ⇔ kurtosis bounded.
(O5) Atomic heuristic. p ≈ Σ_j w_j·(bump of width 1/X at x_j), with m ≈ 4ε²X atoms. So Chowla ⇔ the spike set has
     positive measure. Counterexample ⇔ m = o(X) points whose exponential sum on [1, X] is two-valued (≈ m/K on n
     frequencies, ≈ 0 elsewhere), together with a taper that makes p̂ vanish beyond X with p >= 0. Atomic ν with an
     exactly two-valued transform on all of Z is periodic (K = 1, S = qZ). The band edge X is what costs Gibbs.

## 2. What is known about a counterexample (forced features; each with its source)
| # | Feature | Status | Source |
|---|---|---|---|
| F1 | ∫p² = 1 + 1/(2ε²) | exact | O1 |
| F2 | Concentration dichotomy. Either the spikes with f > √n/ε (p > 1/ε²) carry a constant share of ∫p², or >= const mass of p sits on {p > 1/(4ε²)}, which has measure <= 4ε² (Markov). Proof: ∫p² <= t + sup(p)·∫_{p>t} p | proved (elementary) | cont. 25.7, made exact here |
| F3 | Sparse: X/n >= 7.72 eventually (T-dense), and >= 13.7 if M = o(n^{1/3}) | proved (P61–P63, P66) | STATE |
| F4 | Macroscopic window spikes (height >= c·n_H) lie on the front's spikes; at most 1/(c²ρ_H) per scale | proved (P28) | cont. 25.6 |
| F5 | The concentration set E is additively random-like at its own scale (arcs and Bohr E are forbidden) | heuristic-sharp | cont. 25.7 |
| F6 | Dissociated spike sets (order 6) are impossible when m <~ √X | proved in outline | cont. 25.3 |
| F7 | Weak-L¹ (Carathéodory): P(f > s) ≈ cM/s on M <~ s <~ √n/ε (multifractal, maximally heavy-tailed) | heuristic | cont. 25.6 |
| F8 | Flat sets (negative region of positive measure) lose only constant factors under weight perturbation | proved (P72(b)) + E103 | — |
| F9 | Every known near-extremizer is flat: β_K ≈ 0.18+ and R >= ½ | numerical | E68, E104 |
| F10 | Variance conservation. For ANY random A with marginals w_a = P(a ∈ A), and any correlations: ∫Var(f_A(x))dx = ½Σ_a w_a(1 − w_a). Rounding noise cannot be destroyed, only moved in x. A random construction must move all of it under the positive spikes of E f | proved (exact: ∫cos(2πax)cos(2πbx)dx = δ_ab/2) | this file, 2026-10-19 |

## 3. DESIGN — constructive side (build the object on purpose)
Design rules implied by §2. A candidate that violates one is dead before it is run.
- D1 (F1, F2): concentrated. Mass on a set of measure ~ε² (or on high spikes), not flat.
- D2 (F6): not dissociated at small m. The spike positions must carry additive relations.
- D3 (F5): those relations must not make E an arc or a Bohr set at its own scale (mixing). So it needs additive
  relations among the spike positions at scale 1/X, with E random-like at scale ε². This is the central tension.
- D4 (F4): no macroscopic interior window spikes beyond a bounded frame.
- D5 (F3): sparse, X/n -> ∞ or at least > 7.72.
- D6 (F10): if randomized, the rounding noise must be spectrally confined under the spikes of E f.
- D7 (O5): the band edge must be tapered inside the construction, not by truncation.
Open design question Q-D: which point configurations {x_j} (m = o(X)) have exponential sums on [1, X] that are
two-valued, carry additive relations (D2), and are not Bohr-like at scale ε² (D3)?

## 4. CHAIN — proof side (the lemma skeleton; status of each step)
- (a) Flat/front regime: proved (P28, P61–P66, P72(b)).
- (b) INV: 1_S ≈ Kν̂ with ν = p·1_U, U = {f > √(n/ε)}, error η = O(√ε) (P40(c)). Proved.
- (c) MANY-SPIKE LEMMA, the C* core: INV + positivity + window domination ⇒ K >= c√|S|, or ν is near a GAP of
  bounded rank. Dissociated half proved (F6). OPEN: mesoscopic, non-dissociated, random-like E.
- (d) Structured alternative ⇒ PR(r) + Gibbs (P71-type packets). Rank 1: P73/P74. Rank r: open, believed routine.
The prize is (c). Everything else is support.

## 5. ATTACK LOG (newest last; each entry: claim → test/derivation → where it broke → extracted lemma or design rule)
- A0 (2026-10-19, cont. 25). Window domination + INV. Broke: mesoscopic spikes are invisible at every scale.
  Extracted: F4 is bounded per scale; F5.
- A1 (2026-10-19, this session). Noise shaping (Σ-Δ / co-designed rounding). Claim: round a smooth profile w so that
  the rounding error's spectrum sits under E f's spikes (F10/D6).
  Derivation: shaped noise confined to a region Ω around x₀ means e_a = e(ax₀)·(sequence smooth at scale 1/|Ω|). With
  e_a ∈ {−w_a, 1 − w_a}, that is again a structured 0/1 selection whose own Chowla problem sits at the next scale.
  This is the taper tree (ROUTES), and the earlier E23 and round-13 numerics (R growing) are its first-order instance.
  Extracted: F10 (exact) and D6. Open sub-question: can the recursion depth grow while the loss per level is
  summable? That is the construction form of C*, taken up in A2.

## 6. Side results (recorded; NOT the prize)
P71.2 (kernel), P72 (a–c proved; d, e gaps), P73 (kernel, Z), P74, E103–E105, Ruzsa-question status. See PROOFS.
