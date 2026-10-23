# Joint boundaries, ordered endpoints, and the remaining middle band

2026-10-23. Research checkpoint after a33f2bd. Full Chowla remains
unresolved. Paper derivations and one exact finite verification; no
novelty, external review or Lean/kernel claim. The sole internal advisor
independently checked the consequential formulas. Its complete
[paper review](advisor_joint_boundary_2026-10-23.md) supplies the character
sums, explicit probabilistic constants and elementary pattern checks.

## Conventions and targets

Let A be a finite nonempty set of distinct positive integers,
S=A union(-A), N=|S|=2|A|, D(x)=sum_(s in S)exp(isx)=2f_A(x),
and actual K=-min_circle D=2M(A). All circle integrals use dx/(2pi).
For t in S set

    A_t=S intersect(S+t),
    B_t={s in S:s-t in S,s+t not in S}, m_t=|B_t|.

The raw exact-B target

    sum_(t in S)||F_Bt||_1^2 <= C(NK+K^4)                 (JB)

would give exponent1/4 by the recorded P14/Bedert-Shankar chain.
It is distinct from the historical chosen-Q1 decomposition target.
There is no proof of (JB) in Z. Its finite-group analogue is false,
including the requirement t in S: in the elliptic-quadric complement
S={Q!=0} in F_p^4, K=p, N=p(p-1)(p^2+1), and EVERY admissible
t has p/3<=||F_Bt||_1<=4p-1 for p>=11. Thus the ratio in (JB)
is at least p/11. The advisor's Sections2-5 give exact transforms
on all nonzero null characters; the lead independently checked the
Gaussian sign, translated sections, count and ratio. This refutes a
group-independent proof, not (JB) for integer frequencies.

## The endpoint pivot and the necessary centering

For t>0, B_t consists of tops of finite t-runs of length at least2.
The exact order identity is

    sum_(b in B_t)b=(t/2)|A_t|.

Also B_t and B_t+t are disjoint, and B_t and B_t+2t are disjoint.
The order identity does NOT give a norm or energy estimate on its own.
Define the complex signed witness

    q_t=(1-exp(itx))F_Bt,
    H_t=integral D|q_t|^2.

Its coupling is real, integral D*conj(q_t)=m_t, and ||q_t||_2^2=2m_t.
But its constant coefficient is -epsilon_t, where
epsilon_t=1_(-t in B_t). Set r_t=q_t+epsilon_t to center it. Exactly,

    integral D*conj(r_t)=m_t,
    ||r_t||_2^2=2m_t-epsilon_t,
    integral D|r_t|^2=H_t+2epsilon_t*m_t.

The nonnegative measure D+K therefore gives

    m_t^2 <= K[H_t+2epsilon_t*m_t+K(2m_t-epsilon_t)].   (1)

The uncentered coupling with that measure is m_t-K*epsilon_t;
omitting this constant term would be an error. At t=max A,
epsilon_t=0. K>=1 follows by bounding a nonzero Fourier coefficient
1 of the nonnegative polynomial D+K by its mean K.

Writing a_d=1_S(d), a_0=0, exact orthogonality gives

    H_t=sum_(b,c in B_t)[2a_(b-c)-a_(b-c+t)-a_(b-c-t)]. (2)

A universal H_t<=C K m_t would imply m_t<=O(K^2), hence exponent1/3
with the integer boundary averaging. A universal H_t<=C K^2 m_t
would imply m_t<=O(K^3), hence exponent1/4. These are different
claims. The first is refuted below, while the second remains open
in Z and cannot hold in arbitrary finite groups.

## Genuine integer obstruction to the linear-K energy scale

The following theorem is proved on paper, not inferred from the pilot.
For every integer Q>=2^21 there exists A_Q subset{1,...,Q} containing
Q such that, for t=Q, its actual global K satisfies

    H_t>=Q^2/80,
    K<=4+sqrt(2Q log(128Q^2)),
    m_t<=Q.

In particular H_t/(K m_t) tends to infinity along these choices.
Thus no absolute C makes H_t<=C K m_t true for all integer sets,
even with t the largest positive frequency and q_t mean zero.

Proof mechanism: independently select j<Q with probability1-j/Q,
then include Q. Put Y_s=X_s X_(Q-s). The boundary is Y_s=1 in
1<=s<Q. Formula(2) becomes

    H=-2sum_sY_s+sum_(s!=u)Y_sY_u[2X_|s-u|-X_(Q-|s-u|)].

Outside at most30Q index-collision pairs, its expected summand is
v(s/Q)v(u/Q)(2-3|s-u|/Q), v(r)=r(1-r). Its double integral is

    2(1/6)^2-3/140=43/1260.

A conservative Riemann/collision bound gives EH>=(43/1260)Q^2-100Q.
Changing one bit costs at most16Q in H. The bounded-difference tail
therefore makes H>=Q^2/80 fail with probability<1/4 for Q>=2^21.
Meanwhile ED=Fejer_Q-1+2cos(Qx)>=-3. Hoeffding on16Q^2 grid points
and the deterministic derivative bound Q(Q-1) give the stated
ENTIRE-circle K upper with failure probability<=1/4. The two good
events intersect. See advisor Section9 for every constant and the
collision argument. This square-root-log upper bound is not a
vanishing normalized Chowla ratio or an Epoch construction.

One fixed finite corroboration reuses the PREVIOUS pilot; there was no
fresh sampling or optimization. Append Q=65536 to its n32787 set.
The new genuine set has n32788 and max A=t=65536. Exactly,

    m_t=10921, coupling=10921, ||q_t||^2=21842,
    H_t=146387604.

The old all-circle certificate M<=75623/180 transfers by adding one
cosine to M<=75803/180, hence K<=75803/90. Consequently

    H_t/(actual K*m_t) >=13174884360/827844563 >15.

