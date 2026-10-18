# OR(2)-weak in Z: residue strips and a sampled derivative inequality

2026-10-18. **PROVED on paper; not kernel-checked or externally reviewed.**
This answers task 1 of `or2_brief.md` and gives a quantitative structural
inequality relevant to task 2. Unrestricted OR(2)-weak remains **CONJECTURED**.
Novelty outside the repository has not been checked. No obstruction family at
the quarter-power scale, and no Epoch solution, is claimed.

Further progress after the first checkpoint: **PROVED Theorem C in §5**
removes the short-phase-arc hypothesis for bounded residue width. It uses
all zeros of the pair factor and a macroscopic-profile alternative. For a
fixed width relative to `t` and a fixed number of residue classes it gives
a square-root bound, with separation independent of `n` and quotient heights.

## 1. Main theorem, with exact quantifiers

**PROVED — Theorem A.** Let `t,q` be positive integers and `S⊂Z_{>0}` a
finite nonempty set, `n=|S|`. Suppose its least nonnegative residues modulo
`q` form a set

`R⊂{0,…,floor(t/2)}`, `k=|R|`, and `q≥32t√k`.

Then `S∩(S+jt)=∅` for `j=±1,±2`, `A=S∪(S+t)` has exactly `2n` distinct
positive frequencies, and

`M(A)≥(1/80)√(n/k)`.

If additionally `min S≥q`, the same hypotheses give

`M(A)≥(1/32)√(n/k)`.

The quotient levels `floor(s/q)` may be arbitrarily large and unrelated;
there is no requirement of a full section modulo `t`, no congruence condition
on `q`, and no dependence on `max S`.

**PROVED — the requested OR(2)-weak subclass.** For all sets in this theorem
with `k≤n^(1/4)`,

`M(S∪(S+t))≥n^(3/8)/80`.

Thus absolute `c=1/80`, `δ=1/8` work. More generally, for each fixed
`0<δ≤1/4`, `k≤n^(1/2−2δ)` implies `M≥n^(1/4+δ)/80`. A fixed bound
`k≤k₀` gives the square-root estimate `M≥√n/(80√k₀)`.

**PROVED — strict extension of the nontrivial dilated class.** The theorem
includes `S=qY` with positive quotient levels and `q≥32t`, in particular the
positive-frequency full-section examples in the brief when this quantitative
condition holds. It also includes, for every `m≥1`,

`t=2, q=192, S={192j,192j+1:1≤j≤m}`.

This set has gcd `1`, so is not a dilate `q'Y` with `q'>1`. The sets of
quotient levels in its two residue classes can be chosen independently.
Residue offsets as large as `t/2` are allowed: the proof does not absorb them
into an additive error proportional to `n`.

## 2. General phase-coherence theorem

**PROVED — Theorem B.** Let `t,q≥1` be integers, let `R⊂{0,…,R_*}` be
nonempty, and assume `q>R_*+2t`. For each `r∈R`, let `Y_r⊂Z_{≥0}` be a
finite nonempty set; exclude `0∈Y_0` if `0∈R`. Define

`S=⋃_r(qY_r+r)`, `n_r=|Y_r|`, `n=Σ_r n_r`, `A=S∪(S+t)`.

Assume `S∩(S+jt)=∅` for `j=±1,±2`. For general `R` this must be checked
inside each quotient block; `q>R_*+2t` rules out collisions between blocks.
For each nonnegative integer `y`, define

`C_y=Σ_{r:y∈Y_r} exp(iπr/t)`,

`C=2(Im C_0)^2+Σ_{y≥1}|C_y|²`,

`G=Σ_r [r²+(r+t)²]√n_r`.

Then `G>0` and

`M(A)≥t²C/(4G)−π²G/(2q²)`.                              (B)

Equivalently,

`C≤4GM(A)/t²+2π²G²/(t²q²)`.                              (B′)

These are explicit statistics of the integer set, not existential structure
or an unproved inverse theorem. They impose a checkable phase-balance
condition under the stated representation; they do not force such a
representation for an arbitrary `S`.

## 3. Full proof of Theorem B

No outside theorem is invoked. The proof uses Taylor's inequality,
Cauchy–Schwarz, and finite exponential orthogonality, in the forms below.
Integrals in `θ` are normalized by `dθ/(2π)` on `[0,2π]`.

### 3.1 Sampled derivative lemma

