# Lean M4 report — 2026-10-19

Status: brief items 1–3 kernel-checked through unrestricted planar geometric Brascamp–Lieb; item 4 partially kernel-checked through the explicit general interior frame, its determinant, its exact linear dependence, and its Beckner-factor identity. The final whole-project `lake build` passed (8757 jobs). The ordinary file-based axiom audit passed all 422/422 expected entries, including every one of the 38 new public theorems. Only `propext`, `Classical.choice`, and `Quot.sound` occur. M4, M5 and P31-N are not complete. Read `CLAUDE.md`, `lean_m4_brief.md`, `lean_next_report.md`, and the original P31/Beckner briefs. Loaded the required number-theory research skill. No subagents or commits. Only this designated report was edited among research Markdown files.

## Exact target and starting point

The existing kernel-checked compact-data monotonicity and scalar large-time rescaling are inputs, not a completed sharp Young theorem. Work proceeds in the brief's order: whole-plane product large-time limit; initial-time passage; density and null-set pullback; explicit sharp Young frame and constants; M5; P31-N.

First derivation: trace the weighted-frame identity in an orthonormal basis of dimension two to obtain `sum c = 2`, retain the exact finite-product normalization, prove an integrable rescaled Gaussian envelope, perform the planar dilation change of variables, and evaluate the limiting Gaussian integral. Compact support and positive mass remain intermediate hypotheses wherever explicitly present; they are not claimed for the final unrestricted theorem.

## Verification

The initial whole-project `lake build` passed (8753 jobs). The ordinary build through `HeatFlowInitial.lean` passed (8719 jobs), and the final ordinary build through `HeatFlowDensity.lean`, including the subsequent compact-support corollary, passed (8720 jobs). The first density build used an earlier source revision with an unavailable arithmetic lemma; this was corrected before the successful final density build. Evidence: `lean_m4_scratch/limits_build.log`, `density_final_build.log`.

`HeatFlowProductLimit.lean` now proves the exact large-time limit of the actual full-plane geometric heat-product integral, in square-time and original-time variables, under interval-supported nonnegative L1 data. Zero masses are allowed for this limit. Its 13 public results include the general finite-dimensional frame trace, exact finite-product rescaling, uniform rescaled scalar Gaussian envelope, whole-plane Gaussian integral, planar dilation formula, exact limiting mass product, and the positive-time mass upper bound obtained from the existing monotonicity theorem. The last upper bound still assumes positive initial masses, as does the existing monotonicity input.

`HeatFlowInitial.lean` proves the exact small-time convolution rescaling, approximate-identity convergence at continuity points of bounded measurable data, a general nonnegative Fatou lemma including integrability of the limit, product convergence for bounded continuous data, and geometric Brascamp–Lieb for bounded continuous interval-supported nonnegative L1 data of positive mass. This closes the initial-time passage for this intermediate class, not for arbitrary L1 data.

The initial 18 public declarations have live `#print axioms` entries in `lean_m4_scratch/limits_live_axioms.txt` and `limits_live_diagnostics.json`. The complete 38-entry live audit is in `final_live_axioms.txt` and `final_live_diagnostics.json`. Every entry contains only `[propext, Classical.choice, Quot.sound]`. All four new modules are appended to `lean/ChowlaCosine.lean`, and every public theorem is audited in the appended sections of `lean/AxiomCheck.lean`. The four modules contain 936 lines, with zero proof-hole tokens, new axiom declarations, or `native_decide` tokens. `git diff --check -- lean` passed.

## Remaining exact gaps

M4 is not complete. Items 1–3 of the M4 brief are checked through the unrestricted geometric inequality. The explicit frame, determinant and exact Beckner-factor algebra in item 4 are also checked. Remaining: apply the planar linear change of variables to the actual trilinear integral, cancel the Lp powers and masses, obtain the complex convolution Lp inequality by duality/domination, and verify endpoint constants. Then proceed to M5 and P31-N in the brief's order. No sharp Young, M5, or P31-N completion is claimed.

## Density derivation — checked

`HeatFlowDensity.lean` is checked, with all eight public theorems audited in the live diagnostic session. `geometric_brascamp_lieb` proves geometric Brascamp–Lieb for every finite family of nonnegative real L1 data, every nonnegative weighted frame of unit vectors, and any two-vector orthonormal basis. It asserts integrability of the actual whole-plane product as well as the mass-product upper bound; no support, continuity, boundedness, or positive-mass assumption appears in that statement. All 27 new entries (13 large-time, six initial-time/compact-data, eight density/general-data) print only `[propext, Classical.choice, Quot.sound]`. Evidence: `lean_m4_scratch/density_live_axioms.txt` and `density_live_diagnostics.json`.

