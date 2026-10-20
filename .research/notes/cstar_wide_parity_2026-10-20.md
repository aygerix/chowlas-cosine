# Widening, center-law repair, and a deterministic residue obstruction

2026-10-20. CSTAR DESIGN / CHAIN(c) / ATTACK LOG. Full Chowla remains
OPEN. This is a research record of scoped results, not a manuscript.
The strongest advance here excludes arbitrary selections in a truncated
integer-cone model under the stated phase-rich encoding. It does not
prove a bound for arbitrary positive-integer frequency sets.

## 1. The promised wider-scale test was performed

Take primitive canonical integer vectors u with
sqrt(X)<=||u||<=V=floor(X^(3/4)). In each fiber choose a disk of radius
R_u=sigma_u X/||u||, sigma_u in {1,3/4,1/2}. Its integer center T is
uniform in B_R={z in Z^2:||z||<=R}. The selected nonzero w satisfy
T+w,T-w in B_R. Select one representative of each sign pair M=u w^T;
the full support is symmetric and has ||M||<=X. Write D=2f, n=|A|,
M(A)=-min f_A, and use M(mean) for -min E f_A, not E M(A).

The previous common mesoscopic-window proof requires a scale gap that
this choice removes. Both cyclic radius choices and per-fiber radius
choices maximizing a transposed-plane Gaussian test were actually run.
All six exact fractional means still have negative positive-measure
certificates. At X=4096, V=512 the heat lower bounds are >29071 and
>7046 respectively. These are global LOWER bounds on M(mean), not
upper certificates for any Boolean output.

The test is a product of positive periodic Gaussian kernels

    G_m(t)=sum_r exp(-r^2/(2m^2)) exp(irt)
          =sqrt(2pi)m sum_l exp(-m^2(t-2pi l)^2/2)>=0,
    measure(theta)=G_m(C11 theta-5/V) G_m(C21 theta), m=4V.

Its main Fourier contribution to D isolates w parallel to e1. For an
integer disk with q=floor(R^2), r=floor(R), and column lengths
c_j=2 floor(sqrt(q-j^2))+1, its exact axis coefficient numerator is
c_k+2 sum_(j>k)c_j. The saved main integral is the sum of twice this
coefficient times exp(-k^2||u||^2/(2m^2)) cos(5 k u1/V).

Here h_i=6X^3+(1,3,5,7), P=product h_i, C_i=P/h_i. A nonzero encoding
kernel vector has norm>=min h_i, so all unwanted aliases have plane
coordinate norm>=r0=min h_i-X. Since r0^2>=400m^2, their absolute sum
is at most 25(m+1)^2 exp(-100)<25(m+1)^2/2^100=:t. The lattice Gaussian
sum bound follows from one-dimensional sum-integral comparison. The
measure's mean lies in [1-t,1+t]. The saved rational B is accepted only
when the Arb inequality H+t+2B(1+t)<0 holds. Thus M(mean)>B. The verifier
uses direct row intersections, a different summation order, and 192 bits.

The primitive-ray boundary transform proposed in ROUTES is secondary:
these finite certificates suffice for the failed wider-scale test. No
unverified asymptotic transpose theorem is needed for the results below.

## 2. An elementary parity bound with no scale-gap assumption

For any R>=1, let b=|B_R| and Z_T(v)=sum_(w!=0,T+-w in B_R)(-1)^(v.w).
The endpoint substitution z=T+w,z'=T-w gives EXACTLY

    1+E Z_T(v)=(1/b) sum_(r mod2)
                 |sum_(z in B_R cap(2Z^2+r)) i^(v.z)|^2.       (1)

For v=(1,0), reflection in the first coordinate cancels every class
with odd first coordinate. On each horizontal row the even-coordinate
alternating sum is +1 or -1. There are r and r+1 rows of the two
parities, r=floor R. Hence the numerator in (1) is at most
r^2+(r+1)^2. The disk contains the integer diamond of radius r, with
2r^2+2r+1 points, so E Z_T(1,0)<=0. Rotation gives E Z_T(0,1)<=0.

For v=(1,1), reflection cancels all but the even-even class. Its sum
has absolute value at most the number of even rows, at most r+1.
For r>=1,

    numerator/b <= (r+1)^2/(2r^2+2r+1) <= 4/5,

where the final inequality is equivalent to (3r+1)(r-1)>=0. Thus

    E Z_T(1,0)<=0, E Z_T(0,1)<=0, E Z_T(1,1)<=-1/5.             (2)

The six binary invertible matrices A send every nonzero u mod2 to each
nonzero v=A^T u exactly twice. Primitive u is nonzero mod2. At the
physical matrix phase pi A, (2) therefore gives an averaged contribution
<=-1/15 per active fiber. With arbitrary activation probabilities lambda_u,
conditional uniform disk-center marginals, and arbitrary dependence, put
s=sum lambda_u. Some one of the six phases has E D<=-s/15, hence

    M(mean)>=s/30 on the four-torus.                            (3)

