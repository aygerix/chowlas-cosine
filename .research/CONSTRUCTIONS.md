# Constructions (parametric families)

| family | N | M bound | R limit | status |
|---|---|---|---|---|
| Sidon differences (B Sidon, k) | k(k-1)/2 | k/2 (exact identity) | 1/sqrt2 | proved |
| Bu et al. two-sided Sidon | k(k-1) | k/2 + O(sqrt(k log k)) | 1/2 | cited (asymptotic) |
| A_{k-1} root square, A4={s_i+s_j-s_k-s_l} | ~k^4/8 | ~k^2/4 (completing square) | 1/sqrt2 | derived here, heuristic |
| Wick degree-4, A4={±a_i±a_j±a_k±a_l}=8 e_4(cos a x) | 8C(k,4) | Gaussian heuristic | 0.866 | heuristic |
| Cube framework P7 | sum 2^{|S|-1} | -(1/2) min_eps g_J | R_cube(J) | rigorous template; search EXP-1 |

## Dense near-interval family (2026-10-18; numerical mechanism, no parametric theorem)
A = [1, L] \ H ∪ T: interval with a few holes H and a sparse tail T near t ≈ 2π/x1 (x1 ≈ 4.49/L, first Dirichlet lobe).
Best certified: N=20 (R <= 0.6011), N=34 (R <= 0.6043). R increases with N under SA (0.64 at N=54, 0.69 at N=122);
heuristic explanation (NOTEBOOK 2026-10-18): the positive-definiteness tolerance of the macroscopic profile is ~c/√L,
loose at small L. No infinite family; not a candidate for R -> 0.
