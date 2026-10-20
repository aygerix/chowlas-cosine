# Balanced layers: an exact finite-r full-W2 certificate

2026-10-20. This is a diagnostic of the explicit weak-W1 family, not a new universal Chowla bound. It proves that this family is not a full-W2 counterfamily, including on the already specified weak-W1 diagonal.

## Theorem

Let S_k in Z^r be the vectors with k coordinates +1 and k coordinates -1, and let N_k=binom(r,k)binom(r-k,k). For every k>=1 and r>=4k^2,

    K_W2(S_k) >= sqrt(N_k)/22.

The base-7 encoding preserves this statement for the corresponding Boolean integer supports.

## 1. Layer containment

Every S_j, 0<=j<=2k, is contained in S_k+S_k when r>=4k. Here S_0={0}.

For a target having j positive and j negative entries, choose a,b<=k with a+b=j. Give a target-positive and b target-negative entries to the first summand, and the remaining target entries to the second. Add k-a new coordinates of the form (+1,-1) to the two summands and k-b of the form (-1,+1). Both summands then have k signs of each type. These auxiliary coordinates cancel. Their number is 2k-j, so the construction needs 2j+(2k-j)=2k+j coordinates, at most 4k.

## 2. Exact two-layer compression

Let D_j=sum_(s in S_j) e(s.x), and psi_j=D_j/sqrt(N_j). Distinct layers are orthogonal, so these are unit orthogonal trial vectors. Choose i+j=k and 2i<k.

The compression of multiplication by D_k on span{psi_i,psi_j}, divided by sqrt(N_k), is

    [[0, a rho], [a rho, h eta]],                       (1)

where

    a=binom(k,i),
    rho^2=binom(r-2i,2j)/binom(r,2j),
    eta=binom(r-2j,k)/sqrt(N_k),

and h will be given explicitly below.

The first diagonal is zero because two S_i vectors cannot have difference in S_k when 2i<k.

For the cross entry, two vectors from S_i and S_j have difference in S_k exactly when their supports are disjoint. The total number of these ordered pairs is

    N_i binom(r-2i,j)binom(r-2i-j,j)
    =binom(k,i)^2 N_k.

After normalization this gives a rho. Equivalently, rho^2 is the probability that a uniformly chosen 2j-element support avoids a fixed 2i-element support.

For the second diagonal, two S_j vectors have difference in S_k exactly when they have no opposite-sign overlap and exactly l=2j-k same-sign overlaps. Thus the degree of this cross-layer difference graph is

    binom(r-2j,k)
    sum_b binom(j,b)binom(j,l-b)binom(k,j-b).

The sum is h, giving the second diagonal in (1).

For r>=4k^2,

    rho^2 = product_(b=0)^(2j-1) (1-2i/(r-b))
           >= 1-4ij/(r-2j+1)
           >= 1-k^2/(r-2k+1)
           >= 1/2.

Also 0<=rho<=1 and 0<=eta<=1, since 2j>k and

    binom(r-2j,k)<=binom(r-k,k)<=sqrt(N_k).

## 3. Odd k

For k=2m+1 choose i=m, j=m+1. Then l=1 and

    a=binom(2m+1,m),
    h=2(m+1)a.

Since a>=m+1,

    a^2/(h+a)=a/(2m+3)>=1/3.

## 4. Even k

For k=2m, m>=1, choose i=m-1, j=m+1. Then l=2. Put B=binom(2m,m). Directly summing the three possibilities b=0,1,2 gives

    a=m B/(m+1),
    h=(2m^2+2m+1)B.

Therefore

    a^2/(h+a)
    =m^2 B/(2m^4+6m^3+7m^2+4m+1)
    >=1/11.

For m=1 the ratio equals 1/11. For m>=2, B>=m^2: start from binom(4,2)=6>=4 and use that consecutive central binomial coefficients grow by at least 3, while (m+1)^2/m^2<=9/4. The denominator divided by m^4 is at most its value at m=2, namely 117/16<11, proving the displayed bound.

## 5. Uniform negative eigenvalue

For b>0,d>=0, the negative eigenvalue magnitude of [[0,b],[b,d]] is

    2b^2/(sqrt(d^2+4b^2)+d) >= b^2/(d+b).

In (1), b=a rho and d=h eta. Using rho^2>=1/2, rho<=1 and eta<=1,

    -lambda_min((1)) >= a^2/[2(h+a)] >= 1/22.

This proves the theorem. It is finite, exact, and uniform in k. In particular the weak-W1 choice r_k=ceil(4F_k^2 k^2) satisfies the hypothesis without any new diagonal selection.

## 6. Relation to the Laguerre limit and exact finite-k diagnostics

For fixed j and r->infinity,

    D_j/(r^j/j!) converges in joint moments to P_j(Y)=(-1)^j L_j(Y),
    Y distributed exponentially with mean 1.

One way to see the normalization is the coefficient generating function

    product_a (1+t z_a/sqrt(r)+u conjugate(z_a)/sqrt(r))
    -> exp(tZ+u conjugate(Z)-tu),

with standard circular complex Gaussian Z. The coefficient of t^j u^j is P_j(|Z|^2)/j!.

The limiting matrix on layers 0,...,2k is the exact integer matrix

    M_ij=integral_0^infinity P_k(y)P_i(y)P_j(y) exp(-y)dy.

Its generating function is

    sum_(k,i,j>=0) M_ij t^k u^i v^j
    =1/(1-tu-tv-uv-2tuv).

Explicitly, sum over nonnegative a,b,c,d satisfying

    a+b+d=k, a+c+d=i, b+c+d=j

of (a+b+c+d)! 2^d/(a!b!c!d!). All entries are integers. The two-layer matrices above are exact principal submatrices of this limit, with rho=eta=1.

The accompanying script laguerre_full_w2_diagnostic.py computes all exact matrices for k=1,...,10 and independently verifies the formula against exact polynomial integration for small indices. Floating-point negative minima are approximately:

    k=1: 0.5842254432
    k=2: 0.6264445030
    k=3: 1.412287126
    k=4: 4.983074037
    k=5: 20.16473565
    k=6: 80.50406914
    k=7: 406.1051860
    k=8: 1873.339173
    k=9: 9705.477852
    k=10: 51350.93177

These approximate eigenvalues are diagnostic only, not the proof or certified enclosures. The exact two-layer bound above supplies the uniform conclusion without relying on their precision.
