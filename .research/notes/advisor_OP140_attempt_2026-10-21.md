# Advisor OP140 attempt and changed next hypothesis

2026-10-21. Internal advisor, GPT-6.1 Sol/MAX. Paper derivations only in
this note; no VM jobs, GPU spending, new agents, or independent reruns.
The Number Theory research skill and the existing route ledger govern
the interpretation. No universal Chowla bound is proved here.

All integrals use dx/(2*pi). For an arbitrary nonempty finite set A of
distinct positive integers, write n=|A|, X=max(A),
D=2 sum_A cos(ax), and K=-min_R D. The exact target remains an
absolute positive lower bound for K/sqrt(n), or an effective Boolean
counterexample family with a rigorous all-circle upper bound tending
to zero after this normalization.

## 1. Exact Schur reduction, and the step that did not close

Use the band B={1,...,2X}, c_j=1_A(j), and

    C_jk = (1_A(|j-k|)+1_A(j+k))/2,
    Z = C + 2 sqrt(n) I.

On the actual all-circle hypothesis K<=2sqrt(n), Z>=sqrt(n)I.
The open OP140 assertion is

    J = c^T Z^(-1)c >= sqrt(n)/140.

Partition the band into A and E=B\A. The exact Schur complement is

    S = Z_AA - C_AE Z_EE^(-1) C_EA,
    J = 1^T S^(-1) 1.

Fixing the selected coefficients to 1 and optimizing the exterior gives

    min_{v_A=1} v^T Z v = 1^T S 1,
    J >= n^2/(1^T S 1).

Thus a universal upper bound 1^T S 1=O(n^(3/2)) would suffice. It is
strictly stronger than a bound on 1^T S^(-1)1: a large eigenvalue of S
can spoil the former while the latter still receives useful coupling
from other directions. No arbitrary-support upper bound for this
fixed-interior cost was obtained.

The missing implication was to turn the linked zero/one entries of
C_AE into enough cancellation of the large positive selected-block
cost, uniformly with the interior vector fixed. Neither positive
semidefiniteness nor the Schur identity supplies that cancellation.
For example, the ordered block with rows a in A and columns X+b,
b in A, has entries 1_A(X+b-a)/2 and is triangular with diagonal 1/2.
This proves invertibility of that particular cross block; it does not
give a norm or energy bound for its inverse. An isolated maximum
frequency can also make this block irrelevant to additive triples in
a dense lower portion of A.

The proposed fixed-interior Singer continuum calculation belongs to
the same uniform-completion obstruction already recorded in ROUTES
rows 141--142. It is not a new adaptive inverse theorem. Its informal
weighted weak-limit passage was not completed here, so no new Singer
asymptotic Schur theorem is asserted. In particular, the recorded L4
uniform-completion obstruction is not, merely by naming it, a proof
of every analogous statement about this Z-weighted Schur cost.
Discontinue this expansion; retain adaptive selected coefficients.

## 2. A proved small corollary of existing P73

The following removes a variance/coupling hypothesis from one precise
class of adaptive references. It is a consequence of the project's
existing torsion-free few-spike theorem, not a new route or a proof
of OP140.

**PD variance gap.** Let p:Z->[0,1] be finite, symmetric, positive
definite, with p_0=1. Put

    mu = sum_{j>0} p_j,
    V  = sum_{j>0} p_j(1-p_j).

Then V>=mu/77.

Proof. Let S={j:p_j>=1/2}. This is a finite symmetric set containing
0; write |S|=1+2t. Pointwise,

    (p_j-1_S(j))^2 <= p_j(1-p_j),
    |p_j-1_S(j)| <= 2p_j(1-p_j).

Consequently E=||p-1_S||_ell2^2<=2V and mu<=t+2V.
P73 with p_0=1 applies for every delta<1/5. Taking delta up to 1/5
gives E>=(|S|-1)/75=2t/75. Hence V>=t/75 and
mu<=75V+2V=77V. The only nontrivial outside input here is P73;
its torsion-free sumset step is precisely where a finite subgroup
would invalidate this deduction. QED.