No lower radius beyond R>=1, angular regularity, growing radius,
independence, or bounded radius staggering is required. Equation (1)
also gives the global upper budget M(mean)<=s/2.

For scalar frequencies take h_i=6000X^3+(1,3,5,7) and C_i=P/h_i.
Pairwise coprimality follows from the differences 2,4,6 and the first
and last entries being 1 mod3. The kernel gap gives injectivity on the
radius-X ball. CRT residues approximating pi A have coordinate errors
<=pi/h_min. Each encoded cosine changes by <=2pi X/h_min; D changes
in expectation by <=4pi X mu/h_min, mu=E n. Since
mu<=7 sum lambda_u R_u^2<=7 X^2 s, this is <s/30. Consequently

    s/60 <= M(mean) <= s/2                                    (4)

for all integer X>=1 and all radii 1<=R_u<=X/||u||. The actual finite
certificates retain the original h=6X^3+odd and use the actual mass upper
bound with 4pi<88/7, so they do not rely on this larger-modulus estimate.
At X=4096 the certified parity ratios M(mean)/sqrt(E n) exceed 28.878
(cyclic) and 38.118 (heat-adversarial radii). Even near-linear
V=X/ceil(log2(log2 X)), with radii chosen to resist the six-phase average,
the certified ratios exceed 12.125,25.772,89.788 for X=256,1024,4096.
These are fractional-mean ratios, not ratios of particular Boolean sets.
Convexity gives E M(A)>=M(mean) for every coupling with those coefficient
marginals. Since every output has n<=n_max, the saved expectation ratio
bound is M(mean)/sqrt(n_max), taking the empty output's ratio as zero.
Neither assertion yields a bound for each individual outcome.

One consequence of (4) plus the earlier complete-fiber isolation lemma
is a broader GUARANTEED-sampler exclusion: if every output has
N<=n<=2N and M<=epsilon sqrt(n), conditional centers are uniform when
activated, and the fibers are whole lenses, then for N>=10^20 such a
law cannot have epsilon=1/2000. Indeed s<=60epsilon sqrt(2N). For every
active fiber with R>=R0=100000, the positive-probability event T=0 forces
R^2<=1024epsilon sqrt(2N), by the Fejer isolation lemma; the larger
moduli still give its required kernel gap. The other fibers have
R^2<R0^2. Thus

    N <= 420epsilon R0^2 sqrt(2N)+860160epsilon^2 N.

For N>=R0^4 the right side divided by N is at most
630epsilon+860160epsilon^2<1 at epsilon=1/2000. This statement concerns
an all-output guarantee with prescribed marginals; it does not exclude
each individual outcome or laws changed by rejection/conditioning.

## 3. Changing the center law really does repair parity

Before declaring all center assignments impossible, a different model
was tested. For each R=8,16,32 Gurobi chooses a D4-symmetric probability
law on integer disk centers, with exactly the same expected sign-pair
count as the uniform law. The maximum attainable common parity floors
are approximately 1.223,6.099,6.985 for D. Thus the uniform-marginal
assumption of (2) is essential. The subsequently optimized laws have
all three nonzero parity values exactly nonnegative after rational
reconstruction, with expected sizes

    4758/197, 79054/797, 1285672/3209.

A 561-point triangular two-torus grid was then optimized with repaired
parity. Independent adversarial minimization found other points, with
192-bit checked M(mean) lower bounds >0.4871,0.4888,0.4535. These do not
claim global upper bounds, an asymptotic lower bound for all center
laws, or a Boolean construction. They demonstrate a genuine escape
from the six parity targets at fixed mass. All rational probability
laws and point witnesses are saved. An independent checker reconstructs
their coefficients from endpoint pairs rather than lens membership.

## 4. A stronger deterministic obstruction: invertible residue phases

**Statement.** Let X,B be positive integers, 1<=B<=X. Let S be any
finite symmetric set of nonzero integer rank-one 2x2 matrices with
||M||<=X. Write each as u w^T with primitive canonical u, and suppose
||w||<=B. With the scalar encoding h_i=6000X^3+(1,3,5,7) above, the
absolute encodings of sign pairs form a genuine set A of n=|S|/2
distinct positive integers, and

    M(A)>=n/(8B^2).                                           (5)

No complete fibers, centers, coefficient marginals, angular shape, or
independence are assumed. This is stronger in scope than (4).

**Proof.** Choose a prime B<p<=2B, using p=2 at B=1 and Bertrand's
postulate otherwise. Every M is nonzero of rank one modulo p:
primitive u is nonzero modulo p, and 0<||w||<=B<p prevents w=0 modulo p.
For H uniform on GL2(F_p), H^T u is uniform on F_p^2 minus {0}. Hence

    E_H exp(2pi i <H,u w^T>/p)
       =(1/(p^2-1)) sum_(v!=0) exp(2pi i v.w/p)
       =-1/(p^2-1).                                          (6)

