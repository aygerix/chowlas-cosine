# G3 report (agent "g3", 2026-10-18): run-tops vs K³ in finite abelian groups

Brief: `.research/agents/g3_brief.md`. Scripts: `.research/agents/g3_scratch/` (all generators and verifiers; the
essential ones are also reproduced in Appendix A). Compute: the P21 check, the order-4 runs a ≤ 9, the planar runs and
the F_3^4 / F_3^5 ILPs ran on the laptop (`src/localrun.sh -m 2`, one job at a time) before the rule change; everything
after it (P3 check, framework ILPs k = 5, phase-formula check) ran on the VM "dirichlet" via `src/dirun.sh -c 4` (or
`-c 1`). An orphaned VM job (`framework_cap_hi.py 6 27`, output lost in a restart) was killed and not rerun.

Conventions as in the brief: Γ finite abelian, A = −A ⊂ Γ \ {0} a set, F(χ) = Σ_{a∈A} χ(a) (real), K = −min_χ F(χ)
over all characters, B_t = {m ∈ A : m − t ∈ A, m + t ∉ A}. Labels: PROVED (complete proof here), CITED (standard fact,
reference given), NUMERICAL-EXACT (integer spectrum over all characters, two independent evaluators where stated),
NUMERICAL (search), CONDITIONAL, FAILED, OPEN.

## 0. Summary (statements, quantifiers, status)

**Answer to the brief's question: NO.** There is no absolute C with |B_t| ≤ C·K³ for all finite abelian Γ, all
A = −A ⊂ Γ \ {0} and all t. The counterexamples have ord t = 4 and maximal t-runs of length exactly ord(t)/2.

| # | Statement (exact quantifiers) | Status |
|---|---|---|
| 1 | P21 (F_p^4, p odd prime): A = −A, 0 ∉ A, every t-coset has p − 1 points, K = 3p exactly, \|B_t\| = p³. | PROVED (proof in PROOFS.md checked line by line, attainment of −3p added, §1); NUMERICAL-EXACT p = 3, 5, 7, 11, 13 (two evaluators) |
| 2 | **Theorem O4.** For every odd a ≥ 3, Γ = Z_4 × GR(4,a) ≅ Z_4^{a+1}, t = (1,0) (order 4): the explicit set A of §2.2 satisfies A = −A, 0 ∉ A, min over ALL characters of F equals −2^{(a+1)/2}, so K = 2^{(a+1)/2}, and \|B_t\| = 4^a − 2^a = K⁴/4 − K²/2. Hence for every C > 0 there are Γ, A, t with \|B_t\| > C·K³. | PROVED on paper (§2.1–2.2: Lemma T, Lemma S incl. the explicit phase k(y), full spectrum); NUMERICAL-EXACT a = 3, 5, 7 (FFT + exact level counts + direct RDS difference count), FFT a = 9; independently re-verified by the lead (src/e36_o4_check.py, a = 3, 5, 7) |
| 3 | **Prop O4⁺.** Every finite abelian Γ, every t of order 4: 4\|D₂\| ≤ \|E\| + \|D₃\| + (K + u₀)⁴ (cosets ≠ ⟨t⟩ meeting A in a 2-run / 3-run / one point; u₀ ∈ {0, −1}). Theorem O4 attains it up to −K²/2. | PROVED (§2.3) |
| 4 | Consequence: with Bedert's Prop 7.3 (\|B_t\| ≪ K⁴ in every finite abelian group, cited from the brief/P19) the exponent of run-tops over all groups is exactly 4; "G_arc with runs ≤ ord(t)/2" is false. | PROVED given Bedert 7.3 |
| 5 | **Prop P3 (ord t = 3).** In F_3 × F_9 × F_9 an explicit set has K = 3, \|B_t\| = 36 = (4/3)K³, \|E\| = 36. So Theorem 2's bound \|B_t\| ≤ K³ genuinely needs E = ∅, and G3 restricted to ord t = 3 (if true) needs C ≥ 4/3. | PROVED (Gauss sums, §3.1); NUMERICAL-EXACT (two evaluators) |
| 6 | ILP: max \|B_t\| subject to K ≤ 3 is 18 in F_3^4; ≥ 36 in F_3^5 (bound 81 not closed). | NUMERICAL (exact ILP; F_3^5 not closed) |
| 7 | **Prop RDS3**: exact spectrum of the vectorial-bent / relative-difference-set construction for ord 3; weakly regular case ⇔ N̂ ≥ −2 and \|B_t\|/K³ = \|N\|/3^{m/2}. Necessary conditions cap \|N\|/q at 1.11, 1.78, 1.04, 1.26, 1.01 for (k,q) = (3,9), (4,9), (4,27), (5,27), (5,81). | PROVED (formulae); NUMERICAL (caps, exact ILPs) |
| 8 | Lemma DI (p.d. restriction inequality) and its run-top corollary; singleton barrier for every order ℓ with the exact cost of fibre-size weights; ℓ-th power inequalities, sharp for ℓ = 3 (E = ∅) and ℓ = 4. | PROVED (§4) |

What remains OPEN (details §6):
- **G3 in Z** (equivalently, for the transfer, in Z_N with A ⊂ [−X, X], N > 4X + 4|t|). Untouched by O4.
- **Strict G_arc**: |B_t| ≤ C·K³ whenever every maximal t-run has length < ord(t)/2 (the Z_N transfer even gives
  ≤ ord(t)/2 − 1). O4 shows the strictness is necessary.
- G3 in cyclic groups Z_N (any t); G3 for t of large order in any group.
- Side question (no longer affects the group exponent): ord t = 3 with singleton cosets. Window: C ≥ 4/3 (P3) and
  |B_t| ≪ K⁴ (Bedert); |B_t| ≤ |E| + K³ (Theorem 2). Whether |B_t|/K³ is bounded for ord 3 is OPEN.
- Not checked: novelty of O4 in the literature (the relative difference set itself is classical).

## 1. Task (0): adversarial check of P21 — CORRECT

Statement checked: p odd prime, d a non-residue, N(v) = v3² − d v4², Γ = F_p^4, t = e1,
A = {x2 ≠ 0, x1x2 + N(x3,x4) ≠ 0} ∪ {x2 = 0, x1 ≠ x3x4²}.

Line-by-line:
- Symmetry: x1x2 + N is invariant under x ↦ −x (both terms even); x1 − x3x4² changes sign. ✓. 0 ∉ A: x2 = 0 and
  x1 = 0 = x3x4². ✓
- Each line {x + st} with x2 ≠ 0 misses exactly x1 = −N/x2; with x2 = 0 exactly x1 = x3x4². ✓ (Every coset has p − 1
  points; for p = 3 these are 2-point cosets, i.e. D-type; no singleton cosets for p ≥ 5.)
- Run-top count: F_p \ {τ} has the unique top τ − 1 (τ − 2 ≠ τ since p is odd). |B_t| = p³. ✓
- j = 0: every coset has p − 1 points, so F(0,k,c) = (p−1)Σ e_p(kx2 + c·v) = 0 for (k,c) ≠ 0. ✓
- j ≠ 0, x2 ≠ 0 part: with α = −j/x2, Σ_v e_p(αN(v) + c·v) = η(α)η(−αd)g²e_p(−N*(c)/(4α)); η(α)² = 1,
  η(−d)g² = η(−1)η(d)·η(−1)p = η(d)p = −p. So the part equals p(p·[k + N*(c)/(4j) = 0] − 1) ∈ {−p, p(p−1)}. ✓
