# T-dense round 5: finite TL1, relation defects, and stability

**PROVED scope.** The task is the round-5 brief. Only this report and `tdense5_scratch/` are intentional writes. All calculations use `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2`. No commits, subagents, or LP/MILP are used. Circle measure is normalized. Paper proofs below are not kernel checked; novelty means beyond the supplied record, with external priority unchecked.

**CONJECTURED target, quoted.** For every real C >= 1 there exists c(C)>0 such that every nonempty finite A contained in the positive integers up to C|A| satisfies M(A)>=c(C)sqrt(|A|).

**PROVED main outcome.** The finite TL1 theorem below has completely explicit errors, uses no torus equidistribution, and applies to every finite binary word and every finite list of frequencies. Its direct additive approximation error is proportional to R/D, where R is the sum of the amplitudes. Its sharper form has error proportional to (R/sqrt(W))/D after division by sqrt(W). Thus it is uniform for bounded effective amplitude complexity at fixed positive density, but it does NOT establish the desired degree depending only on epsilon when the number of small spikes grows. An exact symmetric cyclic reduction connects this theorem to P40 without any large-sieve error. It proves a quantitative unbalanced-relation alternative with degree depending on the spike count. A separate dimension-independent stable Gram theorem reduces the missing uniformity to control of negative spectral mass in a binary joint lift. T-dense and QD-half remain CONJECTURED.

## 1. Finite TL1: definitions and complete theorem

**PROVED normalization correction.** P54 bounds the mass on Lambda union minus Lambda. If Lambda contains one representative of each non-self-conjugate pair, and W=sum over Lambda of |c_s| squared, the relevant energy is 2W. The proposed finite display in the notebook uses W but quotes the constant for 2W. With exact second-moment orthogonality alone, W <= p(1-p)/2; the nontrivial TL1 improvement is 2W <= (8/pi squared)p(1-p). At self-conjugate frequencies, such as pi, 2W double counts a character. The functional inequality below still bounds 2W with its relation errors, but that quantity should not be called the actual two-sided mass there.

**PROVED definitions.** Let Y>=1, let a_1,...,a_Y lie in [0,1], and put p=mean(a), b_m=a_m-p. Binary words are a special case. For arbitrary real angles x_1,...,x_S put

    c_s = mean_m b_m exp(i m x_s),
    W = sum_s |c_s|^2,  R = sum_s |c_s|,
    Z_m = sum_s conjugate(c_s) exp(i m x_s),  L_m = Re Z_m.

If R=0 all the assertions are immediate. Otherwise define

    d_Y(t) = mean_(m=1,...,Y) exp(i m t),
    B = mean |Z|^2 - W,
    B_abs = sum_(s != r) |c_s c_r| |d_Y(x_s-x_r)|.

Thus B<=B_abs, and |d_Y(t)| <= min(1, 1/[Y |sin(t/2)|]) <= min(1, pi/[Y ||t||_circle]). These formulas include all endpoint and near-collision errors. If all pair differences have circular distance at least delta>0, then B_abs <= pi(R squared-W)/(Y delta). No separation is assumed in the theorem.

Let T_d be the degree-d Chebyshev polynomial, T_d(cos t)=cos(dt). Define the finite rotation defects

    Delta_d = mean_m T_d(L_m/R)
              - mean_m mean_(phi uniform circle) T_d(Re(exp(i phi) Z_m)/R),
    U_D = sum_(d=1,...,D) |Delta_d| / d^2.

**PROVED explicit relation expansion.** Write T_d(u)=sum_t t_(d,t) u^t. Then

    Delta_d = sum_(t=1,...,d) t_(d,t)/(2R)^t
                * sum_(j=0,...,t; 2j != t) binom(t,j) M_(j,t-j),
    M_(j,k) = mean Z^j conjugate(Z)^k
            = sum_(s_1,...,s_j,r_1,...,r_k)
                [product conjugate(c_s_i) product c_r_i]
                * d_Y(sum x_s_i - sum x_r_i).

Only unbalanced j!=k appear. These are phase-coherent weighted unbalanced-relation counts of degree at most D, at resolution 1/Y. The absolute value is taken after summing the weighted terms in each Delta_d. This distinction prevents claiming a positive count from a canceling polynomial expression without an upper bound by positive counts.

**PROVED positive-count version.** Define Q_D as the maximum, over j!=k with 1<=j+k<=D, of

    sum_(ordered tuples) product |c_s_i| product |c_r_i|
         * |d_Y(sum x_s_i - sum x_r_i)| / R^(j+k).

Then U_D <= C_D Q_D, where

    C_D = sum_(d=1,...,D) 3^d/d^2.

Indeed the coefficient absolute sum of T_d is at most 3^d, by its recurrence, and the normalized binomial weights in the displayed expansion sum to at most 1. If every unbalanced tuple up to degree D has distance at least 1/(eta Y) from zero, then Q_D<=pi eta. This bound does not have an additional factor S to the power D: the tuple weights already sum to one. C_D is exponential in D, not in S. Brute-force enumeration is unnecessary for the coherent version: form Z in O(YS), then evaluate its moments or Chebyshev polynomials in O(YD squared) arithmetic operations. On a Fourier grid, Z is obtained by an FFT.

**PROVED finite TL1, main theorem.** For every Y,S,a,x and integer D>=1 as above,

    2W <= 2 env(p)/pi^2 + 2 B_abs
          + 32 R/(pi D)
          + (16/pi + 4p) R U_D.                           (FTL1)

Here env is exactly the concave envelope from P54. In particular the first term is at most (8/pi squared)p(1-p). Replacing U_D by C_D Q_D gives a wholly positive weighted-count inequality. Every term is explicit. The coefficient of the relation error R U_D is at most 16/pi+4, independently of S,Y,D. The direct additive error is R, not R squared; this scaling was checked against the CVaR identity before the final report.

**PROVED sharper equivalent estimate.** Let k_p=sqrt(env(p))/pi and

    e_D = R [8/(pi D) + (4/pi) U_D + p |Delta_1|].

Then

    W <= k_p sqrt(W+B) + e_D.                            (FTL1-sharp)

If W>0, K=R/sqrt(W), this implies

    sqrt(W) <= k_p sqrt(1+B/W)
               + K [8/(pi D)+(4/pi)U_D+p|Delta_1|].

