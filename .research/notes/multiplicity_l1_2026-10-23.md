# Growing multiplicity with l1 rounding: a changed construction test

2026-10-23. Subsequent result: the [universal centroid bound](multiplicity_centroid_2026-10-23.md)
proves E_r>=((r-2)k+2r)/6 and closes this all-class l1 mechanism.
Its exact finite certificate is always above1/2 for r>=2. The
chronological candidate and failed pilot below are retained.

This is a construction-side mechanism probe after the
fixed-temperature exponential target returned to L1 flatness and the
bounded-depth exponential estimate was dominated by the existing P9
star bound. It is not a numerical cosine-minimum search.

## Exact all-circle certificate and asymptotic target

Let B be a finite integer set of cardinality k, and let r_d be its
positive difference multiplicities. Set A={d>0:r_d>0}, N=|A|. For an
integer r>=2 define E_r=sum_(d in A)|r_d-r|. Exactly,

    2r*f_A=|F_B|²-k+2sum_(d in A)(r-r_d)cos(dx),
    M(A)<=k/(2r)+E_r/r.                            (1)

All output frequencies are distinct positive integers. No sampled
minimum enters (1). Also |rN-k(k-1)/2|<=E_r. Therefore an effective
family with k,r tending to infinity and E_r=o(k*sqrt(r)) would have
N~k²/(2r) and certified M(A)/sqrt(N)->0. No such family is known here.

This differs from P23/E35/E39: the old support kept ONLY exact-r
classes and discarded all others, paying W=2sum_nonexact r_d. Here
every nonzero class is retained; a class r_d=r-1 costs one instead
of r-1. The conversion is W<=2(r+1)E_r, so the growing-r target is
not supplied or refuted by the old fixed-r search. That history is
preserved in NOTEBOOK's October18 near-ruler entry and PROOFS P23.

## Paper gates before computation

Order B=b1<...<bk. The distinct differences bk-bi have multiplicity
at most i, since any lower endpoint realizing that difference is
at most bi. Consequently

    E_r>=r(r-1)/2 for integer 2<=r<=k.

Thus a successful family must have r=o(k^(2/3)). This old extreme-lag
mechanism is a real constraint, not a general exclusion.

The advisor extends P23 parity: if B is reflection-symmetric and r
is odd, E_r>=k(k-1-r)/(2(r+1)). Only floor(k/2) difference classes
can have odd multiplicity; count total pairs in the other classes
and charge each nonexact class to E_r. This excludes that subclass
throughout the required subcritical-r regime. The pilot uses EVEN r
and has no reflection-symmetry restriction. P8/P9 do not provide a
general E_r>=c*k*sqrt(r) bound.

## Predeclared finite pilot

One box only: k=128, r=8, B subset{0,...,2048} containing0;
one chain,15000 proposals, seed2026102308. A proposed continuation
would scale r proportionally to sqrt(k), rather than keep r fixed.
No continuation is authorized merely by improving a finite score.

Minimize the exact integer E_r using1/2/4 point exchanges, with
global and local coordinate proposals. Annealing randomness proposes
B; every multiplicity, support and final certificate uses integers.
Rebuild pair counts periodically. Independently verify the final
counts by an exact polynomial autocorrelation.

Discriminators: E_r/(k sqrt r)<1/8, and the exact all-circle upper
bound in (1) below sqrt(N)/2. Either would warrant a new analytic
scaling question; neither alone would establish a vanishing family.
If both fail, stop this pilot. Do not enlarge the box/steps or buy
GPU throughput without a structural change.

Run only through Dirichlet, two CPU cores,4GB,120-second wall cap.
Shared VM lifecycle is untouched. The experiment is heuristic and
incomplete; its finite all-circle bound is an exact symbolic
certificate.

## Outcome and decision

The one declared job completed normally in2.36seconds on Dirichlet.
Best E fell from7016 to2964, with N=1136. Independent exact
polynomial autocorrelation matches every final pair count. The
symbolic bound is only

    M(A)<=757/2,
    R_upper²=573049/4544, R_upper about11.23,
    E_r/(k sqrt r) about8.187.

Both gates fail by wide margins. The finite run alone is a weak
certified upper bound, not the actual minimum or a general exclusion.
The subsequent centroid proof supplies the general obstruction:
the requested count balance is impossible for every B, and the
half-constant gate itself could never pass. Stop this all-class l1
architecture, not just the optimizer; no box/step enlargement or GPU.
Discarding classes or using signed pointwise correction is outside
the theorem and would require a genuine mathematical change.

Artifact: experiments/multiplicity_l1_2026-10-23/results.json.
environment.json records the explicitly labeled post-run package
inspection; the mathematical pilot was not rerun for metadata.
The advisor read-only audited the update accounting, independent
recount, rational bound and failed gates in
[the global review](advisor_exponential_depth_2026-10-23.md).
