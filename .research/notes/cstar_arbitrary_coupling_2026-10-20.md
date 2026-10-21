# Arbitrary-support witness spaces and direct coupling constraints

2026-10-20. Resumed CHAIN(c) research after the user's strategy revision.
Previous research goal turn: progress (reference-entropy checkpoint608cd3d).
Intervening strategy discussion changed priorities; this pass attempts the
unrestricted witness problem. Full Chowla remains OPEN. No universal
inequality or exponent has improved in this pass. No manuscript,
specialist-review/submission work, or remote push is part of this pass.

## 1. A concrete candidate which takes arbitrary A as input

Let A={a1<...<an} be ANY distinct positive integer set, D=2f_A.
Put a0=0 and

    R_j = sum_{i=0}^{j-1} [exp(i(aj-ai)x)+exp(-i(aj-ai)x)],
    V_A = span{1,D,R_1,...,R_n}.

The R_j are increments of |1+sum_{i<=j}exp(i ai x)|^2-(j+1).
An optional larger space adds suffix autocorrelation increments;
the two spaces are recorded separately. Their frequencies lie in
{0} union ±A union (A-A), with no density, maximal-frequency,
finite-field, or prescribed-law hypothesis on A. This is a concrete
growing subspace of the existing mixed-certificate problem, not a
representation theorem for arbitrary A by structured constructions.

Numerically minimize <D r^2>/<r,r> over V_A using its Fourier Gram
matrix. Round the resulting coefficients to integers. The certificate
is the exact integer scalar Rayleigh form, independent of the
eigensolver's rank cutoff. No optimality or exact-nullity conclusion
comes from floating eigenvalues. An independent checker rebuilds
prefix autocorrelations and scalar shifts without importing the
producer or its moment matrices.

Fifty saved witnesses cover19 Boolean sets in both spaces and six
weighted controls in both spaces. The Boolean probes include dense
near-optima, intervals, sparse sets, root differences, small balanced
layers, the genuine forced-plateau examples, and three cyclic-cone
lifts. These are tests of one proposed arbitrary-support witness
algorithm, not further asymptotic exclusions of those constructions.
The small balanced-layer cases do not test the known asymptotic
weak-W1 diagonal. No exhaustive search over A is claimed.

## 2. Exact calibration: positive coefficients miss signed cancellation

For A={1,...,n}, write q=sum_{j=1}^n c_j(e_j+e_-j), c_j>=0,
S1=sum c_j, Q=2sum c_j^2, T=sum_{i+j<=n}c_i c_j.
Then, exactly,

    a=2S1, H=2S1^2-Q+2T,
    [Q K^2+HK-a^2] at K=2 = 2Q+4T>0.

Thus EVERY such nonnegative-coefficient mean-zero q, optimized with
a free constant in span{1,q}, has positive determinant root below2.
This cone of certificates cannot certify M>1, however large n is.
The bound is asymptotically sharp within the cone: put c_j=1 on
the upper half and0 elsewhere, giving T=0 and a root tending to2.
This is a calibration of the signed-witness issue, not a new proof
of the already settled interval Chowla case or a new universal route.

For n=2m, let D_j=2sum_{a=1}^j cos(ax) and take

    q=4D_(2m)-7D_m.
    a=2m=n, Q=50m=25n, H=-4m^2-26m<0.

The Rayleigh inequality H+KQ>=0 yields

    K>=(2m+13)/25, M>=(n+13)/50.

The three moments follow by direct Fourier counting; eight independent
integer checks cover m=1,2,3,4,8,16,32,64. This gives an unbounded
advantage over the entire preceding positive cone. Only TWO signed
directions suffice here: the example does NOT prove that a growing
number of directions is necessary in general. Universal W1 is already
known to fail on other families; this does not reopen that claim.

## 3. Spectral optimization alone did not enforce the actual target

Remove the constant term of each numerical Rayleigh witness and
measure coupling after normalization Q=n. On the plateau, the prefix
coupling a/n falls from about .245 at n35 to .0636 at n337 despite
strong negative Rayleigh bounds. The finite data do not prove a limit,
but show why an optimized eigenvalue cannot be advertised as a
uniform macroscopic-coupling result. All exact a,Q,H are saved.

