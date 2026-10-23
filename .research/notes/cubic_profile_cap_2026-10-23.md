# Cubic-profile support caps before Gabor-Jensen

2026-10-23. Continuation after86f5ca5. Full Chowla remains open.
Paper lemmas independently checked by the sole internal advisor in
[the current audit](advisor_two_block_gram_2026-10-23.md).
The exact producer AND independent rational verifier have passed.
The theorem below is proved on paper with a checked rational computer
certificate. No kernel, external-priority or publication claim.

## Quantified consequence targeted by the certificate

For EVERY fixed real0<C<400/29, there exists c(C)>0 such that EVERY
nonempty finite set A of distinct positive integers with max A<=C|A|
satisfies

    M(A)=-min_(x in R)sum_(a in A)cos(ax)>=c(C)|A|^(1/3).

The claimed constant c(C) is ineffective, as in P66/P68. The old
proved range was C<1000/73. The new range uses the exact
certificate below and its independent verification. This is a
density-restricted theorem, not an improvement of the unrestricted
universal exponent and not full square-root Chowla. An n^(1/3)
lower bound still permits M/sqrt(n) tending to zero.

## 1. Why this replaces the previous Gram attempt

For any real spectral-factor branch Q_e with |Q_e|^2=P and
mu_e=Q_e'(1)/Q_e(1), put X_e=(z*d/dz-mu_e)Q_e. Away from unit
zeros, write Q_e=sqrt(P)exp(i*phi_e). Direct differentiation gives

    X_e*conj(Q_e)=P(phi_e'-mu_e)-i*P'/2,
    sum_h U_(e,h)^2=integral P'^2/4
                        +integral P^2(phi_e'-mu_e)^2.

The polynomial products extend across unit zeros; no phase jump or
Dirac term is inserted into this almost-everywhere differentiation.
For Boolean coefficients, integral P'^2/4=sum_A a^2/8=SV/4,
exactly the existing centroid lower bound. Root choices make
phi_e'-mu_e affine in their signs. Thus all branch dependence of
the TOTAL Gram energy is a positive quadratic form, and all Walsh
coefficients of degree>=3 vanish. For two selected blocks,

    E_sigmat=2integral P^2*h_i*h_j,
    T_missing,sigmat=4integral P(lambda-1/2-P)*h_i*h_j.

There is no automatic sign on these mixed terms. The same phase
identity holds for weighted spectra. Stop enlarging this total Gram
expansion; the statement does not rule out additional specifically
Boolean constraints on its root-dependent matrix or genuinely
weighted/selected lag forms. Complete proof is in the advisor note.

## 2. Exact dense-limit inputs

Now p denotes a COEFFICIENT PROFILE, not the spectral P above.
Use the existing P58-P61/P66 contradiction framework. For a sequence
with X=max A<=C|A|, X tending to infinity and M=o(X^(1/3)), the
existing theorems give continuous even functions supported[-1,1]:

    0<=p(t)<=p(0)<=u_*=(3-sqrt3)/6,
    e=p(1-p), v=4e, sigma=4e(0)<=2/3,
    d=integral_0^1 p(t)dt>=1/C,
    p=phi(v), phi(v)=(1-sqrt(1-v))/2,
    g(p)=p(1-p)(1-2p) is positive definite.

Writing G(v)=v*sqrt(1-v)/4 gives g(p)=G(v). The normalized energy
profile is approximated by the SAME Gabor mixtures of |w|^2 used
in P61, with total mass sigma. Pieces have slightly enlarged support
before dilation. A literal exact mixture for the unsmoothed e is not
assumed. This distinction matters in the Jensen arguments below.

## 3. A valid cubic dual, and why its first fixed LP gave no gain

For eta in[0,1/2] and fixed omega, define

    F_t(v)=phi(v)+eta*cos(omega*t)*G(v).

The derivatives are

    F_t''=[2-eta*cos(omega*t)(4-3v)]/[16(1-v)^(3/2)],
    F_t'=[2+eta*cos(omega*t)(2-3v)]/[8sqrt(1-v)].

Thus F_t is convex/increasing on[0,2/3], and on a neighborhood
needed by the finite approximations. Cubic PD gives integral
G(v(t))*cos(omega*t)>=0. Add this nonnegative term BEFORE Jensen:

    d<=sup_(w in W)integral_0^1
        [phi((2/3)|w|^2)+eta*cos(omega*t)*G((2/3)|w|^2)].

Here W is P61's normalized Hermitian PD support class. Monotonicity
allows sigma to be increased to2/3 and complex factors to be
majorized by their absolute-value autocorrelations. Apply at the
smoothed-mixture stage, pass to the limit, and control support
dilation by uniform convergence of the fixed cosine.

This does NOT assume G((2/3)|w|^2) PD for every generator. Old E93b
imposed that constraint in a single-generator numerical ansatz; its
value near15.6 is not by itself an upper bound for arbitrary Gabor
mixtures. The old rigorous1000/73 theorem does not use that numerical
claim and is unaffected.

ONE fixed discovery LP at omega9.1,K64,degree10 chose eta about
4.95e-9, effectivelyzero, with D about.07251605. No improvement
from that cosine term in this relaxation, and no frequency/grid sweep.
The paper dual inequality remains valid. This motivated the genuinely
changed convex envelope next, not a larger version of the same LP.

## 4. Support cap on the actual cubic profile

For t>0 put k=ceil(1/t)-1. The normalized sampled sequence
g(p(nt))/g(p(0)) is positive definite and vanishes for |n|>k.
Its finite symbol is nonnegative. Fejer-Riesz and the top eigenvalue
of the length(k+1) path matrix with off-diagonal1/2 give the classical
Caratheodory-Fejer first-coefficient cap

    g(p(t))<=c_k*g(p(0)), c_k=cos(pi/(k+2)).

Indeed after factoring the symbol, its first coefficient is
sum_j q_(j+1)*conj(q_j) at squared norm1; the path eigenvalue is
cos(pi/(k+2)). This bound uses the ACTUAL cubic profile, not a
constraint imposed individually on Gabor generators.

G is increasing on[0,2/3], and G(sigma)<=G(2/3)=sqrt3/18. Hence

    v(t)<=b_k,
    b_k in[0,2/3], b_k^2(1-b_k)=(4/27)c_k^2.       (CAP)

The cubic is increasing on that interval, so the root is unique.
For a cell with lower endpoint t_lo, taking k=ceil(1/t_lo)-1
gives a relaxed cap valid throughout the cell. At t_lo=0 useb=2/3.

## 5. Convex continuation keeps the nonlinear constraint through averaging

For b in[0,2/3], let

    Psi_b(v)=phi(v)                         if0<=v<=b,
             phi(b)+phi'(b)(v-b)            ifv>=b.

Its derivative increases to phi'(b), then stays constant, so it is
convex/increasing on ALL v>=0. It equals phi under(CAP), is below
phi above b, and is nondecreasing as a function of b. Consequently

    d<=sup_(w in W)integral_0^1 Psi_(b(t))((2/3)|w(t)|^2)dt. (ENV)

This follows by Jensen on the original approximating Gabor mixtures,
not by asserting that the cubic constraint survives on every generator.
The uniform Lipschitz bound phi'(2/3) controls mixture-mass errors.
Since b(t) is nonincreasing, dilation t=(1+delta)s gives
Psi_(b((1+delta)s))<=Psi_(b(s)); the usual factor1+delta bounds
the dilated integral. This avoids any unjustified uniform passage
through the infinitely many support-cap staircase jumps.

Replacing b(t) by a cellwise UPPER bound preserves(ENV), because
Psi_b increases with b. Monotonicity also validates the usual
complex-to-nonnegative-autocorrelation majorization.

The new constraint is genuinely different from the old generator
support cap w(t)<=c_k. In fact

    G((2/3)c^2)/G(2/3)=c^2*sqrt(3-2c^2)>c
                                         iff1/2<c^2<1.

It therefore cuts part of the old allowed generator range for k>=3.
For k1 it does not help and at k2 the endpoint bounds agree.

## 6. Exact certificate and independent verification requirement

The single changed-objective LP, at the SAME K64,degree10,shape1/10,
proposed D=.072383312978.... This is discovery only. The producer
then reconstructed rational data with upward a_j rounding plus1e-4,
monotone Bernstein coefficient repair, and the target D=29/400.

Every half-cell has a rational cosine UPPER cap from the existing
Machin/Taylor certificate. An integer bisection on denominator3e9
rounds b UP and verifies exactly

    0<b<=2/3, b^2(1-b)>=(4/27)cap^2.

For the pointwise potential certificate, write x=1-u^2, v=(2/3)x^2,
RHS=a(t)x+B(2t,w(2t))-B(t,x)/2 and A=RHS-1/2. The two proofs are:

    radical: P_low=(1-v)/4-A^2>=0;
    tangent: P_high=(2-b-v)^2-16(1-b)A^2>=0.

The second is valid because
Psi_b(v)=1/2-(2-b-v)/(4sqrt(1-b)), with2-b-v>=2/3>0.
It is used only when v(hi)>=b on the entire u-leaf. Otherwise the
radical phi upper bound is conservative even on a straddling leaf.
If A>=0, the inequality is immediate. Exact rational Bernstein
coefficients certify every sign, with endpoint1-u factors retained.
Monotone B allows the existing exact Gram/support lower branches
for w(2t). Its integrals telescope, leaving integral a(t)w(t).

The exact Schur test with U(s)=1+(2/5)s(1-s) bounds the corresponding
operator by2D, hence the half-line functional byD. All continuum
Schur cells are certified, not sampled. Producer result:

    statusPROVED, failed[], tangent_leaves75,
    D=29/400, minimumSchurmargin=251243300521/1966080000000000.

A separate verifier reconstructs the rational functions using SymPy,
checks all caps and exact interval coverage, re-proves the long lines
and finite-symbol inputs, and interpolates DIRECT exact Schur integrals.
The independent result is PROVED:815 pointwise leaves,127 CF caps,
188 reconstructed support lines,64 direct Schur cells, and the SAME
positive minimum Schur margin. Its artifact hashes the certificate
and the source implementations. Both programs use FLINT rational
arithmetic; no independent arithmetic backend or Lean/kernel claim.

Combining(ENV) with the checked norm upper29/400 gives d<=29/400.
If0<C<400/29 then d>=1/C>29/400, a contradiction. Thus a sequence
with X<=Cn and M/n^(1/3) tending to zero cannot exist. Bounded n
gives only finitely many supports under X<=Cn, each with M>0;
the standard contradiction argument yields the stated c(C)>0
uniformly for all finite A. As in P66, no effective formula for it
is extracted from the compactness/mixture proof.

Reproduce on shared Dirichlet,2cores/4GB:

    src/dirun.sh -c 2 -m 4 -t 140 python src/cubic_dual_discovery.py
    src/dirun.sh -c 2 -m 4 -t 140 python src/cubic_cap_discovery.py
    src/dirun.sh -c 2 -m 4 -t 200 python src/cubic_cap_certify.py
    src/dirun.sh -c 2 -m 4 -t 220 python src/cubic_cap_verify.py

The discovery scripts are not needed to validate saved certificates.
Data: experiments/cubic_cap_2026-10-23/{certificate,independent_verification}.json;
the earlier zero-eta proposal is in experiments/cubic_dual_2026-10-23.
No GPU spending or VM lifecycle action occurred; Dirichlet is shared
and must remain on.

## 7. Structural consequence at the cubic front endpoint

If an eligible P66 profile actually has p(0)=u_*, then v(0)=2/3.
Writing delta_k=2/3-b_k gives

    delta_k^2(1-delta_k)=(4/27)sin^2(pi/(k+2)),
    delta_k>=2sin(pi/(k+2))/(3sqrt3).

Since k+2=ceil(1/t)+1, the sine divided by t tends to pi as t
decreases to zero. Consequently

    liminf_(t down0)[v(0)-v(t)]/t>=2pi/(3sqrt3),
    liminf_(t down0)[p(0)-p(t)]/t>=pi/6.

The second uses phi'(2/3)=sqrt3/4. Thus attaining the old cubic
front cap forces a quantitative cusp. It excludes a C1 EVEN profile
across0, or a one-sided derivative0; it does not exclude a right-C1
profile with negative slope. Cusps are allowed, so this is NOT a
strict universal front gap. The certificate does not depend on it.

## 8. First next derivation: preserve a two-scale cubic interaction

No larger grid or frequency sweep is prescribed. Beyond the pointwise
cap, let c0=G(2/3)=sqrt3/18. The three-point PSD constraint on the
ACTUAL profile gives

    R(t)=G(v(2t))-2G(v(t))^2/c0+c0>=0.

Indeed the same inequality with the actual H0=g(p(0)) follows from
the3x3 Toeplitz determinant. Replacing0<H0<=c0 weakens it, since
2H1^2(1/H0-1/c0)+(c0-H0)>=0. The zero-H0 case has d=0.

For continuous0<=gamma(t)<=1/24, add integral gamma*R>=0 before
Jensen, and change variables in the child term. Set

    Lambda_t(v)=phi(v)+(gamma(t/2)/2)G(v)
                              -(2gamma(t)/c0)G(v)^2.

Then the valid coupled dual is

    d<=c0*integral_0^1 gamma(t)dt
          +sup_(w in W)integral_0^1 Lambda_t((2/3)|w(t)|^2)dt.

The explicit convexity budget is part of this lemma, not an
assumption: (G^2)''=(1-3v)/8 and |G''|<=3sqrt3/8 on[0,2/3]
give

    Lambda_t''>=(16-9sqrt3)/128>0,
    Lambda_t'>=1/4-sqrt3/96>0,
    Lambda_t(0)=0.

Thus the same Gabor-Jensen argument is legitimate WITHOUT giving
individual generators their own cubic PSD constraint. Continuously
extend gamma slightly past1 inside[0,1/24] for the dilation step;
the actual profile vanishes outside support. Its convex tangent
continuation at b(t) can incorporate(CAP) as well.

An explicit analytic discriminator is available, with no new job.
Take the normalized half-sine autocorrelation

    w(t)=(1-t)cos(pi*t)+sin(pi*t)/pi, 0<=t<=1,
    H(s)=s^2sqrt(3-2s^2).

At t0=1/4, x=w(t0)=sqrt2(3/8+1/(2pi)), y=w(2t0)=1/pi.
The elementary bounds3<pi<22/7 imply x^2>57/100 and

    2H(x)^2-1>1/5, H(y)<7/36<1/5.

Thus R_generator(t0)/c0=H(y)-2H(x)^2+1<-1/180. The TWO point
caps are not violated: x^2<3/5 givesH(x)<9/(5sqrt5)<cos(pi/5),
and H(y)<1/2. This generator can violate other caps near0; it is
not claimed to be a feasible actual profile.

For an entirely explicit neighborhood, H'<=3, |w'|<4 and H<=1
give Lipschitz constant72 for R_generator/c0 near t0. Hence it
stays below-1/360 when |t-t0|<=1/30000. On that interval the point
caps at t and2t stay inactive too: x^2<169/288<.59 gives
H(x)<1593/2000; variation adds<1/2500, still below4/5<cos(pi/5).
The child bound varies by<1/1250 and stays below1/2. Consequently
the triangular choice

    gamma(t)=rho*(1-30000|t-1/4|)_+, 0<rho<=1/24,

has integral rho/30000 and changes this generator's dual cost by
at most-c0*rho/(360*30000)<0. The same strict decrease survives
the tangent cap, since its only affected intervals are these t and2t
neighborhoods. This proves that the new interaction is not just a
restatement of those individual caps. It does NOT prove that the
SUPREMUM over all generators decreases or supply a further constant.

FIRST NEXT operation: derive the pointwise/potential certificate for
this genuinely coupled objective, initially with a SINGLE localized
continuous gamma shape justified by this discriminator and a bounded
amplitude, before considering one targeted discovery proposal.
An explicit generator rules out any proposed bound; an optimizer
value never certifies it. Stop if the new term is unused or the
mixture argument is replaced by per-generator PSD. No new constant
or computational result is claimed for this two-scale dual yet.

Maintain three distinct lines: unrestricted signed Boolean coupling,
this dense-profile inverse argument, and genuine growing constructions
requiring all-circle UPPER bounds on M. The present result remains
a partial theorem on the path to the full objective, not its completion.
