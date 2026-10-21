# Advisor audit: the minimum-modulus reduction and the phase retained by Rayleigh

2026-10-21. Independent internal paper derivation. Only this assigned
note was edited; no research computation, VM job, provisioning, spending,
external message, or additional agent was performed. No Lean/kernel check
or external specialist review is claimed. Full Chowla remains open.

All circle integrals are normalized. A is a finite nonempty set of
distinct positive integers, n=|A|, F=sum_(a in A)z^a, f=Re F, D=2f,
M=-min f and K=2M. The principal branch here has ACTUAL M<=sqrt(n),
lambda=2sqrt(n), W=lambda+F, so Re W>=lambda/2 throughout the disk.

## 1. The normalized phase-Hessian infimum is EXACTLY minimum modulus

For nonzero real-coefficient analytic polynomials H with H(0)=0, define

    R=H/W, q=Im R, Q_R=integral q^2,
    C_F(H)=integral |W|q^2.

R is analytic beyond the closed disk, has real coefficients and zero
constant, so q is a real odd mean-zero function and

    Q_R=(1/2)integral |H|^2/|W|^2>0.

Then

    inf_H C_F(H)/Q_R = min_circle |W|.              (1.1)

The lower bound is immediate from the weighted average. For the reverse
bound, take ANY real-coefficient analytic polynomial R with R(0)=0 and
set H=W R. This H is an admissible analytic polynomial, and q=Im R
ranges over every finite sine polynomial. Such polynomials are dense in
odd real L2. Since |W| is even, an odd pair of localized bumps near a
minimum and its reflection has quotient arbitrarily close to min |W|.
If the minimum lies at 0 or pi, use bumps arbitrarily close to that
endpoint, with their odd reflections; continuity gives the same limit.
No positive loss is forced by odd functions vanishing at the endpoint.

Thus an unrestricted normalized phase-Hessian search is a minimum-modulus
problem, not a new Boolean spectral estimate. Removing the denominator
Q_R, or restricting the search and identifying its value with (1.1), would
be invalid.

## 2. A substantive comparison: L1 flatness implies a modulus deficit

Put m=min|W|. Then 0<m<=lambda: otherwise the analytic function 1/W
would have boundary modulus strictly smaller than its value 1/lambda at
zero. Let

    b=lambda-m^2/lambda,
    P=W-m^2/W.

Since Re W>0 and |W|>=m,

    Re P=Re W*(1-m^2/|W|^2)>=0, P(0)=b.

The exact decomposition

    f=Re(P-b)+m^2 Re(1/W-1/lambda)

and positivity give ||Re(P-b)||_1<=2b. The second analytic term has
zero constant; hence

    ||Re(1/W-1/lambda)||_2^2
       =(1/2)*(integral |1/W|^2-1/lambda^2)
       <=(1/2)*(1/m^2-1/lambda^2).

Therefore

    ||f||_1<=2b+(m/lambda)*sqrt((lambda^2-m^2)/2).   (2.1)

Equivalently, for epsilon=1-(m/lambda)^2,

    ||f||_1/lambda<=2epsilon+sqrt(epsilon/2).        (2.2)

Consequently qualitative root-scale L1 flatness implies a root-scale
modulus deficit lambda-m. For example, L25's ||f||_1>=sqrt(n)/10
would force epsilon>=1/512 and hence lambda-m>=sqrt(n)/512; the constants
are deliberately conservative. Indeed epsilon<1/512 would make the
right side of (2.2) less than 9/256<1/20.

Conversely, a uniform root-scale modulus deficit would imply Chowla
directly, since

    |W|>=Re W>=lambda-M, so lambda-m<=M.

This establishes the implication chain

    qualitative low-M L1 flatness => root modulus deficit => root M.

No converse from Chowla ALONE is proved. It would be inaccurate to claim
that minimum modulus is known equivalent to Chowla, or that strict
inequivalence has been established on Boolean supports. A Boolean low-M
family with lambda-m=o(sqrt(n)) would also have ||f||_1=o(sqrt(n)) by
(2.2), so finding such a falsifier reaches the existing flatness gap.

