# P31 adversarial review and Nikolskii lemma

Completed adversarial review. All paper proofs below are independently derived here; none is kernel-checked.
Only this report and `p31_scratch/` were edited; no commit was made. Every computation ran on dirichlet through
`src/dirun.sh`, with at most four cores. The brief's notation `n=|A|` is preserved; `N=L+1` is used only in the
Nikolskii proof.

## Errors identified at the first audit

**PROVED.** The principal displayed P31 inequality has no error in its Fejér–Riesz/averaging derivation, provided its Nikolskii polynomial is **analytic**, with frequencies `0,...,L`. The phrase “every trigonometric polynomial of degree <= L” is incorrect under the ordinary two-sided convention. Smallest counterexample to that equivalence: `L=1`, `U=1+2 cos x`; its fourth/second norm ratio is `19/9 > (L+1)rho_L=3/2`.

**PROVED.** A bound `rho_L <= 0.95` for **all** `L>=0` is impossible: `rho_0=1`. The nontrivial uniform range must start at `L=1`.

**PROVED.** P31(iii) drops a factor `1+epsilon`. At a fixed scale the derivation gives a threshold `2 delta/[rho(1+epsilon)]`, not `2 delta/rho`. This distinction is material at `epsilon=1`; details and exact finite formulas follow below.

**PROVED.** The P29 corollary as printed needs the positive part: `(n-X/2)_+^2/(2X)`. Without it, `A={12}` has `M=1` but the asserted lower bound is `25/24`. This is the smallest singleton counterexample: for `A={X}`, the asserted bound exceeds 1 exactly when `X^2-12X+4>0`, hence first at `X=12`. No minimality over all sets is claimed. This correction does not affect P29 in its intended dense regime.

**PROVED.** For the two-sided-polynomial counterexample above, `rho_1=3/4`: if `v=(a,b)`, then
`||v*v||_2^2=(a^2+b^2)^2+2a^2b^2 <= (3/2)(a^2+b^2)^2`, with equality when `a=b`.
For `U=1+2cos x`, `||U||_2^2=3` and `||U||_4^4=19`. This is the smallest possible degree of a counterexample
to the claimed two-sided equivalence; degree zero is constant. Fejér–Riesz supplies an analytic U, so it does
**not** refute the principal displayed P31 inequality.

**PROVED, scope of the third correction.** I have found an error in the derivation/statement of P31(iii), not an
actual Chowla-counterexample family violating it. No such family is produced or assumed to exist here.

## Results and remaining gap

**PROVED.** The principal P31 inequality survives; P31-N is proved below with an explicit rate and an elementary
finite-range bound. Corrected consequences (i)–(iii), an explicit dense-set constant, and two effective-degree
results are given below. **NUMERICAL.** All 23 requested-type adversarial examples passed 161 window tests.
**CONJECTURED / unresolved.** `rho_L -> approximately 0.687`, a certified upper bound below `4/(3sqrt(3))`, and
square-root lower bounds for the remaining steep tapered class are not established. No SDP or global QCQP
certificate is claimed. The proof uses a limsup and does not presume existence of a limit of `rho_L`.

## PROVED: P31-N by exact sinc interpolation

Write `N=L+1`, `beta=A_(4/3)^4=4/(3 sqrt(3))`. For every `R>0`,

`rho_(N-1) <= beta/N * [(N-1+2R)^(1/3) + (6/pi^(4/3)) R^(-1/3)]^3`.

Consequently, with `R=sqrt(N)`,

`rho_(N-1) <= beta [1+(2/3+6/pi^(4/3))/sqrt(N)]^3 <= beta(1+2/sqrt(N))^3`.

This is an explicit `O(N^(-1/2))` bound; the final inequality follows from `pi>31/10`, giving `6/pi^(4/3)<4/3`.

Normalize a complex vector `u` by `sum |u_j|^2=1` and put `B(t)=sin(pi t)/(pi t)`,
`h_theta(t)=sum_(j=0)^(N-1) u_j exp(ij theta) B(t-j)`.
Use the Fourier convention `hat h(xi)=integral h(t)exp(-it xi)dt`. Then
`hat h_theta(xi)=1_[-pi,pi](xi) sum_j u_j exp(ij(theta-xi))`. Plancherel gives exactly

