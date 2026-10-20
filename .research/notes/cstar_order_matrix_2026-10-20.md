# Order-sensitive boundary matrix: attempted derivations and falsifications

Checkpoint: 2026-10-20T05:32:53.486301+00:00. Research remains ongoing; no universal Chowla/C* theorem is claimed. Reproduction: [experiment index](../experiments/cstar_structural_2026-10-20/README.md).

Scope: CHAIN(c). No universal C* improvement established. Read CSTAR, PROOFS P19–P22, joint_boundary notes, and cstar_boolean_boundary_tests high-rank control.

Let A be positive, a0=0, C_uv=1_A(|u-v|)-1_A(u+v), u,v in A. For ordered x,y in A with z=x+y in A,

w^T C w = sum_[x+y=z] [w_z(w_x+w_y)-w_x w_y].

This includes repeated summands correctly (x=y contributes 2 w_x w_2x-w_x²). It immediately gives the exact identity w^T Cw=0 for w_a=1/a. More generally w_a=a^{-s} gives the ordered-triple summand (x^s+y^s-z^s)/(xyz)^s, strictly negative for s>1. This is an order relation, but NOT a newly established Boolean mechanism: the s=1 identity also holds for general nonnegative coefficients with the matching coefficient-weighted vector. The identity is also integration by parts for h=sum sin(ax)/a, h'=sum cos(ax).

## 1. Explicit harmonic row and failed Krylov sign

For w_a=1/a,

(Cw)_u = sum_[v,t in A;v+t=u] 1/v - sum_[t in A;u+t in A] u/[t(u+t)].

Set H=||w||², v=Cw, b=||v||²/H, r=v^TCv/||v||². Since w and v are orthogonal, the exact two-dimensional Rayleigh minimum is (r-sqrt(r²+4b))/2. Global positivity therefore implies

K >= (sqrt(r²+4b)-r)/2.

The proposed favorable sign r<=0 is FALSE. Exhaustive subsets of [1,12] give r=3.7953713248 for A=[1,12], the largest value in that search. It is not a numerical issue of near-zero sign.

For intervals the method asymptotically sees only a constant, despite the actual C eigenvalue growing linearly:

n=16: -lambda_min(C)=4.51334, r=5.69041, Krylov lower bound=2.17067.
n=64: -lambda_min(C)=14.69037, r=28.18687, bound=2.43740.
n=256: -lambda_min(C)=55.43176, r=117.51306, bound=2.55901.

Thus the harmonic residual can have sqrt(n) norm, but positive r of order n removes that gain. No claim that generic Schur positivity is new progress.

## 2. Exact negative cutoff forms, and their failure

For w^(t)_a=1_[a<=t]/a, all entirely internal triples cancel and

(w^(t))^T C w^(t) = -sum_[x,y in A; x,y<=t<x+y in A] 1/(xy).

This is genuinely sign-controlled by order. More generally w_a=g(a)/a has nonpositive quadratic form for every nonnegative nonincreasing g. However, for intervals, the cutoff numerator tends to a constant (a Riemann integral over x,y<=1<x+y), while the denominator sum 1/a² stays bounded below. These tests alone cannot even recover interval growth. The fixed s=2 test is weaker still: exhaustive [1,14] gives a ratio of its Rayleigh lower bound to |lambda_min| as small as 0.000126878, at A={1,3,5,7,14}. It is not an effective universal replacement for boundary counts.

## 3. Separate spectral-energy candidate: numerical stage, subsequently REFUTED in section 5

Initially tested candidate: ||C||_F² <= |A| lambda_min(C)². Section 5 gives an exact counterexample; do not retain this as an open conjecture.

Exhaustive Boolean enumeration of all 16,383 nonempty subsets of [1,14] and a separate 12,000-case seeded random sample (X between 12 and 129) found no violation; maximum ratio was 1. Boolean matrix entries and triple identities were computed exactly; eigenvalues were floating NumPy eigvalsh, so this is numerical evidence, not an exact spectral certification.

This candidate would imply U<=N K² (since U=2||C||F² and N=2|A|), only giving a cube-root consequence with the unchanged Roth lower bound. It is not a proof or an improved C* result. The stronger guesses lambda_max<=|lambda_min| or tr C³<=0 fail: random samples gave lambda_max/|lambda_min|=4.68019 and normalized positive cubic trace 0.654708. Merely appealing to spectral symmetry cannot prove the candidate.

For the carry-free Boolean digit cube A={nonzero sums of d independent positive superincreasing generators}, write indices as nonzero subsets. C equals comparability adjacency minus disjointness adjacency. Direct spectra give:
d=4, n=15: |lambda_min|=5, Frobenius/(n lambda_min²)=0.4.
d=6, n=63: |lambda_min|=15.32456, ratio=0.12207.
d=9, n=511: |lambda_min|=80.97468, ratio=0.01671.
This explicit torsion-to-order lift does not threaten the candidate, but this special family is not universal evidence.

## 4. Continuous interpolation / topology alternative

