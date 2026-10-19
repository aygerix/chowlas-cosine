# OR3 research report: arbitrary residue positions and the curvature loss

2026-10-18. Research report; proof and verification sections updated below.
Claims below are labelled individually.
Only this report and `or3_scratch/` are being edited; no commit is made.

## Exact target and starting frontier

The target is OR(2)-weak in Z: absolute `c,delta>0` such that
`M(S union (S+t)) >= c |S|^(1/4+delta)` for finite nonempty
`S subset Z_{>0}`, `t>=1`, with `S intersect (S+jt)=empty` for
`j=+/-1,+/-2`. A result with additional hypotheses is a subclass theorem,
not the unrestricted statement.

**PROVED (previous work, not new here):** OR2 Theorem C, with residues
`R subset [0,Lt]`, `B=L^2+(L+1)^2`, `J=2L+3`, `min S>=q`, and
`q>=16BJtk`, gives `M>=sqrt(n)/(32BJ^2 k^(3/2))`. The full proof in
`or2_report.md` and P24/P25/P27/P28 have been read.

**CONJECTURED / unresolved at the start:** removing dependence on residue
spread; improving the `k^(3/2)` loss; forcing residue structure for a
general near-extremizer. The second item is resolved below for bounded L.

## Research lines and falsification targets

1. **CONJECTURED candidate:** replace the coefficient-count step in the
   macro-profile dichotomy by a weighted energy inequality, so the
   derivative energy controls its own curvature denominator. First tests:
   common quotient fibres, highly unequal counts, and `{0,3t}` cancellation.
2. **CONJECTURED candidate:** localize to a residue cluster of diameter
   `O(t)` using a positive Fourier multiplier. First test: two clusters
   separated by `3t` with identical quotient fibres; cancellation must not
   be silently discarded. P24/P25 localize actual integer frequencies,
   not residues modulo q.
3. **CONJECTURED candidate:** a precise alternative using the P28 local
   maximal statistic yields a lower bound unless all windows share a
   common small exceptional phase set. The missing deterministic-to-Bohr
   implication will be stated explicitly if it cannot be proved.

## New result: the square-root loss in k

**PROVED — Theorem D (paper proof; not kernel-checked).** Let `L>=0` be
an integer, `B=L^2+(L+1)^2`, `J=2L+3`. Let `t,q>=1` be integers and
`S subset Z_{>0}` be finite nonempty, `n=|S|`, `min S>=q`. Suppose its
least nonnegative residues modulo q form `R subset [0,Lt]`, `k=|R|`,
and `S intersect (S+jt)=empty` for `j=+/-1,+/-2`. If

`q >= 16 B J sqrt(L+1) t sqrt(k)`,

then, for `A=S union (S+t)`,

`M(A) >= sqrt(n/k) / (32 B J^2 sqrt(L+1)).`                 (D)

This answers item 2 of the brief for the bounded-width class of Theorem C:
the power of k improves from `3/2` to `1/2`. For fixed L and any
`0<delta<=1/4`, `k<=n^(1/2-2delta)` implies
`M>=n^(1/4+delta)/(32 B J^2 sqrt(L+1))`. No conclusion for arbitrary
residue spread is yet claimed. The nonintegral threshold on q is an
ordinary real inequality imposed on an integer.

### Full proof

All integrals in theta below use normalized measure on `[0,2pi]`.
Only finite Fourier orthogonality, Taylor's inequality, and
Cauchy--Schwarz are used. The proof of the needed reciprocal-grid
identity is included, so no outside theorem is needed.

Write `S=union_r(qY_r+r)`, where each `Y_r subset Z_{>=1}` is finite,
`n_r=|Y_r|`, and `z_r(theta)=sum_{y in Y_r} exp(iy theta)`.
Absent residues have `n_r=z_r=0`. Orthogonality gives
`integral |z_r|^2=n_r`. Define

`h_theta(u)=Re[(1+exp(itu)) sum_r exp(iru) z_r(theta)]`,

`Lambda(theta)=sum_r [r^2+(r+t)^2] |z_r(theta)|`.

