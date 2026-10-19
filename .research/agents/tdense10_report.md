# Round 10 T-dense research report

PROVED scope: f_A(x)=sum_{a in A} cos(ax), M(A)=-min f_A, n=|A|, X=max A. T-dense(C) means: there exists c(C)>0 such that M(A)>=c(C)sqrt(n) for every nonempty finite set of distinct positive integers with X<=Cn. All round-10 edits are confined to this report and tdense10_scratch; no commits or subagents. All mathematical computation is to run via DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4, and all LP/MILP/QP discovery uses Gurobi.

PROVED source audit: read the round-10 brief, CLAUDE.md, the number-theory-research skill and its three methodological references, PROOFS P58-P61, NOTEBOOK continuations 11-12, EXPERIMENTS E80-E82, the round-9 report, src/dirun.sh and src/e82_cp_reach.py. Relevant novelty searches precede any new mathematical claim. External priority is not claimed.

## Current checkpoint

PROVED Task 1: P61(a) passes the adversarial audit; P61(b) passes after the explicit complex-generator symmetrization repair below. PROVED Task 2: the exact support-coupled certificate gives D<=1333/10000 and T-dense(C) for every C<10000/1333=7.501875468867217..., including C=7.5. Independent reconstruction passed all 527 pointwise leaves, all 127 nontrivial CF caps, and all 64 Schur intervals. The final VM cubic probes and ball certificates are complete.

PROVED Task 3 (paper): sparse signed cubic corrections preserve the first two profiles and match the third; hence the first-three-profile reach is still 1/D for the explicitly unrestricted weighted class. Their fourth moments diverge, and four matching binary profiles force normalized L2 proximity to {0,1}. The exact four-profile reach and an actual binary construction remain UNKNOWN. D is the supremum of integral_0^1 phi(|w|^2) in P61; 1/D about 8.5708 remains only the quoted numerical estimate.

## Task 1: detailed normalization and limit audit

PROVED normalization check: use the continuous transform F(t)=integral f(v)exp(-itv)dv (no factor in the forward transform), and a normalized u-average over [0,2pi X]. Then the formula in P61 step 4 has exactly the displayed 1/X and 1/4. The density e is the even, two-sided measure limit; there is no extra factor 2. The factor 16 in step 5 is harmless and cancels in the normalized ratio. The Gabor pieces are integrable because H_X is bounded for fixed X and psi is L1. Their transforms are Hermitian PD and have the stated Minkowski-sum support. Zero transform-at-zero pieces vanish identically and receive zero weight.

PROVED limit check: rho is continuous, compactly supported and uniformly continuous. The residual-square measures have uniformly bounded mass and uniformly compact support, so weak convergence gives uniform convergence of their convolutions with rho (finite translate nets). The DC term m^2 rho/X tends uniformly to zero. Jensen uses the probability measure lambda_u du/integral lambda, not unweighted averaging after normalization. Dilation is c(t) -> c((1+delta)t). Fixed-epsilon normalized limits remain in [0,1]; dominated convergence applies on a common bounded interval. Finally e(0)>0 follows from d>0, a<=1/2 and e PD. Letting epsilon tend to zero is therefore legitimate, even at the square-root endpoint. The P59 crossing proof of a<=1/2 and the smaller-root identity p=phi(4e) are correct.

PROVED audit correction (resolved below): P61(b)'s written packet formula explicitly takes real nonnegative w, whereas its quantified statement includes every complex Hermitian w. Real symmetrization of a single translate repairs the mismatch. The precise smoothing diagonal and LLN are proved in the verdict below.

NUMERICAL first support-coupled probe (coupled.py, VM, Gurobi 13.0.3, degree 8, 12 CF intervals): a single t-independent doubling potential plus a Schur test gives sampled C about 7.02. This is a discovery grid, not a certificate; it does not meet the target. A literature lead identifies the continuous additive-energy problem as Garsia-Rodemich-Rumsey (1969), with the same extremal constant appearing as the PW2-to-PW4 embedding norm to the fourth power. Its numerical decimal will not be promoted to a rigorous bound without reading the actual theorem/certificate.

