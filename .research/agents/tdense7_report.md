# Round 7 T-dense report

Status: ROUND-7 CHECKPOINT. PROVED on paper: T-dense(4.4393), hence T-dense(3), with a nonquantitative positive constant, using quoted P31-N. The elementary-input version proves T-dense(4.213). Task 2 has a numerically optimized escape near C=6.05 and an exact PD/all-window witness at C=6.053863..., giving 4.4393<C_PD<=6.053863.... The exact reach over every alternative microscopic model remains undetermined. All edits are confined to this report and tdense7_scratch. No commits or subagents. Mathematical computation ran through DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2. Optimization used Gurobi, Threads=2, NonConvex=2 when needed. No new result is claimed kernel-checked.

PROVED target definition (quoted). T-dense(C) means: there exists c(C)>0 such that every finite nonempty set A of distinct positive integers, with X=max A<=C n and n=|A|, satisfies M(A)>=c(C)sqrt(n), where f_A(x)=sum cos(ax) and M(A)=-min over all real x.

PROVED source audit. Read CLAUDE.md; P29, P31, P31-C, P36, P38, P44, P47, P49, P53; NOTEBOOK night continuation 6; E70/E70b/E72/E72c; the exact high-pass implementation e70_p47_scan.py and the annealer e72_p47_pareto.c. P31 and the stable-Gram argument are quoted ingredients. No claim of external priority is made.

HEURISTIC frontier and three active lines. (1) Replace P47's model/discrepancy selection by a diagonal exact high-pass argument for arbitrary binary sequences. (2) Combine the resulting profile constraints with a quantitative positive-definite profile energy gap. (3) Optimize the profile escape constraints and realize the escaping profiles as genuine sets. The first two concern universal lower bounds; the third tests the putative construction mechanism.

PROVED current result map. R7-T gives a contradiction at C=3 from normalized stable Gram. R7-CF uses the sharp pointwise Caratheodory-Fejer envelope, reaching C=4.164 or 4.331 depending on the quoted Nikolskii input. R7-D then gives a simpler universal L2/L1 profile gap and the strongest result, C=4.4393 (or 4.213 with elementary P31-E). Model selection and the proposed block lemma are bypassed for existence of a constant; no quantitative block lower bound is asserted. The exact high-pass diagonal is the new link between arbitrary binary sets and the rounding-energy profile.

## R7-T: T-dense(3), full compactness proof

PROVED (paper proof, not kernel-checked; new relative to the supplied project record). There is a constant c_3>0 such that every nonempty finite A of distinct positive integers with max A<=3|A| satisfies M(A)>=c_3 sqrt(|A|). The argument below does not make c_3 effective. It uses the proved P31 window inequality and P31-E's asymptotic constant r=811/1000, together with elementary Fourier positivity and the stable-Gram argument. No prefix discrepancy, Lipschitz bound, block hypothesis, or prescribed rounding model is assumed.

PROVED Step 1, contradiction sequence. If the theorem fails, choose A_j with X_j<=3n_j and M_j/sqrt(n_j)->0. For nonempty A, the nonnegative polynomial f_A+M has mean M and a Fourier coefficient 1/2, so M>=1/2. Therefore n_j,X_j->infinity. Pass to a subsequence with n_j/X_j->d>=1/3. The even coefficient step functions, taking a_m=1_A(|m|), a_0=0, zero outside [-X_j,X_j], converge weak-* after scaling m by X_j to an even function p supported in [-1,1], with 0<=p<=1 and integral_0^1 p=d.

PROVED Step 2, continuous PD representative. For every real y,

    f_(A_j)(y/X_j)/X_j -> integral_0^1 p(t)cos(ty)dt >=0,

since M_j/X_j->0. Thus the Fourier transform P(y) of the even p is nonnegative. Testing against exp(-epsilon y^2) and using 0<=p<=1 bounds integral P(y)exp(-epsilon y^2)dy by 2pi. Monotone convergence gives P in L1. Fourier inversion then supplies a continuous positive-definite representative of p, still between 0 and 1 and supported in [-1,1]. In particular p(1)=0. Write a=p(0); then 0<a<=1 and |p(t)|<=a. This is the untwisted special case of quoted P48, with its Fourier argument included to avoid an additional external theorem dependency beyond the standard inversion/positivity facts.

