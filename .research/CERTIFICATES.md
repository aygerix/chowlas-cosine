# Certificates

## Method E2 (src/chowla.py: certify_lower_bound)
g(t) = f_A(2 pi t). Grid t_j = j/L (L power of 2 >= 16 max A). FLINT acb.dft (ball arithmetic, prec 96) encloses
g, g', g'', g''' at all grid points. For |s| <= 1/(2L): g(t_j+s) >= cubic Taylor polynomial - S4 (1/(2L))^4/24,
S4 = (2pi)^4 sum a^4. Cubic minimized exactly on the cell (endpoints + stable critical points); ball radii and a
1e-14 relative + 1e-12 absolute float pad subtracted. Output: rigorous lower bound for min f_A (modulo correctness of
FLINT and of the float-padding argument, which is documented inline).
## Method E3 (sturm_certify): exact integer polynomial P(y) = B_den sum T_a(y) + B_num, PARI polsturm on [-1,1].

## Dense-regime sets (2026-10-18) — examples/dense_certified.json
Method E2 (src/chowla.py certify_lower_bound: arb ball DFT of a^0..a^3 weights on 2L-grid, cubic Taylor per cell,
4th-order remainder S4 (π/2L)^4/24, float pads). Best: X30_s1 N=20 max 30, f_A >= −2.68817 for all real x, R <= 0.6011;
X50_s0 N=34 max 49, f_A >= −3.52350, R <= 0.6043. Re-verify: `.venv/bin/python -c "import sys,json;sys.path.insert(0,'src');
from chowla import certify_lower_bound as c;d=json.load(open('examples/dense_certified.json'));print(c(d['X50_s0']['A']))"`.

## C-N36 (2026-10-18): best finite set known to us, R(A) <= 0.564795
A = [1..11, 13..23, 25..31, 34, 35, 37, 44, 45, 48, 50]  (N = 36, max 50; examples/smallN_best.json key "36";
exhaustive optimum of the box [1,52], small-N agent).
Certificate 1 (lead): src/chowla.certify_lower_bound(A, oversample=64): arb ball-arithmetic DFT on L = 4096 points +
  4th-order Taylor remainder 4.3e−7 ⇒ min_x f_A(x) >= −3.3887702 ⇒ M(A) <= 3.3887702, R <= 0.564795.
Certificate 2 (agent): PARI/GP Sturm sequences on Σ T_a(t) + B over t ∈ [−1,1] bracket M(A) ∈ [3.3887696, 3.3887699].
Status: INTERVAL-CERTIFIED finite case (two independent methods). Says nothing about any limit.
Also certified (same method): N=35 (max 48) R <= 0.567674; N=34 (max 48) R <= 0.574135.

## C-SB (2026-10-18): Bu sums on full Singer sets (E25), examples/singer_bu/certified.json (S, shift, N, max, bound)
Method: src/chowla.certify_lower_bound(A, oversample=16) — arb ball DFT of f, f', f'', f''' on L = 2^⌈log2(16 max A)⌉
points + 4th-order Taylor remainder (rigorous lower bound on min over ALL real x). One method only (no Sturm check: degree
~1.9e5 is beyond the exact route); status INTERVAL-CERTIFIED (single method).
   q = 61: N = 3782, max 10707, min f >= −37.1485, R <= 0.60406
   q = 101: N = 10302, max 30575, min f >= −59.7566, R <= 0.58874
   q = 151: N = 22952, R <= 0.57770;  q = 199: N = 39800, R <= 0.56630;  q = 251: N = 63252, max 189688, R <= 0.56272
   q = 307: N = 94556, max 278751, min f >= −171.2117, R <= 0.55679;  q = 401: N = 161202, max 483272, R <= 0.55476
   (q = 307, 401 certified 2026-10-18 on the laptop with chowla.certify_lower_bound_blocked(A, oversample=16, blocks=64):
   same arb-DFT + Taylor certificate computed in 64 decimated residue blocks; validated bit-identical to the unblocked
   certifier on q = 61, 101 and N = 45. q = 401: grid estimate 0.55358, certificate loses 0.0012 to the Taylor remainder
   at oversample 16 — rerun at oversample 32 to tighten.)
   Tightened 2026-10-18 (certify_lower_bound_blocked, oversample 32, 128 blocks, L = 2^24, ~220 s each):
   q = 307: min f >= −171.184725, R <= 0.556699;  q = 401: min f >= −222.292595, **R <= 0.553656** (N = 161202).

