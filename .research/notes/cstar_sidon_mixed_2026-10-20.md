# Long Sidon fibers and a nonlinear obstruction with a small mean budget

2026-10-20. Research record for CSTAR DESIGN / CHAIN(c), not a manuscript.
Full Chowla and the arbitrary-support mixed-certificate step remain OPEN.
The main paper result below handles arbitrary dependence across a specified
whole-fiber ensemble. It does not handle every deterministic fiber choice.

## Construction and exact mean

Let u range over canonical primitive nonzero integer vectors with
||u||<=U. Choose odd primes p_u comparable to X/||u||, with
sqrt(2)p_u||u||<=X. For example take the largest prime at most
floor(X/(sqrt(2)||u||)); Bertrand gives the comparison uniformly when
U<=X^(1/4) and X is sufficiently large. Apply A in GL2(F_p) and a cyclic
coordinate shift s in F_p^2 to {(t,t^2):t in F_p}, and lift to a set
P_u in {0,...,p-1}^2. Use every unordered positive sign-pair difference
M=u(b-b')^T. A nonzero group difference determines t-t' and t+t', so
the parabola is Sidon for odd p; invertible A preserves this. Integer
differences are therefore distinct. Different primitive-u planes meet
only at zero. The matrix support has norm<X and

    n=sum_u p_u(p_u-1)/2 = Theta(X^2 log U).

The elementary primitive-vector count gives
sum_(||u||<=U) ||u||^(-2)=(6/pi)log U+O(1), while the sum with exponent
3 is bounded. Thus sum p_u^3=O(X^3), without using a prime-gap asymptotic.

Write F_P(theta)=sum_(b in P) exp(i b.theta),
D_P=|F_P|^2-p and f_P=D_P/2. The exact square identity proves
M(f_P)<=p/2 for every physical phase, so the largest isolated left-plane
negative budget is O(X)=o(sqrt(n)) when U grows polynomially.

With uniform A and s the coefficient for a nonzero integer displacement
delta in (-p,p)^2 is exactly

    mu_delta=(p/(p+1)) product_j (1-|delta_j|/p).                 (1)

Indeed GL2 acts transitively on nonzero group differences, of which
p(p-1) occur among p^2-1 possibilities. Conditional on that difference,
uniform coordinate shifts give the two triangular wrap probabilities.
Consequently, with F_p(theta)=|sum_(t=0)^(p-1) exp(it theta)|^2/p,

    E D_P=(p/(p+1))(F_p(theta1)F_p(theta2)-1).

Hence M(mean)<=sum_u p_u/(2(p_u+1))=O(U^2). At U=floor(X^(1/4)) this
is o(sqrt(n)). The preceding turn's large-negative-MEAN argument cannot
exclude this model. The issue is the Boolean realization, including
arbitrarily dependent realizations with these same whole-fiber marginals.

## Exact mixed certificate and torsion-free ruling identity

Let A and B be two matrix difference supports from this architecture,
with the same primes, hence the same n. Here these letters denote
frequency sign-pair sets, not the GL2 matrix parameter. Put

    q=D_A-D_B, a=<D_A,q>=2|A\B|, Q=||q||_2^2=2a,
    H=<D_A,q^2>, K=2M(A).

Normalized torus integration is understood. Positivity of
(D_A+K)(s+tq)^2 for all real s,t gives

    Q K^2 + H K - a^2 >= 0.                                   (2)

For rank-one integer matrices, det(M1+M2) is the product of the left
and right wedge products. Thus an additive triple of nonzero rank-one
matrices lies in a common left ruling plane or a common right ruling
plane. It lies in both exactly when all three are scalar-collinear.
Therefore the cubic has the EXACT inclusion-exclusion decomposition

    H=sum_left H_u + sum_right H_v - sum_scalar_lines H_l.      (3)

All q coefficients belong to {-1,0,1}. The contribution in (3) outside
common left planes has absolute value at most

    |sum_right H_v - sum_lines H_l| <= 19683 X^2 U^4.            (4)

Here is a direct count with deliberately loose constants. Fix ordered
distinct canonical left directions u0,u1,u2. Off-left right triples
have a unique primitive integer relation r0u0+r1u1+r2u2=0, with every
r_i nonzero, and are M_i=r_i u_i w^T for a nonzero integer w. If all
matrix norms are <=X, ||w||<=X/max||u_i||. There are at most
9X^2/(max||u_i||)^2 choices. Also #u with ||u||<=r is <=9r^2.
Assigning one of three maximal directions gives
sum_(u0,u1,u2)1/max||u_i||^2<=2187U^4. Multiply by9. This count includes
all signs and ordered positions; no independence or coefficient
averaging is used. Triples with repeated left direction are already
removed by the scalar-line subtraction.

The identities transfer to ANY integer linear encoding L:Z^4->Z whose
nonzero integer kernel vectors have norm>3X. This gives distinct positive
absolute encodings and no aliases in the degree<=3 moments. In particular
the h=6000X^3+(1,3,5,7) CRT encoding qualifies, as do ordinary base
encodings with base>6X. Unlike the previous residue test, approximating
every matrix phase by scalar phases is unnecessary for (2)-(4).

## Uniform cyclic-shift moment bound

Fix any GL2 orientation of the parabola. At nonzero p-grid Fourier
characters its exponential sum has modulus zero or sqrt(p): a linear
phase sums to zero; squaring a genuine quadratic Gauss sum and changing
variables gives modulus squared p. Let the shifted integer polynomial be

    F_s(theta)=V(theta)+E_s(theta),
    V(theta)=D_p(theta1)D_p(theta2)/p,
    D_p(theta)=sum_(t=0)^(p-1) exp(it theta).

The p-grid Lagrange formula is exact, with
L_k(theta)=D_p(theta-2pi k/p)/p. Uniformly in theta,
sum_k |L_k(theta)|^(6/5)<=13: use the nearest grid point and the tail
bound |L_k|<=1/(2j-1), then compare the decreasing series with its
integral. In two dimensions the sum is <=169. The nonzero Fourier
coefficients of E_s as a function of the cyclic shift s are bounded by
sqrt(p) times these Lagrange weights. The finite inverse
Hausdorff-Young inequality therefore gives

    (E_s |E_s(theta)|^6)^(1/6) <=169 sqrt(p).                   (5)

The constant is loose; 13^(5/3) already suffices. Normalization: shift
space uses probability measure and Fourier coefficients use counting
measure. Equivalently (5) follows from Plancherel and three-fold Young
convolution with exponent6/5. The standard finite-group inequality and
normalization are checked against [Tao, 247B Notes9, Q3, p.13](https://www.math.ucla.edu/~tao/247b.1.07w/notes9.pdf).
That reference supplies the classical inequality only, not this argument.

For independent reference parabola P', write Z=|E_s|+|E'_s| and
q_u=|F_P|^2-|F_P'|^2. Then

    |F_P|^2 q_u^2 <=16|V|^4 Z^2+20|V|^2 Z^4+4Z^6.

This follows from |q_u|<=2|V|Z+Z^2 and |F_P|^2<=2|V|^2+2Z^2.
Since integral|V|^2=1 and integral|V|^4<=p^2, (5) and Holder give

    E J_u <= C1 p_u^3,
    J_u=integral |F_P|^2 q_u^2>=0,
    C1=64*169^2+320*169^4+256*169^6.                            (6)

No cross-fiber independence is needed. Also H_u=J_u-p_u Q_u<=J_u.

## A nonlinear same-marginal theorem despite the small mean

**Paper statement.** Set U=floor(X^(1/4)) and choose the primes as above.
Give each whole fiber the uniform GL2-orientation and cyclic-shift
marginal, with ANY dependence across different fibers. Under any encoding
with kernel gap>3X, for all sufficiently large X,

    Pr[ M(A) >= sqrt(n)/5 ] >= 1/6.                            (7)

The expected polynomial still has M(mean)/sqrt(n)->0 by (1). This is a
nonlinear obstruction to an all-output counterexample guarantee for
these marginal laws, not a theorem for every deterministic assignment.

**Proof and effective sufficient criterion.** Choose B independently of
A, with the same per-fiber ensemble, and the same primes. From (1),
for each fiber the expected positive-frequency intersection is

    E |A_u cap B_u| = (p-1)(4p^2-1)/(18(p+1)) <= n_u/2.

Thus E a>=n and a<=2n, so Pr[a>=n/2]>=1/3. Markov and (6) give
Pr[sum J_u<=6 C1 sum p_u^3]>=5/6. Their intersection has probability
at least1/6, without any independence of these events or of the fibers.
On it H<=T, where

    T=6 C1 sum p_u^3+19683X^2U^4=O(X^3).

Since n=Theta(X^2 log U), eventually T<(9/40)n^(3/2). At k=2sqrt(n)/5,
using Q=2a and a>=n/2,

    Q k^2+H k-a^2 <= -(9/100)n^2+(2/5)T sqrt(n)<0.

Equation (2) forces K>k. Project the good pair event onto A to obtain
(7). This proof permits arbitrary dependence of A's fibers: the reference
B is introduced independently for the certificate only. The explicit
finite sufficient criterion is (40T)^2<81n^3; the conservative constants
give no practical small threshold and the finite probes do not meet it.

## Finite evidence and the remaining conditional cost

The actual Boolean probes used the WIDER U=floor(X^(1/3)), not the
asymptotic theorem's U=X^(1/4). Rotated cases have
(X,n)=(64,3952),(256,81794),(1024,1585878). Their certified global point
ratios exceed1.7533,1.9602,1.8541. Unrotated X256 has a stronger residue
defect (M>512 at q2) than the rotated case (best tested M>90 at q3).
All q=2,...,128 Jordan-Ramanujan averages were independently reconstructed
using the Mobius divisor formula. A finite grid/optimizer selects points
only. Right-plane FFT minima are numerical diagnostics, not all-phase
upper bounds; selected positive-Fejer plane lower certificates are separate.

For three actual/reference pairs, exact integer convolutions in (3) give:

| X | rotated A | a | Q | H_left | H_right-H_line | certified M/sqrt(n)> |
|---|---|---|---|---|---|---|
|64|yes|4558|9116|163054|-56|0.31518|
|256|no|92916|185832|14880106|-1236|0.31328|
|256|yes|92032|184064|12947118|-6272|0.31857|

All bounds follow from exact rational negativity in (2), hence are
all-phase lower certificates. The X64 cubic is independently recounted
in four coordinates without line subtraction or Kronecker polynomials.
The X256 integer polynomial/sparse cubic counts have their certificate
algebra rechecked, but no separate four-coordinate recount is claimed.

Exhaustive affine-parabola populations at p=3,5,7 contain72,600,2352
point sets. A separate graph parameterization reconstructs the entire
population and recounts all conditional moments using sparse convolution.
For every fixed actual P, let the reference P' be uniform. The observed
maxima of E_P' H_u/p^3 are118/243,11212/9375,83159/67228. These are
finite maxima, not a uniform all-prime theorem. All p3/5/7 conditional
reference-averaged certificate inequalities are checked exactly. Off-grid
192-bit sixth-moment checks also corroborate (5)'s normalization.

The p11 extension enumerates ALL14520 affine parabolas and has an
independent sparse-convolution recount of every conditional moment and
certificate. Its maximum is1643756/605, or1643756/805255 times p^3.
Thus the concrete trial bound C=2 is REFUTED: the gap above2p^3 is
33246/605. The maximizer's eleven points are saved in
`population_extra.json`. No finite population size establishes an
absolute bound for all primes, and increasing the fitted constant is
not a substitute for the conditional argument.

The next missing lemma is now precise: does

    E_(uniform reference P') H_u(P,P') <= C p^3                 (8)

hold for EVERY lifted affine parabola P, with absolute C? Only the
average over actual P was proved in (6). Macroscopic conditional coupling
is already elementary: for ANY selected set of n_u=p(p-1)/2 positive
frequencies, E_P' a_u>=n_u/8. Indeed at most half its signed frequencies
can have mu>7/8, since those lie in |delta_j|<p/8; the box contains at
most p^2/16+p/2<=(p^2-p)/2 nonzero integer points for p>=3. The rest
contribute at least1/8 each to a_u. Thus the actual missing step is the
CONDITIONAL cubic cost (8), not correlation or a renamed mean theorem.
If (8) holds, averaging (2) over the reference while keeping A fixed,
and using (4), would exclude EVERY deterministic choice in this Sidon
architecture: at U=floor(X^(1/4)) it would give M>=sqrt(n)/10 for all
sufficiently large X. Indeed a_bar>=n/8, Q_bar=2a_bar and H_bar=O(X^3)
in the averaged positive moment matrix. It would still not prove Chowla
for arbitrary supports.
An exact useful expansion for that attack is

    H_bar(P)=integral D_P^3 -2 integral D_P^2 m
                 + integral D_P W,
    m=E_reference D, W=E_reference D^2.

The finite programs compute this expression by two independent methods.
The difficult issue is the cancellation of its large positive-front
terms for a FIXED actual P; the averaged cyclic-shift proof cannot be
applied conditionally without establishing that cancellation.

## Reproducibility and strategic decision

Code: `src/cstar_sidon_fibers.py`, `cstar_sidon_mixed.py`,
`cstar_sidon_verify.py`, `cstar_sidon_population.py`,
`cstar_sidon_lemmas_verify.py`. Data in
`.research/experiments/sidon_fibers_2026-10-20/`. Exact output sizes,
max frequencies, hashes, parameters, moment integers and rational
inequalities are saved. All computation ran on Dirichlet. No point/grid
minimum is promoted to a global upper certificate. A fresh proof/Lean
review launch failed with the unavailable configured default model;
these are paper arguments with computational checks, not independent-agent
or kernel-checked results. No novelty claim is made.

The previous small-fiber log-gain strategy stays discontinued. Long
incomplete Sidon fibers genuinely evade the old lens sign argument, and
their fractional mean is small; (7) supplies a nonlinear sign result
even under dependence. Stop treating a small mean budget as evidence
that coupling can realize it. Pursue (8) adversarially rather than assume
it, and keep the broader arbitrary-support mixed-certificate problem
and non-cone growing-depth Riesz rounding active. Nothing here resolves
the unrestricted Chowla quantifiers.
