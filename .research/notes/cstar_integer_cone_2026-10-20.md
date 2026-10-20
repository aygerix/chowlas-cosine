# Integer rank-one cone: logarithmic count, forced arithmetic resonances

2026-10-20. DESIGN / ATTACK LOG, with a short CHAIN(c) identity. This is an attempted construction and a paper exclusion of its stated versions, not a universal Chowla theorem. Exact rational and ball checks are separate from the asymptotic proof. No novelty or kernel/independent-agent audit is claimed.

## Outcome

Let X be a positive integer. The nonzero integer rank-one 2-by-2 matrices have a logarithmic counting surplus. If their scalar encoding had negative minimum O(X), a count of order X^2 log X would offer a possible logarithmic improvement over the square-root scale. The following natural encodings fail much more strongly:

1. **Frobenius-ball cutoff.** Take every nonzero integer matrix M of rank one with ||M||_F<=X. Encode it by

       L_(R,S)(M)=M11+S M12+R M21+RS M22,
       S>2X, R>2X(S+1),

   and take the positive member of each encoded ± pair. There is an absolute X0 such that, for every X>=X0 and every pair of admissible integer place values R,S,

       n=3X^2 log X+O(X^2),     M(A)>=n/4000.

   The threshold is uniform in R,S. In particular this excludes every ordinary base encoding 1,B,B^2,B^3 with B>2X, not just one fixed or slowly growing base.

2. **Box cutoff at the smallest balanced base.** Take all nonzero rank-one M with |Mij|<=X, and use B=2X+1 and L(M)=M11+B M12+B^2 M21+B^3 M22. Then

       n=(48/pi^2)X^2 log X+O(X^2),     M(A)>=n/200

   for all sufficiently large X. Its obstruction uses a different resonance from the ball proof.

These are linear-in-cardinality negative minima for these model families. They rule out the desired construction mechanism; they say nothing comparable about every finite integer support. Nonradial direction-dependent windows, arbitrary nonseparated encodings, and genuinely different constructions are not excluded.

## 1. Booleanity and the exact count

Every nonzero integer rank-one matrix has a unique expression M=u w^T with u a primitive integer column vector whose first nonzero coordinate is positive, and w a nonzero integer vector. To select one member of {M,-M}, impose the same sign convention on w. Primitivity makes w integral by Bezout, and fixes the factorization uniquely.

The place-value inequalities guarantee injectivity on the full coordinate box, hence on the cone. If two matrices in [-X,X]^4 have equal encodings, write their difference as

    (d11+S d12)+R(d21+S d22)=0.

Both bracketed integers have absolute value at most 2X(S+1)<R. Thus each is zero. Since S>2X, each of the four differences is zero. A nonzero matrix cannot encode to zero. Positive absolute encodings of the canonical matrices therefore give distinct positive integers, with no multiplicities.

For the ball let P(T) count primitive vectors modulo sign with Euclidean norm at most T. Elementary Mobius inversion of the disk lattice count gives

    P(T)=(3/pi)T^2+O(T log(2T)),
    H(X)=sum_(primitive u modulo sign, ||u||<=X) 1/||u||^2
        =(6/pi)log X+O(1).

For each u the number of nonzero w in the disk of radius X/||u|| is pi X^2/||u||^2+O(X/||u||+1). Summing the errors gives O(X^2), since sum 1/||u||=O(X) and P(X)=O(X^2). Hence the symmetric matrix count is

    N_ball=6X^2 log X+O(X^2),    n=N_ball/2.

For the box put H=||u||_infinity. There are exactly 4phi(H) primitive signclasses at height H, and 4T(T+1) nonzero w with ||w||_infinity<=T=floor(X/H). Thus

    N_box=16sum_(H<=X) phi(H) floor(X/H)(floor(X/H)+1)
         =(96/pi^2)X^2 log X+O(X^2).

