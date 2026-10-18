# Limits of the run-top method for Chowla's cosine problem

Status (2026-10-18). §3 Theorem 1: PROVED (agent conjG; lead re-verified numerically with an independent set).
§3 Theorem 2: PROVED (lead, elementary; numerical check for p ≤ 23). §4: PROVED (agent conjG; checked line by line by
lead). §3b (Theorem O4): PROVED (agent g3; paper proof checked line by line by lead; lead's independent computation
E36). §2 summarises PROVED results of `.research/agents/runtop_report.md` (agent; proof read by lead, independent
numerical check). Nothing here is kernel-checked yet. These are barriers for **lower-bound proofs**, not constructions,
and they say nothing about Epoch's `solution(c, n)`.

## 1. The method

Use the symmetric form. A = −A ⊂ Z \ {0} is finite, n = |A|, F(θ) = Σ_{a∈A} e(aθ) is real, and K = −min_θ F(θ)
(K = 2M for the cosine sum of A ∩ Z_{>0}). For t ≥ 1 the **run-tops** are

    B_t = {m ∈ A : m − t ∈ A, m + t ∉ A},

one for each maximal arithmetic progression ("t-run") of step t and length ≥ 2 in A.
The current polynomial lower bounds (Bedert, arXiv:2509.05260; Shankar, arXiv:2609.05338) chain three facts:

1. **Roth-type counting** (valid in every group): T := #{(a, b) ∈ A² : a − b ∈ A} ≥ n²/K − nK.
2. **Averaging over steps** (Shankar; uses the order of Z): Σ_{t∈A} |B_t| ≥ T/3. Hence max_t |B_t| ≥ n/(3K) − K/3.
3. **Run-top bound** (Bedert Prop 7.3; valid in every finite abelian group, and transferable to Z): |B_t| ≤ C·K^β with
   β = 4.

Combined, n ≲ K^{β+1}, so K ≫ n^{1/(β+1)} = n^{1/5}. **A run-top bound with exponent β gives Chowla exponent 1/(β+1).**
For β = 3 this is 1/4; for β = 2 it is 1/3. Transfer: if A ⊂ [−X, X], embed A in Z_N with N > 4X + 4t. The F-samples
at N-th roots of unity keep F ≥ −K, and B_t is unchanged. So any run-top bound valid in all cyclic groups holds in Z.

## 2. Degree-2 methods are capped at K⁴ (P19, agent "runtop")

Bedert's proof uses F ≥ −K only through degree-2 convolution inequalities
w·((m_1G + m_1'K) ∗ (m_2G + m_2'K)) ≥ 0, where G = F + K ≥ 0 and w, m_i, m_i' are nonnegative trigonometric polynomials
in tx.

**Theorem B.** For any finite family of such A-independent inequalities, there are symmetric random sets
A ⊂ [−N, N] satisfying all of them with K_* ≍ (N log N)^{1/4} while |B_t| ≍ N ≍ K_*⁴/log K_*. Likewise, r-fold
convolutions are capped at K^{2r}.

**Proposition M.** The method proves exactly |B_t| ≲ ∫ min(|1̂_{B_t}|, K|B_t|^{1/2})². To reach K^{4−δ} one must show
∫ min(|1̂_{B_t}|, K³)² ≪ K^{4−δ} ("Lemma S"), and that requires F ≥ −K at degree 1.

## 3. Group-agnostic arguments are capped at K³

**Theorem 1 (P20).** Let p be an odd prime, a ≥ 1 and q = p^a. In Γ = F_p × F_q × F_{q²} with t = (1, 0, 0) there is a
symmetric A ⊂ Γ \ {0} with min F = −q and |B_t| = (q − 1)q² = K²(K − 1).
The simplest instance (lead): A = {x ∈ F_p^4 : x1x2 + x3² − d x4² ≠ 0} with t = e1 and d a non-residue. This gives
K = p and |B_t| = p²(p − 1). Here the t-lines with x2 = 0 are full or empty.

**Theorem 2 (P21; full cosets are not needed).** Let p be an odd prime and d a non-residue, write N(v) = v3² − d v4²,
and take Γ = F_p^4, t = e1 and

    A = {x : x2 ≠ 0, x1x2 + N(x3, x4) ≠ 0} ∪ {x : x2 = 0, x1 ≠ x3·x4²}.

Then A = −A and 0 ∉ A, and every ⟨t⟩-coset meets A in exactly p − 1 points. Also F ≥ −3p, and |B_t| = p³ ≥ K³/27.

