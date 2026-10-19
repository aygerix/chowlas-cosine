# ROUTES — ledger of proof routes and what each reduces to (created 2026-10-19 after the user caught the circling)

RULE: before ANY new route gets work (lead or agent), add a row. The row must say which existing entry the route
reduces to, or give a concrete reason it does not. A new statement that is "new wording" of a row below is NOT a new
route. Grep PROOFS/NOTEBOOK for the MECHANISM, not just the statement.

## The core obstruction C* (first recorded 2026-10-18: NOTEBOOK "localization" note ~l.700, P24/P25, P28's open step; restated P53, day 2)
- Sign-preserving operations on f_A + M >= 0 localize only at the FRONT. PD multipliers satisfy |ψ(m)| <= ψ(0); the
  available family is front windows, dilation-restrictions, products of these, and test measures (P29(b) = M, P70.6).
- Interior (mesoscopic) information is reachable only through the MODULUS (P24/P25/P28), which loses the sign.
- Chowla needs: a set that is locally deterministic / spiky at mesoscopic heights √n << h << n (forced by P28, P40)
  ⇒ a sign (Gibbs) contradiction, quantitatively, with no accumulating loss across scales.
- Every row marked "= C*" below is this statement in different language. Do not re-derive it.

## Ledger
| Route | Where | Reduces to | Status |
|---|---|---|---|
| "deterministic ⇒ Gibbs" quantitative | P28 open step, day 1 | = C* | open |
| Localization + 2-run structure (OR(2)-weak) | NOTEBOOK day 1, P27 | partial C* (bounded unions of dilates done, P27) | open in general |
| Self-reducibility SR | NOTEBOOK cont. (2026-10-19) §3 | = C*: open ingredient is the irrational (Bohr) spike case, plus per-step losses | audited 2026-10-19 (cont. 22) |
| Spike truncation / bulk fraction (SB) | P40, E67/E68 | = C* (spike-dominated ⇔ band-limited, P40(c)) | open |
| Macro twisted profiles | P48, P53 | C* at MACROSCOPIC scale: PROVED (qualitative, any rank) | done; mesoscopic = C* |
| Dense second/third order | P59–P66 | sub-problem; proven barrier: second-order reach 1/D (P61), bounded-M sharpness | T-dense C < 7.72 (½), 13.7 (1/3) |
| Scalar moments | R12-S | capped at 1/3 (proved) | dead |
| Group-agnostic (finite groups) | JMTZ, F_p⁴ quadric | capped at ¼ (proved) | dead |
| Cyclic CSFG / PK | round 12, P64 | C* in cyclic costume (Z_q has no front) | paused |
| Cyclic WRS(η) | rounds 15–16, P68–P69 | C* in cyclic costume; heavy-core fake (P69) | paused |
| Self-difference graph dichotomy | cont. 19.7–9 | P40 (graph form) + P9 | corrected (cont. 19.10–11) |
| Four-way cover | round 17, P70 | = C* | open |
| TAPER (correlated roundings) | round 18 brief | = C* | stopped 2026-10-19 |
| Positivity–resolution PR | cont. 20 | = P53 step 5, quantitative | dropped |
| Szegő / OPUC (Verblunsky energy <= log K) | cont. 21.1(c) | P40(c) band-limitation, plus a log loss | dropped |
| Window-variance bound VB | cont. 21.1(d), E101 | weak L² form of P28 | dropped |
| Hardy/Fejér–Riesz factor WINDOWING | cont. 21.3, 22.1 | = C*: factor Gram = exact SDP primal (dual = test measures, P29(b)); one window sees only |m| < L; interior lags come only from cross-blocks, bounded by Cauchy–Schwarz moduli | killed on paper 2026-10-19; E102 cancelled |
| F_p^r quadric lift with layered taper | cont. 19.6 proposal, cont. 22.2 | = TAPER (construction form): every character's envelope E_c(x) = F_{λ(x)}(c) must be smooth AND >= −κ with κ << (p/m)^{r/2}; layer switches are sharp level sets (Gibbs, R >~ 0.1 m^{r/2}), random increments give κ ~ p^{r/2} | not run; reduced on paper |
| Multi-window Kronecker phase freedom | cont. 22.3 | = P28 coarse sum: windows at AP positions lock phases (rank 1); free (independent) positions are lacunary (M ~ n); the coarse sequence is again a counterexample (self-similar) | dropped |
| Anticoncentration of f(x), x uniform | cont. 22.3 | = P28 spread/spike dichotomy: f >= −M forces P(f ∈ [−M, CM]) >= 1 − 1/C; APs are concentrated yet satisfy Chowla | dropped |
| Low-degree SOS in the indicators x_a | E96 | dead: two-point pseudo-marginals fool level 1.5; growth needs the PEAK (non-symmetric) step | dead (E96) |
| Product / tensor renormalization | day 1, cont. 22.3 | no gain: two-valuedness not preserved (marginal coefficients 1/K, 1/K', 1/(KK')); splitting multiplicities is the rounding problem | dead |
| Iterated spike sub-multiplicativity | cont. 19.5(a), cont. 22.4 | new small PROVED lemma (arc-mass bound); vacuous at the origin | fact, not a route |
| Integrality / Mahler / Galois norms | cont. 19.5(b), cont. 22.3 | gives only AM–GM over conjugates (the test-point average) | fact, not a route |
| High-rank ball / threshold model sets | E73, cont. 22.5 | dead: the main Bragg peaks of a d-ball window have Gibbs ~(2/e)^{d/2}, but high rank turns the window boundary into Bernoulli-type √n noise (E73: approaches the Bernoulli baseline from above, never beats it) | dead (E73) |
| Taper tree / graphon trichotomy (random selection → semicircle √; deterministic Boolean window → Sanders rigidity → Gibbs; structured selection → next level) | cont. 22.6 | = C* (open case: unbounded depth/rank with structured selections) = HBCG/BBG | open; no new tool yet |
| Bourgain–Ruzsa Hilbert-cube iteration (+ Lemma 3.1 boundary pair) | LITERATURE (Ruzsa 2004), cont. 23.1 | structure step group-agnostic, loss 4K² per level by design (energy >= m³/K²); certificate = P9/run-top. Usable only for K <= exp(√log n) | not a C* tool |
| Hierarchical Bohr towers with linear tapers | round-18 recommendation, cont. 23.3 | window = averaged cross-polytope with FLAT facets; flat facets have sinc-product Gibbs that does not decay with rank (packets along facet normals, P71.2 mechanism) ⇒ linear M. Curved windows = E73 (noise) | predicted dead on paper; not run |
| Model-set (cut-and-project) class, any rank | cont. 23.2 | HEURISTIC self-duality: M(A) ≈ n·max_k(−1̂_E(k))/μ + realization noise; the first term is "dual Chowla" for a band-limited Boolean window on T^r with N ~ n/μ frequencies, the same √ scaling. Same problem in dual form | = C* (dual costume) |
| Near-Boolean weights / robust certificates (Ruzsa's [0.99, 1.01] question) | E103, P72 | robust duality = P29(b) test measures plus an ℓ¹ penalty τΣ|c_a(μ)|. Flat sets lose only a constant factor (Singer R_{0.3}/R_0 plateaus at 0.70). The spiky (C*) regime cannot be probed: no spiky sets exist to test | fact; not a C* tool |
