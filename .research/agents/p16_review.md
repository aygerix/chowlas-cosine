# Referee report: P16 (the 1/2 constant is a lower bound for Bu's construction, any Sidon S with L = o(k^3))

Referee: independent adversarial review agent, 2026-10-18. Scope: the statement and proof in .research/PROOFS.md §P16,
and the constants in src/p16_constants.py. I wrote my own code and did not import or rerun the author's scripts.
Status labels follow CLAUDE.md. P16 is **proved on paper and checked by this referee**. It is not kernel-checked, and
nobody outside the project has scrutinised it.

## Overall verdict

**CORRECT.** I found no mathematical gap, no wrong constant and no quantifier error. Every step holds as written. There
are six presentational issues (M1–M6 below), and none of them changes the theorem. The explicit numbers in the statement
(R >= 0.230, 0.376, 0.443, 0.4735 at k = 1e6, 1e8, 1e10, 1e12 with L = k^2/2) reproduce to 4 digits. The asymptotic
constant (author: ~690) recomputes to 686.7.

I also found a strictly stronger variant, P16′ (§4). It replaces the Lipschitz step by the large sieve. That improves
the rate from (L/k^3)^{1/6} to (L/k^3)^{1/5}, and it makes the bound nontrivial from k ≈ 1.3e3 instead of k ≈ 2.9e4
(both at L = k^2/2). P16′ is labelled separately and has not been independently reviewed.

| Step | Verdict | Note |
|---|---|---|
| 0 identity | CORRECT | The "genuine set" hypothesis is automatic: A(S) is genuine iff S is B2 (M2) |
| 1 fourth moment + Chebyshev | CORRECT | Needs full B2, which includes 2s = s'+s''. This is the problem's definition, and Bu's Singer subsets satisfy it. The constant 24π is exact |
| 2 visit lemma | CORRECT | "least h" does not exist (M1). The 4/3 can be 1 (M5). Lindström is applied correctly |
| 3 implication + Lipschitz | CORRECT | — |
| 4 counting | CORRECT | Disjointness, periodicity and the length bound n(2h+2r) <= 2π all check |
| Asymptotics / explicit table | CORRECT | The stated "L <= k^2 (Bu's sets)" is inaccurate: Bu's sets have L ≈ 8–12 k^2, and up to ~32 k^2 in their proof regime (M3) |

## 1. Line-by-line check

**Step 0.** I expanded P^2 = Σ_s cos^2(b_s x) + 2Σ_{s<t} cos(b_s x)cos(b_t x). Two identities are needed:
- 2cos(b_s x)cos(b_t x) = cos((b_s−b_t)x) + cos((b_s+b_t)x), with b_s−b_t = 3(s−t) and b_s+b_t = 3(s+t)+1.
- cos^2(b_s x) = (1+cos((6s+1)x))/2.

Because cos is even, f_{A(S)} = Σ_{s<t}[…] holds exactly when the map from pairs to frequencies is injective and avoids 0.

*Set-ness.* For B2 sets S (all s+t with s <= t distinct):
- The differences 3|s−t| are distinct, because distinct differences are equivalent to B2.
- 3(s+t)+1 = ±(3(s'+t')+1) forces the + sign (since 3∤2), and then s+t = s'+t'.
- The two families differ mod 3, and 3(s+t)+1 ≠ 0.

Conversely, a weak-Sidon set containing a 3-AP repeats a difference: S = {0,1,2} gives 3,6,3. So **A(S) is genuine iff S is B2**,
and the hypothesis "assumed genuine" is equivalent to "S Sidon". Bu et al.'s definition ("every nonzero difference has at
most one ordered representation") is B2.