**PROVED.** Suppose `h:R→R` is twice continuously differentiable and
`2π`-periodic, `h(u₀)=0`, and `|h''|≤L` everywhere for `L≥0`. If

`h((θ+2πj)/q)≥−M` for all integers `j`,

where `q≥1` is an integer, `θ∈R`, and `M≥0`, then

`|h'(u₀)|²≤2LM+π²L²/q²`.                                (D)

If `L=0`, periodicity makes `h` constant. Otherwise put `d=h'(u₀)` and
choose a shifted grid point `v` within `π/q` of `u₀−d/L`. Taylor's upper
bound, valid for every real displacement, gives

`h(v)≤d(v−u₀)+(L/2)(v−u₀)²`

`    =−d²/(2L)+(L/2)(v−u₀+d/L)²`

`    ≤−d²/(2L)+Lπ²/(2q²)`.

Combine with `h(v)≥−M` and multiply by `2L`. This proves (D). It does not
assume an independent continuous rotation; only genuine sample points are
used.

### 3.2 Exact lifting and curvature

Let `z_r(θ)=Σ_{y∈Y_r}exp(iyθ)`. For fixed `θ`, define

`h_θ(u)=Re[(1+exp(itu))Σ_r exp(iru)z_r(θ)]`.

At `u=(θ+2πj)/q`, we have `qu≡θ (mod 2π)` and hence exactly

`h_θ(u)=f_A(u)≥−M(A)`.

The equality relies on `A` being a set of `2n` distinct frequencies.
Holding `θ` fixed when differentiating in `u` gives

`|h_θ''(u)|≤L(θ):=Σ_r [r²+(r+t)²]|z_r(θ)|`.

The large quotient levels do not occur in this macro-curvature bound.
At `u₀=π/t` the pair factor vanishes, and

`h_θ(u₀)=0`,

`h_θ'(u₀)=t Im[Σ_r exp(iπr/t)z_r(θ)]`

`         =t Im[Σ_{y≥0}C_y exp(iyθ)]`.

The derivative of `1+exp(itu)` at `u₀` is `−it`, and
`Re(−it z)=t Im z`, fixing the sign.

### 3.3 Orthogonality and integration

For a finite set `Y` of distinct nonnegative integers, expansion and
`∫exp(imθ)=0` for a nonzero integer `m` give

`∫|Σ_{y∈Y}exp(iyθ)|²=|Y|`.

Thus `∫|z_r|≤√n_r`, and Cauchy–Schwarz gives
`∫|z_r||z_s|≤√(n_r n_s)`. Therefore

`∫L≤G`, `∫L²≤G²`.

If `b(θ)=C_0+Σ_{y≥1}C_y exp(iyθ)`, orthogonality also gives

`∫(Im b)²=(Im C_0)²+(1/2)Σ_{y≥1}|C_y|²=C/2`.

Indeed `(Im w)²=(|w|²−Re(w²))/2`, and a sum of strictly positive
frequencies and its square both have zero mean. The constant coefficient
must be handled separately; the formula is false for arbitrary signed
quotient levels.

Apply (D) to `h_θ` and integrate:

`t²C/2=∫|h_θ'(u₀)|²`

`      ≤2M(A)∫L+(π²/q²)∫L²`

`      ≤2M(A)G+π²G²/q²`.

Here `M(A)≥0`, since `f_A` has mean zero. Dividing by `2G>0` proves (B);
rearrangement proves (B′). This is the complete paper proof.

## 4. Deriving Theorem A and further consequences

### 4.1 Collision audit and the short arc

**PROVED.** Under Theorem A, write `s=qy+r`, `y≥0`, `r∈R` uniquely.
Since `q>2t+R_*`, points in distinct quotient blocks differ by at least
`q−R_*>2t`; points in the same block differ by at most `R_*≤t/2`.
Neither can differ by `t` or `2t`. This proves every 2-run and distinctness
condition, also for the negative shifts.

Write `ℓ_y=#{r:y∈Y_r}` and `e=ℓ_0≤k`. The phases `exp(iπr/t)` lie in an
arc of width at most `π/2`. Rotate its midpoint to zero; each phase has
real part at least `1/√2`. Hence

`|C_y|²≥ℓ_y²/2≥ℓ_y/2`, and `C≥(n−e)/2`.

Also

`G≤(5/2)t²Σ_r√n_r≤(5/2)t²√(kn)`,

