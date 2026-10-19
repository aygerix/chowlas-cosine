# Round 15 report — P66 verified, D_(2/3) certified, cyclic stability obstruction

Status: complete for the round-15 brief, 2026-10-19. PROVED (paper audit plus exact computer certificates): P66 is correct, and its range extends to every C < 1000/73 = 13.6986301369863. Part B produces explicit stability and parity lemmas and a precise obstruction; no new unconditional cyclic exponent is claimed. None of this round is Lean kernel-checked.

## Scope and rules

Read tdense15_brief.md, CLAUDE.md, and the number-theory-research skill. The round-specific rules govern: no subagents, no commits, no edits to the project-level .research markdown files, markdown mathematics only. All substantive computation ran through DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4. This report and tdense15_scratch are the work products.

## Exact targets

- Part A: audit P66 including the double limit and the common class of Gabor kernels; independently certify E94b; port the exact P63 certifier to sigma = 2/3 and aim at D_(2/3) <= 73/1000.
- Part B: for every prime q = 1 mod 4 and every symmetric B in Z_q with 0 outside B and |B| = (q-1)/2, obtain an exponent theta > 1/4, a conditional theorem with one explicit missing lemma, or a mathematically precise obstruction to the proposed equality-stability route.

## Initial research frontier (historical)

KNOWN: the second-order cyclic identity gives the 1/4 exponent; scalar and fixed-order barriers are recorded in P63–P67. P66 is an unreviewed paper argument with a prior exact mixing certificate.

EXACT GAP: equality-case instability alone does not automatically imply a power saving. The dependence on the defect, the zero spike, and the regime K/q^(1/4) must be derived before using a stability assertion.

CANDIDATE MECHANISMS: exact defect identities from the Boolean convolution equation; a sign-controlled algebraic certificate for E94b; a sigma-dependent Bernstein certificate; positivity and sparse-support tests for the proposed flat Fourier model.

DISCRIMINATING TESTS: Paley sets, stored exact small-q optima, random-profile adversaries, and the non-Boolean moment fakes. Numerical observations will be labeled NUMERICAL and will not be used as global proofs.

## Checkpoint log (historical; final results follow)

- Read P61–P67, NOTEBOOK cont. 17–18 (including 18.5), E93–E96, and the relevant prior certificate code. A novelty grep also found P26: the exact equivalence with symmetric nonnegative flat-convolution weights is already in the record and will be quoted, not rediscovered.
- PROVED, finite exact computer check: E94b rerun reproduces 910 rational cells and D_(2/3) <= 106093113972925730591/1406250000000000000000, giving C < 13.254865912964584 (decimal for orientation).
- PROVED, independent exact algebraic check: mixing_sturm.py substitutes s = sqrt(1-x), squares only after checking the right side is positive, and proves a cubic quotient has no roots in [0,1] by Sturm. Details and exact polynomials are saved in mixing_sturm.json. This is a different method from the original interval bisection.
- The first sigma-port attempt stopped at exact monotonicity validation: the floating discovery potentials have tiny decreases. No certificate was claimed. A cumulative-maximum rational reconstruction repairs monotonicity; every resulting continuum inequality is being checked afresh.
- PROVED, finite exact computer certificate: the repaired sigma port passed all 128 half-cells and all 64 continuum Schur cells, with D_(2/3) <= 73/1000. The exact minimum Schur margin is 1704250072843/1966080000000000. Thus P66 extends to every fixed C < 1000/73 = 13.6986301369863, with an ineffective positive constant c(C). A separate verifier is reconstructing the rational inputs and every sign.
- PROVED preliminary correction to Part B: the omitted principal mode gives P-inverse minus N-inverse = b - (q-1)/(2q), not b - 1/2. The exact P26 shift gives nonnegative weights h(0)=K-1/2 and h(gamma)=lambda(gamma)+K off zero, with h*h = (q^2/4) delta_0 + q K(K-1) 1. Hence (Lambda+K)^2 <= q K(K-1). This already rules out asymptotic equality in the weaker sqrt(2q) K bound; it changes a constant, not the exponent. A full defect and stability derivation is in progress.
- PROVED, independent sigma verification completed: 767 covering leaves, 127 support caps, all 188 support lines, the 18 long Gram lines, and all 64 Schur cells pass exact reconstruction. See sigma_independent.json and its log.
- NUMERICAL, VM: stability_probe.json measures exact integer pair-list sets (small enumerated candidates, E41, E90), Paley, repaired random-profile half-sets of R13-PK and R14-UNION type, and an R12-S non-Boolean fake. All genuine half-sets pass the full shifted convolution identity numerically at every displacement. The small-q selected spectra are independently enclosed by 180-bit Arb; floating enumeration alone is not an optimality proof.

## Strategic review after the first two Part B attacks

HEURISTIC decision, based on the proved identities: discontinue attempts to obtain a power improvement just by excluding equality in the old second-order constant. The sharper constant is already forced by the full identity quoted in P26. A stability theorem needs a second, genuinely global estimate when K/q^(1/4) grows. Continue with (a) a defect-sensitive endpoint-rounding lemma and robust parity threshold, and (b) an exact audit of how uncertainty/Galois arguments could control the required error. Additional small-q optimization is not a discriminating experiment for that growing-ratio regime.

