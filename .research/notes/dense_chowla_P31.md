# A √n lower bound for dense, dyadic and sparse-front sets in Chowla's cosine problem

**This file:**
- Consolidated, self-contained paper proof (lead, 2026-10-19). It supersedes the scattered P31 / P31-E / P31-C entries
  in PROOFS.md, which keep the history of corrections.
- Status: PAPER PROOF COMPLETE, modulo the classical Fejér–Riesz theorem.
- Lean: the window inequality is kernel-checked CONDITIONALLY on Fejér–Riesz (codex agent, T3). Fejér–Riesz (T1),
  Lemma 2 (T2) and the corollaries (T4) are in progress.
- No outside review (project rule); verification is by kernel check.

**Conventions:**
- A ⊂ Z_{>0} finite and nonempty; n = |A|; X = max A.
- f_A(x) = Σ_{a∈A} cos(ax); M = M(A) = −min_{x∈R} f_A(x) > 0.
- All averages are (1/2π)∫_0^{2π}.

## 1. Statement of results

**Theorem 1 (window inequality).** Let w >= 0 be an integer and L = X + w. Define
- κ(k) = (1 − |k|/(w + 1))₊;
- W = Σ_{k∈Z} κ(k)² = 2(w + 1)/3 + 1/(3(w + 1));
- S_A = Σ_{a∈A} κ(a)².

Let ρ_L be the sharp constant in ‖U‖₄⁴ <= ρ_L(L + 1)‖U‖₂⁴ for analytic polynomials U = Σ_{j=0}^{L} u_j e^{ijx}. Then
    W·(n/2 + M²) <= ρ_L(L + 1)·(M² + S_A/2).                                                     (1)

**Lemma 2 (elementary Nikolskii constant).** For every L >= 0:
    ρ_L <= 0.8110 + 0.2367/(L + 1).

**Theorem 3 (explicit consequences).** Put C_w := 0.811(X + w + 1) + 0.2367. For every integer 0 <= w <= X:
    (a) M² >= (w + 1)·n/(3C_w) − ½·|A ∩ [1, w]|;
    (b) M² >= (w + 1)·(n/(3C_w) − 1/6).

**Corollaries.**
- (C1, C2) VOID. They are true but trivially superseded; kept only for the record.
  - A ⊂ (X/2, X] already has M >= 0.3729·|A| by averaging f_A(θπ/X) over θ ∈ [1, 3/2] (every cos(aθπ/X) < 0).
  - Sets in [Y, KY] have M >= c(K)|A| by linear test measures (EXPERIMENTS E58).
  - The P31 statements M >= 0.370√|A| (dyadic) and M² >= εn/(2.433(1 + ε) + …) (no elements below εX) add nothing.
- (C3) DENSE SETS. If |A| >= δX with δ > 0.4055, then M >= c(δ)√n. Lower bounds for c(δ) (optimal w, checked for
  X ∈ {10³, 10⁵, 10⁷}):

   δ      0.42     0.45     0.50     0.60     0.75     1.00
   c(δ)   0.0111   0.0324   0.0637   0.1140   0.1696   0.2328

- (C4) NON-FRONT-LOADED SETS. If |A ∩ [1, w]| <= (1 − η)·2(w + 1)n/(3C_w) for some w, then M² >= η(w + 1)n/(3C_w).
  With w = εX this gives M >= √(ηε/(2.433(1 + ε)))·√n (1 + o(1)).

**Sharper constants (proved elsewhere in PROOFS.md).**
- Replace Lemma 2 by Beckner's sharp Young inequality via exact sinc interpolation (Lemma P31-N, review agent, lead
  re-checked): ρ_L <= (4/(3√3))(1 + 2/√(L + 1))³.
- This moves the dense threshold to any δ > 2/(3√3) ≈ 0.3849.
- The numerical limit ρ_∞ ≈ 0.687 (E48; not proved) would give 0.344.

## 2. Proof of Theorem 1

1. The Fejér kernel F(x) = Σ_{|k|<=w} κ(k)e^{ikx} = (1/(w + 1))|Σ_{j=0}^{w} e^{ijx}|² is >= 0, has mean 1, and
   (1/2π)∫F² = W.
2. Fix x₀ ∈ R and put h(x) = F(x − x₀)(f_A(x) + M).
   - h >= 0 everywhere, since f_A >= −M.
   - h is a real trigonometric polynomial of degree <= w + X = L.