We therefore actually attempted the original constrained objective:

    a=<D,q>=n, Q=||q||^2<=25n, minimize H=<D,q^2>.

This is implemented on the mean-zero part W of each V_A. Since D is
in W and ||D||^2=2n, every feasible q has the unique decomposition

    q=D/2+u, u perpendicular to D,
    Q=n/2+||u||^2,
    H=<D^3>/4+<D^2,u>+<D,u^2>.

Thus the proposal is a quadratic minimization on a ball in D-perp.
In orthonormal coordinates write it as c+2b^T u+u^T C u with
||u||<=R. Diagonalize C. A multiplier lambda>=max(0,-lambda_min(C))
gives u=-(C+lambda I)^-1 b, with a scalar equation ||u||=R when
active. At a singular endpoint the component in the bottom eigenspace
fills the remaining radius (the usual hard case). The sufficient
optimality identity is elementary:

    objective(v)-objective(u)
      =(v-u)^T(C+lambda I)(v-u)+lambda(||u||^2-||v||^2)>=0.

This describes the exact finite mathematical optimization. Our
numerical implementation proposes a vector, not a certified optimum.
It uses Q<=24n, leaving room for exact reconstruction. With dyadic
rounding scale B, raw polynomial p/B and raw integer coupling a_raw,
replace it by

    [2n p+(nB-a_raw)D]/(2nB).

Its coupling is EXACTLY n. Recheck Q<=25n and H by integer arithmetic.
This does not assume a frequency ceiling independent of A.

**Finite exact outcome:** all20 trials (ten Boolean supports in both
spaces) have a=n, Q<=25n and H<0. They include the plateau n337,
root-difference n66, balanced n210 and cone-lift n192 controls as
well as arbitrary sparse/dense inputs. Their exact rational quadratic
certificates are independently checked. Consequently each tested
support has M>=sqrt(n)/10 by this criterion. No assertion that the
same estimates hold for every A is inferred. The numerical cost
values and finite optima are not promoted to analytic inequalities.

## 4. An explicit two-profile weighted control and a failed Booleanization

This is a deterministic realization of the EXISTING P61 escape
mechanism, used as an adversarial control, not claimed as a new
obstruction theorem or a genuine Boolean construction.

Let L=X+1, w_k=1-k/L, p_k=phi(w_k^2),
phi(z)=(1-sqrt(1-z))/2, and

    c_k=p_k+r_k,
    r_k=w_k if 5 divides k, and -w_k/4 otherwise.

The period-five r/w has mean0 and second moment1/4. Therefore the
first two weak coefficient profiles of c are p and p^2+w^2/4=p,
exactly the two Boolean profiles. Yet c is not Boolean or even
confined to [0,1]. Its squared coefficient mass
m_X=sum c_k^2 is asymptotic to d X, d=(1-pi/4)/2>0.

The p profile is positive definite (positive Catalan power series
in the PD sequence w^2, with p0=1/2), so sum p_k cos(kx)>=-1/4.
Writing F_L=1+2sum w_k cos(kx), the r polynomial is

    [F_L(x-2pi/5)+F_L(x+2pi/5)
     +F_L(x-4pi/5)+F_L(x+4pi/5)-4]/8>=-1/2.

Thus the weighted M is at most3/4 on the ENTIRE circle. The saved
rational coefficients floor only p with denominator16384L, giving
the exact upper M<=3/4+X/(16384L). The floor is verified separately
by rational radical comparisons, not by the producer's square root.
The Fejer-only weighted controls separately have M<=1/2.

For ANY witness of this weighted sum with a=m_X, Q<=beta*m_X,
positivity at the known valid budget K0 gives

    H>=m_X^2/K0-beta*K0*m_X.

Hence H/m_X^(3/2) diverges as X grows for every fixed beta. A proof
of the desired uniform cost bound cannot use only these two raw
profiles and positivity: it must use further Boolean information.
This follows from the same exact mixed inequality, not from a grid.