Consequently fixed K and small B/W, U_D give the P54 constant with an approximation error O(K/D) in this last square-root estimate. No independence is required. The simpler additive form FTL1 has error 32 R/(pi D). For example, under R<=K0 p(1-p), it has exactly the requested form with epsilon_D=32 K0/(pi D), positive relation count R U_D, and large-sieve error 2B_abs. Alternatively, fixed K and a density bounded away from 0 and 1 give a relative epsilon_D tending to zero by FTL1-sharp. The unrestricted claim with epsilon_D independent of effective amplitude complexity is not proved.

### Proof of the finite theorem

**PROVED hinge majorant.** Fix lambda in [-R,R] and let theta0=arccos(lambda/R). The even periodic function

    h(theta)=(R cos(theta)-lambda)_+

has the absolutely convergent cosine series a0/2+sum_(d>=1) a_d cos(d theta). Its derivative has total variation at most 4R on the full circle: on [0,pi] the variation is at most 2R, including the jump at theta0. Two integrations by parts therefore give |a_d|<=4R/(pi d squared). More explicitly,

    a0 = (2/pi)(R sin(theta0)-lambda theta0),
    a1 = (2/pi)[R(theta0/2+sin(2theta0)/4)-lambda sin(theta0)],
    a_d = (2/pi)[(R/2)(sin((d-1)theta0)/(d-1)
                       +sin((d+1)theta0)/(d+1))
                       -lambda sin(d theta0)/d], d>=2.

The endpoint cases lambda=+/-R follow by continuity. Let P_(D,lambda)(u)=a0/2+sum_(d<=D) a_d T_d(u/R). Since sum_(d>D) d^(-2)<=1/D,

    |P_(D,lambda)(u)-(u-lambda)_+| <= 4R/(pi D), |u|<=R.

Thus P+4R/(pi D) is a polynomial majorant. This constructs the suggested CVaR majorant without an LP or an unproved approximation theorem.

**PROVED CVaR comparison.** For any finite real variable V let Lambda_p(V)=inf_lambda[p lambda+E(V-lambda)_+]. This is also the maximum E(qV) over 0<=q<=1, E q=p; sort the finitely many values, allowing a fractional last value. Let Lstar=Re(exp(i Phi)Z), with Phi independent and uniform. Its law is rotation invariant before taking the real part, and it is supported in [-R,R]. Taking a minimizing lambda for Lstar, the majorant and minorant errors give

    Lambda_p(L) <= Lambda_p(Lstar) + 8R/(pi D)
                   + (4R/pi) U_D.

P54's rotation/superquantile argument, which applies to any radial law, gives

    Lambda_p(Lstar) <= sqrt(env(p) E|Z|^2)/pi.

Finally E(bL)=W exactly, and E L=R Delta_1. Since 0<=a<=1 and E a=p,

    W = E(aL)-p E L <= Lambda_p(L)+p R |Delta_1|.

This proves FTL1-sharp. Apply 2 k_p sqrt(W+B) <= k_p squared+W+B, rearrange, and multiply by two. Use B<=B_abs and |Delta_1|<=U_D. This proves FTL1 with all stated constants.

**PROVED raw-amplitude transfer.** The brief writes raw coefficients chat_s=mean a_m exp(i m x_s). They equal c_s+p d_Y(x_s). If T=sum_s |d_Y(x_s)| squared, then

    sqrt(sum |chat_s|^2) <= sqrt(W)+p sqrt(T).

Apply FTL1 to W and then this inequality. Dropping T at frequencies near zero is invalid. For nonzero characters on an exact cyclic Fourier grid T=0, so the raw and centered coefficients agree. The same finite proof works for any probability weights on the sample points, with their exact exponential averages replacing d_Y. For a slowly varying profile one may apply the theorem on blocks with each block's actual mean; no profile approximation is needed for that assertion. A global energy comparison across blocks requires a separate identity, supplied below in the cyclic case.

### A radius-truncated version for arbitrarily many small spikes

**PROVED finite radial-tail refinement.** The maximum radius R can be replaced by any T>0 if the tail is charged explicitly. Define Delta_d(T) by the preceding formula with every normalization R replaced by T, and U_D(T)=sum |Delta_d(T)|/d squared. For D>=2 put

    q_D(T) = E(|Z|/T)^D,
    e_(D,T) = T [8/(pi D) + (4/pi)U_D(T) + p|Delta_1(T)|
                    + (9+(8/pi)C_D) q_D(T)].

Then, for every T>0,

    W <= k_p sqrt(W+B) + e_(D,T).                       (FTL1-tail)

This has no dependence on S or R except through the explicitly computed moments and relation counts. In particular it makes precise what extra balanced high-moment control is sufficient for a uniform many-spike theorem.

**PROVED tail proof.** Use the same degree-D polynomial on [-T,T]. Outside this interval, its absolute value is at most [2+(4/pi)C_D]T(|u|/T)^D, because |T_d(u/T)|<=3^d(|u|/T)^D for |u|>T and d<=D. The hinge is at most 2T(|u|/T)^D for lambda in [-T,T]. Thus the expectation error for either L or Lstar is at most 4T/(pi D)+[4+(4/pi)C_D]T q_D(T). Restricting the minimizing lambda for the rotation law to [-T,T] costs at most E(|Lstar|-T)_+<=T q_D(T), by integrating the derivative of the CVaR objective from its unrestricted minimizer to the clipped endpoint. Compare the two polynomial expectations and add the centering term. The constants sum to exactly those displayed. The relation expansion is still finite and exact even when |Z|>T.

**PROVED dimension-independent consequence under an explicit moment hypothesis.** Suppose W>0, D>=2, and

    (E|Z|^D)^(1/D) <= L0 sqrt(D W).

Choose T=6 L0 sqrt(D W). Then q_D(T)<=6^(-D), and C_D<=3^(D+1)/2. Therefore

    sqrt(W) <= k_p sqrt(1+B/W)
        + 6 L0 sqrt(D) [8/(pi D) + (4/pi)U_D(T)
                         + p|Delta_1(T)| + 13*2^(-D)].

The coarse constant 13 safely bounds the radial-tail coefficient. With B/W tending to zero, bounded L0, and sqrt(D)U_D(T) tending to zero, the approximation error is O(L0/sqrt(D)), uniformly in S. At density bounded away from 0 and 1 this yields the requested relative epsilon_D tending to zero. For arbitrary data, FTL1-tail retains q_D(T) as an explicit additional balanced-moment error, rather than incorrectly calling it a second-moment large-sieve error.

