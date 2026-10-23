# A two-direction sign condition would suffice for Chowla

2026-10-23. Paper derivation independently checked in Section8 of the
[advisor audit](advisor_S0_boolean_2026-10-23.md).
No new computation or VM operation. All integrals use probability
Haar measure. This is a sufficient-condition reduction, not a proof
of the proposed sign condition or of Chowla.

## 1. The weaker target P2

For every nonempty Boolean A with actual M(A)<=sqrt(n), lambda=2sqrt(n),
put b_A=Im F_A and q_A=Im(1/(lambda+F_A)). Conjectural P2 says:

    Some nonzero real linear combination alpha*b_A+beta*q_A
    has <2f_A(alpha*b_A+beta*q_A)²><=0.

S0 implies P2 by choosing alpha=0. P2 permits an adaptive combination;
it neither asserts the S0 prescribed direction works nor requires a
uniform negative margin. The two functions are linearly independent:
an imaginary-part dependence would make p-cF real analytic, hence
constant, contradicting (lambda+F)p=1 for nonconstant F.

Let t_A=#ordered(a,b,c) in A³ with a+b=c, and define

    C2_A=<F_A²,p_A>, H_A=<2f_A q_A²>.

These pairings are real because all analytic coefficients are real.
The exact D-energy matrix in the basis{b_A,q_A} is

    [[t_A/2, C2_A/2], [C2_A/2,H_A]].

Indeed 2f_A*Im F_A=Im(F_A²), giving the cross entry by analytic
orthogonality. If t_A=0, a nonpositive direction already exists.
For t_A>0, P2 is precisely the determinant condition

    2*t_A*H_A<=C2_A².

It is a coupled inequality, weaker than H_A<=0. The finite coefficient
C2_A=sum_(a,b in A)[z^(a+b)]p_A is determined through degree2maxA.
H_A still needs the full reciprocal norm. A positivity argument for
the two separate remainder terms is not being assumed.

## 2. Conditional amplification makes the entire plane positive

Suppose a Boolean V has cardinality N>=2^44, actual M(V)<=sqrt(N)/2,
and g_V(2sqrt N)<=2^-104. Use exactly the checked padding construction
from [the tensor note](cstar_R0_tensor_2026-10-23.md):

    k=floor(sqrt(N)/2^20), U=positive differences of{1,9,...,9^(k-1)},
    N'=N+k(k-1)/2, lambda=2sqrt(N'), L=2^16*N'*9^k,
    A=U union L*V.

A is actual-lowM Boolean. Its reciprocal energy satisfies

    H_qq>k³/(192lambda^4)>2^-77/sqrt(N).

The first inequality follows from the existing torus lower bound
delta=k³/(96lambda^4) and transfer error/delta<=33792/(65536k)<1/2.
The second uses k>=sqrt(N)/2^21, N'<2N and lambda^4<64N².

Let epsilon=2^-50. From F_V=zeta_V*(lambda0+F_V), Cauchy gives

    L_V=||f_V||1<=sqrt(5g_V*N)<epsilon*sqrt(N).

Since ||f_V||2²=N/2 and M(V)<=sqrt(N)/2,

    <(f_V)_-²><=epsilon*N/4,
    <(f_V)_+²>>=N/4.

Cauchy applied to (f_V)_+ yields

    <(f_V)_+³>>=N²/(8L_V),
    <(f_V)_-³><=epsilon*N^(3/2)/8,
    <f_V³>>=N^(3/2)/(16epsilon).

Thus t_V=(4/3)<f_V³>>=N^(3/2)/(12epsilon). Since L>2maxU,
all mixed additive triples in A are excluded: two low terms cannot
reach the high block, and one low plus one high cannot equal a high
multiple of L. Hence t_A=t_U+t_V exactly and

    H_bb=t_A/2>=N^(3/2)/(24epsilon)>2^45*N^(3/2).

The off-diagonal entry has a direct signed bound. With b=Im F_A,

    J_A=<2f_A*b*q_A>=-2< f_A*b²/|lambda+F_A|²>,
    |J_A|<=2||f_A||1<=2(k+L_V)<2^-18*sqrt(N).

Here b²<=|lambda+F_A|² and ||f_U||1<=||U||2<=k. Consequently

    H_bb*H_qq>2^-32*N,  J_A²<2^-36*N.

Both diagonal entries are positive and the determinant is strictly
positive. Every nonzero vector in this two-direction plane therefore
has positive energy. A thus violates P2, not just the prescribed S0 line.
No Boolean V with the weak-gap premise has been constructed.

## 3. Consequence and limitations

If P2 holds for every admissible Boolean support, no such V can exist.
For smaller N the elementary g_V>=1/(sqrt(N)+2)² already exceeds
2^-104. Thus universal P2 forces g_V>=2^-104 on M(V)<=sqrt(N)/2.
The existing norm-gap/L1 identity and ||f||1<=2M imply, conservatively,

    P2 implies M(A)>=2^-107*sqrt(|A|) for every Boolean A.

The complementary M>sqrt(n)/2 branch is immediate. This is a
conditional paper theorem. No proof of P2, no converse from Chowla,
and no new universal bound without that hypothesis is claimed.

The earlier coefficientwise remainder shortcuts have both failed:
<F,h²> may be negative at actual lowM, while the norm term alone cannot
pay high additive-triple counts. P2 retains the signed interaction
and permits an optimized mixture instead of discarding either term.

The advisor also checks a weighted counterfamily: a Fejer pad with
N>=2^424 makes this same entire plane positive at occupied-count
calibration, after replacing the Boolean variance by its actual
weighted value. Thus positivity and a coefficient cap still do not
prove P2. That counterfamily is not Boolean and does not refute P2.
The exact remaining task is the coupled Boolean determinant inequality,
not an additional successful-control sweep.
