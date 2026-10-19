# Round 11 research report

PROVED scope and rules: f_A(x)=sum cos(ax), M(A)=-min f_A, n=|A|, X=max A. This round edits only this report and `.research/agents/tdense11_scratch/`, makes no commits, and launches no subagents. All mathematical computation runs through `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4`; every LP/MILP/QP uses Gurobi. No LaTeX artifacts.

## Current checkpoint

PROVED round-11 result: D<=259/2000, independently verified, hence T-dense(C) for every fixed C<2000/259=7.722007722... . The requested bounded push improves P62's 7.501875... but does not reach 8. PROVED Task 2 partial results: a quantitative order-X repair-energy obstruction for Gaussian escapes; the total rational-atom budget; a precise anchored-convolution DC barrier, realized by actual three-profile escapes; and the failure of both the positive and DC-deleted Paley packet variants. UNKNOWN/BLOCKED main alternatives: no positive-density four-profile escape and no uniform D4<D or a4<1/2 inequality has been established. No resolution of Chowla is claimed.

PROVED quoted baseline: P61 gives the exact second-order variational reach D; E82 estimates its reciprocal at 8.5708 (NUMERICAL). P62 constructs three matching raw profiles but its fourth moment diverges. Four matching binary raw profiles imply normalized coefficient L2 proximity to {0,1}; this supplies no rounding rate by itself. The brief's converse equivalence requires an additional tail condition, as detailed below.

PROVED source audit: read the brief, CLAUDE.md, the number-theory research skill and its three references, P58-P62, NOTEBOOK continuations 12-14, E82-E84, round-10 report, dirun.sh, and the round-10 discovery and two exact verification programs. No external novelty claim is made. Relevant PROOFS searches will precede each proposed new result.

HEURISTIC frontier and next discriminating tests:

| Known | Exact gap | Candidate mechanism | Test |
| --- | --- | --- | --- |
| D<=0.1333; numerical D about 0.1166747 | A certificate for D<1/8 | Long Chebyshev lines and third dilation | Gurobi discovery, then exact independent verification |
| Three profiles are free | Four profiles and a rounding rate | Correlated/PDS packets or binary-derived positivity | Compute fourth defect and minimum together |
| Higher anchored tests have a DC term | Exact scope of the proposed barrier | Bound signed non-DC contribution uniformly | Prove a quantified statement; adversarially test an overbroad version |
| Subgroup restrictions preserve the lower bound | Their actual extra information | Rational residue profiles | Check atom normalizations and degeneracies |

CONJECTURED main alternatives remain open at this checkpoint: either a weighted o(sqrt(X))-escape with four binary moment profiles at density near D, or a binary-specific inequality forcing d<D. The DC-barrier statement and the kurtosis heuristic are being audited, not assumed.

## Task 1 discovery checkpoint

NUMERICAL (Gurobi 13.0.3, VM, discovery grids only): adding the round-9 long Chebyshev lines to the round-10 support-coupled method gives D=0.1328880302 (C=7.5251322), with K=64, degree 10, quadratic Schur shape 0.2. Adding a separate monotone third-dilation potential at K=48 gives D=0.1323699022 (C=7.5545874). Neither decimal is a rigorous certificate. Both source/input outputs are preserved in the scratch directory.

PROVED successful change: at t>=1/(k+1), the sampled PD symbol is the NONNEGATIVE FINITE polynomial 1+2 sum_{n=1}^k w(nt)cos(n theta). The old long lines discard the information that w(nt)=0 for n>k. Positive combinations of symbol evaluations give support-specific linear lower bounds for w(2t); e.g. k=2 or 3 gives w(2t)>=w(t)-1/2. These were tested and supply the new branches in the final certificate below.

PROVED certificate construction: exact rational reconstruction passes with D1=259/2000=0.1295, giving C<2000/259=7.722007722... . The K=192, degree-12 discovery value was D=0.1292047184 (NUMERICAL). The successful reconstruction increases every a_j by 1/2000 after rounding. The first attempt with 1/10000 failed near u=0.32398 in half-cell 64; its full failed artifact is saved as `failed_certificate_slack_1e4.json`, and is not a theorem. The successful file is `certificate_td.json`, with 384 half-cells and 192 Schur cells. Its minimum exact Schur Bernstein margin is 104315471167/26542080000000000>0. The target C>=8 is not met.

PROVED independent verification COMPLETE: `independent_verify.py` independently reconstructed all 1865 pointwise leaves, 383 nontrivial CF caps, 188 support-specific rational lines, all 18 quoted long lines (Sturm), and all 192 continuum Schur cells. It uses SymPy QQ/FLINT for a fresh polynomial construction and reconstructs the Schur cubics by four exact direct integrals/interpolation. One lower-degree Bernstein representation required further subdivision of the saved leaf; that refinement passed. This changes no rational coefficient or claimed constant. `independent_verification.json` records the exact checks and SHA256 of the certificate. Thus D<=259/2000 and T-dense(C) for every fixed C<2000/259 are PROVED computer-assisted results, not merely discovery values. They are not kernel-checked.

