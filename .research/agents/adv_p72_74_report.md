# Adversarial verification report: P72, P73, P74

**Status: COMPLETE — 2026-10-19.** The assigned proofs have been checked step by step, with the three requested numerical attacks completed on dirichlet. No counterexample was found to P72(a)–(c), P73(Z), P73(T), or P74. P72(d) needs a domain correction and its point-mass comparison is false as a uniform assertion. P72(e) has a quantitative/discrete proof gap; its literal continuum hypotheses do not imply a uniform negative depth.

Only this report and `adv_p72_74_scratch/` were written by this audit. No main research notes were edited, no commit was made, and no subagents were launched. No mathematical numerical computation was run on the laptop. The numerical results below are floating-point evidence, not rigorous certificates for untested instances or universal claims.

## Verdicts

| Item | Verdict | Exact qualification |
|---|---|---|
| P72(a) | **CORRECT** | Sion applies to the compact weight box and weak-* compact probability measures; payoff continuity and both extrema are valid. |
| P72(b) | **CORRECT** | The Parseval factor is exactly `1/2` for the real Haar density. The angular notation for the density needs care. |
| P72(c) | **CORRECT** | Danskin gives the maximum active slope, hence the negative of the **minimum** absolute-moment sum. |
| P72(d) | **GAP** | The displayed bound requires `0<τ<1`; it is undefined at the allowed endpoint `τ=0`. The certificate inequality is correct after that restriction. The point-mass comparison is **FALSE** without averaging or a genericity hypothesis. |
| P72(e) | **GAP** | The qualitative Fourier-positivity obstruction is correct. A uniform constant and the discrete weighted-interval conclusion are not established by the written proof. With only the literal continuum hypotheses, a uniform constant depending solely on τ is **FALSE**; see the explicit family below. |
| P73(Z) | **CORRECT** | Includes complex PD functions, the empty good subset, and infinite error. |
| P73(T) | **CORRECT** | The abbreviated transfer can be justified with compact subsets/inner measure and an explicit saturation case. No measurability obstruction survives. |
| P74 | **CORRECT** | For the standard cutoff `L∈Z_{≥1}`, all identities, cases, constants, and the circle normalization check. Explicitly state `L≥1` to exclude the undefined expression `1/0`. |

These are paper-proof verdicts. The existing Lean certification assertions were not re-audited in this assignment.

## Conventions and audited text

Use `T=R/Z`, Haar probability `dx`, `e(t)=exp(2πit)`, and

`a_k = 1̂_Ω(k) = ∫_Ω e(−kx) dx`.

In P72, the source's angular function `Σ cos(aθ)` becomes `f_A(x)=Σ cos(2πax)` under `θ=2πx`. Its angular set measure `|{θ:f_A(θ)≤−s}|/(2π)` is the same Haar probability `λ_s`. There is no change in the minimax values or Fourier constants under this coordinate change.

The starting proof text is preserved in `adv_p72_74_scratch/PROOFS_at_audit_start.md`. The independent VM check also compares it byte for byte with the source. The fixed task was adversarial verification, not advancement of the broader research program.

## P72(a): minimax, topology, and signs

Let `W=[1−τ,1+τ]^A` and `P(T)` be the Borel probability measures on the compact circle. `W` is compact convex in finite-dimensional Euclidean space. `P(T)` is compact convex in the weak-* topology inherited from `C(T)*`: positivity and total mass one define a weak-* closed subset of the unit ball. The topology here is not the total variation norm topology.

The payoff

`F(w,ν)=−Σ_a w_a ∫cos(2πax)dν(x)`

