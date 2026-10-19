# STATE — current targets and honest status (updated 2026-10-19 night; newest block: "Session 3, round 8: T-dense(6.156), explicit c(3)")

## Targets
- (C) Epoch: algorithm solution(c,n) for all c>0 — requires R(A_k) -> 0. NOT ACHIEVED. No solution.py exists.
- (L) Chowla: M(A) >= c0 sqrt|A|. NOT ACHIEVED. Best known: >> n^{1/5} (Shankar 2609.05338, cited, checked).
- (L-dense) T-dense(C) := M >= c(C)√n for all A with max A <= C|A|.
  - PROVED on paper for every C < 6.156, ineffective c(C) (P58 + P59; lead-verified). With only the elementary P31-E
    constant: C < 5.843.
  - EXPLICIT c(3) = 10^{−6000005} (P59.6, compactness-free).
  - Kernel-checked effective: C <= 2.44 (P31).
  - Macroscopic class {p PD, p(1 − p) PD, windows}: reach above 6.63 (E79/E80). Beyond that, the mesoscopic problem.
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

NEW (session 2): P17 rigorous bounds on the doubly-positive profile constant: ρ* <= 0.9057 (all profiles), <= 4/(3√3)≈0.76980 for
w = h⋆h̃ with h >= 0 (Beckner + Hölder); numerical sup 0.7239.

NEW 2026-10-19 (lead):
- P29 (PROVED; CLASSICAL, cf. Kolountzakis 1996 Thm 2): density > 1/2 forces linear M, and near-extremal sets
  taper to density 1/2. P29(b) is the twisted form.
- **P31** (PROVED modulo Lemma P31-N, whose proof is sketched): window–Nikolskii inequality
  W(n/2 + M²) <= ρ_L(L + 1)(M² + S_A/2). Consequences:
  - M >> √n for every A that is not front-loaded (front density below 2δ/ρ);
  - dense Chowla in Z: |A| >= 0.39·max A ⇒ M >> √n;
  - any counterexample must be front-loaded beyond 2.9δ at every scale.
  Numerical ρ_∞ ≈ 0.687 (E48); rigorous ρ_∞ <= 4/(3√3)≈0.76980 via Beckner. Elementary constant ρ_L <= 0.811 + 0.237/(L + 1) (Lemma P31-E), so it is unconditional on paper. Not kernel-checked. Novelty unchecked
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

## Running now (2026-10-19 late)
- grb_group_bt.py (Gurobi, 2 threads), E37g successor.
- Codex agent (one at a time): Lean P31 + Beckner (.research/agents/lean_p31_brief.md).
  - T1–T4 KERNEL-CHECKED, lead-audited 2026-10-19 (CERTIFICATES):
    - full finite Fejér–Riesz (`finite_fejerRiesz`);
    - P31-E;
    - unconditional P31 (`p31_elementary`);
    - `dense_elementary`: |A| >= 0.41·max A ⇒ M >= √|A|/1000 at every size.
  - Now on T5 (Beckner M1: Young on R).
  - NEXT agent after it: Lean for P31-C (explicit (C) and the dense c(δ) table). The dyadic statement is VOID:
    linear M is trivial there.
- DONE this session (2026-10-19 late):
  - E50: power laws are worse than the triangle.
  - E51: P32 does not contract; the Bu spikes are the mod-3 dilation.
  - E52: two-level profiles give linear M from kinks.
  - E53: P31 efficiency.
  - E55: P31 gives c(profile) > 0 for Bu, Singer and the triangle.
  - E56: smooth numbers are killed by the dilation pinch.
  - E57: L⁴ window, C₄ = 0.4862.
  - PROOFS P31-C.
  - NOTEBOOK: strategic review, dilation pinch, Bu as a map with the bi-flat target, linearity of the P31 family.