PROVED correction to the proposed support conclusion: near saturation controls the heavy core, not the cardinality of every positive eigenvalue. A large number of very small positive coefficients can fit inside a small moment defect. The final theorem below will use an explicitly thresholded core and will retain the principal-mode error.

## Part A — adversarial P66 audit

PROVED conventions for this audit: write a_k for the even binary coefficient array, a_0 = 0; q_k = (k_h*a)_k and r_k = a_k-q_k. Integrals in t below use the positive half of the even profile. The circle variable is still x in cos(kx). In this section q_k is a smoothed coefficient, unrelated to the prime q of Part B.

| P66 input or step | Verdict | Exact qualification |
|---|---|---|
| Step 1: P58 compactness and high-pass centering | CORRECT | Use the same smoothing diagonal for the first, second and third profiles. The degree is X+h, not literally X; h/X tends to zero. |
| Step 2: Schur cube and the 4m^3/X error | CORRECT | The nonzero complex Fourier coefficient is r_k/2 and the zero coefficient is m. |
| Step 3: weak cubic profile | CORRECT | At fixed epsilon there is a residual cross term. It vanishes when epsilon tends to zero; it must not be discarded before that limit. |
| Step 4: PD closure | CORRECT | First pass X to infinity for fixed epsilon, then epsilon to zero, or take a sufficiently slow common diagonal. The final continuous compactly supported profile has nonnegative Fourier transform. |
| Step 5: cubic front cap | CORRECT | The IVT argument uses a = p(0) <= 1/2, continuity, and p(1)=0. It does not use p(0)=max p. |
| Step 6: smaller root, Gabor/Jensen and sigma monotonicity | CORRECT | The identity p=phi(4e) uses p(t)<=1/2 everywhere. That follows from the quoted P58/P59 conclusions, not from a bound at t=0 alone. |
| E94b and the common class W | CORRECT | Both integrals are bounded for the very same w. Complex w are majorized using the nonnegative autocorrelation root before applying the P63 certificate. |

### A1. The cubic limit, with both limiting operations visible

PROVED: fix epsilon > 0 and take h = floor(epsilon X). Weak convergence of the bounded binary coefficient measures gives q_k, on the rescaled grid, uniformly converging to Q_epsilon = k_epsilon*p. One way to justify uniformity is to use a finite net of translates of the continuous triangular kernel; its rescaled discrete translates are uniformly equicontinuous at fixed epsilon. Rounding h changes nothing in this limit. All arrays are supported in a common bounded interval.

PROVED exact binary identity, at every index:

    r_k^3 = r_k (1-3q_k+3q_k^2) + g(q_k),
    g(u) = u-3u^2+2u^3.

PROVED: for any continuous compactly supported test psi, the fixed-epsilon limit of the tested cubic measure is

    integral psi(t) [(p-Q_epsilon)(1-3Q_epsilon+3Q_epsilon^2)
                     + g(Q_epsilon)] dt.

The first displayed term is generally nonzero at this stage. Since p is continuous, compactly supported and bounded, Q_epsilon tends uniformly to p as epsilon tends to zero. On [0,1], |1-3u+3u^2|<=1 and |g'(u)|<=1. Thus the difference of this limit from integral psi*g(p) is at most

    2 ||Q_epsilon-p||_infinity ||psi||_1.

PROVED conclusion: the cubic profile is exactly g(p), with no surviving cross term. Equivalently, choose a slow diagonal with q tending uniformly to p. The weaker strong-L2 diagonal in P58 also suffices: the multiplying polynomials are bounded and Lipschitz, and the bounded coefficients r_k give the corresponding discrete Cauchy-Schwarz bound on the rescaled grid. The O(h) boundary tail disappears when epsilon tends to zero. The single k=0 term has size O(1/X).

### A2. Normalization and PD closure

PROVED: T = (1-kappa_h) f_A has constant r_0/2. Write T = r_0/2 + g_X and choose m = -min g_X, so 0<=m<=M and H = g_X+m>=0. With normalized circle Fourier coefficients,

    H-hat(0)=m,    H-hat(k)=r_k/2 for k!=0.

The finite sequence H-hat is PD. Its pointwise cube is PD, hence its trigonometric symbol is nonnegative:

    m^3 + (1/4) sum_{k>=1} r_k^3 cos(kx) >= 0.

This gives exactly sum r_k^3 cos(kx) >= -4m^3. In a contradiction sequence M=o(X^(1/3)), the normalized error is 4m^3/X=o(1), uniformly in the test value x=y/X. There is no extra factor from the even extension.

PROVED: passing the preceding weak limit for each real y gives integral_0^1 g(p(t)) cos(ty) dt >= 0. The even g(p) is continuous and compactly supported. Nonnegativity of its Fourier transform therefore makes it PD (alternatively use the distributional Bochner criterion and continuity). In particular |g(p(t))|<=g(p(0)). This closure does not assert that a signed weak limit is pointwise nonnegative without the Fourier argument.