**PROVED obstruction to deriving that hypothesis from pair separation or small individual amplitudes.** On the two-dimensional torus take the distinct characters (1,j), j=1,...,S, with coefficients 1/sqrt(S). They have exact pair orthogonality, total squared amplitude 1, and maximal amplitude tending to zero. But

    E |sum_(j=1,...,S) exp(i(theta+j phi))/sqrt(S)|^4
        = (2S^2+1)/(3S).

This follows by counting ordered pairs with equal sums. It diverges with S. The set is genuinely graded, so the exact P54 theorem still holds; this example obstructs the attempted uniform high-moment deduction, not TL1 itself. It also explains why the Gaussian regime needs small higher additive energies as well as many small coefficients. The balanced cross terms of higher degree cannot all be dismissed using ordinary pairwise large-sieve separation.

**PROVED binary realization of the radial obstruction.** The preceding test polynomial can actually occur as a binary Fourier projection at density 1/2. For every S>=1 choose an odd integer q>2S. On K=T times Z/q times Z/2, with coordinates theta,r,e, let E be the following binary set: when r=0 use cos(theta)>=0; when r!=0 use e=0. Then |E|=1/2. The coefficients on Lambda={(1,j,0):1<=j<=S} are all exactly 1/(pi q): outside r=0 the theta integral vanishes, while on r=0 the half-circle coefficient is 1/pi. These characters have a genuine real grading and exact pair orthogonality. Their projection therefore has

    W = S/(pi^2 q^2),
    E|Z|^4 / W^2 = (2S^2+1)/(3S),
    max |c_s|/sqrt(W) = 1/sqrt(S).

The fourth-moment ratio is the same exact additive-energy count, because q>2S prevents wraparound of the pair sums. The pattern has density bounded away from zero, is binary, and has normalized individual amplitudes tending to zero, yet it violates every coefficient-uniform fourth-moment bound. This does NOT refute finite TL1: its captured mass tends to zero for q comparable to S, so it is not an exhaustion example.

**PROVED realization by actual finite words.** Fix an irrational alpha/(2pi) and put a_m=1_(cos(m alpha)>=0) for q dividing m, and a_m=1_(m even) otherwise. Along any length Y tending to infinity with S,q fixed, the empirical pattern equidistributes on this K: on each residue modulo 2q, the irrational rotation is uniform. Thus p tends to 1/2 and the coefficients at alpha+2pi j/q tend to 1/(pi q), with the preceding radial moment limits. Diagonal choice of sufficiently long finite words gives the same divergent normalized fourth moments as S grows. Their pair frequencies are separated by 2pi/q and hence separated at scale 1/Y once Y/q is large. This rules out deducing the radial hypothesis merely from binary values, fixed density, small amplitudes, and pair separation. An exhaustion-specific theorem could still be true; that extra hypothesis is material.

## 2. Gaussian regime: what is actually sufficient

**PROVED finite comparison.** Let L_ind=sum_s Re(conjugate(c_s) exp(i Phi_s)), with independent uniform Phi_s. Let

    V_D = sum_(d<=D) d^(-2)
              |E T_d(L/R)-E T_d(L_ind/R)|,
    rho = sum |c_s|^3 / W^(3/2),
    E_D = (R/sqrt(W))[8/(pi D)+(4/pi)V_D]
          + p |E L|/sqrt(W) + (7/3) rho^(1/3).

For W>0 and 0<p<1,

    2W <= [phi(Phi_inverse(1-p)) + sqrt(2) E_D]^2.        (GTL1)

Here phi and Phi are the standard normal density and distribution. For every 0<p<1,

    phi(Phi_inverse(1-p))^2 <= (2/pi) p(1-p).

Thus GTL1 has the sharp Gaussian leading constant 2/pi for all p; at p=1/2 its limiting bound is 2W<=1/(2pi). To prove the scalar inequality, write t=|Phi_inverse(p)|. For two independent standard normals, the square [-t,t] squared is contained in the disk of radius sqrt(2)t. Hence (2Phi(t)-1) squared <=1-exp(-t squared), by the elementary radial Gaussian integral. Rearranging gives Phi(t)(1-Phi(t))>=exp(-t squared)/4, exactly the desired inequality. Equality holds at t=0; for t>0 the disk strictly contains the square with positive Gaussian measure. This establishes the requested Gaussian constant in a precise many-small-amplitudes regime. Small total-degree unbalanced counts alone do not bound V_D: coordinate-balanced but nontrivial additive relations also enter the comparison with independent phases.

**PROVED elementary Lindeberg estimate used here.** Replace each r_s cos(Phi_s) by an independent normal of variance r_s squared/2. Smooth the hinge by convolution with a normal of standard deviation h. Its third derivative is bounded by 1/h squared; each smoothing changes its expectation by at most h. Taylor replacement, matching the first two moments, changes the smoothed expectation by at most sum r_s cubed/(3h squared), since each of the two third absolute moments is at most r_s cubed. With h=(sum r_s cubed)^(1/3), the total error is at most (7/3)(sum r_s cubed)^(1/3), uniformly in lambda. The same Chebyshev comparison as above transfers the empirical law to L_ind. A normal of variance W/2 has top-p integral sqrt(W/2)phi(Phi_inverse(1-p)). Divide the resulting inequality for W by sqrt(W). No central limit theorem with unstated uniformity is being invoked.

## 3. Exact P40-to-TL1 reduction on a cyclic grid

**PROVED symmetric-padding reduction, new relative to the record.** Let A be contained in [1,X], n=|A|, and take an even integer Y>2X. On the cyclic group Z/YZ let a be the indicator of A union (-A), and p=2n/Y. With the Fourier convention of Section 1, its nonzero coefficients are real:

    c_k = 2 f_A(2pi k/Y)/Y,  k!=0,
    c_0 after centering = 0.

They satisfy sum_(k!=0) c_k squared=p(1-p). Choose Lambda to consist of the representatives 1<=k<Y/2 for which f_A(2pi k/Y)>H. Put W=sum_Lambda c_k squared and R=sum_Lambda c_k. Every selected c_k is positive. Distinct selected characters are exactly orthogonal, so B=0 and E L=0. The self-conjugate character k=Y/2 is handled separately: if it is tall it already has a torsion relation of degree two; denote its squared mass by T_N, and otherwise put T_N=0.