- x2 = 0 part: −ĝ_j(c), ĝ_j(c) = Σ_{v3,v4} e_p(j v3 v4² + c3v3 + c4v4) = p Σ_{v4 : j v4² = −c3} e_p(c4v4): equal to p
  (c3 = 0), 2p cos(2πc4u/p) (−c3/j = u² ≠ 0) or 0. Real, |ĝ| ≤ 2p. ✓
- Hence F ≥ −3p. The value −3p is attained (j ≠ 0, c4 = 0, −c3/j a nonzero square, k ≠ −N*(c)/(4j)), so K = 3p
  exactly; the PROOFS entry only states the inequality, the attainment is this one line. ✓

Independent verification (`g3_scratch/p21_check.py`): two evaluators, numpy FFT and exact level counts
n_r = #{a ∈ A : ⟨ξ,a⟩ = r} at all p⁴ characters (with n_r = n_{−r} checked, and the minimum certified integral:
n_r constant for r ≠ 0 and n_0 − n_1 = −3p), plus a separate check that the two partial sums of the proof equal their
closed forms at every (j ≠ 0, k, c3, c4):

| p | \|A\| | \|B_t\| | K (FFT) | K (levels) | argmin | decomposition mismatches |
|---|---|---|---|---|---|---|
| 3 | 54 | 27 | 9 | 9 | (1,0,2,0) | 0 |
| 5 | 500 | 125 | 15 | 15 | (1,0,1,0) | 0 |
| 7 | 2058 | 343 | 21 | 21 | (1,0,3,0) | 0 |
| 11 | 13310 | 1331 | 33 | 33 | (1,0,2,0) | 0 |
| 13 | 26364 | 2197 | 39 | 39 | (1,0,1,0) | 0 |

No gap found.

## 2. G3 is false: an order-4 family with |B_t| = K⁴/4 − K²/2

### 2.1 Galois ring facts, Lemma T, Lemma S
Let a ≥ 1, R = GR(4, a) = Z_4[x]/(h(x)) with h a basic primitive polynomial of degree a (Hensel lift of a primitive
f ∈ F_2[x]; h(x²) = (−1)^a f(x)f(−x) mod 4). Standard facts, CITED (Z.-X. Wan, *Lectures on finite fields and Galois
rings*, ch. 14; Hammons–Kumar–Calderbank–Sloane–Solé, IEEE Trans. IT 40 (1994)); all were also checked by machine for
a ≤ 7 (`order4.py`, `o4_phase.py`):
- (G1) R is local with maximal ideal 2R, R/2R ≅ F := F_{2^a}, |R| = 4^a, (R, +) ≅ Z_4^a, R^× = R \ 2R; 2x = 0 iff
  x ∈ 2R.
- (G2) ξ = x mod h has order 2^a − 1. T = {0} ∪ ⟨ξ⟩ maps bijectively onto F under reduction z ↦ z̄; τ(α) ∈ T denotes
  the lift of α. T* = ⟨ξ⟩ is a multiplicative group, so τ(α)τ(β) = τ(αβ). Every z ∈ R is uniquely τ(α) + 2τ(β)
  (because 2z depends only on z̄).
- (G3) The Frobenius σ is the ring automorphism with σ(ξ) = ξ² (so σ(τ(α)) = τ(α²), σ fixes Z_4);
  Tr = Σ_{i<a} σ^i : R → Z_4 is Z_4-linear, Tr(z) mod 2 = tr(z̄) (tr = absolute trace of F), hence
  Tr(2τ(γ)) = 2tr(γ). The form (x, y) ↦ Tr(xy) is nondegenerate (its reduction mod 2 is the nondegenerate trace form
  of F), so λ ↦ (y ↦ i^{Tr(λy)}) is an isomorphism R → R̂ and Σ_{y∈R} i^{Tr(λy)} = 4^a[λ = 0]. Also
  Σ_{z∈2R} i^{Tr(λz)} = Σ_{u∈F} (−1)^{tr(λ̄u)} = 2^a[λ ∈ 2R].

**Lemma T (PROVED).** (i) τ(α) + τ(β) = τ(α + β) + 2τ(√(αβ)) for α, β ∈ F. (ii) Every unit u ∈ R^× is x − x′ with
x, x′ ∈ T in exactly one way, and the only element of 2R that is a difference of two elements of T is 0. So T is a
(2^a, 2^a, 2^a, 1) relative difference set in (R, +) relative to 2R.

*Proof.* (i) Write z = τ(α) + τ(β) = τ(c) + 2τ(d) (G2); reducing mod 2, c = α + β. Since 4 = 0,
z² = τ(c)² + 4τ(c)τ(d) + 4τ(d)² = τ(c²). Also z² = τ(α²) + τ(β²) + 2τ(αβ) = σ(z) + 2τ(αβ), and
σ(z) = τ(c²) + 2τ(d²). Comparing, 2τ(d²) + 2τ(αβ) = 0. As τ(γ) + τ(δ) − τ(γ + δ) ∈ 2R (reduce mod 2), multiplying by 2 gives
2τ(γ) + 2τ(δ) = 2τ(γ + δ), this says 2τ(d² + αβ) = 0, i.e. d² = αβ by (G1); d = √(αβ) (squaring is bijective on F).
(ii) −x′ = 3x′ = x′ + 2x′, so by (i) x − x′ = τ(x̄ + x̄′) + 2τ(√(x̄x̄′)) + 2τ(x̄′) = τ(x̄ + x̄′) + 2τ(√(x̄x̄′) + x̄′).
Let u = τ(ū) + 2τ(ν). If ū = 0 then x̄ = x̄′, so x = x′ and the difference is 0. If ū ≠ 0 we need x̄′ = x̄ + ū and
√(x̄(x̄ + ū)) = ν + x̄ + ū; squaring (a bijection) gives x̄² + x̄ū = ν² + x̄² + ū², i.e. x̄ = (ν² + ū²)/ū, which
determines x̄, x̄′ and hence x, x′ uniquely. ∎

**Lemma S (PROVED, except the value of the sign ε_a, which is NUMERICAL).** For y ∈ R let S(y) = Σ_{x∈T} i^{Tr(xy)}
and Q(z) := Tr(τ(z)) ∈ Z_4 (z ∈ F).
1. S(0) = 2^a, S(y) = 0 for y ∈ 2R \ {0}, S(−y) = conj S(y).
2. Q(z₁ + z₂) = Q(z₁) + Q(z₂) + 2tr(z₁z₂) (mod 4), and Q(z) ≡ tr(z) (mod 2).
3. Every unit is uniquely y = τ(ȳ)(1 + 2τ(β)) with β = β(y) ∈ F, and S(y) = i^{−Q(β(y))}·S(1).
4. S(1)² = 2^a i^a. For odd a: S(1) = ε_a(1 + i)^a with ε_a ∈ {±1}; hence |S(y)|² = 2^a and
   S(y) ∈ 2^{(a−1)/2}(1 + i)μ_4 for every unit y.
5. For odd a, the k(y) ∈ Z_4 with conj S(y) = 2^{(a−1)/2}(1 + i)i^{k(y)} is
   **k(y) = Q(β(y)) − (a + 1)/2 + (1 − ε_a)  (mod 4).**
