# Advisor checkpoint: Boolean projection and the negative part

2026-10-21. This mathematical attempt was interrupted by the user's
goal-setting request. No jobs, spending, provisioning, or additional
agents. Only this assigned note was edited. The existing goal remains
active; this checkpoint does not change its status.

I read P31, P61, P63, P66, the current ROUTES ledger, and the early
NOTEBOOK idempotent-density discussion before choosing the calculation.
The basic positive/negative-part convolution reformulation is already
recorded in NOTEBOOK 2026-10-18, session2: its popular-sum mechanism
hits a K^2 threshold. Fixed-order anchored convolution tests encounter
P63's DC barrier; the cubic profile improvement in P66 pays m^3/X,
which does not reach the desired square-root regime. These facts do
not refute all uses of the exact Boolean projection identity.

All circle integrals below are normalized. Let S=+/-A, m=|S|=2n,
D=sum_{s in S}exp(isx), N=D_- and P=D_+. Let mu=integral N,
v=integral N^2, and b_h=hat N(h). The functions are real and even.
Let Pi be the orthogonal Fourier projection onto S. Its convolution
kernel is exactly D, because the coefficients are zero or one.

## Exact negative-part identities

    sum_{h in S}b_h=integral DN=-v,
    sum_h b_h^2=v,
    Pi N=D*N=P*N-N*N.

Since P*N>=0 and N*N(x)<=N*N(0)=v, the projection Pi N attains
its global minimum -v at x=0. This identity alone does not yield
macroscopic coupling: the natural witness -Pi N has coupling v,
which can be much smaller than n unless a new estimate is proved.

## A positive operator calculation, with its limitation

Write r_S(h)=|S intersect(S+h)| and w_S(h)=m-r_S(h). For
multiplication M_N by N, its leakage from the Boolean Fourier space is

    B_N=||(I-Pi)M_N Pi||_HS^2
       =sum_h |b_h|^2 w_S(h).                         (1)

This is exact on the full circle, with no frequency cutoff. One has

    0<=B_N<=sum_{h in S}w_S(h).                       (2)

Proof. The finite compressions Pi M_P Pi and Pi M_N Pi are positive
semidefinite, so the trace of their product is nonnegative. Expanding
in the Fourier basis and using hat P=1_S+b gives

    0<=sum_h r_S(h)(b_h^2+1_S(h)b_h)
      =-B_N-sum_{h in S}w_S(h)b_h.

Weighted Cauchy--Schwarz bounds the final negative sum by

    [sum_{h in S}w_S(h)]^(1/2)
      [sum_{h in S}w_S(h)b_h^2]^(1/2)
    <=[sum_{h in S}w_S(h)]^(1/2)*sqrt(B_N),

proving (2), including the B_N=0 case.

This is consistent with Hilbert--Schmidt contraction of a negative-
part functional calculus. It is not a new Chowla-scale estimate.
Indeed for general real coefficients d_h supported on S, the same
argument yields B_N<=sum_h w_S(h)|d_h|^2. Booleanity turns the
right side into a combinatorial count, but the calculation by itself
does not rule out weighted Fejer escapes or force mu~sqrt(n).

## Exact remaining gap and resumable decision

No arbitrary-support lower bound on mu, negative energy v, or OP140
leverage was established. Equation (1) identifies a possible place
for torsion-free additive boundary information, but no bound linking
that leakage to the required n scale was derived. A next use must
provide such a link; merely renaming (1) as Boolean leakage would
repeat the existing C* gap.

The immediate strategic request superseded further derivation. My
advice was to keep the already active `/goal Pursue the goal outlined
in GOAL.md`, refresh its completed first milestone, explicitly retire
the refuted bounded-mean reference architectures, and carry forward
the cumulative GPU budget rather than reset it. L25 and OP140 remain
conjectural sufficient targets. The full unrestricted proof-or-
counterfamily objective, arbitrary signed witnesses, direct negative-
Rayleigh alternatives, and independent all-circle construction track
remain intact. No mathematical work is promised outside an active
orchestrated continuation.

Status: displayed paper identities only; no new universal inequality,
Lean/kernel-checked theorem, external review, or numerical experiment.
