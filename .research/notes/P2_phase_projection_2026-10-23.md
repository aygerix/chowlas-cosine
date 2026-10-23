# P2: a sharper analytic gate and an exact Boolean projection failure

2026-10-23. Research checkpoint, not a manuscript. Full Chowla remains
unresolved. Paper identities were independently checked by the sole
[internal advisor](advisor_P2_coupling_2026-10-23.md); finite certificates
ran on Dirichlet. No new Lean/kernel verification or priority claim.

## Exact target and new analytic result

Let A be a finite nonempty set of distinct positive integers, n=|A|,
F=sum_A z^a, f=Re F, b=Im F. Assume the ACTUAL all-circle
M(A)<=sqrt(n), and set lambda=2sqrt(n), p=(lambda+F)^(-1).
All integrals are probability Haar averages. Define

    g=lambda²||p||²-1=||F/(lambda+F)||²,
    C1=<F,p>, C2=<F²,p>, T=<F,p²>, t=<F,F²>,
    H=<2f(Im p)²>, h=lambda H, y=-lambda T.

The original sufficient target P2 is the existence of a nonpositive
energy vector in span{Im F,Im p}. For t>0 it is exactly

    Phi=2tH-C2²<=0.

Its conditional implication to full Chowla is already proved in
[the two-direction note](cstar_two_direction_sign_2026-10-23.md).
P2 itself is neither proved nor refuted here.

The new phase identity retains the entire cubic phase:

    K=(F²+lambda*conjugate(F))*p²,
    ||K||²=g-4h.

Pointwise |F²+lambda*conjugate(F)|² equals
(b²-f(lambda+f))²+b²(lambda-2f)². Its constant Fourier coefficient
is -2(g+h), while <K,conjugate(F)>=lambda(C1+2g+2h).
The orthogonal constant/negative-frequency projections give

    g-4h >= 4(g+h)²+4(C1+2g+2h)².                 (1)

Together with the strict Cauchy bound |C1|<sqrt(g)/2 this proves

    g>=4/25  ==> H<0 ==> P2.

Indeed if h>=0 and x=sqrt(g)>=2/5, (1) forces
x²>4x⁴+4(2x²-x/2)²=x²+4x³(5x-2), a contradiction.
The prior generic sufficient threshold was9/16. The new threshold
does NOT prove g has an absolute positive lower bound. These analytic
inequalities also hold for weighted real F when n is its actual
coefficient energy, so exact Booleanity is still missing.

The centered even plane {f,Re(p-1/lambda)} has a separate checked
energy matrix. Simultaneous positive definiteness of both parity
planes requires g+C1<0 and

    (2C1+1/2)² < -16(t/lambda³)(g+C1).

In particular, when g<=1/16 it requires
t/lambda³>(1-8g)²/(64g). This is a high-triple gate, not a
contradiction. Complete derivations and scope are in the advisor note.

## One bounded finite-alias adversary, now stopped

Let U=[0,1,25,30,40,46,53,96,100,114,122,131] and
V=[0,1,4,9,11]. Their positive differences are individually distinct.
For L in1..128 test only disjoint A_L=diff_+(U) union L*diff_+(V).
There are47 admitted cases, each with n76 and the EXACT all-circle
bound M<=12/2+5/2=17/2<sqrt76 from two difference-square identities.
This premise is independent of any grid.

[Producer](../../src/P2_alias_adversary.py),
[data](../experiments/P2_alias_2026-10-23/results.json).
All47 FFT proposals had H<0; no P2 falsifier was found. A doubled
grid was used only on the selected L36. These observations do NOT
prove the remaining46 full inverse signs or a finite-class theorem.
Do not enlarge the L range or deploy a GPU for this failed probe.

## Exact Boolean falsifier of a stronger finite-projection closure

Eliminating h=y/2-g from (1) gives the valid finite-coefficient
lower bound

    G3=[y²+4(C1+y)²+2y]/5 <= g.

A plausible STRONGER sufficient criterion for P2 is

    Psi3=2t(-G3/lambda-T/2)-C2²<=0.               (2)

Unlike P2, every term of(2) depends only on inverse Taylor
coefficients through2max(A). Equation(2) is FALSE for a genuine
Boolean support in the required actual-lowM domain.

Take the single saved A_36 above, n76,maxA396,t1617. The384-bit
Taylor recurrence lambda*p_j+sum_A p_(j-a)=0 and the separate
recurrence (lambda+F)*p²=p give

    Psi3=0.99905643786534157099419156878... >0.

Selected direct convolution of p with itself independently checks T.
The exact rational interval in the artifact, rather than the displayed
decimal, certifies the sign. Thus constant plus conjugate-F projection
cannot close P2 universally, even after all signed finite moments are
retained. This does not falsify richer projections or P2 itself.

On the SAME support, the full inverse was certified using a dyadic
polynomial approximation of band12672, its exact integer residual,
and the global inverse margin lambda-17/2. Sparse Python-integer
shifts independently reconstruct the residual produced by FLINT
polynomial multiplication. The resulting full H is strictly negative,
and Phi is strictly negative near-3.3081176154. The original P2
therefore HOLDS for this finite example while(2) fails.

The precise lost quantity is

    Rperp=||K-Proj_span{1,conjugate(F)}K||²=5(g-G3),
    Phi=Psi3-(2t/(5lambda))*Rperp.

It is not permissible to discard this positive residual when proving
a negative Rayleigh direction. Exact brackets for g,G3,Rperp,Phi
and all certificate numerators are saved in the linked artifact.

[Producer and independent arithmetic paths](../../src/P2_projection_bound.py),
[finite and full-inverse certificates](../experiments/P2_projection_2026-10-23/results.json).

