# Lean brief: P34 (one-sided Littlewood bound) — complex-coefficient P31 chain

You are the Lean formalization agent for the Chowla cosine project:
/Users/jmercedes/Desktop/Projects/Research/chowla-cosine, Lean project in `lean/`.
- Build locally with `lake build`.
- No `sorry`, no new `axiom`, no `native_decide`, no unchecked external solvers.
- Report `#print axioms` for every headline theorem. Only propext, Classical.choice and Quot.sound are acceptable.
- Write your report to `.research/agents/lean_p34_report.md`, with exact statements, file/line locations, axiom output
  and anything left open.
- Do not modify `.research/*.md` (the lead records results after auditing).
- Do not weaken statements:
  - ∀ x : ℝ must stay ∀ x : ℝ (no grids);
  - arbitrary phases must stay arbitrary;
  - every n >= 1 must be covered, or the excluded range announced explicitly.

## Existing kernel-checked infrastructure (reuse, do not duplicate)
`lean/ChowlaCosine/P31/*.lean`:
- `circleMean`, `weightedCos`, `kappa`, `windowFreq`, `fejerKernel` (nonneg, `fejerKernel_nonneg`), `windowMass`.
- `averaged_window_bound` (Averaging.lean).
- `AnalyticNikolskii L C` (WindowBound.lean:103), discharged by `elementary_analyticNikolskii` with
  C = 0.811(L+1) + 71/300.
- `FejerRiesz L`, proved for all L as `finite_fejerRiesz`.
- `p31_main`, `p31_elementary` and `dense_elementary` (Corollaries.lean) are the 0/1 (`cosSum A`) instances.

## Target statements
Notation:
- T(x) = Σ_{j=1}^n (a_j cos(j x) + c_j sin(j x)), with real a_j, c_j and a_j² + c_j² <= 1.
- E = Σ_j (a_j² + c_j²).
- For w : ℕ: κ_j = max 0 (1 − j/(w+1)), S_w = Σ_{j=1}^w κ_j², W_w = windowMass w (= 1 + 2S_w), L = n + w.
- Phase form: a_j cos(jx) + c_j sin(jx) = r_j cos(jx − θ_j).

**P34-main (window inequality, general coefficients).** If AnalyticNikolskii L C, FejerRiesz L, and ∀ x : ℝ, −M <= T(x),
then
    W_w · (M² + E/2) <= C · (M² + (1/2)·Σ_{j=1}^{min(w,n)} κ_j²(a_j² + c_j²)).
In particular, using a_j² + c_j² <= 1:
    W_w · (M² + E/2) <= C · (M² + S_w/2).
Proof (paper; identical in structure to p31_main):
1. h_{x₀}(x) = fejerKernel w (x − x₀) · (T(x) + M) >= 0 is a real trigonometric polynomial of degree <= L. Use
   FejerRiesz + AnalyticNikolskii (exactly as p31_main does for cosSum).
2. circleMean of h_{x₀} = M + Σ_{j<=w} κ_j (a_j cos(j x₀) + c_j sin(j x₀)).
   - This is the new orthogonality computation. It needs the sine terms: circleMean of cos(k(x − x₀))·sin(jx) etc.
   - The x₀-average of its square is M² + ½Σ_{j<=w} κ_j²(a_j² + c_j²).
3. The double average of h² is W_w·(M² + E/2). Use translation invariance of ∫ fejerKernel w (x − x₀)² dx₀ and Parseval
   for T + M (cross terms cos·sin vanish).
4. Average (1) over x₀ via averaged_window_bound.
The existing proof handles real weights b on cosines (`weightedCos`). The work is to add the sine family, or, cleaner,
to work with complex coefficients b_j = a_j − i c_j and T = Σ Re(b_j e^{ijx}). Choose whichever reuses more.

**P34-A (unit amplitudes, every n).** If a_j² + c_j² = 1 for all 1 <= j <= n and ∀ x, −M <= T(x), with n >= 1, then
    √n / 4 <= M.
Paper constants:
- With C = 0.811(L+1) + 71/300 and w = ⌊n/2⌋, the bound tends to 0.2718√n.
- For small n, w = 0 gives M² >= 1/2 (so M >= 1/√2 >= √n/4 for n <= 8).
- Optimizing w (≈ 0.7n) gives 0.282√n. Prove √n/4 with a w of your choice; a better constant is optional.
- Sanity: the trivial C = L + 1 already gives M² >= [n + S_w(n − w − 1)]/(2(n + w − 2S_w)), since W_w = 1 + 2S_w.

**P34-B (±1 Littlewood cosine polynomials).** For ε : ℕ → {−1, 1} and n >= 1:
    ∃ x, Σ_{j=0}^n ε_j cos(j x) <= 1 − √n/4,
and also ∃ x, Σ_{j=0}^n ε_j cos(j x) >= √n/4 − 1 (apply P34-A to −T). The j = 0 term is the constant ε_0.

**P34-C (dense coefficients).** If a_j² + c_j² <= 1 for all j, and E >= (41/100)·n, then M >= √n/1000. This is the
complex analogue of dense_elementary. Reuse its arithmetic.

## Secondary targets (only after P34-main and P34-A are checked)
- P33 ratio lemma: for A ⊂ ℕ_{>0} finite nonempty with min A = m and max A = X, if ∀ x, −M <= cosSum A x, then
  M >= |A|·m/X.
  - Proof via the measure on N-th roots of unity. With N = Y + Z and c = Y/Z, its Fourier coefficients are
    D(b) = (1 + c)(1 − |b̄|/Y)₊ − c, where b̄ is the representative of b mod N in (−N/2, N/2].
  - The lead can supply details on request in the report.
- Dilation pinch: for q >= 1, Σ_{j=0}^{q−1} cosSum A (2πj/q) = q·|A ∩ qℕ|, hence |A ∩ qℕ| >= |A|/q − (1 − 1/q)M.

## Report
List: exact Lean statements, files, axioms, build log location, and any deviation from the statements above.