`||h_theta||_2^2=1`, `||h_theta*h_theta||_2^2=||u*u||_ell2^2=:E`,

for every theta. There are no aliasing or truncation errors. The convolution identity is valid by the Fourier convolution theorem (or by approximation); each finite sinc sum is in `L^(4/3) intersect L^2`, and its Fourier transform is bounded and compactly supported.

On `I=[-R,N-1+R]`, Holder gives `integral_I |h_theta|^(4/3) <= |I|^(1/3)`.
Modulation orthogonality and concavity give

`average_theta |h_theta(t)|^(4/3) <= [sum_j |u_j|^2 |B(t-j)|^2]^(2/3)`.

Outside I the bracket is at most `1/(pi^2 dist(t,[0,N-1])^2)`. Integrating the two tails gives at most
`6 pi^(-4/3) R^(-1/3)`. Thus some theta satisfies
`||h_theta||_(4/3)^(4/3) <= |I|^(1/3)+6 pi^(-4/3)R^(-1/3)`.
Sharp Young, `||h*h||_2 <= A_(4/3)^2 ||h||_(4/3)^2`, now proves the displayed bound after squaring.
The only non-elementary dependency is Beckner's sharp Young inequality, cited precisely in the final source section.

## PROVED: a uniform finite-degree gap

`rho_0=1`, and `rho_L <= 19/20` for every `L>=1`.

Here is an elementary proof independent of sharp Young. Put `N=L+1>=2`, let `v>=0`, `||v||_2=1`, and
`e=(1,...,1)/sqrt(N)`. Write `v=a e+z`, `z perpendicular e`, `d=||z||_2^2=1-a^2`.
Ordinary Young gives `E(v):=||v*v||_2^2 <= ||v||_1^2=N a^2`. If `a^2<=19/20` we are done.
Otherwise `d<1/20`. The following exact estimates hold:

1. `E(e)/N=(2N^2+1)/(3N^2)<=3/4`.
2. `||e*z||_2^2=(2/N)sum_(k=0)^(N-2) (sum_(j=0)^k z_j)^2 <= (N^2-1)/(3N)||z||_2^2 <= Nd/3`.
   Indeed the squared norm of the projection of `1_{0,...,k}` onto `e^perp` is `(k+1)(N-k-1)/N`; sum these bounds.
3. `||z*z||_2 <= sqrt(N)d` by ordinary Young and Cauchy--Schwarz.
4. For `g_j=N^(-3/2)[N(N+1)/2+j(N-1-j)]`, `inner(e*e,e*z)=inner(g,z)` and
   `||g-E(e)e||_2^2=(N^2-1)(N^2-4)/(180N^2)<=N^2/180`.
5. `|inner(e*e,z*z)|<=||e*z||_2^2` by Fourier Cauchy--Schwarz / pointwise absolute values.

Expand `v*v=a^2(e*e)+2a(e*z)+(z*z)` and use these estimates and `a<=1`. Then

`E(v)/N <= 3/4 + (4/sqrt(180))sqrt(d)+2d+(4/sqrt(3))d^(3/2)+d^2`
`< 3/4+1/15+1/10+1/(5sqrt(60))+1/400 < 19/20`.

For the last strict inequality use `1/(5sqrt(60))<3/100`, which gives `1139/1200<19/20`.
The formula in item 4 follows by summing the first four powers of `j`; its finite checks on the VM are recorded below.
Thus an explicit combined bound is `rho_0=1` and, for `N>=2`,

`rho_(N-1) <= min(19/20, beta(1+2/sqrt(N))^3)`.

**PROVED, explicit combination.** In particular,

- `rho_0=1`;
- `rho_L<=0.95` for `1<=L<249999`;
- `rho_L<=0.78` for `L>=249999`.

Indeed `beta<77/100` and `(77/100)(251/250)^3<39/50` are exact algebraic/rational inequalities, and
`N>=250000` gives `2/sqrt(N)<=1/250`. The sharper computed expression at this threshold is approximately
`0.779074962911` (NUMERICAL decimal only). Also
`rho_L <= beta + beta[6/sqrt(N)+12/N+8/N^(3/2)]`, so the rate and all constants are explicit.

