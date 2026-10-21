# Independent internal advisor review, 2026-10-21

Scope: independent paper audit and source-code review by the single internal
"PhD Advisor" AI subagent. This is not an external credentialed review or a
Lean/kernel check. I read AGENTS.md, the Number Theory research skill, current
STATE/CSTAR/ROUTES material, the two October 20 coupling/resolvent notes, the
resolvent producer/checker and coupling-ball implementation, and the Chowla
portion of the supplied GPU proposal. I also reviewed the new Fourier-kernel
source during its bounded pilot. I launched no research computation, VM job,
GPU worker, or external communication, and edited only this note.

The original sustained research goal remains paused. The separately authorized
work is a QUICK kernel pilot/review, using roughly the user's existing $7 of
RunPod credit. Recommendations below do not independently resume the campaign.

## Exact target and present verdict

For every nonempty finite set A of distinct positive integers, put

    D(x)=2 sum_{a in A} cos(a*x), n=|A|, K=-min_{x in R} D(x)=2M(A).

All integrals here are normalized by 1/(2*pi). The desired proof is an absolute
c>0 with K>=2c*sqrt(n) for EVERY A. The alternative is a genuine Boolean family
with n tending to infinity and all-circle upper bounds K=o(sqrt(n)), together
with effective parameter control for an Epoch generator. No such resolution is
established by the material reviewed.

Verdict:

* The stated full-L2 resolvent optimizer and flatness implications are correct
  as paper arguments, with the qualifications below.
* The saved N50 result is an exact finite witness-space separation. It does
  not refute square-root strength of W2 at a smaller absolute constant and
  does not improve a universal exponent.
* The narrowly scoped Fourier-kernel pilot is justified. It measures an
  operator implementation and throughput. It does not yet test the proposed
  universal optimized-cost inequality.
* A uniform fixed-coupling/norm/cost theorem is stronger than Chowla in a
  meaningful way: on bounded-ratio inputs it entails L1 flatness. This must
  remain an explicit mathematical hypothesis to prove or attack.

## 1. Resolvent optimizer: independent derivation

Since A is a genuine nonempty set of positive frequencies,

    integral D=0, integral D^2=2n, K>0.

For lambda>K, define

    w=lambda+D, h=1/w, I=integral h, J=integral h^2,
    T=lambda*I-1, q=n*(I-h)/T.

Strict convexity of t -> 1/t gives I>1/lambda and T>0. The identities

    integral q=0,
    <D,q>=n,
    w*q=n+(n*I/T)*D,
    Q(lambda)=integral q^2=n^2*(J-I^2)/T^2,
    integral w*q^2=n^2*I/T

follow directly from D*h=1-lambda*h. For any other real mean-zero v with
<D,v>=n, the two linear constraints cancel the weighted cross term, giving

    integral w*v^2
      =n^2*I/T+integral w*(v-q)^2.

If Q(lambda)=beta*n and Q(v)<=beta*n, then

    H(v)-H(q)
      =integral w*(v-q)^2+lambda*(Q(q)-Q(v)) >=0.

Here lambda>K>0, so this proves global minimality and uniqueness over the full
real L2 space. The cost is exactly

    F_beta(A)=n^2*I/T-lambda*beta*n.

The strict monotonicity calculation in the source note is also sound. Let
c(lambda)=n*I/T. Differentiating w*q=n+c*D and pairing with q' gives

    <q,q'>+integral w*(q')^2=0,
    Q'(lambda)=-2 integral w*(q')^2.

The derivative lies in the constraint tangent space because integral q'=0
and <D,q'>=0. Equality would force q'=0; the differentiated stationarity
then gives q=c'*D. The coupling forces q=D/2. Original stationarity would
make D^2 affine in D, which is impossible for a nonconstant continuous
function on a connected circle. Therefore Q'<0.