### A concrete actual-low-M Boolean control does not falsify modulus

One finite algebraic test suffices; no family sweep is proposed. Let k be
odd, q0=k+1, B={1,q0,...,q0^(k-1)}, and A its positive integer differences.
The minimal q0-adic exponent proves these differences distinct, and

    n=k(k-1)/2, f=(|F_B|^2-k)/2>=-k/2,
    M<=k/2<=sqrt(n).

Choose theta=2pi*r/(q0+1) nearest pi/2. Then
|theta-pi/2|<=pi/(k+2) and q0^j*theta is congruent to (-1)^j*theta.
Writing k=2s+1 gives

    F_B(theta)=k*cos(theta)+i*sin(theta).

There are equally many ordered even-before-odd and odd-before-even
pairs, so Im F_A(theta)=0 exactly. Consequently

    F_A(theta)=-(k-1)/2+((k^2-1)/2)*cos(theta)^2
              <=-(k-1)/2+pi^2/2.

For large k, W(theta) is positive real and

    lambda-min|W|>=(k-1-pi^2)/2.

Thus this known admissible Boolean control has a root-scale modulus
deficit. It is not a counterexample to (1.1)'s sufficient target and does
not justify another canonical enlargement. No Boolean falsifier of a
universal modulus deficit was obtained in this audit.

## 3. Retaining the sign term recovers the actual Rayleigh problem

The exact identity is

    integral Dq^2
      =2C_F(H)-2lambda*Q_R-2E_F(H),
    E_F(H)=integral (|W|-Re W)q^2>=0.               (3.1)

Dropping E loses genuine information. In particular

    inf_H [C_F(H)-E_F(H)]/Q_R
       =min Re W=lambda-M.                         (3.2)

The proof is the same odd localization as Section 1, now with the even
weight Re W. This is an exact reparametrization of direct odd Rayleigh,
not a Boolean proof of the minimum or an additional spectral lower bound.

An absolute degree bound on q cannot work uniformly: if min A>2B, any
real degree-B trigonometric q has integral Dq^2=0. Dilation preserves
M and n while arranging this obstruction. Frequency-adaptive bands or
signed envelopes with growing dimension are not excluded.

In particular, bounded normalized amplitude is a substantive limitation:
if ||q||_infinity/sqrt(Q)<=C and integral Dq^2<=-eta*sqrt(n)*Q,
then ||f||_1>=eta*sqrt(n)/(2C^2). Individual bounded-amplitude seeds
cannot avoid qualitative flatness merely by being called direct Rayleigh.
General Fourier Rayleigh functions, including concentrated combinations,
are not subject to an absolute C and remain a different surviving option.

## 4. Reciprocal-phase averaging: exact, but the average is old leverage

The root's identity was independently checked. For lambda>M define

    p_y=1/(lambda+F-i*y),
    q_y=Re p_y INCLUDING its constant,
    I=integral_circle 1/(lambda+f).

Pointwise, with a=lambda+f>0 and t=Im F-y,

    integral_real_y [a/(a^2+t^2)]^2 dy=pi/(2a).

The imaginary numerator t gives the same integral. Tonelli, followed by
the boundedness of D for the signed energy, gives

    integral_y Q_y dy=(pi/2)*I,
    integral_y integral_circle Dq_y^2 dy=pi*(1-lambda*I).

Therefore some phase has Rayleigh quotient at most

    -2*(lambda-1/I).                               (4.1)

The analytic constant is 1/(lambda-i*y), so omitting the real constant
would change both Q and the identity. General phases mix parity; this
is a FULL real-Rayleigh statement, not a mean-zero cosine-only one.

Under M<=lambda/2,

    lambda*I-1=integral f^2/[lambda*(lambda+f)]
              <=||f||_1/lambda,
    0<=lambda-1/I<=||f||_1.                         (4.2)