**PROVED, why the lead's truncation paragraph was incomplete.** Superpolynomial decay of an unspecified smooth
cutoff does not by itself supply a uniform truncation error at `O(T log T)` for every vector length. An actual
derivative/tail bound, its constants, and dependence on `||u||_1` would be needed. The sinc proof replaces that
step with an exact Fourier isometry and an explicit integrable tail estimate. It has no unspecified cutoff,
truncation length, or hidden error term.

## PROVED: full audit of the principal P31 inequality

All circle integrals in this report use `dx/(2pi)`. Let A be finite and nonempty, with distinct positive integer
frequencies, `X=max A`, `n=|A|`, and `f=sum_(a in A) cos(ax)>=-M`. Let `w>=1` be an integer,
`kappa(k)=(1-|k|/(w+1))_+`, `F=sum_k kappa(k)e^(ikx)`, and `L=X+w`.

The correct Nikolskii statement is for `U(x)=sum_(j=0)^L u_j e^(ijx)`. Parseval and the coefficientwise triangle
inequality give

`||U||_4^4=||u*u||_ell2^2 <= || |u|*|u| ||_ell2^2 <= rho_L (L+1)||u||_ell2^4`.

Conversely a maximizing nonnegative vector realizes that constant, so the analytic formulation and definition
of rho_L are equivalent. Existence of a maximum follows by compactness of the nonnegative unit sphere.

For each `x0`, `h(x)=F(x-x0)(f(x)+M)` is real and nonnegative with Fourier support in `[-L,L]`. The kernel has
degree w, not w+1. Fejér–Riesz gives `h=|U|^2` for an analytic U supported on `0,...,L`; zeros of h are allowed.
Thus

`integral h^2 <= rho_L(L+1)(integral h)^2`.

There is no measurability issue about choosing the factors U as x0 varies: the conclusion contains only h,
which is continuous in `(x,x0)`. Average this conclusion over x0. Fubini gives

`average_x0 integral_x h^2 = (integral F^2)(integral (f+M)^2)=W(n/2+M^2)`.

Orthogonality of the distinct nonzero frequencies gives `integral f=0`, `integral f^2=n/2`, and

`s(x0):=integral_x h(x)=M+sum_(a in A) kappa(a) cos(a x0)`,

`average_x0 s(x0)^2=M^2+S_A/2`.

In particular the factors of 1/2 in the brief are correct. Therefore, for every such A and w,

`W(n/2+M^2) <= rho_L(L+1)(M^2+S_A/2)`.

Exactly,

`W=1+2sum_(k=1)^w (1-k/(w+1))^2 = 2(w+1)/3+1/[3(w+1)]`,

`0<=d:=2S_A/W<=1-1/W<1`.

Put `C_L=rho_L(L+1)`. It satisfies `C_L>W`: the constant vector on `L+1` coordinates gives
`C_L >= q(L+1)`, where `q(t)=2t/3+1/(3t)` is strictly increasing for integers `t>=1`, while `W=q(w+1)` and
`L+1>w+1`. This verifies the denominator assertion without assuming any numerical estimate on rho_L.

Any certified `C>=C_L` also satisfies `C>W`, and the exact usable bound is

`M^2 >= [W n-C S_A]/[2(C-W)]`.                                      (1)

When the numerator is negative this only gives a negative lower bound; one may replace its right side by zero.
Using a numerical **lower** bound on rho_L in place of an upper bound is not a rigorous use of (1).

## PROVED: corrected consequences, with constants and scale dependence

For the finite formulas define `delta=n/X`, `alpha=W/X`, `q=C/X`, and `d=2S_A/W`. Equation (1) becomes exactly

`M^2/n >= alpha/[2(q-alpha)] * [1-q d/(2delta)]`.                    (2)

This is useful precisely when the bracket is positive. Suppose `0<epsilon<=1`, `epsilon X>=1`,
`w=floor(epsilon X)`, and a certified bound `rho_L<=r` is available. Take `C=r(X+w+1)`. Then

`alpha >= 2epsilon/3`, `q <= r(1+epsilon+1/X)`.

**PROVED, consequence (i), exact finite margin.** If `0<eta<1` and

`d <= (1-eta) 2n/C`,

then

`M^2 >= eta W n/[2(C-W)] >= [eta epsilon/(3r(1+epsilon+1/X))] n`.   (3)

