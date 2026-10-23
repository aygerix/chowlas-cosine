# Joint factor budgets under dilation

2026-10-23. Current research note, not a manuscript. Paper proofs,
independently reviewed by the sole internal advisor in
[the joint-factor audit](advisor_joint_factor_2026-10-23.md).
No new universal exponent, stable-factor existence theorem, finite
minimum record, kernel check or novelty claim. A bounded exact
symbolic/rational check on Dirichlet is terminal/PASS. No GPU
deployment or VM lifecycle action was required for this cycle.

## Target and decision

For every Boolean A, put n=|A| and
p(z)=lambda+(1/2)sum_A(z^a+z^(-a)), lambda>=M(A).
A real factor Q with |Q|^2=p is oriented by Q(1)=S=sqrt(lambda+n)>0.
The signed-centroid theorem gives a root bound if, at lambda=M(A),

    qmax<=C, Nminus/S<=1/8, Vminus<=Vintrinsic/6,
    Vintrinsic=sum_A a^2/(2S).

It is NOT proved that a suitable branch exists. Dilation preserves
M,n and any already stable branch, but can introduce extra signed
branches. This cycle treats that extra freedom exactly, proves a
necessary JOINT mass/variance budget, and excludes a bounded-kernel
flattening shortcut. It does not turn necessary conditions into a
selection algorithm.

## 1. Exact polyphase constraints and concentration

Let Q_L be any real factor of p(z^L). After a monomial translation,
write Q_L(z)=sum_(r=0)^(L-1) z^r*C_r(z^L). For w on the circle,

    sum_r |C_r(w)|^2=p(w),                         (1)

and for 1<=h<L the coefficient of the h-th residue is zero:

    sum_(s=0)^(L-1-h) C_(s+h)(w)*conj(C_s(w))
       +w^(-1)*sum_(s=L-h)^(L-1)
            C_(s+h-L)(w)*conj(C_s(w))=0.           (2)

Both are full Laurent-polynomial identities. At Lth roots of unity
|Q_L|=S. If s_r=C_r(1), Fourier orthogonality implies

    sum s_r=S, sum s_r^2=S^2.

Set N=sum_j(-q_j)_+, Ns=sum_r(-s_r)_+<=N, m=max_r s_r>0.
The positive residue sums total S+Ns. Consequently

    S^2<=m(S+Ns)+Ns^2, hence m>=S-Ns.

Separating the largest positive residue from the other positive
ones also gives S^2<=m^2+(S+Ns-m)^2+Ns^2. If e=Ns/S<=1/8,
the preceding linear bound selects its upper quadratic root:

    m/S >= (1+e+sqrt(1-2e-3e^2))/2
         >= (9+3sqrt(5))/16.                     (3)

The displayed function decreases on [0,1/8]. Thus small negative
mass forces nearly all SIGNED mass into one residue. Under the
stronger TOTAL bound N<=S/8, the absolute coefficient mass outside
it is bounded by

    S-m+2(N-N_dominant)
      <= ((11-3sqrt(5))/16)*S.                    (4)

At N=0 exactly one residue is occupied, since all coefficients
are nonnegative. Every nonnegative factor of p(z^L) is therefore
z^r*C(z^L), |C|^2=p. No extra nonnegative branch appears on dilation.
At N>0, cancellations within a residue prevent this scalar reduction:
the dominant C_r is one term of the sum of squares (1).

## 2. Doubled sets: the zero-sum channel has a forced variance

For L=2 write Q_2(z)=E(z^2)+z*O(z^2). Equation (2) is

    w*O(w)*E(w^(-1))+E(w)*O(w^(-1))=0.            (5)

In the actual Boolean doubled problem there is a stronger fact:
p(z^2)>0 for EVERY real nonzero z, since all its Laurent
coefficients and lambda are nonnegative. After trimming a
monomial, Q_2 has no real roots, has even degree and is positive
on the real line when oriented at1. Thus Q_2(-1)=Q_2(1)=S,
E(0)!=0, E(1)=S and O(1)=0 automatically. The weaker assertion
that one channel sums to S and the other to0 also holds in the
generic setting after a parity shift. Put e1=E'(1), o1=O'(1), and
o2=(w*d/dw)^2 O(1). The t^2 coefficient in (5), at w=exp(t), is

    S*(o2+o1)-2*e1*o1=0.

