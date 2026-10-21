# Boolean boundary tests, coupled recovery, and full-space certification

2026-10-21. GOAL.md remains active. The previous goal-setting turn made
progress by updating authoritative instructions; this continuation performs
an actual derive–falsify–pivot–certify cycle. Full Chowla, L25 and OP140
remain open. One internal GPT-6.1 Sol/MAX advisor independently checked
the paper arguments below; no external review, Lean check or priority claim.

Conventions: normalized circle measure, D=2f_A, n=|A|, K=-min D,
a=<D,q>, Q=<q²>, H=<D,q²>. The existing determinant condition is
Q*K²+H*K-a²>=0. A universal construction of properly scaled signed
witnesses is still missing.

## 1. A genuine Boolean boundary estimate, and the bridge it cannot supply

For S=+/-A of size m=2n, put N=D_-, mu=<N>, v=<N²>,
r_S(h)=|S intersect(S+h)| and

    B_N=sum_h |hat N(h)|²*(m-r_S(h)).

The advisor proved the torsion-free lower bound

    B_N>=t*v-t²*mu²,       every integer 0<=t<=m.

The ordered-pair monotone-chain proof is complete in the
[boundary note](advisor_boolean_boundary_2026-10-21.md). Under lowK,
v<=K*mu bounds its optimized lower by m/2, whereas the available PSD
upper W=sum_{h in S}(m-r_S(h)) is at least m²/4. This comparison is
automatically compatible and gives no flatness bound.

An attempted O(n), or O(K*mu), upper bridge is not merely unproved:
it is false. The existing no-carry Sidon-difference control, inside
K<=2sqrt(n), has max_{h!=0}r_S(h)<=2(k-2),
Var(D_-)>=k²/10000, and B_N>=k^4/20000. The advisor's proof checks
all root-difference patterns and exact moment constants. This tests a
prospective arbitrary-support principle; it is not another effort to
improve the already known Chowla bound for that family.

Selected-frequency odd translations are also not a new escape: the
root-space triangle identity gives H>=-2Q for all such witnesses.
Full odd-band and mixed-coupling methods remain available.

## 2. A signed pivot is tested against every shift and refuted

For every Boolean A and integer z>=1 the boundary notch

    u_z=D*(1-cos(zx))+1_A(z)

has exact mean zero and a_z=m-r_S(z), Q_z<=2a_z. Its mixed cost is

    H_z=(3/2)hat(D³)(0)-2hat(D³)(z)
          +(1/2)hat(D³)(2z)+2*1_A(z)*a_z.

Automatic coupling/norm does not make this restricted formula universal.
Use two existing positive-front blocks: full cyclic (Q0,k,1) Sidon B,
an h=floor(3k/4) subset B', their integer difference supports A_1,A_2,
and A=A_1 union L*A_2, L>6(Q0-1). The union is Boolean and has
K<=k+h<=2sqrt(n) for k>=56.

The lead derived and advisor checked a uniform ALL-INTEGER-z obstruction:

    a_z>=n/4,
    Q'_z<=8n,
    H'_z>=n²/2048,                     k>=8192,

where u'_z=(n/a_z)u_z. Only cost fails; coupling and norm are already
on scale. Each single-notch determinant produces a lower bound on K
of at most2048. This is a cap on that certificate, not on actual K.

The proof requires no phase search. Three-sum Cauchy--Schwarz gives
hat(D_i³)(0)>=k_i^6/(3Q0)-4k_i³+3k_i²>=k^4/384.
The separated low residue/divisible-axis/mixed cases then give
H_z>=k^4/512 for EVERY z. See Sections7–8 of the boundary note for
the complete coefficient expansion, constants and coupling bound.

## 3. Positive changed mechanism: signed certificates combine across gaps

For arbitrary finite mean-zero D_0,D_1,q_0,q_1, with D_0 of degree X0
and q_0 of degree B0, let L be a positive INTEGER satisfying

    L>max(2B0,X0+B0,X0).

Then D=D_0(x)+D_1(Lx), q=q_0(x)+q_1(Lx) have EXACTLY

    a=a_0+a_1,       Q=Q_0+Q_1,       H=H_0+H_1.

All four mixed cubic terms vanish by frequency separation and the
mean-zero conditions. No high-block degree cap is imposed. Iteration
preserves the SAME beta>=0,gamma>=0: block witnesses with
a_i=n_i,Q_i<=beta*n_i,H_i<=gamma*n_i^(3/2) produce such a witness
for the union, since sum n_i^(3/2)<=n^(3/2).

