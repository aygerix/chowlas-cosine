# Joint boundary L1: an admissible finite-field counterexample

2026-10-23. Sole internal AI advisor. Paper derivation and read-only review
of P14/P20, `.research/agents/bedert_avg.md`, and the current handoff.
No computation, VM operation, GPU, additional agent or outreach. Shared
Dirichlet is untouched. No Lean/kernel or external-priority claim.

## 1. Exact candidate, conditional implication, and result

For a finite symmetric S subset Z\{0}, let

    D=sum_(s in S) exp(isx), N=|S|, K=-min_circle D,
    B_t={x in S:x-t in S,x+t not in S}, t in S.

The candidate under review is an absolute-constant estimate

    sum_(t in S) ||F_Bt||_1^2 <= C*(N*K+K^4).              (JB)

The L1 norm uses normalized Haar measure. Its group-independent analogue
is FALSE, even when every summation frequency t is required to be inside
S, and even in the genuinely spiky regime N/K^2 tending to infinity.
The INTEGER statement (JB) is not refuted here.

More precisely, for every odd prime p>=11 there is a genuine Boolean
symmetric S subset F_p^4\{0} with

    K=p, N=p*(p-1)*(p^2+1),
    p/3 <= ||F_Bt||_1 <= 4p-1 for EVERY t in S.            (1)

Consequently

    [sum_(t in S)||F_Bt||_1^2]/[N*K+K^4] >= p/11.        (2)

Thus averaging over admissible t does not repair the finite-group
obstruction. The proof below computes the Fourier transform on the
entire nonzero dual null cone; this already yields a matching-order
L1 lower bound, without evaluating every remaining Fourier modulus.

For completeness the parent's conditional exponent bookkeeping checks:
abstract Prop7.3 with Q=F_Bt gives

    sum |B_t| <= C0*K^2*sum ||F_Bt||_1^2.

If (JB) held in Z, the recorded Shankar lower bound for N>=2K^2 would give

    N^2 <= C1*(N*K^4+K^7).

Either K is at least a constant times N^(1/4), or at least a constant
times N^(2/7), which is stronger for N>=1. The excluded regime
N<2K^2 already gives a square-root lower bound. Hence (JB) WOULD give
a uniform exponent1/4. This is a conditional implication, not a proved
integer bound; I do not assume Shankar's ordering identity in the group.

## 2. Model, characters, and the exact global spectrum

Let d be a nonsquare in F_p and define the nondegenerate quadratic form

    Q(x)=x1*x2+x3^2-d*x4^2,
    beta(x,y)=[Q(x+y)-Q(x)-Q(y)]/2.

Put Z={x:Q(x)=0} and S=F_p^4\Z. This is the P20 elliptic-quadric
complement, but I use ALL anisotropic t in S, rather than its older
isotropic test frequency outside S.

Identify the dual using

    chi_xi(x)=e_p(2*beta(xi,x)), e_p(v)=exp(2pi*i*v/p).

Since beta is nondegenerate these are all characters. For r!=0,
completion of the square gives

    sum_x e_p(r*Q(x)+2*beta(xi,x))
          = -p^2 * e_p(-Q(xi)/r).                       (3)

The sign can be checked directly: the x1*x2 sum is p; the anisotropic
x3^2-d*x4^2 sum is -p. The latter also follows by counting norm fibers
in F_(p^2): the zero fiber has one point and each nonzero fiber p+1.
Thus no unverified square-root cancellation estimate is being imported.

Character orthogonality in the equation Q(x)=0 now gives

    |Z|=p^3-p^2+p,
    F_Z(xi)=-p*(p-1) if xi!=0 and Q(xi)=0,
    F_Z(xi)=p         if Q(xi)!=0.

For nontrivial characters F_S=-F_Z. Its actual minimum is -p, and

    N=p^4-|Z|=p*(p-1)*(p^2+1).

There are exactly

    J=|Z|-1=(p-1)*(p^2+1)=N/p                             (4)

nonzero dual-isotropic characters. This entire spectral sector, not
one exceptional character, will contribute to each boundary L1 norm.

## 3. The admissible boundary is a cone minus two disjoint sections

Fix ANY t in S and write q=Q(t)!=0. For x in B_t put z=x+t. Then

    Q(z)=0,
    Q(z-t)=q-2*beta(z,t)!=0,
    Q(z-2t)=4q-4*beta(z,t)!=0.

Define, for a!=0,

    E_a={z:Q(z)=0, beta(z,t)=a*q}.