[Verification data](../experiments/ordered_boundary_2026-10-23/verification.json)
records source hashes, the derived-set hash and exact values. Two
different identities agree: direct integer boundary-pair kernels and
the full polynomial's exact FLINT integer autocorrelation. The global
bound is inherited from the previously independently checked certificate,
not a newly evaluated minimum. Reproduce on shared Dirichlet:

    src/dirun.sh -c 2 -m 4 -t 120 python src/ordered_boundary_verify.py

No asymptotic selection algorithm is implemented by this finite check.

## New cancellation lemma: only an intermediate band remains

This lemma holds on the integer circle and on finite dual groups.
It is a useful localization, not an integer-only gain.

B_t-t and B_t are disjoint subsets of S with equal cardinality m_t.
Their difference polynomial satisfies

    q_t=exp(itx)[F_(B_t-t)-F_Bt].

Subtract1 from every character in the two equal-size sums. Cauchy-
Schwarz and sum_(s in S)|exp(isx)-1|^2=2(N-D(x)) prove

    |q_t(x)|^2 <=4m_t(N-D(x)).                         (3)

Since integral D_+=integral D_-<=K, for tau,Delta>0 the low positive
band D<=tau contributes at most2tau*m_t to H_t, and the high band
D>=N-Delta contributes at most4m_t*Delta*K. Discarding negative
energy and assigning the low band first when the bands overlap gives

    H_t<=2tau*m_t+4Delta*K*m_t
             +integral_(tau<D<N-Delta)D|q_t|^2.        (4)

In particular

    H_t<=6K^2*m_t+J_t,
    J_t=integral_(K^2<D<N-K)D|q_t|^2.                 (5)

Thus near-maximum spikes cost only O(K^2*m_t); they are quantitatively
suppressed by equal-size endpoint cancellation. Small positive values
cost the same. The missing candidate estimate is now explicitly

    J_t<=C K^2*m_t for ALL finite integer S and t in S. (MID)

(MID) is UNPROVED. Equations(1),(5) show that it would give
m_t<=(C+10)K^3, with no missing constant-term correction. Combining
with the recorded Shankar sum_(t in S)m_t>=N^2/(6K) when N>=2K^2
would give N<=6(C+10)K^4. The complementary regime already has a
square-root bound, so a proof of (MID) would improve the universal
exponent to1/4. This is a conditional implication only.

## P22 already obstructs a group proof, including after admissibility repair

Do not revive the historical P20 group cubic window: P22/O4 closed it.
The following exact diagnostic uses that EXISTING Galois-ring family;
it is not a new construction or a novelty claim for the relative
difference set. Let r=2^a with odd a>=3. Original O4 has

    Gamma=Z_4 x GR(4,a), |Gamma|=4r^2,
    N=2r^2-4, K=sqrt(2r), m_(1,0)=r(r-1).

The original t=(1,0) is OUTSIDE S. Repair this explicitly by adding
{t,-t}. The empty y=0 fiber becomes{1,3}, which creates no adjacent
pair, so B_t and q_t remain EXACTLY unchanged. On character slices
j=1,3, D is unchanged and q_t=D. On j=0, q_t=0 and D increases2;
on j=2, old D=0 and new D=-2. The actual minimum remains -K.
The repaired support has N'=2r^2-2 and t in S'.

Each odd-j slice has r characters of value K(r-1), with all other
r^2-r values -K. Exact spectral summation yields

    H_original=K^3(r-1)(r-2)/2,
    integral_(j odd)|q_t|^2=m_t,
    H_repaired=K^3(r-1)(r-2)/2-2m_t,
    H_repaired/(K^2*m_t)=K(r-2)/(2r)-2/K^2 ->infinity.

All large positive energy occurs at the intermediate height
D=K(r-1) of order K^3, strictly between K^2 and N'-K for r>=8.
Other positive nonidentity values are at most K^2-2; the identity
spike is killed exactly by q_t=0. Therefore the repaired family
refutes the GROUP version of (MID), with an admissible t, and locates
its obstruction in the surviving band. It does not transfer to Z.
See the advisor's final addendum for its independent audit.

## Global review and operational next step

Two different optimistic gains have now been tested and failed:
raw joint L1 averaging by group-independent algebra, and a linear-K
endpoint-energy bound even on actual integers. Stop both. Neither
more successful bounded-ratio controls nor changing NK+K^4 to an
unsupported NK+K^6 estimate distinguishes the missing mechanism.

Retain(3)-(5) as the actual new reduction. Integer order must control
the INTERMEDIATE spectral band, not merely the highest peak. All
known bounded-ratio integer controls satisfy H_t<=2N*m_t trivially;
an unbounded integer violation of H_t<=C K^2*m_t would itself force
N/K^2 unbounded and hence supply a Chowla counterfamily. Do not
spend computation trying to falsify it by larger familiar controls.

First next derivation: retain full finite t-run polynomials in(2),
and attempt summation by parts with the middle-band multiplier in(5)
before taking absolute values. Isolate the resulting signed endpoint
and multiplier-difference term. A useful bound must be O(K^2*m_t)
and must fail for the O4 period4 wrap; merely restating torsion-free
support or renaming (MID) is not a proof. If that calculation produces
only an uncontrolled multiplier derivative, pivot away from this
boundary compression rather than run another calibration scan.

Keep the unrestricted signed Boolean coupling, signed/mixed scalar
factor selection and genuine growing-construction track distinct.
All own jobs terminal/PASS; the check and tightened-assertion rerun
each took<1second of compute on the same fixed input on Dirichlet.
No GPU or VM lifecycle actions. Shared Dirichlet
remains on; cumulative conservative RunPod spend remains$0.10.
