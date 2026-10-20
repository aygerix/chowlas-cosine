# Boolean plateaus separate uniform interpolation from adaptive certificates

2026-10-20. ATTACK LOG / DESIGN / CHAIN(c). Status: paper proof using the classical discrepancy theorem stated below, exact finite algebraic checks, and separate finite Arb upper certificates. No novelty, independent-agent audit, kernel verification, universal Chowla proof, or counterexample to Chowla is claimed.

## Result and implication for the programme

Write f_A(x)=sum_{a in A} cos(ax), M(A)=-min f_A, S=±A, N=2|A|, D_A=2f_A. Let J_≥(S) be the minimum L4 norm of a real mean-zero q with qhat(s)>=1 on S.

**Theorem.** There are genuine Boolean integer sets A_t, with L=t^6 and t tending to infinity, such that

    A_t subset [1,L-2],    [1,t^5] subset A_t,
    |A_t| = (5/12+o(1))L,
    c sqrt(|A_t|) <= M(A_t) <= 70 sqrt(|A_t|),
    liminf J_≥(±A_t) / [sqrt(2|A_t|) L^(1/8)] >= sqrt(6/5),

for one absolute c>0. The lower bound on M is obtained by an adaptive certificate whose selected-frequency coefficients are 1-p_a, including zero on the forced prefix. It does not require a coefficient of 1 at every selected frequency.

Consequently both proposed generic estimates are false:

    M(A)=O(sqrt(|A|))  =>  J_≥(±A)=O(sqrt(|A|)),
    J_≥(S)^4 <= C N K^2 for every Boolean A, K=2M(A),

where the first estimate is meant uniformly on each fixed bounded-ratio class. In fact the first fails on one absolute bounded-ratio class, and the ratio in the second tends to infinity along this family. This is stronger than the previous interval obstruction, since intervals have unbounded M/sqrt(n).

It does **not** refute bounded completion cost specifically on exact strict-record minimizers. No A_t is claimed to be such a minimizer. It does show that bounded ratio by itself cannot replace that missing extremality input. Full Chowla remains open.

## 1. An exact smooth autocorrelation profile

Extend v_j=j(L-j), j=0,...,L, by zero to Z. Set

    E=sum_j v_j^2=(L^5-L)/30,
    r_a=sum_j v_j v_{j+a}/E.

Then r_0=1, r_a=r_{-a}, 0<=r_a<=1, and r_a=0 for |a|>=L-1. If V(x)=sum_j v_j e^{ijx}, then

    F(x)=|V(x)|^2/E = 1+2sum_{a=1}^{L-2}r_a cos(ax) >= 0.

Thus the mean-zero cosine sum with coefficients r_a is bounded below by -1/2. Translation in l2 gives

    2E(1-r_a)=||v-T_a v||_2^2
       <= a^2 ||v-T_1 v||_2^2,
    ||v-T_1 v||_2^2=L(L^2-1)/3,
    1-r_a <= 5a^2/(L^2+1).

Also sum_j v_j=L(L^2-1)/6, so

    sum_{a=1}^{L-2}r_a
      = [(sum_j v_j)^2/E-1]/2
      = 5L(L^2-1)/[12(L^2+1)]-1/2.

All these quantities are rational; the profile uses no transcendental coefficients.

## 2. Force a long Boolean prefix without a linear sign cost

Put b=t^5=L^(5/6). For 1<=a<=L-2 define p_a=1 if a<=b, and p_a=r_a otherwise. Let

    Delta=sum_{a<=b}(1-r_a)
      <= 5b(b+1)(2b+1)/[6(L^2+1)] <= 2 sqrt(L)

for t>=2. Its cosine polynomial therefore satisfies

    f_p(x) >= -1/2-Delta >= -1/2-2sqrt(L).

The expected cardinality mu=sum p_a is (5/12)L+O(sqrt(L)). This is a controlled forced plateau, not the discontinuous truncation of an arbitrary profile.

For later coupling, the continuous autocorrelation limit is

    R(s)=1-5s^2+5s^3-s^5,   0<=s<=1.

Riemann sums for the polynomial window give uniform convergence r_a=R(a/L)+O(1/L). Hence, since b=o(L),

    W=sum_a p_a(1-p_a) = (nu+o(1))L,
    nu=integral_0^1 R(s)(1-R(s)) ds = 80/693 > 0.

The forced prefix changes the variance by only o(L). The exact polynomial integral is independently checked in the saved script.

## 3. Rounding with uniform discrepancy and two additional rows

