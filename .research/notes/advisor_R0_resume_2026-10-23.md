# R0 resumption: qualitative self-improvement and the coefficientwise gap

2026-10-23. Internal AI advisor, independent paper audit. Full GOAL has
been reactivated by the user; the paused labels in the 2026-10-21 handoff
are historical. I read GOAL.md, .research/RESUME.md, the R0 audits and
route ledger. Only this assigned note is edited. No VM was started,
computation run, GPU provisioned, additional agent launched or external
person contacted. Lean/kernel-checked mathematical proofs: none.
Current user constraint: Dirichlet is SHARED and must be left running.
Do not stop, restart, suspend, reset or schedule a shutdown of that VM
without a NEW explicit user instruction. End only this project's own
bounded jobs. This supersedes the historical stopped-VM handoff.

## 1. Exact question and current decision

A is a finite nonempty set of distinct positive integers, n=|A|,
F_A(z)=sum_A z^a, f_A=Re F_A, M(A)=-min_circle f_A. Throughout
lambda=2sqrt(n), and the premise is ACTUAL M(A)<=sqrt(n). Put

    p_A=1/(lambda+F_A), q_A=Im p_A,
    Q_A=<q_A²>, H_A=<2f_A q_A²>,
    g_A=lambda²<|p_A|²>-1,
    T_A=sum_A[z^a]p_A², tau_A=-lambda*T_A/(2g_A).

The existing identities give H_A/Q_A=2lambda(tau_A-1).
R0 asks tau_A<=399/400. The existing Cauchy estimate handles
g_A>=10000/17689; that result was not rerun or relabeled as progress.

No Boolean upper estimate for tau in the remaining range, and no
actual Boolean R0 counterexample, has been obtained in this pass.
There IS a useful change of target: the GLOBAL qualitative assertion

    (S0, also called Rsign here)
       H_A<=0 for EVERY Boolean A with M(A)<=sqrt(|A|)

would already imply full Chowla with an absolute constant, through
the explicit padding amplification below. Thus the numerical margin
399/400 is not necessary for this route to be sufficient. This does
not prove Rsign or show that Rsign implies R0 pointwise.

The initial tensor/padding mechanism is the lead's derivation in
`cstar_R0_tensor_2026-10-23.md`; I independently checked its moments,
norm estimates, constants and finite integer lift. Sections 3 and 4
record the self-improvement and general-margin consequences explicitly.
Section 5 gives a concrete weighted sign falsifier, showing why the
exact unit coefficients cannot be replaced by positivity and a cap.

## 2. Audit of the complete two-variable correction

Let U(z),V(w) be real-coefficient analytic polynomials with zero
constants, and lambda>M_U+M_V. Define

    p=1/(lambda+U+V), p_U=1/(lambda+U), p_V=1/(lambda+V),
    p_mix=p-p_U-p_V+1/lambda.

The inverse is analytic beyond the closed bidisk, because its real
part denominator is bounded below there. Every coefficient of p_mix
has both indices positive. Its coefficient sector is orthogonal to
the two nonconstant pure-axis sectors. Hence, at this SAME lambda,

    g_total=g_U+g_V+lambda²||p_mix||2²,
    T_total=T_U+T_V,
    H_total=H_U+H_V-lambda*||p_mix||2².                 (1)

For T, an axis coefficient of p² is exactly the coefficient of the
corresponding one-variable inverse square. Formula (1) is exact for
Boolean axis supports; with weighted coefficients it remains exact
when the selected coefficient pairing is weighted correspondingly.
Also tau_total=(tau_U*g_U+tau_V*g_V)/g_total. No component is evaluated
at its own cardinality's lambda. In particular, this formula does not
assume component R0 and does not justify dropping mixed coefficients.

For a real C1 torus function h, a shifted L-point Riemann sum gives

    |<h(x,Lx)>-<h(x,y)>| <= pi/(2L)*||partial_x h||infinity.

