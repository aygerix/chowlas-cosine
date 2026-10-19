# P31 Lean formalization report

Status: **T1–T4 KERNEL-CHECKED. T5 PARTIAL: M4 is open at the concrete global integral/limit application.** No sharp Young upper bound, M5, or sinc P31-N theorem is claimed.

The requested order was followed: T3 with the analytic constant and an explicitly announced factorization hypothesis; T1 then removed the factorization hypothesis; T2; T4; Beckner M1; the permitted M2 sharp-shortcut skip; M3; M4. Each claimed milestone was checked and audited before advancing. No subagents or external review were used.

## Current target ledger

| Target | Status | Exact checked result |
|---|---|---|
| T3 | KERNEL-CHECKED | `P31.p31_main`; exact window inequality, with only the requested analytic Nikolskii constant hypothesis |
| T1 | KERNEL-CHECKED | `P31.finite_fejerRiesz`, `P31.finite_fejerRiesz_of_coefficients`; every degree, including degenerate and boundary-root cases |
| T2 | KERNEL-CHECKED | `P31.elementary_convolution_bound`; every L≥0, exact 811/1000 and 71/300 constants |
| T4 | KERNEL-CHECKED | `P31.elementary_analyticNikolskii`, `P31.p31_elementary`, `P31.dense_elementary`, and the M≥1/2 fallback |
| T5 M1 | KERNEL-CHECKED | `Beckner.young_finite`: all finite admissible exponent triples, complex Lp(R) functions; also conjugate L∞ output boundary |
| T5 M2 | Optional sharp shortcut SKIPPED | `Beckner.young_four_thirds` is checked with constant one only; no sharp shortcut is claimed |
| T5 M3 | KERNEL-CHECKED computations | Gaussian norms for every finite real p>0, arbitrary positive-width convolution, exact project Gaussian attainment and sharpness lower bound |
| T5 M4 | PARTIAL: 51 audited declarations | Actual pointwise geometric differential inequality, relative bounds, heat equation, and global integral bridge with explicit hypotheses; no sharp upper theorem |
| T5 M5 | NOT STARTED | Held behind M4; no sharp autocorrelation or interval-support theorem |
| T5 sinc P31-N | NOT STARTED | Held behind Beckner; no sharp Nikolskii or improved density threshold claim |

Namespaces below abbreviate `ChowlaCosine.P31` and `ChowlaCosine.Beckner`.

## Scope, assumptions, and rule compliance

Read `CLAUDE.md`, `.research/agents/lean_p31_brief.md`, the P31/P31-N/P31-E proof records and corrections, `.research/agents/p31_report.md`, and the Beckner brief. Applied the number-theory-research skill. The narrower brief controls write scope and the no-commit rule.

- New `sorry`: **0**. New `axiom` declarations: **0**. `native_decide`: **0**. Unchecked external solvers: **0**. No `sorryAx` in successful audits.
- Every theorem called KERNEL-CHECKED has an axiom audit with no assumptions beyond `propext`, `Classical.choice`, `Quot.sound`.
- All-real hypotheses remain all-real. Original frequencies remain a genuine positive `Finset ℕ`; no multisets replace the set in a theorem about A. Root multisets are used only internally for FTA.
- Builds and proof-producing exact arithmetic were local. No numerical searches, remote numerics, or VM access were used; fejer was not touched.
- This agent made no commits and changed only the allowed new proof directories, scratch/report, and append-only aggregate import/axiom files. Unrelated pre-existing/shared workspace changes were left alone.
- `FejerRiesz`, `AnalyticNikolskii`, `YoungFinite`, and `IsWeightedFrame` are proposition definitions, not axioms. `finite_fejerRiesz` and `young_finite` prove their respective universal propositions. Frame existence is a hypothesis only in the explicitly conditional M4 reductions.

## T3 and T1: exact statements and proof contents

`p31_main` takes positive finite A, `X=A.sup id`, the actual bound `∀x:ℝ, −M≤cosSum A x`, natural window w, and `AnalyticNikolskii (X+w) C`. It proves

`W * (n/2 + M²) ≤ C * (M² + S_A/2)`.

Here the mean is `(2*pi)^(-1)∫_0^(2*pi)`, `κ(k)=max(0,1−k/(w+1))` on positive frequencies, `S_A=Σ_(a∈A)κ(a)²`, and `W=1+2Σ_(1≤k≤w)κ(k)²`. The theorem even permits w=0, so the requested w≥1 loses no cases. It uses no factorization hypothesis in its final form. The initial conditional T3 checkpoint had an announced `FejerRiesz` hypothesis; T1 discharges it internally in `Main.lean`.