Here f^2/(lambda+f)<=|f| holds for positive f directly, and for negative
f because |f|<=lambda/2. This phase AVERAGE is exactly the already
known real-resolvent leverage in the f normalization. It creates no new
Boolean inequality. Individual phases may outperform the average, but
no universal improvement or finite-phase extraction is established here.

## 5. Positive reciprocal carriers and their exact correction

Put p=1/W, S=integral |p|^2, and g=lambda^2*S-1>=0. For a positive
integer h, take R_h=e^(ihx/2)*p and either its real or imaginary part.
If h is odd these tests are anti-periodic, but their squares are
2pi-periodic and are valid nonnegative all-circle Rayleigh test densities.
Define the finite signed coefficient sum

    T_h=sum_(a in A,a>=h) [z^(a-h)]p^2.

Both choices have Q_h=S/2 because mean(z^h p^2)=0. Their energies are

    H_im=1/lambda-lambda*S-T_h/2,
    H_re=1/lambda-lambda*S+T_h/2.                    (5.1)

Indeed integral f|p|^2=integral Re p-lambda*S=1/lambda-lambda*S,
and integral f*z^h*p^2=T_h/2. Thus the adaptive choice obtains

    min(H_re,H_im)=1/lambda-lambda*S-|T_h|/2.

For h>X the correction is zero and the quotient is

    -2*[lambda-1/(lambda*S)]=-2lambda*g/(1+g).      (5.2)

At fixed margin lambda>=2M, |p|<=2/lambda and S>=1/lambda^2, so
EVERY positive carrier has

    ||q_h||_infinity/sqrt(Q_h)<=2sqrt(2).           (5.3)

A root-scale negative quotient from an individual such carrier therefore
implies root-scale L1 flatness. The high-carrier norm gap is equivalent to
qualitative flatness up to constants: besides that implication,

    g=||1-lambda*p||_2^2=||F*p||_2^2,
    ||f||_1<=||F||_1<=sqrt(g)*sqrt(lambda^2+n).      (5.4)

At lambda=2sqrt(n), ||f||_1>=delta*sqrt(n) forces g>=delta^2/5.
Neither high carriers nor an expanded batch of individually bounded
carriers is a new route around flatness.

There is one precise boundary to this amplitude argument. At ZERO
carrier, Im p has

    Q_0=(S-lambda^(-2))/2=g/(2lambda^2),

so the same estimate gives only normalized amplitude <=2sqrt(2)/sqrt(g),
which can diverge. Zero-carrier Re p retains a nonzero mean and a uniform
bound. No useful Boolean sign/cost estimate for the exceptional zero-
carrier odd seed was proved here; this is a limitation of the retirement
argument, not a new successful witness.

### A completely explicit low-M Boolean control has T_1<0

This tests only a possible blanket coefficient-sign estimate. The root
never assumed that estimate, and adaptive Re/Im selection in (5.1) uses
|T_h|. Thus the following does NOT refute that family.

Let B={1,12,...,12^10}, C its 55 distinct positive integer differences,
and A={1,3} union 32*C. Then n=57 and, globally,

    M(A)<=2+11/2=15/2<sqrt(57).

The difference identity supplies the padding bound and elementary
12-adic minimal-exponent uniqueness makes C a genuine set. Put
lambda=2sqrt(57), so 15<lambda<16. The old contribution to T_1 is
[z]p^2=-2/lambda^3.

To bound ALL 55 high contributions, consider the bivariate analytic
function

    P(w,z)=[lambda+w+w^3+F_C(z)]^(-2).

For |w|<=3/2, |z|<=1, Re F_C(z)>=-11/2 and
Re(lambda+w+w^3+F_C(z))>15-39/8-44/8=37/8.
Consequently the Taylor coefficient c_(u,v) of P obeys

    |c_(u,v)|<=(8/37)^2*(3/2)^(-u).

For each c in C, the coefficient at degree 32c-2 after substituting
z=w^32 is therefore bounded by

    (8/37)^2*(3/2)^2*q/(1-q), q=(2/3)^32.