The endpoint arguments need analyticity, which holds here. At infinity,
expanding 1/(lambda+D) gives q -> D/2 uniformly and Q -> n/2. Near K, a
minimum has derivative zero and bounded second derivative, so locally
D+K <= C*(x-x0)^2. Thus I diverges as lambda decreases to K. The minimum
set is finite because D is a nonconstant trigonometric polynomial.
The probability densities h/I concentrate on arbitrarily small
neighborhoods of that finite set. Cauchy-Schwarz on those neighborhoods
then forces J/I^2 -> infinity. Since T/I -> K, Q -> infinity. Hence every
beta>1/2 has one and only one lambda>K.

No numerical quadrature is needed for this paper theorem. Conversely, the
saved numerical lambda/I/J are not thereby certified: the integral formulas
still need rigorous evaluation if a numerical optimum is to be asserted.
Sharp wells can be missed by an otherwise large FFT grid.

The rational trigonometric approximation argument is legitimate: first use
beta'<beta, approximate in L2, and repair the coupling with a small multiple
of D. Boundedness of D makes Q and H continuous in L2. No uniform witness
degree follows. For weighted inputs one must replace n by the intended
coupling parameter and replace n/2 by a^2/||D||_2^2; the Boolean normalization
cannot silently be retained. The weighted controls use effective squared
coefficient mass, which makes their separate normalization consistent.

## 2. Fixed coupling really does require flatness

Write L=||D||_1 and mu=L/2=integral D_+=integral D_-. For any real q, with
a=<D,q>, P=integral D_+*q^2 and N=integral D_-*q^2,

    |a| <= sqrt(mu)*(sqrt(P)+sqrt(N)),
    H=P-N.

If a>=alpha*n, Q<=beta*n, H<=gamma*n^(3/2), and K<=C*sqrt(n), then

    N<=KQ<=C*beta*n^(3/2),
    P<= (gamma+C*beta)*n^(3/2),
    L >= 2*alpha^2*sqrt(n)
         / (sqrt(gamma+C*beta)+sqrt(C*beta))^2.

This is the claimed quantitative flatness implication. It is correct. It
does not follow merely from knowing a square-root lower bound for K.

For the converse let s=sign D, m=integral s, and q=n*(s-m)/L. The zero set
of D has measure zero, so s^2=1 almost everywhere. Directly,

    integral q=0, a=n,
    Q=n^2*(1-m^2)/L^2 <= n^2/L^2,
    H=-2*m*n^2/L <= 2*n^2/L.

In particular, if L>=sqrt(n/beta), then the unrestricted full-space cost
satisfies

    F_beta(A) <= 2*sqrt(beta)*n^(3/2).

This last form is a useful pilot discriminator. A genuine certified
full-space cost exceeding that threshold forces small L1. A large cost
found only in a restricted bandwidth does not have that implication.

Small L1 alone does not oppose Chowla: ordinary intervals have small
L1/sqrt(n) and large K/sqrt(n). A candidate must be examined in BOTH
coordinates. Preserve direct negative-Rayleigh witnesses; they prove a
dip without a macroscopic coupling requirement.

## 3. A quantitative full-space cost lower bound

This is an additional derived paper inequality, useful independently of a
chosen witness basis. Suppose K0 is any rigorous all-circle upper bound
for K, and mu0 is any rigorous upper bound for ||D||_1/2. For every q with
a=n and Q<=beta*n, put B=beta*n*K0. Then

    H >= (max(n/sqrt(mu0)-sqrt(B),0))^2-B.                 (1)

Proof: N<=B and P=H+N<=H+B. The previous Cauchy-Schwarz inequality gives

    n/sqrt(mu0) <= sqrt(H+B)+sqrt(B).

Move the second term to the left, use its positive part, and square.
No Booleanity, Fourier cutoff, or numerical optimizer is used in (1).

In dimensionless form, for

    u=mu0/sqrt(n), kappa=K0/sqrt(n),

the bound is

    H/n^(3/2)
      >= (max(1/sqrt(u)-sqrt(beta*kappa),0))^2-beta*kappa. (2)

