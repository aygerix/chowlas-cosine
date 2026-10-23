# R0 continuation: two-variable prefix/pad interaction

2026-10-23. Paper derivations independently checked by the internal
[advisor audit](advisor_R0_resume_2026-10-23.md). All integrals are
probability Haar integrals. No kernel verification or external review
is claimed. The separate bounded search did not falsify R0 or S0.
Full Chowla and the uniform Boolean sign principle remain open.

## Exact tensor identity

Let U(z),V(w) be nonconstant analytic polynomials with real coefficients,
zero constants, and lambda>M(U)+M(V), where M(U)=-min Re U, etc.
The reciprocal p(z,w)=1/(lambda+U(z)+V(w)) is analytic beyond the
closed bidisk. Write

    p_U(z)=1/(lambda+U(z)), p_V(w)=1/(lambda+V(w)),
    p_mix=p-p_U-p_V+1/lambda.

The coefficients of p_mix have BOTH indices positive. The pure-axis
coefficient arrays of p agree exactly with p_U and p_V, respectively.
Orthogonality on the bidisk boundary therefore gives

    S_total=S_U+S_V-lambda^-2+||p_mix||2²,
    g_total=g_U+g_V+lambda²||p_mix||2².

For Boolean supports on the two coordinate axes, the selected inverse-
square pairing also separates exactly:

    T_total=T_U+T_V.

This is because [z^a w^0]p²=[z^a]p_U² and similarly for the other
axis. The norm does NOT separate without the mixed term.

For q=Im p, D=2Re(U+V), the same analytic orthogonality as on the
circle gives Q=g/(2lambda²), H=-g/lambda-T/2. Consequently

    H_total=H_U+H_V-lambda*||p_mix||2².

Thus mixed reciprocal coefficients give a NEGATIVE energy correction
in this exact two-variable decomposition. They cannot be discarded
when transferring the oversized-lambda prefix example. The individual
H_U,H_V here are evaluated at the SAME lambda fixed by TOTAL cardinality;
neither is automatically an instance of R0 at its own cardinality.
The identity does not determine whether H_total is negative.

For an integer union A_L=A_U union L*A_V with L>max A_U, Booleanity
and cardinality are exact and M(A_L)<=M(U)+M(V). Its circle integrals
converge to these torus quantities as L tends to infinity, with the
explicit checked transfer bound in the next section. No finite-L
equality or prefix-only sign conclusion is claimed.

## Quantitative integer-dilation transfer

For a C1 doubly periodic real function h, partition the x-circle into
the L Voronoi cells around x_j=(2pi*j+y)/L for fixed y. Integrating
the Lipschitz distance within each cell gives

    |<h(x,Lx)>_x-<h(x,y)>_(x,y)|
      <= pi/(2L)*||partial_x h||infinity.

Indeed the diagonal integral is the y-average of these shifted
L-point Riemann sums; the average distance to the nearest grid point
is pi/(2L). No Fourier alias cutoff is assumed.

For Boolean axis supports, put N=|A_U|+|A_V| and J=sum_(a in A_U)a.
Assume the certified split bound M(U)+M(V)<=sqrt(N), and fix
lambda=2sqrt(N), so d=Re(lambda+U+V)>=sqrt(N). For p=1/W,

    |partial_x p|<=J/|W|², |q|<=1/(2d),
    ||partial_x(q²)||infinity<=J/d³.

For H's integrand h=2Re(U+V)q², use |Re(U+V)|<=|W|+lambda and
|q|<=1/|W|. The product derivative is bounded by

    ||partial_x h||infinity<=6J/d²+4lambda*J/d³.

Consequently, with subscripts L and torus denoting diagonal and double
integrals respectively, and pi<22/7,

    |Q_L-Q_torus|<=11J/(7L*N^(3/2)),
    |H_L-H_torus|<=22J/(L*N).

Thus for the actual R0 discriminator E=H+sqrt(N)*Q/100,

    |E_L-E_torus|<23J/(L*N).

If E_torus>=delta>0 is certified, every integer
L>max(max A_U,23J/(N*delta)) is an ACTUAL-lowM Boolean counterexample
to the proposed numerical R0 inequality. If E_torus<=-delta, the same
threshold proves this seed succeeds at its numerical target for all
those L. A positive E is a falsifier of R0, not of Chowla.

This is a transfer/certification lemma only; no torus sign premise is
proved here. Crucially lambda is fixed by total N throughout.