PROVED exact support-line derivation (the new ingredient): for any k>=2 and nonnegative rational weights alpha_l at rational z_l in [-1,1], let T_n be the Chebyshev polynomials and

    A_n=2*sum_l alpha_l*T_n(z_l), c=sum_l alpha_l,
    R=sum_{n=3}^k max(A_n,0).

If A_2>0, every normalized real PD w with w(nt)=0 for n>k satisfies

    w(2t) >= (-A_1*w(t)-c-R)/A_2.

PROVED proof: nonnegativity of the sampled symbol at theta_l=arccos(z_l) gives 0<=c+A_1*w(t)+A_2*w(2t)+sum_{n=3}^k A_n*w(nt). Since 0<=w(nt)<=1, the last sum is at most R. Rearrange. All saved nodes, weights, A_2, R, and line coefficients are rational. `support_lines.py` discovers these lines by Gurobi LP for 2<=k<=16 and repairs every positive higher-moment coefficient by the exact R subtraction. No sampled positivity assertion is used as a proof of a line. The round-9 long lines are additional quoted branches, separately rechecked by Sturm in the independent verifier.

PROVED certificate implication: on each of the 384 t half-cells, the rational certificate verifies

    phi(w(t)^2) <= a(t)*w(t) + B(2t,w(2t)) - B(t,w(t))/2.

Here a is nonnegative and B(t,.) is an increasing degree-12 Bernstein polynomial on each of 192 cells, with B(t,0)=0 and B=0 for t>=1. The argument w(2t) is replaced by a valid Gram, long-line, or support-line lower bound. The support length k is computed at the half-cell's LOWER endpoint; this only enlarges the allowed class. CF caps give an upper bound on w(t). The substitution x=1-u^2 turns every branch into a rational polynomial. Each saved leaf proves either A>=0 or u^2*(2-u^2)/4-A^2>=0, with any exact nonnegative endpoint factor removed. Integration cancels the B terms. Exact continuum Schur integration with U(x)=1+(4/5)x(1-x) gives T_a U<=(259/1000)U, hence D<=259/2000. This uses P61's quoted reduction from complex generators to nonnegative real autocorrelations.

## Task 2: exact DC-barrier scope

PROVED NEW quantified sufficient barrier (elementary; relevant PROOFS grep checked): let X>=1, j>=2 integer, g(x)=sum_{k=1}^X r_k cos(kx) with real r_k, and h=m+g with m>=0. Let tau be any Hermitian positive-definite sequence on Z. Then

    Re sum_{k=-X}^X tau(k)*hhat(k)^j
      >= tau(0)*(m^j - 2^(1-j)*sum_{k=1}^X |r_k|^j).

PROVED proof: positive definiteness gives tau(0)>=0 and |tau(k)|<=tau(0). Here hhat(0)=m and hhat(+-k)=r_k/2. Apply the triangle inequality to the nonzero terms. In particular every such test is automatically nonnegative whenever m^j>=2^(1-j)*sum |r_k|^j. Nonnegative coefficients of tau are unnecessary for this sufficient criterion. This result remains valid for X-dependent tests with arbitrary support and normalization.

PROVED corollary with exact quantifiers: for any fixed finite set of integers j>=3, if sum |r_k|^j=O_j(X), choosing an offset m_X with X^(1/3)=o(m_X) and m_X=o(sqrt(X)) makes ALL of these tests automatically nonnegative for all sufficiently large X. If a given g_X already has min>=-o(sqrt(X)), increase m_X further to dominate its actual negative minimum. This changes no nonzero coefficient moment. For tests whose real coefficients tau(k) are also nonnegative, every EVEN-j test is already trivial, since every term is nonnegative.

PROVED limitation: this does not prove that every conceivable higher-order positivity argument is ineffective. It covers the displayed anchored convolution tests. The inference from M>>X^(1/j) alone is invalid without the absolute-moment bound, and M being an upper bound does not force the minimal admissible DC offset m to be large. The broad exclusivity claim in NOTEBOOK cont.14 remains HEURISTIC.

PROVED correction to a premise of the heuristic: positivity of the physical test function requires tau to be PD; it does NOT by itself require tau(k)>=0. For example tau(0)=1, tau(+-1)=-1/2, all other values zero, has inverse transform 1-cos(x)>=0. It can test the nonnegative convolution h^{*j}. Double positivity is an additional restriction if one also wants nonnegative coefficient-side local weights. The sufficient DC bound above deliberately covers this larger PD test class. Moreover its condition implies h^{*j}>=0 POINTWISE by the same triangle inequality, even for arrays whose h itself need not be positive. No fixed or adaptive positive physical test can extract more information from that convolution power once this condition holds.

PROVED NEW actual-DC realization (PROOFS grep checked): in the uncorrected packet escape with J->infinity, J=o(X), the actual negative minimum, not just an arbitrarily chosen upper bound, satisfies

    M(E_X)=(1+o(1))*sqrt(J/8).

