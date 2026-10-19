# T-dense round 3: twisted profiles, flat anti-spikes, and curved Bohr rounding

## Disposition and status

- **PROVED, new in this report, paper proof:** TD9 gives the exact positive-definiteness constraint on every macroscopic twisted limit. TD10 uses it to prove **M(A_X) >= c(p) X**, uniformly in the rounding phase, whenever a fixed finite piecewise flat/curved profile has a fractional flat interval of positive length. In particular, every fixed nonzero finite staircase profile, including irrational Sturmian slopes, has a linear negative minimum. This resolves the fixed-profile flat case left open in P41.
- **PROVED, new extension of P41:** TD11 proves P41+ for any fixed finite partition into flat pieces and C2 pieces with derivative bounded away from zero, provided the curved rounding energy is positive. Flat energy is completely excluded from the adverse-energy budget. Its proof also gives a square-root bound without using TD10's stronger linear conclusion.
- **PROVED, new precisely scoped version of P41-B:** TD12 proves a square-root bound for cumulative rounding of a fixed smooth Bohr profile P(m/X, m alpha), where alpha is Diophantine and the torus average P0 has derivative bounded away from zero. TD12-F removes the Diophantine assumption entirely for a fixed finite Fourier profile, using the average on the orbit closure. The dimension, profile and alpha are fixed. This does not give uniform constants for the growing-J, X-dependent P42 construction.
- **PROVED, T1 obstruction:** TD13 refutes the premise that a positive localized bump must have monotonically decaying Fourier coefficients. TD14 proves an exact terminal-zero/Vandermonde obstruction for common Fejer bumps, with a square-root corollary for a specified class of exact tall-bump representations. Neither supplies the robust approximation theorem needed for arbitrary dense sets.
- **NUMERICAL, T3:** the VM audit covers the E67 families, centered and E67 optimized Bu/Singer representatives, saved P42-family realizations, all saved small optima, and the E68 data available at execution. It also tests 45 flat/curved and curved-Bohr roundings. Exact input sets are retained. Minima and truncated integrals are not certified. Detailed counts and results are below and in scratch JSON.
- **CONJECTURED, still open:** T-dense for arbitrary sets, and the general SB/MS missing ingredient. No proof of T-dense or counterexample to it is claimed.

All computation was run on dirichlet using `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2`, with an 8 GB job cap. No LP/MILP, subagents, commits, or edits to the root `.research/*.md` notes were used. The report and scratch are the work product. These are paper arguments, not kernel-checked or independently reviewed results. “New” means beyond the supplied project record; external priority is unchecked.

## Exact setting and frontier

**PROVED definitions/normalization.** A is a finite nonempty set of distinct positive integers; f_A(x) = sum over A of cos(ax); n = |A|; X = max A; M(A) = -min over the whole circle of f_A. Integrals on the circle use dx/(2 pi). Thus integral f = 0 and integral f squared = n/2. For every such A, M >= 1/2: the nonnegative polynomial f+M has mean M and Fourier coefficient 1/2 at each a in A.

In the profile theorems, X instead denotes the specified ambient rounding length; max A_X may be smaller than X. The numerical records distinguish `X_ambient` from the actual maximum. All lower-bound comparisons with sqrt(n) use n<=X.

**CONJECTURED target, quoted.** For every real C >= 1 there exists c(C)>0 such that every nonempty A contained in [1,Cn] satisfies M(A) >= c(C) sqrt(n).

**PROVED input, quoted P40.** If M <= epsilon sqrt(n), then the energy below sqrt(n/epsilon) is at most (sqrt(epsilon)+2 epsilon squared)n. The remaining positive spikes carry almost n/2 energy. P38--P46 and the late/late-night notebook entries were read; the single-filter LM conjecture is already false, and fixed-order moment certificates and the recorded convolution estimates must not be revived unchanged.

**PROVED normalization clarification.** The immediate Fourier projection identity applies to the symmetric sequence s = 1_(A union -A), whose transform is 2f. If U is the spike set and P_U is orthogonal projection under the Fourier transform, then

    ||s - P_U s||_2^2 = 4 integral_(U complement) f^2.

For the positive-frequency sequence 1_A, the transform is F_A = sum exp(iax), and the corresponding identity instead involves integral outside U of |F_A| squared. Consequently, almost-complete concentration of 1_A itself is not an algebraically equivalent reformulation of P40. Nothing below uses that stronger reformulation. This identifies a missing inference, rather than asserting a counterexample to an additional cosine-specific theorem about 1_A.

| Status | Known | Exact gap | Mechanism tested |
| --- | --- | --- | --- |
| PROVED, quoted | Small M forces positive spike domination | Control the exact binary spectrum at the square-root scale | Twisted limits and common-bump terminal zeros |
| PROVED here | Fixed fractional flat pieces force linear anti-spikes | Profiles and their complexity may vary with X | Exact rotation coefficients and continuity of a positive-definite profile |
| PROVED here | Curved plus flat cumulative rounding has bulk | Arbitrary structured rounding errors | Bounded curved transform plus removable pure-point spectrum |
| PROVED here | Fixed smooth Diophantine Bohr modulation is covered | Growing dimension/small denominators and non-cumulative rounding | Cohomology twice, weighted exponential sums, rounding-energy accounting |