At every genuine sample `u=(theta+2pi j)/q`, `h_theta(u)=f_A(u)>=-M`,
where `M=M(A)`. This exact identity uses distinctness of the two copies.
Also `|h_theta''|<=Lambda`. At a global minimum of the periodic smooth
function `h_theta`, its derivative is zero. A sample lies within `pi/q`,
so Taylor's upper bound at that minimum proves, for every real u,

`h_theta(u) >= -M-e(theta)`,
`e(theta)=pi^2 Lambda(theta)/(2q^2)`.                       (D1)

Minkowski's inequality (or expanding squares and using Cauchy--Schwarz)
and `r<=Lt` give

`||e||_2 <= pi^2 B t^2 sqrt(k n)/(2q^2)`.                 (D2)

Crucially, average the *artificial macro-profile*, holding theta fixed:

`g_theta(v)=(1/t) sum_{a=0}^{t-1} h_theta((v+2pi a)/t)`
` = Re[(1+exp(iv)) sum_{h=0}^L z_{ht}(theta) exp(ihv)]`.

This is an identity for finite sums, and (D1) implies
`g_theta(v)>=-M-e(theta)` for all v. It does not assert that the averaged
points are themselves on the same real coset grid. That possible grid
incompatibility has already been paid for in e.

Put

`N=sum_{h=0}^L n_{ht}`,
`b_y=sum_{h=0}^L (-1)^h 1_{y in Y_{ht}}`,
`C_0=sum_{y>=1} b_y^2`,
`K(theta)=sum_{h=0}^L [h^2+(h+1)^2] |z_{ht}(theta)|`.

Thus `g_theta(pi)=0`,
`g_theta'(pi)=Im sum_{y>=1} b_y exp(iy theta)`, and
`|g_theta''|<=K(theta)`. A globally lower-bounded twice differentiable
function with value zero at pi and curvature bound K satisfies
`|g'(pi)|^2<=2K(M+e)`: if `K>0`, apply Taylor's upper bound at
`pi-g'(pi)/K`; if `K=0`, periodicity makes the derivative zero.
Integrating this inequality and using positive quotient levels gives

`C_0/2 <= 2M integral K + 2 integral K e`.

Here `integral K<=||K||_2<=B sqrt((L+1)N)`. Therefore, if `N>0`,

`M >= C_0/[4 B sqrt((L+1)N)] - ||e||_2`.                 (D3)

This is the improved curvature branch. Its denominator involves only
the fibres in the single residue class `0 mod t`, not all k residues.

To guarantee either useful C_0 or a macro dip, define

`H(u)=sum_r n_r[cos(ru)+cos((r+t)u)]`, `m=-min H>=0`.

The sign follows from `H((2j+1)pi/t)=0`. The nonnegative polynomial
`H+m` has mean `n_0+m`; its complex Fourier coefficient at `r+t>0`
is at least `n_r/2`. The absolute value of a Fourier coefficient of a
nonnegative function is at most its mean (triangle inequality in its
integral). Consequently

`n <= 2k(n_0+m) <= 2k(N+m)`.                             (D4)

For clarity the needed inequality from OR2 is now re-derived using C_0
alone. Average H over the t shifts, to get

`Hbar(v)=sum_{h=0}^L n_{ht}[cos(hv)+cos((h+1)v)]>=-m`.

The ratio `Q(v)=Hbar(v)/(1+cos v)` extends to a polynomial of degree
at most L, because

`[cos(hv)+cos((h+1)v)]/(1+cos v)`
` = (-1)^h [1+2 sum_{a=1}^h (-1)^a cos(av)]`.

Multiplication by `1+cos v` proves the identity by cancellation.
Thus `Q(0)=N` and `mean Q=Nalt=sum_h(-1)^h n_{ht}=sum_y b_y`.
There are at most N occupied positive y, so `Nalt^2<=N C_0`.
On the odd grid `v_j=2pi j/J`, the mean of Q is exactly Nalt and

`sum_{j=0}^{J-1} 1/(1+cos v_j)=J^2/2`.

