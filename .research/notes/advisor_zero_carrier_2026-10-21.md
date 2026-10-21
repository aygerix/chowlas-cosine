# Independent advisor audit: the exceptional zero reciprocal carrier

Date: 2026-10-21. Internal AI advisor review, not external scrutiny.
Paper identities and the limited sufficient bound below have been checked
independently. The finite computations were run by the lead on Dirichlet;
this advisor read their producers, verifier and saved results and launched
no computation, VM job or worker. Lean/kernel-checked mathematical proofs:
none. Chowla, L25 and a uniform zero-carrier bound remain open.

## 1. Exact seed, energy and sign orientation

Let A be any nonempty finite set of distinct positive integers, n=|A|,
F(z)=sum_{a in A} z^a, f=Re F, D=2f, and M=-min f. All circle integrals
are normalized by dx/(2*pi). For any real lambda>M put

    W=lambda+F,  p=1/W,  S=integral |p|^2,
    g=lambda^2*S-1,  q0=Im p,
    T0=sum_{a in A} [z^a]p^2.

The positive real part of W on the closed disk makes p analytic in a
neighborhood of that disk. Its coefficients are real, its constant is
1/lambda, and g>0. Orthogonality gives

    Q0=integral q0^2=(S-lambda^-2)/2=g/(2*lambda^2),
    H0=integral D*q0^2=1/lambda-lambda*S-T0/2
                              =-g/lambda-T0/2.              (1)

Indeed, integral D|p|^2=2(1/lambda-lambda*S), since
Re p=(lambda+f)|p|^2. Also integral D Re(p^2)=T0, and
q0^2=(|p|^2-Re(p^2))/2. These verify the factors in (1).

There is an exact derivative identity fixing the orientation of the
correction. Write B=Im F and C_p=sum_{a in A}[z^a]p. Analyticity gives
integral Fp=0, hence

    C_p=integral F*conjugate(p)
       =2*integral B*Im p
       =-2*integral B^2/|lambda+F|^2.

Differentiate with F fixed, using d p/d lambda=-p^2:

    T0=-d C_p/d lambda
      =-4*integral (lambda+f)*q0^2 < 0.                    (2)

Thus the correction -T0/2 is POSITIVE. Merely proving T0<0 does not
prove H0<0. Define the dimensionless parameter

    tau=-lambda*T0/(2g).

Then

    H0/Q0=2*lambda*(tau-1).                               (3)

At the actual calibration lambda=2*sqrt(n), M<=sqrt(n), (2) supplies
only

    tau >= 1-M/lambda >= 1/2.

The sign claim needs the opposite-side bound tau<1. A uniform
tau<=1-eta, eta>0 absolute, would give M>=lambda*eta=2*eta*sqrt(n)
from the negative Rayleigh quotient. A qualitative H0<0 by itself
does not give a square-root constant.

The identities above also hold for nonnegative weighted analytic F,
with C_p and T0 interpreted as the corresponding weighted pairings.
No individual Boolean coefficient restriction was used in their proof.

This seed is genuinely exceptional among the reciprocal carriers.
Since |Im p|<=1/[2*(lambda-M)], at low M

    ||q0||infinity/sqrt(Q0) <= sqrt(2)/sqrt(g).

The possible divergence as g tends to zero prevents applying the earlier
bounded-normalized-amplitude retirement of positive carriers to q0.

## 2. A proved large-gap subcase, and its limit

At lambda=2*sqrt(n) with M<=sqrt(n), set zeta=F/(lambda+F).
Then zeta(0)=0, ||zeta||infinity<=1, and ||zeta||2^2=g<=1. The pointwise
Schur bound follows from

    |lambda+F|^2-|F|^2=lambda^2+2*lambda*f >= 0.

Since p=lambda^-1*(1-zeta), Cauchy--Schwarz on the n selected
coefficients gives

    |T0| <= sqrt(n)/lambda^2 * ||zeta^2-2*zeta||2
          <= 3*sqrt(g)/(2*lambda).