Checked window ingredients include weighted orthogonality, exact shifted-window moments, Fejér nonnegativity for every real angle from a finite sum of two squares, exact `W=2(w+1)/3+1/(3(w+1))`, degree control, translation/reflection invariance, and Fubini on the whole square. There is no measurable factor-selection assumption: the scalar inequality is applied to each window, and its factor disappears before integration.

`finite_fejerRiesz_of_coefficients` takes a real h identified at every real x with its complex Fourier sum over integer frequencies `[-L,L]`, plus all-real nonnegativity. It returns `u : Fin(L+1)→ℂ` with the exact all-real identity `h(x)=|Σ_j u_j exp(i*j*x)|²`. It covers L=0, identically zero h, vanishing top coefficients, padding roots at zero, and unit-circle roots.

The proof converts finite-band membership to a shifted polynomial, proves padded conjugate-reflection symmetry by polynomial uniqueness on an infinite circle arc, trims padding to the actual degree, uses FTA and reciprocal-conjugate root symmetry, and proves even unit-circle multiplicity from a local real sign argument and the nonzero divided slope of exp(ix). A root-multiset partition halves fixed multiplicities, assembles a norm-square factor, fixes its scalar by nonnegativity, and extracts/pads coefficients.

Files: `WindowMoments.lean`, `Averaging.lean`, `Fejer.lean`, `WindowBound.lean`, `FejerRiesz.lean`, `Main.lean`.

## T2: elementary convolution constant

`elementary_convolution_bound` states the exact requested bound for every natural L and nonnegative `v : Fin(L+1)→ℝ` with `Σv_j²=1`:

`Σ_(k<2(L+1)−1) (Σ_(i+j=k) v_i v_j)² ≤ (811/1000)(L+1)+71/300`.

`discreteEnergy_eq_convolution` proves equality with the additive-relation quartic energy. E1 follows from quartic AM–GM, exact overlap counts, and the cumulative-mass cut identity. E2 follows from unique relation fibers and AM–GM. The variational argument proves the positive-cell-weight inequality and the exact trapezoid integral, including repeated cumulative masses. Weighted Cauchy–Schwarz then uses the integral certificate.

The certificate proves `(1−71/100)∫_0^1 1/D(A) dA≤1`, where `D(A)=811/1000−(71/100)(1−2A(1−A))`. With t=2A−1 and r=355/456, a 32-term geometric expansion plus the exact tail `r^32*t^64/(1−r)` reduces the estimate to rational arithmetic and exact even moments `1/(2m+1)`. `norm_num` produces kernel-checkable proofs; no numerical quadrature is trusted.

Files: `ElementaryConstant.lean`, `ElementaryConvolution.lean`.

## T4: unconditional elementary transfer and dense theorem

`elementary_analyticNikolskii` proves the analytic complex-coefficient estimate for every degree with `C_L=(811/1000)(L+1)+71/300`. It includes exact second moments, a fourth-moment comparison to the real nonnegative coefficient energy, quartic homogeneity, normalization, and the zero-vector branch. `p31_elementary` discharges the C hypothesis using this theorem.

`dense_elementary` proves at **every finite size**:

`(41/100)*(A.sup id : ℝ) ≤ A.card  ⇒  sqrt(A.card)/1000 ≤ M`.

The positive-frequency set and all-real lower-bound hypotheses are explicit. The empty set is handled. For nonempty A, `half_le_of_nonempty` proves M≥1/2 from the existing singleton star bound.

The large-X argument takes `w=⌊X/200⌋`, X≥2000, and proves `W≥X/300`, `C≤(102/125)X`, `2S_A≤W−1`, and `n−C/2≥n/500`. Thus the explicit parameters include window fraction 1/200, relative margin 1/500, threshold X0=2000, and squared lower constant 1/10^6. The small-X branch uses `n≤X` and M≥1/2. There is no unspecified epsilon, asymptotic restriction, or omitted finite-size case.

Files: `AnalyticNikolskii.lean`, `Corollaries.lean`.

## T5 checked milestones and exact limits

### M1 and the M2 decision

`young_finite : YoungFinite` proves non-sharp Young with constant one for real p,q,r≥1 satisfying `1/p+1/q=1+1/r`, with arbitrary complex-valued Lp and Lq functions on R. It proves both MemLp membership of the convolution and the actual eLpNorm bound. M1 is complete in the finite-exponent form explicitly permitted by the brief. `young_conjugate` also proves the conjugate-exponent L∞ output boundary, with ENNReal exponents.