The elementary positivity determinant separately gives

    H/n^(3/2) >= 1/kappa-beta*kappa.

Take the maximum of these two lower bounds. The L1-sensitive bound need
not dominate the determinant bound on ordinary near-optima; it is useful
when L1 is much smaller than the negative-minimum budget.

Thus a bounded-kappa family with u tending to zero defeats every fixed
beta and finite uniform upper cost constant on the ENTIRE L2 space.
It need not defeat Chowla: its actual K/sqrt(n) could remain bounded
away from zero. This is the precise distinction the pilot should retain.

For the quick kernel pilot it is sufficient to record diagnostic grid
L1/sqrt(n), clearly marked uncertified. Implementing rigorous L1
quadrature is not a prerequisite to timing this operator. If (1) is later
used as a certificate, both input upper bounds must be certified. A
generic rigorous quadrature error follows from |D'|<=2*sum(A), but it
can be very inefficient for widely spaced frequencies.

## 4. What the finite separation establishes

The reported exact certificates have coherent meanings:

* Positive definiteness of 2*B_W2+15*I gives lambda_min(B_W2)>-15/2.
  Hence no Rayleigh witness in that ENTIRE specified W2 space can
  certify K>=15/2. This is a cap on certificates delivered by that
  space, not an upper bound for the actual K.
* The degree1152 polynomial has exact a=50, Q<=1250 and the stated
  rational H. A negative determinant polynomial at the stated rational
  K proves M>3.954718245, which exceeds the W2 certificate cap 3.75.
* The exact prefix dual bounds the constrained prefix cost from below;
  a feasible broader witness with smaller H proves a cost separation.
* The independent Sturm calculation, if its saved PASS is reproduced,
  gives the separate all-circle upper M<=4.0309358. It does not certify
  the numerical full-space optimum or numerical minimizing angle.

I independently checked the mathematical interpretation and read the
producer/checker algorithms; I did not rerun their saved jobs. The
reversed Bareiss and rational Schur procedures are appropriate exact
positive-definiteness checks. The scalar Fourier moments and Chebyshev
Sturm check are independent of the floating optimizer. No fatal defect
was found in this finite logic.

Finite improvements over W2 do not imply that W2 lacks SOME universal
positive square-root constant. They also supply no asymptotic family
with R(A) tending to zero.

The trust-region code's numerical rank and hard-case tolerances may
affect how good a proposal it finds. Its exact post-checks still make an
accepted witness valid. An asserted optimum needs an independent lower
bound; a poor proposed value cannot serve as one.

## 5. GPU proposal and the bounded pilot

The proposal's cosine-coordinate formulas are correct. For
q=sum_{k in B} v_k*cos(k*x), with B a positive-frequency set,

    a=sum_{a in A} v_a,
    Q=(1/2)*sum v_k^2,
    H=(1/2)*sum_{j,k in B} v_j*v_k
       *(1_A(|j-k|)+1_A(j+k)).

If B contains A and v=1_A+z with sum_{a in A} z_a=0, then
Q=(n+||z||^2)/2. The proposal's radius ||z||^2<=3n corresponds to
beta=2. The research code used beta=25. Neither constant is supplied
by Chowla, and replacing 25 with 2 is a stronger experiment rather
than a justified mathematical simplification. The trust-region
reduction already exists in the project; reimplementing it on a GPU
would not be a new mathematical result.

The useful new engineering question is when a batched FFT action wins
over the direct/sparse operator. The lead's initial Dirichlet baseline
already reports that a 12-frequency operator at max(A)=131071 is vastly
faster by a 12x12 direct action than by a long FFT. The band case with
8192 witness frequencies is the meaningful single GPU comparison.
These timing observations were reported by the lead, not independently
rerun by this advisor.

My narrowly scoped verdict is GO after the following mathematical gates:

1. Check the hand controls A={1}, q=cos(x), H=0 and A={2}, q=cos(x),
   H=1/2. They catch the Hankel diagonal and factor-of-two errors.
