# Independent audit of the three-color tapered W1 proof

2026-10-20. Reviewed `obstructions/weak_w1_taper_proof.md` after the deterministic implant audit.

Verdict: the proof is valid. It independently supplies a weak-W1 sequence and repairs the earlier absence of a rigorous random-model W1 upper bound. It is not needed for the deterministic signed-layer theorem.

## Conditioning and dependence

The original entries are not independent, but the proof never applies matrix Bernstein to those entries. For a good ordered pair (u,v), the three positive signclasses |u|,|v|,|u-v| are distinct. Uniform independent coloring selects its specified color pattern with probability 1/27, giving the exact entrywise averaging identity. Terms with |u-v|>X are zero and can simply be omitted before coloring.

The only possible coincidences among the three signclasses for distinct nonzero u,v are v=-u, v=2u, and v=u/2. The discarded symmetric matrix has at most three entries of magnitude at most one in each row, hence norm at most three.

For fixed colors, conditioning on every color-1/color-2 Bernoulli variable leaves color-3 Bernoulli variables independent and unaltered in distribution. The matrices M_d are now deterministic; they depend only on the conditioned endpoint variables. Thus the conditional summands xi_d M_d really are independent and centered.

For each d, every row and column has at most two nonzero entries, so ||M_d||<=2. In the first variance sum, a row-sum estimate uses at most two possible u' for a given v,d; after this factor of two, each selected v contributes to at most one d=|u-v|. The asserted bound 4 alpha n_2 therefore includes every off-diagonal term. The transpose bound is identical. No unjustified assumption that the lag matrices are matchings or that M_d M_d* is diagonal is present.

## Imported concentration result

I checked Theorem 1.6 directly in Joel Tropp's primary-source preprint:

https://tropp.caltech.edu/papers/Tro11-User-Friendly-preprint.pdf

It applies to independent centered rectangular matrices with uniformly bounded operator norm, using the maximum of the two variance-sum norms. These hypotheses hold conditionally here with norm bound 2, dimension sum at most 4X, and variance at most 4 alpha n_*. Its tail gives the stated expectation estimate after integration. Jensen then applies to the random n_*, whose expectation is at most 2 alpha X. The coloring average uses convexity of operator norm and introduces only the constant 27.

## Mean and center

The interval-feature identity for the triangular kernel is exact, including diagonal p_0=2 alpha. Every feature interval lies in [-X,2X]. Cauchy-Schwarz on that interval proves P>=(2 alpha/3)J for complex as well as real coefficient vectors. Restricting to selected rows preserves the bound.

On those selected noncentral rows, B=P-2 alpha I+Z exactly. For e=2 alpha+||Z|| and a=2 alpha/3, adding diagonal k>=max(e,1/a) bounds the centered W1 matrix below by [[k,1*],[1,aJ]]. This last matrix is PSD: on center and the uniform vector its determinant is n(ka-1), and it vanishes on the remaining directions. Thus the center does not create an overlooked sqrt(n) negative eigenvalue.

## Quantifiers

For X=t^4 and alpha=1/t (t>=2), mu is asymptotic to t^3, and the expectation certificate bound is O(t sqrt(log t)). Dividing by sqrt(mu), applying Markov, and using |A|/mu->1 in probability proves K_W1/sqrt(N)->0 in probability. The positive-probability existence claim follows immediately. This asymptotic is asserted for the chosen parameter sequence, not for arbitrary alpha,X with only mu->infinity.

The proof controls W1 only. It makes no claim that the true cosine minimum or the full W2 minimum is small.