The r>1 proof uses the three weights `1/r`, `1−1/q`, `1−1/p`; the zero-weight p=1/q=1 boundaries are handled exactly. Tonelli and translation invariance integrate the powered bound; domination handles complex Bochner convolution. The r=1 branch proves p=q=1 and uses the checked L1 endpoint. No boundedness or compact-support restriction is inserted.

M2's optional shortcut to the *sharp* project case was skipped, as permitted. `young_four_thirds` is a checked auxiliary constant-one specialization, not a sharp-factor theorem.

Files: `Young.lean`, `YoungSpecial.lean`.

### M3 Gaussian computations

For `gaussian a x=exp(−a*x²)`, a>0, `eLpNorm_complexGaussian` proves `‖gaussian a‖_p=(sqrt(pi/(p*a)))^(1/p)` for every finite real p>0, and `memLp_complexGaussian` proves membership. `gaussian_convolution` and `complexGaussian_convolution` prove the all-real formula

`gaussian a * gaussian b (x)=sqrt(pi/(a+b))*gaussian (a*b/(a+b)) x`.

`eLpNorm_complexGaussian_convolution` gives the norm of that convolution for every finite r>0. `gaussian_attains_project_constant` proves the exact squared equality at p=q=4/3,r=2 with `sharpBeta=4/(3*sqrt 3)`. `project_constant_lower_bound` proves every universal squared self-convolution constant is at least beta. These are Gaussian sharpness/attainment results at the project exponents, independent of the still-unproved sharp upper inequality.

No separately formalized general-exponent extremizer algebra identity or Gaussian infinity-norm formula is claimed. Nonzero Gaussian extremizers concern the interior cases; endpoints such as L1×Lq→Lq, q>1, instead have the usual concentration limit.

The literal decimal 0.7698 is below beta and cannot replace beta in a universal squared Young theorem; the code uses the exact expression. Indeed `3*11547²=399999627<400000000` gives `sqrt 3<20000/11547`, hence beta>3849/5000. This last integer explanation is a paper clarification; the formal sharpness theorem uses exact beta directly.

File: `Gaussian.lean`.

### M4 checked foundation and remaining proof block

There are **51 audited M4 declarations** across four files. The first 31 prove frame variance; heat-kernel probability normalization, semigroup, and scalar derivatives; heat-flow positivity/mass/tail bounds; Gaussian product bounds; dominated smoothing for every real L1 datum; and `heatFlow_heat_equation` with the actual derivative operators.

The subsequent 20 declarations close further analytic steps:

- `heatFlow_space_score_bound` and `heatFlow_time_score_bound` prove the relative first and second/time derivative estimates for explicitly interval-supported nonnegative L1 data with positive mass. In particular, the first score is at most `(|x|+R)/(2t)` in absolute value; the second/time score is at most `(|x|+R)^2/(4t^2)+1/(2t)`.
- `hasDerivAt_weighted_product` and `hasDerivAt_weighted_product_slope` prove the actual first/second calculus formulas for arbitrary finite positive weighted products, on genuine real neighborhoods.
- `frame_laplacian_identity` identifies their directional Laplacian algebra using an orthonormal basis.
- `hasDerivAt_geometricHeatProduct_time`, `geometricHeatPath_second_derivative`, and `geometricHeat_defect_nonneg` prove the **actual pointwise geometric heat-flow differential inequality**, for arbitrary nonnegative L1 factors of positive mass, unit vectors, and a nonnegative weighted frame. This is not merely a hypothetical numerical variance formula. With `P_t(x)=Π heatFlow(f_i,t,<u_i,x>)^c_i`, the checked conclusion is `0 ≤ ∂tP_t(x)−Σ_j ∂²_(b_j)P_t(x)` at every positive t and every x.
- `integral_partial_x_eq_zero` and `integral_partial_y_eq_zero` prove whole-plane integration by parts when the stated first and second partial derivatives are jointly integrable. Fubini and the real-line FTC justify zero integral; no boundary limit is assumed silently.
- `parabolic_integral_derivative_nonneg` combines dominated differentiation, those integration-by-parts results, and a pointwise parabolic inequality into a nonnegative derivative of a whole-plane integral. **Its measurability, local uniform domination, and joint-integrability hypotheses are explicit.**

