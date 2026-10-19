# Round 9 T-dense report

PROVED final checkpoint (computer-assisted paper proof, not Lean-kernel checked): T-dense(C) for every C<4000000000000/576649461289=6.936623145469854..., including the exact rational C=6.9366. The new scalar constant is kappa<=749089/1000000. Both rational Bernstein and independent QQ/Sturm verification passed.

NUMERICAL / PROVED reach distinction: local Gurobi searches estimate C_9 about 7.267 for the two-profile relaxation; an exact 160-cell spectral-factor witness satisfies all windows and gives C_9<7.267398825422. Thus its rigorously certified interval is [6.936623145469854...,7.267398825422). The full macroscopic class has additional completely-positive covariance constraints; an exact all-window Horn counterexample proves these constraints are not redundant. Neither a global optimizer nor optimality of shape independence is claimed.

PROVED effective result: an explicit finite Gaussian-scale formula for c(C)>0 now covers EVERY C<4(2-.815276)/r0, with r0=4/(3sqrt(3)) or the elementary r0=.811. This includes all of Task 2's requested C<4/r0 range and the entire previous ineffective range, approximately 6.156 with Beckner. The added range up to 6.936623 remains ineffective here. Task 3 supplies a rigorous weighted packet formal escape and identifies its positive binary cubic-moment deficit; it is not an admissible integer set.

PROVED scope and conventions: f_A(x)=sum cos(ax), M=-min on the whole circle, n=|A|, X=max A. T-dense(C) asserts an absolute c(C)>0 for all nonempty finite sets of distinct positive integers with X<=Cn. This report and tdense9_scratch are the only intended write locations. No commits or subagents. Mathematical computation is restricted to DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2; optimization uses Gurobi.

PROVED source audit: read CLAUDE.md, the round-9 brief, the number-theory-research skill and experiment-design/arithmetic references, PROOFS P17, P31 and its quantitative constants, P40, P47/P48, P53-P56, P58/P59, NOTEBOOK continuations 10-11, E78-E79, and the round-8 report/certification code. P58/P59's compactness diagonal, energy-PD, rho<=.815276 and c(3) are quoted inputs. Targeted novelty greps of PROOFS.md were performed for the new scalar/Catalan reductions, covariance cone, supporting-line certificates, Gaussian regularization, and cubic residual moments. No external priority is asserted.

## Initial frontier (intermediate bounds below are superseded by the final checkpoint)

PROVED (quoted): every hypothetical dense counterexample sequence has continuous even p, supported in [-1,1], 0<=p<=1, p PD, e=p(1-p) PD, a=p(0)<=1/2, and density/energy P31 windows at every fixed theta>0. With r=4/(3sqrt(3)), quoted T-dense holds for C<4(2-.815276)/r; its constant is ineffective except at C=3.

CONJECTURED/OPEN: the supremum density over this class and whether additional higher-product or cross-filter limits impose further constraints on a shape-independent residual spectrum. Task 1 is the main effort. A sampled nonlinear optimum will not be called an exact macroscopic reach.

PROVED methodological observation: a nonzero continuous compactly supported PWL p on a uniform mesh cannot have both p and p-p^2 PD exactly. Its Fourier transform vanishes at all nonzero mesh aliases. If p is PD, that transform is nonnegative, integrable and entire, with only isolated real zeros. Its convolution with itself is therefore strictly positive at every real frequency. The Fourier transform of p^2 is that convolution divided by 2pi, so p-p^2 has a strictly negative transform at every nonzero mesh alias. The final method resolves this issue by taking the ENERGY profile q PWL and defining p through the exact nonlinear inverse, rather than interpolating p and e independently.

HEURISTIC current attacks: (1) audit cross and triple products with normalization and diagonal terms retained; (2) Gurobi profile/pointwise-potential discovery with exact verification after discovery; (3) extend P59.6 by an explicit averaging of the density window rather than its lossy single-window Gaussian comparison. Effective constants follow after the main macroscopic work.

## Task 1: first exact reductions and audit correction

PROVED (paper; internal novelty grep found no corresponding P17/P58/P59 statement): after ENERGY-PD gives a<=1/2, continuity gives p(t)<=1/2 everywhere. Hence

    p(t) = (1-sqrt(1-4e(t)))/2 = sum_{k>=1} Catalan(k-1) e(t)^k.

The series converges uniformly on [0,1/4] (including its endpoint), has nonnegative coefficients, and Schur products preserve PD. Thus e PD, 0<=e<=1/4 already imply p PD; treating their PD constraints as independent hides this useful parameterization. This does not remove the coupling: p is fixed by e, and its window constraints remain.

PROVED scalar reduction. Write e=e(0)q, q(0)=1, 0<=q<=1, q PD. The energy window at theta=0 says integral e <= (r/2)e(0). Since e(0)<=1/4,

    d <= (r/4) kappa,
    kappa = sup_q integral[1-sqrt(1-q)] / integral q,