### A3. Front cap and the smaller-root condition

PROVED: g increases on [0,u*], decreases on [u*,1/2], and u*=(3-sqrt(3))/6. If a=p(0)>u*, then a<=1/2 and the path from p(0)=a to p(1)=0 crosses u*. Since g(u*)>g(a), the PD maximum bound fails. Thus a<=u* and e(0)=a(1-a)<=1/6. The maximum property of p is unnecessary for this particular crossing argument.

PROVED distinction: the subsequent identity p=phi(4e) does need p(t)<=1/2 for every t. The quoted p(0)=max p and a<=1/2 supply it. It can also be recovered by a second IVT argument using energy-PD: if p ever exceeded 1/2, it would cross 1/2, contradicting e(t)<=e(0)<=1/6. Merely asserting p(0)<=1/2 without either additional argument would be insufficient.

### A4. Gabor mixture, sigma and the same class W

PROVED: P61's Gabor calculation gives the normalized energy as a limit of convex mixtures of |c_u|^2, where c_u is Hermitian PD, c_u(0)=1 and its support lies in [-(1+delta),1+delta]. Zero-weight pieces with c_u(0)=0 vanish identically and are omitted. The weights are proportional to c_u's unnormalized squared value at zero, not uniform after normalization.

PROVED: for each fixed sigma in [0,1], the map x -> phi(sigma x) is convex, increasing and vanishes at zero. Jensen with the preceding probability weights, followed by integration and the dilation c_u(t) -> c_u((1+delta)t), gives

    integral_0^1 phi(sigma e(t)/e(0)) dt <= D_sigma.

The two support limits and dominated convergence are valid on a common compact interval; e(0)>0 because the density d is positive. Taking sigma=4e(0)<=2/3 gives the exact identity p=phi(sigma e/e(0)). Pointwise monotonicity in sigma gives D_sigma<=D_(2/3). Thus there is no extra Jensen factor or reversed convexity inequality in P66.

PROVED: W is the continuous Hermitian PD class supported in [-1,1], normalized at zero. The quoted Boas-Kac factorization gives w=G*G-tilde for a complex L2 root on an interval of length one. Replacing G by |G| majorizes |w| pointwise, preserving normalization and support. This allows both the P63 certificate and Beckner's inequality to be applied on the same class. Sharp Young at (4/3,4/3;2), followed by Holder on the unit support, gives

    integral_0^1 |w|^2 <= 2/(3sqrt(3)) = 2sqrt(3)/9.

Consequently the pointwise mixing inequality legitimately yields D_(2/3)<=alpha1*(259/2000)+alpha2*(2sqrt(3)/9). There is no optimization over two different kernels hidden here.

### A5. Independent E94b certificate by sign-controlled squaring and Sturm

PROVED (exact computer-assisted): put s=sqrt(1-x), a=233809/10^6 and b=117344/10^6. The desired mixing inequality is equivalent to

    sqrt((1+2s^2)/3) >= R(s),   0<=s<=1,
    R(s)=(234688s^2+233809s+531503)/10^6.

All coefficients of R are positive, so R>0 and squaring is equivalent, with no lost sign condition. Define H=(1+2s^2)/3-R^2=(1-s)T(s). The exact quotient is

    T(s) = (13446889/244140625)s^3
           +(1287678051/7812500000)s^2
           -(593107426589/3000000000000)s
           +152513682973/3000000000000.

PROVED by exact rational Sturm computation: T has zero roots in [0,1], with variation counts (1,1), T(0)=152513682973/3000000000000>0 and T(1)=21911/300000>0. Hence H>=0 and the mixing inequality holds throughout [0,1]. This method is independent of E94b's directed-square-root cell bisection. Both source and full Sturm sequence are in mixing_sturm.py/json. The original rerun also reproduces its 910-cell certificate.

### A6. Dedicated rational certificate at sigma=2/3

PROVED (exact computer-assisted): D_(2/3)<=73/1000. The discovery input is the existing E95 K=64, degree=10, shape=0.1 file. No new numerical optimizer result is used as proof. Rational reconstruction rounds the potential's Bernstein coefficients to denominator 10^10, replaces each row by its cumulative maximum starting at zero, rounds a_j upwards to denominator 10^9, and adds 1/10000. The initial exact validation failure and its monotonicity repair remain in the source/history above.

PROVED certificate mechanism: with x=1-u^2, the pointwise potential inequality has form

    A(u) + sqrt(1-(2/3)(1-u^2)^2)/2 >= 0.

The port replaces the old squared radical by precisely

    1/12 + u^2/3 - u^4/6.

Every saved leaf proves either A>=0 or the squared radical minus A^2>=0. Each selected lower branch for w(2t) lies in [0,1]; each potential is increasing and vanishes at zero. The integrals of B(2t,w(2t))-B(t,w(t))/2 cancel. The remaining integral is bounded by half the quadratic form of the positive symmetric kernel a(|s-t|). The exact Schur test uses U(s)=1+(2/5)s(1-s) and proves T_a U <= (73/500)U, giving the asserted 73/1000 bound.

