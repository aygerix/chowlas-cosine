# Two-scale cubic dual: independent audit and global stop decision

2026-10-23. Sole internal AI advisor. Paper derivation plus read-only
source/artifact audit. I ran no research computation, VM operation,
GPU, additional agent or outreach. Shared Dirichlet remains untouched.
Full Chowla is unresolved. No kernel, priority or external-review claim.

The already proved density-restricted result remains: for every fixed
0<C<400/29 there is an ineffective c(C)>0 such that every nonempty
finite set A of distinct positive integers with max A<=C|A| satisfies
M(A)>=c(C)|A|^(1/3). This note proves no further constant or exponent.
See [the preceding proof](cubic_profile_cap_2026-10-23.md) and
[its advisor audit](advisor_two_block_gram_2026-10-23.md).

## 1. Exact profile hypotheses and the two-scale inequality

Use the existing P61/P66 contradiction framework, not an assertion
that arbitrary Boolean sets already have these limiting profiles.
Under its hypotheses the actual coefficient profiles satisfy

    p=phi(v), e=v/4=p(1-p), 0<=v<=2/3,
    phi(v)=(1-sqrt(1-v))/2,
    H(t)=G(v(t)) is positive definite,
    G(v)=v*sqrt(1-v)/4,
    H(0)<=c0=G(2/3)=sqrt(3)/18, c0^2=1/108.

The functions have support[-1,1], and d=integral_0^1 p. The Gabor
mixtures approximate the smoothed energy profile; a literal exact
mixture for the original unsmoothed profile is not assumed.

For H0>0, the three-point Toeplitz determinant gives

    H(2t)-2H(t)^2/H0+H0>=0.

Indeed its determinant is
(H0-H(2t))*(H0*(H0+H(2t))-2H(t)^2), and the first factor is
nonnegative; the degenerate equality case follows from the Gram
relations. Equivalently apply Cauchy to the two neighboring increments.
Consequently, for any cU>=c0,

    R_cU(t)=G(v(2t))-2G(v(t))^2/cU+cU>=0.       (1)

Replacing H0 by cU adds
2H(t)^2*(1/H0-1/cU)+(cU-H0)>=0. If H0=0 then H is zero
and the profile has zero density, so the intended contradiction
sequence does not arise.

Let gamma be continuous, 0<=gamma<=1/24. Adding integral gamma*R
before Jensen and changing variables in its child term yields

    d <= cU*integral_0^1 gamma
             + integral_0^1 Lambda_t(v(t)),
    Lambda_t(v)=phi(v)+gamma(t/2)*G(v)/2
                              -2gamma(t)*G(v)^2/cU.        (2)

The change of variables is over the complete support: the child
term has factor1/2. Extending gamma continuously slightly past1
handles the old dilation approximation; the actual profile vanishes
outside its support.

## 2. Explicit convexity budget and passage through mixtures

Put a=gamma(t/2)/2 and h=2gamma(t)/cU. On[0,2/3],

    G'=(2-3v)/(8sqrt(1-v)),
    G''=-(4-3v)/(16(1-v)^(3/2)),
    (G^2)'=v(2-3v)/16, (G^2)''=(1-3v)/8.

Thus 0<=a<=1/48, h<=1/(12cU), |G''|<=3sqrt3/8 and
(G^2)'<=1/48. Since phi''>=1/8 and phi'>=1/4,

    Lambda_t'' >=1/8-sqrt3/128-1/(96cU)
                 >=(16-9sqrt3)/128>0,
    Lambda_t' >=1/4-1/(576cU)
                 >=1/4-sqrt3/96>0,
    Lambda_t(0)=0.                                      (3)

Therefore (2) may be inserted BEFORE the Gabor-Jensen averaging,
giving a valid supremum bound over the old normalized generator
class W after increasing the global mass to2/3. This does not impose
G((2/3)|w|^2) positive definite on every individual generator.
Monotonicity also permits the old complex-to-nonnegative
autocorrelation majorization.

The actual cubic support cap is still

    v(t)<=b(t), b_k^2(1-b_k)=(4/27)cos^2(pi/(k+2)),
    k=ceil(1/t)-1, 0<=b_k<=2/3.                         (4)

Let Lambda_cap,t equal Lambda_t through b(t) and continue by its
tangent thereafter. It is convex/increasing and equals the actual
profile integrand. Thus

    d <= cU*integral gamma
        +sup_(w in W) integral_0^1
           Lambda_cap,t((2/3)|w(t)|^2).                 (5)

A cellwise UPPER bound on b(t) weakens (5) conservatively, because
the tangent continuation of a convex function increases with its
contact point. The cap itself uses the exact c0^2, hence4/27 in(4).
Only the dual coefficient and constant offset are replaced by cU;
one must not silently change the original cap to cU.

