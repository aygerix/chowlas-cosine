# Remainder identity, two failed component bounds, and coupled sign

2026-10-23. Paper derivation and exact Boolean counterchecks;
[independent internal audit](advisor_S0_boolean_2026-10-23.md).
No new computation, VM action or external review. Chowla is unresolved.

## Exact remainder identity

For Boolean F=F_A, n=|A|, actual M<=sqrt(n), lambda=2sqrt(n), define

    p=1/(lambda+F), h=F²/[lambda²(lambda+F)],
    r=||h||2², c=<F,h²>, t=<F,F²>=#ordered a+b=c in A.

The exact identities p=1/lambda-F/lambda²+h and
(lambda+F)h=F²/lambda² give

    H0=<2f(Im p)²>=t/(2lambda^4)-lambda*r-c/2.

One verification: expand ||p-1/lambda||² and <F,p²> in h, insert
H0=-lambda||p-1/lambda||²-<F,p²>/2, then use
<F,h>/lambda+<F,Fh>/lambda²=t/lambda^4. This uses no smallness
assumption on |F|/lambda and drops no phase term.

The desired S0 sign is a coupled inequality involving r and c. Merely
rewriting it this way is not a proof or a new Boolean estimate.

## The selected Hankel correction need not be nonnegative

Take A={1,5,6}, the distinct positive differences of{0,1,6}. The
difference-square identity gives actual M(A)<=3/2<sqrt(3). At
lambda=2sqrt(3), h²=F^4p²/lambda^4 has selected coefficients

    [z]h²=0, [z^5]h²=-2/lambda^7, [z^6]h²=3/lambda^8.

Below degree7 the only nonzero coefficient of F^4 is[z^4]=1;
[z]p²=-2/lambda³ and[z²]p²=3/lambda^4. Therefore

    c=(3-2lambda)/lambda^8<0.

This is an actual-lowM Boolean counterexample to the shortcut c>=0.
It is not a counterexample to S0 or Chowla. The combined norm term
can still compensate for a negative c.

## The norm term alone cannot pay the additive-triple term

LowM makes zeta=F/(lambda+F) Schur, so h=F*zeta/lambda² and

    lambda*r<=n/lambda³.

The proposed component bound t/(2lambda^4)<=lambda*r would thus
force t<=2n lambda=4n^(3/2). Existing dense Sidon-difference controls
contradict this inside actual lowM. For completeness, their elementary
positive-front calculation is enough: on the Singer-difference family
with k generators, n=k(k-1)/2, maxA<=2n, and M<=k/2<=sqrt(n).
For |x|<=1/(4n), f>=n/2. Hence

    <f³>>=n²/(32pi)-n^(3/2)/2,
    t=(4/3)<f³>>=n²/(24pi)-(2/3)n^(3/2).

Thus t/n^(3/2) tends to infinity along that already-used family.
The family is not being pursued as another construction exclusion;
it falsifies an explicitly proposed arbitrary-support component bound.
Positive c is indispensable in this high-triple branch.

## Genuine small-case boundary and the mathematical pivot

The valid general bound |c|<=n*r gives
lambda*r+c/2>=(lambda-n/2)r. Thus for sum-free supports (t=0),
S0 holds when lambda>=n/2. At the fixed calibration, every sum-free
test with n<=16 is automatic. Do not enlarge that control sweep.

Both component shortcuts fail. The signed interaction, not its separate
pieces, must be retained. The next prescribed-witness target is the
weaker adaptive plane P2 from [the two-direction reduction](cstar_two_direction_sign_2026-10-23.md).
In the basis{Im F,Im p}, its exact energy matrix is

    [[t/2,C2/2],[C2/2,H0]], C2=<F²,p>.

For t>0, a nonpositive direction exists exactly when
2tH0<=C2². For t=0 such a direction already exists. This joint
determinant target allows an optimized mixture and avoids assuming
either of the disproved component inequalities. Its universal Boolean
truth remains unproved. The amplification theorem shows that a proof
of this qualitative plane condition would suffice for full Chowla.

Global decision: stop termwise sign/norm proofs and successful-control
enlargement; retain the coupled Boolean determinant as a specific next
target. Generic nonnegative bounded coefficients are insufficient by
the explicit weighted plane counterfamily. If the coupled approach
cannot use exact unit amplitudes, return to unrestricted signed
Rayleigh spaces rather than rename the same relaxed gap.
