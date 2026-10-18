# Conjecture G (run-tops vs K²) in finite abelian groups: report of agent "conjG" (2026-10-18)

Brief: `.research/agents/conjG_brief.md`. **Outcome: Conjecture G is FALSE in finite abelian groups.** There is an
explicit algebraic family with |B_t| = K²(K − 1), proved on paper and verified exactly over all characters (§1). The
exponent 3 is sharp for the class without singleton cosets: for t of order 3 that class satisfies |B_t| ≤ K³ (§2).
Cyclic groups, and above all "Z-like" configurations (t small, A in a short interval), are NOT affected (§3).
Scratch scripts are in the session scratchpad
`/private/tmp/claude-501/-Users-jmercedes-Desktop-Projects-Research-chowla-cosine/fde48ec6-19ca-4821-b9ff-9ab9929dd9e0/scratchpad/`.
The standalone verifier is reproduced in Appendix A because the scratchpad is temporary. All jobs ran through
`src/localrun.sh -m 2`, one at a time, each under 3 minutes.

## Conventions (as in the brief)
- Γ is a finite abelian group and A = −A ⊂ Γ\{0} is a set. F(χ) = Σ_{a∈A} χ(a) is real, and K := −min_χ F(χ).
- B_t = {m ∈ A : m − t ∈ A, m + t ∉ A}.
- ω = e^{2πi/3}, ζ_p = e^{2πi/p}, e_p(x) = ζ_p^x. For a prime-power field, Tr is the absolute trace to F_p and η is the
  quadratic character.
- In Γ = Z_p × H with t = (1,0), A_h ⊂ Z_p is the fibre over h. For p = 3:
  - D = {h : |A_h| = 2} (D-cosets). Each carries exactly one run-top, so |B_t| = |D|.
  - E = {h : |A_h| = 1} (singleton cosets). F = {h : A_h = Z_3} (full cosets).
  - u(h) = Σ_{s∈A_h} ω^s and c(h) = |A_h|.
- Labels: PROVED (complete proof here), NUMERICAL-EXACT (integer spectrum over all characters, computed in floating
  point with |F − round F| < 1e−12 and rounded; for p = 3 and a ≤ 2 also re-done in exact Z[ω] arithmetic),
  NUMERICAL (heuristic search), CONDITIONAL, FAILED, OPEN.

## 0. Results at a glance
1. **Theorem 1 (PROVED; NUMERICAL-EXACT for (p,a) ∈ {(3,1),(3,2),(3,3),(3,4),(5,1),(5,2),(7,1),(11,1),(13,1)}).**
   - Setting: any odd prime p, any a ≥ 1, q = p^a, Γ = F_p × F_q × F_{q²} ≅ F_p^{1+3a}, t = (1,0,0).
   - There is A = −A ⊂ Γ\{0} with min F = −q exactly and |B_t| = (q−1)q².
   - So **|B_t| = K²(K−1)**, i.e. |B_t|/K² = K − 1 → ∞. Conjecture G fails for every constant C.
   - Smallest instances:
     - F_3^4: K = 3, |B_t| = 18, ratio 2.
     - F_3^7: K = 9, |B_t| = 648, ratio 8.
     - F_3^{13}: K = 81, |B_t| = 524880, ratio 80.
     - F_p^4 (p prime): K = p, |B_t| = (p−1)p², ratio p − 1. This is a counterexample in groups of fixed rank 4.
2. **Theorem 2 (PROVED).** Let Γ be any finite abelian group and t ∈ Γ of order 3. Then |D| − |E| ≤ (K + u₀)³ (u₀ is
   defined in §2). Hence **|B_t| ≤ K³ whenever no ⟨t⟩-coset meets A in exactly one point**. Theorem 1 (p = 3) attains
   this up to the factor 1 − 1/K.
3. **Lemma 3 + Theorem 4 (PROVED).**
   - Lemma 3: if all cosets over a subgroup V of index m are empty or full, then |D| + |E| ≤ (m−1)K². Theorem 1
     attains equality.
   - Theorem 4: in Z_3 × H with 3 ∤ |H|, equality forces m ≤ 2, so ratio ≤ 1. The extremal mechanism needs 3-torsion
     (p-torsion in general) outside ⟨t⟩.