Consider a cyclic discrete two-level example with odd q and centered integer frequencies |s|<=X=(q-1)/2. If its discrete minimum -k occurs at r distinct qth roots with r>X, the centered trigonometric interpolant cannot remain >=-k on the continuous circle. Otherwise D+k is a nonzero nonnegative trigonometric polynomial of degree X with r zeros, each of even multiplicity; multiplying by z^X gives a degree-2X polynomial with >2X zeros counted with multiplicity. Thus K>k. This is an exact continuous obstruction to transferring a large flat discrete negative plateau unchanged.

It does not give a sqrt(n) loss. The elementary quantitative strengthening from a plateau node theta_j is

K-k >= |D'(theta_j)|²/(2 L), L=sum_[s in S] s²,

by the global Taylor bound |D''|<=L. This is the familiar derivative-versus-curvature loss, not a new escape from P77. For dense interval-type data its crude global-curvature denominator can suppress an order-n negative excursion to a constant-size bound. Thus exact connectedness/root multiplicity alone excludes exact finite-group interpolation, but supplies no adequate rate. Calling K>k a solution of the rank-versus-eigenvalue problem would be incorrect.

## Reproduction

Reproduction scripts: order_test.py (all subsets [1,14]); krylov.py (all subsets [1,12]); order_test2.py (12,000 random cases, seed 83); matrix_controls.py (interval and digit-cube spectra). Run with OPENBLAS_NUM_THREADS=1. No global trigonometric minimum was needed for these matrix comparisons.

A-only range limitation remains essential: a sum-free A can have C_A=0, so no lower bound for K in terms of |A| can follow from this compression alone. Extra positive-index ranges are necessary in that regime. None of the formulas here silently identifies A with the full index range.

## 5. Exact counterexample to section 3, found after targeted adversarial testing

The matrix-energy candidate is FALSE. Random and small-integer exhaustive tests missed the carry-free positive-root family.

Choose base b>=5 and m>=4, let r_i=b^i (0<=i<m), and A={r_j-r_i:i<j}. Integer uniqueness for bounded signed digit sums ensures that for distinct roots alpha=e_j-e_i, beta=e_l-e_k, their encoded difference belongs to ±A precisely when their Euclidean dot product is +1; their encoded sum belongs to A precisely when their dot product is -1. No doubled root is a root. Let V be the m by n oriented incidence matrix with column e_j-e_i, n=m(m-1)/2. Then exactly

C_A=V^T V-2I.

Since VV^T=mI-J,

lambda(C_A)={m-2 with multiplicity m-1; -2 with multiplicity (m-1)(m-2)/2}.

Consequently ||C_A||F²=2n(m-2), ||C_A||F²/[n lambda_min²]=(m-2)/2 -> infinity. The negative Frobenius mass fraction is 2/m ->0. This refutes both the candidate bound and any universal positive fraction of negative spectral energy for C_A, even with exact order, Booleanity and all harmonic identities.

Actual encoded verification used m=7,b=10 and checked C entrywise against V^TV-2I; discrepancy zero. Values of the energy ratio for m=6,10,20,40 are 2,4,9,19 respectively. This is an analytic counterexample, not an inference from floating spectral output.

It is NOT a high-ratio global Chowla counterexample. D=|sum_i exp(i r_i theta)|²-m gives K<=m. For even m and b≡3 mod4 (e.g. b=7), theta=pi/2 gives alternating +i,-i and K=m exactly. Hence N/K²=(m-1)/m<1, while the A-only local relaxation gives N/4->infinity.

The missing even/root block is visible without adding an enormous index range. Define C^+_uv=1_A(|u-v|)+1_A(u+v) on A. It is unsigned incidence Gram minus2I, with uniform row sum2m-4. Including the constant test adds coupling sqrt(2) times the all-ones vector. The constant/uniform-cosine 2×2 block is

[[0,sqrt(2n)],[sqrt(2n),2m-4]],

whose smallest eigenvalue is (2m-4-sqrt((2m-4)²+8n))/2 ~ -(sqrt2-1)m. Thus the even sector and constant recover square-root scale immediately in this family. The same certificate appears in the collective-boundary calculation and is P10-equivalent, not a new universal advance.

Lesson established by an exact model: positive harmonic isotropy, ordered-triple cancellation, exact Boolean support, and arbitrarily large odd negative eigenspace do not control the odd negative eigenvalue. They are all present in this family. A viable joint-boundary inequality must couple odd and even sectors (or other rows) rather than estimating C_A's negative spectral energy alone.

## 6. What remains after parity repair

The full {0} union ±A local block also cannot simply be asserted to reach sqrt(n). Existing E99c tapered independent rounding controls at density n^(-1/3) have local certificates of order n^(1/3), whereas PROOFS P70.3 separately proves sqrt(n) globally with high probability for those independent roundings. The root-family parity repair therefore does not close the local-block strategy. The larger S+S-generated range is considered in the second-neighborhood continuation; its universal guarantee remains under test, not proved.

A weaker joint candidate ||C_A||F² <= c n K_local², where K_local includes both parity blocks and the constant row, is not decided here. It would yield a cube-root exponent using the unchanged lower count; generic finite-group/Gram reasoning cannot prove it because O4 is a countermodel there. No evidence here justifies elevating the candidate to a theorem, and no universal sqrt claim follows from the completed calculations.