Indeed `P(v)=sum_{a=0}^{J-1}(-1)^a exp(iav)` obeys
`(1+exp(iv_j))P(v_j)=2`; hence its squared modulus is
`2/(1+cos v_j)`, while discrete orthogonality gives
`sum_j|P(v_j)|^2=J^2`. At j=0, Q=N; elsewhere
`Q(v_j)>=-m/(1+cos v_j)`. Summing, and then applying
`J sqrt(N C_0)<=N/2+J^2 C_0/2`, proves

`N <= J^2 C_0+(J^2-1)m`.                                 (D5)

The macro dip transfers to actual points at theta=0. Here
`|H''|<=B t^2 n`, and `H(2pi j/q)=f_A(2pi j/q)`, so the same
nearest-grid Taylor argument gives

`M >= m - pi^2 B t^2 n/(2q^2)`.                          (D6)

There are now two cases.

* If `m>=n/(8kJ^2)`, the assumed lower bound on q makes the error in
  (D6) at most `pi^2 n/[512 B J^2 (L+1) k] <= n/(16kJ^2)`
  (use `pi^2<16`, `B(L+1)>=1`). Therefore
  `M>=n/(16kJ^2)`, which is stronger than (D) since `n>=k`.
* If `m<n/(8kJ^2)`, (D4) implies `N>=n/(4k)>0`, and
  `J^2 m<n/(8k)<=N/2`. By (D5), `C_0>=N/(2J^2)`.
  Hence (D3) gives
  `M >= sqrt(n/k)/[16 B J^2 sqrt(L+1)] - ||e||_2`.
  From (D2) and `q^2>=256 B^2 J^2 (L+1)t^2 k`,
  `||e||_2 <= [pi^2/(512 B J^2 (L+1))] sqrt(n/k)`
  `          <= sqrt(n/k)/[32 B J^2 sqrt(L+1)]`,
  using `pi^2<16<=16sqrt(L+1)`. This proves (D).

The q hypothesis also implies `q>(L+2)t`, so every representation above
lies within the stated residue range. Empty `0 mod t` fibres (`N=0`)
automatically fall into the macro case, and are never divided by N.
All zero-level problems are excluded by the explicit hypothesis
`min S>=q`. This completes the proof, including all constants.

**PROVED — concrete comparison at L=3.** Here `B=25`, `J=9`, so
`q>=7200t sqrt(k)` suffices for
`M>=sqrt(n/k)/129600`. In particular `k<=n^(1/4)` gives exponent
`3/8`; the former Theorem C required `k<=n^(1/12)` for that exponent.
More generally the new result applies with exponent `1/4+delta` up to
`k<=n^(1/2-2delta)`. These are subclass conclusions, with q and L
conditions retained.

**PROVED — data-dependent form, valid at arbitrary residue positions.**
Let `t>=1` be an integer, let `S subset Z_{>0}` be finite nonempty, and for any integer
`q>=1` use the least nonnegative residues `0<=r<q`
and quotient sets `Y_r subset Z_{>=0}` of S, excluding the zero frequency.
Assume `S intersect (S+t)=empty`. Define

`G_all=sum_r [r^2+(r+t)^2] sqrt(n_r)`,
`G_0=sum_{h:0<=ht<q} [h^2+(h+1)^2] sqrt(n_{ht})`,
`C_+=sum_{y>=1} |sum_{h:0<=ht<q}(-1)^h 1_{y in Y_{ht}}|^2`.

If `G_0>0`, then

`M(S union (S+t)) >= C_+/(4G_0)-pi^2 G_all/(2q^2)`.        (D8)

The proof is exactly (D1), the macro projection, and the integrated
derivative inequality, retaining the actual curvature sums rather than
their uniform bounds. Specifically `||e||_2<=pi^2 G_all/(2q^2)`,
`integral K<=||K||_2<=G_0`, and
`C_+/2<=2G_0(M+||e||_2)`. No bound on residue spread, no large-q
assumption, and no positive lower bound on the quotient levels are used
in (D8). It is a structural inequality, not a spread-free exponent bound:
the displayed error can be large. Its proof also shows that Theorems D
and D0 only need disjointness of S and S+t; the stronger 2-run hypotheses
in their statements were retained to match the brief.

