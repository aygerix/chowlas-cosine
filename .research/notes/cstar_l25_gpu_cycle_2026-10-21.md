# L25 derive–test–certify cycle and the next Boolean inverse target

2026-10-21. GOAL.md is active; full unrestricted Chowla is OPEN. This is
the first integrated research cycle under that goal, with the one internal
GPT-6.1 Sol/MAX advisor. Paper arguments were independently reviewed by
that advisor; finite claims below use exact arithmetic. No Lean check,
external review, novelty claim, or universal exponent improvement.

## The useful positive reduction applies to arbitrary A

Write D=2f_A, n=|A|, X=max(A), L=||D||_1, with normalized circle measure.
The lead derived and the advisor independently checked:

    There is a real mean-zero q of degree <2X with
    a=<D,q>=n, Q=||q||_2^2<=n^2/L^2, |H|=|<D,q^2>|<=8n^2/L.

Explicitly, let F_N be the Fejer kernel with coefficients
(1-|j|/N)_+, V=2F_(2X)-F_X, s=sign D, m=<s>, and
q=(n/L)(V*s-m). The multiplier of V equals 1 through X, lies in
[0,1] throughout, and vanishes from 2X onward. Thus V*D=D gives
exact coupling and Parseval gives the norm bound. Also ||V||_1<=3,
so ||q||_infinity<=4n/L. The separate positive and negative masses
of D each equal L/2, giving the factor 8 in the cost bound.

Under L25's conjectural L>=sqrt(n)/5, this gives a=n, Q<=25n,
H<=40n^(3/2) in the FULL band {1,...,2X-1}. It does not prove L25.
It removes a bandwidth uncertainty for a sufficient witness; it does
not claim to approximate the full-space optimum in that band.
Any rigorous lower bound >40n^(3/2) on the entire band's constrained
cost would refute L25's conclusion; additionally certify K<=2sqrt(n)
to obtain an actual L25 counterexample. A failed numerical candidate
or a failed small subspace proves neither statement.

## Two overly small principles fail inside the low-ratio domain

For canonical cyclic (Q,k,1) perfect difference sets B, Q=k(k-1)+1,
let A be their distinct positive INTEGER differences. Then
n=k(k-1)/2 and D=|F_B|^2-k>=-k. Consequently M<=k/2<=sqrt(n)
on the entire circle. These are legitimate L25 adversaries.

The advisor and lead independently derived a fixed-degree scalar-space
obstruction. For every fixed d and all sufficiently large k, every
nonzero mean-zero q=P(D), deg(P)<=d, has H>0 and a^2/H<=C_d.
The entire space, including coefficients depending on k, certifies
only a bounded K. With a=n it requires H>=n^2/C_d, defeating a
universal O(n^(3/2)) cost claim for such witnesses.

The proof separates F_B=(k/Q)(1+...+z^(Q-1))+R. The root-grid samples
of R are bounded by sqrt(k), and the classical analytic
Marcinkiewicz–Zygmund sampling inequality, checked in the primary
source, controls every fixed Lp norm. For r>=3,

    <D^r>/Q^(r-1) -> mu_r,
    mu_r=(1/(2pi))*integral_R sinc(t/2)^(2r) dt.

The centered scalar H matrix divided by Q^2 tends to the positive
Gram matrix (mu_(i+j+1)). Importantly <D^2>/Q->1, not mu_2=2/3.
The explicit limiting cap is v^T H^(-1)v, v_1=1 and
v_j=mu_(j+1) for j>=2. Exact rational constants are saved through d8.

Also <D^3>/n^(3/2)~(11/5)sqrt(n), even though M<=sqrt(n).
Thus low Chowla ratio does not imply bounded normalized cubic cost.
The elementary calibration

    L >= 8n^2/(<D^3>+4nK)

does prove L25 when K<=2sqrt(n) and <D^3><=32n^(3/2), but leaves
a genuinely active high-triple branch. The same MZ decomposition
gives a positive asymptotic L1 constant in the canonical Singer
control class; it does not prove the explicit L25 constant there.

Complete proofs, dependency URL and scope qualifications are in the
[advisor derivation](advisor_L25_derivation_2026-10-21.md). This is a
test of an arbitrary-support witness principle, not another effort
to improve a settled family's square-root lower bound. It rules out
fixed-degree scalar witnesses, not rational resolvents, growing
degree, general Fourier seeds, or truncation-modified Krylov spaces.

## Exact finite separation, including a GPU-discovered witness

Source/data are in ../experiments/l25_2026-10-21/. All CPU research
ran on Dirichlet via dirun.sh. The scalar caps use FLINT integer
moments through9, independently recounted by Python integer
Kronecker convolution through9 for the two Singer cases. Fraction
Schur pivots and exact linear-system identities independently check
positivity and the inverse quadratic form. The plateau data's older
independent recount is through7, covering all d<=3 but not all d4.

