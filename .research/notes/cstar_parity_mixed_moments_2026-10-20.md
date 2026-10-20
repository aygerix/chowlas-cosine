# Exact parity mixed moments for product rounding

Checkpoint: 2026-10-20T05:56:36.620284+00:00. Ongoing research; no universal Chowla/C* or W2 constant is established. [Reproduction index](../experiments/cstar_structural_2026-10-20/README.md).

Status: exact expectation calculation; it exposes an obstruction to a proposed proof, not a counterexample to W2. 2026-10-20.

Let U=[-2,2]^d, p(s)=product_j(1-|s_j|/3), and independently retain each nonzero pair {s,-s} with probability p(s). Write D(theta)=sum_{s in S} e(s.theta), chi(s)=(-1)^(sum_j s_j), and D_chi(theta)=D(theta+(1/2,...,1/2)). N=|S|, E N=3^d-1.

The vector u(s)=chi(s)1_S(s)/sqrt(N) is supported in S. Its full convolution image Bu is supported in S+S. Hence the two-dimensional Krylov trial space span(u,Bu) always belongs to W2, without any ambient filling hypothesis. Moreover (Bu)(x)=0 whenever chi(x)=-1, by pairing s and x-s.

Its first three moments are h=integral D D_chi^2/N, m2=integral D^2 D_chi^2/N, and m3=integral D^3 D_chi^2/N. Exact expectation formulas for the unnormalized numerators have asymptotics

- E integral D D_chi^2 = -(19/9)^d + O((13/9)^d).
- E integral D^2 D_chi^2 = 9^d - (361/81)^d + O((11/3)^d).
- E integral D^3 D_chi^2 = (47/3)^d - (893/81)^d + O((275/27)^d).

In particular, parity suppresses the mean signed triangle but DOES NOT suppress the leading noise-pair times ordinary triangle contribution to the fifth moment. Since 47/3 > 3^(5/2), this third-moment term is very slightly above the square-root Krylov scale. Merely dividing expectations by the typical N suggests the same N^2/T barrier as before. This is not a concentration proof, nor a proof that this Krylov space typically fails: that would require estimates of fluctuations and the random denominator. It does refute the proposed small-expectation argument for m3.

## Exact computation method

The script parity_mixed_expectation.py expands joint moments through set partitions. Each block of size l has symmetric Bernoulli cumulant kappa_l(p)=sum_{r=1}^l (-1)^(r-1)(r-1)! Stirling(l,r) p^r. Equality of symmetric coefficient variables is represented by signed identifications, fixing the first sign in every block. For a signed block b, let c_b be the sum of its signs and a_b the sum of signs on the marked D_chi factors, modulo two. A cumulant monomial is then a product over coordinates of the scalar finite sum

sum_{x_b in [-2,2], sum c_b x_b=0} (-1)^(sum a_b x_b) product_b ((3-|x_b|)/3)^r_b.

Thus its contribution is exactly a rational number raised to the d-th power. The origin is initially included deterministically, and then removed by the binomial expansion D=D_full-1 and D_chi=D_full,chi-1. Higher cumulants at p(0)=1 vanish, so signed identifications at zero introduce no extra terms. All arithmetic determining the rational bases is exact. Full formulas are in parity_mixed_expectation.json. Direct exhaustive enumeration of the four possible sets in dimension one gives moments -4/9, 38/9, -8/9, agreeing with the formulas.

## Independent numerical extension

product_fejer_d6.py extends the same random sequence as the earlier d2 through d5 samples. At d6, N=692, |W2|=90247. Full optimized induced adjacency gives K_W2=64.0445910391, N/K_W2^2=0.1687101381, eigenpair residual 2.52e-7. This ordinary floating-point check supports no asymptotic conclusion by itself. The FFT grid had 11^6=1771561 entries and no circular adjacency aliasing. Raw output: product_fejer_d6.json.

Additional independent check: verify_parity_moments.py enumerates all 4096 symmetric subsets in dimension two and accumulates their probability-weighted integer Fourier moments. It agrees with the rational-base formulas, yielding -1760/729, 145352/2187, and 552128/6561. The moment coefficients are extracted by rounded FFT (well separated from half-integers at this small size), while probability accumulation and final comparison use exact integer/rational arithmetic. This is a computational cross-check, not a formal exact FFT certificate.

The independent fixed-U centered-noise argument in product_fejer_asymptotic.md supersedes the attempted parity approach for this model and supplies the asymptotic square-root lower bound. The parity obstruction remains useful because this alternative had avoided the filling hypothesis; its fifth moment shows exactly where that simplification fails.