## Active lines (>= 3) (updated 2026-10-19 late; strategic review in NOTEBOOK)
1. [lower bound, structural SR] P31 gives Chowla for every non-front-loaded set: δ > 0.385, or any A ⊂ [εX, X].
   - The whole window/Nikolskii family stops at front-loading. Its recursion would need an effective constant
     < 2/3 < 0.687; KILLED.
   - The remaining lever is arithmetic. Idealized SR is rigorous in the toy model: spike set = subgroup ⇒ PD residue
     pattern ⇒ subgroup ⇒ dilated full interval ⇒ P31.
   - NEXT: a robust "near-PD 0/1 pattern ⇒ near subgroup" lemma with √-type loss (localized Sanders), plus a transfer
     from tall spikes at a/q to residue structure.
2. [lower bound, Z-specific run-top] P27 Theorems A–D, bounded unions of translated dilates.
3. [construction] Every known mechanism is pinned at >= ½.
   - Bu = dilation (3D) + phase-rotated square (sums in 1 + 3Z). It saturates M(A ∩ 3Z) <= M(A).
   - Counting: real-square identities with lag multiplicity m give R >= 1/(2√m), so a sub-½ square identity needs
     multiplicity m >= 2 with aligned weights.
   - E52 probes the escape class.
4. [verification] Lean: conditional P31 kernel-checked. Fejér–Riesz, P31-E, the dense corollary and Beckner are in
   progress (agent).
KILLED this session: R3/P32 recursion (Λθ > 1; E51 B >= 1.7); low-pass P31 recursion (needs Nikolskii < 2/3);
window-shape/divisibility tweaks of the dense threshold (O(θ³) gain).

## Compute policy
Gurobi 13.0.3 full distribution at /opt/gurobi1303/linux64 on dirichlet with the user's licence
(/opt/gurobi1303/gurobi.lic; env set in src/dirun.sh). User rule: Gurobi is the solver for every MILP/LP.
All calculations on GCP VM dirichlet via src/dirun.sh; never the laptop or fejer. Global quota CPUS_ALL_REGIONS = 16.
Process rule (user, 2026-10-18): computations are fire-and-forget; foreground time goes to mathematics, one codex agent
in parallel.

## NEW 2026-10-19 (night)
- **P34 (PROVED on paper, lead): one-sided Littlewood.** −min_t Σ_{j=1}^n cos(jt − θ_j) >= 0.28√n for all phases and all
  n. The trivial Nikolskii constant gives 0.189√n. The same holds for max T and for ±1 Littlewood cosine polynomials.
  - Sharp order (Rudin–Shapiro).
  - Supersedes Erdélyi 2607.21877v1's claimed n^{1/3}/60.
  - Proof: the P31 chain with complex coefficients. Only |b_j|² enters.
  - Note: .research/notes/littlewood_onesided_P34.md. E61 adversarial optimum ≈ 0.61√n.
  - **KERNEL-CHECKED** (lead-audited): p34_A_phases (√n/4, all n, all phases), p34_B (±1) and p34_C. P33 and the
    dilation pinch are kernel-checked too.
  - P36 (truncation at gaps, exact constant 1 − cos(π/(D+2))) KERNEL-CHECKED 2026-10-19 (lead-audited, 384/384 standard
    axioms). Beckner M4 is partial: product-integral monotonicity and the scalar asymptotic are checked.
- **Dense comparison:** Bu et al. Prop. 9.7 (Oct 2026) gives only n^{1/4} for A ⊂ [1, Cn] and leaves √n open. Our
  kernel-checked dense theorem gives √n for C < 2.466. New lead target T-dense: all C. Note that localized windows are
  exactly critical (NOTEBOOK no-go), so it needs run/boundary input.