The current concrete application block is **discharging those global analytic hypotheses for the geometric product**, then proving its rescaled large-time limit and density passage. Individual relative score and Gaussian-tail bounds are checked, and the generic global bridge is checked, but the concrete assembly of their uniform bounds, joint measurability/integrability in planar coordinates, and the resulting monotonicity theorem for the actual geometric-product integral is not yet kernel-checked. `monotone_of_heat_defect_identity` also remains an explicitly conditional reduction; it must not be read as that missing concrete theorem.

No lack of an existing named Young theorem was treated as an axiom or as completion. The work proceeded through scalar smoothing, relative estimates, positive-product calculus, the actual pointwise inequality, and the generic unbounded-domain integration bridge. The remaining precise obligations are:

1. Apply `parabolic_integral_derivative_nonneg` to the geometric product in R², proving its local uniform Gaussian-polynomial domination and the joint integrability of its first/second spatial derivatives in those coordinates.
2. Prove the concrete monotone integral's large-time rescaling limit and the initial-time Fatou/approximate-identity passage.
3. Prove the nonnegative compact-data approximation and ae pullback under nonzero linear functionals, so no support restriction survives.
4. Formalize the explicit 2×2 geometric frame construction, sharp-factor algebra, Lp cancellation, and endpoint constants.

The next concrete derivation is obligation 1: combine the checked score bounds uniformly on `[t0/2,2t0]` with `frame_product_gaussian_bound`, obtain an integrable envelope `C(1+x²+y²)exp(−a(x²+y²))`, and instantiate the checked global bridge. This is a proof gap in the current formal development, not a claimed counterexample or impossibility result.

M4 is incomplete. M5 and sinc P31-N were not advanced past this dependency. This is a partial T5 deliverable, as the brief allows; neither sharp Young nor the threshold for every delta>2/(3*sqrt 3) is claimed.

Files: `HeatFlow.lean`, `HeatFlowDerivative.lean`, `HeatFlowRelative.lean`, `GeometricHeat.lean`.

### Quantitative next lemma (paper derivation, not kernel-checked)

For common support radius R and times `0<a≤t≤b`, put

`K_i = m_i * exp(R²/(4a)) / sqrt(4*pi*a)`, `K=Π K_i^{c_i}`.

The checked heat-tail estimate and elementary monotonicity in t imply

`P_t(x) ≤ K*exp(−|x|²/(8b))`.

Write `B1(x)=(|x|+R)/(2a)` and `B2(x)=(|x|+R)²/(4a²)+1/(2a)`. The checked score and product derivative formulas give

`|∂tP_t(x)| ≤ P_t(x)*(Σc_i)*B2(x)`,

`|∂_(b_j)P_t(x)| ≤ P_t(x)*(Σc_i|<u_i,b_j>|)*B1(x)`,

`|∂²_(b_j)P_t(x)| ≤ P_t(x)*[(Σc_i|<u_i,b_j>|)^2*B1(x)^2 + (Σc_i<u_i,b_j>²)*(B2(x)+B1(x)^2)]`.

Unit vectors make every coefficient finite and independent of t,x. Thus these are bounded by explicit constant multiples of `(1+|x|²)exp(−|x|²/(8b))`. In planar coordinates this is integrable by Fubini and one-dimensional Gaussian moments. Joint continuity of the flow and moment functions on positive time can be proved by dominated continuity under their defining integrals, using the already checked global kernel envelopes times `|f_i|`. This supplies the missing measurability. These estimates specify the concrete input proofs still needed for `parabolic_integral_derivative_nonneg`; they have not been silently supplied to that theorem.

## Strategic review and handoff

The elementary route is closed through T4; it no longer waits on sharp Young. The sharp route has moved from a named outside theorem to checked non-sharp Young, Gaussian attainment, scalar/relative heat estimates, and an actual pointwise geometric heat inequality. A second, independent global integration component is also checked with explicit hypotheses.

The remaining work is an application/limit/density layer, not a numerical constant problem. Preserve the elementary theorems and continue the heat route at the concrete global bridge. Do not restart root pairing, re-optimize 0.811, substitute an L1 endpoint for sharp Young, or declare the pointwise heat inequality sufficient for the integrated theorem. The exact next derivation and outstanding dependencies are listed above. M5/P31-N should remain behind that dependency, in the requested order.

## Verification evidence

Lean: `leanprover/lean4:v4.33.1`. Mathlib pinned revision: `0df444a360eaa60ab8c11dca51a86af692955474`.