PROVED verification totals: 767 pointwise covering leaves on 128 half-cells; 127 rational support caps; 188 re-derived support lines; 18 long Gram lines checked by Sturm; 64 exact Schur cells. Minimum Schur Bernstein margin: 1704250072843/1966080000000000>0. The independent verifier uses separate polynomial reconstruction and direct exact row integrals with interpolation. Artifacts: certificate_sigma.json, sigma_independent.json, certify_sigma.py, verify_sigma.py, and their logs.

PROVED integer conclusion: for every fixed real C with 0<C<1000/73, there exists c(C)>0 such that every nonempty finite set A of distinct positive integers with max A<=C|A| satisfies M(A)>=c(C)|A|^(1/3). The constant is ineffective. The endpoint C=1000/73 is not asserted. The passage from a contradiction sequence to a uniform c(C) is valid: bounded n and X<=Cn leave only finitely many sets, each with M(A)>0.

## Part B — corrected equality case and quantitative lemmas

PROVED scope throughout Part B: q is an odd prime, B=-B, 0 outside B, |B|=(q-1)/2, b=1_B, lambda(gamma)=sum_B e(gamma x/q), K=-min_{gamma!=0}lambda(gamma), and Lambda=max_{gamma!=0}lambda(gamma). Such a B exists only when q=1 mod 4. Convolution on Z_q is unnormalized; inverse Fourier transform has factor 1/q. All square roots below are the nonnegative real roots. The main identities work on odd cyclic groups as well; primeness is used for the Galois and support assertions.

### B1. Principal-mode correction and an exact flat-convolution model

PROVED correction to NOTEBOOK 18.5: set P=lambda-positive and N=lambda-negative on nonzero frequencies, and P(0)=N(0)=0. Then

    P-inverse - N-inverse = b - (q-1)/(2q),

not literally b-1/2. Moreover N cannot be exactly K on the positive spectrum. Any argument replacing N by K at every nonzero frequency must account for those missing entries.

PROVED, quoted from P26 after a change of normalization: let

    t=K-1/2,
    h(0)=t,       h(gamma)=lambda(gamma)+K for gamma!=0,
    C0=q K(K-1)=q(t^2-1/4),       L=Lambda+K.

Then h is real, even and nonnegative, and exactly

    h-inverse(x)=b(x)-1/2+K delta_0(x),
    sum h=qt,
    h*h = (q^2/4) delta_0 + C0*1,
    sum h^2 = V := q^2/4 + C0.

PROVED derivation: off zero the inverse is exactly +/-1/2 by Booleanity, and at zero it equals t. Squaring and Fourier transforming gives the displayed convolution equation. Trace gives K>=1/2, hence h(0)>=0. Its nonnegative off-zero convolution first gives K>=1; equality K=1 is impossible because any nonzero h(a) contributes h(a)^2 to (h*h)(2a), whereas C0 would vanish. Thus K>1 and t>1/2. These facts do not drop the zero spike.

PROVED consequence, already implicit in P26's individual square bound:

    L^2 <= C0,    equivalently (Lambda+K)^2 <= q K(K-1).

Take lambda(a)=Lambda and retain the term beta=a in (h*h)(2a). In particular Lambda^2/(2qK^2)<=1/2. Asymptotic equality in the weaker sqrt(2q)K estimate is impossible even before a sophisticated stability theorem. This is a constant correction, not an exponent gain, and is not claimed as a new idea beyond P26.

### B2. Exact local and global defects

PROVED local defect identity: for any a attaining Lambda, define

    R_a = sum_{beta outside {0,a,2a}} h(beta) h(2a-beta),
    Delta_a = [2t h(2a)+R_a]/C0.

Then every summand is nonnegative and

    L^2 = C0(1-Delta_a),    0<=Delta_a<=1.

PROVED global endpoint defect: define

    E = sum_{gamma!=0} (Lambda-lambda(gamma))(lambda(gamma)+K).

Each summand is nonnegative. Trace and Parseval give the exact formulas

    E=(q-1)[Lambda(K-1/2)+K/2-(q+1)/4]
     =(q-1)[tL-t^2-q/4].

Thus L>=t+q/(4t). Combining with L^2<=q(t^2-1/4) yields

    (q-1)t^4 -(3q/4)t^2 -q^2/16 >= 0,
    K >= 1/2 + sqrt( q[3+sqrt(4q+5)]/[8(q-1)] ).

PROVED asymptotic consequence: K>=(1/2+o(1))q^(1/4). This finite constant bound is an elementary consequence of the quoted full convolution model; no exponent above 1/4 follows from it.

### B3. Quantitative rounding, saturation and flatness

PROVED endpoint-rounding lemma: define the symmetric heavy core

    D={gamma!=0 : h(gamma)>=L/2},    s=|D|,
    W=E+t^2.

Then

    sum_gamma |h(gamma)-L*1_D(gamma)|^2 <= W,
    |L sqrt(s)-sqrt(V)| <= sqrt(W).

Proof: for 0<=z<=L, distance(z,{0,L})^2<=z(L-z); sum this on nonzero frequencies and retain the zero-mode error t^2. The second line is the reverse triangle inequality. These statements require no asymptotic notation and remain valid for Paley.