If the total cardinality is n', the low-M split bound is <=sqrt(n'),
lambda=2sqrt(n'), d=Re(lambda+U+V)>=sqrt(n'), and
J=sum_(a in support U)a, the checked derivative bounds are

    ||partial_x(q²)||infinity <= J/d³,
    ||partial_x(2Re(U+V)q²)||infinity
                       <=6J/d²+4lambda*J/d³.

Thus

    |H_L-H_total| <=22J/(L*n').                       (2)

These estimates use the full reciprocal. They do not impose an
incorrect finite Fourier alias cutoff. This audits the lead's
finite-dilation transfer as well as its torus calculation.

## 3. A Boolean positive-energy probe and a rigorous conditional falsifier

Suppose V is a Boolean polynomial of cardinality N>=2^44,

    M_V<=sqrt(N)/2, g_V(2sqrt(N))<=2^-82.              (3)

The existence of such V is NOT established. Given it, define

    k=floor(sqrt(N)/2^20),
    B={1,9,...,9^(k-1)}, U=positive integer differences of B,
    m=k(k-1)/2, n'=N+m, lambda=2sqrt(n'),
    L=2^16*n'*9^k, A=support(U) union L*support(V).

The differences are distinct: in a nonzero relation involving at most
four signed differences, the least nonzero base9 digit has absolute
value at most4 and cannot be divisible by9. In particular the standard
difference-square identity gives M_U<=k/2.

The same no-carry observation verifies the exact triple count and
fourth-moment upper bound

    t=#{(a,b,c) in support(U)^3:a+b=c}=2*binom(k,3),
    <2Re U*(Im U)²>=t/2=binom(k,3),
    <|U|4> <=24*k^4.                                (4)

For the triple count the balanced three-edge configuration must be
the two-edge path across three ordered labels; each path has two
orders. For the fourth moment, choose four ordered source labels in
at most k^4 ways and then their four ordered target labels as a
permutation, in at most4! ways. Ignoring edge restrictions increases
the count. No asymptotic distribution theorem is needed.

The Taylor remainder used here is global, even though |U| can exceed
lambda on a positive front. Along sU, Re(lambda+sU)>=lambda/2 if
lambda>=k. Differentiation therefore gives

    ||lambda+U|^-4-lambda^-4|<=128|U|/lambda^5,
    |H_U-lambda^-4*binom(k,3)|<=6144*k^4/lambda^5.

For k>=4 and lambda/k>=2^19, it follows that

    H_U>=k³/(48lambda^4)>0.                           (5)

All constants in (4)--(5) check. In particular the remainder bound
does not rely on a false uniform expansion in U/lambda.

At the total lambda, the hypothesis on g_V still holds, because
|V/(lambda+V)| decreases pointwise as lambda increases above M_V.
The exact identity

    p-p_U=-[V/(lambda+V)]*p_U*(lambda+V)/(lambda+U+V)

and independence of the two variables imply

    ||p_mix||2² <= ||p-p_U||2² <=36*g_V/lambda².

For this estimate use |p_U|<=2/lambda,
|(lambda+V)/(lambda+U+V)|<=1+|U|/d, d>=lambda/4,
and ||U||2=sqrt(m)<=k<=lambda/2. Also
H_V>=-2M_V*Q_V>=-g_V/(2lambda). Consequently

    H_total >= k³/(48lambda^4)-(73/2)*g_V/lambda
             >= k³/(96lambda^4)>0.                  (6)

Indeed k/lambda>=2^-23 and g_V<=2^-82, and 4096>3504
provides the stated conservative slack. The stronger actual inverse
margin would improve constants but is not required.

For the finite lift, J<=k²*9^k. By (2), positivity follows whenever

    L>33792*J*n'/k³.

