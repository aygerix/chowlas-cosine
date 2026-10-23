# CP vector centroids and bounded translations: exact identities and obstruction

2026-10-23. Sole internal AI advisor. Paper mathematics and read-only
ledger review only. No computation, VM lifecycle action, GPU, extra
agent or outreach. Shared Dirichlet is untouched. Full Chowla remains
open. This is an attempt within the existing P76 CP route, not a new
equivalence, a universal lower bound, or a claim of external novelty.

## 1. Exact finite Boolean setting

Let A be a nonempty finite set of distinct positive integers, n=|A|,
f_A(x)=sum_A cos(ax), and suppose a FINITE completely positive
certificate is given:

    P(x)=lambda+f_A(x)=sum_i |Q_i(exp(ix))|^2,
    Q_i(z)=sum_b q_(i,b) z^b, q_(i,b)>=0 real.

Monomial translations of individual factors are immaterial. Drop zero
factors and put

    S_i=sum_b q_(i,b)>0, lambda_i=sum_b q_(i,b)^2,
    r_i(d)=sum_b q_(i,b)q_(i,b+d).

Then

    sum_i lambda_i=lambda,
    sum_i S_i^2=lambda+n,
    sum_i r_i(d)=(1/2)1_(+/-A)(d), d!=0.              (1)

Nonnegativity is essential: every missing lag has zero correlation
in EVERY component, so every support is an A-difference clique.
For any complex coefficient vector x supported on that clique,

    integral P*|sum_b x_b z^b|^2
          =(lambda-1/2)sum_b |x_b|^2
                         +(1/2)|sum_b x_b|^2.        (2)

This follows by expanding every diagonal and off-diagonal term;
all differences of distinct support points belong to +/-A. In
particular a centered coefficient vector has an exact Gram identity,
not a discarded missing-lag error.

## 2. Rank-free joint centroid inequality

For each factor set

    mu_i=sum_b b*q_(i,b)/S_i,
    V_i=sum_b q_(i,b)*(b-mu_i)^2,
    E_i=sum_b q_(i,b)^2*(b-mu_i)^2,
    X_i=(z*d/dz-mu_i)Q_i.

The coefficient sum of X_i is0. Thus(2) gives EXACTLY

    integral P*|X_i|^2=(lambda-1/2)E_i.               (3)

Differentiating P on the circle gives
P'=-2Im(sum_i X_i*conj(Q_i)). Pointwise Cauchy and(3) imply

    integral P'^2/4
       <=integral P*sum_i |X_i|^2
       =(lambda-1/2)sum_i E_i.                       (4)

The weighted pair-variance identity and(1) give

    sum_i S_i*V_i=sum_(d>0)d^2 sum_i r_i(d)
                    =(1/2)sum_(a in A)a^2,
    integral P'^2/4=(1/8)sum_A a^2.

Hence

    sum_i S_i*V_i
       <=4(lambda-1/2)sum_i E_i
       <=4(lambda-1/2)sum_i qmax_i*V_i,              (5)

where qmax_i=max_b q_(i,b). This extends the single-positive-factor
centroid inequality with no component-count factor. It is a necessary
inequality for the given certificate. It does NOT imply a root bound
unless one obtains a lower bound for the variance-weighted ratio in(5).

## 3. A growing actual-optimal Boolean satellite falsifies that bridge

The tempting lower bound

    (sum_i S_i*V_i)/(sum_i qmax_i*V_i) >=c*sqrt(n)     (6)

is false, even uniformly over EVERY optimal nonnegative certificate
on an explicit growing low-M family.

Take any even k>=8. Choose epsilon_i in{0,1}, exactly half of each,
and put

    B={2*9^i+epsilon_i: 1<=i<=k},
    A0=the positive differences of B,
    X=max A0, n0=k(k-1)/2.

The differences are unique. In an equality of two differences,
2*((9^j-9^i)-(9^l-9^h)) is a multiple of16, since9 is1 modulo8,
while the epsilon error is at most2 in absolute value. Both parts
therefore vanish. The9-adic valuation of9^j-9^i then identifies
i=h, followed by j=l. This proof also works if indices start at0.

At x=pi the k exponentials in F_B have balanced signs, so F_B(pi)=0.
The square identity therefore gives ACTUAL M(A0)=k/2 exactly.

Choose an odd integer L>2X and set A=A0 union{L}. Then

    n=n0+1,
    M(A)=lambda=k/2+1,                               (7)

because the square identity and cos(Lx)>=-1 give the global lower
bound, with equality at pi. For k>=6, lambda<=sqrt(n). Its ACTUAL
ratio tends1/sqrt2, so this is not a vanishing-ratio construction.

An optimal nonnegative certificate is

    Q0=F_B/sqrt2, Q1=(1+z^L)/sqrt2.

For the satellite,

    S1=sqrt2, qmax1=1/sqrt2,
    V1=L^2/(2sqrt2), E1=L^2/4,
    S1*V1=L^2/2, qmax1*V1=L^2/4.

