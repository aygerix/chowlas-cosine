# Reference entropy, cubic cost, and signed combinations

2026-10-20. CHAIN(c) / DESIGN research record. Full Chowla remains OPEN.
This continues the [deterministic Sidon-window result](cstar_sidon_deterministic_2026-10-20.md).
Previous turn: progress. This turn: a paper counterfamily to an automatic
cost bound, complete small reference frontiers, and a stronger finite
certificate obtained by signed combinations. No arbitrary-support
representation, universal square-root theorem, or counteralgorithm follows.

## 1. The exact bridge and the endpoint question

For actual positive-integer support A, put D_A=2f_A and K=2M(A).
For any real mean-zero trigonometric polynomial q, let

    a=<D_A,q>, Q=<q,q>, H=<D_A,q^2>.

Positivity of <(D_A+K)(s+tq)^2> gives Q K^2+H K-a^2>=0.
Thus a>=alpha*n, Q<=beta*n, H<=gamma*n^(3/2), with absolute
positive alpha,beta and finite gamma, would give a universal square-root
bound if established for every A. This is a sufficient bridge, not a
proved inverse theorem or an asserted necessary architecture.

For equal-size Boolean supports A,B and q=D_A-D_B,
a=2|A\B| and Q=2a. In the present model A consists of positive
differences of a k-point cyclic-Sidon P in [0,p)^2. Encode by
L(x,y)=x+(6p+1)y. This preserves zero sums of at most three difference
vectors, hence all moments used here. It gives distinct positive
integer frequencies, n=k(k-1)/2, and the global upper certificate
M(A)<=k/2 from D_A=|F_P|^2-k.

The previously proved window theorem covers Fourier algebra complexity
O(p^delta), fixed delta<1/2. The endpoint can encode arbitrary dense
point selections on a curve. We tested whether exact spatial cell
counts preserve enough freedom for a useful reference.

## 2. Paper counterfamily: fixed coarse counts do not control H

**Statement (paper proof).** Through all sufficiently large odd primes
p there are disjoint P,Q contained in the SAME parabola
C_p={(t,t^2 mod p):0<=t<p}, with k=p/4+O(1), equal counts in each
of the nine 3x3 cells, disjoint signed integer difference supports,
and H=<D_P,(D_P-D_Q)^2>=Theta(p^4).
Consequently these matching/turnover hypotheses alone do not imply
H<=C p^3(log p)^B for any fixed C,B. This concerns a particular
matching reference; existence of a better reference remains open.

Construction: in cell (i,j), sort its N_ij curve points by x and let
m_ij=floor(N_ij/4). Select ranks [s_i m_ij,(s_i+1)m_ij) for P and
[r_i m_ij,(r_i+1)m_ij) for Q, where

    s=(3,1,0), r=(0,2,3).

The blocks in a cell are disjoint. A parabola is cyclic Sidon: an
ordered nonzero difference (d,e) determines t+u=e/d and t-u=d,
so determines its ordered pair. Therefore disjoint point sets on this
curve have disjoint signed difference supports even modulo p, hence
also over the integers. Thus a=2n, Qnorm=4n: maximum turnover.

For completeness, rectangle discrepancy is O(sqrt(p)log^2 p).
Expand each coordinate interval indicator in characters of F_p.
The constant term gives area/p. Nonconstant quadratic sums have
absolute value sqrt(p), by squaring and summing the difference
variable; purely nonconstant linear sums vanish. The product of the
two interval Fourier l1 norms is O(p^2 log^2 p), while Fourier
inversion has factor p^-2. This proves the uniform discrepancy used
here, including rectangles with moving endpoints.

It follows that the normalized empirical measures p^-1 sum_P delta_(w/p)
and p^-1 sum_Q delta_(w/p) converge respectively to

    1_{I_s}(x) dx dy, 1_{I_r}(x) dx dy, 0<=y<=1,
    I_b = union over i=0,1,2 of [i/3+b_i/12, i/3+(b_i+1)/12].