PROVED refinements in the relevant branch Lambda>K: every core element is positive. Write P and N as in B1. Then

    sum |P-Lambda*1_D|^2 <= E,
    |{gamma!=0 : lambda(gamma)>=0 outside D}| <= 2E/(KL),
    |{gamma!=0 : N(gamma)<(1-eta)K}|
        <= s + 2E/(KL) + E/(eta K Lambda),      0<eta<1.

PROVED: on a negative eigenvalue, (Lambda-lambda)(lambda+K)>=(Lambda)(K-N); on a weak positive eigenvalue outside D, h(L-h)>=KL/2. These two observations prove the last two inequalities. On the core, P-Lambda=h-L, and outside it 0<=P<=h, proving the first.

PROVED zero-spike estimate, in the same branch:

    sum_gamma |N(gamma)-K|^2 <= K^2(s+1)+3KE/Lambda =: J.

The extra K^2 is the gamma=0 contribution. On negative modes, (K-N)^2<=K(K-N)<=K E_gamma/Lambda. On weak nonnegative modes use the preceding count; on the core use K^2 per mode. The coefficient 3 is a convenient safe bound because L>Lambda. Therefore, with RMS taken over physical x!=0,

    RMS[P-inverse-(b-1/2)]
        <= sqrt(J/[q(q-1)])+1/(2q) =: R.

This follows from Parseval applied to N-K*1, whose inverse is N-inverse-K delta_0. It retains rather than discards the spike. In particular it cannot repeat the slip in NOTEBOOK 17.7(c).

PROVED quantitative square-flatness consequence: put c_gamma=P(gamma)/q and A0=P-inverse(0). For every xi!=0,

    |sum_beta c_beta c_(xi-beta) -(A0^2-1/4)/q|
        <= [(q-1)/q](R+R^2).

Proof: off zero write P-inverse=(b-1/2)+d; Booleanity gives |P-inverse^2-1/4|<=|d|+d^2. Apply Cauchy-Schwarz to its mean and take its Fourier coefficient. This is the exact point where replacing b by a weighted fake fails.

PROVED scope of the approximate equality conclusions: if q tends to infinity, K=o(sqrt(q)), Lambda*K/q tends to 1/4, and hence E=o(q^2), then W=o(q^2), V~q^2/4, L~q/(4K), and s~4K^2. The bad-negative fraction in the displayed saturation bound tends to zero, so the fraction of the L2 mass of N-inverse at x=0 tends to one. Positive heights on D are close in the stated L2 norm. These are valid quantitative versions of (i) and the heavy-core version of (ii).

PROVED limitation of (ii): the total number of positive eigenvalues is bounded by these estimates only by s+2E/(KL), not by s*(1+o(1)). At K of order q^(1/4), E=o(q^2) need not make the second term o(s). The unthresholded support-size conclusion does not follow from these moment/rounding estimates; no Boolean counterexample to a stronger theorem using additional structure is asserted.

PROVED explicit scalar counterexample to that moment-only inference: for all sufficiently large primes q=1 mod 4, take K=q^(1/4), t=K-1/2, r=4 floor(q^(3/4)/4), and epsilon=1/q. Put r weak positive eigenvalues equal to epsilon. For the shifted nonprincipal spectrum define

    M=(q-1)t-r(K+epsilon),
    V1=(q-1)(t^2+q/4)-r(K+epsilon)^2,
    s=4 ceil(M^2/(4V1)),  mu=M/s,  v=V1/s-mu^2.

Use s/2 core eigenvalues h=mu+sqrt(v), s/2 with h=mu-sqrt(v), all in symmetric pairs, and h=0 at all remaining nonzero modes; h(0)=t. For large q, 0<=v<mu^2, core h>K+epsilon, s~4sqrt(q), and both exact trace and Parseval hold for lambda=h-K off zero. Also Lambda*K/q tends to 1/4 and E=o(q^2), but the positive support has size r+s~q^(3/4), much larger than 4K^2. Assign the core and weak modes in a consecutive symmetric block. Its convolution vanishes outside the block's sumset and therefore fails the full Boolean equation. This is a scalar-relaxation counterexample only. support_counterexample.py/json also certify a finite prime instance at q=1000033 with rational K=32, retaining exact rational mass and energy formulas and Arb core levels.

PROVED limitation of (iii)-(iv): even without endpoint stability, any Boolean half-set has RMS[P-inverse-(b-1/2)]<=K/sqrt(q)+1/(2q). Thus qualitative off-zero L2 flatness is automatic when K=o(sqrt(q)); it is not by itself a new restriction. At the 1/4 scale the needed nonprincipal square-convolution baseline is of order K^2/q, and the preceding error bounds need not be little-o of it. Calling P-inverse=b-1/2 EXACTLY off zero is unjustified. The shifted h model, rather than P alone, is exactly flat.

### B4. A robust reversible-difference obstruction, with an explicit threshold

PROVED parity lemma: let D=-D be a subset of Z_q with 0 outside D and 0<s=|D|<q-1. If r_D=1_D*1_D, then

    r_D(xi) = 1_D(xi/2) modulo 2.