PROVED Step 3, exact high-pass diagonal (arbitrary binary sets). For integers h>=1 put

    k_h(m)=(1-|m|/(h+1))_+/(h+1),
    q^(j,h)=k_h*a^(j),   r^(j,h)=a^(j)-q^(j,h).

Here convolution is on Z, using the actual even binary sequence. One can choose h_j->infinity, h_j/X_j->0, so that the scaled step functions q^(j,h_j) converge strongly in L2(R) to p. To see this, first fix epsilon>0 and take h=floor(epsilon X_j). Weak-* convergence of a^(j) implies strong L2 convergence of its convolution to p*k_epsilon: the continuous triangular kernel is fixed and compactly supported, the convolutions are equicontinuous and supported in a common compact interval, and discretization tends to zero. Then let epsilon decrease to zero and choose a diagonal, using p*k_epsilon->p in L2. The thresholds of this diagonal are the source of ineffectivity.

PROVED Step 3 continued, energy identity. Since a_m^2=a_m and 0<=q_m<=1,

    (a_m-q_m)^2=a_m-2a_m q_m+q_m^2.

Strong L2 convergence of q to p and weak-* convergence of a to p imply weak convergence of the scaled squared-coefficient measures to e(t)dt, where e=p(1-p). Indeed for every bounded continuous test function the cross term a q tends to p^2, while q^2 tends strongly in L1 to p^2. The positive-side total energy divided by X_j tends to b=integral_0^1 e; its window-weighted energy tends to integral_0^theta (1-t/theta)^2 e(t)dt. The o(X_j) frequencies between X_j and X_j+h_j cause no limiting mass.

PROVED Step 4, lower bound is preserved exactly. The multiplier

    H_h(x)=1-K_h(x)/(h+1)

lies in [0,1], where K_h is the Fejer kernel with coefficients (1-|m|/(h+1))_+. Thus T_j=H_(h_j) f_(A_j)>=-M_j everywhere, and

    T_j=r_0/2+sum_(m>=1) r_m cos(mx).

Since r_0=-q_0 in [-1,0], the centered polynomial g_j=sum_(m>=1)r_m cos(mx) is >=-m_j, with m_j=M_j+r_0/2. Averaging T_j>=-M_j shows 0<=m_j<=M_j. Apply the generalized P31 coefficient-window inequality to g_j and m_j, degree at most X_j+h_j. This uses the same Fejer-Riesz/Parseval proof; positivity of the coefficients is not required. No subtraction of a model or P47 additive error occurs.

PROVED Step 5, necessary window conditions. For fixed 0<theta<=1, take w_j=floor(theta X_j). Divide P31 for the original set and for g_j by X_j^2, using M_j^2=o(X_j), m_j^2<=M_j^2, h_j=o(X_j), and rho_L<=r+o(1). The limits give, respectively, for v=p and v=e,

    (2theta/3) integral_0^1 v
        <= r(1+theta) integral_0^theta (1-t/theta)^2 v(t)dt.

Both p and e are continuous at zero. Divide by theta and let theta decrease to zero. Therefore

    a>=2d/r,                 a(1-a)>=2b/r.                     (W)

PROVED Step 6, normalized stable Gram. For t in (0,1], put N=floor(1/t)+1, so Nt>1 and N<=2/t. Positive definiteness, or its positive spectral measure, gives

    a-p(Nt)<=N^2(a-p(t)).

As p(Nt)=0, p(t)<=a(1-t^2/4). Consequently

    integral p^2 <= a d-(a/4)integral t^2 p
                 <= a d-d^3/(12a),

where integral_0^1 t^2 p>=d^3/(3a^2) is the elementary filling bound for 0<=p<=a and mass d (fill [0,d/a] first). Thus

    b >= d(1-a)+d^3/(12a).                                   (G)

PROVED Step 7, rational contradiction at d>=1/3. Combining (W) and (G), multiplying by a, gives

    a(1-a)(a-2d/r) >= d^3/(6r).

Put t=2/(3r)=2000/2433 and q=15/16. Since d>=1/3, this implies a>=t and

    a(1-a)(a-t) >= 1/(162r)=500/65691.

If t<=a<=q, the left side is at most q(1-t)^2/4=937445/126282432. If q<=a<=1, the quadratic (1-a)(a-t) decreases on that range (q>(1+t)/2), so the left side is at most (1-q)(q-t)=4495/622848. Both are strictly below 500/65691. The smaller margin is 640985/3409625664>0. This contradiction proves R7-T.

