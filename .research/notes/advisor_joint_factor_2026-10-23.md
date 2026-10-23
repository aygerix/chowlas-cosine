# Joint factor selection: dilation, polyphase concentration, and a forced variance cost

2026-10-23. Sole internal AI advisor. Paper derivations and read-only
project review; no computation, VM action, GPU, new agent or outreach.
Only this assigned note is edited. Shared Dirichlet is left on.

## 1. Target and actual result of this attempt

The sufficient factor target is: for every Boolean A with actual
M(A)<=sqrt(n), choose a REAL optimal factor

    p(z)=M(A)+(1/2)*sum_(a in A)(z^a+z^(-a))=|Q(z)|^2

with qmax<=C absolute, Nminus/S<=1/8 and alpha<=1/8. It remains
unproved and unfalsified. These are sufficient, not proved necessary,
conditions for Chowla. An optimal real factor is not required to have
nonnegative coefficients.

Concrete results below: exact quantitative concentration under dilation;
an exact signed-variance identity and necessary budget for the two
polyphase channels; the parent's explicit nondilated branch construction;
and a necessary allpass-kernel norm for flattening a large positive
endpoint. None supplies an unrestricted stable-factor selection theorem.

## 2. Dilation allows extra signed branches: exact identities

Let p be as above (the algebra also holds at lambda>=M(A)), and let
Q_L be ANY real polynomial factor of p(z^L), after a monomial shift.
Orient Q_L(1)=S=sqrt(lambda+n)>0. Write its polyphase decomposition

    Q_L(z)=sum_(r=0)^(L-1) z^r*C_r(z^L),
    s_r=C_r(1)=sum_(j congruent r modL)q_j.

For w on the unit circle, averaging the L rotations of z gives

    sum_r |C_r(w)|^2=p(w).                         (1)

The off-residue conditions, for1<=h<L, are exactly

    sum_(s=0)^(L-1-h) C_(s+h)(w)*conj(C_s(w))
      +w^(-1)*sum_(s=L-h)^(L-1)
             C_(s+h-L)(w)*conj(C_s(w))=0.          (2)

These are full Laurent-polynomial identities, not merely constraints at1.
At the Lth roots of unity, |Q_L|=S. Finite Fourier orthogonality gives

    sum_r s_r=S, sum_r s_r^2=S^2.                 (3)

Let N=sum_j(-q_j)_+, N_s=sum_r(-s_r)_+<=N, and m=max_r s_r>0.
Since the positive residue sums total S+N_s,

    S^2<=m*(S+N_s)+N_s^2,
    m>=S-N_s>=S-N.                               (4)

Thus low negative mass forces concentration in ONE residue, but it
does not yet make its C_r a scalar factor of p.

The concentration is stronger than (4). Put e=N_s/S<=1/8. Separating
the largest positive residue sum from all the others gives

    S^2<=m^2+(S+N_s-m)^2+N_s^2.

Bound (4) selects the upper root of this quadratic inequality:

    m/S >= [1+e+sqrt(1-2e-3e^2)]/2
         >=(9+3sqrt(5))/16.                       (5)

The first lower bound decreases on0<=e<=1/8. Its final value is
about.9817627, so the stable mass budget forces at least98.17% of
the SIGNED total coefficient mass into one residue. If N_r is the
negative coefficient mass in this residue, the absolute coefficient
mass outside it is exactly S-m+2*(N-N_r). Under the TOTAL coefficient
mass budget N<=S/8, rather than merely N_s<=S/8, it is at most

    [(11-3sqrt(5))/16]*S,                         (6)

about.2682373*S. Cancellation within a residue is why a concentration
statement about s_r is not the same as deleting all other coefficients.

When N=0, (3) forces exactly one nonzero residue sum, and coefficient
nonnegativity forces every other C_r to vanish identically. Therefore
EVERY nonnegative factor of p(z^L) is z^r*C(z^L), with |C|^2=p,
up to an irrelevant monomial translation. Dilation creates no new
nonnegative spectral branches. It CAN create new signed branches,
which (1)--(6) do not exclude.