P73's Z theorem is recorded as kernel checked in
lean/ChowlaCosine/FewSpike.lean. This corollary and its applications
below have only the displayed paper proof; they have not been
formalized or independently kernel checked.

For any such profile with mu=n, define

    D_p = 2 sum_{j>0} p_j cos(jx),
    q = D-D_p,
    a = integral Dq,
    Q = integral q^2.

Orthogonality gives the exact identities

    a = 2n-2 sum_{j in A} p_j,
    Q = 2n+2 sum p_j^2-4 sum_{j in A}p_j,
    a = Q/2+V.

Therefore EVERY mass-matched normalized PD profile gives

    a>=n/77,      Q<=2a<=4n.

The normalized witness q'=(n/a)q has a'=n and Q'<=154n.
This is only automatic coupling and norm control. It supplies no
mixed-cost estimate H=integral Dq^2.

For clarity, the more general algebraic identity is
a=Q/2+V+n-mu when n=sum a_j^2 for an arbitrary coefficient vector.
That algebra alone is not specifically Boolean. Booleanity identifies
sum a_j=n as well, so matching mu=n also matches the actual front
D(0)=2n. This distinction matters in the weighted countercontrol.

## 3. Historical proposed hypothesis, subsequently REFUTED in Section 5

One testable way to close the remaining reference-choice gap is:

**IPD(C), proposed here and subsequently REFUTED below.**
There exists an absolute finite C such that, for EVERY genuine Boolean
A with K<=2sqrt(n), some profile p as above satisfies

    p_j=0 for j>2X,   sum_{j>0}p_j=n,
    ||D-D_p||_infinity <= C sqrt(n).

The admissible reference class itself is never empty: the Fejer
profile p_j=1-j/(2n+1), 1<=j<=2n, has mass n and is normalized PD;
also 2n<=2X. The unknown is the uniform approximation, not existence
of some feasible PD profile. No bound for a fixed Fejer choice is
claimed.

If IPD(C) holds, the preceding corollary gives a>=n/77, Q<=4n,
and, by Cauchy--Schwarz,

    |H| <= ||q||_infinity ||D||_2 ||q||_2
         <= 2sqrt(2) C n^(3/2).

The mixed determinant inequality a^2<=K(H+KQ), together with
K<=2sqrt(n), then implies

    K >= sqrt(n)/(77^2(2sqrt(2)C+8)).

The complementary branch K>2sqrt(n) is immediate. Hence this
existence hypothesis would prove an absolute Chowla constant. The
normalized q' has Q'<=154n, rather than a justified Q'<=25n; this
reduction must not be advertised as L25 or as OP140 with constant140.
One can also record |H'|<=154sqrt(77) C n^(3/2), using Q<=2a.

This is the inverse of the existing controlled PD-rounding mechanism
in ROUTES row142 / CHAIN(c). It is a changed hypothesis after the
fixed-interior Schur failure, not a newly independent route. Its
universal existence assertion was unproved at this stage and is refuted
by the subsequent Section 5 argument.

There is an inexpensive analytic falsification gate before investing
in this stronger target. Because P=1+D_p>=0 and integral P=1, IPD(C)
requires

    integral (1+D-Csqrt(n))_+ <= 1.

A low-K Boolean family whose positive tail violates this for every
fixed C would refute IPD, without refuting OP140, L25, or Chowla.
Thus even a good mixed-certificate architecture need not admit a
uniformly bounded discrepancy reference. Do not elevate this
sufficient target to the primary goal itself.

The weighted Fejer escape fails this front-matching hypothesis
analytically: for weights w_j=1-j/m, sum w_j=(m-1)/2 while
n_eff=sum w_j^2=(m-1)(2m-1)/(6m). Any profile of mass n_eff has

    |D_w(0)-D_p(0)|
      = 2(sum w_j-n_eff) ~ m/3,

