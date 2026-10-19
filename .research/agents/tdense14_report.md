# Round 14 research report

## Current checkpoint

PROVED final outcome (2026-10-19): the permitted precise-obstruction alternative. Centering does not remove the density dependence of Sanders' binomial main term: the first order with a negative first-order coefficient at density 1/m is m-1 for even m>=4 and m for odd m>=3. More strongly, for any fixed r>=2 and density a<=1/(8r), the ENTIRE exact deleted-atom expression is positive, as proved below. Projecting out the regenerated zero mode destroys associativity. A separate genuine Boolean counterexample shows that union with a fixed dilate can raise the negative threshold from O(sqrt(q log q)) to order q. The corrected integer transfer requires a density interval with a uniform constant. No cyclic exponent above 1/4 at every fixed density and no corresponding new integer exponent or c(C) have been proved.

PROVED limitation of this deliverable. Sanders' asserted half-set exponent 1/3 is source-verified and retained as a QUOTED result. The requested full independent reconstruction of that accounting was NOT obtained. The source-accounting section below identifies the exact unresolved branch: the direct cubic truncation plus Parseval gives only 1/4 when all nonprincipal coefficients are small. This is a limitation of this reconstruction, not a claim that Sanders' theorem is false.

PROVED target and scope. The exact target was: for every fixed density alpha in (0,1/2], find c(alpha)>0 and an absolute exponent theta>1/4 such that every symmetric B in Z_q, q prime, excluding 0, with |B|/q=alpha+O(1/q), satisfies K=-min over gamma!=0 of sum over b in B of exp(2 pi i gamma b/q) >= c(alpha) q^theta. The precise-obstruction alternative, including counterexamples or an identified missing step, is the main deliverable taken here. All following paper proofs are unaudited by a separate agent and are not kernel-checked.

PROVED scope and input checkpoint. Read the round-14 brief, CLAUDE.md, the number-theory-research skill and its method/experiment/review references, and the round-13 report. No applicable AGENTS.md was found in the workspace, relevant subdirectories, or ancestors. The brief overrides generic project instructions to commit, delegate, or edit top-level research Markdown. No subagents, commits, or top-level research Markdown edits were made. Mathematical computation used DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4, launched from bash; every optimization used Gurobi. The local wrapper itself has a zsh shebang, which was preserved.

PROVED prior-art checkpoint. Searched .research/PROOFS.md (the root-level PROOFS.md does not exist) for Sanders, P63, P64, 1/3 and the round-13 fakes before making any novelty claim. P63/P64 already record Sanders' half-set exponent, the cyclic embedding, the elementary peak inequalities and the round-13 barriers. No new mathematical claim has been made at this checkpoint.

HEURISTIC initial research frontier (retained as the research record):

| Known input | Exact gap | Proposed test |
|---|---|---|
| Sanders v2 asserts the half-set exponent 1/3 | Reconstruct the unpublished constant/exponent accounting | Read Sections 2-4 and redo the power argument with all normalizations |
| Centering removes the Fourier zero coefficient | Whether positivity survives centering | Expand the proposed fixed-order binomial argument and identify each sign used |
| R13-C and R13-M2 pass partial convolution or fixed scalar tests | Whether a proposed density argument uses genuine Boolean structure beyond those tests | Audit each derived lemma against both fakes and genuine R13-PK sets |
| Dense integer embedding is recorded in P63/P64 | Constants and uniformity as density varies | Verify q, alpha, K and n inequalities explicitly |

HEURISTIC initial work plan (outcomes recorded below). Extract and inspect the supplied Sanders v2 PDF on the VM; attempt to reconstruct the half-set proof, then test centered positivity and an alternative density argument. Run bounded literature checks and exact-small-set/Arb/Gurobi checks at target densities 1/4 and 1/8.

## First substantive checkpoint: centering is not stable under powers

PROVED normalization. Write normalized spectral convolution as (F*G)(gamma)=q^(-1) sum_beta F(beta)G(gamma-beta), and let delta be the indicator of frequency 0. Thus q delta is its identity. Set a=|B|/q, d=1-2a, H=hat(1_B-a), and, for a!=1/2, U=H/d. Put c=a(1-a)/d^2. Then

    U(0)=0,
    U*U = U + q c delta,
    U*U*U = (1+c)U + q c delta,
    U^(4) = (1+2c)U + q c(1+c)delta.

PROVED consequence. The square is idempotent at nonzero frequencies, but the iterated convolution powers are not. The discarded zero-frequency term acts as the convolution identity at the next multiplication. Projecting out frequency 0 after every multiplication changes the operation and prevents use of the ordinary binomial theorem. This corrects the proposed inference from offzero quadratic idempotence to unchanged higher powers; it does not refute the desired cyclic theorem.

PROVED fixed-order diagnostic. For a nonzero frequency gamma with T=U(gamma)>0, the first two terms in the exact binomial expansion of (U-T 1_gamma)^(r)(gamma) are

    T [A_r - r m_(r-1)],

where A_r=((1-a)^r-(-a)^r)/d^(r-1) and m_j=[a(1-a)^j+(1-a)(-a)^j]/d^j. At r=3 and r=4 the coefficient is 1-2c. It equals -1/2 at a=1/4 and 11/18 at a=1/8. At every fixed r it tends to 1 as a tends to 0. Thus removing the initial zero mode does not give a density-uniform negative first-order coefficient. The nonnegative positive-part truncation introduces additional errors; this diagnostic concerns the ideal exact main terms before those errors.

