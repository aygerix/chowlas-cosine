# T-dense research report

Updated: 2026-10-19. Scope: the user's tdense brief. No commits, subagents, or local mathematical computation. All scratch programs/data are confined to `.research/agents/tdense_scratch/`; all computation must run through `src/dirun.sh -c 2` or less. No root `.research/*.md` files are edited.

## Exact target and inherited facts

**CONJECTURED (target T-dense).** For every real C >= 1 there exists c(C)>0 such that every finite nonempty A subset of the positive integers, with n=|A| and max A <= Cn, satisfies M(A)=-min_x sum_{a in A}cos(ax) >= c(C)sqrt(n).

**PROVED / inherited, not new here.** P31/P31-E and P34 are recorded as kernel-checked in the project: density >=0.41 gives sqrt(n)/1000, and coefficient-energy windows handle non-front-loaded profiles. P33, the dilation pinch, and P36 are tools. Root notes explicitly rule out repeating averaged second-moment profile arguments as a solution of the remaining front-loaded class. No new Lean claim is made in this report.

Sources read: CLAUDE.md; tdense_brief.md; PROOFS P31/P31-C/P33/P34/P36/P37; NOTEBOOK entries on P31 exhaustion, nonlinear requirement, localized criticality, weighted windows, and B-test; experiment drivers E59/E60/E63; number-theory-research skill and its three method/review references. Bu et al. v1, arXiv:2610.17160, opened for the exact boundary/dense-set statements; source verification continues below.

## Initial attacks and first falsification tests (historical)

1. **CONJECTURED route: smooth profile plus fluctuation.** Try to turn the full-support signed-coefficient P34 bound into a certificate for the unsmoothed 0/1 sum using a positive operator. Main obstruction to check: a high-pass operator is not positive, and a signed fluctuation's negative point may lie under a large positive smooth component. First derive the exact energy and pointwise transfer costs.
2. **CONJECTURED route: front loading and runs.** Check whether the implication "front-loaded at all proportional scales implies long consecutive runs" is actually valid. First test rational/Beatty rounding of a convex decreasing profile bounded strictly below 1. A failure here would prohibit an unqualified use of the suggested run dichotomy.
3. **CONJECTURED route: nonlinear local certificate.** Use exact 0/1 Fourier coefficients (equivalently f*f=f/2 under normalized circular convolution), or a localized third moment, to formulate a precise additive condition beyond profile constraints. Falsify on front-loaded random and Beatty rounding, two-level profiles, Bu/Singer examples, and the certified dense optima.

## Work status

Current checkpoint: TD1 and TD2 are complete paper proofs for cumulative profile rounding; TD3 is a complete paper obstruction to bounded-degree positive multipliers followed by Fejer-window P31. TD4 gives an exact reduction of T-dense to the single unproved LM-dense statement. Independent integer checks certify its concrete sufficient conditions on 21 benchmark sets; an exhaustive exact check passes all 262135 admissible sets with max A<=18 and max A<=10|A|. No full T-dense theorem, no extension to every set at any new C, and no new Lean verification are claimed. All calculations ran on the VM at -c 2; no jobs remain running. The final section gives the next falsification target and strategic decision.

## First derivations (2026-10-19, work in progress)

**PROVED (elementary, new here; details below will be expanded).** Put p_j=(1/2)(1-j/X)^2 for 1<=j<=X, S_j=sum_{i<=j}p_i, and a_j=floor(S_j)-floor(S_{j-1}). Then a_j is 0 or 1 and a_j+a_{j+1}<=1, since p_j+p_{j+1}<1. Thus A_X={j:a_j=1} has no consecutive elements. Also |A_X|=X/6+O(1), max A_X/X ->1, and at every fixed 0<theta<=1,

    sum_{j in A_X}(1-j/(theta X))_+^2 / |A_X|
      -> theta(1-theta/2+theta^2/10) >= theta/(1+theta).

The last inequality follows from (1+theta)(1-theta/2+theta^2/10)-1 = theta(5-4theta+theta^2)/10 >=0. Since every analytic Nikolskii constant has asymptotic coefficient at least 2/3 (constant-vector/Fejer example), this profile escapes the original P31 inequality at every fixed proportional window, including its optimal asymptotic constant. Consequently, front-loading alone does NOT imply long consecutive runs. This refutes a shortcut, not T-dense.

