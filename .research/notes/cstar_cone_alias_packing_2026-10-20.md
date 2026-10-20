# Plane tests, alias packing, and critical cone encodings

2026-10-20. DESIGN / ATTACK LOG. This pass attempts the nonseparated encoding left open by the preceding [integer-cone note](cstar_integer_cone_2026-10-20.md). The results below concern that construction class, not arbitrary Chowla supports. Paper proofs, direct finite certificates, and independent checks are labeled separately. No novelty, external-agent audit, or Lean verification is claimed.

## 1. Results and exact scope

Let X be a positive integer and let C be an integer 2-by-2 coefficient matrix. Define

    C_X={M in Mat_2(Z): rank M<=1, ||M||_F<=X},
    L_C(M)=sum C_ij M_ij.

Assume L_C is injective on C_X, including the zero matrix. From every nonzero pair {M,-M} take the positive absolute encoding, forming a genuine set A of distinct positive integers. Its cardinality is

    n=3X^2 log X+O(X^2),

as proved in the previous note. Dividing all entries of C by their common gcd preserves this injectivity and leaves the cosine minimum unchanged, so we normalize gcd(C_ij)=1 when using coefficient height.

For a nonzero integer pair v, call v/gcd(v_1,v_2) its primitive direction. Norms below are Euclidean.

**Theorem A: a long primitive direction.** If at least one row or column of C has primitive direction of norm greater than 47X, then for every X>=30,000,000,

    M(A)>=pi X^2/64 > X^2/32.

This is uniform in all entries of C and does not require separated place values or an upper bound for their height.

**Theorem B: comparable entries and small determinant.** Put H=max|C_ij|. Suppose, after primitive normalization,

    min|C_ij|>=H/10,     |det C|<=H.

If the encoding is injective on C_X, then Theorem A's lower bound holds for every X>=30,000,000. In particular the comparable positive matrices sampled here, with a,b,c of size H0 and d nearest bc/a, cannot give a counterexample family as X tends to infinity. Their large-scale front can be nonnegative; a different positive-measure test forces the negative value.

Since sqrt(n) is of order X sqrt(log X), these bounds force M(A)/sqrt(n) to diverge within the stated classes. This is an exclusion of a construction mechanism, not a universal Chowla lower bound.

A critical Chinese-remainder family below violates the determinant condition and has no long primitive row or column. Its injectivity is proved directly. It too fails, but by a different resonance, with M(A)>=n/100 eventually. Thus the long-direction proof is not being silently extended beyond its hypotheses.

## 2. Why almost-rank-one encodings were worth testing

The normalized Euclidean-cone front at a rank-one real phase matrix of singular value sigma is nonnegative. Parametrize the primitive direction by theta and a unit-disk point by polar coordinates (r,phi). After rotations the phase is sigma r cos(theta)cos(phi). The map

    (theta,phi) -> (theta+phi,theta-phi) mod 2pi

pushes Haar measure to Haar measure on the two-torus. With

    J0(t)=(1/(2pi))integral_0^(2pi) exp(i t cos u) du,

the front therefore equals

    2integral_0^1 r J0(sigma r/2)^2 dr >=0.

The circular integral is real. This gives positivity without relying on a special-function zero estimate. A direct rational series check corroborates the identity through order 12; the Haar calculation proves it at all orders and all finite sigma.

The angular front measure follows from primitive lattice-point counts in sectors, by the same Mobius inversion and harmonic summation as the preceding Euclidean cone count. In particular it is uniform in the angle, rather than concentrated on just a few primitive directions.

Comparable coefficient matrices with determinant O(H) approach rank one after division by H, so this removes a fixed-scale negative front along x=t/(HX). It does not imply positivity at the other angles of the scalar cosine polynomial. That was the substantive change from the separated encoding, not an assumption that the full minimum was controlled.

## 3. Injectivity gives a packing constraint

Let Lambda={T in Mat_2(Z):L_C(T)=0}. Every nonzero T in Lambda has ||T||_F>X. Otherwise split T into its first-row matrix M1 and the negative of its second-row matrix M2. Both have rank at most one and norm at most X, and L_C(M1)=L_C(M2), contradicting injectivity on C_X.

Thus distinct points of Lambda have mutual distance greater than X. Lambda lies in the three-dimensional Euclidean hyperplane perpendicular to C. Disjoint three-dimensional balls of radius X/2 centered at its points in a ball of radius 47X fit inside a ball of radius 47.5X. Therefore

    |Lambda intersect {||T||_F<47X}| <=95^3=857375.

No assertion that an individual solver-found vector is shortest is used here.

There is also an elementary height consequence. Put t=floor(X/2). The (t+1)^4 integer matrices whose entries lie in [0,t] have distinct encodings: a collision would give a kernel vector of norm at most 2t<=X. All encoded values lie in an integer interval of length at most 4Ht. Consequently

    (t+1)^4<=4Ht+1,     H>=X^3/64 for X>=4.

This holds after primitive normalization as well, since scaling does not affect injectivity.

## 4. A positive plane test with explicit unwanted terms