Existence of a stable signed factor is itself preserved by dilation:
Q(z^L) has the same qmax and N/S, while its positive/negative
variances both scale by L^2. Thus dilation of a set ALREADY having
a stable factor cannot falsify the existence target. In particular
the known signed n5 factor lifts with all three budgets intact.

## 3. Two channels: an exact forced negative-variance cost

For L=2 write

    Q_2(z)=E(z^2)+z*O(z^2).

Equations (1)--(2) specialize to

    |E(w)|^2+|O(w)|^2=p(w),
    w*O(w)*E(w^(-1))+E(w)*O(w^(-1))=0.            (7)

At w=1, one of E(1),O(1) is0 and the other is S. A monomial
translation exchanges parities, so assume E(1)=S,O(1)=0. The
zero-sum odd channel has negative coefficient mass exactly
||O||_1/2; no smallness follows automatically.

Let e1=E'(1), o1=O'(1) and o2=(w*d/dw)^2 O(1). Expanding (7)
at w=exp(u) to order u^2 gives

    S*(o2+o1)=2*e1*o1.                            (8)

Indeed the u^2 coefficient is S*(o2+o1)-2*e1*o1. The signed
centroid of the FULL factor is mu=2*(e1+o1)/S. If O(w)=sum o_m*w^m,
the odd coefficients are located at indices2m+1, so

    sum_m o_m*(2m+1-mu)^2
       =4*(o2+o1)-4*mu*o1
       =-8*o1^2/S.                               (9)

This is an exact NONPOSITIVE signed variance, not an absolute
variance estimate. Consequently

    Vminus_total>=Vminus_odd>=8*O'(1)^2/S.         (10)

For the factor of p(z^2), the intrinsic variance is
Vint=2*sum_(a in A)a^2/S. Thus the stable alpha<=1/8 budget
necessarily requires

    O'(1)^2<=sum_(a in A)a^2/24.                  (11)

This is a useful joint phase constraint. A zero-sum odd channel
can be cheap only if its negative variance, including its forced
first-moment cost, fits the budget. It need not vanish identically.
The proof is generic periodic factor geometry; it is not a new
Boolean flatness estimate. Booleanity specifies the intrinsic
right side, but does not supply (11).

There is also a root-selection interpretation. Define
mu_+=Q_2'(1)/Q_2(1) and mu_-=(-1)*Q_2'(-1)/Q_2(-1).
With Q_2(1)=Q_2(-1)=S,

    mu_+-mu_-=4*o1/S,
    Vminus_odd>=S*(mu_+-mu_-)^2/2.                (12)

Logarithmic derivative shifts ADD under a sequence of root
reflections. Thus (12) is a necessary JOINT budget on their
net phase imbalance at1 and-1; individually small costs cannot
be assumed to add favorably. Symmetric flips can cancel this
imbalance, but other negative coefficients still need control.

### 3.1 Coupling the OUTPUT negative mass to its variance

The parent's stronger joint bound checks. Let N_o be the odd
negative coefficient mass. Its positive mass is also N_o because
O(1)=0. Put B=sum_(odd j)j*q_j=2*O'(1), and let m_- be the
negative odd centered first moment about the FULL centroid.
The positive odd centered first moment is m_-+B. Equation(9) is

    Vplus_odd-Vminus_odd=-2*B^2/S.

For N_o>0, the two weighted Cauchy inequalities therefore give

    Vminus_odd>=m_-^2/N_o,
    Vminus_odd>=(m_-+B)^2/N_o+2*B^2/S.

Minimize the maximum of these two quadratics over real m_-.
For N_o<=S/2 their intersection is the minimizer,
m_-=-B*(1/2+N_o/S), giving

    Vminus_odd >= B^2*(1+2N_o/S)^2/(4N_o).        (12a)