Indeed N_ij=p/9+o(p); uniform rectangle discrepancy identifies each
within-cell rank threshold with the indicated x quantile. Both
limiting measures have mass rho=1/4. Integrating x and x^2 exactly gives

    Var(I_r/rho)-Var(I_s/rho)=1/9.

At Y=(y,0), with the Fourier convention exp(i Y dot w/p), this yields

    |hat(1_Is)(y)|^2-|hat(1_Ir)(y)|^2=y^2/144+O(y^4)>0

for fixed sufficiently small nonzero y. The transforms converge
uniformly on compact Y sets (bounded support gives uniform Lipschitz
control). Thus on a fixed small Y-ball around such a point,
D_P(Y/p)>=c p^2 and D_P(Y/p)-D_Q(Y/p)>=c' p^2.
The corresponding torus region has area of order p^-2, so its
contribution to H is at least c''p^4. Everywhere D_P>=-k and
||D_P-D_Q||_2^2=4n. The remaining contribution is at least
-4kn=-O(p^3). Finally H<=||D_P||_infinity*4n=O(p^4).
This proves the statement. No sampled minimum enters the proof.

Exact FLINT cubic counts at p=61,127,251,509,1009 corroborate the
construction; independent scalar recounts cover p<=251 only. Their
H/p^3 values are approximately .01123,.02119,.02813,.04166,.05769.
These finite values alone would not prove asymptotic growth. The
profile argument does. Its particular one-reference certificate has
only a constant-order M lower bound asymptotically; this says nothing
comparable about the true M, or about optimized references.

## 3. Complete small frontiers and direct optimization

Actual P has k=(p-1)/2 and lies on C_p. References Q may be ANY
cyclic-Sidon k-point sets in the p-box with the same g x g cell counts
and integer positive-difference overlap <=floor(3n/4). Five actual
p11 shapes are prefix, quadratic_arc, random, spread, endpoint;
the saved JSON specifies every point and seed 20261104.

All 21 coarse configurations (p11,g=3,5,7 and p31,g=5,7 with the
stated shapes) have exact-checked references. Time-limited p31
solutions are feasible witnesses only. For all 30 p11 configurations
(five shapes, g=3,5,7,9,10,11), a separate complete enumeration gives
the minimum H at EACH coupling a. This replaces solver optimality
and infeasibility claims by exact integer checks. All g11 families
are empty under the overlap condition; every spatial cell is then
a singleton, so its counts force the actual P.

To choose by certificate rather than overlap, let z_w indicate a
positive reference difference, S be the actual signed differences,
and C=1_S*1_S. Exactly

    H=H0-4 sum_w C(w)z_w
       +2 sum_{w,v}[1_S(w+v)+1_S(w-v)]z_w z_v,
    a=2(n-sum_{w in S positive} z_w).

At target K=k/2, maximize twice the determinant margin
2a^2-kH-k^2a. Gurobi's six returned optima agree with the independent
full enumerations, including the time-limited random coarse case.

| Actual p11 shape | g3 exact best margin | g7 exact best margin | g7 admissible references |
|---|---:|---:|---:|
| prefix | 240 | -72 | 69 |
| quadratic_arc | 102 | -92 | 28 |
| random | 172 | -272 | 55 |
| spread | 238 | -132 | 170 |
| endpoint | 60 | -138 | 119 |

Thus individual g3 references give M>5/4 in every shape, while NO
single g7 reference gives a strict certificate at that target. A
negative optimum does not refute a smaller positive constant. Also,
maximizing the margin at a missed fixed target need not maximize the
positive root: retain the baseline witness if its root is better.

## 4. The attempted repair succeeds: signed reference spans

The preceding failure motivated a different certificate, which was
actually tested. Enumerate every admissible fine-grid reference and
write q_j=D_A-D_Bj. Allow

    r=s+sum_j t_j q_j,
    T_ij=2<(D_A+5/2)b_i b_j>, b_0=1, b_j=q_j.