*Proof.*
- Symmetry. The first condition is even and the second odd under x ↦ −x, and x = 0 violates the second.
- Run-tops. A line {x + st} with x2 ≠ 0 misses only x1 = −N/x2. A line with x2 = 0 misses only x1 = x3x4². A cyclic
  run F_p \ {τ} has exactly one top, m = τ − 1. So |B_t| = p³.
- Characters. Take χ = e_p(jx1 + kx2 + c·v).
- Case j = 0. Every line carries p − 1 points, so F = 0 for (k, c) ≠ 0.
- Case j ≠ 0. A line missing τ contributes −e_p(jτ)·χ(line).
  - Lines with x2 ≠ 0. For α = −j/x2 the Gauss sum gives Σ_v e_p(αN(v) + c·v) = −p·e_p(N*(c)x2/(4j)), where
    N*(c) = c3² − c4²/d. (Use g² = η(−1)p and η(d) = −1.) Summing over x2 ≠ 0, these lines contribute
    p(p·[k + N*(c)/(4j) = 0] − 1) ∈ {−p, p(p − 1)}.
  - Lines with x2 = 0. They contribute −ĝ_j(c), where ĝ_j(c) = p·Σ_{v4 : j v4² = −c3} e_p(c4v4). This sum has at most
    two terms, so |ĝ_j(c)| ≤ 2p.
- Hence F ≥ −3p. ∎

Numerically (E33), K = 3p and |B_t| = p³ exactly for p = 3, …, 23.

**Consequences.**
- No run-top bound valid in all finite abelian groups can have β < 3. This holds even for sets with no full and no
  singleton ⟨t⟩-cosets (Theorem 2). So every group-agnostic Fourier argument, including pointwise positivity at all
  characters, gives at best Chowla exponent 1/4 by this route.
- The group window for the optimal exponent was [3, 4]; §3b closes it at 4.
- Theorem 2's set has n ≈ p⁴ and K = 3p, i.e. K ≍ n^{1/4}. It is the group-theoretic shape of a hypothetical exponent-1/4
  counterexample: every t-coset is a single long run.

## 3b. Group-agnostic arguments are capped at K⁴: the group exponent is exactly 4 (P22, agent g3)

**Theorem O4.** Let a ≥ 3 be odd, R = GR(4, a) the Galois ring with 4^a elements, Γ = Z_4 × R and t = (1, 0).
Let T ⊂ R be the Teichmüller set and S(y) = Σ_{x∈T} i^{Tr(xy)}. For a unit y, define k(y) by
conj S(y) = 2^{(a−1)/2}(1 + i)i^{k(y)}. Let F₀ = {2u : ū ∈ W̄ \ 0}, where W̄ is a hyperplane of F_{2^a}. Then

    A = {(s, y) : y ∈ R^×, s ∈ {k(y), k(y) + 1}} ∪ (Z_4 × F₀)

is symmetric, 0 ∉ A, K = 2^{(a+1)/2} and |B_t| = 4^a − 2^a = K⁴/4 − K²/2.

*Mechanism.*
- T is a (2^a, 2^a, 2^a, 1) relative difference set. Its character sums are 2^{(a−1)/2}·(1 + i)·(unit), which is
  exactly the phase set of the transform of a 2-run {k, k + 1} along an element of order 4.
- So the slice χ(t) = ±i takes the two values {−K, K(2^a − 1)}.
- The slice χ(t) = −1 vanishes identically on 2-runs.
- The slice χ(t) = 1 sees only the fibre sizes, and it is repaired by full cosets over a hyperplane of 2R (cost 4).

**Matching upper bound (any group, ord t = 4).** 4|D₂| ≤ |E| + |D₃| + (K + u₀)⁴. This is the fourth-power analogue of §4,
and O4 is extremal for it. Bedert's |B_t| ≪ K⁴ holds in every group, so **the group exponent is exactly 4**.

**Averaged form (E36b).** In O4 the average of |B_t| over t ∈ A is K⁴/8 − O(K²), for a = 3, 5, 7. So the A-averaged
run-top count that Shankar's chain actually uses also has group exponent 4. Run-tops in O4 are as frequent as in a random
set of density 1/2.

**Consequence.** No bound on |B_t|, or on its average over t ∈ A, that holds in all finite abelian groups beats K⁴/8.
The run-top route stops at Chowla exponent 1/5 (Bedert/Shankar) unless **the run-top bound itself** uses a property of Z.
The averaging step (Shankar) is not enough.