Indeed its terms have u=32(c-v)-2 and 0<=v<=c-1. Since
(2/3)^8<1/25, q<1/390625. Summing over C gives a total absolute
high contribution less than

    6/390624=1/65104<1/4096<1/lambda^3.

Hence T_1<-1/4096<0. This is a paper certificate for the explicit
57-frequency support; its very large maximum frequency is harmless to
the quantified statement. No coefficient array or numerical search was
run. It shows that low-carrier correction coefficients need not have a
universal positive sign even inside actual low M, while the adaptive
absolute correction remains available.

## 6. Decision and remaining mathematical work

Retire unrestricted normalized phase-Hessian optimization as an
independent mechanism: (1.1) is exactly minimum modulus. The phase average
in (4.1) and high-carrier gap in (5.2) also reduce to existing leverage
or qualitative flatness. The estimate (2.1) and the explicit T_1 control
are actual derivations, not new names for a missing bound.

The sign-retaining identity remains valid and can represent the full odd
Rayleigh problem, but gives no universal Boolean estimate by itself.
Bounded-degree tests fail under dilation; individual positive carriers
retain a uniform-amplitude flatness requirement. A general growing signed
envelope, or the exceptional zero-carrier odd reciprocal, is not excluded
by these arguments. No decisive Boolean estimate for either is claimed.

The next useful inverse step must exploit actual linked Boolean phase
information or a concentrated full-Rayleigh vector, rather than optimize
a modulus surrogate or count independent phase parameters. Preserve the
independent all-circle construction track. No universal exponent,
absolute Chowla constant, or vanishing-ratio counterfamily was obtained.

## 7. Source audit of the separate Boolean-projection construction pilot

At the root's request I read src/cstar_boolean_projection.py and the
saved boolean_projection_2026-10-21/results.json; no test was rerun.
The two projection normalizations are correct. With grid length N>2X,
the forward-normalized rFFT coefficient vhat_a satisfies

    mean_grid(v*cos(a*x))=Re(vhat_a),
    ||v-f_A||_grid^2=||v||_grid^2+n/2-2sum_(a in A)Re(vhat_a).

Thus selecting the n largest REAL scores at positive frequencies 1..X
and assigning positive half-spectrum 1/2 gives an exact nearest Boolean
cardinality-n projection. The scores themselves need not be positive.
The irFFT with norm='forward' returns sum cos(a*x), not 2sum cos.
DC and exterior frequencies are zero in the Boolean shadow. Pointwise
clipping v to max(v,-Mtarget) is the exact Euclidean sample-positivity
projection. The update v+=P_bool(2P_pos(v)-v)-P_pos(v) is the stated
Douglas--Rachford iteration; no nonconvex global convergence is licensed.

Latent coefficients are unrestricted and can be signed. The final
supports are unrestricted WITHIN the finite ambient interval [1,X], not
restricted to the initializing Bu or fractional-profile family. This
does not resurrect the retired bounded-mean positive-reference residual
class, and it does not establish feasibility for arbitrary span or n.

The all-circle upper certificate also has the correct normalization.
At a true global minimizer f'=0, nearest-grid Taylor comparison gives

    M<=M_grid_upper+pi^2*sum a^2/(2N^2).

The exact remainder 242*sum a^2/(49N^2) exceeds this because pi<22/7.
Every DFT value is checked by an Arb enclosure, so floating hint selection
does not carry the proof. The separately enclosed 192-bit cosine point
certifies a lower M. The saved rational bounds are positive and certify
strict improvement over the particular seeds, as well as BOTH outputs
being above ratio 1/2 and missing the 9/20 target. They are neither
records nor an asymptotic family. GPU deployment is not justified by this
pilot's stated criterion.

One initialization comment in the inspected source needed correction:
coefficients 2n/(X+1)*(1-a/(X+1)), 1<=a<=X, have total mass
nX/(X+1), not n. This affects only the description of an initializer;
the exact n-element Boolean projection and the certified final supports
are unaffected. I notified the root; using 2n/X instead gives exact mass
n if that initialization property is wanted. No rerun of the saved
certificate is required for a comment correction.
