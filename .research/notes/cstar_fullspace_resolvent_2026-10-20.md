# Paused checkpoint: full-space witnesses and the cost criterion's scope

2026-10-20. Previous goal turn was progress (a66fdc6). The user has
paused the goal. This note preserves work already derived and checked;
no universal Chowla bound is proved. Sources, verification data and
derivations are preserved together in this checkpoint; broader index
integration is unfinished. The October 21 commit-and-push request
does not resume the research goal.

## Exact full-space variational derivation

Let D=2f_A, n=|A|, K=-min D, with normalized integrals. Thus mean D=0
and ||D||^2=2n. For lambda>K put

    h=1/(lambda+D), I=integral h, J=integral h^2,
    T=lambda I-1>0,
    q_lambda=n(I-h)/T.

Strict Jensen gives T>0. Directly,

    mean q_lambda=0, <D,q_lambda>=n,
    Q(lambda)=n^2(J-I^2)/T^2,
    (lambda+D)q_lambda=n+(nI/T)D,
    integral (lambda+D)q_lambda^2=n^2 I/T.

For any other mean-zero v with <D,v>=n, weighted completing-square
gives

    integral (lambda+D)v^2
      =n^2 I/T+integral (lambda+D)(v-q_lambda)^2.

Consequently, if Q(lambda)=beta*n, beta>1/2, q_lambda uniquely
minimizes H=<D,q^2> subject to those two linear constraints and
Q<=beta*n, over ALL real square-integrable witnesses. Its cost is

    F_beta(A)=n^2 I/T-lambda*beta*n.

This is an unrestricted variational formula, not a Boolean cost bound.
It applies to weighted trigonometric polynomials as well.

Existence/uniqueness of lambda: as lambda tends to infinity,
q_lambda tends uniformly to D/2 and Q tends to n/2. As lambda
decreases to K, I diverges (a trigonometric minimum has at least
quadratic contact). The normalized h/I concentrates on the finite
minimum set, so J/I^2 diverges; since T/I tends to K>0, Q diverges.
Q is continuous and strictly decreasing. To see strictness, differentiate
the weighted stationarity identity along the constraint tangent space:

    Q'(lambda)=-2 integral (lambda+D)(q'_lambda)^2<0.

Equality would imply q'_lambda=0; differentiated stationarity then
forces q_lambda=D/2. Original stationarity would make D^2 affine in
D, impossible for a nonconstant continuous D on a connected circle.
Thus every beta>1/2 has a unique lambda>K.

Finite rational trigonometric witnesses approximate this optimum with
arbitrary slack in norm and cost. Use beta'<beta, truncate Fourier
series, round rationally and repair coupling by a small multiple of D.
The L2 norm and cubic cost are continuous because D is bounded.
Let beta' increase to beta. No bound on the required frequency degree
uniformly in A has been proved. Formula/proof are self-derived paper
arguments, not independently reviewed or kernel checked.

Singleton calibration: D=2cos x and lambda=5/2 give I=2/3,
T=2/3, q=1-3/(5+4cos x), a=1,Q=2/3,H=-2/3. Its Fourier
coefficients are q_k=-(-1/2)^|k| for k!=0. Exact truncations at
degrees2,4,8,16 independently match their geometric-sum moments.

## A hidden requirement of uniform fixed-coupling cost

Let mu=integral D_+=integral D_-=||D||_1/2. For any real q,

    |<D,q>|<=sqrt(mu)[sqrt(integral D_+q^2)+sqrt(integral D_-q^2)].

If a>=alpha*n, Q<=beta*n, H<=gamma*n^(3/2), gamma>=0, and
K<=C sqrt(n), then integral D_-q^2<=KQ and
integral D_+q^2=H+integral D_-q^2. Hence

    ||D||_1 >= 2alpha^2 sqrt(n)
      / [sqrt(gamma+C beta)+sqrt(C beta)]^2.

Conversely, if ||D||_1>=delta sqrt(n), let s=sign D,
m=integral s, and q=n(s-m)/||D||_1. Exactly,

    a=n, Q=n^2(1-m^2)/||D||_1^2<=n/delta^2,
    H=-2m n^2/||D||_1<=2n^(3/2)/delta.