where the supremum can first be taken over all nonnegative integrable continuous PD q. This is a relaxation, so every rigorous upper bound on kappa proves T-dense(C) for C<4/(r kappa). Support and all finite-theta windows must still be checked for an obstruction witness. Optimize a PWL energy q, then define p by the inverse above: this preserves the exact nonlinear identity and avoids the invalid simultaneous-PWL ansatz.

PROVED further surviving positivity, not present in the inspected PROOFS entries. For centered high-pass g>=-m, set h=g+m>=0. For any fixed k, real y_1,...,y_k, the matrix

    (1/X) integral h(x+y_i/X) h(x+y_j/X) dx/(2pi)

is completely positive: it is an integral of rank-one vv^T with v>=0. In the residual diagonal limit its entries are (1/2)integral_0^1 e(t)cos((y_i-y_j)t)dt. The finite-dimensional completely-positive cone is closed. Therefore the Fourier transform of e must generate completely-positive translation kernels, a stronger cone requirement than merely being nonnegative and positive definite in general (no claim yet that this constraint is strict for the optimizer found here).

PROVED explicit necessary tests: for every copositive k-by-k matrix B and every real y_i,

    sum_ij B_ij integral_0^1 e(t)cos((y_i-y_j)t)dt >=0.

The 5-cycle Horn matrix (diagonal 1, cycle edges -1, other off-diagonals +1) is copositive: on the nonnegative simplex the cycle edge sum is at most 1/4, by merging nonadjacent support vertices until the support is a clique of size at most 2. Thus the quadratic form is (sum v)^2-4 sum_cycle v_i v_(i+1)>=0. This supplies exact higher-positivity tests beyond ordinary pairwise product positivity. A shape-independent residual measure does not erase them. Sufficiency of these constraints and of all triple/higher-product limits remains OPEN.

PROVED first new quantitative certificate (VM exact rational output joint_a0.400_d8_exact.json): for a in [2/5,1/2], the joint three-/four-point Gram constraints certify integral p^2 <= (184189/250000) a integral p. The rational rectangle verification used 243860 leaves, depth at most 26, without unresolved boxes. Below a=2/5, the quoted .815276 inequality suffices. Combining the two ranges proves T-dense(C) for every C<5052976/769801=6.5640029... with r=.769801. This is a computer-assisted paper proof, not kernel-checked. An independent reconstruction and a shorter scalar energy certificate are the next checks; the discovery output is not itself the certificate.

HEURISTIC strategic review after two distinct attempts: the two-variable joint potential has already improved the proved range but is expensive to verify. The Catalan parameterization reduces the main variational problem to one PD energy profile and permits a much shorter univariate exact certificate. Continue that reduction and a PWL-energy search; retain the verified joint certificate as an independent fallback. The completely-positive kernel audit prevents calling the simpler variational class the full macroscopic method's barrier.

## Task 1: shorter scalar certificate

PROVED (exact rational Bernstein certificates, scalar_d12_exact.json). Every continuous even integrable nonnegative PD q on R with q(0)=1 satisfies

    integral [1-sqrt(1-q)] <= (376647/500000) integral q.

PROVED certificate mechanism: for x=q(t), y=q(2t), the quoted four-point Gram bound gives y>=max(0,2x^2-1,x-sqrt(1-x)). A monotone degree-12 polynomial beta with beta(0)=0 satisfies

    kappa*x - [1-sqrt(1-x)] + beta(y) - beta(x)/2 >=0,
    kappa=376647/500000=.753294.

Put x=1-u^2. The three active lower branches become 0, 1-u-u^2, and 1-4u^2+2u^4, so the entire certificate reduces to rational univariate polynomials. Exact Bernstein verification uses 2 leaves for beta' on [-1/100000,1], 3 leaves for the high branch u in [0,.366026], 1 leaf for the middle branch [.366025,.618035], and 3 leaves for the low branch [.618033,1] after dividing its endpoint factor 1-u. The intervals overlap, and the slight negative enlargement of the middle beta argument is covered by the monotonicity certificate. Integration cancels the beta dilation terms. beta(q) is integrable because beta(0)=0. Full coefficients are preserved in scalar_d12_exact.json; degree 4 and 8 give independently shorter weaker certificates.

PROVED consequence (paper, not kernel-checked): with r=769801/1000000>4/(3sqrt(3)), T-dense(C) holds for every

    C < 2000000000000/289943237247 = 6.8979018755... .

For the elementary r=.811 the same theorem holds for C<4/(.811*.753294). This supersedes the joint two-variable certificate (which independently proves at least 6.646 on its completed amplitude split). No exact value of the variational supremum is inferred from this upper certificate.

NUMERICAL current PWL-energy probes (local Gurobi ascent; three starts at each resolution all converge to the same stationary point): the relaxed ratio kappa rises .71406911 (B=40), .71479522 (B=80), .71502332 (B=160), suggesting a reach around 7.267. At B>=80 its optimal dilation would exceed the allowed support interval; the direct support-constrained density search is therefore required before interpreting this ratio as an admissible near-extremizer. The initial B=40 profile already has d=.137285 and C=7.28410 with sampled windows; an exact all-theta witness verifier is running. This explicitly corrects the naive use of a ratio optimum without the support constraint.