## Removing the lower-height hypothesis as well

**PROVED — Theorem D0.** In Theorem D omit `min S>=q`, strengthen the
q hypothesis to

`q >= 24 B J sqrt(L+1) t sqrt(k)`,

and replace its conclusion by

`M(S union (S+t)) >= sqrt(n/k)/(64 B J^2 sqrt(L+1)).`        (D0)

All other hypotheses, including distinct positive frequencies and the
2-run conditions, remain as stated. This includes sets lying entirely
below q. There is no restriction on the largest quotient level.

**PROVED — full modifications of the proof.** Put `p=L+1`. Now the
quotient sets may contain zero, but `0 notin Y_0`. The constant coefficient
`b_0=sum_h(-1)^h 1_{0 in Y_{ht}}` is a real integer, with `|b_0|<=p`.
Define `C_+=sum_{y>=1} b_y^2`. Orthogonality of the imaginary part still
gives exactly `integral |g_theta'(pi)|^2=C_+/2`, since the real constant
has zero imaginary part. The bounds (D1)--(D4), and (D3) with C_+ in
place of C_0, therefore remain valid. In particular (D2) still holds:
orthogonality of `|z_r|^2` allows a constant term.

The reciprocal grid now gives

`N <= J Nalt+(J^2-1)m/2`,
`Nalt=b_0+sum_{y>=1}b_y <= p+sqrt(N C_+)`.

Using the same Young inequality and rearranging proves

`N <= 2Jp+J^2 C_+ +(J^2-1)m`.                            (D7)

Every nonempty admissible A has `M>=1/2`. To see this without any outside
theorem, choose `a in A` and integrate the product of the nonnegative
functions `M+f_A` and `1-cos(ax)`. Fourier orthogonality gives the integral
`M-1/2>=0`.

Write `x=n/k>=1`. If `x<=16Jp`, this bound implies (D0), since its
right side is at most `sqrt(J)/(16 B J^2)<=1/2`. Suppose instead
`x>16Jp`.

* If `m>=x/(16J^2)`, (D6) and the new q bound imply
  `M>=x/(16J^2)-pi^2 x/[1152 B J^2 p] >= x/(32J^2)`.
  Here `pi^2<16<=36Bp`. This is stronger than (D0).
* Otherwise (D4) gives `N>=x/4>0`; also
  `2Jp<x/8<=N/2` and `J^2m<x/16<=N/4`. Thus (D7) implies
  `C_+>=N/(4J^2)`. Using (D3) yields
  `M>=sqrt(x)/[32 B J^2 sqrt(p)]-||e||_2`.
  The new q bound gives
  `||e||_2<=pi^2 sqrt(x)/[1152 B J^2 p]`
  `       <=sqrt(x)/[64 B J^2 sqrt(p)]`, because
  `pi^2<16<18sqrt(p)`. This proves (D0).

This also checks the boundary `N=0`: it cannot enter the derivative case.
For `L=0` the forbidden zero frequency already excludes zero quotient
levels, and the argument is consistent with Theorem D.

## What fails when one tries to remove the residue width

**PROVED — exact positive-filter obstruction.** Let mu be a probability
measure on the circle and `w(a)=integral exp(iax) dmu(x)`. If `w(t)=1`
for a nonzero integer t, then `w(ht)=1` for every integer h. Indeed
`integral |exp(itx)-1|^2 dmu=2-2Re w(t)=0`; consequently
`exp(itx)=1` almost everywhere for mu. Raising to integer powers proves
the assertion.

Quantitatively, if `Re w(t)>=1-epsilon`, then

`Re w(ht)>=1-h^2 epsilon` for every integer h.              (F)

This follows by the geometric-series bound
`|exp(ihtx)-1|<=|h||exp(itx)-1|` and the same squared-modulus identity.
It applies to a discrete positive kernel on the q-root grid as well as
to an ordinary Fejer convolution kernel.

