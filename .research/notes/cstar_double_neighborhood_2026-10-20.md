# Two-neighborhood continuation: escaping the E99c obstruction

Checkpoint: 2026-10-20T05:32:53.486301+00:00. Research remains ongoing; no universal Chowla/C* theorem is claimed. Reproduction: [experiment index](../experiments/cstar_structural_2026-10-20/README.md).

2026-10-20. Continuation of [the collective-boundary calculation](cstar_collective_boundary_2026-10-20.md). This does not prove universal C*. It proves that the exact E99c countercontrols to the first-neighborhood method are detected at square-root scale by their second neighborhoods, and identifies the additional combinatorial ingredient.

Let S=A union (-A), W1={0} union S, W2={0} union S union (S+S), and K_W=-lambda_min(B_W).

## 1. Same E99c samples, a different and much stronger certificate

The RNG seed 20261021 and full generation order in src/e99c_tapered.py were reproduced, including intervening density exponents. The three samples at alpha=n_target^(-1/3) match the recorded sample sizes exactly.

- n=1056, X=10000: K_W1=33.6422. W2 contains [-14551,14551]. One interval-supported Rayleigh vector gives K_W2>=150.2746. Recorded global FFT estimate K=167.3785.
- n=3962, X=63496: K_W1=48.8291. W2 contains [-98255,98255]. Rayleigh lower bound 345.7223. Recorded global FFT estimate K=393.2421.
- n=15881, X=403175: K_W1=77.7303. W2 contains [-674976,674976]. Rayleigh lower bound 736.6127. Recorded global FFT estimate K=798.5333.

The new Rayleigh bounds divided by sqrt(n) are 4.6244,5.4925,5.8452, rather than the decaying W1 ratios. No second-neighborhood eigensolver was necessary.

**Exact membership check.** W2 was first calculated by rounded FFT convolution, then INDEPENDENTLY recomputed with Python arbitrary-precision bitsets: OR of every shifted copy of the exact integer S-bitset. The central radii and full W2 cardinalities agree exactly. Cardinalities are 34193,226269,1496211. Thus the row-set membership is exact; the reported Rayleigh evaluations are ordinary floating-point numerical bounds, not interval-arithmetic certificates.

The test vector is simply v_j=e(j theta)/sqrt(L), supported on the exact contained interval of length L. Its Rayleigh value is

    2 sum_{a in A} (1-a/L) cos(2 pi a theta).

The theta is a sampled minimizer on a grid with at least 32X points. Every sampled value is a valid Rayleigh test, so grid minimization is not being mistaken for a global-minimum certificate. Floating-point roundoff was not Arb-certified. Scripts and JSON outputs are in [the experiment directory](../experiments/cstar_structural_2026-10-20/README.md).

## 2. Analytic reason the second neighborhood succeeds

Consider the exact tapered independent model

    P(a in A)=p_a=2 alpha(1-a/X), 1<=a<=X, alpha<=1/4.

For any integer 1<=t<=floor(X/2), consider edges (j,j+t) with 1<=j<=floor(X/4). Both endpoints lie in [1,3X/4], where p_a>=alpha/2. These edges form a graph of maximum degree 2, and a greedy matching contains at least floor(X/4)/3 disjoint edges. The events that both endpoints of each matched edge belong to A are independent. Consequently

    P(t notin A-A) <= exp[-alpha^2 floor(X/4)/12].

A union bound shows, with failure probability at most

    floor(X/2) exp[-alpha^2 floor(X/4)/12],

that [-floor(X/2),floor(X/2)] is contained in A-A, hence in W2. (For X>=8, the simpler exponent -alpha^2 X/96 is safe.) This uses actual independent Boolean selections and integer differences, not a spectral-gap assumption.

At E99c's alpha=n_target^(-1/3), X approximately n_target^(4/3), the exponent is order n_target^(2/3), overwhelming the number of candidate differences.

### Finite-section version of P28

