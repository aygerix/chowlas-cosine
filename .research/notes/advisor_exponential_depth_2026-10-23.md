# Selected-exponential depth audit and global-review correction

2026-10-23. Internal AI advisor, paper review only. Only this newly
assigned note is edited. No computation, VM operation, GPU, additional
agent or external outreach. Shared Dirichlet remains on. No new
kernel-checked or externally scrutinized theorem is claimed.

## 1. Generic selected-exponential sign and parity: factors check

Let F be a nonconstant analytic polynomial with real coefficients,
F(0)=0, f=Re F and M=-min_circle f>0. Define

    E_u=exp(-uF), C(u)=<F,E_u>, Z(s)=<exp(-2sf)>.

All averages are probability Haar averages. C(u) is real, and
analyticity gives C(u)=2<f*Re E_u>, while <Re E_u>=1. For
0<uM<=1, set y=f/M>=-1, t=uM and mu=1+f/M>=0. Then

    1+C(u)/(2M)=<mu*Re E_u>
                  <=<mu*exp(-uf)><=1,              (1)

because

    (1+y)*exp(-t*y)<=1+(1-t)*y, y>=-1, 0<t<=1.

For completeness, for y>-1 compare logarithms of both sides.
The logarithmic difference has derivative
t*[1-1/((1+y)*(1+(1-t)y))], negative on(-1,0) and positive
on(0,infinity), and is zero at0. The endpoint y=-1 is immediate.
This proves C(u)<=0, strictly for nonconstant F and u>0 in range.
No coefficient positivity or Booleanity enters (1).