This T is an EXACT integer symmetric matrix: T00=5,
T0j=2a_j, Tij=2H_ij+5Q_ij. An integer vector v with v^T T v<0
proves M(A)>5/4 on the whole scalar circle. The mixed cross terms
make this stronger than choosing a reference or averaging the
individual moment matrices.

**Finite exact result:** all FIVE g7 classes have negative integer
forms despite the strictly negative best individual margins above.
Their forms are respectively

    -46612153594347, -3820258789567, -9797265628527,
    -47999218751724, -44635233281023.

Eigenvectors only proposed coefficients; rounding produced saved
integer vectors. A separate program reconstructed each scalar
polynomial and squared it with exact integer FLINT arithmetic,
independently recovering these negative forms.

At g9 and g10, all TEN full reference spans instead have exact PSD
matrices at K=5/2. Rational Schur complements, including exact checks
on zero residual blocks, prove this; small floating eigenvalues are
not used to exclude witnesses. This excludes a strict negative-form
certificate at THIS target in THESE finite spans. It is neither an
upper bound on the actual M nor an exclusion of other q, other
profiles, smaller targets, or asymptotic constructions.

Five concrete scalar A files, each n=10, are saved with max(A),
SHA256, base67, and the global square-identity upper M<=5/2 in
span.json. The span witnesses give strict lower M>5/4. No minimizing
angle or numerical global minimum was needed or is asserted.

## 5. What changed, and what remains

Matching g x g counts permits pairing points with displacement at
most sqrt(2)p/g. At theta=Y/p,
|F_P-F_Q|<=sqrt(2)k||Y||/g. On bounded Y regions, the resulting
worst-case front cost scale is O(p^4/g^2). Thus g of order sqrt(p)
is a natural sufficient scale for controlling this particular front
estimate. This is NOT a necessary lower bound, a guarantee of
reference existence, or a bound on H over the rest of the torus.
Arbitrary dense selections can have other Fourier spikes.

**Distance to full result:** we refuted an automatic coarse-profile
cost implication and showed that a one-reference obstruction can
disappear in the full signed span. No exponent or unrestricted
Chowla bound improved. The universal missing ingredient is still
a quantitative adaptive mixed certificate for arbitrary A.

**Kill / continue / pivot:** stop overlap-only reference searches and
claims that any coarse-matching reference has small cost. Continue
the endpoint with signed combinations selected by their mixed
moment matrix. The next discriminating estimate is a uniform
negative-eigenvalue/coupling bound at critical growing resolution,
allowing adaptive spectral constraints to control non-origin spikes.
First test actual adversarial phase-selected fibers, then seek a
proof or exact obstruction; do not extrapolate the p11 recovery.
This is the existing CHAIN(c) mixed-direction problem in a concrete
family, not a newly solved inverse theorem. Keep non-cone
growing-depth PD/Riesz rounding as the distinct construction line.

## 6. Reproduction and scope of verification

All research computation ran on Dirichlet. Commands use
`src/dirun.sh -c 2 -m 8 -t 480 python src/SCRIPT.py`:

- cstar_reference_entropy.py, also with --fine: results.json, fine.json.
- cstar_coarse_counterfamily.py: counterfamily.json.
- cstar_reference_miqp.py: miqp.json.
- cstar_reference_entropy_verify.py: verification.json; 87 scalar
  cubic witnesses, all 30 exhaustive p11 frontiers, six exact MIQP
  comparisons, counterfamily cubic recounts through p251.
- cstar_reference_span.py: span.json and five actual frequency files.
- cstar_reference_span_verify.py: span_verification.json; five
  independent scalar negative forms and ten rational PSD tests.

Data directory: ../experiments/reference_entropy_2026-10-20/.
All jobs are terminal. The initial verifier output was truncated by
the tool; its completed PASS file and absence of a live launcher
were checked before continuing. A requested separate proof/Lean
reviewer launch failed because the configured default model was
unavailable. No independent-agent, Lean/kernel, or priority claim.
The user paused the goal after the final span verification passed.
The user subsequently requested a remote push; this checkpoint packages
the completed work. Integration into the older research indexes remains
unfinished.