The finite uniform distribution on the Y sample angles has mean f=0 and mean f squared=n/2. The P40 proof is an elementary bounded-variable argument and therefore applies unchanged to this distribution. If M=M(A),

    2W >= p(1-p) - (4/Y)(HM+2M^2) - T_N.               (CY1)

The central character is removed exactly; the grid has no aliasing because Y>2X. This uses the symmetric indicator of +/-A, not the nonsymmetric indicator of A. The latter has an imaginary Fourier component that P40 does not control and would not justify the inference.

**PROVED global finite relation alternative.** Put alpha=8/pi squared and gamma=1-alpha. For every integer D>=1, CY1 and FTL1 give

    R U_D >= (pi/16) [gamma p(1-p)
                    - (4/Y)(HM+2M^2) - T_N
                    - 32 R/(pi D)].                    (CY2)

A negative right-hand side makes no assertion. This is an actual structural necessary condition, without local-window passage, torus equidistribution, or large-sieve errors. R U_D is degree one in the Fourier amplitudes, which themselves arise from a fixed [0,1] signal; no artificial homogeneous degree-two interpretation is intended. Multiplication by Y squared places the necessary lower bound on a scale comparable to n squared at fixed density and Y comparable to X. If raw Fourier amplitudes are used, this multiplies the resulting normalized relation expression by an additional factor Y; that factor must be stated.

If the P40 error plus T_N is at most gamma p(1-p)/4, and

    D >= 64 R/[pi gamma p(1-p)],

then CY2 gives R U_D >= pi gamma p(1-p)/64. Also R<=sqrt(S W)<=sqrt(S p(1-p)/2), so D>=64 sqrt(S)/[pi gamma sqrt(2p(1-p))] is sufficient. In the cyclic case each M_(j,k) is a nonnegative weighted count of EXACT modular relations; the positive coefficients prevent phase cancellation inside M_(j,k). Hence CY2 also gives

    R Q_D >= pi gamma p(1-p)/(64 C_D).

**PROVED exact degree obstruction in this proof, not an impossibility theorem for other methods.** Parseval gives S<=Yn/(4H squared). At H=sqrt(n/epsilon), this is O(epsilon X) when Y is comparable to X. The sufficient degree above can therefore grow like sqrt(epsilon X), not merely as a function of epsilon. Declaring D=D(epsilon) here would be an unproved uniformity step. Likewise replacing R U_D by a count formed only from the masses |c_s| squared discards the square-root weights and phases; it needs a separate comparison.

**PROVED counterexample-sequence interpretation.** If M/sqrt(n)=epsilon tends to zero at fixed C, choose even Y between 8X and 16X and H=sqrt(n/epsilon). Then p is bounded above by 1/4 and below by 1/(8C). The P40 error in CY1 divided by p(1-p) is O_C(sqrt(epsilon)). Either the self-conjugate tall character already gives degree-two torsion, or the positive-count conclusion above holds with its displayed, possibly growing degree. This is weaker than the requested uniform short-relation theorem; it is not a proof of it.

**PROVED short-degree theorem with an explicit additional radial hypothesis.** There is a useful stronger conditional alternative, without S. Fix C and L0>0, put v0=3/(32C), alpha=8/pi squared, gamma=1-alpha, and

    g0 = [sqrt(1-gamma/4)-sqrt(alpha)]/sqrt(2) > 0.

Choose any integer D>=2 for which

    6 L0 sqrt(D) [8/(pi D)+13*2^(-D)] <= g0 sqrt(v0)/2.

Such a D exists and depends only on C,L0. In the cyclic reduction with 8X<=Y<=16X, assume its low-energy loss plus T_N is at most gamma p(1-p)/4. Then at least one of the following holds:

    (E |Z|^D)^(1/D) > L0 sqrt(D W),
    U_D(T) >= g0 sqrt(v0)/[12 L0 sqrt(D)(4/pi+1)],
        T=6 L0 sqrt(D W).

For proof, p(1-p)>=v0, W is between (1-gamma/4)p(1-p)/2 and p(1-p)/2, and the gap between sqrt(W) and k_p is at least g0 sqrt(v0). Apply FTL1-tail with B=0. The displayed choice of D pays at most half this gap; the relation term must pay the other half. Thus a counterexample has either a fixed-degree unbalanced relation defect or an explicitly large balanced radial moment. The latter cannot be discarded using pair separation, as the graded (1,j) example proves. This is a proved three-way reduction after including the initial P40 error, rather than the requested unconditional two-way dichotomy. It identifies precisely which extra case the present finite-moment proof leaves open.

**PROVED central-cluster limitation.** The cyclic result concerns all tall nonzero grid characters. Removing k=0 removes the mean, not the whole central lobe: the nearby nonzero grid points remain and can themselves have relations k+k=2k. CY2 therefore need not locate its relation mass outside the already-known central or fixed rational clusters. Removing a central cluster and invoking the fixed-J residual theorem does not repair this automatically: that theorem supplies a positive residual fraction, not exhaustion of the full global variance by the remaining characters, and TL1's budget cannot be reused without localization. This is a second reason that CY2 is not the proposed noncentral dichotomy or HBCG.

**PROVED exact finite profile identity, additional new bookkeeping.** Let a_m be any finitely supported binary sequence on the integers, let N=sum a_m, and let F(x)=sum a_m exp(i m x). For an integer block length Y>=1 and every integer t, put

    p_t = (1/Y) sum_(t<m<=t+Y) a_m,
    q_(t,s) = (1/Y) sum_(t<m<=t+Y) a_m exp(i m x_s),
    c_(t,s) = q_(t,s) - p_t exp(i t x_s)d_Y(x_s).

Only finitely many blocks are nonempty. Counting the Y-|m-r| blocks containing each pair m,r gives

    sum_t p_t = N,
    sum_t p_t^2 = integral |F(x)|^2 |d_Y(x)|^2,
    sum_(t,s) |q_(t,s)|^2
        = integral |F(x)|^2 sum_s |d_Y(x-x_s)|^2,
    sum_t p_t(1-p_t) = N-integral |F(x)|^2 |d_Y(x)|^2.