For N_o>=S/2, the minimum of that maximum is2B^2/S,
attained at m_-=-B. These are valid lower bounds even when the
formal minimizing moments cannot be realized on the odd lattice.
The formula is symmetric in the sign of B. If B=0 it gives the
trivial zero lower bound. If N_o=0 the entire odd channel is0,
so B=0 and Vminus_odd=0; there is no division-by-zero case.

Under the stable TOTAL mass budget, N_o<=Nminus_total<=S/8.
The expression[1/(4rho)+1+rho] decreases for0<rho<=1/8,
where rho=N_o/S. Thus (12a) strengthens(10) to

    Vminus_total>=25*B^2/(8S)
                   =25*O'(1)^2/(2S).             (12b)

Combining with the stable alpha budget yields the stronger
necessary condition

    O'(1)^2<=2*sum_(a in A)a^2/75.                (12c)

This couples ACTUAL output negative mass and negative variance;
it is not a constraint on an auxiliary kernel norm.

### 3.2 Exact net root-phase increments

Let delta=mu_+-mu_- for an L=2 branch. After arranging the
surviving channel to be even by an irrelevant monomial shift,
delta=4*O'(1)/S. Equations(12b)--(12c) are equivalently

    Vminus_total>=25*S*delta^2/32,
    delta^2<=32*sum_(a in A)a^2/(75*S^2).          (12d)

Starting from Q(z^2), delta=0. Each multiplicative reflection
filter contributes additively to delta via logarithmic derivatives
at1 and-1. For a GENERIC real symbol, a forward outside-to-inside
negative-real reflection at -t, t>1, would contribute

    -4t/(t^2-1).

A conjugate pair z^2-2u*z+v, v>1, contributes

    8u*(v-1)/[(v+1)^2-4u^2].

Reverse flips negate the respective contribution. There is an
important scope correction: for the DOUBLED Boolean symbol,
neither positive NOR negative nonzero real roots are possible.
For real z!=0, Q_2(z)*Q_2(z^(-1))=p(z^2)>0, since z^2>0 and
all Laurent coefficients of p are nonnegative with lambda>0.
After trimming monomial shifts, Q_2 has no real roots at all.
Only conjugate-pair moves are actually admissible in this L=2
problem. The displayed negative-real formula is valid algebra
for general symbols, not an available cancellation move here.
The formal positive-real formula +4t/(t^2-1) is likewise
inadmissible. Positive weighted symbols have the same exclusion.

For a generic symbol, a real-root reflection would have filter
value -1 at z=-1 and switch which parity channel sums to0;
a monomial shift swaps it back without changing delta. In the
canonical doubled Boolean factor, Q_2(-1)=Q_2(1)=S automatically,
as proved in Section8 below. The earlier classification that
listed a negative-real move as admissible was a scope error;
its correction changes no conjugate-pair or budget formula.

The budget concerns the NET SUM of root increments, not the sum
of their squared individual costs. Opposite pair contributions
or reverse flips may cancel. Even delta=0 does not force the
zero-sum channel to vanish or control its higher negative moments,
qmax or total negative mass. The phase filter is necessary and
can reject a branch; passing it does not certify a stable branch.

## 4. The proposed explicit extra n5 branch: algebra and decision

The parent's quartic construction checks. Write the residual cubic
of the already certified n5 factor as

    R(w)=e*(w+t)*(w^2+B*w+C),
    v=sqrt(C)>1, h=sqrt(2v-B)>0.

Its nonreal outside pair gives |B|<2v, so h^2<4v. Then

    R(z^2)=e*(z^2+t)*(z^2+h*z+v)*(z^2-h*z+v).

Reflect just the first quadratic. Their product becomes

    v+h*(v-1)*z+(1+v^2-h^2)*z^2
       -h*(v-1)*z^3+v*z^4.

