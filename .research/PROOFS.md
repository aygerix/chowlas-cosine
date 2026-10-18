# Proofs and exact reformulations

Status labels: PROVED (paper proof here), CITED, HEURISTIC, CONJECTURED, REFUTED.

## P1. Fejér–Riesz reformulation (PROVED, standard)
For finite A ⊂ N, M(A) = min ||q||_2^2 over finitely supported q: Z -> C with autocorrelation
r_q(d) = sum_k q_{k+d} conj(q_k) = (1/2) 1_{±A}(d) for all d != 0.
Proof: f_A + C >= 0 is a nonnegative trig polynomial iff = |Q(e^{ix})|^2 (Fejér–Riesz); coefficient matching; ||q||^2 = C.
Consequence: R(A)^2 = ||q||^4 / (|Q(0)|^2 - ||q||^2), with |Q(0)|^2 = M + N. Equivalently (Bu et al. Prop 8.1, h=0):
R = M2 / sqrt(2(M4 - M2^2)), M_p = (1/2pi) ∫|Q|^p. R -> 0 iff M4/M2^2 -> infinity.

## P2. Probabilistic reformulation (PROVED)
Good A <=> integer symmetric random variable S with characteristic function phi_S >= 0 and P(S=g) in {0, eps} for g != 0;
then M = p0/(2 eps), N = (1-p0)/(2 eps), R^2 = p0^2/(2 eps (1-p0)), p0 = P(S=0).

## P3. Dimension-free / projection principle (PROVED)
For finite symmetric S ⊂ Z^k \ {0} and b ∈ Z^k with s -> |<b,s>| injective on S/± and nonzero:
A = {|<b,s>|} satisfies f_A(x) = (1/2) F_S(x b) >= (1/2) min_{T^k} F_S, |A| = |S|/2.
So the problem over Z is the same as over all f.g. free abelian groups; a line restriction can only raise the min.