**PROVED (identity; new application to investigate).** Multiplication by H_q(x)=1-cos(qx)>=0 preserves the one-sided bound, at cost <=2. If a_j=1_A(|j|) for j!=0 and a_0=0, then

    T_q(x)=(1-cos(qx)) f_A(x)+a_q/2
           =sum_{j=1}^{X+q} b_{q,j}cos(jx),
    b_{q,j}=a_j-(a_{j-q}+a_{j+q})/2,
    T_q>=-2M+a_q/2.

Applying the generalized P31/P34 chain to b gives a genuinely nonlinear certificate because b_j^2 contains products of membership indicators at nearby frequencies. This differs from PD convolution/reweighting, which left only linear profile constraints. Next: VM falsification tests on all required example classes; derive a transparent sufficient condition in the b-energy profile and determine which smooth profiles still evade it.

**CONJECTURED route, historical and now parked.** For bounded-prefix-discrepancy rounding, beta_j=a_j-p_j has energy profile p_j(1-p_j)+O(1) after summation by parts. For the quadratic half-density profile this is sufficiently flat for P31, although the original p-profile is not. A bound on the prefix discrepancy can prevent a sqrt(X) negative fluctuation from lying inside the smooth central spike. The direct positive-operator proof TD1/TD2 below supersedes this route; no additional theorem is being claimed from this fragment.

## VM test completed: nonlinear multiplier works on the no-run family

**NUMERICAL (not a global-minimum certificate).** Ran `src/dirun.sh -c 2 -t 240 python .research/agents/tdense_scratch/probe.py`. Seed 20261019. Code: `tdense_scratch/probe.py`; full generated sets, parameters, coefficients' energy summaries, minima, and diagnostics: `tdense_scratch/probe.json`. Checked power-law profiles alpha=0.5,0.75 (random and cumulative rounding), quadratic and quartic profiles, two-level profiles, two certified N=50 examples, smallN entries N=4,10,20,30,50, and a Singer/Bu q=61 example. All tested multiplier identities matched direct evaluation to the programmed tolerance. Minima use FFT+Newton and direct cosine evaluation, and remain uncertified.

On exact cumulative quadratic rounding:

| Ambient X | n | max A | longest run | observed M/sqrt(n) | original P31 M bound | q=2 transformed M bound |
|---:|---:|---:|---:|---:|---:|---:|
|384|63|297|1|1.63295|0.6750|1.2728|
|1536|255|1316|1|2.25060|0.6166|2.3778|
|6144|1023|5590|1|2.50851|0.5788|4.5607|

The floating bounds in the last columns are diagnostics until checked in exact rational arithmetic. The unfiltered bound stays O(1), while q=2 produces sqrt(n) growth. The same q=2 effect occurs on cumulative quartic and power-law rounding. The q=1 filter does not improve asymptotically on this family, because the local alternating pattern is killed by q=2 specifically.

**PROVED (paper; full proof and exact audits below).** There is a direct all-X sqrt(n) proof for this quadratic family with constant 1/1000, using the q=2 positive multiplier and exact run-defect counts. It avoids the delicate transfer from a signed fluctuation's minimizer to f_A. The general mechanism extends to cumulative rounding of fixed decreasing profiles with rational starting density satisfying TD1.a/TD1.b: a matching denominator filter kills the locally periodic front.

**Strategic review.** The run shortcut is false; discard it. Retain the nonlinear positive-multiplier certificate. The signed-fluctuation route is a valid possible route for bounded discrepancy, but costs much worse constants and misses an available positive operator, so stop optimizing it. The all-C target still needs a mechanism for arbitrary rounding patterns; no result for every A at C>2.466 is claimed.

## Main result TD1: positive denominator filters prove Chowla for cumulative profile rounding

**PROVED (complete paper proof below; not kernel-checked; priority not audited).** This is a restricted-family theorem, NOT T-dense for all sets.

Let integers q>=1 and 1<=r<=q be fixed. Let p:[0,1]->[0,r/q] be nonincreasing, with p(0)=r/q. Assume there is a finite real L>=0 such that

    0 <= r/q-p(t) <= L t   for every t in [0,1].                       (TD1.a)

Assume also there is t0<1 such that p(t)<=1/(q+1) on [t0,1] and

    mu := integral_{t0}^1 p(t)dt > 0.                                (TD1.b)