## Boolean padding theorem under a weak reciprocal norm gap

Candidate proved implication: if R0 holds for EVERY Boolean support,
then there is an absolute positive lowM L1-flatness constant on the
STRICT-margin class M(V)<=sqrt(|V|)/2. Thus the exceptional zero carrier
does not automatically avoid every flatness consequence merely because
its normalized amplitude is unbounded. This is not a proof of R0,
flatness or Chowla, and no weak-gap Boolean input has been found.

More concretely, suppose V is a Boolean support of cardinality N>=2^44,
M(V)<=sqrt(N)/2, and, at lambda0=2sqrt(N),

    g_V(lambda0)=||V/(lambda0+V)||2²<=2^-82.

Here V also denotes its analytic polynomial. Define explicitly

    k=floor(sqrt(N)/2^20),
    B={1,9,...,9^(k-1)}, U=positive differences of B,
    m=k(k-1)/2, N'=N+m, lambda=2sqrt(N'),
    L=2^16*N'*9^k, A=U union L*V.

Claim: this A is a genuine ACTUAL-lowM Boolean set, yet its prescribed
zero-carrier reciprocal has H_A>0. It therefore falsifies even R0's
qualitative negative-sign version. The hypothesis is not asserted to
hold for an existing Boolean set; this is a conditional transformation.

### 1. Difference-block moments and positive energy at oversized lambda

The differences in U are distinct: the least nonzero base9 digit
determines the smaller exponent and then the larger exponent. Hence
|U|=m and the difference-square identity gives M(U)<=k/2.

For any sum of at most4 signed differences, zero exponent forces each
base9 coefficient to vanish, since every coefficient has absolute value
at most4<9; divide repeatedly by9. Thus moments through fourth order
agree with those of sum_(i>j) z_i/z_j on an independent k-torus.

Let t=#ordered(a,b,c) in U³ with a+b=c. A balanced three-edge graph,
with no loops and two edges of one orientation, must be a triangle.
Each chain i>j>ell contributes two ordered decompositions, so

    t=2*binom(k,3),
    <2Re(U)*(Im U)²>=t/2=binom(k,3).

Also <|U|4><=24k^4: a balanced term of U²*conjugate(U)² has four
ordered source labels (at most k^4 choices), and its ordered targets
are one of the4! permutations of that source multiset. Dropping edge
orientation and no-loop restrictions only increases this count.

If lambda>=k, then Re(lambda+sU)>=lambda/2 for0<=s<=1. Differentiating
|lambda+sU|^-4 in s gives the pointwise bound

    ||lambda+U|^-4-lambda^-4|<=128|U|/lambda^5.

Consequently the zero-carrier energy at this SAME lambda satisfies

    H_U>=binom(k,3)/lambda^4-6144k^4/lambda^5.

For k>=4, binom(k,3)>=k^3/24. At lambda>=2^19*k the error is less
than k^3/(48lambda^4), and therefore

    H_U>=k^3/(48lambda^4)>0.

This is an actual Boolean DIFFERENCE block at deliberately oversized
lambda, not a weighted prefix. It will be calibrated by total N'.

### 2. The complete padding cost is small when g_V is small