6. ε_a = +1 for a = 1, 3, 5, 7 (NUMERICAL-EXACT, `o4_phase.py`; the same script checks the formula in 5 at every unit:
   2, 56, 992, 16256 units, 0 mismatches). Theorem O4 does not use the value of ε_a: k(y) is defined intrinsically.

*Proof.* 1. For y = 2u ≠ 0, i^{Tr(2ux)} = (−1)^{tr(ūx̄)} and x̄ runs over F, so S = 0 (ū ≠ 0). S(−y) = conj S(y) is
clear. 2. Apply Tr to Lemma T(i): Q(z₁) + Q(z₂) = Q(z₁ + z₂) + 2tr(√(z₁z₂)) = Q(z₁ + z₂) + 2tr(z₁z₂) (tr is
Frobenius-invariant), and −2 = 2 in Z_4. Q ≡ tr mod 2 by (G3). 3. yτ(ȳ)^{−1} ≡ 1 mod 2R, so it equals 1 + 2w and
2w = 2τ(w̄) (G2). Since x ↦ xτ(ȳ) permutes T (T* is a group), S(y) = S(1 + 2τ(β)) = Σ_{z∈F} i^{Q(z) + 2tr(zβ)}
(Tr(2τ(z)τ(β)) = 2tr(zβ)). By 2., 2tr(zβ) ≡ Q(z + β) − Q(z) − Q(β), so S(y) = i^{−Q(β)} Σ_z i^{Q(z+β)} = i^{−Q(β)}S(1).
4. S(1)² = Σ_{z,u} i^{Q(z) + Q(z+u)} = Σ_{z,u} i^{2Q(z) + Q(u) + 2tr(zu)}; 2Q(z) ≡ 2tr(z) (mod 4) by 2., so
S(1)² = Σ_u i^{Q(u)} Σ_z (−1)^{tr(z(1+u))} = 2^a i^{Q(1)} and Q(1) = Tr(1) = a. For odd a, (1+i)^{2a} = (2i)^a = 2^a i^a,
so S(1) = ±(1+i)^a; then |S(y)|² = 2^a by 3., and (1+i)^a = 2^{(a−1)/2}(1+i)i^{(a−1)/2} gives the phase class.
5. conj S(y) = ε_a i^{Q(β)}(1 − i)^a and (1 − i)^a = (1−i)(−2i)^{(a−1)/2} = 2^{(a−1)/2}(1+i)i^{3}i^{3(a−1)/2}
= 2^{(a−1)/2}(1+i)i^{−(a+1)/2}; ε_a = i^{1−ε_a}. ∎
(Part 4 with 1. gives |S|² ∈ {0, 2^a} off 0 without Lemma T; Lemma T explains it as the relative-difference-set
property and is what the independent difference count in A.2 checks.)
Symmetry check of 5.: −1 = 1 + 2τ(1), so β(−y) = β(y) + 1 and Q(β + 1) = Q(β) + a + 2tr(β); with 2Q(β) ≡ 2tr(β) this
gives k(−y) = −k(y) − 1, as required in the proof of Theorem O4.

### 2.2 The construction
**Theorem O4 (PROVED; NUMERICAL-EXACT for a = 3, 5, 7 with two independent evaluators, FFT-exact for a = 9).**
Let a ≥ 1 be odd, R = GR(4, a), Γ = Z_4 × R, t = (1, 0). For y ∈ R^× define k(y) ∈ Z_4 by
conj S(y) = 2^{(a−1)/2}(1 + i) i^{k(y)} (Lemma S; explicitly k(y) = Tr(τ(β(y))) − (a+1)/2 + (1 − ε_a)
with y = τ(ȳ)(1 + 2τ(β(y))), ε_a = +1 for a ≤ 7). Fix an F_2-hyperplane W̄ ⊂ F_{2^a} and put
F₀ = {2u : ū ∈ W̄ \ {0}} ⊂ 2R \ {0}. Let

  A = {(s, y) : y ∈ R^×, s ∈ {k(y), k(y) + 1}} ∪ (Z_4 × F₀).

Then A = −A, 0 ∉ A, min_χ F(χ) = −max(4, 2^{(a+1)/2}) and |B_t| = 4^a − 2^a. For a ≥ 3:
**K = 2^{(a+1)/2}, |B_t| = K⁴/4 − K²/2, |B_t|/K³ = K/4 − 1/(2K).**

*Proof.*
- Fibres. A_y := {s : (s,y) ∈ A} is the 2-run {k(y), k(y)+1} for y ∈ R^×, Z_4 for y ∈ F₀, ∅ otherwise (in particular
  for y = 0, so 0 ∉ A).
- Symmetry. S(−y) = conj S(y) gives (1+i)i^{k(−y)} = (1−i)i^{−k(y)} = (1+i)i^{−k(y)−1}, so k(−y) = −k(y) − 1 and
  A_{−y} = {−k(y)−1, −k(y)} = −A_y. F₀ ⊂ 2R is symmetric (2R has exponent 2). Hence A = −A.
- Characters: χ_{j,λ}(s, y) = i^{js + Tr(λy)}, j ∈ Z_4, λ ∈ R (G3). With U_j(y) := Σ_{s∈A_y} i^{js},
  F(j, λ) = Σ_y U_j(y) i^{Tr(λy)}. For a 2-run {k, k+1}: U_0 = 2, U_1 = i^k(1 + i), U_2 = (−1)^k(1 − 1) = 0,
  U_3 = conj U_1. For Z_4 and ∅: U_1 = U_2 = U_3 = 0.
- j = 2: U_2 ≡ 0, so F(2, λ) = 0 for every λ (including λ = 0).
- j = 1: U_1(y) = i^{k(y)}(1 + i) = conj S(y)/2^{(a−1)/2} on R^×, 0 on 2R. Using S = 0 on 2R \ {0}, S(0) = 2^a and
  Σ_{y∈R} conj S(y) i^{Tr(λy)} = Σ_{x∈T} Σ_y i^{Tr((λ−x)y)} = 4^a [λ ∈ T],
  F(1, λ) = 2^{−(a−1)/2}(4^a [λ ∈ T] − 2^a) ∈ {−2^{(a+1)/2}, 2^{(a+1)/2}(2^a − 1)}.
  j = 3: F(3, λ) = F(1, −λ) because A = −A; same values.
- j = 0: c(y) := |A_y| = 2 on R^×, 4 on F₀. For λ ≠ 0: Σ_{y∈R^×} i^{Tr(λy)} = −Σ_{z∈2R} i^{Tr(λz)} = −2^a[λ ∈ 2R];
  Σ_{y∈F₀} i^{Tr(λy)} = Σ_{ū∈W̄\0} (−1)^{tr(λ̄ū)} = 2^{a−1}[tr(λ̄ ·) ≡ 0 on W̄] − 1 (= 2^{a−1} − 1 if λ ∈ 2R). So
  λ ∈ 2R \ {0}: F(0, λ) = −2^{a+1} + 4(2^{a−1} − 1) = −4;  λ ∉ 2R: F(0, λ) = 4(2^{a−1}[·] − 1) ∈ {−4, 2^{a+1} − 4}.
- So min F = −max(4, 2^{(a+1)/2}) (both values are attained).
- Run-tops. In the 2-run {k, k+1} the top is k + 1 (k ∈ A_y, k + 2 ∉ A_y); full and empty fibres have none. Hence
  |B_t| = |R^×| = 4^a − 2^a. With K = 2^{(a+1)/2}: K⁴/4 = 4^a, K²/2 = 2^a. ∎