Thus the ratio in(6) tends2 as L grows, with k fixed. Choosing L
much larger than kX and then letting k grow keeps the ratio bounded
while sqrt(n) diverges.

This is not merely a bad choice among positive decompositions.
Any factor containing the lag L has exactly TWO support points:
a third point would require a and L-a both to be in A0 for some
0<a<L, impossible when L>2X. Thus these are pure lag-L factors.
Their total correlation at L is1/2 and their total squared norm is
at least1. The remaining factors certify lambda_low+f_A0>=0,
so their norm cost is at least k/2. At the total optimum(7) both
bounds are equalities. Every lag-L factor is balanced, either by
the equality case of AM-GM or by its required zero at pi.

Writing its two endpoint coefficients as t_j,t_j gives
sum_j t_j^2=1/2. Consequently EVERY optimal nonnegative certificate
has the SAME satellite totals L^2/2 and L^2/4 above. All remaining
factor supports have diameter at most X. In fact the weighted
pair-variance identity gives the stronger representation-independent
formula

    sum_low S_i*V_i=(1/2)sum_(a in A0)a^2<=n0*X^2/2,
    sum_low qmax_i*V_i<=sum_low S_i*V_i.

Hence convergence of the ratio to2 is uniform over all such optimal
certificates. For example any odd L>=k^2X makes the error O(k^-2).
This refutes the global variance bridge, not CP-Chowla, signed-factor
selection, or adaptive certificates that discard a distant singleton.

Conditionally on a hypothetical growing family with CP cost
lambda=o(sqrt(n)), adding a sufficiently distant singleton preserves
that small normalized cost while producing the same variance
domination. Thus merely adding the hypothesis of small normalized
CP cost would not justify the scalar average in(6), if such a family
exists. This is a conditional padding observation, not its existence.

## 4. Why a sharp lag window is not a free replacement

A universal positive-definite lag multiplier m:Z->{0,1} with m(0)=1
must be the indicator of a subgroup of Z. In a Gram representation,
an inner product1 between unit vectors makes those vectors equal;
therefore {d:m(d)=1} is closed under differences. It is qZ, {0},
or Z. Thus universal Boolean-preserving positive Schur filtering
supplies exactly the old sublattice operation P76(d), not a sharp
frequency window. A proposed adaptive localization needs an actual
factor/incidence argument, not substitution of arbitrary weights
for d^2 in the centroid proof.

## 5. Bounded translation identities

Fix a real theta. Define

    c_i=Q_i(exp(i theta))/S_i,
    X_i(z)=Q_i(exp(i theta)z)-c_i*Q_i(z),
    x_(i,b)=(exp(i b theta)-c_i)q_(i,b).

Then sum_b x_(i,b)=0, |c_i|<=1, and(2) gives

    integral P*|X_i|^2=(lambda-1/2)||x_i||_2^2.        (8)

The exact bounded signal is

    sum_i [S_i^2-|Q_i(exp(i theta))|^2]
                                 =n-f_A(theta).     (9)

These tests avoid the L^2 satellite explosion in(5); all their
coefficient multipliers are bounded. They do not automatically
couple their componentwise correlation rows.

For U_i(d)=sum_b x_(i,b)q_(i,b+d), direct index changes give

    U_i(-d)=exp(i d theta)U_i(d)
                  +c_i*(exp(i d theta)-1)*r_i(d).    (10)

Discarding all cross-component products and applying Cauchy to(10)
only controls sum_i |c_i|^2*r_i(d)^2. Booleanity specifies
sum_i r_i(d)=1_A(d)/2, not each r_i. These are different quantities.
Replacing one Q by R copies Q/sqrt(R) keeps A,lambda,P and(9)
unchanged while dividing that diagonal-only square sum by R. This
is an exact algebraic falsifier of any such componentwise closure,
with no new support, asymptotic construction, or numerical test.

## 6. Full intrinsic cross-component completion

The object that survives this test retains EVERY component pair:

    R_ij(d)=sum_b q_(i,b)q_(j,b+d),
    U_ij(d)=sum_b x_(i,b)q_(j,b+d), d in Z.

Parseval and(8) give

    E_theta=sum_(i,j,d)|U_ij(d)|^2
           =integral P*sum_i|X_i|^2
           =(lambda-1/2)sum_i ||x_i||^2.             (11)

The exact phase-paired identity is

    U_ij(-d)-exp(i d theta)U_ji(d)
        =(exp(i d theta)c_j-c_i)*R_ji(d).             (12)

It follows by changing b to b+d in the first term. No coefficient
sign, endpoint or exterior lag has been dropped. Parallelogram under
the involution (i,j,d)<->(j,i,-d) proves the completion

    E_theta
      =(1/4)sum_(i,j,d)|exp(i d theta)c_j-c_i|^2
                                           *R_ji(d)^2
       +(1/4)sum_(i,j,d)|U_ij(-d)
                               +exp(i d theta)U_ji(d)|^2.  (13)

