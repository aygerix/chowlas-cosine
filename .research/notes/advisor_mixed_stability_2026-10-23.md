# Mixed stability: a quantitative scalar-factor gap uniform under dilation

2026-10-23. Sole internal AI advisor. Independent paper derivation and
audit, read-only source review, and this assigned note only. No research
computation, VM operation, GPU, extra agent or outreach. Shared Dirichlet
is left on. This is an archimedean factor estimate, not a Chowla proof
or a certified near-square counterfamily.

## 1. Target and concrete result

The proposed strong stability target was

    lambda*||Q-Qrev||_2^2 >= c*n

for an absolute c>0, actual lambda=M(A), and real optimal factors
of Boolean spectra with n>=3. Its truth or falsity remains OPEN
in this attempt. A Bu near-square SIGNAL or a vector factor does
not by itself give a near-palindromic SCALAR polynomial factor.

There is, however, a complete quantitative factor-independent result
which survives arbitrary dilation and arbitrary complex spectral phases.
Let A be fixed, D=max(A), lambda>=M(A), and

    p(t)=lambda+sum_(a in A)cos(a*t), t complex.

Choose a disk centered at zeta with radius rho>0 such that p has
an ODD total number of zeros inside, counted with multiplicity,
and no zero on its boundary. Put

    m_rho=min_(|t-zeta|=rho)|p(t)|>0,
    Delta=4*m_rho/[3*(D+1)*exp(D*(|Im zeta|+2rho))].

For EVERY integer L>=1 and EVERY complex polynomial factor Q_L
of p(Lx) on the real circle, trim its monomial shift to degree
N=LD and define conjugate reversal

    Q_L^dagger(z)=z^N*conj(Q_L(1/conj(z))).

Then

    ||Q_L-Q_L^dagger||_2^2 >= Delta>0.             (1)

The norm is normalized circle L2, equivalently coefficient l2.
This is uniform over ALL polynomial spectral branches AND all
global phases. For real coefficients dagger is ordinary reversal.
For every Boolean A with n>=3, such a disk exists for EVERY
lambda>=M(A), by the exact square-rigidity theorem proved in the
preceding cycle. Thus a fixed Boolean support cannot evade this
positive gap simply by being dilated and choosing new root phases.

Delta depends on A,lambda and the disk data. No n-scale bound
on lambda*Delta is proved; this dependence is essential to the
current status, not an unrestricted conclusion with hidden constants.

## 2. Why exact Boolean rigidity supplies the odd zero

The monic polynomial

    P_lambda(z)=2*z^D*p(t), z=exp(it),

has the exact off-center0/1 coefficients. For n>=3 it cannot be
a real square by the coefficient-rigidity theorem. If every root
of this real monic polynomial had even multiplicity, taking half
of each multiplicity would give a monic REAL square root, since
the half-root multiset is closed under conjugation. Hence some
root has odd multiplicity.

It is nonzero because P_lambda(0)=1. It is OFF the unit circle:
on the real t axis p>=0, so every real-axis zero has even order;
the exponential substitution preserves local multiplicities.
Choose a logarithm zeta of this off-circle root. The entire
function p(t) has an odd-multiplicity zero at zeta. A sufficiently
small disk around it contains just that zero and has nonzero
boundary, giving the stated m_rho. Only the square case of the
previous power theorem is required here.

This is the actual Boolean input. The analytic estimate below
holds for any nonnegative trigonometric p with an odd complex
zero and does not falsely promote coefficient caps to Booleanity.

## 3. Entire real/imaginary parts and normalization

After removing a monomial shift, any factor has degree N=LD:
the unique extreme autocorrelation is the nonzero frequency LD.
Write Q_L(z)=sum_(k=0)^N q_k*z^k, with complex q_k permitted, and set

    B(t)=exp(-i*D*t/2)*Q_L(exp(i*t/L)),
    Bstar(t)=conj(B(conj(t))),
    R=(B+Bstar)/2, I=(B-Bstar)/(2i).