The two sets E_(1/2),E_1 are disjoint because p is odd and q!=0.
Exactly, with no inclusion-exclusion remainder,

    B_t=-t+[Z\(E_(1/2) union E_1)].                     (5)

This also verifies the required t-in-S hypothesis without changing the
model's actual K or using a nonadmissible isotropic modulation.

## 4. Exact transforms on every nonzero dual-isotropic character

Fix xi!=0 with Q(xi)=0 and let b=beta(xi,t). The two constraints defining
E_a give the double orthogonality formula

    F_Ea(xi)=p^-2*sum_(r,s in F_p) e_p(-2*s*a*q)
                        *sum_z e_p(r*Q(z)+2*beta(xi+s*t,z)).

The r=0 term vanishes: it could survive only if xi+s*t=0, impossible
for nonzero isotropic xi and anisotropic t. Using (3) for r!=0 yields

    F_Ea(xi)=-sum_s e_p(-2*s*a*q)
                   *sum_(r!=0) e_p(-[q*s^2+2*b*s]/r).

For any c in F_p, the last r-sum is p-1 if c=0 and -1 otherwise.
The complete s-sum of e_p(-2*s*a*q) is zero. Therefore

    F_Ea(xi)=-p*sum_(s:q*s^2+2*b*s=0) e_p(-2*s*a*q)
       = -p                            if b=0,
       = -p*[1+e_p(4*a*b)]             if b!=0.         (6)

Both roots of the quadratic have been counted once; they coalesce
when b=0. In particular no extra factor2 occurs in that case.

Combining (5),(6) with F_Z(xi)=-p(p-1) gives the exact boundary formula

    F_Bt(xi)=-p*(p-3),                              if b=0,
    F_Bt(xi)=-p*e_p(-2*b)
                    *[p-3-e_p(2*b)-e_p(4*b)],      if b!=0. (7)

The translation phase is essential in the exact expression and harmless
for its modulus. For p>=5,

    |F_Bt(xi)| >= p*(p-5)                           (8)

uniformly over EVERY admissible t and EVERY character in (4).

## 5. Uniform L1 size and failure of the joint estimate

The normalized dual Haar measure gives weight p^-4 to each character.
Summing (8) over the J=N/p characters in (4),

    ||F_Bt||_1 >= N*(p-5)/p^4
                >=(1-1/p)*(p-5) >=p/3, p>=11.       (9)

For a matching-order upper bound, at xi=0 the same double sum has an
additional r=s=0 contribution p^2; hence |E_a|=p^2-p. Therefore

    |B_t|=p^3-3p^2+3p.

The exact full spectrum of Z gives

    ||F_Z||_1=1+2*(p-1)*N/p^4 <=2p-1.

By Parseval and Cauchy-Schwarz, ||F_Ea||_1<=sqrt(p^2-p)<=p.
The triangle inequality in (5) proves the upper bound4p-1 in (1).
Thus every admissible boundary, not merely a positive fraction of them,
has L1 norm Theta(K).

Now (9) gives sum ||F_Bt||_1^2>=N*p^2/9. Since N>=p^4/2,

    N*K+K^4=N*p+p^4 <=N*(p+2),
    ratio >=p^2/[9*(p+2)] >=p/11, p>=11.

This proves (2). Here N/K^2 grows like p^2, and N/K^3 grows like p;
the additive K^4 term cannot hide the failure as it did in bounded-ratio
integer controls. The model has K of order N^(1/4), so its failure of
(JB) is compatible with the exponent that (JB) was meant to establish.

## 6. What is and is not retired

The old bedert_avg Sections5-7 allowed an empirical estimate of this
shape for the PARTICULAR decomposition norms ell_t=||Q_(1,t)||_1.
They did not prove the exact-B estimate (JB). These are different
statements. The present calculation refutes the group analogue of
(JB); it does not refute that decomposition claim or the integer
version of either statement.

It also identifies the spectral obstruction precisely: all boundary
polynomials retain p^2-sized Fourier values on the SAME p^3-sized dual
null cone. Averaging t, positivity, exact Boolean convolution
idempotence and the requirement t in S do not remove this mass. A
group-agnostic five-linear/PSD proof of (JB) is therefore impossible.

