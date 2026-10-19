# Round 8 T-dense research report

PROVED round-8 checkpoint (paper, not kernel-checked): rho*<=203819/250000=.815276; T-dense(6.156), with an ineffective constant; and the optional explicit T-dense(3) bound c(3)=10^(-6000005), derived below using elementary P31-E. Edits were confined to this report and tdense8_scratch; no commits or subagents. Mathematical computation ran through `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2`. Optimization used Gurobi with two threads and NonConvex=2 where applicable. No external priority is asserted.

PROVED target (quoted): T-dense(C) means that there exists c(C)>0 such that every nonempty finite set A of distinct positive integers with X=max A<=C|A| satisfies M(A)>=c(C)sqrt(|A|), for f_A(x)=sum cos(ax) and M=-min over the entire circle.

PROVED source audit: read CLAUDE.md, the complete round-8 brief, P17, P31/P31-N/P31-E, P32, P40, P47, P48, P52/P53, P54/P55, P58, NOTEBOOK continuations 9–10, E16/E78, and the round-7 report and exact witness code. P17(a), P58's high-pass diagonal and its assembly are quoted inputs, not round-8 discoveries. A grep of PROOFS.md for the improved constant and separable/doubling-potential method found no corresponding entry. This is an internal novelty check, not an external priority claim.

## Task 1: rigorous doubly-positive bound

PROVED (paper argument, newly derived relative to the inspected record). Let w be any nonzero continuous even integrable nonnegative positive-definite function on R. Normalize w(0)=1 and put s=1/sqrt(2), b=1-s. Then

    w(t)^2 <= s w(t) + b w(2t)    for every real t.

Indeed write x=w(t), y=w(2t). Positive definiteness gives 0<=x,y<=1 and y>=2x^2-1. For x<=s use x^2<=s x. For s<=x<=1, subtract the right-hand side with y replaced by 2x^2-1: the result is

    (2s-1)(x-s)(x-1) <= 0.

Integrating and changing variables in the dilation term gives

    integral w^2 <= ((1+s)/2) integral w,
    rho* <= (2+sqrt(2))/4 = 0.8535533906... .

PROVED this improves quoted P17(a)'s 0.90565 for its full class, not just autocorrelations. P58 therefore proves T-dense(C) for every C<(2/r)(1+sqrt(1-(2+sqrt(2))/4))^2, with r the quoted asymptotic P31 constant. The completed polynomial refinement below improves the constant further to .815276.

PROVED completed refinement strategy: use a monotone polynomial beta and certify

    rho x-x^2+beta(max(0,2x^2-1))-beta(x)/2 >= 0,

which integrates to the desired gap. Sampling discovered beta; exact rational polynomial inequalities below support the theorem. The completed general-versus-autocorrelation numerical comparison follows the certificate.

## Task 2: two-scale programme

PROVED new necessary condition (paper argument; supporting exact identities independently checked): in every hypothetical dense counterexample sequence with M=o(sqrt(n)), the limiting rounding-energy profile e=p(1-p) is positive definite, not just nonnegative and front-loaded. This is not stated in the inspected P58 or P40/P47/P48/P53 entries; a targeted grep of PROOFS.md and NOTEBOOK.md was performed before this internal novelty claim.

PROVED derivation. Use P58's diagonal smoothing and write its exact high-pass polynomial as T=r_0/2+g, where g=sum_{m>=1}r_m cos(mx), mean(g)=0, and g>=-m with 0<=m=M+r_0/2<=M. Circle convolution with normalized Haar measure gives

    0 <= (g+m)*(g+m)(x) = m^2 + (1/2)sum_{k>=1}r_k^2 cos(kx).

For fixed real y put x=y/X and divide by X. P58's binary diagonal gives (1/X)sum r_k^2 delta_{k/X} -> e(t)dt. Since m^2/X->0, integral_0^1 e(t)cos(ty)dt>=0 for every y. Thus the continuous even compactly supported e is positive definite.

