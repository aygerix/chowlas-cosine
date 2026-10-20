# Boolean radial realization and a mesoscopic shell obstruction

2026-10-20. DESIGN / CHAIN(c) / ATTACK LOG. Previous goal turn: progress, with a full finite-cone concentration spectrum and an explicit fractional radial escape from rotational averaging. This continuation actually realizes that profile by zero/one coefficients at the macroscopic scale, then tests its mesoscopic signs. These are model results, not full Chowla. No novelty or external/Lean audit is claimed.

## 1. Varying marginals: an exact coefficient-integrality estimate

Retain the [previous full-spectrum notation and proof](cstar_cone_confinement_2026-10-20.md): Q={det=0} in Mat_2(F_p), p odd prime, and unitary Fourier transform on F_p^4 with counting l2 norms. The full concentration operator has eigenvalues 1,1/p,1/p^2. Its 1-space W is spanned by the two families of maximal rank-one planes; in particular every member of W is constant on each nonzero scalar line.

For ANY prescribed real profile b:Q->[0,1] and ANY Boolean eta:Q->{0,1}, write e=eta-b. The origin may be arbitrary. For a scalar line with l=p-1 entries b_1,...,b_l define

    D(b)=min_(epsilon in {0,1}^l) sum_i |epsilon_i-b_i-mean(epsilon-b)|^2.

Then the preceding spectral theorem gives the deterministic estimate

    ||1_(outside Q) F e||^2 >=(1-1/p) sum_(scalar lines) D(b_line).

Proof: projection onto the within-scalar-line zero-sum space is orthogonal to W; its squared norm is the sum of those line variances. No independence, matching-cardinality, constant radial marginal or rounding distribution is assumed. The bound discards the other nonnegative spectral contributions; it need not be sharp for a whole-cone optimization.

There is an exact finite formula. Order b_(1)>=...>=b_(l), put S=sum b_i and B2=sum b_i^2. For fixed k ones, the least variance is obtained by the k largest entries, hence

    D(b)=min_(0<=k<=l) [B2+k-2sum_(i<=k)b_(i)-(k-S)^2/l].

If max b-min b<=1/2, this simplifies to

    D(b)=sum_i (b_i-mean b)^2.

Indeed the difference between the k-term and the zero-term is

    k(l-k)/l-(2/l)sum_(i<=k,j>k)(b_(i)-b_(j))>=0.

There is also the weaker coordinate-free lower bound

    D(b)>=(1/l)sum_(i<j) dist(b_i-b_j,Z)^2,

because epsilon_i-epsilon_j is integral and variance is the pairwise squared-difference sum divided by l. This identifies a genuine source of off-spike error for a varying radial profile, rather than assuming a variance/anti-concentration principle.

**Sign caveat with a precise countercontrol.** This is only an energy statement. In F_p^4 a punctured one-dimensional subgroup inside Q has unnormalized Fourier transform p*1_(its annihilator)-1, so its minimum is -1 while most of its nontrivial spectral energy can lie outside Q. Positive concentrated leakage exists in finite groups. The new estimate alone does not force a square-root negative value in Z; the band edge/torsion-free sign step remains necessary.

## 2. An exact Boolean family with the desired macroscopic profile

Let X=2^L. Use canonical primitive u in Z^2 (first nonzero coordinate positive), and define its dyadic shell by 2^k<=||u||<2^(k+1). Retain only shells

    ceil(L/4)<=k<floor(3L/4).

Let v_b(k) be the radical inverse of the nonnegative integer k in base b, and define the RATIONAL center

    T_k=(2v_2(k)-1,2v_3(k)-1).

For T in R^2 define the symmetric lens

    K_T={z:||T+z||<=1 and ||T-z||<=1}.