is affine and continuous in each variable (in fact jointly continuous because the sum is finite). It therefore satisfies the quasiconcavity/quasiconvexity and semicontinuity hypotheses of [Sion, *On general minimax theorems*, Theorem 3.4](https://msp.org/pjm/1958/8-1/pjm-v8-n1-p14-p.pdf).

For fixed w, maximizing over ν equals maximizing the continuous integrand over x; a Dirac measure attains it. Thus Sion interchanges exactly the optimization problems in the statement. For each coordinate, minimizing `−w_a c_a` on the interval gives `−c_a−τ|c_a|`, including `c_a=0`. The resulting dual objective is continuous in ν, so the outer maximum is attained. The primal minimum is also attained. The empty set A gives zero on both sides and causes no exception.

**Verdict: CORRECT.**

## P72(b): the Parseval constant

Put `E_s={f_A≤−s}` and suppose `λ=|E_s|>0`. Relative to Haar probability, the normalized restricted measure has real density `h=1_E_s/λ`, with

`ĥ(0)=1`, `‖h‖₂²=1/λ`, and `ĥ(−k)=conj(ĥ(k))`.

Consequently Parseval gives exactly

`Σ_{k≥1}|ĥ(k)|² = (1/λ−1)/2`.

Also `c_a=Re ĥ(a)`, so

`Σ_{a∈A}|c_a| ≤ √n (Σ_{a∈A}|c_a|²)^{1/2} ≤ √[n(1/λ−1)/2]`.

The unweighted term satisfies `−Σ c_a=−∫f_A dν≥s`. Substituting this measure into (a) gives the asserted bound. Nothing replaces `|ĥ(a)|²` with a potentially signed square.

The source notation `dν/dx` inside `L²(dx/(2π))` must mean the density relative to normalized Haar measure. If it meant the ordinary angular Lebesgue density, it would be `1/(2πλ)` on the set and the displayed Parseval equation would have the wrong normalization. In the stipulated `R/Z` convention this ambiguity disappears.

**Verdict: CORRECT, with the density interpreted as Haar density.**

## P72(c): Danskin and the optimizer set

The continuous moment map sends `P(T)` to a compact subset `K⊂R^n`. On K define `α(c)=−Σ c_a` and `β(c)=Σ|c_a|`. Then

`M_τ=max_{c∈K}[α(c)−τβ(c)]`.

Both α and β are continuous; the dependence on τ is affine with continuous slope `−β`. This reduces the question to the finite-dimensional compact-index version of [Danskin's theorem, Bertsekas, Proposition 5.4.9](https://www.mit.edu/~dimitrib/convexdualitycondenced.pdf). The displayed maximum can be extended to all real τ to apply the theorem at an interior point; only its right derivative at zero is needed for the original domain.

The active measures at zero satisfy `∫(f_A+M_0)dν=0`. Since the integrand is continuous and nonnegative, this is equivalent to ν being supported on `argmin f_A`. The maximum active slope is

`max_{ν∈Opt₀}(−β(ν)) = −min_{ν∈Opt₀}β(ν)`.

The minimum exists by compactness. Selecting that same measure at positive τ gives `M_τ≥M_0−τ min_Opt₀ β` directly. No uniqueness of the minimizing x or the optimizing measure is assumed. The absolute value is applied after averaging each cosine; replacing this by an average of absolute values would be a different statement.

**Verdict: CORRECT.**

## P72(d): exact domain defect and false point-mass comparison

If “ν certifies `M_τ≥m`” means its dual objective is at least m, then

`m ≤ −Σ c_a(ν)−τΣ|c_a(ν)| ≤ M_0−τΣ|c_a(ν)|`.

For `τ>0`, division proves the stated spread inequality and, under `m≥c√n`, `M_0≤C√n`, the bound `(C−c)√n/τ`. This says nothing finite about spread when `τ=0`. At that allowed endpoint the displayed quotient is undefined, including possible `0/0`. The repair is to state (d) for `0<τ<1`.

The additional assertion that a point mass has `Σ|c_a|≈(2/π)n` is not uniform. For `ν=δ_0`, the sum is exactly n for every A. For `A={1,3,...,2n−1}` and `ν=δ_{1/4}`, every `cos(2πa/4)=0`, so the sum is exactly zero. The correct unconditional statement is the spatial average

`∫_T Σ_{a∈A}|cos(2πax)|dx = (2/π)n`.

This false comparison does not invalidate the restricted certificate inequality.

**Verdict: GAP in the displayed domain; the ancillary point-mass assertion is FALSE as a uniform claim.**

## P72(e): qualitative obstruction versus uniform conclusion

Assume the bounded profile is measurable and real, supported in `[−1,1]`, and at least `c=1−τ>0` on its interior. If its Fourier transform is everywhere real and nonnegative, the nonnegative Fejér-weighted integrals

`∫ (1−|ξ|/R)_+ φ̂(ξ)dξ = (φ*F_R)(0) ≤ ‖φ‖∞`

increase to `∫φ̂`. Here `F_R` is the real-line Fejér kernel of mass one, so the bound holds even if zero is not a Lebesgue point. Hence `φ̂∈L¹`, and Fourier inversion gives a continuous function equal to φ almost everywhere. Such a representative must be zero outside `[−1,1]` and at least c throughout `(-1,1)`, which contradicts continuity at either endpoint. Strictly speaking, inversion gives a continuous **representative**, not pointwise continuity of an arbitrary original measurable version. The contradiction is still valid.

The resulting conclusion is qualitative: **each such profile has a negative Fourier value**. It does not by itself give a common negative depth, a constant depending only on τ, or a uniform discrete linear bound.

There is an explicit counterexample to a uniform depth under the continuum hypotheses as literally written. For fixed c and arbitrary `B>0`, set

`φ_B(x)=c·1_[−1,1](x)+B(1−|x|)_+`.

This is bounded for each B, supported in the required interval, and at least c there. With the convention `φ̂(ξ)=∫_R φ(x)e(−ξx)dx`, write `t=πξ`, `y=sin(t)/t` (continuously at zero). Then

`φ̂_B(ξ)=2c y cos(t)+B y²`

`=B[y+c cos(t)/B]²−c² cos²(t)/B ≥ −c²/B`.

Thus for every ε>0, a permitted B makes the entire Fourier transform at least `−ε`. Each individual transform still has negative values just to the left of a positive integer frequency: the first term has a simple zero and the second term a double zero there. This refutes a uniform negative constant depending only on τ for the stated class.

The intended weighted interval class has the additional common upper bound `φ≤1+τ`. That excludes this family. For that intended class, one must actually supply the uniform compactness argument and the continuum-to-discrete passage (the source acknowledges the latter is not written). The audit does not label the intended box-bounded discrete theorem false.

**Verdict: GAP for the intended quantitative/discrete conclusion; CORRECT qualitative obstruction; FALSE uniform conclusion under the literal continuum hypotheses without a common upper bound.**

## P73(Z): every proof step

Positive definiteness implies `m₀=φ(0)∈R_{≥0}`, Hermitian symmetry, and `|φ(k)|≤m₀`. The GNS construction gives `ψ(k)=m₀−Re φ(k)≥0` and a translation-invariant Hilbert distance `√(2ψ)`. Its triangle inequality yields the asserted subadditivity. In particular,

`ψ(k+l)≤2ψ(k)+2ψ(l)`.

If `E=∞`, the theorem is immediate. Otherwise the bad set `B={k:|φ(k)−1_S(k)|>δ}` is finite and `δ²|B|≤E`.

For `k,l∈S\B`, let `u=m₀−1+δ`. Their existence forces `u≥0`. If `k+l∉S∪B`, then

`m₀−δ ≤ ψ(k+l) ≤ 4u = 4(m₀−1+δ)`,

forcing `3m₀≥4−5δ`, contrary to the strict hypothesis. This is valid for complex φ: only real parts and modulus error bounds were used.

Thus `A+A⊂S∪B` with `A=S\B`. For nonempty finite A in Z, `|A+A|≥2|A|−1`; this is elementary by ordering A and does not require primality or reduction modulo anything. If A is empty, `|B|≥|S|` already proves the required bad-set bound. Otherwise,

`2(|S|−|B|)−1 ≤ 2|A|−1 ≤ |S|+|B|`,

so `|B|≥(|S|−1)/3`. This proves the claimed error bound, including `|S|=1` and sets S that do not contain zero.

**Verdict: CORRECT.**

## P73(T): measurability, inner measure, and saturation

Take `δ∈(0,1/2)`, `μ=|Ω|∈(0,1/2]`, and continuous PD g with `m₀=g(0)<(4−5δ)/3`. Define the Haar measurable sets

`B={x:|g(x)−1_Ω(x)|>δ}`, `b=|B|`, and `A=Ω\B`.

The same Hilbert-distance calculation as in Z proves the pointwise containment `A+A⊂Ω∪B`. Also `|A|≥μ−b`, and `‖g−1_Ω‖₂²≥δ²b`.

One should not silently assume that the algebraic sum of two completed-Haar measurable sets is measurable. Instead, for every nonempty compact `K⊂A`, `K+K` is compact, and the compact connected-group sumset theorem gives

`min(1,2|K|) ≤ |K+K| ≤ |Ω∪B| ≤ μ+b`.

The exact required compact-set theorem is stated in [Tao, *An inverse theorem for an inequality of Kneser*, introduction, equation (1)](https://arxiv.org/html/1711.04337v4); its connected compact group hypotheses apply to `R/Z`. Haar inner regularity lets `|K|` approach `|A|`, giving `min(1,2|A|)≤μ+b`. Equivalently, one may formulate the sumset bound using inner measure throughout. There is no need to take the measure of `A+A` itself.

For the remaining saturation issue, suppose `b<μ/3`. Then `μ+b<4μ/3≤2/3<1`. The saturated value 1 on the left is impossible, so

`2(μ−b) ≤ 2|A| ≤ μ+b`,

which implies `b≥μ/3`, a contradiction. Therefore `b≥μ/3` and

`‖g−1_Ω‖₂² ≥ δ²μ/3`.

If `|A|=0`, the conclusion follows immediately from `b≥μ`; under the contradiction assumption A has positive measure and compact subsets of positive measure exist. Null-set changes to Ω cause no issue with this proof. The restriction `μ≤1/2` is genuinely used; without a density restriction, `Ω=T`, `g=1` would refute the conclusion for small positive δ.

The consequence P73(b) uses a non-strict peak inequality `≤` although the primary statement uses `<`. This endpoint follows by taking `δ'↑δ` with `δ'<δ`; the peak is then strictly below `(4−5δ')/3`. Thus this is not a gap.

**Verdict: CORRECT; the source's abbreviated “identical” transfer should be expanded as above.**

## P74: projection identities, Bernstein, and constants

Assume `L∈Z_{≥1}`. Symmetry of Ω gives real `a_k=a_−k`; nonnegativity for `|k|≤L` makes

`g(x)=Σ_{|k|≤L}a_k e(kx)`

continuous, real, even, and PD. The triangle inequality gives `|g(x)|≤Σa_k=g(0)=γ`, with equality at zero. Thus `γ=‖g‖∞` in the absolute-value norm, and `g'(0)=0`.

Projection/Parseval give, with every integral relative to Haar probability,

`U=‖1_Ω−g‖₂²=μ−Σ_{|k|≤L}a_k²=∫g−∫g²=∫g(1−g)`.

The integral identity is global; its integrand need not be nonnegative pointwise. The unresolved tail is `Σ_{|k|>L}|a_k|²`; the source's squares equal these absolute squares because symmetry makes all coefficients real.

For a trigonometric polynomial in frequencies `[-L,L]`, the sharp angular Bernstein constant is L, not 2L. Changing from `θ` to `x=θ/(2π)` gives `‖g'‖∞≤2πL‖g‖∞`, and applying it to g' gives

`‖g''‖∞≤(2πL)²γ`.

This is the exact form of [Queffélec–Zarouf, *On Bernstein's inequality for polynomials*, Theorem 1.1](https://arxiv.org/pdf/1903.10801). There is also a direct check here using nonnegative coefficients:

`|g''(x)|≤Σ(2πk)²a_k≤(2πL)²Σa_k=(2πL)²γ`.

Taylor's formula at zero therefore gives `g(x)≥γ(1−2π²L²x²)` in the centered circle coordinate.

- **Case A:** `γ<7/6` and `δ=1/10` satisfy P73(T)'s strict hypothesis. Its conclusion is exactly `U≥μ/300`, since `δ²/3=1/300`. This dominates `(1/4000)min(μ,1/L)`.
- **Case B:** `γ≥7/6`, including equality. Restrict to `|x|≤h=√(3/56)/(πL)`. On this neighborhood, `1−2π²L²x²≥25/28>0`, so replacing γ by `7/6` is legitimate. The edge value is exactly `(7/6)(25/28)=25/24`. The source's second Taylor comparison must be read on this neighborhood, not as a global comparison when its bracket is negative.

For `L≥1`, `h<1/2`, so the neighborhood has Haar measure exactly `2h` and does not overlap itself around the circle. Since `1_Ω≤1`, the error there is at least `1/24` in absolute value, hence its square is at least `1/576`. Therefore

`U≥2h/576 = [√(3/56)/(288π)]/L`.

The coefficient is

`0.000255813967521932794722871022425964502014133063... > 0.00025 = 1/4000`.

This comparison also has an exact check: `π<22/7` and

`3/56 > ((9/125)(22/7))²`

imply `√(3/56)>9π/125`, which is equivalent to the required coefficient being greater than `1/4000`. The rational difference is positive in `independent_results_vm.json`. Thus the rounded constant has genuine slack; it does not depend on trusting decimal output.

The two cases exhaust all γ and imply exactly the advertised minimum of μ and `1/L`. They do not imply `U≥cμ` uniformly in the large-peak, `μL≫1` regime. The source explicitly preserves that limitation.

**Verdict: CORRECT, with the standard positive-integer cutoff made explicit.**

## Numerical adversarial checks (VM only)

Reproduce with:

```sh
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -t 420 python .research/agents/adv_p72_74_scratch/audit_vm.py
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -t 120 python .research/agents/adv_p72_74_scratch/independent_vm.py
```

Main seed: `727374`. Environment and measured runtimes are stored with the outputs. The main run used Python 3.12.3, NumPy 2.5.4, SciPy 1.18.1, on Linux/GCP, and took about 26 seconds of script wall time. Computations used at most the requested four-core quota. The independent script uses 90-digit mpmath and exact rational arithmetic for the elementary constant comparison.

### P72(a): both linear programs

Tested all nonempty subsets of `{1,...,6}` of size at most four, plus 20 seeded sparse sets from `{1,...,24}` with sizes two through six; the four τ values were `0,0.1,0.5,0.9`. This gives **304 pairs** of LPs. Each used a 2048-point full-circle grid, reduced to the even half-circle without changing the finite problem. Eight cases were repeated on an 8192-point grid.

The primal minimizes z over the weight box with `−Cw≤z`. The dual uses grid probability masses p, `c=Cᵀp`, and auxiliary variables `t≥±c`, maximizing `−Σc−τΣt`. The actual nonlinear dual objective `−Σc−τΣ|c|` was also evaluated at the resulting measure.

- Maximum primal/dual discrepancy on the 304 coarse cases: `1.06e−11`.
- Maximum discrepancy from the recomputed absolute-value objective: `1.29e−11`.
- Maximum discrepancy on the eight fine cases: `8.72e−11`.
- The largest observed coarse-to-fine value change in those repeats was `3.13e−5`, much larger than LP residuals and correctly attributable to grid resolution.

No duality violation was observed. These are finite-grid comparisons; they do not replace the compact-circle proof or certify a continuum optimum.

### P73(T): complex and real PD polynomials

Tested **5,000 seeded random cases**, with degree zero through 24, nonnegative Fourier coefficients, and peak `0.01≤g(0)<1.332`. Both symmetric real and nonsymmetric complex PD polynomials were included. Delta was chosen strictly below the allowed peak threshold, capped at `0.499`. Sets were random cell unions, shifted intervals, and adversarial unions of cells with largest `Re g`, always with `0<μ≤1/2`. Five constant-polynomial boundary examples were added: **5,005 cases total**.

Each selected grid cell represents an actual arc of width `1/2048`, centered at `j/2048`. Its Fourier coefficient is computed by integrating the arc, namely the discrete Fourier sum times the sinc factor. The exact-in-formula error is

`E=Σ_k b_k²+μ−2Σ_k b_k Re(a_k)`

for `g=Σ b_k e(kx)`, `b_k≥0`. This does not approximate E by point samples of `|g−1_Ω|²`.

There were **zero violations**. The smallest observed ratio `E/(δ²μ/3)` was approximately **4.7737264542**, at degree three, peak `0.5961934955`, delta `0.4418416188`, and `μ=0.23095703125`. The associated coefficients and arc mask are in `p73_best_vm.npz`. Direct 90-digit integration of those arcs independently checks its error and ratio.

This search covers a finite collection of trig polynomials and finite arc unions, not all continuous PD functions or all measurable sets.

### P74: symmetric unions of arcs

Cutoffs were `L∈{1,2,3,4,6,8,12,16,24,32,64}`. Families included centered arcs and their preimages under `x↦qx`, with `q∈{1,2,3,5,8,17}`; independent random symmetric cell unions; random symmetric unions supported in a short neighborhood of zero; unions selected by random cosine scores with nonnegative score coefficients; and signs of Dirichlet kernels.

After filtering for density and nonnegative low coefficients, **4,358 cases** were accepted, of which **157** had `γ≥7/6`. Accepted counts by family:

| Family | Proposed | Accepted |
|---|---:|---:|
| Centered arc or lattice preimage | 2310 | 2310 |
| Dirichlet sign cell union | 11 | 2 |
| Independent random symmetric unions | 1100 | 102 |
| Small-support random symmetric unions | 1100 | 1091 |
| Positive-score random symmetric unions | 2200 | 853 |

Some proposed sets were empty, had density above one half, or had a negative low coefficient; those were excluded rather than tested as though they met the theorem. Floating-point admissibility used a `2e−12` allowance for tiny negative roundoff. Consequently accepted random examples are numerical admissibility checks, not certified sign proofs. Centered arc/lattice coefficients have the explicit formula `a_k=0` when `q∤k`, and `a_k=μ sinc((k/q)μ)` otherwise; the chosen density range ensures analytic nonnegativity for these structured cases.

For all accepted cases U was computed as `μ−a_0²−2Σ_{k=1}^L a_k²`, so no truncation of the unresolved tail was used. Independent direct arc integration and the FFT/sinc formula agreed within `1.09e−16` on the selected cross-checks.

There were **zero violations** of `U≥2.5e−4 min(μ,1/L)`. The smallest ratio `U/min(μ,1/L)` was approximately **0.09471526543**, for the half-circle centered at zero with `L=1`. Here exactly `U=1/4−2/π²`, and the independent high-precision script verifies it. The finite search says nothing universal beyond its saved cases.

### P72(e): missing-upper-bound family

The VM also evaluated the displayed explicit family at τ=1/2 with `B=1,10,100,1000,10000`. For large B, values near the first integer frequency approach the exact global lower bound `−1/(4B)`. The counterexample to a common depth is the completed-square identity, not these sampled evaluations. At B=1 the particular sampled frequency happens to give a positive value; no claim of a negative global minimum is inferred from that sample.

## Evidence artifacts and final disposition

All paths below are relative to `adv_p72_74_scratch/`:

- `audit_vm.py`: main reproducible searches and constant evaluations.
- `results_vm.json`: completed aggregate results, environment, seed, and runtime.
- `p72_lp_cases_vm.json`: all 304 coarse LP comparisons.
- `p73_best_vm.npz`: coefficients and exact cell mask of the strongest observed P73 adversary.
- `p74_cases_vm.json`: all accepted P74 cases and their parameters/ratios.
- `p74_best_vm.json`: parameters of the smallest-ratio P74 case.
- `independent_vm.py` and `independent_results_vm.json`: direct high-precision integration of the P73 adversary, the semicircle check, exact rational constant check, and source snapshot comparison.
- `PROOFS_at_audit_start.md`: exact starting source snapshot.

The main mathematical findings requiring attention are confined to P72(d) and P72(e). P73(T)'s measurability/saturation details and P74's constants survive adversarial review. No broader Chowla claim is inferred, and no ongoing computation is left running by this audit.