For fixed epsilon and a fixed margin eta this is a square-root bound even when delta tends to zero.
The density hypothesis must hold *relatively* to delta; an unspecified absolute `o(1)` error in d is
insufficient at very small delta. A roughly uniform profile has `d/delta approximately 1` and satisfies (3)
at sufficiently small fixed epsilon, provided this approximation has a fixed relative margin.

**PROVED, asymptotic expression.** As X tends to infinity at a fixed epsilon, the leading expression in (2) is

`(epsilon/3) [1-r(1+epsilon)d/(2delta)]/[r(1+epsilon)-2epsilon/3]`.

The finite equation (2) is preferable to treating this expression as an inequality with unexplained errors.
The fixed-scale threshold is `2delta/[r(1+epsilon)]`. Describing it as `2delta/r` is legitimate only as the
limit of arbitrarily small fixed scales, with an explicit margin. For epsilon=1 the threshold is `delta/r`.

**PROVED, consequence (ii), exact finite margin.** Since `d<=1`, if

`n >= (1+eta)C/2`,

then (3) holds with eta replaced by `eta/(1+eta)`. It is sufficient that

`delta >= [r/2](1+epsilon+1/X)(1+eta)`.

Since P31-N permits every fixed `r>beta` for all sufficiently large L, for every fixed
`delta0>beta/2=2/(3sqrt(3))` there is an explicit positive `c(delta0)` such that

`M(A)>=c(delta0)sqrt(|A|)` whenever `|A|>=delta0 max(A)`.

To make the parameters effective, choose `beta<r<2delta0`, then epsilon and eta positive with
`[r/2](1+epsilon)(1+2eta)<=delta0`. It suffices to take X at least

`max{1/epsilon, [2/((r/beta)^(1/3)-1)]^2, (1+eta)/[(1+epsilon)eta]}`,

rounded up. For smaller X use `M>=1/2`, which follows because the nonzero Fourier coefficient `1/2` of
the nonnegative polynomial `f+M` has modulus at most its mean M. Thus a single explicit constant is

`c(delta0)=min{sqrt[eta epsilon/(3r(1+eta)(2+epsilon))], 1/(2sqrt(X0))}`,

where X0 is the rounded-up displayed threshold. At epsilon=1 the sufficient asymptotic density threshold
is r, not r/2. The number `0.384900...` requires small fixed epsilon.

**PROVED, completely numerical universal example.** Every A with `|A|>=(2/5)max A` satisfies

`M(A)>=(1/1000)sqrt(|A|)`.

For `X>=250000`, take `r=0.78`, `epsilon=1/100`, and `eta=1/100`. Then `C<X`,
`(1+eta)C/2<0.4X`, and `W>=X/150`. Hence (1) gives `M^2>=n/30300`, which is stronger than required.
For `X<250000`, `M>=1/2` and `n<=X` finish the proof. This is a consequence of P31, not a claim to resolve
the unrestricted Chowla problem.

**PROVED, consequence (iii), correct relative form.** For every A,w and certified `C>=C_L`, dropping the
nonnegative term `W M^2` from the left of P31 gives

`d/delta >= 2X/C - [4X/W](M^2/n)`.                              (4)

Thus if `n->infinity`, `M^2/n->0`, and epsilon is fixed positive, P31-N implies

`liminf (d_epsilon/delta) >= 2/[beta(1+epsilon)]`.

One can first use any fixed `r>beta`, then let r decrease to beta. More generally any asymptotic upper
bound r for rho gives `2/[r(1+epsilon)]`. This remains valid for delta tending to zero. It does **not**
give `2/r` at every fixed epsilon. It does give `2/r` after the additional small-scale limit.

## NUMERICAL: adversarial VM tests and independent checks

Reproduce from the repository root:

```sh
src/dirun.sh -c 4 -m 4 -t 600 python .research/agents/p31_scratch/audit.py
src/dirun.sh -c 2 -m 2 -t 120 python .research/agents/p31_scratch/verify.py
```

Artifacts: `p31_scratch/audit.py`, `eval.c`, `audit_results.json`, `rho_lower_bounds.json`, `verify.py`, and
`verification_results.json`. Python 3.12.3 and NumPy 2.5.4 were recorded by the VM output file (consult that file
for the authoritative version strings). Sampling seed: 310019; independent identity-check seed: 310020.