## Early probes and candidate record (superseded by the proofs below)

HEURISTIC mechanism, now under exact proof check: for a real normalized compactly supported PD v, let L be an integer of size X^alpha with 3/4<alpha<1, B=(gamma L)^(1/3), and

    Z_X(x)=B sum_{1<=n<=X/L} v(nL/X) cos(nLx).

Sampling PD gives min Z_X>=-B/2. The trivial coefficient bound gives min(-Z_X)>=-BX/L. Both costs are o(sqrt(X)). Its first coefficient profile tends to zero, second tends to zero, and third tends to gamma*v(t)^3 (with sign reversed for -Z). Distinct coprime L_i>X^(3/4) have no shared nonzero multiples <=X, eliminating cross terms among finitely many gadgets. Cross terms against the random packet escape should vanish from its O(sqrt(log X)) coefficient bound. Signed spans of v^3 are dense in even L1[−1,1] by polarization and Fourier modulation of an approximate identity. If these details pass, the exact THREE-profile reach stays 1/D, rather than improving it. Fourth moments of every nontrivial gadget diverge like L^(1/3), so this construction cannot match the full binary law.

NUMERICAL second support-coupled probe: t-dependent degree-6 potentials on 32 dyadic t intervals give sampled C=7.45806 using a positive quadratic Schur test function. This supersedes the first grid probe but is still not a certificate. A refined instance is running; exact rational pointwise and continuum Schur checks are required before any theorem.

## Task 1 verdict: P61(a) and (b), with a repair to (b)

PROVED (paper audit, not kernel-checked): P61(a) is correct with exactly its quantifiers. In every P58 dense contradiction limit, integral_0^1 phi(e/e(0))<=D and d<=D. Consequently every fixed C<1/D admits c(C)>0 uniformly for all nonempty binary A with X<=Cn. The limiting argument needs only the quoted P58 diagonal and P59 energy-PD/crossing result; the windows and Beckner are not additional assumptions. The normalization, support, uniform convergence, continuous Jensen, dilation, and both limits are checked above.