because `r²+(r+t)²≤(t/2)²+(3t/2)²=(5/2)t²`.

### 4.2 Constants and the zero-level boundary

**PROVED.** If `n≥2k`, then `C≥n/4`. Formula (B) implies

`M(A)≥(1/40)√(n/k)−(5π²t²/(4q²))√(kn)`.

Using `q²≥1024t²k` and `π²<10`, the error is at most

`(50/4096)√(n/k)≤(1/80)√(n/k)`

(equivalently, `4000≤4096`). This proves `M(A)≥√(n/k)/80`.

Every nonempty set of distinct positive frequencies satisfies `M(A)≥1/2`:
choose `a₀∈A` and integrate the product of the two nonnegative functions
`M(A)+f_A(x)` and `1−cos(a₀x)`. Orthogonality gives

`0≤∫(M(A)+f_A(x))(1−cos(a₀x))dx/(2π)=M(A)−1/2`.

When `n<2k`, this is stronger than `√(n/k)/80<√2/80`. It handles all
zero quotient levels, including sets lying entirely below `q`.

If `min S≥q`, then `e=0`, and `C≥n/2` for every `n`. The positive term
improves to `(1/20)√(n/k)`, with the same error at most `(1/80)√(n/k)`.
Thus `M(A)≥(3/80)√(n/k)≥√(n/k)/32`. Theorem A and its exponent
consequences are proved for every permitted finite size, without a threshold.

### 4.3 A subclass without a short phase arc

**PROVED.** In Theorem B suppose the `Y_r⊂Z_{≥1}` are pairwise disjoint,
`R_*≤Lt` for a fixed real `L≥0`, and put `B=L²+(L+1)²`. If
`q≥8Bt√k`, then

`M(A)≥√(n/k)/(8B)`.

Each quotient block contains only one point of `S`; all 2-run conditions
hold. Each occupied positive fiber has `|C_y|=1`, so `C=n`, while
`G≤Bt²√(kn)`. Inserting this into (B) gives

`M(A)≥[1/(4B)−π²Bt²k/(2q²)]√(n/k)`.

The error coefficient is at most `π²/(128B)≤1/(8B)`. Also
`8B>L+2` for all `L≥0`, so the stated lower bound on `q` implies the
needed block separation. This proves the corollary. Its positive-level
hypothesis is explicit; Theorem A itself permits a zero level.

### 4.4 Conditional structural content

**PROVED.** For the general theorem with `R_*≤Lt`, (B′) yields

`C/n≤4B√k·M(A)/√n+2π²B²t²k/q²`, `B=L²+(L+1)²`.           (S)

For a sequence with fixed `L`, `M(A)=o(√(n/k))`, and
`q/(t√k)→∞`, necessarily `C=o(n)`. For every fixed `ε>0`, the total
size of positive quotient fibers with `|C_y|²≥εℓ_y` is at most
`C/ε=o(n)`. If also `k=o(n)`, the omitted zero fiber has only `o(n)`
points. Thus almost all points must lie in fibers with substantial vector
cancellation at phase `π/t`. This is a checkable necessary condition, not
a claim that cancellation is impossible in wider arcs; the wider-fiber
example in §6 realizes it. Theorem C below handles that alternative.

## 5. Wider residue patterns: a second theorem after the obstruction

**PROVED — Theorem C.** Fix an integer `L≥0` and put

`B=L²+(L+1)²`, `J=2L+3`.

Let `t,q≥1` be integers. Let `S⊂Z_{>0}` be a nonempty finite set,
`n=|S|`, with `min S≥q`. Suppose its residues modulo `q` form a set
`R⊂{0,…,Lt}`, `k=|R|`. Assume the original 2-run conditions
`S∩(S+jt)=∅` for `j=±1,±2` and

`q≥16BJtk`.

Then

`M(S∪(S+t))≥√n/(32BJ²k^(3/2))`.

For fixed `L,k` this is a square-root theorem for bounded unions of
translated dilates, allowing arbitrary quotient patterns and arbitrary
residues throughout a window of width `Lt`. The short-arc and disjoint-fiber
conditions are absent. For fixed `L` and `k≤n^(1/12)` this gives
`M≥n^(3/8)/(32BJ²)`. Concretely, `L=3` gives absolute constants:

`R⊂[0,3t]`, `q≥3600tk`, `k≤n^(1/12)` imply
`M≥n^(3/8)/64800`, with the other stated hypotheses.