- **E60 + P37:** the escape class contains sets with R -> ½ (Bu + o(√k) far outliers; PROVED in P37 modulo Bu et al.'s theorem). Bu + 2–4 far Sidon outliers has front ratio up to 200 and R within
  +0.026 of Bu. P31's barrier is purely methodological. Profile methods are exhausted for Chowla.

## NEW 2026-10-19 (late night, session 3)
- P36 KERNEL-CHECKED (exact constant). Planar geometric Brascamp–Lieb (rank one, arbitrary L¹ data) KERNEL-CHECKED,
  with the explicit Young frame and the exact Beckner factor (CERTIFICATES). Remaining for sharp Young: the Lp
  substitution step, then M5 and P31-N (next codex agent).
- Construction line: the ONE-BU-STEP class A = 3D ∪ E, analysed (NOTEBOOK "One Bu step with D fixed", T1–T8).
  - Z lies in a triangle of inradius P = f_D(3x) + M.
  - Ceilings: pinch λ <= 2 + O(M/|D|); phase-blind λ <= R(D)² + ½ (bi-flat iff equality).
  - q = 2 is pinned at λ <= 1 + M/|D|, attained by "Bu-q2".
  - Near M = M(D), W must vanish to second order wherever P does. So equioscillating (dense-optimal) D admit almost
    no E, while Sidon D admit W = ½F².
  - "F²·u" designs and phase-locked doubles are killed: the parity obstruction (exact locking impossible) and linear
    phase drift (a violation factor of 1.1255).
  - Experiments E64 (Gurobi exact class optima: Golomb k = 6–12; dense D; second level D = Bu set) and E65 (annealing
    at Singer k = 12–24) are running. They decide whether λ > 1 survives as k grows (approximate locking) or λ -> 1
    (incircle barrier).
  - First data: N24 at M = M(D) gives E = ∅ (proved optimal). At Mt = M_Bu, k = 6: λ = 2.13; k = 7: λ >= 1.67.
    These are finite-size slack effects until larger k are in.
- E61b: the sharp one-sided Littlewood constant is ≈ 0.608 (heuristic, n <= 768), against P34's proved 0.28.

## Session 3, latest block (2026-10-19 late): T-dense round 1 verified; third-moment line; one-step class closes
- NEW, PROVED (lead-verified; PROOFS):
  - P38 (agent TD1/TD2): denominator filters prove Chowla for cumulative rounding of decreasing profiles with
    rational start density. This includes a front-loaded, run-free family with M >= √n/1000.
    The first √n theorem inside the P31 escape class.
  - P39 (agent TD4): third-moment reduction V² <= m²V + mW for any positive multiplier. Physical form: Δ_q is the
    signed Schur count of the second difference g_q = D_q 1_S. LM-dense would imply T-dense.
  - P40 (lead): spike-truncation (Bhatia–Davis). Any counterexample is spike-dominated for every multiplier,
    i.e. 1_A is ℓ²-close to a band-limited function on a set U of characters with |U| <= ε^{3/2}.
- OBSTRUCTIONS (P39-O):
  - (i) Multi-dilate interval unions defeat every multiplier of degree < P/3 (general sets, linear M).
  - (ii) Bohr unions with J ~ log X/log log X probably defeat LM-dense with one filter (HEURISTIC; agent T1 tests it).
    Product filters lose (3/8)^{J/2}.
- E64/E65 (one Bu step): R_opt/R_Bu = 0.84, 0.94, 0.97, 0.98, 1.00 at k = 7, 8, 9, 11, 12 (time-limited MILP).
  At k = 12 the class optimum IS Bu. E65 annealing at k = 12 with λ > 1 raises M by 35–44%.
  The one-step class closes onto Bu (T9/T10 prediction confirmed). Dense optima are rigid: E = ∅.
## Session 3, latest additions (2026-10-19 late night)
- P41 (lead, PROVED on paper): Chowla for cumulative rounding of curved piecewise-C² profiles, at any start density
  (irrational included), with no front-loading or monotonicity condition. Proof: spike truncation (P40), Vaaler and
  van der Corput. E66 numerics agree (curved R ≈ 1.4–3.0).
- P39 V_q normalization corrected (agent catch).
- TD5 (round-2 agent, lead-checked step by step; to be recorded in PROOFS when the report is final): LM-dense is
  FALSE at C = 16.
  - Family: random rounding of a positive Fejér mixture with J ≍ log X bumps.
  - W_q ≳ X²/log²X for every q, with M >= √n/128.
- Conjecture SB (NOTEBOOK; implies Chowla via P40): ∫_{f <= K√n} f² >= c·n for every A.
  - E67 zoo: intervals ≈ 0.05–0.10 (negative sidelobes); Bu/Singer ≈ 0.45–0.53; certified small optima ≈ 0.23–0.41;
    random 0.7–0.96.
  - E67 SA (minimize β_K) is running.
- Next derivations:
  - (1) P41+: flat Sturmian pieces excluded from the bulk accounting (Diophantine bookkeeping).
  - (2) Two-level arbitrary rounding (front-loaded profile × q-periodic pattern): bulk or kink sidelobe.
  - (3) Every 0/1 sequence factors into maximal Sturmian (balanced) pieces via the taut string. Study whether pieces
    of length <= K√n plus long Sturmian pieces give SB.
## Session 3 (2026-10-19 night): P47–P53, E69–E70
- P47 (lead, PROVED on paper; E69b audit passes on 144 rows): the P31 window applied to H_h·f_A, with the high-pass
  multiplier H_h = 1 − K_h/K_h(0).
  - Chowla holds for EVERY bounded-discrepancy rounding (non-cumulative, any D₀ <= cX^{3/4}) of a Lipschitz profile p
    whose rounding energy e = p(1−p) is not front-loaded: e(0) < 2.6ē, or more generally Γ(θ) > 0 for some θ.
  - This covers every profile starting at density 1 and TD2's ½(1−t)². No LO, curvature or Diophantine hypothesis.
  - The nonlinear input is a² = a: ‖1_A − p‖² = Σp(1−p) + O(D₀(1+V)).
- Escape class of the whole P47 family (NOTEBOOK): local variance front-loaded at EVERY scale h, i.e. a front with
  density in (0,1) plus a sparse tail. The tail would have to fill the front's dips (|B| >= 2c²|D_F||F|).
- P48–P51 (round-3 agent, verified): TD9 macroscopic PD twisted profiles; TD10 fixed fractional flat piece ⇒ LINEAR M;
  TD11/TD12/TD12-F (P41+, P41-B incl. finite Fourier Bohr profiles); TD13/TD14 bump obstructions.
- P52 (lead): local Bessel budget Σ_{θ≠0}|q_θ|² <= p(1 − p).
- P53 MACRO-SB (lead, PROVED on paper, adversarial check running): M = o(X) ⇒ the local spectrum is NOT purely
  atomic for any countable nondegenerate frequency family.
  - Proof: joint PD of the local pattern density g on [0,1] × K, plus continuity, plus g ∈ {0,1}.
  - Corollaries: TD10; every Bohr-window set {m : {mα} ∈ E(m/X)} and every residue-pattern set has LINEAR M.
  - Meaning: macroscopic structure alone can never give a counterexample. The remaining mass must sit in spikes of
    height o(X), which motivates the descent (D).
- E70 (P47 family scanned on 159 zoo/E68/Bu sets): best bound >= 0.106√n on every set, and 33–52% of M on near-optimal
  sets. On Bu/Singer, best/√n drifts 0.29 to 0.237 (q = 7 to 31). E70b (q up to 127) is running.
- E69: bounded-discrepancy roundings, R ∈ [1.6, 3.0] (walk); adversarial blocks give linear M.
- Next derivation (lead, foreground): the descent below macroscopic scale.
  - Candidate 0/1 input: a torus level-1 inequality (TL1). For E ⊂ T^S, the Fourier mass of 1_E on the characters
    e^{±iω_s} is at most (8/π²)|E|(1 − |E|), conjecturally sharp at S = 1, |E| = ½.
  - TL1 would force ≥ 19% of a 0/1 local pattern's variance onto COMBINATION frequencies. A counterexample's spike set
    must then be approximately additively closed. This is the robust SR/Sanders line L1 in a cleaner form.
  - Caveat: it applies only where the window equidistributes in T^S, i.e. few, tall spikes.
- P54 TL1 (lead, PROVED): level-1 Fourier weight of any E ⊂ T^S on a graded character set is
  <= (8/π²)|E|(1 − |E|). Proof: Steinhaus rotation trick.
- Round-4 agent (partial, verified by lead): P47 CONFIRMED-WITH-FIX (asymptotic qualifiers); P53 CONFIRMED-WITH-FIX
  (Bohr-window corollary needs joint regularity of B ⊂ [0,1]×T).
  - NEW defect: g <= 1 − t²/4 pointwise, hence b >= m³/12.
  - NEW finite-window QD at fixed complexity: M <= ηX ⇒ energy outside any J windows >= X/(48C³) (ineffective).
- CURRENT REDUCTION (NOTEBOOK cont. 4): T-dense ⟸ (A) finite TL1 for tall-spike sets, with errors given by weighted
  unbalanced relation counts, + (B) the structured case (torsion / additive relations ⇒ P53 rigidity or recursion).
- Round 4 DONE (PROOFS P55). HBCG (window QD-½) is the precise missing inequality, and HBCG ⇒ T-dense is proved.
  PD plus Bessel cannot give it (saturating example), and TL1 (P54) is the binary input that kills that example.
- E70b: the P47 family gives ≈ 0.21√n on Bu up to n = 63252. With the rigorous ρ_L: 0.17√n at q = 127.
- E72: the optima shrink max A to <= 2.9n (mostly inside P31's range), so it does not test C = 3. E72c (box ratios
  4, 6, 10) is running.
## Session 3, round 8: T-dense(6.156), explicit c(3) (2026-10-19 night, NEWEST — read this first)
- Round 8 DONE, lead-verified (PROOFS P59; NOTEBOOK cont. 11).
  - ENERGY-PD: in any dense counterexample limit, the residual energy profile e = p(1 − p) is PD (autocorrelation of
    g + m >= 0). Hence p(0) <= ½. This alone with the density window gives T-dense(5.196).
  - ρ* <= 0.815276 (exact certificate; 4-point Toeplitz plus separable potential). Hand proof: ρ* <= (2 + √2)/4.
  - T-dense(C) for every C < 4(2 − ρ)/r = 6.156 (ineffective).
  - EXPLICIT c(3) = 10^{−6000005}: a finite Gaussian-scale pigeonhole replaces compactness. First effective result
    beyond P31; Lean candidate.
- cont. 10's "macroscopic barrier 6.05" is RETRACTED (it covered only the two scalar windows).
- E79: the ρ*-extremal shape violates energy-PD, so the enlarged class's reach is > 6.63. E80 (running) estimates it.
## Running now (2026-10-19 night, newest)
- VM: E80 (src/e80_enlarged_reach.py): SLSQP over autocorrelation profiles with e-PD and window constraints.
- Codex MATH agent, round 9 (.research/agents/tdense9_brief.md; report tdense9_report.md).
## First concrete next step (2026-10-19 night, newest)
- Round 9 (one codex agent): the exact reach of the enlarged macroscopic class, with certificates, giving T-dense(C₉);
  extra macroscopic constraints (measure-valued PD of σ_t, atoms, Boolean); effective constants.
- Then a Lean round for the effective T-dense(3) (P59.6), with P31-E already kernel-checked.
## Session 3, round 7: T-dense(4.4393) (2026-10-19 night)
- Round 7 DONE, lead-verified (PROOFS P58; NOTEBOOK cont. 10).
  - THEOREM (paper, ineffective constant): M(A) >= c√|A| for every A with max A <= 4.4393|A| (<= 4.2138|A| with the
    elementary Nikolskii constant).
  - Ingredients:
    - compactness gives a PD limit profile p;
    - NEW exact high-pass diagonal: H_h f >= −M has coefficient energy profile p(1 − p);
    - P31 windows on f and on H_h f;
    - P17(a)'s doubly-positive gap ρ* <= 0.90565.
  - In general: T-dense(C) for C < (2/r)(1 + √(1 − ρ*))².
- Exact obstruction: a rational PD profile defeats both windows at every scale at C = 6.0539, so this macroscopic
  method's reach is ≈ 6.05. Numerically ρ* ≈ 0.7239 (E78), so the sharp ρ* would give C ≈ 6.046.
- Beyond 6.05 a counterexample's residual (about half the energy) must sit in MESOSCOPIC spikes (P40 applied to the
  high-passed function). The rest of T-dense is the mesoscopic problem, now with an explicit adversary profile.