As a separate construction attempt, nearest binary rounding fails
explicitly. If 5 does not divide k, c_k<=w_k/4<=1/4. On multiples
of5, p(w)+w is increasing, and it exceeds1/2 precisely when
w>=1/sqrt(5). Thus the rounded frequencies are an initial arithmetic
progression {5,10,...,5m}, m~(1-1/sqrt(5))X/5. This remains an
arithmetic progression after the downward rational rounding.
At x=3pi/[5(2m+1)], the Dirichlet formula gives

    M>2m/(3pi)>7m/33, while M<=m globally.

Its normalized ratio diverges. This kills THIS rounding rule; neither
L2 rounding error alone nor this example excludes other Booleanizations.
Saved controls have m7,14,28, with actual frequencies and bounds.

## 5. Strategic review and the exact next task

Distance: the arbitrary-support witness proposal is now explicit,
Gram-normalized and tested on its actual a,Q,H constraints. The
positive-cone calibration explains an unbounded signed gain; the
weighted control establishes exactly which claimed estimates would
be false without Booleanity. No universal bound has been proved.

Opportunity cost / decision: stop optimizing unconstrained negative
eigenvalues as a proxy for macroscopic coupling. Do not enlarge the
specialized construction catalog. Continue the fixed-coupling cost
problem on arbitrary A, allowing positive H=O(n^(3/2)); H<=0 in the
finite probes is a bonus, not a premise we now require universally.

Precisely, with W_A the mean-zero prefix space, define
T_beta(A)=min{<D_A,q^2>:q in W_A,<D_A,q>=n,||q||^2<=beta*n}.
The set is always nonempty (q=D_A/2) and compact after removing
linear dependencies. A uniform T_25(A)<=C*n^(3/2) would imply
M(A)>=[sqrt(C^2+100)-C]*sqrt(n)/100. This concrete sufficient
candidate is unproved and stronger than simply asserting Chowla.

First concrete next derivation: expand H(D/2+u) in the prefix
autocorrelation basis for arbitrary A and identify a Boolean estimate
on the aggregate signed cross terms sufficient to bound the constrained
minimum. Coordinatewise positive-cost bounds already fail on intervals.
Any proposed estimate must explicitly fail on the period-five weighted
control and survive the Boolean plateau; those are adversarial gates,
not substitutes for proving the estimate. The growing-prefix uniform
claim itself may be false; a verified counterfamily would require a
different adaptive space rather than disposal of Chowla.

Independent construction work remains required to obtain an all-circle
upper bound for a genuine Boolean family; the explicit weighted control
is not such a family. External consolidation/review remains deferred
by the user. No Lean/kernel or independent-agent audit is claimed.

## 6. Reproduction

All computation ran on Dirichlet via
`src/dirun.sh -c 2 -m 8 -t 480 python src/SCRIPT.py`.
Scripts: cstar_ordered_prefix.py (also --extra),
cstar_ordered_prefix_verify.py, cstar_coupling_ball.py,
cstar_coupling_ball_verify.py. Data:
`../experiments/ordered_prefix_2026-10-20/`.
Seed20261023 for the sparse set; all other inputs are explicit or
saved prior Boolean sets. Files contain actual frequencies, n, max A,
integer/rational polynomials, achieved global M LOWER certificates,
and weighted or trivial global upper bounds. No minimizing angles
are estimated for the eigenvalue probes. No Epoch output is claimed.

An extra-suite checkpoint first failed because a square-root variable
overwrote the output-directory variable. The failed job was terminal
before repair/restart; its TypeError and scope are preserved here.
Both final verifiers exited0/PASS:50 scalar witnesses, eight interval
checks, three periodic controls, and20 fixed-coupling scalar checks.
Singleton and two-frequency smoke tests also passed after adding the
zero-dimensional ball boundary case; the singleton has exact a=1,
Q=1/2,H=0. This does not enlarge the20-case data claim.
All jobs from this pass are terminal. No universal theorem follows
from these verifier counts.