For any integer X>=1 and any phase sigma in [0,1), define

    U_j=floor(sigma+sum_{i=1}^j p(i/X)),  U_0=0,
    a_j=U_j-U_{j-1},   A={j in [1,X]:a_j=1},   n=|A|.

Then there exists an explicit c(p,q)>0, independent of X and sigma, such that whenever n>=1,

    M(A) >= c(p,q) sqrt(n).

One valid choice is

    theta=min(1/4, mu/[100q(L+1)]),
    X0=ceil(max(100, 2q/theta, 2(q+3)/mu, 72q/(theta mu))),
    c(p,q)=min(1/(2sqrt(X0)), sqrt(theta mu/192)).                     (TD1.c)

The hypothesis includes fixed polynomial profiles p(t)=(r/q)(1-t)^k for every fixed integer k>=1. It also includes capped power-law and two-level profiles when their starting density is rational, their departure from that starting density obeys (TD1.a), and their terminal density meets (TD1.b). It does not include arbitrary independent rounding.

### TD1 proof, including the nonlinear certificate used

1. **General coefficient-energy window inequality (PROVED, same chain as P31).** If

       T(x)=sum_{j=1}^D b_j cos(jx) >= -m,
       E=sum b_j^2,  S=sum_{j<=w} b_j^2(1-j/(w+1))^2,
       W=2(w+1)/3+1/[3(w+1)],
       C=(811/1000)(D+w+1)+71/300,

   then

       W(m^2+E/2) <= C(m^2+S/2).

   Proof: multiply T+m by a shifted Fejer kernel of degree w, apply Fejer-Riesz and P31-E, and average the squared L2/L1 inequality over the shift. Parseval gives E and S exactly. No amplitude bound on b is used. Thus, when C>W,

       m^2 >= (WE-CS)/[2(C-W)].                                      (TD-window)

   P31-E is the inherited kernel-checked input; its application here is a paper argument.

2. **Positive operator (PROVED identity for every A).** Extend a_j evenly to integers, with a_0=0 and a_j=0 for |j|>X. Put

       b_j=a_j-(a_{j-q}+a_{j+q})/2   (1<=j<=X+q),
       T=(1-cos(qx))f_A+a_q/2=sum b_j cos(jx).

   Hence T>=-2M+a_q/2. In TD-window use D=X+q and m=2M-a_q/2. Since M>=1/2 (proved in step 6), m>=0 and m<=2M. The energies b_j^2 contain pair products of membership indicators, so this is nonlinear in A.

3. **Energy in the tail.** For j>=m0:=ceil(t0 X)+q, any q+1 consecutive indices in [j-q,j+q] have total p-mass <=1. Cumulative rounding therefore puts at most one selected index in each such block. In particular, if a_j=1 then a_{j-q}=a_{j+q}=0 and b_j=1. The number of such j is at least

       sum_{j=m0}^X p(j/X)-1 >= mu X-q-3.

   Here monotonicity bounds the Riemann-sum error, moving the cutoff by at most q+1 loses at most q+1 mass, and the floor difference loses less than 1. Thus

       E >= mu X-q-3 >= mu X/2                                     (TD-tail)

   for X>=2(q+3)/mu.

4. **Small energy in the front: the actual arithmetic ingredient.** For 0<=j<=w set

       d_j=U_{j+q}-U_j,   z_j=r-d_j.

   Since any q consecutive p-values have total <=r, d_j<=r and z_j>=0. For j>=1,

       a_{j+q}-a_j=d_j-d_{j-1},
       (a_{j+q}-a_j)^2=|d_j-d_{j-1}|<=z_j+z_{j-1}.

   Let B_j=U_j-sigma-sum_{i<=j}p(i/X), so -1<B_j<=0. Summing d_j and telescoping B_{j+q}-B_j leaves two boundary blocks of length q, whose difference has absolute value <=q. By (TD1.a),

       sum_{j=0}^w z_j <= qL(w+1)(w+q)/X+q.

   For j>q, Jensen gives b_j^2 <= ((a_j-a_{j-q})^2+(a_j-a_{j+q})^2)/2. Sum this inequality; the j<=q boundary contributes at most q. Consequently, provided w+q<=X,

       S <= sum_{j<=w}b_j^2 <= 3q+2qL(w+1)(w+q)/X.                 (TD-front)

   This count is where cumulative rounding is used. Front-loading alone does not give it.