PROVED quantifier audit. The contradiction excludes every sequence with X<=3n and M/sqrt(n)->0, so inf of that ratio over all such nonempty finite sets is positive. Bounded X cannot escape because M>=1/2. The constant is uniform in A and X; its existence is proved, but this compactness proof supplies no numerical value. All trigonometric lower bounds above are on the whole circle, not sampled grids.

NUMERICAL algebra audit. VM Python 3.12.3, NumPy 2.5.4 and Gurobi 13.0.3 are available. algebra.json verifies the rational contradiction using exact Fraction arithmetic. The sharp reach of just inequality (G) plus (W) is numerically C=3.0131822505 with r=.811, or C=3.1465517789 with the proved asymptotic Beckner constant; these are boundaries of this scalar reduction, not the reach of the full method. The theorem holds at every smaller C by the same strict-inequality contradiction. The value using the unproved .687 constant is only a diagnostic and is not used in a theorem.

## Strategic review after the first two attacks

PROVED advance. Model selection is unnecessary for an ineffective theorem: exact high-pass multiplication plus a diagonal strong-L2 smoothing limit supplies P47's energy conditions for arbitrary sets. The normalized identity value a in the stable-Gram inequality is essential; replacing it by 1 loses the C=3 contradiction. Both parts have been derived with all sequence quantifiers above.

HEURISTIC decision. Discontinue the proposed block-discrepancy case split for the existence theorem: it is bypassed, rather than established. Keep the effective-constant problem open. Pursue a sharper PD profile envelope and the numerical escape profile. A non-PD fixed profile already has linear M from a negative value of its cosine transform, so it cannot be treated as the actual reach limit once the linear-M mechanism is allowed.

NUMERICAL correction to the first profile experiment. profile.py used piecewise-constant profiles and imposed many cosine-transform nonnegativity samples. Its B=24 envelope model was infeasible immediately. This does not bound the intended continuous profile class: exact nonzero staircases are never continuous PD, and their high-frequency aliasing can make that discretization inconsistent. The infeasible result is retained as an audit artifact but is not evidence about C*. The replacement profile_pwl.py uses continuous piecewise-linear interpolation, whose PD condition is positivity of an explicit finite cosine symbol.

## R7-CF: T-dense(4.331), with exact rational certificate

PROVED (paper lemma). Any even continuous PD p supported in [-1,1], with p(0)=a, satisfies

    0<=p(t)<=a u(t),
    u(t)=cos(pi/(floor(1/t)+2)),   0<t<=1.

Indeed the positive-definite sequence p(kt), k in Z, has finite support |k|<=m=floor(1/t). Its Fourier polynomial is nonnegative: it is the limit of its positive Fejer means, or equivalently the quadratic form tested on (1,e^(ix),...,e^(iNx))/sqrt(N+1). By Fejer-Riesz it equals |sum_(j=0)^m z_j e^(ijx)|^2. Its first coefficient p(t) is Re sum z_(j+1) conjugate(z_j), bounded by a times the largest eigenvalue cos(pi/(m+2)) of the path adjacency matrix divided by two. This eigenvalue follows directly from the sine eigenvectors. Boundary points t=1/k only weaken the estimate because p(1)=0.

PROVED scalar envelope reduction. Let u_bar be any decreasing upper step envelope for u. Write U(s)=integral_0^s u_bar and V(s)=integral_0^s u_bar^2. For mu in [0,U(1)], let F(mu)=V(U^(-1)(mu)), with linear interpolation across each constant step. Since q=p/a lies in [0,u_bar] with mass mu=d/a, the filling inequality gives integral q^2<=F(mu): first use q^2<=u_bar q, then maximize the latter weighted integral by filling the largest u_bar values first. Therefore b>=d-a^2 F(d/a).

PROVED continued reduction. Put k=2/r. Conditions (W) imply mu<=1/k and

    a <= (1-k mu)/(1-k F(mu)),
    d <= D(mu):=mu(1-k mu)/(1-k F(mu)).

For a target box C, it suffices to establish, on 0<=mu<=1/k,

    Q_C(mu):=1-C mu+C k mu^2-k F(mu)>0.                    (CF-cert)

The denominator is positive: F(mu)<mu for every mu>0 with the full envelope; for the finite envelope its initial F=mu segment has mu<1/k, and all later segments have F<mu. For step u_bar, F is piecewise linear and Q_C is a convex quadratic on each piece. Its exact minimum is at a segment endpoint or at the vertex (C+k u_bar)/(2Ck).

