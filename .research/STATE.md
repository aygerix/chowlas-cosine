# >>> READ FIRST: .research/CSTAR.md <<<
C* (the mesoscopic many-spike regime) IS the problem. CSTAR.md holds the fixed object, the forced features, the design
rules, the proof chain and the attack log. Everything below is the record: proved side results, certified constructions
and kills. Side results are not the prize (user, 2026-10-19).
Latest (cont. 30):
- SCP(T) REFUTED for every T by orthogonal padding (external review, lead-verified; CSTAR A8): a spread U × 0 plus a
  random F_2^r component 0 × B has ratio → ∞ but C_CP/K → ∞. The chain "Chowla ⇐ SCP + CP-Chowla" is dead as stated.
- Target now: CP-CHOWLA(Z), C_CP(A) >= c√|A| (sum the endpoint multiplicity losses of P76(c) over all blocks).
Previous (2026-10-19, cont. 29):
- F12 CORRECTED. FLAT completely positive certificates are 1.3–1.5× too expensive (N50: R_CP(flat) = 0.857 against
  R = 0.570, lead-verified). Non-flat nonnegative (two-level) CP certificates come within 1–8% of M (X30_s0:
  0.655 against 0.607, lead-verified exact). So near-optima need WEIGHTED blocks, not phase cancellation.
  DNN = M at minimal degree.
- A6/A6′ SPREAD PRINCIPLE: every known ratio → ∞ object in any abelian group is a union of subgroups (CP). Hence
  Chowla ⇐ SCP(T) (group-agnostic: high ratio ⇒ CP-efficient) + CP-Chowla(Z) (Z-specific, P76). SCP(2) is false
  (Paley); E112a puts T > ~2.2.
- A7 FLAT-SPECTRUM BARRIER: symmetric-spectrum objects have ratio 1/(1 − d) <= 2. Beating 2 needs spiky
  asymmetric spectra, i.e. Latin-square-type PDS, all known ones being partial spreads.
- Open toy: SCP in F_p² (NOTEBOOK cont. 29.10).
- Literature check queued: are Latin-square-type PDS with small r always partial congruence partitions?
Earlier (after the advisor review): A2 automatic sets are CLOSED as a design class. All 71,840 small automata
fail the FPC (interval-certified, linear M). P75 is a partial general theorem; T-A2 is open (side lemma).
- A3 (rational-spike anatomies) adds design rules D8 and D9 and the proved feature F11.
- Step (c) is unchanged. D9 made rigorous reduces to M >= ½‖f‖₁ (L¹ additivity over separated pieces), which is too weak.
- A4: the blueprint (continuum) level is consistent, so C* lives entirely in the 0/1 fine structure.
- A5 (cont. 28): regime split at n^{1/3} (additive structure is visible only for M <~ n^{1/3}; the C* core is
  random-dominated). Hoffman bound recorded as a fact. The rank dichotomy (rigorous E73) is DEPRIORITISED.
- cont. 29 (E110 + E111 done, lead-verified):
  - F12 corrected: flat CP is 1.3–1.5× M (N50, verified); two-level nonnegative CP is within 1–8% of M
    (X30_s0, verified). Not phase cancellation: weighted blocks.
  - P76 (proved): DNN = PSD on an unbounded index set; C_CP >= 2n/(ω − 1); extreme-lag multiplicities; sublattice
    restriction.
  - CP½ conjecture: equal-size case proved; rank and coverage give only log.
  - A6/A6′ SPREAD PRINCIPLE and the reformulated chain Chowla ⇐ SCP(T) + CP-Chowla(Z). SCP(2) is false (Paley).
    All known ratio → ∞ objects are spreads (CP).
- FIRST NEXT STEP:
  - E112: in moderate finite groups, search for high-ratio sets FAR from unions of subgroups and measure their
    CP-efficiency.
  - Test the E41 Z_p half-sets (ratio ≈ 2.14) first.
  - A high-ratio non-spread object would break SCP and be the first candidate mechanism for C* in Z.

# STATE — current targets and honest status (updated 2026-10-19 late; newest block at the END: "Handoff 2026-10-19 late (cont. 24–25)")