5. **Choose a proportional window.** Let w=floor(theta X). For X>=X0, w+q<=X, C<=2X, C>W, W>=2theta X/3, and (TD-front) gives

       S <= 3q+8qL theta^2 X.

   Combining with (TD-tail),

       WE-CS >= theta mu X^2/3-16qL theta^2 X^2-6qX
              >= theta mu X^2/6-6qX
              >= theta mu X^2/12.

   The middle inequality follows from theta<=mu/[100q(L+1)]; the last uses X>=72q/(theta mu). TD-window and 2(C-W)<=4X imply

       4M^2 >= m^2 >= theta mu X/48,
       M >= sqrt(theta mu/192) sqrt(X) >= sqrt(theta mu/192) sqrt(n).

6. **Small X.** For any nonempty A and a in A, G=f_A+M>=0 has mean M and Fourier coefficient 1/2 at a. Thus 1/2=|integral G exp(-iax)|<=integral G=M. If X<X0, M>=1/2>=sqrt(n)/(2sqrt(X0)). This proves (TD1.c), with every X, phase and nonempty A accounted for. QED.

### TD2: explicit quadratic instance and the no-run obstruction

**PROVED (paper, new here; not kernel-checked).** For every integer X>=8 put

    p_j=(1/2)(1-j/X)^2,
    a_j=floor(sum_{i<=j}p_i)-floor(sum_{i<j}p_i),
    A_X={j:a_j=1}, n_X=|A_X|.

Then

    M(A_X) >= sqrt(n_X)/1000.                                      (TD2)

Every A_X has no consecutive elements, n_X=X/6+O(1), and max A_X/X->1. Thus its asymptotic hull ratio is 6, well beyond the inherited density threshold, although TD2 addresses this particular family only.

**Explicit proof with better constants than the generic TD1 formula.** For X>=100 choose q=2, w=floor(X/100). Here a_1=a_2=0 and a_j+a_{j+1}<=1, since p_j+p_{j+1}<1. Use the b_j from step 2, so T=(1-cos(2x))f_A>=-2M.

- For j>=ceil(X/4)+2, any three adjacent p-values are <=3*(9/32)<1 in total. Thus if a_j=1 then a_{j-2}=a_{j+2}=0, so b_j=1. The count of these tail elements is at least 9X/128-5/2, hence

      E>=X/16-3.

- Put d_k=a_k-a_{k+2}. Jensen and evenness at the origin give sum_{j<=w}b_j^2<=sum_{k=0}^w d_k^2. For a binary sequence without adjacent 1s,

      d_k^2 <= (1-a_k)(1-a_{k+1})+(1-a_{k+1})(1-a_{k+2}).

  Therefore

      S <= 2 sum_{k=0}^{w+1}(1-a_k-a_{k+1})
        <= 2(w+2-2 sum_{j=1}^{w+1}a_j)
        <= 6+2(w+1)(w+2)/X
        <= 7+X/5000.

  In the penultimate step use sum_{j<=y}a_j>=sum_{j<=y}p_j-1 and sum_{j<=y}p_j>=y/2-y(y+1)/(2X).

- D=X+2. For X>=100, C=(811/1000)(X+w+3)+71/300<=7X/8 and W>=X/150. Once X>=100000 the quantities being bounded below are positive, so

      WE-CS >= (29/120000)X^2-(1229/200)X,
      (2M)^2 >= (29/210000)X-1229/350 >= X/10000.

  The last inequality already holds at X>=92175. Thus M>=sqrt(X)/200 for X>=100000.

- For X<100000, M>=1/2>=sqrt(n_X)/1000 because n_X<=X<100000<250000. This proves TD2 for all X>=8.

**Exact verification status.** Ran `src/dirun.sh -c 2 -t 150 python .research/agents/tdense_scratch/verify_exact.py`. All integer/rational checks passed, including the E/S bounds and all constant manipulations at X=100,384,1536,6144,20000,100000,150000; phase checks at X=6144 for sigma=1/10,3/10,7/10,9/10 also passed the stated auxiliary bounds. Output: `tdense_scratch/verify_exact.json`. These are finite audits of the proof, not replacements for the all-X argument. The proof is not Lean-checked.

**Why these are genuinely escaping profiles.** For every fixed theta>0, bounded prefix discrepancy gives a Riemann-sum limit

    S_A(theta X)/n_X -> 6 integral_0^{min(theta,1)} (1/2)(1-t)^2(1-t/theta)^2 dt.