If W contains a translate of {0,...,m+H-1} with m>=H, then

    K_W >= integral_T |sum_{a in A}(1-|a-m|/H)_+ e(a x)| dx.       (1)

Proof: take

    q_{x,phi}(y) = H^(-1/2) sum_{j=0}^{H-1} e(j(y-x))
                  times (1+exp(i phi)e(m(y-x)))/sqrt(2).

Its frequency support is {0,...,H-1} union {m,...,m+H-1}, contained in W after translation. The two blocks are disjoint, so ||q||_2=1. Positivity of K_W+B_W gives the same phase-optimized inequality as P28. Integrating in x removes the unshifted convolution term and yields (1). Therefore P28's square-root random-rounding test is genuinely a finite W2 principal-minor certificate when the interval-filling event holds, not an appeal to global positivity outside W2.

Choose H=m=floor(X/2). The guaranteed interval has sufficient length for these two blocks. On a subinterval of at least X/4 positive frequencies around H (for X>=16), the triangular weight is at least 1/2 and p_a>=alpha/2, 1-p_a>=1/2. Thus

    v=sum p_a(1-p_a)w_a^2 >= alpha X/64.

P70.3's symmetrization/fourth-moment argument, applied to the right side Z of (1), gives

    E Z >= v/sqrt(6v+1), Var Z<=1.

For v>=1, Chebyshev therefore yields Z>=sqrt(v)/(2sqrt(7)) except with probability <=28/v. Together with n<=2alpha X (a Chernoff event), this proves

    K_W2 >= sqrt(n)/(16sqrt(14))

with probability tending to one in the E99c regime, plus the explicit interval-filling error above. Constants are deliberately loose. This is a new localization/combination of the existing P28/P70 mechanism, not a new universal independent-rounding theorem.

## 3. Root-difference construction: two steps expose higher moments

Let A be positive differences of r sufficiently dissociated integer points b^j (take b>=11 for the moments below), so

    D_S=Y-r, Y=|sum_{j=1}^r e(b^j x)|^2.

The first-neighborhood central mode gives asymptotic K_W1/r=sqrt(2)-1. For W2, any q(Y/r) of degree <=2 has frequencies in W2. Hence

    K_W2/r >= 1-min_{deg q<=2} E[t |q(t)|^2]/E[|q(t)|^2], t=Y/r.

For fixed moment degree through 5, E[t^j] tends to j! as r grows. The generalized Hankel eigenvalue problem tends to the smallest zero of Laguerre L_3, namely 0.4157745568..., so

    liminf K_W2/r >= 0.5842254432... .

At r=6,10,30,100,1000, the degree-2 moment bounds for K_W2 are respectively 3.96324,6.25624,17.89997,58.78288,584.58101. The corresponding degree-1 bounds are 2.78233,4.40967,12.66940,41.65672,414.44611.

Moments were computed exactly in principle from

    E Y^j = (j!)^2 [z^j] (sum_{a=0}^j z^a/(a!)^2)^r,

then evaluated numerically in a 3-by-3 generalized eigenvalue problem. This is the known P11 higher-moment mechanism localized to W2, not a new theorem about arbitrary supports. It confirms that enlarging the actual row space, unlike repeating the odd-sector matrix, adds genuinely usable directions.

## 4. What this does and does not supply toward universal C*

The concrete E99c obstacle to W1 does not survive W2: both the same-instance tests and a proof establish that. The exact additional ingredient is long-interval filling of A-A, followed by finite-section realization of the full P28 test family.

For arbitrary selected Boolean sets, two separate statements remain unavailable: A-A need not contain a long interval, and even if it does, the weighted Fourier L1 functional in (1) need not be bounded below by a constant times sqrt(n) by the independent-rounding proof. Fractional PD tapers demonstrate why interval filling alone is insufficient; selected/correlated Boolean sets require a different ingredient. Thus no universal two-neighborhood spectral inequality is asserted.