Consequently

    H0 <= [-g+(3/4)*sqrt(g)]/lambda,
    H0/Q0 <= -2*lambda*(1-3/(4*sqrt(g))).                 (4)

In particular H0<0 when g>9/16, and a fixed gap above this threshold
gives a square-root negative quotient. This is an independently proved,
restricted sufficient condition. It does not establish any Boolean
lower bound on g, and the large-gap branch was already accessible to
other reciprocal witnesses. It is not a new unrestricted Chowla result.
The unresolved branch includes arbitrarily small g, precisely where the
normalized amplitude argument loses its bound.

## 3. The two-frequency sign reversal is real, but miscalibrated

For F=z+z^2 and lambda>9/8, an independent autocorrelation calculation
gives

    S=(lambda+1)/[lambda*(lambda-1)*(lambda+2)],
    T0=-4/lambda^3+3/lambda^4,
    H0=(lambda^2-11*lambda+6)
          /[2*lambda^4*(lambda+2)*(lambda-1)].             (5)

For example, the first two nontrivial autocorrelations of |p|^2 both
equal -S/(lambda+1), and their constant equation yields S above.
The coefficients of p^2 at 1 and 2 give the stated T0. Substitution
into (1) gives (5).

Thus H0>0 for lambda>(11+sqrt(97))/2. This refutes a sign assertion
with arbitrary oversized lambda, even for Boolean F. It does NOT
refute the stated fixed-cardinality problem: for this A, n=2 and the
required lambda=2*sqrt(2) lies on the negative side of (5). The exact
minimum M=9/8 does satisfy the actual-low-M hypothesis.

Attempted repair: add a large, highly dilated Sidon-difference block to
raise n and hence lambda while preserving the low-frequency prefix.
The repair fails at the required implication. Low-index Taylor
coefficients are preserved, but neither S nor the full selected T0 is.
Every new selected frequency L*c contributes the PURE high-block
coefficient (the low-degree-zero term), which does not tend to zero
with L. The L2 norm also sees the complete high-block reciprocal.
For fixed prefix and pad, separation tends instead to the genuine
two-variable expression

    integral_{x,y} 2*Re(F_prefix(x)+F_pad(y))
          *[Im 1/(lambda+F_prefix(x)+F_pad(y))]^2.

This is not the prefix energy. Continuity and equidistribution apply
because the separated sum retains a positive inverse margin, but they
do not determine the sign of this two-variable integral. Large-lambda
prefix positivity therefore supplies no Boolean fixed-lambda
counterexample without a further pad-energy estimate. No such estimate
or Boolean positive-energy example has been proved here.

## 4. Residual certification: what the code proves

Audited sources:

- `src/cstar_zero_reciprocal.py`;
- `src/cstar_zero_reciprocal_verify.py`.

The FFT proposes a dyadic analytic polynomial P only. If
r=(lambda+F)P-1 and delta=lambda-M_upper>0 is supplied by an existing
ALL-CIRCLE upper bound, then

    ||p-P||2 <= ||r||2/delta =: epsilon.

The producer includes all residual degrees through band+max(A), not
just the retained reciprocal coefficients. Writing its integer
coefficient numerator as U+lambda*V, its exact residual square is

    (sum U_j^2 + 4*n*sum V_j^2 + 2*lambda*sum U_j*V_j)/den^2.

Arb encloses the sole irrational lambda=2*sqrt(n). The propagated bounds

    |S-||P||2^2| <= 2*||P||2*epsilon+epsilon^2,
    |T0-sum_A [z^a]P^2|
       <= sqrt(n)*(1/delta+||P||infinity)*epsilon

are valid. The code safely bounds ||P||infinity by the sum of absolute
coefficients. Formula (1) then encloses the INFINITE reciprocal energy
and quotient. This is not an uncertified circle grid integral.