PROVED proof: S_X(x)=1+2*sum w(k/X)cos(kx)>=0 has mean 1. After scaling x=v/X, its probability measures are tight, because S_X(v/X)/X converges locally to the nonnegative Fourier transform of w, whose integral is 2*pi. Select R_X->infinity sufficiently slowly that J*R_X/X->0 and the S_X mass outside |x|<=R_X/X tends to zero. Outside the union of the 2J translated packet arcs (measure o(1)), the nonnegative packet sum has integral o(sqrt(J)). Also P_X+1/4 is nonnegative and has integral 1/4. At some point outside those arcs their sum is o(sqrt(J)); subtracting the exact packet DC sqrt(J/8)+1/4 gives the matching upper bound on the minimum. The analytic packet lower bound supplies the other direction. This holds for any choice of centres, provided the fixed generator w is used.

PROVED fast-packet moment law: with independent uniform centres and any J(X)->infinity, coefficient moments of each fixed order converge weakly in probability to their Gaussian values. For distinct k,l, the summands cos(k*theta_i), cos(l*theta_i) are centered, uncorrelated, uniformly bounded. Expanding their joint moments, pair partitions give the independent Gaussian contribution; every non-pair partition loses at least J^(-1/2), uniformly in k!=l. Thus each averaged fixed-order moment has variance O_j(1/X+J^(-1/2)); its expectation tends to the Gaussian moment. A countable-test diagonal selects deterministic realizations with all needed moment bounds. This supplies the preceding base hypotheses for fast as well as slow packet growth.

PROVED precise concrete verdict for the anchored-test meta-statement: take J=floor(X^(9/10)) in this packet realization, and add the P62 direct cubic gadget with L=floor(X^(4/5)), z_k=L^(1/3)*cbrt(e(1-2p)) on LZ. This gives the first THREE binary raw profiles for every generator w. The gadget has physical L1 norm at most its physical L2 norm O(X^(11/30))=o(sqrt(J)), so it cannot fill the packet floor on most of the circle. The actual M of the corrected escape is at least (1-o(1))*sqrt(J/8), and is o(sqrt(X)) by P62's l1 upper bound. For every fixed integer j>=3,

    sum |a_k|^j = O_j(X + X^(1/5+4*j/15)),
    M(E_X)^j >= c_j*X^(9*j/20),
    sum |a_k|^j / M(E_X)^j -> 0.

The exponent differences are negative for every j>=3. Therefore with h=E_X+M(E_X), EVERY anchored j-fold convolution test by a PD sequence is automatically nonnegative, uniformly over X-dependent tests, for each fixed j>=3. The same reasoning applies to the displayed residual polynomial after subtracting p, using its own actual minimum. This is an actual weighted three-profile escape for every REAL NONNEGATIVE generator w used in this section, with actual DC domination of all fixed higher convolution orders. Its fourth moment still diverges; it is not a four-profile escape, and the broader assertion excluding all other higher-order arguments is not proved.

PROVED kurtosis identity (quoted binary algebra, independently derived here): for Bernoulli(p), e=p(1-p), the centered fourth moment is e(1-3e) and its kurtosis is 1/e-3. The equality threshold for Gaussian kurtosis is e=1/6, equivalently p=(1-1/sqrt(3))/2 on the smaller branch. The question is whether physical positivity controls this coefficient statistic after the exceptional DC contribution has been removed.

## Task 2: a quantitative obstruction to negligible-energy repair

PROVED NEW lemma (no external priority claim; PROOFS novelty grep checked): for any two real arrays u,v of length X, write E=X^(-1)sum (u-v)^2 and F_u=X^(-1)sum u^4, F_v similarly. Then

    |X^(-1)sum (u^3-v^3)|
      <= sqrt(E)*(sqrt(F_u)+(F_u*F_v)^(1/4)+sqrt(F_v)).

PROVED proof: factor u^3-v^3=(u-v)(u^2+uv+v^2), apply Cauchy-Schwarz, then the L2 triangle inequality and Cauchy-Schwarz to the uv term. The same statement holds with nonnegative test weights psi(k/X)/X, using weighted norms throughout. Thus every L2-small correction between arrays with bounded normalized fourth moments preserves the cubic profile. This is stronger than the failure of the particular P62 sparse gadget: EVERY negligible-energy correction that changes a nonzero limiting cubic profile must lose fourth-moment tightness.

PROVED application, precisely delimited: let v_X be any base weighted escape having raw cubic profile p^3+3pe, raw fourth integral F=integral(p^4+6p^2e+3e^2), e=p(1-p), and p continuous with 0<=p<=1/2, p(0)=1/2, p(1)=0. Suppose u_X matches the four binary raw profiles p. Put d=integral p and S=integral e(1-2p)>0. Then

    liminf X^(-1)sum (u_X-v_X)^2
      >= S^2/(sqrt(d)+(d*F)^(1/4)+sqrt(F))^2 > 0.