which is much larger than sqrt(n_eff). Conversely, choosing p=w
makes the residual zero but violates the required mass match.
The variance lemma does not by itself eliminate weighted escapes.

## 4. Evidence boundary and continuation decision

The lead reports rigorous residual sandwiches for J on the singleton
and saved Singer supports. The selected high-cubic p509 case has
n=129795, tau approximately780.35>552 and

    78522003/500000000 <= J/sqrt(n)
                       <= 31408803/200000000.

This tests beyond the elementary c-only branch
J>=sqrt(n)/(tau/4+2). It is a finite certified nonviolation, not an
arbitrary Boolean inequality. I did not rerun its exact products.
No further Singer size expansion is justified by this attempt.

**Next derivation at the initial handoff (now completed in Section 5):** examine the stated positive-tail obstruction to
IPD and then the existence of a mass-matched peak-one PD reference
for arbitrary low-K A. The first question is whether this stronger
reference hypothesis survives the existing adversarial supports;
the second is the missing selection theorem, not more variance
bookkeeping. If the tail obstruction kills IPD, retain the weaker
mixed-cost problem and direct negative-Rayleigh certificates.

Keep the independent construction track requiring Boolean sets and
all-circle upper bounds. Nothing here revives the ledger's dead
tensor renormalization, finite-automaton, or independent product-Fejer
families. A construction continuation needs an actual changed
mechanism, not those templates at a larger parameter.

**Handoff:** new paper corollary V>=mu/77 and its exact coupling/norm
consequences; no new universal mixed-cost or Schur estimate; known
fixed-interior obstruction recognized and not expanded. Three live
directions remain arbitrary-support adaptive inverse certificates,
direct negative-Rayleigh alternatives, and an independent all-circle
construction. No new Lean/kernel-checked mathematical proof, no
external review, and no unattended computation are claimed.

## 5. Subsequent independent review: IPD(C) is REFUTED

2026-10-21, after the preceding handoff. The lead supplied the
following elementary lacunary-difference counterfamily. I independently
checked the digit argument, moment bounds, tail calculation, and L25
constants. This section supersedes the open status of IPD(C) above.
It refutes that proposed inverse principle; it does not refute OP140,
L25, or Chowla. No computational experiment was needed.

**Theorem.** For each integer k>=2 put q=k+1 and

    B_k={1,q,...,q^(k-1)},
    A_k={q^j-q^i: 0<=i<j<k},
    n_k=k(k-1)/2,
    F_k(x)=sum_{j=0}^{k-1} exp(i q^j x),
    D_k(x)=2 sum_{a in A_k} cos(ax).

Then A_k is a genuine set of n_k distinct positive integers, and

    D_k=|F_k|^2-k >= -k,
    M(A_k)<=k/2<=sqrt(n_k).

Nevertheless, for EVERY fixed C>0,

    integral (D_k-Csqrt(n_k))_+ -> infinity  as k->infinity.

Consequently, for every C>0 and all sufficiently large k, there is
NO nonnegative measurable P of circle mean1 satisfying

    ||D_k-(P-1)||_infinity <= Csqrt(n_k).

This excludes even references with no Fourier coefficient, degree,
mass-at-the-origin, or PD restrictions beyond P>=0 and integral P=1.
Moreover, for every k>=66,

    ||D_k||_1 > k/5 >= sqrt(n_k)/5.

Thus this is an IPD counterfamily on which the L25 conclusion itself
holds, as well as its actual low-K hypothesis.

**Distinctness and the all-circle certificate.** The integer q^j-q^i
has base-q digits q-1 exactly in positions i,...,j-1. These digit
blocks uniquely determine i,j, proving difference uniqueness. The
square identity therefore has coefficient exactly1 at every positive
difference. Nonnegativity of |F_k|^2 proves the global upper bound
on M. Finally, k/2<=sqrt(k(k-1)/2) for k>=2.