- E75–E77 recorded (run-tops closed; zero-set strengthening refuted).
## Running now (2026-10-19 night, round 8; superseded)
- Codex MATH agent, round 8 (.research/agents/tdense8_brief.md; report tdense8_report.md). VM: E78 finishing.
## First concrete next step (2026-10-19 night, round 8; superseded)
- Round 8 (one codex agent):
  - (1) sharpen ρ* rigorously, reaching T-dense up to ≈ 6.04;
  - (2) test whether any other √n-scale inequality survives the macroscopic limit and kills the 6.05 witness (P32 local
    windows, L⁶/third-moment windows, product windows);
  - (3) an effective finite-scale version (explicit c(3)) as a Lean candidate.
- Afterwards: the mesoscopic attack beyond 6.05, with the witness profile as the test object.
## Session 3, round 6 + cont. 9 (2026-10-19 night)
- Round 6 DONE (PROOFS P57; adversarial "formal escape" round). No formal escape and no inconsistency proof.
  - Tent-lift identity: the negative spectral mass of the natural lift is exactly mean|f| >= n/(n + M), and it escapes
    to microscopic scales.
  - Binary-faithful lifts have δ >= m²/24. Natural and binary-faithful lifts FAIL HBSC; existential HBSC is open.
  - Weighted Gram D_N ⇒ WGC (CONJECTURED) ⇒ T-dense. OBSF (CONJECTURED) ⇒ T-dense.
  - Fractional relaxation optimum is exactly n/X (Fejér weights): all of Chowla's difficulty is the 0/1 constraint.
