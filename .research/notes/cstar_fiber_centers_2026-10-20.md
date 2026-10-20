# Small fibers, an exact mean identity, and amplified center fluctuations

2026-10-20. DESIGN / ATTACK LOG, with a probabilistic paper theorem. Previous turn: progress; a Boolean radial realization was constructed and its large coherent fiber was excluded. This pass actually removes those large fibers. The result below concerns independent whole-fiber center choices, not arbitrary correlated selectors or full Chowla. No novelty, external audit or Lean verification is claimed.

## 1. Precise random family and conclusion

Let X tend to infinity through positive integers. Take all primitive u in Z^2 modulo sign with

    X^(1/2)<=||u||<=X^(5/8).

Put R_u=X/||u|| and B_R={z in Z^2:||z||<=R}. Independently for each u choose an integer center T_u uniformly from B_(R_u). Retain every nonzero w with T_u+w and T_u-w both in B_(R_u), and form M=u w^T. The support is symmetric and the primitive factorization is unique. Let n count its sign-pairs.

Use the injective encoding h=6X^3+(1,3,5,7), P=product h_i, C_i=P/h_i, taking positive absolute encodings. All selected matrices have Frobenius norm at most X by the parallelogram identity. Thus the encoding gives a genuine set A of distinct positive integer frequencies whenever n>0.

Choose alpha in (19/5,39/10) with F_disk(alpha)=0, and put tau=2alpha. Such a root exists by exact alternating-series endpoint signs. The same rational polynomial/Bernstein check proves F_disk(tau)>1/100 for EVERY such root. Define the real lens transform

    g(t,e)=integral_{||t+z||<=1, ||t-z||<=1} cos(tau e.z) dz,
    v_tau=(1/pi)integral_(||t||<=1) g(t,e)^2 dt.

Rotational symmetry makes v_tau independent of the unit vector e. It is positive, quantitatively

    v_tau>=pi^2/(200^2*400^2)>0.

**Paper theorem.** The family satisfies

    n/[(3/32)X^2 log X] ->1 in probability.

At the isoclinic matrix phase tau I/X, write the symmetric Fourier sum as D_X (so the corresponding cosine sum is D_X/2). Then

    E D_X=O(X^(5/4)),
    Var(D_X)~(3v_tau/pi)X^3,
    (D_X-E D_X)/sqrt(Var D_X) -> standard normal in distribution.

The same statements about the normalized phase value hold at a nearby EXACT scalar CRT angle, with an additive error O(log X). Put mu_X=(3/32)X^2 log X. There is an absolute c>0 such that, for every fixed epsilon>0,

    liminf Pr[n>0, M(A)>=c X^(3/2), |n/mu_X-1|<=epsilon]
       >=Phi(-1)>0.

More precisely the simultaneous cardinality event can be taken to have probability tending to one, and the negative-point event at one standard deviation has probability tending to the standard normal lower tail at -1. For every fixed B>0,

    liminf Pr[n>0 and M(A)>B sqrt(n)]>=1/2.

This says independent whole-fiber centers have a substantial chance of an amplified failure even after EVERY individual fiber has size O(X), below sqrt(n) by a logarithmic factor. It is NOT a proof that every sample fails, that failure probability tends to one, or that dependent center choices cannot succeed.

## 2. Why the mean is small: exact parity autocorrelation

For one fiber set q=tau e/R, and

    Z_R(T)=sum_(w!=0, T+/-w in B_R) cos(q.w).

Partition B_R into its four coordinate-parity classes B_(R,r). Because the disk is convex, if x,y belong to the same parity class, T=(x+y)/2 is an integer point of B_R and w=(x-y)/2 is integral. Conversely every allowed (T,w) gives such a pair. Thus exactly

    1+E_T Z_R(T)
       =(1/|B_R|)sum_(r mod 2)
          |sum_(z in B_(R,r)) exp(i q.z/2)|^2.

This identity includes all ordered pairs and both signs of w; the omitted origin contributes precisely 1. It is not a model based on independent coefficient selectors.

### Strengthening: the negative mean persists under every same-marginal coupling

The O(1) estimate below can be sharpened to

    E Z_R=-1+O(R^(-2/3)),
    E D_X=-m_X+o(m_X),    m_X=number of u~(3/pi)X^(5/4).

This uses only the individual marginals, NOT independence. Here is the needed weighted disk estimate rather than an unsupported appeal to a lattice-point bound. For any parity coset, at beta=(alpha/R)e, the disk's main integral vanishes and

    sum_(z in B_R intersect (2Z^2+r)) exp(i beta.z)=O(R^(2/3)),

