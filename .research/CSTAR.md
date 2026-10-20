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
     **Chowla (some c₀ > 0) ⇔ every such p (S finite) has ∫p² <= 1 + C. A counterexample ⇔ a family with ∫p² → ∞.**
     Exactly ∫p² = 1 + 1/(2R²). So the SHARP conjecture C½ (R >= ½) is the specific bound **∫p² <= 3**. Proving
     some C does not prove C½ (advisor, 2026-10-19). Track which one a claimed result reaches.
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

(O6) THE OBJECT EXISTS IN FINITE GROUPS: quadrics in F_p^r (lead, 2026-10-19; standard Gauss-sum computation).
     Take A = {x ∈ F_p^r \ 0 : Q(x) = 0}, Q a nondegenerate quadratic form, r EVEN >= 4, p odd.
     - Spectrum (exact): Σ_{x∈Q} e(ξ·x/p) = η p^{r/2−1}(p − 1) on the dual cone Q*(ξ) = 0, and −η p^{r/2−1} off it.
       Here η = ±1 is the Gauss sign χ((−1)^{r/2} det Q). Up to the trivial character it is TWO-VALUED.
     - Choose Q with η = +1. Then M = p^{r/2−1} + 1, n ≈ p^{r−1}, so R ≈ p^{−1/2} → 0 (fixed r, p → ∞), and
       M ≍ n^{(r−2)/(2(r−1))}: n^{1/3} at r = 4.
     - Odd r gives no gain (the off-cone values ±p^{(r−1)/2} carry both signs).
     - η = −1 puts the spikes NEGATIVE (M ≍ p^{r/2}).
     - Anatomy, matching F1–F7 exactly:
       - spikes on the dual cone, of measure ε² ≈ 1/p, at height ≈ √(np) = √n/ε (mesoscopic);
       - a flat negative background −ε√n;
       - the cone is random-like additively at its own scale;
       - the spike set is invariant under scalar multiplication (lines through 0).
     So C* in Z is precisely: can this anatomy be realized with distinct positive integers, i.e. through the band
     limit / taper and in a torsion-free group? A proof must use the Z-features that the quadric lacks:
     - the front and band limit (no box in Z is a group; the box boundary causes Gibbs);
     - torsion-freeness (no lines through 0; dilation does not preserve [1, X]).
     The quadric lift (ROUTES) fails at the taper: a sub-selection C' ⊂ C of relative size s has error spectrum of
     RMS √(s(1−s)|C|) by Parseval (F10). Open finite question: can that error spectrum sit ON the dual cone?
     ("algebraic taper": C ∩ {Q₁ = 0} ∩ ⋯ nested complete intersections; Deligne-type bounds suggest no.)

## 2. What is known about a counterexample (forced features; each with its source)
| # | Feature | Status | Source |
|---|---|---|---|
| F1 | ∫p² = 1 + 1/(2ε²) | exact | O1 |
| F2 | Concentration dichotomy. Either the spikes with f > √n/ε (p > 1/ε²) carry a constant share of ∫p², or >= const mass of p sits on {p > 1/(4ε²)}, which has measure <= 4ε² (Markov). Proof: ∫p² <= t + sup(p)·∫_{p>t} p | proved (elementary) | cont. 25.7, made exact here |
| F3 | Sparse: X/n >= 7.72 eventually (T-dense), and >= 13.7 if M = o(n^{1/3}) | proved (P61–P63, P66) | STATE |
| F4 | Macroscopic window spikes (height >= c·n_H) lie on the front's spikes; at most 1/(c²ρ_H) per scale | proved (P28) | cont. 25.6 |
| F5 | The concentration set E is additively random-like at its own scale (arcs and Bohr E are forbidden) | HEURISTIC (not an exclusion) | cont. 25.7 |
| F6 | Dissociated spike sets (order 6) are impossible when m <~ √X | PROOF OUTLINE only (constants unwritten) | cont. 25.3 |
| F7 | Weak-L¹ (Carathéodory): P(f > s) ≈ cM/s on M <~ s <~ √n/ε (multifractal, maximally heavy-tailed) | heuristic | cont. 25.6 |
| F8 | Flat sets (negative region of positive measure) lose only constant factors under weight perturbation | proved (P72(b)) + E103 | — |
| F9 | Every known near-extremizer is flat: β_K ≈ 0.18+ and R >= ½. Sparse SA (E106, n <= 128) finds only Beatty dilates of dense sets (one macroscopic spike, R >= 0.85) | numerical | E68, E104, E106 |
| F10 | Variance conservation. For ANY random A with marginals w_a = P(a ∈ A), and any correlations: ∫Var(f_A(x))dx = ½Σ_a w_a(1 − w_a). Rounding noise cannot be destroyed, only moved in x. | IDENTITY proved (∫cos(2πax)cos(2πbx)dx = δ_ab/2). The reading "noise must sit under the spikes of E f" is HEURISTIC: large Var(f(x)) where E f ≈ 0 forces negative values only with an anti-concentration input, which is not proved | this file, 2026-10-19 |
| F11 | No flat multiplicative orbits (torsion-freeness, quantified). For every x ∈ T and K >= 1, with Fejér weights w_k = 1 − abs(k)/(K+1): Σ_{0<abs(k)<=K} w_k f(kx)² >= ½n(K+1) − n². Proof: Σ_k w_k f(kx)² = ½Σ_{a,a'}F_K((a−a')x) + ½Σ_{a,a'}F_K((a+a')x) >= ½n(K+1), from the diagonal a = a' with F_K >= 0. So every orbit segment {kx : 0 < k <= 4n} carries orbit-L² >= n²/2. In F_p^r the quadric's off-cone LINES are exactly flat (f ≡ −M). In Z no orbit is flat. Mild: it holds for any random-like E and kills only line-aligned spike sets (with D8) | proved (elementary) | this file, A3 |