## Targets
- (C) Epoch: algorithm solution(c,n) for all c>0 — requires R(A_k) -> 0. NOT ACHIEVED. No solution.py exists.
- (L) Chowla: M(A) >= c0 sqrt|A|. NOT ACHIEVED. Best known: >> n^{1/5} (Shankar 2609.05338, cited, checked).
- (L-dense) T-dense(C) := M >= c(C)√n for all A with max A <= C|A|.
  - PROVED for every C < 2000/259 = 7.7220, ineffective c(C) (P61 + P63: second-order reduction plus the exact
    support-line certificate D <= 259/2000; two independent exact verifications, C-R11 and E85).
    - Earlier: C < 7.5019 (P62), C < 6.9366 (P60).
  - EXPLICIT constants for every C < 6.156 (P60.7); c(3) = 10^{−6000005} (P59.6).
  - Kernel-checked effective: C <= 2.44 (P31).
  - P61 (lead, paper; awaiting adversarial check): T-dense(C) for every C < 1/D, where D = sup ∫_0^1 φ(|w|²) over PD w
    supported in [−1, 1] with w(0) = 1, and φ(x) = (1 − √(1 − x))/2.
    - This is SHARP for positivity + two binary moments (weighted packet escapes).
    - Numerically 1/D ≈ 8.5708 (E82). Rigorous D <= 0.1295 (P63). The certificate family saturates near 0.129.
    - Beyond 1/D: three moments are free (P62.3). The fourth moment / approximate binarity is the open layer.
      - Gaussian packet escapes are order-X away from any four-profile escape (P63.3).
      - Anchored tests of every fixed order >= 3 are provably blind (P63.2).
    - Cleanest binary target FRONT-½: a = p(0) <= a* < ½ gives T-dense(C < 1/(4a*(1 − a*)D)).
      - A front-only proof would prove cyclic half-set Chowla, which is open (NOTEBOOK cont. 16.3; P64.4).
      - So it must use the taper coupling.
    - Round 12 (P64) pins the missing ingredient.
      - Integer side: CSFG(20) ⇒ T-dense(C < min(20, 1/D_σ)), beyond 1/D (R12-B).
      - Cyclic side: the peak lemma PK(η) (Λ <= CK^{2−η}) beats Sanders' 1/3; PK(1) gives √q.
      - Scalar moments provably cannot do it (R12-S). The full convolution identity λ⋆λ = qλ is needed.
- (L-dense, exponent 1/3) PROVED (P66, lead; AUDITED CORRECT by round 15, P68): M >= c(C)|A|^{1/3} for every C < 1000/73 = 13.6986 (computer-assisted: dedicated σ = 2/3 certificate D_{2/3} <= 73/1000, re-run by lead), ineffective; 13.2548 via E94b mixing; fully analytic for C < 9(1 + √3)/2 = 12.294 (Beckner).
  This is the cubic front cap: under M = o(n^{1/3}), the cubic Schur profile g(p) = p(1 − p)(1 − 2p) is PD, so
  a <= (3 − √3)/6. Numerical reach ≈ 15.6 (E93b). Bu et al. have exponent ¼ for all C.
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
## Session 3, round 13: cyclic barriers; round 14 = Sanders at every density (2026-10-19 night)
- Round 13 DONE, lead spot-checked (PROOFS P65; EXPERIMENTS E91).
  - Universal PK is FALSE (R13-PK): profile-rounded half-sets have Λ ~ εq/2 with K = O(√(q log q)). The right
    intermediate is QU(β).
  - Barriers: the exact identity along any prescribed segment J = o(q^{1/3}) of the peak orbit (R13-C), and any fixed
    order of moments, integrality and congruences (R13-M2), are both consistent with exponent 1/3.
  - Binary escapes: 20 laws, all R > 0.6 and growing (certified dips).