3. Fejér–Riesz theorem (classical): a nonnegative trigonometric polynomial of degree <= L equals |U(e^{ix})|² for an
   analytic polynomial U of degree <= L. Then
   - (1/2π)∫h² = (1/2π)∫|U|⁴ = ‖u ∗ u‖₂² (Parseval for U²) <= ‖|u| ∗ |u|‖₂² <= ρ_L(L + 1)‖u‖₂⁴;
   - ‖u‖₂² = (1/2π)∫h.
4. Compute (1/2π)∫h. Since (1/2π)∫F(x − x₀)cos(ax)dx = κ(a)cos(ax₀),
       (1/2π)∫h = M + Σ_{a∈A} κ(a)cos(ax₀) =: s(x₀).
   So (1/2π)∫F(x − x₀)²(f_A(x) + M)²dx <= ρ_L(L + 1)s(x₀)² for every x₀.
5. Average over x₀ ∈ [0, 2π). On the left, Fubini and translation invariance give
       W·(1/2π)∫(f_A + M)² = W(n/2 + M²),
   using mean(f_A) = 0 and (1/2π)∫f_A² = n/2. On the right, the cos(ax₀), a ∈ A, are orthogonal with mean square ½
   and mean 0, so
       (1/2π)∫s² = M² + S_A/2. ∎

Remark (correction from the adversarial review). The Nikolskii inequality must be stated for ANALYTIC U. For
two-sided polynomials it fails: U = 1 + 2cos x has ratio 19/9 > 3/2 at L = 1. Fejér–Riesz supplies an analytic U.

## 3. Proof of Lemma 2

Setup:
- Let v >= 0 on {0, …, L}, N = L + 1, Σ v_j² = 1, and c = v ∗ v.
- The supremum over complex u is attained at |u|, so this suffices.
- p_j = v_j², a_j = Σ_{i<=j} p_i (a_{−1} = 0, a_L = 1), w(t) = t(1 − t), φ(t) = 1 − 2w(t) ∈ [½, 1].

(E1) ‖c‖² <= N − 2Σ_{j<L} w(a_j).
- Cauchy–Schwarz on each c_s's own index range gives c_s <= m_s, where m_s = a_s for s <= L and m_s = 1 − a_{s−L−1}
  for s > L.
- Hence ‖c‖² <= Σ_s c_s m_s <= Σ_s m_s Σ_{i+j=s} (v_i² + v_j²)/2 = Σ_i p_i G(i), with G(i) = Σ_{s=i}^{i+L} m_s.
- G(i) = N − D(i), with D(i) = Σ_{s=i}^{L−1}(1 − a_s) + Σ_{t=0}^{i−1} a_t.
- Exchanging sums: Σ_i p_i D(i) = Σ_{s<L}(1 − a_s)a_s + Σ_{t<L} a_t(1 − a_t) = 2Σ_{j<L} w(a_j).

(E2) ‖c‖² <= (max_s c_s)·Σ_s c_s <= 1·(Σ_j v_j)².

Change of variables:
- Let I_j = [a_{j−1}, a_j], of length p_j. Put g = p_j^{−1/2} on I_j when p_j > 0. Then
  ∫_0^1 g dA = Σ v_j and ∫_0^1 g² dA = N₊ := #{j : p_j > 0}.
- Since w(0) = w(1) = 0, Σ_{j<L} w(a_j) = Σ_{j=0}^{L}(w(a_{j−1}) + w(a_j))/2.
- The trapezoid rule is exact up to the second derivative for the quadratic w (w'' = −2):
  ∫_{I_j} w = p_j(w(a_{j−1}) + w(a_j))/2 + p_j³/6.
- Therefore
      E1 := N − 2Σ_{j<L} w(a_j) = ∫_0^1 g²φ dA + (1/3)Σ_j p_j² + Σ_{j: p_j=0} φ(a_j).

Weighted Cauchy–Schwarz:
- For 0 < λ < μ, (∫g)² <= ∫g²(μ − λφ) · J with J = ∫_0^1 dA/(μ − λφ(A)).
- Writing u = A − ½, μ − λφ = c₀ − 2λu² with c₀ = μ − λ/2, and
      J = √(2/(λc₀))·artanh(√(λ/(2c₀))).
- At λ = 0.71, μ = 0.811: c₀ = 0.456, J = 3.4450…, and (1 − λ)J = 0.99905… <= 1.
- For Lean: certify J by a rational upper Riemann sum; the integrand is monotone in |u|.
- Hence (1 − λ)(Σv)² <= ∫g²(μ − λφ).