## C-N45 (2026-10-18): N = 45, max 61 (E27; examples/milp/N45_best.json)
A = [1..13, 15..35, 37, 39, 40, 41, 45, 50, 52, 57, 58, 60, 61].
Certificate 1: chowla.certify_lower_bound(A, oversample=64) ⇒ min_x f_A >= −3.8360448 (arb ball DFT + Taylor).
Certificate 2: chowla.sturm_certify(A, 38360448, 10^7): PARI/GP Sturm count, Σ T_a(y) + 3.8360448 has no root in [−1,1]
  (True, 0); with 3.8360432 it has 2 roots. Hence M(A) ∈ [3.8360432, 3.8360448], R(A) <= 0.571844.
Status: INTERVAL-CERTIFIED finite case, two independent methods.

## C-N50 (2026-10-18 night): N = 50 structured-class records (E42; examples/construct/N50_certified.json)
A72 = [1..26, 28..40, 43, 44, 47, 49, 50, 52, 54, 60, 68, 69, 72] (max 72).
A68 = [1..18, 20..37, 39..42, 47, 48, 50, 52, 57, 61, 62, 64, 65, 68] (max 68).
Certificate 1: chowla.certify_lower_bound(A, oversample=64):
  - A72: min f >= −4.0309358;
  - A68: min f >= −4.0483108.
Certificate 2: chowla.sturm_certify(A, B, 10^7), PARI/GP 2.15.4 on dirichlet:
  - A72: Σ T_a + 4.0309358 has no root in [−1,1]; with 4.0309354 it has 2 roots.
  - A68: Σ T_a + 4.0483108 has no root in [−1,1]; with 4.0483104 it has 2 roots.
Hence M(A72) ∈ [4.0309354, 4.0309358] and **R <= 0.5700604**; M(A68) ∈ [4.0483104, 4.0483108] and R <= 0.5725176.
Status: INTERVAL-CERTIFIED finite case, two independent methods.
Reproduce with `src/dirun.sh -c 1 python .research/agents/construct_scratch/cert_n50.py`.