PROVED positivity of S: continuity forces p to take values strictly between 0 and 1/2 on a nonempty interval, where e(1-2p)>0. The lemma needs the displayed base moment limits; it makes no assertion for packet arrays that do not have them. Gaussian random packets have these limits under the usual moment law, and the finite probes below test them directly. This excludes all o(X)-energy repairs of such packet escapes into a four-profile escape, hence also all o(X/log X)-energy repairs. It does not exclude a structurally different escape separated from random packets by order-X energy, and it is not the global alternative (B) d<=D4<D.

PROVED deterministic realization of the base hypotheses (so the obstruction is nonvacuous at EVERY generator w): take real nonnegative PD w in the P61 class, p=phi(w^2), and angles theta_i such that 1,theta_1/(2*pi),...,theta_J/(2*pi) are Q-linearly independent for every finite J. For fixed J set

    v_(X,J),k = p(k/X) + w(k/X)/sqrt(2*J)*sum_{i=1}^J cos(k*theta_i).

Weighted Weyl equidistribution gives, for every continuous macroscopic test, residual mean 0, variance e, cube 0, and fourth moment 3*e^2*(1-1/(2*J)). The fourth formula follows from E cos^2=1/2, E cos^4=3/8 and independence of the J Haar phases. The packet minimum is at least -sqrt(J/8)-1/4. A sufficiently slow diagonal J=J(X)->infinity with J=o(X), controlling a countable dense set of tests and the bounded fourth absolute moments, therefore produces an o(sqrt(X)) escape with exactly the base cubic/fourth profiles displayed above. Such angle families exist, e.g. theta_i=2*pi*sqrt(prime_i); the usual independent sign automorphisms in multiquadratic fields prove the required Q-linear independence. This is an existence construction, not a claimed fast effective threshold or a binary construction.

PROVED triangular exact constants for the quantitative obstruction: when w(t)=1-t,

    d=(1-pi/4)/2, S=pi/64, F=67/120-5*pi/32.

These follow by expanding p=(1-sqrt(1-w^2))/2 and using the elementary quarter-circle integrals. Thus the lower bound for the normalized repair energy is the explicit positive number S^2/(sqrt(d)+(d*F)^(1/4)+sqrt(F))^2. A separate VM Arb evaluation below supplies an outward numerical enclosure; the formula, rather than its decimal, is the theorem.

PROVED general sparse-correction bound: |X^(-1)sum z^3|^2 <= (X^(-1)sum z^2)*(X^(-1)sum z^4). A nonzero cubic correction with vanishing second moment therefore has divergent fourth moment. This explains P62's divergence without its particular spacing or amplitude exponents.

PROVED correction to the brief's word "equivalent": four matching raw profiles IMPLY normalized L2 proximity to {0,1}; the converse needs a tail condition. Take any binary array b of fixed density and alter one zero entry to X^(1/4). Its normalized squared distance to {0,1} tends to zero, its first three raw profiles still match those of b, but its fourth moment has an extra unit atom. Uniform boundedness, or uniform integrability of fourth powers, repairs the converse. No unqualified equivalence is used in this report.

PROVED rounding-rate limitation: nearest rounding b gives sum |a-b|<=sqrt(X*E), where E=sum dist(a,{0,1})^2, hence the general triangle bound on the change of the cosine polynomial is sqrt(X*E). E=o(X/log X) alone does not make this bound o(sqrt(X)). If a lies in [0,1], independent unbiased rounding has variance V=sum a(1-a)<=sum dist(a,{0,1})<=sqrt(X*E); Bernstein plus a polynomial-size circle grid gives a uniform error O(sqrt(V log X)+log X) with high probability. Thus E=o(X/(log X)^2) is a SUFFICIENT rate for that particular procedure. This is not asserted to be necessary or optimal, nor does unbiased binary rounding apply to coefficients outside [0,1]. The four weak profiles alone supply no such quantitative rate.

PROVED conditional rounding theorem: for any sequence of real arrays 0<=a_(X,k)<=1, if X^(-1)sum a_(X,k)->d>0, min_x sum a_(X,k)cos(kx)>=-o(sqrt(X)), and sum dist(a_(X,k),{0,1})^2=o(X/(log X)^2), then binary arrays exist with n_X/X->d and M(A_X)=o(sqrt(X)). Independent Bernoulli rounding succeeds with probability tending to one by the preceding variance bound, Bernstein's inequality on an O(X^3)-point circle grid, and the derivative bound X^2. The count concentrates as well. This supplies a concrete sufficient rounding target; no array satisfying its hypotheses at positive density is constructed here.

HEURISTIC strategic review: the two mechanical certificate changes give information, but the principal fourth-moment gap remains structural. Discontinue negligible-energy repairs of Gaussian packets as a possible four-profile construction. Test a cyclic two-valued (Paley) residual and explicitly track its exceptional residue class, rather than assuming that subtracting the random/DC background preserves a kurtosis inequality. This is a different mechanism from rare large cubic gadgets.

## Task 2: subgroup audit and the total torsion budget