Spectrum with multiplicities (from the proof; W̄^⊥ w.r.t. the trace form of F is one nonzero point, with 2^a lifts in
R^×): on χ(t) = ±i, K(2^a − 1) ×2^{a+1} and −K ×2(4^a − 2^a); on χ(t) = −1, 0 ×4^a; on χ(t) = 1, λ ≠ 0,
2^{a+1} − 4 ×2^a and −4 ×(4^a − 2^a − 1). For a = 3 the values −K and −4 coincide (−4 ×167). These match the table.

Verification (Appendix A.1, A.2):

| a | Γ | \|A\| | K | \|B_t\| | K⁴/4 − K²/2 | \|B_t\|/K³ | spectrum (value: multiplicity) |
|---|---|---|---|---|---|---|---|
| 1 | Z_4² | 4 | 4 | 2 | — | 0.031 | −4:1, −2:4, 0:6, 2:4 |
| 3 | Z_4⁴ | 124 | 4 | 56 | 56 | 0.875 | −4:167, 0:64, 12:8, 28:16 |
| 5 | Z_4⁶ | 2044 | 8 | 992 | 992 | 1.94 | −8:1984, −4:991, 0:1024, 60:32, 248:64 |
| 7 | Z_4⁸ | 32764 | 16 | 16256 | 16256 | 3.97 | −16:32512, −4:16255, 0:16384, 252:128, 2032:256 |
| 9 | Z_4¹⁰ | 524284 | 32 | 261632 | 261632 | 7.98 | −32:523264, −4:261631, 0:262144, 1020:512, 16352:1024 |

For a = 3, 5, 7 a second evaluator (no FFT) checked: (i) W := image of T in coordinates is a relative difference set
(every vector with an odd coordinate is exactly one difference, no nonzero even vector is a difference); (ii) A = −A,
0 ∉ A; (iii) F at every character from exact level counts, F = n_0 − n_2 with n_1 = n_3, integer K; (iv) |B_t| counted
directly. All agree.

### 2.3 The matching order-4 upper bound
**Proposition O4⁺ (PROVED).** Let Γ be any finite abelian group, t of order 4, χ₀ a character with χ₀(t) = i,
ρ = χ₀⁴ (trivial on t), H̄ = Γ/⟨t⟩ and U(y) = Σ_{x∈A∩y} χ₀(x). Let D₂, D₃, E be the numbers of cosets y ≠ ⟨t⟩ whose
intersection with A is a 2-run {x, x+t}, a 3-run {x, x+t, x+2t}, or a single point, and u₀ = U(0) ∈ {0, −1}. Then
  4|D₂| ≤ |E| + |D₃| + (K + u₀)⁴.
*Proof.* Û(φ) = F(χ₀φ) ≥ −K for φ ∈ Ĥ̄, so U + Kδ₀ is positive definite on H̄, hence so is (U + Kδ₀)⁴, and
Σ_y (U + Kδ₀)⁴(y) ρ̄(y) ≥ 0. For y = x₀ + ⟨t⟩ with A ∩ y = x₀ + S·t: U(y)⁴ρ̄(y) = (Σ_{s∈S} i^s)⁴, which is 1 for
S = {k}, (1+i)⁴ = −4 for a 2-run, 1 for a 3-run (Σ = i^k·i), 0 for {k, k+2} and for full/empty. A ∩ ⟨t⟩ is symmetric,
so U(0) ∈ {0, −1} is real and the y = 0 term is (K + u₀)⁴. ∎
Tops per coset: 2-run 1, 3-run 1, others 0 (plus at most 1 from ⟨t⟩ itself). Theorem O4 has E = D₃ = ∅, u₀ = 0 and
|D₂| = K⁴/4 − K²/2: the bound is attained up to the lower-order term.

### 2.4 Meaning and limits
- Quantifiers: for every C > 0 there are Γ, A = −A ⊂ Γ \ {0} (a set), t with |B_t| > C·K³ (take a odd with
  2^{(a+1)/2} > 4C + 1). So **G3 is false**; together with Bedert's Prop 7.3 the group exponent is exactly 4.
- Why ord 4 escapes the cube bound: for ord 3, the D-fibre transform −ω^τ has cube −1, so Theorem 2 caps all-D
  configurations at K³ (sharp by P20/P21). For ord 4 the 2-run transform i^k(1+i) needs the 4th power to lose its
  phase, and the slice χ(t) = −1 vanishes on 2-runs, so no other slice constrains them; the slice χ(t) = 1 sees only the
  constant fibre size 2, repaired by full cosets on a hyperplane of 2R (K-cost 4).
- What it does NOT touch: Z, cyclic groups, t of large order. Runs here have length exactly ord(t)/2; the Z_N transfer
  (A ⊂ [−X, X], N > 4X + 4|t|) has runs ≤ 2X/|t| + 1 < ord(t)/2 − 1. Any proof of G3 (or of any K^{4−δ} bound) in Z must
  use a property violated here: strict shortness of runs relative to ord(t), large order of t, cyclicity, or
  torsion-freeness. The order-4 example is the precise obstruction for all group-agnostic arguments.
- Symmetry forces H̄[2] ⊂ {U = 0} (a fibre over y = −y must be symmetric, but U(y) ∈ (1+i)μ₄ is never real), so the
  2-torsion of the quotient must sit inside the repaired region; Theorem O4 meets this with equality (2R = R[2]).
- Novelty: not checked. The relative difference set is classical (it underlies the quaternary Kerdock codes and the
  "Family A" sequences); its use for Chowla-type run-top counting appears new to this project.

## 3. ord t = 3 with singleton cosets (task 1): OPEN, C ≥ 4/3

Notation (split case Γ = Z_3 × H, t = (1,0), χ₀(s,h) = ω^s): U(h) = Σ_{s∈A_h} ω^s, c(h) = |A_h|; E (U ∈ μ₃, c = 1),
D (U ∈ −μ₃, c = 2), full/empty (U = 0, c ∈ {3, 0}); |B_t| = |D|. Constraints: Û ≥ −K, ĉ ≥ −K off the trivial
character. Known: Theorem 2 (P20) |D| − |E| ≤ (K + u₀)³.

### 3.1 Singleton cosets do push |B_t| above K³
**Proposition P3 (PROVED; NUMERICAL-EXACT, FFT and exact level counts, `p3_check.py`).** Let F_9 = F_3[i], Sq / NSq
the nonzero squares / non-squares, Tr(z) = z + z³. In Γ = F_3 × F_9 × F_9 with t = (1, 0, 0) let
  A = {(s,a,b) : b ∈ Sq, s = Tr(a²/b)} ∪ {(s,a,b) : b ∈ NSq, s ≠ Tr(a²/b)} ∪ {(s,a,0) : a ≠ 0}.
Then A = −A, 0 ∉ A, K = 3, |B_t| = 36 = (4/3)K³, |E| = 36, and the nontrivial spectrum is {−3 (×220), 24 (×22)}.