PROVED consequence: a=p(0)<=1/2. If a>1/2, continuity of p from a to p(1)=0 gives a point with p=1/2, hence e=1/4>e(0)=a(1-a), contradicting the maximum-at-zero property of positive definiteness. This kills the exact round-7 witness (a approximately .6563), independently of how its residual energy is split into atoms or mesoscopic spikes.

PROVED new dense reach, using the exact polynomial certificate below and the quoted P31-N/P58 inputs. If rho is a rigorous universal doubly-positive constant, then

    d <= (r/2) a(1-a)/(1-rho a) <= r/[4(2-rho)],

because 0<a<=1/2 and the rational function increases on that interval. Therefore T-dense(C) holds for every C<4(2-rho)/r. The certificate search rigorously verified rho=203819/250000=.815276, which places this reach above 6.054. The next paragraphs record the exact rational C and independent verification. This is a theorem beyond the former macroscopic barrier, not a formal realization of a Chowla counterexample.

NUMERICAL Task 1 certificate discovery: Gurobi LP potentials of degree 1,4,8,12 using the three-point Gram bound give about .853553, .851122, .851122, .851122. Adding the four-point bound y>=x-sqrt(1-x) gives about .832794, .815270, .815175, .815175. Rational rounding and exact Bernstein verification give .815276 at degree 8. All computation was on the VM; exact JSON certificates and discovery code are in tdense8_scratch/potential.py and potential_g4_d8_exact.json. Degree 4 also certifies .815371 and is a shorter independent fallback. Optimization outputs alone are not used as proof.

PROVED independent verification completed: verify.py reconstructed the degree-4 and degree-8 polynomials independently in SymPy over QQ. Sturm root counts are zero on all four prescribed intervals and exact endpoint signs are positive. This independently confirms the rational Bernstein checks, including monotonicity and interval coverage. With rho=203819/250000 and r=769801/1000000>4/(3sqrt(3)),

    4(2-rho)/r = 4738896/769801 = 6.156001356...,
    4(2-rho)-(1539/250)r = 261/250000000 > 0.

PROVED strongest current theorem: T-dense(1539/250), i.e. T-dense(6.156), with an ineffective positive constant. The exact rational reach check is in independent_verification.json. With the elementary quoted r=.811, the same proof gives T-dense(5.843). Neither statement is kernel-checked. The exact old witness violates the new energy-PD constraint already at t=7/48: e(t)-e(0)=6060140520267442285391/250000000000000000000000>0 (about .02424).

PROVED complete quantified assembly. Suppose T-dense(6.156) failed. Then there would be nonempty sets A_j with X_j<=6.156n_j and M_j/sqrt(n_j)->0. Since M_j>=1/2, X_j,n_j tend to infinity after passage to a subsequence. Quoted P58 supplies a continuous even PD p supported in [-1,1], 0<=p<=1, with d=integral_0^1p>=1/6.156, a=p(0)>0, the diagonal residual energy e=p(1-p), and the energy window a(1-a)>=2b/r, b=integral_0^1e. The new correlation identity proves e PD, hence a<=1/2. Task 1 gives b>=d(1-rho a), so

    d<=[r/2] a(1-a)/(1-rho a)<=r/[4(2-rho)]<1/6.156.

The middle function increases on 0<=a<=1/2 because its derivative has numerator 1-2a+rho a^2>=0. The final strict inequality is the exact rational margin displayed above. This contradicts the lower bound on d and proves the existence of a uniform c(6.156)>0. Bounded-X exceptions cannot defeat the sequence argument. The same proof with r=.811 proves 5.843. This argument retains the whole-circle minimum throughout and does not replace it by grid minima.

PROVED strategic review: the old statement that the macroscopic method stops at about 6.05 applies only to its specified two scalar windows. The product window below supplies a new macroscopic constraint and disproves that proposed barrier for the enlarged method. Individual height-normalized PD lifts and their missing tightness are bypassed for this extension, not resolved. Stop trying to realize the old witness as a counterexample: it violates a necessary finite-product inequality after diagonal smoothing. Continue with the strengthened macroscopic class, quantitative smoothing and the remaining mesoscopic phase-coherence problem.

