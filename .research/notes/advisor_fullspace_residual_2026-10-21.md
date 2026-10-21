# Advisor audit: certified full-space leverage from exterior residuals

2026-10-21. Internal advisor, GPT-6.1 Sol/MAX. Both proposed lemmas
are valid, with the normalizations and qualifications below. I read
src/cstar_inverse_residual.py but launched no jobs, provisioning,
spending, or additional agents. Only this note was edited.

This is a positive full-space approximation/certification theorem.
It does not prove an unrestricted Boolean leverage lower bound,
L25, OP140, or Chowla. The arguments also apply to non-Boolean
real trigonometric polynomials.

All integrals use dx/(2*pi). Let D=2sum_{a in A}cos(ax),
X=max(A), and choose real lambda such that

    w=D+lambda>=delta>0  on the ENTIRE circle.

Necessarily lambda=integral w>0. A finite matrix positivity check
alone does not establish the required global delta.

## 1. Full mean-zero variational problem and exact optimizer

Let H0 be the real mean-zero subspace of L2, and define

    J_inf=sup_{q in H0}[2 integral Dq-integral wq^2],
    I=integral 1/w.

The compressed multiplication operator

    A0=P0 M_w restricted to H0

is bounded, selfadjoint, and at least delta times the identity.
The unique optimizer is

    q_star=1-1/(I*w),
    J_inf=lambda-1/I.                              (1)

Indeed q_star has mean zero and
D-w*q_star=1/I-lambda is constant, so the first variation vanishes
on H0. Direct integration gives integral w*q_star^2=lambda-1/I.
Coercivity makes the critical point the unique maximum.

Although H0 includes odd functions, D and w are even. Splitting
q into even and odd parts makes the odd contribution exactly
-integral w*q_odd^2. Thus finite cosine approximations do not
omit an odd coupling component of this particular supremum.
This observation does not discard independent odd negative-Rayleigh
routes to Chowla.

## 2. Full exterior-residual sandwich: valid

For ANY finite cosine polynomial q=sum_{j=1}^B v_j cos(jx), set

    E=2 integral Dq-integral wq^2,
    r=P0(D-wq).

Then r has degree at most B+X and

    E<=J_inf<=E+||r||_2^2/delta.                    (2)

Proof. Put e=q_star-q. Completing the square and using the
constant first variation gives

    J_inf-E=integral w*e^2,
    r=A0 e,
    J_inf-E=<r,A0^(-1)r>.

Since A0>=delta I, (2) follows. The exact residual correction is
also

    J_inf-E=integral r^2/w-(integral r/w)^2/I.        (3)

For (3), solve A0 e=r as
e=[r-(integral r/w)/I]/w and use mean e=0.
No quadrature implementation is required for the simpler bound (2).

The coefficient norm in (2) MUST contain every nonconstant residual
coefficient through B+X. If r=sum rho_j cos(jx), then

    ||r||_2^2=(1/2)sum_{j=1}^{B+X}rho_j^2.

Using only j<=B instead certifies the restricted finite-band
supremum J_B. A finite optimizer can have zero interior residual
and nonzero exterior residual, so the distinction is substantive.

## 3. Normalization against the existing matrix code

Write c_j=1_A(j), extended by zero, and

    C_jk=[1_A(|j-k|)+1_A(j+k)]/2,
    Z_B=C_B+(lambda/2)I.

Then E=2c^T v-v^T Z_B v. Define the extended matrix residual

    d_j=c_j-(C v)_j-(lambda/2)v_j,  1<=j<=B+X,

where v_j=0 for j>B and C v includes its exterior action.
The physical cosine residual is rho_j=2d_j, so

    ||r||_2^2=2sum_{j=1}^{B+X}d_j^2,
    J_inf<=E+(2/delta)sum_j d_j^2.                 (4)

At lambda=4sqrt(n), delta=2sqrt(n), formula (4) is
E+sum_j d_j^2/sqrt(n), exactly the existing code's form once the
residual sum is extended. Its variable r2 is a MATRIX residual
norm, not the physical L2 residual norm.

For integer numerator vector t and denominator s, the existing
polynomial product returns M_j=(2C t)_j. It can return ALL
j=1,...,B+X from the SAME product. Set

    R_j=2s*c_j-M_j,
    d_j=[R_j/2-2sqrt(n)*t_j]/s.

Thus the current aggregate formula

    sum d_j^2=[sum R_j^2/4-2sqrt(n)sum R_j*t_j
                         +4n sum t_j^2]/s^2