For 0<theta<=1 this is theta(1-theta/2+theta^2/10), at least theta/(1+theta), with strict inequality. For theta>=1 it is 1-1/(2theta)+1/(10theta^2), again greater than theta/(1+theta): the difference has numerator 5theta^2-4theta+1 over 10theta^2(1+theta). Since the asymptotic Nikolskii coefficient is at least 2/3, every proportional-scale original P31 numerator is nonpositive. Subproportional w can give at most o(n) in M^2. TD2 succeeds because b_{2,j} sees the periodic rounding pattern, whereas the original coefficient profile does not.

**Failure precisely identified.** The statement "front-loaded at all proportional scales implies long consecutive runs" is false. Here there are no adjacent members at all. A possible corrected run argument must allow arithmetic runs with a matching denominator, or must use information beyond the unweighted density profile.

## TD3: a rigorous obstruction to every bounded-degree positive multiplier followed by Fejer-window P31

**PROVED (paper, with exact polynomial certificate; not kernel-checked).** The denominator filter in TD1 cannot be extended to arbitrary dense sets merely by allowing a fixed finite list of shifts, or even all nonnegative multipliers of any fixed degree.

There exist sets A_X subset [1,X] with |A_X|=ceil(X/10), such that, for every fixed integer d and every nonzero nonnegative real trigonometric polynomial H of degree <=d, applying the coefficient-energy Fejer-window inequality (TD-window) to

    T=H f_{A_X}-mean(H f_{A_X})

cannot produce a lower bound M(A_X)>=c sqrt(|A_X|) with c>0 independent of X. More precisely, the largest positive lower bound on the transformed offset squared furnished by that inequality is o(X), uniformly over H normalized by ||H||_infinity=1 and over the window degree w. The statement concerns this certificate family only; it says nothing adverse about the actual M(A_X).

### Construction and coefficient-energy limit

Start with independent Bernoulli membership of probabilities

    p(j/X)=(1/2)(1-j/X)^4.

The cardinality is X/10+o(X). Add or remove o(X) indices to arrange exactly ceil(X/10) members. This correction preserves every fixed-lag limiting correlation and all proportional weighted energies below. In particular A_X subset [1,10|A_X|], so these are genuinely dense sets.

Write H=sum_{k=-d}^d h_k exp(ikx), h_{-k}=conj(h_k), and let

    u=|H(0)|^2>=0, v=sum |h_k|^2>0.

Away from O(d) boundary indices, the complex cosine coefficient of Hf is b_j=sum_k h_k a_{j-k}. Independence gives the limiting energy density

    e_H(t)=u p(t)^2+v p(t)(1-p(t)).                                  (TD3.e)

Consequently, for every fixed theta>0,

    E/X -> E_e:=integral_0^1 e_H(t)dt,
    S/X -> S_e(theta):=integral_0^{min(theta,1)} e_H(t)(1-t/theta)^2dt.

These limits are available simultaneously for all fixed degree bounds: bounded-difference concentration gives exponentially small failure probabilities for every fixed-lag weighted correlation, then Borel-Cantelli and a countable dense family of cutoff functions give the assertion. For a fixed d there are only finitely many correlation terms in the quadratic form in h, so convergence is uniform in the normalized coefficients. The o(X) cardinality correction changes E and S by o(X), since each changed bit affects at most O(d) bounded coefficients.

### Exact profile inequality killing the certificate

For each of e_v=p(1-p) and e_s=p^2,

    S_e(theta) > [theta/(1+theta)] E_e   for every theta>0.             (TD3.profile)

For 0<theta<=1 put D_e(theta)=(1+theta)S_e(theta)/theta-E_e. In the degree-9 Bernstein basis binom(9,i)theta^i(1-theta)^(9-i), the coefficients of D_{e_v} are exactly

    1/90, 11/540, 7/270, 1/35, 389/13230,
    103/3528, 43/1512, 311/11340, 547/20790, 349/13860.

They are all strictly positive. For e_s the coefficients are

    1/18, 5/108, 7/180, 1/30, 11/378,
    13/504, 5/216, 17/810, 19/990, 7/396.

Again they are all strictly positive. These are exact rational polynomial identities, reproducible without third-party algebra software by `tdense_scratch/barrier.py`; its full coefficients are saved in `tdense_scratch/barrier.json`.

