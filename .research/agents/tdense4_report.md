# T-dense round 4: adversarial audit and descent

## Final disposition

**CONJECTURED target, quoted.** For every C >= 1 there is c(C)>0 such that M(A)>=c(C)sqrt(n) for every nonempty set A contained in [1,Cn], n=|A|. The cosine convention is f_A(x)=sum cos(ax); circle measure is dx/(2 pi).

**PROVED scope of work.** This report and `tdense4_scratch/` are the only intended writes. All computation is performed through `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2`. No subagents, LP/MILP, commits, or changes to the shared root research notes are authorized or used.

**PROVED audit verdicts: P47 CONFIRMED-WITH-FIX; P53 CONFIRMED-WITH-FIX.** P47's finite argument survives the even-extension Abel estimate, the factor 96, energy pinning and the nonzero mean. Its asymptotic corollary needs the sufficiently small prefactor at D0 of order X^(3/4) or X^(1/4), a right-limit interpretation at t=0, and positive total variance. P53's joint Fourier argument survives; its unrestricted Bohr-window corollary requires joint regularity of the set in (t,omega), not merely Jordan measurability of each fiber. An explicit counterexample to the unrestricted corollary is below.

**PROVED new lemma, paper proof.** If h is a continuous real nonnegative positive-definite function on R times any compact abelian K, bounded by 1, supported on |t|<=1, then

    1-h(t,omega) >= t^2/4 for 0<|t|<=1.

Indeed let h0=h(0,e)<=1 and N=floor(1/|t|)+1, so h(N(t,omega))=0 and N<=2/|t|. In a Gram representation, the triangle inequality along N translates gives h0-h(t,omega)>=h0/N^2. Therefore h(t,omega)<=h0(1-1/N^2)<=1-1/N^2. This is uniform in K.

**PROVED consequence.** If m=integral_0^1 integral_K g>=1/C, then its P53 defect satisfies

    integral g(1-g) >= (1/4) integral t^2 g >= m^3/12 >= 1/(12 C^3).

The last inequality fills the earliest t first, since 0<=integral_K g<=1. This strengthens strict positivity to a uniform defect for exact macroscopic limits. The finite-X fixed-window theorem is proved below, including moving centers and near relations. The coupled delta^(-2)-window version is not established.

**PROVED obstruction / CONJECTURED remaining step.** Normalizing a mesoscopic twisted measure by H instead of X makes its total variation diverge, ruling out weak measure compactness. An explicit joint positive-definite profile system saturates the Bessel budget with zero residual, disproving the Bessel-only repair. Conditional mesoscopic positivity is proved; the missing height-uniform binary capture inequality HBCG is stated with complete quantifiers. T-dense is not proved.

**NUMERICAL and PROVED finite checks.** The VM work includes 4,260 rational window checks, three nonvacuous-numerator interval cases, 24 golden-ratio window sets with 1,044,480 certified membership decisions, 74 zoo sets, 30 mesoscopic diagnostics, and 304 capture-gap diagnostics on 76 sets. Numerical minima and energy integrals are not global certificates. All new theorems are paper proofs, without kernel checking or independent adversarial review. “New” means beyond the supplied record; external priority is unchecked.

## Task 1A: P47 verdict

**PROVED verdict: CONFIRMED-WITH-FIX.** The finite theorem is confirmed as written. The asymptotic corollary is valid with the qualifications below. Its finite input is quoted P31, not a new proof of Nikolskii's inequality.

**PROVED even-extension bound.** Extend beta by zero outside +/-[1,X], with beta_bar(0)=0. Every interval sum of beta_bar has modulus at most 2D0: on one side it is a difference of two original prefixes; across zero it is a sum of two prefixes. The normalized triangular kernel has total variation 2/(h+1). Abel summation therefore gives the stated bound 4D0/(h+1). The zero at the origin and the terminal zero extensions introduce no extra prefix error. The factor 4 is safe; no sign or factor-of-two defect was found.

**PROVED smooth-part bound.** The Fejer normalization is essential: ktilde(k)=(h+1-|k|)/(h+1)^2, whose mass is 1 and whose second moment is h(h+2)/6. Consequently H <= x^2 h(h+2)/12 on [-pi,pi]. With Phi=P1+2f_P, the identity for its second difference gives |Phi| <= Q2/(4 sin(x/2)^2). Since P1>=0, the subtracted term -P1 H/2 has the favorable sign. Combining these estimates gives U <= pi^2 h(h+2)Q2/96. At x=0, H=0 and the estimate is understood by continuity. Also U>=0 because H f_P vanishes there. No extrapolated value of P at index zero is needed or permitted in the theorem.

**PROVED mean and denominator.** G has mean gamma0/2, so the nonnegative polynomial is

    G + M + U = (G-gamma0/2) + mprime,
    mprime = M+U+gamma0/2 >= 0.

The last inequality follows by integrating this nonnegative polynomial, even if gamma0 is negative. P31 then gives the displayed inequality in mprime. Its denominator is strictly positive: the optimal degree-L Nikolskii factor R=rho_L(L+1) is at least the squared L2 norm of the degree-L Fejer kernel, which strictly exceeds W for L>w. Replacing rho_L by any certified upper bound preserves the argument. Taking the nonnegative square root and using gamma0<=delta gives the stated lower bound for M.

**PROVED binary energy.** For every index, beta^2=p(1-p)+beta(1-2p). Weighted Abel summation with prefixes bounded by D0 gives the two stated errors D0(1+2V) and D0(2+2V). For the latter, the Fejer-squared weight is nonnegative decreasing with variation at most 1, and |1-2p|<=1. The terminal model zero is already included in V. Since |beta|<=1 and delta<=1, (beta-conv)^2<=beta^2+2delta+delta^2<=beta^2+3delta. All the tails generated by convolution contribute nonnegative energy to E and are handled correctly.