PROVED finite rational envelope definition. On [0,1/101] set u_bar=1. On [1/(n+1),1/n], n=100,...,1, set x_n=333/(106(n+2)) and

    u_bar=1-x_n^2/2+x_n^4/24-x_n^6/720+x_n^8/40320.

The classical rational bound 333/106<pi and the alternating cosine series give u_bar>=cos(pi/(n+2)); these step values decrease with t. The Taylor derivative is negative for 0<x<=333/318, so the ordering also follows directly. All quantities in (CF-cert) are rational.

PROVED finite exact certificate, executable verification on the VM. envelope_exact.py checks every segment minimum using Fraction arithmetic. It reports a strict positive margin for C=4.164 at r=.811, and C=4.331 at r=.77. These finite inequalities combined with R7-T's compactness steps prove T-dense(4.164) using P31-E alone, and T-dense(4.331) using quoted P31-N, since 4/(3sqrt(3))<.77. Both constants c(C) remain ineffective. The exact certificate is in envelope_exact.json. The decimal locations from envelope.py (4.164686 at .811 and 4.332215 at the Beckner limit) are NUMERICAL diagnostics of this particular scalar envelope, not the reach of all windows or all models.

PROVED assembly for an arbitrary C passing (CF-cert). Repeat R7-T Steps 1-5 with X_j<=C n_j, so d>=1/C; do not use the special d>=1/3 algebra. The PD envelope gives d<=D(mu), while (CF-cert) gives D(mu)<1/C for every allowed mu. This contradiction proves the theorem for all sets in the box. The exact minimum margins exceed 1/25000 for C=4.164, r=.811, and 1/100000 for C=4.331, r=.77. constants_exact.json additionally verifies the rational pi bound from the Machin identity, using four alternating terms for arctan(1/5), and verifies 16/27<(.77)^2.

## R7-D: a simpler universal profile-energy gap, extending the theorem further

PROVED (paper lemma; new relative to this project record, external priority unchecked). For any continuous nonzero nonnegative PD q on R, with q(0)=1 and q in L1, define I_j=integral_0^infinity q(t)^j dt. Then

    I_2/I_1 <= v_* := (1+sqrt(17))/(4sqrt(2)) < .905646.

PROVED proof. Bochner/Jensen gives q(2t)>=2q(t)^2-1. Multiply by q(t)>=0 and integrate:

    I_3 <= I_1/2 + (1/2)integral q(t)q(2t)dt
        <= I_1/2 + I_2/(2sqrt(2)),

by Cauchy-Schwarz and integral q(2t)^2=I_2/2. A second Cauchy-Schwarz inequality gives I_2^2<=I_1 I_3. Therefore v=I_2/I_1 satisfies v^2<=1/2+v/(2sqrt(2)), whose positive root is v_*. All integrals are finite because 0<=q<=1. This argument needs no support restriction and no numerical optimization.

PROVED combination with exact high-pass compactness. For the limiting profile p, put a=p(0), d=integral p and b=integral p(1-p). Apply the lemma to q=p/a to get

    integral p^2 <= v_* a d,
    b >= d(1-v_* a).

The energy condition in (W) now implies

    d <= (r/2) a(1-a)/(1-v_* a)
      <= (r/2)/(1+sqrt(1-v_*))^2.

Thus T-dense(C) holds for every

    C < (2/r)(1+sqrt(1-v_*))^2,

whenever r is an asymptotic P31 Nikolskii upper bound. This proof only needs the energy window, the PD profile, and the exact diagonal high-pass. The original density window is consistent but not needed in this last scalar contradiction.

PROVED rational certificate form. Take r=769801/1000000 and v=905646/1000000. The exact inequalities r^2>16/27 and 8(v^2-1/2)^2>v^2, v^2>1/2, prove r>4/(3sqrt(3)) and v>v_*. With k=2/r, a candidate C is valid whenever

    k-(k v+C)^2/(4C)>0.

Indeed C a^2-(k v+C)a+k is then positive for every real a, and hence d<=a(1-a)/(k(1-v a))<1/C. The exact Fraction computations in moment_gap.py verify the constants stated in moment_gap.json. This retains a paper/exact-arithmetic status; it is not kernel verification and does not give an effective c(C).