- Run-tops CLOSED as a T-dense route (NOTEBOOK cont. 9; E74–E76).
  - |B_t| = r(t) − T₃(t), so the averaged statement IS T-dense.
  - Per-t RT2 contains OR(2)-weak.
  - E76: Bu et al.'s per-t split loses the factor Kμ on Bu sets, and averaging cannot recover it.
  - E75: annealing finds no RT2 violation (max |B_t|/K² <= 0.39).
- Zero-set strengthening S(A) <= M(A) REFUTED (E77): S([1, n]) = 1 exactly. On near-extremal sets S ≈ M (the minimum
  sits on a negative-axis crossing of G).
- Round 7 (RUNNING): the C₁ programme. Extend the kernel-checked dense theorem (C <= 2.44) to T-dense(3), and compute
  the reach C₁* of windows + near-0/1 lemmas (NOTEBOOK cont. 9 §4).
## Running now (2026-10-19 night, round 7; superseded)
- Codex MATH agent, round 7 (.research/agents/tdense7_brief.md, report tdense7_report.md, log tdense7_codex.log).
- VM: free apart from the agent's jobs (E75/E76/E77 done).
## First concrete next step (2026-10-19 night, round 7; superseded)
- Verify round 7 when it lands. If T-dense(3) is proved: lead re-check, then hand the proof to Lean (P31 is already
  kernel-checked). If it fails: record the obstruction at C = 3 and the extremal escaping profile.
