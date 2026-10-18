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
- NOT formalized: P7 admissibility count, P1 (Fejér–Riesz absent from mathlib), P6, P10–P13, gain identity.

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
Claim: if Diss(2d+4) holds then M(A) >= (k/2)(1 − η_d) − O_d(1), where η_d = min_{deg q <= d} E[Z^2 q(Z)^2]/E[q(Z)^2]
(Z ~ N(0,1)), and η_d -> 0 as d -> ∞ (η_d ≍ (smallest Gauss–Hermite node)^2 ≍ 1/d). Hence R(A) >= (1/2)(1 − η_d) − o(1).
Proof. Average over x in a common period (half-integer α's: period 4π). For any polynomial P in c_1..c_k of degree <= D,
E_x P(c(x)) = E_iid P(cos θ_1, .., cos θ_k) EXACTLY (both sides expand into products of cosines; E_x of a product
2^{-m} Σ_ε 1[Σ ε_i α_{j_i} = 0] equals the iid value iff only trivial relations occur). Take the test measure
dμ = q(ρ/sqrt(k/2))^2 dx / E[q^2]: M >= −E_μ f = E_iid[(Σ c_j^2 − ρ^2) q^2]/E_iid[q^2] (degree 2d+2 <= D). In the iid
model Σ_j E[c_j^2 q(ρ)^2] = (k/2) E[q^2] + O_d(1)·E[q^2] (the c_j^2 − 1/2 terms interact with q(ρ) only through O(d)
coordinates), and E[ρ^2 q^2]/E[q^2] = (k/2)(E_G[Z^2 q^2]/E_G[q^2] + O_d(1/k)) by the moment CLT. Choose q optimal. □
Remarks: (i) d = 2 already gives η ≈ 0.55 (q = 1 − 0.18 Z^2), i.e. R >= 0.22 for B_3-type S; (ii) the analogous
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
