# Single nonnegative spectral factors: endpoint bounds and a local obstruction

Checkpoint: 2026-10-20T06:12:18.377072+00:00. Ongoing research; no universal Chowla/C* or W2 constant is established. [Reproduction index](../experiments/cstar_structural_2026-10-20/README.md).

2026-10-20. Status: restricted exact results, no universal Chowla proof or counterexample.

## Scope and prior repository work

Let q be a finitely supported nonnegative real sequence on Z. For every t>0 assume c_t=sum_j q_j q_{j+t} belongs to {0,1}. Write B=supp(q), m=|B|, n=number of positive lags with c_t=1, N=2n, and K=sum q_j^2. Then (sum q_j)^2=K+N. The desired positive-single-factor assertion is N<=C K^2. A sufficient, stronger assertion is K>=c m, since N<=m(m-1).

P76 already poses CP-Chowla for sums of nonnegative-factor squares and proves its clique bound and extreme-lag restrictions. E111 treats flat and two-level positive blocks computationally, not the single-factor theorem. The calculations below do not solve that existing open problem.

## Endpoint restriction

Translate and trim the support so its endpoints are 0,L. Put a=q_0, d=q_L. Then ad=c_L=1. Every interior q_j satisfies both a q_j<=1 and d q_j<=1, hence q_j<=min(a,d)<=1. Let E=sum_{0<j<L}q_j^2 and t=a^2+d^2, so K=t+E and t>=2.

For 1<=s<L decompose c_s=e_s+r_s, where e_s=a q_s+d q_{L-s} is the endpoint contribution and r_s is the interior-interior correlation. Cauchy-Schwarz gives 0<=r_s<=E. If E<1, every active lag s<L therefore has e_s>=1-E. On the other hand,

sum_{s=1}^{L-1} e_s^2 <= (a+d)^2 E.

Consequently the exact inequality is

(n-1)(1-E)^2 <= (a+d)^2 E, provided E<1.

In particular, for 2<=K<3,

n <= 1 + (K+2)(K-2)/(3-K)^2.

This is a uniform finite bound near the minimum possible energy K=2, but its denominator degenerates at K=3. It supplies no large-K theorem.

## Small-support classification

For two support points, ad=1 gives K>=2. For three points in non-arithmetic-progression position, all three positive differences are distinct, so every pair product is1 and every coefficient is1: K=3, N=6.

For three points in arithmetic progression, q=(a,b,d), ad=1, b(a+d)=1. Setting u=a+d>=2 gives K=u^2-2+u^(-2)>=9/4, with equality q=(1,1/2,1), N=4. In particular the integer-coefficient bound N<=K^2-K does NOT extend to real coefficients: 4>45/16.

If there are at least four support points, consider the largest difference below L. If the endpoint gaps agree, it has precisely the two endpoint representations, involving distinct interior coefficients. Thus 1<=sqrt(t E) and K>=t+1/t>=5/2. If the endpoint gaps differ, it has one representation; the repeated endpoint reciprocal gives K>=2sqrt(2)>5/2. These are only small-energy restrictions.

## Explicit obstruction to using only outer-lag equations

Let a_j=binom(2j,j)/4^j for j>=0. Since sum a_j z^j=(1-z)^(-1/2),

sum_{i=0}^r a_i a_{r-i}=1 for every r>=0.

Fix m and L>3m. Define q_j=a_j and q_{L-j}=a_j for 0<=j<=m, and set the remaining coefficients to zero. The supports at the two ends are disjoint. For every r=0,...,m, the outer-lag correlation is exactly

c_{L-r}=sum_{i=0}^r a_i a_{r-i}=1.

Yet K=2 sum_{j=0}^m a_j^2=(2/pi)log m+O(1), while the support size is 2m+2 and there are m+1 exact outer unit correlations. Thus arbitrarily many extreme-lag equalities, positivity, and endpoint product1 alone cannot imply either K>=c m or a square-root bound in the number of those lags. Remaining correlations are generally fractional, so this is NOT a valid factor for the original Boolean problem. The missing ingredient must use those other exact 0/1 conditions, not merely improve extreme-lag multiplicity counting.

## Bounded nonlinear search

positive_factor_search.py enumerated all endpoint-anchored supports of diameters2 through9, 510 supports total. For each support it used nonnegative least squares with small energy regularization, then unregularized polishing. This is local optimization, not an exhaustive feasibility or global-minimum proof. It found 100 solutions satisfying residual<1e-7 and all coefficients>1e-6.

Smallest observed K/m was about .5412687664 on the full support [0,7], with K=4.3301501308 and residual3.87e-12. One coefficient was about1.11e-6, so even this finite support count is sensitive to the positivity threshold. No m/K counterfamily was found. The earlier full support [0,5] example had K=3.4575364830 and a coefficient .0184430780. These examples caution against coefficientwise lower bounds but do not support a theorem by themselves. Raw data are in positive_factor_search.json.

## Outcome

The actual new usable bound is the endpoint-energy inequality for E<1, with exact low-support consequences. The central-binomial two-end construction is a quantitative countercontrol against an endpoint-only extension. The proposed uniform linear support-energy inequality remains unproved and unfalsified here; it requires genuinely global Boolean autocorrelation rigidity.