- Lead foreground meanwhile: the construction line (escaping profiles at C₁* as test objects), and WGC/OBSF as the
  deep targets.
## Session 3, round 5 + review (2026-10-19 night)
- Round 5 DONE (PROOFS P56; lead re-checked FTL1, CY1, SG and the interval obstruction):
  - FTL1: a finite TL1 with explicit errors. The error is R/D with R = Σ|c_s|, so it is NOT uniform in the spike count.
  - CY1: exact cyclic P40 → TL1 bridge.
  - SG: stable Gram, h <= 1 − t²/4 + 2δ.
  - HBSC: CONJECTURED single sufficient lemma.
  - QD with any exponent β > ½ is FALSE (interval example).
- Lead caveats (NOTEBOOK cont. 7). CY2's relation alternative is uninformative:
  - the padded profile/central lobe is never graded and supplies the relations itself;
  - L(0) = R makes Z heavy-tailed, so the radial-moment branch holds automatically for mesoscopic spikes.
- Lead (PROVED): uniform LAW-LEVEL TL1 by radial truncation, with error 4√(2/(πD)) uniform in S, R and the tails.
  Its defect is the angular harmonics of the truncated law of the spike signal. Gap: from the law-level defect to
  usable structure.
- Lead (NOTEBOOK cont. 8): DIMENSION BARRIER.
  - PD at all levels ⇒ Wiener budget Σĥ_χ(0) <= 1 ⇒ every spike is macroscopic (limit object).
  - The finite front Riesz test costs M(1 + λ)^S.
  - The dimension-free tools (TL1, SG, P40) are ℓ²/law-level and do not give ℓ¹ budgets.
  - HBSC needs negative mass <= M/H, but natural accounting gives <= M. HBSC may be false.