PROVED quoted subgroup operation: for every fixed positive integer q, averaging f_A(x+2*pi*j/q) over 0<=j<q gives f_{A intersect qZ}(x)>=-M(A). Dilation by q preserves the minimum, so A_q=(A intersect qZ)/q has M(A_q)<=M(A). In a common subsequence on which all rational twisted profiles exist, with coordinates t=k/X, its density profile is

    p_q(t)=p(t)+sum_{j=1}^{q-1} W_{2*pi*j/q}(t).

PROVED normalization: its degree scale is X/q, and its normalized counting measure is (q/X)sum_{q divides k} a_k delta_(k/X). The root-of-unity filter gives the displayed formula with NO factor q. The even Hermitian extension of each W is PD by P48, so W_theta(0)>=0 and |W_theta(t)|<=W_theta(0). In particular p_q(0)>=a>0; continuity gives positive limiting density for every fixed q, making the application of P59/P61 legitimate.

PROVED NEW quantitative consequence of the quoted operation: for every dense counterexample limit with a=p(0),

    sum_{theta in 2*pi*(Q/Z), theta != 0} W_theta(0) <= 1/2-a.

PROVED proof: apply p_q(0)<=1/2 to q=lcm(1,...,L), then increase L. All summands at zero are nonnegative. Consequently the rational macroscopic part R(t)=sum_{theta !=0 rational} W_theta(t) converges absolutely and uniformly, |R(t)|<=1/2-a, and sum_theta |W_theta(t)|^2<=(1/2-a)^2 for every t. At a=1/2 all rational macroscopic atoms vanish. This extends the lead's fixed-q observation to a total budget; it does not constrain mesoscopic atoms whose limiting individual amplitudes vanish.

PROVED additional bound: writing a_q=p_q(0), the same P61 Jensen/scaling argument gives integral p_q<=4*a_q*(1-a_q)*D. The operation therefore constrains rational atoms but leaves the atom-free P61 escapes unchanged. No D4<D follows from it here.

PROVED classification of a restricted auxiliary-operation class (assembly of the classical 0/1-PD subgroup lemma, not a new classification theorem): suppose a translation-invariant linear operator is convolution by a probability measure on the circle, and maps every binary cosine coefficient array to a binary coefficient array by a real diagonal Fourier multiplier eta(k). Testing singleton frequency sets forces eta(k) in {0,1}. Its full multiplier sequence is PD, eta(0)=1. For a probability measure mu, eta(k)=1 implies exp(i*k*x)=1 mu-almost everywhere; hence H={k:eta(k)=1} is a subgroup of Z. The operation is exactly restriction to qZ, to {0}, or the identity. Thus universal positive linear coefficient masks do not provide further binary-derived objects beyond subgroup restrictions. Nonlinear, set-dependent, or non-diagonal operations are outside this lemma.

## Task 2: the kurtosis assertion and the Paley boundary

PROVED full-Haar positive-amplitude inequality, with the needed hypothesis: let theta_i be finitely many distinct characters of a compact abelian group, no theta_i=-theta_i and no duplicate up to sign, and a_i>=0. For S=sum a_i cos(theta_i), Haar averaging gives

    E S^2 = (1/2) sum a_i^2,
    E S^4 >= (3/4)(sum a_i^2)^2 - (3/8)sum a_i^4.

PROVED proof: expand into characters. Every zero-sum quadruple contributes a nonnegative quantity; retain the three pairings, correcting their overcount on a single frequency. Additional relations can only increase the fourth moment. Thus kurtosis is at least 3-(3/2)sum a_i^4/(sum a_i^2)^2, and at least 3/2. If no single amplitude carries a positive fraction of the variance, the lower bound tends to 3. An order-two character can have kurtosis 1, so it must be excluded explicitly.

PROVED refutation of an unrestricted "remove DC and retain kurtosis >=3-o(1)" extension: let q=1 mod 4 be prime, Q its nonzero quadratic residues, chi the Legendre character, and

    S_q(k)=sum_{a in Q} cos(2*pi*a*k/q).

PROVED classical Gauss-sum evaluation: S_q(0)=(q-1)/2 and S_q(k)=(-1+sqrt(q)*chi(k))/2 for k!=0. On the q-1 NONZERO residues, S_q+1/2 has mean zero, variance q/4 and fourth moment q^2/16, hence exact kurtosis 1. All cosine amplitudes are positive. After normalization by sqrt(q), every individual amplitude tends to zero and the prime group has no proper nontrivial subgroup. The omitted DC value of (S_q+1/2)/sqrt(q) is sqrt(q)/2 and contributes q/16 to the NORMALIZED fourth moment over all q residues (equivalently q^2/16 before dividing by q). This is exactly the concentration that invalidates subtraction of the DC contribution. The full-Haar inequality above remains true. This example is cyclic, and does not refute a theorem that imposes the integer interval envelope AND four-moment tightness; it refutes the unqualified subtraction step.

PROVED constructive boundary for integer envelopes: fix any real continuous nonnegative PD w supported in [-1,1], w(0)=1, p=phi(w^2), and let q=q(X)=1 mod 4 be prime with q->infinity and q=o(X). The positive weighted packet family

    r_k = w(k/X)*S_q(k)/sqrt(2*q)

