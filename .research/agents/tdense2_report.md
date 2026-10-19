# T-dense round 2 — completed research report

All calculations in this report are executed only on dirichlet through `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2`. No commits, subagents, root research-note edits, or LaTeX manuscripts.

## Main findings and task disposition

* **PROVED / T1:** TD5 disproves the quantified LM-dense single-filter certificate at C=16, with an effective, search-defined infinite family. Its proof uses positive Fejer mixtures, not the unproved mixed-triple estimate for sharp Bohr unions. Separately, M>=sqrt(n)/128 on that family. The construction is not computationally practical: X=2^t, t>=1024.
* **PROVED finite / NUMERICAL / T1:** exact full-q audits of eight sharp Bohr unions through ambient X=200000 support the original obstruction heuristic. Their cosine minima remain numerical. Original P39-O(ii)'s sharp-union asymptotics remain unproved.
* **PROVED / T2:** reciprocal masks work with a constant independent of J on high-probability realizations of the positive-mixture obstruction family (TD6). Seventh-moment rational witnesses give M>=sqrt(n) for all four J=32..40 Bohr samples, and M>=(4/5)sqrt(n) for the four J=16..20 samples. No infinite sharp-Bohr-union theorem from moments 5 or 7 is claimed.
* **PROVED / T3:** TD7 extends P38 from cumulative rounding to bounded prefix discrepancy plus averaged local overshoot. TD7-O gives a full-profile fixed-discrepancy family on which the fixed q=2 window cannot recover a square-root constant.
* **CONJECTURED / T4:** MS is a precise deterministic multiplier-selection statement sufficient for the general dense theorem. Its missing invariant is retained residual variance at bounded positive bump mass. It is not proved.
* **PROVED correction:** P39's physical-space variance identity needs deletion of the zero coefficient; the verified centered third-moment formula is unchanged.

These are paper proofs and exact finite calculations, not new kernel verification. External priority is unchecked. The full T-dense target is not solved.

## Scope and frontier

**CONJECTURED (target, inherited).** For every real C >= 1 there exists c(C) > 0 such that every nonempty finite A of distinct positive integers with X=max A <= C|A| satisfies -min_x sum_{a in A}cos(ax) >= c(C)sqrt(|A|).

**PROVED (quoted project inputs).** P38 gives this for its cumulative profile roundings; TD4 gives a sufficient third-moment criterion. P40 gives the spike-truncation criterion. None is a proof of the target for arbitrary C.

**HEURISTIC (inherited).** P39-O(ii) proposes dense Bohr unions as an obstruction to every single denominator filter. The mixed triples and overlap/union errors require verification; finite growth cannot alone disprove its quantified LM statement.

**PROVED / NUMERICAL (mechanisms investigated this round).** Exact finite Bohr-union audits; positive Fejer mixtures with independent Bernoulli thinning as an infinite obstruction; reciprocal spike masks; local discrepancy expressed as shift variation rather than prefix mass alone. Individual statuses are specified below.

## Normalization correction discovered during setup

**PROVED (new audit correction).** In P39's physical-space variance formula, the zero-frequency coefficient must be removed. For s=1_{A union(-A)}, g=2s-s(. -q)-s(. +q), and a_q=1_{q in A}, g(0)=-2a_q. Therefore the centered T=(1-cos(qx))f+a_q/2 has

    V = (||g||_2^2 - 4a_q)/16,

not the full norm divided by 16. Writing r(k)=sum_j s(j)s(j-k), this is

    16V = 12n - 8r(q) + 2r(2q) - 4a_q.

The quoted Delta and centered W formulas remain valid:

    32W = Delta + 48a_q V + 4a_q,
    Delta = 10c(0)-15c(q)+6c(2q)-c(3q).

Proof: Fourier coefficients of H_q f are g/4; centering deletes g(0)/4. Expand the squared difference and then the centered cube. For A={1}, q=1, T=cos x-(1/2)cos 2x, giving V=5/8, whereas the uncentered norm gives 7/8. This correction does not change the previously verified TD4 coefficient formula or asymptotic obstruction.

## Reproducibility

Scratch directory: `.research/agents/tdense2_scratch/`. Exact finite claims and numerical minima are recorded separately. Claims below are marked PROVED / NUMERICAL / HEURISTIC / CONJECTURED.

## TD5: an effective infinite counterexample to LM-dense

**PROVED (new paper proof; not kernel-checked).** There is a terminating algorithm producing, for every integer t >= 1024, a set A_t subset [1,X], X=2^t, with n>=X/16, such that, simultaneously for every integer 1<=q<=X,

    V_q >= X/256,
    W_q >= X^2/(2^28 J^2),       J=128(t+1).

Consequently

    W_q/V_q^(3/2) >= sqrt(X)/(2^30 J^2) -> infinity

uniformly in q. Moreover the algorithm can require f_A(pi)<=-sqrt(X)/128, so M(A)>=sqrt(n)/128. This disproves LM-dense as quantified in P39, already at C=16. It does not disprove T-dense. The construction below is a positive Fejer-mixture analogue of the proposed Bohr unions, rather than a proof of the sharp-cutoff union heuristic.

### TD5.1. Positive signal and effective choices of angles

**PROVED.** Write N=X+1 and

    F_N(x) = (1/N)|sum_{j=0}^{N-1} exp(ijx)|^2,
    B(x) = F_N(x)+(1/(4J))sum_{i=1}^J [F_N(x-theta_i)+F_N(x+theta_i)].

All integrals use normalized Haar measure on the circle. Thus B>=0, integral B=3/2, integral B^2<=(9/4)N (convexity/Jensen applied to its positive mixture), and

    F(x):=(B(x)-3/2)/4 = sum_{m=1}^X p_m cos(mx),
    p_m=(1/2)(1-m/N)[1+(1/(2J))sum_i cos(m theta_i)].