Apply FTL1 to each block's c coefficients and write its additive error as Err_t. For every zeta>0, the squared triangle inequality then proves

    2 integral |F|^2 sum_s |d_Y(x-x_s)|^2
      <= (1+zeta) [alpha sum_t p_t(1-p_t)+sum_t Err_t]
         + 2(1+1/zeta) [sum_s |d_Y(x_s)|^2] sum_t p_t^2.

These are exact identities and an explicit inequality; they require no slowly varying profile. With a=1_(A union -A), F=2f_A and N=2n, so they retain precisely the cosine energy relevant to P40. They explain how a local TL1 would enter a capture proof. What is not proved is that its summed relation, balanced-overlap, radial-tail, and centering errors stay small for an arbitrary cover with J growing like Xn/H squared. Dense coverage of windows of width 1/X and the small large-sieve error needed for the same block length cannot simply be assumed simultaneously. The global cyclic trick avoids pair overlap but, as just explained, does not remove whole central profiles.

## 4. Structured side: proved subcases and the exact inverse-theorem gap

**PROVED fixed-period family.** Fix q>=1 and a nonempty residue set R0 modulo q, let d=|R0|/q, and put A_X={1<=m<=X:m mod q belongs to R0}. For every X with A_X nonempty,

    M(A_X) >= 2d X/(3pi) - (q+1)(1+3pi/2).

Indeed the prefix discrepancy of 1_(A_X)-d is at most q. Abel summation at x=3pi/(2X) bounds its cosine sum in modulus by q(1+3pi/2). The error between sum_(m<=X) cos(3pi m/(2X)) and X times its integral is at most 1+3pi/2. The integral is -2/(3pi). Thus every fixed full residue pattern has linear M with explicit constants. Fixed regular Bohr windows have family-dependent linear M by the corrected P53 corollary, quoted from round 4. These are valid landing zones only if the extracted pattern meets their hypotheses.

**PROVED dilation step, quoted and made explicit.** Averaging f_A(x+2pi j/q) over j gives f_D(qx), where qD=A intersect qZ. Thus M(A)>=M(D). At x=0 the same averaging and f>=-M give |D|>=n/q-(1-1/q)M. If P31 supplies M(D)>=c sqrt(|D|) for that actual residue core, then, whenever M<=n/[2(q-1)] for q>1, M(A)>=c sqrt(n/(2q)). The q=1 case is immediate. This establishes a fixed-q reduction when the core meets P31's profile hypothesis. A residue atom alone does not establish that hypothesis.

**PROVED obstruction to the shortcut “torsion spike implies linear M.”** Genuine Bu sets have f_A(2pi/3)=n/4 exactly, as recorded in round 4, while their construction has M=O(sqrt(n)) along the quoted Bu family. Thus torsion spikes are compatible with sublinear M and a fractional joint residue pattern. They must not be conflated with a full binary residue pattern. This also refutes the brief's literal assertion that Bu sets have no tall spikes. The contradiction hypothesis M<=epsilon sqrt(n) with epsilon tending to zero is absent in these examples, so the correct dichotomy can remain vacuous on them.

**PROVED external theorem, quoted with verified constants.** Reiher--Schoen, Theorem 1.2, states: if a finite nonempty subset B of any abelian group has additive energy E(B)>=|B| cubed/K, K>=1, then for each delta in (0,1/2) there is Bprime contained in B with

    |Bprime| >= (1-delta)|B|/sqrt(K),
    |Bprime-Bprime| <= 2^33 delta^(-9) K^4 |Bprime|.

The exact constant and hypotheses were checked in the authors' [paper](https://arxiv.org/html/2308.10245v1), Theorem 1.2. This is an ordinary unweighted quadruple-energy theorem, not a theorem about an arbitrary weighted, unbalanced relation of degree D.

**PROVED external theorem, quoted with its published dependence.** Green--Ruzsa, Theorem 1.1, states that |B+B|<=K|B| in any abelian group implies containment in a coset progression of dimension at most C K^4 log K and size at most exp(C K^4 log squared K)|B|, for an absolute constant C. See the authors' [paper](https://arxiv.org/html/math/0505198v1), Theorem 1.1. C is not numerically specified in that statement. It must not be replaced by an invented numerical constant. One may safely use log(2K) in the upper bounds to include K=1. The subgroup component is essential in a cyclic group; its order need not be bounded by D. Applying the standard sum/difference-set inequality |B+B|<=|B-B| cubed/|B| squared to the BSG output gives an available sum-doubling parameter at most (2^33 delta^(-9)K^4) cubed, before the Freiman bound. This already raises its rank dependence to an absolute constant times delta^(-108)K^48 times a logarithm.

**PROVED hypothesis audit / remaining gaps.** CY2 is not E(B)>=constant |B| cubed. To invoke those results requires: converting the weighted count into bounded-weight levels without losing all fixed mass; converting general j!=k relations to quadruple energy; and retaining the actual local binary pattern when passing to the extracted structure. A naive amplitude dyadic decomposition has up to 1+log2(n/H) levels, which grows with X; its largest level need carry only the reciprocal of this many levels of energy. Near-relations off a cyclic grid add a discretization issue. The exact cyclic reduction removes that last issue but does not remove the first three. No BSG invocation is justified solely by the word “structured.”

**PROVED limited counterexample to an overstrong qualitative inference.** In the free abelian group with basis e_1,...,e_r, the set {e_i,2e_i:1<=i<=r} has a short unbalanced relation e_i+e_i=2e_i for every i. With equal masses, a subgroup of rank k carries at most k/r of the mass: a rank-k rational subspace contains at most k of the coordinate axes. Hence existence of many individual short relations is not a bounded-rank mass-extraction theorem. Its normalized cubic count decreases with r, so this example does not refute a correctly quantified positive-density weighted inverse theorem. Even bounded rank is insufficient to preserve binary limits when window features become arbitrarily fine: the sets {omega:cos(k omega)>=0} on one circle converge weakly to density 1/2 as k tends to infinity. P53's binary conclusion therefore needs capture of the relevant harmonics or a complexity bound, not rank alone.

**HEURISTIC strategic decision after two attacks.** The finite rotation method advances the exact analytic inequality; the cyclic reduction advances its connection to P40. The inverse-theorem audit shows that neither “short relation” nor “fixed rank” completes the structured half. Discontinue attempts to get a proof by merely naming BSG/Freiman or by replacing the degree error with an unspecified o(1). Pursue a dimension-independent stability estimate retaining the binary bound. The next section proves the part of that estimate which is genuinely dimension independent and isolates the missing spectral completion.

