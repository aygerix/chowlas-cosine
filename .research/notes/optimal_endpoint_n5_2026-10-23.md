# One optimal endpoint test: certify the existing five-frequency branch

2026-10-23. Protocol written before computation. This targets the
provisional bound qmax<=1, not the existence of ANY absolute qmax
bound. It is not a new cosine-minimum search or a parameter sweep.

The advisor identified an old, unverified positive-factor-search branch
for A={1,...,5}, with q0 about1.044 in the current normalization.
The old floating artifact alone did not prove optimality or positivity.

Write

    Q(z)=(z²-2cz+1)*(a+bz+dz²+ez³).

Impose its five nonzero autocorrelations R_j(Q)=1/2, j=1,...,5.
This is a five-variable polynomial system. A real solution with all
six q coefficients positive, q0>1, and |c|<1 proves an optimal
positive factor: coefficient matching gives |Q|²=lambda+f_A with
lambda=sum q²; the quadratic factor has a unit-circle zero, so
min f_A=-lambda on the entire circle. No sampled premise is used.

The producer uses high-precision algebra only to propose a center
and inverse Jacobian. Rational interval evaluation then proves that
x -> x-R*F(x) maps a closed rational box strictly into itself and
has derivative norm<1; R has exact nonzero determinant. Banach's
theorem gives a real zero in the box. The independent checker
rebuilds Q by convolution, differentiates by dual intervals instead
of symbolic expanded polynomials, and verifies the same strict
contraction and coefficient bounds using rational arithmetic.

Additional branch gate, before the run: the cubic residual has
negative discriminant, one negative real root -t with t>1, and a
complex-conjugate pair of modulus>1. Reflecting just the real root
preserves the circle modulus but gives a negative q coefficient.
The four real spectral branches are the original, its reversal,
the real-root reflection and its reversal. Validating those signs
would refute qmax<=1 even after choosing the nonnegative branch.
It would still leave every larger absolute bound and any growing
counterfamily question unresolved.

One branch only, no follow-up family sweep. Dirichlet through dirun,
two CPU cores,4GB,120s cap per producer/checker; shared VM lifecycle
untouched, no GPU. A pass refutes only the constant1 and changes the
next endpoint estimate; it cannot refute every absolute C or Chowla.
Results and exact certificate follow.

## Certified outcome, including branch selection

Both producer and checker completed normally/PASS on Dirichlet.
The exact rational contraction box certifies a real solution with
all q_j positive, q0 the largest coefficient, |c|<1 and lambda<2.
It gives

    M(A)=lambda about1.7287682073931698<2<sqrt5,
    qmax=q0 about1.0437967021412156>1.

Rational intervals, rather than these display decimals, are the
authoritative enclosures in experiments/optimal_endpoint_2026-10-23/
n5.json. The checker in n5_verification.json independently rebuilds
the polynomial by convolution and differentiates via dual intervals.
Both programs share the small exact Fraction interval primitives;
this is independent differentiation/reconstruction, not a separate
arithmetic backend or a Lean proof.

The residual cubic has exactly one real root -t, with t>1, and
a nonreal conjugate pair with squared modulus a/(e*t)>1. These
claims are certified by its negative discriminant, exact sign
bracket and rational interval modulus bound. Thus all residual
zeros are outside the unit circle. Every real optimal factor,
after shift and overall sign, must choose one member of each
reciprocal pair while keeping conjugates together. The unit pair
must be kept once each. This gives exactly four real branches:
Qplus, its reversal, the real-root-reflected Qr, and its reversal.
The reflected branch has a negative z² coefficient and positive
endpoints, so neither overall sign makes it nonnegative. Therefore
the only nonnegative branches are Qplus and its reversal; BOTH
have qmax>1. This refutes the constant1 even existentially, while
every larger absolute bound and the existence of a growing
counterfamily remain unresolved.

## The same reflection recovers the signed sufficient conditions

Without changing A or lambda, src/optimal_endpoint_phase.py checks
the signed geometry of Qr from the same certified box/root bracket.
It performs no new root search or support sweep. Exact rational
intervals in phase_recovery.json give

    qmax<0.786161,
    Nminus/S<0.068887<1/8,
    alpha<0.002623<1/8.

The sole negative coefficient is at degree2. The separate invariant
variance check also proves Vminus<Vintrinsic/6. Thus all three
C=1 conditions in [the signed lemma](signed_centroid_2026-10-23.md)
hold on this reflected optimal factor, even though the nonnegative
branches fail qmax<=1. The resulting lower estimate is not a new
best bound for this five-frequency set. The significance is the
exact branch trade, not the numerical minimum. The advisor read-only
audited the certificate, classification, phase source and saved
intervals in the linked endpoint/signed notes.