**PROVED asymptotic fix and quantifiers.** Fix a BV, finitely piecewise C2 profile, theta in (0,1] with Gamma(theta)>0, and its right-hand endpoint convention. There are constants c0,c1,C1>0 and X0 depending on this fixed profile and theta such that, for all X>=X0 and all binary a with D0<=c0 X,

    M(A) >= c1 sqrt(X) - C1 (1+D0^2 Q2).

One can take h+1=max(2,ceil(48D0/Gamma)); w=max(1,floor(theta X)). For large X, the ceiling changes only harmless O(1) terms. The main normalized window gap is theta Gamma X^2. The delta errors cost at most

    theta X^2 delta [4/3 + 3 rho (1+theta)] + o(X^2),

and delta<=Gamma/12 leaves a positive fraction because theta<=1 and rho=4/(3 sqrt(3)). Taking c0 sufficiently small controls the h/X and D0/X errors. Here the constants depend on theta as well as p; writing c(p) is justified only after fixing a qualifying theta as a function of p.

**PROVED threshold qualification.** If p is Lipschitz and piecewise C2 with p(1)=0, then Q2=O_p(1/X). Thus D0=o(X^(3/4)) gives M>=c sqrt(X) eventually; D0<=d X^(3/4) also does so for a sufficiently small fixed d depending on the constants. An arbitrary prefactor in D0 asymptotic to X^(3/4) is not justified by this estimate. For finitely many jumps, replace the threshold by o(X^(1/4)), or a sufficiently small fixed multiple. These are sufficient conditions, not necessary ones.

**PROVED endpoint qualifications.** The small-theta limit uses e(0+), rather than an arbitrary assigned value e(0), and requires positive total variance. A profile equal to 1 only at t=0 and to 1/2 for t>0 refutes the unqualified use of p(0). The assertion that every p(0)=1 qualifies also needs total variance >0 and right continuity. For an affine start with nonzero right derivative the displayed first-order expansion is correct. Higher-order or flat starts still qualify by right continuity when e(0+)=0 and total variance is positive; no nonzero derivative is needed.

**PROVED finite validation.** `audit.py exact` exhausts all nonempty binary words at ambient X=1,...,6 against four rational models: zero, 1/2, 1-t, and (1-t)^2/2. It checks direct rational convolution, both energy pinning estimates, E and S bounds, the complete conservative P31 window inequality, and all h=1,...,100 kernel second-moment identities. There are 4,260 window instances, with no failed assertions. Their sufficient numerator Delta is never positive, so these cases alone are only an audit of the finite chain.

**PROVED nonvacuous interval validation.** `exact_extended` uses the exact cumulative rounding of 1-t with phase 1/2, h=128, theta=1/8, and X=1024,4096,16384. It computes the full convolution by rational prefix sums, uses Pbar0=P1 and exactly Q2=4/X, and encloses the final pi and square root with 128-bit Arb. The valid conservative Nikolskii choice is rho=1. The certified lower bounds at X=4096 and 16384 are respectively greater than 1.18568658269 and 5.75828057139; both are below independent Arb-certified point lower bounds on M. These verify actual positive instances of the finite sufficient inequality. They are not a claim to have certified any global numerical minimum. Exact data: `exact_checks.json`, `exact_extended.json`; execution logs: `exact_vm.log`, `extended_vm.log`.

**PROVED audit-source caveat.** The preexisting `src/e69_p47_audit.py` uses an extrapolated Pbar0=2P1-P2 in its numerical Q2 computation and actual coefficient energies rather than Eminus and Splus. Thus E69b is useful evidence for the filtered P31 identity but is not a literal test of every sufficient quantity in P47. The new rational checks use the definitions in P47.

## Task 1B: P53 verdict

**PROVED verdict: CONFIRMED-WITH-FIX.** The joint theorem, including its strict positive defect, is confirmed under its stated nondegenerate countable-group hypotheses. The unrestricted Bohr-window corollary is false as literally stated; impose joint regularity as specified below. The new explicit defect estimate in Task 2 strengthens the theorem.

**PROVED construction and quantifiers.** Regard Gamma as a discrete countable abelian group. Its dual K is compact metrizable, since it is a closed subgroup of the countable product of circles. The coordinate evaluation map is a homomorphism because Gamma consists of actual additive angle sequences modulo 2 pi, not just an informal list of peaks. For each nonzero theta, geometric summation on any interval gives

    |(1/X) sum_(sX<m<=tX) exp(i m theta_j)|
        <= min(t-s+O(1/X), 2/[X |1-exp(i theta_j)|]) -> 0.

Nondegeneracy is exactly what is needed for this implication. Tensor products of continuous t-functions and characters are uniformly dense, proving convergence of the full-integer measures to dt times Haar. The selected measures are dominated by those full measures; their weak limit consequently has density 0<=g<=1. Compactness gives a subsequence. Countability gives simultaneous twisted limits; there is no uncountable diagonal extraction. A fixed rational angle is allowed: the group can have torsion and K can be finite.

**PROVED use of P48.** P48 already allows arbitrary j-dependent angles. For every theta in Gamma, the limiting twisted measure is the corresponding coefficient of g; applying P48 separately to that sequence proves nonnegativity of the joint transform for every real y and every theta. Local uniform convergence in y follows from the uniformly bounded total variations and supports of the X-normalized measures. Applying the result to all countably many theta causes no extra assumption on the rate of nondegeneracy.