has an all-circle lower bound -((q-1)/(4*sqrt(2*q)))-1/4 after adding the p baseline. Indeed write the cosine product as the average of the two translates of V(x)=sum w(k/X)cos(kx), each with V>=-1/2, and sum over the (q-1)/2 residues. Thus it is an o(sqrt(X)) weighted escape. Its first two coefficient profiles are p and p, but

    (1/(X*q)) sum r_k^4 -> (1/64) integral_0^1 w(t)^4 dt > 0.

PROVED explanation: multiples of q have r_k=(q-1)w/(2*sqrt(2*q)); their Riemann sum has mesh q/X. All other coefficients are bounded, so vanish after division by q in the fourth moment. The fourth moment therefore diverges; unlike P62, this failure comes from the exceptional cyclic residue class of an exact PDS.

PROVED failure after deleting that exceptional class: the natural variance-renormalized deletion gives r'_k=w(k/X)*chi(k)/2 (chi=0 on multiples of q). For q->infinity with q=o(X^(2/3)), it has negative minima of order at least X/sqrt(q), hence M/sqrt(X)->infinity. To see this, choose any nonresidue a. The q-periodic sequence chi(k)cos(2*pi*a*k/q) has mean -1/sqrt(q). Partial summation against w gives

    sum_{k=1}^X w(k/X)*chi(k)cos(2*pi*a*k/q)
      = -(X/sqrt(q))*integral_0^1 w + O(q),

where w has bounded variation for the smooth/step-autocorrelation generators used here. The p baseline at the same angle is O(q) by its bounded variation. Hence f(2*pi*a/q)=-(X/(2*sqrt(q)))*integral w+O(q). This proves failure in the stated range, not for every possible relation between q and X. Moreover deleting the class gives symmetric residuals, so the required cubic profile remains absent away from p=1/2. Both the moment defect and the minimum obstruction matter.

PROVED nearest-rounding cost for the positive Paley family: its exceptional multiples of q alone give

    liminf (1/X)sum dist(p(k/X)+r_k,{0,1})^2
      >= (1/8)integral_0^1 w(t)^2 dt > 0.

The squared distance on those multiples equals r_k^2+O(|r_k|+1); the normalized lower-order terms tend to zero, and the leading term is the displayed Riemann sum. Thus this positive escape has order-X rounding energy, in addition to divergent fourth moment. The small minimum is not a near-counterexample to the binary problem.

## VM experiment record and certificates

NUMERICAL reproducible probe: `fourth_probe.py`, seed 2026101911, uses the E82 N=320 factor rounded to integer entries (saved in `packet_factor.json`) and its EXACT rational PWL autocorrelation. The quoted target densities are 0.1166139255 at X=4096 and 0.1166708884 at X=65536. Random packet centres are saved as exact grid indices in `packet_centres_X*.json`. The two Paley moduli 61 and 257 were checked prime on the VM. Each FFT uses the full circle with a power-of-two grid at least 32*(X+1). No FFT is treated as a proof.

NUMERICAL finite construction outcomes (all failed four-profile candidates; energy means X^(-1)sum dist(a,{0,1})^2):

| Family | X | J or q | Fourth raw moment | Binary target | Nearest energy | FFT minimum |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Random packets | 4096 | J=147 | 0.08740652 | 0.11661393 | 0.05119892 | -4.532190 |
| Positive Paley | 4096 | q=61 | 0.33550797 | 0.11661393 | 0.05475514 | -1.606004 |
| Paley DC removed | 4096 | q=61 | 0.05746491 | 0.11661393 | 0.04259230 | -125.578245 |
| Random packets | 65536 | J=776 | 0.08793212 | 0.11667089 | 0.05078462 | -10.097312 |
| Positive Paley | 65536 | q=257 | 1.16217547 | 0.11667089 | 0.06558228 | -3.072421 |
| Paley DC removed | 65536 | q=257 | 0.05814572 | 0.11667089 | 0.04276017 | -977.208126 |

NUMERICAL moment discrimination at X=65536: random packets have residual cube -0.00005615 versus binary requirement 0.04270704. Positive Paley has residual cube 0.18740022 and fourth 0.91177954 versus required fourth 0.04157470. DC removal gives cube about 4.25e-9 and fourth 0.01442197. The positive family overconcentrates on the exceptional class; the deleted family lacks the cubic skew and loses the lower bound. Matching one kurtosis statistic alone is insufficient.

PROVED finite weighted certificate for the BEST positive Paley escape, X=65536, q=257, exact saved factor: the analytic all-circle lower bound is -(256)/(4*sqrt(514))-1/4, enclosed by -3.0729189849038777010105473227513157820854675503393647 with Arb radius below 3.3e-53. A 180-bit Arb evaluation at x=2*pi*2078304/4194304 encloses the value -3.07242066887755174830315100621001527283224240 with radius below 5.6e-45. Thus its global minimum is rigorously bracketed between these two balls. This is a weighted polynomial, not a binary set.