Here sum_(H<=X)phi(H)/H^2=(6/pi^2)log X+O(1), directly from the divisor formula for phi. The zero matrix changes the classical singular-matrix count by one only. The logarithmic box count is preexisting: Chapman–Mudgal explicitly state the h=0 asymptotic in their [introduction](https://arxiv.org/html/2509.20259v1). The elementary derivation above fixes our normalization and sign-pair convention.

## 2. A negative disk-transform interval, checked exactly

The normalized Fourier transform of the unit disk is

    F(t)=(1/pi)integral_(|z|<=1) cos(t z1) dz
        =sum_(k>=0) (-1)^k (t^2/4)^k/[k!(k+1)!].

The series follows by integrating the cosine series and the elementary even moments of the disk. It is also 2J1(t)/t, but no special-function zero estimate is needed.

Let P20(u) be the sum through k=20. For u in [5929/1600,49/4], the omitted alternating terms decrease in absolute value, so F(t)<=P20(t^2/4). Exact rational checks establish

    P20(u)+1/2000<0 on [5929/1600,49/4],
    hence F(t)<-1/2000 for 77/20<=t<=7.

Two independent finite algorithms verify the sign: SymPy's exact Sturm count is zero with negative endpoint value, and a standard-library rational Bernstein conversion gives all 21 coefficients negative on the entire interval. No floating approximation to a Bessel zero is involved. A narrower stronger interval F(t)<-1/50 for 4<=t<=44/7 is also checked in both ways.

The important geometric fact is the width 7-77/20=63/20>pi. It will dominate the quantization step forced by an injective separated encoding.

## 3. Mixed-place-value resonance for the ball

Fix X,R,S as in the theorem and write

    k=floor(S/X),    q=RS.

Choose an integer j congruent to -k modulo S with

    77/20 <= lambda1=2pi Xj/R <=7.

Such j exists: the interval for j has length (63/20)R/(2pi X)>R/(2X)>S+1. Alternatively choose the first member of this progression above the lower endpoint. Its phase increment is 2pi XS/R<pi, so it remains below 77/20+pi<7.

Also put lambda2=2pi Xk/S. If r=S/X>2, then floor(r)/r>=2/3 and at most one. Therefore

    4pi/3<=lambda2<=2pi,

which lies inside the same negative disk interval.

At the exact scalar angle x=2pi j/(RS), integer matrix entries permit reduction modulo 2pi. The rescaled coefficient matrix is

    Y=X Theta = [[lambda1/S, lambda1],[-lambda2,0]].

The lower-right entry is zero because RSx=2pi j, and the lower-left reduction follows from j+k divisible by S. Removing the upper-left entry changes Y in operator norm by at most 7/S=O(1/X), uniformly in both place values. For the remaining off-diagonal matrix, every unit u has ||Y^T u|| between lambda1 and lambda2. Thus every primitive-direction fiber has a negative disk transform, not merely an average over a favorable angular sector.

More precisely, for r_u=X/||u||, a two-dimensional Riemann-sum estimate gives

    sum_(0<||w||<=r_u) exp(i u^T Theta w)
      =pi r_u^2 F(||Y^T u_hat||)+O(r_u+1).

Its constant is uniform because ||Y|| is uniformly bounded. The disk transform is 1-Lipschitz, so every main term has normalized transform at most -1/2000+O(1/X). Summing over all primitive u gives

    D_A(x)/N_ball <= -1/2000+O(1/log X),

uniformly in admissible R,S. The symmetric exponential sum here is D_A=2f_A, and N_ball=2n, so D_A/N_ball=f_A/n. For all sufficiently large X this proves M(A)>=n/4000.

The first exploratory resonance used q=B^2+B+1 for ordinary bases. It reduced the matrix to [[1,B],[-B-1,1]] and produced a nearly isoclinic phase. The argument above removes the special identity R=S^2, so merely replacing geometric place values by independently chosen separated ones cannot evade the obstruction.

## 4. A changed cutoff really removes that first proof

For the box at B=2X+1, the limiting isoclinic phases from fixed numerators in q=B^2+B+1 are pi*j times a rotation matrix. The normalized box-fiber transform then includes sinc(pi*j), which is zero. Thus the disk's negative-annulus argument does not automatically exclude this changed model. This was the reason for a separate test rather than declaring all cone windows impossible.

The finite scan instead found the stable pattern

    q=B^2+3B+1,    j=2B+5.

Using B^2=-3B-1 and B^3=8B+3 modulo q, then subtracting integer multiples of 2pi from the coefficient entries, gives

    X Theta -> pi [[2,-1],[1,-2]]

as X tends to infinity. This is a non-isoclinic phase; it survives the sinc-zero alignment that blocked the first proof.

## 5. Box profile and a negative limiting integral

Primitive directions of max-norm height H lie on two projective pairs of square faces. For any fixed bounded phase matrix Y, their limiting angular average is

    Phi_box(Y)=(1/4)integral_(-1)^1 [
      sinc(Y11+Y21 t)sinc(Y12+Y22 t)
      +sinc(Y11 t+Y21)sinc(Y12 t+Y22)] dt,

where sinc(z)=sin(z)/z with its continuous value at zero. At the matrix above the two products coincide by evenness, giving

    Phi=(1/2)integral_(-1)^1
         sinc(pi(2+t))sinc(pi(1+2t)) dt.

Here the singularity-looking points are removable. A direct elementary sign proof is available. Define Si(y)=integral_0^y sin(s)/s ds. Product-to-sum and partial fractions give

    Phi=[I-S]/(12pi^2),
    I=integral_1^3 [cos(pi s)-cos(3pi s)]/s ds,
    S=Si(pi/2)+2Si(3pi/2)+Si(9pi/2).

Now I<=2log3<12/5. Concavity of sin on [0,pi/2] gives Si(pi/2)>=1; pairing the adjacent positive and negative quarter waves gives Si(3pi/2)>=1. For completeness,

    Si(2pi)>=pi/2-pi^3/144-1/pi
             >31/20-(22/7)^3/144-10/31>1.

This uses sin(s)>=s-s^3/6 on [0,pi/2], a lower bound for the positive half-quarter, and the negative-lobe bound 2/pi. Pairing successive full positive/negative lobes shows Si(4pi)>=Si(2pi), and the next quarter is positive, so Si(9pi/2)>1. Consequently S>=4 and, since pi^2<10,

    Phi < (-8/5)/(12pi^2) < -1/75.

A separate 256-bit calculation expands both entire sinc factors through degree 80, integrates their polynomial product, and adds an explicit rational uniform remainder. It gives Phi<-1/25, with midpoint approximately -0.052409288048863245. The elementary weaker sign bound is sufficient for the theorem.

To justify the limiting profile, weighted sums over reduced residues satisfy

    sum_(a mod H, gcd(a,H)=1) g(a/H)
      =phi(H)integral_0^1 g(t)dt+O(tau(H)(||g||_infinity+TV(g))).

This follows immediately by Mobius inversion and a one-dimensional Riemann-sum bound. Multiplying by the fiber area O(X^2/H^2) and summing gives total angular error O(X^2), since sum tau(H)/H^2 converges. The box-fiber lattice error sums to O(X^2) as well. The rescaled phase converges with error O(1/X), so

    D_A(x)=Phi N_box+O(X^2),    N_box asymptotic to (96/pi^2)X^2 log X.

Therefore f_A(x)/n tends to Phi<-1/75, and M(A)>=n/200 eventually. This is an asymptotic paper argument, not an extrapolation from the finite ratios.

## 6. Adaptive-profile identity, and why it is not yet the universal step

Let eta_a=1_A(a), let 0<=p_a<=1 be finitely supported, and put n=sum eta_a, mu=sum p_a, V=sum p_a(1-p_a), q=D_A-D_p. Fourier orthogonality and eta_a^2=eta_a give exactly

    Q=||q||_2^2=2sum(eta_a-p_a)^2,
    a=integral D_A q=2sum eta_a(1-p_a),
    a=Q/2+V+n-mu.

In particular, if n-mu=o(n) and V>=c n, then a is macroscopic without an additional weighted p_a row. This improves the sufficient hypotheses of the previous forced-plateau certificate. Its extra weighted row was valid and supplied the sharper asymptotic a~2V, but was not needed merely for a square-root lower bound.

The identity does not construct p. Asking for a large-variance, mass-preserving p with ||D_A-D_p||_infinity=O(sqrt(n)) on arbitrary low-ratio sets still contains C*: for any such q,

    a<=||D_A||_1 ||q||_infinity<=2K||q||_infinity, K=2M(A).

Do not present that existence assumption as a new smoothing theorem. This led to the separate construction test above rather than another unproved profile reformulation.

## 7. Computation, scope, and review

All research calculation used Dirichlet. There are 12 certified ordinary-base evaluations, 24 independently chosen mixed-place-value evaluations, and 28 box-denominator probes. All are single exact root-of-unity evaluations enclosed by Arb, hence rigorous lower bounds for M. None is called a global upper certificate.

For the Frobenius cone the positive cardinalities at X=8,16,32,64 are 552,2776,13344,61928. At X=64 the ordinary B=129 test gives R>22.56; mixed encodings remain strongly negative. For the box the cardinalities are 1184,5440,24128,109248. At X=64 the fixed q=B^2+3B+1, j=2B+5 witness gives R>15.58. These are failed constructions, not improved Chowla records.

Exact rational Bernstein signs independently reproduce both Sturm disk certificates. Direct four-coordinate enumeration at X=2,4,8 agrees with the primitive parameterization and with the box encoding. The Boolean variance identity is checked on all 32 indicator vectors for a fixed rational five-frequency profile; its all-size proof is the displayed algebra. Rational bounds used in the elementary Si argument are checked independently. The cone-limit counting and resonance proofs have not received independent-agent or Lean review; separate-agent execution remains unavailable with the configured default model. No external audit is claimed.

Code: src/cstar_integer_cone.py, src/cstar_integer_cone_mixed.py, src/cstar_integer_cone_box.py, src/cstar_integer_cone_box_limit.py, src/cstar_integer_cone_verify.py. Data: experiments/integer_cone_2026-10-20/{results,mixed,box,box_limit,verification}.json. Inputs, seeds (none), exact roots, set hashes, precision, and software versions are saved. All jobs are terminal.

**Strategic decision:** stop the unmodified integer rank-one ball construction, every separated product encoding of it, and the box construction at B=2X+1. Changing from a ball to a box removed the first resonance but did not remove all resonant negative profiles. The extracted mechanism is a band-edge sign obstruction at explicitly constructible arithmetic phases, not a generic scalar-moment obstruction. Direction-dependent nonradial tapers or encodings outside the stated separation hypotheses remain untested; no general impossibility is asserted. The universal adaptive-certificate step and full Chowla remain open. The original active goal is preserved.

**Subsequent continuation:** the comparable nonseparated small-determinant class is now excluded by a [positive plane test and alias-packing argument](cstar_cone_alias_packing_2026-10-20.md). An explicit critical CRT encoding outside that determinant condition was tested and excluded by a separate phase. These do not classify all nonseparated encodings or all tapers.