Even a low-block witness alone retains a,Q,H when all added frequencies
exceed twice its degree. The canonical full Sidon block has the recorded
proved L1>=c k (MZ/L6 argument, independently rechecked by the advisor),
so its broader VP witness gives a properly scaled certificate for the
two-block control. Thus the all-z failure is a restriction failure;
it does not defeat the unrestricted certificate programme.

This is a closure lemma for genuinely separated supports, not a theorem
that arbitrary supports admit such a decomposition. Prior L=Q0 choices
need not satisfy the witness-band separation. L=Q0³ does, and larger
scales can be selected in the many-block construction when needed.

## 4. Full-space upper certificates, with the cutoff error counted

The lead proved and advisor independently checked a second positive lemma.
If w=D+lambda>=delta>0 globally, define

    J_inf=sup_{mean q=0}(2<D,q>-<wq²>)
         =lambda-1/<1/w>.

For ANY finite cosine q of degree B, E=2<D,q>-<wq²> and
r=P0(D-wq) give

    E<=J_inf<=E+||r||²/delta.

The residual includes EVERY frequency through B+X, X=max A. Counting
only the interior frequencies proves a finite-band upper bound, not
an unrestricted one. The same exact FLINT product and independent
signed Python product now decode the exterior tail in
src/cstar_inverse_residual.py. All older finite-band fields retain
their original meaning; new full_L2 fields explicitly report the
broader bounds.

A finite-rank Laurent/Toeplitz boundary argument also proves

    0<=J_inf-J_B<=2X*lambda²/[(B+1)delta].

At lambda=4sqrt(n), K<=2sqrt(n), this is
16X*sqrt(n)/(B+1). It gives a universal approximation rate, not a
universal Boolean lower bound. The residual certificate is much sharper
on the selected controls. [Complete audit](advisor_fullspace_residual_2026-10-21.md).

## 5. Exact/interval evidence, scope and runtime

All computations ran on Dirichlet through dirun.sh. No RunPod deployment
or new GPU spending. The final two verifier runs and residual run are
terminal/PASS; earlier output-directory and Arb/Fraction conversion
errors were corrected before the successful saved runs.

- Six no-carry root cases k=4,5,6,8,10,12: every popular-difference
  threshold, maximum overlap, exact fourth moment and a separate
  signed triangle-convolution calculation agree.
- Three small lowK two-block controls: every potentially nonconstant
  cubic coefficient is checked through shifts543,6066,109434;
  selected q_z squares are independently counted by sparse rational
  convolution. These verify formulas; the asymptotic positive-cost
  theorem is a paper result, not inferred from these small cases.
- Singleton analytic control: at lambda4,B2, finite J=8/15 but
  J_inf=4-2sqrt(3). The exact finite optimizer has zero interior
  residual and exterior (2/15)cos(3x); its full upper is121/225.
  Five exact tridiagonal controls check the rank-boundary inequalities.
- Reused n496 and8128 inputs now have full-L2 normalized brackets
  [0.205283186,0.205719643] and [0.170095211,0.170231911]. These
  quantify the entire variational space; they are not a trend search,
  L25 proof, or stronger universal exponent.
- A lowK n706 two-block union inherits the saved n496 broader witness
  with exactly unchanged a,Q,H. Independent signed Python products
  recheck it. An additional high-block witness checks all additive
  closure moments directly; no uniform claim is made for that
  elementary high-block witness by itself.

Reproducible artifacts:

    src/cstar_boolean_boundary_verify.py
    src/cstar_inverse_residual.py
    experiments/boolean_boundary_2026-10-21/results.json
    experiments/boolean_boundary_2026-10-21/inheritance.json
    experiments/fullspace_residual_2026-10-21/results.json

## 6. Global review and next discriminating question

Stop the generic leakage-versus-PSD comparison, the small-leakage repair,
selected-frequency odd translations as a universal remedy, and the
single-notch sufficient-cost claim. None survives as a route to full Chowla.
Do not enlarge successful canonical-control sweeps or fit new constants.

Continue unrestricted signed cost and OP140. The positive closure proof
identifies exactly what becomes uncontrolled without gaps: mixed terms
<D_i,q_j²> and <D_i,q_j q_l>, not the diagonal coupling or norm.
The next actual derivation must retain those signed cross terms on
arbitrary overlapping supports, or produce a genuinely different Boolean
input. Absolute-value suppression of every cross term is not licensed
by this cycle and risks repeating the recorded weak-block barrier.
The full-space residual upper is now available to distinguish a bad
finite search space from a genuinely weak unrestricted input.

The independent all-circle construction track remains open; no new
counterconstruction upper bound was obtained here. This cycle's two
falsifiers reject proposed universal proof steps, not Chowla itself.