## 5. QD-half: a dimension-independent stable Gram theorem

**PROVED stable defect lemma, new relative to the supplied record.** Let K be any compact abelian group. Let h be a continuous real function on R times K, with 0<=h<=1 and h(t,omega)=0 for |t|>1. Suppose h is the Fourier--Stieltjes transform of a finite real signed measure nu on the dual group; let delta be the total mass of its negative part. Put m=integral_(0<t<1,K) h and b=integral h(1-h). Then

    h(t,omega) <= 1-t^2/4+2delta, 0<|t|<=1,
    b >= m^3/12-2delta m.                               (SG)

There is no rank, torsion, or J in this statement. In particular delta<=m squared/48 implies b>=m cubed/24. The exact delta=0 case is the round-4 bound, quoted rather than claimed new.

**PROVED proof of SG.** Symmetrize the Jordan parts under inversion, which preserves positivity and their masses, so their transforms hplus,hminus are real positive-definite functions and |hminus|<=delta. Write a=hplus(0,e); since h(0,e)<=1, a<=1+delta. For z=(t,omega), let N=floor(1/|t|)+1, so h(Nz)=0 and hplus(Nz)=hminus(Nz)<=delta. The Gram triangle inequality for hplus gives

    a-hplus(z) >= [a-hplus(Nz)]/N^2 >= (a-delta)/N^2.

Consequently h(z)<=a(1-1/N squared)+delta/N squared+delta <=1-1/N squared+2delta <=1-t squared/4+2delta. Multiply 1-h>=t squared/4-2delta by h>=0 and integrate. Since 0<=integral_K h(t,omega)<=1 and its total mass is m, filling the earliest t first gives integral t squared h>=m cubed/3. This proves SG. The argument also handles a-delta<0; no division by it is made.

**PROVED quantitative consequence conditional on a binary spectral lift.** Suppose a finite reconstruction at complexity J produces such h with m=n/X>=1/C, negative spectral mass delta<=L_J M/X, and captured cosine energy <=(X/2)integral h squared. Then SG gives

    residual cosine energy >= X m^3/24 - L_J m M.

For M<=X/(48 C squared L_J), it is at least X/(48 C cubed). Thus the required eta is explicitly 1/(48 C squared L_J) IF that reconstruction bound holds. This is a conditional formula, not a proved rate in J. No such L_J estimate is supplied by P53 compactness.

**PROVED obstruction to the naive estimate.** A pointwise lower bound -M/X for each of J Fourier components on a y-interval of length 2B bounds their total negative spectral mass only by a constant times J B M/X. The Lebesgue length and the component count both have to be included. Cauchy--Schwarz does not automatically turn this into sqrt(J)M/X: the L2 norm of a function bounded by M/X on a set of measure proportional to J B already has the factor sqrt(J B), which is multiplied by sqrt(J B) in the L2-to-L1 conversion. Pointwise negativity bounds alone therefore retain a linear J loss. The old singular-profile and joint-PD examples remain pertinent to extraction; SG does not presume they are binary lifts.

**CONJECTURED single sufficient missing lemma, height-uniform binary spectral completion (HBSC), asymptotic form.** For every C>=1 there is B(C)<infinity with this property. For every sequence X_j tending to infinity, A_j contained in [1,X_j] with n_j>=X_j/C and M(A_j)/X_j tending to zero, every choice sqrt(n_j)<=H_j<=n_j, and every union U_j of at most ceil(3pi X_j n_j/H_j squared) radius-1/X_j windows with f_Aj(center)>H_j, there are compact abelian groups K_j and continuous functions h_j as in SG, with finite signed Fourier measures, for which

    integral h_j = n_j/X_j + o(1),
    delta_j <= B(C) M(A_j)/H_j + o(1),
    integral_Uj f_Aj^2 <= (X_j/2) integral h_j^2 + o(X_j).

All little-o terms refer to the chosen sequence and must hold despite its growing window count; no ineffective fixed-J substitution is allowed. This is one reconstruction lemma, not three independently proved facts. Its substantive requirements are retention of 0<=h<=1 and the negative spectral mass bound uniformly in H and the number of windows. Its scope is deliberately M=o(X), the regime needed for the contradiction. Requiring a continuous supported h of mass exactly n/X for EVERY A would already fail for the full interval n=X, since such an h cannot have mass 1. The asymptotic mass condition and the small-M hypothesis avoid that elementary false strengthening. HBSC is stronger than the needed asymptotic capture inequality and is not claimed equivalent to it. Empty unions and H>n need no completion, since their residual is the full n/2.

**PROVED HBSC implies HBCG asymptotically in the needed small-M/H regime, and hence T-dense.** By SG and the total cosine energy n/2, HBSC gives residual >=X/(24 C cubed)-B(C)XM/H-o(X) along sequences with bounded M/H. In a hypothetical counterexample sequence choose H=sqrt(n/epsilon), epsilon=M/sqrt(n) tending to zero, and use the separated-window cover from round 4. The quoted elementary lower bound M>=1/2 ensures H=o(X) and H<=n eventually, so the stated HBSC range applies. P40 gives residual o(X); HBSC gives a fixed positive multiple of X. This contradiction proves T-dense conditionally. The same reconstruction at measure mu, with delta bounded by a constant times M sqrt(mu/n) plus a vanishing error, would give QD-half for sufficiently small threshold constants. No such completion has been proved here.

**PROVED best unconditional dependence recorded.** The actual finite-window result remains: for each fixed C,J,K there exist eta(C,J,K)>0 and X0(C,J,K), with residual >=X/(48 C cubed). No explicit numerical rate of eta in J is proved in this report or in round 4. SG improves the stability mechanism but does not provide the missing finite lift. A multiscale iteration with a fixed loss per step remains inadequate; no summable-loss recurrence has been established. This is the exact nonclosure, rather than a claim that the existing compactness proof has an effective J-uniform rate.

**PROVED correction to the claimed scale-sharpness evidence.** Singer at mu=1 cannot distinguish powers of mu, since every power equals 1 there. There is a simple direct sharpness obstruction for any proposed exponent beta>1/2. Take A={1,...,n}. Its cosine sum has |f(x)|<=1/[2|sin(x/2)|]+1/2 away from zero, so for a central interval of normalized measure mu,

    E_out(A;mu) <= constant/mu,  0<mu<=1.