The sum includes d=0. The coefficients are real in R, but x,c,U
are generally complex, so absolute values are essential. Artificial
component replication leaves the full sums in(11)-(13) unchanged.
Independent monomial translations also preserve them after the
corresponding reindexing of cross lags and phases.

This is the retained finite joint object. Its cross R_ji(d) are not
fixed by the Boolean diagonal sum(1); there is no proved lower bound
at a scale that would force lambda>=c*sqrt(n). It is not a new
completeness theorem, an automatic repair of(6), or an authorization
for a new component/parameter probe.

## 7. Ordered-cut version and its exact coherence price

For a common real cut position T put phi(b)=1_(b>T),
c_i=sum_b phi(b)q_(i,b)/S_i, and x_(i,b)=(phi(b)-c_i)q_(i,b).
Again(2) has zero mean penalty. For d>0 the full pair satisfies

    U_ij(-d)-U_ji(d)
      =J_ij(d)+(c_j-c_i)R_ji(d),                     (14)
    J_ij(d)=sum_b q_(j,b)q_(i,b+d)
                                *(phi(b+d)-phi(b))>=0.

Thus J counts actual ordered crossing pairs, but independently
centering the factors introduces the signed coherence term in(14).
Choosing a common c removes that term and instead gives the exact
upper penalty (1/2)sum_i S_i^2*(c_i-c)^2 in(2). Dropping either
price is invalid. Component origins can be shifted without changing
the certificate, so an order-based assertion must also specify or
optimize those choices; it is not automatically intrinsic.

## 8. Common complex c and the generic contraction collapse

For bounded translations choose a COMMON c in C and put
X_i=Q_i(exp(i theta)z)-cQ_i(z). Write

    a_theta=sum_(i,b) q_(i,b)^2 exp(i b theta),
    T_theta=sum_i S_i Q_i(exp(i theta)),
    A_theta(x)=sum_i Q_i(exp(i(x+theta)))*conj(Q_i(exp(ix))).

The mean term in(2) sums to

    (1/2)sum_i |Q_i(exp(i theta))-cS_i|^2.

Its minimum is achieved at

    c_mean=T_theta/(lambda+n),
    penalty_min=(1/2)[P(theta)-|T_theta|^2/(lambda+n)]. (15)

Complex conjugation/moduli in this formula cannot be omitted.
This minimizes ONLY the mean penalty, not the complete energy.

Lagrange's identity gives

    integral P*sum_i|X_i|^2
      =||A_theta-cP||_2^2
       +sum_(i<j)||Q_i(shift)Q_j-Q_j(shift)Q_i||_2^2. (16)

The exterior-square sum is independent of c. Furthermore

    wedge_sum=lambda^2+f_A(theta)/2-||A_theta||_2^2,
    <A_theta,P>=(lambda-1/2)a_theta+T_theta/2.         (17)

The second identity uses the Boolean off-lag coefficients and the
componentwise missing-lag zeros. It follows by summing the Fourier
coefficients of A_theta. Equations(16)-(17) reproduce EXACTLY

    E(c)=lambda^2+f_A(theta)/2
          +|c|^2*(lambda^2+n/2)
          -2Re(conj(c)*B_theta),
    B_theta=(lambda-1/2)a_theta+T_theta/2.             (18)

The full-energy minimizer is therefore
c_energy=B_theta/(lambda^2+n/2), generally different from(15).
Its nonnegativity gives only

    |B_theta|^2<=(lambda^2+f_A(theta)/2)
                                      *(lambda^2+n/2),

the same generic Schur/Cauchy completion already present in(16).
Do not optimize c again and report this algebra as a new Boolean
size estimate. Dropping the exterior-square term is a generic
Cauchy relaxation, not control of it.

## 9. Strategic decision and exact remaining operation

The changed finite attempt has produced a rank-free necessary
inequality(5), an explicit optimal growing Boolean falsifier of its
global variance bridge, and the full bounded cross-lag completion(13).
The proposed easy repairs fail: sharp universal lag filters give only
sublattices, independent component pairing loses information under
replication, and common-c contraction collapses to(18).

Retain(13) only as a precise object for a genuinely Boolean next
derivation. A useful result would have to relate its off-diagonal
R_ji(d) to the EXACT diagonal incidences(1), with a quantitative
lower bound or an explicit Boolean counterexample to such a bound.
It is not enough to assume component coherence or rewrite (1) after
discarding the cross terms. Kill a proposed closure if it is merely
generic PSD polarization, changes under replication, or uses the
false unit-amplitude equation separately for r_i.

No numerical pilot is warranted by the identities alone. This does
not close CP-Chowla, signed Boolean witnesses or the construction
track, and it does not turn a sufficient CP subclass into the full
unrestricted problem. The preceding continuum stop decision and
its exact profile model are in the
[two-scale audit](advisor_cubic_two_scale_2026-10-23.md).