## TD9: the exact macroscopic twisted-profile constraint

**PROVED.** Let X_j tend to infinity, let A_j be contained in {1,...,X_j}, and suppose M(A_j)/X_j tends to zero. For any real angles theta_j, form the complex measures

    nu_j = (1/X_j) sum_(a in A_j) exp(ia theta_j) delta_(a/X_j).

Every weak subsequential limit is q(t) dt on [0,1], with |q|<=1 almost everywhere. Define its Hermitian extension by

    H(t) = q(t)/2 for 0<t<1,
    H(t) = conjugate(q(-t))/2 for -1<t<0,
    H(t) = 0 for |t|>1.

Then H has a continuous positive-definite representative. Equivalently its real transform

    F(y) = Re integral_0^1 q(t) exp(ity) dt

is nonnegative for every real y. In particular, a nonzero compactly supported step function q is impossible.

**PROVED proof.** The total variation of nu_j on any interval I is at most |I|+2/X_j, which gives absolute continuity and the density bound for any limit. For fixed y,

    f_(A_j)(theta_j+y/X_j)/X_j -> F(y).

Convergence is uniform on bounded y intervals, by equicontinuity and bounded support. The lower bound f >= -M gives F>=0 on the entire real line.

For completeness, positivity also gives the asserted continuity, with no unjustified integrability assumption. The Fourier transform of H is F. For delta>0, Fubini with a Gaussian gives

    integral_R F(y) exp(-delta y^2) dy
      = sqrt(pi/delta) integral_R H(t) exp(-t^2/(4 delta)) dt
      <= 2 pi ||H||_infinity.

Monotone convergence on the nonnegative left side shows F is integrable. Fourier inversion then gives a continuous representative of H. It is positive definite because its inverse-transform measure has nonnegative density F/(2 pi). A compactly supported step function can agree almost everywhere with a continuous function only if all its jumps vanish, hence only if it is zero. This proves the last assertion.

**PROVED scope limitation.** This is an exact obstruction at height comparable to X. A spike whose height is only comparable to sqrt(n) disappears after division by X in the dense regime. TD9 does not by itself close the square-root gap. This is why the next result concerns a specified source of macroscopic resonances.

## Analytic tools used below

### A. Elementary substitute for a Vaaler truncation

**PROVED.** Put s(u)={u}-1/2, using s(integer)=-1/2. For every delta>0 there exist a real zero-mean trigonometric polynomial T and a nonnegative trigonometric polynomial W such that

    |s(u)-T(u)|^2 <= W(u) for all real u,
    integral_0^1 W(u) du < delta^2.

One may also arrange ||T||_infinity <= 1/2.

**PROVED proof.** Replace s on a small symmetric neighborhood of its jump by a continuous odd interpolation g, with |g|<=1/2, agreeing with s elsewhere. A continuous nonnegative cutoff h, supported on twice that neighborhood, majorizes |s-g| squared and has arbitrarily small integral. Fejer approximation gives a zero-mean sine polynomial T, of supremum at most 1/2, uniformly close to g. The inequality |s-T| squared <= 2h+2||g-T||_infinity squared holds even at the jump. Approximate 2h uniformly by a trigonometric polynomial and add a small positive constant to majorize it. Choosing the neighborhood and uniform errors sufficiently small gives W as stated.

**PROVED consequence.** If a sequence u_m has, for each fixed nonzero integer k, sums of exp(2 pi i k u_m) equal to o(X) on the intervals under consideration, uniformly in its initial phase, then

    sum |s(u_m)-T(u_m)|^2 <= delta^2 X + o(X).

This follows by expanding the finite polynomial W. On a curved piece the error is O_W(sqrt(X)); for a fixed irrational rotation it is O_(W,alpha)(1). Thus the new arguments do not need an unverified external sawtooth approximation formula.

### B. Curved cumulative phase

**PROVED using the stated external exponential-sum theorem.** On a fixed interval where p is C2, c1<=|p'|<=c2 and |p''|<=c3, put Phi(m)=sum_(j<=m) p(j/X). For every fixed nonzero integer k,

    sup_(xi real) |sum_(m in I) exp(2 pi i k Phi(m) + i m xi)|
        <= D_k sqrt(X),

uniformly over subintervals I of that piece. A constant phase accumulated before the piece is harmless. Euler--Maclaurin replaces Phi by a C2 phase H_X with uniform O(1/X) error and H_X''=p'/X+O(1/X^2). Apply the second-derivative estimate with curvature comparable to |k|/X; the replacement error in the sum is O(|k|).

