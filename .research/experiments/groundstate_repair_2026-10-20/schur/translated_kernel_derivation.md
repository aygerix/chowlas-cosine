# Full-cost translated-ground-state compression

Research note, 2026-10-20. No universal Chowla or full-W2 bound is proved here.

Let S=-S subset Z\{0}, N=|S|, I={0} union S, W2=I+I, D=sum_{s in S} e_s. Let q be a real coefficient unit eigenvector of B_I at eigenvalue -k, k=K_I. Regard q as a Laurent polynomial. Set

    r=(D+k)q, R=||r||_2^2.

The coefficient eigen-equation says r vanishes on I. Thus r lies entirely in the exterior W2\I. In particular <q,r>=0 and R=||C^*q||^2. This is the full exterior leakage, not a selected subset of columns.

For every s in I, e_s q is supported in W2. Write

    Gamma_st = integral |q|^2 e_(s-t),
    E_st = integral (D+k)|q|^2 e_(s-t).

The actual energy matrix of the translated space is E-k Gamma. Gamma is positive definite: multiplication by a nonzero Laurent polynomial is injective on finite Laurent polynomials. Its diagonal is one. E has diagonal zero because q has Rayleigh quotient -k. Consequently

    K_W2 >= k - lambda_min(E,Gamma).

This is an exact admissible subspace of full W2, not an assumption about independent coefficients or a replacement of the exterior matrix by its norm. It remains a restricted test space and cannot be asserted to be universally adequate without proof.

## An exact pair certificate

Let gamma_d=integral |q|^2 e_d and E_d=integral (D+k)|q|^2 e_d. Real coefficients make these real (even if q is not even). Any two distinct translates s,t in I have

    Gram = [[1,gamma_d],[gamma_d,1]],
    defect = [[0,E_d],[E_d,0]],  d=s-t.

Their generalized defect eigenvalues are E_d/(1+gamma_d) and -E_d/(1-gamma_d). Since |gamma_d|<1 for nonzero d,

    K_W2 >= k + |E_d| / (1-sign(E_d)*gamma_d).

The exterior energy is accounted for exactly: both translated ground states have the same energy -k, so their self-defect is zero. This does not mean exterior energy was ignored.

Summing the center-to-neighbor coefficients gives

    sum_(s in S) gamma_s = -k,
    sum_(s in S) E_s = integral D(D+k)|q|^2 = R.

The second equality uses ||Dq||^2=k^2+R. Since every denominator 1-gamma_s is positive, some s satisfies E_s/(1-gamma_s)>=R/(N+k). Therefore

    K_W2 >= k + R/(N+k).

This certificate only closes the desired square-root scale if R is order N^(3/2) when k is small. No such universal leakage estimate has been established. In preliminary taper controls R was merely order N, so the aggregate estimate is not the observed successful mechanism.

## Compare with q,r

The ordinary full-cost two-vector test has matrix

    [[-k, sqrt(R)], [sqrt(R), g]],
    g=<r,D r>/R.

It gives

    K_W2 >= (k-g + sqrt((k+g)^2+4R))/2.

If R is order N and g is at most order sqrt(N), this is enough. This condition is NOT proved for arbitrary supports with k=o(sqrt(N)). Replacing g by a favorable number without controlling it would repeat the previously identified exterior-cost error.

## What remains missing

One needs an order/Boolean statement forcing either a large negative generalized eigenvalue of E relative to Gamma, or cost-weighted leakage on an exterior subspace. The identities above do not supply that statement: a general zero-diagonal matrix can put nearly all its Frobenius energy in positive eigenvalues. Nor does trace(E)=0 enforce balanced signed energy. Any proof based on these identities must exclude that concentration using the simultaneous equations P_I(D+k)q=0 and the exact 0/1 coefficients of D.

The numerical comparison is handled separately in ../obstructions/translated_kernel.py and its results. It tests a proposed estimate, not a substitute for a universal reduction.