PROVED failure certificate after DC deletion: for the same factor and q, 180-bit Arb at x=2*pi*652810/4194304 encloses -977.208125612170760617960991463024557487450995163 with radius below 7.1e-46. It certifies an actual negative dip, not just a missed-grid concern.

PROVED failed nearest binary roundings, with the exact sets saved and 200-bit Arb point certificates: `random_round_X4096.txt` has n=480, max A=2400, R>17995/10000; `random_round_X65536.txt` has n=7672, max A=39584, R>19944/10000. Note that nearest rounding changes the support endpoint and density. These are failure examples, not controlled-density seeds of a claimed binary construction. A final independent 220-bit reevaluation of the SAVED sets is performed by `final_check.py`.

## Final verdict, novelty, and precise remaining block

PROVED Task 1 deliverable: exact D1=259/2000 with independent verification. Every nonempty binary A with max A<=C*|A| has M(A)>=c(C)*sqrt(|A|) for some c(C)>0, for EVERY FIXED C<2000/259. The constant c(C) is ineffective. The capped certificate task stops here; C>=8 remains unachieved.

PROVED Task 2 deliverable at partial scope: the displayed quantitative repair-energy inequality, total torsion budget, restricted positive-mask classification, and precise anchored-test DC theorem all have complete proofs above. The actual three-profile escape satisfies every fixed-order anchored convolution test automatically, while its fourth moment diverges. The Paley computations have analytic/Arb all-circle and point certificates. The full alternatives (A) and (B) are BLOCKED at a concrete missing statement: one needs either a genuinely different positive packet configuration with bounded fourth moments and the required nonsymmetric local Bernoulli law, or a binary-specific second-order inequality that excludes ALL such configurations. None of the proved subcase obstructions supplies a uniform D4<D or a4<1/2.

PROVED Task 3 deliverable: the unqualified prime-cyclic square-root statement is false by the complete graph; Sanders' fixed-density theorem is polynomial with the half-density exponent 1/3 specified in v2; exact regular cyclic PDS classification forces prime Paley graphs after trivial graphs are removed. Exact weighted identities are much less rigid. The interval-support and continuous-minimum requirements prevent a direct transfer of a small sampled cyclic minimum to an integer counterexample. Source versions and access limits are stated above.

PROVED new versus quoted: new to the grepped project record are the support-specific symbol-line certificate and improved rational D1; the quantified bounded-fourth-moment repair-energy lower bound; the actual-DC realization and resulting all-fixed-order anchored-test statement for the three-profile escape; the total rational-atom budget; and the explicit Paley envelope failure records. The subgroup lemma, packet mechanism, cubic gadget, four-profile defect identity, Catalan/Boas-Kac/P61 reduction, Gram/CF and round-9 long lines, Gauss-sum formulas and PDS classification are quoted or elementary classical inputs. No external priority claim is made for the new assemblies or inequalities.

HEURISTIC final global review and decision: stop increasing certificate resolution in this round, since it already consumed the bounded mechanical lane and remains below 8. Kill negligible-energy Gaussian repair and the natural Paley DC-deletion construction for the proved reasons. Three distinct live next directions remain: (1) a NON-negligible-energy, bounded-fourth-moment weighted-PDS construction with varying density and PD envelopes; (2) nonlinear or set-dependent binary-derived positive objects, beyond the classified linear masks; (3) a quantitative stability theorem for approximate WEIGHTED cyclic PDS under an interval envelope and a small offset. The first concrete next derivation is to formulate that weighted stability statement with the DC residue retained and a uniform fourth-moment budget; ordinary Ma rigidity cannot be substituted for it. No unattended continuation is implied.

PROVED final-check record: `final_check.py` independently verifies the saved binary point dips at 220 bits, the cubic/fourth algebra, the rational exponent budget, the certificate hash, and syntax of every round-11 Python source. For the triangular generator it encloses the positive repair-energy lower bound by 0.0031187508030468019210144239454574291863920472877059392430425144054 with radius below 6.5e-68, in particular strictly above 3/1000. `final_checks.json` and `manifest.json` record the source/data SHA256 values and Python 3.12.3. No root `.research/*.md` file, commit, subagent, or LaTeX artifact was created or edited by this round.

PROVED reproducibility commands (run from the project root; the saved discovery JSON is the input to reconstruction):

```sh
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 python .research/agents/tdense11_scratch/support_lines.py
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 python .research/agents/tdense11_scratch/discover.py 192 12 0.2 0
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 python .research/agents/tdense11_scratch/certify.py discovery_K192_d12_s0.2_t0_support.json 1/2000 259/2000
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 python .research/agents/tdense11_scratch/independent_verify.py
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 python .research/agents/tdense11_scratch/fourth_probe.py
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 python .research/agents/tdense11_scratch/final_check.py
```

## Task 3: short literature check and precise scope

