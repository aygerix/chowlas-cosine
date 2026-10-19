# P34 — One-sided Littlewood bound: −min Σ cos(jt − θ_j) ≥ c√n (lead, 2026-10-19)

Status: PROVED on paper (lead). The proof is the P31 chain with general coefficients.
- The 0/1 instance of that chain (`p31_elementary`, `dense_elementary`) is KERNEL-CHECKED (CERTIFICATES 2026-10-19).
- The complex-coefficient generalization below is NOT yet formalized. It is the next Lean task.
- Numerically consistent (E61): adversarially optimized phases give −min T ≈ 0.61√n; ±1 signs give ≥ 0.73√n.

## Statement
Let n ≥ 1, b_1, …, b_n ∈ ℂ with |b_j| ≤ 1, E := Σ_j |b_j|², and

    T(x) = Σ_{j=1}^n Re(b_j e^{ijx}),   x ∈ ℝ.

Suppose T(x) ≥ −M for every real x (M ≥ 0). For an integer 0 ≤ w ≤ n put:
- L = n + w;
- κ_j = 1 − |j|/(w+1);
- S_w = Σ_{j=1}^w κ_j² = w(2w+1)/(6(w+1));
- W_w = Σ_{|k|≤w} κ_k² = 1 + 2S_w.

**Theorem (window inequality).** W_w(M² + E/2) ≤ C_L(M² + S_w/2), where C_L is any constant with the property

    (N_L)   (1/2π)∫h² ≤ C_L·((1/2π)∫h)²   for every nonnegative trigonometric polynomial h of degree ≤ L.

Admissible values:
- C_L = L + 1 (trivial: Fejér–Riesz plus Cauchy–Schwarz);
- C_L = 0.811(L + 1) + 0.2367 (P31-E, kernel-checked: `elementary_analyticNikolskii` together with `finite_fejerRiesz`).

**Corollary A (unit amplitudes, any phases).** If |b_j| = 1 for all j (T(x) = Σ_{j=1}^n cos(jx − θ_j)), then
for every n ≥ 1:

    −min_x T(x) >= 0.189·√n     (trivial C_L),
    −min_x T(x) >= 0.282·√n     (C_L from P31-E; asymptotic value of the optimized bound 0.2820).

The same holds for max_x T(x), by applying the corollary to −T (phases θ_j + π). Asymptotically, the trivial
constant is √(7/2 − 2√3) = 0.18947, attained at w/n → 2√3 − 3.

**Corollary B (Littlewood ±1 cosine polynomials).** For every a_j ∈ {−1, 1}:

    −min_t Σ_{j=0}^n a_j cos(jt) >= 0.282√n − 1,

and the same lower bound holds for the max.

**Corollary C (dense coefficients).** If |b_j| ≤ 1 and E ≥ δn with δ > 0.4055, then −min T ≥ c(δ)√n.
- Large-n constants with P31-E: c(0.5) = 0.048, c(0.6) = 0.096, c(0.75) = 0.168, c(0.9) = 0.237.
- This is the complex-coefficient form of the kernel-checked dense Chowla theorem.

**Sharpness of the order.** Rudin–Shapiro: for n = 2^k there are ε_j = ±1 with |Σ_{j=0}^{n−1} ε_j e^{ijx}| ≤ √(2n).
Hence T(x) = Re(e^{ix}Σε_j e^{ijx}) = Σ_{j=1}^n ε_{j−1}cos(jx) has |T| ≤ √(2n). So −min T ≍ √n is the true order,
with the constant between 0.282 and √2. The best constant found by search is ≈ 0.61 (E61, phases).

**Comparison.**
- Erdélyi, arXiv:2607.21877v1 (24 Jul 2026), claims −min T_n ≥ n^{1/3}/60 and max T_n ≥ n^{1/3}/60 for exactly
  this class. Its Remark 2.3 records only the trivial two-sided bound max(max T, −min T) ≥ (n/4)^{1/2}. Its v1 proof
  has a gap (LITERATURE).
- Its introduction quotes, for ±1 polynomials, maximum bounds of size exp(c√log n) (from [Er11], via Ruzsa).
- Corollaries A and B give the sharp order √n for both one-sided quantities.

