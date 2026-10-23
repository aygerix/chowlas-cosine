# Current state — Chowla

Updated 2026-10-23. Research is paused at the user's request.
No research, advisor work or deployment resumes without user instruction.
All our jobs ended; advisor stopped. Leave shared Dirichlet running.

This is the ONLY live handoff. [GOAL.md](../GOAL.md) holds stable rules.
Update this file once per checkpoint; stop cross-posting status.

## First milestone when resumed

Complete a new GPU-driven discovery -> exact CPU check -> advisor
review cycle before another proof-route sequence. Build/test on
Dirichlet, then use one bounded resident RunPod job under the existing
limits. Old successful Singer controls alone do not count.

Default experiment: attack the recorded arbitrary-support OP140 bound
J/sqrt(n)>=1/140, J=c^T(C+2sqrt(n)I)^(-1)c, c=1_A, using NEW
adversarial Boolean supports with actual M<=sqrt(n). The existing
Fourier operator and residual verifier supply the starting machinery.
A numerical screen does not certify the low-M premise or a violation.
The advisor may select a better precise GPU-suitable target; a renamed
open inequality or an unexecuted plan is not the milestone.

Starting code: [Fourier kernel](../src/cstar_gpu_kernel.py),
[resident optimizer](../src/cstar_gpu_projected.py),
[exact residual verifier](../src/cstar_inverse_residual.py).
Prior evidence: [integrated GPU cycle](notes/cstar_l25_gpu_cycle_2026-10-21.md).
The new adversarial runner has NOT yet been implemented.

## Mathematical frontier

Full Chowla remains unresolved; no family with certified ratio tending
zero or quantified Epoch generator has been established.

- Dense partial theorem: M>=c(C)n^(1/3) for every fixed C<400/29,
  max A<=Cn. Paper proof plus two exact certificate checks.
  [Proof](notes/cubic_profile_cap_2026-10-23.md).
- Exact single nonnegative real factor lambda+f=|Q|^2 implies
  lambda>sqrt(n/48). A real factor with negative mass N<=Q(1)/64
  implies lambda>sqrt(31/4608)*sqrt(n). These bound M only when
  the factor is optimal. Paper proofs, internal advisor review and
  exact constants; no new kernel or external-priority claim.
- Universal stable-factor selection is REFUTED: growing low-M
  examples force every optimal real factor to violate even N/S<=1/8.
  The three-color realization uses Bu's cited upper theorem. This
  does not refute selection restricted to hypothetical much smaller
  normalized M. [Proof, counterfamilies and audit](notes/signed_translation_2026-10-23.md).
- Current continuum p/e/g positivity and Gabor conditions admit an
  explicit positive-density model. More valid duals of those same
  conditions cannot give an all-density contradiction. It is not a
  Boolean counterexample. [Scope proof](notes/cubic_two_scale_and_profile_barrier_2026-10-23.md).

Later mathematical target: the full multiple-factor coherence bound
D>=P(theta)(P(0)-P(theta))/(4P(0)) is OPEN. Ordinary Cauchy does
not prove it, and even a CP result needs a bridge to arbitrary A.
[Definitions and checked identities](notes/advisor_cp_translation_2026-10-23.md).
It is no longer the instruction to begin another paper-only turn.

## Resources and references

[GPU_BUDGET.json](GPU_BUDGET.json) is authoritative: recorded spend
$0.10 against the $6.50 cumulative cap; no active worker recorded.
Refresh provider state before any future deployment. Full constraints
and exactly-one-advisor rule are in GOAL.md.

[ROUTES](ROUTES.md) and [PROOFS](PROOFS.md) are historical reference
catalogs, not checkpoint destinations. Old overlapping handoffs and
journals are under [archive/handoffs-2026-10-23](archive/handoffs-2026-10-23/).
Research notes and experiment data retain their existing paths.