Let U be the original unit quadratic and K(w)=e*(w+t)*U(w).
The resulting full factor has EXACT channels

    E(w)=[v+(1+v^2-h^2)*w+v*w^2]*K(w),
    O(w)=h*(v-1)*(1-w)*K(w).                      (13)

Put Den=(v+1)^2-h^2. Then S=Den*K(1), and (10) gives the
explicit unavoidable odd negative-variance cost

    O'(1)=-S*h*(v-1)/Den,
    Vminus_odd>=8*S*h^2*(v-1)^2/Den^2.             (14)

If the total stable mass budget is imposed, (12b) strengthens
the coefficient8 on the right of(14) to25/2. This is a condition
on the same net odd first moment, not an additive cost per flip.

The odd negative MASS is also exact:

    Nminus_odd=|h|*(v-1)*||(1-w)*K||_1/2.         (15)

This constructs a genuinely nondilated signed branch and shows
precisely where the cancellation and budget enter. There is no
automatic reduction of this branch to a base scalar factor.

Recommendation: NO additional n5 branch-geometry certificate.
The already proved signed base factor Qref(z^2) is stable. A good
or bad result for (13) therefore cannot falsify the existential
stable-factor target; it would be another finite control. The
paper construction and necessary budget are the current result.
No numerical test of (13) was performed by the advisor.

## 5. A bounded-kernel allpass flattening principle is impossible

One other precise necessary condition distinguishes an actual joint
selection from low-cost filtering. Start with a NONNEGATIVE Boolean
factor, shifted/reflected so q0=a=qmax. All other q_j<=1/(2a).
Let L(z)=sum_(j>=0)l_j*z^j be a real analytic allpass filter with
absolutely summable coefficients, |L|=1 on the circle, L(1)=1.
It may be a finite product of outside-to-inside root reflections;
assume L*Q is the selected polynomial factor. Put T1=sum |l_j|.

Parseval gives sum l_j^2=1, hence max |l_j|>=1/T1. At an index
attaining that maximum, the contribution of all nonendpoint
coefficients of Q is at most T1/(2a). Therefore

    qmax(L*Q)>=a/T1-T1/(2a).                      (16)

If qmax(L*Q)<=C, then necessarily

    T1>=[sqrt(C^2+2)-C]*a.                        (17)

Thus a bounded-l1 allpass kernel cannot flatten an unbounded
positive endpoint. Its negative KERNEL mass is (T1-1)/2 and
must grow in this situation. Its OUTPUT negative coefficient
mass can nevertheless be small through cancellation with the
rest of Q. Inferring the latter budget from the former without
that cancellation analysis would be false.

T1 is a property of this chosen transform, NOT a dilation-
invariant inverse statistic. Extra branches of p(z^L) may use
filters with large T1 and are not excluded by (16)--(17). This
bound rules out a precise low-kernel-norm flattening shortcut,
not the unrestricted stable-factor target.

## 6. Global review and exact remaining question

The relevant existing route entries on tensor/no-carry composition
and separated-block closure were checked before making a new
claim. No new M-preservation theorem for products, no-carry sums
or arbitrary block additions is asserted here. Dilation has been
handled exactly, including its extra signed spectral branches.

There is no Boolean lowM counterfamily to the stable target from
this attempt. There is a useful quantitative polyphase theorem
and a forced variance cost for a joint phase change. The remaining
step must use the FULL constraints(1)--(2) to control cancellation
or select a branch satisfying the mass, variance and maximum
conditions together. Mass concentration at w=1 alone is not that
step; dominant C_r is only one square in (1).

Stop endpoint balancing, bounded-kernel flattening, raw inverse-
root-modulus sums as intrinsic tests, and extra successful n5
branches as research substitutes. A changed next result would
be an arbitrary-support bound on the needed phase cancellation,
or a genuine all-circle construction mechanism. The sufficient
factor class is not asserted complete for Chowla or for signed
negative-Rayleigh certificates. All new results here are paper
proofs, not kernel-checked or externally novelty-reviewed.