Indeed f=(D_n-1)/2, D_n=sin((n+1/2)x)/sin(x/2), and integration of x^(-2) outside |x|>=pi mu gives this bound with an absolute constant. Also M<=n. Choose mu=n^(-a), with 1/(2beta)<a<1. Then E_out/n tends to zero while M/[sqrt(n)mu^(-beta)]<=n^(1/2-a beta) tends to zero. Thus a uniform QD implication with exponent beta>1/2 is false even for C=1. Exponents below 1/2 give a weaker hypothesis when mu<1; this argument does not refute them. This supplies a valid mu-varying reason for the endpoint 1/2.

## 6. Numerical falsification and reproducibility

**PROVED execution record / NUMERICAL scope.** All runs used the specified VM through `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2`, with an 8 GB cap and at most a 900-second per-job timeout. Python was 3.12.3, NumPy 2.5.4 and SciPy 1.18.1. No local calculation, LP/MILP, subagent or commit was used. The numerical runs are finished, with passing assertions. All Fourier minima, scalar local refinements, memberships made with floating irrational rotations, and quadratures are NUMERICAL, not global or interval certificates. Exact integer/rational checks are identified separately. The paper proofs do not depend on these calculations.

**NUMERICAL actual-word tests.** `finite_checks.json` contains 22 words: golden-ratio Bohr windows at Y=1024,4096,16384 and densities 1/4,1/2; random half-density words at those three lengths; period-2,3,5 residue words at the same lengths; and sign thresholds of sums of S=1,4,16,64 irrational cosines at Y=32768. The latter use the square roots of the first S primes. The coefficient/correlation identity, rotation CVaR upper bound, explicit Chebyshev FTL1, and domination of coherent moments by positive counts of degrees up to three were checked. All words and frequencies are saved in `finite_sets.json`.

| NUMERICAL word | Actual two-sided mass / variance | Relevant observation |
| --- | ---: | --- |
| Golden-ratio half-window, Y=16384 | 0.8106639955 | Approaches 8/pi squared; the slight finite excess is within the relation errors |
| Random half-density word, Y=16384, four test frequencies | 0.0006743140 | Small mass on these four specified characters |
| Period 2, Y=16384 | 1 | Genuine mass counts the self-conjugate character once; its degree-2 unbalanced moment is 1 |
| Period 3, Y=16384 | 0.9999694834 | Degree-2 error is about 0.000061; degree-3 torsion moment is 1 |
| Period 5, Y=16384, both positive representatives | 0.9998168796 | Degree-3 unbalanced moment is about 0.37496, including x+x=2x |
| Cosine majority, S=4 | 0.6559699890 | Toward the Gaussian constant |
| Cosine majority, S=16 | 0.6400950085 | Toward 2/pi, approximately 0.63662 |
| Cosine majority, S=64 | 0.6395005356 | A finite observation, not a CLT proof |

**NUMERICAL nonvacuous finite bound.** `sharp_checks.json` uses the exact one-frequency identity Delta_d=Re(exp(-i d arg(c))d_Y(d x)), avoiding unstable monomial conversion at large degree. It checks D=32,128,512,2048 on three saved words. For the Y=16384 half-window, the actual ratio is 0.8106639955, while FTL1's proved-form RHS divided by the variance is 0.9126169144 at D=128, 0.8366292089 at D=512, and 0.8176323419 at D=2048. These are nontrivial instances of the finite leakage estimate. The generic low-degree tests are often numerically vacuous because their explicit R/D error is large; that is reported rather than hidden.

**PROVED finite input checks / NUMERICAL zoo.** `zoo_sets.json` snapshots 90 distinct actual sets: 4 fixed Bohr windows, 2 random dense sets, 6 full residue patterns, 3 Singer positive-difference sets and 3 genuine Bu sets at q=7,19,43, all 40 current E68 rows, and 32 E72 rows including the then-current E72c files. These files were being extended elsewhere in the shared workspace; replay uses the saved snapshot rather than assuming the source files stop growing. Singer difference-set and cardinality predicates, genuine Bu cardinalities, and the exact divisibility-by-3 count were asserted. All retained sets were checked for distinct positive integer entries.

**NUMERICAL tall sets and relation counts.** `tall_checks.json` contains 360 rows, thresholds H=2,4,8,16 times sqrt(n), on FFT grids of size 2^ceil(log2(128X)). The full sampled tall-set measure and energy are retained. Greedy representative positive peaks have separation at least 2/X; the center list includes zero, whose globally centered coefficient is zero. Thus a one-center row can have W=0 and is not evidence of a noncentral structured pattern. For those lists the data include positive degree-2/3 counts, coherent unbalanced moments through degree eight, and individual torsion diagnostics through degree four. `zoo_tl1_checks.json` applies the actual finite-word theorem to the selected threshold-4 lists. All relation counts are explicitly for these lists and this resolution; the lists are not a certificate of the optimal window capture.

**NUMERICAL exact-grid reduction checks.** `cyclic_checks.json` contains another 360 rows for symmetric padding with the smallest power of two at least 8X. Every nonzero tall grid character in the positive half is included, rather than only local peaks. The identities B=0, E(bL)=W, nonnegativity of the cyclic weighted modular-relation moments, discrete P40, and FTL1 were checked. The largest S was 282; the largest displayed sufficient degree for paying the approximation error was 2432. These observed values are not claimed to be uniform asymptotic bounds. The numerical inverse numerator conservatively subtracts the full Nyquist squared mass even when it is not tall; this can only weaken its lower bound. At the tested thresholds no zoo row meets M_grid<=sqrt(n)/k squared. Thus none tests an actual sequence with epsilon tending to zero.

**NUMERICAL Bu falsification.** Bu at q=19 and 43 has a threshold-4 noncentral peak near 2pi/3, with degree-3 positive relation diagnostic about 0.96861 and 0.16243, respectively, for the full selected lists. For q=43 the individual degree-3 torsion diagnostic is about 0.53894. Removing neighborhoods of radius max(32/X,X^(-1/2)) about 0 and +/-2pi/3 leaves largest positive peaks of 3.16799, 3.52306, and 4.80226 times sqrt(n) for q=7,19,43. These finite values do not prove a uniform no-tall-spikes theorem. At threshold 16 none of these residual peaks is tall, but the central peak can still be tall.