HEURISTIC next pivot. Quantify how the necessary order grows with 1/a, find a genuine Boolean small-q witness for the failed r=4 identity replacement, and examine whether a different positive transformation can raise density without an uncontrolled new negative Fourier contribution. Separately reconstruct what the displayed Sanders proof actually yields; do not silently infer the asserted 1/3 from an estimate giving 1/4.

PROVED tool checkpoint. VM Poppler and Python PDF packages were initially absent. Installed pypdf and PyMuPDF in the existing VM venv through dirun, extracted the supplied 21-page PDF to sanders.txt, and rendered page 6. No mathematical computation was run locally.

## Second checkpoint: exact density dependence and transfer qualifications

PROVED centered order formula. Put t=a/(1-a). The sign of A_r-r m_(r-1) is the sign of

    1-r t-(r-t)(-t)^(r-1).

For every fixed r>=2 this is positive for all sufficiently small a. More quantitatively, it is positive for every r>=3 and a<=1/(2r): here r t<=r/(2r-1)<=3/5 and (r-t)t^(r-1)<=r/(2r-1)^(r-1)<=3/25. The r=2 coefficient is exactly 1. Thus a negative main coefficient requires r>1/(2a). The first negative order is asymptotic to 1/a as a tends to 0: uniformly for r of order 1/a, the last displayed power term tends to zero and r t=r a(1+O(a)). Exact rational checks of the finite-order signs on the VM passed, as recorded below.

PROVED affine-transformation obstruction. Every pointwise function of the Boolean variable 1_B has two values s and t. A nonzero mean-zero such function satisfies a s+(1-a)t=0. If its square is a positive constant, then s=-t!=0, forcing a=1/2. Consequently a pointwise polynomial transformation cannot simultaneously have zero Fourier mode and a nontrivial involution away from half density. The choice g=2 1_B-1 is an involution at EVERY density, but hat(g)(0)=(2a-1)q. For fixed a<1/2 it therefore has a negative Fourier value of order q, so its positive-part truncation cannot have error controlled by K. Centering fixes this large negative coefficient at the cost quantified above.

PROVED prime-range qualification. For A in [1,X], |A|=n, X<=Cn, the brief's q in (2X,4X] gives a=2n/q>=1/(2C), B=+/-A without collisions, and K_B<=2M(A). It does NOT ensure a<=1/2, which is the density range of the proposed cyclic theorem. For example A={1,2}, X=2, q=5 gives a=4/5. Instead choose, by Bertrand, a prime q in (4X,8X]. Then 1/(4C)<=a<1/2, q>4n, and the same exact Fourier relation holds.

PROVED uniformity qualification and conditional corollary. Suppose that for each delta in (0,1/2) there is k_delta>0 such that EVERY odd prime q and EVERY symmetric B excluding 0 with delta<=|B|/q<=1/2 satisfy K_B>=k_delta q^theta. Then EVERY C>=1 and EVERY nonempty finite positive integer A with X<=Cn satisfy

    M(A) >= 2^(2theta-1) k_(1/(4C)) n^theta.

This follows directly from the corrected prime range and K_B<=2M. If the cyclic theorem holds only for large q, finitely many smaller n can be absorbed using M(A)>=1/2. Separate pointwise constants c(a)>0 at every fixed a do not, without local uniformity or an explicit lower bound, imply a positive infimum over [1/(4C),1/2]. The conditional theorem here states the needed uniform quantifier explicitly.

NUMERICAL experiment checkpoint (now completed). check_round14.py ran Gurobi K-minimization for all odd primes 5<=q<=61, at cardinalities 2*round(q/8) and 2*round(q/16), with at least one pair. It independently exhausted every symmetric set at those cardinalities for q<=31 using integer enclosures of Arb cosine coefficients and cyclotomic equality tests. Stored witnesses received exact rational Boolean-power checks and 220-bit Arb spectral/inequality checks. An initial strict-positivity assertion rejected the q=5 sharp Parseval equality; the verifier was corrected to require an exact cyclotomic two-level equality certificate in that case. This was a verifier boundary case, not a failed mathematical inequality.

## Third checkpoint: a different density boost also has a concrete obstruction

PROVED R14-UNION (new assembly in this round; external priority unchecked). Fix 0<a<1/2 and 0<epsilon<min(a,1-a). For every sufficiently large odd prime q there is a symmetric B excluding 0, of size a q+O(1), such that K_B=O_(a,epsilon)(sqrt(q log q)), whereas C=B union (3^(-1)B) satisfies

    lambda_C(2) = -epsilon^2 q/4 + O_(a,epsilon)(sqrt(q log q)),
    |C|/q = 2a-a^2 + O_(a,epsilon)(sqrt(log q/q)).

Here 3^(-1) means inversion modulo q, not division of an integer set. Thus the most direct Boolean density boost by a union of two dilates can create a negative coefficient of order q from an input whose negative threshold is only of square-root order up to logarithms. In particular, for any fixed s<2 and D>0 the bound K_(B union 3^(-1)B)<=D K_B^s fails for some such B. This does not rule out a carefully selected dilation or a different adaptive boost.

PROVED proof. Independently select each pair +/-x with probability p_x=a+epsilon cos(2 pi x/q). For every nonzero frequency the expected spectrum of B is epsilon q/2-(a+epsilon) at +/-1 and -(a+epsilon) elsewhere. For x!=0, membership of x in C is the OR of the independent bits at +/-x and +/-3x. Its expected value is

    2a-a^2 + epsilon(1-a)(cos x+cos 3x)
      - (epsilon^2/2)(cos 2x+cos 4x),