It is empty if ||T||>1, convex, symmetric under z->-z, contained in the unit disk, and has perimeter at most 2pi. For every retained u, put R=X/||u|| and keep ALL nonzero integer w with w/R in K_(T_k). Take M=u w^T and one member of each sign-pair. The primitive factorization is unique, so this is a genuine zero/one matrix support.

Membership is exact integer arithmetic. If T=(a/q,b/q), d=||u||^2, and w=(r,s), define

    Z=X^2(q^2-a^2-b^2)-d(r^2+s^2)q^2.

Then w is selected exactly when

    Z>=0 and Z^2>=4X^2q^2 d(ar+bs)^2.

No floating comparison or uncertain boundary selection is used.

**Cardinality and fixed-phase theorem (paper proof).** Let n_L count the sign-pairs. Then

    n_L~(3pi/32) X^2 log X.

For every FIXED real 2-by-2 matrix Y,

    (1/n_L) sum_(canonical M) cos(<Y,M>/X)
      -> (1/(2pi)) integral_0^(2pi)
             F_disk(||Y^T v_theta||/2)^2 dtheta >=0,

where v_theta is a unit vector and F_disk(t)=2J1(t)/t, defined at zero by continuity. This is a nonnegative front realized by actual Boolean coefficients, not merely by a fractional mean. It is not uniform as Y grows with X, and it does not bound the global minimum.

Here is a proof with the needed normalizations. The simultaneous radical-inverse sequence is equidistributed in [0,1]^2 even over sliding consecutive intervals of length tending to infinity: a base-2 cylinder and a base-3 cylinder prescribe one residue class modulo 2^a3^b by CRT. Its count in any such interval is length/(2^a3^b)+O(1). Approximation by cylinder rectangles proves the assertion for continuous functions. The lens integrals are continuous in T, including empty lenses, by L1 continuity of disk translations.

The primitive harmonic measure of each large dyadic u-shell tends uniformly in angle to (6log 2/pi) times uniform angular measure. This is the same elementary sector count/Mobius summation used in the [previous cone count](cstar_integer_cone_2026-10-20.md); its error is O(k2^(-k)) for bounded Lipschitz angular tests. Uniform convex-boundary lattice comparison in each w-fiber has error O_Y(R+1). Summing those fiber errors gives O_Y(X^(7/4)); the angular primitive-count errors contribute O_Y(X^(7/4)log X). Both are o(X^2 log X). The number of active shells is asymptotic to L/2.

For T uniformly distributed on [-1,1]^2,

    E_T 1_(z in K_T)=(pi/4)rho(||z||),
    rho(r)=(2/pi)[arccos r-r sqrt(1-r^2)] on [0,1].

Equivalently set A=T+z, B=T-z; the Jacobian from (A,B) to (T,z) in four dimensions is 1/4. Thus the averaged lens transform is

    E_T integral_(K_T) exp(i xi.z) dz
       =(pi^2/16)F_disk(||xi||/2)^2.

The expected lens area is pi^2/16. Multiplying by (6log 2/pi) X^2, by L/2 shells, and dividing by two for sign-pairs gives exactly 3pi/32. The same argument gives the stated fixed-Y transform limit. This realizes the fractional escape recorded in the preceding pass without claiming any control at mesoscopic Y=Y(X).

## 3. A uniform negative Fourier value for every symmetric lens

The Boolean lens has a sign feature that its averaged radial profile loses. Rotate T to (t,0), 0<=t<1, and set b=sqrt(1-t^2). At frequency perpendicular to T with magnitude 2pi/b,

    integral_(K_T) cos(2pi z_2/b) dz < -|K_T|/64.

To prove it, the integral equals

    4b integral_0^1 g(y)cos(2pi y)dy,
    g(y)=sqrt(1-b^2 y^2)-t.

Twice integrating against (1-cos(2pi y))/(4pi^2) gives

    integral_0^1 g(y)cos(2pi y)dy
      =-(b^2/(4pi^2))integral_0^1
          (1-cos(2pi y))/(1-b^2 y^2)^(3/2)dy
      <=-b^2/(4pi^2).