**PROVED asymptotic vacuity, quoted correctly.** For the Bu family with a Sidon range O(k squared), P16/P16-prime gives M/sqrt(n)>=1/2-o(1), so it cannot satisfy the counterexample hypothesis epsilon tending to zero. For Singer positive-difference sets n=q(q+1)/2 and X<=q(q+1), hence n>=X/2; the quoted proved dense P31 corollary gives M>=sqrt(n)/1000. Thus their exclusion from a counterexample sequence is rigorous and does not require the false premise that they have no positive macroscopic peaks.

**NUMERICAL E68/E72 assessment.** All 72 saved E68/E72 sets have tall-set measures, captured energies, and degree-2/3 counts recorded. At threshold 4, 9 of the E68 rows have a selected noncentral positive peak; the remaining E68 rows and all saved E72 rows have only the central selected peak. For example E68 row 0 has n=64, X=133, S=2 including zero, Q2=0.00513826 and Q3=0.00491035. The best saved E68 ratio is approximately 0.6061875. These observations neither falsify the finite theorem nor demonstrate the counterexample hypotheses needed for the inverse conclusion. The full cyclic data retain the neighboring central-lobe grid characters as well, so their S should not be compared directly with the local-peak S.

**PROVED exact tests / NUMERICAL approximation audit.** `exact_checks.json` checks the balanced fourth-moment integer count for every S=1,...,128; 271 exact rational stable-Gram integral cases and 34,688 exact rational pointwise cases on the family h(t,omega)=(1-|t|)_+(p0-q chi(omega)) on R times Z/2. Their negative spectral mass is exactly q. Separately, the analytic hinge coefficients were evaluated on 174,165 floating grid points, D=2,4,8,16,64 and 17 lambda values; the largest observed error was less than 0.248 times the proved error bound. This last grid check is NUMERICAL and is not the proof of the uniform majorant.

**NUMERICAL binary radial-obstruction check.** `radial_obstruction_checks.json` evaluates the actual-word construction above at Y=4,194,304 and (S,q)=(8,17),(32,67),(128,257), using geometric sums on the even indices and the override positions divisible by q. The observed normalized fourth moments are 5.3749844, 21.3436064, and 85.3353422; the proved limits are 5.375, 21.34375, and 85.3359375. The observed captured fractions of the binary variance are respectively 0.0224405, 0.00577804, and 0.00157095. Thus the experiment supports both the large-moment obstruction and its lack of exhaustion. Empirical unbalanced moments through degree eight are also retained. `radial_words.json` records the exact override bits of these computed binary words, their frequencies and coefficients, so the words can be reconstructed without treating floating irrational membership as certified.

**NUMERICAL evaluator checks.** The largest relative Parseval discrepancy over the zoo FFTs was 3.34e-16; the largest direct-cosine versus FFT discrepancy at the checked grid minimum was 9.78e-12. Local scalar optimization only refines the lowest sampled neighborhood and is not a certificate of a global minimum. Energy residuals are grid quadratures, and the saved finite bounds are evaluated in floating arithmetic.

**PROVED reproduction procedure.** Run from the project root. The first command regenerates from current external example files; the replay command uses the exact saved arrays and frequencies. The final manifest is produced by verify and records SHA-256 hashes of the script and JSON artifacts.

    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -m 8 -t 900 python .research/agents/tdense5_scratch/audit.py all
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -m 8 -t 900 python .research/agents/tdense5_scratch/audit.py replay
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -m 8 -t 300 python .research/agents/tdense5_scratch/audit.py verify

The actual combined-run log is `final_vm.log`; the added high-degree run is `sharp_vm.log`; the binary-obstruction run is `radial_vm.log`; the final verification log is `verify_vm.log`. The script can also run each named stage separately. The earlier mathematical normalization correction was incorporated before the combined final numerical run. The final verification additionally checks each zoo row's n, X and grid length against the saved integer arrays and checks all retained finite TL1 inequalities again.

## 7. Completion boundary and handoff

**PROVED new paper results.** FTL1 and its explicit polynomial majorant; the radial-tail refinement and its dimension-independent conditional consequence; the actual binary realization of the divergent radial moments; the elementary Gaussian comparison with stated hypotheses; the exact symmetric cyclic P40 reduction and its qualified relation lower bound; the exact sliding-block energy identities; the stable Gram defect bound with negative spectral mass; and the interval-family obstruction to exponents above 1/2. These have complete paper arguments here. They are not claimed kernel checked, independently refereed, or externally novel.

**PROVED quoted inputs.** P40's bounded-variable truncation; P54's sharp rotation superquantile bound; round 4's fixed-complexity QD, defect bound, cover lemma and P53 regularity corrections; P31 and P16 for the stated families; and the precisely attributed BSG/Freiman theorems. These are separated from the new results. The qualitative finite-period estimate also has a direct proof here.

**CONJECTURED exact remaining target.** Unconditional degree-D(epsilon) finite TL1 on the relevant noncentral, increasing-complexity binary profiles is not proved. Neither is the weighted inverse theorem retaining a fixed fraction of mass and binary capture. HBSC is one precisely quantified sufficient missing lemma that would settle the entire uniform-capture problem through the proved SG estimate. The best actual eta(C,J,K) remains ineffective for each fixed J; no J-uniform QD-half or proof of T-dense is asserted.

**HEURISTIC strategic decision / next discriminating work.** Keep three distinct directions: (1) analytic stability, seeking an HBSC reconstruction with total negative mass O(M/H), testing its identity bound rather than only componentwise positivity; (2) additive structure, treating the explicit large balanced-moment alternative and weighted unbalanced counts separately, with a fixed-mass extraction target; (3) constructive falsification, seeking an actual binary realization that simultaneously has small negative spectral L2 mass and concentration in high-rank tall spectra, while tracking the extra combination harmonics. The first concrete next calculation is the negative spectral mass of a proposed finite joint lift on a saved E68/E72 or genuine Bu pattern, before a claim of sqrt(J) stability. Repeating pairwise Bessel, raw H-normalized measure compactness, or the already-false no-Bu-spikes premise is discontinued.

**PROVED task disposition.** All three research tasks were pursued, the requested families were tested, artifacts are reproducible, and the main finite theorem has explicit errors. The outcome is a finite analytic advance and rigorous obstructions to the proposed uniformity deductions, together with a single sufficient completion lemma. The unrestricted intended bridge and T-dense remain open in this report.
