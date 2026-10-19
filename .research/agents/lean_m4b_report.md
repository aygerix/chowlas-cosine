# Lean M4b continuation — 2026-10-19

Status: IN PROGRESS. The live Lean diagnostic server now checks the exact trilinear substitution, complex sharp Young for all finite triples, and the complete extended-exponent theorem (including every infinity endpoint). M4 and M5 now pass the whole-project ordinary build (8759 jobs) and the complete file-based axiom audit (447/447 entries). P31-N remains in progress. Resuming exactly from `lean_m4_report.md`, “First concrete remaining derivation”. The existing unrestricted geometric Brascamp–Lieb theorem, explicit interior Young frame, determinant and Beckner factor are inputs. No completion of sharp Young, M5, or P31-N is claimed yet.

Read `CLAUDE.md`, `lean_m4_brief.md`, `lean_m4_report.md`, `lean_p31_brief.md`, `lean_beckner_brief.md`, and the sinc derivation in `p31_report.md`. Applied the required number-theory research skill. No subagents, commits, or edits to top-level `.research/*.md`.

## Exact derivation in progress

For positive complementary weights `a,b,d` of sum one, set `c=(1-a,1-b,1-d)` and `α=youngFrameScale a b d`. Apply `geometric_brascamp_lieb_youngFrame` to `Fᵢ(s)=gᵢ(αᵢs)^(1/cᵢ)`. The invertible 2×2 map defined by `youngFrameMatrix` has determinant `sqrt(a*b*d)` (in fact the existing statement is the product of square roots). Under this map the three arguments become `x,y,-(x+y)`. Establish integrability and the exact planar substitution, then the one-dimensional substitutions and finite-product cancellation. Proceed to complex Lp convolution, endpoints, M5 and P31-N in that order.

## Verification

Pending this continuation's local build and appended `#print axioms` audit. All claims about new Lean declarations will be recorded only after successful compilation and audit. Allowed axiom set: `propext`, `Classical.choice`, `Quot.sound`. No `sorry`, new axiom, or `native_decide` is permitted.

## M4 derivation now checked in the live diagnostic server

`YoungSharp.lean` contains 16 public theorems. `plane_linear_change` proves the equivalence of integrability under an invertible planar linear map and its exact ordinary-integral Jacobian. `young_trilinear_complement` carries out the specific frame substitution, one-dimensional mass substitutions, and finite-product cancellation with the exact Beckner factor. `young_trilinear_interior` is the unrestricted nonnegative trilinear Lp form.

`sharp_young_normConvolution_interior` tests the actual convolution of norms against its reflected `(r-1)` power. The existing non-sharp theorem supplies Lr membership; a measure-preserving planar shear and Fubini identify the test integral exactly, and `young_power_cancel` handles both positive and zero mass. `sharp_young_finite_interior` then uses complex norm domination. `sharp_young_finite` handles the L1 finite endpoints by the exact identity `becknerFactor c * becknerFactor (1-c) = 1`. `sharp_young_ennreal` treats arbitrary extended exponents, including `r=∞` and the infinity input boundaries, by the already checked conjugate-exponent theorem. `sharp_young` states the constant as `A_p A_q A_{r'}`, with `r'=(1-r⁻¹)⁻¹`, `A₁=A∞=1`.

No support, boundedness, continuity, positivity of norms, or finite-exponent restriction appears in the final `sharp_young` statement. Existing checked proof files are unchanged; only a new module, an appended umbrella import, and appended audit entries were added. The only verified live axiom output requested so far is for the trilinear complement and interior convolution-of-norms results: both list exactly `[propext, Classical.choice, Quot.sound]`. The full file-based audit is pending.

## M5 exact-constant issue

The brief's decimal `0.7698` is a rounded display, strictly below the exact sharp factor `4/(3√3)`. The Gaussian result already in `Gaussian.lean` attains that exact factor, so `0.7698` cannot be used literally as an exact upper bound. The formalization preserves the exact symbolic constant. The live server has checked `becknerFactor (3/4)^4 = 4/(3√3)`; the arbitrary-data autocorrelation and interval-support corollaries are next.

## M4 and M5 checkpoint

The ordinary target build for `YoungSharp.lean` passed (`sharp_build_final.log`, 8722 jobs). The whole-project build has compiled `YoungSharpSpecial.lean` successfully and is still completing the umbrella module. A first ordinary audit was started too early and reported a missing umbrella object file; it will be rerun after the whole build completes. No failed audit is counted as verification.

The complete live audit now prints all 25 new public M4/M5 theorems with exactly `[propext, Classical.choice, Quot.sound]`; evidence: `m4_m5_live_axioms.txt`, `m4_m5_live_diagnostics.json`. `YoungSharpSpecial.lean` checks the exact fourth power of the Beckner factor, the arbitrary complex L4/3 autocorrelation theorem, the exact interval Hölder bound, and both interval-supported self-convolution and autocorrelation bounds. The interval statements are for arbitrary complex L2 data supported in `Icc a b`, and retain the exact length factor `ENNReal.ofReal (b-a)`; no regularity hypothesis is added.

## P31-N in progress

Started `P31/SincInterpolation.lean`. The target remains the unrestricted analytic Nikolskii inequality with constant `β (L+1) (1+2/√(L+1))³`, equivalent to the brief's bound on `ρ_L`. No proof of that target is claimed yet. The immediate lemmas concern the actual finite sinc sum: exact full-circle second-moment orthogonality, concavity for its averaged L4/3 integrand, and explicit left/right inverse-distance envelopes with the exact π factors. They are being checked. The remaining analytic bridge is the exact real-line sinc Plancherel/convolution identity and the subsequent integration/existence passage; none is inserted as an assumption into a purported final P31-N theorem.

## File-based M4/M5 verification — PASSED

- `lake build` in `lean/`: exit zero, 8759 jobs; `m4_m5_build.log`.
- `lake env lean AxiomCheck.lean`: exit zero; `m4_m5_axioms_final.log`. Its parsed summary has 447 expected commands, 447 printed entries, no unexpected axioms, no `sorryAx`, and no Lean errors. Every new M4/M5 theorem is included.
- All 25 new M4/M5 theorems print only `[propext, Classical.choice, Quot.sound]`. M4 and M5 are now kernel-checked under the permitted axioms. This supersedes the earlier diagnostic-only checkpoint.

Headline ordinary outputs:

```text
'ChowlaCosine.Beckner.young_trilinear_complement' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.Beckner.sharp_young' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.Beckner.sharp_autocorrelation' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.Beckner.sharp_interval_selfConvolution' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.Beckner.sharp_interval_autocorrelation' depends on axioms: [propext, Classical.choice, Quot.sound]
```

P31-N uses mathlib's Fourier convention `exp(-2π i t ξ)`, so the exact sinc spectral band is `[-1/2,1/2]`, of length one. This is precisely the brief's `[-π,π]` convention after rescaling frequency by `2π`; the physical cardinal kernel remains `sinc(π t)`. Local mathlib has the L2 Fourier isometry and its agreement with Schwartz functions. I am developing the needed classical L1∩L2 agreement through tempered distributions, rather than assuming the sinc Plancherel identities.