## Task 2: an explicit constant on the whole previously proved range

PROVED theorem (paper, not kernel-checked; quantitative inequalities below are intentionally coarse). Let rho=203819/250000. Use either r0=4/(3sqrt(3)), D=21 (quoted P31-N/Beckner), or r0=811/1000, D=1 (quoted elementary P31-E). For every real C with 1<=C<4(2-rho)/r0 choose any rational r with r0<r<1 and r*C<4(2-rho). Put

    X0 = ceil((D/(r-r0))^2)+100,
    g = 4(2-rho)/(r*C)-1,
    eta = min(1/1000,g/1000),
    J = ceil(10^8/eta^2), B=J, K=J^3,
    beta = min(eta/(4J),1/(X0+1))*K^(-J),
    c(C) = beta/100.

Then every nonempty A with X<=C*n satisfies M>=c(C)*sqrt(n). All parameters are explicit finite real/integer expressions. For C<1 there are no such nonempty sets. This proves explicit constants for every C<4/r0 as requested and, in fact, for every C<4(2-rho)/r0: approximately 6.156 with Beckner and 5.843 with elementary P31-E. The stronger round-9 range near 6.898 still has an ineffective constant here.

PROVED finite Nikolskii input: P31-N implies rho_L<=r0+21/sqrt(L+1), since 26r0<21 and (1+2/u)^3<=1+26/u for u>=1. Elementary P31-E implies rho_L<=.811+1/sqrt(L+1). Thus X>=X0 ensures rho_L<=r for every L+1>=X. For a completely rational X0 in examples, replace the Beckner r0 in this denominator by any verified rational upper bound strictly below r.

PROVED reduction to large X. M>=1/2 follows from any nonzero Fourier coefficient of f+M>=0. If X<beta^(-2), M/sqrt(n)>=1/(2sqrt(X))>beta/2>c. Hence suppose X>=beta^(-2) and M<c*sqrt(n). We then have s0=beta*X>=beta^(-1), M/s0<=c, M^2/s0<=c^2/beta, 1/s0<=beta, and X>=X0. Since C<7, n>=X/7.

PROVED finite Gaussian pigeonhole (quoted P59.6 with these parameters). Let a_m=1_A(|m|), a_0=0, k_s(m)=exp(-m^2/(4s^2))/Z_s, q_s=k_s*a, L_s=Fourier(k_s), and s_j=beta*X*K^j for j=0,...,J. The PD sequences Q_s=q_s+2M*k_s and the almost-monotonicity of L_s give some j<J, s=s_j, S=Ks, with

    sup_m |q_s(m)-q_S(m)| <=2/J+42c <= delta:=3/J.

Here all s_j<=eta*X/(4J). The quoted Gaussian bounds Z_s>=2s, Z_s<=4s+1, sum |u|k_s(u)<=4s, and the continuous derivative bound 3/S give

    sum_u k_s(u)|q_s(m-u)-q_s(m)| <=2delta+12/K = omega <=7/J.

PROVED binary and finite product consequences (same identities as P59.6, with new constants): for q=q_s, rvec=a-q, E=k_s*rvec^2 and A0=q(0),

    |E(m)-q(m)(1-q(m))| <=4omega,
    q(m)(1-q(m)) <= A0(1-A0)+8omega+2beta.

Also |q(m+1)-q(m)|<=2delta+3/S<=7/J and q(m)->0 at infinity. A discrete crossing of 1/2 therefore yields

    A0 <=1/2+sqrt(8omega+2beta+(7/J)^2) <=1/2+8/sqrt(J) <=1/2+eta.

PROVED robust doubly-positive lemma (new relative to the inspected record, and the key finite replacement for compactness). Extend the Gaussian convolution continuously:

    q_cont(z) = sum_m a_m exp(-(z-m)^2/(4s^2))/Z_s,
    Q_cont(z) = q_cont(z)+2M exp(-z^2/(4s^2))/Z_s.

Its Fourier transform is exactly a positive Gaussian times 2(f+M), so Q_cont is a continuous nonnegative integrable PD function on R. In particular the quoted rho inequality applies EXACTLY, without claiming q alone is PD:

    integral Q_cont^2 <= rho*(A0+M/s)*(2n+2M).

Completing the square in the Gaussian products and using the shifted unimodal sampling bound sum exp(-(m-u)^2/(2s^2))<=sqrt(2pi)*s+2 gives

    sum_m q(m)^2 <= (1+1/s) integral q_cont^2
                    <=2rho*A0*n+10beta*n.

The uniform omega bound and self-adjointness of k_s give

    |sum a_m*q(m)-sum q(m)^2| <=2n*omega,
    sum rvec_m^2 >=2n*(1-rho*A0)-10beta*n-4n*omega.