remains valid. Only sum R_j^2 needs its new nonzero tail; t is
zero-padded. Cost t^T M, sum R_j*t_j, and sum t_j^2 still use
the original numerator support. The independent packed-product
check should decode the exterior coefficients as well.

Earlier finite-band lower bounds remain valid lower bounds for
J_inf. Earlier finite-band upper bounds are not automatically
full-space upper bounds. No change to those records' mathematical
scope should be inferred without the exterior calculation.

## 4. Toeplitz boundary estimate: valid

Let L_w be multiplication by w expressed as the bi-infinite Laurent
matrix on ell2(Z). For any interval Lambda of N consecutive integer
indices, let T_N be its compression. The infinite inverse is the
Laurent matrix with symbol 1/w, so

    trace(P_Lambda L_w^(-1) P_Lambda)=N*I.

Block the Laurent matrix into Lambda and its complement:

    L_w=[[A,B],[B*,C]],   A=T_N.

Both L_w and C are at least delta times identity. The inverse
compression is (A-B C^(-1)B*)^(-1). Therefore

    R=P_Lambda L_w^(-1)P_Lambda-T_N^(-1)

is positive semidefinite. Only the first X and last X rows can
couple to exterior indices, so rank B<=2X, including N<2X.
The resolvent identity gives rank R<=rank B. Moreover
0<=R<=P_Lambda L_w^(-1)P_Lambda<=delta^(-1)I. Hence

    0<=N*I-trace(T_N^(-1))<=2X/delta.              (5)

This proves exactly the proposed trace lower bound. It is an
elementary finite-rank boundary argument, with no Toeplitz limit
theorem being silently invoked.

Define

    I_B=(T_{[-B,B]}(w)^(-1))_(0,0),  B>=0.

Compression monotonicity gives I_B<=I. For N=B+1, translate any
diagonal index i of T_N to zero. Its relative index interval is
[-i,B-i], contained in [-B,B]. The variational characterization
of an inverse diagonal then yields

    (T_N^(-1))_(i,i)<=I_B,
    trace(T_N^(-1))<=(B+1)I_B.

Combining this with (5) gives

    0<=I-I_B<=2X/[(B+1)delta].                      (6)

The use of N=B+1 is deliberate. An arbitrary diagonal index in
an interval of length 2B+1 need not have its relative interval
inside [-B,B], so replacing the denominator B+1 by 2B+1 would
require an additional argument.

## 5. Conversion to leverage and constants

Let J_B denote the supremum over real mean-zero cosine polynomials
of degree at most B. A Schur complement at the constant Fourier
index gives

    I_B=1/(lambda-J_B),
    J_B=lambda-1/I_B.

The odd Fourier block decouples from the constant, so this identity
matches the stated cosine problem, with the same normalization as
Section3. In particular I_B>=1/lambda; Jensen also gives
I>=1/lambda. From (6),

    0<=J_inf-J_B
      =(I-I_B)/(I*I_B)
      <=2X*lambda^2/[(B+1)delta].                   (7)

For lambda=4sqrt(n) and a separately established K<=2sqrt(n),
w>=2sqrt(n). Taking delta=2sqrt(n) proves

    0<=J_inf-J_B<=16X*sqrt(n)/(B+1).                (8)

This is an approximation-rate theorem, not a frequency-independent
lower bound for J_inf or J_B. In particular the coarse error at
B=2X is much larger than the OP140 target; a small computed full
residual can be far more useful than (8). None of these arguments
uses Booleanity to establish the missing uniform leverage estimate.

## 6. Analytic control that detects a missing exterior residual

For A={1}, D=2cos(x), lambda=4, delta=2 and B=2,

    J_B=8/15,
    q=(8/15)cos(x)-(2/15)cos(2x).

At this exact finite optimizer, EVERY interior residual vanishes.
However,

    r=(2/15)cos(3x),
    ||r||_2^2=2/225,
    E=8/15,
    E+||r||_2^2/delta=121/225.

The analytic full-space value is

    I=1/(2sqrt(3)),
    J_inf=4-2sqrt(3),
    8/15<4-2sqrt(3)<121/225.

Thus 8/15 must remain the FINITE-band control, not the expected
full-space answer. This hand computation checks the tail, the
factor2 convention, and the claimed meaning of the new bound.

**Verdict.** Approve the exterior-residual extension and the stated
Toeplitz rate, provided delta is certified globally, all residual
coefficients are included, and finite versus full leverage are
named explicitly. This supplies a concrete unrestricted-space
certificate, not a universal Boolean theorem. Exact finite checks
are still required of the implementation; none was run by the
advisor. No Lean/kernel check or external scrutiny is claimed.