PROVED strongest theorem and exact margin. There exists c>0 such that every finite nonempty set A of distinct positive integers with max A<=(44393/10000)|A| satisfies M(A)>=c sqrt(|A|). At C=44393/10000 the preceding quadratic minimum is exactly

    3506490276101151/1052280271169087720000 > 0.

Using r=.811 instead gives T-dense(4.213), with exact margin 63761551/443356571680>0, without Beckner. Both statements are proved by the contradiction sequence and exact high-pass diagonal above. The numerical limiting reaches of this last scalar inequality are 4.439325748 (Beckner) and 4.213803396 (elementary); neither is the full profile-method reach.

## Task 2: precise escape definitions and first results

PROVED ambiguity audit. Merely requiring b=integral p(1-p)>0 does not exclude profiles arbitrarily close to an indicator. For the raw P31/P47 macroscopic window conditions, the reach is exactly C_raw=2/r, not a new value above 3, when r>=2/3. Indeed p(0)<=1 and (W) force d<=r/2. Conversely take p=a 1_[0,phi], 0<a<1 and phi=r/2. Density and rounding energy are scalar multiples of the same indicator. If theta<=phi, window failure is 2phi<=r(1+theta). If theta>=phi, put u=phi/theta; the window integral divided by its mass equals 1-u+u^2/3, which is at least 1/(1+2u), since the difference after multiplication is u(1-u)(1-2u/3)>=0. Therefore window failure follows from 3r(1+theta)>=2(theta+r), true for r>=2/3. Let a increase to 1. The infimum box ratio is 2/r, with b>0 at every a<1. These fixed step profiles are non-PD and have linear negative cosine-transform dips. They are not counterexamples to R7-T. A quantitative meaning of "not near 0/1", and a specified class of admissible alternative models, is necessary to make the brief's full C_1* unique.

PROVED useful well-defined refined problem. Fix r=4/(3sqrt(3)). Define C_PD as the infimum of 1/d over nonzero even continuous nonnegative PD profiles supported in [-1,1], with support reaching 1, 0<=p<=1, b>0, and BOTH macroscopic window inequalities in Step 5 for every theta in (0,1]. This automatically excludes the non-PD linear-M profile obstruction. All regular fixed macroscopic models whose prefix discrepancy is o(X) have the same limiting p, so choosing such a different model does not change these conditions. This does not assert that every microscopic or X-dependent P47 model, or every other positive multiplier, is represented by C_PD.

PROVED lower bound for this refined reach. R7-D proves C_PD>4.4393 with the true asymptotic r=4/(3sqrt(3)); its rational proof uses the slightly weaker r=.769801. Strictness has a finite rational margin. This is a reach lower bound, not a computation of the full infimum.

NUMERICAL Gurobi results at r=.7698, b>=.01. Continuous piecewise-linear profiles are interpolated at i/B, p_B=0, p_(B-1)>=1e-5, with exact quadratic energy integrals. PD is sampled through S(theta)=p_0+2 sum_(i=1)^(B-1) p_i cos(i theta)>=1e-6. All quadratic equalities use NonConvex=2, Threads=2.

| B | sampled PD grid | status | density incumbent | density upper bound | incumbent C |
| --- | ---: | --- | ---: | ---: | ---: |
| 24 | 1025 | Gurobi OPTIMAL at relative gap .001 | .1649536523 | .1650490855 | 6.062308934 |
| 48 | 4097 | 180-second TIME_LIMIT | .1653486109 | .3103187511 | 6.047828251 |

NUMERICAL limitations. The fine symbol reevaluation finds minima -1.18e-5 and -5.19e-6, respectively, so the raw candidates are not claimed PD. Their energy-window tightness occurs at theta tending to zero, while the density window has substantial slack. The exact repaired witness is given below. No discretization convergence theorem or global optimality at B=48 is claimed. The full C_1* of all alternative models remains unspecified/uncomputed; C_PD has a numerical candidate near 6.05.

NUMERICAL mechanism candidate. The optimized shape resembles the scaled sine autocorrelation

    q(s)=(1-s)cos(pi s)+sin(pi s)/pi,  0<=s<=1,
    p(t)=a q(t/phi),  0<=t<=phi,

with a about .655 and phi about .62, plus a very small far tail. This is PD because q is the normalized autocorrelation of a half-sine. Its integrals are integral q=4/pi^2 and integral q^2=1/6+5/(4pi^2). Thus v=(integral q^2)/(integral q)=pi^2/24+5/16. Optimizing only the theta=0 energy condition over amplitude gives a=1/(1+sqrt(1-v)) and d=(r/2)/(1+sqrt(1-v))^2. This explains the observed C near 6.05; it does not prove global optimality among all PD profiles or all windows.