**PROVED — exact error in approximate localization.** Take a symmetric
probability measure on the q-root grid, with real q-periodic multiplier w.
Convolving f_A with it preserves the lower bound `-M`. At the lifted
sample points its artificial macro polynomial is

`Re sum_r [w(r)+exp(itu)w(r+t)] z_r(theta) exp(iru)`.

Writing this as
`Re[(1+exp(itu))sum_r w(r)z_r(theta)exp(iru)] + Delta_theta(u)`,
one has exactly

`Delta_theta(u)=Re[exp(itu)sum_r(w(r+t)-w(r))z_r(theta)exp(iru)]`,
`||sup_u |Delta_theta(u)||_{L2(theta)}`
`    <=sum_r |w(r+t)-w(r)|sqrt(n_r)`.                       (F2)

The equality is expansion of the two terms. For the bound, first use the
triangle inequality pointwise in u, then the triangle inequality in theta
L2 and `||z_r||_2=sqrt(n_r)`. This is also valid with zero quotient levels.
For a triangular cyclic Fejer multiplier of integer residue width
`1<=H<=q/2`, the right
side is at most `min(1,t/H)sqrt(kn)`, since cyclic distance is 1-Lipschitz.
The inequality is exact, but does not by itself make the error small
compared with the projected lower bound. Thus simply increasing the
window width, while using D's deteriorating L constant and this uniform
error bound, does not establish the proposed spread-free theorem.

In particular, a normalized positive convolution that preserves macro
frequencies 0 and t exactly cannot discard macro frequencies 3t and 4t.
Thus the proposed cluster localization cannot simply replace the full
macro-profile by the profile of one cluster while retaining both pair
coefficients 1. This is a certified obstruction to that *exact filtering
step*. It is not an obstruction to OR(2)-weak, to approximate filters with
controlled errors, or to the complete arbitrary-spread task.

**PROVED — dips of different clusters can cancel macroscopically.** For
the admissible common-fibre pattern `R={0,3t}`, the macro profile per
quotient point is, with `v=tu`,

`H(v)=1+cos v+cos(3v)+cos(4v)`
`    =2(1+c)(2c-1)(2c^2-1)`, `c=cos v`.

In fact `H(v)>=-1/2` for every v. Here is a complete elementary check.
The polynomial is nonnegative outside
`[-1,-1/sqrt(2)] union [1/2,1/sqrt(2)]`. On the first interval set
`a=1+c`, so `0<=a<1/2`. Then
`-H=2a(3-2a)(1-4a+2a^2)<=6a(1-3a)<=1/2`.
The first inequality uses `3-2a<=3`,
`1-4a+2a^2<=1-3a`, and nonnegativity of these factors on this interval.
On the second interval set `b=2c-1`, so `0<=b<1/2`. Then
`-H=(3+b)b(1-2b-b^2)/2 <=2b(1-2b)<=1/4`.
Both final inequalities are just completion of a square.

Yet the cluster `R={3t}` alone has profile `cos(3v)+cos(4v)`, whose
value at `v=pi/3` is `-3/2`. Hence its negative macro minimum is at
least three times that of the full profile. The support `{0,3t}` was
already the OR2 cancellation test; the explicit global `-1/2` bound
and its use against inherited cluster bounds are additional checks here.
There is no claimed finite or infinite Z obstruction with quarter-power M.
The macro comparison concerns theta=0, not the global minimum of the lifted
cosine sum.

**CONJECTURED / unresolved:** a positive localization with a sufficiently
small, correctly quantified error may still work. Theorem D0 has constants
depending on L; merely substituting `L=floor(q/t)` makes its q hypothesis
unusable for arbitrary residues. No removal of width dependence is proved.

## A precise structure-versus-randomness statement that does follow

**PROVED — common exceptional phase set.** This is an elementary
quantitative consequence of P25/P28, not a proof of a Bohr inverse theorem.
Let A be any finite nonempty set of distinct positive integers, `M=M(A)`.
Fix an integer `H>=1` and a finite nonempty family of integer centres
`mathcal M subset {H,H+1,...}`. Set