The signed centroid of Q_2 is mu=2(e1+o1)/S. In its zero-sum
odd channel put B=sum_m(2m+1)*o_m=2o1. Centering does not change B.
Its signed variance is EXACTLY

    Vplus_O-Vminus_O
       =sum_m o_m*(2m+1-mu)^2
       =4(o2+o1)-4mu*o1
       =-8o1^2/S=-2B^2/S.                        (6)

In particular Vminus_total>=2B^2/S. This identity alone does not
bound the negative mass or exclude a nonzero O with B=0.

## 3. Coupling the OUTPUT negative mass to its variance

Let N0 be the negative mass in O. Its positive mass is also N0.
If N0=0, O=0 and B=0. For N0>0, let m0 be its negative centered
first moment. Its positive centered first moment is m0+B.
Cauchy applied to the two nonnegative measures and (6) gives

    Vminus_O >= max(m0^2/N0,
                    (m0+B)^2/N0+2B^2/S).        (7)

For B!=0 and N0<=S/2 the minimum of this maximum occurs at
m0=-B(1/2+N0/S), where the quadratics agree. Therefore

    Vminus_total >= Vminus_O
      >= (B^2/(4N0))*(1+2N0/S)^2.                (8)

For N0>=S/2 the minimum is 2B^2/S, attained in the relaxed
moment problem at m0=-B. At N0=S/2 the two formulas agree.
For B=0 the claimed lower bound is0 and asserts no rigidity.
These are inequalities, not an assertion that polynomial factors
attain the relaxed moment extrema.

If the FULL factor has Nminus<=S/8, then N0<=S/8. The function
1/(4N0)+1/S+N0/S^2 decreases up to S/2, so (8) yields

    Vminus_total >= 25B^2/(8S)=25o1^2/(2S).       (9)

For p(z^2), Vintrinsic=2*sum_A a^2/S. Both stable signed budgets
can therefore hold only if

    O'(1)^2 <= (2/75)*sum_A a^2.                 (10)

This improves the mass-free necessary bound sum_A a^2/24.
The improvement uses the ACTUAL OUTPUT negative mass, not the
negative mass of a convolution kernel.

## 4. A necessary budget on a batch of root reflections

Define mu_+=Q_2'(1)/Q_2(1), mu_-=(-1)Q_2'(-1)/Q_2(-1),
and delta=mu_+-mu_-. After the parity convention above,
delta=4o1/S=2B/S. Multiplying by a monomial changes both mu's
equally, so delta is independent of the translation convention.
Equations (9)--(10) give

    Vminus_total >= (25/32)*S*delta^2,
    delta^2 <= 32*sum_A a^2/(75*S^2)             (11)

as a NECESSARY condition for both signed budgets. The first
inequality in (11) assumes the mass budget Nminus<=S/8.

Logarithmic derivatives add, so a sequence of root reflections
has a net delta equal to the initial delta plus its increments.
For an outside-to-inside conjugate pair z^2-2uz+v, v>1,u^2<v,
the increment is

    8u(v-1)/((v+1)^2-4u^2).                     (12)

Reverse moves negate it. The shifts at +1 and -1 are respectively
2(v-1)/(v+1-2u) and 2(v-1)/(v+1+2u); subtract them.
ONLY conjugate-pair moves occur for p(z^2): both positive and
negative real roots are excluded by the real-line positivity
proved above. For general undoubled p, positive real roots are
excluded but negative ones can occur. The algebraic increment
for a negative real root is -4t/(t^2-1), with a parity switch;
it is NOT an admissible move in this doubled Boolean problem.

A lifted base factor Q(z^2) starts at delta=0. Equation (11)
then bounds the NET sum of its selected reflection increments.
Opposite-sign contributions can cancel. Neither their squared
costs nor individual negative masses may simply be added.
Satisfying (11) still does not control qmax or all negative mass.

## 5. Why bounded-kernel flattening does not supply the rule