*Proof.* Symmetry: Tr(a²/b) is odd in (a,b) jointly and Sq, NSq are symmetric; 0 has b = 0, a = 0. Fibres: E over
b ∈ Sq, D (missing τ = Tr(a²/b)) over b ∈ NSq, full over (a ≠ 0, 0), empty over 0; so |B_t| = 9·|NSq| = 36. The
quadratic Gauss sum of F_9 is G = Σ_x ω^{Tr(x²)} = 3, and Σ_x ω^{Tr(γx² + αx)} = η(γ)·3·ω^{−Tr(α²/(4γ))} (4 = 1).
- j ≠ 0 (characters (j, α, β)): the full cosets give Σ_s ω^{js} = 0, and an E-fibre contributes ω^{jτ}, a D-fibre
  −ω^{jτ}, i.e. η(b)ω^{jτ} in both cases. F = Σ_{b≠0} η(b) ω^{Tr(βb)} Σ_a ω^{Tr(ja²/b + αa)} = 3 Σ_{b≠0} η(b)η(j/b)
  ω^{Tr(b(β − α²/j))} = 3(9·[β = α²/j] − 1) ∈ {−3, 24} (η(j) = 1 for j ∈ F_3^*).
- j = 0: for α ≠ 0 the a-sum kills every b ≠ 0 term and the full cosets give 3Σ_{a≠0} ω^{Tr(αa)} = −3. For α = 0,
  β ≠ 0: 9Σ_{b≠0}(1 + 1_{NSq}(b))ω^{Tr(βb)} + 24 = 9(−1 + (−1 − 3η(β))/2) + 24 ∈ {−3, 24}. ∎

General q = 3^e (same formula over F_{q²}): j ≠ 0 still gives {−q, q(q²−1)}, but the j = 0 slice at α = 0 gives
q²(−1 + (−1 − η(β)q)/2) + 3(q² − 1), whose minimum is −q²(q − 3)/2 − 3: K = q only for q = 3 (q = 9: K = 246, see
§5(a)). With b restricted to F_q (all squares in F_{q²}) and the twist θ one recovers P20 Theorem 1 (E = ∅).

### 3.2 Exact ILP in small 3-groups (NUMERICAL)
`ilp_bt.py`: variables x_a (a ∈ Γ\{0}, x_a = x_{−a}) and z_m ≤ x_m, z_m ≤ x_{m−t}, z_m ≤ 1 − x_{m+t}; constraints
Σ_a x_a Re χ(a) ≥ −K₀ for every nontrivial χ (one per pair χ, χ̄); maximise Σ z_m = |B_t|. HiGHS, 4 threads.

| Γ, t | K₀ | status | best \|B_t\| (K of the solution) | dual bound |
|---|---|---|---|---|
| F_3^4, e1 | 2 | optimal | 2 (K = 2) | 2 |
| F_3^4, e1 | 3 | optimal | 18 (K = 3; P20 Thm 1, p = 3) | 18 |
| F_3^5, e1 | 3 | time limit 1500 s | 36 (K = 3; \|A\| = 132, same counts as P3) | 81 |
F_3^6 at K₀ = 4: see §3.3.

