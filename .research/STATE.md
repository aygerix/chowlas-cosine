# STATE — current targets and honest status (updated 2026-10-18 late night)

## Targets
- (C) Epoch: algorithm solution(c,n) for all c>0 — requires R(A_k) -> 0. NOT ACHIEVED. No solution.py exists.
- (L) Chowla: M(A) >= c0 sqrt|A|. NOT ACHIEVED. Best known: >> n^{1/5} (Shankar 2609.05338, cited, checked).
- Working hypothesis **C½**: M(A) >= sqrt|A|/2 for ALL finite A (sharp by Bu et al.). CONJECTURED. If true, Epoch's
  algorithm cannot exist. Not assumed: both tracks stay open.

## Best certified constructions (ball-arithmetic certificates, E2; Sturm brackets for N <= 40)
- Small-N exhaustive box optima (agent, E14): **N=36, max 50, R <= 0.56481** (best finite R known to us; lead re-certified),
  N=35 0.5677, N=34 0.5741, N=24 0.5769 (= exact [1,40] optimum by MILP, E13), N=27 1/√3 (M = 3 at x = π).
- Structured MILP (E27, C-N45): N=45 R <= 0.571844 (two certificates). LNS-MILP (E18): N=45 0.5948, N=50 0.6036, N=60 0.6243, N=80 0.6630 (uncertified objective; certify before quoting).
- Bu et al. reproduction (E4): N=6320 R <= 0.6573. Bu's identity on FULL Singer sets with best shift (E25, C-SB):
  N=63252 R <= 0.56272; N=94556 R <= 0.556699; **N=161202 R <= 0.553656** (q = 401, oversample-32 certificate; best certified finite R known to us).
  Fit R − 1/2 ≈ 0.42–0.45·√(log k / k) (k = 62..402). Nothing below 1/2 anywhere.

## Proved here
Paper: P1 Fejér–Riesz; P2 probabilistic; P3 projection; P4 no exact t>=2 uniform difference sets; P5 intersection;
P6 energy bounds; P7 cube framework; P8 multiplicity bound (R < 1/2 needs coherent multiplicity > 2); P9 star lemma;
gain identity; P10 B_3 differences R >= 0.293; P11 B_h differences -> 1/√2; P12 dissociated Bu class; P13 even part.
NEW 2026-10-18: P14 (averaged boundary bound: precise obstruction L(A); finite-model counterexample to "no middle
layer"); P15 (Bu = P^2 − k/2 − C/2, P(x) = C(x/2)); **P16/P16′: R(A(S)) >= 1/2 − O((L/k^3)^{1/5}) for every Sidon S ⊂ [−L,L]**
— C½ for Bu's construction, unconditional. PROVED on paper and INDEPENDENTLY REVIEWED (agent: CORRECT; P16′ large-sieve
form re-derived by lead). Explicit: R >= 0.302 at k = 1e6 and 0.423 at k = 1e8 for Bu's range L ≈ 12.5k^2. Lean: P16 is
KERNEL-CHECKED in unconditional explicit form (HalfSquareExplicit.lean: R(A(S)) > 1/2 − η whenever η^6k^3 >= 7000L;
re-verified by lead, 85 axiom lines standard); P16′ (exponent 1/5) is KERNEL-CHECKED too (HalfSquareSieve.lean:
R(A(S)) > 1/2 − η whenever η^5k^3 >= 4200L, Gallagher sieve; lead re-elaborated, 103 axiom lines standard).
KERNEL-CHECKED (Lean 4, axioms propext/choice/Quot.sound only, no sorry; re-verified by lead, 37 axiom lines):
difference-set identity; Sidon consequence; mean zero/Parseval; P5; P7 cube identity + vertex min; P9 star lemma and
star bound; P8 multiplicity bound; P13(a) averaging identity, restriction to multiples, (q−1)M >= |A| − q|A∩qZ|.

NEW (session 2): P17 rigorous bounds on the doubly-positive profile constant: ρ* <= 0.9057 (all profiles), <= 0.7698 for
w = h⋆h̃ with h >= 0 (Beckner + Hölder); numerical sup 0.7239.