## An explicit finite weighted falsifier of the generic relaxation

The complete two-parity extension also fails without Booleanity,
even at actual coefficient-energy calibration. A simple exact example is

    F_N=sum_(a=1)^1024 (99/101)^(a-1)*z^a,
    lambda_N=(101/10)*sqrt(1-(99/101)^2048).

Every coefficient is in(0,1], but most are NOT1. The all-circle
weighted minimum satisfies M<=505001/1000000, far below its
coefficient-energy square root. Uniform rational tail bounds transfer
closed-form infinite geometric-series matrices to the COMPLETE finite
inverse. Both normalized parity matrices are positive definite;
their determinant lower bounds exceed0.00022995 and0.00939703.
No sample grid or finite inverse truncation is used as proof.

[Exact producer](../../src/P2_geometric_certificate.py),
[certificate](../experiments/P2_geometric_2026-10-23/results.json),
[independent paper/source audit](advisor_P2_coupling_2026-10-23.md#7-explicit-norm-calibrated-geometric-obstruction-to-generic-closure).
This is a falsifier of a RELAXATION, not of Boolean P2 or Chowla.

## Full negative block recovers the same example; a Boolean boundary lemma

Two candidate closures were tested: generic full-norm/parity closure
fails on an exact weighted example, and finite rank-two phase projection
fails on an exact Boolean example. Stop further generic Gram polishing
or more successful-control scans. Preserve the proved4/25 branch.

The next attempt used all relevant coefficient positions. The FULL
negative Fourier block gives the exact bound

    k_j=[z^(-j)]K=lambda*sum_(a in A,a>=j)[z^(a-j)]p², 1<=j<=D,
    Gminus=[y²+sum_(j=1)^D k_j²+2y]/5 <= g,
    g-Gminus=||P_(strictly positive frequencies)K||²/5.

All k_j are finite and explicitly depend on the actual Boolean bits;
Gminus>=G3. On the SAME L36 support, exact ball recurrences now give

    Gminus=0.11930072719334103...,
    Psi_minus=2t(-Gminus/lambda-T/2)-C2²
             =-0.73997255709792434437999943676... <0.

Thus the full negative block RECOVERS the finite certificate that the
rank-two projection lost. In fact 2Gminus>y proves H<0 already,
without needing C2. This is one certified finite recovery, not
a universal theorem or a reason to enlarge a control scan. The exact
intervals are in the same projection artifact. For t>0 the new
stronger finite sufficient target is

    Nminus+(5lambda/(2t))*C2² >= y/2-y²,          (3)
    Nminus=sum_(j=1)^D k_j².

This is a growing support-dependent Hankel action, not the already
refuted uniform Hankel-operator norm or fixed-degree phase-polynomial
witness. On the geometric relaxation the entire negative block is
collinear with conjugate(F), so Gminus=G3 and(3) fails. Unit amplitudes
must therefore enter any universal proof of(3). Its truth for every
Boolean A is CONJECTURAL, and it is stronger than original P2.

There is a new, small quantitative contribution from those amplitudes.
For ANY Boolean A with n>=2 and analytic inverse, let m=minA<D=maxA.
Then the first inverse-square coefficients give EXACTLY

    k_D=1/lambda,
    k_(D-m)=1_A(D-m)/lambda-2/lambda².             (4)

To check intervening frequencies, p²_j=0 for0<j<m and
p²_m=-2/lambda³. In the second row sum only a=D-m (if occupied)
and a=D contribute; every intermediate difference is below m.

Let kappa be the scalar projection of the full negative block onto
conjugate(F). If D-m is unoccupied, its offsupport residual squared
is4/lambda⁴. If it is occupied, the two residuals at D and D-m
have a fixed difference2/lambda²; the sum of their squares is at
least2/lambda⁴, for every kappa. Consequently

    Nminus-4(C1+y)² >= 2/lambda⁴,
    Rperp>=2/lambda⁴,
    g-G3>=2/(5lambda⁴)=1/(40n²)                  (5)

at lambda²=4n. The scalar projection energy is4(C1+y)²
because <K,conjugate(F)>=lambda(C1+y). The first bound in(5) is
the negative-block excess over that projection. The advisor independently
checked this general paper lemma. It uses unit endpoint coefficients;
the weighted geometric truncation has a tiny top coefficient instead.
It does NOT force a root-scale gap or improve a universal exponent.

## Global review and first next derivation

Stop generic finite-rank Gram closure and more alias controls. Retain
the4/25 sign theorem, the false G3 closure, its exact Boolean recovery
by the full negative block, and the unit-row lower bound(5).

First next derivation: aggregate Boolean row equations beyond the
two outer rows in(4), toward(3), or find an actual-lowM Boolean
falsifier of(3). The current two-row contribution is onlyO(n^-2)
in g; it does not pay a cost of order y when y is macroscopic.
Keep C2 and the signed inverse coefficients coupled, since discarding
them restarts the earlier refuted component arguments. The available
positive-frequency remainder is exactly5(g-Gminus); do not assume
it vanishes. No new support search is justified by one finite recovery.

Three distinct retained lines: arbitrary-support signed inverse/Boolean
coupling (primary); actual scalar-factor/mixed-norm coefficient control
outside the refuted odd-zero certificate; and independent Boolean
constructions with growing cardinality and all-circle upper bounds.
No vanishing-ratio construction or universal exponent gain occurred.
All own jobs are terminal; no GPU use or VM lifecycle operation. Shared
Dirichlet stays on and cumulative conservative RunPod spend remains$0.10.