At t=0 the endpoint derivative is unbounded, but the boundary term vanishes and the displayed weighted integral converges; truncation justifies the same identity. Thus the unnormalized transform is <=-b^3/pi^2. If t<=1/2, b^3>=9/16 and area<=pi, so its magnitude relative to area is >=9/(16pi^3)>1/64, using pi^3<32. If t>=1/2, g(y)<=b^2(1-y^2) and area<=8b^3/3, giving relative magnitude >=3/(8pi^2)>1/64. This proves a quantitative hard-boundary obstruction for every center, without importing a convex-body Fourier theorem.

## 4. Mesoscopic Fejer isolation kills the Boolean shell family

Encode the matrix support by four pairwise-coprime CRT moduli

    h=(6X^3)+(1,3,5,7), P=product h_i, C_i=P/h_i.

They are pairwise coprime because any common prime divides a difference 2,4,6; the only possible odd prime 3 does not divide the pair at distance six. The encoding is injective on the ball of radius X. Every nonzero kernel matrix has norm at least min h_i, since reduction modulo h_i forces its i-th coordinate divisible by h_i. This much larger separation will isolate a whole fiber.

If k=10 mod 12, then v_2(k) lies in [1/4,1/2), v_3(k) in [1/3,2/3), and ||T_k||^2<=13/36<4/9. In any 12 consecutive shells there is such a k. Choose the first at or above ceil(L/4), and u0=(2^k,1). For L>=64 this shell is active and

    R=X/||u0||>=X^(3/4)/2^13,
    |K_(T_k)|>=pi/9>1/3.

Use m=ceil(1024R) and the nonnegative product-Fejer measure

    mu(theta)=F_m((C^T u0)_1 theta-alpha_1)
              F_m((C^T u0)_2 theta-alpha_2),

where alpha=omega/R and omega is the perpendicular lens frequency in Section 3. Its Fourier indices are P=u0 w^T with |w_i|<=m. They satisfy ||P||<1500X. For X>=16 every nonzero encoding-kernel matrix has norm>1501X, so the mean is exactly one and NO other support fiber aliases into this test.

The integral H=integral D_A mu is therefore just the weighted discrete lens transform in the u0-fiber. For ||T||<=2/3, ||omega||<10. Convex boundary cells have discrepancy area at most 20R, and the within-cell phase error contributes at most 40pi R; a safe unweighted lattice error is 200R. The lens lattice count is at most area*R^2+20R. Fejer weights differ from one by at most 1/512, yielding

    H<=-(7 area/512)R^2+201R
      <=-(7/1536)R^2+201R.

For R>=100000 this is <=-R^2/512. Since mu>=0 and has mean one,

    M(A)>=R^2/1024>=X^(3/2)/2^36

for L>=64. The latter lower bound uses conservative constants, not extrapolation from finite tests. The full cone count also gives n<=[2pi log X+2pi+20]X^2, so this family's Chowla ratio tends to infinity. It is NOT a counterexample despite its nonnegative fixed-matrix-phase limit.

This is the missed mesoscopic scale made explicit: a single early but nondegenerate shell can be isolated by a positive measure. Its negative contribution is invisible after division by n in the fixed-phase limit. The argument depends on the very separated CRT kernel; arbitrary scalar encodings are not excluded.

The fiber-isolation argument itself does not require a Halton assignment or any assumption on the OTHER fibers: whenever a rank-one support in the radius-X ball has its intersection with one primitive-u plane EQUAL to the complete lens fiber above, with ||T||<=2/3 and R=X/||u||>=100000, the same encoding gives M>=R^2/1024. Merely containing a lens inside a larger selected fiber is not sufficient. Thus a bounded-ratio construction of this lens type with n~X^2 log X must suppress all such fibers with ||u|| much smaller than sqrt(X)/(log X)^(1/4). This is a concrete necessary scale condition for the next construction, rather than a claim about every possible correlated taper.