Candidate properties of Z that O4 violates:
- **Run length.** Runs in O4 have length exactly ord(t)/2, while every t-run in Z is shorter than ord(t)/2 − 1.
- **Order of t.** ord t = 4 in O4.
- **Torsion.** The quotient 2-torsion lies inside the repaired region.

Caution: in Z we have |B_t| ≤ |A|, so Chowla itself implies |B_t| ≤ CK². Any Z run-top bound is therefore a weakening
of Chowla, not an independent tool.

## 4. The cubic bound for t of order 3 (P20, agent conjG)

**Theorem.** Let Γ be finite abelian and t ∈ Γ of order 3. Let D and E be the sets of ⟨t⟩-cosets meeting A in exactly 2
and exactly 1 points, so |B_t| = |D| up to the coset ⟨t⟩ itself. Then |D| − |E| ≤ (K + u0)³, where u0 ∈ {0, −1}.

*Proof.*
- Set-up. Fix χ0 with χ0(t) = ω, let H̄ = Γ/⟨t⟩, and put U(y) = Σ_{x∈A∩y} χ0(x).
- Positivity. For φ ∈ ⟨t⟩^⊥ we have Σ_y U(y)φ(y) = F(χ0φ) ≥ −K. So U + Kδ0 is positive definite on H̄, and by the Schur
  product theorem so is (U + Kδ0)³.
- Cube values. U³ = ρ·(1_E − 1_D) off y = 0, where ρ = χ0³ ∈ Ĥ̄. On a 2-point coset U = −χ0(missing point), since
  1 + ω + ω² = 0.
- Evaluating the transform of (U + Kδ0)³ at ρ̄ gives (K + u0)³ + |E| − |D| ≥ 0. ∎

This is sharp: Theorem 1 with p = 3 has E = ∅. Every positive combination of such fibre monomials takes the value +1
on singleton cosets. So these methods bound |D| − ε|E|, never |D| alone (conjG report §2).

## 5. Why Z is different, and what a better bound must use

- **Negative-definite fibres.** In both K³ constructions every fibre is F_p \ {τ}, whose transform along t is
  −e_p(jτ) at every j ≠ 0.
- **Lemma (PROVED).** If a fibre I ⊂ Z_ℓ, translated so that 0 ∉ I, has transform ≤ 0 at every j ≠ 0, then |I| ≥ ℓ/2.
  *Proof:* |I|/ℓ − 1_I has nonnegative transform, so its value at 0 dominates its value on I. So these fibres are runs
  longer than half the cycle.
- **In Z.** In Z, and in its Z_N transfer, every t-run has length ≤ 2X/t + 1 < ord(t)/2. The transform of a run along t
  is a Dirichlet kernel, with a positive main lobe and negative side lobes.
- **Torsion-free first-order effect (HEURISTIC).** Write θ = (j + φ)/t. Because F is even, the term linear in φ at
  θ = j/t has opposite signs at j and −j. Groups of exponent p have no small φ.
- **Conclusion (updated after §3b).** G3 in groups is FALSE (Theorem O4). Any run-top bound below K⁴, and hence any
  Chowla exponent above 1/5 by this route, must use the order or interval structure of Z. One example is the continuity
  of the t-direction offset φ. G3 in Z, and G_arc with strict run length < ord(t)/2, remain OPEN; they would give
  exponent 1/4. §4 proves the ord t = 3 case without singleton cosets.

## 6. Refuted intermediate conjectures (kept)
- G: |B_t| ≤ CK² in every finite abelian group. Refuted by Theorem 1.
- G_noFull: the same bound when no ⟨t⟩-coset lies inside A. Refuted by Theorem 2.
- "Paley sets are optimal, C = 1/2." Refuted by quadric level sets (ratio 1, 2) and by Theorems 1–2.
- Group form of Lemma S with δ > 1. Refuted by Theorem 1.
- G3: |B_t| ≤ CK³ in every finite abelian group. Refuted by Theorem O4 (§3b), also in its A-averaged form.
- G_arc with "≤ ord(t)/2": refuted by Theorem O4 (its runs have length exactly ord(t)/2).

Novelty: not checked. The spectra {−q, (p−1)q, q(q−1)} suggest links with two-weight codes and strongly regular
Cayley graphs. These should be searched before any external claim.
