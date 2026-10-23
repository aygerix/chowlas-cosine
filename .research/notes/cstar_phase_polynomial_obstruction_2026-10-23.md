# Fixed-degree phase polynomials cannot provide universal root-scale Rayleigh bounds

2026-10-23. Paper theorem, independently checked by the internal advisor
in [the current audit](advisor_P2_boolean_2026-10-23.md). Not a
kernel-checked or externally scrutinized result; novelty unverified.
This tests an arbitrary-support certificate architecture. It is not
another search for an improvement inside a settled construction family.

All circle averages below use dx/(2pi). For a Boolean set A, write
F_A=sum_A z^a, f_A=Re F_A, b_A=Im F_A, and D_A=2f_A.

## Quantified statement

Let B be a cyclic perfect difference set of size k, represented in
{0,...,Q-1}, where Q=k(k-1)+1. Every nonzero residue modulo Q occurs
exactly once as an ordered difference of B. Let A be its positive
integer differences. Then

    n=|A|=k(k-1)/2, max A<Q, M(A)<=k/2<sqrt(n) for k>2.

For every fixed integer d>=1, there are constants C_d and k_d,
independent of the choice of B, such that whenever k>=k_d,

    <D_A*q²>/<q²> >= -C_d

for every nonzero real function q(x)=P(f_A(x),b_A(x)), where P is a
real polynomial of total degree at most d. Its coefficients may depend
arbitrarily on A and k. Consequently this whole fixed-degree family
cannot certify M(A)>=c*sqrt(n) for any absolute c>0 on all Boolean A.

More strongly, the energy is strictly positive for every nonzero
linear combination of the nonconstant monomials f_A^r*b_A^s,
1<=r+s<=d, once k is sufficiently large. After their means are
subtracted it is still strictly positive. The constant is what permits
bounded negative energy in the full polynomial space.

The existence of infinitely many cyclic perfect difference sets is a
classical prior dependency, already used for the dense Singer controls.
Nothing here is a new construction-side upper constant. The claim
does not restrict unrestricted signed trigonometric witnesses,
non-polynomial transforms, or polynomial degrees tending to infinity.

## 1. Booleanity and the exact all-circle premise

Equal positive integer differences would also be equal cyclic ordered
differences, so A is a genuine set with n=k(k-1)/2. For
U=sum_(b in B)z^b, the exact square identity is

    D_A=|U|²-k.

It gives the stated all-circle M upper bound without sampled minima.
At the Qth roots omega^j, U(1)=k and |U(omega^j)|²=k-1 for j!=0.

Put D_Q=sum_(j=0)^(Q-1)z^j, S=(k/Q)*D_Q, R=U-S, and ell=1+log Q.
R vanishes at 1 and has modulus sqrt(k-1) at the other Qth roots.
Cardinal interpolation gives

    R(z)=(1/Q)*sum_j R(omega^j)*D_Q(z*omega^(-j)),
    ||R||infinity=O(sqrt(k)*ell).

The second assertion follows from the elementary Dirichlet Lebesgue
sum Q^-1*sum_j|D_Q(z*omega^(-j))|=O(ell): order the roots by circular
distance from z and use |D_Q(e^ix)|<=min(Q,pi/|x|) for |x|<=pi.
All constants are independent of B. No sampling-to-Lp theorem is needed.

## 2. Analytic Fejer-front approximation for every fixed moment above two

Write

    Phi_Q=|D_Q|²/Q,
    G_Q=sum_(j=1)^(Q-1)(1-j/Q)z^j,
    alpha=k²/Q -> 1.

Then 2Re G_Q=Phi_Q-1. For fixed p>2,
||D_Q||p=O_p(Q^(1-1/p)), so

    ||D_A-alpha*(Phi_Q-1)||p
      =O_p(k^(3/2)*Q^(-1/p)*ell+k*ell²).

Indeed the error is 2Re(S*conjugate(R))+|R|²-k+alpha.
Project onto positive Fourier frequencies. On degree<Q trigonometric
polynomials this projection has Lp operator norm O(ell), by convolution
with the one-sided Dirichlet kernel and its L1 bound. Hence

    ||F_A-alpha*G_Q||p
      =O_p(Q^(3/4-1/p)*ell²+Q^(1/2)*ell³)
      =o(Q^(1-1/p)).                              (1)

This is deliberately asserted only for p>2. In degree two the profile
need not capture all variance. That missing assertion is not used.

