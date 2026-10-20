# Rank versus the negative floor: a proved integral-SOS case and the remaining gap

Checkpoint: 2026-10-20T05:56:36.620284+00:00. Ongoing research; no universal Chowla/C* or W2 constant is established. [Reproduction index](../experiments/cstar_structural_2026-10-20/README.md).

2026-10-20. CHAIN(c). Separate from the W2 derivations. No universal rank bound is proved or assumed.

Let S=-S⊂Z^r\{0} span rank r, D=sum_{s∈S}e(s·x), and K=-min D. The proposed target is K≥c r. The simplex difference example shows that linear dependence on r would be the natural scale: Q=1+e(x_1)+...+e(x_r) has |Q|²=(r+1)+D for its distinct nonzero differences, and min |Q|²=0, giving K=r+1.

## A valid theorem under an extra arithmetic factorization hypothesis

Suppose K+D has a representation

  K+D = sum_{j=1}^J |Q_j|²,

where each nonzero Q_j is an integer-coefficient Laurent polynomial. Put E_j=supp Q_j. Comparing constant terms gives

  K=sum_j sum_{u∈E_j}|coefficient_u Q_j|² ≥ sum_j |E_j|.

The support of D is contained in the union of E_j-E_j, even if cancellations occur between different squares. Hence

  r ≤ sum_j rank(span(E_j-E_j)) ≤ sum_j(|E_j|-1)
    ≤ K-J ≤ K-1.

Thus this hypothesis proves K≥r+1, not just a constant multiple of r. The argument remains valid for Gaussian-integer coefficients.

The hypothesis is essential to the proof: a real or rational coefficient can have arbitrarily small squared magnitude, so constant term need not count support points. Ordinary positivity is not an integral Hermitian SOS assertion. Rounding K upward to make the polynomial's constant term integral does not produce such a representation. No step here promotes a general multivariate nonnegative polynomial to integer SOS.

## Why a basis Riesz product is insufficient

Choose independent frequencies b_1,...,b_r∈S. A product of negative first-harmonic factors creates negative Fourier coefficients on odd subsets and positive coefficients on even subsets. The remaining Boolean support may include the even-subset sums, so those contributions cannot simply be discarded. Independence of the basis does not rule them out. The finite elementary-abelian examples show the combinatorial danger of such parity tests particularly clearly, although they are not counterexamples to the torsion-free rank assertion.

## Status

The integral-SOS rank bound is fully proved. A general implication from Boolean positivity to a comparable rank bound, or an explicit torsion-free counterexample with K/r tending to zero, remains unresolved in this pass. A narrow literature search did not identify a primary theorem that could safely be invoked; no novelty claim is attached to the elementary SOS observation.

## Exact obstruction: even rounding the floor upward does not give integer SOS

Consider the exact Boolean polynomial

  P(z)=3+z+z^{-1}+z²+z^{-2}.

On the unit circle write t=cos x. Then P=4t²+2t+1=4(t+1/4)²+3/4>0. Its off-zero coefficients are exactly 0 or 1, and its integer constant term is the ceiling of the optimal floor K=9/4. Nevertheless P is not a sum of Hermitian squares of integer Laurent polynomials.

Indeed an integer-SOS representation would have total coefficient-square mass 3. Every nonzero coefficient must therefore be ±1, and the only possibilities for nonconstant factors are:

- One three-monomial factor. Translate its exponents to have minimum 0. Its unique extreme difference must be a frequency of P, so its exponent width is at most 2. Three distinct integer positions then force {0,1,2}. Writing the coefficients as epsilon_0,epsilon_1,epsilon_2∈{±1}, the coefficient at 2 is epsilon_0 epsilon_2=1, so epsilon_0=epsilon_2. The coefficient at 1 is epsilon_1(epsilon_0+epsilon_2)=±2, not 1.
- One two-monomial factor and one monomial factor. This gives only one nonzero frequency pair, not the two pairs of P.
- Three monomial factors, which give no nonzero frequencies.

This exhausts the possibilities and proves the obstruction. The same obstruction holds for Gaussian-integer factors: the endpoint units must agree, and the adjacent coefficient is twice the real part of a unit, hence 0 or ±2.

Furthermore, the integer-SOS hypothesis would directly imply a square-root cardinality bound, not merely a rank bound. With m_j=|E_j|,

  |S|≤sum_j m_j(m_j-1)≤K²-K.

Thus assuming such a representation is already stronger than the desired Chowla estimate, and the tiny positive example above shows it cannot serve as a general bridge from Boolean positivity. This identifies an exact failed mechanism rather than an unverified technical assumption.

## A nonintegral, cancellation-free single-factor rank bound

There is a broader valid special case which does not require integer coefficients. Suppose

  K+D=|Q|²,   Q=sum_{u∈E} a_u e(u·x),   a_u>0,

and let m=|E|. Because all coefficients are positive, there is no cancellation in autocorrelation, so S=(E-E)\{0}; hence E has affine dimension r. Evaluation at x=0 and the Boolean off-zero coefficients give

  K+|S|=(sum a_u)²≤m sum a_u²=mK,
  |S|≤(m-1)K.                                             (4)

The classical difference-set dimension inequality is

  |E-E|≥(r+1)m-r(r+1)/2.

A primary reference explicitly recording this inequality is Akshat Mudgal, “Difference sets in higher dimensions,” introduction and Lemma 2.3, https://arxiv.org/pdf/2007.11526. Applying it to (4) yields

  K≥r+1-r(r-1)/(2(m-1))≥(r+3)/2,                         (5)

since m≥r+1. This is a linear-rank theorem for an arbitrary positive-real single spectral factor. It applies, for example, to 9/4+z+z^{-1}+z²+z^{-2}=|1+z/2+z²|², whose factor is not integral.

The limits are important. Signed or complex coefficients can cancel difference coefficients, so S need not equal E-E\{0}. With several positive-real squared factors, the individual autocorrelations need not be Boolean; they may add to the final coefficient 1. Therefore neither the support identification nor (4) may be applied to each factor separately. No universal positive-factor representation or reduction to one such factor has been proved. Equation (5) supplies a legitimate cancellation-free rank mechanism, not a theorem for all Boolean cosine sums.