uniformly in unit e. To prove it, choose a nonnegative smooth unit-mass bump of physical support delta=R^(-1/3), and smooth the disk indicator. The Fourier transform of a radius-R disk at nonzero frequency xi is O(R^(1/2)||xi||^(-3/2)), from J1(s)=O(s^(-1/2)) for real large s; the precise standard asymptotic used is [NIST DLMF 10.17.3](https://dlmf.nist.gov/10.17.E3), fixed order nu=1 and positive real argument.

Poisson summation on the parity coset gives a zero main term at beta and nonzero terms bounded by

    O(R^(1/2) sum_(k!=0)||k||^(-3/2)(1+delta||k||)^(-N))
       =O(R^(1/2)delta^(-1/2)).

The nonsmoothed and smoothed indicators differ only in a delta boundary strip. Pointwise its absolute difference is bounded by the difference of radius-(R+2delta) and radius-(R-2delta) smoothed disks. Applying the unweighted Poisson bound to these two disks bounds the strip's coset count by O(R delta+R^(1/2)delta^(-1/2)). The phase factor has modulus one, so the same controls the weighted error. With delta=R^(-1/3), both terms are O(R^(2/3)). The finitely many small R are absorbed into the constant. This argument needs no unproved cancellation among lattice points and is uniform for alpha in the fixed compact root interval.

Squaring those O(R^(2/3)) parity sums and dividing by |B_R| of order R^2 yields the stated O(R^(-2/3)) remainder in the exact parity identity. Since min R>=X^(3/8), it is uniformly o(1) across the fibers. The scalar CRT transfer costs only O(log X) and does not change the leading negative mean.

Now allow ANY joint distribution of Boolean frequency choices with the SAME coefficient marginals as the independent-center model; individual outputs need not even be complete lenses. Expectation of the cosine sum is fixed by those marginals. Hence

    E M(A)>=-E f_A(theta_X)~m_X/2.

Every output has n<=n_max, where the support of all possible fibers has n_max~(3/8)X^2 log X. Set M=R=0 on an empty output, merely to define these expectations. Since R>=M/sqrt(n_max),

    E R(A)>=c X^(1/4)/sqrt(log X) ->infinity

for EVERY such coupling. In particular no same-marginal distribution can be supported entirely on bounded-ratio outputs. This expectation obstruction does NOT imply a positive limiting failure probability without independence: rare very bad outputs can dominate expectation. Nor does it exclude a good deterministic assignment obtained by conditioning and thereby changing the marginals. The independent-center CLT above is a separate, stronger probability statement under its extra hypothesis.

This exposes a cost in the proposed mean profile itself: each positive plane autocorrelation loses its origin coefficient, contributing a -1 term, and the isoclinic zero makes their positive square terms small simultaneously. A nonnegative normalized macroscopic front had hidden that accumulated cost. Correlation preserving the mean cannot erase it.

The exact parity squares also give f_mean(theta)>=-m_X/2 at EVERY scalar angle. Together with the negative point this proves the GLOBAL fractional-mean statement M(mean profile)~m_X/2, not merely a lower estimate for a random realization. This is an instance of the existing positive-Gram origin cost, now shown to be asymptotically sharp on this specific profile.

### A growing phase survives activation and staggered radii

Staggering the disk radii removes a common fixed zero but does not remove the origin-cost obstruction. Fix any a>0. For each u in the same range, allow ANY predetermined scale sigma_u in [a,1] and put R_u=sigma_u X/||u||. Activate the fiber with any probability lambda_u in [0,1]; conditional on activation its integer center is uniform in B_(R_u). All activation/center choices may be dependent.

Use the GROWING isoclinic matrix phase

    Y_X=t_X I,   t_X=X^(17/48).

The half-frequency beta in a parity sum has magnitude sigma_u t_X/(2R_u)=t_X||u||/(2X)=O(X^(-1/48)). Thus the same Poisson/smoothing bound is uniform, while the now nonzero main disk integral satisfies

    |parity sum|<=C_a[R_u^2 t_X^(-3/2)+R_u^(2/3)].

Here the large real disk transform decays as t^(-3/2), from the same verified fixed-order Bessel asymptotic. Squaring and dividing by |B_R| gives

    0<=1+E Z_u<=C_a[R_u^2 t_X^(-3)+R_u^(-2/3)]
       <=C_a[X^(-1/16)+X^(-1/4)] ->0,

uniformly over ALL chosen radii and directions. If s_X=sum lambda_u>0, linearity therefore gives E D=-s_X+o(s_X), irrespective of dependence or thinning. The scalar CRT error in expectation is o(s_X): each phase error is O(X^(-2)), and E n<=7X s_X. Consequently the mean polynomial has the sharp global budget

    M(mean profile)~s_X/2.

The upper bound s_X/2 is exact from the positive parity squares, and the lower bound comes from this mesoscopic phase. This statement is uniform in the activation weights and radius staggering for a fixed lower scale a. It is not a theorem for unrelated smooth windows.

There is also a quantitative tradeoff for a GUARANTEED sampler in this architecture. Suppose every output is made of these whole lens fibers, and for some N_X>=1 every output has N_X<=n<=2N_X. For all sufficiently large X (depending only on a), such a law cannot have M<=sqrt(n)/300 on EVERY output. Proof: write epsilon for a claimed uniform ratio. The mean bound gives E M>=s_X/4, whereas a claimed guarantee gives E M<=epsilon sqrt(2N_X), so s_X<=4epsilon sqrt(2N_X). For every u with lambda_u>0 the event of activation and center zero has positive probability. On that event the complete disk fiber is isolated by the preceding Fejer lemma, yielding M>=R_u^2/1024 once min R is large. The guarantee would force R_u^2<=1024epsilon sqrt(2N_X) for every such u. Finally each fiber has at most 7R_u^2 sign-pairs, so

    N_X<=E n<=7sum lambda_u R_u^2
       <=57344 epsilon^2 N_X.

But 57344/300^2<1, a contradiction. This rules out an all-output vanishing-ratio guarantee for this precise, size-comparable, prescribed-marginal whole-fiber sampler class, even with arbitrary dependence, thinning and bounded radius staggering. It does NOT prove a lower bound for each individual deterministic lens assignment, exclude rare good outputs or rejection schemes that change marginals, or establish full Chowla.

A mesh-two disk Riemann sum gives, uniformly in the direction e,

    sum_(z in B_(R,r)) exp(i q.z/2)
      =(pi R^2/4)F_disk(tau/2)+O(R)=O(R).

Since |B_R| is of order R^2, the exact square identity yields E Z_R=O(1), uniformly for R>=1. A direct unsquared Riemann error would only give O(R), which is too large for the argument below. This improvement is essential. There are O(X^(5/4)) u-fibers, giving the asserted total mean bound.

The same identity at q=0 gives

    E number_of_nonzero_w
       =(sum_r |B_(R,r)|^2)/|B_R|-1
       =(pi/4)R^2+O(R).

The primitive harmonic count is

    sum_(X^(1/2)<=||u||<=X^(5/8)) 1/||u||^2
      =(3/(4pi))log X+o(log X).

Multiplying by pi X^2/4 and dividing by two for sign-pairs gives E n~(3/32)X^2 log X. All constants use canonical u and both w signs; no multiplicities enter A.

## 3. Variance, positivity and the triangular-array theorem

Uniform convex-boundary comparison gives

    Z_R(T)/R^2 = g(T/R,e)+O(1/R),

uniformly in T in B_R and unit e. Riemann sums over T/R in the unit disk converge uniformly in e, since the lens transform is jointly continuous and bounded on this compact parameter set. The continuous-center mean is exactly

    (1/pi)integral g(t,e)dt
      =(pi/4)F_disk(tau/2)^2=0.

This follows by x=t+z, y=t-z, whose four-dimensional Jacobian is 1/4. Therefore Var Z_R=(v_tau+o(1))R^4, uniformly in direction.

To prove v_tau>0 rather than assume nondegeneracy, at t=0,

    g(0,e)=pi F_disk(tau)>pi/100.

The lens contains the disk of radius 1-||t|| and is contained in the unit disk, so |g(t,e)-g(0,e)|<=2pi||t||. For ||t||<=1/400 this gives g>=pi/200. That region has probability 1/400^2 under the uniform unit-disk center, proving the explicit lower bound above.

The primitive harmonic fourth-power sum satisfies

    sum_u ||u||^(-4)~(3/pi)X^(-1),
    sum_u ||u||^(-6)=O(X^(-2)).

Since the smallest R tends to infinity, independence now gives Var D~(3v_tau/pi)X^3. Every centered summand is bounded by O(R_u^2), hence

    sum_u E|Z_u-E Z_u|^3 / (Var D)^(3/2)
       <= O(X^6 sum_u ||u||^(-6)/X^(9/2))
       =O(X^(-1/2)) ->0.

This is Lyapunov's sufficient condition. Equivalently the largest normalized summand is O(X^(-1/2)), so Lindeberg's condition is automatic. The exact triangular-array theorem used is Dembo's [Probability Theory notes, September 2010, Theorem 3.1.3, p. 96](https://stanford.edu/~montanar/TEACHING/Stat310A/lnotes.pdf#page=96), checked at the source: within-row independence, zero means, variance sum tending to one, and vanishing truncated variance. No independence between different X rows is needed.

Also Var n=O(sum R_u^4)=O(X^3), so Chebyshev proves the asserted cardinality concentration. Since E D/sqrt(Var D)=O(X^(-1/4)), the mean shift vanishes. This proves the stated normal limit and negative-point probabilities. It does not establish the distribution of the GLOBAL minimum.

## 4. Transfer to actual integer cosine sums

Round the four entries of h_i(tau I)_i/(2pi X) to integers k_i, and choose j=k_i mod h_i by CRT. The scalar angle theta=2pi j/P induces coefficient phases 2pi k_i/h_i. Their Frobenius distance from tau I/X is O(X^(-3)). Every matrix has norm<=X, so its phase error is O(X^(-2)). The deterministic full-cone cardinality bound N=O(X^2 log X) gives a total error O(log X), negligible relative to X^(3/2). Thus the CLT-derived negative value occurs at a genuine scalar angle as claimed.

For every fixed B, the threshold 2B sqrt(n)/sqrt(Var D) tends to zero in probability; the normal law has no atom at zero. The probability that this ONE point certifies M>B sqrt(n) tends to 1/2. The global M can only be larger, giving the liminf result, not equality for the global event.

## 5. Finite tests and the correlated escape test

src/cstar_fiber_centers.py enumerates the exact integer disk/lens incidence relation for X=64,128,256. It checks the parity square identity numerically in every fiber, computes full finite center-population means/variances and third-moment diagnostics, and samples 96 independent choices per X with seed 20261026. These distribution diagnostics use floating arithmetic and are not statistical proofs of the asymptotic theorem. A selected negative sample is exported by its center choices and verified with Arb at its exact CRT root; those lower certificates are rigorous.

src/cstar_correlated_centers.py changes the mechanism: at X=64 it uses Gurobi to choose one center per fiber, fixes cardinality near the exact independent mean, and first controls eight isoclinic zero phases. Each fiber has at most 12 distinct lens options in this bounded experiment. After each choice a separate search attacks other matrix phases; a missed negative point is appended for the next round. Solver claims are numerical. Arb separately certifies the ACTUAL finite floors at listed scalar CRT angles and the missed negative point. A finite floor is never called an all-circle upper bound for M.

The two experiments discriminate independence from correlation. Even successful suppression of the eight predicted fluctuation phases would not refute the independent-center theorem, and failure of three finite correlated choices would not exclude every correlated construction.

## 6. Analytic correlated countercontrol: the entire zero circle can be repaired

The dependence caveat is mathematically necessary, beyond the finite Gurobi experiment. Use the SAME u range and the SAME allowed integer-center/lens mechanism. Retain a full disk fiber exactly when

    u mod 5 belongs to S={+/-(1,0),+/-(0,1),+/-(1,1)}.

Set T_u=0 for those u. For every other u choose the lexicographically largest point of B_(R_u). That point is an extreme point of the disk's integer convex hull: if T+/-w are both in the disk, maximal first coordinate forces w_1=0, then maximal second coordinate forces w_2=0. Thus its nonzero lens fiber is EMPTY. This is a valid deterministic correlated center assignment.

It preserves the LEADING CARDINALITY, but it changes the radial coefficient marginals. The finite Gurobi repairs also constrain cardinality rather than those marginals. Neither is a counterexample to the same-marginal expectation obstruction above.

The six selected nonzero residue classes have primitive harmonic density 6/(5^2-1)=1/4. To see the uniform residue density directly, apply Mobius inversion separately to each nonzero class: only divisors coprime to 5 contribute, each invertibly permutes the classes, and the leading density is (1/25)sum_(5 not dividing d)mu(d)/d^2=(6/pi^2)/24. Sector boundary errors remain O(T log T). The selected classes are closed under sign, so the canonical-u convention preserves the same fraction. It follows that this deterministic family's cardinality is AGAIN

    n~(3/32)X^2 log X.

For ANY fixed t and ANY planar rotation R_phi, disk-fiber Riemann sums give, uniformly in phi,

    f_matrix(t R_phi/X)/n ->F_disk(t).

The phase magnitude in the u-fiber is t/R_u, independent of its direction; the total error is O_t(sum R_u)=O_t(X^(13/8))=o(n). Thus no angular equidistribution assumption is needed for this transform statement. Since F_disk(tau)>1/100, the ENTIRE isoclinic zero circle from the independent mean is positive for this correlated family, eventually uniformly in phi. It is not enough to add more rotation angles to that same circle.

A different phase still kills this explicit assignment: F_disk(5)<-1/8, already checked by an exact alternating-series upper bound, so the scalar CRT transfer gives M(A)>=n/16 eventually. This is a correlated escape from the specific zero-circle fluctuation mechanism and a separate paper exclusion of that escape; it is not a construction with small Chowla ratio. Arbitrary nontrivial lens choices are not classified by this argument.

## 7. Verification, repair record and strategic decision

Numerical independent-center diagnostics at X=64,128,256 give variance/X^3 approximately 0.00961,0.00984,0.01014; the normalized third-moment ratios decrease from0.1727 to0.1128 to0.0745. The negative means are still substantial at these finite sizes, so 94,94,93 negative samples out of96 are not presented as estimates of the asymptotic probability1/2. Selected samples have rigorous point ratios>2.6182,3.3424,4.8221.

At X=64 Gurobi used116 fibers, at most12 options per fiber, and fixed n=1599. Three rounds suppress8,9,10 listed exact CRT phases to f>=-1/1000000, yet separate searches give certified missed-point ratios>1.8052,2.1552,1.8608. These are finite surrogate repairs, not global upper certificates. The full/empty congruence examples have n=1376,6984,32720; their eight tested zero-circle values are positive, but the t=5 certificates give ratios>5.1019,11.3456,24.3083. The paper uniform-circle statement has a separate asymptotic proof.

The independent verifier caught a producer serialization bug: appending new targets mutated historical target lists. The saved8/9/10 value-ball counts identified the intended original prefixes. The producer now copies each list; the saved lists were restored, with original/corrected counts recorded in correlated.json. No candidates were reoptimized or negative points removed. Every restored floor was then rechecked independently. This prevents the unsupported interpretation that an earlier repaired candidate also controlled later discovered bad angles.

src/cstar_fiber_centers_verify.py imports no producer code. It re-enumerates primitive directions and disk centers in another order, reconstructs selected lenses by endpoint pairs rather than a center-window incidence table, checks exact parity coefficient counts, and matches set hashes. It uses exact Sturm rather than producer Bernstein to check the doubled-root disk sign. At192-bit Arb it rechecks every saved negative point, all finite correlated floors, and the deterministic countercontrol values. Direct parity-square evaluations also give rigorous mean-D upper bounds -108.070818,-279.164489,-715.059694. These imply finite expectation bounds for ANY coupling with the original coefficient marginals; they do not bound each output. The fractional mean itself has the exact all-circle upper budget m/2. Verifier versions and rational bounds are retained.

Reproduce:

    src/dirun.sh -c 2 -m 8 -t 240 python src/cstar_fiber_centers.py
    src/dirun.sh -c 2 -m 8 -t 180 python src/cstar_correlated_centers.py
    src/dirun.sh -c 2 -m 8 -t 180 python src/cstar_center_countercontrol.py
    src/dirun.sh -c 2 -m 8 -t 240 python src/cstar_fiber_centers_verify.py

Data: experiments/fiber_centers_2026-10-20/{independent,correlated,countercontrol,verification}.json. All research computation ran on Dirichlet. The mathematical mean/CLT/activation statements are paper arguments; finite simulation or MIP status is not their proof. The required reviewer launch again failed with the unavailable configured default; no independent-agent or Lean audit completed. All jobs are terminal.

**Global review.** Removing the old large-fiber hypothesis was a real change. Independence produces amplified fluctuations, but the sharper result is that the proposed mean profile itself has budget s/2, even after bounded radius staggering and activation in this scale range. Stop treating correlation with those fixed marginals as a way to erase that budget. The same-marginal expectation bound is not a deterministic Chowla theorem; the finite repairs deliberately change marginals, and their missed phases show why finite zero constraints are insufficient.

The growing-phase proof uses a concrete scale gap: R_max^(2/3)<<R_min, allowing t between those scales and below the first lattice aliases. A discriminating next profile test is to widen the u range to X^(1/2)<=||u||<=X^(3/4) AND stagger radii. Then R_min~X^(1/4) is below R_max^(2/3)~X^(1/3), so this uniform mesoscopic-hole proof does not apply. One must test the actual fractional mean BEFORE optimizing another Boolean rounding; no success or exclusion outside the scale gap is claimed. Keep the unrestricted torsion-free mixed-certificate and growing-depth non-cone PD/Riesz lines active. Full Chowla remains open; no universal exponent improvement or quantified counterexample algorithm is claimed.
