# Odd zeros force phase energy, but their sampling certificates are not universal

2026-10-23. Research derivation, not a manuscript. The previous
turn2b7b13f was progress. Full Chowla remains unresolved. Paper
proofs independently checked by the sole internal advisor in
[the mixed-stability audit](advisor_mixed_stability_2026-10-23.md).
No kernel verification or external novelty claim. No computation,
GPU deployment or VM lifecycle operation was needed this cycle.

## 1. A gap uniform in dilation and all complex factor branches

Let A be any Boolean set with n>=3, D=maxA, lambda>=M(A), and

    p(t)=lambda+sum_A cos(at).

This is an entire function of the COMPLEX variable t. Choose a
disk B(zeta,rho) containing an ODD total multiplicity of zeros,
with no boundary zero, and set

    eta=min_(|t-zeta|=rho)|p(t)|>0.

Such a disk exists: exact Boolean power rigidity says
P_lambda(w)=2w^D*p(t), w=exp(it), is not a square when n>=3.
It has an odd-multiplicity root. Its unit-circle roots have even
multiplicity because p is nonnegative on the real circle, so an
odd root is off the unit circle. A local logarithm supplies zeta
off the real axis, and a small disk isolates its odd multiplicity.

For ANY positive integer L, let Q_L be ANY complex polynomial
spectral factor

    |Q_L(exp(ix))|^2=p(Lx).

Trim a monomial shift so its coefficient width is N=LD, and
let q_0,...,q_N be its coefficients. Define conjugate reversal
Q_L^dagger by coefficients conjugate(q_(N-k)), and put

    E_L=sum_(k=0)^N |q_k-conjugate(q_(N-k))|^2.

Then, for EVERY branch and EVERY global phase,

    E_L >= 4eta/[3(D+1)exp(D(|Im zeta|+2rho))] >0.       (1)

Thus dilating one fixed support cannot drive its factor's
conjugate-reversal asymmetry to zero. The constant depends on
A and lambda through the zero/disk data. It is not a universal
n-scale lower bound.

One may first divide A by its gcd and absorb that gcd into L.
This avoids weakening the displayed constant by an artificial
frequency dilation.

## 2. Entire real and imaginary parts and exact sampling

Define B_L(t)=exp(-iDt/2)*Q_L(exp(it/L)) and
B_L^star(t)=conjugate(B_L(conjugate(t))). The entire functions

    R_L=(B_L+B_L^star)/2,
    I_L=(B_L-B_L^star)/(2i)

are real on the real axis. Analytic continuation of the factor
identity gives R_L^2+I_L^2=p on the WHOLE complex plane. If
d_k=q_k-conjugate(q_(N-k)), then

    I_L(t)=(1/(2i))*sum_k d_k*exp(i(k/L-D/2)t).           (2)

The normalized mean of I_L^2 on a real period2piL is E_L/4.
An anti-periodic sign when LD is odd does not affect the square
or coefficient orthogonality.

At every complex z, discrete Fourier orthogonality across L
translates gives

    (1/L)sum_(j=0)^(L-1)|I_L(z+2pi*j)|^2
      =(1/4)sum_(r modL)
          |sum_(k congruent r) d_k*exp(i(k/L-D/2)z)|^2
      <= (D+1)exp(D|Im z|)*E_L/4.                       (3)

Each residue class has at most D+1 entries and every frequency
lies in[-D/2,D/2]. This is independent of factor degreeLD.

## 3. Rouché and Poisson supply the lower estimate

Each translated disk B(zeta+2pi*j,rho) has the same odd zero
count. If |I_L|^2<|p| on its entire boundary, Rouché would give
R_L^2=p-I_L^2 the same odd zero count, impossible for a square.
Therefore the maximum of |I_L|^2 on that inner circle is at
least eta. No simple-zero or derivative assumption is used.

The Poisson kernel for radiusrho inside radius2rho is at most3.
Subharmonicity of |I_L|^2 consequently gives

    eta <=3*mean_theta |I_L(zeta+2pi*j+2rho*exp(i theta))|^2.

Average over j, apply (3) on the outer circle, and use
|Im(zeta+2rho exp(i theta))|<=|Im zeta|+2rho. This proves (1).
Overlapping translated disks cause no problem: (3) is an exact
sampling bound, not a disjoint-region argument.

For a fixed branch, minimization over its global phase yields

    min_phase E_L=2lambda-2|sum_k q_k*q_(N-k)|.