All off-diagonal ordered pairs are paired by swapping their entries; the unique diagonal pair is (xi/2,xi/2). Some nonzero displacements have odd counts and some have even counts. Consequently, for every real c,

    max_{xi!=0} |r_D(xi)-c| >= 1/2.

This proves directly, for odd cyclic groups, the relevant impossibility of a nontrivial unweighted reversible difference set. The full classical cyclic statement is Brualdi, [A Note on Multipliers of Difference Sets](https://nvlpubs.nist.gov/nistpubs/jres/69B/jresv69Bn1-2p87_A1b.pdf), J. Res. NBS 69B (1965), 87–89, theorem on p. 87: for 0<lambda<k<v-1, -1 is not a multiplier. Its odd-order proof is precisely the parity argument on p. 88. This theorem is about unweighted sets, not arbitrary nonnegative real weights.

PROVED quantitative weighted consequence: suppose h is the exact model in B1 and D is its rounded core, with 0<s<q-1. Put e=h-L*1_D. Then

    ||h*h-L^2 r_D||_infinity <= 2L sqrt(s)||e||_2+||e||_2^2.

Since h*h=C0 off zero, parity forces

    2L sqrt(s) sqrt(W)+W >= L^2/2,
    E+t^2 >= L^2 [sqrt(s+1/2)-sqrt(s)]^2
             = L^2/[4(sqrt(s+1/2)+sqrt(s))^2].

PROVED proof of the norm inequality: expand h*h=(L1_D+e)*(L1_D+e) and apply the convolution bound ||f*g||_infinity<=||f||_2||g||_2 to each error term. Thus the displayed numerical threshold is a rigorous stability version of the exact parity obstruction, with no cancellation assumption on the error.

PROVED scale diagnosis: if K~q^(1/4)/2, Lambda~q^(3/4)/2 and s~sqrt(q), the right side has order q, whereas V has order q^2 and t^2 has order sqrt(q). Parity therefore forces only E of order at least q, or a relative moment defect of order at least 1/q. It does not give a fixed relative defect, much less a power saving on Lambda. At K~q^(1/4) times a polylogarithm and an endpoint-like spectral distribution, the corresponding threshold is of order q divided by the fourth power of that polylogarithm. No estimate obtained here forces E below that threshold.

### B5. Galois and uncertainty: exact facts and failed quantitative extensions

PROVED exact two-value classification: all nonprincipal lambda(gamma) are Galois conjugates in the real cyclotomic field. Two distinct values have equal multiplicities, since every fiber of the Galois orbit has the same stabilizer size. Trace and Parseval then force the two values to be (-1+sqrt(q))/2 and (-1-sqrt(q))/2. Thus K=(1+sqrt(q))/2. This verifies the Paley spectrum assertion in NOTEBOOK 18.5; it is a verification of the lead's observation, not this round's discovery.

PROVED weak quantitative consequence of algebraic integrality: in the real field of degree d=(q-1)/2, a nonzero difference of two eigenvalues is an algebraic integer, all of whose conjugates have magnitude at most q-1. Its norm is a nonzero integer. Hence distinct eigenvalues are separated by at least (q-1)^(-(d-1)). If a third value exists, this only gives E>=(q-1)^(-2(d-1)) from one interior summand. This estimate is exponentially small in q and does not supply the needed polynomial stability. No stronger Galois estimate is claimed.

PROVED exact support consequence of [Tao's uncertainty theorem](https://arxiv.org/pdf/math/0308286), Theorem 1.1: a nonzero function on Z_q has physical support plus Fourier support at least q+1. Apply this to u=h-inverse-1/2. Its physical support has size (q+1)/2 (K>1 makes its value at zero nonzero), while its Fourier support has size at most 1+|supp(h) outside 0|. Therefore the nonzero support of exact h has size at least (q-1)/2. Exact sparse support of size about sqrt(q) is impossible. An approximate support statement does not follow from this exact theorem.

PROVED counterexample to the tempting unrestricted quantitative replacement: for every odd prime q and integer 1<=d<q/2, the function

    F_d(x)=cos(pi*x/q)^(2d)
          =4^(-d) sum_{j=-d}^d binomial(2d,d-j) e(jx/q)

has nonnegative symmetric Fourier coefficients, support size 2d+1, F_d(0)=1, and |F_d(x)|<=2^(-d) on the half-circle q/4<=x<=3q/4. Taking d of order sqrt(q) makes it exponentially small on about half the group. Thus positivity plus sparse frequencies does not give a polynomial lower bound on the size of values throughout a half-group. This preserves the failed intermediate lemma and identifies the missing hypothesis: F_d is not a Boolean +/-1/2 plateau off zero. Nazarov/Turan type sparse-sum estimates cannot be used here without retaining that extra property and proving the needed dependence on the number of frequencies.

## Adversarial checks and finite data

NUMERICAL unless explicitly labeled exact: all computations used the specified VM wrapper with four cores. No new LP, MILP, QP or SDP was needed. Existing Gurobi discovery data were inputs only to rational certificate reconstruction. The small enumerations selected candidates using floating point, and therefore are not newly claimed exact global optimum certificates.

| Exact set or family | q | K | Lambda | positive modes | fraction with N>=0.9K | RMS distance of P-inverse from b-1/2 |
|---|---:|---:|---:|---:|---:|---:|
| selected small-q candidate | 17 | 2.561553 | 1.561553 | 8 | 0.5000 | 0.314011 |
| selected small-q candidate | 37 | 3.367213 | 10.105610 | 12 | 0.1667 | 0.218244 |
| E41 stored pair list | 61 | 4.081699 | 7.084233 | 12 | 0.2000 | 0.185027 |
| E41 stored pair list | 89 | 4.630072 | 13.394879 | 22 | 0.1818 | 0.182774 |
| E90 stored candidate | 149 | 6.263652 | 37.567965 | 46 | 0.0405 | 0.173113 |
| E90 stored candidate | 601 | 14.155915 | 151.574926 | 242 | 0.0400 | 0.183257 |
| Paley | 65537 | 128.500977 | 127.500977 | 32768 | 0.5000 | 0.250978 |
| repaired R13-PK random profile | 65537 | 491.720297 | 6683.735719 | 32698 | 0.0001 | 0.280058 |
| repaired R14-UNION type | 65537 | 550.192615 | 2449.119538 | 32822 | 0.0001 | 0.290326 |

NUMERICAL interpretation with scope: the stored optima/candidates are not close to simultaneous endpoint saturation and a sparse positive plateau. Paley is the exact two-valued endpoint example E=0, but its K is of square-root size, half its frequencies are positive, and its substantial zero-mode error t^2 must not be dropped. The R13-PK and union probes have large K and remain adversaries against unqualified universal peak bounds. The branch Lambda>K in B3 explicitly excludes Paley; B1, B2, endpoint rounding, and the parity threshold all apply to it and passed.

PROVED finite checking scope: proof_checks.py exhaustively checked the parity identity and its nonconstant consequence for all 318 nonempty proper symmetric nonzero supports at q=5,13,17, using integer representation counts. It also independently checked the defect algebra symbolically. NUMERICAL: 19 stored exact pair-list sets were tested against the new rounding, negative-saturation, zero-spike, square-flatness and parity-error inequalities when their hypotheses held. No violation occurred. All genuine half-set cases in stability_probe.py were also checked against the full off-zero convolution equation at every displacement, including the entire positive sumset, not only 2a.

PROVED/NUMERICAL distinction for the small data: exact integer inputs are preserved in stability_probe.json, along with 180-bit Arb enclosures of K and Lambda for the selected q<=101 sets. Exhaustive candidate selection used 2,20,70,3432,48620 sets at q=5,13,17,29,37. E41 optimality beyond those checks is quoted, not re-proved here. Larger E90 lists are candidate inputs. In particular the q=89 printed historical scalar was ignored in favor of the actual pair-list spectrum.

PROVED fake rejection mechanism: R12-S, R13-C and R13-M2 are not Boolean Fourier arrays. The identities (2b-1)^2=1 and therefore h*h=(q^2/4)delta+C0*1 are not consequences of their scalar moments. The proof of square-flatness in B3 and the exact model in B1 use Booleanity exactly at that point. Merely showing that P-inverse and the weighted fake's b-1/2 are close does not show |P-inverse| is close to 1/2.

NUMERICAL R12-S check: reconstructed at q=1000033 with its defining scalar formulas (not asserted to be a binary set); it has K about 50.00055, 99.03% of modes within 10% of -K, and RMS[P-inverse-(b-1/2)] about 0.004903, yet its Boolean square identity fails. The RMS of P-inverse^2-1/4 is about 19.81454 and max|(2b-1)^2-1| about 9797.21. Thus saturation plus that misinterpreted flatness test can look very good on a forbidden fake. The squared-plateau and Boolean residuals are saved as separate metrics.

PROVED finite support geometry / Arb verification of R13-C: re-ran the old construction at odd composite index size 201^3=8120601 and J=3. The prescribed equations at displacements 1,2,3 have exact monomial counts and Arb residuals containing zero. At displacement 8, outside that segment, the normalized sign-convolution defect is enclosed at 0.9703906670001710202791302500160207358750901200561 with radius 3.95e-50. This is a finite check of the fake construction, not a prime half-set example. Its existing paper construction for sufficiently large primes is quoted from P65. R13-M2's fixed-order arithmetic repair does not impose this missing full convolution equation and is rejected for the same stated reason; no numerical instance of that implicit repair is claimed.

## Part B deliverable — precise obstruction and a single missing estimate

PROVED obstruction to the proposed route: excluding the equality configuration, even with an explicit fixed positive defect, only changes the constant in K>=c q^(1/4). The hypotheses K<=A q^(1/4) for a large constant A and Lambda>=c q/K do not force E=o(q^2). Indeed the proved inequalities give only

    E <= (q-1)[t sqrt(q(t^2-1/4))-t^2-q/4].

When t~A q^(1/4), its upper bound divided by q^2 tends to A^2-1/4, which need not be small. For t=q^(1/4) times a growing polylogarithm the bound is even larger. This is an algebraic diagnosis of what follows from the established inequalities, not a claim that a Boolean example attaining the bound exists. It is enough to invalidate the inference from a hypothesized power counterexample directly to the near-equality configuration.

PROVED second obstruction: when endpoint proximity is added explicitly, the rigorous support is a thresholded core and the parity contradiction requires E+t^2 below a threshold of order L^2/s, not merely o(q^2). Exact Galois nonexistence and exact uncertainty do not provide that rate. No Boolean or near-Boolean family at K=q^(1/4) times polylogarithms has been constructed in this round.

CONJECTURED missing lemma, Uniform Reversible Spreading WRS(eta): there are eta in (0,1], A>0 and delta0>0 such that, for every odd prime q and every nonnegative real even array h with

    h(0)=t,  sum h=qt,
    h*h=(q^2/4)delta_0+q(t^2-1/4)*1,
    1/2<t<=delta0 sqrt(q),

one has

    max_{gamma!=0} h(gamma) <= A q^((1-eta)/2) t^(1+eta).

PROVED exact scope of this missing lemma: the displayed flat equation and two normalizations reconstruct a Boolean half-set. In fact h-inverse(0)=t and h-inverse(x)=+/-1/2 off zero; sum_x h-inverse(x)=h(0)=t forces equal numbers of the two signs off zero. Thus the fakes do not meet WRS's hypotheses. This is a precisely normalized form of QU(1+eta), not a claim to have bypassed P65's barrier by renaming it.

PROVED conditional theorem: WRS(eta) implies

    K >= c(eta,A,delta0) q^theta,
    theta=(1+eta)/(4+2eta)>1/4

for every symmetric prime-cyclic half-set. In the small-t branch use L>=q/(4t), giving

    t^(2+eta) >= q^((1+eta)/2)/(4A).

In the other branch t>delta0 sqrt(q) the claimed weaker power bound is immediate. This establishes the exact implication and all quantifiers, without asserting WRS. At eta=1 the exponent is 1/3, consistent with the quoted Sanders half-set theorem; that quoted result does not constitute an independent reconstruction of its missing small-spectrum argument here.

PROVED defect requirement equivalent in scale: WRS would force 1-Delta_a to decrease like a positive power of t/sqrt(q), rather than merely force Delta_a away from zero. For t>=1,

    1-Delta_a <= (4/3) A^2 (t/sqrt(q))^(2eta).

This identifies the additional quantitative estimate needed to convert the equality idea into a power improvement. None of B1–B5 proves it.

PROVED limitation on the integer conclusion: no fixed-density extension or new uniform exponent for all dense integer ranges follows from this round's Part B. Away from half density the original Boolean convolution has the extra (1-2alpha)q lambda term recorded in P67. A future per-density result would need constants uniform on alpha in [1/(4C),1/2] before embedding with q in (4X,8X]. The unconditional integer improvement delivered here is precisely Part A's C<1000/73 range.

## Novelty, reproducibility and final strategic decision

PROVED novelty scope relative to the project record, after grepping PROOFS.md: the independent Sturm mixing check and the sigma=2/3 rational certificate are new verification/certification artifacts. The explicit E-defect, thresholded-core bounds, zero-spike estimates and robust parity-error threshold are new quantified assemblies in this report. P26's exact weighted model and its square bound, P58/P59/P61's compactness and Gabor arguments, P63's certificate machinery, the lead's exact two-value Galois observation, and the classical parity/uncertainty theorems are quoted or verified. No external priority claim is made.

PROVED reproducibility: all substantive numerical and symbolic jobs were run using DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 with bash for shell scripts. The scratch directory contains source, logs, exact rational certificate data, finite input sets, and machine-readable results. No project-level research markdown was edited, no subagents were launched, and no commit was made. The workspace already contains unrelated changes; they were not reverted or intentionally edited.

PROVED artifact verification record: Python 3.12.3, NumPy 2.5.4, SymPy 1.14.0, python-flint 0.9.0. The final manifest hashes the source inputs, report and finished artifacts; its own stdout log is excluded to avoid a self-referential hash. There are 24 numerical probe records, 19 independent stored-pair stability checks, and 318 exact parity supports. The certifier and independent verifier agree on D_sigma=73/1000 and the positive exact Schur margin. No new optimizer calls were made. All assertions about infinite families are proved in the text, not inferred from these finite counts.

HEURISTIC final review: stop this round's near-equality constant-tightening branch. It has yielded rigorous quantitative lemmas, but an equality exclusion alone cannot cover the power-sized annulus that the target theorem requires. The next discriminating derivation is a global estimate for the nonnegative remainder R_a in B2 that forces the WRS scale, exploiting the full Boolean equation at an adaptively chosen growing set of displacements. A separate viable line is the integer taper/CSFG question, where the hard boundary supplies information absent from cyclic half-sets. Growing-order Galois information is another distinct route; fixed-order arithmetic and unqualified robust uncertainty are explicitly excluded by the preserved adversaries. No unattended continuation is implied.