Sets were checked for positive distinct frequencies. The minimum estimator uses an FFT grid of more than 16X
points and scalar refinement at its 48 deepest sampled local minima on `[0,pi]`, including endpoints. The second
evaluator uses C `long double` cosine summation. For Bu sets scalar refinement uses the independently checked
two-sided-square identity from `src/bu.py`, greatly reducing its cost. The largest FFT/direct discrepancy at
the checked grid points was `1.84e-8`, and the largest Bu/direct discrepancy was `8.38e-11`.

For each example, seven windows were used: `w=max(1,floor(epsilon X))`, with epsilon in
`{.01,.05,.1,.25,.5,1,2}`. The fourth column below is an estimate of the global M, **not** a new all-circle
certificate. The proved-P31 column is the largest lower-bound formula over these windows using
`r=min(.95,beta(1+2/sqrt(L+1))^3)`, evaluated numerically. The last column substitutes the **unproved** constant
0.687 and is shown only to distinguish a sharper conjectural constant from the proved one.

| case | n | X | estimated M | proved-P31 formula | unproved rho=.687 formula |
|---|---:|---:|---:|---:|---:|
| singleton 1 | 1 | 1 | 1.000000 | 0.540062 | 0.936842 |
| singleton 12 | 1 | 12 | 1.000000 | 0.532886 | 0.749058 |
| interval 32 | 32 | 32 | 7.565720 | 1.318248 | 2.278962 |
| interval 128 | 128 | 128 | 28.415943 | 2.439121 | 4.398745 |
| interval 512 | 512 | 512 | 111.832591 | 4.787944 | 8.717146 |
| random density .1 | 56 | 499 | 14.570747 | 1.730422 | 2.991761 |
| random density .35 | 186 | 510 | 28.718068 | 2.010232 | 4.812536 |
| random density .7 | 375 | 512 | 78.967059 | 3.909901 | 7.389211 |
| tapered p=1 | 1011 | 1993 | 43.074173 | 1.938943 | 5.511174 |
| tapered p=2 | 666 | 1894 | 40.944552 | 0 | 0.543809 |
| tapered p=4 | 440 | 1490 | 35.011572 | 0 | 0.316480 |
| tapered p=8 | 236 | 916 | 23.461836 | 0 | 0 |
| powers of 2 | 13 | 4096 | 6.704039 | 0 | 0 |
| powers of 3 | 9 | 6561 | 9.000000 | 0 | 0 |
| core 128 + 4 tails | 132 | 52810 | 31.307694 | 0 | 0 |
| core 128 + 32 tails | 160 | 64937 | 40.294211 | 0 | 0 |
| N50_x72 | 50 | 72 | 4.030936 | 0.935669 | 1.874417 |
| N50_x71 | 50 | 68 | 4.048311 | 1.040291 | 2.031605 |
| Singer differences q=7 | 28 | 55 | 4.000000 | 0.897031 | 1.594573 |
| Singer differences q=31 | 496 | 991 | 15.999977 | 1.611640 | 4.931689 |
| Bu q=61 | 3782 | 10707 | 37.146016 | 4.361686 | 9.151719 |
| Bu q=101 | 10302 | 30575 | 59.730819 | 7.133128 | 14.344785 |
| Bu q=401 | 161202 | 483272 | 222.262857 | 40.241831 | 62.328669 |

No violation was found in these 23 cases / 161 windows. The largest required ratio
`W(n/2+M_est^2)/[(L+1)(M_est^2+S_A/2)]` was `2/3` (singleton 1). This experiment does not compute the exact
rho_L or certify all x. The two dense records and Bu records retain their **pre-existing** upper bounds on M
from the JSON files specified in the brief; those certificates were read, not independently re-proved here.
For example Bu q=401 has the pre-existing `M<=222.292595400`, consistent with the estimate above.

Independent finite-Fourier checks used five sets and three windows each. On grids large enough for exact
Fourier integration in exact arithmetic, the numerical mean-of-h, mean-of-h-squared, mean-of-s-squared and W
identities had maximum discrepancy `4.55e-13`. Exact rational checks of the uniform-proof power-sum identities
passed for `N=2,...,64`. A random complex coefficient sinc/Fourier check gave L2 `0.9999999999999999` and energy
discrepancy `2.23e-16`. These are cross-checks of the paper derivations, not substitutes for them.