Bound (1) therefore applies to this phase minimum too. It covers
complex coefficients and all extra dilation branches, without a
continuity theorem for selecting roots.

## 4. Combining arbitrarily many disks with an exact Gram bound

Take a finite collection of odd-zero disks (zeta_j,rho_j), their
positive boundary minima eta_j, and weights w_j>=0, not all0.
Write z_j(theta)=zeta_j+2rho_j exp(i theta). For a finite frequency
set Omega define the positive semidefinite Gram matrix

    G_Omega(a,b)=sum_j w_j*mean_theta
          exp(-i*omega_a*conjugate(z_j(theta)))
             *exp(i*omega_b*z_j(theta)).

Use Omega_*={a-D/2:0<=a<=D} and
Omega_s={a+s-D/2:0<=a<D}, 0<=s<=1, and set

    Lambda=max(||G_Omega_*||, sup_(0<=s<=1)||G_Omega_s||).

The norms are Hermitian operator norms. Lambda is finite and
positive. The residue blocks in (3) are precisely subsets of
these frequency sets; zero extension and the same orthogonality
give the stronger bound

    E_L >= (4/(3Lambda))*sum_j w_j*eta_j.                (4)

The same Gram bound holds for any finite exponential polynomial
with frequencies in[-D/2,D/2] on a common rational mesh: average
over a common number of2pi translates, group frequencies modulo1,
and bound each block by Lambda times its coefficient energy.
In particular it holds for integer/half-integer functions, using
two translates and normalized real-period mean on4pi.

Define the certificate strength

    F_D(p)=sup_(finite disks,nonnegative weights)
                          (sum_j w_j*eta_j)/Lambda.     (5)

One disk and the crude trace bound recover (1). The supremum
is finite: (4) and min_phase E_L<=2lambda give F_D(p)<=3lambda/2.
A tempting universal target would be F_D(p)>=c*n/lambda at actual
lambda=M(A)<=sqrt(n). Together with min_phase E_L<=2lambda,
(4) would imply lambda^2>=(2c/3)n. The target is SUFFICIENT,
not an established equivalent of Chowla. Section6 refutes it.

## 5. A band-limited vector majorant bounds the WHOLE certificate class

Suppose p=R^2+e, where R is entire and real on the real axis,
and suppose |e(z)|<=sum_l |J_l(z)|^2 for ALL complex z, with
each J_l a finite integer/half-integer exponential polynomial
of bandwidth at most D/2. Then

    F_D(p)<=3*sum_l ||J_l||_2^2.                         (6)

Proof: on every odd-zero disk, Rouché compared to R^2 gives
eta_j<=sup_inner |e|<=sup_inner sum|J_l|^2. Poisson gives the
factor3 as in Section3. Average over two translates, sum with
w_j, and apply the exact Gram bound to every J_l. The right
side is at most3Lambda sum||J_l||_2^2. This proves (6) for
EVERY finite disk/weight collection, hence for the supremum.

No scalar factor with small anti-energy is constructed or
assumed by (6). A cheap vector majorant can defeat this lower-
certificate architecture without proving a cheap scalar phase.

An elementary useful majorant is as follows. If
e(z)=c+sum_(a=1)^D c_a*cos(az), c,c_a real, put W=sum c_a^2.
Let u_+=exp(iDz/2),u_-=exp(-iDz/2),
F_+=sum c_a exp(i(a-D/2)z),F_-=sum c_a exp(-i(a-D/2)z).
Then, for any t>0, the complex triangle inequality and Young give

    |e(z)|<=|c| + (|F_+|^2+|F_-|^2)/(4t)
                        +t*(|u_+|^2+|u_-|^2)/4.       (7)

All five square-root majorant functions have bandwidthD/2.
Their total coefficient energy is |c|+W/(2t)+t/2, minimized
at t=sqrt(W) when W>0. Thus

    F_D(p)<=3*(|c|+sqrt(W))                             (8)

whenever p=R^2+e has such an error. W0 is handled by the
constant majorant alone. The inequality holds throughout the
complex plane; no unverified strip estimate is involved.

## 6. A genuine Boolean near-square family falsifies the universal target

