# Mean-zero partial majorants and the failed dual threshold heuristic

Date: 2026-10-20. Paper derivations and exact finite checks are distinguished below. No full Chowla theorem, asymptotic counterexample, novelty claim, or kernel verification is asserted.

## 1. Target and the precise sufficient estimate

Let A be any nonempty finite set of distinct positive integers, S=±A, N=|S|=2|A|, D(x)=sum_{s in S} e^{isx}=2f_A(x), and K=-min D=2M(A). All integrals below use probability Haar measure on the circle.

Define the relaxed completion cost

    J_≥(S) = inf ||q||_4,
    q real, mean(q)=0, qhat(s) >= 1 for every s in S.

The coefficients on S are real, and coefficients at unused frequencies are unrestricted. Reflection averaging permits restriction to real even q. This is weaker than prescribing qhat(s)=1, hence J_≥ <= J_=.

For any feasible q, let a=integral Dq >= N, Q=integral q², H=integral Dq². Positivity of K+D gives a positive semidefinite two-by-two matrix on span{1,q}:

    K(KQ+H) >= a² >= N².

Also Q <= ||q||_4² and |H| <= sqrt(N)||q||_4². Thus, with k=K/sqrt(N) and j=J_≥/sqrt(N),

    k(k+1) j² >= 1.

In particular, J_≥^4 <= 128N² implies M(A)>sqrt(|A|)/20, by the same numerical comparison as the equality-completion criterion. This is a sufficient criterion, with a complete implication to Chowla; the needed uniform cost bound is not proved.

A uniform all-support bound J_≥=O(sqrt(N)) is false: the nonnegative Fourier coefficients of the interval Fejér dual used for J_= give the same obstruction for J_≥. For A=[1,n], pairing with F_{n+1} gives J_≥ >= n/(n+1)^(1/4). The constant term pairs to zero. Indeed its nonconstant pairing is n and ||F_{n+1}||_{4/3} <= (n+1)^(1/4), using its mean one and peak n+1.

A possible remaining sufficient statement is a bounded normalized cost on a sequence of exact strict-record minimizers. This still requires a new quantitative theorem about Boolean extremality; no equivalence with Chowla is claimed.

## 2. Existence, duality, and a positive-spectrum statement that is valid

The feasible set is nonempty, convex, and weakly closed in real L4. A bounded minimizing sequence has a weakly convergent subsequence, and the norm is weakly lower semicontinuous. Strict convexity gives a unique minimizer q. Reflection invariance and uniqueness make q even.

There are finitely many coefficient inequalities on the mean-zero subspace. Their linear map is onto (use the cosine basis), and (1+epsilon)D is strictly feasible. Convex separation, or finite-dimensional Lagrange duality after passing to the quotient by the common kernel, therefore gives

    u=q³ = c0 + sum_{s in S} lambda_s e^{isx},
    lambda_{-s}=lambda_s >= 0,
    lambda_s (qhat(s)-1) = 0.

Here the conventional positive factors in the objective's derivative are absorbed into the multipliers. Conversely, this representation and complementary slackness certify optimality: for any feasible v, integral q³(v-q)>=0, and convexity of integral v^4 supplies the claim. The mean-zero equality is why c0 is free; positivity of c0 is not asserted.

The corresponding exact dual formula is

    J_≥ = sup (sum_{s in S} uhat(s)) / ||u||_{4/3},
    u=c0+sum_{s in S} lambda_s e^{isx}, lambda_s>=0,

excluding the zero polynomial. The upper inequality is Hölder and coefficient domination. Equality is attained by u=q³: complementary slackness gives

    m := integral q^4 = sum_s lambda_s = u(0)-c0,
    ||u||_{4/3} = m^(3/4).