For theta>=1, write m_i=integral t^i e(t)dt/E_e. Then S_e/E_e=1-2m_1/theta+m_2/theta^2. Direct integration gives

    e_v: E_e=13/180, m_1=5/26, m_2=59/1001;
    e_s: E_e=1/36,   m_1=1/10, m_2=1/55.

Both have m_1<1/4 and m_2>0. Since theta^2/(1+theta)>=theta/2 when theta>=1,

    theta^2/(1+theta)-2m_1 theta+m_2>0,

which is precisely (TD3.profile) after multiplying by theta^2. Nonnegative linear combinations prove the same inequality for e_H.

### Why this is a P31 obstruction, including small and large windows

The Fejer example forces every valid analytic Nikolskii constant to satisfy C_L>=(2/3)(L+1). For a proportional window w~theta X, the leading TD-window numerator is therefore at most

    (2/3)X^2[theta E_e-(1+theta)S_e(theta)]<0.

For w=o(X), dropping the negative CS term already bounds the claimed offset squared by O(w+1)=o(X). For w/X->infinity, insert S/E=1-2m_1 X/w+O((X/w)^2); even at the optimistic constant 2/3 the leading numerator is a negative multiple of X E because 2m_1<1. Thus no scale escapes. Uniformity for degree <=d follows from compactness after ||H||_infinity=1, the finite-dimensional correlation convergence, and v>=1/(2d+1). The mean subtracted from Hf is O_d(1), so it cannot change an o(sqrt(X)) conclusion into a sqrt(X) conclusion. QED.

**What is excluded.** Any fixed finite menu q<=Q of H_q=1-cos(qx); any bounded-degree nonnegative multiplier, including adaptive coefficients; followed by the specific Fejer-window P31/TD-window certificate. This includes optimal Nikolskii constants, not merely 0.811.

**What is not excluded.** Degree growing with X; different window shapes without a separate argument; higher additive moments; nonlinear operators other than multiplication; arithmetic information not represented by these quadratic energies; the actual T-dense conjecture. In particular TD3 is not a counterexample to Chowla.

**Computation log.** The first attempt at the polynomial audit failed because sympy is absent on the VM. Replaced it with a standard-library Fraction implementation; reran via `src/dirun.sh -c 2 -t 100 python .research/agents/tdense_scratch/barrier.py`. All rational Bernstein and moment checks passed. No packages were installed and no local computations were performed.

## TD4: a precise single missing lemma using localized third moments

**PROVED (algebraic reduction; the underlying third-moment inequality is classical).** This formulation goes beyond TD3's quadratic-energy obstruction.

For any nonempty A, integer q>=1, and the same T_q=(1-cos(qx))f_A+a_q/2, define normalized circular moments

    V_q=integral T_q^2=(1/2)sum_j b_{q,j}^2,
    W_q=integral T_q^3,
    m_q=2M-a_q/2.

All integrals here use dx/(2pi). Then

    V_q^2 <= m_q^2 V_q+m_q W_q.                                    (TD4.moment)

Proof: T_q+m_q>=0, mean T_q=0, so Cauchy-Schwarz gives

    (V_q+m_q^2)^2
       <= mean(T_q+m_q) mean((T_q+m_q)^3)
       =m_q(W_q+3m_q V_q+m_q^3).

Cancel the equal terms to obtain (TD4.moment). In particular if V_q>=eta n and W_q<=B V_q^(3/2), with eta>0 and B>=0, then

    M >= (sqrt(eta)/4)(sqrt(B^2+4)-B) sqrt(n).                       (TD4.bound)

### Exact integer form of the third moment

Let S=A union (-A), and c(k)=#{(s1,s2,s3) in S^3:s1+s2+s3=k}. Then

    Delta_q=10c(0)-15c(q)+6c(2q)-c(3q),
    W_q=Delta_q/32+(3a_q/2)V_q+a_q/8.                              (TD4.triples)

Derivation: (1-cos y)^3=5/2-(15/4)cos y+(3/2)cos(2y)-(1/4)cos(3y), and integral cos(kx)f_A(x)^3=c(k)/8 by symmetry. Thus integral ((1-cos(qx))f_A)^3=Delta_q/32. Centering by a_q/2 and using mean((1-cos(qx))f_A)=-a_q/2 adds (3a_q/2)V_q+a_q/8.

This is a sixth finite difference of the signed triple-convolution count near zero, with exact centering terms. Controlling this finite difference at a shift having substantial filtered variance is the specific missing additive mechanism.