### 3.3 Status of the remaining ord-3 computations
- F_3^6 at K₀ = 4 (ILP, 364 binary pair variables): started on the laptop, stopped after 16 min without output when the
  compute rule changed; not rerun, because after Theorem O4 the ord-3 question no longer affects the group exponent
  (coordinator's instruction: no new long computations on it). So there is no data point beyond F_3^5.
- `p3_check.py` (VM): |A| = 132, |B_t| = 36, K = 3 from FFT and from exact level counts (n_1 = n_2 checked at every
  character), spectrum {−3: 220, 24: 22}. This is the explicit-formula version of P3, independent of `planar2.py`
  (which built the same set from Gauss sums, |B_t| = 36, K = 3, spectrum {−3: 220, 24: 22}).
- Evidence summary for ord 3 with singletons: best ratio |B_t|/K³ found anywhere is 4/3 (P3, K = 3). Every structured
  family tried with K → ∞ gives ratio ≤ 1 (P20/P21, E = ∅) or fails the slice χ(t) = 1 (§5(a)–(d)). This is evidence,
  not a proof, that the ord-3 answer may be different from ord 4.

### 3.4 The relative-difference-set mechanism for ord 3 and why it stalls
**Proposition RDS3 (PROVED).** Let m be even, q = 3^{m/2}, β : F_3^m → F_3^k with every component b·β (b ≠ 0) bent.
Then W_{b·β}(a) := Σ_x ω^{b·β(x) + a·x} = ε(a,b)·q·ω^{g(a,b)} with ε = ±1. In Γ = Z_3 × F_3^m × F_3^k (t = e₀) put
U(a,b) = q^{−1} conj W_{b·β}(a) for b ≠ 0 (an E- or D-fibre according to ε = +1 or −1), full fibres over (a, 0), a ≠ 0,
and the empty fibre over 0. Let D = {(a,b) : b ≠ 0, ε(a,b) = −1}. Then |B_t| = |D|,
  F(χ) ∈ {−q, q(3^k − 1)} on χ(t) ∈ {ω, ω²},  F(0, α, β) = 1̂_D(α, β) + 2·3^m[α = 0] − 3 for (α, β) ≠ 0.
So K = q iff 1̂_D(α,β) ≥ 3 − q for α ≠ 0 and 1̂_D(0,β) ≥ 3 − q − 2·3^m for β ≠ 0; then |B_t|/K³ = |D|/q³.
*Proof.* Û(α, β) = q^{−1}Σ_x Σ_a ω^{a(α−x)} Σ_{b≠0} ω^{b·(β − β(x))} = q(3^k[β = β(α)] − 1) (write conj W as a sum over
x). For j = 0: c = 1 + 1_D on {b ≠ 0}, 3 on {b = 0, a ≠ 0}; 1̂_{b≠0}(α,β) = −3^m[α = 0] for (α,β) ≠ 0 and
3·1̂_{a≠0}(α) = 3(3^m[α = 0] − 1). ∎
- Weakly regular case (ε depends on b only, D = F_3^m × N): the conditions become N̂ ≥ −2 on F_3^k \ 0 (integer
  values), and |B_t|/K³ = |N|/q. P3 is m = k = 2, N = NSq(F_9) = two lines, N̂ ∈ {1, −2}.
- Theorem 2 restricted to the subgroups Z_3 × F_3^m × W (W ≤ F_3^k) gives |N ∩ W| − |W \ (N ∪ 0)| ≤ q.
- These two necessary conditions alone already cap the weakly regular framework (exact ILP `framework_cap.py` over
  unions N of lines of F_3^k; NUMERICAL, optimal):

| k | q | max \|N\| | \|N\|/q |
|---|---|---|---|
| 3 | 9 | 10 | 1.11 |
| 4 | 9 | 16 | 1.78 |
| 4 | 27 | 28 | 1.04 |
| 5 | 27 | 34 | 1.26 |
| 5 | 81 | 82 | 1.01 |

  (k = 6, q = 27 — the planar case for m = 6 — was started with the relaxed `framework_cap_hi.py` but the job was
  orphaned by a restart and killed; not rerun.)

  (For k = 3 the value 10 is also forced by hand: N̂ ≥ −2 means every line of PG(2,3) contains ≥ (r − 2)/3 of the r
  points of N, and arcs in PG(2,3) have ≤ 4 points, which leaves r ≤ 5 or r = 13; r = 13 violates the Theorem 2
  constraint.) The known planar functions over F_3 (x², Coulter–Matthews x^{(3^k+1)/2}) are weakly regular; for m = 4
  both give K = 246 (§5(a)).
- CONDITIONAL criterion. If for some m, k > m/2 there is a vectorial bent β : F_3^m → F_3^k whose sign set D satisfies
  the two inequalities of Proposition RDS3 with |D| ≫ q³ — this needs non-weakly-regular components with the
  D-density in each b-class close to 1/2 (the coarse condition) and Fourier-flat sign sets — then G3 fails for ord 3.
  Whether such β exist is OPEN (I know of no planar function over F_3 with non-weakly-regular components).
- Why ord 4 works and ord 3 does not (heuristic diagnosis, consistent with every computation above): in ord 4 the
  2-run class has its own modulus |U| = √2, so the RDS phases select a single top-carrying fibre type and the slice
  χ(t) = 1 sees the constant 2; in ord 3 the E and D classes have the same modulus 1, the Gauss-sum sign decides between
  them, and the slice χ(t) = 1 sees c = 1 + 1_D, i.e. the sign pattern itself. Uniform sign (all-D) is capped by the
  cube (Theorem 2), mixed sign must be Fourier-flat.

## 4. General tools (task 3)

**Lemma DI (PROVED; standard for positive-definite functions).** If f : H → C has f̂ ≥ 0 and V ≤ H, then
Σ_{h∈H} |f(h)|² ≤ [H : V]·Σ_{h∈V} |f(h)|².
*Proof.* For a coset C = φ₀V^⊥ of V^⊥ in Ĥ, Σ_{φ∈C} f̂(φ) = |V^⊥|·(f|_V)^(φ₀|_V) ≥ 0, and for nonnegative reals
Σ x² ≤ (Σ x)². Summing over the |V| cosets and using Parseval on H and on V:
|H|Σ_H|f|² = Σ_φ f̂² ≤ |V^⊥|²Σ_{ψ∈V̂}|(f|_V)^(ψ)|² = |V^⊥|²|V|Σ_V|f|². ∎
**Corollary (PROVED).** ord t = 3, κ := K + u₀: for every subgroup V ≤ H̄,
|D| + |E| + κ² ≤ [H̄ : V](|(D ∪ E) ∩ V \ 0| + κ²), hence (Theorem 2)
|D| ≤ ½([H̄ : V](|(D ∪ E) ∩ V \ 0| + κ²) − κ² + κ³). P20 Lemma 3 is the case (D ∪ E) ∩ V = ∅. So G3-type bounds hold
whenever U almost vanishes on a subgroup of index ≤ K; Theorem O4 and Proposition P3 have the zero region of index
≍ K² and = K², respectively, i.e. this is not the general mechanism.

**Singleton barrier for every order (PROVED).** Let ord t = ℓ, ζ = e^{2πi/ℓ}, Ŝ(j) = Σ_{s∈S} ζ^{js} for a fibre
S ⊂ Z_ℓ. Every inequality obtained as Σ_y (positive combination of products of the positive-definite functions
U_j + Kδ₀ and c + Kδ₀, twisted by the character that removes the coset phase) evaluated at the trivial character has
the form Σ_{y≠0} Φ(S_y) ≥ −Φ₀ with Φ(S) = Σ_J w_J Π_{i} Ŝ(j_i)·P_J(|S|), w_J ≥ 0, Σ_i j_i ≡ 0 (mod ℓ), P_J with
nonnegative coefficients. For a singleton S = {k}: Π_i ζ^{j_i k} = 1, so Φ({k}) = Σ_J w_J P_J(1) > 0. If Φ ≤ −1 on
every top-carrying fibre, then |B_t| ≤ Φ₀ + Φ({·})·#(singleton fibres). Suppressing the singleton weight to ε relative
to the 2-run weight forces deg P_J ≥ log₂(1/ε) (P(1)/P(2) ≥ 2^{−deg P}), and multiplies the y = 0 term by
≥ (K/2)^{log₂(1/ε)}: with μ_k = c_k2^k/P(2) (P = Σ c_k x^k), P(1)/P(2) = E_μ[2^{−k}] ≥ 2^{−E_μ k} and
P(x)/P(2) = E_μ[(x/2)^k] ≥ (x/2)^{E_μ k} for x ≥ 2 (Jensen), so P(1) ≤ εP(2) forces E_μ k ≥ log₂(1/ε).
This is barrier (i) of the conjG report for all ℓ, with the exact price of the c-weights; it applies to the Z-fibre
transform inequality of the brief as well (singleton fibres are t-isolated points of A, which are ≍ |A| in Z).

**ℓ-th power inequalities (PROVED).** For ord t = ℓ and fibre classes S: Σ_{y≠0} Ŝ_y(1)^ℓ ≥ −(K + u₀)^ℓ (u₀ real by
symmetry of A ∩ ⟨t⟩). ℓ = 3 is Theorem 2 (D: −1, E: +1); ℓ = 4 is Proposition O4⁺ (2-run: −4, singleton and 3-run:
+1). Both are sharp: P20/P21 (ℓ = 3, E = ∅) and Theorem O4 (ℓ = 4). For ℓ = 6 the slice j = 2 gives, for 2-runs,
Ŝ(2) = (1 + ω)ω^k ∈ −μ₃, so pure 2-run configurations of order 6 (runs < ℓ/2, the Z-like regime) are capped at K³ by the
cube of that slice (singletons count +1 again).

## 5. FAILED constructions and refuted intermediate claims (preserve)
- (a) Weakly regular planar functions for ord 3, m = 4: x² and Coulter–Matthews x^{14} over F_81 (NUMERICAL-EXACT,
  `planar2.py` with an exact ILP choosing the best full-coset set): D-density per b-class is 0/1, K = 246 (forced by
  the slice χ(t) = 1 at α = 0: 81(1̂_N − 1) + 240 with 1̂_N = −5), |B_t| = 3240, ratio 2·10⁻⁴. Spectrum
  {−246 ×40, −9 ×12960, −3 ×6480, 483 ×40, 720 ×162}.
- (b) Many all-D blocks on a partial spread (to realise conjG's barrier-(ii) configuration with phases): for
  complementary blocks the cylinder sets {φ : φ|_{V_i} ∈ R_i} are exactly independent, and Σ_i 1_{C_i} − r/q has Fourier
  support in ∪_i V_i \ 0, so it cannot be constant; the −K backgrounds add up to ≈ −rK (heuristic count) and the ratio
  drops like 1/r².
- (c) Layering planar maps β_e = λ_e x² over an extra coordinate e ∈ F_3 (to balance the D-density): symmetry forces
  λ₁ = λ₂, and then the χ(t) = ω slice equals −q³ at the common peak. Refuted by direct computation.
- (d) Sign split by a Z₂ coordinate, U(e,h) = (−1)^e W(h): the χ(t) = 1 slice at the character (1, trivial) gives
  |H₀| ≤ 4|V̄| + K, i.e. |B_t| = O(K²). PROVED.
- (e) Order-p (p ≥ 5) analogue of Theorem 1 with 2-runs of a fixed shape: F(j,·) = Î(j)·X(j,·) with
  Î(j) = ±2cos(πj/p) changing sign over j, so some slice carries −Î·q(q−1): K ≍ q². The P21 diagnosis (negative
  definite fibres) is needed for fixed-shape Gauss-sum families; O4 avoids it only because ℓ = 4 has a single
  nontrivial slice pair.
- (f) Ternary Galois-ring analogue for ord 3: the Teichmüller set of GR(9, a) is not a relative difference set
  (a = 1: T = {0, ±1} ⊂ Z_9 and 8 = 0 − 1 = 8 − 0), and for |P| = 3^{odd} the phases are (1 − ω)μ₆ ∉ μ₆.
- (g) Refuted claims: "G3 in every finite abelian group" (Theorem O4); "G_arc with runs ≤ ord(t)/2" (Theorem O4,
  runs = ord(t)/2); "Theorem 2's |B_t| ≤ K³ extends to E ≠ ∅" (Proposition P3); "the group exponent is < 4" (O4);
  "negative-definite fibres are necessary for |B_t| ≫ K³" (P21 diagnosis, refuted by O4's 2-runs, whose transform
  i^k(1+i) is not real).

## 6. Open items and most promising next lemmas
OPEN (none of these is affected by Theorem O4 except as stated):
- **G3 in Z** (and in the Z_N transfer: A ⊂ [−X, X], N > 4X + 4|t|). This is what the Chowla application needs
  (G3 in Z ⇒ exponent 1/4 via Shankar). Its weaker relative "G in Z" follows from C½ and is still believed.
- **Strict G_arc**: is |B_t| ≤ C·K³ whenever every maximal t-run has length < ord(t)/2? O4 has runs = ord(t)/2, so the
  strict inequality is necessary for any such statement.
- **G3 in cyclic groups** (any t), and **G3 for t of large order** in arbitrary groups.
- **ord t = 3 with singleton cosets** (side question): bounded |B_t|/K³? Known window: ≥ 4/3 (P3), ≤ K (Bedert, up to
  constants), and |B_t| ≤ |E| + K³ (Theorem 2).
- The value of ε_a (sign of the Teichmüller Gauss sum) for general odd a (only used for the explicit k(y) formula).
- Novelty of Theorem O4 (not searched).

Next lemmas, in order of value for the project:
1. **Strict arc / Z-side.** First lemma to try: for a fibre shape that is a single run of length L < ℓ/2, find a
   nonnegative combination of slice monomials (frequencies summing to 0 mod ℓ) that is ≤ −1 on L-runs; the ℓ = 6 cube
   (§4) is the model, and the singleton barrier (§4) says singletons must then be handled by a non-product argument.
   First test of the opposite direction: an order-5 analogue of O4 with 2-runs (all slices j = 1..4 must be oriented
   simultaneously; §5(e) shows the Gauss-sum family fails, so a different relative difference set would be needed).
2. **Cyclic groups.** O4 needs a (2^a, 2^a, 2^a, 1) relative difference set with phases in ζ_8^{odd}; decide whether any
   cyclic group admits a near-analogue (t = N/4). A negative answer would isolate cyclicity as a usable hypothesis.
3. **ord 3 (side).** Decide the CONDITIONAL criterion of §3.4 (non-weakly-regular vectorial bent functions over F_3 with
   balanced, Fourier-flat sign sets); prove the structure lemma "N̂ ≥ −2 on F_3^k ⇒ N lies in a union of two
   subspaces", which with Theorem 2 on subspaces would bound the weakly regular framework by ratio 2.

## Appendix A. Code (all files in `.research/agents/g3_scratch/`)

Other scripts there: `p21_check.py` (P21, two evaluators), `ilp_bt.py` (exact run-top ILP), `planar2.py` (power-map
RDS for ord 3 with optimal full-coset repair), `framework_cap.py` / `framework_cap_hi.py` (weakly regular caps),
`o4_phase.py` (explicit k(y) and ε_a), output `o4_phase.txt`.

### A.1 `order4.py` — generator and FFT spectrum for Theorem O4 (`python order4.py a [out.npy]`)
```python
# Order-4 construction (Galois ring / Teichmueller relative difference set).
#   Gamma = Z_4 x Z_4^a (a odd), t = (1, 0).  H = Z_4^a = additive group of GR(4,a) in the basis 1, xi, ..., xi^{a-1}.
#   p_n = Tr(xi^n) in Z_4;  W = {0} u {(p_e, ..., p_{e+a-1}) : 0 <= e < 2^a - 1}  (Teichmueller set seen through the
#   trace pairing);  S(y) = sum_{w in W} i^{w.y}.
#   Fibre over y not in 2H:  the 2-run {k, k+1} subset Z_4 with (1+i) i^k = conj(S(y)) / 2^{(a-1)/2}.
#   Fibre over y = 2u in 2H \ {0}: Z_4 if u_0 = 0 (a hyperplane of F_2^a), else empty.  Fibre over 0: empty.
# Claim: A = -A, 0 notin A, K = max(4, 2^{(a+1)/2}), |B_t| = 4^a - 2^a.
# Usage: python order4.py a
import sys, itertools
import numpy as np

a = int(sys.argv[1]); n2 = 2 ** a
def polymulmod(u, v, h, mod=4):            # polynomials as int arrays low->high, h monic of degree a
    r = np.convolve(u, v) % mod
    for k in range(len(r) - 1, a - 1, -1):
        c = r[k]
        if c: r[k - a:k + 1] = (r[k - a:k + 1] - c * h) % mod
    out = np.zeros(a, int); out[:min(a, len(r))] = r[:a]
    return out
# primitive binary polynomial f of degree a
def is_primitive2(cf):
    f = np.array(list(cf) + [1]); x = np.zeros(a, int); x[1 % a] = 1 if a > 1 else 0
    cur = np.zeros(a, int); cur[0] = 1
    for k in range(1, n2):
        cur = polymulmod(cur, np.array([0, 1]), f, 2)
        if cur[0] == 1 and not cur[1:].any(): return k == n2 - 1
    return False
for cf in itertools.product(range(2), repeat=a):
    if cf[0] and is_primitive2(cf): break
f = np.array(list(cf) + [1])
# Hensel (Graeffe) lift: h(x^2) = (-1)^a (e(x)^2 - o(x)^2) mod 4
e = f.copy(); e[1::2] = 0; o = f.copy(); o[0::2] = 0
g = (np.convolve(e, e) - np.convolve(o, o)) * (-1) ** a % 4
assert not g[1::2].any()
h = g[0::2] % 4; assert h[-1] == 1 and len(h) == a + 1
# xi = x mod h has order 2^a - 1
pw = [np.eye(1, a, 0, dtype=int)[0]]
X = np.zeros(2, int); X[1] = 1
for k in range(1, 2 * n2 + a):
    pw.append(polymulmod(pw[-1], X, h))
assert (pw[n2 - 1] == pw[0]).all() and not any((pw[k] == pw[0]).all() for k in range(1, n2 - 1))
# trace of xi^n = sum_k xi^{n 2^k}  (must be a constant polynomial)
def tr_pow(nn):
    s = np.zeros(a, int)
    for k in range(a): s = (s + pw[(nn * 2 ** k) % (n2 - 1)]) % 4
    assert not s[1:].any(), "trace not in Z_4"
    return int(s[0])
p = [tr_pow(nn) for nn in range(n2 - 1)]
W = [tuple([0] * a)] + [tuple(p[(ee + j) % (n2 - 1)] for j in range(a)) for ee in range(n2 - 1)]
assert len(set(W)) == n2
# S(y) via FFT over Z_4^a: S(y) = sum_w i^{w.y}
IW = np.zeros((4,) * a)
for w in W: IW[w] = 1
S = np.fft.ifftn(IW) * 4 ** a            # ifft uses e^{+2 pi i k.y/4} = i^{k.y}
ys = np.array(list(itertools.product(range(4), repeat=a)))
even = np.all(ys % 2 == 0, axis=1).reshape((4,) * a)
absS2 = np.abs(S) ** 2
assert np.allclose(absS2[~even], n2) and np.allclose(absS2[even & (np.arange(4 ** a).reshape((4,) * a) != 0)], 0)
# fibres
I = np.zeros((4,) + (4,) * a, bool)
units = [(1 + 1j) * 1j ** k for k in range(4)]
for idx in itertools.product(range(4), repeat=a):
    if even[idx]:
        if any(idx) and (idx[0] // 2) == 0: I[(slice(None),) + idx] = True   # full fibre, u_0 = 0
        continue
    val = np.conj(S[idx]) / 2 ** ((a - 1) / 2)
    ks = [k for k in range(4) if abs(val - units[k]) < 1e-8]
    assert len(ks) == 1, f"phase condition fails at {idx}: {val}"
    k = ks[0]; I[(k,) + idx] = True; I[((k + 1) % 4,) + idx] = True
n = a + 1
neg = I
for ax in range(n): neg = np.take(neg, [(-i) % 4 for i in range(4)], axis=ax)
assert (neg == I).all() and not I[(0,) * n]
F = np.fft.fftn(I.astype(float))
assert np.abs(F.imag).max() < 1e-6
F = F.real; F[(0,) * n] = np.inf; K = -F.min()
B = int((I & np.roll(I, 1, 0) & ~np.roll(I, -1, 0)).sum())
print(f"a={a}: |Gamma|={4 ** n} |A|={int(I.sum())} K={K:.9f} (pred {max(4, 2 ** ((a + 1) / 2)):.3f}) "
      f"|B_t|={B} (pred {4 ** a - 2 ** a})  |B_t|/K^3={B / K ** 3:.4f}  |B_t|/K^4={B / K ** 4:.4f}")
vals, cnt = np.unique(np.round(F[np.isfinite(F)], 6), return_counts=True)
print("  spectrum:", dict(zip(vals.tolist(), cnt.tolist())))
if len(sys.argv) > 2:
    np.save(sys.argv[2], I); np.save(sys.argv[2].replace(".npy", "_W.npy"), np.array(W))
```

### A.2 `order4_check.py` — independent evaluator (no FFT): RDS difference count, A = −A, exact level counts, tops
```python
# Independent evaluator for the order-4 sets: exact level counts (no FFT) and direct RDS difference count.
#   usage: python order4_check.py A.npy   (A_W.npy must sit next to it)
import sys, itertools
import numpy as np
I = np.load(sys.argv[1]); W = np.load(sys.argv[1].replace(".npy", "_W.npy"))
n = I.ndim; a = n - 1
# (1) RDS property of W in Z_4^a: every element outside 2Z_4^a is exactly one difference, none inside except 0
cnt = {}
for x in W:
    for y in W:
        d = tuple((x - y) % 4); cnt[d] = cnt.get(d, 0) + 1
outside = [d for d in itertools.product(range(4), repeat=a) if any(v % 2 for v in d)]
inside = [d for d in itertools.product(range(4), repeat=a) if not any(v % 2 for v in d) and any(d)]
assert all(cnt.get(d, 0) == 1 for d in outside) and all(cnt.get(d, 0) == 0 for d in inside) and cnt[(0,) * a] == len(W)
# (2) set axioms
pts = np.argwhere(I)
S = set(map(tuple, pts))
assert all(tuple((-p) % 4) in S for p in pts) and (0,) * n not in S
# (3) exact F at every character via level counts: F = n0 - n2, and n1 = n3 (realness)
K = -10 ** 9; Kint = None
chars = np.array(list(itertools.product(range(4), repeat=n)))
for c0 in range(0, len(chars), 512):
    C = chars[c0:c0 + 512]
    lev = (C @ pts.T) % 4                        # (#chars, |A|)
    n0 = (lev == 0).sum(1); n1 = (lev == 1).sum(1); n2 = (lev == 2).sum(1); n3 = (lev == 3).sum(1)
    assert (n1 == n3).all()
    Fv = n0 - n2
    nz = np.any(C != 0, axis=1)
    if nz.any(): K = max(K, int(-Fv[nz].min()))
# (4) run-tops along t = e_0, counted directly
B = sum(1 for p in pts if tuple(((p[0] - 1) % 4,) + tuple(p[1:])) in S and tuple(((p[0] + 1) % 4,) + tuple(p[1:])) not in S)
print(f"a={a}: RDS ok, A=-A ok, 0 notin A ok; exact integer K={K}; |B_t|={B}; |B_t|/K^3={B / K ** 3:.4f}; K^4/4-K^2/2={K**4/4-K**2/2}")
```

### A.3 `p3_check.py` — Proposition P3 from the explicit formula (FFT and exact level counts)
```python
# Proposition P3 (ord t = 3): explicit set in Gamma = F_3 x F_9 x F_9, t = (1,0,0), F_9 = F_3[i], i^2 = -1.
#   A = {(s,a,b) : [b square != 0 and s = Tr(a^2/b)] or [b non-square and s != Tr(a^2/b)] or [b = 0, a != 0]}
# Claim: A = -A, 0 notin A, K = 3, |B_t| = 36, spectrum {-3: 220, 24: 22}.  Two evaluators: FFT and exact level counts.
import itertools
import numpy as np
F9 = [(u, v) for u in range(3) for v in range(3)]
mul = lambda x, y: ((x[0] * y[0] - x[1] * y[1]) % 3, (x[0] * y[1] + x[1] * y[0]) % 3)
inv = lambda x: next(y for y in F9 if mul(x, y) == (1, 0))
tr = lambda z: (2 * z[0]) % 3                      # z + z^3 = (u+vi) + (u-vi)
sq = {mul(x, x) for x in F9 if x != (0, 0)}
I = np.zeros((3,) * 5, bool)
for s, a, b in itertools.product(range(3), F9, F9):
    if b == (0, 0):
        val = a != (0, 0)
    else:
        tau = tr(mul(mul(a, a), inv(b)))
        val = (s == tau) if b in sq else (s != tau)
    I[(s,) + a + b] = val
neg = I
for ax in range(5): neg = np.take(neg, [0, 2, 1], axis=ax)
assert (neg == I).all() and not I[0, 0, 0, 0, 0]
F = np.fft.fftn(I.astype(float)).real; F[0, 0, 0, 0, 0] = np.inf
B = int((I & np.roll(I, 1, 0) & ~np.roll(I, -1, 0)).sum())
pts = np.argwhere(I); Kx = 0
for xi in itertools.product(range(3), repeat=5):
    if any(xi):
        lev = (pts @ np.array(xi)) % 3; n = np.bincount(lev, minlength=3); assert n[1] == n[2]
        Kx = max(Kx, -(int(n[0]) - int(n[1])))
vals, cnt = np.unique(np.round(F[np.isfinite(F)], 6), return_counts=True)
print(f"|A|={len(pts)} |B_t|={B} K_fft={-F.min():.9f} K_exact={Kx} spectrum={dict(zip(vals.tolist(), cnt.tolist()))}")
```