Use the two-sided Sidon family in Bu et al.,
[v1, Proposition2.1 and Theorem1.2](https://arxiv.org/html/2610.17160v1).
Its defining identity has n=k(k-1) and

    f_A=T^2-k/2-C/2,
    T=sum_(j=1)^k cos(b_j z), C=sum_(j=1)^k cos(2b_j z),

where b_j=|3s_j+1/2| are distinct positive half-integers. Write
h=max b_j and g=second largest; then D=maxA=h+g. All its
cross frequencies are genuine distinct unit-coefficient frequencies.

Remove the largest term from the trial real square: T0=T-cos(hz).
It has bandwidth g<D/2. For actual lambda=M(A), delta=lambda-k/2,
the EXACT identity becomes

    p=T0^2+e0,
    e0=delta+1/2
         +sum_(b_j<h)[cos((h+b_j)z)+cos((h-b_j)z)]
         -(1/2)sum_(b_j<h)cos(2b_j z).                  (9)

Every error frequency is at most D. The positive cross terms
are2(k-1) distinct frequencies; the negative diagonal terms
are k-1 distinct frequencies of weight-1/2. Any overlap is
between opposite signs and reduces the squared coefficient sum.
Consequently W<=9(k-1)/4. Equations (8)--(9) prove the uniform
upper bound on ALL odd-disk/sampling certificates

    F_D(p)<=3*(|delta+1/2|+(3/2)sqrt(k-1)).              (10)

This uses the ACTUAL bandwidth D and ACTUAL minimum. There is
no padded-degree loophole and no scalar-factor continuity step.

The cited construction gives the upper asymptotic, while the
repository's independently checked P16' lower theorem applies
to its Sidon sets of spanO(k^2); together they give

    lambda=k/2+o(k), in fact |delta|=O(k^(4/5)).

See [the P16' proof record](../PROOFS.md) and its stated quantitative
span hypothesis. Hence these are actual-lowM Boolean examples
eventually, and

    F_D(p)=O(k^(4/5))=o(n/lambda).                      (11)

Therefore NO absolute positive c can make the target following
(5) hold on every Boolean support, even with arbitrarily many
odd-zero disks, arbitrary nonnegative weights and the exact
sampling operator norm. This is a falsification of that specific
certificate route. It neither disproves Chowla nor shows that
all scalar spectral factors of this family have small anti-energy.

## 7. Strategy review and next derivation

This cycle proves a quantitative fixed-symbol phase gap valid
for all complex branches/dilations, then falsifies its proposed
universal upgrade with an infinite genuine Boolean family.
The single-disk stability statement remains valid. Stop trying
to reach a universal root bound by optimizing this odd-zero/
Poisson/sampling certificate class; (10) covers the whole class.

Two preliminary ideas were checked and dropped before new
computation: f=g-h with h<=M gives a convolution errorO(M||f||1),
which reaches the recorded n^(1/3) barrier; high-degree Hermite
diagonal completion repeats the recorded H1/Parseval-noise issue.
Neither is counted as a new route or theorem.

The next argument must retain the ACTUAL scalar coupling or
use the full signed Rayleigh form. The vector majorant in (7)
deliberately loses that coupling. Preserve the exact Boolean
autocorrelation equations and signed-centroid identity, rather
than infer a universal phase-energy gap from odd roots. Also
retain the independent mixed-correction construction track.

First concrete retained derivation: for actual-lowM A, set
F=sum_A z^a, lambda_R=2sqrt(n), r=(lambda_R+F)^(-1),
t=<F,F^2>, C1=<F,r>, C2=<F^2,r> and
H0=<2f_A*(Im r)^2>, with normalized circle pairings. The existing
exact Boolean recurrence is

    lambda_R*C2=-t/lambda_R-(2n-1)*C1-R_A(r),
    R_A(r)=sum_(a,b,c in A; c!=a,b; a+b>c) r_(a+b-c).

The retained P2 target is C2^2>=2tH0, or for t>0

    [t/lambda_R+(2n-1)C1+R_A(r)]^2
                         >=2t*lambda_R^2*H0.           (12)

This remains unproved and optional, not a new theorem or a
complete description of useful witnesses. It must control the
signed residual jointly with the inverse norm inside H0; its
component signs are already refuted. Do not replace r by another
fixed polynomial span or run another successful-control sweep.

The published outer-factor continuity results require additional
control and concern the chosen OUTER factor; they do not supply
the missing all-branch polynomial selection step. This scope was
checked against [Ephremidze--Shargorodsky--Spitkovsky, Theorems1--2,
v2](https://arxiv.org/html/1603.01101v2). No claim is made that their
counterexamples settle optimization over all root flips.