**PROVED Gaussian/Folner step with normalizations.** Enumerate Gamma. Finite boxes in the subgroup generated by the first r elements, enlarged sufficiently in their free directions and including their finite torsion component, give a sequence of finite sets F_r invariant in relative size under each fixed translation. Put

    psi_r(theta)=|F_r intersect (F_r+theta)|/|F_r|,
    P_r(omega)=|sum_(theta in F_r) chi_theta(omega)|^2/|F_r|.

Then psi_r has finite support, 0<=psi_r<=1, psi_r(theta)->1, P_r>=0, and integral_K P_r=1. For delta_r decreasing to zero, the inverse Gaussian is the nonnegative density

    k_delta(t)=exp(-t^2/(4delta))/sqrt(4 pi delta).

Using the transform with exp(i t y) and counting measure on Gamma, direct Fubini yields

    sum_theta psi_r(theta) integral_R Ghat(y,theta) exp(-delta_r y^2) dy
      = 2 pi integral_(R times K) h(t,omega) k_delta_r(t) P_r(omega) dt domega
      <= 2 pi.

Here h is the reflected g, 0<=h<=1. Both transforms on the left are nonnegative. Fatou on the product measure proves sum integral Ghat<=2 pi. No monotonicity of the Folner cutoffs is required. This establishes the exact integrability needed for inversion, rather than assuming it.

**PROVED inversion and binary contradiction.** The inverse absolutely convergent integral of Ghat/(2 pi) defines a continuous positive-definite h_c on R times K, agrees with h almost everywhere, and is bounded by 1. Fourier uniqueness can be checked one character at a time using ordinary real Fourier inversion, then compact-group character completeness. Full support of Haar times Lebesgue implies h_c is everywhere real, in [0,1], and zero for |t|>1. If g were binary almost everywhere, h_c would be binary everywhere. Its restriction to each line t mapped to (t,omega) would then be constant, hence zero by its support, contradicting mass >=1/C. For the harmonic-analysis framework, the primary source checked was Terence Tao's [Fourier transform notes, LCA section](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/), especially Plancherel and inversion. The Gaussian/Folner calculation above supplies the specific integrability proof used here.

**PROVED corrected Bohr-window corollary.** Fix an irrational alpha and a fixed measurable set B contained in [0,1] times the circle whose boundary has product measure zero and whose product measure is positive. Put A_X={m<=X:(m/X,{m alpha}) in B}. Joint equidistribution gives local pattern g=1_B and positive limiting density. If liminf M(A_X)/X were zero, a subsequence would satisfy P53 and its binary contradiction. Therefore there are c(B,alpha)>0 and X0 such that M(A_X)>=cX for every X>=X0. The same argument works for fixed finite-rank rotations on their orbit closure and fixed residue patterns with the corresponding product-boundary condition. The constant is family dependent. Windows [0,c(1-t)^k) and centered windows with fixed c in (0,1], positive integer k, meet the condition.

**PROVED counterexample to fiberwise Jordan measurability alone.** Choose rapidly increasing Singer sets S_j of size q_j+1 in [0,v_j-1], v_j=q_j^2+q_j+1, and their distinct positive differences B_j. Then n_j=q_j(q_j+1)/2 and M(B_j)<=(q_j+1)/2 by the exact square identity. Choose distinct primes X_j in (v_j,2v_j). Thus B_j is contained in [1,X_j-1], n_j>=X_j/5 eventually, and M(B_j)=o(X_j). For each rational t=m/X_j in lowest terms set E(t)=the whole circle if m is in B_j, and E(t)=empty otherwise. These assignments do not conflict, since the X_j are distinct primes; take E(1)=empty. At all other t set E(t)=[0,1/2). Every individual fiber is Jordan measurable, and its measure is 1/2 for almost every t. Nevertheless the resulting Bohr-window construction at X_j is exactly B_j, for every alpha. It has sublinear M. This disproves the literal fiberwise statement while preserving nonzero actual density. Its product boundary is not null, so it does not challenge the corrected statement.

**PROVED TD10 explanation.** On a fractional flat piece, the Sturmian pattern is binary on that piece; the curved pieces need not be binary. Thus the strict-defect part of P53 alone is not the stated reason TD10 follows. Joint continuity already rules out a nontrivial window in the compact variable for irrational slopes. More uniformly, the pointwise bound proved below gives g(t,omega)<1 at every t>0, so a positive-measure binary flat piece is impossible, including rational slopes. This supplies the missing precise implication. Existing P49 independently proves TD10 through its nonzero step transform.

## Task 2A: an explicit uniform macroscopic defect

**PROVED, NEW relative to the supplied record (external priority unchecked), QD-limit.** In every instance of P53,

    b = integral_0^1 integral_K g(t,omega)(1-g(t,omega)) >= m^3/12,
    m = integral_0^1 integral_K g >= 1/C.

In particular b>=1/(12 C^3), independently of Gamma, its rank, its torsion, and the rate of nondegeneracy. This removes the stated wrong-semicontinuity difficulty for exact macroscopic limits: the defect is not merely strictly positive.

**PROVED quantitative pointwise lemma.** Let h be any continuous real positive-definite function on R times a compact abelian group, with 0<=h<=1 and h(t,omega)=0 for |t|>1. For z=(t,omega), 0<|t|<=1, let N=floor(1/|t|)+1. A Gram representation has vectors v_z with inner products h(z-zprime). Since h is real,

    ||v_Nz-v_0||^2 = 2h(0,e),
    ||v_z-v_0||^2 = 2(h(0,e)-h(z)).