### 5.1 Derivative energy at all t zeros

Write `s=qy+r`, so all quotient levels are positive. For `0≤j<t`, set

`u_j=(2j+1)π/t`,

`C_j=Σ_{y≥1}|Σ_{r:y∈Y_r} exp(iru_j)|²`,

`C_*=t^(-1)Σ_{j=0}^{t−1}C_j`.

The proof of Theorem B applies unchanged at any `u_j`: each is a zero of
`1+exp(itu)`, with derivative `−it`. Thus

`M(A)≥t²C_j/(4G)−π²G/(2q²)`,

where `G≤Bt²√(kn)`.

Finite DFT orthogonality in `j` gives the exact integer expression

`C_*=Σ_y Σ_{a=0}^{t−1} b_{y,a}²`,

`b_{y,a}=Σ_{r=a+ht ∈R: y∈Y_r} (−1)^h`.

Indeed the inner phase sum equals
`Σ_a exp(iπa/t)exp(2πija/t)b_{y,a}`; averaging its square modulus over
`j` kills distinct `a` terms.

Let `n_r=|Y_r|`, setting absent counts to zero, and define

`N=Σ_{h=0}^L n_{ht}`, `N_alt=Σ_{h=0}^L (−1)^h n_{ht}`.

Then `N_alt=Σ_y b_{y,0}`. At most `N` positive quotient fibers contribute
to this sum, so Cauchy–Schwarz gives

`N_alt²≤N C_*`.                                           (C1)

This is valid also when `N=0`.

### 5.2 A macro-profile inequality

Define the macro-profile with quotient phase zero:

`H(u)=Σ_{r∈R} n_r[cos(ru)+cos((r+t)u)]`,

`m=−min_u H(u)≥0`.

The sign follows because `H(u_j)=0`. The nonnegative function `H+m`
has mean `n_0+m`. Its cosine coefficient at frequency `r+t` is at least
`n_r`, since all counts are nonnegative. The absolute value of any complex
Fourier coefficient of a nonnegative function is at most its mean, simply
by the triangle inequality in the integral. Therefore

`n_r≤2(n_0+m)`, and `n≤2k(n_0+m)`.                        (C2)

Average over the `t` shifts to project onto multiples of `t`:

`H_bar(v)=t^(-1)Σ_{a=0}^{t−1} H((v+2πa)/t)`

`        =Σ_{h=0}^L n_{ht}[cos(hv)+cos((h+1)v)]≥−m`.

The quotient `R_bar(v)=H_bar(v)/(1+cos v)`, initially away from `π`,
extends to a real trigonometric polynomial of degree at most `L`, since

`[cos(hv)+cos((h+1)v)]/(1+cos v)`

` = (−1)^h[1+2Σ_{a=1}^h (−1)^a cos(av)]`.

The identity follows by multiplication by `1+cos v` and cancellation of
adjacent cosine terms. Consequently

`R_bar(0)=N`, `∫R_bar=N_alt`.

Take the odd grid `v_j=2πj/J`, `0≤j<J`. Since `J>L`, its average of
`R_bar` is exactly `N_alt`. No grid point is `π`, and

`Σ_{j=0}^{J−1} 1/(1+cos v_j)=J²/2`.

For completeness, put `P(v)=Σ_{h=0}^{J−1}(−1)^h exp(ihv)`. At each grid
point, `(1+exp(iv_j))P(v_j)=2`, because `J` is odd. Hence
`|P(v_j)|²=2/(1+cos v_j)`. Discrete orthogonality gives
`Σ_j |P(v_j)|²=J²`, proving the reciprocal identity.

At `j=0`, `R_bar=N`. At the other points,
`R_bar(v_j)≥−m/(1+cos v_j)`. Summing yields

`N≤J N_alt+(J²−1)m/2`.

Using (C1) and `J√(N C_*)≤N/2+J²C_*/2`, we get

`N≤J²C_*+(J²−1)m`.

Since `n_0≤N`, (C2) now proves the useful dichotomy inequality

`n≤2kJ²(C_*+m)`.                                         (C3)

This is the new pivot: cancellation at all the zeros forces a macro dip.
It does not require a higher-order derivative estimate.

### 5.3 Transfer of the profile dip and constants

At every `u=2πa/q`, the original cosine sum equals `H(u)` exactly.
Furthermore