2. Compare FFT actions with an independently built exact integer
   Toeplitz-plus-Hankel action on small examples.
3. With X=max(A), b=max(B), use FFT length strictly greater than X+2b
   for the cubic no-alias condition. If constructing D in an irfft
   half-spectrum by indexing A directly, also require length>2X.
4. Round/repair coupling and check a,Q,H exactly before calling a
   candidate a mathematical certificate. A throughput run needs no
   new optimized-cost assertion.

I identified the half-spectrum condition in item 3 while reviewing the
new kernel. The lead reports applying the stronger padding and adding
A={101}, B={1} as a regression control. The existing benchmark cases
were already safe; this fixed the generic small-B/large-X edge case.

One matched NumPy/CuPy throughput comparison on the large-band case,
with a newly created short-lived worker and the user's credit limit,
fits the authorized pilot. No broad support search, long norm sweep,
large provisioning effort, or certified-L1 implementation should delay
that run. The experiment's finding is implementation readiness and
dispatch, not a new universal principle.

## 6. ONE prioritized post-pilot mathematical test

Before a large optimized-cost search, attack the explicit low-ratio
flatness assertion

    For every genuine Boolean A,
    K(A)<=2*sqrt(n)  ==>  ||D_A||_1 >= sqrt(n)/5.          L25

This is a conjectural falsification target, not an asserted theorem
or a new route distinct from the current C* inverse problem. Its
constants match the existing beta=25 sign-witness budget. The exact
constant 1/5 is provisional; a single violating set would disprove
L25 as written without disproving every possible flatness constant.

Why it reaches full Chowla: ||D||_1<=2K always. If L25 were proved,
then K>=sqrt(n)/10 in its low-ratio branch; the complementary branch
already has K>2*sqrt(n). Therefore it would prove

    M(A)>=sqrt(n)/20 for EVERY nonempty Boolean A.

No density, maximal-frequency, Sidon, cone, or construction-class
hypothesis appears. A proof must use the exact Boolean coefficient
identity and a torsion-free feature; the supplied weighted controls
already exclude a proof from positivity and low moments alone.

How to falsify it: find a genuine positive distinct-integer set with
both a certified global upper K<=2*sqrt(n) and a certified L1 upper
below sqrt(n)/5. A family with bounded K/sqrt(n) and vanishing
L1/sqrt(n) would invalidate the entire uniform fixed-coupling cost
architecture, while still leaving direct Rayleigh and construction
tracks open. Conversely, finding small grid L1 with a large negative
dip is only the interval-type control and does not test L25.

For the quick pilot, collect the diagnostic pair (grid L1/sqrt(n),
achieved direct negative-Rayleigh bound/sqrt(n)) from already available
cases. Do not launch a new search while the main goal is paused.
If research is later resumed, prioritize unrestricted Boolean inputs
and exact global certificates on the Pareto-worst candidate rather
than returning to settled Sidon/cone parameter tuning.

## Handoff

Paper-audited: full-L2 resolvent optimizer, endpoint/monotonicity proof,
sign-witness equivalence on bounded-ratio classes, and inequalities
(1)-(2). Existing exact finite certificates: interpreted and source
reviewed, not rerun here. Lean/kernel-checked mathematical proofs: none. Universal exponent
improved: none. Epoch algorithm: none.

The important correction is strategic: exact witnesses provide upper
bounds on optimized cost, and small-bandwidth failure is not full-space
failure. Full-space failure can be certified by (1) only with rigorous
K/L1 inputs. It would refute a stronger flatness route, not automatically
Chowla. The independent construction track still needs a Boolean family
and an all-circle UPPER bound; a negative-Rayleigh certificate supplies
a LOWER bound and cannot play that role.

First concrete next action within current authorization: finish the
single large-band CPU/GPU operator comparison and preserve its exact
controls, timings, and dispatch conclusion. The mathematical next task
above is conditional on a later resumption of research.

