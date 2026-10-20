# Independent audit: balanced-layer full-W2 certificate

2026-10-20. Reviewed `translation/balanced_layers_full_w2_certificate.md`.

Verdict: Sections 1–5 prove the exact finite-r theorem as stated. The constant 1/22 is valid for every k>=1 and r>=4k^2. It also gives an unchanged certificate on the implanted supports, providing a rigorous same-family separation between full W2 and bottom-mode repair.

## Counts and normalization

The layer-containment construction balances both summands correctly. It uses 2k+j coordinates for a target in S_j, at most 4k for j<=2k. Therefore all proposed trial layers are actually in W2 under the theorem's hypothesis.

For i+j=k, a difference of an S_i vector and an S_j vector is in S_k precisely when their supports are disjoint. An overlap with opposite signs creates a forbidden digit of magnitude two; any same-sign overlap reduces the difference support below 2k. The disjoint ordered-pair count is both

    N_i binom(r-2i,j) binom(r-2i-j,j)

and

    binom(k,i)^2 N_k.

The normalized cross entry is this count divided by sqrt(N_i N_j N_k). Its square equals a^2 rho^2 because

    N_k/(N_i N_j)
      = rho^2 / binom(k,i)^2.

Thus the report's entry a rho is correct; neither a binomial factor nor a square root is missing.

For the S_j diagonal, no opposite-sign overlap is permitted, and the number of same-sign overlaps must be ell=2j-k. Choose b positive and ell-b negative matches from the fixed vertex; the remaining k positions lie outside its support and carry j-b positive signs. This gives exactly

    binom(r-2j,k) sum_b binom(j,b)binom(j,ell-b)binom(k,j-b),

so the normalized diagonal h eta is correct. The first diagonal is zero since 2i<k.

## Uniform constant

The product estimate for rho gives rho^2>=1/2 when r>=4k^2. The denominator r-2k+1 in the intermediate bound is positive, and k^2/(r-2k+1)<=1/2 even at k=1. Also eta<=1 follows from binom(r-2j,k)<=binom(r-k,k)<=sqrt(N_k).

For odd k, direct substitution gives h=2(m+1)a and a^2/(h+a)>=1/3, including m=0. For even k, the three overlap cases yield h=(2m^2+2m+1) binom(2m,m) and a=m binom(2m,m)/(m+1). The displayed rational expression is correct. At m=1 it equals 1/11; for m>=2, binom(2m,m)>=m^2 and the denominator divided by m^4 is at most 117/16<11. Thus a^2/(h+a)>=1/11 uniformly.

Finally sqrt(d^2+4b^2)<=d+2b for b,d>=0, giving negative eigenvalue magnitude at least b^2/(d+b). Substitution yields a^2/[2(h+a)]>=1/22. Rayleigh–Ritz transfers this to full W2 with the correct inequality direction.

## The implanted supports retain the certificate

Before integer encoding, let S=(T x {0}) union ({0} x U_L), with T a balanced-layer support. Every W2(T) row appears on the x-axis of W2(S). For any trial polynomial F(x) from the two-layer certificate,

    integral_(x,y) (D_T(x)+D_U(y)) |F(x)|^2
      = integral_x D_T(x)|F(x)|^2,

because integral_y D_U(y)=0; its norm is likewise unchanged. Hence

    K_W2(S) >= K_two-layer(T) >= sqrt(|T|)/22.

The carry-free integer encoding preserves this quotient. Along the explicit weak-W1 diagonal, L=O(k(T))=o(sqrt(|T|)), so |S|=|T|+2L is asymptotic to |T|. Consequently the full-W2 certificate is at least (1-o(1))sqrt(|S|)/22, whereas the entire odd W2 sector and all bottom-mode translates have certificate o(sqrt(|S|)). The successful trial vectors are even in the auxiliary coordinate, exactly the sector excluded by the odd-ground-state argument.

## Additional finite checks and scope

Independent enumeration at (r,k)=(4,1),(5,1),(6,2),(7,2),(8,3) verified the exact cross counts, diagonal degrees, and normalized cross formula; outputs are in `full_w2_two_layer_checks.json`. Some enumerations lie below the theorem's r threshold and test only the exact counting identities, not the uniform lower bound.

Section 6's Laguerre asymptotics and floating-point eigenvalues are not needed for this theorem. This is a positive full-W2 result for the explicit obstruction family, not a universal full-W2 bound or a solution to Chowla.