This argument is a mean-zero version of the partial-majorant variational framework in Fournier–Vrecko, *Minimal Fourier majorants in L^p*, Section 2, [arXiv:2112.13799v1](https://arxiv.org/html/2112.13799v1). Their general partial-majorant problem does not impose our mean-zero constraint; the free constant above must be retained. Their special full-majorant theorem at p=4/3 does not imply positivity for our equality-constrained primal at p=4.

## 3. Exact translation identity and its limitation

Take the continuous representative q=cuberoot(u). Define

    g(x)=u(0)-u(x)=sum_s lambda_s(1-e^{isx}).

The nonnegative multipliers imply g>=0. They also imply conditional negative definiteness: for any real b_i with sum b_i=0,

    sum_{i,j} b_i b_j g(x_i-x_j)
      = -sum_s lambda_s |sum_i b_i e^{isx_i}|² <= 0.

Complementary slackness and qhat(0)=0 give

    integral q(t)³q(t+x) dt = u(x)-c0.

Expanding a fourth power now proves the exact identity

    g(x) = (1/8) integral |q(t)-q(t+x)|^4 dt
         + (3/4)[m - integral q(t)²q(t+x)² dt].

The bracket is nonnegative by Cauchy–Schwarz. Fourier orthogonality and qhat(s)>=1 also give

    integral |q(t)-q(t+x)|² dt >= 2(N-D(x)),
    g(x) >= (N-D(x))²/2.

These are genuine structural facts about the relaxed optimizer. Their immediate direction is a lower bound for the completion cost, not the upper bound needed in Section 1. In particular, integrating the last inequality gives m>=(N²+N)/2, weaker than the direct m>=N² from Parseval. Multiplying it by K+D gives another lower bound for m. This calculation does not close the Boolean extremality gap and must not be advertised as doing so.

## 4. An exact weighted countercontrol to equality-dual positivity

This example concerns positive unequal prescribed coefficients, not an admissible Boolean Chowla support with all coefficients one.

Let h(x)=sign(cos x)|cos x|^(1/3), I=integral |cos x|^(4/3), and q*=h/I. Then mean(q*)=0 and q*hat(1)=1. Hölder shows that q* is the unique minimum-L4 function with mean zero and qhat(1)=1, and also for qhat(1)>=1. Its cube is I^(-3)cos x.

Write I_r=integral |cos x|^r. Integration by parts gives I_{r+2}/I_r=(r+1)/(r+2). The identities for cos(3x) and cos(5x) therefore give, for alpha=1/3,

    q*hat(3)/q*hat(1) = (alpha-1)/(alpha+3) = -1/5,
    q*hat(5)/q*hat(1)
      = 16(alpha+2)(alpha+4)/[(alpha+3)(alpha+5)]
        -20(alpha+2)/(alpha+3)+5 = 1/10.

Fix any beta in (0,1/10), for example beta=1/100. The inequality problem qhat(1)>=1, qhat(5)>=beta is minimized by q*, with the frequency-5 constraint strictly slack. The equality problem qhat(1)=1, qhat(5)=beta has strictly larger norm.

More precisely, let V(b) be its minimum fourth power with qhat(5)=b. Existence and strict convexity of the primal imply strict convexity of V. Its unique global minimum is at b=1/10. If u_beta=q_beta³=c0+2lambda_1 cos x+2lambda_5 cos(5x), the supporting derivative is 8lambda_5: convexity of the fourth power gives V(b')>=V(b)+8lambda_5(b'-b). Taking b'=1/10 yields lambda_5<0 whenever b<1/10. Thus the true unrestricted equality optimizer has a negative nonconstant dual coefficient, despite strictly positive prescribed data.

This disproves a generic sign inference from convexity or from positivity of the data. It does not disprove a sign theorem special to Boolean data. The targeted numerical comparison reproduces this gap and slack; the proof above supplies the all-frequency conclusion without trusting a solver.

## 5. Exact finite miss for computed dual threshold deletion

The finite probe augments B={1,2,3,4,5,6,7,9}, whose M(B)=2 exactly. It found

    A={1,2,3,4,5,6,7,8,9,13},
    R(A) approximately 0.73413735,
    R(B)=1/sqrt(2) approximately 0.70710678.

Starting from the saved rounded rational finite-degree completion, cube its Laurent polynomial exactly and retain its coefficients on S∪{0}. This is a valid rational polynomial in the equality-dual space. Sort the positive frequencies by these exact integer weights. All 18 nonempty proper upper/lower coefficient-rank prefixes have R strictly larger than R(A), even though B improves it. Rank prefixes allow tie-breaking and are at least as permissive as strict level sets.

Independent verification reconstructs the cube by dictionary convolution. It proves M(A)<=580387/250000=2.321548 with a rational Chebyshev polynomial and exact Sturm root count. A rational evaluation proves R(B)<R(A). For every prefix C, another rational Chebyshev evaluation gives a negative value v with

    |A| v² > |C| (580387/250000)²,

so R(C)>R(A). Finally, the exact factorization of f_B+2 by t+1 and a root count for the quotient establish M(B)=2.

Scope: this refutes thresholding the saved computed rational dual as a guaranteed deletion rule. It does not certify the ordering of the true unrestricted optimizer, whose Fourier coefficients differ from the finite completion; nor does it refute a large-cost theorem restricted to exact global minimizers. The candidate A has only moderate cost and is not a strict-record minimizer.

## 6. Reproducibility and strategic decision

Code: src/cstar_dual_deletion.py, src/cstar_dual_deletion_verify.py, src/cstar_dual_sign.py, src/cstar_partial_majorant.py. Data: .research/experiments/dual_deletion_2026-10-20/{probe,verification,dual_sign,partial_majorant}.json.

All computation was on Dirichlet through src/dirun.sh, with Gurobi 13.0.3. The sign probe tested all 968 subsets of [1,10] of size at least 3 and found no projected coefficient with relative negativity below -0.001. This is a finite numerical screen, not a sign theorem. The partial-majorant probe ran eight convex solves: equality/inequality pairs for the weighted {1,5} control, B, A, and [1,32]. All reported optimal finite QCP status. The three Boolean pairs agreed numerically; the weighted pair had normalized costs about 1.072574 versus 1.064165 and frequency-5 slack about 0.089959. Finite cutoffs and numerical dual integrals do not certify unrestricted optimality.

Global review: the cheap rank-threshold version of the inverse/deletion step is discontinued. Positive dual spectrum can be obtained legitimately by relaxation; this weakens the sufficient target and gives a precise translation structure, but its immediate estimates have the wrong direction. Do not increase the sign-search box or promote these identities into a full proof. The next useful analytic task is to turn exact Boolean extremality into an upper bound on the relaxed cost, or find an exact strict-record countercontrol. The construction track still needs a nonproduct, non-band-concentrated correlated law; neither this finite miss nor the weighted sign control is a counterexample to Chowla. The original lower-bound, factor/construction, and correlated-selector lines remain distinct; no new universal progress is claimed beyond these delimited results.

Independent proof review / Lean: not completed. Earlier attempts to launch the instructed separate reviewer failed because the configured default agent model was unavailable. This paper argument has been checked directly here but is not labeled externally audited or kernel checked.