For t in a fixed bounded interval,

    G_Q(e^(it/Q))/Q -> H(t)=int_0^1(1-u)e^(iut)du.

Abel summation gives |G_Q(e^(it/Q))|/Q<=C/(1+|t|) on |t|<=pi Q.
For every homogeneous polynomial V of degree m>=3, (1), Holder and
dominated convergence therefore imply

    Q^(-(m-1))*<V(f_A,b_A)>
      -> (1/(2pi))*int_R V(Re H(t),Im H(t))dt.      (2)

The Holder error is o(Q^(m-1)); each remaining factor has Lm norm
O(Q^(1-1/m)). This also proves the absolute moment estimates needed
below. All convergence is uniform in the chosen cyclic difference set.

## 3. The limiting nonconstant energy matrix is strictly positive

Use the basis v_rs=f_A^r*b_A^s/Q^(r+s), 1<=r+s<=d. By (2), its
D_A-energy matrix converges to

    G_((r,s),(u,v))=(1/pi)*int_R Re H(t)
                      *(Re H)^r*(Im H)^s*(Re H)^u*(Im H)^v dt. (3)

The entries themselves converge; there is no extra factor Q.
Here Re H(t)=(1-cos t)/t² is nonnegative and positive almost everywhere.
To prove strict positive definiteness, it remains to exclude a
polynomial relation between Re H and Im H on the real axis.

Suppose a nonzero polynomial had such a relation. By the invertible
change of variables Re H=(H(t)+H(-t))/2 and
Im H=(H(t)-H(-t))/(2i), a nonzero polynomial T would satisfy
T(H(t),H(-t))=0 for every real t. H is entire, so the identity extends
to complex t. Set t=iy and let y tend to positive infinity. Then

    H(iy)=(y-1+e^(-y))/y² ~ 1/y,
    H(-iy)=(e^y-1-y)/y² ~ e^y/y².

Write T(X,Y)=sum_(j=0)^J a_j(X)*Y^j with a_J nonzero. For some
finite m>=0, a_J(H(iy))~c*y^(-m), c!=0. The j=J term dominates
all smaller j exponentially, a contradiction (also for J=0).
Thus no such relation exists. Every nonzero coefficient vector in
(3) has strictly positive integral. Its least eigenvalue is positive
because d is fixed.

This proves eventual strict positivity for the uncentered nonconstant
monomials, including all odd polynomial phase spaces of fixed degree.

## 4. Add the constant and obtain a uniform O_d(1) Rayleigh cap

Let mu_rs=<v_rs>. The linear means are zero. For total degree m>=2,
<|F_A|^m>=O_m(Q^(m-1)), using exact <|F_A|²>=n when m=2 and (1)
when m>2. Therefore mu_rs=O_d(1/Q). Let w_rs=v_rs-mu_rs.

The cross energies beta_rs=<D_A*v_rs> are O_d(1). For degree one
they are exactly n/Q and zero; for larger degrees apply the absolute
moment bound of degree m+1>=3. Centering changes nonconstant energy
entries by O_d(1/Q), since <D_A>=0. Consequently their centered
matrix E_k has a uniform positive lower bound eta_d*Id eventually,
and the constant-cross vector beta_k has uniformly bounded norm B_d.

Every polynomial in the theorem has a unique expression
q=a0+sum a_rs*w_rs. Since all w_rs have mean zero,

    <q²> >= a0²,
    <D_A*q²> = 2*a0*beta_k dot a + a^T E_k a
             >= -(B_d²/eta_d)*a0²
             >= -C_d*<q²>.

The conclusion allows arbitrary parameter-dependent coefficients;
positive definiteness is a statement about the entire finite-dimensional
space, not selected test vectors. It needs no convergence of the
linear-basis norm matrix to the front profile.

## Decision and relation to the main goal

The exact n56/n306/n337 five-count falsifiers prompted this general
derivation. Stop trying to repair the same architecture by adding
another fixed number of powers of F, f or b. Retain unrestricted signed
Rayleigh and non-polynomial witnesses. The reciprocal sign S0 and
adaptive P2 are still unproved and are not covered by this obstruction:
their denominators resolve a changing amplitude scale.

The advisor's new inverse-coefficient identity uses the exact unit
coefficients but has a residual with both signs inside actual lowM.
The next useful derivation must control that residual jointly with
the reciprocal norm/cross energy, or construct a different non-polynomial
Boolean witness. Another component sign or fixed-degree power ansatz
does not remove either recorded obstruction.