Four-start L-BFGS runs reproduced lower bounds for rho at `N=2,3,5,10,20,50,120`:
`0.75, 0.7142857143, 0.6966900439, 0.6893961318, 0.6875842395, 0.6870777303, 0.6869980344`.
These are **NUMERICAL LOWER BOUNDS** on the suprema, not upper bounds. There is no certified monotonicity
argument in this report, and no promotion of these optimizer results to a proof of the limiting constant.

## PROVED: effective-degree results, and a precise smoothing obstruction

### Removing a genuinely sparse tail by cardinality

Let `A=B disjoint-union T`, with `r=|T|`. At a minimizing point for f_B,
`f_A<=-M(B)+r`; therefore

`M(A)>=M(B)-r`.                                                   (5)

This bound is independent of the largest tail frequency. Any core theorem `M(B)>=c sqrt(|B|)` transfers when
`r<=c sqrt(|B|)/2`, giving `M(A)>=c sqrt(|B|)/2`. In particular it handles arbitrarily remote tails of
`o(sqrt(|B|))` frequencies without inflating the degree in P31.

For the requested full interval core, substantially more holds. If `B={1,...,Y}`, evaluate at
`x=3pi/(2Y+1)`. The Dirichlet identity gives exactly

`f_B(x)=-1/2-1/[2sin(3pi/(4Y+2))]`.

Since `sin t<=t`, for every `Y>=1`,

`M(A)>=1/2+(2Y+1)/(3pi)-r >= 2Y/(3pi)-r`.                        (6)

Thus `r=o(Y)` gives a linear negative dip, despite `max A` being arbitrarily larger than Y. This entire
interval-core escape class is excluded as a candidate for `M/sqrt(n)->0`. The numerical core128 examples
illustrate the limitation of the original P31 degree, while (6) supplies a degree-free explanation.

### Exact positive low-pass version of P31

For any integer H>=2, positivity of convolution with F_H gives

`M+g_H := (M+f_A)*F_H >=0`,
`g_H(x)=sum_(a in A, a<H) (1-a/H) cos(ax)`.

Here F_H has degree H-1 and mean 1. Apply the already-proved argument to g_H: the equal-coefficient assumption
is used only for the second moments, so replacing it by these real coefficients gives, with
`b_a=(1-a/H)_+ 1_A(a)`, `E_H=sum b_a^2`, `S_H,w=sum b_a^2 kappa_w(a)^2`, and `D=H-1+w`,

`W_w(E_H/2+M^2) <= rho_D(D+1)(M^2+S_H,w/2)`.                     (7)

This is a rigorous effective-degree inequality: frequencies at or above H do not occur at all, even in D.
It holds for every A, with no tail-size assumption.

### Why this low-pass version cannot prove the interval-core target

If A contains `{1,...,H-1}`, then `g_H=(F_H-1)/2`, so its own negative minimum is at most 1/2,
while `E_H=sum_(a=1)^(H-1)(1-a/H)^2 = (H-1)(2H-1)/(6H) approximately H/3`.
Consequently (7) cannot force a square-root lower bound from this filtered polynomial alone: the same
inequality is already valid with `M=1/2`, which bounds any positive lower bound obtained from it by 1/2.
This is an exact obstruction, not a failed numerical optimization. More generally a nonnegative mean-one
kernel K with Fourier support `[-H+1,H-1]` sends a full low-frequency core to `(K-1)/2`, again bounded below
by -1/2. Positive compact low-pass smoothing loses the very dense-core negativity one hoped to preserve.

**CONJECTURED / unresolved.** A useful multiscale extension must retain additional information coupling the
filtered polynomial to the original 0/1 coefficients, or exploit cross-scale terms. Equation (7) alone does
not control tapered profiles with p>=2. No such missing cross-scale estimate is claimed here.

## CITED: literature and novelty audit