Any proof in Z must exploit a genuinely integer ingredient that fails
here. In this model each t-orbit is a p-cycle. Since Q(t)!=0, the
restriction of Q to a t-line is a quadratic with at most two zeros;
the orbit is full or has at most two holes. Their spectral repair uses
the finite-field quadratic identities around the entire cycle. In Z,
the corresponding finite runs have ordered endpoints rather than a
periodic wrap. Merely naming torsion-freeness is not an estimate: the
missing step would have to make those endpoint/order constraints
quantitatively control the JOINT Fourier mass or a chosen residual
decomposition. There is no homomorphic transfer of F_p^4 into Z, and
no all-circle integer lower bound for a chosen encoding is supplied.

Strategic decision: stop trying to prove (JB) by group-independent
positivity or joint Gram algebra. Preserve this exact admissible-t
falsification before returning to an order-sensitive integer lemma or
to a genuinely chosen Q_(1,t) plus its signed residual. The latter
still needs an actual construction/inequality; allowing arbitrary Q
alone is the already-recorded K-functional restatement, not progress.
No new finite experiment, larger finite-field sweep, or GPU run is
needed to decide this particular obstruction.

## 7. Integer-order addendum: exact endpoint witness and its constant term

The parent next proposed a genuinely order-sensitive witness. Let
t>0 belong to S, m=|B_t|, and

    q_t=(1-exp(itx))*F_Bt.

Each B_t element is the top of a finite t-run in S of length at least2.
Its reflected run has its start at the negative of such a top. Summing
top-minus-start over all these runs proves the exact identity

    sum_(b in B_t) b=(t/2)*|S intersect(S+t)|.

Also B_t intersect(B_t+t) is empty because the latter points are outside
S, and B_t intersect(B_t+2t) is empty because such a second top would
have predecessor b+t inside S. These facts imply

    <D,q_t>=m, ||q_t||_2^2=2m.

The complex witness has real coupling. However its mean is

    q0=-delta, delta=1_(-t in B_t),                      (10)

NOT +delta. For example S=+/-{1,2},t=1 gives
q=z^-1-1+z^2-z^3. Set q_c=q_t+delta to obtain mean zero. If
H=<D*|q_t|^2>, then exactly

    <D,q_c>=m,
    ||q_c||_2^2=2m-delta,
    <D*|q_c|^2>=H+2*delta*m.

Cauchy-Schwarz for the nonnegative measure (D+K)dx/(2pi) gives

    m^2 <= K*[H+2*delta*m+K*(2m-delta)].                (11)

Equivalently the uncentered determinant has coupling m-K*delta.
It must not be replaced by m when delta=1. At the largest positive
frequency t=max S, delta=0, so the simple mean-zero formula is exact.

The elementary inequality K>=1 follows from the nonzero coefficient
1 of the nonnegative polynomial D+K. Thus a universal H<=C*K*m
would imply m<=(C+4)K^2, while H<=C*K^2*m would imply
m<=(C+4)K^3. Combined with the recorded Shankar boundary lower
bound these would give exponents1/3 and1/4, respectively. Centering
allows summation over ALL admissible t; no restriction such as
2t not in S has been silently imposed on that summation.

## 8. Exact energy cancellations and elementary pattern checks

Write a_d=1_S(d), including a0=0. Fourier orthogonality gives

    H=2*sum_(b,c in B_t) a_(b-c)
          -sum_(b,c in B_t)[a_(b-c+t)+a_(b-c-t)]
     =2*sum_(b,c in B_t)[a_(b-c)-a_(b-c+t)].           (12)

The last equality uses the symmetry under exchanging b,c. Its diagonal
is -2m because t in S. This formula retains all integer positions and
all signed cross terms; neither the first-moment identity nor the two
forbidden differences turns its remaining coefficients nonpositive.

For S=+/-{1,...,n}, t=n, one has B_t={1,...,n-1}, m=n-1.
The first count in the last expression of (12) is m(m-1), and the
second m(m+1)/2. Hence

    H=m*(m-3)=(n-1)*(n-4).

Thus H may be positive even for a single interval; an order-only sign
shortcut is false. The interval's large K prevents this example by
itself from falsifying an upper bound at scale K*m.

As a separate sparse difference-pattern check, take a no-carry encoding
of the root support {e_i-e_j:i!=j} using powers of9, and let
t=e_1-e_2>0. All relations required in (12) have coefficients bounded
by4, so this encoding preserves them exactly. Writing l=k-2,

    B_t={e_1-e_j:j>=3} union {e_i-e_2:i>=3},
    m=2l,
    sum a_(b-c)=2l(l-1), sum a_(b-c+t)=2l,
    H=4l(l-2)=4(k-2)(k-4).

Here D=|sum exp(ib_j*x)|^2-k and K<=k. This check exposes positive
within-star correlations; it does not supply a growing violation of
either K scale by itself. No actual K lower bound is inferred from
the square identity.

