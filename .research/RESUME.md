# Paused handoff — start here on explicit resumption

Last updated: 2026-10-21. The user has NOT resumed the research goal.
This handoff and the requested novelty review are bounded documentation
work. They authorize no proof search, experiment, provisioning or GPU run.
The latest pushed research checkpoint is d66736d.

## Exact objective and current candidate

For EVERY nonempty finite set A of distinct positive integers, with
n=|A| and f_A(x)=sum_(a in A)cos(ax), prove M(A)=-min_x f_A(x)>=c sqrt(n)
for an absolute c>0; alternatively produce a growing Boolean family with
rigorous ALL-CIRCLE M(A)/sqrt(n)->0. Full Chowla remains OPEN.

The immediate proof candidate is **R0**, not an assumption or an
established equivalence with Chowla. Under the ACTUAL all-circle
hypothesis M(A)<=sqrt(n), fix lambda=2sqrt(n) and define

    F_A(z)=sum_(a in A)z^a, p=1/(lambda+F_A), q0=Im p,
    Q0=<q0²>, H0=<2f_A q0²>, S=<|p|²>, g=lambda²S-1,
    T0=sum_(a in A)[z^a]p², tau=-lambda*T0/(2g).

Angle brackets mean normalized integration dx/(2pi) over the ENTIRE
circle. n is the exact number of occupied coefficients, all equal to1.
The identities Q0=g/(2lambda²)>0 and H0/Q0=2lambda(tau-1) are proved.

**Provisional R0:** EVERY such Boolean support satisfies

    tau<=1-1/400,
    equivalently H0/Q0<=-sqrt(n)/100.

This would imply M(A)>=sqrt(n)/200; supports with M>sqrt(n) already
satisfy that conclusion. The number1/400 is a provisional target, not
a measured universal constant. A different absolute positive margin
would suffice. Neither R0 nor its qualitative sign version is proved.

## The exact missing step

The positive correction -T0/2 in H0=-g/lambda-T0/2 must be bounded
from ABOVE relative to g. T0<0 is proved, but its sign alone does not
help. LowM gives tau>=1-M/lambda>=1/2: this is the OPPOSITE direction
from the missing upper bound tau<=1-eta.

A Schur/Cauchy estimate proves

    H0/Q0<=-2lambda*(1-3/(4sqrt(g))).

It handles g>9/16, with a root-scale margin only when separated from
that threshold. It does not handle the remaining g range or prove a
Boolean norm-gap lower bound. The next argument must exploit the actual
zero-or-one coefficients, beyond the generic analytic identities.

For the SPECIFIC R0 constant1/400, the displayed sufficient estimate
already gives R0 when g>=10000/17689=(100/133)². Thus the precise
remaining range is 0<g<10000/17689, including the interval just ABOVE
9/16. Do not confuse the sign threshold with this quantitative cutoff.

## First actions after the user explicitly resumes

1. Read GOAL.md, this file, the current top of STATE/CSTAR, the
   [zero-carrier advisor audit](notes/advisor_zero_carrier_2026-10-21.md),
   and the [R0 novelty review](notes/R0_novelty_2026-10-21.md). Reuse the
   existing PhD Advisor; no additional agents.
2. Attempt a Boolean selected-coefficient upper bound on -T0/g in
   the unresolved g range. Alternatively finish the SPECIFIC failed
   counterexample transfer: for an explicitly chosen prefix/pad pair,
   derive the TWO-VARIABLE reciprocal energy and determine whether its
   sign can transfer. An oversized-lambda prefix calculation alone is
   not a counterexample at lambda=2sqrt(n).
3. Before any computation, state the exact estimate and a discriminating
   adversarial input. A valid counterexample to R0 requires the fixed
   lambda, genuine Boolean coefficients, and a certified global lowM
   premise. Certify the full reciprocal energy by the existing residual
   method. A failure of R0 refutes this witness target; the broader
   signed-Rayleigh and construction tracks remain available.
4. Obtain an advisor-reviewed prove/falsify/pivot decision. If the single
   reciprocal ansatz gives no new coefficient or interaction estimate,
   pivot to the FULL signed-Rayleigh problem. Do not spend another cycle
   adding successful reciprocal controls. Retain the independent
   construction track only with an actual changed asymptotic mechanism.

## What has already been checked; do not repeat it

* Certified reciprocal quotients H0/(Q0 sqrt(n)) are near-.360 (n56),
  -.302 (n306), and-.544 (saved coherent-prefix n337). Producer and
  independent sparse-residual/formal-inverse verification PASS. These
  are three finite results, not a universal estimate or best-bound claim.
* The n337 occupied prefix1..243 was already the single stronger stress
  test. Its negative result does not justify a size/parameter sweep.
* The two-frequency prefix {1,2} has positive energy for sufficiently
  OVERSIZED lambda, but not at its required lambda=2sqrt(2). Separated
  padding preserves neither S nor the complete unshifted T0; pure
  high-block contributions persist. Increasing a dilation is no repair.
* Unrestricted normalized phase-Hessian optimization is exactly minimum
  modulus. Reciprocal phase averaging recovers the old real resolvent.
  Positive reciprocal carriers retain a bounded-amplitude flatness gap;
  the zero carrier is exceptional because Q0 subtracts lambda^-2/2.
* Boolean projection/reflection produced all-circle construction ratios
  near.642 and.651, both ABOVE.5 and missing.45. Stop that pilot. Its
  span proportional to n supplies no vanishing-ratio mechanism at fixed
  density. No GPU deployment was justified.

## Artifacts and resources

Detailed cycle: [cstar_projection_phase_cycle_2026-10-21.md](notes/cstar_projection_phase_cycle_2026-10-21.md).
Exact saved certificates: experiments/zero_reciprocal_2026-10-21/
{results,verification,prefix,prefix_verification}.json. Source:
src/cstar_zero_reciprocal.py and src/cstar_zero_reciprocal_verify.py.
They use exact polynomial residuals to enclose the INFINITE reciprocal;
a sample grid integral is not a certificate.

All research jobs are terminal; no GPU worker is active. All ordinary
research computation must use Dirichlet through src/dirun.sh. The
RunPod cumulative cap is$6.50, with$0.10 conservatively recorded and
no new spending in this cycle; consult GPU_BUDGET.json before any
deployment. Use exactly one existing internal PhD Advisor (Sol6.1/MAX).
No new resources or user-supplied mathematical input are needed for the
next derive/test cycle. Resume only after an explicit user instruction.
