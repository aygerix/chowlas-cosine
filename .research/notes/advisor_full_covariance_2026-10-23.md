# Full covariance: exact Schur-vector tests and their loss of information

2026-10-23. Sole internal AI advisor. Paper derivations and read-only
record review only. No VM, research computation, GPU, additional agent
or outreach. Shared Dirichlet remains on. This is a focused audit and
global review, not a manuscript, a new universal bound or a Lean proof.

## 1. Setting and actual result

For Boolean A, n=|A|, D=max(A), put F=sum_A z^a, lambda=2sqrt(n),
W=lambda+F and p=1/W. The ACTUAL low-M premise M(A)<=sqrt(n)
implies Re W>=lambda/2 on the circle and W is zero-free on the
closed disk. Let C be the exact kernel matrix in the preceding
aggregation note, so

    G=C^-1=Toeplitz_D(|p|^2),
    S=G00=||p||2^2, g=lambda^2*S-1.

Let L=T_D(W), P=L^-1=T_D(p), R=Re(P), and

    H=R-(lambda/2)*G.

Actual low M implies H>=0. The parent proposed testing H on the
adaptive tail Schur vector x=Ctail^-1*v0 and on(1,-x), where

    C=[[lambda^2-1,v0^T],[v0,Ctail]],
    (v0)_j=lambda*1_A(j)-1_A(D-j), 1<=j<D.

The independent result is a precise negative one for this attempted
reduction, with the full matrix retained in the audit:

1. The entire span of those two vectors can be positive definite on
   a growing BOOLEAN zero-free prefix family while g tends to zero.
   The prefixes do not satisfy actual low M; they falsify only the
   proposed relaxation that replaces the full half-plane information
   by these two adaptive tests.
2. The FULL H is exactly a finite compression of the old pointwise
   Schur cap |lambda*p-1|<=1. The covariance representation is exact,
   but the reformulation supplies no new Boolean estimate.
3. The Schur optimizer is genuinely signed even on an explicit
   actual-lowM Boolean support. Absolute-value shortcuts are invalid.

No new coupled zero/one inequality forcing a norm gap was derived.
The mathematically justified decision is to stop generic covariance
repackaging and two-vector/projection polishing as claimed new routes.
The exact representation and original unrestricted goal remain valid.

## 2. Exact evaluation of the adaptive two-vector compression

Write

    ell=v0^T*Ctail^-1*v0,
    s=lambda^2-1-ell=1/S, x=Ctail^-1*v0,
    rho=||x||2^2, X=x^T*Ctail^-1*x,
    A0=x^T*Rtail*x, b0=sum_(j=1)^(D-1)p_j*x_j.

The block inverse is EXACT:

    G=[[S,-S*x^T],[-S*x,Ctail^-1+S*x*x^T]].

For z=(0,x), the compression of H to span{e0,z} has entries

    H00=(1-g)/(2lambda),
    H0z=[b0+(1+g)*rho/lambda]/2,
    Hzz=A0-(lambda/2)*X-(1+g)*rho^2/(2lambda).   (1)

In particular

    z^T*H*z=Hzz,
    (1,-x)^T*H*(1,-x)
      =1/lambda-b0+A0
        -(lambda/2)*[X+S*(1+rho)^2].             (2)

The off-diagonal in(1) is indispensable. Positivity of the two
quadratics alone does not justify subtracting their lower bounds
to infer a new sign; their nonnegative remainders are different.
Even retaining the FULL2-by-2 compression cannot imply the desired
gap, as Section3 shows. Formula(1) is a correct compression, not
an additional Boolean positivity theorem.

## 3. A growing Boolean relaxation counterfamily: prefixes

For A=[1,n], D=n and ANY lambda>1,

    C=(lambda-1)*(lambda*I+J),
    x=(lambda+n-1)^(-1)*1_(n-1),
    g=n/[(lambda-1)*(lambda+n)].

W is zero-free on the CLOSED disk: its numerator
lambda-(lambda-1)z-z^(n+1) is nonzero for |z|<1 by strict
triangle; its only possible circle zero is z1, canceled by1-z,
with W(1)=lambda+n>0. No outside zero-location result is used.

Set m=n-1, q=1-1/lambda and d=(0,1,...,1). The adaptive
two-vector span is exactly span{e0,d}. Direct coefficient summation
gives its H matrix

    H00=(1-g)/(2lambda),
    Hdd=1-q^m-m*(lambda+1)/[2*(lambda-1)*(lambda+n)],
    H0d=-(1-q^m)/(2lambda)
                         +m/[2*(lambda-1)*(lambda+n)]. (3)

For example the first term in Hdd is the exact Toeplitz form

    d^T*R*d=m/lambda
       -lambda^-2*sum_(k=1)^(m-1)(m-k)*q^(k-1)=1-q^m.

At lambda=2sqrt(n), as n tends to infinity,

    g->0, H00~1/(2lambda), Hdd->1/2,
    H0d=-3/(8n)+o(1/n).

Thus this whole adaptive plane is positive definite for all
sufficiently large n, although its putative norm-gap conclusion
is false. This is not an actual-lowM counterfamily: old P29 gives
linear M for prefixes. It isolates the information lost when
actual half-plane positivity is replaced by these tests.

### One explicit paper check: n256, lambda32

Here g=8/279<1/32, m255, q31/32. Bernoulli's strict binomial
inequality gives(32/31)^31>2, so q^255<q^248<1/256.
In(3),

    H00>31/2048,
    Hdd>127/256,
    |H0d|<1/32.