In particular, w_m/4 <= p_m <= 3w_m/4 <=3/4, where w_m=1-m/N.

Take theta_i independently uniform on the P=16X equally spaced points. For each 1<=q<=X the order of q in Z/PZ is at least 16 and is a power of two, so P(cos(q theta_i)<=0)>=1/2. The elementary binomial Chernoff bound gives

    P(#{i:cos(q theta_i)<=0}<J/4) <= exp(-J/8).

For completeness, Markov applied to exp(-log(3)*K) bounds this by
`[3^(1/4)*(2/3)]^J <= exp(-J/8)`; increasing each success probability can only improve the bound. Union over q costs at most X exp(-J/8). Since P>X, discrete Fourier orthogonality gives E B(pi)=F_N(pi)+1/2<=1. Markov therefore bounds P(B(pi)>16) by 1/16. Their sum is less than 1. Choose the lexicographically first angle tuple satisfying

    #{i:cos(q theta_i)<=0}>=J/4 for every q<=X, and B(pi)<=16.

This is an effective finite selection: all values are real algebraic numbers in cyclotomic fields, so each comparison is decidable exactly. Repeated angles are allowed and do not invalidate any positive-mixture inequality.

### TD5.2. A cubic lower bound for every filter, with no mixed-triple estimate

**PROVED.** On |u|<=1/(4N), the sine formula gives F_N(u)>=N/4. If cos(q theta_i)<=0, then q<N and

    1-cos(q(theta_i+u)) >= 3/4 >=1/2.

Thus, for H_q=1-cos(qx), integrating over that interval,

    integral H_q^3 F_N(x-theta_i)^3 >= N^2/8192.

Indeed its normalized length is 1/(4 pi N), and the crude lower bound is N^2/(2048 pi)>N^2/8192. Since every summand of B is nonnegative, its cube dominates the sum of the cubes of its summands, even if bumps overlap. At least J/4 of the chosen positive shifts contribute, giving

    integral H_q^3 B^3 >= N^2/(2^21 J^2).

Expanding (B-3/2)^3/64, dropping its positive linear term, using H_q^3<=8 and integral B^2<=(9/4)N, gives

    integral (H_q F)^3 >= N^2/(2^27 J^2)-2N.

Let T_0=H_q F+p_q/2. Since mean(H_q F)=-p_q/2 and p_q>=0, the centered third moment equals the raw third moment plus `(3p_q/2) Var(H_q F)+p_q^3/8`, which is nonnegative. Also integral T_0^2<=N. Hence

    integral T_0^3 >= N^2/(2^27 J^2)-2N.

This is the point that replaces the unproved mixed-triple step in P39-O(ii).

### TD5.3. Rounding errors and density

**PROVED.** Independently select a_m in {0,1} with probability p_m. Put xi_m=a_m-p_m and Z=sum xi_m cos(mx). Then

    sum p_m >= X/8,
    sigma^2:=sum p_m(1-p_m)>=X/32.

The second inequality uses 1-p_m>=1/4 and sum w_m=X/2. Hoeffding gives P(n<X/16)<=exp(-X/128).

Use a grid of K=64X^2 points on the circle and set R=10 ceil(sqrt(X(t+1))). Since |Z'|<=X(X+1)/2<=X^2, its value differs from that at a nearest grid point by less than 1. At a fixed point the independent summands have mean zero and absolute value <=1, so the (weaker than usual) Hoeffding bound `P(|Z|>u)<=2 exp(-u^2/(2X))` suffices. A union bound shows

    P(||Z||_infinity>R) <= 128X^2 exp(-(R-1)^2/(2X)),

which is less than 1/512 for t>=1024. No sampled numerical minimum is used in this proof.

The centered noise in T_q is E_q=H_q Z+xi_q/2, so ||E_q||_infinity<=3R. Since integral T_0^2<=N and R>=sqrt(N), expansion and Cauchy give

    |integral (T_0+E_q)^3-integral T_0^3|
        <=9RN+27R^2 sqrt(N)+27R^3 <=63R^3.

For all q this proves W_q>=N^2/(2^27 J^2)-2N-63R^3. For t>=1024,

    R<=20 sqrt(X(t+1)), J=128(t+1),
    2N+63R^3 <= X^2/(2^28 J^2).

One sufficient elementary inequality is `2^(t/2)>=2^64(t+1)^4`. It holds at t=1024 because the right side is less than 2^108 and the left side is 2^512, and the ratio increases thereafter: its consecutive ratio is sqrt(2)*((t+1)/(t+2))^4>1. This proves the stated W bound.

**PROVED.** Uniform positive variance can also be imposed. The coefficient of xi_m in centered T_q is H_q cos(mx)+(1/2)1_{m=q}; its squared integral is at least 1/4 (the exceptional q=2m gives exactly 1/4). Independence yields E V_q>=sigma^2/4>=X/128. Changing one a_m changes at most six entries of g_q, each in [-2,2], so |change in V_q|<=24/16<2. McDiarmid's elementary bounded-differences bound gives

    P(V_q<X/256)<=exp(-X/131072).

Union over q is less than 1/512 for t>=1024. This supplies the nonvacuous V bound; the divergence conclusion itself only needs the cubic bound and V_q<=2n, the latter following from H_q<=2 and integral f^2=n/2.

### TD5.4. A separate square-root negative witness

**PROVED.** At pi, the chosen signal satisfies F(pi)<4. The independent centered sum Z(pi)=sum (-1)^m xi_m has variance sigma^2>=X/32 and fourth moment at most 3sigma^4+sigma^2<=4sigma^4. Holder interpolation gives E|Z(pi)|>=sigma/2. Since E Z(pi)=0, E Z(pi)_- >=sigma/4. Paley-Zygmund applied to its negative part now gives

    P(Z(pi)<=-sigma/8)>=1/64.

In detail, P(Y>=(1/2)EY)>=(EY)^2/(4 EY^2), with EY>=sigma/4 and EY^2<=sigma^2. The preceding density, variance and uniform-error failure probabilities total less than 1/128 (the much smaller density term is included). Their complement therefore intersects this negative-tail event. For t>=1024, sigma/8-4>=sqrt(X)/128. The intersection yields f_A(pi)<=-sqrt(X)/128.

### TD5.5. A terminating integer-only output algorithm

**PROVED.** For input t>=1024, set X=2^t and J=128(t+1). Enumerate subsets A of [1,X] lexicographically until all of the following exact tests hold:

1. n>=X/16;
2. for every q<=X, the rational moments (computed by finite integer convolution) satisfy V_q>=X/256 and W_q>=X^2/(2^28 J^2);
3. the integer sum sum_{a in A}(-1)^a is <=-sqrt(X)/128 (decide using integer signs and squares).

The probabilistic proof above proves that the search terminates for every such t. It is an effective explicit family, with deliberately enormous computational complexity and threshold; it is not offered as a practical construction at t=1024. The proof uses random positive Fejer mixtures to establish existence of a passing subset, but the final selection tests do not require algebraic probabilities or numerical trigonometry. No claim is made that this is the original sharp Bohr-union family or that its constants are optimized.

## TD6: reciprocal spike masks recover a constant independent of J

**PROVED (new, on the positive-mixture random family; not asserted for every sharp Bohr union).** Conditional on any angles as above, let H=1/(1+B). With probability at least `1-2^30/X-1/512-1/2048`, the Bernoulli realization has

    |mu|=|integral Hf|<=33,
    V=Var(Hf)>=X/2^20,
    W=integral(Hf-mu)^3 <=2^16 X^(3/2)

for X sufficiently large (X>=2^40 suffices for these deliberately loose estimates). These bounds do not depend on J. For X>=2^128, TD4 implies M>=sqrt(X)/2^58. The good event intersects all the events used in TD5, so there are realizations on which every single denominator filter fails uniformly but this one reciprocal mask succeeds with a fixed square-root constant.

Proof. Since F=(B-3/2)/4, |HF|<=3/8<1. On the complement of U={B>12}, whose measure is at most 1/8, H>=1/13. For every positive integer m,

    integral H^2 cos^2(mx) >= (1/169)(1/2-1/8)>1/512.

Write Q=integral H^2 Z^2. Independence and the variance bound from TD5 give EQ>=X/16384. Its Gram matrix G has entries integral H^2 cos(mx)cos(kx), operator norm <=1/2, and sum G_mk^2<=X/4. Expanding the quadratic form using independent centered |xi_m|<=1 gives Var Q<=X. Therefore

    P(Q<X/32768)<=2^30/X.

The mean noise eta=integral HZ has variance at most 1/2, by Bessel's inequality, so P(|eta|>32)<=1/2048. On this event's complement, |mu|<=33. Removing the mean from HZ costs at most 1024 in its squared norm; adding the bounded signal HF costs at most 1 in norm. For X>=2^40 these bounds imply V>=X/2^20.

For each x, independence gives E Z(x)^2<=X and E Z(x)^4<=4X^2, whence E|Z(x)|^3<=2X^(3/2). Fubini and Markov give

    P(integral |HZ|^3>1024 X^(3/2))<=1/512.

Using |u+v|^3<=4(|u|^3+|v|^3) twice, |HF|<1 and |mu|<=33, bounds the centered absolute third moment by 2^16 X^(3/2). Thus B_TD4<=2^46. The positive root kappa(b)=(sqrt(b^2+4)-b)/2 is at least 1/(b+1) for b>=0. Hence m=M+mu>=sqrt(X)/2^57, and subtracting |mu|<=33 gives M>=sqrt(X)/2^58 for X>=2^128. Negative W only improves the conclusion. The combined failure bounds in TD5 and TD6 are less than 1/64 at t>=1024, so they still intersect the negative-tail event there.

**PROVED (finite polynomial approximation).** The reciprocal is not itself a trigonometric polynomial, but this is not an essential restriction. Put L=(3/2)N, so 0<=B<=L, and

    H_d=(1/(1+L))sum_{k=0}^d ((L-B)/(1+L))^k.

Then 0<=H_d<=H<=1 and `||H-H_d||_infinity <= [L/(1+L)]^(d+1)`. Since |f|<=X, uniform approximation with error o(X^-3) preserves the above moment inequalities with slightly relaxed constants. Taking d=256N(t+1) is more than sufficient when X=2^t. This gives an effective algebraic-coefficient positive polynomial certificate; it is very high degree. There is no product-filter factor `(3/8)^(J/2)`.

**PROVED (exact formulas for arbitrary finite multipliers).** If `H=sum h_k exp(ikx)` is real and nonnegative, `s=1_S`, and `R_j=(h^{*j}*s^{*j})(0)/2^j`, with R_0=1, then

    mu=R_1, V=R_2-mu^2, W=R_3-3mu R_2+2mu^3,
    moment_k(T)=sum_{j=0}^k binom(k,j)(-mu)^(k-j)R_j.

For rational h these are exact rational combinations of integer sum counts. For the reciprocal itself one may equivalently use

    R_j=2^-j sum_{a_1,...,a_j in S} Fourier(H^j)(-sum a_i).

These identities follow by multiplying finite Fourier series (or integrable bounded multipliers against f^j). They do not assert that numerical quadrature is exact.

## Higher moments: exact witnesses rather than floating PSD claims

**PROVED (general certificate; application new, framework standard).** If T has mean zero and T>=-m, define mu_k=integral T^k, mu_0=1. For each integer r>=0,

    K_r(m)=[mu_(i+j+1)+m mu_(i+j)]_(0<=i,j<=r) is PSD.

Proof: for every real polynomial P of degree <=r, integral (T+m)P(T)^2>=0. Thus moments through 2r+1 suffice. A negative generalized eigenvalue is a numerical way to find a witness; a rational vector p gives the exact inequality

    m >= - sum p_i p_j mu_(i+j+1) / sum p_i p_j mu_(i+j),

whenever the denominator is positive. The implementation rounds the eigenvector to integers and evaluates this ratio using Fraction and exact FLINT integer convolution. The reported rational bound is rigorous conditional only on the exact input set and elementary Fourier identity; the eigenvalue is not used as a certificate.

For H_q, form the Laurent polynomial G(z)=sum_{j !=0}g_q(j)z^j (zero constant coefficient). Exactly

    mu_k=CT G(z)^k/4^k.

For H=1 use G(z)=2sum_{s in S}z^s. These formulas incorporate every centering term and apply through order 7 without modular wrap. `audit.py:moments` uses FLINT fmpz_poly, hence arbitrary-size signed integer coefficients.

**Strategic review (after the infinite obstruction and first finite audits).** The missing uniform single-filter lemma is now refuted by TD5. Stop trying to prove it or interpreting bounded-size success as evidence of its truth. Fixed higher moments remain useful finite certificates but have no established uniform-in-J theorem here. Pursue spike masks and local shift variation; distinguish the effective Fejer-mixture proof from the still heuristic original union argument. The remaining full dense theorem requires a deterministic way to retain enough variance after masking positive structure.

## TD7: P38 extends to averaged local overshoot, with bounded discrepancy

**PROVED (new paper theorem).** Retain the profile hypotheses of P38: q>=1, 1<=r<=q integers; p nonincreasing in [0,r/q]; 0<=r/q-p(t)<=Lt; and p<=1/(q+1) on [t0,1], where mu_tail=integral_(t0)^1 p>0. Replace cumulative rounding by arbitrary binary a_1,...,a_X satisfying, for a fixed real D>=0,

    |sum_(i<=j)(a_i-p(i/X))|<=D       (0<=j<=X).

For d_j=sum_(i=j+1)^(j+q) a_i, assume in addition that fixed K0,K1>=0 satisfy

    O_q(w):=sum_(j=0)^w (d_j-r)_+
        <=K0+K1 (w+1)(w+q)/X          (0<=w<=X-q).                 (LO)

Then every nonempty resulting A satisfies M(A)>=c(p,q,D,K0,K1)sqrt(n), for a positive explicit constant given below. In particular, bounded prefix discrepancy plus the front cap d_j<=r is sufficient (K0=K1=0). LO allows a sparse set of cap violations; it is weaker than the pointwise front cap.

### TD7 proof and constants

**PROVED.** Put z_j=r-d_j and beta_j=sum_(i<=j)(a_i-p(i/X)). Then

    sum_(j=0)^w z_j <= qL(w+1)(w+q)/X+2qD,
    sum_(j=0)^w |z_j| = sum z_j+2O_q(w).

The first inequality follows by summing p-deficits and telescoping `beta_(j+q)-beta_j`, leaving two boundary blocks of length q. Since d_j-d_(j-1)=a_(j+q)-a_j is in {-1,0,1},

    (a_(j+q)-a_j)^2 <= |z_j|+|z_(j-1)|.

For b_j=a_j-(a_(j-q)+a_(j+q))/2, even extension and zero padding as in P38, Jensen and a boundary cost q therefore give

    S_w<=sum_(j<=w)b_j^2
       <=A0+2K (w+1)(w+q)/X,
    A0=q+4qD+4K0,     K=qL+2K1.                                  (F)

**PROVED.** Prefix discrepancy alone supplies enough *tail* energy, with worse constants. Let K_run=ceil(2D(q+1))+1. A run of ell selected positions spaced q apart, entirely in the tail, occupies an interval of length q(ell-1)+1. The profile mass on it is at most that length divided by q+1; interval discrepancy is at most 2D. Thus

    ell <=[q(ell-1)+1]/(q+1)+2D,
    ell <=2D(q+1)+1-q <=K_run.

There are at least `mu_tail X-2D-2` tail elements. Splitting them into q-chain runs gives at least that number divided by K_run runs. At most q of their starts have a selected predecessor before the tail cutoff. At every remaining start b_j>=1/2. Therefore

    E=sum b_j^2 >=(mu_tail X-2D-2)/(4K_run)-q/4.

For `X>=(4D+4+2K_run q)/mu_tail`, this yields `E>=lambda X`, where lambda=mu_tail/(8K_run).

**PROVED.** Set

    theta=min(1/4,lambda/[100(K+1)]),
    X0=ceil(max(100,2(q+1)/theta,
                (4D+4+2K_run q)/mu_tail,8A0/(theta lambda))).

For X>=X0 use w=floor(theta X) in the inherited TD-window inequality, with degree X+q. Its constants obey C_window<=2X, W_window>=2theta X/3, and (F) gives `S<=A0+8K theta^2 X`. Hence

    W_window E-C_window S
        >=(2/3)theta lambda X^2-16K theta^2 X^2-2A0 X
        >=theta lambda X^2/4.

Since `2(C_window-W_window)<=4X`, `(2M)^2>=m^2>=theta lambda X/16`. For X<X0 use the universal M>=1/2. Thus one explicit constant is

    c=min(1/(2sqrt(X0)),sqrt(theta lambda/64)).

This proof quotes P38/TD-window and its underlying kernel-checked Nikolskii input, but the local-overshoot argument and the tail-run replacement are new paper arguments. The theorem is not itself kernel-checked.

### What is and is not the weakest rounding assumption

**PROVED.** For this method, the exact requirement at a chosen q,w is a positive margin `W_window E-C_window S` of order X^2. That is the sharp algebraic criterion delivered by TD-window. There is no canonical weakest hypothesis among all possible rounding conditions. LO is a concrete weaker substitute for cumulative rounding that gives the required small front variation. An asymptotic variant suffices: bounded D, positive tail mass, and

    lim_(theta down to 0) limsup_(X to infinity) O_q(floor(theta X))/(theta X)=0.

Indeed the added front cost is o(theta X), whereas the useful term is a fixed multiple of theta X^2. Choose theta first, then X. No particular quadratic bound LO is necessary.

**PROVED (first local failure).** Bounded mass discrepancy by itself does not imply LO or the front-energy estimate. At density 1/2, the periodic string 1100 has prefix discrepancy <=1 but d_j-r=+1 on one quarter of its length for q=2,r=1. Thus O_2(w)=w/4+O(1), while cumulative rounding would give zero overshoot. This is the smallest period of a balanced binary string with that q-cap violation.

### TD7-O: a full-profile bounded-discrepancy obstruction to the minimal-denominator window

**PROVED (new, asymptotic paper obstruction).** Bounded prefix discrepancy alone does not ensure a square-root certificate from the *fixed minimal denominator q=2* followed by TD-window, even for p(t)=(1/2)(1-t)^2. This does not assert failure of every q, every multiplier, or T-dense.

Construction: choose fixed block length B=65536 and a=1/20; let X tend to infinity through multiples of B. At block endpoints use the exact cumulative profile counts. Inside each block beginning at j<=aX, put the prescribed m selected positions in the string 1100, truncated after m ones and padded with zeros. In all later blocks, put all m ones in one q=2 chain at the beginning of the block. Since each block has m<=B/2, this is feasible. At every block endpoint the discrepancy is less than 1; inside it the discrepancy is at most B+1. Thus D=B+1 is fixed independently of X, n/X->1/6, and max A/X->1.

For q=2, the interior of a 1100 portion has b_j^2=1, on 2m positions. A q=2 chain has filter energy <=3/2 when isolated. Only a bounded number of positions per block meet a boundary. Counting them, with a generous error allowance of 20 per block, gives

    E <= (a+20/B)X+O(B) <=1.01aX+O(B),
    sum_(j<=u)b_j^2 >=.89u-O(B)       (0<=u<=aX).

Here 2p(t)>=(1-a)^2=.9025 on the front, and .9025-20/B>.89. The boundary allowance can be checked directly from the support {j-2,j,j+2}: a transition affects at most four additional indices, each with square <=1, and a chain's isolated energy is <=3/2; 20 covers their interactions as well.

For w/X->s>0, summation by parts gives

    S_w/X >=.89 integral_0^min(a,s) (1-u/s)^2 du+o(1).

The limiting TD-window numerator is strictly negative:

* If 0<s<=a, its positive part is at most `(2/3)s*1.01a`, while its negative part is at least `.811*.89*s/3`.
* If a<=s<=2a, the corresponding bounds are `(4/3)*1.01a^2` and `.811*.89*a/3`.
* If 2a<=s<=1, they are `(2/3)*1.01as` and `.811*.89*a(1+s)/2`. The latter is larger even at s=1, and the difference is linear in s with its minimum there.

All three comparisons are strict at a=1/20. If w=o(X), the positive part of the TD-window bound for m^2 is O(w)=o(X), since C_window-W_window is bounded below by a positive multiple of X. By subsequences, the maximum over *all* windows of the positive lower bound for m^2, divided by X, tends to zero. Therefore this fixed-filter window certificate cannot supply c sqrt(n) with c>0 on this family. Other filters, including q=4, are not excluded.

## TD8: a precise fixed-order moment obstruction (abstract distributions)

**PROVED (new obstruction for a specified certificate class, not a cosine-set construction).** For each fixed integer r>=1 there is a constant C_r such that, for all sufficiently large integers X, a centered random variable T_X has variance asymptotic to a positive constant times X and minimum `-sqrt(X)-O(1)`, yet all shifted Hankel/localizing matrices through moment 2r+1 are PSD at m=C_r. Thus no method using only those PSD conditions can uniformly recover a square-root bound for arbitrary spike-plus-bulk distributions. This does not prove failure of order 5 or 7 on all filtered cosine sums.

Proof. Let Y be uniform on [1,2], a_k=E Y^k=(2^(k+1)-1)/(k+1), and let epsilon be an independent symmetric sign. With probability 1-1/X put

    T_X=sqrt(X)epsilon-b_X,   b_X=a_1/(1-1/X),

and with probability 1/X put T_X=XY. This has mean zero, minimum -sqrt(X)-b_X, and mu_2/X->1+a_2. For k>=3, mu_k/X^(k-1)->a_k. Express `K_r(m)` in the polynomial basis 1,T/X,...,(T/X)^r. For fixed m its limit is

    [ m   b^T ]
    [ b    D  ],

where b_1=1+a_2, b_j=a_(j+1) for j>=2, and D_ij=a_(i+j+1) for 1<=i,j<=r. D is positive definite: its quadratic form is `E[Y*(sum_(i=1)^r v_i Y^i)^2]`, positive for every nonzero polynomial on [1,2]. Choose C_r=1+b^T D^-1 b. The limiting matrix is strictly positive definite by its Schur complement; convergence makes K_r(C_r) positive definite for all sufficiently large X. Every smaller shifted Hankel matrix is a principal submatrix, and the ordinary Hankel matrices are PSD because the distribution is real. This proves the claimed obstruction. For r=1, C_1=107/27. Exact r=1,2,3 Schur thresholds are recorded by `proof_checks.py`.

This proves the precise limitation behind the phrase "a few more moments see through spikes": they can improve finite constants, but fixed-order PSD alone is insufficient for general distributions. A cosine-specific relation or an adaptive multiplier is required for a theorem about this problem.

## T4: a precise deterministic selection lemma that would finish T-dense

**CONJECTURED (sufficient selection lemma; no proof for arbitrary dense A).** For every C>=1 there are constants K,L,eta>0 such that every sufficiently large finite A subset [1,Cn] of cardinality n admits a nonnegative real trigonometric polynomial B with integral B<=K and a real |gamma|<=K for which, writing

    H=1/(1+B),  R=f_A-gamma(B-integral B),

one has

    integral H^2 R^2 >=eta n,
    |integral HR| <=K,
    integral |HR|^3 <=L n^(3/2).                                  (MS)

The polynomial degree may depend on A; constants K,L,eta may depend only on C. This is a testable deterministic statement about retaining bulk energy after removing positive structure. The moment formulas above make every polynomial approximation of the proposed certificate checkable.

**PROVED (reduction, new precise packaging of the remaining gap).** MS implies T-dense. Indeed, for S=gamma H(B-integral B), `||S||_infinity<=K max(1,K)=:K_s`. Therefore the mean of Hf is bounded by K+K_s; the centered L2 norm of HR is at least `sqrt(eta n-K^2)`, and adding S costs at most K_s. For all sufficiently large n, V=Var(Hf)>=eta n/4. The inequality |u+v|^3<=4(|u|^3+|v|^3), twice, bounds its centered third absolute moment by a constant depending only on K,L times n^(3/2). TD4 then gives `M+mean(Hf)>=c sqrt(n)` for c=c(K,L,eta)>0. Subtract the bounded mean and absorb finitely many small n using M>=1/2. Thus M>=c(C)sqrt(n).

**HEURISTIC (energy-increment implementation, not a proof).** Start with B=0. If the residual violates the third-moment bound, locate a positive spike component and add a positive Fejer bump to B. The unfinished invariant is a bound on total bump mass `integral B<=K(C)` together with preservation of `integral H^2R^2>=eta(C)n`. Pure structure can be removed at low mass cost in TD5/TD6; arbitrary deterministic 0/1 coefficients need not have independent noise, and the proof of TD6's variance lower bound does not transfer to them. A successful increment argument must prove this invariant or find a different terminal certificate. The number of independent components J alone is not the right cost variable: TD6 handles arbitrarily many with fixed total positive mass.

**PROVED / scope check.** This selection lemma is sufficient, not established equivalent to T-dense. The known P40 truncation criterion remains an exact general distributional reduction. No universal structural decomposition, general energy increment, or new all-C dense theorem is claimed here.

## T1 finite Bohr-union construction and results

**PROVED (description of explicit finite inputs).** For each ambient X in {4096,16384,65536,200000}, choose

    J=ceil(k log X/log log X), k=8 or 4,
    epsilon=1/(8J), alpha_i=u_i/2147483647,
    U={1<=m<=X:min_i ||m alpha_i||<epsilon}.

Seed `2026101900+X` selects the saved u_i and then integer thinning draws. All eight first angle samples passed the *exact* finite condition

    #{i:min_(1<=j<=3)||jq alpha_i||<3epsilon}<=floor(J/2)  for every q<=X.

Keep m in U when its saved uniform integer draw in `[0,5(X+1)^2)` is less than `4(X+1-m)^2`. Thus the thinning profile is the convex decreasing `(4/5)(1-m/(X+1))^2`; membership, angle activity, and the final bitstring use only integer comparisons. Parameters, all angle numerators, seeds and every selected frequency are saved in each input JSON. The nominal epsilon parameter C0=2 is not the final density constant: tapering and thinning make these sets substantially sparser. All eight satisfy max A<=17n.

The reason for both k choices is discriminating: k=8 makes the activity requirement very comfortable but dilutes individual components; k=4 tests whether less dilution strengthens the excess while still passing the same finite condition. No seed optimization of M or W was performed. Pseudo-random generation is only a method of selecting these fixed inputs, not a probabilistic proof about the family.

**PROVED (exact finite moment audit).** The following q is the exact minimizer of W_q/V_q^(3/2) among *all* 1<=q<=X with V_q>=n/10. Every q in each Bohr input in fact meets that variance threshold. Ratios below are decimal renderings of exact algebraic quantities from rational V,W; M and M/sqrt(n) are NUMERICAL grid-plus-Newton estimates.

| k | ambient X | n | J | maximum active | minimizing q | min W/V^(3/2) | M (NUMERICAL) | M/sqrt(n) (NUMERICAL) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 4096 | 236 | 32 | 8 | 895 | -0.125735 | 31.817264 | 2.071127 |
| 8 | 16384 | 922 | 35 | 9 | 1192 | 0.153429 | 73.147808 | 2.408995 |
| 8 | 65536 | 3882 | 37 | 10 | 2917 | 0.547765 | 151.688301 | 2.434582 |
| 8 | 200000 | 11817 | 40 | 9 | 22934 | 0.946261 | 288.758234 | 2.656322 |
| 4 | 4096 | 268 | 16 | 7 | 1140 | 0.214058 | 33.731213 | 2.060462 |
| 4 | 16384 | 901 | 18 | 8 | 898 | 0.394355 | 75.942848 | 2.530023 |
| 4 | 65536 | 3914 | 19 | 9 | 16138 | 1.065448 | 161.732969 | 2.585164 |
| 4 | 200000 | 11878 | 20 | 10 | 30175 | 1.883905 | 297.653569 | 2.731112 |

**NUMERICAL interpretation.** Both sequences show growth in the minimum standardized cubic moment; neither finite sequence alone contradicts LM-dense with its unspecified constants. The smaller-J family shows the expected stronger obstruction. Original sharp-union P39-O(ii) still needs control of overlaps and mixed triples for an asymptotic proof; TD5 avoids rather than fills that gap.

**PROVED (exact count algorithm).** `audit.py:exact_counts` forms `P(z)=sum_(s in S)z^(s+max A)`, multiplies P^2 and P^3 over the two primes 998244353 and 1004535809 using FLINT nmod_poly, and reconstructs each coefficient of P^3 by CRT. This is an exact alternative to a hand-coded two-prime NTT. For each k, c(k)<=|S|^2=4n^2, strictly below the prime product. Pair counts are <=2n and fit the first prime. All intermediate machine integer products are below 2^60<2^63. The full arrays c(0..3max A) and r(0..2max A) are saved in compressed NPZ files. The comparisons of candidate minima use integer signs and cross-products of W^2 and V^3, not floating comparisons.

**PROVED (independent checks).** A separate FLINT fmpz_poly multiplication over Z reproduced *every* saved cubic coefficient for the three largest Bohr(k=8), Bohr(k=4), and Fejer cases: respectively 579370, 586468, and 596209 coefficients. Direct ordered-tuple enumeration also agreed with both modular convolutions and centered Fourier moment formulas on 63 small random sets and every q in their support range. The largest finite Fejer example has c_max=2751454716, above 998244353, so a one-prime computation would indeed wrap.

**NUMERICAL (positive-mixture finite falsification check).** The practical Fejer variant uses J=ceil(2 log X), delta=1/2, modulation 1/2, the saved rational angles, and triangular thinning. Its minimum standardized cubic moments at the same sizes are -0.358379, -0.105886, -0.080280, -0.043815. This does not show practical failure of the single-filter certificate in that parameter range. It also does not meet TD5's much stronger angle-count guarantee: its minimum counts of indices with cos(q theta_i)<=0 are 2,1,2,2. TD5's theorem uses J=128(t+1) and an explicit very large threshold; do not substitute these finite samples for its hypotheses. Their M/sqrt(n) numerical values are 2.160904, 2.234339, 2.542780, 2.964092.

## T2 finite higher-moment and mask results

**PROVED (finite rational certificates).** The chosen q is the exact third-moment minimizer above; higher moments were not optimized over q. Decimal entries are the rigorous rational lower bound for M divided by sqrt(n), rounded for display. The exact rational witnesses and moments are in each JSON. The simple stated bounds in the first-page summary are independently checked using rational squares.

| k | ambient X | order 3 | order 5 | order 7 |
|---|---:|---:|---:|---:|
| 8 | 4096 | 0.457904 | 1.049477 | 1.390179 |
| 8 | 16384 | 0.386888 | 0.913233 | 1.260907 |
| 8 | 65536 | 0.312680 | 0.770525 | 1.101575 |
| 8 | 200000 | 0.257718 | 0.671686 | 1.008089 |
| 4 | 4096 | 0.369578 | 0.873084 | 1.190739 |
| 4 | 16384 | 0.339853 | 0.813679 | 1.158396 |
| 4 | 65536 | 0.242220 | 0.591785 | 0.881509 |
| 4 | 200000 | 0.174689 | 0.512675 | 0.864359 |

**NUMERICAL (mask quadrature; not exact certificates).** Two masks were tested on 16X and 32X full-circle grids, rounded up to a power of two:

1. `H=1/(1+|F_expected|)`, where F_expected uses the deterministic Bohr-union thinning probabilities;
2. the adaptive positive clip `H=min(1,sqrt(n)/f)` where f>sqrt(n), and H=1 elsewhere.

On k=8 Bohr samples, the finer-grid first mask gives V/n=0.02791,0.01471,0.00997,0.00771 and TD4-implied M/sqrt(n) bounds 0.17363,0.12960,0.10427,0.08623. It visibly loses variance; the expected sharp-union signal has growing negative/oscillatory content, so blindly taking its absolute value is not the positive-mixture mask of TD6.

The adaptive clip gives V/n=0.39054,0.38181,0.35616,0.33250 and TD4-implied bounds 0.71670,0.69423,0.65556,0.63827. Doubling the grid changes those normalized bounds by at most 0.000005. This supports a clipping criterion on these finite examples, not a proof independent of J. On the finite Fejer samples the expected-signal reciprocal retains V/n about 0.174..0.177 and bounds 0.43537,0.41748,0.42500,0.42166. Neither grid agreement nor the exact positivity of the mask certifies the numerical integrals. TD6 is the independent proof for the positive-mixture family.

**PROVED / failed extension.** Applying TD6's argument to `1/(1+|F_expected|)` for sharp Bohr unions would require a bound on the mean absolute expected signal and a corresponding lower bound on its weighted noise Gram matrix. No uniform bound of that kind was proved here; the finite variance loss is a warning against assuming it. Likewise, the rational order-7 successes do not establish a uniform order-7 theorem. TD8 explains why generic spike-plus-bulk intuition alone cannot establish one.

## Benchmark falsification, local tests, and provenance

**PROVED (finite certificates) / NUMERICAL (minima).** `benchmarks_summary.json` contains all 21 round-1 benchmark sets, plus [1,512] and the union 2[1,512] union 3[1,512]. Thus it includes the cumulative quadratic, quartic, two-level and power-law profiles and their random roundings, both N50 certified dense examples, smallN n=4,10,20,30,50, and Singer/Bu q=61. Full-q exact cubic audits and exact order-3/5/7 rational witnesses were computed for every set. All 23 satisfy the finite LM criterion V>=n/10, W<=2V^(3/2) at a selected q. This is a falsification test, not a universal theorem.

For Singer/Bu q=61, the exact minimizing filter is q=1902, with n=3782, V=9833/8, W=981465/16 and W/V^(3/2)=1.423511; the order-7 bound is 0.364419sqrt(n), against numerical M/sqrt(n)=0.604020. The N50_x72 example has q=21 and order-7 bound 0.441436sqrt(n), against numerical 0.570060. No benchmark falsified the exact certificate identities.

**NUMERICAL (local-discrepancy probes).** For the block construction with B=4096 and X=65536,262144,1048576, prefix discrepancies are about 488.325,506.041,510.348, all below the proved B+1 bound. For q=2, the best TD-window has w=1, with m^2 about 0.02317,0.02320,0.01357; the ratios m^2/X decrease to 1.29e-8. Filters q=4,8,16 do yield positive proportional-window energy on these samples; this is why TD7-O is stated only for the fixed minimal denominator. The proof uses B=65536 for ample margin in the coarse boundary estimates; the script accepts B as an explicit parameter.

For the proof's B=65536, the additional X=1048576 and 4194304 tests give prefix discrepancies 7815.087 and 8099.582, below 65537. Again q=2 chooses w=1, with m^2 about 0.02302 and m^2/X about 2.20e-8 and 5.49e-9. These finite tests agree with the asymptotic paper obstruction and are not its proof.

**PROVED (verification record).** `proof_checks.json` records 210 independently re-evaluated rational moment witnesses; the all-coefficient integer rechecks above; the exact t=1024 endpoint inequality in TD5; and the rational TD8 Schur thresholds 80/27, 69125/4488, 792130993/2241000. Software: Python 3.12.3, python-flint 0.9.0, NumPy 2.5.4, SciPy 1.18.1. No LP or MILP is used, so no alternative solver to Gurobi was introduced.

`final_checks.json` additionally verifies the stated eta=1/10, B=2 moment criterion on all 23 benchmarks using Fraction, and exhaustively verifies the new front-energy inequality with even extension on all binary sets with ambient X<=10, q<=min(3,X), 1<=r<=q and every eligible w: 94242 checks, no failures.

All code and results are under `.research/agents/tdense2_scratch/`:

* `audit.py`: exact CRT counts, exact minimizing-q comparisons, family/benchmark generation, integer moments through order 7, rational witnesses, direct small-set self-test.
* `extra.py`: less-diluted Bohr samples, two-grid numerical masks, rearranged bounded-discrepancy profiles.
* `proof_checks.py`: independent integer convolution and rational witness verification.
* `final_checks.py`: exact benchmark criterion and exhaustive local front-variation audit.
* `family_summary.json`, `bohr4_summary.json`, `benchmarks_summary.json`: compact complete finite results.
* `bohr_X*.json`, `bohr4_X*.json`, `fejer_X*.json`: parameters, explicit A, exact V/W and higher moments and witnesses, numerical minima.
* `*_counts.npz`: exact nonnegative-offset c and r arrays; `masks.json`, `local*.json`, `proof_checks.json`: ancillary output.

Reproduction commands (all computation is remote, maximum two cores):

```sh
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 180 python .research/agents/tdense2_scratch/audit.py --mode selftest
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -m 8 -t 900 python .research/agents/tdense2_scratch/audit.py --mode family --moments
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -m 8 -t 900 python .research/agents/tdense2_scratch/audit.py --mode benchmarks --moments
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -m 8 -t 900 python .research/agents/tdense2_scratch/extra.py bohr4
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -m 8 -t 600 python .research/agents/tdense2_scratch/extra.py masks
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -m 4 -t 300 python .research/agents/tdense2_scratch/extra.py local
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -m 4 -t 300 python .research/agents/tdense2_scratch/extra.py local 65536 1048576 4194304
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -m 8 -t 300 python .research/agents/tdense2_scratch/proof_checks.py
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -m 4 -t 180 python .research/agents/tdense2_scratch/final_checks.py
```

**Quoted literature, checked for exact scope.** [Bu et al., arXiv:2610.17160v1, Proposition 9.7](https://arxiv.org/html/2610.17160v1#S9.SS2) gives an n^(1/4) lower bound for each fixed density constant C. It does not supply the square-root target. Its proposition was inspected directly; the research results above do not assume an unverified stronger literature theorem.

## Final strategic decision and remaining gaps

**PROVED / new versus quoted.** New work here consists of the centering correction, TD5's effective LM counterexample, TD6's J-independent mask argument for its random positive-mixture family, TD7 and TD7-O, TD8's specified abstract moment obstruction, the precise MS reduction, and the exact finite audits and witnesses. P38/TD-window, TD4's moment inequality, P40, and the literature n^(1/4) theorem are quoted inputs; the generic moment-positivity principle is standard.

**CONJECTURED / remaining exact gap.** The general dense theorem requires a deterministic variance-preserving selection argument such as MS, or a different certificate. The original sharp Bohr-union infinite asymptotic statement and a uniform order-7 theorem for filtered cosine sums have not been proved. The numerical minimum search has not been turned into a certified global minimum for the new large sets.

**HEURISTIC / next discriminating experiment.** Use the exact order-7 dual vectors and the successful clip to design a low-mass positive bump mask, then optimize its retained coefficient energy on the sharp Bohr inputs while increasing J at fixed density. The useful question is whether its mass/variance cost stays bounded; additional large searches for a single q cannot repair the refuted LM statement. For the discrepancy branch, test averaged overshoot rather than prefix mass discrepancy alone.

This round's deliverable is a rigorous certificate obstruction, a rigorous repair on its positive-mixture model, a local-discrepancy extension with an explicit limitation, and a precise reduction of the unsolved dense theorem.

All remote jobs launched for this round have completed. No continued unattended computation is claimed.