All are entire finite exponential sums. R and I are real on the
real axis, of bandwidth at most D/2. On the real axis Bstar=conj(B)
and |Q_L(exp(i*t/L))|^2=p(t). Analytic continuation therefore gives

    R(t)^2+I(t)^2=B(t)*Bstar(t)=p(t)              (2)

throughout the complex plane. This is an identity of analytic
squares, not an absolute-value equality off the real axis.

Put d_k=q_k-conj(q_(N-k)) and E=sum |d_k|^2. Then

    I(t)=(1/(2i))*sum_(k=0)^N d_k
                         *exp(i*(k/L-D/2)*t),
    E=||Q_L-Q_L^dagger||_2^2.                    (3)

The squared I norm over its real interval of length2piL is E/4.
If N is odd, R,I can be antiperiodic on that interval; their
squares and the coefficient orthogonality remain valid. No
unannounced real-coefficient or phase convention enters (2)--(3).

## 4. Exact complex sampling bound

For ANY complex t, discrete orthogonality at t+2pi*j gives

    (1/L)*sum_(j=0)^(L-1)|I(t+2pi*j)|^2
      =sum_(r modL)|sum_(k congruent r modL)
                (d_k/(2i))*exp(i*(k/L-D/2)*t)|^2.

Every residue class among0,...,LD has at most D+1 entries.
Apply Cauchy within each class and use |k/L-D/2|<=D/2:

    (1/L)*sum_j |I(t+2pi*j)|^2
       <=(D+1)*exp(D*|Im t|)*E/4.                (4)

The common phase exp(-iD*pi*j) cancels in the absolute squares.
This is why the alias count is D+1, not LD+1. The normalization
and all factors4 are explicit. There is no independent-sampling
assumption and no root-modulus continuity estimate.

## 5. Rouche parity and the Poisson constant

At each translated disk centered zeta+2pi*j, p has the same odd
zero count and the same minimum boundary modulus m_rho. If
|I|^2<|p| everywhere on its inner boundary, Rouche's theorem
would give the same odd zero count for p-I^2=R^2. An analytic
square has an even zero count. Therefore

    max_(|t-zeta-2pi*j|=rho)|I(t)|^2>=m_rho.      (5)

Equality is allowed: the contradiction excludes strict inequality
everywhere, which is sufficient for (5). The identically-zero
square case cannot defeat the argument; it would likewise make
the stated strict comparison impossible.

The function |I|^2 is subharmonic in the outer disk of radius2rho.
Its value on the inner circle is bounded by the Poisson integral
of the outer boundary values. The Poisson kernel at radius ratio
1/2 has maximum(1+1/2)/(1-1/2)=3. Hence

    max_inner |I|^2 <=3*average_outer |I|^2.

By (5), that outer average is at least m_rho/3 for EVERY j.
Average in j and interchange with the circle average. Applying
(4) at t=zeta+2rho*exp(i*theta), with
|Im t|<=|Im zeta|+2rho, gives

    m_rho/3 <=(D+1)*exp(D*(|Im zeta|+2rho))*E/4.

This is exactly(1). Zeros of p on the OUTER circle cause no
problem; only I's analyticity is used there. All operations are
on the full complex/circle domains, with no grid approximation.

## 6. All phases, fixed-family consequence, and actual missing scale

Multiplying Q_L by ANY unimodular constant keeps p fixed, so the
same bound holds for every such phase. In coefficient form,

    inf_phi ||exp(i*phi)Q_L-(exp(i*phi)Q_L)^dagger||_2^2
       =2lambda-2*|sum_k q_k*q_(N-k)| >= Delta.   (6)

There is no conjugation INSIDE the final sum. For real factors,
ordinary reversal is the original quantity under investigation.
At fixed A and actual lambda=M(A), equations(1),(6) imply

    lambda*E_L/n >= lambda*Delta/n>0

uniformly in L and all branches/phases. Thus pure dilation of a
FIXED support is not an asymptotic antisymmetry-gap counterfamily.
The theorem does not assert a positive infimum when the underlying
supports themselves vary.