PROVED finite polynomial filter (needed: the Gaussian high pass itself has infinite Fourier support). Truncate k_s to |m|<=R=ceil(Js) and transfer its discarded mass zeta to the zero coefficient. The new kernel ktilde has nonnegative coefficients of total mass 1, its transform Ltilde is in [0,1] (Ltilde>=L_s), and zeta<=4/J by the first-moment bound. Thus T=(1-Ltilde)f>=-M has degree at most X+R. Write T=rtilde_0/2+gtilde, where gtilde has mean zero and gtilde>=-mtilde, 0<=mtilde<=M. Young's inequality gives

    ||rtilde-rvec||_2<=2zeta*sqrt(2n),
    |sum rtilde^2-sum rvec^2|<=16zeta*n,
    Eplus:=sum_(k>=1) rtilde_k^2 >=n*(1-rho*A0-100/J).

PROVED finite energy window at w=floor(Js). Put kappa_w(m)=(1-|m|/(w+1))_+ and W=sum kappa_w^2. The total variation of kappa_w^2 is 2, so convolution with k_s changes its l1 norm by at most 8s. On |m|<=w, |q(m)-A0|<=7/J. Since |rtilde^2-rvec^2|<=2zeta,

    (2/W) sum_(k>=1) kappa_w(k)^2 rtilde_k^2
        <= A0(1-A0)+55/J.

Here 4omega+7/J+2zeta<=43/J and 8s/W<=12/J. Applying P31 to gtilde with its finite degree, and using 4M^2/W<=1/J, gives the deliberately relaxed inequality

    t*(1-rho*A0-100/J) <= A0(1-A0)+60/J,
    t = 2n/[r*(X+R+w+1)].

PROVED final numerical-free contradiction. R+w+1<=eta*X, so

    2/[r*C*(1+eta)] <= t <=2/r<3.

For a in [0,1/2+eta], eta<=.001, the function F(a)=a(1-a)/(1-rho*a) is increasing and has derivative at most 4. Put F0=F(1/2)=1/[2(2-rho)]>.4. Since 1-rho*A0>1/2, the last energy window implies

    t <= F0+4eta+720/J <= F0*(1+12eta).

But g>=1000eta gives t>=F0*(1+g)/(1+eta)>=F0*(1+998eta). This is a contradiction. Every use of X, n, scale, Fourier degree, discarded Gaussian mass and regularizer is finite; no compactness or limiting profile is used in this theorem.

PROVED Lean handoff requirements. Reuse kernel-checked P31/P31-E, finite sums/Parseval, Young l1-l2, and the round-8 exact rational rho certificate (still to formalize). New analytic lemmas: continuous Fourier transform of a Gaussian and of its integer translate sum; Poisson/Jacobi-theta positivity and its periodization error; almost-monotone Gaussian multipliers; shifted Gaussian Riemann-sum upper bound; first moment and derivative bounds; absolute convergence and convolution self-adjointness. New finite steps: geometric-scale telescoping/pigeonhole, binary energy identity, crossing lemma, mass-to-zero truncation preserving transform in [0,1], and the rational final inequalities. Beckner is required only for r0=4/(3sqrt(3)); the elementary version uses no Beckner. No Lean verification is claimed.

## Completeness audit: what is and is not reduced to the two profiles

PROVED positivity ledger (all necessary statements, with their information content separated):

| Surviving statement | Shape-independent residual sigma_t=e(t)nu | Status of reduction |
| --- | --- | --- |
| Untwisted and P48/P53 twisted density transforms | p PD; an atom-free nu has no nonzero macroscopic twists | Quoted P48/P53 and local Bessel remain valid; they do not force a prescribed nonzero atom |
| Binary coefficient identity | total residual mass is exactly e=p-p^2 | Quoted P58 diagonal; essential nonlinear coupling |
| P31 windows for each Hf | marginal H(0)^2 p^2 + nu(H^2)e is front-loaded | e windows are necessary; p^2 windows already follow from p PD and P31, as explained below |
| Scalar correlation of each Hf+M | each tested energy marginal is PD | Reduces to e PD and the Schur-positive p^2 for this ansatz |
| Cross correlations of arbitrary finite families of nonnegative shifted/filtered functions | their joint covariance matrices are COMPLETELY POSITIVE, not merely PSD with nonnegative entries | Gives all copositive tests of Fourier(e); nu cannot remove this constraint |
| Nonnegative triple and higher products | nonnegative higher correlation tensors, with height-weighted normalizations and all mixed filtered versions | Not determined by p,e or by an unweighted second-order sigma; no completeness/sufficiency claim |
| Local Bessel, TL1, stable Gram | control any selected finite graded atom family and any actual bounded binary lift | Atom-free sigma avoids the selected-atom obstruction; applying the bounds uniformly to growing mesoscopic families still requires the missing completion theorem |