The outside input is precisely: if lambda<=|h''|<=A lambda on an interval of length L, then the exponential sum is O_A(L sqrt(lambda)+lambda^(-1/2)+1). This statement and its hypotheses were checked in Olivier Robert, [“On van der Corput's k-th derivative test for exponential sums,” Section 3.1, Theorem 1](https://perso.univ-st-etienne.fr/rool6510/robert-2015-indag.pdf). It is also the input already used in P41. No other literature claim is needed here. The original Vaaler PDF was inaccessible in the attempted web fetch; Tool A avoids relying on it.

### C. A reusable bounded-bulk lemma

**PROVED.** Suppose, for each sufficiently large X, a real mean-zero cosine polynomial f=f_A has a decomposition

    f = P + B + E,
    ||P||_infinity <= L sqrt(X),       ||P||_2^2 >= a X,
    ||E||_2 <= delta sqrt(X),          delta <= sqrt(a)/8,

where a,L>0 are fixed. Suppose there are measurable U_X with measure tending to zero and

    ||B 1_(U_X complement)||_2 = o(sqrt(X)).

Then, for all sufficiently large X,

    integral_(f <= 2L sqrt(X)) f^2 >= a X/2,
    M(A) >= min(sqrt(a)/4, a/(16L)) sqrt(X).

All estimates must be uniform in any phase over which the conclusion is asserted.

**PROVED proof.** Off U write f=P+e, where ||e||_2 <= (delta+o(1))sqrt(X). The boundedness of P and the small measure of U give ||P 1_(U complement)||_2 >= (sqrt(a)-o(1))sqrt(X). On the exceptional set |e|>L sqrt(X), the integral of P squared is at most ||e||_2 squared, so the integral of f squared there is at most 4||e||_2 squared. On its complement f<=2L sqrt(X). The retained energy is therefore at least

    [a - 2 sqrt(a) delta - 3 delta^2 - o(1)] X >= a X/2.

P40 bounds this energy by 2L sqrt(X) M + 2M squared. Substitution of the displayed lower-bound constant proves the claim.

## TD10: a fixed fractional flat piece forces a linear anti-spike

**PROVED theorem.** Fix a profile p:[0,1]->[0,1] with a finite interval partition. On each piece p is either constant or C2 with |p'| bounded above and bounded away from zero and |p''| bounded. Values at the finitely many partition endpoints may be arbitrary. Suppose there is a flat interval of positive length on which p=alpha with 0<alpha<1. For every integer X>=1 and every sigma in [0,1), define

    a_m = floor(sigma + Phi(m)) - floor(sigma + Phi(m-1)),
    Phi(m) = sum_(j=1)^m p(j/X),      A_X = {m<=X : a_m=1}.

There exists c(p)>0 such that every nonempty resulting A_X satisfies

    M(A_X) >= c(p) X.

The constant is uniform in sigma. The profile and partition are fixed; this is not uniform over X-dependent slopes or an increasing number of pieces.

### Exact spectrum of one flat piece

**PROVED.** Away from a partition endpoint, the word on a flat piece has the form

    a_m = g_alpha(xi + m alpha),     g_alpha(u)=1_[0,alpha)({u}),

where xi may depend on X, sigma and earlier pieces. For irrational alpha, the Fourier coefficient of g_alpha at integer k!=0 is

    c_k = (1-exp(-2 pi i k alpha))/(2 pi i k).

At the angle theta=2 pi alpha, the demodulated mean of a_m exp(i m theta) has magnitude

    d_alpha = sin(pi alpha)/pi > 0,

independently of xi. Initial phase only changes its argument.

For rational alpha=r/q in lowest terms, the word is exactly q-periodic. Its coefficient at the same angle has magnitude

    d_alpha = sin(pi r/q)/(q sin(pi/q)) > 0,

again independently of xi, including intercepts at discontinuities.

**PROVED rational calculation.** Let s_m={xi+m r/q}-1/2. The first demodulated coefficient of this periodic sawtooth has magnitude 1/(2q sin(pi/q)), by summing j exp(2 pi i j/q) over a full q-cycle. Since a_m-alpha=s_(m-1)-s_m, multiplication by exp(2 pi i r/q)-1 gives the asserted coefficient. This also handles all cyclic shifts of the word and the exact floor endpoint convention.

For irrational slopes, the same coefficient statement follows by approximating g_alpha by continuous trigonometric polynomials in mean absolute error. Uniform rotation averages bound that error for every intercept; nonresonant terms have bounded geometric sums. This supplies uniformity in xi even when xi changes with X, rather than invoking an almost-everywhere ergodic theorem.

### Limits on the other pieces

**PROVED.** Fix theta=2 pi alpha from the chosen flat piece. On any other irrational flat piece of slope alpha_j, finite Fourier approximation of g_(alpha_j), followed by geometric summation, shows that a_m exp(i m theta) has a constant weak density on that piece. It is zero unless theta/(2 pi)+k alpha_j is an integer for some integer k. If there is a resonance, its coefficient is bounded in modulus by 1 and may depend on the intercept. The approximation error tends to zero uniformly in the intercept, because a fixed irrational rotation has uniform averages for Riemann-integrable interval functions. Continuous majorants/minorants and finite Fourier approximation give this assertion directly; no uniform Diophantine rate is asserted.

On rational flat pieces use the exact finite periodic expansion instead. A 0 or 1 flat piece has zero demodulated limit at this nonzero theta. On a curved piece, write a_m=p(m/X)+s_(m-1)-s_m. The profile term is O(1) at theta by Abel summation. Tool A followed by Tool B makes the second term o(X), uniformly in sigma, even after multiplication by any fixed smooth function of m/X. Thus its weak density at theta is zero. Finitely many boundary coefficients contribute O(1/X) to the measures.

### Contradiction and uniformity

**PROVED.** If the asserted uniform linear bound failed, there would be X_j tending to infinity and phases sigma_j with M(A_(X_j))/X_j tending to zero. Pass to a subsequence on which the finitely many flat-piece resonance coefficients converge. The measures nu_j of TD9, at the fixed theta just selected, then converge to a step density q, constant on each flat interval and zero on the curved intervals. On the selected interval its coefficient has magnitude d_alpha>0. Thus q is a nonzero step function. TD9 forbids this. This proves a uniform positive linear constant for all sufficiently large X. The bound M>=1/2 absorbs the finitely many smaller nonempty cases.

**PROVED corollary.** Every fixed finite piecewise constant p with positive integral has M(A_X)>=c(p)X on all nonempty roundings. If a fractional flat piece exists, use the theorem. Otherwise p is 0 or 1 almost everywhere, and a_m=p(m/X), apart from finitely many endpoint choices. The central angle theta=0 produces the nonzero step limit q=p; TD9 again gives a contradiction to M/X tending to zero.

**PROVED relation to the supplied state.** The irrational-flat case in P41 is therefore not an unresolved obstruction for a fixed finite-piece profile. The result does not address staircase approximations whose number of steps grows with X or slopes tending to 0, 1, or moving rational resonances. It is stronger than a square-root conclusion on the stated class, and does not contradict the notebook's concern about increasing-complexity staircases.

## TD11: P41+ with flat pieces excluded from bulk accounting

**PROVED theorem.** Keep the fixed finite piecewise flat/curved hypotheses of TD10, but require only

    eta = integral_(curved pieces) p(t)(1-p(t)) dt > 0.

Then there exist c(p)>0 and X0(p) such that all phases sigma and all X>=X0 satisfy M(A_X)>=c(p)sqrt(X). There is no subtraction of flat rounding energy. Smaller nonempty cases can again be absorbed by M>=1/2. Since n<=X, this implies M>=c'(p)sqrt(n) for every nonempty rounding.

**PROVED proof.** On curved pieces put beta_m=a_m-p(m/X). Exact summation by parts with the prefix rounding error gives

    sum_(curved) beta_m^2 = X eta + O_p(1),
    ||sum_(curved) beta_m cos(mx)||_2^2 = X eta/2 + O_p(1).

Indeed beta squared equals p(1-p)+beta(1-2p), and the last weighted discrepancy sum is bounded by 1+2 times the variation on each piece. Tool A and Tool B decompose this curved polynomial into P+Q_G, with ||P||_infinity<=L sqrt(X) and ||Q_G||_2<=delta_G sqrt(X), where delta_G can be made arbitrarily small before choosing X. Thus, for a suitable fixed truncation, ||P||_2 squared >= eta X/8.

On each irrational flat piece, apply Tool A to its fixed rotation. Its rounding error is a finite sum of modulated interval Dirichlet polynomials, plus an L2 error as small as desired relative to sqrt(X). For a rational flat slope r/q use its entire q-term periodic expansion, with zero remainder. This is the rational/minor-arc distinction needed here: the irrational geometric-sum constants can be large, but are finite for fixed truncation and fixed slope; rational zero denominators are never estimated that way.

More explicitly, for a finite polynomial W of degree K and a fixed irrational alpha,

    |sum_(m in I) W(xi+m alpha) - |I| integral W|
      <= sum_(0<|k|<=K) |W_hat(k)| min(|I|, 1/|sin(pi k alpha)|).

This bound is uniform in xi. It proves the required mean-square remainder once X exceeds a threshold depending on alpha and the chosen K. If alpha=r/q, use the periodic expansion instead, even when q<=K. There is no claim of a threshold uniform as alpha varies with X near a small-denominator rational.

The profile polynomial rho=sum p(m/X)cos(mx) is concentrated near zero by its bounded variation. Let B be rho plus all the finite flat modes. Remove neighborhoods of width h=X^(-a), 0<a<1, about zero and the finitely many mode frequencies. Their total measure tends to zero. Abel summation bounds each finite slow or constant-amplitude mode by a constant divided by distance to its frequency. Hence its squared L2 norm off these neighborhoods is O_p(1/h)=o(X). The sum E of flat and curved remainder terms has arbitrarily small L2 norm relative to sqrt(X), uniformly in sigma. Tool C, with a=eta/8 and sufficiently small total error, proves the theorem.

**PROVED novelty/scope.** P41's curved estimates and P40 are quoted ingredients. The new step is removing the complete fixed pure-point spectrum of flat pieces and retaining curved energy. This proves the fixed-profile P41+ statement; it does not prove a uniform major/minor-arc theorem for all X-dependent slopes. TD10 gives a stronger linear conclusion whenever any fractional flat piece is present.

## TD12: a precise P41-B theorem

**PROVED theorem.** Fix an integer d>=1, alpha in R^d, and constants kappa>0 and tau<infinity such that

    distance(l dot alpha, Z) >= kappa (1+|l|)^(-tau)
    for every nonzero l in Z^d.

Fix a real C-infinity function P on [0,1] times the d-torus, with 0<=P<=1. Let

    P0(t) = integral_(torus) P(t,theta) dtheta,
    c1 <= |P0'(t)| <= c2 on [0,1],
    eta = integral_0^1 integral_(torus) P(t,theta)(1-P(t,theta)) dtheta dt > 0.

For every X and sigma use p_m=P(m/X,m alpha), and cumulatively round p_m exactly as above. There is c(P,alpha)>0 such that all nonempty resulting A_X satisfy

    M(A_X) >= c(P,alpha) sqrt(|A_X|).

In fact M>=c sqrt(X) for sufficiently large X, uniformly in sigma. All dependencies in this statement are fixed before X varies.

### 1. The cumulative cohomology error is O(1/X), not merely O(1)

**PROVED.** Expand P in the torus variable and define the real zero-mean smooth function

    Omega_l(t) = P_l(t)/(1-exp(-2 pi i l dot alpha)),     l!=0.

Smoothness and the Diophantine bound make this series and all the derivatives needed below absolutely summable. Thus

    P(t,theta)-P0(t) = Omega(t,theta)-Omega(t,theta-alpha).

With t_m=m/X and Phi0(m)=sum_(j<=m)P0(j/X), telescoping gives, uniformly for m<=X,

    Phi(m) = Phi0(m)+Omega(t_m,m alpha)-Omega(0,0)+O_(P,alpha)(1/X).

To check the rate, the untelescoped term is

    -(1/X) sum_(j<=m) Omega_t(t_j,(j-1)alpha) + O(1/X).

The sum is O(1), rather than O(X): its torus average vanishes, and Abel summation bounds each Fourier mode by its supremum plus t-variation divided by |1-exp(2 pi i l dot alpha)|. The resulting series is summable by a second use of smoothness and the Diophantine bound. The Taylor remainder is O(m/X^2). This verifies the rate needed inside exponential sums.

### 2. Uniform exponential sums with smooth Bohr weights

**PROVED.** For fixed nonzero k and any fixed smooth g(t,theta),

    sup_x |sum_(m in I) g(t_m,m alpha)
             exp(2 pi i k Phi(m)+i m x)| <= D_(k,g,P,alpha) sqrt(X)

on every subinterval I. Replace Phi by the preceding expansion, at total error O_k(1). Euler--Maclaurin replaces Phi0 by H_X with H_X'' comparable to 1/X. Expand g exp(2 pi i k Omega) in torus Fourier modes. Their coefficient supremum norms plus t-variation norms are summable. For each mode, Tool B and Abel summation give O_k(sqrt(X)), uniformly in its added linear frequency and x. Summing proves the assertion. Constants need not be polynomial in k, since only a fixed finite truncation is used.

### 3. The rounding energy really is positive

**PROVED.** Put beta_m=a_m-p_m and s_m={sigma+Phi(m)}-1/2. Then beta_m=s_(m-1)-s_m. The weighted exponential-sum estimate and Tool A give

    (1/X) sum s_m g(t_m,m alpha) -> 0

for every fixed smooth g, uniformly in sigma. First prove this for the finite zero-mean polynomial T; Cauchy--Schwarz makes the residual at most a constant times delta X; then let delta decrease to zero.

Now

    sum beta_m p_m
      = boundary terms + sum_(m<X) s_m (p_(m+1)-p_m).

The boundary terms are bounded, and

    p_(m+1)-p_m
      = P(t_m,m alpha+alpha)-P(t_m,m alpha)+O(1/X).

The preceding weighted estimate proves sum beta_m p_m=o(X). Also sum beta_m=O(1). Consequently

    sum beta_m^2 = sum p_m(1-p_m)+o(X) = eta X+o(X).

The last equality follows from ordinary torus Fourier expansion, geometric sums for nonzero modes, and Riemann sums for the zero mode. This step is necessary: the O(1) variation argument from P41 does not apply to a rapidly Bohr-modulated sequence.

### 4. Remove the profile spikes and retain the bounded bulk

**PROVED.** Tool A and Step 2 split the rounding-error cosine polynomial into a uniformly O(sqrt(X)) polynomial P_b and a remainder of arbitrarily small L2 norm relative to sqrt(X). Step 3 and Parseval show that ||P_b||_2 squared is bounded below by a positive multiple of eta X if the approximation error is chosen sufficiently small.

For the expected profile rho=sum p_m cos(mx), truncate the torus Fourier series of P at a fixed finite set of modes. The discarded coefficient error is uniformly as small as desired, so its cosine polynomial has L2 norm at most that error times sqrt(X/2). Each retained mode has a smooth amplitude P_l(m/X). Abel summation concentrates it near x=-2 pi l dot alpha, and its conjugate near the opposite frequency. Outside neighborhoods of width X^(-a), 0<a<1, the squared L2 norm is O( X^a )=o(X). There are finitely many neighborhoods. Tool C now proves the square-root lower bound. Uniformity in sigma follows at every step. M>=1/2 completes the smaller nonempty cases.

**PROVED examples and limitation.** The theorem covers, for fixed Diophantine alpha and fixed coefficients,

    P(t,theta) = (1/2)(1-t)[1+(3/10)cos(2 pi theta)]

and the version replacing the last term by (1/5)cos(2 pi theta)+(1/10)cos(4 pi theta). These profiles have positive Fejer-type expected signals; the tested examples do not rely on an abrupt nonzero terminal density to create a linear central sidelobe. A fixed finite positive Bohr mixture is also covered when these hypotheses hold. P42 has growing J, X-dependent rational frequencies and Bernoulli rounding, so it is outside the theorem.

### TD12-F: fixed finite Fourier profiles need no Diophantine condition

**PROVED corollary, stronger for the finite-mode class.** Let alpha be any fixed vector in R^d, including rational, rationally dependent, or Liouville vectors. Let Gamma be the closure in the torus of {m alpha : m integer}, with its normalized Haar measure. Suppose P is real, smooth in t, a finite trigonometric polynomial in theta, and takes values in [0,1] on [0,1] times Gamma. Replace P0 and eta in TD12 by

    P_Gamma(t) = integral_Gamma P(t,theta) dtheta,
    eta_Gamma = integral_0^1 integral_Gamma P(t,theta)(1-P(t,theta)) dtheta dt.

Assume c1<=|P_Gamma'|<=c2 and eta_Gamma>0. Then all the conclusions of TD12 hold with a constant depending on this fixed profile and alpha. In particular the displayed one-mode and two-mode examples work for every fixed irrational alpha, with no Diophantine hypothesis; rational alpha works whenever its orbit-average hypotheses hold.

**PROVED proof.** In the finite Fourier series, a character has nonzero orbit average exactly when l dot alpha is an integer. On Gamma all such characters are identically 1, so their terms belong to P_Gamma. For every remaining Fourier term divide by 1-exp(-2 pi i l dot alpha) to construct Omega. There are only finitely many such divisions, and every denominator is nonzero. The second summation used to prove the O(1/X) cumulative remainder is also finite. Thus Step 1 holds without any uniform small-divisor condition.

For Step 2, exp(2 pi i k Omega) has an absolutely summable smooth torus Fourier expansion even though it need not have finitely many terms. No denominators occur when estimating this expansion: the second-derivative bound is uniform in every added linear frequency. Steps 2--3 therefore go through unchanged. The mean of P(1-P) is now its Haar average on Gamma, by its finite Fourier expansion and geometric summation. The expected profile already has finitely many frequencies, so Step 4 needs no Fourier-tail approximation. Tool C completes the proof.

**PROVED scope.** The constants may become arbitrarily poor as a nonresonant angle approaches a resonance. This is a fixed-parameter theorem; it gives no uniform control for the rational angles or number of modes changing with X in P42.

## TD13: positivity does not force monotone Fourier decay

**PROVED counterexample to the unrestricted bump premise.** For every integer L>=2, let

    F_L(x) = (1/L)|sum_(j=0)^(L-1) exp(ijx)|^2,
    phi_L(x) = F_L(x) [1+cos(2Lx)].

Then phi_L>=0, has mean 1, is bounded above by 2F_L, and has degree 3L-1. Its mass outside |x|<=W/L is O(1/W) for 1<=W<=L, by the usual sine formula for F_L. Thus it is a positive localized bump of width comparable to the reciprocal of its degree. Nevertheless,

    phi_hat_L(L) = 0,      phi_hat_L(2L) = 1/2.

Indeed its Fourier coefficients are the central triangular Fejer coefficients plus half of their translates by +/-2L. This is an exact secondary Fourier lobe, defeating a monotone-decay inference from positivity and spatial localization alone. It does not have the required flat 0/1 spectrum, and is not a Chowla construction. A successful general bump argument must use that binary spectrum or impose an additional shape hypothesis and justify it.

## TD14: a terminal-zero obstruction for identical Fejer bumps

**PROVED.** Let A be nonempty with max A=X, let L>X be an integer, and suppose there is an exact representation

    f_A(x)+m = sum_(j=1)^J w_j F_L(x-theta_j),
    w_j>0,

where theta_j are distinct modulo 2 pi. Then

    sum w_j=m,
    J >= L-X,
    m >= L/[2(L-X)].

**PROVED proof.** Write u_k=sum w_j exp(-ik theta_j). At k=X the Fourier identity is (1-X/L)u_X=1/2, so |u_X|<=m gives the last inequality. At every k=X+1,...,L-1, u_k=0. If J<=L-X-1, take the first J of these consecutive zero equations. The resulting matrix is a diagonal matrix with nonzero entries times a Vandermonde matrix in the distinct exp(-i theta_j); it is invertible. Hence all w_j vanish, a contradiction. Therefore J>=L-X. The rank argument does not need positivity; the coefficient bound uses it.

**PROVED square-root corollary for an explicit exact class.** In addition assume L>=(1+delta)X for fixed delta>0, and that every component peak is at least n/(8m), i.e. w_j L>=n/(8m). Then

    J <= 8m^2 L/n,
    m^2 >= n(L-X)/(8L) >= delta n/[8(1+delta)].

In particular, an exact representation with m=M cannot be a T-dense counterexample within this tall-common-Fejer-bump class. If L=2X the representation requires at least X atoms, so a picture with only o(X) such identical positive bumps cannot hold exactly. The cardinality bound is sharp in general: X equally weighted points on an X-root-of-unity coset, convolved with F_(2X), give 1+cos(Xx).

**PROVED obstruction/remaining gap.** The Vandermonde conclusion is exact. An L2-small remainder does not give a uniformly well-conditioned Vandermonde system when points cluster; an exponential loss in J is useless at the square-root scale. Nor has a representation with a common Fejer kernel and only tall components been derived from P40. These are limitations of the proposed mechanism, not a robust proof for arbitrary spikes. TD13 also prevents replacing the common kernel by an unspecified “positive localized bump” while retaining a decay argument.

## T3: reproducible falsification and numerical evidence

**NUMERICAL protocol.** `audit.py` uses an FFT on G=2^ceil(log2(64 max A)) full-circle points, trapezoid weights on the even half-circle, and an independent direct-cosine minimization near the lowest grid point. It records beta_K = integral_(f<=K sqrt(n)) f squared divided by n/2 for K=1,2,3. This is floating quadrature at a discontinuous cutoff, not an interval certificate. The refined value is still only an estimate of M; a missed minimum is possible. Parseval and direct/FFT agreement are checks of evaluation and normalization, not certificates.

**NUMERICAL reproducibility.** Exact sets are stored in `tdense3_scratch/sets.json` and `extension_sets.json`. The seed for new random zoo members is 2026101903. Python and NumPy versions, per-set grid sizes, errors and all metrics are in `zoo.json`; extension data are in `extensions.json`. The saved P42-family realizations are those already retained in the round-2 scratch at ambient X=4096,16384,65536,200000. Bu/Singer data include both a centered shift and the exact shift optimization implemented in `src/e67_zoo.py`. The small-optimum source files are `examples/smallN_best.json` and `examples/construct/N50_certified.json`. All rows present in the E68 JSONL snapshot are loaded and their actual integer sets saved, including the source filename and row index in the key. Snapshot counts and selected metrics are in `summary.json`.

**PROVED membership / NUMERICAL energy and minima, extension tests.** Ambient X=4096,16384,65536; sigma=0,0.37,0.999, interpreted as exact rationals. Flat densities are 2/5, the golden-ratio conjugate, and 2/5+sqrt(2)*10^(-7). The profile is flat on [0,1/4], curved down to zero on [1/4,3/4], and zero afterwards. All floor decisions for these 27 flat/curved examples are made exactly in the relevant quadratic field: for integers u,v,D with v>=0 and D>0,

    floor((u+v sqrt(d))/D) = (u+isqrt(d v^2)) // D.

The exact cumulative profile has this form. This avoids spurious word changes at rational floor boundaries caused by floating cumsum. Energy values and minima remain numerical. The two smooth Bohr examples displayed in TD12 are tested at the same sizes and phases; their rounding arithmetic is labeled separately in the data. These tests are evidence for the stated fixed-parameter theorems, not proofs or tests of uniformity over all near-rational slopes.

**PROVED finite membership certification, Bohr examples.** After generation, every floor decision in all 18 Bohr examples was independently enclosed using Arb ball arithmetic at 192-bit precision, with the exact quadratic alpha, exact rational amplitudes and exact rational sigma. Every enclosing floor ball contained a unique integer, and every resulting set agreed with the saved floating-generated set. Thus all 516096 Bohr floor decisions were certified; no membership uncertainty remains for those saved examples. `bohr_membership_certificate.json` records each example and its count, and `bohr_membership_vm.log` records completion. This certifies membership in the analytic profile family, not any all-x cosine minimum or truncated integral.

**PROVED finite checks / NUMERICAL diagnostics.** `checks.json` records exact Fraction-based Fourier dictionary checks for TD13 at L=2,...,64; exact rational periodicity and counts for every reduced r/q with 2<=q<=24 and four intercepts; numerical checks of the rational first-harmonic magnitude; and an independent direct cumulative-sum check of the O(1/X) cohomology expansion for the one-mode affine profile. The latter checks report X times the error and do not certify irrational arithmetic.

**NUMERICAL results.** The completed snapshot contains 121 zoo sets, including 40 E68 rows, and 45 extension examples. Python was 3.12.3 and NumPy 2.5.4. The largest relative Parseval error was 5.78e-15; the largest direct-versus-FFT absolute discrepancy at the checked grid point was 1.04e-9.

| NUMERICAL input | n | actual max A | refined R estimate | beta_1 | beta_2 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Interval | 4096 | 4096 | 13.91246 | 0.07007 | 0.07323 |
| Curved quadratic rounding | 4096 | 23818 | 2.67111 | 0.52736 | 0.69497 |
| E67 optimized Bu/Singer, q=31 | 992 | 2973 | 0.65624 | 0.29252 | 0.44392 |
| Saved N50_x72 optimum | 50 | 72 | 0.57006 | 0.19929 | 0.21166 |
| Saved P42-type sample, ambient 200000 | 50037 | 198736 | 2.96409 | 0.53579 | 0.66392 |
| Smallest-R E68 snapshot row | 64 | 91 | 0.60619 | 0.19331 | 0.20097 |
| Smallest-beta_1 E68 snapshot row | 64 | 90 | 1.26175 | 0.13219 | 0.15314 |

**NUMERICAL assessment.** No audited set has both beta_1<0.13 and R<0.60. These are stated finite thresholds for this snapshot, not proposed universal constants. In particular, the E68 row with the smallest beta_1 has substantially larger R than the smallest-R row. The two tested smooth Bohr families have R estimates between 1.94300 and 2.59591. The flat/curved examples show much larger R as X grows, consistent with TD10's linear conclusion; this trend is not part of the proof.

**NUMERICAL E68 exact-set handoff.** The smallest-R row is `E68_e68_14` in `sets.json`, from row index 14 of the original `e68.jsonl`. Its exact set is

    A = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
         21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,
         42,43,44,45,46,47,48,51,52,53,54,55,58,59,64,68,70,72,74,77,
         79,80,82,91}.

