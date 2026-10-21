# Advisor: popular differences, negative-part leakage, and a signed pivot

2026-10-21. Internal advisor, GPT-6.1 Sol/MAX. GOAL is active. I read
the current ROUTES ledger, P31/P61/P63/P66, P9/P19, and the previous
negative-part checkpoint before this attempt. No jobs, provisioning,
GPU expenditure, or additional agents. Only this note was edited.

This note proves an unrestricted torsion-free leakage inequality,
checks its exact quantitative limitation, and gives a genuine low-K
Boolean falsifier of the small-leakage upper bound that would be
needed to rescue that comparison. It does not prove Chowla or L25.

All integrals use dx/(2*pi). For nonempty finite A of distinct
positive integers, write S=+/-A, m=|S|=2n,

    D=sum_{s in S}exp(isx),  K=-min_R D,
    N=D_-,  mu=integral N,  v=integral N^2,
    b_h=hat N(h),
    r(h)=|S intersect(S+h)|,  w(h)=m-r(h).

Pi is the orthogonal Fourier projection onto S. Its convolution
kernel equals D exactly. The preceding checkpoint proved

    B_N=||(I-Pi)M_N Pi||_HS^2=sum_h |b_h|^2 w(h),
    B_N<=W:=sum_{h in S}w(h),
    sum_{h in S}b_h=-v,  sum_h |b_h|^2=v,
    v<=K*mu,  |b_h|<=mu.

## 1. Unrestricted popular-difference lower bound: proved

**Lemma.** For EVERY finite S subset Z of size m, and EVERY
nonnegative function N in L2 of circle mean mu>0, define v, b_h
and B_N as above. For every integer t with 0<=t<=m,

    B_N >= t*v-t^2*mu^2.                            (1)

No positivity of D, density, frequency ceiling, or support-filling
hypothesis enters this lower bound.

Here is an elementary proof of the needed popular-difference fact.
Sort two m-point integer sets U,V increasingly. Partition their
m-by-m pair grid into monotone chains C_i, 1<=i<=m: C_i runs
along row i through columns 1,...,m-i+1, then down column m-i+1
through rows i+1,...,m. These chains are disjoint, partition the
grid, and have lengths 2m-2i+1. Sums u_j+v_l strictly increase
along each chain. The first a chains therefore contain
a(2m-a) pairs and use each sum at most a times. Taking U=S,V=-S
gives, for every integer 0<=a<=m,

    sum_h min(r(h),a)>=a(2m-a).

Because sum_h r(h)=m^2, setting a=m-t yields

    sum_h (r(h)-(m-t))_+ <= t^2.                    (2)

Put M=mu^2. Since |b_h|^2<=M and sum_h|b_h|^2=v,

    sum_h r(h)|b_h|^2
      <=(m-t)v+M*sum_h(r(h)-(m-t))_+
      <=(m-t)v+M*t^2.

Subtracting this from m*v proves (1). This is an elementary
Pollard-type inequality in Z, with its torsion-free order step
displayed. It would fail for a finite subgroup with r(h)=m on
that subgroup.

## 2. Exact factor gap: this comparison cannot force flatness

In the actual low-K branch, K<=2sqrt(n)=sqrt(2m). First,

    mu>=m/(m+K).                                    (3)

Indeed P=D_+ has mean mu and hat P(h)=1+b_h for h in S.
Its nonnegativity implies 1+b_h<=mu. Summing and using
sum_S b_h=-v gives v>=m(1-mu); combine with v<=K*mu.

Consequently v/(2mu^2)<=K/(2mu)<=sqrt(2m)/2+1<=m
for m>=2. Rounding the continuous optimizer in (1) gives

    B_N >= v^2/(4mu^2)-mu^2/4,

as well as the exact integer maximum in (1). However, that maximum
can NEVER exceed

    v^2/(4mu^2)<=K^2/4<=m/2.                        (4)

The available PSD upper bound W is on the m^2 scale. In fact (2)
with t=m/2 (m is even), applied to the m selected shifts, gives

    sum_{h in S}r(h)<=3m^2/4,
    W>=m^2/4.                                      (5)

Thus, given the existing low-K bound v<=K*mu, the popular-difference
lower bound and the PSD upper bound are automatically compatible:
their comparison cannot add any lower bound on mu or v. The gap
is a factor of order m, not a missing absolute constant. Improving
the chain constants cannot close it.