For Hdd the rational subtraction8415/17856 is below1/2;
for H0d both displayed absolute summands are below1/64.
Consequently its determinant exceeds

    (31*127)/524288-1/1024=3425/524288>0.

Nevertheless the FULL H has a negative vector. Take h with
coefficients+1 on0,...,127 and-1 on128,...,255. It has
squared norm256 and coefficient sum0. The exact prefix inverse
gives

    h^T*G*h=256/[32*31],
    h^T*R*h=3-4q^128+q^256<=3.

Hence h^T*H*h<=3-128/31=-35/31<0. The two Schur-vector
tests miss a genuine negative direction of the full necessary
matrix condition, even on this simple Boolean input. No numerical
test or resource action is required for any of these statements.

## 4. The full matrix is exactly the existing Schur multiplier cap

The parent found the following exact cancellation; I checked every
coefficient independently. Put

    u=lambda*p-1=-F/W, u0=0,
    r_d=sum_(j>=1)u_j*u_(j+d), d>=0.

Here r0=g. Real coefficients give, for d>0,

    G_(i,i+d)=sum_(j>=0)p_j*p_(j+d)
                      =p_d/lambda+r_d/lambda^2.

The off-diagonal of R is p_d/2, so ALL finite p_d terms cancel
in H. Its diagonal is(1-g)/(2lambda), and off-diagonal is
-r_d/(2lambda). Therefore

    H=[I-Toeplitz_D(|u|^2)]/(2lambda).          (4)

The pointwise statement |u|<=1 is EXACTLY equivalent to
Re W>=lambda/2, since

    |W|^2-|F|^2=lambda^2+2lambda*Re F.

Thus the new matrix language is a finite compression of the
already-used Schur condition. C^-1 retains all inverse coefficients,
but that retention by itself does not produce a lower bound on g.
Weighted geometric low-M countermodels also satisfy the full Schur
cap and can have g arbitrarily small. Booleanity must enter through
an additional quantitative identity, not another compression of(4).

Equation(4) does not prove that every possible Boolean use of C is
futile, nor that a finite compression is equivalent to the entire
pointwise cap. It proves that this particular positivity constraint
has not supplied information beyond the old generic half-plane.

## 5. Audit of the parent's congruence identity

Let V=T_D(Wrev), B_D=L^-1*V=T_D(B). Coefficient Toeplitz
matrices commute, and the exact kernel factorization is

    C = L L^* - V V^* = L (I - B_D B_D^*) L^*.

Here multiplication signs are matrix products; L^* denotes
conjugate transpose. Consequently

    L^* C^-1 L = (I - B_D B_D^*)^-1.

Congruencing Re(P)>=(lambda-M)C^-1 by L^*,L gives

    Re(L) >= (lambda-M) (I - B_D B_D^*)^-1.     (5)

The orientation L^* on the LEFT is necessary; replacing it by L
would be wrong for nonnormal Toeplitz matrices. This is a valid
full-matrix identity. Generic trace/Hilbert-Schmidt estimates or
operator-norm bounds on its factors would again lose the linked
Boolean structure. No new such estimate was proved in this audit.

## 6. Signedness cannot be removed inside actual low M

Take A={1,3,4}, the positive differences of{0,1,4}. Its exact
square identity proves M<=3/2<sqrt(3), so this is INSIDE the
actual premise, with lambda=2sqrt(3). Direct kernel entries give

    Ctail=(lambda-1)*
       [[lambda+1,1,0],[1,lambda+1,1],[0,1,lambda+1]],
    v0=(lambda-1)*(1,0,1).

Therefore exactly

    x=(lambda+1,-2,lambda+1)/(lambda^2+2lambda-1).

Its middle coordinate is negative. Any argument that treats the
adaptive optimizer as nonnegative, takes absolute values while
retaining its variational identity, or turns every Boolean row
pairing into a favorable contribution is invalid. This refutes
that shortcut, not the desired norm gap or original P2.

## 7. Global review and precise stop/pivot criterion

There were two materially distinct tests of the current matrix
proposal. The adaptive two-vector reduction has an explicit
Boolean relaxation counterfamily; the full operator inequality
reduces exactly to the generic Schur cap. The actual low-M signed
example additionally excludes a positivity shortcut for x.

Preserve the exact C^-1 representation as a way of certifying
the full scalar norm. Do NOT count another kernel identity,
congruence, scalar trace, cyclic allpass projection or selected
Schur-vector test as a new route or a proof of a Boolean gap.
The previous finite closures already have actual-lowM Boolean
falsifiers; Section3 addresses the further two-vector relaxation.

The uniform leverage target must remain correctly quantified:

    1+ell=4n*g/(1+g),  1+ell>=eta*n.

It is the existing sufficient norm-gap/flatness programme, not
a newly discovered equivalent or a completeness theorem for a
finite witness space. Every singleton has ell0, so dropping1
without a stated large-n restriction is false.

No new Boolean inequality advancing that target was obtained
from the two proposed tests. A continuation on this lane needs
an actual unit-amplitude interaction beyond(4), with a precise
gain and adversarial falsifier; otherwise the next cycle should
change mechanism to unrestricted signed Rayleigh or the independent
all-circle construction track. This is a global pivot requirement,
not a claim that the full research goal or all remaining routes
are blocked. No further projection/Schur-vector control sweep is
justified by this audit, and no new experiment is authorized here.

Status: exact paper scope results and falsifiers, no universal
exponent improvement, no Boolean norm-gap proof, no full Chowla
resolution, and no advisor computation or resource operation.