- E72c: the window family is escaped at C ≈ 5–10 (B/√n ≈ 0.02) by box-filling sets with R ≈ 0.9–1.3. C₁ ∈ [2.47, 4.8].
- E73: Gaussian-threshold (growing-rank Bohr) sets have linear M at every fixed rank (R ∝ √X). High rank approaches
  the Bernoulli baseline (R ≈ 2.9 at X = 2^18) from above. The simplest escape class is dead as a construction.
## Running now (2026-10-19 night, superseded)
- Codex MATH agent, round 6 (.research/agents/tdense6_brief.md, report tdense6_report.md). ADVERSARIAL:
  - build a "formal escape" (every proved constraint, mesoscopic spikes, M ≪ √n), or prove the constraints
    inconsistent;
  - HBSC verdict;
  - optionally, averaged run-tops in Z.
- VM: E74 (src/e74_runtops.py: run-top counts |B_t| against K² and K³μ on the zoo, Bu/Singer, small-N, random and
  E68/E72c sets); E64 bu2 k7; E65 q23.
## First concrete next step (2026-10-19 night, superseded)
- Verify round 6.
- If a formal escape exists, realize it as actual sets (construction lead). If not, its inconsistency proof or
  missing constraint replaces HBSC.
- Read E74. If mean_t|B_t| <~ K² holds empirically with room, the averaged run-top route (Bu et al. Prop. 9.7 with
  K^{3−δ}μ on average) becomes a second lower-bound line.
## Running now (2026-10-19 night, round 5; superseded)
- Codex MATH agent, round 5 (.research/agents/tdense5_brief.md, report tdense5_report.md):
  - finite J-uniform TL1;
  - the dichotomy toward HBCG;
  - QD-½.
- VM: E64 bu2 k7; E65 q = 19/23 SA. Free cores available.
## First concrete next step (2026-10-19 night)
- Verify round 5 when it lands.
- Lead foreground: the "P31 + P47 ⇒ T-dense for C < C₁" case analysis (E72 suggests C₁ >= 3), or a direct attack on
  HBCG via TL1.