The lower bound (1) also applies to the negative part of weighted
Fejer examples. For general real Fourier coefficients d_h on S,
the PSD calculation becomes
B_N<=sum_h w(h)|d_h|^2. Merely changing this weighted sum into
the Boolean count W does not separate the escape at the needed
scale. A further Boolean input is genuinely necessary.

## 3. A precise low-K falsifier of a proposed small-leakage repair

A natural attempted repair would be an upper bound B_N=O(m), or
B_N=O(K*mu), in the low-K Boolean branch. BOTH are false.
Use the already recorded no-carry difference control, rather than
launching a new family search. For k>=66 let q=k+1 and

    B={1,q,...,q^(k-1)},
    S={q^i-q^j:i!=j},   m=k(k-1),
    D=|F_B|^2-k>=-k.

Thus K<=k<=sqrt(2m), so the exact low-K hypothesis holds.

**Maximum-overlap calculation.** Encode the formal roots e_i-e_j
by q^i-q^j. Equality between two differences of roots has coordinate
coefficients of magnitude at most4. Since q>4, reducing at the
least nonzero base-q digit proves that this encoding introduces no
extra equality. The nonzero formal differences and their possible
overlaps are:

    e_i-e_j:                         2(k-2),
    2e_i-2e_j:                       1,
    2e_i-e_j-e_l, or its negative:    2,
    e_i+e_j-e_l-e_a (four distinct):  4.

In the first line one chooses a common head or a common tail,
with the remaining index different from i,j. In the other lines
the two roots are fixed up to the displayed two or four choices.
These cases exhaust the coefficient patterns of a root difference.
Therefore

    max_{h!=0}r(h)<=2(k-2).                         (6)

**Variance calculation.** The no-carry moments already proved in
advisor_OP140_attempt_2026-10-21.md give, for k>=66,

    integral D^2=k^2-k<=k^2,
    integral D^4<=10k^4,
    ||D||_1>k/5,       mu>k/10.

For completeness, the last inequality follows by Holder from
integral D^2>=3k^2/4, since
||D||_1^2>=(integral D^2)^3/integral D^4
>=27k^2/640>k^2/25. All moments use exact no-carry identities
through order4, not a CLT.

Write p_+=measure{D>0}. Since integral D_+=mu and
integral D_+^2<=k^2, Cauchy--Schwarz gives p_+>=1/100.
Also mu^2<=measure{D<0}*v<=(1-p_+)*v. Hence

    v-mu^2>=p_+*v>=p_+*mu^2>=k^2/10000.            (7)

Combining (6)--(7), with b_0=mu, proves

    B_N>=[m-2(k-2)]*(v-mu^2)
        >=k^4/20000.                               (8)

The last step uses k^2-3k+4>=k^2/2 for k>=4.
On the other hand K*mu<=k^2 and m<=k^2. Thus no absolute
constant can give either proposed small-leakage upper bound.
The obstruction is genuine Boolean and lies inside low-K.

This tests a specific prospective universal operator step. It is
not a new lower bound for this already understood difference-set
family. Its negative energy v is extensive; it is NOT a falsifier
of a universal v>=c*n target.

## 4. Negative energy is the L1 target up to constants

Within K<=2sqrt(n),

    mu^2<=v<=K*mu<=2sqrt(n)*mu.                     (9)

Therefore existence of some absolute lower bound v>=c*n is
equivalent, up to constants, to existence of an absolute L1 bound
||D||_1>=delta*sqrt(n). It is not a structurally new route.
For the exact L25 constants:

    L25 implies mu>=sqrt(n)/10 and v>=n/100;
    v>=n/5 suffices to imply L25;
    v>=c*n implies ||D||_1>=c*sqrt(n).

No general v lower bound or genuine low-K falsifier is derived
here. Assuming extensive variance merely to finish the leakage
argument would assume the missing flatness conclusion.

## 5. Check on selected-frequency odd translations

The root also considered the odd witnesses
u_t(x)=D(x+t)-D(x-t). These have spectrum only in S. The same
no-carry control gives an exact warning against making that
restriction universal.

Write z_i=exp(iq^i x). Every real witness supported on S has the
form u=sum_{i!=j}H_ij*z_i*conj(z_j), with H Hermitian and zero
diagonal. Orthogonality and the balanced directed-triangle count
give

    Q_u=||H||_F^2,
    integral D*u^2=2||H*1||_2^2-2||H||_F^2>=-2Q_u.  (10)