**CITED, verified dependency.** W. Beckner, *Inequalities in Fourier analysis*, Annals of Mathematics 102
(1975), 159–182, Theorem 3 (p.169), proves sharp Young for Euclidean convolution. The needed specialization is
`||h*h||_2<=A_(4/3)^2||h||_(4/3)^2`, including complex h (or apply the nonnegative theorem to |h|).
The dimension is one and the exponents obey `3/4+3/4=1+1/2`; `A_p=[p^(1/p)/(p')^(1/p')]^(1/2)`.
Source: [publisher record](https://annals.math.princeton.edu/1975/102-1/p11),
[author-paper scan, Theorem 3](https://www1.cmc.edu/pages/faculty/MONeill/Math%20138/papers138/Beckner.pdf).

**CITED, directly relevant prior art missed in the repository's quick dense-case search.** M. N. Kolountzakis,
*The density of B_h[g] sequences and the minimum of dense cosine sums*, Journal of Number Theory 56 (1996),
4–11, Theorem 2, already proves `M>=C epsilon^2 N` for distinct frequencies bounded by `(2-epsilon)N`
(epsilon>3/N in the displayed theorem). Its proof multiplies the nonnegative cosine polynomial by a Fejér
kernel and uses Fejér's peak/mean bound, explicitly derived from Fejér–Riesz. Thus the density-above-1/2
mechanism of P29 is classical, and the multiplication/factorization framework of P31 has a direct predecessor.
The paper's displayed bound is linear above density 1/2; it does not state P31's averaged second-moment
inequality or its density threshold beta/2. Source: [author's paper, §2](https://eigen-space.org/mk/ps/dense.pdf),
[publisher](https://www.sciencedirect.com/science/article/pii/S0022314X96900025).

**CITED, verified limitation.** E. Levin and D. S. Lubinsky, *Asymptotic behavior of Nikolskii constants for
polynomials on the unit circle*, January 2015 manuscript, define
`Lambda_(N,p,q)=inf_(deg P<=N-1) ||P||_p/||P||_q` with normalized circle measure. Their Theorem 1 gives
`limsup N^(1/p-1/q)Lambda_(N,p,q)<=E_(p,q)` and conjectures equality of the limit for finite q.
For p=2,q=4, `rho_(N-1)=1/[N Lambda_(N,2,4)^4]`; their displayed one-sided inequality therefore points toward
a **lower**, not an upper, bound on the limiting rho. It cannot justify the upper bound required in P31-N.
The paper uses interpolation and sinc functions, so sinc transfer itself is not claimed novel.
Source: [authors' manuscript, pp.1–2](https://lubinsky.math.gatech.edu/Research%20papers/LevLubSharpNikolskiiJanuary2015.pdf).

**CONJECTURED / novelty unresolved.** The targeted searches did not find the precise x0-averaged P31 inequality
or the resulting density-beta/2 theorem. This is not a claim of priority. The strongest concrete historical
correction is that dense cosine-sum results in Z, and Fejér multiplication followed by Fejér–Riesz, were already
present in Kolountzakis (1996). A publication-level novelty check should follow that paper's citations and the
sharp finite-q Nikolskii literature before asserting a new theorem.

## Research review and handoff

**PROVED / strategic assessment.** The missing constant lemma has been closed, rather than deferred to numerical
optimization. P31 remains a valid profile-sensitive square-root result after correcting its quantifiers.
The tail cardinality argument excludes full interval cores with genuinely sparse tails; positive low-pass
smoothing is too lossy for a general steep profile. These facts justify stopping this assigned audit with a
substantive result, not asserting completion of the broader research project.

Three distinct continuing directions are:

1. **CONJECTURED, analytic lower bound:** add a cross-scale term to (7) that charges the discrepancy between
   actual 0/1 coefficients and their Fejér damping. First derive it for a two-scale core/tail decomposition,
   explicitly testing the `g_H=(F_H-1)/2` obstruction.
2. **CONJECTURED, sharp constant:** certify an upper bound for the finite-support convolution optimization,
   together with a proved transfer/limit argument. The numerical value 0.687 alone supplies neither.
3. **CONJECTURED, construction and falsification:** test steep p>=2 taper families for any structure capable of
   lowering their actual M beyond random fluctuation scale; retain all-x certificates and exact distinctness.
   The current sampled tapered examples have substantial negative dips and are not counterexamples.

**First concrete next derivation:** start with the exact positive low-pass inequality (7), write
`1_A=b+(1_A-b)`, and derive an inequality retaining the cross term between these two coefficient sequences.
Any proposed bound must survive a full interval and must state its dependence on tail cardinality or energy.
The finite-degree paper proofs above are ready for separate independent/formal review; no additional agent
was launched and no Lean verification is claimed.
