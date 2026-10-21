# Collective-energy symmetry audit and conditional phase transfer

2026-10-21. Lead checkpoint of complete derivations independently checked
by the existing internal PhD Advisor in this session. The lead prepared
this file from those checked derivations when the user requested commit
and push. Further unfinished derivations are not asserted here. No new
computation, GPU deployment, spending, external review or kernel checking.
Full unrestricted Chowla remains OPEN and the goal ACTIVE.

All integrals are normalized. Write F=sum_(a in A) z^a, n=|A|,
X=max A, D=2Re F, K=-min D=2M. In the low-M branch M<=sqrt(n), set
lambda=2sqrt(n), W=lambda+F, G=integral |W|-lambda.

## 1. Separated dilation is an exact countercontrol to a naive energy inference

Take an integer L>4X, A'=L*A, F'=F(z^L), and H=F'-F. The sets are
disjoint, both have n elements, and s=||H||_2^2=2n. Change of variables
on the circle gives EXACTLY

    M(A')=M(A), G_lambda(F')=G_lambda(F).

Put E4=||F||_4^4. Orthogonality and frequency separation give

    ||HF||_2^2=||HF'||_2^2=E4+n^2,
    ||H||_4^4=2E4+4n^2.

For example HF=F'F-F^2. Its two squared norms are n^2 and E4;
the cross term has no constant coefficient because the nonzero
frequencies from F' exceed every relevant low-frequency combination.
The other identities follow by the same expansion. L>4X is a safe
common separation condition; no asymptotic equidistribution is used.

Boolean additive energy has the elementary lower bound E4>=2n^2-n:
ordered pairs with the same unordered multiset already contribute that
many solutions to a+b=c+d. Consequently

    ||HF||_2^2/(n*s)>=3/2-1/(2n)>1 for n>1,
    ||H||_4^4/s^2=1+E4/(2n^2).

Thus EVERY nontrivial separated dilation automatically violates the
mixed-energy<=n*s hypothesis of the preceding collective-move lemma,
despite being an exact isometry of both M and G. The conditional lemma
remains correct. Its exceptional-energy branch ALONE is not evidence
of new inverse structure, low G, or a negative dip. A putative bridge
must handle this symmetry and retain the linked phase information.

## 2. Exact normalized phase-Hessian transfer to a Rayleigh witness

Let H be any nonzero analytic polynomial with real coefficients and
zero constant term. Since Re W>=sqrt(n)>0 throughout the disk, put

    R=H/W, q=Im R, Q_R=integral q^2,
    C_F(H)=integral |W| q^2.

R is analytic on a neighborhood of the closed disk, has zero constant,
and has real Taylor coefficients. Thus q is real, odd, mean zero and

    Q_R=(1/2)integral |H|^2/|W|^2>0.

Differentiating the circle integral shows that the ACTUAL Hessian of G
in direction H is exactly C_F(H). The energy identity is

    integral D q^2
      =2C_F(H)-2lambda*Q_R
         -2integral (|W|-Re W)q^2
      <=2C_F(H)-2lambda*Q_R.

Therefore the CONDITIONAL estimate

    C_F(H)/Q_R<=lambda-eta*sqrt(n), eta>0,

would yield integral Dq^2<=-2eta*sqrt(n)*Q_R and hence
K>=2eta*sqrt(n), or M>=eta*sqrt(n). This is a valid direct negative-
Rayleigh implication and does not assume L1 flatness.

No universal H achieving that estimate is constructed here. Small
curvature relative to ||H||_2^2 does not suffice: Q_R may also be tiny
because division by W suppresses directions amplified at a positive
front. Dropping this denominator would be an invalid inference.
The modulus ratio is a sufficient test, not an established equivalence
with Chowla. The nonnegative deficit term in the exact identity can
also matter; no universal lower bound on it is established.

R generally has infinitely many Taylor coefficients. A strict negative
Rayleigh inequality can be approximated by finite odd trigonometric
polynomials because R is analytic beyond the circle and D is bounded.
An actual finite candidate must still have its norm and energy checked
exactly or by rigorous enclosures. No finite extraction or GPU test of
a new candidate is claimed in this checkpoint.

## 3. Decision

The previous turn's collective-energy bounds remain proved, but a raw
failure of their mixed-energy hypothesis is not a discriminating new
structural result. Stop interpreting that failure as a sign certificate.
Retain the exact normalized phase transfer and the FULL real Rayleigh
operator, including constants and both parity sectors. The open step is
to exploit actual Boolean phase correlations or construct a genuine
all-circle counterfamily; neither has been obtained here.

The user requested commit and push during this derivation. This file
preserves only complete checked statements. All prior CPU jobs are
terminal; there is no new worker or spending to clean up.