The displayed L meets that bound for k>=4 and exceeds max support(U).
Thus A is a genuine Boolean set, its cardinality is exactly n', and
M(A)<=M_U+M_V<sqrt(n') for ALL real angles. Its prescribed reciprocal
has H_A>0. This completes a conditional positive-energy counterexample
mechanism while retaining pure-axis and mixed costs. The sole
unproved input is the existence of a Boolean V satisfying (3).

## 4. Self-improvement of the GLOBAL sign statement

If Rsign were true, (3) would be impossible. For smaller N, the Boolean
bound |V|<=N gives the elementary estimate

    g_V(2sqrt(N))>=N/(2sqrt(N)+N)²
                 =1/(sqrt(N)+2)²>2^-82.

Thus Rsign alone would force a uniform positive gap on every
M_V<=sqrt(N)/2 input. The exact identity

    <f_V/|lambda0+V|²>=-g_V/lambda0, lambda0=2sqrt(N)

then gives

    ||f_V||1 >= (lambda0-M_V)²*g_V/lambda0
                >=2^-84*sqrt(N)                    (conservatively).

Since <f_V>=0, ||f_V||1<=2M_V. Therefore Rsign implies

    M_V>=2^-85*sqrt(N) for EVERY Boolean V.          (7)

For M_V>sqrt(N)/2, (7) is immediate; the other branch is covered
above. This is a CONDITIONAL theorem, not a proof of Rsign or Chowla.

This distinction corrects a possible overreading of the earlier
statement that qualitative negativity gives no square-root rate.
Negativity for ONE support supplies no quantitative margin. A sign
assertion for ALL Boolean supports, together with the explicit
augmentation closure, self-improves and does supply a uniform bound.
No converse from Chowla to Rsign has been proved.

More generally, for each fixed 0<delta<=1, use
k=floor(delta*sqrt(N)/2^20) and N>=2^44/delta². Then
k/lambda>=delta*2^-23 and the same argument applies if

    M_V<=(1-delta)*sqrt(N),
    g_V(2sqrt(N))<=delta³*2^-82.

The all-circle low-M budget is preserved because
M_U<=delta*sqrt(N)/2^21. For smaller N the elementary lower bound
exceeds delta³*2^-82. Hence universal Rsign would imply, for every
strict-margin class,

    g_V>delta³*2^-82,
    ||f_V||1>=delta³*2^-84*sqrt(N).                  (8)

This quantified dependence is useful: the padding argument does not
automatically extend to the zero-slack premise M_V=sqrt(N).

## 5. An explicit calibrated weighted SIGN falsifier

To test whether positivity and a coefficient cap could replace exact
unit amplitudes, take the finite Fejer taper

    V_N(z)=sum_{j=1}^N (1-j/(N+1))*z^j.

It has exactly N occupied positive frequencies, all coefficients in
(0,1), and Re V_N=(Fejer_(N+1)-1)/2>=-1/2. Even at the SAME
occupied-count calibration lambda0=2sqrt(N), its norm gap satisfies

    g_V(lambda0)<=3*N^-1/4  for N>=16.               (9)

Here is an explicit estimate, not a numerical observation. Put
epsilon=N^-1/4 and use the finite geometric identity

    V_N(z)=z/(1-z)
             -z*(1-z^(N+1))/[(N+1)*(1-z)²].

On epsilon<=|theta|<=pi, |1-e^(i theta)|>=2|theta|/pi,
and pi<4 gives |V_N|<=2*N^1/4+8*N^-1/2<=3*N^1/4.
Also |lambda0+V_N|>=lambda0-1/2>=1.5*sqrt(N).
Thus |V_N/(lambda0+V_N)|²<=4*N^-1/2 on that region.
On the central arc it is <=1, since Re V_N>=-lambda0/2.
The arc's Haar measure is epsilon/pi<=epsilon. Therefore
g<=epsilon+4epsilon²<=3epsilon, proving (9).

For EVERY integer N>=2^336, (9) gives g_V<2^-82. Apply the explicit
probe U, total-cardinality lambda, and integer L from Section 3.
Its estimates did not require Booleanity of V: the mixed norm bound,
negative-energy lower bound and derivative transfer remain valid for
this weighted V. The resulting polynomial

    U(z)+V_N(z^L)

has N+m distinct occupied positive frequencies, all coefficients in
(0,1], fixed lambda=2sqrt(N+m), ACTUAL lowM, and STRICTLY POSITIVE
zero-carrier energy. This is a fully explicit weighted sign falsifier.
It does NOT refute Rsign or R0, because most high-block coefficients
are not1. It is not an admissible Chowla counterfamily.

The scalar discrepancy is material: ||V_N||2² is asymptotic to N/3,
not N. A proof that keeps nonnegativity and an upper coefficient bound
but loses exact coefficientwise idempotence would admit this example.
Conversely, a positive Boolean unit-coefficient conclusion cannot be
inferred from this relaxed example. No rounding procedure preserving
both the weak gap and the low-M budget is supplied.

## 6. Exact unresolved step and strategic decision

The attempt to use only positive analytic machinery plus nonnegative
bounded coefficients FAILS by Section 5. The Boolean padding
counterexample mechanism SUCCEEDS conditionally by Sections 2--3.
What is still missing is genuinely Boolean: either a universal sign
inequality H_A<=0, or a concrete unit-coefficient V with a sufficiently
weak norm gap and a strict low-M margin. Neither follows from the
existing coefficient identities or the three successful finite tests.

Prioritize the qualitative selected-pairing target

    -sum_A[z^a](lambda+F_A)^-2 <=2*g_A/lambda,
    lambda=2sqrt(|A|), ACTUAL M_A<=sqrt(|A|),

before demanding R0's arbitrary numerical margin. By (7) a successful
UNIVERSAL proof would already resolve the original square-root goal.
This is the same prescribed-witness route with a weaker local target,
not a new proof mechanism or a proof of flatness. A failed R0 margin
with still-negative energy would not yet falsify Rsign.

If another proof attempt cannot exploit coefficientwise unit amplitude,
do not replace it with more successful controls or a GPU run. Pivot
to unrestricted signed Rayleigh directions outside a fixed reciprocal
ansatz, retaining the independent construction track. The weighted
taper is an adversarial test, not a restarted construction proposal;
the old fixed-degree, bounded-mean-reference, finite-automaton and
fixed-density projection pilots remain retired as recorded. No claim
that all other routes are blocked is justified.

## 7. Source audit of the single bounded adversarial search

After the paper derivation, I read `src/cstar_R0_adversary.py` and the
retrieved `R0_adversary_2026-10-23/{results,results_verification}.json`.
No additional evaluation was run by this advisor. The lead ran the
bounded search and independent verifier; both are terminal/PASS.

The source's normalization is correct: its complex grid array is
F=sum_A exp(i*a*x), lambda=2sqrt(n), q=-Im(F)/|lambda+F|², and the
objective is <2Re(F)q²>/(<q²>sqrt(n)). Exchanges keep exactly n=56
distinct positive frequencies with unit coefficients; zero is excluded.
One-, two- and four-frequency exchanges are proposal sizes, not weights
or multiplicities. The acceptance sign maximizes this objective.

The sampled M<=.98sqrt(n) condition is only a proposal constraint,
as labeled. It is not an all-circle premise for every visited support.
For the saved support, the producer separately checks the all-circle
M upper bound, then the full infinite-reciprocal residual certificate.
The refutation flags use the correct directions: a certified lower
normalized quotient above -.01 refutes numerical R0; strictly positive
certified H refutes S0. No normalization or hard-set-constraint error
was found in this source review.

The recorded four chains of3000 proposals in ambient frequencies
1..165 made NO improvement over the initial score
-0.35989817796264406; `best_step=-1`. The saved full reciprocal has a
tight negative certified interval, and the independent verifier PASS
is reported in the retrieved artifact. Neither R0 nor S0 was falsified.
This is one unsuccessful finite adversarial search, not a completeness
result, a new lower bound, or a reason to enlarge the box or deploy a
GPU. The new paper reduction and weighted sign falsifier, rather than
this lack of finite improvement, are the substantive results of the
cycle. No VM lifecycle action is authorized by finishing these jobs.