The N consecutive increments all have the latter norm, by translation invariance. The triangle inequality therefore gives

    h(z) <= h(0,e)(1-1/N^2) <= 1-1/N^2 <= 1-t^2/4.

This also handles h(0,e)=0, when h vanishes identically. The Gram representation can be constructed directly from the positive semidefinite finite matrices, so no additional spectral theorem is being assumed.

**PROVED independent check of the pointwise inequality.** With P53's nonnegative spectral measure in hand, the elementary inequality 1-cos(Nu)<=N^2(1-cos(u)) gives the same bound after integration: h(0,e)-h(Nz)<=N^2[h(0,e)-h(z)]. Since h(Nz)=0, this reproduces the Gram argument and its constants.

**PROVED integration.** Apply the pointwise lemma to the continuous representative from P53. With p(t)=integral_K g and mass m, the bound gives

    b >= (1/4) integral_0^1 t^2 p(t) dt >= m^3/12.

For the second inequality, 0<=p<=1 and integral p=m imply integral t^2 p>=integral_0^m t^2=m^3/3. One direct proof integrates (t^2-m^2)(p(t)-1_(t<m)), which is nonnegative on both sides of m. This uses the exact [0,1] density bound supplied by the binary sequence. It is stronger than the continuity-only argument in P53 and also forbids any positive-measure region g=1 at t>0.

## Task 2B: QD with fixed finite observation complexity

**PROVED, NEW, finite-window theorem.** Fix C>=1, an integer J>=1, and a real K>0. For a set A contained in [1,X] with n>=X/C let

    Eout(A;J,K) = inf_(theta_1,...,theta_J)
        integral_(circle outside union_l {|x-theta_l|_circle<=K/X}) f_A(x)^2 dx/(2 pi).

There exist eta(C,J,K)>0 and X0(C,J,K) such that, for every integer X>=X0 and every such A with M(A)<=eta X,

    Eout(A;J,K) >= X/(48 C^3).

For the complex polynomial F_A=sum exp(iax), the corresponding residual is at least X/(24 C^3). The constants 1/48 and 1/24 allow a factor-two compactness margin; their limiting counterparts are 1/24 and 1/12. The proof establishes existence of eta and X0, but does not compute them. They are not claimed effective here.

**PROVED moving-center and degeneracy argument.** Merely citing P53 for the group generated by arbitrary moving centers would be invalid: a relation can have angle of order 1/X, violating its nondegeneracy assumption. The following repair handles every finite list of moving centers.

Suppose X_j tends to infinity and M(A_j)/X_j tends to zero. After a diagonal subsequence, for each integer vector k in Z^J the scaled principal argument X_j(k dot theta_j) either tends to a finite real b_k or has modulus tending to infinity. The finite case defines a subgroup N of Z^J, and b:N->R is additive. Extend b to a real linear functional on R^J, represented by a vector bstar. Replace the center coordinates by

    alpha_lj = theta_lj - bstar_l/X_j.

For k in N their scaled arguments now tend to zero; for k outside N they diverge. Let Kgroup be the subgroup of the J-torus annihilated by N. Fourier testing shows that the full-integer trajectory measures, now viewed in [0,1] times the J-torus, tend to dt times Haar on Kgroup. The selected measures have density 0<=g<=1 relative to this limit. The approximate trajectories need not lie exactly in Kgroup at finite j; their limiting measures do, which is all this argument needs.

For every character class in Z^J/N, P48 applies to the actual angle sequence k dot alpha_j. The character coefficients of the limit are independent of its chosen representative because relations in N have scaled error tending to zero. Thus the Gaussian/Folner proof of P53 applies to this limit. It gives the preceding explicit defect b>=m^3/12. This proves the required extension of P53 without assuming away near relations.

**PROVED energy passage.** On a fixed bounded y interval,

    2 f_Aj(theta_lj+y/X_j)/X_j
        -> 2 Re integral_0^1 q_[e_l](t) exp(i t(y+bstar_l)) dt,

uniformly. Centers in different character classes have scaled separation tending to infinity. Centers in the same class have finite scaled shifts; combine their intervals before integrating, rather than counting overlapping windows twice. Plancherel bounds the energy of the resulting finite union by the full real-transform energy of the distinct character coefficients. Consequently

    limsup captured cosine energy / X_j
        <= (1/2) sum_(all characters) integral_0^1 |q_theta(t)|^2 dt
         = (m-b)/2,

where n_j/X_j tends to m along the subsequence. Total cosine energy divided by X_j is m/2, so the residual is at least b/2>=1/(24 C^3). The complex version has no factor 1/2. A contradiction sequence with M/X tending to zero proves the finite-window statement with the stated margin.

**PROVED localized variant.** The same conclusion holds for a fixed finite family of continuous coefficient cutoffs psi_r(t) with sum_r psi_r(t)^2=1, allowing finitely many windows for each localized cosine polynomial sum a_m psi_r(m/X) cos(mx). Include all their center sequences in the same finite group. At each character the sum of the captured localized energies is at most integral sum_r psi_r^2 |q_theta|^2=integral |q_theta|^2. Thus the local t formulation does not change the fixed-complexity result.

**UNKNOWN coupled QD, exact quantifier distinction.** The theorem just proved is

    for each fixed C,J,K, there exist eta and X0.