The finite sine vector Im P is independently certifiable, with

    Qfinite=(1/2)*sum_{j>=1} P_j^2,
    Hfinite=sum_{a in A} sum_{j>=1} P_j*P_{j+a}
               -(1/2)*sum_{a in A} sum_{1<=j<a} P_j*P_{a-j}.

The signed Laurent-square implementation agrees with that correlation
formula. The separate verifier rebuilds the polynomial residual by
sparse integer shifts, reconstructs the selected T0 by the direct
formal inverse, and independently checks the finite signed moments.
The margin remains conditional on the saved all-circle M_upper
certificate; the reciprocal calculation does not create that bound.

Saved results in `.research/experiments/zero_reciprocal_2026-10-21/`:

| Input | Status | Certified H0/(Q0*sqrt(n)), coarsely rounded outward |
| --- | --- | --- |
| Boolean-projection n=56 | Producer and independent verifier PASS | [-0.3603,-0.3595] |
| Boolean-projection n=306 | Producer and independent verifier PASS | [-0.3023,-0.3020] |
| Actual-low-M forced prefix n=337, occupied 1 through 243 | Producer and independent verifier PASS | [-0.5441,-0.5431] |

The exact rational intervals are in `results.json` and `prefix.json`;
the independent reports are `verification.json` and
`prefix_verification.json`. The coherent-prefix case was a predeclared
adversarial sign test, different from the two projection outputs. It
did not falsify the sign. It also does not justify extending a control
sweep or claiming a universal rate. All three are finite certified
successes for this explicit seed.

## 5. Decision and the next mathematical discriminator

Keep q0 available as an actual signed Rayleigh seed; it has not been
falsified or proved uniformly. Stop successful-control enlargement and
do not deploy a GPU on the basis of these three cases. The meaningful
next proof target is a BOOLEAN bound on the selected-coefficient
correction, for example

    -sum_{a in A}[z^a](lambda+F_A)^-2
        <= (2*(1-eta)/lambda)
               *(lambda^2*||(lambda+F_A)^-1||2^2-1),       (6)

for some absolute eta>0, with precisely n=|A|, lambda=2*sqrt(n), and
actual M<=sqrt(n). Equation (6) is an explicit conjectural sufficient
inequality, not a new derivation or an assumed universal principle.
Even its eta=0 sign version is unproved. Any attempted proof must use
the zero/one coefficients beyond the generic analytic identities in
Section 1; positivity yields only the lower bound on tau.

The lead's provisional quantitative discriminator R0 takes eta=1/400:
tau<=1-1/400, equivalently H0/Q0<=-sqrt(n)/100, implying
M>=sqrt(n)/200. This is a falsifiable candidate for the next derivation,
not an inference from the three successful finite tests. Its small-g
branch is the priority; (4) does not settle it.

A useful next derivation, before any new numerical examples, is to
analyze the two-variable energy in Section 3 for a specified Boolean
prefix/pad interaction and establish an actual SIGN transfer or its
failure. That addresses the exact missing step in the attempted
counterexample; merely increasing a dilation does not. If no such
coefficient or interaction estimate emerges, pivot away from the
single reciprocal ansatz to the existing full signed-Rayleigh problem,
and retain the independent all-circle construction track. A new
construction cycle needs a structural change: the completed projection
pilot kept span proportional to n, so its finite improvements did not
give a credible vanishing-ratio mechanism at fixed density.

For completeness the lead's odd square-root diagnostic is algebraically
correct. If h=2*sqrt(lambda)*(sqrt(lambda+F)-sqrt(lambda)) and q=Im h,
then h^2=4*lambda*(F-h) implies

    integral D*q^2=2*lambda*(integral D*|lambda+F|-n).

This does not supply a Boolean bound on the right side and should not
be promoted to a new route simply by changing the nonlinear seed.
There is no new universal exponent, full Chowla proof, or all-circle
counterexample family in this cycle.