## Heuristic / numerical
H1 Wick model. Dense-profile identity R = c_E sqrt((1−ρ)/2) (σ_E^2 = (1−ρ)N/2), ρ <= ρ* ≈ 0.7239 (numerical sup over
doubly-positive profiles; autocorrelation analogue of the Matolcsi–Vinuesa constant). Symmetric rounding (c_E >= √2)
⇒ dense limit >~ 0.5255. Exhaustive optima DO use positive skew (E21: +1.18 at N=29) but the skew fades (+0.19 at N=40)
and c_E rises (1.43 → 1.79); anatomy extrapolation from N=36 gives R_∞ ≈ 0.50–0.51 — the dense regime is the one live
candidate against C½ (needs c_E < 1.35 with a p.d. profile). LNS/SA at N >= 45 are search-limited (calibration: random
starts reach only 0.60 at N=36), so "R rises past N=36" is NOT established.

Quadratic ("square-identity") class (NOTEBOOK 2026-10-18 late): in the Gaussian model R >~ 1/2 with equality only for one
positive eigenvalue (= complete multipartite by Smith's theorem) with small parts, i.e. Bu. E22: complete-multipartite
Bu sums with blocks of size >= 2 are much worse (M/k ≈ 1.0 at b = 2 vs 0.65 for Bu). Killed as a construction route.
Literature check: Erdélyi 2607.21877v1's n^{1/3} proof for Littlewood cosine polynomials has a gap (LITERATURE.md;
Fejér-kernel counterexample to the displayed chain); not used here.

## Session-2 late additions (2026-10-18)
- P16′ KERNEL-CHECKED (HalfSquareSieve.lean, η^5k^3 >= 4200L). Formalization corrected the window-folding step of the
  lead's Gallagher sketch (windows inside one period window); conclusion unaffected.
- P18 (dense min–max Bernstein lemma) PROVED but numerically empty on records (E28): qualitative only.
- E29: Erdős–Turán quadratic Sidon sets have min|F_B|^2/k -> 0 (killed). Profile analysis: Sidon forces the profile
  autocorrelation <= λ, so the spike carries <= ρ* of E|F|^4 — the doubly-positive constant ρ* ≈ 0.724 is a COMMON
  obstruction to dense sets and Sidon-difference sets (NOTEBOOK).
- Bedert framework barrier (NOTEBOOK): the K^4 in Prop 7.3 = O(K^2) (degree-2 gap inequality) × ||H||_1^2; PROVED that no
  degree-1 (single nonnegative multiplier) inequality has a coefficient gap (|c_1| <= c_0). Exponent 1/4 would need a
  run-top test function with L^1 <~ K^{1/2}.

- P19 (agent, proof read by lead): Bedert's |B_t| << K^4 is sharp for all degree-2 gap-inequality methods (random
  relaxed sets); the universal exponent 1/4 needs Target Lemma S (degree-1 input).
- P20 (agent conjG; Theorem 1 lead-verified E31): Conjecture G FALSE in groups, |B_t| = K²(K−1); ord t = 3 without
  singleton cosets gives |B_t| <= K³ (sharp). Group-agnostic run-top bounds cannot beat K³.
- P21 (lead, elementary): K³ without full/singleton cosets (F_p^4, K = 3p, |B_t| = p³); G_noFull refuted; diagnosis:
  negative-definite fibres need runs > ord(t)/2 (absent in Z).
- P22 (agent g3 Theorem O4; proof re-derived by lead; lead-independent E36 for a = 3, 5, 7): G3 FALSE. In Z_4 × GR(4,a),
  K = 2^{(a+1)/2}, |B_t| = K⁴/4 − K²/2; A-averaged run-tops K⁴/8 (E36b). With Bedert's group-valid K⁴: the group
  exponent of run-tops is EXACTLY 4, per t and on average. Every group-agnostic run-top argument stops at Chowla exponent
  1/5; beyond needs a Z-specific run-top bound (a weakening of Chowla itself). Barrier note §3b.

## Refuted / killed routes (keep)
Cube vertex framework; A_{k-1} root squares; quarter-integer trick; fractional decomposition; dithered Fejér/Beatty;
error diffusion; separated-block unions; local SA from Bu seeds; Sidon lower-flat polynomials (E8/E12/E15: c -> 0);
cyclotomic Z-lifts and model sets (E11); Erdős–Turán quadratic Sidon flatness (E29); P18 as a finite probe (E28); averaged Bedert (P14: (a) is t-independent); sums of several squares
Σ P_j^2 (P15 remark: pseudo-random squares give R ~ √log X).