The desired universal lower lambda*E>=c*n would imply Chowla,
since E<=4lambda by the triangle inequality. It has not been
proved equivalent to Chowla, nor is it proved or refuted here.
To obtain it from(1) would require a uniform n-scale lower bound
on the disk expression or on a correctly framed sum of disk costs.
Sections8--10 below now supply that exact common sampling frame
and REFUTE its proposed universal n-scale upgrade. Individual
disk costs cannot simply be summed, and optimizing the resulting
nonnegative-weight Gram certificate does not repair the loss.

## 7. Bu near-square stress test: the unproved scalar step remains

The recorded Bu identity has n=k(k-1), f=P_0^2-k/2-C/2, with an
all-circle construction upper bound of the form M<=k/2+o(k).
This is a real near-square SIGNAL and suggests testing small
antisymmetric energy. It does NOT exhibit an exact scalar
polynomial factor close in coefficient L2 to a palindromic one.
A vector/matrix factor with a small residual component cannot
be silently compressed to that scalar conclusion.

I independently inspected the primary source Ephremidze,
Shargorodsky and Spitkovsky, arXiv1603.01101v2 (27 April2016),
Theorems1--2 in the [primary text](https://arxiv.org/html/1603.01101).
Theorem1
rules out a uniform continuity modulus for OUTER scalar factors
from only normalized L1 and logarithmic-L1 perturbations. Its
moving pairs do not contradict continuity at a fixed density.
Theorem2 has an additional L-infinity multiplier on its logarithmic
error term. Neither statement settles selection among ALL polynomial
root-reflection branches. They do not prove a Bu counterfamily
or a no-go theorem for specially selected scalar factors.

Our theorem avoids those continuity assumptions entirely. The
argument below also avoids them when bounding the WHOLE weighted
odd-zero certificate class. That certificate bound is not an
upper bound on the scalar factor energy E. No growing Boolean
counterexample to lambda*E>=c*n has been established.

Status: complete independently checked paper proof; no new Lean
check, external novelty claim, experiment or universal exponent.
No extra Bu control sweep, pure-power search, denominator variant
or VM action follows. The former recommendation to optimize disk
packing is superseded by Section10. A next universal argument must
retain information lost by the positive vector majorant below.

## 8. Exact weighted-disk Gram certificate and all frequency endpoints

Fix a finite collection of odd-zero disks as in Section1, with
centers zeta_j, radii rho_j, boundary minima eta_j>0 and weights
w_j>=0, not all zero. Let

    z_j(theta)=zeta_j+2rho_j*exp(i*theta).

For an INTEGER bandwidth B>=D, put

    Omega_s={a+s-B/2: a=0,...,B-1}, 0<=s<=1,
    Omega_*={a-B/2: a=0,...,B}.

For either frequency set define the Hermitian positive Gram matrix

    G(a,b)=sum_j w_j*mean_theta
         exp(-i*omega_a*conj(z_j(theta)))
            *exp(i*omega_b*z_j(theta)),

and let Lambda_B be the maximum of ||G_*|| and sup_s||G_s||.
The FIRST factor is conjugated. Thus c^*G*c is the weighted
outer-circle mean of |sum_a c_a*exp(i*omega_a*z)|^2. Lambda_B
is finite and positive for every allowed collection.

For I_L in Section3, averaging L translates removes cross terms
between different coefficient residues moduloL. The frequencies
in a residue block differ by integers and lie in[-D/2,D/2].
After adding B/2 their common fractional part is some s in[0,1).
If s>0 their integer indices are a subset of0,...,B-1. If s=0
they can include BOTH endpoints0 and B; this is why G_* is needed.
Zero extension into the corresponding Gram matrix proves

    sum_j w_j*mean_theta mean_(ell modL)
                   |I_L(z_j(theta)+2pi*ell)|^2
           <=Lambda_B*E_L/4.

The translated Rouché/Poisson lower bound gives the converse
lower estimate sum_j w_j*eta_j/3. Therefore

    E_L >=4*sum_j w_j*eta_j/(3Lambda_B).          (7)

This is valid for ALL L, branches and phases, without disjointness
of disks, a simple-zero condition or degree padding. Define

    F_B(p)=sup_(finite odd disks, weights>=0)
                       sum_j w_j*eta_j/Lambda_B.

The supremum is positive, and at most3lambda/2 by (7) and the
phase minimum E_L<=2lambda. If at actual lambda=M(A)<=sqrt(n)
one could prove F_B(p)>=c*n/lambda, then

    lambda^2 >=(2c/3)*n.

The Chowla constant in this low-M branch would be sqrt(2c/3),
and the unrestricted constant min(1,sqrt(2c/3)). This is a
SUFFICIENT target, not an established equivalence. Section10
refutes it even if B and all the disks/weights are optimized.

## 9. A cheap vector majorant bounds the entire certificate class

Suppose p=T^2+e with T entire and real on the real axis. Suppose
also that, throughout the COMPLEX plane,

    |e(z)|<=sum_l |J_l(z)|^2,

where each J_l has frequencies on a common rational mesh within
[-B/2,B/2]. Write Emaj=sum_l||J_l||_2^2, using coefficient l2,
equivalently normalized mean over a common real period of the
absolute squares. Then

    F_B(p)<=3*Emaj.                              (8)

Indeed Rouché compared to the analytic square T^2 gives
eta_j<=sup_inner|e| on EVERY translated odd-zero disk. The sum
of |J_l|^2 is subharmonic, so its inner supremum is at most3
times its outer mean. Average over a common finite number of
2pi translates to separate fractional frequency classes. For
each J_l the Gram bound is at most Lambda_B*||J_l||_2^2.
Summing proves sum_j w_j*eta_j<=3Lambda_B*Emaj, for every
finite collection. Neither T nor J_l needs to be a scalar
spectral factor of p.

In particular, for real c,c_a and frequencies a<=D<=B, set

    e(z)=c+sum_a c_a*cos(az), W=sum_a c_a^2,
    u_+=exp(i*D*z/2), u_-=exp(-i*D*z/2),
    F_+=sum_a c_a*exp(i*(a-D/2)*z),
    F_-=sum_a c_a*exp(-i*(a-D/2)*z).

Since the cosine sum is (u_+F_++u_-F_-)/2, Young's inequality
with a parameter t>0 gives the pointwise COMPLEX-plane bound

    |e(z)|<=|c|+(|F_+|^2+|F_-|^2)/(4t)
                      +t*(|u_+|^2+|u_-|^2)/4.

All five square-root majorant functions are within bandD/2.
Their total coefficient energy is

    |c|+W/(2t)+t/2,

minimized at t=sqrt(W) when W>0, with minimum |c|+sqrt(W).
When W=0 use only the constant. Consequently

    F_B(p)<=3*(|c|+sqrt(W))                     (9)

whenever p=T^2+e has this error and B>=D. This is an UPPER
bound on a lower-certificate functional. It does not give an
upper bound on any actual scalar factor's anti-energy.

## 10. Actual-bandwidth Bu family refutes the universal upgrade

I checked the required identity/cardinality, construction span
and upper bound in [Bu et al., v1, Proposition2.1, Theorem1.2,
Sections3 and5](https://arxiv.org/html/2610.17160v1). Take its
Sidon sets S_k of size k and spanO(k^2). Put b_j=|3s_j+1/2|,
ordered b_1<...<b_k. These are distinct positive half-integers.
The genuine support has n=k(k-1), and

    f_A=T^2-k/2-C/2,
    T=sum_j cos(b_j*z), C=sum_j cos(2b_j*z).

Write h=b_k, g=b_(k-1). Its ACTUAL degree is D=h+g: the
pair sum of the largest two is present, and dominates every
pair sum or difference. A majorant using band2h/2 alone would
leave a bandwidth loophole. Remove the largest term instead:

    T0=sum_(j<k)cos(b_j*z), bandwidth g<D/2.

For actual lambda=M(A), delta=lambda-k/2, direct expansion gives

    p=T0^2+e0,
    e0=delta+1/2
       +sum_(j<k)[cos((h+b_j)*z)+cos((h-b_j)*z)]
       -(1/2)*sum_(j<k)cos(2b_j*z).             (10)

Every error frequency is at most D. The 2(k-1) positive cross
frequencies are distinct: sums exceed h, differences are below h,
and each group is strictly ordered. The k-1 diagonal frequencies
are distinct. Any cross/diagonal collision has opposite signs,
so merging coefficients reduces their total squared sum. Thus

    W<=2(k-1)+(k-1)/4=9(k-1)/4.

Equations(9)--(10) prove, for EVERY integer B>=D,

    F_B(p)<=3*(|delta+1/2|+(3/2)*sqrt(k-1)).      (11)

No frequency was added and no scalar-factor closeness was
assumed. The actual lower bound comes from the independently
reviewed [P16' theorem](../PROOFS.md): for Sidon span L,
M>=k/2-O(k*(L/k^3)^(1/5)). Its recorded Gallagher form has a
kernel-checked theorem with hypothesis eta^5*k^3>=4200*L;
this cycle did not rerun Lean or extend that formalization.
With L=O(k^2), combine this with the cited upper bound to get

    lambda=k/2+O(k^(4/5)), lambda~k/2,
    sup_(integer B>=D) F_B(p)=O(k^(4/5))=o(n/lambda).

These are ACTUAL-lowM Boolean supports eventually, since
M/sqrt(n)->1/2. Thus the universal target F_B>=c*n/lambda
fails for every absolute c>0, even with arbitrary finite
nonnegative disk weights and arbitrarily many disks, with the
exact Gram norm and with bandwidth optimized over all B>=D.

This is a theorem about the WHOLE DEFINED CERTIFICATE CLASS.
It does not falsify lambda*E>=c*n for the actual scalar factors,
does not settle all methods using complex zeros, and gives no
family with M/sqrt(n)->0. The cheap vector majorant can make
this lower bound weak while the actual scalar phase remains
expensive. No uniform scalar-factor continuity theorem is used.

## 11. Final parent audit and one retained next derivation

I read the parent's complete
[odd-zero stability proof](odd_zero_phase_stability_2026-10-23.md).
Its conjugate-first Gram convention, endpoint matrix, factors4
and3, Young coefficients1/4, actual-bandwidth T0 error, and P16'
span dependency agree with the independent derivation here. No
substantive mathematical gap was found. The implied constant
2c/3 is the constant in the SQUARED lower bound for lambda;
the root bound uses its square root. The parent writes that
squared inequality correctly.

Stop optimizing this odd-zero/positive-majorant Gram architecture
as a proposed universal n-scale proof. Retain (1), (6) and (7)
as valid fixed-symbol tools. The precise information discarded
by (8) is the actual scalar coupling; recovering it is a changed
mathematical requirement, not a larger disk search.

One concrete retained proof attempt is the existing full nonlinear
P2 determinant, with its Boolean recurrence residual kept signed.
At actual M<=sqrt(n), let F=sum_A z^a, lambda=2sqrt(n),
p=(lambda+F)^(-1), t=<F,F^2>, C1=<F,p>, C2=<F^2,p>,
H0=<2Re(F)*(Im p)^2>. The already proved recurrence is

    lambda*C2=-t/lambda-(2n-1)*C1-R_A(p),
    R_A(p)=sum_(a,b,c in A; c!=a,b; a+b>c) p_(a+b-c).

For t>0 the next existing quantitative target is to prove or
give an actual-lowM Boolean counterexample to

    [t/lambda+(2n-1)*C1+R_A(p)]^2
                        >=2*t*lambda^2*H0.       (12)

This is exactly C2^2>=2tH0, not a new estimate or an established
unrestricted equivalence. An argument would need a JOINT bound
on this finite signed coefficient pairing and the full inverse
norm inside H0. R_A has both signs even on actual-lowM supports;
discarding it, prescribing its sign, or replacing p with a fixed
number of polynomial powers is already invalid. The two-plane
completeness is not assumed: unrestricted signed Rayleigh and
the independent all-circle construction track remain alternatives.
Equation(12) is a concrete next derivation in a retained route,
not a promise of a proof or a reason for another control sweep.

Final status: independently checked paper theorems and an infinite
Boolean falsifier of a universal certificate principle; no new
computation, experiment, Lean proof, VM operation, GPU spend,
agent, external review or outreach. Full Chowla remains OPEN.