`|H''(u)|≤Σ_r n_r[r²+(r+t)²]≤Bt²n`.

Choose a grid point within `π/q` of a global minimum of `H`. Since `H'`
vanishes at that minimum, Taylor gives

`M(A)≥m−π²Bt²n/(2q²)`.                                  (C4)

By (C3), either `C_*≥n/(4kJ²)` or `m≥n/(4kJ²)`.

In the first case some `C_j≥C_*`, so

`M(A)≥[1/16−π²/512]√n/(BJ²k^(3/2))`

`     ≥√n/(32BJ²k^(3/2))`,

using `q²≥256B²J²t²k²` and `π²<16`.

In the second case the error in (C4) is at most
`π²n/(512BJ²k²)≤n/(8kJ²)`. Thus

`M(A)≥n/(8kJ²)≥√n/(32BJ²k^(3/2))`.

Finally, the stated lower bound on `q` guarantees `q>Lt+2t`:
`B≥L+1`, `J≥3`, `k≥1`, and `48(L+1)>L+2`. Thus all uses of the
quotient representation and distinctness are legitimate. This completes
the proof of Theorem C, including all constants and finite cases.

### 5.4 Resolving the explicit cancellation test family

**PROVED.** For the family `S=qY∪(qY+3t)`, `Y⊂Z_{≥1}`, the first
derivative energy vanishes at every `u_j`. The macro-profile equals

`|Y|[1+cos(tu)+cos(3tu)+cos(4tu)]`.

At `tu=5π/6` its value is `−|Y|(√3−1)/2`, and its second derivative
has absolute value at most `26t²|Y|`. The same nearest-grid argument gives

`M(A)≥|Y|[(√3−1)/2−13π²t²/q²]`.

For `q≥24t`, this is at least `|Y|/8=|S|/16`. For an elementary check
of the constants, use `√3>12/7`, `π²<10`, and
`5/14−65/288>1/8`. Thus the exact first-derivative obstruction itself
has a proved linear dip in this separated regime.

## 6. Adversarial checks and precise limitations

**PROVED — free rotation cannot simply be assumed.** Set `q=t=1`, `S={1}`.
This satisfies the 2-run hypotheses, but

`f_A(x)=2cos²x+cos x−1`, `M({1,2})=9/8`,

since `2c²+c−1=2(c+1/4)²−9/8` and `c=−1/4` is attainable.

The independent macro minimum is instead

`min_{u,θ}Re[(1+exp(iu))exp(iθ)]=−2`.

The grid error in (D) is essential.

**PROVED — complete derivative cancellation in admissible wider fibers.**
For `q>5t` and a finite nonempty `Y⊂Z_{≥1}`, take

`R={0,3t}`, `Y_0=Y_{3t}=Y`, `S=qY∪(qY+3t)`.

These are admissible 2-run sets: the within-block gap is `3t` and the
between-block gap exceeds `2t`. But
`C_y=1+exp(3πi)=0` for every occupied `y`. Thus `C=0`, the first
derivative at `π/t` vanishes identically, and (B) is uninformative.
This refutes `C≥c n` for general fibers, not OR(2)-weak.

**PROVED — signed levels break the analytic identity.** If `Y={−1,1}`,
then `F_Y(θ)=2cos θ` has identically zero imaginary part despite `|Y|=2`.
The proof above uses nonnegative levels and separates their constant term.

**PROVED limitation of scope.** No argument here puts arbitrary small-`M`
sets into a residue strip. E40's dense transversal regime need not satisfy
these hypotheses. Consequently this is a subclass result and does not
improve the universal run-top or Chowla exponent. It does not combine P24
with the 2-run structure by pretending P24 separates the copies; P24 is not
used at all. Its bounded-spread corollary was already known in the project
and is not claimed as new.

**CONJECTURED / unresolved:** unrestricted OR(2)-weak and structural
hypotheses forcing the residue representation for general near-extremizers.
The wider-residue first-derivative obstruction is genuine, but its exact
cancellation family is handled by §5. The earlier higher-derivative proposal
was superseded by the proved profile alternative, not left as an open claim.

## 7. Reproducible computation

**NUMERICAL**, with interval-certified finite checks as specified. All
substantive computation ran on `dirichlet` through

`src/dirun.sh -c 3 -m 6 -t 180 python .research/agents/or2_scratch/verify_or2.py`.

