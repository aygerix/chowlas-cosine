# Two-block centered Gram: exact phase collapse and next pivot

2026-10-23. Sole internal AI advisor. Independent paper expansion and
audit of the parent's all-block phase formula. No computation, VM
operation, GPU, extra agent or outreach. Shared Dirichlet is untouched.
Full Chowla remains open; no new universal exponent or kernel check.

## 1. Fixed Boolean data and moving centered vectors

Let A be a nonempty finite set of distinct positive integers, n=|A|,
X=max A, lambda=M(A), and

    p=lambda+f_A=|Q|^2,
    S=Q(1)=sqrt(lambda+n)>0,
    V=sum_(a in A)a^2/(2S).

Use a real factor of degree X with no monomial padding. Keep two real
reciprocal-root blocks variable and the remaining factor C fixed:

    Q_(sigma,tau)=a+sigma*b+tau*c+sigma*tau*d,
    a=C*A_i*A_j, b=C*B_i*A_j,
    c=C*A_i*B_j, d=C*B_i*B_j,
    sigma,tau in{+1,-1}.

Thus a*d=b*c as POLYNOMIALS. The product-sign law is not being
assumed to meet any signed budget. Put

    mu=mu0+sigma*theta+tau*eta, y_k=k-mu0,
    x_k=(k-mu)q_k.

Expansion gives exactly

    x0=y*a-theta*b-eta*c,
    xsigma=y*b-theta*a-eta*d,
    xtau=y*c-theta*d-eta*a,
    xsigmatau=y*d-theta*c-eta*b.                    (1)

Every x vector has coefficient sum0, so each Walsh component in(1)
has sum0 as well. Zero coefficients can be retained on the fixed
index set0,...,X; no changing-support convention is needed.

## 2. Complete autocorrelation and missing-lag coefficients

For real coefficient vectors u,v write

    R_uv(h)=sum_k u_k*v_(k+h).

The four autocorrelation coefficients are

    C0=R_aa+R_bb+R_cc+R_dd
                =lambda*delta_(h0)+(1/2)*1_(+/-A)(h),
    Csigma=R_ab+R_ba+R_cd+R_dc=0,
    Ctau=R_ac+R_ca+R_bd+R_db=0,
    Csigmatau=R_ad+R_da+R_bc+R_cb=0.                (2)

The zero equations and a*d=b*c hold for weighted spectra too.
Booleanity adds C0(h)^2=C0(h)/2 for h!=0.

Let G_kl=R_qq(k-l), which is fixed for all four branches, and let
M_kl=1 precisely when k!=l and |k-l| not in A. For sum-zero x,

    x^T G x=(lambda-1/2)||x||^2-(1/2)x^T M x.     (3)

Define U_h=sum_k x_k*q_(k+h). Expanding the sums proves

    E=sum_h U_h^2=x^T G x.

No diagonal U0 term or exterior lag is omitted. The mixed Walsh
coefficients are, writing x11=xsigmatau,

    W11=2*(<x0,x11>+<xsigma,xtau>),
    T11=2*(x0^T M x11+xsigma^T M xtau),
    E11=(lambda-1/2)W11-T11/2.                    (4)

Thus the full mixed missing-lag expression has been retained rather
than replaced by absolute values or a positive-factor bound.

## 3. Exact lag pairing and the branch-independent Boolean contribution

For any branch let R_h=R_qq(h). Changing summation endpoints gives

    U_-h=U_h+h*R_h.

Put Z_h=U_h+h*R_h/2; it is even in h. Pairing ALL signed lags yields

    E=sum_h Z_h^2+(1/2)sum_(h>0)h^2*R_h^2.

For the Boolean spectrum this last term is

    (1/2)sum_(h>0)h^2*R_h^2
             =(1/8)sum_(a in A)a^2=S*V/4.         (5)

This is the exact completion of the old signed-centroid lower bound.
The unit-amplitude identity changes this BRANCH-INDEPENDENT constant;
it does not supply a sign for its mixed Walsh coefficient, which is0.

## 4. Phase calculation, including optimal unit-circle zeros

Let z=exp(ix) and write Q(z)=sqrt(p(x))*exp(i*phi(x)) away from
its finitely many circle zeros. Define

    X(z)=(z*d/dz-mu)Q(z).