Our choices imply k>=4, k<=sqrt(N)/2^20, N'<2N, lambda<3sqrt(N),
lambda/k>=2^21 and k/lambda>=2^-23. Also

    M(U)+M(V)<=k/2+sqrt(N)/2<sqrt(N)<=sqrt(N').

Thus the joint torus inverse margin d is at least lambda/4, and
lambda-M(U)>=lambda/2. Monotonicity of |lambda+V| in real lambda
above M(V) gives g_V(lambda)<=g_V(lambda0)<=2^-82.

Write zeta_V=V/(lambda+V). The exact identity

    p-p_U=-zeta_V*p_U*(lambda+V)/(lambda+U+V)

and |(lambda+V)/(lambda+U+V)|<=1+|U|/d give

    ||p-p_U||2²
      <=4g_V/lambda²*(1+||U||2/d)²
      <=36g_V/lambda².

Here ||U||2=sqrt(m)<=k<=lambda/2. Orthogonality gives
||p_mix||2²<=||p-p_U||2². Furthermore, since M(V)<=lambda/2,

    H_V>=-2M(V)Q_V>=-g_V/(2lambda).

Using the FULL tensor identity, not a prefix-only truncation,

    H_torus>=k³/(48lambda^4)-(73/2)*g_V/lambda.

Since (k/lambda)³/4096>=2^-81>g_V, the negative cost is smaller
than k³/(96lambda^4). Thus

    H_torus>=delta=k³/(96lambda^4)>0.

### 3. Explicit finite integer lift

Let J=sum_(u in U)u. Certainly J<=k²*9^k. The preceding derivative
transfer, with total N', gives

    |H_A-H_torus|<=22J/(L*N').

It is enough that L>33792*J*N'/k³, because lambda^4=16N'².
Our integer L=2^16*N'*9^k meets this inequality for k>=4 and also
exceeds max(U). Hence A is disjoint Boolean, has cardinality N',
satisfies the ACTUAL all-circle lowM hypothesis and has H_A>0.
The frequencies can be enormous; R0 has no frequency ceiling.

### 4. Consequence and exact limitation

If R0 is universal, the previous weak-gap V cannot exist. Thus
g_V(2sqrt N)>=2^-82 whenever M(V)<=sqrt(N)/2 and N>=2^44.
For smaller N, the elementary bound

    g_V=||V/(lambda0+V)||2²>=N/(lambda0+N)²
        =1/(sqrt(N)+2)²>2^-82

already suffices. Finally the exact identity

    <Re(V)/|lambda0+V|²>=-g_V/lambda0

implies ||Re V||1>=(lambda0-M(V))²*g_V/lambda0
>=lambda0*g_V/4. Therefore R0 would force, conservatively,

    ||f_V||1>=2^-84*sqrt(N) whenever M(V)<=sqrt(N)/2.

This is only a NECESSARY consequence of a hypothetical uniform R0.
It neither proves the project's numerical L25 constant1/10 nor a
converse from flatness to the particular zero-carrier bound. It does
complete an explicit Boolean padding sign-transfer conditional on
weak gap, retaining both pure high-block and mixed contributions.

## Qualitative sign self-improves under Boolean padding (advisor checked)

The proof above uses only that a universally admissible set cannot have
H_A>0; it does NOT need R0's uniform negative margin. Define **S0**:

    For EVERY Boolean A with ACTUAL M(A)<=sqrt(|A|),
    at FIXED lambda=2sqrt(|A|), H_A=<2f_A(Im 1/(lambda+F_A))²><=0.

If S0 holds, the explicit padding argument rules out weak g_V on
M(V)<=sqrt(N)/2, giving the same flatness conclusion. Since
||f_V||1<=2M(V), this proves

    S0 implies M(V)>=2^-85*sqrt(N) for EVERY Boolean V.

The complementary M(V)>sqrt(N)/2 branch is immediate. Therefore a
UNIVERSAL qualitative sign theorem, coupled to the proved Boolean
closure/amplification, would suffice for full Chowla. A sign calculation
on one set supplies no such uniform conclusion. No converse from Chowla
to this prescribed sign witness, and no proof of S0, is claimed.

This sharpens the old audit's warning that a qualitative sign alone
gives no rate: that remains true for an individual witness, while the
global quantifier plus Boolean padding now gives a rate. Preserve both
distinctions rather than silently treating the old statement as a
universal impossibility result.

For any fixed0<delta<=1, the same proof with
k=floor(delta*sqrt(N)/2^20) gives a positive-energy Boolean output if
M(V)<=(1-delta)sqrt(N), N>=2^44/delta² and
g_V(2sqrt N)<=delta³*2^-82. Under S0, therefore,
||f_V||1>=delta³*2^-84*sqrt(N) on every strict-margin class. This does
not supply the original numerical L25 constant on its full boundary.

## Relaxation check and strategic limit

The advisor supplies an explicit weighted sign falsifier in Section5
of the linked audit: V_N=sum_(j=1)^N(1-j/(N+1))z^j has exactly N
occupied frequencies and coefficients in(0,1), M(V_N)<=1/2 and
g_V(2sqrt N)<=3N^-1/4. For N>=2^336 the preceding probe and integer
lift give positive H at the same occupied-count calibration. Thus
nonnegativity and an upper coefficient cap do not imply S0. This
does not provide a Boolean weak-gap input or a Chowla counterexample.

The quantitative R0 margin is no longer necessary as a sufficient
target. The next attempt is a proof or valid Boolean falsification of
the universal sign S0, retaining coefficientwise unit amplitudes.
The conditional amplification is a completed reduction, not a proof
of that remaining sign. The failed finite adversary does not strengthen
the universal conjecture or justify a larger search or GPU deployment.