## KERNEL-CHECKED: P31 chain and the dense theorem (2026-10-19; Lean agent, lead-audited)
Files: lean/ChowlaCosine/P31/*.lean (2764 lines): WindowMoments, Averaging, Fejer, WindowBound, FejerRiesz, Main,
ElementaryConstant, ElementaryConvolution, AnalyticNikolskii, Corollaries.
Lead audit:
- `lake env lean` on a separate file, using the built .oleans as of 22:05. Every theorem below depends only on
  [propext, Classical.choice, Quot.sound].
- grep finds no sorry / axiom / admit / native_decide in the P31 sources.
Theorems (statements read by the lead):
- `finite_fejerRiesz (L) : FejerRiesz L`. Every real h whose complexification is a trigonometric polynomial of degree
  <= L and which is >= 0 everywhere equals |Σ_{j<=L} u_j e^{ijx}|² for some u ∈ C^{L+1}. This is the FULL finite
  Fejér–Riesz theorem, including zeros on the circle; the local mathlib has no version.
- `elementary_convolution_bound`: v >= 0 on Fin (L+1), Σv² = 1 ⇒ Σ_k (v∗v)_k² <= (811/1000)(L + 1) + 71/300
  (Lemma P31-E). The integral constant is certified by a 32-term geometric expansion with exact tail.
- `elementary_analyticNikolskii`: the same bound for all complex analytic coefficient vectors, as circle means of
  |U|⁴ and |U|².
- `p31_elementary` (Theorem 1 with the elementary constant). For every w, every finite A ⊂ N with all a > 0, and
  every M with ∀ real x, −M <= Σ_{a∈A} cos(ax):
      windowMass w·(|A|/2 + M²) <= ((811/1000)(max A + w + 1) + 71/300)·(M² + windowEnergy w A/2).
- `dense_elementary`. Same hypotheses plus (41/100)·max A <= |A| ⇒ √|A|/1000 <= M. Holds at every finite size (the
  small-X case uses the earlier checked bound M >= ½).
Meaning: Chowla's conjecture is KERNEL-VERIFIED for all sets of density >= 0.41 in [1, max A], with c₀ = 1/1000.
The constants are not optimized; the paper constants are in .research/notes/dense_chowla_P31.md (C3).

## 2026-10-19 (night) Beckner track T5 (Lean, codex agent; lead-audited)
Lead audit:
- `lake build` passes (8739 jobs).
- `lake env lean AxiomCheck.lean` gives 272/272 entries, each depending only on [propext, Classical.choice, Quot.sound].
- 0 sorryAx, and grep finds no sorry/axiom/native_decide in ChowlaCosine/Beckner or ChowlaCosine/P31.
KERNEL-CHECKED:
- `Beckner.young_finite`: Young's convolution inequality on ℝ for complex L^p functions. Every finite admissible triple
  1/p + 1/q = 1 + 1/r, constant 1.
- `young_conjugate`: the L^∞ boundary.
- `young_four_thirds`: L^{4/3} ∗ L^{4/3} ⊂ L², constant 1.
- Gaussian computations: `integral_gaussian_rpow`, `gaussian_convolution`, and exact attainment of 4/(3√3) by Gaussians,
  i.e. the sharpness lower bound.
- M4 infrastructure (51 declarations): heat-flow time/space derivatives, the heat equation for heat-flow
  convolutions, score/moment bounds, the weighted-frame variance identity, and the pointwise frame heat-defect
  nonnegativity (`frame_heat_defect_nonneg`).
NOT done:
- The sharp Young / Beckner upper bound (the global Brascamp–Lieb monotonicity application, the rescaling limits and
  density passage).
- M5 and the sinc P31-N constant.
- Consequently P31-N (Beckner constant 4/(3√3)≈0.76980) is still a paper result. The kernel-checked chain uses P31-E (0.811).
Report: .research/agents/lean_p31_report.md.

## 2026-10-19 (night) P34 + P33 + dilation pinch — KERNEL-CHECKED (codex Lean agent; lead-audited)
Lead audit:
- `lake build` passes (8745 jobs).
- `lake env lean AxiomCheck.lean` gives 321/321 entries, each depending only on [propext, Classical.choice, Quot.sound],
  with 0 sorryAx. 49 entries are new P34-namespace declarations.
- grep finds no sorry/axiom/native_decide in lean/ChowlaCosine/P34.
- Definitions checked: trigSum A b x = Σ_{j∈A} Re(b_j e^{ijx}); energy = Σ‖b_j‖²; windowFreq n = [1, n];
  littlewoodSum n ε x = Σ_{j=0}^n ε_j cos(jx).
Headline statements (exact; lean/ChowlaCosine/P34/):
- `p34_elementary` (Main.lean). For A ⊂ [1, n] positive, ‖b_j‖² <= 1 and ∀x, −M <= trigSum A b x:
  windowMass w·(M² + energy/2) <= elementaryC(n + w)·(M² + (windowMass w − 1)/4).
  `p34_main` is the general version, with explicit Fejér–Riesz/Nikolskii hypotheses.
- `p34_A` (Corollaries.lean). n >= 1, ‖b_j‖² = 1 on [1, n], ∀x, −M <= trigSum ⇒ √n/4 <= M.
- `p34_A_phases` (RealForm.lean). n >= 1, any θ : ℕ → ℝ, ∀x, −M <= Σ_{j=1}^n cos(jx − θ_j) ⇒ √n/4 <= M.
- `p34_B` (Littlewood.lean). n >= 1, ε_j ∈ {−1, 1} ⇒ (∃x, Σ_{j=0}^n ε_j cos jx <= 1 − √n/4) ∧
  (∃x, Σ_{j=0}^n ε_j cos jx >= √n/4 − 1).
- `p34_C` (Corollaries.lean). ‖b_j‖² <= 1, energy >= (41/100)n, ∀x, −M <= trigSum ⇒ √n/1000 <= M.
- `p33_ratio` (Secondary.lean). A nonempty, 1 <= m <= a <= X for all a ∈ A, ∀x, −M <= cosSum A x ⇒ |A|·m/X <= M.
- `dilation_pinch` (Secondary.lean). q >= 1, ∀x, −M <= cosSum A x ⇒ |A|/q − (1 − 1/q)M <= |A ∩ qℕ|.
Report: .research/agents/lean_p34_report.md.

## 2026-10-19 P36 truncation at gaps — KERNEL-CHECKED (codex Lean agent; lead-audited); Beckner M4 partial
Lead audit:
- `lake build` passes (8753 jobs).
- AxiomCheck gives 384/384 entries, all [propext, Classical.choice, Quot.sound], with 0 sorryAx.
- grep finds no sorry/axiom/native_decide in P36/ or Beckner/.
Statements (lean/ChowlaCosine/P36/Main.lean; cosSum A x = Σ_{a∈A} cos(a x)):
- `p36_truncation`. A positive, D >= 1, ∀x, −M <= cosSum A x ⇒
  ∀x, −(M + (1 − cos(π/(D+2)))·Σ_{a∈A, a<=D} a²) <= cosSum (A.filter (· <= D)) x.
  This is the exact sine kernel, with no fallback constant.
- `p36_gap`. Y <= D and no a ∈ A in (Y, D] ⇒ the error is <= (1 − cos(π/(D+2)))·Y²·|A ∩ [1, Y]|.
- `p36_gap_pi`. The same bound with error (π²/2)(Y/(D+2))²·|A ∩ [1, Y]|.
Beckner M4 (partial, NOT the sharp Young theorem):
- `geometricHeatProduct_integral_monotone`: monotone product integral for compact-support positive-mass data.
- `tendsto_sqrt_mul_heatFlow`: scalar large-time Gaussian asymptotic for every signed L¹ datum.
- Remaining: the product large-time limit, the initial-time passage, density, and the 2×2 frame algebra
  (.research/agents/lean_next_report.md).

## 2026-10-19 Geometric Brascamp–Lieb (planar, rank one) — KERNEL-CHECKED (codex Lean agent; lead-audited)
Lead audit: `lake build` passes (8757 jobs); AxiomCheck gives 422/422 standard-axiom entries, 0 sorryAx; no forbidden
tokens in Beckner/.
- `ChowlaCosine.Beckner.geometric_brascamp_lieb` (HeatFlowDensity.lean:211). Hypotheses: E is a real inner-product
  space with an orthonormal basis b : Fin 2; ι finite; f_i >= 0 integrable on ℝ; c_i >= 0; ‖u_i‖ = 1; and the frame
  identity Σ_i c_i⟨u_i, x⟩⟨u_i, y⟩ = ⟨x, y⟩ for all x, y. Conclusion: z ↦ Π_i f_i(⟨u_i, z⟩)^{c_i} is integrable on ℝ²
  and ∫ Π_i f_i(⟨u_i, z⟩)^{c_i} dz <= Π_i (∫ f_i)^{c_i}.
  There are no support, continuity or positive-mass hypotheses. This is the Ball–Barthe geometric Brascamp–Lieb
  inequality in the plane, proved by heat flow: large-time limit, initial-time Fatou passage and L¹ density.
- `youngFrame_isWeightedFrame`, `youngFrameMatrix_det` (= √a√b√d) and `youngFrame_sharp_factor`. These give the
  explicit Young frame for interior exponents and the exact Beckner factor Π A_{p_i}.
- NOT yet: the Lp change-of-variables passage to the sharp Young inequality, M5, P31-N
  (.research/agents/lean_m4_report.md).

## 2026-10-19 Beckner's sharp Young inequality on ℝ — KERNEL-CHECKED (codex Lean agent; lead-audited); M5
Lead audit:
- `lake build` passes (8759 jobs). AxiomCheck gives 447/447 entries, all [propext, Classical.choice, Quot.sound],
  with 0 sorryAx and no forbidden tokens.
- The P31-N drafts lean/ChowlaCosine/P31/FourierL2.lean and SincInterpolation.lean are NOT imported or audited, and
  are left uncommitted (agent stopped mid-task by user request).
Statements (lean/ChowlaCosine/Beckner/YoungSharp.lean, YoungSharpSpecial.lean):
- `sharp_young`. For p, q, r ∈ [1, ∞] (ℝ≥0∞) with 1/p + 1/q = 1 + 1/r and f ∈ L^p(ℝ; ℂ), g ∈ L^q(ℝ; ℂ):
  f ∗ g ∈ L^r and ‖f ∗ g‖_r <= A_p A_q A_{r'} ‖f‖_p ‖g‖_q, with A_p = becknerA p = (p^{1/p}/p'^{1/p'})^{1/2}
  (becknerFactor (1/p)). All endpoints are included.
- `sharp_autocorrelation` (M5). For h ∈ L^{4/3}(ℝ; ℂ), the sharp autocorrelation bound with constant
  A_{4/3}⁴ = 4/(3√3) (`becknerFactor_three_quarters_fourth`). Interval-support corollaries:
  `sharp_interval_selfConvolution`, `sharp_interval_autocorrelation`.
- Proof route: heat-flow geometric Brascamp–Lieb → explicit Young frame → planar change of variables →
  duality/domination.
- Correction found by the agent: the constant previously recorded as "0.7698" is a rounding of 4/(3√3) =
  0.7698003589… and is NOT itself a valid exact upper bound. All records now say 4/(3√3) ≈ 0.76980. The thresholds
  derived from it are unchanged at displayed precision.