## 9. A genuine integer counterfamily to H<=C*K*|B_t|

The parent supplied the following probabilistic family. I independently
checked its exact coefficients, expectation, collision terms, bounded
differences and all-circle probability argument. No computation is
needed for its existence theorem.

For an integer Q, force X_Q=1 and take independent

    X_j~Bernoulli(1-j/Q), 1<=j<Q,
    A={j:X_j=1}, S=+/-A, t=Q.

The admissible boundary is exactly

    B_t={s in{1,...,Q-1}:Y_s=1}, Y_s=X_s*X_(Q-s).

It is symmetric about Q/2, lies in the positive integers, and q0=0.
For d=|s-u|, (12) becomes

    H=-2*sum_s Y_s
        +sum_(s!=u)Y_s*Y_u*[2*X_d-X_(Q-d)].           (13)

In the noncollision case, the variables indexed by
s,Q-s,u,Q-u,d,Q-d are distinct. Put v(r)=r(1-r). The expectation
of its summand is

    f(s/Q,u/Q), f(r,z)=v(r)*v(z)*[2-3|r-z|].

Direct integration yields

    integral v=1/6,
    integral integral v(r)*v(z)*|r-z|=1/140,
    integral integral f=2/36-3/140=43/1260.             (14)

For example the middle integral equals twice the integral of
(r-r^2)*(r^3/6-r^4/12) over[0,1]. Thus the sign and constant in
the leading term are positive.

Here is an explicit conservative error bound. There are15 possible
index equalities among the six indices. On each of the chambers s>u
and s<u an equality is a nonidentically-zero affine equation, with
at most Q integer solutions. Thus at most30Q pairs are collisions.
Each collision changes the expected summand from f by less than3.
The function f is Lipschitz in each coordinate with constant at most
11/16; the square-grid Riemann error and omitted diagonal together
are at most3Q/2. Finally -2*E sum Y_s>=-2Q. Consequently

    E H >=(43/1260)*Q^2-100Q.                         (15)

To verify the bounded-difference constant, changing X_a affects at
most two Y rows. Updating these with the kernel fixed changes the
ordered sum by at most8Q. Updating the kernels at d=a and d=Q-a
costs at most4Q, and the linear term costs at most4. Therefore16Q
is a valid uniform bit-flip bound. McDiarmid's inequality gives

    Pr[H < E H-r] <=exp(-r^2/(128Q^3)).

For every Q>=2^21, (15) is at least Q^2/40, since43/1260>1/30
and Q>=12000. Taking r=Q^2/80 therefore gives

    Pr[H<Q^2/80] <=exp(-Q/819200)<1/4.                (16)

Independently, the exact mean of D is

    E D=Fejer_Q-1+2cos(Qx)>=-3.

For its centered noise R, Hoeffding at each point gives

    Pr[|R(x)|>u] <=2exp(-u^2/(2Q)).

On a16Q^2-point grid put u=sqrt(2Q*log(128Q^2)). The union bound
has failure probability at most1/4. Deterministically
||R'||infinity<=Q(Q-1); the nearest grid point is within pi/(16Q^2),
so the entire-circle discrepancy is below u+1. With probability at
least3/4 the ACTUAL global K therefore satisfies

    K<=4+sqrt(2Q*log(128Q^2)).                        (17)

The events (16),(17) occur simultaneously with positive probability.
For such a genuine integer set, m<=Q, H>0, and

    H/(K*m) >= Q/[80*(4+sqrt(2Q*log(128Q^2)))] ->infinity.

This rigorously refutes EVERY absolute-constant H<=C*K*m claim.
It does not refute H<=C*K^2*m or prove an all-circle upper bound
M/sqrt(n) tending to zero. The upper bound available here grows at
the square-root-log scale after normalization. No sampled minimum
is being substituted for the all-circle claim (17).

## 10. Remaining K^2 scale and the weaker joint statement

For ANY integer S and this witness, D<=N and ||q_t||^2=2m give
the elementary upper bound H<=2N*m. Consequently failure of a
universal H<=C*K^2*m along a sequence would REQUIRE

    N/K^2 ->infinity along a subsequence.

For S=+/-A this is n/(2M(A)^2). Such an unbounded violation would
itself yield a genuine Chowla counterfamily. Conversely Chowla's
square-root bound would immediately imply H<=C*K^2*m by the
same trivial upper estimate. Thus the remaining bound is a meaningful
weaker consequence of the full conjecture, not something the linear
counterfamily or a few successful controls can settle. Its proof
would still require a new integer interaction in (12); none is
obtained by dropping its signed terms.