PROVED quoted external factorization input: the one-dimensional Boas-Kac-Krein theorem gives every continuous Hermitian PD w supported in [-1,1] a complex L2 autocorrelation root G supported on an interval of length 1. Translation puts that interval in [0,1]. This is exactly Theorem 2.1(a) of Ehm-Gneiting-Richards, [Convolution roots of radial positive definite functions with compact support](https://citeseerx.ist.psu.edu/document?doi=75594857443678ec8145b86f19c2c31f183fffb6&repid=rep1&type=pdf). Replacing G by |G| preserves its L2 normalization and pointwise dominates |w| by a real nonnegative autocorrelation. This proves equality of the TWO SUPREMA; it does not assert that every given w has a nonnegative root. P61's WLOG is valid in that precise optimization sense.

PROVED correction of P61(b)'s written formula: for complex Hermitian w put S_X(x)=sum_{k in Z}w(k/X)exp(ikx), which is real and nonnegative but need not be even. For uniform independent theta_j use

    g_X(x)=c sum_j [S_X(x-theta_j)+S_X(-x-theta_j)-2],
    c=1/sqrt(32J), J=floor(X^(9/10)).

This is even, real, and bounded below by -sqrt(J/8). Its cosine coefficients are

    r_k=4c sum_j Re(w(k/X)exp(-ik theta_j)).

They have mean zero and variance |w(k/X)|^2/4. For k!=l, both E[r_k r_l] and Cov(r_k^2,r_l^2) vanish exactly by circle orthogonality (the phases of w cause no change). Fourth and sixth moments are uniformly bounded; in particular E r_k^4<=3|w(k/X)|^4/16. Thus every bounded continuous macroscopic test has first profile zero and second profile |w|^2/4 in probability, with O(1/X) variances. A countable dense set of tests and a diagonal realization gives simultaneous weak limits. For real even w the repair reduces to the original paired-translate formula.

PROVED completion of P61(b): |w|^2 is PD, so p=phi(|w|^2) is PD by its nonnegative uniformly convergent power series. Its sampled smooth cosine polynomial P_X satisfies P_X>=-p(0)/2=-1/4. Therefore E_X=P_X+g_X has min E_X>=-sqrt(J/8)-1/4=-o(sqrt(X)), first coefficient profile p, and coefficient-square profile p^2+|w|^2/4=p. The degree is at most X; if 'degree X' is meant literally, append a nonzero vanishing multiple of cos(Xx), which leaves every asserted limit and lower bound unchanged.

PROVED smoothing audit: choose h=floor(X^(2/5)) in the triangular coefficient smoothing. The smooth sampled p convolves uniformly to p. The smoothed random r has variance O(1/h) at each index, and is a sum of independent centered variables bounded by O(J^(-1/2)); Bernstein plus a union bound over O(X) indices gives its supremum tending to zero in probability. Consequently q=k_h*a tends uniformly to p, and the residual first and second profiles are exactly (0,e), e=p-p^2. This is a valid P58 diagonal for the escape, rather than a separate informal decomposition. The same moment calculation gives residual cubic profile zero: possible cross-covariances of cubes lie on finitely many resonance lines mk=nl with 1<=m,n<=3, so their tested variance is O(1/X).

PROVED scope qualification: the sharpness statement concerns physical-space positivity of E_X+M_X and all of its valid positivity consequences, with the listed macroscopic binary moment identities. The constructed Fourier coefficients need not be nonnegative or bounded by 1. Those coefficient restrictions are additional binary information. Reading 'every positivity statement' as including coefficient nonnegativity would make P61(b)'s wording false; its displayed weighted escape never claimed that property. No actual binary counterexample is supplied.

## Task 3: proof of the sparse correction theorem

PROVED NEW (paper, internal novelty grep found no corresponding construction in PROOFS): let v be any continuous real even PD function supported in [-1,1], v(0)=1; let gamma>0 and sigma in {+1,-1}. Choose integer L with L asymptotic to X^alpha, 3/4<alpha<1, and B=(gamma L)^(1/3). Define Z as in the candidate above, and add sigma*Z to a weighted polynomial. The coefficient measures of this gadget have limits

    first: 0; second: 0; third: sigma*gamma*v(t)^3.

Indeed the multiples of L give a Riemann sum of mesh L/X, and B/L=gamma^(1/3)L^(-2/3), B^2/L=gamma^(2/3)L^(-1/3), B^3/L=gamma. Sampling PD gives Z>=-B/2. Also |Z|<=BX/L, so -Z>=-BX/L. Since alpha/3<1/2 and 1-2alpha/3<1/2, either signed gadget costs o(sqrt(X)) in its global minimum. These are analytic all-circle bounds, not FFT claims.

PROVED finite signed sums: choose distinct prime L_i asymptotic to X^alpha, with constants allowed to depend on the fixed finite family. Bertrand's postulate suffices to construct them. Since L_i*L_j>X eventually, their nonzero coefficient supports are disjoint in [1,X]. The mixed gadget cubic terms vanish identically. The round-9/P61 random residual has max_k |r_k|=O(sqrt(log X)) with probability tending to one by Hoeffding plus a union bound. Hence all cubic cross terms with the base p+r vanish: their absolute normalized sums are bounded by constants times

    (log X) L_i^(-2/3) and sqrt(log X) L_i^(-1/3).

First and second cross terms vanish as well. Thus adding finitely many signed gadgets preserves the first two profiles and the o(sqrt(X)) minimum, and adds exactly sum_i sigma_i gamma_i v_i^3 to the residual cubic profile.

PROVED finite-span density observation (not needed for the final construction): put Lambda(t)=(1-|t|)_+ and v_lambda(t)=Lambda(t)cos(lambda*t). Every v_lambda is real even normalized PD with the required support. The identity

    cos z = (4/3)cos(z)^3 - (1/3)cos(3z)

iterated N times expresses cos z, with uniform remainder at most 3^(-N-1), as a finite signed linear combination of cubes cos(3^j z)^3. Cosine polynomials are uniformly dense on [0,1]. Multiplying by Lambda^3, and first cutting off an arbitrarily short neighborhood of t=1, proves that the real signed span of v_lambda^3 is dense in even L1[-1,1]. HEURISTIC failed continuation, preserved: a slow diagonal of these signed PD sums does NOT by itself prove weak convergence against every continuous test. The sums of absolute cubic masses may grow, despite cancellation in the target functions. The required uniform total-variation bound was missing. No infinite-family theorem is inferred from that diagonal. The direct construction immediately below fixes the gap and is stronger.

PROVED NEW direct sparse cubic-profile theorem: positive definiteness of the correction shape is unnecessary. Let s be ANY continuous real function on [0,1], put v(t)=the real cube root of s(t), L=floor(X^(4/5)), B=L^(1/3), and define z_k=B*v(k/X) when L divides k, zero otherwise. Let Z_X=sum z_k cos(kx). Then, for every continuous test on [0,1], its first and second profiles tend to zero, while its third profile tends to s and its absolute-third profile tends to |s|. These are ordinary Riemann sums of mesh L/X with multipliers B/L=L^(-2/3), B^2/L=L^(-1/3), and B^3/L=1. In particular their signed cubic measures have uniformly bounded total variation.

PROVED all-circle bound for the direct construction: |Z_X(x)|<=sum |z_k|<=||v||_infinity*X*L^(-2/3)=O(X^(7/15))=o(sqrt(X)). Thus adding Z_X preserves any o(sqrt(X)) lower-minimum bound, regardless of its sign or shape. The shifted polynomial Z_X+sum |z_k| is itself nonnegative, so physical-space positivity and all its consequences remain valid. No pointwise Fourier coefficient sign restriction is asserted. This simple l1 estimate supplies both signs of every cubic correction; no PD expansion, prime moduli, or approximation diagonal is required.

PROVED compatibility with the exact smoothing diagonal: take h=floor(X^(2/5)). Each smoothing interval of width O(h) contains at most one multiple of L, so the direct gadget's smoothed coefficient supremum is O(B*||v||_infinity/h)=o(1). Together with the preceding base smoothing estimate, q tends uniformly to p. Replacing a-p by a-q changes its tested cube by o(1), because the normalized second moments are bounded. The cubic cross terms against the base again vanish by the two bounds displayed above. This verifies the residual cube for P58's actual filter, not just the displayed decomposition.

PROVED NEW third-order reach theorem (precise relaxation): for EVERY w in P61's class there exist real even weighted cosine polynomials E_X with min E_X>=-o(sqrt(X)), smoothing q->p uniformly, and weak local coefficient profiles

    a -> p, a^2 -> p, a^3 -> p,
    p=phi(|w|^2), e=|w|^2/4,
    (a-q)^3 -> e(1-2p).

To obtain them apply the DIRECT sparse correction theorem to the continuous function s=e(1-2p), starting from P61(b). The raw-cube identity is p^3+3pe+s=p. The base residual has uniformly bounded normalized absolute third moment along a deterministic realization: its expectation is bounded uniformly by the subgaussian moment bound, so a fixed Markov event of positive probability can be intersected with the finite-test events of probability tending to one. This total-variation control extends convergence from a countable dense set of tests to every continuous test; the direct correction has the same control by its absolute-third Riemann sum. Therefore physical positivity plus the FIRST THREE macroscopic binary coefficient profiles has exactly the same supremal density D, and the same reach 1/D, as the first-two-profile class. The upper bound follows from the already quoted second-order theorem; the construction supplies the reverse sharpness. This is not a claim for classes also imposing pointwise coefficient nonnegativity or a bounded coefficient range.

PROVED full-law obstruction for these gadgets: the direct gadget has normalized fourth coefficient moment asymptotic to L^(1/3)*integral_0^1 |s|^(4/3), hence diverges whenever s is not identically zero. The base O(sqrt(log X)) coefficients cannot cancel it on the gadget support. For every nonzero w in P61, s=e(1-2p) is nonzero: continuity from |w(0)|=1 to w(1)=0 forces values strictly between zero and one. The third-moment correction exploits rare large coefficients; it cannot solve the four-moment or binary problem.

PROVED NEW exact formulation of the remaining binary obstruction: for any real coefficient sequence, distance(a_k,{0,1})^2 <= 4 a_k^2(a_k-1)^2. If its first FOUR raw weak moment profiles are all the same bounded p, then for every nonnegative continuous test psi,

    (1/X)sum psi(k/X)*a_k^2(a_k-1)^2 -> 0,

by the expansion a^4-2a^3+a^2. Thus it is asymptotically binary in normalized coefficient L2. If coefficients are assumed nonnegative already, THREE profiles suffice: a(a-1)^2=a^3-2a^2+a>=0 and distance(a,{0,1})^2<=2a(a-1)^2 for a>=0. This explains the essential scope restriction of the three-profile theorem. Neither approximate L2 binarity nor these moment identities alone controls the global minimum after rounding on the sqrt(X) scale; that completion remains open.

HEURISTIC strategic review after two distinct certificate attempts and the cubic construction: discontinue the t-independent potential and cap the literature search (the original GRR full text was inaccessible in the attempted endpoints; the modern paper quotes its decimal but no unverified decimal is used). Continue the t-dependent certificate, which has sampled reach above 7.5 and an explicit continuum Schur proof. The new cubic construction advances the actual moment-reach target; seeking a universal cubic obstruction in this unrestricted weighted class is now disproved by the construction. Pivot the binary question to coefficient nonnegativity/fourth-moment tightness, where the sparse-spike mechanism fails. This does not assert that the four-moment reach is already strictly larger than 1/D.

NUMERICAL exact-check correction: the initial 801-node x grids miss a cusp near x=(sqrt(5)-1)/2. Dense diagnostics find violations of the rounded pointwise inequality as large as 0.0004375 in its divided-by-x form. The first two attempted certificate runs are UNRESOLVED, not proofs. Increasing every a_j by 1/2000 is being checked against the exact continuum Schur budget D1=1333/10000 (C=10000/1333>7.5). Failed discovery/certificate attempts are preserved in source and summarized here; the final successful certificate, if obtained, will supersede them.

## Task 2: exact support-coupled certificate and theorem

PROVED NEW (computer-assisted paper proof, independently reverified; not Lean-kernel checked): D<=D1=1333/10000. Consequently T-dense(C) holds for EVERY fixed

    C < C10=10000/1333=7.501875468867217...,

including C=15/2. For each such C there exists c(C)>0 such that every nonempty finite binary A with X<=Cn has M(A)>=c(C)sqrt(n). The constant is ineffective. This is a rigorous improvement over the quoted 6.936623... and meets the round-10 target 7.5; it does not certify the numerical second-order endpoint 8.5708.

PROVED certificate data: certificate_td.json contains 64 rational nonnegative kernel values a_j, 64 monotone degree-10 Bernstein potentials beta_j with beta_j(0)=0, all pointwise rational covering leaves for 128 half-cells, and 64 exact continuum Schur polynomials. Reconstruction rounds beta coefficients to denominator 10^10 and each a_j upward to denominator 10^9, then increases it by 1/2000 to repair the missed cusp. The successful run has no unresolved boxes. Every sign uses exact fractions. The smallest Schur Bernstein margin is 18576429767/491520000000000>0. No optimizer status or sampled inequality is used as a proof.

PROVED derivation: by the quoted Boas-Kac majorization, take w=G*Gtilde real nonnegative with G>=0 supported in [0,1] and integral G^2=1. Let B(t,x)=beta_j(x) for j/64<=t<(j+1)/64 and B=0 for t>=1. Let a(t)=a_j on the same cells. On each half-cell the exact certificate proves, for every allowed x=w(t) and y=w(2t),

    phi(x^2) <= a(t)*x + B(2t,y) - B(t,x)/2.

The lower branches for y are the quoted 0, 2x^2-1 and x-sqrt(1-x). Monotonicity of every beta_j justifies replacing y by a certified branch. The support-coupled x range is x<=cos(pi/(k+2)), where k=ceil(1/t_lower)-1 for the half-cell's lower endpoint (the zero endpoint uses x<=1). This follows by sampling w at nt: the sampled PD sequence vanishes beyond degree k, so Egervary-Szasz bounds its first coefficient. At reciprocal boundaries w(1)=0 makes the same statement valid; endpoint choices also have measure zero.

PROVED pointwise verification details: set x=1-u^2. The lower branches become the rational polynomials 0, 1-4u^2+2u^4 and 1-u-u^2. Write

    A(u)=a_j*(1-u^2) - beta_j(1-u^2)/2 + beta_child(L(u)) - 1/2,

with beta_child=0 outside the support. The desired expression is A(u)+u*sqrt(2-u^2)/2. Each saved leaf proves either A>=0 or u^2*(2-u^2)/4-A^2>=0 by exact rational Bernstein coefficients; the latter implies the desired sign regardless of the sign of A. An exact endpoint factor 1-u is removed where present. Each selected branch lies in [0,1] throughout the leaf. Rational CF caps are bounded above using Machin's formula for pi, alternating arctangent series, and an alternating cosine upper truncation; the square-root endpoint is rounded outward. Leaves cover the enlarged u interval exactly.

PROVED cancellation and operator bound: integrating the pointwise inequality gives

    integral_0^1 phi(w^2) <= integral_0^1 a(t)w(t)dt,

because integral B(2t,w(2t))dt is exactly one half of integral B(t,w(t))dt and B(t,0)=0. For T_a with kernel a(|x-y|) on [0,1], the right side equals (1/2)<G,T_a G>. The positive Schur function is U(x)=1+(4/5)x(1-x). Exact integration of the piecewise constant kernel against this quadratic gives cubic row polynomials. On every cell the certificate proves

    (T_a U)(x) <= (1333/5000) U(x).

The weighted inequality 2G(x)G(y)<=G(x)^2 U(y)/U(x)+G(y)^2 U(x)/U(y), integrated against the nonnegative symmetric kernel, implies <G,T_a G><=1333/5000. Thus D<=1333/10000. The proof uses neither the Beckner split nor a claimed numerical value of the GRR constant.

PROVED independent verification completed: independent_verify.py reconstructs every beta from the rational Bernstein coefficients in SymPy QQ, checks its power form, recomposes with FLINT, and independently verifies all 527 pointwise leaves and all 127 nontrivial CF caps. It uses a different arctangent truncation for the pi bound. It reconstructs each Schur cubic by Lagrange interpolation of FOUR direct exact row integrals, rather than the certifier's symbolic clipping formulas. All 64 continuum cells pass with the same strictly positive minimum margin. independent_verification.json records checks, source/certificate SHA256 values, Python 3.12.3, SymPy 1.14.0, and runtime. The theorem is therefore independently computer-assisted exact, still not Lean-kernel checked.

PROVED independent-check correction: an initial verifier required the numerical minimum of two Bernstein representations to be identical. The certifier retains some zero high-power coefficients, hence uses a higher Bernstein degree; the independent reconstruction trims them. Degree elevation changes Bernstein lower bounds even for the identical polynomial. The final verifier requires each independently recomputed lower bound to be nonnegative, not equal to the discovery representation's lower bound. All 527 independent bounds pass at the lower degrees; no certificate coefficient or theorem constant was changed for this correction.

PROVED final fourth-moment detail: the direct third-profile construction has an explicit fourth-moment divergence, with no approximation diagonal. The earlier signed-PD-span diagonal had an unproved total-variation step and is superseded. The delivered theorem uses only the direct continuous cube-root profile, sparse Riemann sums, and the l1 minimum bound.

## Final numerical record and binary tests

NUMERICAL direct-correction probe (third_direct.py, seed 2026101910): for the triangular generator w(t)=1-t, the required cubic profile is s(t)=((1-t)^2/4)*sqrt(1-(1-t)^2), with integral pi/64. The direct gadget has the following tested normalized moments. FFT minima are numerical; all-circle lower bounds come separately from the exact l1 inequality and 180-bit Arb enclosures of its algebraic inputs.

| X | L | second | third | fourth |
| --- | --- | --- | --- | --- |
| 4096 | 776 | 0.011877592 | 0.043330807 | 0.16390896 |
| 65536 | 7131 | 0.006056563 | 0.046525225 | 0.36935790 |
| 1048576 | 65536 | 0.002982318 | 0.047959032 | 0.79609884 |

PROVED target integral: substitute u=1-t and then u=sin(theta) to obtain integral s=(1/4)integral_0^1 u^2 sqrt(1-u^2)du=pi/64. The limiting second moment is zero and the fourth moment diverges by the theorem, not by extrapolating this table.

NUMERICAL full weighted example at X=65536, J=21618: the uncorrected random packet residual has mean cube 0.00032955 versus the binary requirement 0.04908738. The direct correction changes it to 0.05347118 at this finite size; the first raw moment is 0.10737479 versus target 0.10729711, the second 0.11289166, and the third 0.11363462. The fourth is 0.54905997 versus binary target 0.10729711. Its sampled minimum is -62.42383, while the exact ideal construction has the analytic global lower bound enclosed by -107.2451649720397702636... from nonnegative base packets plus the l1 correction. These finite deviations are preserved, not described as exact finite moment matching.

NUMERICAL failed one-positive-PD-family construction (third_probe.json): at the same X and seed, a single triangular PD cubic gadget produces residual cube 0.03559417, raw fourth moment 0.38128620 and about 39.8 percent of coefficients outside [0,1]. It misses the required cubic shape, as predicted by the w^3 versus w^2*sqrt(1-w^2) mismatch. Both signs of the pure PD gadget were tested at X=4096,65536,1048576, with all numbers, FFT minima and analytic bounds preserved. This route is superseded by the direct arbitrary-shape gadget.

PROVED / NUMERICAL binarisation check: threshold rounding of the base weighted example yields n=6782 distinct positive frequencies, max A=46260, numerical R=2.07957079. Threshold rounding of the direct-cubic example yields n=6790, max A=64179, numerical R=2.08139946. The coefficient error energies divided by X are 0.05382397 and 0.05896194. Their exact saved frequency lists are rounded_base.txt and rounded_direct_cubic.txt. At the exact angles 2*pi*526017/1048576 and 2*pi*522559/1048576, respectively, 180-bit Arb gives rigorous negative values and proves R>2079/1000 and R>2081/1000. These point certificates rigorously reject the finite rounded candidates as small-R examples; they are NOT global minimum enclosures or an asymptotic impossibility theorem for every rounding scheme. The best rounded candidate was therefore checked beyond the FFT. No promising binary R->0 construction was found or asserted.

## Final deliverable, novelty, and handoff

PROVED Task 1 COMPLETE: P61(a) audited with no mathematical gap found; P61(b) repaired for every complex Hermitian generator by the reflected-translate formula. Its literal degree wording and physical-versus-coefficient positivity scope are clarified. The LLN and the actual P58 smoothing diagonal are supplied.

PROVED Task 2 COMPLETE: exact D1=1333/10000; T-dense(C) for every C<10000/1333, including 7.5. Certificate discovery used Gurobi on the VM; validity is established by exact rational Bernstein checks and the independent QQ/FLINT reconstruction. The constant c(C) is ineffective. Nothing is kernel-checked or externally scrutinized in this round.

PROVED Task 3 COMPLETE at the requested moment-reach/obstruction level: the first-three-profile weighted reach equals the second-order reach 1/D. The direct sparse cube-root correction proves this for every generator w, not merely the triangular example. The same correction fails the fourth profile; four raw binary moment profiles force normalized coefficient L2 binarity, and three suffice if coefficient nonnegativity is assumed. UNKNOWN: the exact four-profile reach, a physical positivity obstruction for every binary sequence, and a binary escape beyond 1/D. Neither a dense counterexample nor a proof of all-C T-dense is claimed.

PROVED new versus quoted: new to the grepped project record are the complex-generator repair to P61(b), the t-dependent support-coupled potential and exact Schur certificate giving T-dense(7.5), the arbitrary continuous cubic-profile sparse correction and the resulting third-order sharpness theorem, and the explicit fourth/nonnegative-third moment binarity handoff. The binarity polynomial identities are elementary and carry no external priority claim. Quoted inputs are P58's diagonal/compactness framework, P59's energy-PD and a<=1/2, P60's Catalan argument, P61's Gabor/Jensen reduction, the classical Boas-Kac-Krein factorization, the three-/four-point Gram branches, Egervary-Szasz, and elementary concentration/Riemann-sum facts. The inaccessible GRR full text and the decimal quoted in [Garrido-Persico-Zelent (2026)](https://arxiv.org/html/2609.02541v1) are NOT proof inputs to D1.

PROVED artifact map (all under tdense10_scratch):

| Artifact | Role |
| --- | --- |
| coupled_td.py / coupled_td_d10_K64_s0.2.json | Gurobi support-coupled discovery |
| certify_td.py / certificate_td.json | Exact rational reconstruction, all pointwise leaves and Schur cells |
| independent_verify.py / independent_verification.json | Independent QQ/FLINT/cap/Schur checks |
| coupled.py / coupled_d8_K12_s*.json | Failed t-independent potential probes, retained |
| coupled_td_d6_K32_s0.2.json / diagnose_td.py | Earlier 7.458 grid and missed-cusp diagnosis |
| third_probe.py / third_probe.json | Both-sign PD gadget probes and failed single-family construction |
| third_direct.py / third_direct.json | Direct cubic-profile probe, analytic/ball bounds and rounding evidence |
| rounded_base.txt / rounded_direct_cubic.txt | Exact finite failed binary candidates |
| final_check.py / manifest.json | Independent saved-candidate dip checks, exact exponent budget, source compilation and hashes |

PROVED reproduction commands (sequentially, maximum four VM cores):

    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -t 600 python .research/agents/tdense10_scratch/coupled_td.py 10 64 .2
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -t 600 python .research/agents/tdense10_scratch/certify_td.py coupled_td_d10_K64_s0.2.json 1/2000 1333/10000
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -t 600 python .research/agents/tdense10_scratch/independent_verify.py
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -t 300 python .research/agents/tdense10_scratch/third_probe.py
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -t 300 python .research/agents/tdense10_scratch/third_direct.py
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -t 120 python .research/agents/tdense10_scratch/final_check.py

HEURISTIC final strategic decision: discontinue cubic-resonance obstructions for unrestricted weighted coefficients, since the direct sparse correction refutes that route. Three distinct useful next lines remain: (1) improve the support-coupled certificate toward 8 or 8.57, with richer dilations or adaptive t cells; (2) attack coefficient nonnegativity/fourth-moment tightness together with physical positivity, which is the next binary-sensitive condition; (3) constructive search for bounded nonnegative weighted escapes with rounding error controlled in the one-sided sup norm, retaining actual binary error energy. The first concrete derivation is to impose the nonnegative polynomial defect a^2(a-1)^2 in a joint coefficient/packet model; an independent alternative is to add a third-dilation potential to the exact certificate. None of these next tasks is reported as done, and no unattended continuation is implied.

PROVED final verification checkpoint: final_check.py passed on the specified VM. All eight scratch Python sources compile; the independent certificate's SHA256 matches certificate_td.json; the exact exponent budget is l1 cost 7/15<1/2, amplitude 4/15, second-profile exponent -4/15, fourth-growth exponent 4/15, smoothing exponent -2/15, and base-minimum exponent 9/20<1/2. Independent 220-bit Arb evaluation of the SAVED integer sets again proves the two stated R lower bounds, with ball radii below 7.1e-58. manifest.json records all source/data/candidate hashes and versions. No root .research markdown, commit, subagent, LaTeX artifact, or local mathematical computation was created by this round. All three requested deliverables are complete at the precise scope stated above.
