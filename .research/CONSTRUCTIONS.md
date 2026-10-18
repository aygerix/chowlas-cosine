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

## Status of the Bu family after P16 (2026-10-18)
Bu et al. (2610.17160): A(S) = {3|s−t|} ∪ {|3(s+t)+1|}, S Sidon, N = k(k−1), R -> 1/2 from above (excess ≈ 1.0–1.4√k in
our reproductions). P15: f_{A(S)} = P^2 − k/2 − C/2 with P(x) = C(x/2), C = Σcos((6s+1)x). P16: R(A(S)) >= 1/2 − O((L/k^3)^{1/6})
for every Sidon S ⊂ [−L,L], and for all dilate/shift variants A_{q,r}. So the family is EXHAUSTED at constant 1/2: no
choice of Sidon set, dilation or shift helps. Beating 1/2 needs a different algebraic template (not a single real square
minus a concentrated diagonal); unions of several squares need 2-D (or r-D) visits to fail, i.e. lower-flat vectors of
Sidon-type cosine sums — the same missing lemma as SNZ (STATE line 1).
## Dense family status (E14, E16–E18)
Best certified finite R = 0.56481 (N=36). Theory (E16): ρ <= ρ* ≈ 0.7239 for doubly-positive profiles; unless rounding
errors are positively skewed the dense limit is >~ 0.5255. LNS/SA data rise with N past 36.