## P4. Exact t-fold uniform difference sets do not exist in torsion-free groups for t >= 2 (PROVED)
If B ⊂ Z^k finite, |B| >= 2, the difference v-w maximizing a generic linear functional is represented once.
Moreover the only maps of pairs induced by point maps preserving the difference are translations and the reversal
(u,v) -> (c-v, c-u); hence "multiplicity by symmetry" is at most 2 (this is Bu et al.'s factor 2).

## P5. Intersection lemma (PROVED)
M(A1 ∩ A2) <= 2 M(A1) M(A2). Proof: (f1+M1)*(f2+M2) (normalized convolution on the circle) >= 0 has
constant M1 M2 and coefficient 1/4 at ±a for a ∈ A1∩A2, i.e. equals M1M2 + f_{A1∩A2}/2.

## P6. Additive-energy lower bound (PROVED, elementary; cf. Roth/Bedert)
M >= ||f||_1/2 >= ||f||_2^3/(2||f||_4^2), ||f||_2^2 = N/2, ||f||_4^4 = m4 = (6E(A)+8Q3(A))/16
(E = #{a+b=c+d}, Q3 = #{a+b+c=d}). Hence R(A) >= N/(2^{5/2} sqrt(m4)): R -> 0 forces m4/N^2 -> infinity.
Third moment version: M >= max_alpha (alpha N - (3/4)T3)/(alpha^2+N/2), T3 = #{a+b=c}; sum-free A have R >= 1/sqrt2... (check constant: M >= sqrt(N/2) for T3=0).

## P7. Cube (torus) framework — rigorous construction template (PROVED)
Let J be a family of nonempty subsets of [k]; alpha_1..alpha_k positive integers such that the signed sums
sum_{j in S} eps_j alpha_j (S in J, eps in {±1}^S) are pairwise distinct up to global sign and nonzero.
Then A = {|sum_{j∈S} eps_j alpha_j|} has |A| = sum_{S∈J} 2^{|S|-1} and
f_A(x) = (1/2) p_J(2cos alpha_1 x, ..., 2cos alpha_k x),  p_J(y) = sum_{S∈J} prod_{j∈S} y_j,
hence min f_A >= (1/2) min_{eps ∈ {±1}^k} sum_{S∈J} 2^{|S|} eps^S   (multilinear => vertex minimum).
R_cube(J) := -min_eps g_J / sqrt(2 sum_J 2^{|S|}) bounds R(A) rigorously for every admissible alpha.
Hypercontractivity gives only R_cube >= (1/2)(sqrt2/3)^d for degree-d families: no a priori barrier.

## H1. Gaussian-chaos heuristic and the 1/2 barrier (HEURISTIC; see NOTEBOOK 2026-10-17)
At typical x, blockwise cosine sums behave like independent Gaussians; set-ness forces WICK-ordered chaos with
fixed positive coefficients kappa_a = (1/2) prod t_i^{a_i}/a_i! (t_i^2 = 2k_i). Degree-2 chaos: R >= 1/2, equality
iff single block (= Bu). Degree 4 single block: R = sqrt3*... = 0.866. Non-Wick z^4-3 would give 0.2165 but needs
lower-chaos multiplicities ~ block size. CONJECTURE H1: large-block Wick models have inf R = 1/2.

## P8. Weighted-multiplicity bound for square certificates (PROVED, paper; generalizes Bu et al. Prop 8.2)
Let A ⊂ N finite, N = |A|. Suppose lambda + f_A(x) = |Q(x)|^2 - h(x) for all x, where Q(x) = sum_{β∈B} q_β e^{iβx}
(B a finite subset of a single coset γ0+Z of R, q_β ∈ C) and h is a real trig polynomial whose spectrum avoids ±A ∪ {0}.
Let mu(g) = |B ∩ (B+g)| and w(g) = sum_{β-β'=g} |q_β|^2 |q_β'|^2, mu_bar = sum_{g≠0} mu(g) w(g) / sum_{g≠0} w(g).
Then N <= 2 mu_bar lambda^2; in particular lambda >= sqrt(N/(2 mu_max)).
Proof. r(g) := sum_{β-β'=g} q_β conj(q_β') is the coefficient of e^{igx} in |Q|^2; matching coefficients,
r(g) = 1/2 for g ∈ ±A and r(g) = ĥ(g) otherwise (g≠0), r(0) = lambda (since ĥ(0)=0). Hence
N/2 <= sum_{g≠0} |r(g)|^2 <= sum_{g≠0} mu(g) w(g) (Cauchy–Schwarz over the mu(g) pairs) = mu_bar (lambda^2 - sum|q|^4) <= mu_bar lambda^2.
Consequences: (i) exact FR factors supported on Sidon sets give R >= 1/sqrt2; on sets with all multiplicities <= 2,
R >= 1/2 (this is the Bu barrier, now for arbitrary weights); (ii) R(A) < 1/sqrt(2m) forces the FR factor of
f_A + M(A) to have |q|^2-weighted mean difference multiplicity > m; equality-type efficiency requires the pair
products q_β conj(q_{β-g}) to be nearly constant along each difference class (=> nearly flat multiplicities).
Note: lambda here is ||Q||_2^2; when h != 0, M(A) <= lambda + max_x (h - |Q|^2)_+ ... only lambda is bounded.

## Lean status (2026-10-17, re-verified by lead: `lake build` OK, 15 theorems, axioms = [propext, Classical.choice, Quot.sound], no sorry/native_decide)
- KERNEL-CHECKED: difference-set square identity (`norm_sq_sum_exp`); Sidon consequence f_{D-D} >= -|D|/2 with |D-D|_+ = k(k-1)/2
  (`sidon_diffSet_main`); mean zero and Parseval (`integral_cosSum`, `integral_cosSum_sq`); P5 intersection lemma
  (`cosSum_inter_ge`, no sign hypothesis on M_i needed); P7 cube identity + multilinear vertex minimum (`cubeSum_min`).
- KERNEL-CHECKED 2026-10-18 (Lean agent, re-verified by lead: build OK, 29 #print axioms lines all [propext, Classical.choice,
  Quot.sound], no sorry): P9 `star_lemma` (∀ W, v: Σ v_u v_w 1[|u−w|∈A] >= −2M Σ v^2) and `star_bound` (A-independent
  I ⊂ ±A ⇒ sqrt|I|/2 <= M); P8 `card_le_of_sq_certificate` (λ + f_A = |Σ_{β∈B} q_β e^{iβx}|^2 − Σ_{g∈G} c_g cos(gx), G avoiding
  0 and ±A, pair counts <= m at |g| ∈ A ⇒ |A| <= 2mλ^2; integer-frequency version) and the stated variant.
- KERNEL-CHECKED 2026-10-18 (Lean agent; lead re-ran `lake build` (OK) and regenerated AxiomCheck: 37 lines, all
  [propext, Classical.choice, Quot.sound], no sorry/admit/native_decide): P13(a) in lean/ChowlaCosine/Averaging.lean —
  `averaging_identity` ((1/q)Σ_{j<q} f_A(x + 2πj/q) = f_{A∩qZ}(x), q >= 1), `cosSum_filter_dvd_ge` (f_A >= −M ∀x ⇒
  f_{A∩qZ} >= −M ∀x, every q : ℕ), `card_sub_le_of_cosSum_ge` (|A| − q|A∩qZ| <= (q−1)M, q >= 2) and
  `card_le_of_no_multiples` (no multiples of q ⇒ |A| <= (q−1)M).
- KERNEL-CHECKED 2026-10-18 (Lean agent; lead re-ran `lake build` (8716 jobs OK), regenerated AxiomCheck.out (identical,
  61 lines, all [propext, Classical.choice, Quot.sound]), grep: no sorry/admit/native_decide/axiom): P16 lemmas M1–M4 in
  lean/ChowlaCosine/HalfSquare.lean — `cosSum_buSet_of_sidon` (f_{A(S)} = P^2 − k/2 − C/2 ∀x, S Sidon), `card_buSet`
  (|A(S)| = k(k−1)), `normalized_halfC_pow_four` ((1/2π)∫C^4 = 3k^2/4 − 3k/8), `visit_lemma` (|P| >= δ on [c−h,c+h] ⇒
  δ <= Σ sinc^2(b_s h/2)), `abs_halfC_sub_le` (Lipschitz), `halfSquare_lower_bound_of_visit` / `halfSquare_lower_bound`
  / `halfSquare_lower_bound_min` (P16 Chebyshev form: under Σ_s min(1, 4/((3s+½)h)^2) < √(ηk/2) and
  24π/(η^4 k^2) < 2r⌊2π/(2h+2r)⌋, r = η/(2(6L+1)), ∃x f_{A(S)}(x) < −(½−η)k).
  NOT formalized: the Lindström/Abel step Σ_s ḡ(|b_s|) <= Σbar(h) (so the explicit rate (L/k^3)^{1/6} is paper-only; the
  Lean theorem takes the frequency-wise majorant sum as a hypothesis, checkable per S), and the P16′ large-sieve form.
- NOT formalized: P7 admissibility count, P1 (Fejér–Riesz absent from mathlib), P6, P10–P12, P13(b–d), P14, gain identity.

## P9. Induced-subgraph (local spectral) lemma (PROVED, elementary)
For finite W ⊂ Z and real v on W: Σ_{u,w∈W} v_u v_w 1[u−w ∈ ±A] = (1/2π)∫ 2 f_A(x) |V(x)|^2 dx >= −2M(A) Σ v_u^2,
V(x) = Σ v_u e^{iux}. Hence M(A) >= −λ_min(Cay(Z,±A)[W])/2. Star case: I ⊂ ±A, (I−I)∩±A = ∅, v = sqrt|I| δ_0 − 1_I
gives M >= sqrt|I|/2. Turán: α(Cay[±A]) >= 2N/(d̄+1), d̄ = S3/(2N) => M >= N/sqrt(S3+2N).

## Gain identity (PROVED): for every spectral factor q of λ + f_A (λ = ||q||^2 >= M), with r = q ⋆ q̃,
Γ := Σ_{g≠0}|r(g)|^2 / Σ_{g≠0} Σ_{β−β'=g}|q_β|^2|q_β'|^2 and L := Σ|q_β|^4/λ^2 satisfy Γ(1−L) = N/(2λ^2).
(Numerator = N/2 by r = ½·1_{±A}; denominator = λ^2 − Σ|q|^4.)  P8 is Γ <= μ̄ (Cauchy–Schwarz).

## C½ (CONJECTURED, see NOTEBOOK 2026-10-17 late): M(A) >= sqrt|A|/2 for all finite nonempty A ⊂ Z_{>0}.

## P10. Sidon differences of B_3 sets: R >= (sqrt2-1)/sqrt2·... ≈ 0.293 (PROVED, paper; moment method)
Let D be a B_3 set (all 3-sums distinct up to order), |D| = k, A = (D-D)_+, N = k(k-1)/2, Y = |F_D|^2 on the circle.
EY = k, EY^2 = 2k^2 - k (Sidon), EY^3 <= 6k^3 (B_3: only trivial solutions). If Y >= (1-δ)k everywhere, Z = Y-(1-δ)k >= 0
and (EZ^2)^2 <= EZ * EZ^3 with EZ = δk, EZ^2 = k^2(1+δ^2) - k, EZ^3 <= k^3(2 + 3δ + δ^3) + O(k^2) give, to leading
order, (1+δ^2)^2 <= δ(2+3δ+δ^3) ⟺ 1 <= 2δ + δ^2 ⟺ δ >= sqrt2 - 1. Hence min Y <= (2 - sqrt2)k + O(1) and
M(A) = (k - min Y)/2 >= ((sqrt2-1)/2) k - O(1), i.e. R(A) >= (sqrt2-1)/sqrt2 · (1 - O(1/k)) = 0.2929...
Equivalent reformulation used for C½: R(D-D) >= 1/2 ⟺ min_x |F_D(x)|^2 <= (1 - 1/sqrt2)k(1+o(1)) for Sidon D.
Numerics (scratchpad sidon_flat.py, SA): best min|F_D|^2/k = 0.103 (k=5), 0.096 (6), 0.034 (8), 0.020 (10), 0.0041 (12),
0.0017 (16) — far below 0.293. Singer sets (all multipliers tried, q <= 101): min|F_D|^2/k <= 0.008.

## P11. B_h-difference sets: R(D-D) >= (1 - ε_h)/sqrt2 - o_h(1), ε_h -> 0 (PROVED, sketch at paper level)
D a B_h set (only trivial solutions of d_1+..+d_m = d'_1+..+d'_m, m <= h), Y = |F_D|^2: EY^m = m! k^m (1 + O_m(1/k)),
the moments of k·Exp(1). If Y >= ck everywhere, take q(y) = (y - ck)(1 - y/(Bk))^{2j} (degree 2j+1 <= h): q(Y) >= 0
pointwise, while E q(Y) = k E[(E-c)(1-E/B)^{2j}] + O(k/k) with E ~ Exp(1); with λ = 2j/B fixed > 1/c - 1 and
j -> ∞, (1-E/B)^{2j} -> e^{-λE} (dominated convergence on the Exp tail) and E[(E-c)e^{-λE}] = 1/(1+λ)^2 - c/(1+λ) < 0:
contradiction. So min Y <= ε_h k, M(D-D) >= (1-ε_h)k/2. Meaning: Sidon differences can beat 1/sqrt2 only through
additive relations of bounded length in D (structure), never through "generic" Sidon sets. Same mechanism expected
(not yet written) for the Bu class A(S): dissociated S => f ≈ (k/2)(Z^2-1) in moments => M >= (1/2 - ε)k.

## P12. C½ for dissociated two-sided (Bu-class) sets (PROVED at paper level; constants not optimised)
Setting: α_1..α_k distinct positive reals such that the k(k−1) numbers α_i ± α_j (i<j) are distinct positive
integers; A = {α_i − α_j, α_i + α_j}, so f_A = ρ^2 − Σ_j c_j^2 with c_j = cos(α_j x), ρ = Σ c_j (exact algebra).
Hypothesis Diss(D): every relation Σ_{i=1}^m ε_i α_{j_i} = 0 with m <= D, ε_i ∈ {±1}, is trivial (indices pair off
with opposite signs). (For Bu's α_j = 3s_j + 1/2: Diss(4) ⟸ S Sidon; Diss(6) needs S to be B_3-like, false for Singer.)
Claim: if Diss(2d+2) holds then M(A) >= (k/2)(1 − η_d) − O_d(1), where η_d = min_{deg q <= d} E[Z^2 q(Z)^2]/E[q(Z)^2]
(Z ~ N(0,1)), and η_d -> 0 as d -> ∞ (η_d ≍ (smallest Gauss–Hermite node)^2 ≍ 1/d). Hence R(A) >= (1/2)(1 − η_d) − o(1).
Proof. Average over x in a common period (half-integer α's: period 4π). For any polynomial P in c_1..c_k of degree <= D,
E_x P(c(x)) = E_iid P(cos θ_1, .., cos θ_k) EXACTLY (both sides expand into products of cosines; E_x of a product
2^{-m} Σ_ε 1[Σ ε_i α_{j_i} = 0] equals the iid value iff only trivial relations occur). Take the test measure
dμ = q(ρ/sqrt(k/2))^2 dx / E[q^2]: M >= −E_μ f = E_iid[(Σ c_j^2 − ρ^2) q^2]/E_iid[q^2] (f·q(ρ)^2 has degree 2d+2 <= D). In the iid
model Σ_j E[c_j^2 q(ρ)^2] = (k/2) E[q^2] + O_d(1)·E[q^2] (the c_j^2 − 1/2 terms interact with q(ρ) only through O(d)
coordinates), and E[ρ^2 q^2]/E[q^2] = (k/2)(E_G[Z^2 q^2]/E_G[q^2] + O_d(1/k)) by the moment CLT. Choose q optimal. □
Remarks: (i) η_d (even q; generalized eigenproblem on Gaussian moments): η_2 = 0.5505, η_4 = 0.3803, η_6 = 0.2906,
 η_8 = 0.2352, η_10 = 0.1975, η_12 = 0.1702, giving R >= 0.2247 (Diss(6), B_3-type S), 0.3098 (Diss(10)),
 0.3547 (Diss(14)), 0.3824 (Diss(18)), 0.4013 (Diss(22)), 0.4149 (Diss(26)); (ii) the analogous
statement for several blocks / any 0-1 PSD block matrix Q gives R >= 1/2 with equality iff Q = J (single block):
this is the rigorous form of H1 for degree-2 dissociated chaos; (iii) Bu's Singer-based S are Diss(4) only, so the
extremal examples lie OUTSIDE the class — C½ for them is not covered.

## P13. Even-part reduction for the Bu class (PROVED; numerically confirmed)
(a) For every finite A ⊂ Z_{>0} and q >= 1: (1/q) Σ_{j<q} f_A(x + 2πj/q) = f_{A ∩ qZ}(x), hence M(A) >= M(A ∩ qZ).
(b) Bu class: S ⊂ Z Sidon, α_j = 3s_j + 1/2, A = A(S) (|A| = k(k−1)). Then A ∩ 2Z = (S' − S')_+ with
    S' = {ε_j α_j}, ε_j = (−1)^{s_j}: a ∈ A is even iff a = 3|s_i − s_j| with s_i ≡ s_j (2) or a = |3(s_i+s_j)+1| with
    s_i ≢ s_j (2), i.e. exactly one frequency per pair, and these are the differences ε_iα_i − ε_jα_j. S' is Sidon
    (its differences are distinct elements of ±A), so f_{A∩2Z} = (|F_{S'}|^2 − k)/2 and
        M(A(S)) >= (k − min_x |Σ_j e^{i ε_j α_j x}|^2)/2.
    Explicit instance (x = π/2): F_{S'}(π/2) = e^{iπ/4} Σ_j (−1)^{⌊s_j/2⌋}, so M(A(S)) >= (k − (n_{0,1} − n_{2,3})^2)/2,
    n_{0,1} (n_{2,3}) = #{s ∈ S : s mod 4 ∈ {0,1} ({2,3})}.
(c) Numerics (certified Bu sets, examples/bu_reproduction_certified.json): M(A ∩ 2Z) = k/2 to 3 decimals for
    k = 12, 20, 40, 60, 80 (min |F_{S'}|^2/k < 1e-4; exact zero at x = π/2 for k = 80). So Bu's M = k/2 + excess with
    the k/2 coming entirely from the even part, which is a Sidon-difference set.
(d) Consequently: C½ for the whole Bu class (R(A(S)) >= 1/2 − o(1) for every Sidon S) follows from
    **Sidon near-zero conjecture (SNZ)**: for every Sidon set D of k reals in a common coset of Z (integers or
    half-integers), min_x |F_D(x)|^2 = o(k).  SNZ also gives R(D−D) -> 1/√2 for Sidon differences. P11 proves SNZ for
    B_h sets with h -> ∞; E8 supports it (best min|F_D|^2/k decreasing to 0.0017 at k=16).

## P14. Bedert–Shankar boundary bound: what averaging over t can and cannot give (PROVED at paper level by agent
## 2026-10-18, notes .research/agents/bedert_avg.md; lead re-derived (i) and (ii))
Setting (Bedert 2509.05260 v3 §7, Shankar 2609.05338 v1): A = −A ⊂ Z\{0}, n = |A|, F = 1̂_A ≥ −K on T = R/Z (K = 2M),
A_t = A ∩ (A+t), B_t = A_t \ (−A_t). Shankar: Σ_{t∈A}|B_t| >= T/3 >= n^2/(6K) (n >= 2K^2); Bedert: |B_t| << K^4 ⇒ K >> n^{1/5}.
(i) Abstract Prop 7.3. The proof uses only (38) and Lemma 7.2, so for EVERY t ≠ 0 and EVERY Q ∈ L^2(T):
    |B_t|^{1/2} <= 33.12 ||1̂_{B_t} − Q||_2 + 6.727 K ||Q||_1.   [(β−α)b^2 <= 2(α+γ)br + (α+γ)r^2 + 32K^2||Q||_1^2,
    β−α = 1/√2, α+γ = 11.536; solve in b = |B|^{1/2}.]  The method's output is the K-functional inf_Q(r^2 + K^2||Q||_1^2).
(ii) Localisation. Q = 1̂_{B_t} 1_{F >= λ} and Cauchy–Schwarz with weight F+K (∫(F+K) = K) give ||Q||_1^2 <= K|B_t|/(λ+K);
    λ = 181K^3 gives |B_t| <= 4388 ∫_{F<181K^3} |1̂_{B_t}|^2.
(iii) Refined bound: |B_t| <= 140416 L(A) + 8776 ||Q_{2,t}||_2^2, L(A) := ∫_{F<181K^3}(F+K)^2 <= 182K^4, hence
    n/(6K) <= 140416 L(A) + 8776 avg_{t∈A} ||Q_{2,t}||_2^2.   (★)
    Source (a) is t-INDEPENDENT: averaging cannot improve it. Any exponent gain needs L(A) << K^{4−δ} ("no middle layer:
    F+K carries o(K) L^1-mass at heights ≍ K^3") or non-saturation ∫_{F<CK^3} Σ_t |Q_{1,t}|^2 << nK^3, plus (b) averaged.
(iv) (b), partially: every piece of Q_2 with a factor T_2 = min(F,0) has Σ_{t∈Z} ||·||_2^2 <= C(n+K^4)K^2. Pure-T_1
    truncation remainders are NOT averaged (reduce to an additive-closure statement (S') for the spectrum {F > K^2}).
(v) [lead, 2026-10-18] The "no middle layer" statement FAILS in finite groups: in Z_N (N = product of distinct primes) let
    A = ∪_i (H_i \ {0}) for r subgroups of sizes ≈ r^3 and r of sizes ≈ r^10 (pairwise trivial intersections). Then
    F = Σ_i |H_i| 1_{H_i^⊥} − r, K = r, n ≈ r^11 >= K^4, and L(A) ≈ Σ_{|H_i| < C r^3} |H_i| ≈ r^4 ≍ K^4. So any proof of
    L(A) << K^{4−δ} must use torsion-freeness of Z (as must C½ itself, cf. E10). Heuristic reading: a middle layer in Z
    requires sub-structures that are themselves strong Chowla counterexamples (a possible induction-on-scales route; no
    rigorous decomposition of A along level sets of F is known).
Numerics (agent, uncertified floats): on every √n-family, avg ||Q_{1,t}||_1 ≈ 0.25K, so Σ_t ||Q_{1,t}||_1^2 << nK^{2−δ}
is FALSE; the weaker Σ_t ℓ_t^2 <= C(nK + K^4) (C ≈ 0.05–0.07) is consistent but untestable (n ≍ K^2 in all known sets).

## P15. Bu's construction is the square of a half-integer cosine sum (PROVED, one line; presumably implicit in Bu et al.)
For |w| = 1, |z|^2 + Re(w z^2) = 2 (Re(w^{1/2} z))^2. With G(x) = Σ_{s∈S} e^{3isx} and w = e^{ix}:
    (|G|^2 − k)/2 + Re(e^{ix} G^2)/2 = P(x)^2 − k/2,   P(x) = Σ_{s∈S} cos((3s + 1/2) x).
Expanding P^2 = k/2 + (1/2)C(x) + Σ_{s<t}[cos(3(s−t)x) + cos((3(s+t)+1)x)], C(x) := Σ_s cos((6s+1)x). For Bu's set
A(S) = {3|s−t|} ∪ {|3(s+t)+1|} (s<t; src/bu.py) this is the EXACT identity
    f_{A(S)}(x) = P(x)^2 − k/2 − C(x)/2,   hence   k/2 + max_{x: P(x)=0} C(x)/2  <=  M(A(S))  <=  k/2 + max_x C(x)/2·[P small].
So the excess M − k/2 is governed by the diagonal sum C at the real zeros of P (P is 2π-antiperiodic, so zeros exist);
for pseudo-random S, C at the zeros behaves like a sample of a √k-scale sum, matching the observed excess ≈ 1.3√k (E4) and
Bu et al.'s O(n^{1/4}√log n) error. The Bu class is {P^2 − const − C/2 : P a half-integer cosine sum with distinct
pairwise sums/differences}; C½ for the class ⟸ "some real zero of P has C >= −o(k)" (weaker-looking than SNZ, P13). Consequence (HEURISTIC): sums of several squares Σ_j P_j^2 − rk/2 give
R ≈ √r/2 · (1 − min Σ P_j^2/(rk/2)); with pseudo-random P_j the minimum of the χ^2_r-like sum gives R ~ √(log X), worse.
Beating 1/2 inside this template needs Σ_j P_j^2 >= δ rk/2 everywhere — a lower-flatness statement of SNZ type.

## P16. C½ for Bu's construction with any Sidon set of range L = o(k^3) (PROVED on paper by lead 2026-10-18;
## numerics src/bu_halfsquare.py, constants src/p16_constants.py; INDEPENDENTLY REVIEWED by agent 2026-10-18: CORRECT,
## no gap (.research/agents/p16_review.md); lemmas M1–M4 KERNEL-CHECKED 2026-10-18, Lindström step paper-only)
Review corrections (presentational): (M1) read "h := any h > 0 with Σbar(h) < δ" (the infimum is not attained; the
inequality is strict, so h* itself works). (M3) Bu et al.'s own sets have L ≈ 8–12 k^2 (up to ≈ 32 k^2 in their proof
regime), not L <= k^2; the rate k^{−1/6} is unaffected but the explicit table below is for L = k^2/2. (M6) Remark (c) needs
ALL sign patterns of quadruples (2+2−, 3+1−, 4+) to be trivial. "A(S) genuine" is equivalent to S being B_2 (incl. 2s = s'+s'').
Statement. Let S ⊂ Z ∩ [−L, L] be a Sidon set, |S| = k, such that A(S) = {3|s−t|} ∪ {|3(s+t)+1|} (s < t) is a genuine
set of k(k−1) positive integers (Bu et al.). Let 0 < η <= 1/2, δ := (ηk/2)^{1/2}, h := the least h > 0 with Σbar(h) < δ
(Σbar below), r := η/(2(6L+1)), n := ⌊2π/(2h+2r)⌋. If 2rn > 24π/(η^4 k^2), then M(A(S)) > (1/2 − η)k, so
R(A(S)) > 1/2 − η. Asymptotically: R(A(S)) >= 1/2 − O((L/k^3)^{1/6}); for L = O(k^2) (Bu's dense Sidon sets)
R >= 1/2 − O(k^{−1/6}) = 1/2 − O(N^{−1/12}). (Superseded quantitatively by P16′ below.) Explicit (L = k^2/2): R >= 0.230 (k = 1e6), 0.376 (1e8), 0.443 (1e10),
0.4735 (1e12). Together with Bu et al.'s upper bound, R(A(S)) -> 1/2 exactly along their family.
Notation. b_s = 3s + 1/2, P(x) = Σ_s cos(b_s x), T = {6s+1}, C(x) = Σ_s cos((6s+1)x); note P(x) = C(x/2).
Step 0 (identity, exact). 2cos(b_s x)cos(b_t x) = cos(3(s−t)x) + cos((3(s+t)+1)x) and cos^2(b_s x) = (1 + cos((6s+1)x))/2,
    so f_{A(S)} = P^2 − Σ_s cos^2(b_s x) = P^2 − k/2 − C/2.   (numerically 1e−8 on all certified Bu sets)
Step 1 (fourth moment, uses Sidon). Mean over [0,2π): E[C^4] = 2^{−4}#{(u_1..u_4) ∈ (±T)^4 : Σu_i = 0}. Writing
    u_i = σ_i(6s_i+1): Σσ_i ≡ 0 (mod 6) forces two + and two − signs, and then s_1+s_2 = s_3+s_4, so (Sidon) the − pair
    is a permutation of the + pair: count = 6(2k^2 − k). Hence E[C^4] = 3k^2/4 − 3k/8 (checked exactly by DFT, k <= 80).
    Chebyshev: |{x ∈ I : C(x) <= −τ}| <= 2π E[C^4]/τ^4 for every interval I of length 2π.
Step 2 (visit lemma, uses Sidon counting). Let φ be the triangle kernel of half-width h centred at c (φ >= 0, ∫φ = 1,
    φ̂(ν) = sinc^2(νh/2)). If |P| >= δ on [c−h, c+h], P has constant sign there, so δ <= |∫Pφ| <= Σ_s sinc^2(|b_s|h/2).
    The |b_s| are distinct (3(s+s') ≠ −1) and N(t) := #{s : |b_s| <= t} counts a Sidon set in <= 2t/3 + 4/3 consecutive
    integers, so N(t) <= α t^{1/2} + β t^{1/4} + γ (Lindström; α = (2/3)^{1/2}, β = (2/3)^{1/4}, γ = 1+(4/3)^{1/2}+(4/3)^{1/4}).
    With gbar(t) = min(1, 4/(th)^2) >= sinc^2(th/2) nonincreasing, Σ_s gbar(|b_s|) = ∫N(−gbar') <= ∫_{2/h}^∞ (αt^{1/2}+βt^{1/4}+γ)
    8/(h^2 t^3) dt =: Σbar(h) ≈ 1.54 h^{−1/2}. So every interval of half-length h (Σbar(h) < δ) contains y with |P(y)| < δ.
Step 3 (assume the conclusion fails: f_{A(S)} >= −(1/2−η)k everywhere). At a visit y: −(1/2−η)k <= δ^2 − k/2 − C(y)/2,
    i.e. C(y) <= 2δ^2 − 2ηk = −ηk. Since |C'| <= Σ_s|6s+1| <= k(6L+1), C <= −ηk/2 on [y−r, y+r], r = η/(2(6L+1)).
Step 4 (count). Windows [c_j − h, c_j + h], c_j = j(2h+2r), j < n, each contain a visit y_j; the intervals [y_j − r, y_j + r]
    are disjoint and lie in an interval of length <= 2π, so |{C <= −ηk/2}| >= 2rn. Step 1 with τ = ηk/2 gives
    |{C <= −ηk/2}| <= 24π/(η^4 k^2). If 2rn > 24π/(η^4k^2) this is a contradiction.  ∎
Asymptotics: h ≈ 2.4/δ^2 = 4.8/(ηk), n ≈ 0.66ηk, so the condition is ≈ 0.66η^2 k/(6L) > 75.4/(η^4 k^2), i.e. k^3 >~ 690 L η^{−6}.
Remarks. (a) Only Steps 1–2 use the Sidon property; no SNZ, no dissociation (contrast P12, P13). (b) The bottleneck is the
crude Lipschitz radius r ~ η/L; a local (typical-derivative) bound or higher moments of C (B_h-type S) extend the range
of L. (c) The same proof applies to any "half-integer square" f = P^2 − Q with P = Σcos(b_s x), b_s ∈ Z+1/2 and
{2|b_s|} having only trivial ± additive quadruples and Sidon-type counting near 0. (d) Mechanism: Q = Σcos^2(b_s x)
concentrates at k/2 (variance k/8 for ANY distinct |2b_s|), and a positive cosine sum cannot avoid small values on any
window of length >> 1/k; so at some near-zero of P, f ≈ −Q ≈ −k/2. This is the 1/2 of Bu's construction, rigorously.
P16 generalisations (same proof, paper level, lead 2026-10-18):
(G1) Dilate/shift family A_{q,r}(S) = {q|s−t|} ∪ {|q(s+t)+r|} (s<t), q >= 3, q ∤ 2r: use b_s = qs + r/2, C = Σcos((2qs+r)x).
     Step 1 needs Σσ_i(2qs_i + r) = 0 ⇒ rΣσ_i ≡ 0 (mod 2q) ⇒ Σσ_i = 0 (since q ∤ r, q ∤ 2r); Lipschitz |C'| <= k(2qL+|r|);
     counting N(t) <= #{s : |s| <= t/q + 1}. Same conclusion with 6L+1 replaced by 2qL+|r| and the counting constants rescaled.
(G2) Counting-function form: let h_S(δ) := inf{h > 0 : Σ_s sinc^2(|b_s|h/2) < δ}. If 2r⌊2π/(2h_S(δ) + 2r)⌋ > 24π/(η^4k^2)
     (δ = (ηk/2)^{1/2}, r = η/(2(6L+1))) then M(A(S)) > (1/2−η)k. Lindström gives h_S(δ) <~ 2.4/δ^2 for every Sidon S; for
     S spread out at scale L (N(t) ≈ kt/L) h_S ≈ k/(Lδ), and the condition holds for every L once k >> η^{-11}: only Sidon
     sets with a dense core near 0 AND range L >> k^3 escape the theorem.

## P16′. Large-sieve form of P16 (found by the review agent 2026-10-18; re-derived and constants recomputed by lead,
## src/p16prime_constants.py; PROVED on paper, two independent derivations)
Hypotheses as P16, D := 6L+1, 0 < θ < 1, δ := (θηk)^{1/2}, any 0 < h <= π/2 with Σbar(h) < δ, m := ⌊π/(2h)⌋.
If m (2(1−θ)ηk)^4 >= (4D + π/h)(3k^2/4 − 3k/8) then M(A(S)) > (1/2 − η)k.
Proof. Assume f_{A(S)} >= −(1/2−η)k. Windows [4hj−h, 4hj+h], j < m, contain visits y_j (|P(y_j)| < δ, Step 2); Step 3
gives C(y_j) < −2(1−θ)ηk. The y_j are 2h-separated mod 2π (4hm <= 2π). F := C^2 has the 4D+1 frequencies |ν| <= 2D and
Σ|F̂(ν)|^2 = E[C^4]; the large sieve (Selberg/Montgomery–Vaughan, δ_0-separated points, δ_0 = h/π) gives
Σ_j C(y_j)^4 <= (4D + π/h) E[C^4] < m(2(1−θ)ηk)^4, a contradiction.  ∎
Asymptotics (θ = 1/5): η ≈ (20.9 L/k^3)^{1/5}, so R(A(S)) >= 1/2 − O((L/k^3)^{1/5}); nontrivial from k ≈ 1.3e3 at
L = k^2/2. Explicit lower bounds on R(A(S)) (lead's recomputation = agent's table):
   k:          1e4     1e5     1e6     1e8     1e12
   L=k^2/2:    0.209   0.328   0.395   0.459   0.4936
   L=12.5k^2:  —       0.177   0.302   0.423   0.4879     (Bu et al.'s typical range)
   L=32k^2:    —       0.112   0.261   0.407   0.4854
Gain over P16: the depth C(y_j)^4 is used directly instead of a Lipschitz neighbourhood (one factor of η).
(I3, agent, PROVED as a lemma; application CONDITIONAL) Density visit lemma: N(t) <= ρt + E ⇒ windows of half-length
h > 4ρ/(δ−E) contain visits. For spread S (ρ ≍ k/L, E = O(1)) L cancels and η ≍ k^{−1/3} for every L; applying it to
Bu's random thinnings needs a w.h.p. counting bound near 0 (not verified).
Literature: Bu et al. 2610.17160v1 do not prove a matching lower bound (their Remark 8.5: sharpness "we do not prove");
P16/P16′ rule out improving their identity-based route (their Remark 8.4) for L = o(k^3).

## P17. Rigorous upper bounds for the doubly-positive profile constant ρ* (PROVED, elementary; lead 2026-10-18)
ρ(w) := ∫w^2/(w(0)∫w) over continuous integrable even w: R → [0,∞) with ŵ >= 0 (so 0 <= w <= w(0) = 1 after scaling).
(a) ρ* <= 0.9057 for the whole class. Proof: the Gram matrix of {0, t, 2t} is PSD, det = (1−w(2t))(1+w(2t)−2w(t)^2) >= 0,
    so w(t) <= sqrt((1+w(2t))/2) <= a + b w(2t) (tangent at y0 = 0.64: b = 1/(2 sqrt(2(1+y0))) = 0.27608, a = 0.72885).
    Multiply by w(t) >= 0 and integrate; Cauchy–Schwarz ∫w(t)w(2t)dt <= ||w||_2^2/√2. Hence (1 − b/√2)||w||_2^2 <= a∫w,
    ρ <= a/(1 − b/√2) = 0.90565.  ∎
(b) ρ <= 0.76980 on the subclass w = h⋆h̃ with h >= 0: Beckner's sharp Young inequality ||h⋆h̃||_2 <= A_{4/3}^2 ||h||_{4/3}^2
    (A_{4/3}^2 = (4/3)^{3/4}/4^{1/4} = 0.87738) and Hölder ||h||_{4/3}^2 <= ||h||_1 ||h||_2, with ||h||_1^2 = ∫w, ||h||_2^2 = w(0).
    Strict (Beckner's equality needs Gaussians, Hölder's needs |h| constant on its support).  ∎
Numerical sup (E16, src/profile_opt.py): 0.7239 (h >= 0), 0.7245 (signed). Relevance: under symmetric rounding
(c_E = √2) dense sets have R ≈ sqrt(1−ρ), so beating 1/2 that way needs ρ > 3/4; (b) comes within 0.02 of excluding it
for h >= 0 profiles, (a) does not. Neither bound is needed elsewhere; recorded so the constant is not re-derived.