To see the second identity, every surviving triple of roots is a
directed triangle on three distinct indices. Choosing the D-edge
and ordering the two u-edges gives
2 sum_{i,j,l distinct}H_jl H_li
=2||H*1||^2-2||H||_F^2. No-carry uniqueness excludes extra
integer relations. This includes all sine witnesses supported in A,
and in particular u_t, whose entries are 2i*sin((q^i-q^j)t).

Thus their direct Rayleigh lower bound for K is at most2, or at
most1 for M, independently of k. This is the selected-frequency
weak-W1 obstruction; it is consistent with P9/P19 and the route
ledger, not a new proof route. Full odd-band witnesses are not
excluded.

For calibration, the mixed determinant certificate with u=D has
a=Q=m and H=2m(k-2), giving
K>=sqrt(2k^2-5k+4)-k+2, which is of order k. This is the
already recorded P10 moment mechanism, not new progress on the
family. It shows why failure of selected odd Rayleigh tests must
not be mistaken for failure of the actual mixed-coupling problem.

## 6. Actual signed-certificate pivot: exact boundary-notch formulas

After the two leakage comparisons fail, change the witness rather
than propose another PSD leakage estimate. For EVERY arbitrary
Boolean A and every integer h>=1 define

    delta_h=1_A(h),
    u_h=D(1-cos(hx))+delta_h.

This witness has mean zero, signed Fourier coefficients, and degree
at most max(A)+h. Put T(j)=hat(D^3)(j). Exact orthogonality gives

    a_h=integral D*u_h=w(h),
    Q_h=integral u_h^2=2w(h)-w(2h)/2-delta_h<=2a_h,
    H_h=integral D*u_h^2
       =(3/2)T(0)-2T(h)+T(2h)/2+2delta_h*a_h.       (11)

Thus an h with a_h>=alpha*n and H_h<=gamma*n^(3/2)
would give a correctly scaled mixed certificate, with coupling
normalized to n at cost Q'<=2n/alpha. The missing quantity has
changed from generic PSD leakage to an explicit signed cubic
curvature of additive-relation counts. No positive bounded-mean
reference is assumed; D+b-u_h need not be nonnegative.

I have NOT proved or assumed that a single h always works.
Multifront Boolean controls make such a one-notch assertion
suspect, so it must be checked analytically before any new run.
Allowing arbitrary signed combinations returns to the existing
unrestricted certificate problem; no universal cost bound is
obtained merely by choosing this basis. Formula (11) is an actual
unrestricted witness calculation and a concrete next quantity,
not a declared new route or a resolution of C*.

Adversarial scope: intervals nearly saturate popular-difference
majorization but have K of order n, so cannot refute a conditional
low-K claim. The exact no-carry control above falsifies the needed
small-leakage upper bound inside low-K. Weighted Fejer examples
still satisfy the generic functional-calculus inequalities, showing
why those inequalities alone are insufficient. Forced-plateau
controls retain their known adaptive signed certificates; no fixed
interior completion or bounded-mean reference is reintroduced.

**Decision / next derivation:** stop the popular-bound-versus-PSD
comparison and any conjectured B_N=O(n) repair. Retain the positive
lemma (1) and the precise falsifier (8). Primary work remains an
actual arbitrary-support signed cost estimate / OP140, with direct
full-band negative-Rayleigh alternatives and the independent
all-circle construction track. First analyze the cubic curvature
in (11), including multifront controls, or a genuinely different
signed decomposition; do not replace the missing estimate by
v>=c*n and count it as a new argument.

Status: paper auxiliary inequality and an exact universal-step
falsifier, with no claimed exponent improvement, universal flatness
bound, Lean/kernel check, outside review, or numerical experiment.

## 7. Subsequent audit: the universal single-notch hypothesis is false

The lead supplied the following all-h falsifier after Section6.
I checked the coefficient cases, cubic lower bound, and constants.
Thus Section6's formulas remain correct, but a universal sufficient
cost theorem using ONE u_h is now REFUTED. No new experiment or
new construction family is required for this decision.

Take a canonical cyclic (Q0,k,1) perfect difference set B,
Q0=k(k-1)+1, and ANY subset B' of size h=floor(3k/4).
Let A_1,A_2 be their positive integer difference sets and

    X=Q0-1,  L>6X,
    D=D_1(x)+D_2(Lx),
    k_1=k,  k_2=h,  m_i=k_i(k_i-1).