PROVED automatic p^2 windows: if p is continuous PD and supported in [-1,1], the sampled finite sequence p(k/X) is PD on Z. Its Fourier polynomial is nonnegative, so sum_(k>=1)p(k/X)cos(kx)>=-p(0)/2. Apply P31 to that polynomial, divide by X^2, and pass to Riemann sums. The result is precisely every P31 window for p^2. Thus extracting p^2 by filters near the central atom adds no constraint to this class.

PROVED general quadratic hierarchy: if B is any copositive matrix, integration of v(x)^T B v(x)>=0 for the nonnegative vector of shifted/filtered h's gives a necessary inequality. Complete positivity is its exact finite-dimensional dual formulation. Triple/higher products require extra tensors; in the purely mesoscopic regime their naive macroscopic normalizations can erase them (quoted round-8 L6 calculation), so retaining height tags is necessary. Listing pairwise products alone is not a completeness audit of all positivity.

CONJECTURED/OPEN verdict: shape independence has not been proved optimal for the adversary. The two-profile class is an explicitly identified relaxation, not the full macroscopic admissible class. The numerical reach near 7.267 and the exact witness are reported for this relaxation. Its true supremum is not certified by local Gurobi ascent. A strict completely-positive obstruction witness is being checked, rather than assuming that the new cone condition is redundant.

PROVED additional simplification of the audited relaxation (this strengthens the initial live frontier above). The density window is redundant once e is PD and has every energy window. Indeed p=p^2+e, the window functional is linear, and p^2 has every window automatically by the preceding PD sampling argument. Consequently the two-profile relaxation is EXACTLY equivalent to the following scalar class:

    q continuous, even, nonnegative, PD, supported in [-1,1], q(0)=1;
    (2theta/3) integral_0^1 q <= r(1+theta) integral_0^theta (1-t/theta)^2 q(t)dt
    for every theta>0.

At its density optimum one can take a=1/2 exactly: replacing e=e(0)q by q/4 preserves PD, support and all energy windows, and increases p=(1-sqrt(1-4e))/2 pointwise. Its new p is PD by the Catalan series and has the density windows by p=p^2+e. Thus

    sup d = (1/2) sup_q integral_0^1 [1-sqrt(1-q)],

for this scalar windowed class. This is an equivalence for the specified relaxation, not for the additional completely-positive/higher-product hierarchy. The earlier remark that p's windows still require independent checking is now superseded by this proof; explicit witness checks remain as independent validation.

## Task 3: a concrete two-scale formal escape and its precise binary gap

PROVED formal escape (weighted coefficients, emphatically not a Chowla set). Let X tend to infinity, J=floor(X^(9/10)), and choose independent uniform circle angles theta_j. Let F_X be the Fejer kernel of degree X, with kappa_X(k)=1-k/(X+1). Put

    c=1/sqrt(32J),
    g_X(x)=c sum_(j=1)^J [F_X(x-theta_j)+F_X(x+theta_j)-2],
    r_k=4c*kappa_X(k) sum_j cos(k theta_j).

Then g_X has mean zero, degree X, and g_X>=-m_X with m_X=2cJ=sqrt(J/8)=o(sqrt(X)). Its residual energy is mesoscopic: a Bernstein bound at an X^4 grid, followed by the Fejer derivative bound, gives sup g_X=O(X log X/sqrt(J))=o(X) with probability tending to one. For the grid bound each independent summand has range O(X), variance O(X), and mean 2; the threshold 100X log X and union bound suffice. The derivative error is O(JX^2/X^4) before multiplication by c.

PROVED local first/second moments, without a central-limit approximation. For distinct positive k,l,

    E r_k=0, E r_k^2=kappa_X(k)^2/4,
    E r_k r_l=0, Cov(r_k^2,r_l^2)=0,
    E r_k^4 <=3 kappa_X(k)^4/16.

The covariance identity follows directly from integral cos^2(kx)cos^2(lx)=1/4 for k!=l and independence of the angles. Hence every bounded macroscopic test of r converges in probability to 0, and every such test of r^2 converges to e(t)=(1-t)^2/4, with variance O(1/X). Countably many tests admit a diagonal realization.

PROVED choose

    p(t)=(1-sqrt(2|t|-t^2))/2  for |t|<=1, p=0 outside.

Here e=p(1-p), e is PD (the square of a triangle), and p is PD by the Catalan expansion. The sampled polynomial P_X=sum_(k>=1)p(k/(X+1))cos(kx) satisfies P_X>=-1/4 exactly by discrete PD. Therefore the weighted polynomial P_X+g_X has minimum at least -sqrt(J/8)-1/4=o(sqrt(X)). It has density profile p and total coefficient-square profile p^2+e=p. Its formal density is d=(4-pi)/8, so C_formal=8/(4-pi), about 9.32, beyond the numerical two-profile reach near 7.267.

PROVED this formal escape consists of actual nonnegative trigonometric polynomials after the stated constant shift. Thus every finite shifted/filtered positive-product inequality holds before taking limits, including the completely-positive covariance hierarchy and triple products. It is not an admissible binary sequence: its coefficients p+r lie outside {0,1}. Its shape-independent residual marginal is e(t) times Haar measure in the packet centers (the law of large numbers for bounded continuous filters). No claim of an integer-set realization is made.