**Exact moments without a limiting-distribution assertion.** Put
Y=|F_k|^2/k. For every positive integer s with q>s, no carries occur
when summing s powers of q. Equality of two such sums is equivalent
to equality of their multiplicities at all k positions. Hence

    integral Y^s
      = k^(-s) sum_{m_1+...+m_k=s}
                    (s!/(m_1!...m_k!))^2.

The all-distinct terms give the lower bound

    integral Y^s >= s!(k)_s/k^s,              (k>=s).

For each ordered left tuple of s indices there are at most s!
ordered right tuples with the same multiplicities. Thus the upper
bound is

    integral Y^s <= s!.

These are exactly the corresponding independent-Steinhaus moments,
but independence or a CLT is not being asserted for the functions
exp(iq^j x). The finite no-carry identities are sufficient.

**Positive-tail lower bound.** Fix C>0 and t=1+C. Choose an integer
r such that r!>=4(2t)^r. This choice is effective: take
h=ceil(8t^2), r=2h, and use r!>=(h)^h.
For k>=max(2r,r(r-1)), q>2r, and

    (k)_r/k^r
      = product_{j=0}^{r-1}(1-j/k)
      >= 1-r(r-1)/(2k) >= 1/2.

Therefore integral Y^r>=r!/2 and integral Y^(2r)<=(2r)!.
The contribution from Y<=2t is at most (2t)^r<=r!/4, so

    integral Y^r 1_{Y>2t} >= r!/4.

Cauchy--Schwarz now gives a k-independent positive constant

    measure{Y>2t} >= eta_r,
    eta_r=(r!)^2/(16(2r)!).

Since sqrt(n_k)<=k and D_k=k(Y-1),

    integral (D_k-Csqrt(n_k))_+
      >= k integral (Y-t)_+
      >= kt eta_r -> infinity.

If P>=0, integral P=1, and the asserted uniform approximation
held, then pointwise

    P >= (1+D_k-Csqrt(n_k))_+.

Its integral would be at most1, contradicting the tail lower bound
once kt eta_r>1. All thresholds depend only on C; the family A_k
itself does not depend on C.

**Direct verification of L25 on the same family.** For k>=66 we
have q>4, so the preceding identities give

    integral Y=1,
    integral Y^2=2-1/k,
    integral Y^3>=6(1-3/k),
    integral Y^4<=24.

It follows that

    integral D_k^2=k^2-k >= 3k^2/4,
    integral D_k^4
      = k^4 integral (Y-1)^4
      <= k^4(9+66/k) <=10k^4.

Holder interpolation yields

    ||D_k||_1^2
      >= (integral D_k^2)^3/(integral D_k^4)
      >= 27k^2/640 > k^2/25.

The claimed L1 lower bound follows. In the original f convention,
this is ||f_A||_1>k/10>=sqrt(n_k)/10.

**Interpretation and pivot.** The new event is a rigorous refutation
of a proposed unrestricted inverse reference theorem, rather than
another exclusion of a construction from beating square-root scale.
It shows why bounded uniform discrepancy from a nonnegative
mean-one reference is overstrong even on L25-good Boolean supports.
The P73 variance corollary remains correct, but it does not rescue
that reference-existence hypothesis. Stop IPD optimization.
Retain adaptive witnesses with mixed-cost control, OP140 and direct
negative-Rayleigh alternatives; preserve the independent all-circle
construction track. Any replacement reference criterion must allow
these unbounded positive tails, for example by controlling a weighted
mixed integral rather than uniform discrepancy. No universal such
criterion is proved by this counterexample.

Status: complete elementary paper proof independently checked by
the advisor against the lead's derivation; no Lean formalization or
kernel-checked proof of this theorem, external scrutiny, VM job, or
additional GPU expenditure.