The support is a disjoint Boolean union, n=(m_1+m_2)/2, and
K<=k+h<=2sqrt(n) for k>=56, as checked in the averaged-reference
note. Define d_i(j)=hat D_i(j), R_i(j)=hat(D_i^2)(j), and
T_i(j)=hat(D_i^3)(j), with T_i=T_i(0).
All these coefficients are nonnegative integers; d_i(0)=0,
R_i(0)=m_i, and R_i(j)<=m_i.

**Uniform cubic lower bound.** The analytic polynomial F_{B_i}
has degree at most Q0-1. The multiplicities of its three-sums
are supported on fewer than3Q0 integers and sum to k_i^3.
Cauchy--Schwarz and integer Sidon uniqueness give

    integral |F_{B_i}|^6>=k_i^6/(3Q0),
    integral |F_{B_i}|^4=2k_i^2-k_i,
    T_i>=k_i^6/(3Q0)-4k_i^3+3k_i^2.

For k>=192, k_i>=2k/3 and Q0<=k^2 imply

    T_i>=[64/2187-4/k]k^4>=k^4/384.                (12)

Indeed 4/k<=1/48 and 64/2187>1/48+1/384.

**All coefficient cases.** Expanding D^3 yields

    T(z)=T_1(z)+3sum_b R_1(z-Lb)d_2(b)
                 +3sum_c d_1(z-Lc)R_2(c)
                 +1_{L divides z}T_2(z/L).

Since L>6X, each mixed sum has at most one nonzero term: its
low-frequency support has width at most4X. Consequently, for z>0,

    0<z<=3X: T(z)=T_1(z)+3m_2*d_1(z);
    z=Lb:    T(z)=T_2(b)+3m_1*d_2(b);
    otherwise: T(z)<=3(m_1+m_2).

The first two cases are disjoint. Also T(0)=T_1+T_2 and every
T(2z)>=0. In the first case, retaining the nonnegative T_1(2z)
component of T(2z) preserves the exact bracket

    (3/2)T_1-2T_1(z)+T_1(2z)/2
       =integral D_1^3(1-cos(zx))^2>=-4k*m_1.

The lower bound uses D_1>=-k and (1-cos)^2<=4. In the divisible
case, the same bracket for D_2 is at least -4h*m_2. The remaining
case uses the displayed upper bound on T(z). Finally the term
2*1_A(z)*a_z in (11) is nonnegative. Uniformly for EVERY integer
z>=1, these facts give

    H_z>=(3/2)min(T_1,T_2)-(4k+6)(m_1+m_2)
        >=k^4/256-8k^3-12k^2
        >=k^4/512,                                (k>=8192). (13)

No omitted residual or sampled phase is used in this estimate.

Since a_z<=m_1+m_2<=2k^2, the positive root of
Q_z*K^2+H_z*K-a_z^2 is at most

    a_z^2/H_z<=2048.                               (14)

Thus every LOWER bound on K furnished by a single-notch mixed
determinant is capped by2048. This is NOT an upper bound on the
actual K. Equivalently, after scaling any notch to coupling n,

    H'_z=(n/a_z)^2 H_z>=n^2/2048,

so its normalized mixed cost diverges uniformly over z. The
single-notch sufficient-certificate principle fails even allowing
arbitrary scalar normalization and arbitrarily large z.

The extra statement that actual K is of root scale is unnecessary
for this falsification. It can be justified for the existing choice
L=Q0^3: convolving D with the mean-one Fejer kernel of degree L-1
removes the L A_2 block and approximates D_1 uniformly within
m_1 X/L. Positivity of convolution gives

    K>=K(A_1)-m_1 X/L.

The already proved dense theorem applies to A_1, whose cardinality
is at least half its frequency ceiling, giving K(A_1)>=c*k.
Thus K>=c*k-o(1) for that choice of L. The present coefficient
argument alone does not establish this extra lower bound for every
L merely satisfying L>6X.

**Mandatory pivot.** Do not run a universal single-notch optimizer.
The popular-difference-versus-PSD comparison and its O(n) leakage
repair failed, and the subsequent single-notch restriction now has
an exact all-h falsifier. Multiple adaptive notches, arbitrary
signed witnesses, full-space residual certification, OP140 and
direct full-band Rayleigh alternatives survive. No square-root
bound follows by naming those surviving spaces; the next claim
must supply an actual unrestricted cost estimate. Independent
all-circle construction work remains active in the full goal.