PROVED the missing binary information is already visible in the third local coefficient moment. A genuine P58 diagonal has

    r^3 -> p(1-p)(1-2p),
    r^4 -> p(1-p)[1-3p(1-p)]

in macroscopic weak tests: expand (a-q)^j using a^j=a, and use strong convergence of q with bounded coefficients. The packet model instead has zero odd centered coefficient moments (rotation theta_j -> theta_j+pi/k makes each fixed r_k symmetric); in particular its expected coefficient cube is 0, while p(1-p)(1-2p)>0 on (0,1). For this model the sum of coefficient cubes also converges to zero in probability: nonzero cross-covariances can occur only on resonance lines m*k=n*l with positive integers m,n<=3, so there are O(X) possibly nonzero pairs, each bounded by the uniform sixth-moment estimate. The formal model therefore satisfies the binary FIRST/TWO moment identities and positivity but fails the full binary law.

PROVED quantitative skew forced by binary profiles. Using the quoted rho=.815276 bound and weighted Jensen,

    integral p(1-p)(1-2p)
      >= d*(1-rho/2)*(1-rho) >0,

because s=(integral p^2)/d<=rho/2 and 1-3s+2s^2 decreases on [0,1/2]. This is a definite macroscopic cubic deficit, not a vanishing correction.

CONJECTURED precise remaining mesoscopic target (not proved here): bound this positive local binary skew by the cost of phase-coherent resonances among the tall nonnegative packets, uniformly when the number of packets grows and their heights lie between sqrt(X) and o(X). A sufficient concrete inequality is sum_(k>=1) r_k^3 <= B(C) M^2+o(X) for the exact P58 smoothing diagonal of every binary sequence with X<=Cn; combined with the preceding positive lower limit it would prove T-dense for all C. No such bound is asserted, and the packet construction explains why a covariance-only or unweighted triple-product argument cannot establish it. The existing HBSC/HBCG completion route is a different sufficient formulation of the same unresolved binary-versus-packet compatibility problem; it is quoted, not renamed as a new theorem.

PROVED computation log correction: the first 160-cell Sturm/window batch completed its mathematical checks but failed while serializing a rational density enclosure with more than Python's default 4300 integer digits. No 160-cell certificate was claimed from that failed run. The witness evaluator now rounds enclosure sums OUTWARD to a fixed dyadic denominator after every cell, preserving exact inequalities and avoiding denominator growth. An independently constructed rational spectral-factor witness is being verified as a faster positive-definiteness certificate. The already delivered 40-cell exact witness is unaffected.

## Verified Task-1 witness and strictness of the audit

PROVED exact near-extremal witness: witness_B160_full_factor.json supplies 160 integer spectral-factor coefficients g_j and the rational PWL q with

    q_i = sum_j g_j*g_(j+i) / sum_j g_j^2,
    q(t) = linear interpolation at t=i*phi/160,
    phi=99998963/100000000,
    e=q/4, p=(1-sqrt(1-q))/2.

The interpolation symbol is exactly |sum g_j exp(ijz)|^2/sum g_j^2, so q and e are PD for every real frequency; p is PD by the Catalan proof. Every rational q_i is in [0,1]. Both density and energy windows are verified for EVERY theta>0 using exact rational Bernstein certificates, including theta>=1 via u=1/theta. The density integration uses outward rational square-root bounds, and its lower window uses just the first 8 positive Catalan terms. This is an exact nonlinear identity e=p-p^2, not interpolation of e independently of p.

PROVED witness values (the decimal is enclosed by rational bounds in the artifact): d=0.13760081482002123..., a=1/2, and 1/d<7.267398825422. It satisfies the windows with r=.7698, slightly smaller than 4/(3sqrt(3)), hence also with the actual Beckner value. No tiny negative Fourier dips are ignored: the spectral-factor identity is exact. The separate B=40 witness uses a positive Sturm symbol and provides an independent PD method.

NUMERICAL estimated reach of the TWO-PROFILE relaxation: approximately 7.267 at 160 cells. Direct density searches at B=40,80,160 give 7.27682, 7.26953, 7.26732 before the deliberate witness safety margin. Half-sine, triangular and seeded random starts agree at each resolution. Tight constraints are a=1/2, support length approximately 1, the theta->0 energy window, and zeros of the q-PD symbol. Density windows have substantial slack (about .036 in the normalized slack), consistently with their proved redundancy. These are local optima, not certified global upper bounds on density. The rigorous interval currently is 6.8979018755 <= C_9(two-profile) < 7.267398825422; further certificates below may improve its left endpoint.

PROVED the completely-positive condition is STRICT even inside the two-profile class WITH ALL WINDOWS. Put Lambda(u)=(1-|u|)_+, eps=1/1000, s=1/2 and

    q(t)=Lambda(t/eps)+[Lambda((t-s)/eps)+Lambda((t+s)/eps)]/2.