Pointwise there,

    X*conj(Q)=p*(phi'-mu)-i*p'/2,
    E=integral |X*conj(Q)|^2
      =integral p'^2/4+integral p^2*(phi'-mu)^2.   (6)

The generating Laurent polynomial of the earlier U_h convention is
Q*conj(X), the conjugate of the first expression; its squared modulus
is the same. This avoids an irrelevant sign ambiguity in the imaginary
part of the generating polynomial.

The zeros cause no gap. Formula(6) is first proved off the finite zero
set; X*conj(Q) and p' are ordinary continuous trigonometric polynomials.
The weighted real term is their real part and extends continuously.
No global differentiable choice of phi is required. Jumps of an
unweighted phase at unit zeros are not inserted as Dirac terms.
Since p'=f_A', Fourier orthogonality proves

    integral p'^2/4=(1/8)sum_A a^2=S*V/4,

in agreement with(5). This is also the phase interpretation of Z_h.

## 5. Every branch-dependent term is a generic quadratic phase energy

For a block D_j of degree d_j, circle reversal changes its phase
velocity v_j(x) to d_j-v_j(x). Its centered contribution is

    h_j(x)=v_j(x)-v_j(0),
    v_j(x)=Re[z*D_j'(z)/D_j(z)].

The unit-circle part has constant phase velocity away from its zeros;
its contribution cancels on subtracting mu. With other choices fixed,

    phi'-mu=h0+sigma*h_i+tau*h_j.

For the full ensemble, one can choose the balanced representation
with h0=0. Thus(6) is a quadratic Ising functional in the root signs.
In particular

    E11=2*integral p^2*h_i*h_j.                   (7)

Its matrix is positive semidefinite, but an off-diagonal inner product
has no specified sign. ALL Walsh coefficients of degree at least3
vanish. Increasing the number of retained blocks cannot produce a
new higher mixed term from this Gram expression.

The centered derivative norm has the same collapse:

    ||x||^2=integral p'^2/(4p)
                        +integral p*(phi'-mu)^2,
    W11=2*integral p*h_i*h_j.                     (8)

The quotient p'^2/p is locally integrable at an even-order zero of
the nonnegative polynomial p. Its amplitude term is independent of
the branch. Equations(4),(7),(8) give the complete missing-lag answer

    T11=2*(lambda-1/2)W11-4*integral p^2*h_i*h_j
       =4*integral p*(lambda-1/2-p)*h_i*h_j.      (9)

Thus the missing-lag quadratic form itself has no Walsh terms of
degree at least3. The factor lambda-1/2-p=-f_A-1/2 is not one-signed;
neither are the phase products. Equation(9) is a checked exact formula,
not an upper bound for the signed negative-coefficient budget.

For explicit root geometry, an outside root rho=R*exp(i alpha), R>1,
contributes

    Re[z/(z-rho)]=(1-P_(1/R)(x-alpha))/2,

where P is the Poisson kernel. Therefore h_j is a sum of centered
Poisson kernels. This representation is also generic factor geometry;
no absolute budget follows from writing its kernel explicitly.

## 6. Kill decision and precise limitation

The recorded calculation has been carried out completely. Boolean
R_h^2=R_h/2 changes the amplitude constant in(5), which disappears
from the mixed Walsh coefficient. Every branch-dependent term in
(6)-(9) is the same generic phase formula for a weighted positive
polynomial. Thus this mixed-Gram expansion supplies no quantitative
Boolean branch-selection sign beyond the already known centroid
invariants. Stop larger-block Gram expansions, new factor controls,
or a descent conjecture justified only by this identity.

This is an ALGEBRAIC COLLAPSE, not a counterexample to every possible
inequality for the resulting Ising matrices on the restricted Boolean
family. The root kernels still depend on p. A future bound using new
information about their Boolean geometry is not logically excluded,
but none has been proved by the expansion above. Do not present a
generic PSD polarization as such a bound.

The earlier ensemble counterexamples retain their full scope limits:
they have n=3 and R>3/4. They refute the advertised all-actual-lowM
unbiased certificate and the universal single-flip cost claim, not
an asymptotic theorem restricted to hypothetical R tending to zero.
Arbitrary fair correlations still give exactly branch-cost minimization
by pairing a branch with its reverse; they provide no independent
selection mechanism.

## 7. Global review and changed next calculation

The parent proposes returning to the EXISTING P31-P61-P63-P66
support-density program. This is a genuinely different mathematical
input from phase/root bookkeeping: it uses the physical support
constraint X<=C*n together with coefficient binarity. Current proved
thresholds quoted in the project are C<2000/259 for a square-root
bound and C<13.6986... for the recorded one-third bound. They are
conditional-family results, not full Chowla.

Before adopting a fourth-order strengthening I am reading P66 and
the tdense10-12 reports. In particular sparse signed cubic repairs,
divergent fourth moments, rational-atom exceptions and anchored-DC
domination are existing falsifiers, not missing observations. The
next task must identify ONE quantitative fourth-order term outside
those barriers, with its exact implication and first falsification;
merely demanding another coefficient moment is not a new gain.

## 8. Audited changed dense-profile lemma: insert cubic PD before Jensen

The parent's subsequent concrete derivation is preferable to an
unproved fourth-PD or kurtosis assertion. I checked its derivatives,
normalization and order of the mixture step. It is a new coupled
inequality in the inspected project record; no external priority or
improved numerical constant is claimed.

Use the P58/P66 contradiction setup: A_X is Boolean, max A_X=X,
|A_X|/X tends to d>0 and M(A_X)=o(X^(1/3)). The quoted project
limit theorem gives continuous profiles p,e on[-1,1] with

    e=p(1-p), p=phi(4e),
    phi(v)=(1-sqrt(1-v))/2,
    sigma=4e(0)<=2/3,
    g(p)=p(1-p)(1-2p) positive definite.

Here p denotes the COEFFICIENT profile, not the trigonometric
spectral polynomial in Sections1-6. The cubic PD conclusion uses
M^3/X tending to zero and is NOT available merely from
M=o(sqrt(X)). Thus this lemma targets the one-third dense range,
not the existing square-root threshold.

Set v=4e and

    G(v)=v*sqrt(1-v)/4, so g(p)=G(v).

For fixed real omega and0<=eta<=1/2, define

    F_t(v)=phi(v)+eta*cos(omega*t)*G(v).

Direct differentiation gives

    G'=(2-3v)/(8sqrt(1-v)),
    G''=-(4-3v)/(16(1-v)^(3/2)),
    F_t''=[2-eta*cos(omega*t)*(4-3v)]
                                  /[16(1-v)^(3/2)],
    F_t'=[2+eta*cos(omega*t)*(2-3v)]/[8sqrt(1-v)].

Hence F_t is convex and strictly increasing on0<=v<=2/3;
the same properties hold throughout0<=v<1 under this eta bound.
Also F_t(0)=0. The potentially negative cosine multiplier therefore
does NOT reverse the monotonic majorization step.

Cubic PD gives integral_0^1 G(4e(t))*cos(omega*t)dt>=0, so

    d<=integral_0^1 F_t(4e(t))dt.

Apply this convex function to the SAME normalized Gabor mixture
used in P61, with its global mass sigma. It follows that

    d<=D_cubic(eta,omega),                           (10)
    D_cubic(eta,omega)=sup_(w in W) integral_0^1
        [phi((2/3)|w(t)|^2)
           +eta*cos(omega*t)*G((2/3)|w(t)|^2)]dt,    (11)

where W is the existing normalized Hermitian PD support class.
Monotonicity allows sigma<=2/3 to be increased to2/3. The complex-
generator reduction is valid: replace a Boas-Kac factor by its
absolute value, pointwise majorizing |w| by a nonnegative
autocorrelation, and apply the monotonic F_t.

### The required approximation justification

P61 constructs approximating Gabor mixtures after smoothing and
support dilation; it does not automatically furnish a literal exact
probability mixture for the unsmoothed e. Formula(10) must be
proved in that framework. At fixed smoothing radius, the mixture
mass converges to4(e*rho)(0)<=4e(0)<=2/3, since e is PD and maximal
at0. Finite-X masses may exceed this by o(1); apply F on a fixed
interval below1, then let that error tend to zero. Convexity and
monotonicity hold there as checked above.

The piece profiles have support[-1-delta,1+delta]. Dilation to W
changes cos(omega*t) to cos(omega*(1+delta)*t), which tends uniformly
to the original cosine for fixed omega. All arguments v stay bounded
away from1, so the other terms also pass uniformly or by dominated
convergence. Finally let smoothing/dilation tend to zero. These
steps justify(10) without an unproved exact-mixture assertion.

### What this corrects and what still needs proof

The cubic constraint must be inserted BEFORE Jensen. It is NOT
legitimate to assume G((2/3)|w|^2) is PD for EVERY individual
generator merely because g(p) is PD for the actual mixture. The
old E93b constrained single-generator numerical value does not by
itself upper-bound arbitrary mixtures. The existing rigorous
13.6986... range uses the unconstrained D_(2/3) certificate and
is unaffected by this qualification.

The actual next quantitative target is an exact certificate

    D_cubic(eta,omega)<73/1000

for ONE specified eta,omega; it would extend the proved dense
one-third threshold beyond1000/73. No such strict bound is proved
in this advisor note. A negative transform at one numerical old
optimizer is not enough to bound the supremum over ALL generators.
Conversely any explicit generator above the proposed target rules
out that particular parameter choice. A certificate must keep the
support-coupled inequalities and all continuum errors, not rely on
the previously invalid single-generator constraint. This is a
mathematically changed, testable universal-conditional-family
derivation, not another root-ensemble calibration or a full Chowla
resolution.

## 9. Read-only audit of the one fixed discovery implementation

The parent predeclared one bounded Dirichlet LP at omega=9.1,
64 support cells, degree10, eta in[0,1/2], and100seconds solver
time. I read `src/cubic_dual_discovery.py` and the complete legacy
`src/e95_discover_sigma.py` it ports. I did not execute either.

The LP divides its pointwise inequality by x=w(t)>0. The inserted
term is correctly G(sigma*x^2)/x=
sigma*x*sqrt(1-sigma*x^2)/4. The cell cosine upper envelope is
conservative since eta and G are nonnegative, including an interior
maximum at a multiple of2pi. The floating envelope and x-grid are
discovery only, not exact interval or continuum certificates.
Every source substitution is count-checked, the legacy source is
unchanged, and the new record is explicitly labelled uncertified.
No consequential normalization error was found.

The parameter choice is intended to test(11), not prove a new
constant by a sampled optimum. Exact radical/Bernstein and Schur
checks would be required for any claimed improvement. If this
single proposal fails to beat the old bound, no extra cell/degree
or frequency sweep follows from this advisor audit. The paper
inequality(10) remains valid independently of that outcome.

## 10. First LP outcome and a different support-cap envelope lemma

The parent reported the fixed cosine-dual discovery terminal with
eta about4.95*10^-9, effectively0, and D about0.072516053.
These are UNCERTIFIED floating discovery values. They give no
automatic use of the new cubic Fourier multiplier, and no omega,
degree or cell sweep is justified by that outcome. No improved
density constant is claimed from them.

The parent then derived a DIFFERENT valid way to use the cubic
profile: a pointwise support cap followed by a convex tangent
extension. I checked the full argument below. This changes the
objective using a new proved constraint, rather than retuning the
failed cosine parameter.

### Cubic support cap on the actual profile

Continue in the P66 one-third contradiction regime of Section8.
The profile H(t)=g(p(t))=G(v(t)), v=4e, is continuous, PD and
supported in[-1,1]. Also v(t)<=2/3 and G is strictly increasing
on[0,2/3], with G(2/3)=1/(6sqrt(3)).

For0<t<1 put k=ceil(1/t)-1. Since H(nt)=0 for n>k, the sampled
positive-definite sequence has a nonnegative trigonometric symbol
of degree k. The same Caratheodory-Fejer/Egervary-Szasz bound used
in the existing support-coupled certificates gives

    H(t)<=c_k*H(0)<=c_k*G(2/3),
    c_k=cos(pi/(k+2)).

At reciprocal boundaries the value H(1)=0 supplies exactly the
same finite-support conclusion. If H(0)=0 then the entire profile
vanishes, inconsistent with positive limiting density; no invalid
division by zero is needed.

There is a unique b_k in[0,2/3] with

    G(b_k)=c_k*G(2/3),
    b_k^2*(1-b_k)=(4/27)c_k^2.                     (12)

Consequently the ACTUAL v(t) is at most b_k. Define b(0)=2/3 and
b(t)=0 for t>=1. On(0,1) the staircase b(t)=b_k is nonincreasing.
On any certificate t-cell the cap from its lower endpoint is an
upper bound throughout the cell, so using that relaxed cap is valid.

### A convex function that preserves the actual density

For b in[0,2/3] define

    Psi_b(v)=phi(v),                         0<=v<=b,
    Psi_b(v)=phi(b)+phi'(b)*(v-b),            v>=b.

Its derivative increases up to phi'(b), then remains constant.
Thus Psi_b is C1, convex and increasing; Psi_b(0)=0. It lies below
phi above b, but is exactly phi at every value of the actual v(t).
This last equality is what licenses its insertion before Jensen.
It is not legitimate merely to replace phi by a smaller function
on arbitrary profiles.

The valid new functional bound is

    d<=D_envelope,
    D_envelope=sup_(w in W) integral_0^1
                     Psi_(b(t))((2/3)|w(t)|^2)dt.   (13)

Indeed d=integral Psi_(b(t))(4e(t)); apply convexity to the SAME
Gabor mixture, and use monotonicity to increase the global mixture
mass sigma<=2/3. Complex generators may again be majorized by a
nonnegative autocorrelation because Psi_b is increasing. Individual
generators need not satisfy the cubic cap. Their excursions beyond
it are measured by the linear branch instead of being incorrectly
forbidden.

### Smoothing and support dilation

The exact-mixture caveat of Section8 remains essential. At fixed
smoothing radius use the finite-X Gabor mixtures; the actual smoothed
profile tends uniformly to the continuous limiting e as the radius
tends to zero. Each Psi_b is uniformly Lipschitz on the relevant v
interval, since phi'(b)<=phi'(2/3)=sqrt(3)/4. Thus replacing 4e by
its smoothed approximation introduces a vanishing integral error.
Finite mixture masses are handled as before with a vanishing
upper slack on sigma.

There is an especially simple dilation check. For every fixed v,
Psi_b(v) is NONDECREASING in b: when v>b its b-derivative is
phi''(b)*(v-b)>=0, and on the other branch it is constant. Since
b(t) is nonincreasing,

    Psi_(b((1+delta)s))(v)<=Psi_(b(s))(v).

Dilation of the piece support[-1-delta,1+delta] into W therefore
bounds its integral by(1+delta) times the functional in(13) directly.
No uniform passage through infinitely many staircase jump points
is required. This avoids a possible hidden approximation gap.

### The new cap is genuinely different from the old generator cap

For w in W, the existing support constraint is |w(t)|<=c_k, so
the old argument only enforces v_generator<=(2/3)c_k^2. Put c=c_k.
Direct substitution gives

    G((2/3)c^2)/G(2/3)=c^2*sqrt(3-2c^2).

This exceeds c exactly when c^2 is in(1/2,1). Consequently b_k is
strictly below the old maximal generator argument for EVERY finite
k>=3. At k=2 the caps agree (b_2=1/3); at k=1 the generator cap
is already stronger. The inequality therefore contains additional
information, rather than duplicating the earlier support cap for w.

The inspected P66/tdense10-12/tdense15 records use the cubic front
cap, generator support caps, and single-generator numerical tests.
I found no prior pre-Jensen tangent-envelope argument there. This is
only a project-record check, not an external novelty claim.

An exact bound D_envelope<73/1000 would extend the existing dense
one-third range. No such constant is proved here. A discovery LP
with this NEW objective can propose a fixed exact certificate; it
does not certify a new theorem by floating convergence. Upward
rational enclosure of a cap b is conservative, since Psi_b increases
with b. Any final certificate must handle its piecewise breakpoint,
the radicals and the support/Schur inequalities globally. The full
unrestricted square-root problem remains open.

## 11. Envelope discovery and exact-certificate algebra audit

The single changed-objective LP was reported terminal with numerical
D about0.072383313, compared with the fixed old-objective discovery
about0.072516053. This is a DISCOVERY comparison, not a certified
new constant. I read the complete `src/cubic_cap_discovery.py` and
checked its substitutions into the unchanged legacy LP. It correctly
uses Psi_b((2/3)x^2)/x, with the tangent slope1/[4sqrt(1-b)] and
the cell's lower-endpoint support k. Its floating bisection is not
an exact cap certificate.

The parent subsequently proposed a rational certificate with
D1=29/400 and C<400/29. I read the complete
`src/cubic_cap_certify.py` and its reused rational/Bernstein/Schur
helpers. The proof algebra and conservative directions check:

- The rational cap is rounded UP on the increasing cubic branch
  b in[0,2/3], with b^2(1-b)>=(4/27)*cap^2 and cap an exact upper
  bound for the cosine. Thus it weakens, rather than overstates,
  the actual cubic cap.
- The coordinate u=sqrt(1-x) has its lower endpoint rounded DOWN,
  so the covered interval contains the entire allowed generator
  domain x<=cap.
- With v=(2/3)(1-u^2)^2 and A=RHS-1/2, the radical branch is
  certified by (1-v)/4-A^2>=0, or directly A>=0.
- The high branch is
  Psi_b(v)=1/2-(2-b-v)/(4sqrt(1-b)). Since b,v<=2/3, its numerator
  is at least2/3 and has the required positive sign. Hence
  (2-b-v)^2-16(1-b)A^2>=0 is a valid sufficient squared inequality.
- On a u-leaf[lo,hi], v is decreasing. Therefore v(hi)>=b correctly
  guarantees the entire leaf is on the tangent branch. Otherwise
  proving the full phi upper bound is conservative, including a
  leaf straddling the breakpoint.
- Removing an exact factor1-u preserves nonnegativity on[0,1].
  Monotone Bernstein coefficients for beta justify using the
  certified lower branches for w(2t). The potential terms cancel
  after integration.
- The Schur bound has RHS2D1 times its positive test function,
  as required for the HALF-line objective integral_0^1 a(t)w(t)dt.

I found no consequential algebraic or source-normalization gap.
The exact producer must still finish with all leaves and continuum
Schur cells passing, followed by independent reconstruction before
claiming C<400/29. The theorem remains unclaimed at this audit
stage; neither an optimizer status nor the numerical LP value can
replace those checks.

An optional explicit enclosure avoids the cubic root. Writing
delta=2/3-b, equation(12) is

    delta^2*(1-delta)=(4/27)sin^2(pi/(k+2)).

Thus b<=2/3-a_k, a_k=2sin(pi/(k+2))/(3sqrt(3)). One monotone
refinement is delta>=a_k/sqrt(1-a_k). These are valid conservative
upper caps; they are not needed for the rational bisection method.
No computation or additional parameter choice is introduced by
these paper enclosures.

## 12. Completed independent certificate and quantified theorem

The producer and independent checker have now BOTH completed. I read
the complete `src/cubic_cap_verify.py` port, its complete legacy
independent implementation, the saved certificate metadata and
`.research/experiments/cubic_cap_2026-10-23/independent_verification.json`.
I did not execute a checker or recompute any artifact.

The completed exact verification records

    815 pointwise leaves, 127 CF caps,
    188 reconstructed support lines, 64 Schur cells,
    75 tangent leaves,
    D1=29/400,
    min Schur margin=251243300521/1966080000000000>0.

The independent implementation reconstructs the beta polynomials
from their rational Bernstein data; proves the long Gram lines by
Sturm and support lines by rational finite-symbol evaluations;
independently encloses pi/cosine caps; verifies the cubic caps;
checks exact no-gap leaf coverage; and reconstructs both radical
and tangent proofs. The continuum Schur polynomials are rebuilt
from direct exact integrals at four rational points and interpolation.
They match the producer's polynomials and positive margins.

Both use FLINT rational arithmetic in parts of their implementations.
This is independently reconstructed exact arithmetic, not an independent
arithmetic backend, Lean/kernel proof or external specialist review.
The optimizer contributes only the proposal; every accepted sign in
the saved certificate is rationally verified. I found no consequential
gap in the complete source/artifact audit.

Combining the envelope lemma with this certificate proves, under
the explicitly quoted P58/P61/P66/P68 inputs, the following partial
theorem:

    For EVERY fixed real0<C<400/29 there exists c(C)>0 such that
    EVERY nonempty finite set A of DISTINCT POSITIVE INTEGERS
    satisfying max A<=C|A| obeys

        M(A)=-min_(all real x)sum_(a in A)cos(ax)
                                      >=c(C)|A|^(1/3).

The constant c(C) is INEFFECTIVE. The endpoint is STRICT C<400/29,
approximately13.7931034483. This extends the project's previous
C<1000/73 range. It does not improve an unrestricted universal
exponent, prove full square-root Chowla, or give a counterfamily.
External priority has not been investigated in this bounded pass.

For clarity, failure of this uniform statement would give a sequence
with M/n^(1/3) tending to zero. Bounded n yields only finitely many
supports under max A<=Cn and each has M>0, so n and X tend to
infinity along a subsequence. The existing compactness framework
then gives d>=1/C. The exact functional bound gives d<=29/400,
contradicting C<400/29. This proves the all-finite quantifier, not
merely the assertion on a chosen limiting family.

I also read the completed main record
`cubic_profile_cap_2026-10-23.md`. Its proof normalizations,
conservative rounding, completed verification status and final
finite-case argument agree with this audit.

## 13. A quantitative cusp at the old cubic front endpoint

The parent noted a useful paper consequence, independent of the
new constant. IF p(0)=u_*=(3-sqrt(3))/6, then v(0)=2/3.
Writing delta_k=2/3-b_k, equation(12) gives

    delta_k^2*(1-delta_k)=(4/27)sin^2(pi/(k+2)),
    delta_k>=2sin(pi/(k+2))/(3sqrt(3)).

For k=ceil(1/t)-1 one has sin(pi/(k+2))/t tending to pi as
t decreases to zero. The actual support cap v(t)<=b_k therefore
proves

    liminf_(t down to0) [v(0)-v(t)]/t>=2pi/(3sqrt(3)),
    liminf_(t down to0) [p(0)-p(t)]/t>=pi/6.       (14)

The second statement uses phi'(2/3)=sqrt(3)/4 and continuity of v.
It excludes an EVEN profile that is C1 across0, or any front with
zero right derivative, from attaining the endpoint p(0)=u_*.
A right-C1 front with a negative slope is allowed. Thus this is not
a strict universal front gap: a cusp is a legitimate possibility.
Neither the exact certificate nor the theorem in Section12 depends
on this bonus consequence.

## 14. First next lemma: a coupled cubic three-point dual

This is a PAPER derivation, not a new experiment or a claimed further
constant. It retains actual (t,2t) cubic PD information beyond the
pointwise caps. Let c=G(2/3)=sqrt(3)/18, H(t)=G(v(t)). The3-by3
Toeplitz inequality gives

    H(2t)-2H(t)^2/H(0)+H(0)>=0.

Since H(0)<=c, weakening its right normalization proves pointwise

    R(t)=G(v(2t))-2G(v(t))^2/c+c>=0.              (15)

If H(0)=0 all H vanish and(15) remains immediate; otherwise the
difference from the previous left side is
2H(t)^2*(1/H(0)-1/c)+(c-H(0))>=0.

Take ANY continuous gamma:[0,1]->[0,1/24]. Adding the nonnegative
integral gamma*R to the density bound and changing variable2t gives

    d<=c*integral_0^1 gamma(t)dt
                        +integral_0^1 Lambda_t(v(t))dt,
    Lambda_t(v)=phi(v)+(gamma(t/2)/2)G(v)
                                -2gamma(t)G(v)^2/c. (16)

The new coefficient functions retain the cross-scale interaction.
They are valid BEFORE Jensen; no PD condition on an individual
generator has been imposed. Since

    (G^2)''=(1-3v)/8,
    max_(0<=v<=2/3)(G^2)'=1/48,
    |G''|<=3sqrt(3)/8, phi''>=1/8,

one gets the explicit uniform bounds

    Lambda_t'' >=(16-9sqrt(3))/128>0,
    Lambda_t' >=1/4-sqrt(3)/96>0,
    Lambda_t(0)=0.                               (17)

Thus Jensen and complex-generator majorization apply as before:

    d<=c*integral gamma
       +sup_(w in W)integral_0^1
                            Lambda_t((2/3)|w(t)|^2)dt. (18)

One may also continue Lambda_t tangentially at the actual cap b(t),
just as in Section10. It remains convex/increasing and equals the
actual integrand. For dilation, extend gamma continuously a short
distance past1 within[0,1/24], for example constantly; the actual
profile vanishes there and Lambda_t(0)=0, so this changes no actual
integral. Uniform continuity of gamma and the nonincreasing cap
give the same vanishing approximation errors as before.

No new constant is asserted from(18). It is the precise next
analytic/certificate input, rather than a larger version of the
previous cell grid or an unproved fourth-moment condition.

### An analytic discriminator for the new interaction

The coupled condition is not automatically satisfied by all normalized
generators, and can detect an interaction where both local caps are
inactive. Let w be the normalized half-sine autocorrelation,

    w(t)=(1-t)cos(pi*t)+sin(pi*t)/pi, 0<=t<=1,

extended evenly and by0. It is the autocorrelation of
sqrt(2)sin(pi*s) on[0,1], hence belongs to W and is nonnegative.
At t=1/4 write

    x=w(1/4)=sqrt(2)*(3/8+1/(2pi)), y=w(1/2)=1/pi,
    H_*(s)=G((2/3)s^2)/c=s^2*sqrt(3-2s^2).

From pi<22/7 and pi>3,

    57/100<x^2<3/5,
    2H_*(x)^2-1>1/5,
    H_*(y)<sqrt(3)/pi^2<7/36<1/5.

The middle inequality follows by monotonicity of6u^2-4u^3-1
on0<=u<=1 and its value at u=57/100. Consequently

    R_generator(1/4)/c
                    =H_*(y)-2H_*(x)^2+1<-1/180. (19)

At the same two positions, the scalar cubic caps are satisfied:
H_*(x)<9/(5sqrt(5))<cos(pi/5), and H_*(y)<1/2.
The generator may violate other scalar caps near0; no global
feasibility assertion is made. But by continuity a nonnegative
gamma supported sufficiently near1/4 yields a strictly negative
dual contribution for this generator. Both scalar caps remain
inactive on the relevant neighborhoods near1/4 and1/2, so the
conclusion persists with tangent continuation there. This is a
concrete paper discrimination of the new coupled term, not a proof
that the supremum in(18) decreases. Any further quantitative
theorem must still be proved or exactly certified over ALL W.

This analytic direction can be made explicit without another computation.
On[0,1], H_*'(s)=6s(1-s^2)/sqrt(3-2s^2)<=3, H_*<=1, and
|w'(t)|=pi*(1-t)|sin(pi*t)|<4. Therefore

    L(t)=H_*(w(2t))-2H_*(w(t))^2+1

is72-Lipschitz near1/4. Equation(19) gives

    L(t)<-1/360 whenever |t-1/4|<=1/30000.

For ANY0<rho<=1/24 the explicit continuous triangular choice

    gamma(t)=rho*(1-30000|t-1/4|)_+

therefore satisfies

    integral gamma(t)*R_generator(t)dt
                          <=-c*rho/(360*30000)<0. (20)

Its area is rho/30000. The numerical-looking radii here are exact
rational paper choices, not optimized data. The scalar caps remain
inactive throughout these neighborhoods: pi>3 strengthens the upper
bound to x^2<169/288<59/100, hence
H_*(x)<1593/2000. Its variation is below12/30000=1/2500,
still leaving it below4/5<cos(pi/5). For the child value the variation
is below24/30000=1/1250, leaving H_*(y)<1/2. Thus(20) remains
a strict improvement on this generator even when the tangent cap
is retained. It is NOT a proof that the supremum over W improves,
nor that this generator satisfies every other scalar cap near0.
The exact new theorem in Section12 is independent of this FIRST NEXT
application; no further job or parameter sweep is asserted here.