By permuting rows or transposing, a long row or column can be made the first row. These operations preserve the cone and its encoded frequency set. Write this row as (a,b), let m=32X, and put alpha=5/X. Use the nonnegative function

    mu(theta)=F_m(a theta-alpha) F_m(b theta),

where F_m is the Fejer kernel of mean one, with coefficients w_r=1-|r|/(m+1) for |r|<=m.

Its Fourier terms are indexed by plane matrices P(r,s)=[[r,s],[0,0]], weighted by w_r w_s exp(-ir alpha). Their norms are at most 32sqrt(2)X. A nonzero plane kernel vector has norm at least sqrt(a^2+b^2)/gcd(a,b)>47X. Thus only r=s=0 contributes to the mean of mu, so integral mu=1 exactly.

Let D_A=2f_A. The terms with 0<r^2+s^2<=X^2 form the main plane contribution

    H_main=sum w_r w_s cos(5r/X).

Other terms can occur because P outside the original cone can have the same scalar encoding as a matrix M in C_X. Call these alias pairs. Since the original cone encoding is injective, each plane index has at most one such M.

For an alias pair, T=P-M is a nonzero kernel matrix, with

    ||T||_F <=(32sqrt(2)+1)X<47X.

Its second row cannot be zero: that would make T a nonzero plane kernel vector shorter than 47X. Once this nonzero second row is fixed, a rank-one M has first row an integer multiple of the primitive direction of its second row. There are at most 2X+1 such first rows of norm at most X. Thus each kernel vector creates at most 2X+1 alias pairs, and

    number of alias pairs <=95^3(2X+1),
    |H_alias|<=95^3(2X+1).

The weights have magnitude at most one, so the last bound also controls their signed contribution. This is the reason a sparse encoding collision just beyond the cutoff does not by itself save the construction.

## 5. The negative main term and explicit constants

The unit-disk transform at radius five satisfies

    F_disk(5)<-1/8.

This follows from the rational even partial sum of its alternating series through degree 20; the exact fraction is saved in alias.json. The omitted tail is decreasing and starts with a negative term.

Here is a concrete lattice-sum error. Associate unit square cells to lattice points of the disk of radius X. Their union differs from the disk only in an annulus of width less than one, of area at most 4pi X. Within one cell the function cos(5x_1/X) differs from its center value by at most 5/(2X); there are at most 4pi X^2 cells. Including the boundary discrepancy, the error is less than 14pi X<44X. Excluding the origin only improves the upper bound. Hence

    sum_(0<r^2+s^2<=X^2) cos(5r/X)
      <=-pi X^2/8+44X.

For the Fejer weights, 1-w_r w_s<=2X/(32X+1)<1/16 on this disk. Its nonzero lattice count is at most pi X^2+10X. Therefore

    H_main<=-pi X^2/16+45X.

Combining with the aliases and putting K0=95^3 gives

    integral D_A mu <=-pi X^2/16+(45+3K0)X.

The elementary integer inequality

    3(30,000,000)>=32(45+3*95^3)

and pi>3 imply that, for X>=30,000,000, this is at most -pi X^2/32. Because mu is nonnegative of mean one,

    2min f_A <=integral D_A mu <=-pi X^2/32,

which proves Theorem A. This is an all-circle certificate from a positive measure, not a sampled minimum.

## 6. Comparable small-determinant matrices have a long direction

Normalize C to primitive entries, let L=47X, and suppose first that det C is nonzero. If both primitive rows have norm at most L, their gcds g1,g2 satisfy

    g_i>=H/(10L),
    0<|det C|=g1 g2 |det(primitive rows)|>=H^2/(100L^2).

Together with |det C|<=H this gives H<=100L^2. But injectivity gives H>=X^3/64, so

    X<=64*100*47^2=14,137,600.

Thus at larger X one primitive row is long.

If det C=0, a primitive integer rank-one C factors as u v^T with both integer factors primitive. Every nonzero primitive row is plus/minus v and every nonzero primitive column is plus/minus u. If none is long, H<=||u||||v||<=L^2, contrary to the same height lower bound once X>64*47^2. All entries are nonzero by comparability, so no zero-line exception is hidden. The threshold 30,000,000 covers both cases. Theorem B follows.

For the actual sampled class, raw a,b,c lie in [H0,2H0] and d is nearest bc/a. For H0>=10 its entries differ by less than a factor ten and |det C|<=a/2. Primitive normalization preserves both required inequalities. The theorem therefore applies to the full asymptotic class, not merely the 48 tested matrices.

## 7. The bounded comparable-encoding experiment

Seed 20261021 tested X=4,8,12,16 and H0=4X^3,16X^3. It accepted six collision-free encodings in each group: 48 accepted matrices, 27 rejected for zero frequencies or collisions. Each accepted set was checked with exact integer encodings. Root denominators came from entries, pair sums/differences, and the determinant. The weakest certified root bound among the twelve accepted cases at each X was respectively R>2.1709,4.2060,6.3400,8.1249.