The proposed QD asks for a delta with J up to delta^(-2), while assuming M<=delta X. Substituting J=floor(delta^(-2)) into an unquantified eta(C,J,K) is circular: no inequality eta(C,floor(delta^(-2)),K)>=delta has been proved. The explicit limiting defect alone does not give that rate. For fixed J one can absorb all finite exceptions by further shrinking eta, using M>=1/2. In the coupled formulation, shrinking delta also increases J; the same finite-exception argument therefore does not apply. The following examples identify a concrete finite-scale issue for that coupled definition.

**PROVED finite-scale obstruction to omitting X0.** Let S be a Singer Sidon set of k=q+1 integers in [0,q^2+q], and A its distinct positive differences. Then n=k(k-1)/2, M(A)<=k/2, and X=max A<=q^2+q. Put delta=k/(2X), J=floor(delta^(-2)). For sufficiently large q, J is comparable to 4X, so J windows of radius 16/X cover the entire circle, while M<=delta X and n>=X/2. Thus Eout=0 for this sequence of small deltas at the transition X comparable to delta^(-2). This is an exact square-identity obstruction, not a numerical counterexample to the fixed-complexity asymptotic theorem or to every possible height-qualified definition of QD. The finite checks in `finite_cover.json` retain concrete instances.

**PROVED height qualification caveat.** The fixed-window definition above intentionally permits arbitrary centers and therefore upper-bounds the energy any specified list of tall atoms can capture. If QD instead requires each window to contain a peak of height at least delta X, the circle-covering obstruction need not satisfy that extra requirement. The fixed-J result still applies; the coupled, height-qualified version remains unproved here.

## Task 2C: MP48, what survives and the exact obstruction

**PROVED conditional mesoscopic positivity.** Let H_j satisfy sqrt(X_j)<<H_j<<X_j, and suppose M(A_j)/H_j tends to zero. If a coherent profile r in L1[0,1] has been extracted at angles theta_j so that, for every real y,

    f_Aj(theta_j+y/X_j)/H_j
        -> Re integral_0^1 r(t) exp(i t y) dt,

then that real transform is nonnegative. The Hermitian extension of r/2 is consequently positive definite in the distribution sense. If r is uniformly bounded, the same Gaussian argument as P48 makes its transform integrable and gives a continuous positive-definite representative. More generally a uniform bound on the value at the joint identity is enough. Thus positivity itself survives at mesoscopic heights; the missing hypotheses concern extraction, boundedness, and transfer of binary information.

**PROVED exact failure of the raw P48 compactness argument.** The proposed H-normalized twisted measures are

    nu_j = (1/H_j) sum_(a in A_j) exp(i a theta_j) delta_(a/X_j).

Their total variations are exactly n_j/H_j, which tend to infinity for every dense sequence with H_j=o(X_j), irrespective of the angles. A weakly convergent sequence of finite complex measures on the compact interval has uniformly bounded total variation, by uniform boundedness on C[0,1]. Therefore these raw measures have NO weakly convergent subsequence. This is an unconditional obstruction to literally rerunning P48 with H replacing X. Distributional convergence on smooth test functions is a different, weaker possibility, and must not be called weak convergence of measures.

**PROVED noise qualification.** A bound O(sqrt(X)/H) for a specified fixed smooth test follows from an actual O(sqrt(X)) estimate for the remainder's twisted sum. Independent Bernoulli rounding gives such a variance bound for each fixed test, and a fixed number B of bins has the natural scale sqrt(BX)/H. Curved cumulative rounding has special exponential-sum estimates. For arbitrary binary sets no such decomposition or estimate has been proved. Uniformity over all continuous unit-norm tests is impossible by the preceding total-variation calculation. Describing a remainder as incoherent does not establish the estimate.

**PROVED L2 bounds do not restore the lost diagonal bound.** There are unbounded compactly supported L2 functions with nonnegative transform. For any 0<alpha<1/2, put

    h_alpha(t)=integral_(s=1)^infinity s^(alpha-1) (1-s|t|)_+ ds.

Each triangular integrand is positive definite, so its transform is nonnegative. Tonelli against test functions justifies this statement for the integral. For 0<|t|<1 it equals

    |t|^(-alpha)/[alpha(alpha+1)] - 1/alpha + |t|/(alpha+1),

and it is zero for |t|>=1. It belongs to L1 and L2, but diverges at zero. Its nonnegative Fourier transform is not integrable: the integral of the transforms of its triangular components is proportional to integral_1^infinity s^(alpha-1) ds, which diverges. Thus even an L2-extracted coherent profile need not enjoy the continuous bounded representative or bounded spectral mass that drove P53. This is a functional counterexample, not an admissible Chowla set.

**PROVED exact obstruction to the suggested Bessel-only transfer, NEW.** Individual positive definiteness, even joint positive definiteness, plus the proposed local Bessel budget do not force a positive residual. Here is an explicit formal profile system saturating the budget.

Fix d=1/8, let phi(t)=(1-|t|)_+, and set

    p(t)=[1-sqrt(1-4d phi(t)^2)]/2,
    a=1/(4 sqrt(J)).

On K=the J-dimensional torus prescribe q_0=p, q_(+e_l)=q_(-e_l)=a phi for l=1,...,J, and all other coefficients zero. Then for every t,

    p(t)^2 + sum_(theta!=0) |q_theta(t)|^2
       = p(t)^2 + 2J a^2 phi(t)^2 = p(t).

Every q_theta has a nonnegative real Fourier transform. For p, use the convergent expansion of [1-sqrt(1-4u)]/2 as a power series in u with nonnegative Catalan coefficients, together with positive definiteness of every power phi^(2r). The joint function

    h_J(t,omega)=p(t)+2a phi(t) sum_(l=1)^J cos(omega_l)