The original coarse-grid R was 0.605231; independent FFT/direct refinement gives 0.60618820. This is a grid-resolution correction to a supplied candidate, not a new construction record. Its beta values are given in the table. No all-x upper certificate for this row was produced.

**PROVED finite / NUMERICAL check results.** All 63 rational Fourier-dictionary identities and 716 exact rational word-period/count checks passed. The floating first-harmonic comparison differed from the formula by at most 3.58e-15. For X=1024,4096,16384, the computed values of X times the maximum cohomology remainder were respectively 0.08633734, 0.08633745, 0.08633768. These support the stated rate while keeping exact and floating claims separate.

**NUMERICAL energy-accounting checks.** In the 27 exact flat/curved roundings, the largest absolute difference between curved rounding energy and sum p_m(1-p_m) on the curved piece was 0.570435. In the Bohr cases, the largest absolute normalized energy discrepancy was 0.00208823 at the smallest tested size. The exact copied E68 set in this report was also checked against the saved 64-element snapshot by `verify`.

Commands, run sequentially so the VM job quota remains at two cores:

    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -m 8 -t 900 python .research/agents/tdense3_scratch/audit.py extensions
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -m 8 -t 900 python .research/agents/tdense3_scratch/audit.py final_audit
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -m 4 -t 300 python .research/agents/tdense3_scratch/audit.py certify_bohr
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -m 4 -t 300 python .research/agents/tdense3_scratch/audit.py verify