The derivation is as follows. A continuous tent `max(1-|x|,0)` has compact support and strictly positive finite mass. For an L1 approximant `g` to a nonnegative datum `f`, taking `|g|` does not increase the L1 error. Adding `δ` times the tent makes the approximant's mass strictly positive with arbitrarily small extra L1 error, even when the target mass is zero. L1 convergence gives convergence in measure and hence an almost-everywhere convergent subsequence; its masses converge by continuity of the L1 integral. For a nonzero planar linear form, a measurable null hull and one-dimensional translation/dilation invariance allow Fubini to pull back any almost-everywhere statement. The two coefficient cases are handled separately, including a vanishing coordinate coefficient. The unit-vector hypothesis ensures the frame's linear forms are nonzero. A finite intersection gives almost-everywhere convergence of the products, while nonnegative real-power continuity includes zero masses and zero weights. The compact-data bound applies to each approximant with a common finite support radius for that finite family. Fatou, with the converging mass-product upper bounds, proves integrability and the unrestricted geometric bound.

## Explicit interior Young frame and factor — checked

`YoungFrame.lean` has 11 checked public theorems. For arbitrary positive `a,b,d` with `a+b+d=1`, its weights are `c=(b+d,a+d,a+b)=(1-a,1-b,1-d)`. In the given orthonormal basis the three unit vectors have coordinates

```
u0 = (sqrt b, sqrt a * sqrt d) / (sqrt(a+b) * sqrt(b+d))
u1 = (-sqrt a, sqrt b * sqrt d) / (sqrt(a+b) * sqrt(a+d))
u2 = (0,-1).
```

The three entries of the weighted symmetric 2×2 matrix are proved to be `(1,1,0)`, and `youngFrame_isWeightedFrame` proves the full bilinear identity for every pair of vectors in the whole ambient space. `youngFrame_unit` supplies all three unit norms. `geometric_brascamp_lieb_youngFrame` applies the unrestricted theorem to this actual frame.

Put `alpha=(sqrt a*sqrt(b+d), sqrt b*sqrt(a+d), sqrt d*sqrt(a+b))`. The checked vector identity is `sum alpha_i • u_i = 0`. The actual 2×2 matrix taking frame coordinates to the first two scaled forms has determinant exactly `sqrt a*sqrt b*sqrt d > 0` (`youngFrameMatrix_det`). For the complementary weights `d_i=(a,b,d)`, `youngFrame_sharp_factor` proves exactly

```
det(matrix) / product_i alpha_i ^ c_i
  = product_i sqrt ((1/c_i)^c_i / (1/d_i)^d_i).
```

Since `p_i=1/c_i` and `p_i'=1/d_i`, each factor is exactly `A_{p_i}`. This is an identity of the intended sharp constant for all interior triples, not a numerical approximation or only the project exponent. It does not itself assert the remaining Lp inequality or endpoint cases.

## First concrete remaining derivation

For nonnegative trilinear data `g_i`, apply the checked frame theorem to `F_i(s)=g_i(alpha_i*s)^(1/c_i)`. Use `youngFrame_relation` to identify the third physical argument as `-(x+y)`, and use `youngFrameMatrix_det` for the planar Jacobian. Prove integrability of the physical product and the exact change-of-variables identity before rewriting its integral. Then one-dimensional dilation gives `integral F_i = alpha_i^(-1) * integral g_i^(1/c_i)`, and the checked `youngFrame_sharp_factor` supplies the exact constant. This analytic substitution/Lp passage is not yet checked.

Useful local APIs already located for that next derivation: `Basis.finTwoProd`, `Matrix.toLin_finTwoProd_apply`, `Measure.map_linearMap_addHaar_eq_smul_addHaar`, `Measure.LinearMap.quasiMeasurePreserving`, and `Measure.integral_comp_mul_left`. No mathematical claim from these APIs has been substituted for the missing Lean proof. The existing M1 bounds can supply endpoint/duality integrability, but their sharp-factor specialization still needs checking.

## Final verification — passed

- `lake build` in `lean/`: exit zero, 8757 jobs. All four new modules and the umbrella import compiled. Transcript: `lean_m4_scratch/final_build.log`.
- `lake env lean AxiomCheck.lean` in `lean/`: exit zero. The complete transcript has 422/422 expected audit entries, no Lean errors, no `sorryAx`, and no axioms outside the allowlist. Every one of the 38 new public theorems is present. Transcripts: `final_axioms.log`, `final_axioms.summary.json`, `headline_axioms.txt`.
- Source audit: four new proof modules, 936 lines, 38/38 public theorems covered by appended audit commands, zero forbidden tokens. SHA-256 hashes match the sources checked by the final build and audit. Manifest: `final_source_manifest.json`.
- `git diff --check -- lean`: passed. Existing kernel-checked proof modules were not modified; only the four new modules and appended imports/audit commands were added. Some harmless linter warnings remain.
- The persistent Lean diagnostic server was stopped after saving the checked checkpoint. There is no background proof work, no commit, and no subagent.

Headline ordinary `#print axioms` output:

```text
'ChowlaCosine.Beckner.tendsto_integral_geometricHeatProduct' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.Beckner.geometric_brascamp_lieb' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.Beckner.youngFrameMatrix_det' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.Beckner.youngFrame_sharp_factor' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.Beckner.geometric_brascamp_lieb_youngFrame' depends on axioms: [propext, Classical.choice, Quot.sound]
```
