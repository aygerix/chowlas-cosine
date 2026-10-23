# A span-free centroid bound for multiplicity rounding error

2026-10-23. New paper derivation in this research record, independently
checked and strengthened in [the advisor audit](advisor_multiplicity_centroid_2026-10-23.md).
No external novelty, kernel verification or unrestricted Chowla claim.
It resolves the all-class l1 construction target formulated before
the bounded pilot, with no symmetry, density or span assumption.

## Quantified theorem

Let B be any finite set of k>=2 distinct real numbers. Write
r_d=#{b in B:b+d in B} for each positive occurring difference d.
For a real reference multiplicity r>=2 define

    E_r=sum_(d>0,r_d>0)|r_d-r|.

Then

    E_r>=((r-2)k+2r)/6.                            (1)

In particular E_r/(k sqrt r) tends to infinity whenever r tends
to infinity. Thus no integer B family can have r->infinity and
E_r=o(k sqrt r). The all-class l1 rounding mechanism is closed.

For integer B, A=diff_+(B), N=|A|, its square/l1 certificate is

    R_cert=(k/2+E_r)/(r sqrt N).

For every finite k>=2 and every real r>0 this certificate satisfies

    R_cert>1/2.                                   (2)

This is a lower bound on the displayed UPPER certificate, not a
lower bound on actual M(A). Signed cancellation of the correction
polynomial, deletion of low-multiplicity classes, weighted/signed
factors and arbitrary Boolean constructions are not excluded.

## 1. A row Gram identity and its uniform error norm

Let mu be the ordinary mean of B and x_b=b-mu. Put V=sum_b x_b²>0
and, for every signed lag d (including zero),

    S_d=sum_(b in B,b+d in B)x_b.

The incidence matrix M_(b,d)=1_B(b+d) has Gram
G_(b,c)=r_|b-c| for b!=c, and diagonal k. Consequently

    sum_d S_d²=x^T G x.

Set delta_d=r_d-r. On centered vectors the baseline matrix
(k-r)I+rJ has quadratic form (k-r)V. The off-diagonal error row
has absolute sum at most2E_r: for a fixed b, each positive lag
can occur at most twice. Therefore

    sum_d S_d² <= (k-r+2E_r)*V.                   (3)

No comparison of frequency magnitudes is used. Here S_0=sum x=0.

## 2. Lag pairing and the arithmetic-chain improvement

For d>0, translating the summation endpoints gives

    S_(-d)=S_d+r_d*d,
    S_d²+S_(-d)²>=(r_d*d)²/2.                     (4)

Also the standard pair-variance identity is

    sum_(d>0)r_d*d²=k*V.                          (5)

For each fixed d, the graph of pairs b,b+d is a disjoint union of
finite arithmetic progressions. A component with m vertices has
sum of squared globally centered coordinates at least
d²*m*(m²-1)/12, hence at least (m-1)d²/2. Summing the components
gives the uniform lag bound

    r_d*d²<=2V.                                  (6)

This improves the root's initial max-degree-two estimate4V. Since
r_d²>=r*r_d-|delta_d|*r_d, equations (4)--(6) imply

    sum_d S_d² >= (r*k/2-E_r)*V.                  (7)

Compare (3) and (7) and cancel V>0. The result is
3E_r>=(r/2-1)k+r, which is (1). The initial4V version already
proved the weaker denominator8; the advisor's chain variance
gives the stated denominator6.

## 3. Exact finite half-constant barrier for this certificate

Put T=k(k-1)/2. Since sum_d r_d=T, one has rN<=T+E_r, so

    R_cert² >= (k+2E_r)²/[4r(T+E_r)].              (8)

The right side is strictly increasing in E_r>=0 for k>=2.
Use just the weaker bound e=((r-2)k+2r)/8. Direct expansion gives

    16*((k+2e)²-r*(T+e))
       =(r-2)²*k²+2r*(r+10)*k>0.

Equations (8) and E_r>=e prove (2) for r>=2, with no asymptotic caveat.
For fixed r, the weaker bound gives asymptotic floor
(r+2)/(4sqrt(2r)); use (8), not that fixed-r expression, in joint
limits where r is comparable to k.

For completeness, noninteger reference multiplicities cannot evade
the finite floor. Between consecutive integer multiplicities E_r
is affine in r, so R_cert(r) has the form b+a/r and is monotone or
constant. Below1 it is decreasing. Above the largest multiplicity it
equals sqrt(N)+k*(2-k)/(2r*sqrt(N)), increasing for k>2 and constant
for k=2. Its minimum is therefore attained at an integer breakpoint.
At r=1 it is at least k/(2sqrt(N))>=k/(2sqrt(T))>1/sqrt2.
Together with the r>=2 result this proves (2) for every real r>0.

## Decision and remaining scope

The pilot's r=8 half-constant gate was mathematically impossible,
as this subsequent proof now establishes. Its failed finite result
is preserved as the event that prompted the derivation. More local
search or GPU throughput cannot repair the all-class l1 target.

P76(c) contained the extreme-lag bound; P77 treated finite-group
lifts under spectral hypotheses. The inspected statements do not
contain (1), whose proof uses an arbitrary-support incidence Gram
and a lag-chain variance bound. External priority remains unverified.

The old P23 construction that discards nonexact classes is distinct:
small-multiplicity discarded classes cost little there but each cost
about r in E_r here. It remains outside this theorem, as does an
oscillation-aware bound on the signed correction near zeros of F_B.
Do not mark all high-multiplicity square methods or full Chowla closed.