Suppose a NONNEGATIVE Boolean factor has an endpoint q0=a=qmax.
All its other coefficients are <=1/(2a), by nonnegative
autocorrelation and the exact off-zero correlation cap1/2.
Let L=sum_(j>=0) l_j*z^j be a real analytic allpass filter,
absolutely summable, L(1)=1, with LQ the chosen polynomial factor.
Write T=sum|l_j|. Parseval gives sum l_j^2=1, hence
max|l_j|>=1/T. At an index attaining this maximum, the remaining
coefficients of Q contribute in magnitude at most T/(2a). Thus

    qmax(LQ)>=a/T-T/(2a).

To reach qmax(LQ)<=C one necessarily needs

    T >= (sqrt(C^2+2)-C)*a.                       (13)

Growing endpoint amplitude cannot be flattened by uniformly
bounded-l1 allpass kernels. A large kernel negative mass can
still cancel against the rest of Q and leave small OUTPUT
negative mass. Equation (13) is a property of that transform,
not a dilation-invariant inverse obstruction. It does not refute
the stable-factor target.

## 6. What the new moment budget cannot see

Equation (5) implies the full, local analytic identity

    H(t)=exp(t/2)*O(exp(t))/E(exp(t)) is ODD,

where E(1)=S ensures a neighborhood without denominator zeros.
It does not force its first Taylor coefficient to be nonzero.
For every integer m>=0, E(w)=w^(m+1), O(w)=(w-1)^(2m+1)
satisfies (5), and H(t)=(2sinh(t/2))^(2m+1). Thus arbitrarily
many initial Taylor coefficients can vanish with O nonzero.
At m=1, O'(1)=0 and Q_2=z^4+z(z^2-1)^3 has
|Q_2|^2=1+(2-w-w^(-1))^3. These are GENERIC factor examples;
their Fourier coefficients have signs and are not Boolean A's.
They disprove treating phase jets ALONE as complete control in
the generic cross-phase class. They do NOT disprove a Boolean
existence statement or a finite-jet estimate that additionally
uses the exact Boolean coefficient equations. A common factor
w+1 can make the generic p vanish on the circle without changing
H, so generic boundary optimality alone does not remove the issue.

One extra n5 branch can be written exactly by splitting and
reflecting one pair in R(z^2); the advisor gives its channels and
forced mass/variance costs. We deliberately did not certify more
metrics on it: the known signed base factor already lifts with
all budgets, so either finite outcome would leave the existence
target unchanged. No support sweep, arbitrary constant change
or GPU experiment is justified by that example.

A stronger, exact WEIGHTED countermodel removes both the signed-
Fourier and nonoptimality loopholes. Set

    E0=(1+w)^4, O0=(w-1)^3, K0=1+w^9,
    Q2(z)=K0(z^2)*(E0(z^2)+z*O0(z^2))/sqrt(180).

Then |Q2(z)|^2=p0(z^2), where p0(w)=1+sum_(a=1)^13 c_a*cos(ax)
on w=exp(ix), and the cosine weights are exactly

    (c1,...,c13)=(82,68,14,2,1,7,34,41,90,41,34,7,1)/90.

All are positive and <=1. The common factor K0 vanishes at
w=exp(i*pi/9), so the weighted minimum is EXACTLY-1 on the
entire circle, not a sampled minimum. Direct integer convolution
and exact rational geometry give

    qmax^2=1/5, Nminus/S=1/4, alpha=21/127,
    O'(1)=0, delta=0.

Thus this optimal prescribed factor has small qmax and zero first
phase imbalance but fails BOTH signed budgets, even with positive
Fourier coefficients capped at1/2. This is not a Boolean support,
not a failure of EVERY branch, and not a Chowla counterexample.
It rules out that particular phase-only relaxation of the selection
problem. [Exact artifact](../experiments/joint_factor_2026-10-23/identities.json)
and [reproducible verifier](../../src/joint_factor_identities.py).

## 7. Removing the common factor gives the full polynomial norm

This uses all of (5), not a Taylor truncation. Let D=maxA and
trim Q_2 to degree2D with nonzero constant. Then degE=D and
degO<=D-1. If O=0, take K=E,U=1,V=0 below. Otherwise let
K be a real polynomial gcd of E and O and write E=K*U,O=K*V,
with coprime U,V. E(0)!=0 implies K(0),U(0)!=0. Set d=degU.

