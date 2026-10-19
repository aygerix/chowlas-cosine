# Lean next-slot report — 2026-10-19

Status: P36 complete; M4 concrete integral monotonicity and scalar rescaling checked. The whole-project build and ordinary axiom audit both passed. Targets 2/3 were skipped as requested. No subagents or commits. This is the only research Markdown document edited.

## Target 1: P36 — exact requested constant

`ChowlaCosine.P36.p36_truncation` proves, with A a genuine `Finset ℕ`, explicit positive-frequency and D≥1 hypotheses, and every real x,

`-(M + (1-cos(pi/(D+2))) * sum_{a in A, a≤D} a²) ≤ cosSum (A.filter (·≤D)) x`.

The proof uses the exact sine-vector square-modulus kernel. It proves the mass is positive, normalizes the mean to one, obtains first coefficient `cos(pi/(D+2))` from the finite sine recurrence including both boundary terms, proves exact vanishing above degree D, and computes translated-cosine convolution. The all-real inequality `1-cos(a*x) ≤ a²*(1-cos x)` yields the positive-definite increment bound. No fallback constant, grid, or weakened quantifier is used.

Also proved:

- `p36_gap`: under `Y≤D` and no A frequencies in `(Y,D]`, the exact error is at most `(1-cos(pi/(D+2))) * Y² * (A.filter (·≤Y)).card`.
- `p36_gap_pi`: the paper's error `(pi²/2) * (Y/(D+2))² * core.card`.

Empty sets/cores are covered. Modules: `P36/Kernel.lean`, `P36/SineKernel.lean`, `P36/Main.lean`. The ordinary P36 build passed (8713 jobs), and these modules passed again in the final whole-project build.

All three headline `#print axioms` outputs are:

`[propext, Classical.choice, Quot.sound]`.

Live evidence: `lean_next_scratch/p36_live_axioms.txt` and `p36_live_diagnostics.json`.

## Target 4: Beckner M4 — concrete global integration bridge closed

The previous report's obligation 1 is now checked for nonnegative interval-supported L1 data of positive mass in dimension two, with a common support radius, unit frame vectors, nonnegative weights, and the exact weighted-frame identity.

New modules and content:

- `HeatFlowUniform.lean`: one explicit scalar Gaussian tail constant uniform on `0<a≤t≤b`; uniform product Gaussian bound; spatial/time relative-score bounds; bound on the actual product time derivative.
- `HeatFlowIntegral.lean`: continuity of scalar heat flow and first moments; measurability of actual second moments via their spatial derivative; planar Gaussian-polynomial integrability; concrete product integrability and differentiation under its whole-plane integral.
- `HeatFlowSpatial.lean`: actual first-slope derivative on every affine line; Gaussian-polynomial envelopes for both spatial slopes; measurability and whole-plane integrability of both slopes and the time slope.
- `HeatFlowMonotone.lean`: `geometricHeatProduct_integral_derivative_nonneg` applies the existing `parabolic_integral_derivative_nonneg` with every hypothesis supplied, including the actual coordinate derivative identities and all unbounded-domain integrability assumptions. `geometricHeatProduct_integral_monotone` proves monotonicity of the actual product integral on all positive times.

The ordinary builds through `HeatFlowIntegral.lean` and `HeatFlowMonotone.lean` passed (8714 and 8716 jobs respectively). All five new M4 modules, including scalar rescaling, also passed the final whole-project build. The incremental axiom outputs for every new public M4 theorem contain only `propext`, `Classical.choice`, and `Quot.sound`.

This is the compact-data stage of M4. Its support and positive-mass hypotheses are explicit intermediate hypotheses, not a claimed arbitrary-data sharp Young theorem.

## M4: scalar large-time rescaling also checked

`HeatFlowRescale.lean` proves dominated convergence for the normalized scalar rescaling, the exact heat-kernel/flow dilation identities, and Gaussian asymptotics in both square-time and original-time variables. In particular `tendsto_sqrt_mul_heatFlow` proves, for every signed real L1 datum f and every real x,