### The one missing lemma

**CONJECTURED (LM-dense; unproved).** For every real C>=1 there are eta(C)>0 and finite B(C)>=0 such that for every finite nonempty A subset [1,Cn], n=|A|, X=max A, some integer 1<=q<=X satisfies

    V_q>=eta(C)n,   W_q<=B(C)V_q^(3/2).                             (LM-dense)

**PROVED implication.** LM-dense implies T-dense with c(C)=(sqrt(eta(C))/4)(sqrt(B(C)^2+4)-B(C)). There is no additional analytic or certification gap in this implication: it follows from TD4.moment for every real angle.

This is a sufficient structural lemma, not an asserted equivalence to T-dense. Its independent content is the simultaneous choice of q with large variance and controlled third moment. A bound for every fixed q is not expected: long intervals have V_q=O(q), so q must be allowed to grow with the set. TD3 does not obstruct LM-dense, since W_q contains triple correlations and not just the energy profile.

### Evidence and exact finite certificates

**NUMERICAL.** `tdense_scratch/third_moment.py` evaluates moments by FFT quadrature with sample size exceeding the cubic degree; floating calculations remain uncertified. Best lower-bound ratios from TD4.bound with actual V,W were approximately:

| Example | n | chosen q | derived M/sqrt(n) lower bound (floating) |
|---|---:|---:|---:|
|Quadratic cumulative, ambient X=6144|1023|1|0.45085|
|Quadratic independent rounding|261|8|0.44614|
|Quartic cumulative rounding|153|1|0.41388|
|Quartic independent rounding|152|8|0.45406|
|Two-level independent rounding|196|4|0.39619|
|Power-law alpha=0.5 cumulative|251|2|0.45648|
|Certified N50_x72 input|50|1|0.23363|
|Singer/Bu q=61 input|3782|3|0.14087|

These are lower bounds derived from moment values, not estimates of the actual minimum. Their decimal values are not themselves certified by the floating run.

**PROVED finite checks (exact arithmetic, independent evaluator).** `tdense_scratch/third_moment_exact.py` computes the integer convolution c(k) with python-flint modulo 998244353. There is no modular ambiguity: c(k)<=(2n)^2<998244353 for every input. The exact V_q and TD4.triples then reproduce the floating values and test the rational inequalities

    V_q>=n/10 and [W_q<=0 or W_q^2<=4V_q^3].

Every one of the 21 test sets has q in {1,2,3,4,8,16} satisfying these conditions. Hence, on these exact inputs, paper proof plus integer arithmetic certifies the global lower bound

    M(A) >= [(sqrt(2)-1)/(2sqrt(10))]sqrt(n).

Full integer counts, rational moments, and selected q are in `tdense_scratch/third_moment_exact.json`. This is a finite certification statement, not a proof of LM-dense. Runs used `src/dirun.sh -c 2 -t 100 python .../third_moment.py` and `src/dirun.sh -c 2 -t 150 python .../third_moment_exact.py`.

**NUMERICAL negative test of a different extension.** `tdense_scratch/growing_shift.py` scans q/X in [1e-5,2] and window ratios up to 10 using the continuum energy for independent rounding:

    e_s(t)=[p(t)-(p(|t-s|)+p(t+s))/2]^2
             +p(t)(1-p(t))
             +[p(|t-s|)(1-p(|t-s|))+p(t+s)(1-p(t+s))]/4,

where p is extended evenly and set to zero outside [-1,1]. On 49,500 sampled shift/window pairs per profile, the quartic and eighth-power profiles gave no positive proportional P31 certificate; the quadratic did. This is only sampled evidence, with output in `growing_shift.json`, but it argues against spending the next effort merely enlarging q in the quadratic-energy certificate. The third-moment criterion succeeds on the finite quartic independent-rounding test instead.

### Exhaustive falsification of concrete LM constants

**PROVED finite verification (exact integer arithmetic).** Ran

    src/dirun.sh -c 2 -t 150 bash -c 'g++ -O3 -std=c++17 .research/agents/tdense_scratch/moment_exhaust.cpp -o .research/agents/tdense_scratch/moment_exhaust_vm && .research/agents/tdense_scratch/moment_exhaust_vm 18 | tee .research/agents/tdense_scratch/moment_exhaust.jsonl'