## Plan in priority order (updated 2026-10-18 late night, after E40/E41 and the branch-2 review)
1. **Line D: the dense regime, the common crux of both tracks** (NOTEBOOK "Branch 2 reassessed").
   - Lower bound: Chowla for dense sets is open even in Z_p (half-sets: Sanders p^{1/3} vs Spencer/Paley p^{1/2}).
   - Proved here: the elementary p^{1/4}; the exact identities h*h = const and h^{*3} = p²h + p²λ(λ−1)(λ−2) for
     h = ĝ + λ (g = 2·1_A − 1); the spectral gap ĝ(γ) <= λ³/2 (γ ≠ 0).
   - Target: exponent > 1/3 in Z_p (difference-set rigidity / global large-spectrum structure), then dense A ⊂ [1, X].
   - E41 (exact half-set optima) running: does min M_p/√p level off near 1/2 or keep falling?
2. Construction agent (native, started before the codex rule): dense regime at N ≈ 50–300 plus >= 2 new mechanisms.
   Verify and record its report when it lands.
3. OR(2) demoted to a test case:
   - its energy half is the standard energy bound;
   - its structured half contains the dense problem;
   - C½ holds in its dilated sub-family (rotation sweep, PROVED).
4. Lean (next subagent, via codex): O4⁺, P20 Theorem 2, the Z → Z_N transfer lemma; then the line-D identities.
5. Low priority:
   - exhaustive N = 43 in [1,60] (src/exh2.c);
   - λ-ruler obstruction proofs (C-W, W' >= ck^{1+δ}).
Compute (user rule 2026-10-18): ALL calculations, lead and agents, on the GCP VM dirichlet via src/dirun.sh
(8 vCPU = 4 physical cores, 32 GB; default -c 4 so lead + one agent share it; -c 8 for exclusive jobs). Not the laptop
(shared with other projects), never the VM fejer. F4 (src/f4run.sh) only as fallback.
Subagents (user rule 2026-10-18): no native Opus subagents. Launch via the codex CLI, Sol 6.1 at xhigh reasoning
(`codex exec -m gpt-6.1-sol -c model_reasoning_effort="xhigh" ...`), still at most one at a time.

## Running now (2026-10-18 late night)
- Construction agent a6d21d62b5c3e53ad (native; brief .research/agents/construct_brief.md).
- E41 (dirichlet, src/e41_batch.sh): exact half-set optima for p = 59..89 → examples/zp_half/e41_mid.txt.
- E37 main batch (Z_105, Z_256, Z_4^4) still running. E37b done: primal values only, they track the 3-rank.

## Active lines (>= 3) (updated 2026-10-18 late night)
1. [lower bound, dense] Line D (above). The finite model Z_p has no subgroups. E10 shows that in the sparse regime
   Z_p still allows grid-R ≈ 0.31, so any Z proof needs continuity. Only the dense regime might be provable in Z_p.
2. [lower bound, universal] Run-top route mapped:
   - group exponent exactly 4 (P22);
   - the two-step scheme is capped at 1/3 in Z;
   - JMTZ capped at 1/6 with an optimal clique theorem.
   No Z-specific run-top mechanism yet; OR(2) gave only the rotation sweep.
3. [C½ for construction classes] P16/P16′ (Bu class, kernel-checked); λ-rulers killed (P23). Line D's half-set data
   doubles as dense-regime evidence.
4. [construction] Dense FR supports: the agent's report is the next input. Every other known mechanism is pinned at
   >= 1/2.
5. [verification] Lean: P21 and the negative-definite fibre lemma done; next O4⁺ via codex.

## Compute policy
All calculations on GCP VM dirichlet via src/dirun.sh (user rule 2026-10-18); F4 fallback; never the laptop or fejer.

## First concrete next step (updated 2026-10-18 late night)
(1) Read E41 for p = 59..89. If min M_p/√p keeps falling below 0.5, find the structure of the optima (dilated
near-interval + tail): fit the profile and the tail, and test a parametric family for large p. That would be a
dense-regime construction in Z_p and the first sub-Paley dense family. If it levels off, attack exponent > 1/3:
  - a symmetric near-planar large spectrum is what the identities allow at λ ~ p^{1/4};
  - rule it out by difference-set rigidity (Johnsen: −1 is never a multiplier of a nontrivial abelian difference set)
    in a quantitative form.
(2) When the construction agent reports: re-certify its records, record them, commit.
(3) Lean via codex (one subagent at a time).