Status: lead's universal-step falsifier independently checked on
paper by the advisor; no new computation, Lean check, outside
review, or spending.

## 8. Refinements: only notch cost fails, and broader witnesses inherit

Subsequent advisor audit, 2026-10-21. Both refinements proposed by
the lead are valid. They clarify the distinction between failure
of the single-notch restriction and failure of unrestricted witnesses.

**Every notch already has macroscopic coupling and bounded norm.**
For the Section7 support S=S_1 union L*S_2 and z!=0, the two
within-block overlaps r_1(z) and 1_{L divides z}r_2(z/L) cannot
both be nonzero. Indeed a nonzero first overlap requires
|z|<=2X<L, whereas the second requires L divides z.
Each cross-overlap has at most one pair: its low-frequency point
lies in [-X,X] and in a fixed residue class modulo L, with
2X<L. Consequently

    r_S(z)<=max(m_1,m_2)+2,
    a_z=m-r_S(z)>=min(m_1,m_2)-2>=n/4.

The final inequality certainly holds at k>=8192. For example,
h>=k/2 gives 7m_2-m_1>=3k^2/4-5k/2>=16 already for k>=8,
which is equivalent to m_2-2>=(m_1+m_2)/8=n/4.
Thus all these notches satisfy

    a_z>=n/4,    Q_z<=2a_z<=4n,

and normalizing their coupling to n gives

    Q'_z<=8n,    H'_z>=n^2/2048.

In particular, lack of coupling or an excessive norm budget does
not explain their failure: their mixed COST alone is too large.

**Exact bandwidth inheritance lemma.** Let A=A_0 disjoint union
A_far be any Boolean support, and let u be any real mean-zero
trigonometric polynomial of degree at most B_w. If

    max(A_0)<=B_w,    min(A_far)>2B_w,

then u has exactly the same a, Q and H for D_A as for D_{A_0}.
Proof: u has no frequencies beyond B_w, u^2 has none beyond
2B_w, and every frequency of D_{A_far} is strictly larger than
2B_w. Orthogonality annihilates its contribution to both a and H;
Q does not depend on A. The stated ceiling on A_0 is natural for
the intended witness, although it is not required for this simple
orthogonality implication itself.

If |A_0|>=eta*|A|, a witness with coupling alpha*|A_0| therefore
retains macroscopic coupling at least alpha*eta*|A|. Norm and
mixed-cost bounds of orders |A_0| and |A_0|^(3/2) remain bounds
of the corresponding orders in |A|, with absolute constants when
alpha and eta are fixed.

For the Section7 control, choose the canonical full block A_0=A_1
and the far block L*A_2. The paper proof in
advisor_L25_derivation_2026-10-21.md Section5 gives
||D_{A_0}||_1>=c*k with one absolute c>0 eventually. I rechecked
that proof: with F=S+R, classical MZ gives ||R||_6=O(sqrt(k));
the three mixed fourth-moment terms are O(k^(3/2)), O(k^(5/3)),
and O(k^(11/6)). Thus integral |R|^4~4k^2/3,
Y=|R|^2-k has integral Y^2~k^2/3 and integral |Y|^3=O(k^3),
so ||Y||_1>=c_1*k. The O(sqrt(k)) L1 difference between D and Y
preserves the lower bound. This uses the already recorded MZ
dependency; it is NOT an inference from a lower bound on M alone.

The existing VP sign-witness lemma then supplies a witness u_0 of
degree B_w<2max(A_0)<=2X with

    a_0=n_0,    Q_0=O(n_0),    |H_0|=O(n_0^(3/2)),
    n_0=|A_0|.

Since min(L*A_2)>=L>6X>2B_w, this witness inherits exactly to
the two-block support. Also n_0/n>=1/2. It therefore supplies a
properly scaled mixed certificate for the full control, despite
the all-notch lower bound (13). No universal L25 assumption, new
family M-bound claim, or numerical optimization is used here.

Status: both refinements checked on paper; the control remains a
counterexample to a proposed restricted universal method, not to
the existence of unrestricted signed certificates. No new jobs,
spending, external review, or Lean verification.

## 9. Positive changed mechanism: additive closure under separated dilation

The lead proposed this closure statement. I independently checked
the full expansion. It is valid with L a positive INTEGER and,
for the unchanged-budget corollary, beta>=0 and gamma>=0.