All 262135 sets satisfying max A<=18 and max A<=10|A| passed: each has some 1<=q<=max A with V_q>=n/10 and W_q<=2V_q^(3/2). The program enumerates each set once at X=max A (the top bit is forced), uses direct integer pair/triple convolutions, and tests the equivalent integer criteria

    E8=sum_j(2a_j-a_{j-q}-a_{j+q})^2,
    W32=Delta_q+6a_q E8+4a_q,
    10E8>=8n and [W32<=0 or W32^2<=8E8^3].

Here V=E8/8 and W=W32/32. At X<=18, signed 64-bit integers easily contain every product. Runtime reported by the VM program: 0.694067 seconds (excluding compile/transport). The full log is `tdense_scratch/moment_exhaust.jsonl`. No inference about unbounded X follows from this finite success.

## Source verification and new-versus-inherited boundary

**CITED-VERIFIED.** Bu et al., arXiv:2610.17160v1 (12 Oct 2026), https://arxiv.org/html/2610.17160v1#S9: Proposition 9.1 gives |B_t|<=2*10^5 K^3||F||_1; Proposition 9.7 yields M^3||f_A||_1>=(n-1)/(32C*2*10^5), hence M>=((n-1)/(64C*2*10^5))^(1/4). Remark 9.8(iii) expressly leaves the square-root order for dense sets undecided. These are the quoted literature facts, not this report's results.

**PROVED / inherited.** The analytic Nikolskii input and the original P31/P34 window mechanism are inherited. The third-moment Cauchy-Schwarz inequality is classical. The identity f*f=f/2 is also elementary and was not pursued as a new result.

**PROVED / derived here, priority unchecked.** TD1's denominator-filter argument with exact local deficit counts; TD2's explicit no-consecutive-members front-loaded family and its sqrt(n)/1000 bound; TD3's bounded-degree positive-multiplier obstruction with exact profile certificates; TD4's particular sixth-difference/centering formula and precise LM-dense reduction. The exact finite checks and their reproducible code are new work in this report. No claim of a first-in-literature theorem is made.

## Final strategic review and operational handoff

**PROVED state of the target.** T-dense for arbitrary dense A remains unproved here. The report does not improve the inherited universal hull threshold C<2.466; TD1/TD2 handle substantial specified families at larger hull ratios. TD3 explains why their positive-multiplier proof cannot simply be extended to arbitrary rounding by a bounded-degree quadratic-energy argument.

**Decision: continue the localized third-moment line; stop bounded-degree quadratic-filter optimization as a route to all C.** The latter has an explicit counterfamily. The former survives exact finite falsification and has a complete analytic implication to T-dense. This is evidence for the next test, not evidence of a proof.

Three distinct active mathematical lines for continuation:

1. **CONJECTURED, additive lower-bound line.** Prove LM-dense or a weaker density-dependent version. The missing step is simultaneous control of V_q and the sixth triple-count difference Delta_q, not another positivity/Nikolskii constant.
2. **HEURISTIC, constructive/adversarial line.** Seek front-loaded dense sets for which every q with V_q>=eta n has W_q/V_q^(3/2) large. Such a family would refute proposed uniform LM constants, and potentially reveal a different construction mechanism. Preserve the actual minima separately; failure of LM need not imply a small M.
3. **PROVED seed / CONJECTURED extension, arithmetic-rounding line.** Extend TD1 beyond exact cumulative rounding to bounded local defects in the matching rational-period pattern. The tail-energy/front-defect inequalities isolate exactly what must be retained; a bare front-loaded density hypothesis is insufficient by TD2/TD3.

**First concrete next experiment.** Use exact moment evaluation to search front-loaded examples in boxes X=40,80,160 at densities 1/3,1/6,1/10, deliberately minimizing the best simultaneous moment certificate over every q<=X (rather than minimizing M alone). Start from TD3 quartic independent rounding, the exact cumulative families, two-level rounding, and the existing Bu/dense optima. Test eta=1/10,B=2 first; preserve the first counterexample and its full q-table if found. A local-search failure is not a theorem. If the criterion survives, derive a scale-selection lemma for Delta_q that explicitly excludes shifts with V_q=o(n).

All files written by this task are the report and `tdense_scratch/` contents. No root `.research/*.md` was edited by this task, no commit was made, no subagent was launched, and every computation was run through `src/dirun.sh -c 2`. No external messages were sent. All VM jobs have completed; continuation requires a later agent turn.
