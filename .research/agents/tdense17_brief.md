# Math brief (codex research agent), round 17: the self-difference graph dichotomy — noise ⇒ √n, structure ⇒ Gibbs

You are a research mathematician working on Chowla's cosine problem in /Users/jmercedes/Desktop/Projects/Research/chowla-cosine.
- Read CLAUDE.md first: conventions, honesty labels, and the rule that numerics are not proofs.
- Conventions: f_A = Σ_{a∈A} cos(ax), M(A) = −min f_A, n = |A|, X = max A, S = A ∪ (−A), K = 2M.
- Rules (unchanged):
  - Do NOT edit .research/*.md. Do not commit. Do not launch subagents. No LaTeX; markdown only.
  - Report: `.research/agents/tdense17_report.md` (keep it current). Scratch: `.research/agents/tdense17_scratch/`.
  - Computation ONLY on the VM via `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 ...` (at most 4 cores; bash, not
    zsh).
  - Gurobi for every LP/MILP/QP. SDPs, if any, use Clarabel or SCS via cvxpy.
  - Label every claim PROVED / NUMERICAL / HEURISTIC / CONJECTURED, with exact quantifiers.
  - Grep .research/PROOFS.md before any novelty claim.
- GOAL: the user's priority is a PROOF of Chowla (M >= c√n for ALL finite A). The cyclic WRS line is paused (P69).

## State (read NOTEBOOK cont. 19 in full, EXPERIMENTS E99, PROOFS P9, P27, P28, P29, P63, P66, P69)
- Proved lower bounds in the record:
  - P28: spread spectrum ⇒ about 0.21√n.
  - P9: induced subgraphs, M >= −λ_min(Cay(Z,S)[W])/2 for every finite W; star/sum-free ⇒ √n/2.
  - T-dense(C) ⇒ c(C)√n for max A <= 7.72|A|; exponent 1/3 up to 13.7.
  - P27: unions of translated dilates have √n.
- NEW (E99, NUMERICAL): let H = Cay(Z,S)[A] (a ~ a' iff |a − a'| ∈ A). On every near-extremal set known to us, H has a
  SOFT bottom edge λ_min(H) ≈ −0.72√n, with delocalized bottom eigenvectors orthogonal to 1_A. This holds for small-N
  optima n <= 100 and Singer–Bu n = 3782 … 39800 with R -> 0.566. Cay[A] alone certifies ≈ 0.6K.
  - The AP is the opposite extreme: H = J − I, λ_min = −1, and its M is linear by Gibbs.
  - Lead's reading: C½ is a random-matrix semicircle edge. At density α = ½, −2√(α(1−α)n) = −√n gives exactly √n/2,
    and the star extreme gives √n/2 too.
- NEW PROVED inequalities (NOTEBOOK cont. 19.7; re-check them):
  - (a) Bhatia–Davis. For symmetric H with tr H = 0 and any τ > 0, let μ_τ, v_τ be the mean and variance of the
    eigenvalues <= τ. Then −λ_min(H) >= v_τ/(τ + |μ_τ|) + |μ_τ|.
  - (b) Trace split. If λ_min(H) >= −K, then H = P − N with P >= 0, ‖N‖ <= K, tr P = tr N <= nK and
    ‖H − P‖_F² <= nK².
- Barriers to respect:
  - scalar moments of D_S cap at 1/3 (R12-S);
  - group-agnostic arguments cap at ¼ (F_p^4 quadric complement; JMTZ);
  - cyclic core-sumset equations (P69);
  - low-degree SOS (E96).
  - Any argument must use something Z has and F_p^4 lacks: order, boundaries, or trivial stabilizers of finite sets
    (cont. 19.8, including its correction).

## Task 1 (main): the NOISE branch — a √n-scale bulk for H, or the exact obstruction
Target lemma BULK(β, γ), CONJECTURED. Pick a canonical vertex set W = W(A): A, A ∪ {0}, or A ∪ (A + t) for a chosen t.
Then for every A, either
- (i) Σ_{|λ| <= γ√n} λ² >= β·n² for the spectrum of H_W, or
- (ii) A is "structured" in a precisely stated sense, e.g. H_W is ε-close in normalized Frobenius norm to a PSD matrix
  of effective rank <= R(ε).
With (a), (i) gives M >= c(β, γ)√n.

Steps.
1. Derive what controls the bulk. Express tr H, tr H², tr H³, tr H⁴ as exact additive counts in A. For example,
   tr H² = 2T₃ with T₃ = #{a < a' : a' − a ∈ A}; tr H⁴ counts 4-cycles a₁a₂a₃a₄ with all four steps in ±A.
   - Use Chung–Graham–Wilson-type quasirandomness: C4 count close to α⁴n⁴ ⇒ spectrum mass outside the top eigenvalue
     is O(αn) per eigenvalue ⇒ a bulk at scale √(αn).
   - The dense case has macroscopic graphon structure (eigenvalues of order n from the density profile). Remove the
     top eigenvalues with Bhatia–Davis's τ cut and track |μ_τ|.
2. Decide whether (i) can fail without (ii). If you find a family with no √n bulk and not structured, that is the
   decisive obstruction. Test it on the VM before claiming.
3. Booleanity must enter: H has 0/1 entries, zero diagonal, and the TOEPLITZ-INDUCED form H_{aa'} = 1_A(|a − a'|).
   - Generic 0/1 graphs with λ_min >= −K exist with huge degree (disjoint cliques). Say exactly where the
     self-referential form is used.

## Task 2: the STRUCTURED branch — clique rigidity and Gibbs
1. CLIQUE-S (CONJECTURED, NOTEBOOK cont. 19.9): every clique C of Cay(Z,S), i.e. C − C ⊂ S ∪ {0}, has
   |C| <= c₁K + c₂.
   - Tight examples: Sidon differences (B is a clique of size K) and Bu sets (3B).
   - FALSIFY FIRST on the VM. Search for large cliques in Cay[S] for the near-extremal sets (heuristic clique search
     is fine for lower bounds on ω). Try constructions: a Sidon clique C plus an extra S' disjoint from C − C designed
     to cancel the dips of |F_C|². Report the best ω/K found.
   - Then attempt a proof. Hint: at the zeros of F_C (C Sidon), D_{S'} >= |C| − K is forced.
2. From (b): if K = ε√n, H is ε-close to PSD with trace <= εn^{3/2}. Extract clusters (near-cliques, i.e.
   approximate groups) from the Gram structure, quantitatively in ε.
   - Then show each large cluster forces a Gibbs dip >= c√n through another vertex set (intervals, translates). Use
     the PD-profile/continuity mechanism (P29(b), P48, P53) and P27.
   - Track losses: we only need M >= c√n, while a Gibbs dip is typically LINEAR in the cluster size. Say how small a
     cluster may be before Gibbs stops beating √n.

## Task 3: adversaries (before investing in any lemma)
- E99 sets: examples/e99/e99.jsonl, smallN_best.json, singer_bu/certified.json (build A with src/bu.py A_of_S).
- APs, rank-2 and rank-3 Bohr sets, and unions of many small APs or Bohr pieces (the "many small clusters" danger).
- A Z-lift of the F_p^4 quadric complement through a rank-4 GAP, with hard and tapered boundaries. It shows how the
  stabilizer escape dies in Z.
- Random sets of density α ∈ {0.05, 0.25, 0.5}.
- For every intermediate inequality, report its value on these sets.

## Deliverable
The report contains one of:
- a theorem (a new universal or broad-class √n bound);
- a conditional theorem with ONE named lemma, surviving all adversaries;
- a precise obstruction (an explicit family defeating the dichotomy as stated, with what it violates).
Also include adversarial tables, the CLIQUE-S verdict (best ω/K found), and a strategic recommendation. Say exactly
what is new versus quoted.

## CORRECTION (lead, added mid-round; SUPERSEDES the framing of Tasks 1–2 above). Read this first.
Your interim report already found two of these problems. The lead's statements in NOTEBOOK cont. 19.7–9 were wrong
in four ways:
1. Sparse regime (external review). Cay[A] carries only ‖H‖_F² = 2T₃ = αn² of spectral mass, so BULK(β, γ) needs
   β <= α. It is false for every sparse set.
   - For random sum-free A ⊂ (N, 2N], H = 0, and the trace split calls it "structured" with P = 0, which is vacuous.
   - Their certificate is the star on {0} ∪ ±A: P9 gives M >= √(n/2).
2. Intermediate density (lead; CORRECTED by E99b/E99c). P9 on W2 = {0} ∪ ±A gives roughly
   max(1/α, c(φ)·αn, 3√(αn)), where:
   - 1/α is the star, coupled to the top eigenvector;
   - c(φ)·αn is a macroscopic negative eigenvalue. The graphon of W2 is the kernel ρ(|x − y|) on [−1, 1], so
     c(φ) > 0 iff the profile shape φ is NOT positive definite. This is Gibbs in graph form.
   - 3√(αn) is the noise bulk.
   Consequences:
   - FLAT random sets get >~ √n at every density (E99b: W2/√n ≈ 0.9–2.6 for n <= 16000).
   - PD-TAPERED random sets (triangle profile) at α ~ n^{−1/3} get only ≈ 3.1n^{1/3} (E99c: W2/n^{1/3} = 3.30,
     3.09, 3.09 at n ≈ 1000, 4000, 16000). Their true M ~ √(n log n) comes from Fourier spread (P28).
   - So the advisor's "intermediate region" is real: tapered profile, density ~n^{−1/3}, exponent 1/3 (the same as
     the moment cap R12-S).
3. Large-M sets (your shifted-interval obstruction). The dichotomy must be CONDITIONED on λ_min >= −ε√n.
4. CLIQUE-S is FALSE (your forced-prefix smooth-profile roundings; certified clique/K >= 6.67 at L = 4096). Clusters
   much shorter than X that sit inside a smooth taper cost nothing. Clique rigidity cannot drive the structured branch.

Revised targets (replace Tasks 1–2; Task 3 stays):
- T1 (main): FOUR-WAY COVER.
  - Assume M = ε√n. Write down the JOINT necessary conditions that each certificate imposes on A, with explicit
    dependence on ε:
    - (i) P28 Fourier spread forces a spiky spectrum;
    - (ii) the star / P9 on {0} ∪ ±A forces T₃ >~ n^{3/2};
    - (iii) P9 on A plus Bhatia–Davis bounds the √n-bulk of Cay[A];
    - (iv) PD-profile / Gibbs constraints (P29(b), P48, P53).
  - Then EITHER prove these conditions are jointly inconsistent for small ε (a cover lemma with constants independent
    of n), OR construct an explicit family on which all four certificates are simultaneously o(√n).
  - The latter is the decisive adversarial test. Run a multi-objective search: minimize the maximum of the four
    certificates divided by √n, not M. Seed it with structured candidates: tapered rank 2–4 Bohr sets, quadric lifts,
    forced-prefix roundings, and TAPERED random sets of density n^{−1/3}
    (src/e99c_tapered.py), where the graph certificates are already only ~n^{1/3}. The open question is whether some
    structure there ALSO defeats P28.
- T2: write up the CLIQUE-S refutation rigorously (asymptotic proof plus certified instances). Then state the correct
  structured-branch input: what kind of cluster forces Gibbs. The forced-prefix example says a cluster inside a smooth
  taper does not, so the condition must involve the SHARPNESS of the cluster's boundary relative to the ambient
  profile.
- Keep your shifted-interval obstruction and its proof in the report.