`sqrt(t) * heatFlow f t (sqrt(t)*x) -> (integral f) * heatKernel 1 x` as `t -> +infinity`.

These scalar theorems have no support or sign restriction. They also print only `[propext, Classical.choice, Quot.sound]`. Live evidence for all 34 new public M4 theorems is in `lean_next_scratch/m4_final_live_axioms.txt` and `m4_final_live_diagnostics.json`.

## Exact remaining dependencies and next derivation

M4 is incomplete. No sharp Young, M5 autocorrelation bound, or sinc P31-N completion is claimed.

1. Prove the large-time limit of the actual whole-plane product integral. The scalar asymptotic is checked, but the finite-product normalization, two-dimensional change of variables, dominated product limit, and final Gaussian integral are not yet assembled.
2. Prove the initial-time Fatou/approximate-identity passage.
3. Prove the nonnegative compact-data density approximation and ae pullback by nonzero linear forms, including zero-mass cases, so the intermediate support restriction disappears.
4. Construct the explicit 2×2 frame and prove its determinant/sharp-factor algebra, Lp cancellation, and endpoint constants.
5. Then resume M5 and P31-N in the brief's order.

First concrete next derivation: trace `IsWeightedFrame` in the two-vector orthonormal basis to get `sum_i c_i=2`. Use `tendsto_sqrt_mul_heatFlow` factorwise. For t≥1, the existing scalar Gaussian tail gives

`sqrt(t) * heatFlow (f_i) t (sqrt(t)*s) ≤ K_i * exp(-s²/8)`,

with `K_i=heatTailConstant (f_i) R 1`. The frame identity then gives an integrable planar envelope for `t * geometricHeatProduct f c u t (sqrt(t) • x)`. The planar dilation Jacobian cancels t, and dominated convergence plus the two scalar Gaussian integrals gives the mass-product limit. This assembly remains to be formalized; it is not claimed from scalar convergence alone.

## Final verification — passed

`lean/AxiomCheck.lean` now audits all 63 new public theorems: 29 P36 and 34 M4. The eight new proof modules contain 1270 lines and zero proof-hole tokens, new axiom declarations, or `native_decide` tokens. `git diff --check -- lean` passed. The source hashes and audit coverage are recorded in `lean_next_scratch/final_source_manifest.json`.

The final ordinary `lake build` passed (8753 jobs, exit zero). The file-based `lake env lean AxiomCheck.lean` also exited zero. The transcript contains all **384/384 expected audit entries**, with no unexpected axioms, no `sorryAx`, and no Lean errors. Every one of the 63 new public theorems is present. All dependencies belong to `propext`, `Classical.choice`, `Quot.sound`.

Headline output (ordinary file-based audit):

```text
'ChowlaCosine.P36.p36_truncation' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P36.p36_gap' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.P36.p36_gap_pi' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.Beckner.geometricHeatProduct_integral_monotone' depends on axioms: [propext, Classical.choice, Quot.sound]
'ChowlaCosine.Beckner.tendsto_sqrt_mul_heatFlow' depends on axioms: [propext, Classical.choice, Quot.sound]
```

Evidence in `lean_next_scratch/`:

- `final_build.log`: successful final whole-project build.
- `final_axioms.log`, `final_axioms.summary.json`: complete ordinary axiom transcript and checked counts/allowlist.
- `headline_axioms.txt`: the five outputs quoted above.
- `final_source_manifest.json`: SHA-256 hashes, line counts, zero forbidden tokens, and audit coverage for every new proof module.
- `p36_build.log`, `m4_integral_build.log`, `m4_monotone_build.log`: successful milestone builds.
- `p36_live_axioms.txt`, `m4_final_live_axioms.txt`: earlier incremental axiom evidence, followed by the ordinary builds/audit.

Some harmless linter warnings remain. The persistent Lean diagnostic server was stopped after saving its checked checkpoint; there is no background proof work. No commit was made, no subagent was launched, and no other research Markdown document was edited.
