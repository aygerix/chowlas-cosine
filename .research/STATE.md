# STATE — current targets and honest status (updated 2026-10-18 late night)

## Targets
- (C) Epoch: algorithm solution(c,n) for all c>0 — requires R(A_k) -> 0. NOT ACHIEVED. No solution.py exists.
- (L) Chowla: M(A) >= c0 sqrt|A|. NOT ACHIEVED. Best known: >> n^{1/5} (Shankar 2609.05338, cited, checked).
- Working hypothesis **C½**: M(A) >= sqrt|A|/2 for ALL finite A (sharp by Bu et al.). CONJECTURED. If true, Epoch's
  algorithm cannot exist. Not assumed: both tracks stay open.

## Best certified constructions (ball-arithmetic certificates, E2; Sturm brackets for N <= 40)
- Small-N exhaustive box optima (agent, E14): **N=36, max 50, R <= 0.56481** (best finite R known to us; lead re-certified),
  N=35 0.5677, N=34 0.5741, N=24 0.5769 (= exact [1,40] optimum by MILP, E13), N=27 1/√3 (M = 3 at x = π).
- Structured MILP (E27, C-N45): N=45 R <= 0.571844 (two certificates). Structured-class B&B (E42, C-N50): **N=50 R <= 0.5700604** (max 72, two certificates; exact optimum of the class C(72,50,38,2)), N=50 0.5725176 (class optimum for X=71,Y=40,h=3). LNS-MILP (E18): N=45 0.5948, N=50 0.6036, N=60 0.6243, N=80 0.6630 (uncertified objective; certify before quoting).
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

NEW 2026-10-18 late night: P27 (codex agent, lead-checked) OR(2)-weak for residue-strip 2-run sets:
M(S∪(S+t)) >= √(n/k)/80 when S lies in k residues mod q within an arc [0,t/2], q >= 32t√k (exponent 3/8 for k <= n^{1/4}).
P27 Theorem C (codex agent, lead re-checked every step): residues in [0, Lt] (k classes), q >= 16BJtk, B = L²+(L+1)²,
J = 2L+3 ⇒ M(S∪(S+t)) >= √n/(32BJ²k^{3/2}): SQUARE-ROOT for bounded unions of translated dilates; cancellation
family qY ∪ (qY+3t) has M >= |S|/16. Mechanism: the real coset grid (θ+2πZ)/q splits micro phase from macro profile
(Z-specific). Unrestricted OR(2)-weak OPEN.
P25 sharpened localization; P26 half-set ⟺ symmetric weighted near-planar sets.
P28 averaged local-maximal bound (proved) + E45: recovers ~0.21√n on all non-deterministic sets; turning it into a
theorem needs "locally deterministic ⇒ Gibbs". E46: ball-shaped Bohr sets killed.
KERNEL-CHECKED 2026-10-18 night (codex agent, lead re-verified: rebuild + 33 standard-axiom declarations): T0 Schur
products; P20 Thm 2 (order 3) and its run-top corollary |B_t| <= |E| + (K+u₀)³ + 1; O4⁺ (order 4); line-D half-set
identities T3(a)–(e) incl. the spectral gap (PROOFS 'Lean status update').

NEW (session 2): P17 rigorous bounds on the doubly-positive profile constant: ρ* <= 0.9057 (all profiles), <= 0.7698 for
w = h⋆h̃ with h >= 0 (Beckner + Hölder); numerical sup 0.7239.

NEW 2026-10-19 (lead):
- P29 (PROVED; CLASSICAL, cf. Kolountzakis 1996 Thm 2): density > 1/2 forces linear M, and near-extremal sets
  taper to density 1/2. P29(b) is the twisted form.
- **P31** (PROVED modulo Lemma P31-N, whose proof is sketched): window–Nikolskii inequality
  W(n/2 + M²) <= ρ_L(L + 1)(M² + S_A/2). Consequences:
  - M >> √n for every A that is not front-loaded (front density below 2δ/ρ);
  - dense Chowla in Z: |A| >= 0.39·max A ⇒ M >> √n;
  - any counterexample must be front-loaded beyond 2.9δ at every scale.
  Numerical ρ_∞ ≈ 0.687 (E48); rigorous ρ_∞ <= 0.7698 via Beckner. Elementary constant ρ_L <= 0.811 + 0.237/(L + 1) (Lemma P31-E), so it is unconditional on paper. Not kernel-checked. Novelty unchecked
  beyond one search.