**Exact closure lemma.** Let D_0,D_1,q_0,q_1 be real mean-zero
trigonometric polynomials with integer frequencies. Suppose
degree(D_0)<=X_0 and degree(q_0)<=B_0. No upper bandwidth bound
on D_1 or q_1 is needed beyond their being finite. If

    L>max(2B_0,X_0+B_0,X_0),
    D(x)=D_0(x)+D_1(Lx),
    q(x)=q_0(x)+q_1(Lx),

then

    a=a_0+a_1,    Q=Q_0+Q_1,    H=H_0+H_1.        (15)

Here a_i=integral D_i*q_i, Q_i=integral q_i^2, and
H_i=integral D_i*q_i^2. Integer dilation preserves all block
integrals. Orthogonality removes the two coupling cross terms,
since L>X_0,B_0, and the norm cross term since L>B_0.

For completeness, expand all cubic terms:

    Dq^2=D_0 q_0^2+D_1(Lx)q_1(Lx)^2
       +D_0 q_1(Lx)^2+D_1(Lx)q_0^2
       +2D_0 q_0 q_1(Lx)+2q_0(D_1 q_1)(Lx).

The four mixed integrals vanish individually:

1. q_1(Lx)^2 has a constant Q_1 and nonconstant frequencies
   of magnitude at least L. The latter cannot pair with D_0,
   since X_0<L; the constant pairs with mean(D_0)=0.
2. D_1(Lx) has no constant term, and q_0^2 has degree at most
   2B_0<L.
3. D_0 q_0 has degree at most X_0+B_0<L, whereas q_1(Lx)
   has no constant term.
4. (D_1 q_1)(Lx) has a constant a_1 and all other frequencies
   at least L. The latter cannot pair with q_0; the constant
   pairs with mean(q_0)=0.

This proves (15). In particular, a constant generated by a high
product is accounted for rather than incorrectly treated as a
nonzero high frequency.

**Arbitrarily many blocks with unchanged budgets.** Iterate (15),
choosing each new integer scale above twice the maximum of the
previous aggregate D and q bandwidths. This is sufficient for
the displayed separation condition at each stage.
If the underlying D_i are genuine Boolean polynomials, their
frequency supports are disjoint under this separation, so
n=sum_i n_i. If every block has

    a_i=n_i,    Q_i<=beta*n_i,    H_i<=gamma*n_i^(3/2),

then the aggregate satisfies

    a=n,    Q<=beta*n,    H<=gamma*n^(3/2),         (16)

with EXACTLY the same beta and gamma. Indeed a and Q add, and

    sum_i n_i^(3/2)<=sqrt(n)*sum_i n_i=n^(3/2).

The hypothesis gamma>=0 is required for this last comparison.
For negative gamma, exact additivity still holds but retaining
the same negative gamma in (16) is not justified; the common
nonnegative bound gamma=0 remains available.

The resulting square-root mixed-certificate constant is independent
of the number of blocks. For beta>0 and gamma>=0, positivity gives

    K/sqrt(n)>=[sqrt(gamma^2+4beta)-gamma]/(2beta).

This is conditional on block certificates, not a proof that every
arbitrary A admits the required decomposition or certificates.

**Application and scale qualification.** Canonical full Singer
blocks above the common threshold have the uniform L1 lower bound
checked in Section8, and therefore VP witnesses with uniform
beta,gamma and degree<2Q_i.
Their sufficiently separated unions inherit (16), regardless of
the number of fronts. The earlier recurrence L_j=product_{i<j}
(L_i Q_i) guarantees disjoint blocks and exact front overlaps but
does NOT automatically guarantee witness-band separation. One may
instead choose

    L_0=1,    L_j=4*product_{i<j}(L_i Q_i).

Then each new scale exceeds twice the previous witness bandwidth,
and L_j/(L_i Q_i) remains an integer. Thus both the earlier exact
front-overlap accounting and the present certificate closure hold.
The two-block L=Q0^3 example already meets the condition.

This is a true additive signed repair of those separated-front
controls. It incurs no deterioration in norm or mixed-cost
constants as the number of certified blocks grows. It does not
revive bounded-mean positive references, establish a decomposition
for arbitrary supports, or give a vanishing-ratio construction.

Status: positive paper closure lemma independently checked by the
advisor. No new computation, expenditure, external scrutiny, or
Lean/kernel formalization.