`P_m(x)=sum_{a in A}(1-|a-m|/H)_+ exp(iax)`,
`W(x)=max_{m in mathcal M}|P_m(x)|`,
`E_m=integral |P_m|^2=sum_a(1-|a-m|/H)_+^2`.

Integrals and measures here are normalized on the circle. For every
`V>0` and `0<eta<1`, there is a single measurable set Omega such that

`measure(Omega)<=4M^2/(eta V)`,
`integral_Omega |P_m|^2 >= (1-eta)E_m`

for every m in the family satisfying `E_m>=V`.

**PROVED — full proof.** P25 gives pointwise
`|P_m(x)|<=2M+2g_H(x)`, where `g_H=f_A*F_H` has mean zero.
Taking the finite maximum and integrating gives `integral W<=2M`.
Let `lambda=eta V/(2M)` (M is positive) and
`Omega={x:W(x)>=lambda}`. Markov's inequality, itself obtained by
integrating `W>=lambda 1_Omega`, gives the asserted measure bound.
On its complement, `|P_m|^2<=lambda |P_m|`, so

`integral_{Omega^c}|P_m|^2 <=lambda integral |P_m|`
`                              <=2M lambda=eta V<=eta E_m`.

Subtract from E_m. This proves simultaneous concentration for the whole
family, without a separate exceptional set for each window.

**PROVED — exact implication for a hypothetical OR2 counterexample.**
If `A=S union (S+t)`, `n=|S|`, and
`M<=c n^(1/4+delta)`, then, at every scale and for every finite window
family, the preceding statement holds with

`measure(Omega)<=4c^2 n^(1/2+2delta)/(eta V)`.

If `V=n^gamma` with `gamma>1/2+2delta`, this common exceptional set
has measure tending to zero. The formula follows by substitution and is
uniform in the number of windows. If the bound is above 1 it is, of
course, vacuous.

**CONJECTURED / precise middle case still missing.** Neither simultaneous
concentration on a small measurable phase set nor a large structured
subset proves that all of S lies in a residue strip. To apply D/D0 one
needs such a representation for the full set, or a positive localization
that transfers its lower bound. Deleting arbitrary frequencies is not
monotone for M. The remaining middle case consists of sets with small M
whose sufficiently energetic windows all concentrate on common small
phase sets, but for which no modulus/strip representation or transferable
localized representation has been proved. The measure statement contains
no assertion that Omega is a Bohr set or a set of almost-periods. In
particular, replacing that missing assertion by the phrase "no large
almost-periods" would not complete item 3.

## Strategic review and handoff

**PROVED / decision after two different routes:** retain the real-grid
mechanism but change the curvature branch: average out the irrelevant
macro residue classes *after* controlling the grid error, rather than
integrating their curvature cost. This resolves the requested k loss.
Discontinue the exact positive-filter deletion step, which (F) disproves.
Keep approximate localization open with its coefficient errors explicit.

**CONJECTURED / next three distinct lines:** (i) arbitrary residue
localization with quantitative pair-coefficient errors; (ii) an inverse
theorem converting the common phase concentration above into transferable
structure; (iii) adversarial construction using widely separated residue
clusters to evade the bounded-width theorem. None is represented as solved.

**CONJECTURED / first concrete next derivation:** improve (F2) using the
actual distribution of fibre mass in the taper, or a cancellation property
of its coefficient differences, so the error is small relative to the
gain after projection. The uniform `sqrt(kn)` estimate above does not
close this comparison. This is a specific extension problem, not a
claimed continuation process.

## Reproducible verification

**NUMERICAL — completed.** Code is
`or3_scratch/verify_or3.py`, seed `20261018`, invoked only via

`src/dirun.sh -c 2 -m 4 -t 180 python .research/agents/or3_scratch/verify_or3.py`.

Data: `or3_scratch/verification.json`. Versions: Python `3.12.3`,
NumPy `2.5.4`, SciPy `1.18.1`. The completed run passed 125 cases:

* 80 random fibre configurations, with `t in {1,2,3,6,12}`,
  `L in {0,1,3,5}`, four trials each; every fibre obeys the 2-run exclusions.