PROVED quoted, source-verified: Sanders, *Chowla's cosine problem*, arXiv:0807.5104v2 (14 October 2010), Theorem 1.2, states a polynomial negative-Fourier bound for symmetric sets of size (p+1)/2 in Z/pZ; the following sentence specifies that exponent 1/3 can be arranged. His Theorem 1.3 gives a polynomial bound in the distance to a subgroup for fixed positive density. These are not square-root theorems. The same introduction compares with Spencer's O(sqrt(p)) construction. See [Sanders v2, pp.1-2](https://arxiv.org/pdf/0807.5104). This short search did not establish a current square-root theorem for prime cyclic groups at densities bounded away from 0 and 1; no absence-of-literature claim is inferred.

PROVED elementary correction to the UNQUALIFIED cyclic question: no absolute c>0 can give -lambda_min>=c*sqrt(|B|) for EVERY symmetric B subset Z/pZ minus {0}; B=Z/pZ minus {0} gives the complete graph, lambda_min=-1, and |B|=p-1. Any viable prime-cyclic statement must impose distance from the full group (or a density cap). This exception persists even though Z/pZ has no proper nontrivial subgroup.

PROVED quoted classification, with its exact scope checked: a nontrivial strongly regular circulant is a Paley graph on a PRIME p=1 mod 4. Here nontrivial excludes disjoint unions of equal cliques and their complements (complete multipartite graphs). Theorem 259 of [Liu-Zhou, *Eigenvalues of Cayley graphs*, EJC 29(2), #P2.9 (2022)](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v29i2p9/pdf), p.107, attributes this independently to Bridges-Mena, Hughes-van Lint-Wilson, and Ma (*Partial difference sets*, Discrete Math.52 (1984), 75-89), with a partial result of Marusic. The broader distance-regular classification is independently restated as Theorem 2 in [Zhan-Huang-Lu, EJC 33(1), #P1.14 (23 January 2026)](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v33i1p14/pdf/), citing Miklavic-Potocnik (2003), Theorem 1.2 and Corollary 3.7. It lists cycles, complete graphs, complete multipartite graphs, odd crown graphs, and prime Paley graphs. Only the appropriate diameter-two members are strongly regular.

PROVED source limitation: Ma's 1984 original full text was not obtained in this capped search, so no unverified Ma theorem number is supplied. The 2022 theorem and the 2026 restatement were read, and an independent proof for the prime case is given below. Ma's 1994 *On subsets of partial difference sets* has a different exact result: if G is abelian, D=D^(-1) is a PDS, gcd(|H|,|G|/|H|)=1 and |G|/|H| is odd, then D intersect H is a PDS in H ([publisher abstract](https://www.sciencedirect.com/science/article/pii/0012365X94901678)). It is not an approximate weighted-PDS theorem.

PROVED independent prime-case check (classical result, not a novelty claim): let D=-D be a nonempty proper subset of F_p minus {0} whose Cayley graph is strongly regular and nontrivial. The nonprincipal character sums have two values r,s, roots of the PDS quadratic. For zeta primitive of order p, alpha=sum_{d in D} zeta^d has at most two Galois conjugates. If alpha were rational, all nonprincipal sums would coincide and Fourier inversion would force D to be empty or all nonzero residues. Thus alpha has degree two, and its stabilizer is the square subgroup of F_p^*. For each square h, sum_{d in hD} zeta^d=sum_{d in D} zeta^d. The polynomial difference has degree <=p-1 and zero constant coefficient, so divisibility by 1+z+...+z^(p-1) forces it to vanish identically. Hence D is invariant under square multiplication and equals the nonzero squares or nonsquares. Symmetry requires p=1 mod 4. These have parameters (p,(p-1)/2,(p-5)/4,(p-1)/4) and nonprincipal eigenvalues (-1+-sqrt(p))/2.

PROVED relevance limitation: these classifications concern EXACT regular 0/1 partial difference sets, not arbitrary positive WEIGHTED spike measures or approximate convolution identities. Indeed, for any symmetric B in Z/pZ with 0 not in B, F_B(j)=sum_{b in B} exp(2*pi*i*b*j/p), m>=-min F_B, and sigma(j)=m+F_B(j)>=0, normalized convolution satisfies

    sigma*sigma = sigma + (m^2-m)*1.

PROVED verification: the Fourier coefficients of sigma are 1_B(k)+m*1_{k=0}; square them coefficientwise. Thus weighted identities alone encode all symmetric binary sets once the offset is unrestricted. Ordinary PDS rigidity supplies no quantitative weighted stability theorem for the present problem.

PROVED integer/cyclic transfer: if p>2X is prime and B=A union (-A) embeds without collisions in Z/pZ, the Cayley eigenvalues are 2*f_A(2*pi*j/p). Therefore a uniform prime-cyclic square-root lower bound for this embedded class would imply the corresponding integer lower bound. Conversely, a cyclic construction with a small sampled minimum gives no continuous-circle certificate. The Lipschitz sampling loss is at most (pi/p)*sum_{a in A} a for f_A. Controlling it by o(sqrt(n)) generally requires p much larger than n*X/sqrt(n); such an embedding has vanishing density and is not a fixed-density prime model. The dense integer problem is related to a cyclic problem with an interval support constraint, not reduced here to unrestricted dense circulants.