is also positive definite on R times K: all its Fourier-character components have nonnegative transforms. Nevertheless its formal defect integral p-sum |q|^2 is exactly zero. Its value at the identity is

    h_J(0,e)=p(0)+sqrt(J)/2,

which tends to infinity; it is negative at omega_l=pi when J is large. Thus it lacks exactly the pointwise condition 0<=g<=1 supplied by a genuine local binary pattern. The coherent atoms have amplitudes a tending to zero and there are order a^(-2) of them, precisely the mesoscopic bookkeeping proposed in the brief. This is a rigorous counterexample to deriving the needed defect from positive definiteness and Bessel alone, including their joint version. It is not a counterexample to T-dense or to a theorem that successfully retains the binary-pattern bounds.

**PROVED Bessel renormalization loss.** If a macroscopic coefficient q is written as (H/X)r, the exact budget becomes

    sum |r|^2 <= (X/H)^2 p,

rather than sum |r|^2<=p. For order (X/H)^2 atoms the budget can be saturated by the formal system above. Recovering a [0,1] joint density, with a bounded value at the joint identity, is new information; it does not follow by rescaling the original Bessel inequality.

## Task 2D: descent attempt and a single precise missing inequality

**PROVED strategic review.** The macro proof was strengthened and extended to arbitrary fixed moving windows, but its compactness parameters do not close the coupled QD quantifiers. The mesoscopic positivity step works conditionally, while raw measure compactness fails outright. The explicit saturating profile system then rules out the proposed repair using only positive definiteness and a quadratic Bessel budget. Repeating those two inferences would not advance the descent. The next useful target must keep the joint binary-pattern constraint at increasing frequency complexity.

**PROVED sampling reduction, NEW here as explicit bookkeeping.** For any real trigonometric polynomial f=f_A of degree X and H>0, select a maximal collection of points theta_l in {f>H} separated by 1/X on the circle. Their radius-1/X windows cover {f>H}. If J is their number, disjoint intervals I_l of length 1/X around these points give

    f(theta_l)^2 <= X integral_Il f(x)^2 dx + 2 integral_Il |f(x)f'(x)| dx.