One representative per X also received a finer FFT point search. FFT only chose an angle; Arb at the exact rational angle supplied the reported lower bound. A smaller grid bound than an earlier point bound is possible and is not interpreted as a global minimum.

The positive Fejer test was checked separately on those representatives. Its verified lower ratios were >0.5673,0.7675,0.7548,0.9054. Independent reconstruction grouped the unwanted terms into 34,34,20,30 kernel vectors, with 134,134,124,88 alias pairs respectively. Every group obeyed the 2X+1 bound. The mean of each test was one. Integer Gurobi solves located explicit collisions beyond the original cutoff, at radii about 1.68X,1.15X,1.84X,1.58X. Each vector and equality was checked exactly; they are not claimed to be shortest collisions.

All direct finite certificates are valid at their actual X, independently of the much larger conservative threshold in the uniform theorem. No finite search is promoted into the theorem's infinite quantifier.

## 8. A genuine escape from the determinant condition, and its CRT obstruction

It would be incorrect to infer a long primitive row from injectivity and comparable entries alone. For X divisible by four, put

    h=(3X/2+1,3X/2+3,3X/2+5,3X/2+7),
    P=product h_i,    C=(P/h_1,P/h_2,P/h_3,P/h_4).

These four odd integers are pairwise coprime: any common prime divides a difference 2,4,6, and the only possible odd prime 3 does not divide the first and fourth entries, the sole pair at distance six. The matrix C is primitive, has comparable entries, and

    det C=P(h_2h_3-h_1h_4)=8P,

which is larger than its coefficient height. Its primitive rows and columns are pairs of the h_i and all have norm asymptotic to (3sqrt(2)/2)X, well below 47X.

Nevertheless this encoding is injective, even on the full Euclidean ball of radius X. If L_C(T)=0, reducing modulo each h_i shows T_i=h_i k_i, and then sum k_i=0. A nonzero kernel vector has at least two nonzero coordinates, so its norm is at least sqrt(2)min h_i>2X. It cannot be a difference of two points of that ball.

The short primitive row directions do create plane kernel vectors just beyond the original scale, so origin aliases can occur in the Fejer rectangle. They cannot be discarded using the long-direction argument.

This removes the long-direction hypothesis in a real way. A different phase still blocks the construction. By CRT choose j modulo P with residues (0,1,-1,0). At theta=2pi j/P the rescaled coefficient matrix is exactly

    [[0,2pi X/h_2],[-2pi X/h_3,0]],

whose two singular values tend to 4pi/3. The disk transform is strictly negative on an interval containing that limit. The previous uniform fiber Riemann estimate and N~6X^2 log X therefore give

    f_A(theta)/n ->F_disk(4pi/3)<-1/50,
    M(A)>=n/100 eventually.

The stronger disk interval [4,44/7] and margin 1/50 were certified in the preceding cone pass. The four saved CRT witnesses use X=48,64,96,128 and n=32840,61928,150488,282112, with certified ratios >12.10,18.40,31.12,44.57. These are failed constructions, not new small-ratio records.

## 9. Verification and strategic decision

Code: src/cstar_cone_comparable.py, src/cstar_cone_alias.py, src/cstar_cone_alias_verify.py, src/cstar_cone_critical.py. Data: experiments/cone_comparable_2026-10-20/{results,alias,verification,critical}.json. Every computation ran on Dirichlet. Gurobi 13.0.3 was used only to locate short integer kernel vectors; exact arithmetic checked each reported witness. Arb point certificates use 96 bits, the plane producer 128 bits, and the independent grouping verifier 160 bits. Set hashes, all representative sets, coefficients, bounds, seeds and versions are retained.

The independent verifier checks the exact hypotheses on all 48 accepted inputs, reconstructs the four representative matrix sets, groups aliases by exact kernel vectors, checks their norms/multiplicities, and rechecks the positive-measure bounds. It also validates the CRT congruences, injectivity criterion, determinant identity, and failure of the long-direction condition in the escape family. These computational checks do not constitute an external audit of the asymptotic argument. A new independent-review launch failed because the configured default model gpt-daybreak-blue-latest was unavailable; independent-agent/Lean review has not been completed.

**Global review:** the previous turn was progress, with paper exclusions and exact sign/point evidence. This pass changed an actual encoding hypothesis, verified that the fixed-scale front obstruction disappeared, and derived a different arithmetic obstruction rather than relying on the finite search. It then tested a family outside the determinant hypothesis and found a separate CRT mechanism. Neither proof is a universal C* bound. The generic comparable almost-rank-one search should stop; merely increasing its height or sample size would repeat a now-excluded class. The CRT example shows that critical short directions need their own analysis, not that all such encodings are good or that the determinant condition can be omitted from Theorem B.

The universal adaptive-profile/coupled-certificate step still lacks a proof for arbitrary integer supports. The plane-packing argument uses a known complete rank-one configuration and cannot simply be asserted for the mesoscopic random-like spike sets in C*. No arbitrary-support bound, quantified counterexample algorithm, exhaustive impossibility, or ongoing unattended computation is claimed. The original full Chowla goal remains active.