## Post-pilot evidence audit: completed, worker deleted

I read the saved `cpu.json`, `cpu_runpod.json`, `gpu_runpod.json`, and
`comparison.json` under `.research/experiments/gpu_pilot_2026-10-21/`.
No additional computation was launched for this audit. The lead reports
that the new L4 worker was deleted and no pilot pod remains; I did not
independently query provider state. The reported observed credit change
was $7.4312 to $7.4120, not a separately audited final invoice.

The RunPod CPU and GPU records identify the same host, use float64,
the same seed, matching dimensions and NumPy 2.4.6; the GPU backend
is CuPy 14.2.0 on an NVIDIA L4. The summary describes warmed medians
of seven repeats, excluding setup and input transfer. It does not
preserve individual samples or establish timing variability.

All five small exact-action controls passed in both backend records.
Three are hand controls and two use integer vectors and the independent
integer Toeplitz-plus-Hankel action. The GPU's largest recorded control
error is about 3.11e-15. Exact reconstruction of the old degree1152
witness gives a=50, Q<=1250 and its saved rational H; the GPU H differs
from that exact value by about 1.09e-11. This is a numerical agreement
check against an existing exact certificate, not a new exact GPU proof.
The large benchmark actions have finiteness checks; their full outputs
are not saved for a separate CPU/GPU residual comparison.

The matched same-host large-band case has n=256, max(A)=4095, 8192
witness frequencies, and FFT length32768:

| Batch | CPU FFT median | GPU FFT median | Warmed operator ratio |
| --- | --- | --- | --- |
| 1 | 0.560 ms | 0.253 ms | 2.22 |
| 8 | 2.903 ms | 0.591 ms | 4.91 |
| 32 | 18.233 ms | 1.0005 ms | 18.22 |

These are ratios for this operator implementation and host. They are
not a comparison with every optimized CPU alternative, and the GCP
CPU batch32 value was lower, about12.36 ms. The matched-host numbers
are the appropriate primary comparison, with that environment
sensitivity retained.

The crucial qualification is residency: the recorded batch32
host-to-device transfer took20.06 ms, already exceeding that batch's
18.23 ms CPU FFT time before its1.00 ms GPU action. Large-band GPU
setup took87.1 ms, and first-call warmup is also outside the timed
medians. Therefore the pilot does not demonstrate that a one-shot
offload is faster. Repeated matvecs must reuse device-resident data
to realize the warmed advantage. The benchmark batches different
vectors for ONE fixed A; it does not benchmark batches of different
supports or complete trust-region iterations.

Dispatch is settled at the tested extremes. For the 144-frequency
case, the GPU FFT is slower than the same-host CPU FFT and direct
matrix action. For the wide-sparse 12-frequency case, CPU direct
batch32 takes about0.0027 ms against13.04 ms for the GPU FFT. Its
large GPU-versus-CPU-FFT ratio is consequently not a reason to use
the GPU there.

Specific integration recommendation, conditional on future authorized
research: retain this operator as an OPTIONAL large-band callback
for a matrix-free projected trust-region/Krylov method. When B
contains A, use P=I-1_A*1_A^T/n on cosine-coefficient vectors; the
quadratic callback is P*C*P, with the affine forcing P*C*1_A. Keep
D, masks, work arrays and repeated vectors on device, and return
only the final proposal for rational reconstruction and exact CPU
verification. A block method could use the measured batched regime;
a sequential one-vector method should be assessed against the more
modest measured batch1 gain. Keep direct/sparse CPU actions for
small frequency spaces, and do not replace the existing dense solver
merely because an FFT kernel ran faster.

Final verdict: the QUICK pilot succeeded as an operator-correctness
and dispatch/throughput experiment and should now remain closed.
It establishes no solver speedup, proof speedup, new witness optimum,
universal cost inequality, improved Chowla bound, or construction.
No additional integration work or research run was initiated here.