- Lead.
  - E90 large-q cyclic search: inconclusive (search-limited).
  - NOTEBOOK cont. 17.6–7:
    - sparse P61 is second-order trivial apart from front shape (it gives P31's 2.91);
    - 2-D obstruction: independent lacunary scales force linear M, so counterexamples are one-dimensional at every
      scale;
    - the dilation-deficit form of the cyclic problem.
- NEW (lead, P66): CUBIC FRONT CAP. Dense exponent 1/3 for every C < 13.2548 rigorously (P63 + E94b mixing; 12.294 fully analytic; ≈ 15.6 numerically, E93b).
  Codex adversarial check pending.
- Lead read Sanders 0807.5104v2 pp. 1–10.
  - Thm 4.1 gives exponent α/5 at density α, from r = 2⌈1/α⌉ convolution powers in Lemma 3.2; the half-set case is
    1/3 after careful accounting.
  - JMTZ give ¼ − ε at every density; Bu et al. dense ¼.
  - So a density-INDEPENDENT cyclic exponent θ > ¼ would give DENSE CHOWLA EXPONENT θ FOR EVERY C, via the embedding
    q ∈ (2X, 4X]. That beats the 2026 literature for C > 7.72.
## Session 3, round 14: Sanders transfers end at ¼; P66 range 13.25 (2026-10-19 night)
- Round 14 DONE, lead-verified (PROOFS P67; examples/r14_certificates/).
  - R14-CENTER: centred convolution powers regenerate the δ term at every order, U^{(r)} = A_rU + qm_rδ. The first
    favourable order is ≍ 1/α, and even then the norm estimate gives K^{r+1} >> q.
  - R14-UNION: union with a fixed dilate creates order-q negativity.
  - Sanders' half-set 1/3 is not reconstructed in the small-spectrum branch: Λ = O(KL²) = O(K³) gives ¼ only.
  - Embedding correction: use q ∈ (4X, 8X].
- Lead.
  - E94b (RIGOROUS): P66 now holds for C < 13.2548 (mixing P63 and Beckner on 𝒲).
  - E95: the dedicated D_{2/3} LP saturates near 13.8.
  - E96: degree-3 SOS / Sherali–Adams gives K = O(1) for half-sets (two-point pseudo-marginals): dead end.
  - NOTEBOOK cont. 18.2: profile and moment methods at θ > ¼ are capped by the third-order reach.
  - NOTEBOOK cont. 18.5: the equality case of the cyclic ¼ argument is a flat ±½ PD function with spectrum Π, |Π| ~ √q,
    and Π + Π covering Z_q uniformly, i.e. a weighted REVERSIBLE difference set. Exact versions are impossible
    (Galois ⇒ Paley; cyclic reversible difference sets are trivial). Making this quantitative is the new route past ¼.
## Session 3, round 15: P66 audited, C < 13.699; WRS isolated (2026-10-19 night, NEWEST — read this first)
- Round 15 DONE, lead-verified (PROOFS P68; examples/r15_certificates/).
  - P66 audited step by step: CORRECT. E94b re-proved by Sturm.
  - Dedicated certificate D_{2/3} <= 73/1000, so exponent 1/3 for every C < 1000/73 = 13.699. The lead re-ran the
    certifier and the independent verifier.
  - Cyclic half-sets.
    - Exact flat model h⋆h = (q²/4)δ_0 + qK(K − 1)·1 (P26), giving K >= (½ + o(1))q^{1/4} explicitly.
    - Parity lemma: cyclic reversible difference sets are trivial (Brualdi).
    - Precise missing lemma WRS(η) ⇒ exponent (1 + η)/(4 + 2η). Its η = 1 case is PK(0): Λ <~ K².
- Lead: NOTEBOOK cont. 18.5–18.8, the corrected equality case and the clustered-peak heuristic. 18.7(a) is
  refuted (difference sets are flat).
## Running now (2026-10-19 night, newest)
- Codex MATH agent, round 16 (.research/agents/tdense16_brief.md): PK(0) adversarial search and proof attempt.
## First concrete next step (2026-10-19 night, newest)
- Verify round 16. A family with Λ/K² -> ∞ and K = o(√q) refutes PK(0), which is important either way. A proof of
  PK(0) or of any WRS(η > 0) is a new half-set exponent above ¼: re-derive it, run the adversaries, and check the
  literature.
## Session 3, round 14: Sanders transfers end at ¼; P66 range 13.25 (2026-10-19 night)
- Round 14 DONE, lead-verified (PROOFS P67; examples/r14_certificates/).
  - R14-CENTER: centred convolution powers regenerate the δ term at every order, U^{(r)} = A_rU + qm_rδ. The first
    favourable order is ≍ 1/α, and even then the norm estimate gives K^{r+1} >> q.
  - R14-UNION: union with a fixed dilate creates order-q negativity.
  - Sanders' half-set 1/3 is not reconstructed in the small-spectrum branch: Λ = O(KL²) = O(K³) gives ¼ only.
  - Embedding correction: use q ∈ (4X, 8X].
- Lead.
  - E94b (RIGOROUS): P66 now holds for C < 13.2548 (mixing P63 and Beckner on 𝒲).
  - E95: the dedicated D_{2/3} LP saturates near 13.8.
  - E96: degree-3 SOS / Sherali–Adams gives K = O(1) for half-sets (two-point pseudo-marginals): dead end.
  - NOTEBOOK cont. 18.2: profile and moment methods at θ > ¼ are capped by the third-order reach.
  - NOTEBOOK cont. 18.5: the equality case of the cyclic ¼ argument is a flat ±½ PD function with spectrum Π, |Π| ~ √q,
    and Π + Π covering Z_q uniformly, i.e. a weighted REVERSIBLE difference set. Exact versions are impossible
    (Galois ⇒ Paley; cyclic reversible difference sets are trivial). Making this quantitative is the new route past ¼.
## Running now (2026-10-19 night, newest)
- Codex MATH agent, round 15 (.research/agents/tdense15_brief.md; report tdense15_report.md).
  - (A) Adversarial verification of P66 and E94b, plus a ported σ = 2/3 certificate.
  - (B) Stability of the equality case of the cyclic ¼ bound, aiming at an exponent θ > ¼ for half-sets.
## First concrete next step (2026-10-19 night, newest)
- Verify round 15.
  - If P66 has a gap, fix it or downgrade STATE immediately.
  - If a half-set exponent θ > ¼ is claimed, re-derive it, run the adversaries (Paley, E41 optima, R13/R14 families),
    and check Sanders, JMTZ and Bu §9 before recording.
## Session 3, round 12: the missing ingredient pinned (CSFG / PK) (2026-10-19 night)
- Round 12 DONE, lead-verified (PROOFS P64; E89: R12-N falsification, 538 cases, 0 violations).
  - No new unconditional endpoint: T-dense stays at C < 7.722.
  - R12-N (proved): if A ∩ NZ is an initial progression, M >= n/((3π + 2)r). This excludes dense nested schedules with
    N = o(√X).
  - R12-U: nonnested 2-periodic sets with M = O(X^{3/4}√log X). So X/N is false without a bound on the number of
    changes.
  - R12-H (proved): symmetric half-sets of Z_q with K = o(√q) are balanced on all intervals of all dilates. Lead
    corollary: they are Fourier-uniform, max|λ| = o(q).
  - Cyclic barrier with exact quantifiers: TBS ⇒ cyclic √ (normalization corrected: H_γ = 2λ_γ).
  - CSFG(20) (conjectured) ⇒ T-dense beyond 1/D (R12-B, proved).
  - PK(η) ⇒ exponent 1/(3 − η). R12-S: scalar moments cannot beat 1/3.
- Lead (NOTEBOOK cont. 17):
  - weak-limit positivity at order k needs K = o(q^{1/k}), so a cyclic √q proof must be quantitative at finite q;
  - the finite second-order identity gives exponent 1/4;
  - the spectrum is a Galois orbit (unused so far);
  - the construction side is reduced to binarizing P61's weighted escapes.
## Running now (2026-10-19 night, round 13; superseded)
- Codex MATH agent, round 13 (.research/agents/tdense13_brief.md; report tdense13_report.md).
  - Task 1: PK(η) through full convolution, tested on exact cyclic optima.
  - Task 2: a binary-escape construction probe.
- Lead (foreground): P61 for sparse sets, written out in full (NOTEBOOK cont. 16.6c).
## First concrete next step (2026-10-19 night, round 13; superseded)
- Verify round 13. Then: does any k >= 4 power-sum (additive-count) constraint kill the R12-S fake? This decides whether
  PK can come from counts or needs the full identity.
## Session 3, round 11: T-dense(7.72); FRONT-½ and the cyclic barrier (2026-10-19 night)
- Round 11 DONE, lead-verified (PROOFS P63; E85 re-derives all 188 support lines, 22615 leaves, 0 failures).
  - D <= 259/2000, so T-dense(C < 7.7220). New support-specific symbol lines (P63.1).
  - DC-barrier theorem: Re Στ(k)ĥ(k)^j >= τ(0)(m^j − 2^{1−j}Σ|r|^j). Three-profile escapes pass every anchored test.
  - Repair-energy lemma: four-profile escapes are order-X far from Gaussian packet escapes.
  - Torsion budget: Σ_{rational θ ≠ 0} W_θ(0) <= ½ − a.
  - Full-Haar kurtosis >= 3/2. The Paley boundary: positive Paley escapes put half the variance on qZ (unbounded);
    deleting qZ costs X/√q.
  - Literature: Sanders' half-set exponent 1/3; nontrivial strongly regular circulants are Paley graphs.
- Lead (NOTEBOOK cont. 15–16):
  - Exact front rigidity: in the macroscopic model, PD indicator ⇒ subgroup ⇒ no taper.
  - Taper coupling = Fourier domination.
  - FRONT-½: a <= a* < ½ would beat 1/D.
  - CYCLIC BARRIER: the front-only lemma TBS implies cyclic half-set Chowla (open).
  - Parseval roughness: nested tapers force Hölder-½ envelopes. M >~ X/N is proved for locally N-periodic
    families; X√(p/N) is heuristic.
## Running now (2026-10-19 night, round 12; superseded)
- Codex MATH agent, round 12 (.research/agents/tdense12_brief.md; report tdense12_report.md): the coupled front problem.
## First concrete next step (2026-10-19 night, round 12; superseded)
- Verify round 12:
  - FRONT-½ via coupling, or the precise obstruction;
  - the rigorous Parseval-roughness theorem;
  - the Paley-front taper construction probe (R values, certificates).
## Session 3, round 10: T-dense(7.5); DC barrier (2026-10-19 night)
- Round 10 DONE, lead-verified (PROOFS P62; E84).
  - D <= 1333/10000 (t-dependent support-coupled potentials plus a continuum Schur test), so T-dense(C < 7.5019).
  - P61 audited and repaired for complex w.
  - Three binary moment profiles are free: sparse gadgets, ℓ¹ cost X^{7/15}.
- Lead (NOTEBOOK cont. 14):
  - The DC barrier: an order-j anchored positivity statement carries m^j/ℓ, so it is blind unless M << n^{1/j}. This
    explains n^{1/4} (Bu et al.).
  - Subgroup restrictions A ∩ qZ are counterexamples too, so rational atoms vanish when a = ½.
  - Kurtosis heuristic for the fourth-moment layer.
  - Cyclic-PDS (Ma) connection.
## Running now (2026-10-19 night, round 11; superseded)
- Codex MATH agent, round 11 (.research/agents/tdense11_brief.md; report tdense11_report.md).
## Session 3, round 9 + P61: the second-order reach 1/D ≈ 8.571 (2026-10-19 night)
- Round 9 DONE, lead-verified (PROOFS P60; E81 re-checks every certificate by a different exact method).
  - T-dense(C < 6.9366) (κ <= 0.749089).
  - The two-profile witness at 7.2674.
  - CP covariances, strictly stronger than doubly nonnegative (Horn).
  - Explicit constants on C < 6.156.
- P61 (lead): complete positivity made exact by the Gabor identity avg_u|(hψ_u)^|² = |ĥ|² ⋆ |ψ̂|², plus Jensen.
  - Hence d <= D and T-dense(C < 1/D). Weighted escapes show 1/D is the exact reach of positivity + two moments.
  - E82: 1/D ≈ 8.5708, with a symmetric bump optimiser.
  - The rounds 7–9 classes (6.05, 7.27) were relaxations.
- So the macroscopic / second-order theory of T-dense is SOLVED up to certificates. Beyond 8.571 the question is
  BINARISATION: can binary coefficient sequences have a residual made of positive packets? (NOTEBOOK cont. 12: subgroup
  lemma, Bohr failure, cubic skew.)
## Running now (2026-10-19 night, round 10; superseded)
- Codex MATH agent, round 10 (.research/agents/tdense10_brief.md; report tdense10_report.md).
- Lead, done while waiting:
  - E83: escape-seeded binary sets show NO advantage over random seeds at C ≈ 8.6 (R ≈ 1.1–1.3, search-limited).
  - NOTEBOOK cont. 13: binarisation heuristics. The subgroup lemma needs macroscopic atoms. The coefficient-square
    hierarchy gives only n^{1/4}. Anchored versus Gabor information. Spikiness ⇔ additive energy. Binary ⇔ the spike
    measure is a WEIGHTED PARTIAL DIFFERENCE SET. Random packets cost Θ(K) non-binarity.
## First concrete next step (2026-10-19 night, round 10; superseded)
- Verify round 10 when it lands:
  - P61 adversarial check;
  - rigorous D₁ (target T-dense(7.5–8));
  - third-order / binarisation result.
- Then decide: (a) Lean for P61(a); (b) a binarisation construction attempt on the VM (Track C, dense).
## Session 3, round 8: T-dense(6.156), explicit c(3) (2026-10-19 night)
- Round 8 DONE, lead-verified (PROOFS P59; NOTEBOOK cont. 11).
  - ENERGY-PD: in any dense counterexample limit, the residual energy profile e = p(1 − p) is PD (autocorrelation of
    g + m >= 0). Hence p(0) <= ½. This alone with the density window gives T-dense(5.196).
  - ρ* <= 0.815276 (exact certificate; 4-point Toeplitz plus separable potential). Hand proof: ρ* <= (2 + √2)/4.
  - T-dense(C) for every C < 4(2 − ρ)/r = 6.156 (ineffective).
  - EXPLICIT c(3) = 10^{−6000005}: a finite Gaussian-scale pigeonhole replaces compactness. First effective result
    beyond P31; Lean candidate.
- cont. 10's "macroscopic barrier 6.05" is RETRACTED (it covered only the two scalar windows).
- E79: the ρ*-extremal shape violates energy-PD, so the enlarged class's reach is > 6.63. E80 (running) estimates it.
## Running now (2026-10-19 night, round 9; superseded)
- VM: E80 (src/e80_enlarged_reach.py): SLSQP over autocorrelation profiles with e-PD and window constraints.
- Codex MATH agent, round 9 (.research/agents/tdense9_brief.md; report tdense9_report.md).
## First concrete next step (2026-10-19 night, round 9; superseded)
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


## Session 3, rounds 16–17: all-sets programme, P69–P70 (2026-10-19 evening)
- PRIORITY (user, 2026-10-19): PROVE Chowla. The evidence leans that way. Both tracks stay recorded.
- Cyclic WRS line PAUSED (P69: heavy-core-sumset fake). The new programme works on integer sets directly
  (NOTEBOOK cont. 19, with corrections in items 10–11).
- New tools:
  - spike sub-multiplicativity;
  - ∫log(M + f_A) >= −log 2 (torsion-free);
  - Bhatia–Davis bound for P9 graphs;
  - the trace split;
  - the sharp-boundary Gibbs lemma M >= c₀k − D_d(k) (P70.2);
  - √n w.h.p. for independent roundings of any profile with window variance >~ μ (P70.3).
- E99: near-extremizers have a self-difference-graph edge ≈ −0.72√n. E99b/c: flat random sets get >~ √n from W2 at
  every density; PD-tapered sets at density n^{−1/3} get only ≈ 3.1n^{1/3} from graphs (P70.3 covers them w.h.p.).
- REFUTED this block:
  - the unconditioned bulk-vs-PSD dichotomy (three ways);
  - CLIQUE-S (P70.1, certified clique/K >= 6.73);
  - "C½ is a semicircle edge" (downgraded to an analogy).
- OPEN core: the FOUR-WAY COVER under M = ε√n (P28 spread / star / bulk / sharp boundary). Remaining adversary:
  correlated selected roundings at vanishing density that hide P28 window variance with no sharp ambient boundary.
- First next derivation: decide whether the four joint conditions of P70.5 are INCONSISTENT for small ε, or merely
  an equivalent restatement. Concretely: try to build a correlated rounding with small P28 window variance and
  D_d(k) >~ k at every scale (the tapering heuristic), or prove that low window variance at every scale forces a
  sharp boundary somewhere.

## 2026-10-19 late: circling acknowledged; ROUTES ledger
- Audit: since day 2 (P53), no progress on the core obstruction C* (.research/ROUTES.md). CSFG, WRS, the four-way
  cover, TAPER and PR are all C* restated. Real results since then are on sub-problems (dense C, Bu class,
  obstructions).
- Round 18 STOPPED (TAPER = C*). Its partial report .research/agents/tdense18_report.md is kept unverified.
- New rule: every route gets a ROUTES.md row first (mechanism-level equivalence check) plus a cheap kill test.
- The only route currently claimed NOT to be C*: Fejér–Riesz factor windowing (sign-preserving interior
  localization). Kill test E102 is next.
- (cont. 22) Ledger audit: factor windowing, quadric lift, SR, Kronecker phases, anticoncentration, low-degree
  SOS, tensor renormalization, Mahler/Galois and high-rank ball windows all reduce to C* or to recorded dead ends
  (ROUTES.md). E102 cancelled.
- Round 18 results verified/recorded as P71: periodic triangular Bohr tapers have linear M (transverse packets);
  bounded-occupancy selectors give √n w.h.p.; tapered Singer–Bu (R ≈ 0.77, sparse) is the only sub-1 adversary.
- New fact P71.1 (arc-mass bound), weak. C* unchanged and open.
- (cont. 24) E103: near-Boolean weights buy only constant factors on Singer/Bu (R_{0.3}/R_0 -> 0.70 plateau). With E62
  (phases), no relaxation of Booleanity opens a sub-½ regime. P72 (robust duality, PROVED). P71.2 KERNEL-CHECKED
  (BohrTaper.lean, lead-audited). Helson–Szegő/A_2 and five other candidates killed on paper (NOTEBOOK cont. 24.5,
  ROUTES). Literature spot-check: no news. C* unchanged and open. Evidence leans further toward Chowla TRUE.

## Handoff 2026-10-19 late (cont. 24–25) — read this first
(a) Proved / formalized this block.
- P71.2 KERNEL-CHECKED. Periodic triangular Bohr tapers have M >= 7n/6290 + 1/2 (BohrTaper.lean, lead-audited).
- P72 PROVED. Robust duality M_τ = max_μ Σ(−c_a − τ|c_a|), the flat lemma, and the slope at τ = 0.
- P73 PROVED. Robust few-spike lemma: Boolean S is L²-far from PD φ with φ(0) < 4/3 (Z and T); PR(1) small-peak regime.
  KERNEL-CHECKED (Z version): lean/ChowlaCosine/FewSpike.lean, lead-audited.
(b) Constructions. Nothing new. Relaxations of Booleanity (weights E103, phases E62) buy only constant factors.
  Nothing below ½ anywhere.
(c) Refuted / killed on paper this block (ROUTES rows):
- Herglotz composition counts;
- subordination;
- spectral energy;
- Helson/Cohen idempotent;
- integral Gram lattice;
- Hoffman / vector chromatic number;
- 2-adic Chowla (equivalent by descent);
- Spencer discrepancy (= TAPER);
- Helson–Szegő A_2/BMO (consequence of positivity, satisfied by non-positive random sets).
(d) Evidence. E104: every known near-extremizer is FLAT (λ_half = |{f <= −M/2}| >= 0.2, β2 >= 0.2) at all reachable n.
  The C* regime is empty of examples. The evidence leans to Chowla TRUE; the proof needs a C* tool.
(e) Three active directions.
- (1) Lower bound (C*): the many-spike front core. "1_B + m₀δ₀ ≈ PD forces m₀ >~ √|B|." P73 settles m₀ < 4/3; nothing
  for large m₀.
- (2) PR(1) large-peak case (g(0) >= 4/3). A clean lemma on the architecture's step (d).
- (3) Robust Chowla_τ (Ruzsa's open question). Construction or a polynomial bound.
(f) FIRST concrete next derivation.
- PR(1) large-peak case: if 1̂_Ω(k) >= 0 for |k| <= L and g = P_L1_Ω has g(0) >= 4/3, show U >= cμ.
- Start by testing whether g(0) >= 4/3 with U/μ < 0.1 is possible (SLSQP over unions of arcs, as in E100b, objective
  g(0)). If it is impossible numerically, prove it via Bernstein plus the identity ∫g(1 − g) = U.
- (cont. 25) E105: in the PR(1) large-peak regime (g(0) >= 4/3) the best unresolved fraction found is 0.104–0.157 at
  L = 8, 16, above c* = 0.0947 and growing with the peak. L = 32 is a search failure, not evidence. Next: a paper proof of
  the large-peak case (EXPERIMENTS E105 reading).