| F12 | RETRACTED in its first form ("C* needs phase cancellation"). What holds: FLAT completely positive certificates (P76) are 1.3–1.5× too expensive on dense near-optima. N50_x72: R_CP(flat) = 0.857 against R = 0.570, lead-verified. BUT non-flat nonnegative (two-level {0,1,2}) CP certificates come within 1–8% of M. X30_s0 (n = 20): R_CP <= 0.655 against R = 0.607, lead-verified exact. X = 11, 12 optima: within 1%. So near-extremal certificates are cancellation-free once block WEIGHTS are non-flat. What is forced is non-flat (weighted) blocks, not phase cancellation. Two-level CP also beats 1/√2 at n = 20, so CP½ is a FLAT-class statement only | numerical (E111) | this file, A6 |
## 3. DESIGN — constructive side (build the object on purpose)
Design rules implied by §2. A candidate that violates one is dead before it is run.
- D1 (F1, F2): concentrated. Mass on a set of measure ~ε² (or on high spikes), not flat.
- D2 (F6, outline only): not dissociated at small m. The spike positions must carry additive relations.
- D3 (F5, heuristic only): those relations must not make E an arc or a Bohr set at its own scale (mixing). So it needs additive
  relations among the spike positions at scale 1/X, with E random-like at scale ε². This is the central tension.
- D4 (F4): no macroscopic interior window spikes beyond a bounded frame.
- D5 (F3): sparse, X/n -> ∞ or at least > 7.72.
- D6 (F10 reading, heuristic): if randomized, the rounding noise must be spectrally confined under the spikes of E f.
- D7 (O5): the band edge must be tapered inside the construction, not by truncation.
- D8 (A3, heuristic + E109): aperiodic at every scale Q << X (periodicity amplifies rounding noise by √(X/Q)).
- D9 (A3, heuristic): spectrally irreducible (disjoint-spike sub-pieces would each need R <~ R/√J).
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

- A2 (2026-10-19). AUTOMATIC SETS as the design class (new; not in ROUTES before today). Reason: they are the
  taper tree with unbounded depth L = log_b X, built in by construction. Their spectrum is a matrix Riesz product
  F_L(x) = e₀ᵀ M(b^{L−1}x)···M(x) 1, with M(y) = Σ_d C_d e(dy) and C_d the digit-d transition 0/1 matrices. It is
  multifractal, with spikes at b-adic rationals of every depth k: mesoscopic for 1 << k < L/2. For λ < b
  (n = X^α, α = log_b λ) the front is power-law loaded (density ~ u^{α−1}). Booleanity is automatic: it is a set.
  Derivation (lead, asymptotic L → ∞, C primitive; C^m ≈ λ^m r πᵀ):
  - Spike values. f(j/b^k) ≈ n·μ̂_k(j). Here Φ_k(j) := πᵀ M(j/b)···M(j/b^k) 1 and μ̂_k(j) = Φ_k(j)/Φ_k(0) is the
    DFT on Z_{b^k} of the π-weighted low-digit language.
  - Spike profiles. F_L(j/b^k + y) ≈ Σ_t F^{(t)}_{L−k}(b^k y)·(w_{jk})_t, with w_{jk} = M(j/b)···M(j/b^k)1. Under the
    Parry measure every top-language profile ν_t equals ONE measure ν on [0, 1], with ν([d₁…d_p]) = λ^{−p}
    r_{s(d₁…d_p)}/r₀. So the twisted profile at every b-adic spike is Re[Φ_k(j)·ν̂(s)], s ∈ R.
  - NECESSARY (NOT sufficient) for R_L bounded (let alone → 0). It controls only FIXED depths k; spikes at depths k = k(L) that grow with L (the mesoscopic cloud) are not controlled: the negativity there is λ^{L−k}|min_s Re[Φ_k(j)ν̂(s)]|, which must be
    O(λ^{L/2}) for every FIXED k. So EXACTLY Re[Φ_k(j)ν̂(s)] >= 0 for all s, j, k. With θ_ν := π/2 − sup_s|arg ν̂(s)|,
    this says: every b-adic spike value Φ_k(j) lies in the sector |arg| <= θ_ν (or is 0), and Re ν̂ >= 0 (the main
    profile is PD).
    - The power-law front gives ν̂(s) ~ Γ(α)(−2πis)^{−α}, so θ_ν <= (1 − α)π/2.
    - Sparse automata get a SECTOR condition, not reality: less rigid than the exact-PD conditions that kill dense
      or rational templates.
  - Dichotomy: an automatic family either satisfies this sector condition at every b-adic rational, or has
    M >= c·n·λ^{−k₀} (linear in n).
  - Periodic orbits. For x of exact ×b-period p, F_L(x) ~ ρ(Q_x)^{L/p} with Q_x = M(b^{p−1}x)···M(x). If
    |ρ(Q_x)|^{1/p} > √λ, then ρ(Q_x) must be REAL POSITIVE; otherwise the phase rotates with L and M >= |ρ|^{L/p} >> √n.
  - Global cone obstruction (PROVED, but TAUTOLOGICAL: it restates that negative excursions exist; useful only if a cone ESCAPE is shown to cost >= c√n). If every M(y) mapped one complex cone K ∋ 1 (with e₀ᵀK in the right
    half-plane) into itself, then Re F_L >= 0 everywhere, so f >= −1: impossible (M → ∞). So a "bad" set B ⊂ T is
    unavoidable. A counterexample must keep every trajectory that passes through B at growth < √λ, or map it back
    into K. Tool candidate: Rugh's complex-cone Perron–Frobenius (contraction of complex cones under perturbations
    of a positive matrix).
  E107 RESULT (small automata, exhaustive): no automaton has R_L decreasing (168k screened). The exact sector
  violation has min D = 0.102 over 11.9k automata (b <= 5, S <= 4), and the binding constraint is the MAIN profile
  (front, h₀ >= 0.085).
  E107c (annealing, S <= 10, b <= 6): D >= 0.06. The violation of Re ν̂ >= 0 is SCALE-INVARIANT: min Re ν̂ ≈ −0.06 to
  −0.09 equally at s ≈ 0.75, s ∈ [3, 30] and s ∈ [30, 400].
  - Mechanism: a finite-state Parry measure is singular and non-Rajchman, so ν̂(b^m σ) does not decay and repeats its
    negative excursions at every b-adic scale. Equivalently, the stationary Parry measure μ_P on T is not positive
    definite.
  - Contrast: a pure power-law front u^{α−1} on [0, 1] IS PD for α <~ 0.68 (E107 plaw). Sparsity is not the obstruction;
    finite-state singularity is.
  VERDICT A2: dead for finite automata (S <= 10, b <= 6), with linear M; the mechanism is recorded above.
  What survives (the reduction):
  - ×b-invariant PD measures exist, e.g. the Riesz product Π_{i>=0}(1 + a·cos 2πb^i x), 0 < a <= 1, b >= 3, with
    nonnegative coefficients and invariance (μ̂(bj) = μ̂(j)).
  - A set whose distribution at every scale is such a Riesz density would satisfy the b-ADIC (integer-frequency)
    conditions. CORRECTED (review, cont. 30): it does NOT satisfy all macroscopic conditions. The main-profile
    condition is Re ν̂(s) >= 0 at every REAL s for the profile on [0, 1], and nonnegative integer Fourier
    coefficients on T do not give that (the untapered uniform profile already has Re ν̂ < 0 on s ∈ (½, 1)). A front
    taper is needed in addition.
  - But it is not finite-state: realizing it as a set means ROUNDING a multifractal PD density, which is the taper
    tree again. The density is explicit: R(a/X) = Π_j (1 + a·cos 2π(a/b^j)), a Gibbs weight on digit strings.
    "Riesz rounding" is the sharpest constructive form of C* found so far.
  Side fact (Mahler, classical): exp∫log(f_A + M) >= 1/2 (z^X(f + M) has leading coefficient ½). Gives only θ <=
  log(2M)/log(1/δ) for {p <= δ}; logarithmic, not a C* tool.
  Side fact (unimodular factors): the extreme lag max(B) − min(B) has multiplicity 1, so a unimodular Fejér–Riesz
  factor has an exactly two-valued autocorrelation only with λ = 1 (Sidon). Phased digit-cube designs are dead.