NUMERICAL run correction. The initial exact-witness verification failed before any certificate was evaluated because SymPy was absent from the VM. SymPy 1.14 was installed through dirun. Pip temporarily replaced mpmath 1.4.1 by 1.3.0; the original mpmath 1.4.1 was restored before final verification. All subsequent verification completed on the VM. No local mathematical computation was substituted.

## Exact escaping profile and actual sets

PROVED finite exact witness. The 49 rational nodal values in witness_B48.json define p by linear interpolation at i/48, even reflection, and zero extension. They are obtained from the B=48 Gurobi candidate by rounding each node to denominator 10^9, multiplying by 999/1000, adding 1/20000 to p(0), and setting p(1)=0. They lie in [0,1], and p(47/48)>0 ensures support reaches 1. The profile has

    p(0)=.656320080992,
    d=.16518378313908333...,
    1/d=6.053863042705642...,
    b=.08673803465569628...,
    b/d=.525100182399041... .

The displayed decimals are NUMERICAL summaries of exact rationals saved in the file. A positive rounding-energy share exceeding half the mass is far from the near-indicator escape.

PROVED PD certificate. For this piecewise-linear even profile the full Fourier transform is

    (1/48) sinc(y/96)^2 [p_0+2 sum_(i=1)^47 p_i cos(iy/48)].

Here sinc(z)=sin(z)/z. Exact Sturm counting for the rational Chebyshev polynomial S(t)=p_0+2 sum p_i T_i(t) finds zero roots in [-1,1], and S(1)>0. Hence S>0 on that interval and the Fourier transform is nonnegative on the entire real line. This is an exact finite algebraic certificate, not a positivity conclusion from the 4097-point optimization grid.

PROVED all-window certificate. For v=p and v=p(1-p), define J_v(theta)=integral_0^theta (theta-t)^2 v(t)dt. On each of the 48 interpolation cells, J_p is a polynomial of degree at most 4 and J_e of degree at most 5. For r=3849/5000=.7698, which is strictly below 4/(3sqrt(3)), the exact rational polynomials

    r(1+theta)J_v(theta)-(2/3)theta^3 integral_0^1 v

have nonnegative Bernstein coefficients on every cell (divide by theta^3 in the first cell). There were 48 verified leaves for each profile, with no adaptive subdivision needed. Thus both window-failure inequalities hold for EVERY theta in (0,1], also with the larger true Beckner constant. witness.py contains the exact derivation and verifier; witness_B48.json records every cell result. This proves the upper bound C_PD<=6.053863042705642..., while R7-D proves the lower bound C_PD>4.4393. No equality of either endpoint with C_PD is claimed.

NUMERICAL numerical reach estimate. The raw incumbents at B=24,48 and the half-sine formula (predicted C=6.046990286) suggest a reach near 6.05 for this explicitly defined PD/macroscopic-window problem. This estimate has no continuum global-optimality certificate. The B=48 solver's 87.7% relative gap is reported above; the exact repaired witness is an upper bound regardless of that gap. The full C_1* including every alternative microscopic model remains unresolved.

NUMERICAL realization protocol. At target n=512,1024,2048,4096 choose X=ceil(n/d). Cell probabilities are X times the exact profile integral over ((j-1)/X,j/X), computed in floating point, rescaled by n/(Xd) to total n. Cumulative rounding uses phase .3721. The random construction draws independent Bernoulli values with these probabilities, rejecting until the cardinality is exactly n; it is therefore conditional Bernoulli, not an unconditioned independent sample. Seed is 2026101907 and the attempt counts are saved. If X is absent, remove the smallest element and add X, preserving n and pinning the true endpoint; that single change does not change the limiting profile. Every output is independently checked for positivity, distinctness, n and X.

| n | X | cumulative R estimate | conditional-Bernoulli R estimate | cumulative certified R lower | random certified R lower |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 512 | 3100 | 2.196809 | 1.984815 | 2.19 | 1.98 |
| 1024 | 6200 | 2.080615 | 1.934010 | 2.08 | 1.93 |
| 2048 | 12399 | 2.186993 | 1.821003 | 2.18 | 1.82 |
| 4096 | 24797 | 2.445833 | 2.056875 | 2.44 | 2.05 |