The final-audit command refreshes the zoo snapshot, runs the checks, and creates the summary. Logs include `extensions_vm.log`, `final_audit_vm.log`, `bohr_membership_vm.log`, and `verify_vm.log`. Re-running the zoo against a later growing E68 file may increase the snapshot count. No optimization solver is invoked.

## Strategic review and exact remaining problem

**PROVED assessment after the distinct attempts.** The macroscopic positivity argument succeeds for a nonzero step resonance, producing a linear theorem on fixed flat profiles. The common-bump coefficient argument succeeds only with an exact kernel representation. Its proposed generalization based solely on positivity is refuted by TD13. These are different mechanisms; repeating a convolution-stability estimate or increasing the order of an unmasked moment certificate would not repair either limitation.

**CONJECTURED remaining ingredient, inherited SB/MS.** One still needs an estimate that uses the exact 0/1 spectrum to force a fixed positive fraction of energy below K(C)sqrt(n), or an equivalent retained-variance estimate after an adaptive positive mask, uniformly for arbitrary A contained in [1,Cn]. TD9 has no information when every relevant spike is o(X), and TD14 has no established robust form under P40-sized errors. No new lemma is silently substituted for these gaps.

**HEURISTIC decision.** Discontinue the unrestricted “positive bump means Fourier decay” route. Retain TD14 as a test for specified exact common-kernel constructions. The productive proof-writing outcome is TD10--TD12. For further work, the most discriminating extension would quantify the curved-Bohr estimates while allowing controlled growth of the number of modes and small-divisor norms, or construct a binary example with growing resonant structure and both small beta_K and small R. An undifferentiated larger zoo search has less information value than those two tests.

**PROVED handoff boundary.** Fixed finite-piece profiles, fixed smooth Diophantine Bohr profiles, and fixed finite Fourier Bohr profiles with the orbit-average curvature hypotheses are covered as stated. Growing-complexity staircases, X-dependent Bohr mixtures, arbitrary non-cumulative structured roundings, and the full T-dense statement remain outside the proofs. The project is not claimed solved.

**PROVED constant-status clarification.** TD10 obtains existence of c(p)>0 by a compactness contradiction; it does not provide a useful numerical value for that constant. TD11--TD12 specify all parameter dependencies and a quantitative final bulk inequality, but do not optimize or evaluate the preceding approximation and exponential-sum constants. No ineffective statement is advertised as an explicit numerical certificate.