## 3. The single practical bump and its constant offset

The predeclared shape was

    s(t)=(1-32|t-7/32|)_+,
    I=[3/16,1/4], gamma(t)=rho*s(t), 0<=rho<=1/24.

Its area is1/32. Its child interval2I=[3/8,1/2] is disjoint
from I. The additive density offset in(5) is exactly

    cU*rho/32.                                         (6)

If an operator certificate bounds the remaining half-line functional
by D_kernel, the total density bound is D_kernel+(6). Equivalently,
an exact Schur certificate aimed at D_total must use the kernel
allowance2*(D_total-cU*rho/32). Omitting this offset would be an
incorrect gain.

All parent/child knots lie on the current K64 half-cell mesh.
With a fixed cap b for each half-cell, the unsquared integrand and
its tangent are affine in rho and in t on each linear piece. It is
therefore enough to verify the desired pointwise inequality at BOTH
time endpoints of each piece. This interpolation applies to the
UNSQUARED affine inequality, not to the polynomial obtained after
squaring a radical; the squared polynomial need not be affine in t.

The chosen rational constant is

    cU=962250449/10000000000, 108*cU^2>1.

It is an upper bound for c0. Raising cU increases the constant offset
and weakens the negative G^2 term, both conservative directions.
There is no generally valid upward/downward rounding rule for rho:
any chosen rational rho must be fully recertified in its allowed range.

## 4. Radical and tangent polynomial certificates

For the old pointwise potential bound set x=1-u^2, v=(2/3)x^2,
with u in[0,1]. Let RHS denote the existing potential/kernel upper
bound. Write a=rho*s(t/2)/2 and h=2rho*s(t)/cU.

Below the cap,

    Lambda=.5-(1-a*v/2)*sqrt(1-v)/2
                    -h*v^2*(1-v)/16.

Define

    A_low=RHS-.5+h*v^2*(1-v)/16,
    L=1-a*v/2,
    P_low=L^2*(1-v)/4-A_low^2.                         (7)

Here L>=143/144>0. If A_low>=0 the required inequality is
immediate; otherwise P_low>=0 suffices with the indicated sign.

For tangent continuation at b put

    K=b^2*(1-b)+b*(2-3b)*(v-b),
    N=4-2b-2v-a*(b^2+(2-3b)*v),
    A_high=RHS-.5+h*K/16.

Direct differentiation gives

    Lambda_cap=.5-N/(8sqrt(1-b))-h*K/16,
    P_high=N^2-64*(1-b)*A_high^2.                     (8)

The crude uniform bound N>=4/3-(1/48)*(16/9)=35/27>0 is
sufficient for the sign when squaring. Use(8) only on a leaf entirely
above the chosen cap. On a straddling leaf, the uncapped convex
Lambda is an upper bound for its tangent continuation, so(7) remains
a conservative proof. Every monotone child-potential lower branch
must retain its independently verified domain. No sign is inferred
solely from a floating optimizer.

## 5. Certified generator discriminator, including cap activity

Take the normalized half-sine autocorrelation

    w(t)=(1-t)cos(pi*t)+sin(pi*t)/pi, 0<=t<=1,
    H_*(s)=s^2*sqrt(3-2s^2).

It is nonnegative/decreasing and G((2/3)w(t)^2)=c0*H_*(w(t)).
For every subinterval[l,h] of I, monotonicity gives

    R_cU(t) <= c0*H_*(w(2l))
                     -2c0^2*H_*(w(h))^2/cU+cU.        (9)

The lower endpoint enclosure is obtained with l,h interchanged in
the two variable terms. No assertion that R itself is monotone is
needed.

I inspected src/cubic_two_scale_probe.py and its saved probe.json.
The parent ran192-bit Arb evaluations on64 rational adjacent
subintervals partitioning ALL of I. Every upper enclosure in(9)
is less than-c0/100. The artifact contains all rational intervals,
not only a sampled maximum. Status PASS, elapsed about.00484s on
Dirichlet. I did not rerun it or independently validate the Arb backend.

The cap continuation does not undo this discriminator:

* On I, a=0. The relevant cap is at least b3>1/3. Above that
  contact point, -(G^2) is convex because (G^2)''<0. Its tangent
  continuation is therefore no greater than the raw negative
  correction. Parent-cap activity can only help this comparison.
* On2I, the negative coefficient is0. The probe also verifies
  w(3/8)<27/50. Thus v_generator<(2/3)*(27/50)^2<1/5<b1,
  so the child cap is inactive. The last inequality follows from
  (1/5)^2*(1-1/5)<1/27=b1^2*(1-b1).