Approximation gives finite rational trigonometric witnesses with slack.
Thus on bounded-ratio classes the unrestricted fixed-coupling programme
requires a quantitative L1-flatness statement, and flatness supplies
such witnesses. This is stronger than merely asserting a negative
minimum of square-root size on that class. No Boolean counterexample
to flatness and no reverse implication from Chowla are asserted.

Keep the original negative-Rayleigh branch: H<=-c sqrt(n) Q itself
proves a square-root dip without macroscopic a. The earlier decision
to stop treating eigenvalue success as proof of large coupling must
not be read as abandoning valid direct Rayleigh certificates. The
flatness-versus-many-spike issue is the existing CSTAR obstruction;
these formulas do not constitute a new solution by rewording it.

## Exact finite separation from the restricted spaces

Input is the saved irregular N50_x72 set: n50, actual max A72.
Numerical quadrature at65536 and262144 points proposes lambda about
8.080979822 at Q=24n and cost about-9228.4264. These numerical
integrals, lambda and claimed optimum are UNCERTIFIED diagnostics.
Their rational Fourier polynomials are checked independently.

The degree1152 rational mean-zero q has exactly a=50 and Q<=1250,

    H=-2946171810440610303/343597383680000,
    M>790943649/200000000=3.954718245.

For the ENTIRE mean-zero prefix space, a51-dimensional exact dual is

    1000000 H_matrix+6277382 Q_matrix-186281 a_vector a_vector^T >0.

Thus every prefix q with a=50,Q<=1250 satisfies

    H>=-295241/40=-7381.025.

The degree1152 witness has strictly smaller cost. Producer Bareiss
pivots and an independent reversed rational Schur check prove the
dual's positivity, without numerical optimum claims.

There is also a stronger spectral comparison: full W2 has269 Fourier
rows. The integer matrix 2B_W2+15I is positive definite, so ALL full-W2
Rayleigh certificates have K<15/2, equivalently M-bound<15/4=3.75.
The producer checks the positive coefficients of det(tI+2B_W2+15I).
Since the matrix is symmetric, absence of nonnegative roots proves
positive definiteness. An independent checker rebuilds W2 and checks
all269 reversed-order Bareiss pivots/divisions and its determinant.
The broader witness exceeds this cap. Already the tested degree576
polynomial exceeds the W2 cap; no minimal-degree claim is made.

At K0=79/10 the explicit r=-50/K0+q has the exact negative form

    integral (D+K0)r^2
      =-596337414288051139/54288386621440000<0.

An independent rational Sturm chain rechecks the global upper
M<=20154679/5000000=4.0309358. Therefore .55<R(A)<.571 by exact
squared comparisons. No sampled minimum or minimizing angle is used.
This proves a finite witness-space separation, NOT a counterexample
to the existence of a weaker universal square-root W2/prefix bound.

## Dependency screening, status and restart

A possible shortcut through claimed L1-flat Singer polynomials was
screened in [arXiv1508.06439v8, Section5.1](https://arxiv.org/html/1508.06439v8#S5.SS1).
Its literal identity c_-l=c_(q-l) used near(5.22)-(5.24) does not hold
for integer lifts: the Singer set {0,1,3} mod7 has c_-1=1,c_6=0.
Collapsing negative powers by residues is valid on the root grid,
not automatically after shifting it. That finite countercheck is saved.
No flatness theorem from this lead is assumed, and no global judgment
on that paper's main claim is made. Broader literature review is deferred.

Scripts: src/cstar_resolvent_witness.py and cstar_resolvent_verify.py.
Data: ../experiments/resolvent_2026-10-20/results.json,verification.json.
All computation ran on Dirichlet via src/dirun.sh,2 cores,8GB.
Final verification exited0/PASS, including five scalar witnesses,
the full-W2/prefix dual bounds and independent Sturm upper bound.
All jobs from this pass are terminal. An internal technical proof-agent
launch failed because the configured default model was unavailable;
no independent-agent or Lean audit is claimed. Goal status is PAUSED.

First derivation on resumption: use exact Boolean/torsion-free structure
to bound the full-space cost or prove the needed low-ratio L1 inverse
estimate; retain direct negative-cost witnesses as an alternative.
Do not assume fixed witness bandwidth, do not infer a uniform bound
from this finite separation, and do not restart specialized exclusions.