4. **Proposition 5 (PROVED, restricted class).** In Z_3 × H with |H| odd: if S₀ ∪ {0} is a subgroup
   (S₀ = {h : 0 ∈ A_h}), then |B_t| ≤ 8K² + 3K. So G holds in the class the brief suggested.
5. **Consequences (PROVED / CONDITIONAL, §3).**
   - The route "G in all groups ⇒ Chowla exponent 1/3" is dead.
   - Any group-agnostic statement (Fourier positivity at all characters of an arbitrary finite abelian group, even at
     degree 1) can give at best |B_t| ≲ K³.
   - The group form of P19's Lemma S fails for every δ > 1.
   - K³ in Z would still give exponent 1/4 via Shankar.
   - G in Z itself is untouched. It follows from C½.
6. **Numerics.**
   - Quadric level sets in F_3^n, n ≤ 10, all exact: ratio exactly 1 (anisotropic t) and exactly 2 (isotropic t).
   - Exhaustive all-D search in 20 small groups: ratio < 1.
   - Simulated annealing fails to find any of this structure; the family is a local maximum under fibre moves.
   - So E30's "never above 1/2" was search-limited. The guess "C = 1/2 (Paley)" is refuted.

## 1. The counterexample family

**Theorem 1.**
- Setup:
  - Let p be an odd prime, a ≥ 1, q = p^a, W = F_{q²}, and regard F_q ⊂ W as the subfield.
  - Let G := Σ_{w∈W} e_p(Tr(w²)). Since [W:F_p] = 2a is even, G = −(p*)^a = ±q is real, where p* = (−1)^{(p−1)/2}p.
  - Choose θ ∈ W^* with η(θ)G = −q (θ = 1 if G < 0, a non-square otherwise).
- Let Γ = F_p × F_q × W, t = (1,0,0), and
      A = { (s,r,w) : r ≠ 0, s ≠ τ(r,w) }  ∪  { (s,0,w) : s ∈ F_p, Tr(θw²) ≠ 0 },   τ(r,w) := Tr(w²/(θr)).
- Then:
  - A = −A and 0 ∉ A.
  - F(χ) ≥ −q for every character χ, with equality attained.
  - |B_t| = (q−1)q², and |A| = (p−1)(q³+q).

*Proof.*
- Symmetry. τ(−r,−w) = −τ(r,w), and the second part is invariant under w ↦ −w. At the origin r = 0 and Tr(0) = 0,
  so 0 ∉ A.
- Characters. They are χ_{j,k,c}(s,r,w) = e_p(js + Tr_{q/p}(kr) + Tr(cw)) with j ∈ F_p, k ∈ F_q, c ∈ W.
- Gauss sum. For α ∈ W^*,
      Σ_w e_p(Tr(αw² + cw)) = η(α) G e_p(−Tr(c²/(4α))).
  Proof: complete the square, using Σ_w e_p(Tr(αw²)) = η(α)G.
- Case j ≠ 0.
  - The second part contributes Σ_s e_p(js) = 0. A fibre F_p\{τ} contributes Σ_{s≠τ} e_p(js) = −e_p(jτ). So
        F(j,k,c) = −Σ_{r≠0} e_p(Tr_{q/p}(kr)) Σ_w e_p(Tr(jw²/(θr)) + Tr(cw))
                 = −Σ_{r≠0} e_p(Tr_{q/p}(kr)) η(j/(θr)) G e_p(−Tr(c²θr/(4j))).
  - Every element of F_q^* (in particular j and r) is a square in W, so η(j/(θr)) = η(θ).
  - For r ∈ F_q we have Tr(xr) = Tr_{q/p}(r·Tr_{W/F_q}(x)). Put κ := k − Tr_{W/F_q}(c²θ/(4j)) ∈ F_q. Then
        F(j,k,c) = −η(θ)G Σ_{r∈F_q^*} e_p(Tr_{q/p}(κr)) = q(q·[κ = 0] − 1) ∈ {−q, q(q−1)}.