Code: `.research/agents/or2_scratch/verify_or2.py`.
Data: `.research/agents/or2_scratch/verification.json`.
Seed `20261018`; versions are saved in the JSON. No frequency optimization
or ILP was used. No processes belonging to the lead were modified or killed.

The first run passed 33 phase cases, covering `t∈{1,2,3,6,12}`, one,
two, or all allowed residues, and common, disjoint, or random quotient sets;
plus 98 exhaustive nonempty membership patterns for two residue classes and
levels `{1,2,3}` at `t=2,4`. Checks compare the lifted and direct cosine
evaluations, verify the macro zero and derivative formula, the sample
inequality, and the integrated derivative identity by independent
quadrature. The expanded run also passed four boundary cases with zero
levels or sharply unbalanced fibers, and the sharper weighted-curvature
form (D). Its maximum direct-vs-lift discrepancy was `2.00e−9`.
These are finite checks, not premises of the proof.

Three finite examples use the project's FFT/Newton evaluator and independent
128-bit Arb cosine evaluation at a rational angle. The first two also use
`src/chowla.py:certify_lower_bound` for an all-circle upper bound on `M`:

| `t` | `q` | residues | `n` | `|A|` | `max A` | finite bounds / evidence for `M` |
|---:|---:|---|---:|---:|---:|---|
| 1 | 48 | `{0}` | 3 | 6 | 385 | `[4.96161882188,4.96165901342]` |
| 2 | 136 | `{0,1}` | 6 | 12 | 1227 | `[8.02625300131,8.02627558079]` |
| 8 | 666 | `{0,1,4}` | 96 | 192 | 21324 | Arb point witness `M>80.42008131505`; FFT estimate `80.42008136318`; no all-circle upper bound computed |

The quotient sets and rational witness angles are saved in the JSON.
The lower endpoints come from rigorous point evaluations. The opposite
endpoints for the first two come from the existing Arb-DFT/Taylor project
certifier, with 128-bit balls and grid sizes 8192 and 32768. Its float padding
was not independently audited here. Neither the symbolic theorem nor its
proof relies on this certifier or on a numerical global minimum.

**NUMERICAL — wider-residue checks.** Run
`src/dirun.sh -c 3 -m 6 -t 180 python .research/agents/or2_scratch/verify_wide.py`.
Code and data are `or2_scratch/verify_wide.py` and
`or2_scratch/wide_verification.json`, seed `20261019`. The completed run
checks 80 fiber configurations with `t∈{1,2,3,4}`, `L∈{0,1,3,5}`,
including eight exact all-root cancellation cases. It checks the integer
formula for `C_*` against independent complex DFT sums, the projected
polynomial and reciprocal-grid identities, macro-profile inequalities,
and actual lifted sample points in the derivative lemma. The macro-minimum
estimate uses a curvature padding rather than promoting a grid minimum to
an exact one. These checks are floating evidence, not all-circle certificates
or exhaustive statements about the class. The latest run additionally
checks the stronger inequality (C3).

## 8. Strategic review and handoff

**PROVED progress:** a square-root bound for nearby residue classes, a
natural OR(2)-weak subclass with exponent `3/8`, and a quantitative
phase-coherence reduction; then the wider-residue square-root theorem C.
The useful Z feature is availability of all actual circle points: fixing
the quotient phase still leaves `q` genuine
sample points. Macro-curvature is independent of quotient heights. The
method uses exact vanishing of the pair factor instead of assuming free
rotation or local separation of the copies.

**PROVED obstructions retained:** free lifting fails without its grid error;
wider arcs can cancel all first-derivative energy; signed levels invalidate
the imaginary-part identity. None is a counterexample to the target.

**Decision:** keep these completed partial theorems. The explicit failure
of first-derivative energy led to a genuine pivot and theorem C, using a
finite-residue macro inequality rather than repeated search or unsupported
generalization. Do not replace `C` by `n` without the dichotomy. The first
concrete next derivation is to reduce the `k^(3/2)` loss in theorem C's
derivative branch by relating fiber counts to the curvature statistic `G`.
Another distinct route is to remove the bounded `R_*/t` hypothesis using
localized macro-profile tests. The separate dense-profile lower-bound and
construction tracks remain unresolved; no progress on them is asserted.

Only this report and files in `.research/agents/or2_scratch/` were
intentionally edited. No commits or subagents were used.