- REVIEW after A1, A2 (2026-10-19). Both reduce to one constructive core: ROUND a PD multifractal density (Riesz
  product / quadric spectrum) to a set, with the rounding noise confined under the spikes, recursively. O6 shows the
  object exists in F_p^r, so the obstruction is purely the Z-features (band limit, order, torsion-freeness).
  - Next constructive test: does F_p^r admit an "algebraic taper", i.e. sub-selections of the quadric whose error
    spectrum lies on the dual cone?
  - Next proof-side target: a quantitative statement that each taper level costs a fixed fraction of the spike
    height (Gibbs) or adds noise (F10), with no recursion that pays both less.

- ADVISOR REVIEW (2026-10-19), adopted.
  (i) ∫p² <= 3 ⇔ C½ is distinct from "some C" (O1).
  (ii) A2's sector condition is necessary, not sufficient. The open part is uniform control of negative excursions at
       depths k(L) → ∞, i.e. the many-spike lemma again.
  (iii) FINITE-PREFIX CERTIFICATE (FPC, advisor). For a primitive automaton with Parry measure ν from s₀ and
        admissible words w of length h (cylinder mass q_w = λ^{−h}r_{s(w)}/r_{s₀}, left endpoint u_w):
            |ν̂(t) − Σ_{|w|=h} q_w e(t u_w)| <= 2π|t|/b^h,
        and Σ_w q_w e(t u_w) = λ^{−h} e_{s₀}ᵀ M(t/b)···M(t/b^h) r / r_{s₀}.
        So Re(...) + 2π|t|/b^h < 0 certifies Re ν̂(t) < 0, hence M(A_L) >= (|Re ν̂(t)| − o(1))|A_L|.
        Advisor's Fibbinary instance: t = 1, h = 8 gives Re ν̂(1) < −0.0318.
  (iv) Turn A2 into a YES/NO question: either PROVE every nontrivial sparse primitive automaton fails an FPC (main
       profile or b-adic sector), or EXHIBIT a survivor and analyse its depth-dependent (mesoscopic) matrix products.
       More screening alone decides neither.
  (v) Verdict accepted: CSTAR is a better discipline; it is NOT yet an advance on the many-spike lemma (step (c)).
  (vi) FPC implemented in ball arithmetic: src/e108_fpc.py (python-flint arb/acb, 128 bits).
       - λ is a rigorous root of charpoly(C), isolated by real part; r is an arb_mat solve.
       - Advisor's Fibbinary numbers reproduced exactly: Σ = −0.05636818, bound < −0.03182448 (t = 1, h = 8).
       - Tightened with h = 24: Re ν̂(1) < −0.0578943, so M(A_L) >= (0.0579 − o(1))|A_L|.
  (vii) T-A2 (the YES/NO question, sharpened by the lead). Along t = b^m j, ν̂(t) → μ̂(j), where μ is the STATIONARY
        Parry measure (the max-entropy measure of the sofic shift, viewed on T). So a single integer j with
        Re μ̂(j) < 0 forces an FPC failure.
        CONJECTURE T-A2: the max-entropy measure of a sofic subshift of the b-shift with 0 < h < log b is never
        positive definite (some Re μ̂(j) < 0).
        - Heuristic: ×b-invariant PD measures exist (Riesz products Π(1 + a cos 2πb^i x); Bernoulli convolutions
          ν⋆ν̃), but each needs NON-uniform digit weights (the 0-digit doubled = multiplicity).
        - Maximal entropy forces uniform path weights (a set has no multiplicity), and finite-state splitting of a
          multiplicity recurs at every scale with the same relative defect.
        - T-A2 would answer the advisor's question NO for all primitive automata with s₀ recurrent. It is the
          multiplicity obstruction in ergodic language. Test: src/e108_mu.py.
  (viii) ANSWER to (iv), as far as it goes (E108, P75).
         - FINITE CLASS: YES, all fail. Every one of the 71,840 automata of the sector scan (b = 3, 4, 5; S <= 3) is
           INTERVAL-CERTIFIED to fail the FPC on the MAIN profile, with Re ν̂(t) < −0.084 at a certified t. So
           M(A_L) >= (0.084 − o(1))|A_L| for each, uniformly. No survivor exists, so there are no mesoscopic products
           to analyse in this class.
         - GENERAL: T-A2 is OPEN. P75 (proved, elementary) reduces "not PD" to a 2-point domination-or-twin
           inequality among explicit cylinder weights. It covers 28.5% of the class (float).
         - Obstructions to finishing: (1) base-2 symmetric b = 4 automata tie at u = 1/2 only (fix: descend to
           (×2)_*σ); (2) automata where 0 is the strictly heaviest point need a >= 3-point Gram test.
         - Lesson for C*. A finite-state self-similar law is a FIXED scale-invariant measure. A non-PD measure
           repeats its negative excursion at every scale, which gives linear M. So a C* set cannot carry the same
           finite-state law at all scales: its mesoscopic statistics must CHANGE with depth (the Riesz-rounding
           reduction above). A2 is CLOSED as a design class. Its general theorem T-A2 is a side lemma (§6).