Thus the positive average of f over these four-dimensional phases is
-n/(p^2-1). Approximate H_i/p by k_i/h_i with error <=1/(2h_i), and take
the scalar CRT point theta=2pi j/P with j=k_i mod h_i. The coordinate
phase error has Euclidean norm <=2pi/h_min, so the cosine error for
every M is <=2pi X/h_min. Averaging the scalar points proves

    M(A)>=n/(p^2-1)-2pi Xn/h_min.                              (7)

Since p<=2B, the first term is >=n/(4B^2). Because B<=X and
h_min>6000X^3, the error is <n/(8B^2), proving (5). Injectivity and the
absence of zero encodings follow from the kernel gap already proved.

In particular ||u||>=sqrt(X) implies ||w||<=sqrt(X). With
B=ceil(sqrt X)<=2sqrt X,

    M(A)>=n/(32X),    R(A)>=sqrt(n)/(32X).                     (8)

The original h_i=6X^3+odd also suffice for (8) when X>=64: the error
bound needed above follows from 16pi X B^2<=64pi X^2<6X^3.
Therefore EVERY such truncated-cone family with n/X^2->infinity has
R(A)->infinity under these encodings. In particular arbitrary
nonuniform, correlated, or non-lens selections cannot turn its
logarithmic count surplus into a Chowla counteralgorithm.

**Essential scope controls.** A zero residue matrix averages +1 in (6),
and rank-two residues average +1/((p^2-1)(p-1)). Neither may be included
in the negative class. More generally, if n_p sign pairs are zero
modulo p, the four-torus f average is (p^2 n_p-n)/(p^2-1), giving a
content-divisibility correction, not (5). For arbitrary scalar
encodings these simultaneous matrix phases may be unavailable.
Nor can an arbitrary integer-frequency set be assumed to have this
rank-one representation with B=O(sqrt X).

For the rank-two control, invertible changes of variables reduce to
sum_H exp(2pi i tr H/p). Fix the first column a!=0 and sum the second
column outside span(a). Subtracting that span from the full column sum
leaves -p when a2=0, and zero otherwise. Then sum_(a1!=0) exp(2pi i a1/p)
=-1 gives total p, hence the stated positive normalized average.

Two deliberately incomplete-fiber Boolean examples at X=16,64 retain
only (3u1+5u2+7w1+11w2+u1w2) mod5 outside {0,1}. They have n=592,15320
and distinct positive encodings, with saved SHA256 hashes and generator.
Their scalar points have certified R>3.8315,3.9424. Direct encoded-scalar
and matrix-residue Arb evaluations agree. These test the CRT transfer
on actual sets; they are not all-phase upper certificates or submissions.

## 5. Verification and strategic review

- `src/cstar_wide_mean.py`, `src/cstar_parity_mean.py` produce the saved
  six widened and three near-linear means. The independent
  `src/cstar_wide_mean_verify.py` uses row counts, alternating row sums,
  reverse traversal, SHA256 checks, and 192-bit Arb; all nine pass,
  including all q=1,...,4096 elementary disk inequalities.
- `src/cstar_center_law_lp.py` is the new-marginal Gurobi probe. Its
  rational laws preserve mass exactly; its grids are only numerical
  objectives. `src/cstar_residue_mean_verify.py` reconstructs them
  independently and checks all saved parity and adversarial point bounds.
  It also checks exact GL2 character histograms at p=2,3,5,7,11,
  including the zero/rank-two countercontrols and transfer constant.
- Data: `.research/experiments/wide_mean_2026-10-20/`. All computation
  ran on Dirichlet, not locally or on fejer. Two reviewer launches
  failed because the configured default model `gpt-daybreak-blue-latest`
  was unavailable. No independent-agent review, Lean formalization,
  novelty claim, or unrestricted Chowla theorem is asserted.

The distance to full Chowla remains the unrestricted torsion-free
Boolean sign estimate in CSTAR. The new exact finite-group identity is
elementary; its useful contribution here is the scalar transfer and the
deterministic truncated-cone exclusion, not a claim of new finite-group
Fourier theory. Discontinue radius/activation/correlation tuning of this
truncated, phase-rich cone as a logarithmic-gain construction. The
center-law experiment invalidates overextending the uniform-parity
theorem, but (5) supplies the actual broader exclusion.

Keep three distinct lines: (a) the arbitrary-support mixed Boolean
certificate; (b) constructions outside this truncated phase-rich cone,
such as non-cone growing-depth Riesz rounding; (c) the unclassified
integer-cone region with incomplete long fibers or scalar encodings
that do not approximate all matrix phases. A concrete next inverse
test is to use the corrected average (p^2 n_p-n)/(p^2-1) across several
primes on incomplete long-fiber supports, asking whether the content
balance required to evade all those tests can coexist with weak plane
certificates. The identity alone does not prove that incompatibility.