Summing, applying Cauchy--Schwarz and using integral_circle f^2 dx=pi n, integral_circle (f')^2 dx<=pi X^2 n, yields

    J H^2 <= 3 pi X n.

This requires no individual spike-shape or derivative-flatness assumption. The selection can be made finite by circle packing; maximality gives the stated cover. It is therefore legitimate to use order Xn/H^2 frequency windows at height H.

**CONJECTURED single missing inequality, height-uniform binary capture gap (HBCG).** For every C>=1 there are constants c(C)>0 and B(C)>0 such that, for all sufficiently large X, every nonempty A contained in [1,X] with n>=X/C, every H>=sqrt(n), and every union U of at most ceil(3 pi Xn/H^2) radius-1/X windows whose centers satisfy f_A(theta_l)>H,

    integral_(circle outside U) f_A(x)^2 dx/(2 pi)
        >= c(C) X - B(C) X M(A)/H.

The constants must be independent of H, the number of windows, and their additive relations. This is a precise missing inequality, not a theorem established by the present report. A weaker asymptotic form restricted to M=o(sqrt(n)), H/sqrt(n)->infinity would suffice. A hypothesis H/sqrt(n)->infinity alone cannot replace all the uniformity requirements by invoking P48.

**PROVED conditional completion from HBCG and quoted P40.** If T-dense fails for some fixed C, take a sequence with epsilon=M/sqrt(n) tending to zero and let H=sqrt(n/epsilon). Then M/H=epsilon^(3/2), H/sqrt(n)->infinity, and the maximal separated cover above obeys HBCG. P40 gives

    integral_(f<=H) f^2 <= (sqrt(epsilon)+2 epsilon^2)n = o(X).

Since outside U is contained in {f<=H}, its energy is o(X), while HBCG gives at least c(C)X-o(X), a contradiction. Also H=o(X): M>=1/2 implies epsilon X tends to infinity in the dense regime. Thus the obstruction is exactly at mesoscopic heights, not at the already controlled top scale.

**PROVED novelty boundary and nonclosure.** HBCG is a uniform binary-energy transfer statement, close in strength to the inherited SB target. It is not advertised as a newly simplified equivalent theorem or as proved by the macro defect lemma. The result proved here covers its fixed-number-of-windows limiting regime. The formal profile counterexample shows why its joint binary content cannot be discarded. No sum over levels has been established: the same residual mass can witness every fixed-scale gap, so those gaps cannot simply be added or assumed to contract a parent at each level.

**HEURISTIC decision after the pivot.** Discontinue the literal H-normalized weak-measure descent and the Bessel-only defect transfer. Retain the explicit macro bound and the fixed-window theorem. The next discriminating mathematical step is a quantitative estimate retaining the [0,1] joint density as the number of near relations grows, or a concrete binary construction falsifying HBCG. Its crucial required gain is uniformity as J grows like Xn/H^2; an error proportional to J times M/X is too large, while the natural L2 error sqrt(J) times M/X is of order M/H. Turning that latter small L2 error into a bounded joint positive-definite pattern is precisely the unproved stability step, and the singular-profile example explains why it cannot be taken for granted.

## Numerical falsification and reproducibility

**PROVED protocol / NUMERICAL observables.** The script is `tdense4_scratch/audit.py`. Every computation was run on the requested VM with CPUQuota=200%, OMP/OpenBLAS/MKL threads=2, and at most 8 GB assigned memory. Jobs ran sequentially. No optimizer beyond scalar numerical minimization was used; no LP/MILP solver was invoked. The numerical full-circle FFT uses G=2^ceil(log2(64 max A)). Independent direct cosine evaluation refines the lowest grid neighborhood. This is not a certificate that all minima were found. Truncated integrals and window energies use floating grid quadrature. The largest relative Parseval error over the Bohr and zoo runs was 4.45e-16; the largest direct-versus-FFT error at the audited grid point was 3.68e-9. Python was 3.12.3 and NumPy 2.5.4.

**PROVED input provenance / NUMERICAL zoo.** The 74-set zoo retains exact integer arrays in `zoo_sets.json`. It includes the saved E67 optimized Bu/Singer sets, fresh calls to `src/e67_zoo.py bu(q)` at q=7,19,43, P42-type random Fejer-mixture realizations at ambient X=4096,16384,65536,200000, every E68 row in the round-3 snapshot, smooth TD12 cumulative-Bohr roundings, and random dense sets. The P42-type finite samples are mechanism tests, not instances of every enormous parameter bound in P42's existence proof. Reusing the saved arrays makes the snapshot reproducible even if the source JSONL files later grow. All generated and reused input arrays are saved; the existing source files were not appended to.

**NUMERICAL window diagnostic.** For each zoo set, greedy nonoverlapping frequency windows of radius approximately 8/X capture the energy of the complex polynomial F_A at 1,4,16,64 centers. These are heuristic lower bounds on the best possible capture, not upper bounds or a test of all center choices in QD. In particular they must not be confused with the cosine energy n/2 used by P40 and HBCG. The smallest observed beta1 was 0.13218623 (E68_e68_1), and the smallest refined R was 0.60618820 (E68_e68_14). No new construction record or certified global minimum is asserted.

**PROVED important Bu correction.** For every genuine Bu set A(S) of k(k-1) frequencies, the difference frequencies number n/2 and are divisible by 3; the sum frequencies number n/2 and are congruent to +/-1 modulo 3. Hence exactly

    f_A(2 pi/3) = n/2 - (n/2)/2 = n/4.

Thus the notebook claim that Bu has uniform local patterns at every fixed frequency is false for the displayed Bu construction. The macroscopic residue atoms must first be removed. This does not refute P53: their local pattern remains fractional and does not exhaust the budget. The chi-square mesoscopic description applies to the residual structure after the central and residue atoms, rather than to the entire spectrum.

**PROVED provenance clarification.** The earlier notebook's night-continuation T8 already records the same 3-adic bias |A intersect 3Z|=n/2. The residue calculation is a correction to the later uniform-pattern premise, not a new discovery of that bias. Likewise, the later statement that P31 is the h=0 case of the displayed smoothing-defect filter is false literally: H_0=1-K_0=0. P31 is a separate identity-filter case. P47 assumes h>=1 and does not rely on that notebook shorthand.

**NUMERICAL corrected mesoscopic diagnostics.** `meso` excludes neighborhoods of radius max(32/X,X^(-1/2)) about 0 and, for Bu sets, +/-2 pi/3. It then selects the highest remaining positive cosine peak and records H, M/H, and H-normalized twisted block averages for B=8,32,128. The radius is an explicit diagnostic choice, not a theorem isolating all macroscopic tails. Thirty sets are retained in `meso_checks.json` and `meso_sets.json`, including larger centered Singer/Bu sets q=61,127. The exact residue peak is checked by integer residue counts for every Bu row.

| NUMERICAL residual-peak example | n | X | H/sqrt(X) | M_grid/H | Energy fraction outside excluded neighborhoods |
| --- | ---: | ---: | ---: | ---: | ---: |
| Centered Bu, q=61 | 3,782 | 11,343 | 2.34493 | 0.15369 | 0.52705 |
| Centered Bu, q=127 | 16,256 | 48,765 | 2.43317 | 0.14130 | 0.51766 |
| P42-type realization, ambient 200,000 | 50,037 | 198,736 | 1.56797 | 0.94848 | 0.66667 |

**NUMERICAL limitation relevant to MP48.** At these sizes H/sqrt(X) is only a modest constant, and the normalized fine-bin noise is not small. For centered Bu q=127 the block-profile squared L2 means at B=8,32,128 are 1.11854,1.62841,3.88011, while the corresponding nominal random-noise scales are 1.16245,2.32490,4.64979. The P42 sample has M/H near one, so it does not test the asymptotic assumption M/H->0. These data support separating macro atoms and restricting the noise assertion to controlled tests; they do not validate an automatic vanishing-noise limit.

**PROVED Bohr membership / NUMERICAL minima.** The required Bohr-window test uses alpha=(sqrt(5)-1)/2, which is the golden ratio modulo 1, and p(t)=(1-t)^k/2 for k=1,2,4. Left windows are [0,p(t)); centered windows are the circle points with distance from zero <p(t)/2. Sizes are ambient X=2048,8192,32768,131072. All 1,044,480 membership decisions were checked individually with 128-bit Arb using the exact quadratic irrational and rational endpoints. Thus the saved arrays are certified to belong to the stated families. Their numerical minima and integrals remain uncertified.

| NUMERICAL family | M/X at 2,048 | M/X at 8,192 | M/X at 32,768 | M/X at 131,072 |
| --- | ---: | ---: | ---: | ---: |
| Left, k=1 | 0.136603 | 0.135434 | 0.135463 | 0.135383 |
| Centered, k=1 | 0.054677 | 0.054013 | 0.053988 | 0.053991 |
| Left, k=2 | 0.080475 | 0.080469 | 0.080269 | 0.080348 |
| Centered, k=2 | 0.038438 | 0.038140 | 0.037779 | 0.037778 |
| Left, k=4 | 0.048908 | 0.048297 | 0.048270 | 0.048347 |
| Centered, k=4 | 0.021490 | 0.020757 | 0.020589 | 0.020714 |

**NUMERICAL assessment.** These six fixed-parameter families show the predicted positive limiting scale for M/X. The corrected Bohr-window corollary supplies their qualitative linear theorem; the displayed constants are finite numerical observations, not the constants certified by that theorem. Data and exact sets are `bohr_checks.json` and `bohr_sets.json`.

**NUMERICAL falsification of HBCG.** For all 76 distinct named sets in the combined zoo and larger-Bu collection, `hcg` tests H=2,4,8,16 times sqrt(n), totaling 304 rows. It expands the entire sampled set {f>H} by radius 1/X; this contains any permitted center-window union, so its complement supplies a stronger residual diagnostic, subject to grid error. All five requested families are included. The smallest residual/X was 0.04006085, attained by E68_e68_16 at H=2sqrt(n). The smallest value of residual/X+M_grid/H was 0.12454104, attained by centered Bu q=127 at H=16sqrt(n), with residual/X=0.08732447 and M_grid/H=0.03721657. This is finite evidence compatible with HBCG (for example, the tested inequality with coefficients 0.12 and 1), not a universal choice of its constants. It does not test arbitrarily small epsilon or arbitrarily large scale counts. Full data: `hbcg_checks.json`, `hbcg_summary.json`.

**PROVED finite circle-covering checks.** For Singer positive-difference sets at q=7,19,43,101, `finite_cover` checks exact cardinality, density, the square-identity upper threshold delta=k/(2X), and 16J>pi X using pi<22/7. Every instance has enough windows to cover the full circle. For q=101, n=5151, X=10301, delta=51/10301, and J=40796. These are exact finite obstructions to forgetting the ambient-size qualification, rather than numerical counterexamples to the asymptotic fixed-window theorem.

**PROVED reproducible commands.** Run sequentially from the project root; the driver supplies Python, libraries, thread limits and copyback. Each writes only the assigned scratch data. The commands below use the final unified dispatcher; the logs for extended, meso, summary and hcg were produced by equivalent import-based entry calls before that dispatcher cleanup.

    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -m 6 -t 900 python .research/agents/tdense4_scratch/audit.py exact
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -m 6 -t 900 python .research/agents/tdense4_scratch/audit.py extended
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -m 8 -t 900 python .research/agents/tdense4_scratch/audit.py bohr
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -m 8 -t 1200 python .research/agents/tdense4_scratch/audit.py zoo
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -m 4 -t 300 python .research/agents/tdense4_scratch/audit.py finite_cover
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -m 8 -t 900 python .research/agents/tdense4_scratch/audit.py meso
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -m 4 -t 300 python .research/agents/tdense4_scratch/audit.py summary
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -m 8 -t 900 python .research/agents/tdense4_scratch/audit.py hcg
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -m 4 -t 300 python .research/agents/tdense4_scratch/audit.py verify

**PROVED finite artifact verification.** The final `verify` pass checks every retained set for positive integer entries, distinctness, cardinality and maximum against its diagnostic record, independently checks the Bu residue-count identity, and checks the saved finite-audit counts. `verification.json` records its result; `manifest.json` records SHA-256 hashes of the numerical data and final script. These are reproducibility and finite input checks, not proof certificates for the paper theorems or numerical global minima.

## Handoff: what changed and what is still missing

**PROVED, quoted and checked.** P31's window chain and P40's spike truncation remain the inputs. P47's finite theorem and P53's joint theorem survive. Neither is promoted to a proof of T-dense. P40's informal projection claim for 1_A itself is not used: the exact Fourier projection identity concerns the symmetric indicator of +/-A, as already corrected in the round-3 report.

**PROVED, new paper results.** The uniform bound b>=1/(12 C^3); a finite-X fixed-complexity residual theorem with cosine residual >=X/(48 C^3); treatment of arbitrary moving centers through the near-relation quotient; the exact raw-measure compactness obstruction; the joint positive-definite budget-saturating profile example; a counterexample to the unrestricted fiberwise Bohr corollary; and the explicit separated-window cover bound JH^2<=3 pi Xn. The exact Bu residue peak corrects an erroneous premise used in the brief's spectrum description. These claims have complete arguments above, but no independent proof review or kernel verification.

**CONJECTURED, exact remaining step.** HBCG, or an equivalent estimate retaining the binary pattern uniformly when J is of order Xn/H^2, would close the contradiction. Fixed-J compactness and positivity of individual coherent profiles do not do so. The coupled delta^(-2) version of QD is also not supplied by the proved quantifiers.

**HEURISTIC next discriminating work.** (1) Seek an L2-stable joint positivity statement with a retained identity bound and complexity dependence sqrt(J), testing the singular and budget-saturating examples first. (2) On the construction side, try to realize the formal saturated profile system by actual binary patterns; the required extra coefficients or negative values should expose either a counterexample mechanism or the missing transfer loss. (3) Keep the proven fixed-window theorem separate as a reusable obstruction for specified bounded-complexity constructions. Merely increasing the zoo or iterating an unchanged Bessel budget would not resolve the gap.

**PROVED completion boundary.** The requested proof audits, exact finite checks, numerical Bohr tests, and adversarial descent attempts are complete. The research outcome is a quantitative macroscopic theorem and rigorous obstructions to the proposed mesoscopic inferences, together with one precisely stated missing inequality. The full T-dense conjecture remains unproved in this report.