- A3 (2026-10-19, after A2). RATIONAL-SPIKE (Ẑ) ANATOMIES. Every A ⊂ Z is a model set over R × Ẑ (Z is a lattice there).
  Spikes at rationals t/Q see the Ẑ-structure (residues); irrational spikes see the R-structure (Bohr). The quadric's
  "lines through 0" exist in T only as finite subgroups (1/Q)Z/Z. So the F_p^r anatomy, copied into Z, has RATIONAL spikes.
  Test class: residue staircases. W₀ ⊂ Z_Q symmetric, and A ∩ (r + QZ) is the initial segment {a < u_r X} (u_{−r} = u_r).
  - Exact profile (continuous-u model; verified numerically, E109, errors ~1% of values):
        f(t/Q + τ/X) ≈ (X/(2πQτ))·Σ_{r∈W₀} cos(2πrt/Q)·sin(2πτu_r),   1 <~ τ <~ X/(2Q).
    It equals (X/Q)·Re R̂(t, τ), where R̂ is the transform of the staircase window {(r/Q, u) : 0 <= u <= u_r} in Z_Q × R.
  - Where it broke. All three choices of the graph r ↦ u_r fail:
    - Smooth graph: Sturmian/Bohr level sets, Bessel-signed profiles, linear M.
    - Random graph: the rounding noise is confined to the Q columns of width 1/X, so it is AMPLIFIED. Measured
      R ≈ 1.3·√(X/Q): R = 32.4 at Q = 31, X = 2·10⁴ (√(X/Q) = 25), and R = 24.8 at Q = 101, X = 4·10⁴ (√(X/Q) = 20).
    - Structured graph: dual Chowla for the staircase window in Z_Q × R. This is the model-set row ("= C*, dual
      costume") with a finite internal group.
  - Extracted design rules:
    - D8 (heuristic, with E109 numbers): no exact periodicity with Q << X. Periodicity concentrates F10 noise onto
      measure Q/X and multiplies its height by √(X/Q). A Z-C* must be aperiodic at every scale Q << X.
    - D9 (HEURISTIC, union descent). Suppose A = ⊔_j B_j with pairwise disjoint spike sets and independent
      backgrounds. Then the background means add: M >~ Σ_j μ_j, with μ_j ≈ (L² of f_{B_j} on its spikes)/(its spike
      height). With J equal pieces this forces R(B_j) <~ R(A)/√J: every piece must be a BETTER C* than the whole.
      The quadric escapes because its pieces (totally singular planes, p + 1 per ruling) are subgroups with M_j = 1.
      Z has no such pieces, so a Z-C* must be spectrally irreducible: its spike set cannot split into the spike sets
      of independent sub-pieces.
  - Route check this session: three further re-derivations were caught and are NOT new:
    - cut-and-project / high-rank balls (ROUTES model-set row, E73);
    - clique covers / stabilizers (cont. 19.8);
    - lower-flat Sidon squares (E8, E15, E29; Bu et al. Prop 8.2).
    The one new quantitative point is E73's mechanism. Window perimeter puts L² ≈ Per/(2π²ρ) beyond radius ρ. That
    forces N·vol >= (c·log X/δ²)^D significant frequencies, whereas a ball's Gibbs is only (2/e)^{D/2}.

- A4 (2026-10-19). BLUEPRINT LEVEL and the missing robust-structure tool.
  - Literature check: one extended search for robust or approximate versions of Ma's theorem (cyclic PDS) and for
    stability of two-valued spectra found nothing. The robust step "approximately two-valued spectrum ⇒ union of
    approximate subgroups" appears to be new territory, not a citation gap.
  - Prime-field face of D8: multiplicative-period sets in Z_p. Take A = union of cosets of a subgroup H of index e. On
    Z_e, f is 1_J ⋆ η, where η is the vector of Gauss periods. η has two-valued autocorrelation (p·δ − |H|), and its
    DFT is the Gauss sums G(χ), each of modulus √p.
    - So one-sidedness needs every arg G(χ) aligned (real Gauss sums). That is the semiprimitive case, which exists
      only in F_{p^{2γs}}, never in F_p.
    - For e >= 3 the phases are equidistributed, so v is random-like.
    - Number-theoretic restatement: the C* object needs elementary-abelian torsion.
  - Blueprint consistency (heuristic, checked by hand). Write the anatomy as a time–frequency blueprint: front density
    ρ₀(u), and twisted local densities ρ_j(u) of the spikes x_j at position u = k/X. Four constraints:
    - local Booleanity: Σ_j |ρ_j(u)|² ≈ ρ₀(u);
    - local Wiener: Σ_j |ρ_j(u)| >= 1, so at least 1/ρ₀(u) spikes are active at every position;
    - twisted <= untwisted: |ρ_j| <= ρ₀;
    - PD profiles.
    These are mutually CONSISTENT. Example: ρ_j = c_j(1 − |u|) gives ρ₀ ∝ (1 − |u|)², which is PD. So no contradiction
    lives at the continuum level.
  - Fractional blueprints are empty. Write 1_A = ρ + e (ρ a profile, e the rounding). Only Σρ²/2 of f's L² can be
    coherent, and C* needs essentially all n/2 in spikes, so ρ must itself be Boolean. Hence C* is entirely a property
    of the 0/1 fine structure. This sharpens A1 and F10: the rounding IS the object.
  - E5 already showed that Bu sets are strict local optima, so a local-search probe from them adds nothing.
  - Next proof-side target: a RANK DICHOTOMY for the Bohr pieces that INV (P40(c)) produces.
    - Low rank: sharp boundaries, hence Gibbs (P70.2-type).
    - High rank: boundary noise approaches Bernoulli (E73, currently numerical only).
    First lemma: a rigorous E73, i.e. M >= c√n·g(d) for model sets with convex windows in T^d, with g(d) bounded
    below uniformly in d.

- A5 (2026-10-19, cont. 28). REFLECTION and a new discriminating class: NONNEGATIVE-GRAM (DNN) CERTIFICATES.
  Mandatory review (number-theory skill §3). A0–A4 all reduce to the same open step: "deterministic ⇒ Gibbs" in the
  random-dominated regime. The rank-dichotomy target (rigorous E73) was re-examined. It only extends step (d), and only
  pays off once step (c)'s structure theorem exists, so it is DEPRIORITISED (not killed).
  Three facts derived this session:
  (i) REGIME SPLIT at n^{1/3} (exact identity plus heuristic reading).
      - Set ν = p·1_U. Since ν <= p, ∫ν·(ν⋆ν) <= (1 − 1/K)ν(T) + (1/K)∫_U p². The random baseline is ν(T)³ and the
        additive EXCESS is ≈ ∫p²/K = 1/(4ε³√n).
      - The excess dominates iff ε <~ n^{−1/6}, i.e. M <~ n^{1/3}. The F_p^4 quadric (M ≍ n^{1/3}) sits exactly at the
        threshold; r >= 6 quadrics are random-dominated.
      - So BSG/Freiman-type structure (the Bedert/Shankar mechanism) can only see M <~ n^{1/3}.
      - The C* core (n^{1/3} << M = o(√n)) has an additive excess that is a vanishing relative perturbation at every
        order: the (r+1)-fold excess is K^{1−r}/(2ε²), from the exact p^{⋆r} = 1 − K^{1−r} + K^{1−r}p.
      - Reading (HEURISTIC, review cont. 30): proofs through the r-fold additive excess cannot see the C* core. This is
        not a theorem ruling out every energy-type method.
  (ii) HOFFMAN BOUND (proved, elementary, standard Delsarte LP). If I ⊂ Z has density α and (I − I) ∩ S = ∅, then
      K >= |S|α/(1 − α). Proof: the autocorrelation of I is PD with spectral mass α and atom α² at 0, and
      0 = Σ_{s∈S}φ(s) >= |S|α² − K(α − α²).
      - Bohr corollary: K >= |S|δ/(1 − δ), with δ = sup_θ min_{s∈S}‖sθ‖.
      - So C* needs every θ to be o(|S|^{−1/2})-approximable by S. Random S satisfy this, so it is a FACT, not a route.
  (iii) OVERDETERMINATION COUNT (heuristic). The spike measure has ~2δX = 4ε²X free parameters but must satisfy ~X
      two-valuedness equations on [−X, X].
      CORRECTED (cont. 29): the original reading compared per-frequency levels and was WRONG.
      - In L², INV forces off-S mass <= η² × on-S mass, whereas a random m-point measure has off/on ≈ X/n. So INV
        does force strong spectral concentration.
      - But that concentration is just ν ≈ p, so it is tautological, not new rigidity.
  CORRECTION (cont. 29, PROVED). DNN with an UNBOUNDED index set is NO restriction.
  - Q_T = (1/T)·Toep_T(λδ + ½1_{±A}) is entrywise >= 0 (since 1_A >= 0) and PSD for λ >= M (Toeplitz form of the
    symbol λ + f_A >= 0).
  - Its diagonal sums are ½ − k/(2T). Adding (k/(2T))·[[1,1],[1,1]] on {0, k} for each k ∈ A makes them exact, at
    extra trace ΣA/T → 0. So inf DNN cost = M.
  - E110 (index set [0, X]) therefore measures only a minimal-degree edge effect, not cancellation.
  - The genuinely restrictive class is COMPLETELY POSITIVE (CP): 2f_A + C = Σ_j|P_j|², P_j >= 0 coefficientwise.
  - Each supp P_j is a clique of Cay(Z, ±A) (B − B ⊂ ±A ∪ {0}). Hence Σ‖P_j‖₁² = 2n + C <= ω·C, i.e.
    C_CP >= 2n/(ω − 1) with ω the clique number (PROVED).
  - The dual cone is copositive Toeplitz kernels.
  - Z-specific EXTREME-LAG FACT (proved): in any finite B ⊂ Z with elements b_1 < … < b_s, the lag b_s − b_i has
    multiplicity <= i. So no block has flat multiplicity, unlike the subgroup blocks of F_p^r.
    - Corollary (proved): |A ∩ (a* − Δ, a*]| <= C_CP·(|A ∩ [1, Δ]| + 1).
  - OPEN sub-question CP-CHOWLA: C_CP >= c√n for every A? This would make "C* needs phase cancellation" a theorem
    (F12) and cap Bu's square-identity paradigm.
    - Sidon squares give C = √(2n).
    - Interval, Singer⊗interval and AP blocks all fail flatness (convex triangle sums).
  - The text below is kept for the record; read "DNN" there as "CP".
  NEW CLASS (route-checked; not in ROUTES): DNN certificates.
  - Definition. f_A + λ = v*Qv with Q ⪰ 0 AND Q >= 0 entrywise. Equivalently (CP form) 2f_A + C = Σ_j|P_j|² with
    nonnegative-coefficient P_j: 1_A is a nonnegative combination of autocorrelations of nonnegative sequences.
  - Both known C*-type mechanisms are DNN:
    - Sidon squares (Bu's core);
    - F_p^r quadrics (blocks = totally singular subspaces, i.e. subgroups).
  - Q >= 0 forces every diagonal k ∉ A to vanish entrywise. N = D^{−1/2}QD^{−1/2} − I is nonnegative with
    λ_min(N) >= −1, hence weighted-clique structure (cliques of Cay(Z, ±A), cf. JMTZ).
  - Uniform-clique form: C/n = 2/(s − 1), so C <~ √n needs cliques B with B − B ⊂ ±A ∪ {0} and |B| >> √n. Their
    autocorrelations (triangle-like near the band edge) must sum to a FLAT indicator: the taper problem, exactly
    posed, with no rounding noise.
  - AP-block subclass: 1_A = Σ_d Σ_L u_{d,L}(1 − k/(dL))₊·1[d | k]. Every prime element of A needs its own step-p
    block (cost 1 − v_1(p)).
  - E110 (running next) asks whether near-extremal sets need PHASE CANCELLATION (M_DNN/M large) or are DNN-certified
    (ratio ≈ 1).
    - If ≈ 1: a Chowla theorem for DNN-certified sets (clique cover + band edge) is a precise, attackable sub-C*
      target that contains both known mechanisms.
    - If large: C* objects must use complex or signed factors, which is a new forced feature F12.
  - Smoke (2 sets): Sidon differences q = 5: M_DNN/M = 1.024. Interval [1, 30]: 1.000.

- A6 (2026-10-19, cont. 29). SPREAD PRINCIPLE and the clique chain (programme; heuristic links marked).
  Survey of every known R → 0 object (lead; standard finite-geometry facts, not re-verified in detail):
  - F_p^r quadrics (r even, η = +1): union of totally singular subspaces.
  - Semiprimitive uniform cyclotomy C_0 ⊂ F_{p^{2s}} (p ≡ −1 mod e). Ŝ is two-valued, with values
    ((e − 1)√q − 1)/e and (−√q − 1)/e. So |S|/K² ≈ e and R ≈ √(2/e) → 0. C_0 ∪ {0} is a union of F_{p^s}-lines.
  - Latin-square-type partial spreads (m subgroups of order q in a group of order q²): |S|/K² = (q − 1)/m.
  - Unions of coprime-order subgroups in Z_N.
  ALL are unions of additive subgroups (spreads). Every known subgroup-free object (Paley in Z_p, Singer differences,
  Bu) sits at |S|/K² ≈ 2, i.e. R ≈ 1/2. Small Z_p half-sets reach 2.08 (E41, p = 71–89), so the constant 2 is not
  sharp in Z_p. Z has no finite subgroups.
  SPREAD CONJECTURE (heuristic): |S|/K² >> 1 forces S to be close to a union of subgroups.
  - In Z: approximate subgroups only, each paying Gibbs.
  - Its sharp form would give C½.
  Why energy methods cannot see the spread in the C* core (A5(i)): for r >= 6 the subgroup structure sits at the
  random triple level. It IS visible as CLIQUES of Cay(G, S): the totally singular subspaces are cliques of size
  ≈ n/M, which is Delsarte-maximal (ω <= 1 + n/M).
  CLIQUE CHAIN (each link a research problem):
  - (L1) SHARP CLIQUE THEOREM: M <= ε√n ⇒ A's difference structure is covered by cliques of size ~n/M. Current
    status: JMTZ gives d^{1−O(γ)} with unspecified O(·), which is not sharp.
    CORRECTION (cont. 29): L1 is FALSE at ratio |S|/K² ≈ 2. The Paley graph has n/M ≈ √p but clique number O(√p)
    (conjecturally polylog). So L1 can hold only for ratio >= 2 + η, i.e. in the C* regime proper. Bu's cliques
    (≈ 0.55·n/M) are consistent with either reading.
  - (L2) Cliques + exact two-valuedness ⇒ a near-CP block design (the quadric's certificate IS CP).
  - (L3) CP-CHOWLA in Z (P76): extreme-lag multiplicities forbid flat block designs. E111 is testing this
    numerically.
  Equivalently, C* in Z would need a spread whose blocks have flat multiplicities, and Z-blocks never do (P76(c)).
  (L3) is the most concrete link. If E111 supports it, attempt a proof next.
  Numbers: Bu has cliques (Sidon translates) of size k ≈ √n against n/M ≈ 1.8√n.

- A6′ (cont. 29, after E110 + E111). REFORMULATED CHAIN: Chowla ⇐ SCP(T) + CP-CHOWLA(Z).
  **SCP(T) AS STATED IS FALSE FOR EVERY T (orthogonal padding; review cont. 30, lead-verified; see A8). Do not build
  on it. The implication below is valid but its hypothesis fails.**
  - SCP(T), group-agnostic: in any abelian group, a symmetric S with |S| <= |G|/2 and ratio |S|/K² > T has a
    completely positive certificate of cost <= C(T)·K.
  - CP-CHOWLA(Z): C_CP(A) >= c√n (P76). CP½ (c = √2) is conjectured for FLAT CP only. Non-flat CP reaches
    R_CP = 0.655 < 1/√2 at n = 20 (E111), so general CP-Chowla is numerically close to Chowla itself.
  - Proof of the implication: if ratio > T, then K >= C_CP/C(T) >= c√n/C(T). So ratio <= max(T, 2C(T)²/c²), which
    is bounded, i.e. Chowla.
  - Status:
    - SCP(2) is FALSE. Paley has ratio ≈ 2, cliques O(√p) (conjecturally polylog), so CP cost >~ p/log p against
      K ≈ √p.
    - SCP(T) for large T is consistent with every known object: all ratio → ∞ objects are spreads and CP (quadrics,
      semiprimitive cyclotomy, Latin-square partial spreads, subgroup unions).
    - E112a: E41's Z_p half-sets (ratio 2.05–2.17, no subgroups) have C_CP/K ≈ 2.6–5.5 (upper bounds). So SCP
      needs T > ~2.2. E41 SA data suggest the Z_p ratio peaks near 2.15. No refutation for fixed T.
  - Meaning for C* (CORRECTED after E111 two-level): near-extremal Z sets ARE nearly CP-certifiable with non-flat
    weights, so SCP is not obviously violated in Z and CP-Chowla(Z) is not much easier than Chowla. The spread
    observation stands (every ratio → ∞ object is a spread). The original reading follows, kept for the record:
    a Z counterexample needs a CANCELLATION object (non-CP, F12) with ratio → ∞. No such object is
    known in ANY abelian group: all known cancellation objects (Paley, Gauss periods) sit at ratio <= ~2. So the
    constructive search should target "high-ratio non-spread objects in finite groups" first. Finding one would
    break SCP; finding none supports Chowla.
  - Caveat: inside Z, SCP(T) is essentially Chowla-strength (vacuous if Chowla holds with ratio <= T). Its value is
    as a GROUP-AGNOSTIC statement, which could be attacked in F_p^r / Z_N where the spreads live.
  - Next discriminating experiment (E112): optimize the ratio in moderate finite groups (F_p², Z_{p²}², Z_N
    composite, Z_p) for sets FAR from unions of subgroups, and measure their CP-efficiency. Also test the E41 Z_p
    half-sets.

- A7 (cont. 29). WHY RATIO 2: the FLAT-SPECTRUM BARRIER (elementary, proved).
  - If |Ŝ(ξ)| ≡ λ for all ξ ≠ 0 (Paley, bent/Menon difference sets, Singer-type sets), Parseval gives
    λ² = σ(1 − d) with d = σ/|G|. So the ratio σ/K² = 1/(1 − d) <= 2 at density d <= ½.
  - Every symmetric-spectrum cancellation object is capped at ratio 2.
  - Beating 2 needs an ASYMMETRIC spectrum: positive spikes of height μK with μ >> 1 over shallow negatives. This
    is the C* anatomy.
  - The only known exactly two-valued asymmetric objects are Latin-square-type PDS (eigenvalues n − r and −r with
    r << n) from partial spreads / partial congruence partitions (PCPs).
  - (A8: SCP(T) is false by padding; the question below is now a structural side question, not a chain link.)
    So the EXACT form of SCP is the classification question: are Latin-square-type PDS with small r always PCPs
    (unions of subgroups)? This needs a literature check (queued; one agent at a time). If true, SCP is its robust
    (approximately two-valued) version, which is the "robust Ma" gap of A4 in a sharper form.

- A8 (cont. 30, external review, lead-verified). SCP(T) REFUTED; CP-CHOWLA(Z) is the surviving chain link.
  - Counterexample (orthogonal padding). B ⊂ H = F_2^r random of density ½: K(B) = O(√(N log N)) and clique number
    polylog N, so C_CP(B) >= 2|B|/(ω − 1) >> N/polylog N (P76(b)). U = s lines of F_q² minus 0: |U| = s(q − 1),
    Û ∈ {q − s, −s}, K(U) = s. S = (U × 0) ∪ (0 × B) in F_q² ⊕ H. Then Ŝ(ξ, η) = Û(ξ) + B̂(η), so K(S) <= K(U) + K(B)
    <= 2s for s ≍ √(N log N), and ratio >= (q − 1)/(4s) → ∞ for q >> s. A clique of Cay(G, S) has all its
    differences of one type (a mixed pair (u, 0), (0, b) gives a difference (u, −b) ∉ S), so it lies in a coset of one
    factor, and the B-type blocks form a CP certificate for B. Hence C_CP(S) >= C_CP(B) and C_CP(S)/K(S) → ∞.
    Lead check: all steps elementary and correct.
  - What survives padding: SCP′(T), "ratio > T ⇒ some S₁ ⊂ S with |S₁| >= c(T)|S| and C_CP(S₁) <= C(T)·K(S)". It
    still implies Chowla with CP-Chowla(Z), and in orthogonal sums the low-ratio part carries <= (2.2/T)|S|. But in Z it
    is Chowla-strength, and NOTEBOOK cont. 29.12 (hidden pieces) is its first obstacle. NOT pursued.
  - Decision: CP-CHOWLA(Z), C_CP(A) >= c√|A|, is the concrete target. Its proof must sum the extreme-lag
    (endpoint) multiplicity losses of P76(c) over all blocks. It is a rigorous obstruction for the whole class of
    nonnegative-coefficient square certificates, which by E111 is within 1–8% of M on near-optimal sets. Fourier
    plus clique size alone caps at max(2n/(ω − 1), 2M) (NOTEBOOK cont. 29.11), so the dual must see positions inside
    cliques.
  - Also corrected: A2's Riesz-product line (real-frequency profile condition) and A5(i)'s reading (heuristic only).
  - The review read the pre-retraction F12 ("flat CP 0.857 ⇒ phase cancellation"); that reading is superseded by E111
    two-level (within 1–8%).

- A9 (cont. 30, literature agent + exact checks). SPREAD PRINCIPLE REFUTED AS STATED. Jedwab–Li LS_{p^{a−1}}(p^a) PDS
  in Z_{p^a}² (a >= 3) are exact two-valued, ratio (n − 1)/r ≈ p, and NOT unions of subgroups (for j ≠ 0 they contain no
  nontrivial subgroup). They are disjoint unions of index-p subgroup SHELLS H \ K, one per p-adic level of y. Each
  shell's transform |H|1_{H⊥} − |K|1_{K⊥} has a negative part; for a character at level h, the shells at every level
  k < h cancel exactly (the K⊥-solutions are p times the H⊥-solutions), level h gives n − r or −r, and levels > h
  vanish. So this is CROSS-LEVEL CANCELLATION: a finite-group taper tree that closes exactly. Revised principle: all
  known ratio → ∞ objects are built from subgroups (unions of subgroups OR of subgroup shells). The Z obstruction is
  unchanged in kind (Z has no subgroups, so no shells: an AP minus a sub-AP pays Gibbs), but the class "cancellation
  objects with ratio → ∞" is NOT empty, contrary to A6′. The ratio is ≈ p for every a (no gain from depth); depth
  buys non-subgroup structure, not ratio. Next: E114 measures the CP cost of D_{3,j} ⊂ Z_27² (is it CP-efficient
  with non-subgroup cliques, or a genuine cancellation object?).
  - Certificate reading (lead): 1_D = Σ_shells (1_H − 1_K), so D̂ = Σ (|F_H|²/|H| − |F_K|²/|K|) is a SIGNED sum of
    subgroup squares whose positivity holds level by level. This is the finite-group analog of Bu's paradigm
    (2f + k = 2ρ² − g: a square minus a correction), and it reaches ratio → ∞.
  - Why Z cannot copy it (lead): the selection freedom (one lift per slope class) needs the projective line over
    Z_{p^a}, i.e. rank 2 over ONE prime. Z's p-adic completion Z_p has rank 1 and every finite quotient of Z is cyclic
    (Ma: only trivial PDS and Paley). The 1-D valuation shells {v_p = k} just tile an interval. So Z's only exact
    algebraic structure is cyclic, and its continuous part (T connected) forces Gibbs. These are the two Z-features any
    proof must use.

## 6. Side results (recorded; NOT the prize)
P71.2 (kernel), P72 (a–c proved; d, e gaps), P73 (kernel, Z), P74, E103–E105, Ruzsa-question status. See PROOFS.
P76 (DNN = PSD on unbounded index; CP certificates: C >= 2n/(ω−1), extreme-lag multiplicities; CP-Chowla open, E111).
P75 (automatic sets: domination-or-twin ⇒ Re μ̂ < 0 ⇒ linear M; 28.5% coverage) + E108 (FPC: all 71,840 small automata certified dead). T-A2 open.