The only imported discrepancy fact is Spencer's real-matrix theorem: for an m-by-m real matrix with entries of absolute value at most one, some sign vector has discrepancy at most 6sqrt(m). This precise real-matrix form is stated in the introduction of Larsen, *Fast Discrepancy Minimization with Hereditary Guarantees*, [primary research paper, p. 2](https://cs.au.dk/~larsen/papers/Hereditary.pdf). Lovett–Meka's [Theorem 4](https://arxiv.org/pdf/1203.5747) also supplies the arbitrary-vector partial-coloring formulation. No claim about a newly proved discrepancy theorem is made.

Use the matrix with L-2 columns and 16L+2 rows consisting of

    cos(2pi a j/(16L)),    j=0,...,16L-1,
    1,
    p_a.

Every restriction to a subset of columns can be padded by zero columns to an m-by-m matrix, m=16L+2. Its sign discrepancy is therefore at most D=6sqrt(m)<25sqrt(L) for L>=2.

Here is the needed fractional rounding consequence, including why forced coefficients remain fixed. Approximate p by dyadic vectors. At denominator 2^k, change only odd coordinates by plus/minus 2^(-k), using a discrepancy coloring of their restricted matrix. This rounds to denominator 2^(k-1) and changes every row sum by at most D/2^k. The sum over all stages is less than D. Integral coordinates are never changed. Taking a subsequence of the finitely many resulting Boolean vectors gives, for the original rational p, a vector eta in {0,1}^(L-2) with eta_a=1 for a<=b and row errors at most D.

Let A={a:eta_a=1} and e(x)=sum_a(eta_a-p_a)cos(ax). The grid errors are at most D. Bernstein's derivative inequality for a degree-(L-2) trigonometric polynomial gives

    ||e||_infinity <= D+(pi/16)||e||_infinity,
    ||e||_infinity < 32sqrt(L).

The two extra rows give

    |n-mu| <= D,
    |sum_a p_a(eta_a-p_a)| <= D.

It follows that n=(5/12+o(1))L and

    M(A) <= 1/2+Delta+||e||_infinity <= 35sqrt(L)

for sufficiently large L. Since n>=L/4 eventually, M(A)<=70sqrt(n). The argument proves existence for each sufficiently large integer t; exhaustive search with a little slack in the row bounds is an effective finite selection procedure. The finite computation below uses heuristic rounding/MIP rather than claiming to implement Spencer's algorithm.

## 4. Completion cost necessarily diverges

Let F_{b+1} be the nonnegative Fejer kernel of mean one, peak b+1, and coefficients 1-|a|/(b+1) on |a|<=b. For any feasible mean-zero completion q, all these nonconstant frequencies belong to ±A, so

    integral q F_{b+1} >= 2sum_{a=1}^b [1-a/(b+1)] = b.

Also ||F_{b+1}||_(4/3) <= (b+1)^(1/4), by its mean and peak. Thus

    J_≥ >= b/(b+1)^(1/4),
    J_≥^4/N^2 >= b^4/[(b+1)N^2]
        = (36/25+o(1))sqrt(L).

The asserted normalized L^(1/8) divergence follows. Together with N=O(L) and K=O(sqrt(L)), it also gives J_≥^4/(NK^2) tending to infinity. This is a genuine Boolean obstruction, rather than a failure confined to fractional packets.

## 5. Adaptive interior coefficients still give a square-root certificate

For the Spencer-selected sets above take

    q=D_A-D_p=2e,
    a=integral D_A q=2sum_{a in A}(1-p_a).

This q is real and mean-zero, but is **not** a uniform-coefficient completion. Its coefficient on the forced prefix is zero. From the two extra rounding rows,

    a=2W+O(sqrt(L)),    hence a>=nu L eventually.

Also ||q||_infinity<64sqrt(L). Notice the factor two: the discrepancy e above was defined for cosine sums, while D_A-D_p=2e. Thus Q=integral q^2<=4096L and |H|=|integral D_A q^2|<=4096sqrt(2)L^(3/2).

With K=2M(A), positivity of K+D_A on span{1,q} gives

    K^2 Q+K H >= a^2.

Writing k=K/sqrt(L),

    4096 k(k+sqrt(2)) >= nu^2.

This already gives a positive constant. Since this particular q is bounded in supremum norm, a simpler L1 estimate gives a stronger explicit value. Mean(D_A)=0 and D_A>=-K imply ||D_A||_1<=2K. Consequently

    nu L <= a <= ||D_A||_1 ||q||_infinity <= 128K sqrt(L),
    M(A) >= [nu/256]sqrt(L) >= [5/11088]sqrt(n).

This completes the two-sided theorem with c=5/11088 for sufficiently large t. It proves a square-root bound for the constructed family even though its uniform-coefficient completion cost diverges. It does not provide a comparable discrepancy profile for an arbitrary A. The finite certificates below use actual Q,H and rational determinants rather than the coarse supremum constants.

## 6. An energy check that isolates the prefix obstruction

A separate prefix-only test uses q_b=2D_[1,b]-D_[1,2b]. Its coefficients are +1 for 1<=|a|<=b, -1 for b<|a|<=2b, and zero elsewhere. Its constant Fourier coefficient and its value at x=0 are both zero, and Q=4b.

Let c be these Laurent coefficients. Then integral F q_b^2=||v*c||_2^2/E. For L>=4b, in the interior 2b<=j<=L-2b the quadratic formula for v and the zero zeroth/first moments of c give |(v*c)_j|<=20b^3. On the at most 8b+2 boundary indices, |(v*c)_j|<=16Lb^2. Since E>=L^5/32,

    integral F q_b^2 <= 12800 b^6/L^4 + 81920 b^5/L^3
                      <= 100000 b^5/L^3.

For b=L^(5/6) this is O(L^(7/6))=o(L^(3/2)), while the fourth power is at least b^4/(b+1), of order L^(5/2). Thus controlling energy directly can be much cheaper than controlling the global fourth moment. q_b only interpolates the prefix and can conflict with selected frequencies in (b,2b]; it is explicitly **not** a full-support certificate. The complete adaptive q in Section 5 is the actual certificate for the rounded family.

## 7. Finite witnesses and verification

All calculation used Dirichlet through src/dirun.sh. Gurobi 13.0.3 refined the t=2,3 candidates; t=4,5 used the best of 32 seeded cardinality-adjusted Bernoulli samples. These finite witnesses are distinct from the existential Spencer choice above. Their lower certificates are exact for the actual saved sets, regardless of how they were selected.

| L | b | n | Fejer lower bound J_≥/sqrt(N) | Exact certificate R lower | Arb certificate R upper |
| --- | --- | --- | --- | --- | --- |
| 64 | 32 | 35 | 1.595777 | 0.233612 | 1.017678 |
| 729 | 243 | 337 | 2.368257 | 0.264086 | 0.821552 |
| 4096 | 1024 | 1793 | 3.022134 | 0.346443 | 1.209338 |
| 15625 | 3125 | 6687 | 3.613866 | 0.356711 | 1.457435 |

The last set rigorously has J_≥^4>128N^2, so the previous uniform-completion threshold cannot certify it. Its variable-coupling certificate has a/N about 0.246861 and fourth power/N^2 about 0.183119, and does certify R>0.3567. The exact rational lower K values and negative determinants, not rounded table values, are authoritative.

Upper verification: a 96-bit Arb DFT encloses the entire finite grid. An integer H is accepted only after every ball value is strictly above -H. At a true global minimizer f'=0, so a nearest grid point yields

    M(A) <= H + pi^2 sum_a a^2/(2Q_grid^2)
          < H + 242 sum_a a^2/(49Q_grid^2).

The final upper bound is rational. This uses the entire circle, not grid minima as substitutes for global minima.

Lower verification: q=D_A-D_p has rational coefficients. FLINT integer polynomial multiplication gives Q,H,a and integral q^4 exactly. The rational K lower candidate is accepted only if K^2Q+KH-a^2<0. A separate standard-library verifier reconstructs the square using signed Kronecker substitution and Python integer multiplication; all four Q,H,a,fourth-power values and determinants agree. It also checks the Fejer lower bound and the strict 128 obstruction for t=5. The independent verifier does not replace the Arb grid enclosures for the upper bounds.

Files: src/cstar_forced_plateau.py, src/cstar_plateau_noise.py, src/cstar_plateau_verify.py, src/cstar_plateau_energy.py. Data: experiments/forced_plateau_2026-10-20/{results,noise,verification,energy}.json. No solver job remains live from this pass. A separate-agent review was attempted, but spawning failed because the configured default model gpt-daybreak-blue-latest was unavailable. No independent human/agent or Lean audit is claimed.

## Strategic review

**Discontinue:** a generic deduction of bounded uniform-completion cost from a bounded Chowla ratio, and the proposed bound J_≥^4=O(NK^2). Both have actual Boolean asymptotic counterfamilies. Increasing the completion cutoff would not repair the Fejer lower bound.

**Continue:** the actual mixed certificate with variable interior coefficients and coupling a of order N. The plateau family demonstrates why forcing every interior coefficient to 1 loses useful certificates. Full W2 already allows variable interior coefficients; this returns to that genuine open problem rather than asserting a new universal theorem. The prefix-only energy calculation and full variable-coupling certificates test this change of mechanism concretely.

**Exact remaining gap:** obtain such a certificate for arbitrary hypothetical low-ratio extremizers, where no independent or controlled-discrepancy profile is given. A general bounded-supremum error with macroscopic coupling would itself imply Chowla immediately from ||D_A||_1<=2K. Calling that condition an adaptive density theorem would merely rename C*. The next general attempt must exploit Boolean integer structure to produce the certificate or exclude a specified many-spike model; model-specific rounding alone has not done that.

The construction track is preserved: the present family has a proved positive lower ratio, so it is not a candidate for a quantified disproof. The strict-record uniform-completion conjecture remains logically open, but this pass supplies no new reason to expect its missing inverse step. It is deprioritized in favor of certificates that retain variable interior coupling. Full Chowla and the original active goal remain open.

**Subsequent simplification (same date).** The exact Boolean identity a=Q/2+V+n-mu, proved in the [integer-cone continuation](cstar_integer_cone_2026-10-20.md#6-adaptive-profile-identity-and-why-it-is-not-yet-the-universal-step), shows that the extra weighted p_a row above is unnecessary merely to obtain a macroscopic lower coupling: the cardinality row and V~nu L already suffice. The weighted row remains a valid way to obtain the sharper asymptotic a~2V. This changes the sufficient hypotheses, not the open general-profile existence step.