## Proof
Put g = T + M >= 0. Let K_w(y) = Σ_{|k|≤w} κ_k e^{iky} >= 0 be the Fejér kernel.

1. For fixed x₀, the function h_{x₀}(x) = K_w(x − x₀)·g(x) is a nonnegative trigonometric polynomial of degree ≤ L.
   By (N_L):
       (1/2π)∫h_{x₀}² dx <= C_L·I(x₀)²,   I(x₀) := (1/2π)∫h_{x₀} dx.
2. Here ĝ(0) = M, ĝ(j) = b_j/2 and ĝ(−j) = b̄_j/2 for 1 <= j <= n. Hence
       I(x₀) = Σ_k κ_k e^{−ikx₀}ĝ(−k) = M + Σ_{j=1}^{w} κ_j Re(b_j e^{ijx₀}).
   By orthogonality (x₀-average, using |b_j| ≤ 1):
       (1/2π)∫I(x₀)² dx₀ = M² + ½Σ_{j≤w} κ_j²|b_j|² <= M² + S_w/2.
3. By Fubini and the translation invariance of ∫K_w(x − x₀)² dx₀ = 2π·W_w (Parseval):
       (1/2π)²∫∫h_{x₀}(x)² dx dx₀ = W_w·(1/2π)∫g² = W_w(M² + E/2).
4. Average step 1 over x₀ and insert steps 2–3: W_w(M² + E/2) <= C_L(M² + S_w/2). ∎

**Trivial (N_L).** By Fejér–Riesz, h = |U|² with U = Σ_{k=0}^{L} u_k e^{ikx}. Then
h(x) <= (Σ|u_k|)² <= (L + 1)Σ|u_k|² = (L + 1)·(1/2π)∫h, so (1/2π)∫h² <= max h·(1/2π)∫h <= (L + 1)((1/2π)∫h)².

**Corollary A from the theorem (trivial C_L = L + 1, E = n).**
- Since W_w = 1 + 2S_w and L + 1 = n + w + 1:
      M²(n + w + 1 − W_w) >= W_w n/2 − (n + w + 1)S_w/2 = n/2 + S_w(n − w − 1)/2,
  so M² >= [n + S_w(n − w − 1)] / (2(n + w − 2S_w)) for every 0 <= w <= n − 1.
- Use w/3 − 1/6 <= S_w <= w/3, the left inequality since the difference is 1/(6(w+1)). With w = ⌊θn⌋ this gives
  M² >= n·θ(1 − θ)/(6 + 2θ) − O(1).
- The maximum is at θ = 2√3 − 3, with value 7/2 − 2√3 = 0.035898. So M² >= 0.035898n − O(1).
- The exact maximum over w is checked for n <= 2000 (src/scratch/littlewood_constant.py; minimum ratio 0.1899 at
  n = 2000, decreasing to 0.18947). The O(1) analysis covers n >= 6000.
- The P31-E constant is handled the same way (ratio 0.2822 at n = 2000, limit 0.2820).

## Why this was not visible from the Chowla side
- P31 needs a non-front-loaded energy profile: the energy in the low frequencies [1, w] must be at most the
  "uniform share". Unit amplitudes on [1, n] have the flattest possible profile.
- So the one-sided Littlewood problem is exactly the δ = 1 (full interval) instance of dense Chowla.
- The window–Nikolskii mechanism cannot see phases: only |b_j|² enters. So it handles arbitrary phases at no cost.

## Open / next
- Lean: generalize `p31_elementary` / `dense_elementary` from `cosSum A` to Σ_j (a_j cos jx + c_j sin jx) with
  a_j² + c_j² <= 1, and prove Corollaries A–C. The existing proof already handles real weights in `weightedCos`.
  The new parts are the sine terms and the averaging identity of step 2.
- Constant: is the sharp constant for unit amplitudes ≈ 0.6 (E61)? An upper construction below √2 (Rudin–Shapiro)
  would need phase design; lower: numerical ρ_∞ = 0.687 gives 0.37.
- Sparse frequencies λ_j: the same chain gives −min Σ A_j cos(λ_j t) >= c(Σ A_j²)^{1/2} whenever the energy profile is
  not front-loaded at some window scale (P31 escape-class criterion). That is Chowla's problem when A_j ∈ {0, 1}.