The exact parity identities at E_s are

    Q_even=(Z(s)+1)/2, Q_odd=(Z(s)-1)/2,
    H_even=(-Z'(s)+C(2s))/2,
    H_odd =(-Z'(s)-C(2s))/2.                        (2)

They use <E_s²>=1 and <2f*Re E_(2s)>=C(2s). The EVEN component
includes its constant1. Since Z'(s)>0 for nonconstant f and s>0,
H_even<0 whenever2sM<=1. This generic sign must not be confused
with the Boolean S0 or P2 hypotheses; it also holds for the weighted
flatness escapes and alone supplies no root-scale gain.

There is a useful quantitative check. The scalar deficit in (1),
at y=-v, 0<=v<=1, is

    D_t(v)=1-(1-t)v-(1-v)*exp(t*v),
    D_t''(v)=t*exp(t*v)*(2-t+t*v)>=t.

Consequently

    -C(u)>=u*<f_-²>>=u*||f||1²/4,
    |C(u)|<=2*exp(uM)*||f||1.                      (3)

At u=1/sqrt(n), ACTUAL M<=sqrt(n), a uniform root-sized amplitude
of this finite C polynomial is therefore equivalent up to constants
to the old qualitative L1 flatness. Similarly (2), bounded normalized
even amplitude, and (3) show that a uniform root-sized even exponential
Rayleigh gain at s=1/(2sqrt(n)) is equivalent to that flatness target.
The sign window uM<=1 need not cover the later temperatures at which
a rare negative well becomes visible. No all-scale lower estimate
follows just from (1).

## 2. Positive-sum depth and the exponential Bernstein bound

Return to a Boolean A of n distinct positive integers. Define

    h=max{r>=1:A intersects rA},

where rA consists of sums of r elements of A, with repetitions allowed.
This is finite, at most max(A)/min(A). If
R_r=<F,F^r>, the selected-exponential polynomial is exactly

    C(u)=sum_(r=1)^h (-u)^r*R_r/r!,
    R_1=n, C'(0)=-n.                               (4)

For Boolean coefficients R_h>0, so its degree is h. With arbitrary
real coefficients on the same support, degree at most h is sufficient
for all arguments below; the leading pairing could cancel.

For every real u>=0, Parseval/Cauchy and the constant term E_u(0)=1
give

    |C(u)|²<=n*(Z(u)-1)<=n*(exp(2uM)-1).            (5)

Let P(v)=C(v²/M)/v, continuously extended at0. This is an odd
polynomial of degree2h-1, P'(0)=-n/M, and for |v|<=1,

    |P(v)|²<=n*(exp(2v²)-1)/v²<=n*(e²-1).

The last inequality is the convex secant bound for exp(2t) on[0,1].
Bernstein's interior derivative inequality at0 consequently yields

    M>=sqrt(n)/[(2h-1)*sqrt(e²-1)].                 (6)

Every factor in this derivation checks. More generally, replacing
v²/M by b*v²/M, b>0, gives

    M>=b*sqrt(n)/[(2h-1)*sqrt(exp(2b)-1)].           (7)

No actual-low-M premise is needed for (5)--(7). For real coefficient
polynomials, n is replaced by the coefficient square sum ||F||2².

The derivative inequality can be proved here without an external
theorem. For odd D=2h-1, suppose |P'(0)|>D*||P||infinity. Choose
c so (P-c*T_D)'(0)=0, where T_D is the Chebyshev polynomial;
|c|>||P||infinity. At its D+1 alternating extrema, P-c*T_D has
strictly alternating signs, hence at least D zeros in their open
intervals. It is odd and its derivative at0 vanishes, so the zero
at0 has multiplicity at least3. This gives at least D+2 zeros with
multiplicity, impossible for degree at most D. The identically-zero
case would contradict |c|>||P||infinity.

### Depth two: valid factors, but not a new bounded-depth theorem

The condition h<=2 means A intersects NO rA for ANY r>=3. It does
not mean merely A intersects no3A: {1,4} avoids3A but intersects4A.
Under the actual h<=2 condition, (4) is
C(u)=-nu+t*u²/2. Applying (1) at u=1/M gives t<=2nM.
The positive weighted Gram on{1,f} gives

    3M*t+2M²*n>=n².

Indeed its entries are M,n/2,3t/4+Mn/2. Combining the two bounds
gives M>=sqrt(n/8). This calculation is correct, with the stated
full depth condition. Its strength is superseded by the existing
star method below.

## 3. Stronger direct P9 corollary: M>=sqrt(n/(2h))

Define ell(a)=max{r:a belongs to rA} for a in A, and L_j={a:ell(a)=j},
1<=j<=h. If a>b and a-b belongs to A, then ell(a)>=ell(b)+1.
Also if a+b belongs to A, ell(a+b)>=ell(a)+ell(b).

For each j define the signed leaf set

    W_j=L_j union(-L_(h+1-j)).

No difference of two distinct members of W_j belongs to plus/minus A.
Within either level this follows from strict height increase. Across
the two signs, an A-difference would be a sum of heights at least
j+(h+1-j)=h+1, impossible. Each W_j lies in plus/minus A.

The sum of their cardinalities over j is2n, so some W_j has size
at least2n/h. P9's independent-leaf star certificate gives

    2M>=sqrt(|W_j|), hence M>=sqrt(n/(2h)).          (8)

One can see the certificate directly from the Fourier polynomial
sqrt(m)-sum_(w in W_j)z^w. Its norm square is2m and its D=2f
energy is-2m*sqrt(m), since all leaf-leaf differences are absent.
Its Rayleigh quotient is-sqrt(m), proving the same bound.

Thus the exponential depth argument is a valid method-specific
derivation, but the resulting bounded-depth partial bound is
DOMINATED by an elementary consequence of the already-recorded P9
mechanism. In particular h<=2 gives M>=sqrt(n)/2, stronger than
the exponential quadratic constant. This should not be presented
as a new universal advance, a new route, or a reason for a depth
control experiment. The h-level corollary itself is paper-derived
here; no new kernel formalization of it is claimed.

## 4. Why a cheap short-chain core is false: distinguish two deletions

Take ANY integer Sidon B={b1<...<bk}, and A=diff_+(B). Then
n=k(k-1)/2 and ACTUAL M(A)<=k/2<sqrt(n) for k>2. A concrete
infinite choice is B={1,3,...,3^(k-1)}.

### 4.1 Deleting vertices, retaining the ORIGINAL connection set A

Partition A into disjoint sets C_j={b_i-b_j:i>j}, of sizes k-j.
Each is a clique of the A-difference DAG, and its increasing order
is a directed chain. If only vertices are removed while adjacency
is STILL defined by original A, height<=H requires retaining at
most H vertices from each clique. Thus at least

    sum_(r=1)^(k-1)(r-H)_+
      =(k-H-1)*(k-H)/2                             (9)

vertices must be removed. For fixed H this is n-O_H(k), so
O(M)=O(k) vertex deletions cannot leave a bounded-height core.
It also obstructs original-A representation heights at retained
vertices. This is the precise scope of the lead's clique-partition
falsifier.

### 4.2 Deleting frequencies and RECOMPUTING with A'

If A'=A\D, labels of edges may themselves be deleted. Bound (9)
does not follow from the same clique argument for this different
operation. For example, B={0,2,5}, A={2,3,5}, deleting3 leaves
A'={2,5} of positive-sum depth1, although the retained vertices2,5
were an original-A clique joined by the deleted label3.

A robust lower bound still refutes O(M) deletion. Deleted frequencies
correspond bijectively to d deleted edges from the complete graph on B.
The remaining graph has a clique of size at least k²/(2d+k). An
elementary proof takes a random order in the deleted-edge graph;
vertices earlier than all their neighbors form an independent set
of expected size sum_v1/(deg(v)+1)>=k²/(2d+k).

A surviving clique of r B-points gives r-1 increasing differences
from its least point, with EVERY intervening edge label in A'.
Its last difference is a sum of r-1 selected positive differences.
Thus

    h(A')>=k²/(2d+k)-1.

To obtain h(A')<=H it is necessary that

    d>=k²/[2(H+1)]-k/2=Omega_H(n).                  (10)

In particular O(M)=O(k) deletions cannot leave bounded recomputed
positive-sum depth either. This corrects the edge-label issue while
retaining the substantive falsification of the proposed cheap-core
principle.

### 4.3 The stronger n-O(k) recomputed claim is actually false

Choose a Sidon set C of size m in[1,X], put L=4X,T=16X², and let
B=C union(T+L*C). This B is Sidon. The two internal difference
scales are disjoint; a cross collision would imply
L*(c_j-c_l)=c_i-c_v, which forces both differences zero; the cross
range lies above both internal ranges.

Here k=2m, n=m*(2m-1), and M(diff_+(B))<=m<sqrt(n). Delete only
the two internal-difference classes, a total of m(m-1) frequencies.
The retained m² cross differences lie in

    [T+L-X, T+L*X-1].

Twice the lower endpoint exceeds the upper endpoint, so the retained
set has positive-sum depth1. Thus a macroscopic core CAN remain
after Theta(n) deletions; the n-O(k) count cannot be asserted for
recomputed depth. This does not rescue O(M) deletion and does not
give a low-M construction for the remaining core.

### 4.4 Exact balanced Turan deletion threshold: the sharp statement

Fix integers H>=1 and k>=H+1. Put q=H+1, write k=q*a+s with
0<=s<q, and define

    d_*(k,H)=s*binom(a+1,2)+(q-s)*binom(a,2).

Among ALL integer Sidon sets B of size k, the minimum number of
frequencies which must be deleted from diff_+(B) to leave a nonempty
set of RECOMPUTED positive-sum depth at most H is EXACTLY d_*(k,H).
For every B this is a lower bound; there exist explicit B attaining
it, with the retained depth exactly H. This is a scoped deletion
theorem, with no assertion that every B attains the bound.

For the lower bound, label each edge of K_k by its positive B
difference. Sidon uniqueness makes these labels distinct. Retaining
A' retains precisely the edges labelled in A'. A clique on H+2
ordered B-points would put its total endpoint difference in A'
and express it as a sum of H+1 successive differences, all in A'.
Thus h(A')<=H forces this graph to be K_(H+2)-free. The classical
exact Turan theorem bounds its edges by those of the balanced
complete (H+1)-partite graph. Its complementary edge count is
precisely d_*(k,H). This strengthens (10) by the exact integer
rounding and identifies its optimal order. Turan's theorem is the
only outside combinatorial fact in this sharp lower-bound step.

For attainment, partition indices1,...,k into q nonempty groups
I_0,...,I_H of balanced sizes. Set delta=9^k, choose any integer
T>(H+2)*delta, and put

    B_j={j*T+9^i:i in I_j}, B=union_(j=0)^H B_j.

Every offset lies in[1,delta]. If two positive B differences are
equal, their center gaps are equal, because the discrepancy in
their offset differences has absolute value less than2*delta<T.
Their signed power-9 differences must then coincide. A nonzero
signed power-9 difference uniquely determines its ordered pair:
its sign gives the order and its 9-adic valuation gives the smaller
exponent. Thus B is Sidon.

Delete just the within-group difference labels. Their number is
d_*(k,H). All retained cross-group differences lie in

    [T-delta,H*T+delta].

Since (H+1)*(T-delta)>H*T+delta, no retained element is a sum
of H+1 or more retained elements. Hence h(A')<=H. Conversely,
choose one B-point from each of the H+1 ordered groups. Its H
successive positive differences and its total endpoint difference
are all retained, giving a telescoping H-term representation and
h(A')>=H. This proves exact attainment.

The original full difference support still has ACTUAL M<=k/2.
This supplies the sharp structural falsifier to the proposed
O(M)-deletion bounded-depth reduction. It does not assert low M
for the retained core, and neither this statement nor its priority
has been kernel-checked or externally reviewed.

## 5. Changed construction question: growing multiplicity with L1 defect

After fixed temperature reduced to the old flatness gap and the
exponential depth bound was dominated by P9, a global review is
appropriate. The lead proposed a genuinely quantified construction
question. Let B have k points, A its FULL positive difference support,
N=|A|, r_d its integer multiplicities, and fix an integer r>=2. Put

    E_r=sum_(d in A)|r_d-r|.

The exact square identity gives the ALL-CIRCLE certificate

    M(A)<=k/(2r)+E_r/r,
    |r*N-k*(k-1)/2|<=E_r.                          (11)

Thus growing r with E_r=o(k*sqrt(r)) would imply
N~k²/(2r) and

    M(A)/sqrt(N)<=1/sqrt(2r)
                       +sqrt(2)*E_r/(k*sqrt(r))+o(1) ->0.

This is a scoped square-identity mechanism, not a claim that such
B exist and not an unrestricted conclusion from any frequency or
density assumption.

The endpoint multiplicity argument in existing P76 gives
E_r>=r(r-1)/2 (for r<=k), forcing the only potentially successful
regime r=o(k^(2/3)). I did not derive a general lower bound
E_r>=c*k*sqrt(r). Existing P8's growing-multiplicity estimate is
consistent with this scaling; P9 alone does not supply that missing
robust autocorrelation bound. This absence of a derivation is not
evidence that the construction is feasible.

There IS a cheap structural gate from old P23. If B is reflection
symmetric, exactly floor(k/2) difference classes have odd multiplicity.
For ODD r, all the other nonzero classes contribute at least1 to E_r.
Combining E_r>=N-k/2 with rN>=k(k-1)/2-E_r gives

    E_r>=k*(k-1-r)/[2*(r+1)].                       (12)

In the critical regime r=o(k^(2/3)), this is much larger than
k*sqrt(r). Reflection-symmetric odd-r candidates are therefore
excluded immediately. This gate does not cover even r or asymmetric B.

The revised objective is not the old fixed-r near-ruler pilot. P23
kept only exact-r classes and paid W=2sum_nonexact r_d. With the
present definition the conversion is only

    W<=2*(r+1)*E_r,

which need not be O(k) when r grows. Counts r_d=r-1 now cost1
rather than causing the entire class weight to be dropped. The
old fixed-r heuristic demotion does not settle the critical growing-r
L1 defect question. Its recorded experiments should not be rerun.

Paper advice before the test below: this new growing-r defect is
not ruled out by the elementary gates checked here. At most a
single bounded, predeclared exact combinatorial mechanism test was
justified; no angle-minimum sweep, old fixed-r near-ruler revival,
GPU pilot or inference from finite failure was warranted. A
parametric structural candidate and an asymptotic E_r upper bound
would be the substantive result. The universal obstruction
E_r>=c*k*sqrt(r), if proved, would exclude this particular
construction mechanism, not prove full Chowla.

### 5.1 Read-only audit of the completed bounded pilot

I inspected src/multiplicity_l1_pilot.py and the saved artifact
.research/experiments/multiplicity_l1_2026-10-23/results.json. I did
not execute or independently recount the support. The artifact
records one Dirichlet CPU chain, seed2026102308, k=128, r=8,
B subset[0,2048], 15000 proposed moves, and about2.36 seconds.
The source keeps0 in B, uses cardinality-preserving exchanges of
sizes1,2,4 and minimizes exactly sum_(r_d>0)|r_d-r|. A zero
multiplicity class costs0, so this is the FULL nonzero-support
objective of (11), rather than the old exact-class retention rule.

The source's final verifier recomputes pair counts directly, checks
them against an exact FLINT polynomial autocorrelation, checks
sum r_d=k*(k-1)/2, and forms the rational certificate in (11).
The incremental update removes/adds both changed-to-kept pairs
and pairs internal to each changed set, so I found no omitted
pair category or cosine normalization error. These are source and
artifact audits, not a fresh independent execution.

The saved best values are

    initial E=7016, final E=2964, N=1136, max(A)=1638,
    certified M(A)<=757/2,
    certified R(A)^2<=573049/4544,
    E/(k*sqrt(r)) approximately8.187.

The rational values agree with (11). The predeclared defect gate
E/(k*sqrt(r))<1/8 is exactly the integer test64*E²<k²*r;
the half-constant upper gate is4*M_upper²<N. Both failed. The
reported R_upper is about11.23. This is a poor certificate from
this mechanism, NOT a lower bound on the actual M or R. The
heuristic box is incomplete and tests a single finite even r;
it establishes no growing-r asymptotic obstruction or feasibility.
The source/artifact therefore support stopping this optimizer,
with no enlargement, repetition or GPU deployment from this run.

## 6. Current status and decision

AUDITED: generic exponential sign/parity and quantitative flatness
comparison; Bernstein depth bound and its h<=2 factors. PROVED
paper comparisons/falsifiers: stronger P9 depth corollary; failure
of the O(M)-deletion bounded-core principle, with original/recomputed
scope separated; the exact sharp balanced Turan deletion threshold;
explicit falsity of the stronger recomputed n-O(k) deletion count;
reflection/odd-r defect gate. The one new multiplicity pilot was
source-audited and failed both declared gates; it supplies no
asymptotic result.

No universal coefficientwise exponential growth, flatness bound,
new exponent or counterexample family has been established. Stop
counting fixed-temperature equivalences and dominated bounded-depth
bounds as new primary progress. The next choice must use genuinely
new unit-coefficient structure or the changed growing-multiplicity
construction question (11), with all-circle certification supplied
by its exact identity. No resource action follows from this note.