where cos jx abbreviates cos(2 pi jx/q). Orthogonality, with the omitted point 0 subtracted, gives the asserted coefficient -epsilon^2 q/4+O(1) at frequency 2 and the asserted expected cardinality. Changing one pair bit changes at most four sites of C, hence changes any real Fourier coefficient or its cardinality by at most 4. The independent bounded-difference exponential estimate and a union bound over q frequencies give simultaneous O(sqrt(q log q)) errors for the spectra of B,C and the count of B. Flip O(sqrt(q log q)) pairs to make |B| the nearest even integer to a q. Each flip changes a B coefficient by at most 2 and a C coefficient by at most 4; the same bounds survive. This proves all quantifiers above. It is the R13-PK cosine-profile mechanism used as an adversary to a genuinely different proposed transformation, rather than a new PK claim.

PROVED rounding diagnostic. Another possible boost is w=1/2+(1_B-a)/2, which has density 1/2 and nonzero Fourier coefficients lambda_B/2. For every binary y of density 1/2+O(1/q), at least q/2 sites outside B have |y-w|>=1/4. Hence sum |y-w|^2>=q/32. Parseval and the O(1) mean error force max_(gamma!=0)|hat(y-w)(gamma)|>=sqrt(q/32-O(1/q)). Thus a uniformly two-sided Fourier rounding error o(sqrt(q)) is impossible for this boost. This is an absolute-error obstruction; it does not prove a one-sided negative-error lower bound.

HEURISTIC strategic review. The centered-power route loses the desired fixed-order sign, while union boosting has a genuine Boolean large-negative counterexample and soft boosting cannot be rounded with small two-sided error. Discontinue those three direct transfers. Continue the source accounting audit and complete the reproducible small-prime checks; a new exponent would require an adaptive Boolean operation with a proved one-sided spectral estimate, or a stronger global Fourier inequality. Neither is asserted here.

## Source audit: Sanders v2, Sections 2-4