In the real Laurent ring, (5) becomes
w*V(w)*U(w^-1)+U(w)*V(w^-1)=0,
where the star means substitution w->w^(-1). Coprimality gives
U divides U*. Their equal exponent spans make the quotient a
Laurent unit c*w^k. Applying star twice gives c^2=1; U(1)!=0
forces c=1. The support endpoints give k=-d. Substitution into
the cross-phase relation then gives

    U*=w^(-d)*U, V*=-w^(1-d)*V.                  (14)

Thus U is reciprocal, V is anti-reciprocal with support within
[0,d-1]. If d were odd, (14) would force BOTH U(-1)=0 and
V(-1)=0, contradicting coprimality. Hence nonzero V requires
even d>=2. The reduced factor U(z^2)+zV(z^2) has degree2d and
its coefficient reversal equals its value at -z.

The entire spectrum satisfies

    p(w)=K(w)K(w^-1)*w^-d*(U(w)^2-w*V(w)^2).     (15)

The reduced factor |U|^2+|V|^2 is STRICTLY positive on the unit
circle, since otherwise coprime U and V would share a root.
Therefore ALL circle zeros at lambda=M are carried by K.
Optimality alone does not control the nontrivial mixed factor.

Writing k=degK, D=k+d and Krev=w^k*K(w^-1), (15) gives the
exact Boolean coefficient problem

    2lambda*w^D+sum_(a in A)(w^(D+a)+w^(D-a))
      =2*K(w)*Krev(w)*(U(w)^2-w*V(w)^2).          (16)

Every off-center coefficient on the LEFT is exactly0 or1.
Discarding those equations loses the essential Boolean content.
The norm reduction is exact algebra/root-orbit bookkeeping;
it supplies neither an amplitude bound nor a new construction.

There is a useful equivalent real-polynomial form. For d=2m>=2,
write U=w^m*u(T), V=(w-1)w^(m-1)*v(T),
T=(w+w^-1)/2. Then the mixed norm is

    w^-d*(U^2-wV^2)=u(T)^2+2(1-T)v(T)^2.        (17)

It is strictly positive for EVERY real T. For T<1 the two
squares cannot vanish together, by coprimality; at1, U(1)!=0.
For T>1 choose w>0: p(w)>0, and K has no positive real root,
so K(w)K(1/w)>0 in (15). Consequently all real roots of the
Chebyshev polynomial lambda+sum_A T_a(T), including ones outside
[-1,1], belong to the inherited common factor. This still leaves
the exact coefficient constraint (16) as the unresolved ingredient.

## 8. Global decision and first next derivation

Previous turn32f83bc was progress. This cycle is also progress:
it supplies the exact dilation constraints, the stronger coupled
budget (8)--(11), the full norm reduction (14)--(16), and the scoped
obstruction (13), with independent paper review. It does not
close the universal gap.

Stop endpoint balancing as a global-max descent, bounded-kernel
flattening as a universal mechanism, raw root-radius sums as
intrinsic statistics, and successful n5 controls as evidence of
existential selection. Preserve the signed centroid theorem.

First next derivation: use the FULL cross-phase identity (5) and
the exact Boolean coefficient equations

    R_E(d)+R_O(d)=(1/2)*1_A(d), d!=0,
    R_E(0)+R_O(0)=lambda,

to control or exploit correlated cancellation with a nonzero
zero-sum channel, explicitly allowing O'(1)=0. Phase jets or
(11) ALONE give no generic completeness. The first algebraic
reduction has been done: (16) gives the full coprime polynomial
norm and isolates all boundary zeros in K. Attempt a coefficient
estimate from its EXACT0/1 left side, or an actual Boolean
signed-correction construction; do not infer it from optimality
of K or positivity of the reduced factor alone.

Retain three distinct lines: this full signed autocorrelation
problem; the existing unrestricted Rayleigh/all-scale Boolean
susceptibility route; and a genuine construction with signed
correction and an all-circle upper bound. No new valid Epoch
solution or infinite vanishing-ratio family is recorded.