- Case j = 0.
  - The D-part contributes (p−1)Σ_{r≠0,w} χ = (p−1)q²[c = 0](q[k = 0] − 1). The second part contributes
    p·1̂_{F'}(c), where F' = {w : Tr(θw²) ≠ 0}.
  - Let Z₀ = W\F'. By orthogonality over λ ∈ F_p and the Gauss sum (η(λθ)G = −q):
        1̂_{Z₀}(c) = (1/p)(q²[c = 0] − q(p·[Tr(c²/(4θ)) = 0] − 1)).
  - For c ≠ 0 this gives p·1̂_{F'}(c) = −p·1̂_{Z₀}(c) ∈ {(p−1)q, −q}.
  - For c = 0 and k ≠ 0: |Z₀| = (q² − (p−1)q)/p, so |F'| = (p−1)(q²+q)/p and F(0,k,0) = −(p−1)q² + p|F'| = (p−1)q ≥ 0.
  - So every nontrivial character has F ≥ −q, and the value −q is attained.
- Run-tops. For r ≠ 0 the fibre F_p\{τ} has exactly one run-top m = τ − 1: indeed m−1 = τ−2 ≠ τ because p ≠ 2, and
  m+1 = τ. Fibres over r = 0 are empty or full and contribute none. Hence |B_t| = (q−1)q².
- |A| = (p−1)(q−1)q² + p|F'| = (p−1)(q³+q). ∎

*Spectrum.*
- Nontrivial characters take the values {−q, (p−1)q, q(q−1)}.
- Example: p = 3, a = 2 gives −9 ×1836, 18 ×188, 72 ×162, which matches the computation.

*Verification (NUMERICAL-EXACT).*
- For every listed (p,a), the set was built on F_p^{1+3a} and F was computed at all p^{1+3a} characters by FFT.
  The values were integers to 1e−12, with K = q and |B_t| = (q−1)q² exactly.
- Table:

  | (p, a) | group | K | B_t |
  |---|---|---|---|
  | (3,1) | F_3^4 | 3 | 18 |
  | (3,2) | F_3^7 | 9 | 648 |
  | (3,3) | F_3^10 | 27 | 18954 |
  | (3,4) | F_3^13 | 81 | 524880 |
  | (5,1) | F_5^4 | 5 | 100 |
  | (5,2) | F_5^7 | 25 | 15000 |
  | (7,1) | F_7^4 | 7 | 294 |
  | (11,1) | F_11^4 | 11 | 1210 |
  | (13,1) | F_13^4 | 13 | 2028 |

- For p = 3, a ∈ {1,2} an independent evaluator summed χ over A in exact Z[ω] arithmetic. It confirmed realness and
  min F = −3 and −9.
- Scripts: `fieldfamily.py`, `fieldfamily_p.py`, `conjG_family.py` (Appendix A).

*Explicit smallest set (p = 3, a = 1, isomorphic form).*
- In F_3^4, A = {x : x₁² + x₂² + x₃² + 2x₄² ≠ 0} and t = (1,1,1,0). Note Q(t) = 0, so t is isotropic.
- Exact check: K = 3, |B_t| = 18. The 60 elements are:
  0001 0002 0010 0020 0100 0110 0111 0112 0120 0121 0122 0200 0210 0211 0212 0220 0221 0222 1000 1010 1011 1012 1020
  1021 1022 1100 1101 1102 1111 1112 1121 1122 1200 1201 1202 1211 1212 1221 1222 2000 2010 2011 2012 2020 2021 2022
  2100 2101 2102 2111 2112 2121 2122 2200 2201 2202 2211 2212 2221 2222.

*Mechanism, in slice language.*
- Take H = F_q × W, V = {r = 0} (index m = q), and D = H\V (all D-cosets; E = ∅).
- u = −ω^τ on D. Full cosets lie on part of V and repair the degree-0 slice: 2·1̂_D = −2|V| on V^⊥\1.
- The phase τ(r,w) = Tr(w²/(θr)) is the dual of a vectorial bent map. After summing over w, the phase becomes
  F_p-linear in r. So the j ≠ 0 slice is exactly two-valued: −K, except (m−1)K on a transversal R of V^⊥.
- In this sense the lead's "failed homomorphism construction" is repaired: the D-phases are quadratic and bent
  rather than linear, so D need not be a coset. The degree-0 penalty of D = H\V is paid by full cosets inside V.

## 2. Upper bounds in the same model

**Theorem 2 (PROVED). Let Γ be any finite abelian group and t of order 3 (no splitting assumed).**
- Notation:
  - D and E are the sets of ⟨t⟩-cosets meeting A in exactly 2 and exactly 1 points, so |B_t| = |D|.
  - u₀ = −1 if {t, 2t} ⊂ A, and u₀ = 0 otherwise.
- Claim: |D| − |E| ≤ (K + u₀)³, where D here excludes the coset ⟨t⟩ itself; that coset is accounted for by u₀.
- In particular, if E = ∅ then |B_t| ≤ K³ (≤ (K−1)³ + 1 when u₀ = −1).

*Proof.*
- Set-up:
  - Fix χ₀ with χ₀(t) = ω and put H̄ = Γ/⟨t⟩. For y ∈ H̄ let U(y) = Σ_{x∈A∩y} χ₀(x).
  - For φ ∈ Ĥ̄ = ⟨t⟩^⊥ we have Σ_y U(y)φ(y) = F(χ₀φ) ≥ −K. So U_K := U + Kδ₀ is positive definite on H̄.
- Values of U³:
  - A D-coset with missing point x′ has U = −χ₀(x′) (because 1 + ω + ω² = 0). An E-coset {x} has U = χ₀(x).
  - Hence U³ = ρ·(1_E − 1_D) off the coset y = 0, where ρ := χ₀³ ∈ ⟨t⟩^⊥.
- U_K³ is positive definite (products of positive-definite functions are positive definite), and multiplying by ρ̄
  only translates its transform. So
      0 ≤ Σ_y U_K(y)³ ρ̄(y) = (K + U(0))³ + |E| − |D|,
  with U(0) = u₀. ∎

This extends the lead's |D| ≤ |E| + K³ (split case, u(0) = 0) to all groups. It is **sharp**: Theorem 1 with p = 3
has E = ∅ and |D| = K³ − K².

**Lemma 3 (PROVED; coset-mean bound).**
- Same setting. Suppose every ⟨t⟩-coset lying over a subgroup V̄ ≤ H̄ of index m is empty or full (U ≡ 0 on V̄).
- Then |D| + |E| = Σ_y |U(y)|² ≤ (m−1)K².

*Proof.*
- For each coset C of V̄^⊥, Σ_{φ∈C} Û(φ) = |V̄^⊥| Σ_{y∈V̄} U(y)φ_C(y) = 0.
- Real numbers x_i ≥ −K with Σx_i = 0 over m terms satisfy Σx_i² ≤ m(m−1)K²: put y_i = x_i + K ≥ 0, then
  Σx_i² = Σy_i² − mK² ≤ (Σy_i)² − mK² = m(m−1)K².
- Summing over the |V̄| cosets and applying Parseval gives the bound. ∎
- Theorem 1 attains equality, since m = q = K and |D| = (q−1)q².

**Theorem 4 (PROVED; extremality needs 3-torsion).**
- Let Γ = Z_3 × H with 3 ∤ |H| and t = (1,0). Under the hypothesis of Lemma 3, equality |D| + |E| = (m−1)K² forces
  m ≤ 2, and then |D| ≤ K².

*Proof.*
- Equality forces the shape of Û:
  - Equality forces Û to take the value (m−1)K at exactly one character of each V̄^⊥-coset, and −K at the others.
    So Û = K − mK·1_R with R a transversal.
  - Fourier inversion gives U(y) = −conj(1̂_R(y))/K off V̄, and 0 on V̄ (automatically, because R restricts
    bijectively onto V̄^).
  - |U| = 1 off V̄ together with Parseval gives K² = |V̄|.
- Galois step forces U = ±1:
  - 1̂_R(y) ∈ Q(ζ_e), where e = exp(H) and 3 ∤ e, and U(y) ∈ ±μ₃.
  - Ratios U(y)/U(y′) lie in Q(ζ_e) ∩ μ₆ = {±1}. So U = ε·α with ε = ±1 and α ∈ μ₆ fixed.
  - U(−y) = conj U(y) forces α = ±1. So U is real: every non-empty, non-full coset over H\V̄ is {0} (u = 1) or {1,2}
    (u = −1).
- Contradiction from the degree-0 slice:
  - Then c = (3 − u)/2 on H\V̄, so ĉ = −û/2 + 3·1̂_F off V̄^⊥ (with F ⊂ V̄).
  - At the characters of R outside V̄^⊥ (one restriction to each nontrivial character of V̄), ĉ ≥ −K forces
    1̂_F ≥ (m−3)K/6.
  - Summing 1̂_F over the nontrivial characters of V̄ gives −|F| ≤ 0. This contradicts m > 3. And m = 3 is
    impossible because 3 ∤ |H|. ∎
- Consequence: in a cyclic group Z_{3M} (3 ∤ M) with t = M, Theorem 1's mechanism cannot occur in its exact form.
  Near-extremal versions are not excluded (OPEN).

**Proposition 5 (PROVED; the brief's subclass "S₀ a subgroup").**
- Setting: Γ = Z_3 × H, |H| odd, t = (1,0), slice sets S_i = {h : i ∈ A_h}, a = 1̂_{S₀}, z = 1̂_{S₁}, and S₀ ∪ {0} = V a
  subgroup.
- Claim: |B_t| ≤ 8K² + 3K.

*Proof.*
- F(j,ψ) = a + 2Re(ω^j z) ≥ −K for j = 0,1,2. Some j has cos ≤ −1/2, so |z| ≤ a + K.
- Off V^⊥, a = −1, hence |z| ≤ K − 1. At the trivial character, |S₁| ≤ |V| − 1 + K.
- Let s(y) = |S₁ ∩ (y+V)|/|V|. Parseval off V^⊥ gives Σ_y s(1−s) ≤ (K−1)²/|V| =: ε.
- D-points inside V (h ∈ S₀, exactly one of ±h ∈ S₁) number at most 4|V|s(0)(1−s(0)).
- D-points outside V lie in S₁ ∩ (−S₁), at most Σ_{y≠0} |V| min(s(y), s(−y)).
- If |V| ≥ 4(K−1)² + K, no pair {y, −y} (y ≠ −y because |H| is odd) has s(±y) > 1/2: that would give Σs ≥ 2 − 4ε,
  contradicting Σs ≤ 1 + K/|V|. So min(s(y), s(−y)) ≤ 2[s(1−s)(y) + s(1−s)(−y)] and |D| ≤ 1 + 4|V|ε = 1 + 4(K−1)².
- Otherwise |D| ≤ |V| + |S₁| ≤ 2|V| + K ≤ 8(K−1)² + 3K. ∎

**Symmetric subclass (A_h = −A_h for all h, i.e. u = 1_E − 1_D real; PROVED, partial).**
- Inequalities:
  - Trivial character: |D| ≤ |E| + K.
  - From Σ u_K c_K ≥ 0: 2|D| ≤ |E| + K² + O(K).
  - From Σ u_K c_K² ≥ 0: 4|D| ≤ |E| + O(K³).
- None of these bounds |D| alone, because |E| always enters with coefficient +1.
- This is forced for every "Σ_h of a product of positive-definite atoms" argument: every monomial in u_K, ū_K, c_K
  equals 1 on fibres {0}.
- The best symmetric example found has ratio 1: the anisotropic-t quadric, which is tight in 2|D| ≤ |E| + K².
- Whether G holds in the symmetric subclass is OPEN. It is plausible: the real-phase analogue of Theorem 1 fails
  (see FAILED (c) in §6).

**Barrier for the "reduced" two-face problem (PROVED).**
- Theorem 2's proof only uses that ψ₁ := 1_E − 1_D + K₁δ₀ and ψ₂ := 1_E + 2·1_D + 3·1_F + K₂δ₀ are positive definite
  on H̄ (with K₁ = (K+u₀)³ and K₂ = K), together with their products.
- Example (spread):
  - In F_p^{2d}, take a partial spread of 2r d-subspaces (r ≤ p^d/2). Let E be the union of r of them and D the union of
    r others, minus 0.
  - Then ψ₁ and ψ₂ are positive definite with K₁ = p^d and K₂ = 3r, while |D| = r(p^d − 1) ≈ K₁K₂/3.
  - The products have constant terms ≥ K₁K₂ and are also satisfied.
- So arguments that see only these real-reduced functions cannot beat K₁K₂ = K⁴ (Bedert's exponent).
- Reaching K³ in general (with singleton cosets) must use the phase of U (Û ≥ −K at degree 1). This is the
  finite-group counterpart of P19's message.

## 3. What this does and does not mean for the project
- PROVED:
  - Conjecture G is false for elementary abelian p-groups of rank ≥ 4, for every odd p.
  - So "G in all finite abelian groups ⇒ Chowla exponent 1/3" can never be used.
  - Bedert-type group-agnostic arguments cannot prove better than |B_t| ≍ K³. Fourier positivity at every character,
    even pointwise at degree 1, is satisfied by Theorem 1.
- PROVED, group form of Lemma S fails for δ > 1. In Theorem 1, |1̂_{B_t}| ≤ |B_t| < K³ pointwise, so
  ∫min(|1̂_{B_t}|, K³)² = |B_t| = K³ − K².
- CONDITIONAL / reformulated target:
  - The strongest group-agnostic run-top statement still possible is **G3: |B_t| ≤ C·K³**.
  - If G3 held in Z (or in Z_N for A in a short interval), Shankar's max_t|B_t| ≥ n/(3K) − K/3 would give
    K ≳ n^{1/4}, i.e. Chowla exponent **1/4** (current record 1/5).
- NOT affected:
  - G in Z. It follows from C½ and is therefore still believed.
  - The transfer only ever needed Z_N with |t| < N/4 and A ⊂ [−N/4, N/4], which is essentially Z.
  - In all examples above ord(t) = p ≤ K and Γ has p-rank 1 + 3a ≥ 4.
  - Theorem 4 shows the exact extremal mechanism is impossible in Z_3 × H with 3 ∤ |H|. This includes all cyclic
    Z_{3M} with 3 ∤ M.
  - Cyclic Z_{3^e} with t = 3^{e−1} (non-split t) is not covered by Theorem 4. It is irrelevant to Z because t is
    large.

## 4. Searches (exact search spaces)
1. **Quadric level sets (NUMERICAL-EXACT, `quadrics.py`).**
   - Search space: F_3^n for 2 ≤ n ≤ 10. Forms Q = Σd_i x_i² with d = (1,…,1) and (1,…,1,2). Sets {Q = 1}, {Q = 2},
     {Q ≠ 0}, {Q = 0}\{0}. One t for each value of Q(t) ∈ {0,1,2}.
   - Even n, anisotropic t (Q(t) ≠ 0): |B_t| = K² exactly. Examples: n = 4: (K, |B_t|) = (3, 9); n = 6: (9, 81);
     n = 8: (27, 729).
   - Even n, isotropic t, {Q ≠ 0} with the good sign: |B_t| = 2K² exactly. Examples: n = 4: (3, 18); n = 6: (9, 162);
     n = 8: (27, 1458); n = 10: (81, 13122).
   - Odd n: ratio ≤ 2/3.
   - The isotropic case is the a = 1, p = 3 member of Theorem 1. Lemma 3 with m = 3 shows that 2 is optimal for
     D = complement of an index-3 subgroup.
2. **Exhaustive "all-D" search (NUMERICAL, float K, exhaustive, `alld_exhaust.py`).**
   - Search space: A = {(s,h) : s ≠ τ(h)} in Z_3 × H, over all odd τ : H → Z_3.
   - Groups H ∈ {Z5, Z7, Z3², Z11, Z13, Z17, Z19, Z23, Z5², Z25, Z3×Z9, Z27, Z3³, Z29, Z31}. In every case min K > √|H|
     (best ratio 0.78 at Z31). The Z7² run was stopped as infeasible.
   - Cyclic Z_{3M} with t = M (non-split for 3 | M), exhaustive over symmetric transversals (`cyclic_alld.py`),
     M ∈ {9,15,21,27,33}: best ratio 0.75.
   - Small groups are uninformative here: the first ratio > 1 example needs full cosets.
3. **Fibre-level simulated annealing (NUMERICAL, `fibre_sa.py`).**
   - Moves: replace a fibre pair (A_h, A_{−h}). Exact integer K of the best state is re-checked by FFT.
   - Results:

     | group | K0 | start | best B_t at K ≤ K0 |
     |---|---|---|---|
     | F_3^4 | 3 | empty | 4 |
     | F_3^4 | 3 | Theorem 1 | stays at 18 |
     | F_3^5, F_3^6 | 3 | empty | 4 |
     | F_3^6 | 6 | empty | 15 |
     | F_3^7 | 9 | empty | 7 |
     | F_3^7 | 6 | empty | 5 |
     | F_3^7 | 9 | Theorem 1 | stays at 648 |

   - Unstructured local search is useless for this problem (cf. E30). The algebraic examples are isolated local
     maxima.

## 5. Boundary of the result (quantifiers)
- Theorem 1 gives, for each fixed odd p, an infinite family with K = p^a → ∞ and |B_t| = K²(K−1).
- For fixed rank 4 it also gives an infinite family (p → ∞) with K = p.
- All sets are genuine sets with A = −A and 0 ∉ A. F ≥ −K holds at every character, and B_t is exactly as defined.
- No claim is made about Z, about cyclic groups, or about t of order larger than K.

## 6. FAILED / refuted statements (preserve)
- (a) "Paley is optimal, C = 1/2" (E30, weak evidence): **refuted** by the quadrics (ratio 1 and 2) and by
  Theorem 1 (unbounded ratio).
- (b) Exactly two-valued ĝ for all-D (E = F = ∅, D = H): **impossible**. ĝ is even, so its negative set R is
  symmetric. Then 1̂_R is constant −√n off 0, which forces 1_R to be trivial.
- (c) Real-phase (symmetric-subclass) analogue of Theorem 1 with r ∈ F_2^a and vectorial bent F_2^b → F_2^a (the
  u-part works, ratio (2^a−1)/2): **fails**. c = (3u² − u)/2 couples ĉ to −û/2, which forces 1̂_F ≥ (m−3)K/6 at every
  nontrivial character of V. This is the same contradiction as in Theorem 4.
- (d) Rank-3 attempt (W = F_p, b = 1): the factors η(r) turn the r-sum into a Gauss sum, so F takes values ±p with both
  signs and the ratio is < 1. Rank 4 (b = 2a) is the smallest rank the method reaches.
- (e) τ(r,w) = Tr(β(r)w²) (non-inverted phase) with a ≥ 2 gives Kloosterman-type r-sums, not two-valued, and
  ratio O(1). The inversion w²/β(r) is essential.
- (f) A tensor product of two quadric examples: the trivial-character term of one factor (≈ 3K₁²K₂) destroys K.

## 7. Most promising next lemmas
1. **G3 for t of order 3 in all finite abelian groups.** Remove the singleton hypothesis in Theorem 2: is
   |D| ≤ C K³ even when E ≠ ∅? The barrier of §2 says the proof must use the phase of U (Û ≥ −K at degree 1), not only
   U³ρ̄ and c. Test case: E ⊃ a large subgroup coset structure. A counterexample would have to beat K³ using singleton
   cosets. The exponent window in groups is now [3, 4].
2. **Z-side target (best possible group-agnostically): cubic Lemma S, |B_t| ≤ CK³ in Z.** This gives exponent 1/4.
   - Theorem 2 shows where K³ comes from: the threefold self-convolution of (F + K) on the "ω-slice" {χ : χ(t) = ω},
     plus the identity U³ = ±ρ on 2-point cosets.
   - A Z-analogue needs a substitute for the order-3 fibres (e.g. multipliers supported on χ with e(3tθ) = 1).
     Working this out is the first concrete derivation to try.
3. **Decide G for groups without the Theorem 1 mechanism:** cyclic Z_N, or ord(t) ≫ K. Theorem 4 kills the exact
   mechanism for 3 ∤ |H|. A near-extremal or Bohr-set version is the obvious next construction attempt. A proof
   would need p-rank or interval structure.

## Appendix A. Standalone verifier (`conjG_family.py`; numpy only; `python conjG_family.py p a`)
```python
import sys, itertools
import numpy as np
p, a = int(sys.argv[1]), int(sys.argv[2]); b = 2 * a; Q = p ** b; q = p ** a
def mulmod(x, y, m):                                   # F_p[X]/(m), coefficient lists low->high, m monic deg b
    r = [0] * (2 * b)
    for i, xi in enumerate(x):
        for j, yj in enumerate(y): r[i + j] = (r[i + j] + xi * yj) % p
    for k in range(2 * b - 1, b - 1, -1):
        c = r[k]
        if c:
            for j in range(b + 1): r[k - b + j] = (r[k - b + j] - c * m[j]) % p
    return r[:b]
one = [1] + [0] * (b - 1); X = ([0, 1] + [0] * b)[:b]
for cf in itertools.product(range(p), repeat=b):       # find a primitive polynomial (x has order Q-1)
    m = list(cf) + [1]; cur, k = X, 1
    while cur != one and k < Q: cur, k = mulmod(cur, X, m), k + 1
    if cf[0] and k == Q - 1: break
enc = lambda v: sum(c * p ** i for i, c in enumerate(v))
exp = []; cur = one
for k in range(Q - 1): exp.append(enc(cur)); cur = mulmod(cur, X, m)
exp = np.array(exp); log = np.zeros(Q, int); log[exp] = np.arange(Q - 1)
dig = np.array([[(z // p ** i) % p for i in range(b)] for z in range(Q)])
add = lambda u, v: int(((dig[u] + dig[v]) % p) @ (p ** np.arange(b)))
mul = lambda u, v: 0 if u == 0 or v == 0 else int(exp[(log[u] + log[v]) % (Q - 1)])
inv = lambda u: int(exp[(-log[u]) % (Q - 1)])
def tr(z):
    s, y = 0, z
    for _ in range(b): s, y = add(s, y), (0 if y == 0 else int(exp[(p * log[y]) % (Q - 1)]))
    return s
TR = np.array([tr(z) for z in range(Q)]); SQ = np.array([mul(z, z) for z in range(Q)])
G = round(sum(np.exp(2j * np.pi * TR[SQ[z]] / p) for z in range(Q)).real); assert abs(G) == q
theta = 1 if G < 0 else int(exp[1])                    # exp[1] = x is a non-square
sub = [0] + [int(exp[(k * (q + 1)) % (Q - 1)]) for k in range(q - 1)]   # subfield F_q
basis, span = [], {0}
for z in sub:
    if z not in span and len(basis) < a:
        basis.append(z); span = {add(s0, mul(c, z)) for s0 in span for c in range(p)}
n = 1 + a + b; I = np.zeros((p,) * n, bool)
for rv in itertools.product(range(p), repeat=a):
    rz = 0
    for c, e in zip(rv, basis): rz = add(rz, mul(c, e))
    for wz in range(Q):
        if rz:
            tau = TR[mul(SQ[wz], inv(mul(theta, rz)))]
            for s in range(p):
                if s != tau: I[(s,) + rv + tuple(dig[wz])] = True
        elif TR[mul(theta, SQ[wz])]:
            I[(slice(None),) + rv + tuple(dig[wz])] = True
J = I
for ax in range(n): J = np.take(J, [(-i) % p for i in range(p)], axis=ax)
assert (J == I).all() and not I[(0,) * n]              # A = -A, 0 notin A
F = np.fft.fftn(I.astype(float)).real; F[(0,) * n] = np.inf
K = -F.min(); B = int((I & np.roll(I, 1, 0) & ~np.roll(I, -1, 0)).sum())
print(f"p={p} a={a}: |Gamma|={p ** n} |A|={int(I.sum())} K={K:.9f} (q={q}) |B_t|={B} ((q-1)q^2={(q - 1) * q * q}) "
      f"|B_t|/K^2={B / K ** 2:.4f}")
```

Output of this verifier:

| (p, a) | output |
|---|---|
| (3,1) | K = 3, B_t = 18 |
| (3,2) | K = 9, B_t = 648 |
| (3,3) | K = 27, B_t = 18954 |
| (5,1) | K = 5, B_t = 100 |
| (13,1) | K = 13, B_t = 2028 |

## Novelty
Not checked against the literature. The spectrum {−q, (p−1)q, q(q−1)} suggests a link to strongly regular Cayley
graphs and two-weight codes, which should be searched before any external claim is made.