Combine:
    ‖c‖² <= λE1 + (1 − λ)E2 <= μ∫g² + (λ/3)Σp_j² + λ·#{p_j = 0} <= μN + λ/3,
using Σ p_j² <= 1 and λ <= μ. Dividing by N = L + 1 gives Lemma 2, since λ/3 = 0.23666… <= 0.2367. ∎

Numerical checks (src/scratch/rho_elem.py): 4000 random v including zeros; trapezoid identity to 2·10⁻¹⁴; no violation.
Sharp values (E48): ρ_L = 0.75, 0.714, …, 0.6870 (L = 119), with a dome-shaped extremizer.

## 4. Proof of Theorem 3 and the corollaries

Step 1: rearrange (1).
- Write C = ρ_L(L + 1) <= C_w (Lemma 2, L + 1 = X + w + 1).
- C_w > W for all w >= 0: C_w − W >= 0.144(w + 1) + 0.2367 − 1/(3(w + 1)) > 0.
- (1) holds with C_w in place of C. Rearranging, M²(C_w − W) >= (Wn − C_w S_A)/2.
- If Wn >= C_w S_A, then M² >= (Wn − C_w S_A)/(2C_w) = Wn/(2C_w) − S_A/2. Otherwise the right side is negative and
  the bound is trivial.

Step 2: (a) and (b).
- W >= 2(w + 1)/3 gives Wn/(2C_w) >= (w + 1)n/(3C_w).
- κ(a) < 1 for a >= 1 gives S_A <= |A ∩ [1, w]|. This is (a).
- S_A <= Σ_{k=1}^{w} κ(k)² = w(2w + 1)/(6(w + 1)) <= (w + 1)/3. This is (b).

(C1, C2) [void: superseded by linear bounds]. Derivation via (a): w = ⌊X/2⌋, resp. w = ⌊εX⌋.
Linear replacement for (C1): for t = a/X ∈ (1/2, 1],
    mean_{θ∈[1,3/2]} cos(tθπ) = (2/(tπ))(sin(1.5tπ) − sin(tπ)) <= −0.3729.

(C3) Take n = δX in (b) and optimize w; the table is src/scratch/dense_constants.py.
The bound is positive iff n > C_w/2 ≈ 0.4055(X + w + 1).

(C4) Directly from (a). ∎

## 5. What the method cannot do (recorded so it is not re-attempted)

1. Linearity. After integrating over x₀, (1) involves A only through |A| and Σ_{a∈A} κ(a)², because 1_A² = 1_A.
   - The same holds for every second-moment window argument: general nonnegative windows Φ, PD reweightings, dilated
     windows, low-pass recursions.
   - So these arguments give only PROFILE (linear) constraints.
   - Sets whose weighted density near 0 exceeds about (2/ρ)·(global density) at every scale satisfy all of them.
     This is the escape class.
2. Recursion. Applying (1) to low-passed functions loses a factor 2/(3ρ) per scale.
   - It would force density growth, and so all dense sets, iff the effective Nikolskii constant were < 2/3.
   - Fejér attains 2/3, and a flat front makes the central window exactly Fejér-shaped.
3. L⁴ upgrade. The L⁴ form (constant C₄ = 0.4862) brings in additive energy. It helps only small dense sets
   (EXPERIMENTS E57).
4. Profile-only lower bounds. Every known construction family (Sidon differences, Singer, Bu et al. 2610.17160, SA
   triangle profiles) lies outside the escape class. So (1) alone proves R >= c(profile) > 0 for each such family
   (E55: Bu ≈ 0.06, Singer ≈ 0.14 with the Beckner constant).

## 6. Novelty and dependencies

- Dependencies:
  - Fejér–Riesz (classical).
  - Elementary inequalities.
  - For the sharp constants only: Beckner, Ann. Math. 102 (1975), Thm 3.
- Predecessor framework: Kolountzakis 1996 (Fejér multiplication and Fejér–Riesz; Turán-type bound, PROOFS P29).
- Novelty check (LITERATURE 2026-10-19). No √n bound for dense sets was found. (Dyadic sets are trivial: linear M.) The closest is Sanders'
  polynomial estimate for frequencies O(N), cited in Bedert 2509.05260 and Shankar 2609.05338. Not a thorough survey.