## 5. Verification, limits and next decision

Producer scripts: src/cstar_radial_quantization.py and src/cstar_lens_shell.py. All research computation runs on Dirichlet. The line optimizer is checked by exhaustive Boolean enumeration at lengths 2 through 8; finite cone leakage uses exact rational matrices and a separate ambient FFT only as corroboration. The lens generator uses integer membership and exact collision checks. Floating optimization only chooses a rational CRT point; ball arithmetic supplies a rigorous lower bound for M. The independent positive-Fejer measure is a separate lower certificate. Neither is a global upper bound.

The bounded tests use seed 20261024 for 84 rational line profiles and 16 varying-profile cone cases at p=5,7, and seed 20261025 for the lens point probes. The lens supports have (X,n)=(64,2420),(128,14672),(256,95608), with certified point ratios greater than 6.4201,10.6327,18.6951. The separate exact-mean-one Fejer certificates give lower ratios greater than 0.1809,0.2960,0.4544. These are actual finite certificates; they are not presented as instances of the much later conservative L>=64 bound.

An independent program, src/cstar_radial_boolean_verify.py, exhaustively rechecks all 84 line minima, enumerates finite-cone points in a different order, and recomputes all 16 rational leakage inequalities. It reconstructs the three integer supports in reverse factor order, uses a ceiling-square-root membership decision rather than the producer's squared comparison, matches every set hash, and re-evaluates direct four-residue phases and positive-Fejer tests at 192-bit Arb. A separate incomplete-moment recurrence supplies seven validated lens-transform checks, including t=0 and t=99/100; these corroborate rather than replace the all-t curvature proof. Exact rational checks validate the constant inequalities; finite shell checks L=64,...,256 corroborate the all-L index argument.

Reproduce:

    src/dirun.sh -c 2 -m 4 -t 180 python src/cstar_radial_quantization.py
    src/dirun.sh -c 2 -m 8 -t 240 python src/cstar_lens_shell.py
    src/dirun.sh -c 2 -m 8 -t 240 python src/cstar_radial_boolean_verify.py

Data are experiments/radial_boolean_2026-10-20/{quantization,lens,verification}.json, including exact profiles, masks, shell centers/counts, hashes, cardinalities, maximum frequency, rational bounds and verifier versions. All jobs are terminal. The fresh required reviewer launch failed with configured default model gpt-daybreak-blue-latest unavailable; no independent-agent or Lean audit completed.

The nonnegative macroscopic front, the varying-marginal leakage theorem, and the mesoscopic exclusion are paper arguments with distinct scopes. The macroscale result does not imply a uniform global bound. L2 leakage does not by itself imply a negative value. No independent-agent/Lean audit or priority claim is made.

**Strategic review.** The promised Boolean radial realization was attempted rather than left as a fractional wish: it exists at the fixed front scale, but the explicit shell implementation has a proved larger negative excursion. Stop this Halton shell family under the stated encoding. The next construction must distribute its center choices WITHIN each short-u shell or remove every large coherent fiber, while preserving the marginal; merely averaging O(log X) whole-fiber choices is insufficient. On the proof side, the varying-marginal integrality bound is usable but still needs a torsion-free sign mechanism. Keep the unrestricted adaptive certificate and growing-depth non-cone PD rounding lines active. Full Chowla and the original goal remain open.

A concrete next falsification target is to move the smallest retained direction above sqrt(X), making every individual fiber size O(X), below sqrt(n) by a logarithmic factor. This escapes the present single-fiber proof, not Chowla. Before optimizing such a family, derive the fluctuations at a zero of the squared-disk mean transform: independent whole-fiber centers may amplify noise at the scale sqrt(sum R_u^4), rather than sqrt(n). That is an unproved next estimate, not a claimed negative-minimum theorem for every correlated assignment.