## Task 1 certificate in full

PROVED four-point input. For x=w(t), y=w(2t), z=w(3t), restrict the Toeplitz Gram matrix at 0,t,2t,3t to its antisymmetric subspace. The resulting matrix is

    [1-z, x-y; x-y, 1-x].

It is PSD. Since z>=0, (x-y)^2<=(1-z)(1-x)<=1-x. Together with P17(a)'s three-point condition this gives

    y >= max(0, 2x^2-1, x-sqrt(1-x)).

PROVED exact certificate: let beta be the degree-8 polynomial with Bernstein coefficients on [0,1]

    0,
    60373517/500000000,
    60373517/500000000,
    168409617/1000000000,
    512507/2500000,
    9802107/40000000,
    142881077/500000000,
    163667237/500000000,
    184824801/500000000.

Thus beta(x)=sum_{k=0}^8 b_k binom(8,k)x^k(1-x)^(8-k); beta(0)=0. Put rho=203819/250000 and A(x)=rho x-x^2-beta(x)/2. The exact rational checks establish:

| Polynomial | Exact interval | Bernstein proof | Independent Sturm roots |
| --- | --- | --- | --- |
| beta'(x) | [-1/1000,1] | 2 leaves | 0, positive endpoints |
| A(x)/x | [0,61804/100000] | 1 leaf | 0, positive endpoints |
| A(1-u^2)+beta(1-u-u^2) | [366/1000,61804/100000] | 1 leaf | 0, positive endpoints |
| A(x)+beta(2x^2-1) | [86603/100000,1] | 1 leaf | 0, positive endpoints |

PROVED coverage: the low and high x intervals leave only [.61804,.86603]. The change x=1-u^2 puts that interval inside the listed rational u interval. On this larger u interval, 1-u-u^2>=-1/1000. Therefore monotonicity of beta applies even to the tiny negative endpoint enlargement. For low x use y>=0; for middle x use y>=x-sqrt(1-x); for high x use y>=2x^2-1>=0. In all three cases

    rho x-x^2+beta(y)-beta(x)/2 >= 0.

PROVED integrability: beta(0)=0 and 0<=w<=1 imply |beta(w)|<=C w, so both dilation terms are integrable. Integrating the last inequality cancels integral beta(w(2t)) against half of integral beta(w(t)). This proves rho*<=203819/250000 for every continuous even integrable nonnegative PD w with w(0)=1. It is an exact-arithmetic computer-assisted paper proof, not an optimization-based or kernel-checked assertion. P58 alone now gives T-dense(5.311), before using the new energy-PD condition.

NUMERICAL comparison, seed 2026101908, VM Gurobi 13.0.3. General PWL profiles used 40,80,160 nodes, an initial 32B+1 symbol grid, separation of negative minima on a 512B+1 grid, and local tangent-LP ascent of the fractional quadratic objective. Half-sine and random autocorrelation starts reached the same general-PWL stationary values at each B. The autocorrelation optimizer used Gurobi quadratic proximal steps and normalization, with a 400-iteration cap; these are local lower bounds, not global maxima.

| Class and resolution | Best observed integral w^2 / integral w |
| --- | --- |
| General PWL, B=40 | .7235318917 |
| General PWL, B=80 | .7237960428 |
| General PWL, B=160 | .7238641393 |
| Nonnegative autocorrelation, N=160 | .7238644538 |
| Nonnegative autocorrelation, N=400 | .7238789197 |
| Nonnegative autocorrelation, N=800 | .7238796373 |

NUMERICAL best estimate: rho* is about .72388 from below in the autocorrelation class. At the common B=160 resolution the sampled general class did not beat the nonnegative autocorrelation value. The general sampled symbols had fine-grid minima around -1e-8; numerical diagonal repair changes J by about 1.4e-8. No continuum upper bound, proof of equality of the classes, or absence of a better signed/general extremizer is claimed. A preliminary unrefined symbol grid produced negative dips up to .0011 and is retained in profile_numeric_initial.json; those apparent improvements were sampling artifacts. Refined records are profile_numeric.json and autocorrelation_refined.json. This refines E78's numerical lower value slightly; it does not alter the rigorous certificate.

