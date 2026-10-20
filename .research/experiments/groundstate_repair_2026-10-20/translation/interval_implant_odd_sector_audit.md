# Independent audit: interval implant and its full odd-sector obstruction

2026-10-20. Audited the argument in ../schur/groundstate_product_no_amplification.md, especially Section 7.

## Result

The odd-sector theorem is valid, conditional only on the interval parity-gap lemma established in the same note. The independent balanced-sign calculation supplies an unconditional weak-W1 base sequence. The composition therefore gives a genuine Boolean integer sequence for which the unique W1 bottom mode and its entire coupled odd-sector exterior resolvent fail to produce a square-root certificate.

This does not refute full W2. The uncoupled even sector remains available and may contain the needed negative eigenvalue.

## Row-set and positivity check

For S=(T x {0}) union ({0} x U_L), the W2 rows are exactly

(W2(T) x {0}) union ({0} x W2(U_L)) union (T x U_L).

Every row whose first coordinate lies outside I_T={0} union T has second coordinate zero. A coefficient vector odd under reflection in the second coordinate vanishes on all rows with second coordinate zero. Thus any polynomial in the entire odd W2 sector has, for each fixed physical y, x-Fourier support in I_T.

Consequently W1 positivity for T gives

integral_x D_T(x)|F(x,y)|^2 >= -k(T) integral_x |F(x,y)|^2.

Combining this with D_U(y)>=-2L and integrating in y yields

K_W2,odd <= k(T)+2L.

No support or independence hypothesis is missing from this step.

## Resolvent check

Reflection preserves the full W2 matrix, its W1 principal block, and the exterior block. Hence the coupling C* takes odd interior vectors to odd exterior vectors, and every defined exterior resolvent preserves parity. The unique W1 bottom vector from the implant is odd. Its exterior-coupled optimization therefore stays in the odd sector and inherits the preceding upper bound.

An independent even negative direction is not excluded. It need not couple to the old bottom vector, and it could already provide a full-W2 square-root certificate. The theorem rules out universal repair of this selected bottom mode, not all use of the exterior block.

## Wording correction identified

The odd W2 sector does not contain the entire translated-bottom-vector space. Multiplication of odd q(y) by an odd multiplier such as sin(y) gives an even polynomial. Therefore the product-space obstruction and the odd-sector obstruction are complementary, not nested. The claim that the odd sector is 'much larger' should refer only to possible dimension, not containment. This correction was sent to the author.

## Additional checks

- The continuum interval operator has odd bottom -2/(3pi), even bottom -1/(2pi-arctan(3/4)), with a positive linear gap after rescaling. The parity differential equations and endpoint conditions in the proof agree.
- The Schur correction from T is bounded by k(T), and the odd interval vector has zero central coordinate, so it remains an exact simple ground state once the even gap exceeds the correction.
- The residual decomposition gives R=|T|+R_U and exterior numerator t3(T)-k_L|T|+<r_U,D_U r_U> exactly; cross terms vanish as stated.
- The moment lower bound t3(T)>=|T|^2/k(T)-k(T)|T| follows directly from the W1 center/uniform quadratic form.
- Encoding (t,u) as t+Q u with Q>5 max|T| preserves every required W2 adjacency and all product-space Gram and energy integrals.
