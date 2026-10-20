# Growing-order cyclotomic and determinant test

Scope: C* CHAIN(c). This is a concrete failure calculation, not a proof that every possible arithmetic approach fails. Read CSTAR O1–O6, PROOFS P61(b), P65.3 (the fixed-order M1/M2 obstruction). The tests here run at unbounded orders and all coprime cyclotomic orders simultaneously.

Let S=-S be finite, 0 not in S, N=|S|, X=max S, and let

P(z)=K+sum_{s in S} z^s >=0 on the unit circle,

where K is an integer ceiling of the true negative excursion. Target N<=C K^2.

## 1. The precise prime-norm constraint

Take a prime q>2X+1 and d=q-1. P(zeta_q) is a totally positive algebraic integer. It cannot vanish: z^X P(z) has degree 2X<deg Phi_q. Consequently

R_q=Norm(P(zeta_q))=product_{j=1}^{q-1} P(zeta_q^j) is a positive integer, hence R_q>=1.

There is no aliasing at this order, and Booleanity gives the exact identities

mu_q = average_j P(zeta_q^j) = K-N/d,

V_q = average_j (P(zeta_q^j)-mu_q)^2 = q N(d-N)/d^2.

Derivation: sum_j zeta_q^{js}=-1 for s nonzero, and the ordered zero sums in S+S are exactly N. Thus sum_j D(j)^2=qN-N^2, before centering.

AM–GM and the norm yield only

K >= 1+N/(q-1).

At q comparable to X this is a density bound, not a square-root bound; at growing q it tends to K>=1.

Here is a quantitative second-moment refinement, rather than simply asserting that AM–GM loses information. For 0<t<=B and 0<mu<B,

log t <= log mu +(t-mu)/mu - c(mu,B)(t-mu)^2,

c(mu,B)=[B/mu-1-log(B/mu)]/(B-mu)^2.

The scalar inequality follows because (u-1-log u)/(u-1)^2 decreases for u>0 (or by the integral representation integral_0^1 (1-s)/(1+s(u-1))^2 ds). Set B=K+N. The norm lower bound now implies

c(mu_q,B) V_q <= log mu_q.

As q tends to infinity, this becomes exactly

N/K-log(1+N/K) <= N log K.

For every integer K>=2 this is automatically true for every N: the left side is <=N/K, while log K>=1/K. Thus even the exact Boolean second moment added to the full prime norm, through this sharp global quadratic log majorant, imposes no C* restriction.

This does NOT prove that all optimizations with more information about the conjugates fail. It identifies the actual failed inequality.

## 2. An all-orders, full-Galois, no-wrap weighted integer control

For L>=2, define U_L(z)=1+z+...+z^{L-1} and

P_L(z)=U_L(z)U_L(z^{-1})
       =L+sum_{0<|k|<L}(L-|k|)z^k.

This is nonnegative, has integral nonnegative coefficients, constant K=L, and extreme coefficients exactly 1. Its off-zero Fourier energy is

E_L=2 sum_{r=1}^{L-1} r^2 = L(L-1)(2L-1)/3,

so E_L/K^2 is asymptotic to 2L/3, unbounded. The off-zero coefficient mass is L(L-1), asymptotic to K^2; the counterexample concerns the L2 target, which equals support size precisely in the Boolean case.

For EVERY q>1 with gcd(q,L)=1,

Norm_{Q(zeta_q)/Q} U_L(zeta_q)
 = Norm[(1-zeta_q^L)/(1-zeta_q)] = 1,

because zeta_q -> zeta_q^L is a field automorphism and permutes the primitive conjugates. Therefore

Norm P_L(zeta_q)=1.

This is exact saturation of the strongest elementary integer-product lower bound, at all coprime orders simultaneously, including every prime q>2L. There is exact no-wrap compatibility across these orders because they are evaluations of ONE fixed Laurent polynomial on Z, not independent finite-group models.

For noncoprime q the evaluations can vanish; any nonzero norm is still a positive integer. Thus integrality and all-order norm constraints, by themselves, cannot bound off-zero Fourier energy by CK^2. This control does not satisfy the coefficient cap a_k<=1 and is NOT a counterexample to C*.

## 3. All Toeplitz principal determinants: integer lower bounds are redundant

More generally, let P be any nonnegative real Laurent polynomial with extreme coefficient 1, without integral or Boolean coefficient assumptions. Since F(z)=z^X P(z) is monic, Jensen's root formula gives

integral_T log P >=0.

Zeros on the circle cause no problem: logarithmic singularities are integrable. For any finite distinct integer index set I={i_1,...,i_m}, let

G_I=(P_hat(i_a-i_b))_{a,b}.

Then

 det G_I >= exp(m integral_T log P) >=1.

One proof: choose an outer Fejer–Riesz factor Q with P=|Q|^2 and |Q(0)|^2=exp integral log P. Sort the indices increasingly. The Gram vectors z^{i_a}Q have a triangular coefficient minor with diagonal Q(0), so Cauchy–Binet gives det G_I>=|Q(0)|^{2m}. A common shift makes every i_a nonnegative. This works for arbitrary principal index sets, not just contiguous blocks, and at all growing matrix orders.

Thus the putative extra arithmetic inference “positive determinant is an integer, so it is >=1” adds NOTHING to positivity plus the outer coefficient 1. P_L above satisfies these determinant bounds while its energy/K^2 diverges. Stronger arithmetic involving individual determinant values or relations between distinct minors is not ruled out by this observation.

## 4. What exactly survives the adversarial controls

- P61(b) is fractional and need not have monic extreme coefficient or integral norms. Therefore raw norm tests may reject those particular packets, but rejecting P61 alone is not evidence for a Boolean theorem: P_L is the replacement integral, no-wrap, all-orders control.
- Finite-group cones have exact Boolean coefficients and the bad N/K^2 asymptotics. They already satisfy positivity and algebraic-integer norm/determinant tests on their character fields. What fails upon lifting is positivity between finite-grid points, not these arithmetic facts. Cyclic prime arithmetic could still contain more information than vector-space cones; no equivalence is asserted.
- The integer Fejer control has true global positivity and simultaneous no-wrap data, but violates Booleanity. Hence a successful arithmetic argument must use a quantitative upper coefficient restriction/exact Boolean relation in a step that rejects this control. Frobenius congruences P(z)^ell=P(z^ell) mod ell do not do so: they hold for every integer coefficient polynomial.
- Full knowledge of P(zeta_q), not merely its norm or scalar traces, at one q>2X+1 encodes all coefficients by Fourier/Galois inversion. Adding exact Booleanity to that full object is not a relaxation; it can restate C*. The calculation above closes the elementary norm/determinant inference, not the entire growing-order/full-Galois direction left open in P65.3.

Bottom line: no C* advance. The exact all-orders Fejer cyclotomic-unit control rules out integrality-only Fourier-energy bounds even with simultaneous no-wrap compatibility; arbitrary growing principal determinant lower bounds are provably redundant. The tested norm-plus-exact-Boolean-variance inequality is vacuous for K>=2. A new arithmetic argument would have to use more than these invariants and explicitly exploit the coefficient cap.