Its transform is eps*sinc(eps*y/2)^2*(1+cos(s*y))>=0; q>=0 and q(0)=1. Let e=q/4 and p=(1-sqrt(1-q))/2. Exact piecewise-polynomial/Catalan window certificates verify both windows for every theta>0 with r=.7698. Yet at y_i=4pi*i/5, i=0,...,4, the Horn copositive test is strictly negative:

    sum_ij Horn_ij * integral_R q(t)exp(i*(y_i-y_j)*t)dt
       = -0.001180318357773884... <0.

The sign is certified by 160-bit Arb ball arithmetic with radius below 4.1*10^(-49), independently of any sampled plot; cp_obstruction.py / cp_obstruction.json reproduce it. Rescaling q to e only multiplies the negative value by 1/4. Thus no choice of shape-independent nu makes this profile a genuine macroscopic residual covariance. This explicitly refutes the claim that every macroscopic positivity constraint reduces to p PD, e PD and their windows. It does NOT prove that the near-extremizer at C~7.267 violates a copositive test, nor that shape independence is suboptimal at its true optimum.

PROVED independent verification: independent_verify.py reconstructed each degree-4/8/12 scalar certificate over QQ and found zero Sturm roots with positive endpoint signs in all four required intervals. It also verified the derivative, crossing, pigeonhole and final rational constants in the effective theorem. A second method independently reconstructs the 160-cell witness from integer autocorrelations. None of this is Lean-kernel verification.

PROVED explicit examples from the general effective formula (conservative, not optimized): C=5 admits c=10^(-90045246770288816); C=6 admits c=10^(-8153483994615623237); C=6.15 admits c=10^(-12250021987257925557874), using r=.77 and the verified upper base .769801. The elementary version at C=5.8 admits c=10^(-147307970906420494701), using r=.812. For C=3 the quoted round-8 10^(-6000005) is much stronger than the uniform formula here and should be retained.

## Task 1 final strengthening: long Toeplitz certificates

PROVED new finite-moment supporting lines. For every normalized nonnegative PD q and every real t, each rational record in long_gram_bounds.json proves q(2t)>=m*q(t)+b. For that record, lambda_n>=0 and the exact polynomial

    T_2(z)-m*z-b-sum_(n=3)^24 lambda_n*T_n(z)

is nonnegative on [-1,1]. Integrate against the push-forward of q's Bochner probability measure under frequency times t, and use q(nt)>=0. The lambda_n terms have the required sign, so the supporting line follows. Discovery used a Gurobi LP on 4097 angles; validity was then established independently by exact rational Bernstein subdivision on the whole interval. There are 18 rational supporting lines. They encode longer Toeplitz/nonnegative-moment information than the three-/four-point branches alone.

PROVED strongest scalar certificate: using the maximum of these lines and the two quoted Gram lower branches, a monotone degree-24 beta certifies

    integral [1-sqrt(1-q)] <= (749089/1000000) integral q.

The rational polynomial check is preserved in long_scalar_d24_exact.json. Its leaves cover u in [0,1] exactly, each records an explicitly valid lower branch for q(2t), and the corresponding pointwise inequality has nonnegative exact Bernstein coefficients. The u=1 endpoint is divided by 1-u only on the zero-lower-branch cells. beta is verified increasing even on [-1/100000,1], so the slight interval enlargement of branch arguments is harmless. As before, the dilation potential cancels upon integration. The degree-8 and degree-12 long-potential certificates are weaker independent alternatives. Gurobi's finite-grid values are not used without the exact checks.

PROVED final round-9 theorem (computer-assisted paper proof; not kernel-checked): T-dense(C) holds for every

    C < 4000000000000/576649461289 = 6.936623145469854... .

For every such fixed C there exists c(C)>0 valid for ALL nonempty finite sets of distinct positive integers with max A<=C|A|, and M(A)>=c(C)sqrt(|A|). This theorem follows from the quoted P58/P59 compactness diagonal, energy-PD, the theta=0 energy window, and the new exact scalar inequality. Its constant is ineffective on the newly added range. In particular T-dense(34683/5000)=T-dense(6.9366) is a concrete rational consequence. With elementary r=.811, the exact reach is 4/(.811*.749089), computed in long_independent_verification.json.

PROVED current rigorous interval for the two-profile macroscopic reach is therefore

    6.936623145469854... <= C_9(two-profile) < 7.267398825422.

NUMERICAL best estimate remains about 7.267 at the tested resolutions. There is no certified global optimizer, no proof of equality with the autocorrelation subclass, and no claim that this is the full macroscopic class's reach. The strict Horn witness is the reason to preserve that distinction.

HEURISTIC final strategic review: discontinue further increases of the same single-dilation potential degree in this round; degree 24 and longer moment lines reduce the rigorous gap but do not address the translation-kernel complete-positivity condition. The useful next tests are a copositive separation oracle for the near-extremal q, a mixed-dilation potential retaining q(2t),q(3t) jointly, and a binary cubic-resonance bound for mesoscopic packets. The effective-constant extension and a Lean implementation of its Gaussian/Poisson lemmas are a separate concrete line. No unattended continuation is claimed.