PROVED (quoted, version verified). The supplied PDF is Sanders, arXiv:0807.5104v2, 14 October 2010. Read the complete relevant statements and proofs on PDF pages 3-9, the statement and exponent sentence on page 2, and the concluding discussion on pages 19-20. Relevant displayed pages were also rendered and inspected. Use b=1_B, F=hat(b), m=|B|, a=m/|G|, L=average |F| and K=-min F. Spectral convolution in this report is normalized; physical ell-1 norms in the next statements use counting measure. The following are restatements in this notation, not new results. [Versioned source](https://arxiv.org/pdf/0807.5104v2).

| Result | Exact applicable statement in this notation |
|---|---|
| Proposition 2.1 | For any nonempty finite symmetric B in an abelian group, either B is a subgroup or K>=1/2. |
| Lemma 2.2 | Let V be a finite subgroup. Let a real symmetric summable f be constant on V-cosets, have f(x)>1/2 somewhere, and satisfy inf_E ||f-1_E||_1<=epsilon ||f||_1. Then either ||f-1_H||_1<=epsilon ||f||_1 for a subgroup H, or min hat(f)<=-|V|/8+epsilon ||f||_1. |
| Lemma 2.3 | Under the analogous hypotheses with inf_E ||f-1_E||_infinity<=epsilon ||f||_infinity, either {f>1/2} is a subgroup, or min hat(f)<=-|V|(1/8-5 epsilon ||f||_infinity/8). |
| Lemma 3.1 | For finite G, symmetric B of density a>0 and 0<epsilon<1, either Spec_epsilon(B)={gamma: |F(gamma)|>=epsilon m} is a subgroup; or K>=epsilon^2 a m/(2L); or there is gamma with epsilon^2 a m/2<=F(gamma)<epsilon m. |
| Lemma 3.2 | For finite G and symmetric B of density a>0, if 0<=F(gamma)<=m/32, then K>=a F(gamma)/(16 L^(2/a+1)). |
| Theorem 4.1 | For finite G, symmetric B CONTAINING 0, density a>0 and 0<D<=m/8192, either |B symmetric-difference H|<=D for some subgroup H, or K>=D^(a/5)/64. The hypothesis 0 in B is present in the source and was omitted in the brief's shortened statement. |
| Lemma 4.2 | For a subgroup V, ||b-b*mu_V||_1=2 inner-product(b,b-b*mu_V), with physical convolution and uniform probability measure mu_V. |

PROVED mechanism of the quoted arguments. For Lemmas 2.2-2.3, threshold f at 1/2. If the threshold set is not closed under addition, choose x,y in it with x+y outside. Pair f (or its threshold indicator) with the physical measure (mu_V-(mu_(x+V)+mu_(-x+V))/2) convolved with its y version. Its Fourier multiplier is nonnegative, bounded by 4 and supported on V-perp. The physical value is at most -1/2 plus the stated approximation error. This gives the displayed negative alternative. Lemma 4.2 follows from 0<=b*mu_V<=1 and equality of its total mass with that of b; the signs of b-b*mu_V on B and its complement are opposite.

PROVED reconstruction of the norm and power accounting. Fourier inversion gives average F=b(0). Since F>=-K,

    L = b(0)+2 average F_minus <= b(0)+2K.

For a nonsubgroup the quoted Proposition 2.1 implies K>=1/2, hence L<=4K. For our 0-excluding B, the sharper L<=2K holds. Put P=max(F,0). Young's inequality and telescoping give, for each integer r>=1,

    ||P^(r)-F^(r)||_infinity <= r K L^(r-1).

Booleanity gives F^(r)=F for EVERY r. For t=P(gamma)=F(gamma)>0, positivity of P-t 1_gamma and the binomial theorem yield

    0 <= P^(r)(gamma) - (r t/|G|) P^(r-1)(0)
         + sum_(j=2)^r binom(r,j)(t/|G|)^j
                              |P^(r-j)((1-j)gamma)|.

The exact first-order main term is (1-r a)t. The source chooses r=2 ceil(1/a), so 2<=r a<=4. At t<=m/32 the higher binomial terms are absorbed. The error above is of order K L^(r-1), and r-1<=2/a+1, which yields Lemma 3.2 with its printed constant. The source then takes nu=aD/(4Lm), so an intermediate coefficient t>=nu m gives K L^(2/a+2)>=a^2 D/64. This extra L comes from the lower cutoff t of order D/L; it must not be dropped when converting a coefficient bound into an exponent.

PROVED reconstruction of the subgroup branch. Apply Lemma 3.1 at epsilon=1/32 after excluding coefficients in [nu m,m/32]. Unless its quantitative negative alternative already applies, Spec_nu=Spec_(1/32)=V is a subgroup of the dual. The omitted spectral energy is at most nu m L, so b*mu_(V-perp) is almost Boolean in ell-1 by Lemma 4.2. Lemma 2.2 either gives a physical subgroup at distance <=4 nu m L<=D, or gives K>=|V-perp|/8-2nu m L. Parseval on Spec_(1/32) gives |V-perp|>=m/1024, so the latter branch is linear in m after the source's choice of D. This reconstructs the mechanism of Theorem 4.1, with density dependence intact.

PROVED (quoted) half-set assertion. Theorem 1.2 concerns every prime q and symmetric B of size (q+1)/2; its displayed conclusion is K>=q^(an absolute positive exponent) times an absolute constant. The following sentence specifies exponent 1/3. Theorem 1.3 is the fixed-positive-density distance-to-a-subgroup version, and primality leaves just {0} and G. For q congruent to 1 modulo 4, a 0-excluding set of size (q-1)/2 becomes a Theorem 1.2 set on adding 0, changing K by 1. At q congruent to 3 modulo 4, parity requires the nearest feasible symmetric cardinality instead. Exact density 1/2 is impossible for odd q; the O(1) cardinality convention is essential.

PROVED partial half-set accounting and its exact remaining gap. One can improve the source's r=4 choice to r=3 near a=1/2. For q odd, gamma!=0 and t=F(gamma)>0, the expansion is exactly

    0 <= P^(3)(gamma) - (3t/q) P^(2)(0) + 3t^3/q^2.

Using ||P^(3)-F||_infinity<=3KL^2 and P^(2)(0)>=m-2KL gives

    0 <= (1-3a)t + 3t^3/q^2 + 3KL^2 + 6tKL/q.

For a=1/2+O(1/q), t<=m/32 and K=o(sqrt(q)), the t terms have a fixed negative gap. Hence t=O(KL^2)=O(K^3). If a nontrivial coefficient of size >=m/32 exists, Lemma 3.1 at fixed epsilon either gives K>>sqrt(q) or an intermediate positive coefficient t>>q; its subgroup alternative cannot be a proper nontrivial subgroup in Z_q, and the full dual is excluded by Parseval for large q. This branch gives K>>q^(1/3).

PROVED obstruction in completing THIS reconstruction. If every nonprincipal positive coefficient is <m/32, the same cubic estimate bounds the peak only by O(K^3). Parseval supplies a peak of order at least q/K when K=o(sqrt(q)), giving q<<K^4, exponent 1/4. The extra factor K cannot be omitted. Thus a complete 1/3 reconstruction still needs a stronger estimate for this small-spectrum branch, or a different argument bypassing it. The branch is not vacuous: Paley spectra are all o(q), although those particular examples already have K of square-root order. No counterexample to Sanders' 1/3 assertion has been found or claimed. Reporting a complete half-set proof here would be unjustified.

## Exact counterexamples and quantitative form of the centered obstruction

PROVED R14-CENTER (new explicit accounting in this report; no external priority claim). For any Boolean B of density a in (0,1/2), the two values of u=(b-a)/(1-2a) are (1-a)/(1-2a) and -a/(1-2a). Consequently, at every r>=1,

    U^(r) = A_r U + q m_r delta,
    A_r = ((1-a)^r-(-a)^r)/(1-2a)^(r-1),
    m_r = (a(1-a)^r+(1-a)(-a)^r)/(1-2a)^r.

This follows by writing the two-valued function u^r as A_r u+m_r and using average u=0. It uses the full pointwise Boolean identity, not merely a scalar moment count. The coefficient of T=U(gamma)>0 in the first two terms of the deleted-atom expansion is A_r-r m_(r-1), as stated above. Its sign formula follows by factoring (1-a)^r/(1-2a)^(r-1)>0.

PROVED sharp reciprocal-density order. At a=1/m, m>=3 an integer, t=1/(m-1). For r<m-1, each even r has positive sign formula immediately. For each odd r>=3 with r<=m-2, its first term 1-r/(m-1) is at least 1/(m-1), while its subtracted term is at most r/(m-1)^2<1/(m-1). At r=m-1 the leading term vanishes: the sign is negative exactly when m is even. If m is odd this order has positive sign, and r=m has negative sign. Therefore the first negative order is exactly m-1 (m even) or m (m odd). For even m its coefficient at the first negative order is

    A_(m-1)-(m-1)m_(m-2) = -(m-2)^(-(m-3)).

So even that first available gap is very small. At a=1/8, the r=7 gap is -1/7776, whereas the r=4 gap is +11/18. SymPy/rational checks through order 20 and an independent exact check at m=3,...,100 agree with these paper identities. Using the next order can improve the constant, but does not change the order's dependence on density.

PROVED explicit genuine-prime witness against the false identity U^(3)=U. Take q=17, B={-1,1}, a=2/17 and c=30/169. At gamma=1, U(1)=(34/13)cos(2 pi/17)>0, and

    U^(3)(1)-U(1)=(30/169)U(1)>0.

The r=3 and r=4 main coefficient is 109/169>0. This B has cardinality within 1 of q/8, is exactly symmetric and excludes 0. It refutes the identity substitution on a genuine Boolean set, independent of any relaxation fake. It does not refute a q^(1/3) lower bound.

PROVED R14-FULL: positivity of the COMPLETE ideal expression at small density. Fix an integer r>=2. Let q>r be prime, let B be any symmetric set of density 0<a<=1/(8r), and let gamma!=0 have T=U(gamma)>0. Then, with normalized convolution,

    (U-T 1_gamma)^(r)(gamma) >= T/4 > 0.

This statement is about the exact signed transform U, before positive-part truncation. It makes the failure of the intended sign contradiction stronger than the first-order diagnostic alone: the complete unperturbed expression already has the sign that positivity requires. It is not a lower bound on K or a barrier to other identities.

PROVED proof of R14-FULL. Put d=1-2a, s=(1-a)/d=1+a/d and v=a/d. Since a<=1/16, d>=1/2, v<=2a, and for every j<=r we have s^j<=exp(2ra)<=exp(1/4)<4/3. Hence |A_j|=|d(s^j-(-v)^j)|<=3. For j>=2, |m_j|<=a s^j+v^j<=4a/3+4a^2<=2a, and m_1=0. Moreover A_r>=d(1-v^r)>=d(1-4a^2)>=1-3a. It follows that

    A_r-r m_(r-1) >= 1-3a-2ra >= 9/16.

Also |U(eta)|<=a q/d<=2a q, so T/q<=2a and rT/q<=1/4. For each 2<=j<=r-1, the frequency (1-j)gamma is nonzero because q>r. Thus |U^(r-j)((1-j)gamma)|<=6a q. The j=r term vanishes for the same reason. The absolute value of ALL terms from j=2 onward in the binomial expansion is therefore at most

    6a q sum_(j=2)^r binom(r,j)(T/q)^j
       <= 6a q r^2(T/q)^2
       <= 12r^2 a^2 T <= 3T/16.

The middle inequality follows from rT/q<=1/4 and the exponential/geometric bound on the binomial tail. Subtracting this remainder from the first two terms gives at least 3T/8, and in particular T/4. This proves the claim uniformly for every B with these parameters. A focused VM check is recorded below; the proof is independent of that finite check.

PROVED explicit failure of projected associativity, even for even arrays. In Z_5 let E1=1_{+/-1}, E2=1_{+/-2}, and define X diamond Y as their UNNORMALIZED convolution with its zero entry then deleted. Then E1 diamond E1=E2, E2 diamond E2=E1, and E1 diamond E2=E1+E2. Hence

    (E1 diamond E1) diamond E2 = E1,
    E1 diamond (E1 diamond E2) = E1+2E2.

Normalization only multiplies both sides by 1/25. Thus projecting at every multiplication cannot support the usual associative convolution-power/binomial calculation.

PROVED size of the retained truncation error. Since ||U||_1=(L-a)/(1-2a)<=2K/(1-2a), positive-part truncation obeys

    ||U_plus^(r)-U^(r)||_infinity
       <= r (K/(1-2a)) (2K/(1-2a))^(r-1).

At fixed density this is O_(a,r)(K^r), not O(K^2) for arbitrary fixed r. Combining the direct bound T=O_(a,r)(K^r), when its other binomial remainders can be absorbed, with a Parseval peak of order q/K gives only K^(r+1)>>_(a,r)q. This is the quantitative output of that norm estimate, not a universal impossibility theorem for all higher-order arguments. At a=1/8 the first favorable r=7 gives only exponent 1/8 through this estimate. It cannot beat the quoted 1/4 dense bound.

## Peak facts, Boolean scope, and round-13 adversaries

PROVED elementary identities (classical inputs, rechecked). For nonempty symmetric B excluding 0 with m=a q, write lambda(0)=m and let Lambda=max_(gamma!=0)lambda(gamma). Then

    sum_(gamma!=0)lambda(gamma)=-m,
    sum_(gamma!=0)lambda(gamma)^2=m(q-m)=a(1-a)q^2.

The trace implies K>=m/(q-1)>a. In fact K>=1: lambda+K is pointwise nonnegative, has average K, and its inverse Fourier coefficient at any x in B is 1, whose absolute value is at most that average. The positive spectral mass S is at most qK, so Parseval gives precisely the brief's valid coarse bound

    Lambda >= [a(1-a)q-K^2]/K.

If a<=1/2, the positive peak exists: otherwise the negative trace and |lambda|<=m would give squared mass at most m^2, less than m(q-m) for odd q. The interval inequality (lambda+K)(Lambda-lambda)>=0 gives the sharper classical form

    Lambda >= [m(q-m)-mK]/[(q-1)K-m].

The denominator is positive in this range by K>=1. This refinement is a moment estimate, not an exponent improvement.

PROVED density-dependent second-order equation. Full Booleanity gives, for gamma!=0,

    sum_(beta!=0,gamma)lambda(beta)lambda(gamma-beta)
       = (1-2a)q lambda(gamma).

At twice a peak frequency this implies

    Lambda^2 <= (1-2a)q Lambda + 2K S
             <= (1-2a)q Lambda + 2qK^2,

when a<=1/2. Omitting the first term is invalid at a fixed density below 1/2. Near the half-set convention it is only an O(Lambda) term, explaining why the elementary quarter-power calculation there does not carry over unchanged.

PROVED adversarial scope audit. The following table covers all mathematical ingredients used above; none is claimed to exclude an exponent-1/3 fake by scalar data alone.

| Ingredient / conclusion | R13-PK genuine cosine-profile sets | R13-C partial-convolution arrays | R13-M2 scalar arithmetic arrays |
|---|---|---|---|
| Trace, energy, sign split, norm and coarse/sharp peak bounds | Satisfied | Satisfied by their exact trace/energy and actual floor | Satisfied by their exact trace/energy and actual floor |
| Nonempty Boolean K>=1 proof | Applies | Not applicable as a Boolean proof; their K tends to infinity anyway | Same |
| Full offzero quadratic equation | Holds at every frequency | Holds only on the prescribed segment; fails at s=2J+2 by order q^2 | Not imposed; scalar counts do not imply it |
| All-power centered recurrence | Holds, since Boolean | Cannot infer it from the selected equations: the missing delta terms need global convolution | Cannot infer it from any fixed list of scalar moments |
| Fixed-order sign obstruction / affine two-value obstruction | Applies, and does not contradict their square-root threshold | Formal coefficient calculation still has the same density cost; physical two-valued hypothesis is absent | Same |
| Small-spectrum cubic estimate Lambda=O(K^3) | Compatible | Compatible at K~q^(1/3), Lambda~q^(2/3) | Compatible at the same scales |
| R14-UNION | Constructed FROM this adversary, with the profile generalized to density a | No Boolean union operation is available for the fake | Same |
| Soft half-density rounding's absolute-error bound | Applies | Requires a genuine binary coefficient array, absent here | Same |
| Integer embedding / conditional corollary | Uses actual integer sets only | Not an integer counterexample | Not an integer counterexample |

PROVED R14-FULL's additional scope check. All three original round-13 inputs have density tending to 1/2, so its hypothesis a<=1/(8r) fails there. The low-density genuine cosine-profile family in R14-UNION does satisfy its Boolean hypothesis when a is small enough, and its complete deleted-atom expression is positive as asserted. For a low-density analogue of either relaxation fake, the full Boolean power recurrence would have to be established before R14-FULL could be applied. The statement imposes no restriction on K and is not claimed to rule out any round-13 spectral scale.

PROVED retained round-13 check. In R13-C's sign notation z=2lambda-q delta, the full Boolean equation is z*z=q^2 delta in UNNORMALIZED convolution. Its recorded defect z*z(s)=q^2(1+o(1)) at s=2J+2 is exactly a failure of the global equation required for the centered recurrence. The round-13 archived finite support checks have defect/q^2 approximately 0.970244, 0.975111 and 0.980046. These are QUOTED prior data, not reruns or prime examples; their q were composite cubes. R13-M2 repairs only each fixed scalar order, and does not assert the pointwise two-valued inverse transform. No fake is silently upgraded to a Boolean set, and no claim of an improved exponent rests on information shared by those fakes.

## Bounded literature check, 2010-2026

PROVED source-verification scope. Checked the supplied Sanders v2 plus the exact theorem locations below, Sanders' author page, and bounded searches for Sanders/Chowla/density/prime/1/3 and later work. Some broad searches returned unrelated Chowla-conjecture material, which was discarded. This is a bounded check, not a priority proof. No source in this checked set gives a cyclic exponent strictly above 1/4 at every fixed density or a dense-integer exponent strictly above 1/4 for every C. No theorem that such an improvement is unknown in all literature is asserted.

PROVED (quoted). [Jin-Milojevic-Tomon-Zhang, arXiv:2509.03490v2, 27 October 2025, Theorem A.1](https://arxiv.org/html/2509.03490v2#A1): for every delta>0 and every gamma in (0,1/4), all sufficiently large finite groups Gamma have the property that A=A^(-1) and M_Gamma(A)<=|Gamma|^gamma imply |A symmetric-difference H|<=delta|Gamma| for some subgroup H. For gamma<1/6 it gives an error |Gamma|^(1-eta), where eta>0 is sufficiently small depending on gamma. In prime cyclic groups with density separated from 0 and 1, the first assertion gives exponent 1/4-epsilon, not a strict improvement above 1/4.

PROVED (quoted). [Bu et al., arXiv:2610.17160v1, Section 9.2 and Proposition 9.7](https://arxiv.org/html/2610.17160v1#S9.SS2): for EVERY C>=1 and n>=2, every A in [1,Cn] of size n satisfies

    M(A)^3 ||f_A||_1 >= (n-1)/(32 C C1),
    M(A) >= ((n-1)/(64 C C1))^(1/4),   C1=200000.

Its preceding discussion distinguishes Sanders' density-dependent exponent a/5 from the indicated half-set 1/3. This confirms the requested comparison but does not supply the omitted half-set accounting.

PROVED (quoted). [Bedert, arXiv:2509.05260v3, 24 July 2026, Theorem 1.1](https://arxiv.org/html/2509.05260v3#S1): every n-element positive integer set has M(A)>=n^(1/5-o(1)), asymptotically. [Shankar, arXiv:2609.05338v1, 4 September 2026, Theorem 1.1](https://arxiv.org/html/2609.05338v1#S1): there is an absolute c>0 such that M(A)>=c n^(1/5) for EVERY nonempty finite positive integer set. Both statements use the same cosine convention after x=2 pi t.

PROVED (quoted). [Yip, arXiv:2610.01657v2, 13 October 2026](https://arxiv.org/html/2610.01657v2), Theorem 1.7 (restated in Section 4), gives: for every epsilon>0 there is c(epsilon)>0 such that any n-vertex graph epsilon-far from all disjoint unions of cliques has least-eigenvalue magnitude at least c(epsilon)n^(1/4). Theorem 1.24 gives the all-integer bound -2 min f_A=Omega(n^(1/6.43)). These exact statements do not give the proposed exponent >1/4. Proposition 1.11's strengthened eigenvalue recursion uses a threshold at least the square of the least-eigenvalue magnitude; that improvement is already part of its stated quarter-power dense result.

## Completed finite checks

PROVED finite certificate scope. The exact input sets are symmetric, exclude 0 and have cardinalities within O(1) of q/4 or q/8. check_round14.py used Gurobi 13.0.3, seed 1914, four threads and a 12-second per-model limit, on every odd prime 5<=q<=61 (16 primes, 32 models). Every model returned status OPTIMAL. For q>31 this is only a NUMERICAL optimum of a floating-cosine model. For q<=31, a separate exhaustive enumeration with integer enclosures of 220-bit Arb cosines certifies the exact optimum, including cyclotomic equality checks for tied dilation orbits. There were 2860 enumerated candidates and 214 dilation orbits counting the few duplicated small-cardinality models. Numerical solver optimality is never used as an exact certificate.

PROVED independent verification. audit_round14.py reevaluated every saved spectrum from a separate cached cosine table at 256 bits. It checked trace and energy, K>=1, the saved minima, every finite optimum enclosure, rational centered identities, and the reciprocal-density order formula at m=3,...,100. Selected spectral minima/maxima with overlapping balls are checked for exact cyclotomic equality, rather than assuming overlapping intervals imply equality. The q=5 sharp Parseval inequality is equality and has a separate exact two-level certificate. Every other tested inequality has a positive Arb margin.

PROVED focused R14-FULL verification. test_fixed_order.py checked 38 exact interval/random symmetric sets at q=101,257,509, orders r=2,...,8 when the required density bound permits a nonempty set, and every positive frequency modulo conjugation: 2377 positive frequencies total. At 256-bit Arb precision, every complete deleted-atom expression divided by T exceeded 1/4 by a positive margin. Exact rational checks also verified A_r-r m_(r-1)>=1/2 for each parameter row. This finite check verifies the implementation of the derived expression; the theorem for all q,r,B rests on the paper proof.

NUMERICAL decimal summaries (each individual K is Arb-enclosed; optimum status as indicated):

| q | Target density | Actual cardinality | Minimum K, approximate | Optimum certificate |
|---:|---:|---:|---:|---|
| 17 | 1/4 | 4 | 2.247760251603 | Exhaustive exact enclosure |
| 17 | 1/8 | 2 | 1.965946199368 | Exhaustive exact enclosure |
| 31 | 1/4 | 8 | 3.036810894340 | Exhaustive exact enclosure |
| 31 | 1/8 | 4 | 2.249998296807 | Exhaustive exact enclosure |
| 41 | 1/4 | 10 | 3.164447961719 | Gurobi floating model only |
| 41 | 1/8 | 6 | 2.586083816801 | Gurobi floating model only |
| 61 | 1/4 | 16 | 3.711842481232 | Gurobi floating model only |
| 61 | 1/8 | 8 | 3.024203506456 | Gurobi floating model only |

NUMERICAL density-union probes. The independent Bernoulli-pair model of R14-UNION, with exact count repair, was tested at q=4093,65537,1048583. The quarter-density epsilon was 1/8; the eighth-density epsilon was 1/10. At the largest prime the quarter-density input had K_B approximately 1990.6060 and its union had lambda_C(2) approximately -4032.9677, compared with leading expectation -4096.0273. The eighth-density input had K_B approximately 1553.5961 and lambda_C(2) approximately -2377.2278, compared with -2621.4575. These largest-prime spectra are FFT evidence only. At q=65537 the quarter-density union's lambda_C(2) is independently Arb-certified near -262.396657778255. The other small samples include positive lambda_C(2) values (q=4093 quarter-density and q=65537 eighth-density); these fluctuations are retained in audit_results.json, not discarded. The infinite-prime conclusion rests on the bounded-difference paper proof, not finite extrapolation.

## Integer conclusion and bounded constants task

PROVED (quoted baseline plus elementary normalization). The unconditional exponent proved for every C in this report remains the quoted 1/4. The displayed Bu bound implies, for EVERY C>=1 and EVERY nonempty finite A in positive integers with max A<=C|A|,

    M(A) >= b(C)|A|^(1/4),
    b(C)=(128 C 200000)^(-1/4).

For n>=2 use n-1>=n/2; for n=1, M(A)=1 and b(C)<1. This is an explicit all-n corollary of a known bound, not a new dense result. The VM-enclosed values of b(C) are approximately 0.008359253812 (C=8), 0.007029266565 (C=16), and 0.005910885056 (C=32). The original (n-1)-version is slightly stronger.

PROVED scope of Task 2. Its premise, success of Task 1 with an exponent improvement, was not established, so no new c(C) at exponent 1/3 or any exponent >1/4 is extracted. There is consequently no numerical break-even claim. If a future proof yields M>=c(C)n^(1/3), comparison with b(C)n^(1/4) would give the rough threshold n>(b(C)/c(C))^12. That conditional algebra is not a quantitative bound here.

## Failed steps retained, novelty, and handoff

PROVED failed-step record:

| Proposed step | Exact reason it fails / replacement |
|---|---|
| U(0)=0 and offzero U*U=U imply U^(r)=U offzero | False already at r=3: U^(3)=(1+c)U+q c delta; q=17, B=+/-1 is an explicit witness. Use the full two-valued recurrence. |
| Project away zero at each multiplication and keep the usual binomial theorem | Projected convolution is nonassociative, even on even arrays in Z_5, as calculated above. |
| The fixed choice r=4 has a density-independent negative main term | At a=1/8 its coefficient is +11/18. At a=1/m the first favorable order grows as m, with the exact parity formula above. |
| g=2b-1 supplies a small-negative involution at every density | Its zero-frequency coefficient is -(1-2a)q at a<1/2. Positive truncation would have an error of order q. |
| A pointwise polynomial can fix both mean and involution | Every such polynomial still has two values; zero mean and equal nonzero squares force a=1/2. |
| Union with a fixed dilate raises density at negligible spectral cost | R14-UNION has K_B=O(sqrt(q log q)) but K_C>>q. Adaptive dilation choice is not excluded. |
| Soft half-density boosting can be rounded with a two-sided o(sqrt(q)) Fourier error | Its coefficient repair has squared mass >=q/32, forcing an absolute Fourier error of square-root order. A one-sided rounding theorem remains a different unproved claim. |
| The half-set cubic estimate Lambda=O(K^3) proves exponent 1/3 | Parseval gives Lambda>>q/K, so this yields only K^4>>q in the small-spectrum branch. Sanders' stated 1/3 is quoted; the missing independent branch is retained. |
| q in (2X,4X] always puts the embedding in the proposed density range | False for A={1,2}, q=5. Use q in (4X,8X]. |
| Separate c(a)>0 imply a constant for every C | A lower bound uniform on the required density interval must be proved or explicitly supplied. |

PROVED novelty accounting. Grepped .research/PROOFS.md before claiming new assemblies. Trace/Parseval, the norm bound, the prime embedding, Boolean convolution, the half-set citation and all round-13 fake properties are quoted/classical. The added work is R14-CENTER's explicit deleted-zero recurrence, its sharp reciprocal-density order and coefficient; R14-FULL's positive lower bound for the complete fixed-order expression at small density; the even-array projected-associativity counterexample; R14-UNION's use of a genuine R13-PK-shaped family to obstruct fixed-dilation density boosting; the soft-rounding absolute-error obstruction; the quantified transfer correction; and the new finite data/certificates. These are new to this round's record; external priority is not claimed. No unconditional exponent advance is claimed.

PROVED reproducibility. All mathematical/PDF extraction and rendering computation ran through the prescribed VM wrapper from bash, at at most four cores. No LP/MILP/QP solver other than Gurobi was used. The final scripts, data, exact pair lists, source PDF and SHA256 manifest are in tdense14_scratch/; the initial verifier equality failure and its correction are retained in the report. No commits or subagents were launched, and no .research/*.md files were edited. Existing unrelated workspace changes were preserved.

```bash
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -t 600 python .research/agents/tdense14_scratch/check_round14.py
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -t 300 python .research/agents/tdense14_scratch/audit_round14.py
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -t 120 python .research/agents/tdense14_scratch/test_fixed_order.py
```

PROVED artifact map: check_round14.py and small_q_results.json contain all models and exact finite optimum data; algebra_results.json contains the symbolic coefficients; audit_round14.py and audit_results.json contain the independent spectrum checks, exact order checks, and retained union fluctuations; test_fixed_order.py and fixed_order_test.json contain the focused R14-FULL checks; union_q*_den*.npz store the exact pair lists; manifest.json records source/data hashes. Python 3.12.3, NumPy 2.5.4, Gurobi 13.0.3 and python-flint/Arb were used. PDF rendering/extraction used PyMuPDF on the VM.

HEURISTIC final strategic decision. Stop the direct centered fixed-order transfer and the fixed-dilate/soft-rounding boosts tested here: their failures are now precise mathematical artifacts. Three distinct directions remain for a subsequent round: (1) independently recover Sanders' half-set 1/3 in the all-small-spectrum branch before proposing a density extension; (2) seek an adaptive Boolean density boost with a proved one-sided Fourier estimate, testing it first against R14-UNION's cosine profiles; (3) use full-frequency convolution or growing-degree Galois constraints rather than R13-C/M2's retained scalar information. The first discriminating derivation is to identify a small-spectrum estimate that yields K^3>>q at half density; replacing it with the already checked Lambda<<K^3 repeats the quarter-power calculation and is not progress.