Replacing the failed raw joint target by C*(N*K+K^6) has no derivation
in this addendum. The quadric model merely has matching K^6 order;
that is not a reason to conjecture the weaker target universally.
No probe is justified without an actual mechanism. In particular do
not promote the finite-group saturation, the exact first moment of
B_t, or the forbidden differences t,2t into an unproved norm bound.

The concrete retained question is the K^2 endpoint-energy inequality
with ALL terms in (12), together with the centered determinant (11).
The integer linear-scale claim is now retired on paper; the stronger
raw joint L1 estimate remains blocked by the exact finite-group
adversary and needs order-sensitive input, not a changed exponent
chosen to fit that model.

## 11. Checked localization of the remaining endpoint energy

The parent subsequently derived a useful exact near-maximum cancellation.
I independently verified all factors and its domain. It holds in any
abelian group, so it supplies no torsion-free ingredient by itself.

The sets B_t and B_t-t are disjoint subsets of S, both of size m. Write

    q_t=chi_t*(F_(B_t-t)-F_Bt).

Subtracting1 from every character in these two equal-cardinality sums
and applying Cauchy-Schwarz proves pointwise

    |q_t|^2 <=2m*sum_(s in B_t union(B_t-t))|chi_s-1|^2
              <=4m*(N-D).                           (18)

The second inequality uses S=-S and
sum_(s in S)|chi_s-1|^2=2(N-D). It does not use mean-zero q_t,
so the exceptional constant term in (10) is harmless here.

For any tau,Delta>0, the low positive band0<D<=tau contributes at
most2*tau*m to H. On the high band D>=N-Delta with D>0, (18)
bounds |q_t|^2 by4m*Delta. Since mean D=0 and D>=-K,

    integral D_+=integral D_- <=K.

The high positive contribution is therefore at most4m*Delta*K.
Ignore the negative contribution to obtain

    H <=2*tau*m+4m*Delta*K
                  +integral_(tau<D<N-Delta) D*|q_t|^2. (19)

If tau>=N-Delta the positive bands overlap. Allocate the low band
first, then its complement inside the high band: (19) still holds,
with empty middle band. Atoms at either boundary are included in
the low or high term, so the finite-group statement has no missing
endpoint mass.

In particular

    H <=6K^2*m+I_mid,
    I_mid=integral_(K^2<D<N-K) D*|q_t|^2.             (20)

Hence I_mid<=C*K^2*m, with a constant uniform in S,t, is a precise
sufficient target for the weaker endpoint-energy bound. The centered
determinant (11), not the false uncentered formula, then gives the
cubic run-top bound and conditional exponent1/4 discussed above.

The earlier P20 counterexample does NOT obstruct (20): its only
nontrivial positive spectrum is p(p-1)<K^2, and at the identity D=N
one has q_t=0. Thus I_mid=0. This observation neither repairs (JB)
nor contradicts its exact Fourier-L1 counterexample: (JB) is a
different and stronger demand on the complete boundary polynomials.

Relative to the existing P14 record, (18) is an elementary equal-size
near-period estimate at the top N-Delta. It removes the neighborhood
of the absolute maximum and the low positive band, but leaves the
entire window K^2<D<N-K. This window includes the previously recorded
intermediate K^3 layer whenever N is sufficiently large. No claim is
made that its joint energy has been controlled, that its size forces
an integer contradiction, or that merely localizing it is a new
unrestricted lower bound. A next proof must retain and estimate this
actual window or change the witness, rather than delete its signed
or coupled terms.

## 12. Existing P22, repaired admissibility, and the actual middle obstruction

The parent correctly brought forward the stronger EXISTING P22/O4 model.
P20's old heading describing a group exponent in[3,4] is historical:
P22 already proves the group run-top exponent is4. Group G3 must not
be revived. The following is a new energy consequence of that recorded
model, not a new finite-group construction or a proof in Z.

Use P22 with a>=3 odd, r=2^a, K=sqrt(2r), and
Gamma=Z_4 cross GR(4,a), of cardinality4r^2. Its original symmetric
Boolean support S0 has size2r^2-4. Along t=(1,0), the unit fibers
are the two-runs {k(y),k(y)+1}; the other fibers are full or empty.
Each two-run has one top, giving m=r^2-r.