NUMERICAL minimum protocol. R estimates use a power-of-two FFT grid with at least 128X samples on the full circle, plus direct cosine minimization near the best 24 local minima. They are not certified whole-circle minima or upper bounds on M. The exact point certificates in the last two columns are PROVED finite lower bounds for M/sqrt(n): at the saved rational angle, 192-bit Arb balls prove f_A(x)+r sqrt(n)<0. This establishes a genuinely large negative value without claiming that it is the global minimum. point_certificates.json records angle, cosine enclosure, threshold and strict negative slack.

NUMERICAL family comparison. For these eight sets, the enlarged elementary P31/P47 scan yields only .0078-.0232 times sqrt(n); the numerical-rho=.687 scan yields .0252-.0480 times sqrt(n). P29 gives .0077-.0317 times sqrt(n). The four tested largest-ratio P36 gaps give no positive bound after the gap error. Exact rational reevaluation verifies the selected elementary window lower bound for every set; these weak certificate values do not limit the true M. The escaping profile is Chowla-safe in all realized finite tests, certified at R>=1.82; no small-R construction or asymptotic R->0 mechanism is observed.

## Required adversarial finite-set search

NUMERICAL search scope. pareto.c adapts e72_p47_pareto.c but fixes max A=X throughout, avoiding the endpoint shrinkage in E72c. For (n,X)=(128,384), use 300000 swaps, two restarts, and mu=0,.1,.3, seed 2026101907. For (512,1536), use 180000 swaps, one restart and mu=0,.1, seed 2026101908. The objective is the sampled P31/P47 bound at asymptotic r=.811 divided by sqrt(n), plus mu times the 8X-grid R. This is annealing, not a complete search or a valid finite certificate by itself. The entire compiled batch completed under the 300-second VM wall limit; per-restart runtime was not instrumented.

NUMERICAL independent reevaluation. evaluate.py scans a larger h/theta family, uses the actual finite elementary Nikolskii bound .811+.2367/(L+1), and checks P29, prefix-P29 minus tail cardinality, and the four largest-ratio P36 gaps. All eight explicit sets are saved in adversarial_sets.json. The pure-certificate n=512 set is the worst among these tests: its enlarged elementary window bound is .0533264 sqrt(n), with numerical R=4.810674 and a PROVED point certificate R>=4.81. The pure-certificate n=128 sets have numerical R=3.13 and 3.06; one is additionally caught by prefix P29 minus the tail at .52017 sqrt(n). At n=128, the mu=.1 sets have numerical R=.9176-.9182, while the mu=.3 sets have R=.9347 and 1.0071; the smallest has a PROVED point certificate R>=.91. The n=512,mu=.1 set has R=1.164464 and P29=.404764 sqrt(n). These are evidence about the sampled search only, not a finite proof of T-dense(3).

PROVED finite certificate details. For selected h,w, the high-pass coefficients have integer numerators with denominator (h+1)^2, so E,S,W and the elementary Nikolskii upper bound are rational. evaluate.py forms them independently of the FFT convolution and rounds the square root down to denominator 10^8. Those lower bounds are in adversarial_checks.json and realized_checks.json. The stronger pointwise negative-value certificates for all 16 sets are in point_certificates.json. Neither certificate type asserts an all-circle lower bound for f_A.

## Supplementary dip-filling lemma and its exact limitation