Ordinary builds passed at the T1/T3 split (8728 jobs), T2 split (8730), T4 split (8732), M1 (8733), M3 (8735), and the first M4 foundation split (8737). The final ordinary build including the relative/geometric continuation passed (8739 jobs, exit zero). The final whole-project `lake env lean AxiomCheck.lean` audit also exited zero: all **272 axiom audit entries** were printed, with no axioms outside `propext`, `Classical.choice`, `Quot.sound`, and no `sorryAx` or Lean errors. The final source manifest matches every delivered proof module.

Audit artifacts under `lean_p31_scratch/`:

| Artifact | Evidence |
|---|---|
| `conditional_t3_live_axioms.txt` | Initial explicitly conditional T3 chain |
| `t1_t3_live_axioms.txt`, `t1_t3_file_axioms.log` | Full factorization and exact T3; 48 declarations in the separate file audit |
| `t2_live_axioms.txt` | 13 principal T2 declarations |
| `t1_t2_t3_axioms.log` | Earlier whole AxiomCheck run, exit zero, 176 axiom entries, no sorryAx |
| `t4_live_axioms.txt` | 11 T4/complex-transfer declarations |
| `beckner_m1_file_axioms.log` | 13 M1 declarations; ordinary file-based audit, exit zero |
| `beckner_m2_live_axioms.txt` | Constant-one project specialization |
| `beckner_m3_live_axioms.txt` | 13 Gaussian declarations |
| `beckner_m4_live_axioms.txt` | Initial 31 M4 foundation declarations |
| `beckner_relative_geometric_live_axioms.txt` | Further 20 M4 relative, geometric, and integration declarations |
| `t1_t4_m1_build.log`, `t1_t4_m3_build.log` | Successful ordinary builds through M1 and M3 |
| `final_build.log` | Successful first M4 foundation build, 8737 jobs |
| `final_full_build.log` | Successful final build with the complete partial-M4 continuation, 8739 jobs |
| `final_axioms.log`, `final_axioms.summary.json` | Final whole-project audit, exit zero; 272/272 entries, only allowed axioms, no errors/sorryAx |
| `final_source_manifest.json` | SHA-256/line-count/hole-token record for all 17 proof modules |

The persistent Lean server was used for incremental elaboration and `#print axioms`, followed by ordinary Lake builds of the actual organized files. A saved complete checked source is `beckner_m1_m4_checked_combined.lean`; it is a checkpoint, not an additional trusted tool. The source manifest records 17 proof modules and 4350 lines, with zero sorry tokens, axiom declarations, or native_decide tokens. Some harmless linter warnings remain. No theorem relies on the Python diagnostic runner's correctness: the proofs are checked by Lean, and ordinary file builds/audits verify the delivered modules.

## M4 paper proof before formalization: geometric heat flow

Status of this section: PAPER DERIVATION, NOT KERNEL-CHECKED. It specifies the analytic obligations rather than using them as axioms.

1. **Geometric datum.** Let finitely many unit vectors `u_i ∈ R^d`, weights `0<c_i≤1`, satisfy `Σ c_i u_i u_iᵀ=I`. Tracing gives `Σc_i=d`. For every real score vector `v`,
   `|Σ c_i u_i v_i|² ≤ Σ c_i v_i²`.
   To see this, put `V=Σc_i u_i v_i`, expand `Σc_i(v_i−u_i·V)²`, and use the frame identity to obtain exactly `Σc_i v_i²−|V|²`.

2. **Heat flow and bounds.** Start with nonnegative continuous compactly supported `F_i`, with masses `m_i>0`, and a common support bound `[-R,R]`. Put
   `H_t(s)=(4*pi*t)^(-1/2) exp(-s²/(4t))`,
   `F_i(t,s)=∫ H_t(s−y)F_i(y)dy`, for `t>0`.
   Then `F_i(t,s)>0`, `∂t F_i=∂ss F_i`, and its mass is `m_i`. For any compact positive time interval `[t0,t1]`, completion of the square gives a Gaussian upper bound `F_i(t,s)≤C exp(-s²/(8t1))`.
   The probability measure with density proportional to `exp(s*y/(2t)−y²/(4t))F_i(y)` is supported on `[-R,R]`. Consequently
   `v_i=∂s log F_i=−s/(2t)+E[y]/(2t)`,
   `∂s v_i=−1/(2t)+Var(y)/(4t²)`.
   Thus `|v_i|≤(|s|+R)/(2t0)` and `|∂s v_i|≤1/(2t0)+R²/t0²`. These are the explicit bounds needed for differentiating and integrating, including where the initial functions vanish.