There is an important admissibility issue: the ORIGINAL y=0 fiber
is empty, so t is NOT in S0. Repair it exactly by setting

    S'=S0 union{t,-t}, N'=2r^2-2.

The changed fiber is {1,3}, which contains no adjacent pair and hence
no B_t element. All other t-fibers are unchanged. Thus the boundary
and q_t are EXACTLY unchanged; there is no estimated boundary error.
Now t belongs to S', and q0=0.

Write characters as (j,lambda) with chi(t)=i^j. On j=1,3,
the recorded P22 spectrum has r spikes K(r-1) and r^2-r values -K
in each slice. The j=2 slice of D0 is0, and the j=0 minimum is -4.
For a two-run,

    F_Bt=[i^j/(1+i^j)]*D0, j=1,3,
    (1-i^j)*i^j/(1+i^j)=1,

so q_t=D0 on these slices. On j=0, q_t=0. The support repair adds
2cos(pi*j/2) to D: it does not change odd slices, changes j=2
from0 to-2, and increases j=0 by2. Consequently the ACTUAL minimum
of D' is still -K for K>=4.

Normalized dual Haar measure has denominator4r^2. Cubing the odd
spectral values therefore gives the original energy

    H0=K^3*(r-1)*(r-2)/2.

Their contribution to ||q||^2 is K^2(r-1)/2=r(r-1)=m.
The total norm is2m, so the j=2 contribution is the remaining m.
The repaired energy is thus EXACTLY

    H'=K^3*(r-1)*(r-2)/2-2m,
    H'/(K^2*m)=K*(r-2)/(2r)-2/K^2 ->infinity.        (21)

This refutes the group version of the K^2 endpoint-energy bound
WITH admissible t, consistent with P22's stronger run-top obstruction.
It does not refute its integer version. The repair is essential:
the unmodified O4 calculation alone did not meet t in S.

Moreover the only positive energy comes from the odd-slice spikes

    D'=K(r-1),

which satisfy K^2<D'<N'-K for every r>=8. The other positive
spectrum has q=0. Thus the middle contribution in (20) is EXACTLY

    I_mid=K^3*(r-1)^3/(2r),
    I_mid/(K^2*m)=K*(r-1)^2/(2r^2) ->infinity.        (22)

The offending height is asymptotic to K^3/2. This is precisely an
intermediate spectral layer, rather than a near-identity defect left
over from an incorrect top-band estimate. It makes concrete why
localization (20) must be followed by INTEGER-specific mathematics.
The model's two-runs have length exactly half their order4 cycle;
the periodic phase relations underlying P22 do not supply the ordered
finite-run structure of Z.

Final decision for this addendum: preserve (12),(18)-(20) and the exact
centering (11); retire the integer linear-energy bound and every
group-agnostic K^2-energy/middle closure. Any retained improvement
must control the integer middle window, or replace the witness using
a derived interaction absent from these finite-torsion models. No
further group test or successful-control sweep is justified by these
calculations.

## 13. Final root-record and finite-artifact audit

Before checkpoint I read the complete parent record
`.research/notes/ordered_boundary_2026-10-23.md`, the complete
`src/ordered_boundary_verify.py`, and
`.research/experiments/ordered_boundary_2026-10-23/verification.json`.
I found no consequential gap requiring a correction to the parent note.
The centering, probability threshold, band allocation and admissibility
repair agree with the derivations above. In particular (MID) gives
m<=(C+10)K^3, hence N<=6(C+10)K^4 in the stated Shankar regime;
this is a conditional exponent1/4, not a proved new exponent.

The single finite check adds Q=65536 to the PREVIOUS saved triangular
support; it performs no new sampling or optimization. The resulting
set has n32788, maxA=t65536, m10921, coupling10921 and norm squared21842.
Its exact energy is H146387604. The direct ordered pair implementation
correctly overrides the diagonal with -2; the independent full FLINT
polynomial multiplication extracts the correlations at degree+a and
agrees exactly. Integer magnitudes are below the stated int64 bound.

The old all-circle M<=75623/180 transfers to the new support by adding
one cosine, giving M<=75803/180 and K<=75803/90. Therefore the saved
fraction

    H/(actual K*m)>=13174884360/827844563>15

has the correct bound orientation. It refutes the particular constant15
in the linear-energy proposal, while the paper family refutes every
absolute constant. The finite check does not implement the asymptotic
selection theorem or certify a vanishing Chowla ratio. The artifact
records terminal PASS and both exact energy methods. I inspected its
source and saved evidence; I did not rerun it, recompute hashes, start
a VM or perform any additional research computation.