* Seven common, disjoint, unbalanced, short-arc, no-`0 mod t`, and
  arithmetic-progression configurations, including steps `3t` and `3t/2`.
* Three explicit zero-quotient-level configurations, including one with all
  points below q and one with large positive-level mass plus a zero fibre.
* All 35 nonempty choices of admissible fibre subsets of `{0,1,2,3}`
  at quotient levels `{1,2}`, with `t=1` (a complete finite membership test).

Ten cases had `C_+=0`; one had no residues divisible by t. Seventy-three
cases had `t not dividing q`, testing that the macro projection does not
illegitimately treat the t shifts as genuine samples on the same coset
grid. The macro branch was selected in 101 cases. Maximum absolute
errors were `2.65e-10` for independent direct-versus-lifted cosine values,
`8.99e-13` for the projected formula, `6.78e-15` for the derivative at pi,
and `1.36e-13` for the independent derivative-energy quadrature.

These are NUMERICAL identity and inequality checks. For practical memory
use, their test moduli are `q=8(L+2)t+1`, generally below the sufficient
threshold in D/D0; each record separately saves the actual sufficient q.
The script checks the general grid-error and projection identities, not
a finite exhaustive verification of the theorem at all admissible q. Macro
minima from numerical minimization are explicitly uncertified. No upper
bound on the global M of a Z construction is inferred from them.

**PROVED / exact auxiliary checks:** integer polynomial arithmetic verifies
the quotient identity for degrees `h=0,...,12`. In addition to the complete
analytic proof above, rational Bernstein coefficients independently certify
`1+T_1(c)+T_3(c)+T_4(c)+1/2>0` on `[-1,1]`. The JSON saves the five rational
subintervals and all degree-4 Bernstein coefficients. The smallest of all
saved coefficients is `1/24>0`. To check the certificate, substitute
`c=a+(b-a)s`; the polynomial is `sum_{i=0}^4 b_i binom(4,i)s^i(1-s)^(4-i)`
with every b_i positive, so it is positive on each interval. The five
intervals partition `[-1,1]`. This auxiliary certificate concerns the macro
cancellation example, and is not advertised as a lifted finite example or
an obstruction to OR(2)-weak.

**PROVED / independent exact certificate audit:**
`or3_scratch/audit_or3.py` reconstructs the polynomial in the original
variable from each saved Bernstein expansion, using a different calculation
from the forward conversion in the verifier. It checks all five rational
identities exactly, the interval partition, and the minimum coefficient
`1/24`. In fact the certificate proves the stronger bound `H>=-11/24`.
The result is saved in `or3_scratch/audit.json`.

**NUMERICAL — additional localization audit:** the same audit script, seed
`20261019`, checks (F2) independently on all 125 stored configurations,
including that the discrete kernel has nonnegative weights and mass one
up to floating error. The largest expansion error was `1.07e-14`; the
largest sampled L2 error divided by the proved bound was `1.0`. This uses
only a finite u grid for that numerical check; the continuous supremum in
(F2) is justified by its paper proof. The audit ran via

`src/dirun.sh -c 2 -m 4 -t 120 python .research/agents/or3_scratch/audit_or3.py`.

**NUMERICAL / execution history:** the first two attempts stopped on an
unavailable optional SymPy import
and a scalar-versus-array initialization in the verifier. The verifier
now uses only the VM's existing NumPy/SciPy and Python rational arithmetic;
no VM package was installed or shared environment changed. These failures
did not produce mathematical counterexamples. All computations used
`dirichlet`, at most two cores and 4 GB; no jobs belonging to anyone else
were modified or killed. No other research documents or source files were
intentionally edited, and no commit was made.

**PROVED / final status:** D, D0, D8, F, F2, and the common-phase-set lemma
have complete paper proofs in this report. They have not been Lean
formalized or independently reviewed by another agent. No external novelty
claim is made. Item 2 of the brief is answered for bounded L; items 1, 3's
Bohr inverse step, and 4 remain unresolved. Neither Chowla nor unrestricted
OR(2)-weak is claimed to be settled.
