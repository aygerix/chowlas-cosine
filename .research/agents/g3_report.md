# G3 report (agent "g3", 2026-10-18): run-tops vs K³ in finite abelian groups

Brief: `.research/agents/g3_brief.md`. Scratch scripts: session scratchpad `.../scratchpad/g3/` (temporary; the essential
generators and verifiers are reproduced in Appendix A). All computations ran through `src/localrun.sh -m 2 -t 1800`,
one job at a time.

Conventions as in the brief: Γ finite abelian, A = −A ⊂ Γ \ {0} a set, F(χ) = Σ_{a∈A} χ(a) (real), K = −min_χ F(χ)
over all characters, B_t = {m ∈ A : m − t ∈ A, m + t ∉ A}. Labels: PROVED (complete proof here), CITED (standard fact,
reference given), NUMERICAL-EXACT (integer spectrum over all characters, two independent evaluators where stated),
NUMERICAL (search), CONDITIONAL, FAILED, OPEN.

## 0. Results at a glance

1. **(0) P21 is CORRECT** (line-by-line check, no gap; independent code for p = 3, 5, 7, 11, 13: K = 3p and |B_t| = p³
   exactly, both partial character sums of the proof match their closed forms at every character). §1.
2. **G3 is FALSE in finite abelian groups (Theorem O4, PROVED; NUMERICAL-EXACT for a = 3, 5, 7, 9).** For every odd
   a ≥ 3 there is A = −A ⊂ Γ = Z_4 × Z_4^a \ {0} and t of order 4 with
   **K = 2^{(a+1)/2} and |B_t| = K⁴/4 − K²/2**, so |B_t|/K³ = K/4 − 1/(2K) → ∞.
   Construction: the Teichmüller set of the Galois ring GR(4, a) is a (2^a, 2^a, 2^a, 1) relative difference set; its
   character sums have phases in ζ_8^{odd}, which is exactly the phase set of the fibre transform of a 2-run in Z_4.
   Every ⟨t⟩-coset off 2R meets A in a 2-run; the slice χ(t) = −1 vanishes identically; full cosets on a hyperplane of
   2R repair the slice χ(t) = 1. §2.
   - Matching upper bound (PROVED, any group, ord t = 4): 4|D₂| ≤ |E| + |D₃| + (K + u₀)⁴ (D₂, D₃, E = cosets meeting A
     in a 2-run, a 3-run, one point). Theorem O4 is extremal for it (E = D₃ = ∅).
   - Consequence: with Bedert's Prop 7.3 (|B_t| ≪ K⁴ in every group) **the group exponent of run-tops is exactly 4.**
     Every group-agnostic run-top bound is ≥ K⁴/4 − K²/2, i.e. the run-top + Shankar route cannot beat exponent 1/5
     without using a property that fails in Z_4 × Z_4^a for an element of order 4.
   - The maximal t-runs in Theorem O4 have length exactly 2 = ord(t)/2, so the brief's G_arc with "≤ ord(t)/2" is
     FALSE (at the K⁴ level). The Z-transfer has runs < ord(t)/2 − 1 (strict), which O4 does not reach: G3 in Z, and
     G_arc with strict inequality, remain OPEN.
3. **ord t = 3 with singleton cosets (task 1): OPEN; constant C ≥ 4/3.**
   - Proposition P3 (PROVED, NUMERICAL-EXACT): in F_3 × F_9 × F_9 an explicit set has K = 3 and |B_t| = 36 = (4/3)K³,
     with |E| = 36. So Theorem 2's "|B_t| ≤ K³ when E = ∅" really needs E = ∅, and G3 for ord 3 (if true) needs C ≥ 4/3.
   - Exact ILP (NUMERICAL): max |B_t| at K ≤ 3 is 18 in F_3^4 (proved optimal) and ≥ 36 in F_3^5 (P3 is the best found;
     solver bound 81 not closed). F_3^6 at K ≤ 4: see §3.3.
   - Proposition RDS3 (PROVED): exact spectrum of the general "vectorial bent / relative difference set" construction
     for ord 3; in the weakly regular case the slice χ(t) = 1 forces the negative-sign set N to satisfy N̂ ≥ −2, and
     |B_t|/K³ = |N|/3^{m/2}. CONDITIONAL criterion: a vectorial bent F_3^m → F_3^k (k > m/2) with balanced and
     Fourier-flat dual-sign set would refute G3 for ord 3. In the weakly regular case the necessary conditions cap the
     ratio (ILP, §3.4).
4. **General tools (PROVED):** restriction inequality for positive-definite functions (Lemma DI) and its corollary for
   run-tops; the singleton barrier for every order ℓ (any nonnegative combination of fibre-slice products times
   polynomials in the fibre size gives singletons weight ≥ (mass)·P(1) > 0, with an explicit cost of suppressing it);
   ℓ-th power inequalities for every ℓ, sharp for ℓ = 3 (E = ∅, P20/P21) and ℓ = 4 (Theorem O4). §4.
5. FAILED constructions and refuted intermediate claims are listed in §5; next lemmas in §6.

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

