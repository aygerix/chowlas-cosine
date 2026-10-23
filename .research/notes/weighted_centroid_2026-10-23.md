# A weighted centroid inequality for one positive square factor

2026-10-23. Paper proof, independently checked in
[the advisor audit](advisor_weighted_centroid_2026-10-23.md).
This extends the multiplicity centroid mechanism to arbitrary positive
factor weights. No external novelty or kernel-check claim. It is a
certificate restriction; arbitrary Chowla supports need not have a
positive-coefficient factor at their optimal floor.

## Statement

Let A be a nonempty finite set of distinct positive integers, n=|A|.
Suppose, for all real x,

    lambda+f_A(x)=|Q(e^ix)|²,
    Q(z)=sum_(b in B)q_b*z^b, q_b>0 real,

where B is finite in an integer-frequency coset. Put k=|B|,
S=sum q_b, qmax=max q_b. Then lambda=sum q_b², S²=lambda+n, and

    lambda-1/2 >= S/(4qmax),                       (1)
    n <=16lambda*(lambda-1/2)²-lambda.             (2)

In particular lambda>1/2 and lambda>=(n/16)^(1/3). If
L=qmax/qmin, then

    k<=4L*(lambda-1/2),
    n<=[4L*(lambda-1/2)-1]*lambda,
    lambda>=sqrt(n)/(2sqrt L).                     (3)

Old P8 plus the extreme-lag product also gives
lambda>=sqrt(n)/(sqrt(2)*L); it is stronger when1<=L<2. The
centroid dependence in (3) is stronger for L>2. Do not present all
bounded-ratio conclusions as newly unavailable from P8.

These lower bounds concern lambda. They apply to M(A) only when such
a factor exists at lambda=M(A). General Fejer--Riesz factors can
have signs or phases. Multiple positive factors are also outside
this single-factor theorem. No unrestricted exponent improved.

## Exact proof

Let R(d)=sum_b q_b*q_(b+d), extending q by zero. Coefficient
matching gives R(d)=1/2 on A, zero on all other positive lags.
Since the weights are positive, A is exactly diff_+(B). Thus the
row Gram G_(b,c)=R(c-b) has diagonal lambda and every off-diagonal
entry1/2. In particular lambda>1/2 follows in the argument below.

Define the q-weighted centroid

    mu=(sum b*q_b)/S, x_b=(b-mu)*q_b,
    U_d=sum_b x_b*q_(b+d).

One has sum_b x_b=0 and

    sum_(all signed d)U_d²
      =x^T G x=(lambda-1/2)*sum q_b²*(b-mu)².      (4)

Here U_0 is generally NOT zero; the centroid used q rather than
q². It stays in (4) and can be discarded only as a nonnegative
square in the next lower bound.

For d>0, translating endpoints gives U_(-d)=U_d+d*R(d), hence

    sum_d U_d² >=(1/2)*sum_(d>0)R(d)²*d²
               =(1/4)*sum_(d>0)R(d)*d²
               =(S/4)*sum q_b*(b-mu)².             (5)

The last equality is the weighted pair-variance identity. The
variance is positive since n>0 forces k>=2. Bound
sum q_b²*(b-mu)²<=qmax*sum q_b*(b-mu)² in (4), compare (5),
and cancel the positive variance. This proves (1). Since
qmax<=sqrt(lambda) and S²=lambda+n, squaring proves (2).

If all weights have ratio at most L, S/qmax>=k/L. Equation (1)
gives k<=4L*(lambda-1/2). Cauchy S²<=k*lambda gives
n<= (k-1)*lambda and then (3).

## What optimality might add, and what it has not added

From each pair product q_b*q_c<=R(|b-c|)=1/2, at most one weight
exceeds1/sqrt2. The extreme pair has product exactly1/2, so if a
larger weight exists, it must be at one endpoint of B. All other
weights are at most1/(2qmax).

These facts do not yet bound an optimal qmax. Arbitrary certificates
have unbounded qmax even on A={1,2}: take support{0,1,2} with
weights t, 1/[2(t+1/(2t))], 1/(2t). Their two correlations are1/2.
Their lambda is minimized at9/8; taking t large gives nonoptimal
certificates with unbounded qmax. At an optimal factor a unit-circle
zero forces only k-1>=2qmax² by the triangle inequality. That still
permits growth. No positive-coefficient assertion for interval
spectral factors has been proved or used.

An absolute optimal-factor qmax bound would turn (1) into a root
bound for this class. The next derivation should test that statement
or extend (4)--(5) to factors with signed/complex coefficients while
quantifying the phase-cancellation terms. It must not assume that
all Boolean supports have positive factors, or identify a lower
certificate-energy bound with a lower bound on actual M(A).