## 7. Final independent read-only audit of the parent budget note

I read the full parent note joint_factor_budget_2026-10-23.md after
the preceding derivations. The constants, parity conventions and
quantifiers in its signed-variance, minimax and root-increment proofs
agree with the independently checked formulas here. I sent two
precision requests: its absolute outside-mass bound must explicitly
assume TOTAL N<=S/8, and finite-jet nonrigidity must be distinguished
from a hypothetical estimate using the full Boolean equations. The
same total-mass qualification is made explicit in Section2 above.

The new Section6 blindspot is correct. Divide the full cross-phase
identity by E(w)*E(w^(-1)) near w=1, where E(1)=S>0. It gives

    [O/E](w^(-1))=-w*[O/E](w).

Thus H(t)=exp(t/2)*O(exp(t))/E(exp(t)) is analytic and ODD near0.
Oddness does not force a nonzero first derivative. The proposed
example E=w^2,O=(w-1)^3 satisfies the identity exactly because

    O(w^(-1))=-w^(-3)*O(w),
    w*O(w)*E(w^(-1))=-E(w)*O(w^(-1)).

It has O'(1)=0 and O nonzero. Its even norm sum is

    |Q_2|^2=|E|^2+|O|^2
       =1+(2-w-w^(-1))^3
       =21-15*(w+w^(-1))+6*(w^2+w^(-2))
          -(w^3+w^(-3)).

The signed, unequal Fourier coefficients explicitly violate the
Boolean spectrum; this is NOT an A, not a stable-factor existence
falsifier and not an Epoch construction. Its purpose is to refute
rigidity inferred solely from the first phase moment.

For the generic finite-jet scope, an exact extension is available:
E=w^(m+1), O=(w-1)^(2m+1), for any integer m>=0. The same
cross-phase cancellation holds, and

    H(t)=(2*sinh(t/2))^(2m+1).

This can vanish to arbitrarily high finite order without O=0.
It remains a GENERIC non-Boolean family. Therefore the precise
conclusion is that finitely many jets ALONE do not exhaust the
generic cross-phase identity. It does not refute a Boolean theorem
whose proof additionally exploits all exact coefficients.

The parent's Section7 next derivation retains the correct stronger
data, R_E(d)+R_O(d)=(1/2)*1_A(d), diagonal lambda, and the ENTIRE
cross-phase relation. It explicitly permits O'(1)=0 and does not
claim the net-phase budget complete. That global decision is sound.
The cancelled extra n5 test still could not distinguish existence
because the known stable branch already lifts. No further branch
calibration, VM operation or computation was performed by this audit.

## 8. Full coprime reduction: support, parity, and the Boolean identity

The parent's PID reduction is correct, with the following canonical
normalization resolving its Laurent boundary. Set D=max(A) and trim
a real factor Q_2 of p(z^2) to minimum exponent0. Its degree is2D
and its extreme product is q0*q_(2D)=1/2. For real z!=0,

    Q_2(z)*Q_2(z^(-1))=p(z^2)>0.

Thus Q_2 has no nonzero real zero, and q0!=0 excludes a zero at0.
Oriented by Q_2(1)=S>0, it is positive on the entire real axis.
In particular Q_2(-1)=S, E(1)=S, O(1)=0 and E(0)=q0!=0.
This justifies the real-root admissibility correction in Section3.2.

Take the USUAL real polynomial gcd K of E and O and write

    E=K*U, O=K*V, gcd(U,V)=1.

If O=0, choose U constant and V=0; the reduced degree is0.
Otherwise K(0)!=0 and U(0)!=0, because E(0)!=0. Also K(1)
and U(1) are nonzero because E(1)=S. If k=deg(K), then

    deg(E)=D, d=deg(U)=D-k,
    deg(V)<=d-1.