It follows that this bump strictly decreases the capped dual cost
of this ONE generator whenever rho>0, by at least c0*rho/3200.
This is not a decrease of the supremum over W. The generator may
violate other actual-profile caps; no Boolean realization is claimed.

## 6. The fixed discovery result and stopping decision

I also inspected src/cubic_two_scale_discovery.py, the legacy
src/e95_discover_sigma.py it ports, and the saved discovery JSON.
The source checks every intended substitution occurs exactly once;
uses the same K64,degree10,shape1/10 support-cap objective;
retains the monotone child potential; constrains both time endpoints;
and minimizes D_kernel+cU*rho/32. The tangent correction uses the
correct derivatives G' and (G^2)'. The sampled x and Schur rows are
discovery constraints, not a continuum certificate.

The terminal fixed result is

    rho=8.139804678365318e-10, effectively0,
    D_kernel=.07238331307546421,
    offset=2.447665845790415e-12,
    D_total=.07238331307791188,
    certified=false.

The unchanged support-cap baseline proposal was about.072383312978.
The difference is numerical tolerance, not a further result. The valid
generator discriminator did not turn into useful weight in this fixed
dual optimization. STOP this bump: no amplitude/grid/shape sweep,
exact reconstruction or new density theorem is justified by this run.
The previous exact29/400 certificate remains the theorem.

## 7. An exact positive-density countermodel to the retained profiles

The parent's global review makes the old NOTEBOOK cont.18 heuristic
precise. Put

    W(t)=(1-|t|)_+, sigma=1/4,
    v(t)=sigma*W(t)^2,
    p(t)=phi(v(t)), e(t)=v(t)/4.

Then p,e are continuous positive definite functions supported[-1,1].
For p use the nonnegative Catalan power series of phi and closure
of PD under Schur products and positive uniformly convergent sums.
Moreover e/e(0)=W^2 is EXACTLY one permitted Gabor generator, not
just a weak second-moment approximation. Its height is below the
cubic front cap and it uses the smaller root of e=p(1-p).

Write H(t)=G(v(t)). For0<t<1, with v=sigma*(1-t)^2,

    H''(t)=sigma*(2-9v+6v^2)/(4*(1-v)^(3/2))>0.       (10)

The numerator decreases on[0,1/4] and its endpoint value is1/8.
Also H is nonnegative/decreasing and H(1)=H'(1)=0. Hence

    H(t)=integral_0^1 r*H''(r)*(1-|t|/r)_+ dr,          (11)

which is an explicit positive mixture of triangular PD kernels.
This proves the actual cubic PD condition, with all its finite
Toeplitz constraints, all support caps, and EVERY valid two-scale
gamma inequality above. Adding only those consequences cannot
exclude this model.

The density is exactly

    d=1/2-sqrt(3)/8-pi/12 >3/140>0.                   (12)

For the strict rational bound use sqrt3<26/15 and pi<22/7:
1/2-13/60-11/42=3/140. Thus every C>=140/3 is compatible
with d>=1/C in this continuum relaxation. No actual Boolean sequence
with M=o(X^(1/3)), weighted physical construction, or all-circle
counterexample follows from the profile model.

The focused record search found the heuristic at NOTEBOOK cont.18,
roughly lines3138-3146: small PD bumps pass low-order profile
conditions. I found no earlier explicit formula(10)-(12) in that
search. This is a rigorous implementation of the old heuristic,
not a claim of external novelty.

Even generic complete positivity of the translate kernels does not
remove this example. A triangular kernel is the autocorrelation of a
nonnegative interval function, so all its finite Gram matrices are
completely positive. Positive sums and Schur products preserve that
property. Apply this to e, the Catalan series for p, and(11) for H.
This assertion concerns continuum CP kernels; it is not an exact
finite Boolean CP spectral certificate.

## 8. Global review and the changed finite calculation

The support-cap theorem is real partial progress. The unused
two-scale bump and exact profile escape give a clear stop rule:
do not turn a sequence of dense n^(1/3) constant refinements into
a substitute for the unrestricted square-root objective. More valid
duals derived only from the listed profile conditions cannot remove
the explicit positive-density model.

The changed attempt returns to the existing OPEN finite Boolean
CP-certificate problem P76, with exact lag incidences retained rather
than another continuum profile. Its joint centroid identity and a
growing low-M satellite obstruction are written in the separate
[CP vector audit](advisor_cp_vector_2026-10-23.md). Bounded
translations lead to a full cross-component lag completion invariant
under artificial component splitting. No quantitative lower bound
for it is proved. A generic Cauchy contraction or independent
component sum must not be presented as the missing Boolean estimate.

Keep the unrestricted signed Boolean proof line and genuine growing
all-circle construction line active alongside the recorded dense
partial theorem. No promise of unattended work or final resolution.