3. **Pointwise monotonicity identity.** Let `P_t(x)=Π F_i(t,u_i·x)^{c_i}` and `V=Σc_i u_i v_i(t,u_i·x)`. Differentiation gives
   `∂t P_t = ΔP_t + P_t(Σc_i v_i²−|V|²)`.
   The bracket is nonnegative by step 1. Step 2 and the frame identity bound `P_t`, `∂tP_t`, and `ΔP_t` by `C(1+|x|²)exp(-|x|²/(8t1))`. The same bounds control the first derivatives and their boundary limits. Hence dominated differentiation is valid, Fubini and one-dimensional integration by parts give `∫ΔP_t=0`, and `Φ(t)=∫P_t` is nondecreasing.

4. **Large-time limit.** Rescale `x=sqrt(t)z`. Since `Σc_i=d`, all powers of t cancel. The rescaled heat convolutions tend pointwise to `m_i exp(-(u_i·z)²/4)`. For t≥1, `(u_i·z−y/sqrt(t))²≥(u_i·z)²/2−R²` gives a product bound `C exp(-|z|²/8)`. Dominated convergence and the frame identity yield
   `lim Φ(t)=Πm_i^{c_i}`,
   because the normalized d-dimensional Gaussian integrates to one (in d=2, use Fubini and the checked one-dimensional Gaussian integral).

5. **Initial-time limit and geometric BL.** The heat approximate identity converges pointwise to each continuous initial F_i. Fatou therefore gives `∫ΠF_i(u_i·x)^{c_i}≤liminf_(t↓0)Φ(t)≤Πm_i^{c_i}`. Zero-mass nonnegative initial data vanish ae and are treated separately.

6. **Density with no silent support restriction.** For arbitrary nonnegative L1 data choose nonnegative continuous compactly supported approximations converging in L1, then pass to a common ae-convergent subsequence. Pullback by each nonzero linear functional is ae preserving from Lebesgue measure on R^d to that on R (orthogonal coordinates plus Fubini, applied on countably many bounded boxes). Fatou and convergence of the masses extend geometric BL to all nonnegative L1 data. This step is required; a theorem only for smooth or compactly supported data would not finish M4.

7. **Explicit passage to the sharp Young constant.** For interior finite Young exponents set `c=(1/p,1/q,1/r')`, so `Σc_i=2` and `0<c_i<1`. On R² use linear forms `l_1(y,z)=y`, `l_2(y,z)=z`, `l_3(y,z)=y+z`, and let `a_i=1/(c_i(1−c_i))`. Set `H=Σc_i a_i l_i l_iᵀ`, choose `B=H^{-1/2}`, and put `u_i=sqrt(a_i)Bᵀl_i`. Direct 2×2 algebra, using `Σc_i=2`, gives `det H=1/Π(1−c_i)` and `a_i l_iᵀH^{-1}l_i=1`; thus the vectors are unit and form a geometric frame. Changing variables by B and applying step 6 gives the trilinear constant
   `(det H)^(-1/2) Πa_i^(c_i/2) = Π[(1−c_i)^(1−c_i)/c_i^c_i]^(1/2) = A_p A_q A_{r'}`.
   Apply this to `F_1=|f|^p`, `F_2=|g|^q`, `F_3=h^{r'}`. For the nonnegative convolution K, M1 already gives K∈Lr. Choose `h=K^(r−1)`; cancel its finite norm, treating K=0 separately. Complex convolution follows by domination by convolution of norms. Endpoint admissible triples have sharp factor one and follow from M1 or the checked conjugate-exponent boundary; the constants must be proved to reduce to one rather than inferred by continuity.

**Original formalization plan, recorded before the M4 files.** First prove the finite-frame sum-of-squares identity, normalize the real heat kernel and check its Gaussian convolution semigroup and scalar heat equation. Then prove step 2's score bounds and product domination, step 3's differentiation/integration bridge, step 4's rescaling limit, step 5's approximate-identity passage, step 6's density/pullback, and finally the 2×2 change of variables and Lp cancellation. None of these missing analytic steps is declared an axiom. A Gaussian formula alone, or the nonnegative variance identity alone, will not be reported as sharp Young.

The relative derivative bounds, positive-product calculus, pointwise geometric inequality, and generic integral bridge were subsequently completed and audited as detailed in the current M4 section above.
