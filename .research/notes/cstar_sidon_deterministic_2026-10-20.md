# Deterministic Sidon-fiber bounds by a selective reference certificate

2026-10-20. CSTAR CHAIN(c) / DESIGN research record, not a manuscript.
Full Chowla remains OPEN. This extends the previous [averaged result](cstar_sidon_mixed_2026-10-20.md)
to deterministic choices in the specified architectures. It does not
classify arbitrary positive-integer supports or arbitrary encodings.

## 1. The sharp conditional estimate was unnecessary

The previous remaining target was H_bar(P)<=C p^3 for every fixed
lifted affine parabola P. C=2 failed at p11. Here a weaker, UNIFORM
pairwise bound with four logarithms is proved. A reference certificate
which leaves the shortest directions unchanged absorbs that loss.
The actual support is never truncated by this certificate operation.
No uniform marginal law or independence of the actual choices remains.

Let X be a sufficiently large integer, U=floor(sqrt(X)). For every
canonical primitive u in Z^2, 0<||u||<=U, choose the largest odd prime
p_u<=floor(X/(sqrt(2)||u||)). All actual point sets below lie in
{0,...,p_u-1}^2, and every matrix u(b-b')^T has norm<X. A cyclic Sidon
set means that all ordered nonzero differences are distinct modulo p.
Its integer differences are also distinct. Primitive-u planes intersect
only at zero. Encode sign pairs by an integer linear map L:Z^4->Z with
no nonzero integer kernel vector of norm<=3X, taking positive absolute
values. This gives distinct positive frequencies and preserves every
moment of degree<=3 used below. CRT h=6000X^3+odd and ordinary base
6X+1 encodings qualify. Write n for the positive frequency count,
D_A=2f_A, K=2M(A).

**Theorem A (paper proof).** In each direction take ANY p_u-point
cyclic Sidon set P_u, without a probability-law assumption. Then

    n=sum p_u(p_u-1)/2=Theta(X^2 log X),
    M(A)>=sqrt(n)/16                                           (A)

for all sufficiently large X, uniformly in all these deterministic
choices. This includes the entire affine-parabola family of the
previous turn, not only its uniform-marginal samplers.
The same proof works for U=floor(X^alpha), any fixed0<alpha<=1/2;
the threshold may depend on alpha.

## 2. Pairwise completion estimate

For a p-point cyclic Sidon set C there are exactly p-1 missing nonzero
differences in F_p^2. At every nontrivial group character,

    |F_C|^2=p-1-sum_(missing d) character(d)<=2p-2.              (1)

No classification of such Sidon sets is assumed. With
D_p(t)=sum_(j=0)^(p-1) exp(ijt), set

    V(theta)=D_p(theta1)D_p(theta2)/p, E_C=F_C-V,
    L_p=3+2log p.

The p-grid Lagrange kernel is D_p(t-2pi j/p)/p. Its l1 sum is <=L_p:
bound the nearest term by1 and the remaining terms by the harmonic
tail using |sin(pi d/p)|>=2|d|/p. Tensoring the two kernels and (1) gives

    ||E_C||_infinity^2 <=2p L_p^4.                             (2)

For two p-point cyclic Sidon sets, F=F_C,G=F_C', q=|F|^2-|G|^2,
integer Sidonicity gives integral|F|^4=2p^2-p and likewise for G.
Also ||V||_4^2<=p, so ||F||_4^2<=2p and each residual has L4 norm
squared<=9p. More generally, for any common V with these L4 bounds,
and ||F-V||_infinity,||G-V||_infinity<=R,

    H(C,C')=integral (|F|^2-|C|) q^2 <=208 p^2 R^2.             (3)

To check constants put E=F-V,E'=G-V. Then
q^2<=16|V|^2(|E|^2+|E'|^2)+4(|E|^4+|E'|^4).
Use integral |F|^2|V|^2<=2p^2 and
integral |F|^2|E|^4<=R^2||F||_4^2||E||_4^2<=18p^2R^2,
and the same bound for E'. Since |F|^2-|C|<=|F|^2, the constants
are16*(2+2)+4*(18+18)=208. Thus in particular

    H(C,C')<=416 p^3 L_p^4                                    (4)

for EVERY pair of p-point cyclic Sidon sets. This is stronger than a
conditional expected bound with those logarithms. No actual or
reference averaging was used for (4), and no sixth-moment theorem is
needed for this step. The sharper Cp^3 question stays open but is no
longer a necessary ingredient for (A).

## 3. Freeze the reference on short directions

For a fixed actual A, construct reference B as follows. If
||u||<T=ceil((1+log X)^4), leave P_u unchanged. Above T choose a
uniform affine-parabola reference of the same p_u points. The source
of randomness is a finite averaging device in the certificate only.

For each reference realization q=D_A-D_B, equal cardinality gives

    a=<D_A,q>=2|A\B|, Q=||q||_2^2=2a.

The known conditional coefficient-count bound for uniform affine
parabolas is a_bar_u>=n_u/8. It applies to ANY actual set of n_u
sign pairs, not just another affine parabola. Its reference coefficient
is p/(p+1) times the product triangular taper. At most half the selected
signed frequencies can have coefficient>7/8, by the small-origin-box
count. Thus a_bar>=n_high/8. Since the excluded reference directions
carry only O(X^2 log T)=O(X^2 loglog X) frequencies, n_high/n->1,
and eventually a_bar>=n/16.

The exact ruling identity gives

    H=<D_A,q^2>=sum_left H_u+sum_right H_v-sum_lines H_l,
    |sum_right H_v-sum_lines H_l|
        <=36000000X^2U^2(1+2log U).                            (5)

This identity still includes ALL actual A targets on frozen planes.
Only q vanishes there. Dropping those A targets would be an error.
Additive rank-one triples lie in one ruling, with scalar lines counted
twice. The preceding note proved the coarser19683X^2U^4 bound; the
sharper count is proved in the next section.

The lattice tail sum_(||u||>=T)||u||^(-3)<=64/T, T>=2, follows by
integer square shells. Since p_u<=X/||u|| and
L_p^4<=81(1+log X)^4, (4) implies

    H_bar<=5184*416 X^3+36000000X^2U^2(1+2log U)
         =O(X^3(1+log X)).                                    (6)

Here H_bar averages over the reference with A FIXED. Positivity of
(D_A+K)(s+tq)^2 gives positive 2x2 moment matrices. Average them over
the reference; the resulting determinant inequality is

    2a_bar K^2+H_bar K-a_bar^2>=0.                             (7)

At k=sqrt(n)/8 and a_bar>=n/16 its left side is at most
-n^2/512+H_bar sqrt(n)/8, which is negative eventually because
n=Theta(X^2 log X). This proves (A). A checkable sufficient parameter
condition is n_high>=n/2 and (64T_X)^2<n^3, with T_X the explicit
right side of (6). At the earlier U=X^(1/4), using the coarser count
instead gives the alternative H_bar<=2176227X^3; that constant is recorded by the
finite checker. The probes do NOT meet the conservative size condition.

The elementary prime comparison (Bertrand) and primitive-vector count
sum_(||u||<=R)||u||^(-2)=(6/pi)log R+O(1) suffice throughout. No claim
p_u asymptotic to X/(sqrt(2)||u||), or delicate prime-gap result, is needed.

## 4. A sharper off-left count without a boundary error

For ordered distinct canonical primitive u0,u1,u2 with norm<=U let
a=(a0,a1,a2) be their primitive integer relation and
ell=max_i |a_i| ||u_i||. Define D(U)=sum1/ell^2. Then

    D(U)<=4000000U^2(1+2log U).                                (8)

All coefficients are nonzero, and max|a_i|<=U^2 by the determinant
formula. Sort their absolute magnitudes1<=a<=b<=A; at most48 sign/
permutation choices suffice. The two coordinate rows of u0,u1 lie
in the congruence lattice a_signed x+b_signed y=0 mod A, of covolume A
since gcd(a,b,A)=1. They are independent because u0,u1 are nonparallel.

Here is the needed boundary-free lattice fact. If a symmetric convex
body B in the plane contains two independent lattice vectors, choose
a primitive lattice v in B and an independent w in B. Extend v to a
basis(v,b0), write w=zv+k b0, and adjust b0 by an integer multiple of
v so b0=w/k-theta v with |theta|<=1/2. Its B-gauge is at most3/2.
The centered fundamental cell is contained in(5/4)B. Disjoint cells
around lattice points of B lie in(9/4)B. Consequently

    |Lambda cap B| det Lambda <=(81/16)area(B).

Apply this to the rectangle of half-widths R/a,R/b. If it has no
independent vectors there are no admissible triples; otherwise the
number of coordinate-row pairs is at most441R^4/(a^2b^2A^2).
The relation and ||u_i||<=U imply ell<=2bU, using the SECOND largest
coefficient, rather than AU. Dyadic summation of1/ell^2 contributes at
most40000U^2/(a^2A^2) per signed coefficient vector: the bin ending
at R contributes at most1764R^2/(a^2b^2A^2), and the sum of squared
dyadic endpoints through2bU is at most22b^2U^2.
Sum over a<=b<=A<=U^2: sum_a sum_b1/a^2<=2A and
sum_(A<=U^2)1/A<=1+2log U. Multiplying by48 gives3840000, below (8).

For each left triple, every off-left matrix triple is uniquely
M_i=a_i u_i w^T with nonzero integer w, so its exact number is
|B_(floor(X^2/ell^2))|-1. The disk count is <=9X^2/ell^2; summing
proves (5). Here B_q denotes the integer disk of squared radius q.
This is a paper proof, not a fit of the finite data. Direct four-coordinate
controls at (X,U)=(4,2),(6,3),(8,4) corroborate the exact count formula.

## 5. Profile matching: a deterministic window theorem

There is a broader sufficient class. For W subset F_p^2 define

    sigma(W)=p^(-2) sum_xi |sum_(z in W) exp(2pi i xi.z/p)|.

Fix rho0>0,B>=1 and 0<=delta<1/2. In each direction choose ANY
p_u-point cyclic Sidon set C_u and ANY window W_u with

    |W_u|>=rho0 p_u^2, sigma(W_u)<=B p_u^delta.

The windows may depend on the actual curves and need have no prescribed
shape. Take P_u=C_u cap W_u and lift into the p-box before taking
differences. Then, under the same kernel gap, EVERY deterministic
assignment satisfies

    n=Theta(X^2 log X), M(A)>=c(rho0,delta) sqrt(n)              (B)

eventually. The threshold may also depend on B. This is a sufficient
complexity range of this proof, not a claimed sharp boundary or a
classification of arbitrary windows.

Here are the additional details. The common actual/reference template is
V_W(theta)=p^(-1)sum_(z in W) exp(iz.theta). Fourier multiplication on
F_p^2, separating the zero character of C, proves at each p-grid point

    |F_(C cap W)-V_W|<=sqrt(2p) sigma(W),
    ||C cap W|-|W|/p|<=sqrt(2p) sigma(W).                      (9)

Complete the first bound by Lagrange interpolation to gain only L_p^2.
The reference is a uniform affine parabola C' intersected with the SAME
W, then trimmed or padded WITHIN C' to the actual cardinality k. There
are enough points since k<=p. The adjustment is at most3sqrt(p)sigma(W)
points. Consequently both actual and adjusted-reference residuals to
V_W are bounded by R=5sqrt(p)sigma(W)L_p^2 on the whole torus.
Both are Sidon subsets, so their L4 bounds persist. Also
||V_W||_4^4<=|W|^3/p^4<=p^2, simply by counting window additive quadruples.
Equation (3) now gives the PAIRWISE bound

    H_u<=5200p_u^3 sigma(W_u)^2 L_(p_u)^4.                     (10)

The proof of (3) applies unchanged to equal-cardinality Sidon subsets
of at most p points, with D=|F|^2-k: it only uses the displayed L4
bounds and D<=|F|^2, not k=p.

For correlation, affine two-transitivity gives probability1/[p(p+1)]
that a specified distinct pair belongs to a uniform affine parabola.
Before adjustment, the mean coefficient at integer displacement w is
N_W(w)/[p(p+1)], no greater than the full-box triangular coefficient.
Since k>=rho0 p/2 eventually, the actual signed support has at least
rho0^2 p^2/8 entries. Coefficients>1-epsilon, epsilon=rho0/16, lie
in |w_j|<epsilon p; this box has at most4epsilon^2 p^2+4epsilon p
nonzero integer points, less than half that support for large p.
Thus a_pre>=epsilon n_u. The adjustment changes at
most2pr<=6p^(3/2)sigma(W)=o(p^2) signed differences. Therefore
a_bar_u>=rho0 n_u/32 eventually, uniformly. This avoids assuming a cardinality
concentration theorem or silently retaining unequal reference sizes.

Choose eta with 2delta/(1+2delta)<eta<1/2 and freeze the reference below
X^eta. The retained cardinality is a positive fraction of n, uniformly
in actual choices, by prime/density comparison and the primitive count.
The high-direction left cost in (10) is at most

    C X^(3+2delta)(1+log X)^4 / X^(eta(1+2delta))=o(X^3).

The off-left term is O(X^3 log X) as in (5). Thus H_bar=o(n^(3/2)),
Q_bar=2a_bar, a_bar>=c1 n, and (7) proves (B). For polylogarithmic
sigma(W), a polylogarithmic cutoff instead retains1-o(1) of n.
Rectangular windows and coordinate strips have sigma bounded by fixed
powers of log p, so this includes prefix, quadratic-arc, and joint
coordinate-window selections. No actual sampling law is imposed.
The initial U^4 count gave only delta<1/6. The lattice argument is
what permits the larger sufficient range. The endpoint delta=1/2 is
NOT settled: its cutoff would reach U and lose the required cardinality.

## 6. Why a fixed reference profile fails outside the first model

The proof does NOT justify using the full-box reference indiscriminately.
Let k=(p-1)/2 and P={(t,t^2 mod p):0<=t<k}. Reference sets are uniform
k-subsets of uniform full affine parabolas, so

    m=E D_reference = c_k(F_p(theta1)F_p(theta2)-1),
    c_k=k(k-1)/(p^2-1).

For every odd prime p>=41 their conditional cubic satisfies

    H_bar(P)>=p^4/10485760000-p^3/4.                            (11)

Thus no Cp^3 log^4 p bound is possible for THIS mismatched law.
At (theta1,theta2)=(2pi/p,0), the actual exponential sum is exactly
D_k(2pi/p), whose modulus exceeds p/4. In the box of radius1/(64p)
in each coordinate it remains at least15p/64. Hence D_P>=p^2/40.
The reference mean is at most p^2/(16*64^2), since D_p vanishes at
2pi/p and its derivative is bounded by p^2/2. Jensen gives
E q^2>=(D_P-m)^2>=p^4/6400 there. Its normalized area exceeds
1/(40960p^2). This gives the p^4 term. Outside, use D_P>=-k and
E||q||_2^2<=2k^2 to subtract at most2k^3<=p^3/4.

Exact probes at p31/61/127/251/509 corroborate the mismatch: certified
conditional-cost lower bounds divided by p^3 are about
0.0511,0.1206,0.2214,0.4327,0.8744. These are LOWER bounds, not exact
conditional means or global Chowla minima. They are computed as

    H_bar>=integral D_P(D_P-m)^2-k*(k(k-1)-||m||_2^2).          (12)

The mean-matched horizontal reference reduces this cost. Matching only
the horizontal projection is insufficient for a quadratic-arc selection
I={t:2(t^2 mod p)<p}: its p251 conditional-cost lower bound is about
0.8477p^3. The appropriate window in (B) is the VERTICAL strip, not
that horizontal-index set. This is why the reference uses the actual
two-dimensional window and restores cardinality afterward.

## 7. Checks and strategy

All computation ran on Dirichlet. The finite cutoffs used exact squared
radii2 or4 and U=X^(1/3); they test certificate algebra,
not the asymptotic threshold. Four frozen-reference examples have exact
mixed lower ratios>0.2364,0.2516,0.2134,0.2453. The X64 four-coordinate
recount gives H=66498 and shows that frozen ACTUAL targets contribute520;
omitting them would be wrong. Larger cubics have independent correlation
and rational-certificate checks, not full four-coordinate recounts.

Independent exact small searches enumerate all normalized p-point cyclic
Sidon sets at p3/5/7 and find totals72/600/2352, all affine parabolas in
these finite cases only. No all-prime classification is inferred.
Off-grid192-bit checks corroborate completion bounds and fourth moments.
Two additional Boolean partial/windowed examples have full direct
four-coordinate recounts, exact rational lower certificates and square-
identity upper bounds, with concrete positive frequencies saved.
The sharp ruling count also has three direct four-coordinate controls
and451 independent-vector lattice cases. These validate the count
formula and normalizations, while the uniform U^2 log U estimate uses
the paper lattice proof rather than a finite extrapolation.

Data: `.research/experiments/sidon_cutoff_2026-10-20/`. Code:
`src/cstar_sidon_cutoff.py`, `cstar_sidon_cutoff_verify.py`,
`cstar_cyclic_sidon_probe.py`, `cstar_sidon_profile_probe.py`,
`cstar_sidon_profile_verify.py`, `cstar_sidon_partial.py`,
`cstar_ruling_triples.py`, `cstar_ruling_count_verify.py`.
The profile checker independently recounts p31 mean-cubics and the exact
p7 reference laws; larger FLINT convolutions have their variance/lower-
bound algebra rechecked, not independent full recounts. Review-agent
launches failed with the unavailable configured default model; no external
proof review, Lean check, or novelty claim is made.

**Decision.** Stop treating sharp Cp^3 cost or the uniform-marginal
restriction as required gaps in the full-size Sidon-fiber architecture;
(A) removes them by an adaptive certificate, and (B) covers a broad
windowed extension. Do not continue fitting conditional constants or
scanning those settled fixed-complexity models for counterexamples.
The universal arbitrary-support certificate is still missing. The next
model boundary is genuinely large Fourier complexity (delta>=1/2 is
unclassified by this argument), or point selections with no suitable
common spectral template. The U^2 log U off-left bound is proved; do
not leave U^4 or the earlier delta<1/6 restriction as the active frontier.
At the endpoint, point selections on a curve can change by a fixed
fraction while windows change in only O(p) cells, with Fourier norm
O(sqrt(p)); our cardinality correction can then be linear in p. The
next inverse test must distinguish a poorly matched template from
intrinsic high-complexity Boolean noise. Keep that endpoint task,
unrestricted mixed Boolean certificates, and non-cone growing-depth
PD/Riesz rounding as distinct active lines.

More precisely, any dense subset P of a cyclic Sidon curve C can be
written C cap W=P with W=(W0\C) union P, where W0 is a fixed dense
coordinate strip. This changes at most p cells. Parseval and Cauchy
give sigma(1_W-1_W0)<=sqrt(p), while sigma(W0)=O(log p). Thus the
endpoint sigma(W)=O(sqrt(p)) already contains arbitrary dense point
selections on the curve. The delta<1/2 theorem does not silently settle
that endpoint or the further arbitrary-frequency inverse problem.