HEURISTIC short literature check: targeted searches for doubly-positive L2/L1 and Turan extremal constants returned related doubling/Turan/Logan work, including [Gorbachev–Ivanov's doubling problem](https://geodesic.mathdoc.fr/item/CHEB_2018_19_2_a6/), but no inspected exact theorem identifying this ratio. The search was capped as requested. No external novelty or completeness claim follows from it.

## Task 2(a–d): finite identities, two-scale bookkeeping and feasibility

PROVED exact two-scale bookkeeping (no compactness claim for individual height-normalized lifts). In a hypothetical counterexample sequence retain p, all P48/P53 macroscopic twisted profiles q_gamma, and their local Bessel budget. Choose P58's high-pass diagonal, and use its centered polynomial g>=-m, 0<=m<=M. For epsilon=M/sqrt(n) and lambda=sqrt(n/epsilon), P40 gives

    integral_{g<=lambda} g^2 <= lambda m+2m^2
        <= (sqrt(epsilon)+2epsilon^2)n = o(X).

Hence u=g 1_{g>lambda}>=0 has ||g-u||_2^2=o(X). Its tall energy can be recorded by the positive height-tagged measure

    d mu_X(x,h) = (2/X)u(x)^2 dx/(2pi) delta_{h=u(x)}.

Its mass tends to b=integral_0^1 e. Components with h comparable to X are retained as macroscopic atoms; the rest have lambda<=h=o(X). Use all height cutoffs as a family of measures, or a compactification of the height coordinate; a single normalized h/X coordinate would collapse the mesoscopic part to zero and lose the requested scale information. Subsequences exist for compactified finite marginals. No uniform individual profile compactness is inferred from this.

PROVED an exact amplitude-profile representation before taking limits. Partition the tall set into disjoint measurable cells I_s, each inside a radius-1/X window about a P55 separated-cover center x_s. Put h_s=max_{I_s}g (or the essential supremum), and

    w_s(t) = integral X u(x_s+y/X)1_{I_s}(x_s+y/X)
                      exp(-ity)dy/(2pi X h_s),
    c_k = 2 integral u(x)exp(-ikx)dx/(2pi)
        = (2/X)sum_s h_s exp(-ikx_s)w_s(k/X).

The first formula simplifies to integral u(x_s+y/X)1_{I_s}exp(-ity)dy/(2pi h_s). Each w_s is Hermitian PD, since it is the transform of a nonnegative cell function. The coefficient error between c and the actual residual coefficients is o(X) in squared l2 norm, by Parseval and the displayed P40 estimate. The cells carry the positive masses (2/X)integral_{I_s}u^2; keep cross terms in the displayed sum. These w_s are not supported on [-1,1], and their individual squared amplitudes cannot silently be equated with e. Their superposition has negligible coefficient energy outside that support. This identifies precisely the support/tightness issue of HBSC rather than assuming it away. Macroscopic atoms can first be removed at fixed height cutoffs and the remaining measure then records only the mesoscopic cells.

PROVED (a), quoted P32 made quantitative in the amplitude normalization. For any real centered polynomial T>=-m of degree D and the Fejer window F_w, put g_w=T*F_w and W=integral F_w^2. At every x_0,

    (1/W)integral F_w(x-x_0)^2(T(x)+m)^2 dx/(2pi)
        <= [rho_(D+w)(D+w+1)/W](m+g_w(x_0))^2.

With w=floor(theta X), D=X+o(X), the factor is 3r(1+theta)/(2theta)+o(1); the (1+theta) factor must be retained. Thus a spike of this normalized local energy E requires m+g_w(x_0)>=sqrt(E W/[rho_(D+w)(D+w+1)]). This is the exact front-amplitude requirement, before averaging. For an isolated packet of height h>>m with limit Phi(y)=T(x_s+y/X)/h and a genuine coefficient profile v_s for which front tests converge, it becomes

    theta^2/(2pi) integral sinc(theta y/2)^4 Phi(y)^2 dy
        <= r(1+theta) [Re integral_0^theta(1-t/theta)v_s(t)dt]^2.

Here sinc(z)=sin(z)/z. Without isolation and convergence of front tests the exact finite inequality still holds, but the right side concerns the total twisted amplitude at the center, not an arbitrarily chosen component. Errors are the exact finite Nikolskii error, w/X-theta=O(1/X), m/h, and the asserted local/profile convergence error; no rate for an unavailable compactness theorem is invented.

PROVED (b),(c), surviving aggregated form. For every real nonnegative trigonometric filter 0<=H<=1 of degree d_H, let T_H=Hf-mu_H, mu_H=mean(Hf), and m_H=M+mu_H. Then |mu_H|<=M and 0<=m_H<=2M. Write T_H=Re sum b_k exp(ikx), with degree <=X+d_H. P31's averaged window applies with coefficient energies |b_k|^2, and its exact error is proportional to m_H^2. More strongly, reflection-correlation gives

    m_H^2+(1/2)sum |b_k|^2 cos(ky)
        = integral (T_H(x)+m_H)(T_H(x+y)+m_H)dx/(2pi) >=0.

Every weak limit v_H(t)dt of X^(-1)sum |b_k|^2 delta_{k/X}, with d_H=o(X), therefore has nonnegative cosine transform whenever M^2=o(X); the finite lower error is -2m_H^2/X>=-8M^2/X. Whenever local spectral measures sigma_t have been constructed, all tested marginals v_H(t)=integral H^2 d sigma_t must be PD in t, in addition to the front-loaded measure window. This is the aggregate/windowed mesoscopic PD statement that survives unconditionally. It does not grant compact support or small total negative mass to the individual natural HBSC lifts.

PROVED (d), product windows give the new constraint. The last identity is exactly the averaged product window (T_H+m_H)(T_H shifted+m_H)>=0. For H=1 it only gives the familiar f/2+M^2>=0 because a_k^2=a_k. For H equal to the exact high pass it instead yields energy-PD, e=p(1-p) PD, and changes the macroscopic feasibility region. No higher-order lift is needed.

PROVED finite L6 window: for any nonnegative degree-L polynomial Q, Fejer-Riesz and ||U||_infinity^2<=(L+1)||U||_2^2 give

    integral Q^3 <= (L+1)^2(integral Q)^3.

Using Q=F_w shifted*(T+m) pointwise (multiplication, not convolution), then averaging window centers, gives

    W_3 [mean(T^3)+3m mean(T^2)+m^3]
        <= (D+w+1)^2 mean[(m+T*F_w)^3],
    W_3=mean(F_w^3).

This is rigorous with the trivial finite constant; no unverified sharp L6 Nikolskii constant is inserted. For a purely mesoscopic high-pass part with sup T=o(X), mean T^2=O(X), the third moment is o(X^2), so division by X^4 at a fixed proportional window erases this part. Retaining information requires height-weighted spike measures and isolated-packet L3 data. There is no claim here that all L6 refinements are redundant; the product-window constraint already suffices for the requested C extension.

PROVED (3), feasibility verdict: the specified exact witness and any packet system with that macroscopic p are infeasible for (a)–(d), local Bessel and the binary energy identity, because (d) plus that identity forces e PD and the witness violates e(t)<=e(0). More generally the argument proves the quantified T-dense(6.156) theorem above. Thus the brief's infeasible branch is fulfilled; an actual-set realization of the rejected formal object would contradict the proved inequality. No formal escape satisfying the enlarged system, and no small-R construction, is claimed.

## Task 3

PROVED (paper; elementary input, not kernel-checked). Every nonempty finite A of distinct positive integers with X=max A<=3n satisfies

    M(A) >= 10^(-6000005) sqrt(n).

PROVED internal novelty audit: a grep of PROOFS.md for Gaussian smoothing, geometric widths, energy increments and this constant found no existing corresponding proof. The finite-scale choice below replaces P58's diagonal and bypasses a robust P17 bound: the finite product constraint already contradicts the density at C=3.

PROVED notation. Let a_m=1_A(|m|), a_0=0 on Z. For real s>=1 put

    Z_s=sum_{m in Z} exp(-m^2/(4s^2)),
    k_s(m)=exp(-m^2/(4s^2))/Z_s,
    L_s(x)=sum_m k_s(m) exp(imx),
    q_s=k_s*a.

Thus 0<=q_s<=1 and q_s(m)->0 as |m|->infinity. Poisson summation gives 0<=L_s<=1. Its periodized-Gaussian formula on [-pi,pi] gives

    |L_s(x)-exp(-s^2 x^2)| <= 5 exp(-pi^2 s^2).

Consequently for S>=s, L_s-L_S>=-10 exp(-pi^2 s^2). We use only the following coarse Gaussian bounds:

    2s <= Z_s <= 4s+1,
    sum_m |m|k_s(m) <=4s,
    sup_z |d/dz sum_m a_m exp(-(z-m)^2/(4S^2))/Z_S| <=3/S.

PROVED details of these elementary bounds. Poisson gives Z_s>=2sqrt(pi)s>=2s; the monotone Gaussian Riemann sum gives Z_s<=1+2sqrt(pi)s<=1+4s. For the moment, compare m exp(-m^2/(4s^2)) on m>=1 with (x+1)exp(-x^2/(4s^2)) on [m-1,m], then divide by Z_s. This gives at most 2s/sqrt(pi)+1<=3s, hence the stated 4s. For the derivative, the integral of |d/dz exp(-z^2/(4S^2))| is 2, and its total variation is at most 4/S. The shifted-grid sampling bound sum F(z-m)<=integral F+TV(F) therefore gives a numerator at most 6, divided by Z_S>=2S. For the periodization error, the images are at distance at least (2k-1)pi and sum to at most 3exp(-pi^2s^2); the denominator differs from 1 by at most 3exp(-4pi^2s^2). These imply the displayed bound 5. All series converge absolutely; no numerical kernel test is used for these facts.

PROVED finite scale parameters. Put

    K=10^6, J=10^6, tau=10^(-3),
    beta=tau K^(-J)=10^(-6000003), c=beta/100=10^(-6000005).

Assume toward contradiction that M<c sqrt(n). If X<beta^(-2), the universal M>=1/2 gives M/sqrt(n)>=1/(2sqrt(X))>beta/2>c. Therefore X>=beta^(-2). Take s_j=beta X K^j, j=0,...,J. Every s_j>=1, and s_J=tau X. Also

    M/s_0 <= c,
    M exp(-pi^2 s_0^2) <= c,
    1/s_0 <= beta,
    M^2/s_0 <= c^2/beta.

PROVED almost-monotone PD energy increment. The sequence

    Q_s(m)=q_s(m)+2M k_s(m)

is PD, since its transform is 2L_s(f+M)>=0. In particular 0<=Q_s(0)<=1+M/s<=2. The signed spectral measure for Q_s-Q_S has negative mass at most 20M exp(-pi^2s^2). Hence, for every integer m,

    |Q_s(m)-Q_S(m)|
        <= Q_s(0)-Q_S(0)+40M exp(-pi^2s^2).

Telescoping the J identity-value increments selects j<J with Q_(s_j)(0)-Q_(s_(j+1))(0)<=2/J. For s=s_j and S=Ks, subtracting the diagonal regularizers gives the uniform estimate

    sup_m |q_s(m)-q_S(m)| <=2/J+42c < delta:=3/10^6.

This uses a finite pigeonhole principle. It does not use a compactness subsequence or the asymptotic relation M=o(sqrt(X)).

PROVED approximate binary energy identity, uniformly in position. Put q=q_s, r=a-q and E=k_s*r^2. The Lipschitz bound at scale S and the uniform increment give

    sum_u k_s(u)|q(m-u)-q(m)|
        <=2delta+(3/S)sum_u |u|k_s(u)
        <=2delta+12/K = omega:=18/10^6.

Since a^2=a and 0<=a,q<=1,

    E=q-2k_s*(a q)+k_s*q^2,
    |E(m)-q(m)(1-q(m))|<=4omega.

The first convolution product differs from q(m)^2 by at most omega, and the second by at most 2omega; this proves the error bound without a discrepancy hypothesis.

PROVED finite product constraint. Let r_0=-q(0), T=(1-L_s)f=r_0/2+g, and m_*=M+r_0/2. Then 0<=m_*<=M and g>=-m_* has mean zero. The autocorrelation of g+m_* is nonnegative. Therefore the sequence v with v_0=4m_*^2 and v_k=r_k^2 (k!=0) is PD. Its convolution with k_s is PD, so its value at every integer is at most its identity value. Since r_0^2<=1 and k_s(k)<=k_s(0)<=1/(2s),

    E(m)<=E(0)+(4M^2+1)/(2s) <=E(0)+2beta.

Combining the two preceding displays gives the finite energy maximum bound

    q(m)(1-q(m))<=q(0)(1-q(0))+8omega+2beta.       (EM)

PROVED finite density bound. Choose w+1=floor(4s). Since w<=4tau X and X>=100, the exact elementary P31-E constant obeys

    C_L=.811(X+w+1)+.71/3 <=(5/6)X,
    n/C_L>=2/5.

P31 gives S_A(w)>=W n/C_L-2M^2. For 0<=v<1,

    exp(-4v^2)>=(1-v)^2;

indeed the derivative of log(exp(-4v^2)/(1-v)^2) is 2(2v-1)^2/(1-v)>=0. Thus for k<=w, exp(-k^2/(4s^2))>=kappa_w(k)^2. With W>=2(w+1)/3>=(8s-2)/3 and Z_s<=4s+1,

    q(0) >= (2/Z_s)S_A(w)
         >= 8/15-1/s-M^2/s
         >= 8/15-2beta >53/100.

The P31 bracket is positive by these same bounds, so replacing Z_s by its upper bound has the indicated direction. This is a finite inequality, not a limiting front-density assertion.

PROVED crossing contradiction. Since q(0)>.53, q(m)->0 and

    |q(m+1)-q(m)|<=2delta+3/S<7/10^6,

some nonnegative integer m has |q(m)-1/2|<7/10^6. Therefore

    q(m)(1-q(m))-q(0)(1-q(0))
        >= (3/100)^2-(7/10^6)^2
        > 8omega+2beta,

contradicting (EM). Exact Fraction arithmetic in effective_checks.json verifies the relaxed comparison already with beta replaced by 10^(-12); the actual beta is much smaller. The proof establishes the stated explicit c(3).

PROVED finite/formalization scope. The new load-bearing steps are finite geometric telescoping, a signed-measure coefficient estimate, the exact binary identity, P31-E at one integer window, and a discrete intermediate-value crossing. No P31-N/Beckner or optimized rho certificate is needed for this c(3). The Gaussian lemmas use elementary Fourier/Poisson analysis and absolutely convergent sums. They have not been formalized here. If a strictly finite polynomial implementation is desired, truncate k_s outside [-R,R] and move its discarded mass tau_R to its zero coefficient: its transform remains in [0,1], since the omitted cosine tail has modulus at most tau_R. The coefficients remain nonnegative with total mass 1, and the transform changes by at most 2tau_R. Gaussian tail bounds choose finite R with tau_R<=c/[100(X+1)]; the resulting errors are far smaller than the displayed contradiction margin. This explains which analytic lemmas a Lean formalizer must supply; it is not a claim that such a Lean file was produced. No subagent was launched.

NUMERICAL independent checks: effective_checks.py also evaluates the Gaussian identities at s=1,2,5,10,30 and smoothing/energy formulas on seeded binary sets at X=100,300,800. Floating residuals at machine epsilon are not treated as rigorous kernel positivity or periodization certificates. Those checks test formulas and normalization only; the proof and exact constant comparisons are separate.

## Verification, task verdict and handoff

PROVED artifact map. `potential.py` discovers monotone potentials with Gurobi LPs and verifies rational Bernstein polynomials. `potential_g4_d8_exact.json` is the strongest rho certificate; degree 4 is an independent shorter fallback. `verify.py` reconstructs the certificates over QQ, verifies them by independent Sturm root counts, checks the rational T-dense constants, and proves the old witness's energy-PD violation exactly; output is `independent_verification.json`. `profile_numeric.py` and its JSON files preserve the local numerical profile experiments, resolutions, starts and seed. Its default path reproduces the earlier QCP-start/general-PWL comparison; `auto` runs the refined proximal-QP autocorrelation search. `effective_checks.py` / `.json` verify the optional proof's rational constant comparisons and retain numerical kernel sanity checks. `final_audit.py` / `manifest.json` list software versions, source/data hashes and source compilation status. All are inside tdense8_scratch.

PROVED reproduction commands (sequential; mathematical work only on the specified VM):

    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 180 python .research/agents/tdense8_scratch/potential.py g4 1 4 8 12
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 120 python .research/agents/tdense8_scratch/verify.py
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 360 python .research/agents/tdense8_scratch/profile_numeric.py
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 180 python .research/agents/tdense8_scratch/profile_numeric.py auto
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 120 python .research/agents/tdense8_scratch/effective_checks.py
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 60 python .research/agents/tdense8_scratch/final_audit.py

PROVED task verdict. Task 1 supplies a rigorous universal rho_1=.815276 with two independent exact arithmetic verification methods, and hence P58-only T-dense(5.311). Task 2 fulfills the infeasible branch: a new finite product constraint gives e PD, excludes the stated witness, and proves T-dense(6.156), strictly beyond 6.054. Task 3 supplies an explicit c(3)=10^(-6000005) by a finite-scale argument using P31-E and elementary Gaussian bounds. The general-versus-autocorrelation comparison is NUMERICAL only; equality of their suprema is still CONJECTURED/UNRESOLVED. The c(6.156) value remains ineffective. No general Chowla resolution, Epoch generator, certified small-R construction, external priority, independent human review or new Lean kernel verification is claimed.

PROVED new versus quoted. New relative to the inspected project record: four-point monotone-potential rho certificate; correlation/product-window energy-PD and the a<=1/2 consequence; the strengthened T-dense threshold 4(2-rho)/r; the aggregate filtered version; and the quantitative Gaussian energy-increment proof for c(3). Quoted/classical: P31-E/P31-N, P32, P40, P48/P52/P53, P58's exact diagonal, positive-definite/Toeplitz facts, Poisson summation and the elementary Fourier correlation identity. Their uses and normalization are spelled out above. No mature theorem was sent to a formalization agent because the brief explicitly prohibits subagents.

HEURISTIC final strategic review and three active directions. (1) Optimize the genuinely stronger variational class with both p and p(1-p) PD, plus all scalar and filtered windows; the old witness is no longer an admissible adversary. (2) Improve the four-point potential using longer Toeplitz constraints, while comparing the nonnegative autocorrelation numerical lower value .7238796 against rigorous general-class upper bounds. (3) Carry the finite Gaussian proof to the 6.156 range, or attack the remaining coherent mesoscopic spike configurations using the new positive marginal kernels; keep exact binary energy and cross terms in every attempted construction. The first concrete next experiment is a Gurobi PWL model imposing PD symbols for p and e simultaneously (e must be approximated with a certified interpolation error), then testing the resulting profile against the product constraint before any rounding experiment. Main open gap: whether the enlarged profile class remains feasible, and which additional phase-coherence constraint would exclude its surviving profiles. This is a completed round-8 checkpoint, not a claim of unattended future work.