Independent verification (`p21_check.py`, Appendix A.3): two evaluators, numpy FFT and exact level counts
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

### 2.1 Galois ring facts
Let a ≥ 1, R = GR(4, a) = Z_4[x]/(h(x)) with h a basic primitive polynomial of degree a (Hensel lift of a primitive
f ∈ F_2[x]; h(x²) = (−1)^a f(x)f(−x) mod 4). CITED-standard (e.g. Z.-X. Wan, *Lectures on finite fields and Galois
rings*, ch. 14; Hammons–Kumar–Calderbank–Sloane–Solé, IEEE-IT 1994):
- (G1) R is local with maximal ideal 2R, R/2R ≅ F_{2^a}, |R| = 4^a, (R, +) ≅ Z_4^a, units R^× = R \ 2R.
- (G2) ξ = x mod h has order 2^a − 1; the Teichmüller set T = {0} ∪ ⟨ξ⟩ maps bijectively onto F_{2^a} under reduction
  z ↦ z̄; write τ(α) ∈ T for the lift of α. Every z ∈ R is uniquely z = τ(α) + 2τ(β).
- (G3) The Frobenius σ (ring automorphism, σ(τ(α)) = τ(α²)) and Tr = Σ_{i<a} σ^i : R → Z_4 is Z_4-linear,
  Tr(z) mod 2 = tr(z̄), and (x, y) ↦ Tr(xy) is nondegenerate, so y ↦ (x ↦ i^{Tr(xy)}) is an isomorphism R → R̂.

**Lemma T (PROVED).** τ(α) + τ(β) = τ(α + β) + 2τ(√(αβ)) for α, β ∈ F_{2^a}. Consequently every unit u ∈ R^× is
x − x′ (x, x′ ∈ T) in exactly one way, and no element of 2R \ {0} is a difference of two elements of T. (T is a
(2^a, 2^a, 2^a, 1) relative difference set in (R, +) relative to 2R.)

*Proof.* Write z = τ(α) + τ(β) = τ(c) + 2τ(d) (G2); reducing mod 2, c = α + β. Since 4 = 0,
z² = τ(c)² = τ(c²), while z² = τ(α²) + τ(β²) + 2τ(αβ) = σ(z) + 2τ(αβ) = τ(c²) + 2τ(d²) + 2τ(αβ). Hence
2(τ(d²) + τ(αβ)) = 0, i.e. d² = αβ in F_{2^a}. For the differences: −x′ = x′ + 2x′, and 2τ(γ) + 2τ(δ) = 2τ(γ + δ), so
x − x′ = τ(x̄ + x̄′) + 2τ(√(x̄x̄′) + x̄′). Given u = τ(ū) + 2τ(ν): if ū = 0 then x̄ = x̄′, x = x′, difference 0. If ū ≠ 0,
x̄′ = x̄ + ū and the condition √(x̄(x̄ + ū)) = ν + x̄ + ū squares (Frobenius is bijective) to x̄ū = ν² + ū², whose unique
solution is x̄ = (ν² + ū²)/ū. ∎

**Lemma S (PROVED).** For y ∈ R put S(y) = Σ_{x∈T} i^{Tr(xy)}. Then S(0) = 2^a; S(y) = 0 for y ∈ 2R \ {0};
|S(y)|² = 2^a for y ∈ R^×; and if a is odd, S(y) ∈ 2^{(a−1)/2}(1 + i)μ_4 for every y ∈ R^×. Also S(−y) = conj S(y).

*Proof.* For y = 2u ≠ 0: i^{Tr(2ux)} = (−1)^{tr(ūx̄)} and x̄ runs over F_{2^a}, so S = 0 (ū ≠ 0). By Lemma T,
|S(y)|² = Σ_{x,x′∈T} i^{Tr((x−x′)y)} = 2^a + Σ_{u∈R^×} i^{Tr(uy)} = 2^a + 4^a[y = 0] − Σ_{z∈2R} i^{Tr(zy)}, and
Σ_{z∈2R} i^{Tr(zy)} = Σ_ū (−1)^{tr(ūȳ)} = 2^a[ȳ = 0]; for y ∈ R^× this gives 2^a. Finally S(y) ∈ Z[i] has norm 2^a;
Z[i] is a UFD in which 2 = −i(1+i)² and (1 + i) is the only prime over 2, so S(y) = unit·(1+i)^a =
unit·(2i)^{(a−1)/2}(1 + i) for odd a. ∎

### 2.2 The construction
**Theorem O4 (PROVED; NUMERICAL-EXACT for a = 3, 5, 7 with two independent evaluators, FFT-exact for a = 9).**
Let a ≥ 1 be odd, R = GR(4, a), Γ = Z_4 × R, t = (1, 0). For y ∈ R^× define k(y) ∈ Z_4 by
conj S(y) = 2^{(a−1)/2}(1 + i) i^{k(y)} (Lemma S). Fix an F_2-hyperplane W̄ ⊂ F_{2^a} and put
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

Spectrum (a ≥ 5): {−K, K(2^a − 1)} on χ(t) = ±i, {0} on χ(t) = −1, {−4, 2^{a+1} − 4} on χ(t) = 1.

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