- P30 (CONJECTURED reformulation): uniform cap on the share of ‖f‖₂² above K·M implies Chowla. E47 measures it.

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

## Running now (2026-10-18, VM restarted on c2d-standard-8)
- E44 (src/e44_grb_dense.sh): Gurobi lazy-cut box MILP, warm-started, N=45 X=64 → N=50 X=72 → N=55 X=79;
  progress in examples/gurobi/e44.jsonl (N=45 bound 3.23 vs incumbent 3.836 at 1500 s).
- E37g (src/e37g_batch.sh): Gurobi group run-top ILP, 18 instances → examples/cyclic_ilp/e37g.jsonl.
- Codex agent queue (one at a time):
  1. DONE: P31 adversarial check (report verified by lead). Main inequality survives, with 4 corrections.
     P31-N is proved (ρ_L <= β(1 + 2/√(L+1))³). Kolountzakis 1996 is prior art for P29.
  2. RUNNING (started 2026-10-19): ONE combined Lean project, .research/agents/lean_p31_brief.md.
     - T1–T4: Fejér–Riesz, Lemma P31-E, main inequality, dense corollary with the elementary constant.
     - T5: Beckner sharp Young (lean_beckner_brief.md M1–M5) + P31-N, for the sharp threshold 2/(3√3).
     - User request: Beckner formalized. The local mathlib has neither Young convolution nor Fejér–Riesz.
- E49 (src/e49_batch.sh, 6 cores): profile-constrained SA, triangle vs (1−t)^2, (1−t)^3 vs free, n = 150/300
  -> examples/profile_sa/e49.jsonl.

## Active lines (>= 3) (updated 2026-10-19)
1. [lower bound, dense/profile] NEW lead line. P29 (Turán), then P31 (window–Nikolskii): Chowla for non-front-loaded
   and dense (>= 0.39) sets. Next:
   - finish Lemma P31-N;
   - attack the front-loaded escape class (multi-scale/effective-degree P31);
   - P30/E47 spike-share as the diagnostic.
2. [lower bound, Z-specific run-top] OR(2)-weak. P27 Theorems A/B/C (bounded unions of translated dilates). The codex
   agent OR3 is on spread residues, the k^{3/2} loss and structure vs randomness.
3. [C½ for construction classes] P16/P16′ (Bu class, kernel-checked). Line D Z_p half-set data.
4. [construction] Every known mechanism is pinned at >= 1/2. E47 quantifies the target: >= 28% of ‖f‖₂² must sit in
   secondary spikes far above M; no known family does this. P31(iii): a counterexample must be front-loaded beyond
   2.9δ. That is where to search (core + sparse-tail designs).
5. [verification] Lean T0–T3 done. Next: P27 Theorem C, P31 after review.

## Compute policy
Gurobi 13.0.3 full distribution at /opt/gurobi1303/linux64 on dirichlet with the user's licence
(/opt/gurobi1303/gurobi.lic; env set in src/dirun.sh). User rule: Gurobi is the solver for every MILP/LP.
All calculations on GCP VM dirichlet via src/dirun.sh; never the laptop or fejer. Global quota CPUS_ALL_REGIONS = 16.
Process rule (user, 2026-10-18): computations are fire-and-forget; foreground time goes to mathematics, one codex agent
in parallel.

## First concrete next step (updated 2026-10-19)
(1) P31 is now unconditional on paper via the ELEMENTARY Lemma P31-E: ρ_L <= 0.8110 + 0.2367/(L + 1) (Cauchy–Schwarz,
    Abel summation, one explicit integral). The codex agent P31 is running an adversarial check. Next agent: Lean
    formalization of P31 + P31-E (plan L1–L4 in PROOFS). The verification route is the kernel check, never an
    outside review.
(2) Attack the escape class of P31, front-loaded sets: steep profiles (1 − t)^p with p >= 1.91, and core + sparse tail.
    Candidate: a multi-scale P31, with the window degree replaced by an effective degree. A sparse tail inflates
    L + 1 without carrying mass.
(3) Verify the OR3 agent report when it lands. Then Lean for P27 Theorem C / P31.