## Running now (2026-10-19, session 3, latest)
- Codex MATH agent, round 3: .research/agents/tdense3_brief.md (report tdense3_report.md).
  - T1: spike-dominated dense sets (P40 + twisted profiles / positive-bump uncertainty / multiscale).
  - T2: rigorous P41+ (flat pieces) and P41-B (Bohr-modulated).
  - T3: falsification against E67/E68.
  Round 2 (tdense2) is DONE and recorded as P42–P46.
- VM: E68 Pareto search β_K + μR on dense boxes X = 3n (src/e68_pareto_sa.c, examples/e68/): can spike domination
  and small R coexist?
- (superseded) Codex MATH agent, round 2: .research/agents/tdense2_brief.md (report tdense2_report.md).
  - T1: decide LM-dense on Bohr unions (exact triple counts).
  - T2: a certificate surviving Bohr unions (Stieltjes 5/7 moments, spike-masking multipliers).
  - T3: P38 for bounded local discrepancy.
  - T4: energy-increment lemma.
- Round 1 (tdense_brief.md, tdense_report.md) is DONE and recorded.
- Lean: sharp Young (Beckner) and M5 are KERNEL-CHECKED. Only P31-N remains; its drafts are uncommitted
  (P31/FourierL2.lean, P31/SincInterpolation.lean).
- VM: E64 second level (D = Bu, k = 6, 7) and dense N50 eps; E65 (Singer q = 13–23); grb_group_bt; e37g.

## Running now (2026-10-19 night, earlier)
- Codex Lean agent (one at a time): P34 complex-coefficient chain and Corollaries A–C, then P33/pinch
  (.research/agents/lean_p34_brief.md; report lean_p34_report.md). Beckner T5 is PAUSED after a partial: M1/M3 and M4
  infrastructure are kernel-checked (CERTIFICATES). Resume M4 in the next Lean slot after P34.
- VM:
  - grb_group_bt (2 threads);
  - E61b (sharp unit-amplitude constant, n up to 1024; baselines done: chirp 1.17, Rudin–Shapiro 1.41, random 2.3–2.7);
  - E62b (phase relaxation on larger supports; so far N50 0.498, Singer q31 0.598, q61 0.633, triangle 0.550).
- New tools this block:
  - P34 (one-sided Littlewood);
  - P36 (truncation at gaps, quadratic error);
  - the frequency-localization no-go (NOTEBOOK);
  - exact real-square identities: |A| = (Σc²)² − Σc⁴, and multiplicity >= 2 is impossible for real squares.

## First concrete next step (updated 2026-10-19, end of session block)
Proved this block:
- P33: M(A) >= |A|·min A/max A. The linear-test optimum (E58); folklore-level.
- KERNEL-CHECKED dense theorem (CERTIFICATES).
- P31-C(a, b) found VOID: sets without small elements have linear M. Corrected everywhere.
(1) Lower bound. Window/Nikolskii (second-moment) arguments are linear in 1_A and cannot reach the escape class
    (NOTEBOOK, "Why the P31 family stops").
    - Needed: a NONLINEAR certificate.
    - Candidates: weighted windows with weight 1/(M + G) (derived; untested); robust SR via a residue-pattern lemma on
      Z_q; Cayley-graph structure (λ_min = −2M) à la JMTZ with Z-specific input.
    - First derivation: state the weighted-window inequality ∫(f + M)²/(M + G) <= (C/W)M precisely and evaluate it
      in the spike model.
(2) Construction. The bi-flat factor target (NOTEBOOK/CONSTRUCTIONS).
    - Bu is optimal among phase-blind square identities (single class; incircle).
    - Beating ½ needs either phase-locking or lag multiplicity >= 2 with approximate bi-flatness.
    - E59 (running) gives the R(n) trend for smooth escape-class profiles.
(3) Lean. The agent is on T5 (Beckner M1–M5). Next agent: P34 in complex-coefficient form (generalize p31_elementary to
    Σ(a_j cos jx + c_j sin jx) with a_j² + c_j² <= 1; Corollaries A–C), then P33, the dilation pinch and P29.