The leading degree of E follows from q_(2D)!=0, not an assumed
support pattern. Define star by w->w^(-1). After dividing out
K*K*, cross-phase is

    w*V(w)*U(w^(-1))+U(w)*V(w^(-1))=0.

In the Laurent PID, coprimality implies U divides star(U).
Applying star gives the reverse divisibility. Hence U*=c*w^j*U
for a real nonzero c. Involution gives c^2=1, and U(1)!=0 gives c=1.
The endpoint exponents, with valuation(U)=0 and degree d,
force j=-d. Substituting back gives

    U*=w^(-d)*U,
    V*=-w^(1-d)*V.                               (18)

If V has endpoint exponents l,u, (18) gives l+u=d-1. In a
general Laurent normalization this does NOT force l>=0. Here
the canonical ordinary gcd makes V polynomial, so l>=0 and
u<=d-1, as already obtained from degrees. One must not apply
this polynomial conclusion to an arbitrary monomial choice.

For V!=0, d is EVEN and at least2. If d were odd, (18) at w=-1
would give both U(-1)=0 and V(-1)=0, contradicting coprimality.
The exact reduced polynomial is

    Qred(z)=U(z^2)+z*V(z^2),
    deg(Qred)=2d, Qred_rev(z)=Qred(-z).            (19)

Its degree and reversal sign depend on the stated normalization.
The unrestricted Laurent version is centered at exponent d;
an arbitrary monomial shift can change the ordinary reversal sign.

On the circle, coprimality gives STRICT positivity of

    p_mix=|U|^2+|V|^2=w^(-d)*(U^2-w*V^2),

since U and V have no common complex zero. Consequently every
unit-circle zero of p is carried by K, and lambda=M(A) is equivalent
to K having a unit-circle zero. K can also have nonunit zeros;
optimality does not say that all its roots lie on the boundary.

The full coefficient identity, without dropping the Boolean data, is

    P_A(w)=2lambda*w^D+sum_(a in A)(w^(D+a)+w^(D-a))
          =2*K(w)*K_rev(w)*(U(w)^2-w*V(w)^2).     (20)

Here D=k+d and K*=w^(-k)K_rev, which check the factor2 and all
exponents. Off center the coefficients on the left are EXACTLY0
or1, including endpoint coefficients1. They are not merely
positive or bounded coefficients.

This is a valid full algebraic reduction, not merely finite jets.
It is also a description of the same root-selection/correlation
problem: no quantitative bound on the mixed coefficients follows
solely from (18)--(20). The genuine next estimate must use all
the coefficient equations in (20); coprime norm structure and
the existence of boundary zeros alone are insufficient.

## 9. A positive-coefficient, optimal weighted blindspot

The parent's stronger prescribed-factor counterexample checks by hand.
Start with E=(1+w)^4 and O=(w-1)^3. These obey cross-phase,
E(1)=16 and O(1)=O'(1)=0. Their summed autocorrelations are

    R0=70+20=90,
    R1=56-15=41, R2=28+6=34,
    R3=8-1=7, R4=1.

All off-zero Fourier coefficients are now POSITIVE, eliminating
the negative-Fourier loophole in the earlier generic example.
Multiply both channels by K=1+w^9 and divide the full Q_2 by
sqrt(180). The resulting weighted symbol has constant lambda=1
and cosine coefficients at frequencies1,...,13 exactly

    (82,68,14,2,1,7,34,41,90,41,34,7,1)/90.

Every coefficient lies in(0,1], with maximum1; they are not
all1. The unit-circle zeros of K prove actual weighted M=1
from the all-circle square identity, not a sampled minimum.
The full factor is

    Q_2(z)=(1+z^18)*[(1+z^2)^4+z*(z^2-1)^3]/sqrt(180).