**Step 1.**
- C = (1/2)Σ_{u∈±T} e^{iux}. The set ±T has 2k distinct elements, since 6s+1 = −(6s'+1) is impossible mod 6.
- Mean of C^4 = 2^{-4}·#{Σu_i = 0}. Write Σu_i = 6Σσ_i s_i + Σσ_i. Since Σσ_i ∈ {0,±2,±4}, only Σσ_i = 0 is possible.
- There are C(4,2) = 6 sign patterns. For each, the equation s_a + s_b = s_c + s_d has, under B2, the solutions {s_c,s_d} = {s_a,s_b}: 2k(k−1) with s_a ≠ s_b and k with s_a = s_b, so 2k^2 − k in total.
- The diagonal case s_a = s_b needs exactly the "2s" part of B2, which the problem statement includes.
- Hence E[C^4] = 6(2k^2−k)/16 = 3k^2/4 − 3k/8. This matches Bu et al.'s M(ρ^4) (their §8).
- Chebyshev on any length-2π interval: |{C <= −τ}| <= 2π E[C^4]/τ^4 < 2π(3k^2/4)·16/(η^4k^4) = 24π/(η^4k^2) at τ = ηk/2. The constant is correct.

**Step 2.**
- The triangle φ = h^{-1}(1−|x−c|/h)_+ is the convolution of two boxes of width h and height h^{-1}. So ∫φ = 1 and ∫cos(bx)φ(x)dx = cos(bc)·sinc^2(bh/2). Both are correct.
- If |P| >= δ on [c−h,c+h], then P has constant sign there by the IVT, and δ <= ∫|P|φ = |∫Pφ| <= Σ_s sinc^2(|b_s|h/2). Correct.
- Counting: the s with |3s+1/2| <= t lie in a real interval of length 2t/3, which holds at most 2t/3 + 1 integers. The author's 2t/3 + 4/3 is a safe over-estimate.
- Lindström (J. Combin. Theory 6 (1969) 211–212) gives F_2(N) < N^{1/2} + N^{1/4} + 1 for B2 subsets of {1..N}. It applies after translation, and the bound is monotone in N.
- Subadditivity of the square root and fourth root then gives α, β, γ. Correct.
- gbar = min(1, 4/(th)^2) >= sinc^2(th/2). It is absolutely continuous and nonincreasing with gbar(∞) = 0. So Σ_s gbar(|b_s|) = ∫_0^∞ N(t)(−gbar'(t))dt exactly, which is Fubini on Σ_s ∫_{|b_s|}^∞.
- Since −gbar' >= 0 is supported on [2/h, ∞) with value 8/(h^2t^3), the bound by U(t) = αt^{1/2}+βt^{1/4}+γ is legitimate.
- I re-derived the closed form, and it matches quadrature to 12 digits (§2).

**Step 3.** Suppose f >= −(1/2−η)k everywhere. At a visit y:
- C(y)/2 = P^2 − k/2 − f(y) < ηk/2 − k/2 + (1/2−η)k = −ηk/2, so C(y) < −ηk.
- |C'| <= Σ|6s+1| <= k(6L+1), so C < −ηk + k(6L+1)r = −ηk/2 on [y−r,y+r].

Correct.

**Step 4.**
- y_j ∈ [c_j−h, c_j+h], so y_{j+1} − y_j >= 2r and the r-neighbourhoods overlap in at most one point.
- Their union lies in [−h−r, c_{n−1}+h+r], which has length n(2h+2r) <= 2π.
- C is 2π-periodic, so Chebyshev applies on a length-2π interval containing the union.
- The contradiction 2rn > 24π/(η^4k^2) is exactly what the statement requires. Even ">=" would suffice, because E[C^4] < 3k^2/4.
- Conclusion: M > (1/2−η)k, and so R = M/sqrt(k(k−1)) > 1/2 − η.

**Asymptotics.**
- h ≈ (1.5396/δ)^2, n ≈ π/h ≈ 0.663ηk, and r/h ≈ η^2k/(57L) ≪ 1 because L >= ~k^2/8 for B2 sets.
- So the condition is ≈ 0.110 η^2 k/L > 75.4/(η^4k^2), that is, k^3 > ~685 L η^{-6}. The fit at k = 1e12 gives 686.7.
- The O-statement needs ηk → ∞. This holds, since ηk ≍ L^{1/6}k^{1/2} >= k^{5/6}.

### Presentational issues (none affects validity)
- **M1.** "h := the least h > 0 with Σbar(h) < δ" is not well defined. Σbar is continuous and decreasing, so the set is the open ray (h*, ∞). Fix: take any h with Σbar(h) < δ, as the author's code does. Alternatively, take h = h* and note that Σ_s sinc^2 < Σbar(h*) strictly, because Lindström's inequality is strict and sinc^2(u) < 1 for u > 0.
- **M2.** The hypothesis "A(S) a genuine set" is redundant. It is equivalent to S being B2 (Step 0). The theorem does need full B2: weak Sidon fails both set-ness and the moment count.
- **M3.** "for L <= k^2 (Bu's dense Sidon sets)" is wrong as a description of Bu's family:
  - In examples/bu_reproduction_certified.json, L/k^2 = 11.1, 8.0, 10.9, 11.7, 11.9.
  - Bu's proof regime q <= 8k gives L ≈ v/2 <= ~32k^2.
  - The rate O(k^{-1/6}) still holds with L = O(k^2), but the explicit table at L = k^2/2 overstates P16 for Bu's actual sets. At L = 12.5k^2: R >= 0.040 (k=1e6), 0.289 (1e8), 0.402 (1e10), 0.455 (1e12).
- **M4.** "Nontrivial only around k >= 1e5": the first k with some η <= 1/2 is k ≈ 2.94e4 at L = k^2/2, and k ≈ 6.15e5 at L = 12.5k^2.
- **M5.** The count bound 2t/3 + 4/3 can be 2t/3 + 1, giving γ = 3 instead of 3.229. This is negligible asymptotically.
- **M6.** Remark (c) ("any half-integer square …") must assume that **all** sign patterns of ±(2b_s) quadruples are trivial: 3+1−, 4+ and 2+2−. In Bu's case the mod-6 argument kills the first two; in general it does not, because a sum of three odd numbers can equal an odd number. Set-ness of the general A must also be assumed.

## 2. Recomputed constants (src/agents/p16_review_constants.py, mpmath at 50 digits; log: .log next to it)

- Σbar: the closed form equals quadrature to 12 digits for h ∈ {1e-1, …, 1e-8}.
- Σbar·√h → 1.5396 (16α/(3·2^{3/2})), with γ = 3.22927.

P16 as stated (θ = 1/2, E4 bounded by 3k^2/4). The table gives the guaranteed lower bound on R:

| k | L = k^2/2 | L = 12.5 k^2 | L = 32 k^2 |
|---|---|---|---|
| 1e4 | none | none | none |
| 1e5 | 0.0979 | none | none |
| 1e6 | **0.2302** | 0.0400 | none |
| 1e7 | 0.3178 | 0.1889 | 0.1362 |
| 1e8 | **0.3764** | 0.2889 | 0.2531 |
| 1e10 | **0.4429** | 0.4024 | 0.3858 |
| 1e12 | **0.4735** | 0.4548 | 0.4471 |

The bold entries match the author's claims. I did not reproduce the author's bisection code; the agreement is between two
independent implementations (mine in mpmath, the author's in float with a 1e-9 margin). The condition is monotone in η
(n, r, δ all increase and the right-hand side decreases), so bisection is valid.

## 3. Falsification attempts (src/agents/p16_review_lemmas.py, p16_review_extra.py; logs and JSON alongside)

**Test sets (16).**
- The 5 certified Bu sets (k = 12…80).
- Singer q = 101 and 307, full and centred (L/k^2 = 0.5, densest near 0).
- Singer 101 shifted to [1e5, 1.1e5] (avoids small elements).
- Erdős–Turán p = 211, centred.
- Erdős–Turán 101 dilated ×7.
- Greedy-near-zero B2 sets with k = 80 and 150 (as much low-frequency mass as possible at every scale).
- Mian–Chowla with k = 100 (all positive).
- Lacunary {2^i} and {−2^i} with k = 16 (L/k^2 = 128).

**Results per lemma.**
- **B2 / set-ness:** all 16 sets are B2 and A(S) is genuine.
- **Step 0:** the identity error is at most 2.6e-7 at 400 random x ∈ [−50, 50], against direct cosine sums over up to 94,556 frequencies. This is float64 rounding.
- **Step 1:** two evaluators agree.
  - Exact integer quadruple count: Σ_v r_{±T}(v)^2 = 6(2k^2−k) for **all 16 sets**.
  - Alias-free FFT mean of C^4 (grid > 4·max T): 3k^2/4 − 3k/8 to 4 decimals.
- **Lindström:** brute-force maximal Sidon sizes for m <= 45 agree with the optimal Golomb ruler table (A003022). Over m <= 586, max F(m)/(m^{1/2}+m^{1/4}+1) = 0.931 < 1. For the test sets, max_t N(t)/U(t) = 0.938, reached by Singer 307 near 0.
- **Step 2 bound:** over h ∈ [1e-6, 10], max Σ_s sinc^2(|b_s|h/2)/Σbar(h) = 0.669 (Singer, centred). It is 0.54 for greedy-near-zero and <= 0.18 for the Bu sets.
- **Visit lemma, using the exact sum.** h_ex is the smallest grid h with Σ_s sinc^2 < δ. A grid point counts as a visit if |P| < δ or if P changes sign at the next grid point (IVT). Across all sets and η ∈ {0.1, 0.3, 0.5}, the longest visit-free run is at most 0.40·2h_ex. No violation.
  - **False alarm, resolved.** A first version counted only grid points with |P| < δ. It reported a run of 5.45·2h_ex for Singer-101-shifted-far. The carrier there has frequency ~3.3e5, and its zero crossings with |P| < δ are about 1e-7 wide, narrower than the grid step. With sign-change detection the ratio is 0.34.
  - h_ex for that set is a genuine resonance: all |b_s| ∈ [3e5, 3.3e5], so sinc^2 ≈ 0 simultaneously at h ≈ 2π/b. The visit lemma is still valid there.
- **Σbar slack at small k is huge.** Examples: Bu 401_80 at η = .5 has h_ex = 3.8e-4 against h_bar = 8.6. Singer 307 has h_ex = 6.6e-4 against h_bar = 0.18. The worst-case Lindström density near 0 and the constant γ dominate. This is harmless asymptotically.
- **Steps 3–4, where P16's windows exist (h_bar < π):** in every window, some grid visit had C(y) > −ηk (zero "bad windows"). The measure of {C <= −ηk/2} was at most 0.005 of the Chebyshev bound. As expected at these k, the P16 inequality fails by 2.5–5 orders of magnitude, so the conclusion is not tested here, only the lemmas.
- **Structural fact found while testing:** for every S, P(π) = 0 (cos(3sπ+π/2) = 0) and C(π) = −k. So x = π is **always** a visit with C = −k, a "bad" visit with f(π) = 0. The proof never assumes that all visits are good, so this is consistent.
  - The half-width of {C <= −k/2} at π is 3.4–6.0 times the Lipschitz radius |min C|/(2k(6L+1)).
  - So a local Lipschitz bound alone gains only a constant at the deepest dips and cannot change the exponent. The large sieve does better (§4).
- **Large-sieve sanity:** I chose 2h-separated points greedily at the most negative values of C. Then Σ_j C(y_j)^4 <= 0.27·(4D + π/h)E[C^4], for h ∈ {h_bar, 1/(6L), 10/(6L)}.

## 4. Improvements (REFEREE, labelled separately; proved on paper by the referee, NOT independently reviewed)

**(I1) Free parameter θ.** Take δ^2 = θηk instead of ηk/2.
- Step 3 then gives C(y) < −2(1−θ)ηk.
- In the Lipschitz version, use r = (1−θ)η/(6L+1) and τ = (1−θ)ηk.
- The condition becomes η^6 >~ 10.66 L/(θ(1−θ)^5 k^3). It is optimised at θ = 1/6, which improves the constant 687 by a factor 4.3.
- At L = k^2/2: R >= 0.286 (k=1e6), 0.403 (1e8), 0.479 (1e12).

**(I2) THEOREM P16′ (large sieve replaces Lipschitz + Chebyshev).**

Hypotheses: S is B2, S ⊂ [−L, L], |S| = k, and D := max_s|6s+1| <= 6L+1. Let 0 < η <= 1/2 and 0 < θ < 1, and set δ = sqrt(θηk). Let 0 < h <= π/2 with Σbar(h) < δ, and set m = ⌊π/(2h)⌋.

Claim: if m·(2(1−θ)ηk)^4 >= (4D + π/h)(3k^2/4 − 3k/8), then M(A(S)) > (1/2−η)k.

*Proof.*
1. Suppose instead that f >= −(1/2−η)k everywhere.
2. The windows [4hj−h, 4hj+h] for 0 <= j < m each contain a visit y_j with |P(y_j)| < δ (Step 2).
3. As in Step 3, C(y_j) < −2(1−θ)ηk.
4. The y_j are 2h-separated mod 2π:
   - for i < j, y_j − y_i >= 4h(j−i) − 2h >= 2h;
   - and y_i + 2π − y_j >= 2π − 4h(m−1) − 2h >= 2h, because 4hm <= 2π.
5. F := C^2 = Σ_{|ν|<=2D} a_ν e^{iνx} is a trigonometric polynomial with N = 4D+1 consecutive frequencies, and Σ|a_ν|^2 = E[C^4].
6. The large sieve inequality (Selberg / Montgomery–Vaughan: Σ_r |S(α_r)|^2 <= (N − 1 + δ_0^{-1})Σ|a_n|^2 for δ_0-separated α_r mod 1) applies with δ_0 = h/π. It gives Σ_j C(y_j)^4 <= (4D + π/h)E[C^4].
7. The left side is > m(2(1−θ)ηk)^4, which is a contradiction. ∎

Asymptotically m ≈ 0.663θηk, so the condition is η^5 >~ 18L/(10.6·θ(1−θ)^4 k^3). It is optimised at θ = 1/5, which gives
η ≈ (20.9 L/k^3)^{1/5} (fitted 20.95 at k = 1e12). Hence **R(A(S)) >= 1/2 − O((L/k^3)^{1/5})**, which for Bu's L = O(k^2)
is 1/2 − O(k^{-1/5}). The admissible range of L is still L = o(k^3). The gain is exactly one factor of η: the depth^4 at
the points is used directly, instead of a Lipschitz neighbourhood of width ∝ η. Explicit values:

| k | L = k^2/2 | 12.5 k^2 | 32 k^2 |
|---|---|---|---|
| 1e4 | 0.209 | none | none |
| 1e5 | 0.328 | 0.177 | 0.112 |
| 1e6 | 0.395 | 0.302 | 0.261 |
| 1e8 | 0.459 | 0.423 | 0.407 |
| 1e12 | 0.4936 | 0.4879 | 0.4854 |

At L = k^2/2 the bound is nontrivial from k ≈ 1.3e3.

**(I3) Density form of the visit lemma (proved). Its application to Bu's family is CONDITIONAL.**

Lemma: if N(t) <= ρt + E for all t >= 0 and δ > E, then Σ_s sinc^2(|b_s|h/2) <= ∫N(−gbar') <= 4ρ/h + E. So every closed window of half-length h > 4ρ/(δ−E) contains a visit.

For "spread" S with ρ ≍ k/L and E = O(1), combining this with P16′ makes L cancel. The condition becomes
(δ−E)(1−θ)^4η^4 k >~ 1.9c, where ρ = c·2k/(3L), so η ≍ k^{-1/3} **for every L, including L ≫ k^3**.

For the five Bu sets at η = 1/2, the smallest admissible E with ρ = 2·2k/(3L) is E <= 1.25. The resulting window is
h = 0.0017–0.023, against h_bar = 8.6 or undefined. The Lindström-based P16 window is therefore far from what Bu's
sets actually allow.

Turning this into a theorem for Bu's random thinning needs a uniform w.h.p. bound N(t) <= 2E[N(t)] + O(log k) near 0
(Chernoff plus Singer equidistribution). I have **not** verified that bound. The L = o(k^3) restriction in P16 is an
artefact of using worst-case Lindström density near 0.

## 5. Literature (alphaXiv, 2026-10-18)

I read Bu et al. arXiv:2610.17160v1 §§1–2 and 8–10, which cover the statements, Remarks 8.4–8.5 and Table 1.
- **They do not prove any lower bound of the form M(A(S)) >= (1/2 − o(1))k.**
- Remark 8.5 records only −min f >= k/2 + (1/2)sup{g(x_0): ρ(x_0) = 0}, which is useful only if g >= 0 at some zero of ρ. They write that they expect the k/2 term and the √(k log k) error term to be sharp for their construction, but "We do not prove this."
- Remark 8.4 names a "second route" below 1/2: the correction is negative by a fixed proportion of λ at every zero of P. P16 rules out exactly this route for the identity of their Prop. 2.1, for every B2 S with L = o(k^3).
- Their Prop. 8.2 bounds the *representation constant* λ (= k/2 here), not −min f, so it does not imply P16.

A recency search ("Chowla cosine problem", "Sidon", "half-constant") returned only 2610.17160, 2609.05338 and
2509.05260. Absence of a hit is not proof of novelty.

## Files
- src/agents/p16_review_constants.py (+ .log): independent mpmath constants for P16 as stated, the θ-optimised Lipschitz version and P16′.
- src/agents/p16_review_lemmas.py (+ .log, .json): Steps 0–4 lemma tests on the 16 sets.
- src/agents/p16_review_extra.py (+ .log): Lindström and OGR check, N(t) bound, large-sieve sanity, Lipschitz slack at x = π, density visit lemma.