PROVED (elementary; the brief's dip-filling calculation made precise). Let F,B be disjoint finite sets of distinct positive integers. For any u>0 let D={x:f_F(x)<=-u}, and let alpha be its normalized circle measure. If alpha>0, then

    M(F union B) >= u-sqrt(|B|/(2alpha)).

Indeed if M(F union B)=m<u, then f_B>=u-m on D; Parseval gives |B|/2=integral f_B^2>=(u-m)^2 alpha. If m>=u the displayed bound is immediate. In particular a front with a negative dip of depth c sqrt(|F|) on measure at least alpha remains Chowla-safe after every arbitrary tail of size at most delta|F| whenever delta<2alpha c^2. A lower bound c/2 for the front normalization survives when delta<=alpha c^2/2; divide by sqrt(1+delta) to express it relative to the total size.

PROVED obstruction to applying this from P31's minimum bound alone. For F={1,...,N}, P31 certifies a square-root minimum, but for every fixed c>0 the set {f_F<=-c sqrt(N)} has measure O_c(N^(-1/2)). From

    f_F(x)+1/2=sin((N+1/2)x)/(2sin(x/2)),

that set is contained in |sin(x/2)|<=1/(2c sqrt(N)-1), of measure at most (2/pi)arcsin(1/(2c sqrt(N)-1)) once the denominator exceeds 1. Hence the hypothesis M(F)>=c sqrt(|F|), even when P31-certified, gives no uniform positive dip measure. This does not refute T-dense for the union; it identifies the additional distributional input needed for this particular dip-filling lemma. No new universal C extension is claimed from dip filling.

## Verification, provenance and handoff

PROVED what is new relative to the supplied record. The discrepancy-free exact high-pass diagonal; the resulting rounding-energy necessary condition for arbitrary sets; the normalized stable-Gram combination proving C=3; the CF-envelope finite certificate; and the universal doubly-positive L2/L1 gap leading to T-dense(4.4393). The exact rational PD/all-window profile is a new obstruction witness for the specified macroscopic family. The generalized coefficient-window argument, P31-E/P31-N, Fourier positivity, Fejer-Riesz, the path eigenvalue inequality and the stable-Gram idea are quoted/classical ingredients, with their needed implications derived here. No external priority or kernel verification is claimed.

HEURISTIC focused novelty audit. A short primary-source search revisited [Bu et al., 2026](https://arxiv.org/abs/2610.17160), whose abstract gives a dense-box n^(1/4) lower bound, [Sanders, 2008](https://arxiv.org/abs/0807.5104), and [Kolountzakis, 1996](https://doi.org/10.1006/jnth.1996.0002). This is not a complete priority search. The new proof is assessed from its explicit argument, not from absence of search hits.

PROVED reproduction commands, sequentially from the repository root (all mathematical work runs on the specified VM):

    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 300 bash .research/agents/tdense7_scratch/run_search.sh
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 100 python .research/agents/tdense7_scratch/algebra.py
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 150 python .research/agents/tdense7_scratch/profile_pwl.py pd 24 120
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 240 python .research/agents/tdense7_scratch/profile_pwl.py pd 48 180
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 120 python .research/agents/tdense7_scratch/envelope_exact.py
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 60 python .research/agents/tdense7_scratch/moment_gap.py
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 240 python .research/agents/tdense7_scratch/evaluate.py search
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 180 python .research/agents/tdense7_scratch/witness.py certify 48
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 360 python .research/agents/tdense7_scratch/witness.py realize 48
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 120 python .research/agents/tdense7_scratch/point_certify.py
    DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 120 python .research/agents/tdense7_scratch/finalize.py

PROVED artifact map. moment_gap.py/json is the shortest exact arithmetic certificate for the strongest theorem. envelope_exact.py/json and constants_exact.json verify the earlier CF proof independently. witness.py and witness_B48.json give all rational nodal data, exact PD and all-scale window checks. summary.json contains compact numerical tables; manifest.json contains software versions and source hashes. adversarial_sets.json, realized_sets.json, their checks, realized_construction.json and point_certificates.json preserve every notable finite set and certificate. All paths are inside tdense7_scratch. The abandoned staircase model and its infeasible result are retained with their stated limitation.

PROVED task verdict. Task 1 succeeds at the paper-proof/nonquantitative level, exceeding C=3. Task 2 supplies a specified escape problem, numerical extremizer, exact obstruction profile, realizations, and rigorous reach bounds; it does NOT determine the full C_1* over every alternative model, or prove continuum optimality of the numerical extremizer. The supplementary dip-filling lemma is proved, but the distributional hypothesis needed to extend T-dense by that route remains open. No general Chowla theorem, Epoch construction, effective c(3), or kernel-checked round-7 theorem is claimed.

HEURISTIC final strategic review and concrete handoff. Three useful next directions remain: (1) quantify the exact high-pass diagonal to extract an effective c at C=3 or 4.4393; (2) improve the universal doubly-positive L2/L1 gap or solve the PD/all-window variational problem with certified continuum bounds; (3) obtain a dip-measure or residual-energy statement for the fractional front, while using the certified profile as an adversarial input. The first concrete derivation is a finite-scale replacement for the diagonal: select a Fejer smoothing width through an energy-increment argument and bound both its profile approximation error and its identity value. The exact profile above is the rejection test for any claim that density and rounding-energy windows alone settle all C. The project is checkpointed; no unattended continuation is implied.