Its maximum coefficient magnitude is6/sqrt(180)=1/sqrt(5)<1.
It still has O'(1)=0 and net delta=0. Direct moment bookkeeping,
BEFORE the common linear scale1/sqrt(180), is

    base: S16, Nminus4, mu4, Vint64, Vminus12;
    duplicated: S32, Nminus8, mu13,
                Vint2720, Vminus672, Vabs4064.

For the duplicate, the two old copies are18 apart. Their new
centers are displaced by plus/minus9, and the base negative
centered first moment is -3+3=0. Thus
Vint=2*64+2*16*81=2720 and Vminus=2*(12+4*81)=672.
It follows exactly that

    Nminus/S=1/4>1/8,
    alpha=672/4064=21/127>1/8.

All S,N and variance quantities scale linearly with the common
factor; the ratios do not change. This is an OPTIMAL weighted
positive-coefficient-cap example with bounded qmax, zero first
phase imbalance, and BOTH signed budgets false. It falsifies
the PRESCRIBED-factor phase-only inference. It is not Boolean,
does not rule out a better spectral branch, and is not a
counterexample to the existential stable-factor target.

The paper calculation uses no numerical minima and needs no
new root search. The root may separately exact-check the small
polynomial identities on Dirichlet; the advisor did not execute
that verification or perform any VM action. Preserve this scoped
falsifier while continuing with the complete unit-amplitude
identity (20), not phase jets or coefficient caps alone.

## 10. Final canonical/Chebyshev and machine-artifact audit

The parent's optional real-Chebyshev consequence checks too. For
nontrivial V and d=2m, reciprocity gives real polynomials u,v with

    U(w)=w^m*u(T),
    V(w)=(w-1)*w^(m-1)*v(T), T=(w+w^(-1))/2.

Here deg(u)=m and deg(v)<=m-1. Therefore

    p_mix=u(T)^2+2*(1-T)*v(T)^2.                 (21)

This polynomial is STRICTLY POSITIVE for every real T. For T<1,
a zero would require u=v=0. The corresponding nonzero solution
of w+w^(-1)=2T would then be a common root of U,V, forbidden by
coprimality. At T=1, U(1)!=0. For T>1, choose a positive real w.
The Boolean symbol p(w) is positive. K has no positive real root,
so its sign is constant on(0,infinity) and K(w)K(1/w)>0. Thus
p_mix=p(w)/(K(w)K(1/w))>0. For V=0 the mixed factor is simply
a positive constant and the same conclusion holds.

The symmetric expression w^(-k)*K(w)*K_rev(w), k=deg(K), is a
real polynomial in T. Consequently every real root of
lambda+sum_(a in A)T_a(T) is carried by this K polynomial,
not by the reduced norm(21). This is a root-location consequence,
not a quantitative Boolean coefficient inequality. It does not
permit deleting the exact off-center0/1 equations in(20).

I read the final src/joint_factor_identities.py and its saved
experiments/joint_factor_2026-10-23/identities.json, without running
either. The CURRENT artifact has13checks with PASS after the
canonical additions. It uses symbolic rational simplification
for identities and separate sparse Fraction convolution for the
examples. The weighted normalization and doubled/undoubled
angles are correct: the Q_2 circle zero at x=pi/18 corresponds
to the undoubled weighted minimum at pi/9. The signed geometry,
gcd, reciprocity and full norm example checks match this audit.

The machine artifact explicitly does NOT certify the general
minimax inequalities, polyphase concentration, stable-factor
existence, a universal Chowla bound or a Lean theorem. Those
distinctions are accurate. I sent one minor parent reference
correction: its transform-norm discussion should cite its(13),
not its newly renumbered root-increment equation(12).

The parent has corrected the actual/generic real-root distinction
and retained the full Boolean coefficient identity as the next
derivation. That canonical formulation and the decision not to
launch another n5 control are sound. No extra search, computation,
agent, outreach, GPU or VM lifecycle action was performed here.