## Final verification and handoff

PROVED independent final checks passed (long_independent_verification.json): all 18 degree-24 supporting-line polynomials have zero Sturm roots on [-1,1] and strictly positive endpoint values; beta's derivative has zero roots on its enlarged interval; all 29 rational leaves were reconstructed independently in SymPy and cover [0,1] without gaps; every branch-argument and Bernstein sign check passed. The concrete rational C=34683/5000 has margin

    4-r*kappa*C = 66734113613/5000000000000000 >0.

PROVED the elementary consequence is C<4000000000/607511179=6.5842409790... . The integer spectral-factor identity was independently reconstructed, and a separate 180-bit Arb integration gave

    d=0.1376008148200212229772238871762788134801027881590348

with ball radius below 4.5*10^(-53), strictly inside the saved rational enclosure. Exact rational comparison proves 1/d<7.267398825422. All source files compiled on the VM. manifest.json records source/data hashes and software versions; these checks are computer-assisted exact/ball proofs, not Lean or external human scrutiny.

NUMERICAL Task-3 probe, seed 2026101909, X=256,1024,4096, J=floor(X^alpha) with alpha=.5,.9: coefficient energy follows the analytic triangular-square profile, mean coefficient cubes fluctuate near zero, and roughly 40% of coefficients lie outside [0,1]. At X=4096, alpha=.9, the sampled mean r^3 is .00179 whereas the binary profile requires .04910; the global analytic lower bound is -15.17482 for P+g. FFT minima are labeled numerical; the global lower bound comes from the exact nonnegative Fejer packets and PD of p. packet_probe.json preserves every value and normalization.

PROVED new versus quoted: new in this round relative to the grepped project record are the Catalan parameterization/redundancy reduction; the scalar nonlinear DP inequality and its longer Toeplitz supporting-line certificates; T-dense(6.9366); the completely-positive covariance audit and strict all-window Horn example; the continuous-Gaussian robust DP lemma and explicit constants over the entire old range; and the packet/cubic-moment handoff. Quoted are P31-N/P31-E, P40, P48/P53-P56, P58's exact diagonal, P59's energy-PD and finite Gaussian pigeonhole, rho<=.815276, classical Schur products/Bochner/Poisson, and the Fejer identities. No external priority claim, general Chowla resolution or Epoch solution function is made.

PROVED artifact map:

| File in tdense9_scratch | Role |
| --- | --- |
| long_gram.py / long_gram_bounds.json / long_scalar_d24_exact.json | Strongest theorem discovery and exact certificates |
| long_verify.py / long_independent_verification.json | Independent QQ/Sturm/Bernstein/Arb verification |
| energy_profile.py / full_B{40,80,160}_*.json | Numerical local profile search, three starts each |
| exact_witness.py / witness_B160_full_factor.json | Exact PD and all-theta near-extremal witness |
| cp_obstruction.py / cp_obstruction.json | Strict completely-positive covariance obstruction |
| independent_verify.py / independent_verification.json | Shorter scalar certificates and effective-constant comparisons |
| packet_probe.py / packet_probe.json | Reproducible numerical check of the formal weighted escape |
| final_checks.py / manifest.json | Final sequential verification, source compilation, versions and hashes |
| joint_potential.py / joint_*json | Earlier independent joint-amplitude attempt, including clearly labeled unresolved cases |

PROVED reproduction commands (run sequentially on the specified VM, maximum two cores):

    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 480 python .research/agents/tdense9_scratch/long_gram.py 24
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 600 python .research/agents/tdense9_scratch/energy_profile.py full 40 80 160
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 180 python .research/agents/tdense9_scratch/exact_witness.py 160 full factor
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 120 python .research/agents/tdense9_scratch/cp_obstruction.py
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 300 python .research/agents/tdense9_scratch/final_checks.py

PROVED limits of the deliverable: the exact value of C_9 is not established; the reported numerical value belongs to the specified two-profile relaxation. Shape independence is not proved optimal. The newly added T-dense range has an ineffective constant, while the entire previous range now has explicit constants. The proposed mesoscopic cubic upper bound is CONJECTURED, and the weighted packet escape is not binary. No root-level .research markdown was edited, no commit or subagent was created, and no mathematical computation was run locally.

HEURISTIC first concrete next experiment: feed the exact 160-cell adversary to a copositive separation routine for translation kernels (start with Horn matrices and diagonal scalings, then higher-order copositive certificates), while retaining its exact spectral factor and all windows. If it survives, derive a mixed q(2t)/q(3t) potential; if it fails, optimize the CP-constrained energy class. In parallel the concrete formalization target is the finite effective theorem's Gaussian regularization and mass-to-zero truncation, with the same quantified statement. The longer-term construction test is whether packet centers can supply the mandatory positive binary cubic skew without paying a square-root negative minimum.