| Support | n | ALL scalar degree<=4 M cap | Broader exact M lower | Exact M upper |
|---|---:|---:|---:|---:|
| canonical Singer p31 | 496 | 13.72328947... | 3018398299/200000000 = 15.091991495 | 16 |
| canonical Singer p127 | 8128 | 31.37549762... | 365845369/6250000 = 58.53525904 | 64 |

The displayed decimal caps are abbreviated; exact rational caps and
all inputs/matrices are saved in scalar_singer.json. The broader
witnesses have exactly a=n, Q<=25n, H<0. Each GPU and Dirichlet
proposal was rationally rounded and coupling repaired on Dirichlet.
FLINT square moments and independent signed Python integer products
agree, and Q*K0^2+H*K0-n^2<0 proves the stated ALL-CIRCLE lower bound.
No floating eigenvalue or sampled minimum establishes these claims.

Rigorous L1 enclosures on the same inputs come from Arb grid balls
plus the advisor-checked quadrature bound

    |grid_mean_N |D| - ||D||_1|
      <=7*ceil(sqrt(2 sum a^4))/N^2.

Its proof uses the distributional second derivative of |D| and
absolute Fourier summability. Both inputs meet L25's conclusion;
they are method-separation controls, not L25 counterexamples.
Analytic one/two-frequency checks pass. An interval with n4096 has
rigorously small normalized L1 but a large negative dip, illustrating
why a small absolute average alone does not challenge L25.

The p257/p509 probe values are diagnostics only; they supply no L25
violation and no monotone falling trend. Stop expanding that sweep.

## What the GPU actually did

src/cstar_gpu_projected.py integrates the validated FourierCost action
with a projected trust region in the full band B=1,...,2X. In cosine
coordinates, center c=1_A gives a=n, Q=n/2. Tangent vectors are
orthogonal to c; radius sqrt(47n) targets Q<=24n, leaving rounding
slack before the exact 25n check. A block begins with sampled rational
resolvents, the explicit tapered-sign seed, independent random
Fourier seeds, and Cc. Four Galerkin/Krylov steps retain vectors and
actions on device, transferring only small reduced problems to CPU.
The matrix normalization and constraint factors were advisor-audited.
Grid-resolvent starts are proposals: lambda>K is not certified there.

Dirichlet controls and the complete CPU solver passed before GPU
deployment. The single L4 run repeated both supports and produced
the exact certificates above after CPU reconstruction. On the SAME
worker, one p127 trial took0.1275s GPU versus0.3952s CPU; the first
p31 GPU trial took2.583s versus0.0343s CPU because of startup/setup.
These are single-run solver measurements, not a general speedup or
universal convergence claim. CPU remains the dispatch for small
or wide-sparse spaces. Only achieved cost is certified, not the full
band's optimum or the numerical subspace's exact optimality.

Pod jfom1hoabqgu1w was created at$0.59/hr with automatic termination,
all results retrieved, then DELETED; a follow-up list showed no
chowla-* pods. Other account resources were untouched. Conservative
charge$0.10 of the$6.50 additional budget, balance observed$7.3765.
GPU_BUDGET.json is authoritative; no worker or research job remains
active at this checkpoint.

## Decision and next exact question

The derive–test–certify–review milestone is met: a proposed universal
fixed-degree witness principle is refuted, a positive arbitrary-A
finite-band reduction is proved, and the GPU optimizer demonstrably
escapes the certified obstruction. Full Chowla and L25 remain OPEN.

Continue the Boolean inverse problem with the advisor's explicit
matrix target OP140, documented in PROOFS.md and the advisor note.
It is a computationally useful form of the SAME C* gap, not a new
independent proof. Prove or falsify the linked zero/one operator
inequality rather than enlarging successful Singer examples. Retain
direct negative-Rayleigh certificates and the independent all-circle
construction track; none is eliminated by the scalar obstruction.

Reproduction on Dirichlet (each command is a separate run):

    src/dirun.sh -c 2 -m 8 -t 240 python src/cstar_l25_probe.py --certify-small
    src/dirun.sh -c 2 -m 8 -t 240 python src/cstar_scalar_moment_barrier.py --singer --output .research/experiments/l25_2026-10-21/scalar_singer.json
    src/dirun.sh -c 2 -m 8 -t 180 python src/cstar_gpu_projected.py --labels singer_integer_differences_p31,singer_integer_differences_p127 --output .research/experiments/l25_2026-10-21/projected_cpu.json
    src/dirun.sh -c 2 -m 8 -t 240 python src/cstar_projected_verify.py --input .research/experiments/l25_2026-10-21/projected_cpu.json --output .research/experiments/l25_2026-10-21/projected_cpu_verification.json --certify-L1
    src/dirun.sh -c 2 -m 8 -t 240 python src/cstar_projected_verify.py --input .research/experiments/l25_2026-10-21/projected_gpu.json --output .research/experiments/l25_2026-10-21/projected_gpu_verification.json
