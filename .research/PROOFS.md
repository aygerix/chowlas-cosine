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
- KERNEL-CHECKED 2026-10-18 (Lean agent; lead re-ran `lake build` (8717 jobs OK), regenerated AxiomCheck.out (identical,
  85 lines, all [propext, Classical.choice, Quot.sound]), grep: no sorry/admit/native_decide/axiom): **P16 unconditional,
  explicit** in lean/ChowlaCosine/HalfSquareExplicit.lean —
    theorem halfSquare_lower_bound_explicit (S : Finset ℤ) (hS : IsSidon S) (L : ℝ) (hL : ∀ s ∈ S, |(s:ℝ)| ≤ L)
      (hL1 : 1 ≤ L) (η : ℝ) (hη : 0 < η) (hη' : η ≤ 1/2) (hk : 1000 * (6 * L + 1) ≤ η ^ 6 * (S.card : ℝ) ^ 3) :
      ∃ x : ℝ, cosSum (buSet S) x < -((1/2 - η) * S.card)
  (and the corollary with hk : 7000 * L ≤ η^6 k^3). I.e. R(A(S)) > 1/2 − η whenever η^6 k^3 >= 7000 L: the P16 rate
  (L/k^3)^{1/6}, with the trivial Sidon count k(k−1) <= 2·diam (Lindström not needed) and h = 64/(3ηk) inside the proof.
  Supporting lemmas: sidon_card_mul_pred_le_of_Ico, card_filter_abs_half_le (N(N−1) <= 4u/3 for |3s+½| <= u),
  sum_min_le_sidon (Σ_s min(1, 4/((3s+½)h)^2) <= 1 + (4/3)sqrt(8/(3h))), halfSquare_hcond_explicit.
  Still paper-only: Lindström's sharper count.
- KERNEL-CHECKED 2026-10-18 (Lean agent #2; lead forced re-elaboration `lake env lean ChowlaCosine/HalfSquareSieve.lean`
  (OK), `lake build` (8718 jobs OK), regenerated AxiomCheck.out from scratch (byte-identical to agent's; 103 axiom lines,
  all [propext, Classical.choice, Quot.sound]); grep: no sorry/admit/native_decide/axiom; only new def halfS): **P16′
  (exponent 1/5), Gallagher-sieve form**, lean/ChowlaCosine/HalfSquareSieve.lean —
    theorem halfSquare_lower_bound_sieve (S : Finset ℤ) (hS : IsSidon S) (L : ℝ) (hL : ∀ s ∈ S, |(s:ℝ)| ≤ L)
      (hL1 : 1 ≤ L) (η : ℝ) (hη : 0 < η) (hη' : η ≤ 1/2) (hk : 600 * (6 * L + 1) ≤ η ^ 5 * (S.card : ℝ) ^ 3) :
      ∃ x : ℝ, cosSum (buSet S) x < -((1/2 - η) * S.card)
  (corollary: 4200·L ≤ η^5 k^3). I.e. R(A(S)) > 1/2 − η whenever η^5 k^3 >= 4200 L: rate (L/k^3)^{1/5}, C0 = 600 not
  optimised (agent estimate ≈ 100 with θ = 1/5). Route: Gallagher's inequality instead of Montgomery–Vaughan —
  gallagher_local, gallagher_sum (needs every window [y_j − δ0/2, y_j + δ0/2] inside ONE period window [c0, c0+T]);
  integral_halfC_sq_mul_halfS_sq_le (∫C^2 C'^2 <= D^2 ∫C^4, frequencies ≡ 1 mod 6, no Sidon needed);
  integral_abs_halfC_cube_mul_halfS_le (∫|C^3 C'| <= D ∫C^4, AM–GM); sieve_halfC_pow_four
  (Σ_{j<m} C(y_j)^4 <= (1/δ0 + 4D)∫_0^{2π}C^4); θ = 1/2, h = 64/(3ηk), δ0 = 2h, m = ⌊π/(2h)⌋ visits; hidden lower
  bound η^4k^2 >= 600 comes from the Sidon count k(k−1) <= 4L (sieve_numerics). Report .research/agents/lean_p16_sieve.md.
  CORRECTION found by formalization: the lead's Gallagher sketch (brief, Step A) let the windows I_j sit in a window of
  length 2π + δ0 and folded by periodicity — that double-counts the overlap; the correct hypothesis is containment in a
  single period window, which Step D satisfies exactly (centres 4hj, δ0 = 2h, c0 = −2h, 4hm <= 2π). Conclusion unaffected.
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
## no gap (.research/agents/p16_review.md); lemmas M1–M4 and the unconditional explicit form (η^6k^3 >= 7000L) KERNEL-CHECKED 2026-10-18; P16′ (Gallagher form, η^5k^3 >= 4200L) KERNEL-CHECKED 2026-10-18)
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
## src/p16prime_constants.py; PROVED on paper, two independent derivations; Gallagher-sieve form with C0 = 600
## KERNEL-CHECKED 2026-10-18, lean/ChowlaCosine/HalfSquareSieve.lean)
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

## P18. Dense min–max lemma: Chowla for dense sets whose positive-definite residual is upper-flat (PROVED; lead 2026-10-18)
Statement. Let A ⊂ [1, X], f = f_A >= −M on R. Let W = (W_n)_{1<=n<=X} be real with Ŵ(x) := Σ_n W_n cos(nx) and
||Ŵ'||_{L^1[0,2π]} <= βX, and put G := f − Ŵ = Σ_n e_n cos(nx), e_n = 1_A(n) − W_n. If max_x |G(x)| <= Λ, then
    π Σ_n n^2 e_n^2 <= X Λ (2πXM + βX),   i.e.   M >= Σ n^2 e_n^2 / (2 X^2 Λ) − β/(2π).
Proof. Bernstein in L^1 for the nonnegative degree-X trig polynomial f + M: ||f'||_1 <= X||f + M||_1 = 2πXM. Hence
||G'||_1 <= 2πXM + βX. Bernstein in sup: ||G'||_∞ <= X Λ. And ||G'||_2^2 = πΣ n^2 e_n^2 <= ||G'||_∞ ||G'||_1.  ∎
Admissible W: if W extends to a positive-definite sequence on Z with W_0 <= 1 (so W_0 + 2Ŵ >= 0), Bernstein in L^1
applied to Ŵ + W_0/2 >= 0 gives ||Ŵ'||_1 <= πX W_0, so β = π works.
Reading. For dense A (N >= αX) with a p.d. profile W and residual mass Σe_n^2 >= γN spread over [1, X]
(Σ n^2 e_n^2 >= c X^2 Σ e_n^2), upper-flatness Λ = λ√X gives M >= (cγα^{1/2}/(2λ))·√N − 1/2: Chowla for that A.
Random dense A and Bu sets have Λ ≈ √(X log X) off the main spike, so the lemma recovers M >~ √(N/log N) for them;
the hypothesis fails exactly when the residual has secondary spikes (large Fourier coefficients of 1_A − W at
minor-arc frequencies) — the multi-level structures of NOTEBOOK session 2. Open pieces: (a) a finite/discrete version
of ||1_A − W||^2 >= (1 − ρ* − o(1))N for every p.d. W with 0 <= W <= 1 (the doubly-positive bound, P17/E16); (b) a way to
charge secondary spikes of the residual to uncompensated negative lobes (maximality of W). (a)+(b) would give
Chowla up to √log for dense sets — a target, not a result. Note the L^∞ hypothesis must hold on the major arc too
(where G is the profile-approximation error).

## P19. Bedert's run-top bound |B_t| << K^4 is sharp for degree-2 methods (agent "runtop" 2026-10-18; report
## .research/agents/runtop_report.md; proof read by lead, key identity re-derived by hand; lead's independent numeric
## check src/p19_thmA_check.py: min f_t∗f_t ≈ −3.4√(N log N), |B_t|/K_*⁴ ≈ 0.05 for N = 2e3..3.2e4, t = 1, 3)
Setting: A = −A ⊂ Z\{0}, F = 1̂_A, G = F + K, B_t = {m ∈ A : m − t ∈ A, m + t ∉ A}, f_t = 2(1 + sin 2πtx)F.
Identity (lead re-derived): f_t∗f_t = (4 − 2cos 2πtx)F + 2e(−tx)1̂_{A∩(A+2t)} + 8 Im 1̂_{A∩(A+t)}.
Theorem A (OBSTRUCTION, PROVED by agent; probabilistic, explicit constants). For N >= 2.4e6, 1 <= t <= √N, random symmetric
A ⊂ [−N,N] with P(j ∈ A) = h(W(j/N)), W(u) = (1−|u|)_+/2, 2h + 2h² = w (so E[coefficients of f_t∗f_t] = Fejér profile
+ O(t/N)), satisfies with probability >= 1/2: f_t∗f_t >= −16K_*² on T with K_*⁴ <= 21 N log N (so Bedert's (37)/(38) hold
with K = K_*), the norm conclusions of Lemma 7.1 hold (Q_1 = 0), |B_t| >= 0.0055N >= 6.6e-5 K_*⁴/log K_*, and
inf_Q (||1̂_B − Q||² + K_*²||Q||_1²) >= c|B_t| (no test function helps). What fails is only degree-1 information: F >= −K_*,
||F||_1 <= 2K_*, |Q_1| <= 4G.
Theorem B (PROVED by agent). For ANY finite family of A-independent inequalities w·((m_1G + m_1'K)∗(m_2G + m_2'K)) >= 0
(w, m nonnegative trig polys in tx) random sets satisfy all of them with K_* ≍ (N log N)^{1/4}, |B_t| ≍ N; r-fold
convolutions cap at K^{2r}. With the degree-1 no-gap barrier (NOTEBOOK; audited CORRECT, extends to any frequency support
of an A-independent multiplier): every "pointwise gap inequality + test function" proof is capped at K^4.
Proposition C (agent, arb-certified single points): the K² in (37) is attained by genuine sets (Singer q=31: −0.668K²,
q=53: −0.590K², Erdős–Turán p=59: −0.511K², with K <= |D|), so the constant term cannot be o(K²).
Proposition M (PROVED by agent from (38) + Lemma 7.2): |B_t| <= 4388 ∫ min(|1̂_{B_t}|, 13.46 K|B_t|^{1/2})² — the exact power
of the method. TARGET LEMMA S (OPEN): ∫ min(|1̂_{B_t}|, K³)² <= C K^{4−δ} under F >= −K; δ = 1 gives Chowla exponent 1/4
(with Shankar). It fails for the Theorem A sets, so it must use F >= −K at degree 1. Splits into (S1) little L² mass of
1̂_{B_t} below height K² and (S2) meas{|1̂_{B_t}| >= s} << K^{1−δ}/s for K² <= s <= K³.
Groups: Prop 7.3 holds in every finite abelian group and bounds in all Z_N transfer to Z; unions of subgroups and an F_3^d
family give |B_t| <~ K² (PROVED for those classes). OPEN: does some finite group have |B_t| >> K^{2+ε}? (If yes, Lemma S
must use torsion-freeness.) ANSWERED (P20): YES, |B_t| = K²(K−1) in F_p^{1+3a}; the group
exponent window is [3, 4]. By-product (agent, elementary): fibre domination |1̂_{S_r}(θ)| <= K + 1̂_{S_0}(θ) for residue
fibres S_r = {s : r + st ∈ A}.
Conjecture G (2026-10-18, lead; evidence E30). There is an absolute C such that for every finite abelian group Γ, every
symmetric A ⊂ Γ\{0} with F = 1̂_A >= −K on Γ̂, and every t ∈ Γ: |B_t| <= C·K² (B_t = {m ∈ A : m − t ∈ A, m + t ∉ A}).
Consequence: by the transfer Z -> Z_N (P19) |B_t| <= CK² in Z for every t, and with Shankar's averaging
(max_t|B_t| >= T/(3n) >= n/(3K) − K/3, Roth T >= n²/K − nK) this gives K >= (n/(3C))^{1/3} − O(1): Chowla exponent 1/3.
Status: OPEN; Paley sets show C >= 1/2 is needed; P19 shows it cannot be proved by degree-2 gap inequalities (and
degree-r Fourier manipulations cap at K^{2r}), so it needs structural (degree-1 / additive-combinatorial) input. In Z the
statement follows from C½ (|B_t| <= n <= K²), so it is a strictly weaker, finite-field-model target.
**REFUTED 2026-10-18 (P20 Theorem 1; agent conjG, lead-verified with an independent construction, E31):** in F_p^4 the
complement of an elliptic quadric with isotropic t has K = p, |B_t| = p²(p−1) = K²(K−1). G in Z is untouched (it follows
from C½); the route "G in all groups ⇒ exponent 1/3" is dead.

## P20. Run-tops in finite abelian groups: Conjecture G is false, the group exponent is in [3, 4] (agent "conjG"
## 2026-10-18, report .research/agents/conjG_report.md; Theorem 1 lead-verified (E31, independent construction);
## Theorem 2 and Lemma 3 proofs checked line by line by lead; Theorem 4 / Prop 5 read, not re-derived)
Setting: Γ finite abelian, A = −A ⊂ Γ\{0}, F = 1̂_A real, K = −min F, B_t = {m ∈ A : m − t ∈ A, m + t ∉ A}.
Theorem 1 (PROVED on paper by agent; NUMERICAL-EXACT for 9 (p,a), lead-confirmed for F_p^4, p <= 13). For every odd p,
a >= 1, q = p^a, Γ = F_p × F_q × F_{q²}, t = (1,0,0): A = {(s,r,w) : r ≠ 0, s ≠ Tr(w²/(θr))} ∪ {(s,0,w) : Tr(θw²) ≠ 0}
(θ chosen with η(θ)·Σ_w e_p(Tr w²) = −q) has min F = −q and |B_t| = (q−1)q² = K²(K−1). Spectrum {−q, (p−1)q, q(q−1)}.
Mechanism: every t-line with r ≠ 0 misses A in exactly one point (one run, one top); after the w-sum the phase
Tr(w²/(θr)) becomes F_p-linear in r (dual of a vectorial bent map), so the j ≠ 0 slices are two-valued; fibres over r = 0
are empty/full and repair the degree-0 slice. Simplest form (lead, E31): A = {x ∈ F_p^4 : x1x2 + x3² − d x4² ≠ 0}
(d a non-residue), t = e1 isotropic: Q is affine on each t-line, so lines with x2 ≠ 0 lose exactly one point.
Theorem 2 (PROVED; lead checked). ord t = 3, χ0(t) = ω, H̄ = Γ/⟨t⟩, U(y) = Σ_{x∈A∩y} χ0(x). Û(φ) = F(χ0φ) >= −K, so
U + Kδ0 is p.d. on H̄, hence so is its cube; U³ = ρ(1_E − 1_D) off y = 0 (ρ = χ0³ ∈ Ĥ̄; D = 2-point cosets = run-tops,
E = singleton cosets). Evaluating at ρ̄: |D| − |E| <= (K + u0)³, u0 = U(0) ∈ {0, −1}. So |B_t| <= K³ if E = ∅ (sharp
by Theorem 1 with p = 3).
Lemma 3 (PROVED; lead checked). If all ⟨t⟩-cosets over a subgroup V̄ of index m are empty/full, |D| + |E| <= (m−1)K²
(Û sums to 0 on each V̄^⊥-coset; Σx_i² <= m(m−1)K² for x_i >= −K, Σx_i = 0; Parseval). Equality in Theorem 1.
Theorem 4 (agent). In Z_3 × H with 3 ∤ |H| equality in Lemma 3 forces m <= 2 (Galois: U real ⇒ degree-0 contradiction):
the exact extremal mechanism needs p-torsion outside ⟨t⟩. Prop 5 (agent): if S0 ∪ {0} is a subgroup, |B_t| <= 8K² + 3K.
Barriers (agent, PROVED): (i) every "Σ_h product of p.d. fibre atoms" inequality has monomials equal to 1 on singleton
fibres, so it bounds |D| − c|E|, never |D| alone; (ii) arguments seeing only real-reduced fibre data (1_E − 1_D,
1_E + 2·1_D + 3·1_F) are capped at K⁴ (partial-spread example). (iii) Group form of Lemma S fails for every δ > 1.
Consequences: any group-agnostic run-top bound is >= K³ (so the run-top + Shankar route gives at best exponent 1/4
unless it uses torsion-freeness / interval structure); G3 (|B_t| <= CK³ in all groups, or just in Z) would give
exponent 1/4 (> Shankar's 1/5). Novelty: not checked (likely related to two-weight codes / strongly regular Cayley graphs).

## P21. Full cosets are not needed: |B_t| = K³/27 with every t-coset a single (p−1)-run (lead 2026-10-18; PROVED,
## elementary; NUMERICAL check E33 for p = 3..23: K = 3p and |B_t| = p³ exactly)
Theorem. Let p be an odd prime, d a non-residue, N(v) = v3² − d v4², Γ = F_p^4, t = e1, and
    A = {x : x2 ≠ 0, x1x2 + N(x3,x4) ≠ 0} ∪ {x : x2 = 0, x1 ≠ x3·x4²}.
Then A = −A, 0 ∉ A, every ⟨t⟩-coset meets A in exactly p − 1 points (no full cosets; no singleton cosets for p >= 5),
F(χ) >= −3p for every nontrivial χ, and |B_t| = p³. Hence |B_t| >= K³/27 and |B_t|/K² >= p/9 -> ∞.
Proof. Symmetry: both conditions are invariant under x -> −x (N even; x3x4² odd), and x = 0 has x2 = 0, x1 = 0 = x3x4².
Each line {x + st} with x2 ≠ 0 misses exactly x1 = −N/x2; each line with x2 = 0 misses exactly x1 = x3x4². A cyclic run
F_p \ {τ} has exactly one top (m = τ − 1: m − 1 = τ − 2 ≠ τ as p >= 3, m + 1 = τ ∉ A), so |B_t| = #lines = p³.
Characters χ = e_p(jx1 + kx2 + c·v). j = 0: every line has p − 1 points, so F = (p−1)·Σ_{x2,v} e_p(kx2 + c·v) = 0 for
(k,c) ≠ 0. j ≠ 0: a line missing τ contributes −e_p(jτ)·χ(line). The x2 ≠ 0 part: for α = −j/x2,
Σ_v e_p(αN(v) + c·v) = η(α)η(−αd)g² e_p(−N*(c)/(4α)) = −p·e_p(N*(c)x2/(4j)) (g² = η(−1)p, η(d) = −1,
N*(c) = c3² − c4²/d), so this part equals p(p·[k + N*(c)/(4j) = 0] − 1) ∈ {−p, p(p−1)} (the E31 / P20 bulk). The x2 = 0
part is −ĝ_j(c), ĝ_j(c) = Σ_{v3,v4} e_p(j v3v4² + c3v3 + c4v4) = p·Σ_{v4 : j v4² = −c3} e_p(c4v4) ∈ [−2p, 2p] (real:
at most two roots ±u). So F >= −p − 2p. ∎
Meaning. The P20 mechanism (Theorem 1) repairs the degree-0 slice with full cosets; here it is repaired by making all
fibres the same size (c ≡ p − 1, so ĉ = 0), at the price of a second Gauss-type sum over the q²-point subspace x2 = 0,
which is O(p) = O(K). Conjecture G_noFull (NOTEBOOK; "no ⟨t⟩-coset inside A ⇒ |B_t| <= CK²") is REFUTED; |B_t| ≍ K³ is
attained with no full and no singleton cosets, matching Theorem 2's |D| <= |E| + K³ (E = ∅) up to the factor 27.
Diagnosis (PROVED part / HEURISTIC part). Along t, each fibre I = F_p \ {τ} has transform Σ_{s∈I} e_p(js) = −e_p(jτ) for
every j ≠ 0: a NEGATIVE-DEFINITE fibre (up to the phase). A symmetric fibre I ⊂ Z_ℓ with 0 ∉ I whose transform is <= 0
at all j ≠ 0 must have |I| >= ℓ/2 (PROVED: |I|/ℓ − 1_I is p.d., so |I|/ℓ >= |I|/ℓ − 1_I(s)... i.e. |I|/ℓ >= 1 − |I|/ℓ on I),
so every run-top in such a fibre sits on a run longer than half the cycle. Both known K³ mechanisms (P20 Thm 1, P21)
use runs of length p − 1 = ord(t) − 1. In Z (and in its Z_N transfer) every maximal t-run has length <= 2X/t + 1 < ord(t)/2,
and its transform along t is a Dirichlet kernel with main lobe +ℓ and side lobes ≈ −0.22ℓ (HEURISTIC: sign changes force
a Gibbs penalty). Refined target G_arc: |B_t| <= CK^{2 or 3} whenever every maximal t-run has length <= ord(t)/2.
Lean: KERNEL-CHECKED 2026-10-18. Formalization agent; lead re-ran `lake build` (8720 jobs OK) and AxiomCheck on dirichlet:
109 lines, all [propext, Classical.choice, Quot.sound], no sorry. Theorem statements are byte-identical to the lead's
statement file. lean/ChowlaCosine/RunTopGroup.lean proves: runSet_neg (A = −A), zero_not_mem_runSet, card_line_inter
(p − 1 points per t-line), card_runTops (|B_t| = p³) and charSum_lower (for ψ primitive and c ≠ 0, F real and >= −3p).
Not formalized: (i) that (ψ, c) runs over all nontrivial characters (standard); (ii) attainment of −3p.
The negative-definite fibre lemma (ℓ <= 2|I|) is KERNEL-CHECKED too, in lean/ChowlaCosine/NegDefFibre.lean
(le_two_mul_card_of_negDef). Report: .research/agents/lean_p21_report.md.

## P22. The group exponent of run-tops is exactly 4 (Theorem O4, agent "g3" 2026-10-18; report
## .research/agents/g3_report.md §2; paper proof checked line by line by lead; NUMERICAL-EXACT, lead-independent E36)
Setting as in P20. G3 (|B_t| <= CK³ in every finite abelian group) is FALSE, and so is any group-agnostic K^{4−δ}.
Theorem O4 (PROVED). a >= 3 odd, R = GR(4, a) (Galois ring: |R| = 4^a, (R,+) ≅ Z_4^a, R^× = R \ 2R), Γ = Z_4 × R,
t = (1, 0). T = Teichmüller set (|T| = 2^a, lifts of F_{2^a}). S(y) = Σ_{x∈T} i^{Tr(xy)}; for y ∈ R^×,
conj S(y) = 2^{(a−1)/2}(1+i)·i^{k(y)} defines k(y) ∈ Z_4. W̄ ⊂ F_{2^a} an F_2-hyperplane, F₀ = {2u : ū ∈ W̄ \ 0}.
    A = {(s, y) : y ∈ R^×, s ∈ {k(y), k(y)+1}} ∪ (Z_4 × F₀).
Then A = −A, 0 ∉ A, K = 2^{(a+1)/2}, |B_t| = 4^a − 2^a = K⁴/4 − K²/2.
Proof (lead re-derived every step).
- Lemma T: τ(α) + τ(β) = τ(α+β) + 2τ(√(αβ)) (square both sides; 4 = 0 kills cross terms of the 2-part; compare with
  Frobenius). Hence x − x′ = τ(x̄ + x̄′) + 2τ(√(x̄x̄′) + x̄′), and every unit is a difference of T in exactly one way
  (x̄ū = ν² + ū² has one solution), no nonzero element of 2R is one: T is a (2^a, 2^a, 2^a, 1) relative difference set.
- Lemma S: S = 0 on 2R \ 0; |S|² = 2^a + Σ_{u∈R^×} i^{Tr(uy)} = 2^a on R^× (the 2R-sum is 2^a[ȳ = 0]); S ∈ Z[i] of norm
  2^a ⇒ S = unit·(1+i)^a = unit·(2i)^{(a−1)/2}(1+i). S(−y) = conj S(y) ⇒ k(−y) = −k(y) − 1 ⇒ A_{−y} = −A_y.
- Fibres A_y (along t): the 2-run {k(y), k(y)+1} on R^×, Z_4 on F₀, ∅ else. Characters χ_{j,λ} = i^{js + Tr(λy)}.
  j = 2: a 2-run, a full and an empty fibre all have Σ(−1)^s = 0 ⇒ F ≡ 0. j = 1: U_1 = conj S/2^{(a−1)/2} on R^×, and
  Σ_{y∈R} conj S(y) i^{Tr(λy)} = 4^a[λ ∈ T] ⇒ F(1, λ) = 2^{−(a−1)/2}(4^a[λ ∈ T] − 2^a) ∈ {−K, K(2^a − 1)}; j = 3 by
  symmetry. j = 0: fibre sizes 2 on R^×, 4 on F₀ ⇒ F(0, λ) = −4 (λ ∈ 2R \ 0) or 4(2^{a−1}[tr(λ̄·)|W̄ ≡ 0] − 1).
  So min F = −max(4, K). Each 2-run has one top, full/empty none: |B_t| = |R^×|. ∎
Proposition O4⁺ (PROVED, agent; lead checked). Any Γ, ord t = 4, χ₀(t) = i, U(y) = Σ_{x∈A∩y} χ₀(x) on H̄ = Γ/⟨t⟩:
U + Kδ₀ p.d. ⇒ (U + Kδ₀)⁴ p.d. (Schur); U⁴ρ̄ (ρ = χ₀⁴ ∈ Ĥ̄) equals (Σ_{s∈S} i^s)⁴ = −4 on 2-runs, +1 on singletons and
3-runs, 0 on {k, k+2}, full, empty. Hence 4|D₂| <= |E| + |D₃| + (K + u₀)⁴, u₀ ∈ {0, −1}; O4 is extremal (E = D₃ = ∅).
Upper side: Bedert Prop 7.3 (|B_t| << K⁴) holds in every finite abelian group. So the group exponent of |B_t| is EXACTLY 4.
Averaged form (lead, E36b, NUMERICAL-EXACT a = 3, 5, 7): in O4, (1/|A|)Σ_{t∈A}|B_t| = 30.97, 511, 8191 = K⁴/8 − O(K²)
(every t ∈ A of order 4 has |B_t| ∈ {29,33,56}, {497,525,992}, {8129,8253,16256}). So also the A-AVERAGED run-top count
used in Shankar's chain has group exponent 4: run-tops in O4 are as frequent as for a random set of density 1/2.
Consequences (PROVED, modulo the transfer bookkeeping of the barrier note §1):
- Every bound on |B_t| or on its A-average that holds in all finite abelian groups is >= K⁴/8 − O(K²); the Bedert/Shankar
  exponent 1/5 is the limit of the run-top route unless the run-top bound itself uses Z (order, intervals, absence of
  torsion). P20/P21's K³ window is closed from above: [3, 4] → {4}.
- O4 has |A| ≈ 2·4^a, so K ≈ (2|A|)^{1/4}: a symmetric set in an exponent-4 group, with no subgroup structure, whose minimum
  is |A|^{1/4}. Runs have length exactly ord(t)/2 = 2. In Z (and its Z_N transfer) every t-run is < ord(t)/2 − 1, so
  G_arc with strict inequality and G3 in Z stay OPEN. But in Z, |B_t| <= |A| and Chowla itself would give |B_t| <= CK², so
  "G3 in Z" is a weakening of Chowla, not an independent lemma: progress on it needs genuinely Z-specific input.
Novelty: not checked (the RDS is classical: quaternary Kerdock / Family A sequences; its use here appears new).

## P23. λ-fold near-rulers (agent "lambda" 2026-10-18; report .research/agents/lambda_report.md; T2 and T5 proofs checked
## by lead; T1, T3, T4 read; exact optima for k = 6..11 reproduced by the lead's independent enumerator, E39)
Setting: D ⊂ Z, |D| = k, r(d) = #{(u,v) ∈ D² : u − v = d}, A = {d > 0 : r(d) = λ}, def = Σ_{d>0, r(d) ∉ {0,λ}} r(d),
W = 2·def, φ = λ|A|/C(k,2) = 1 − def/C(k,2). Identity 2λf_A = |F_D|² − k − E, |E| <= W (NOTEBOOK evening entry).
- T1 (PROVED, agent): for λ >= 3, W >= 6, and def ≡ C(k,2) (mod λ). Tight at k = 3, 4, 6.
- T2 (PROVED; lead checked). If D = c − D (reflection-symmetric), exactly ⌊k/2⌋ difference classes have odd r.
  - Proof: the involution (u,v) ↦ (c−v, c−u) preserves u − v. Its fixed pairs are (u, c−u) with u > c/2, one per class
    d = 2u − c. So for odd λ, |A| <= ⌊k/2⌋ and φ <= λ/(k−1).
  - The signed version holds the same way.
- T3 (PROVED formula, agent): D = [0,N) + N·B with B Sidon, λ = N has def = C(N,2)(b + 2R(B)), where R(B) is the number
  of runs of B − B. This gives explicit φ = 0.80–0.85 for k = 18..216 (refutes "φ <= 2/3 + o(1)"), but W ≍ k² and actual
  R is 1.36–1.71.
- T4 (PROVED, agent): a product A + N·B is λ-fold only if A is a cyclic (N,|A|,λ) difference set, and then the aligned
  classes are all defects.
- T5 (PROVED; lead checked). If the cross family X = U × V is isolated (no other pair of D has a difference u − v), then
      λ·#(good pairs of X) <= Σ_d c(d)² = Σ_δ r_U(δ) r_V(δ) <= √(E(U)E(V)).
  - For Sidon U, V of size s, more than a fraction 1 − 2/λ of X are defects.
  - So separated homometric triples have W >= (2/27)k² + (2/9)k, or W >= (2/9)k² with three distinct gaps.
- Conjecture C-W (CONJECTURED): λ = 3 ⇒ W >= k for all k >= 4, tight at k = 6 ({0,1,3,4,5,7}). It holds for k <= 12
  (NUMERICAL-EXACT, agent; k <= 11 also lead, E39) and in the certified spans at k = 13, 14.
  - Caution: C-W does not kill the mechanism, since λ = 2 also has W = k (Bu) and survives because its defects are
    harmless.
  - Kill statement needed: non-harmless defect weight W' >= c·k^{1+δ}, or max over {F_D ≈ 0} of E >= ck.
Status of the line: the λ >= 3 near-ruler route to R < 1/2 is KILLED as a construction line (heuristically; no
asymptotic theorem). Revival criteria: a λ = 3 set with W < k at some k >= 7, or W < 0.22k with φ near 1.

## P24. Localization lemma: windowed local transforms are bounded by 2M (lead 2026-10-18 late night; PROVED,
## elementary, one line; novelty unchecked, likely folklore; sanity-checked by hand on [H, 3H) and random A ⊂ [Y, 2Y])
Setting: A ⊂ Z_{>0} finite, f_A >= −M on R, N(H) := |A ∩ [1, H)|, F_H the Fejér kernel with F̂_H(k) = (1 − |k|/H)_+.
Lemma. For every integer H >= 1, every m >= H and every x₀ ∈ R:
    |L_m(x₀)| <= 2M + 2·Σ_{a∈A, a<H} (1 − a/H),    L_m(x₀) := Σ_{a∈A} (1 − |a − m|/H)_+ e^{i a x₀}.
Proof.
- W(x) := F_H(x − x₀)(1 + cos(m(x − x₀) + φ)) >= 0 and (1/2π)∫W = 1 + Re(e^{iφ})F̂_H(m) = 1 because m >= H.
- (1/2π)∫cos(ax)W(x)dx = Re(e^{iax₀}[F̂_H(a) + ½e^{iφ}F̂_H(a + m) + ½e^{−iφ}F̂_H(a − m)]), and F̂_H(a + m) = 0.
- So −M <= (1/2π)∫f_A W = Σ_{a<H}(1 − a/H)cos(ax₀) + ½Re(e^{−iφ}L_m(x₀)) (the m-shift cancels inside L_m).
  Choose φ to make the last term −½|L_m(x₀)|. ∎
Corollaries (PROVED).
- (a) If A ⊂ [Y, 2Y], then M >= |A|/4 (H = Y, m = ⌊3Y/2⌋, x₀ = 0; all weights >= 1/2; N(Y) = 0). More generally,
  A ⊂ [Y, λY] gives M >= |A|/(4⌈λ − 1⌉). A set with M <= c√|A| must spread over a multiplicative range
  max A / min A >= √|A|/(4c).
- (b) Shell growth: |A ∩ [H, 2H)| <= 8M + 8N(H), i.e. N(2H) <= 9N(H) + 8M (two windows of half-width H/2, weights
  >= 1/2).
- (c) Local Fourier uniformity: at every location m >= H and every frequency x₀ (e.g. x₀ = 2πr/q), the Fejér-weighted
  local exponential sum of A at scale H is <= 2M + 2N(H). So A is locally equidistributed in every residue class and
  every Bohr direction, up to M, at every scale H at which few elements lie below H.
Meaning. This is the rigorous form of the macroscopic Gibbs constraint ("profiles must be nearly p.d.") and of the
localization noted in NOTEBOOK (iii). It holds in Z_N only for localized A (N >> max A). It explains E40's uniform-level
results (M ≈ 0.44t) and the E11 failures (lifts concentrated at one scale) in one line. It cannot reach √n alone:
Singer/Bu sets satisfy every instance with room to spare (N(H) ~ H).

## Lean status update (2026-10-18 night): O4⁺, P20 Theorem 2 and the line-D identities are KERNEL-CHECKED
Codex agent (Sol 6.1, brief .research/agents/lean_o4plus_brief.md, report .research/agents/lean_o4plus_report.md).
Lead re-verification: full rebuild on dirichlet ("Build completed successfully", 8722 jobs); AxiomCheck.lean prints 33
declarations, all exactly [propext, Classical.choice, Quot.sound]; no sorry, axiom or native_decide in the new files;
main statements read against the brief.
- lean/ChowlaCosine/FibreSchur.lean (namespace ChowlaCosine.FibreSchur), on the actual quotient G ⧸ ⟨t⟩:
  - PositiveDefinite.mul / .pow: T0, Schur products on finite abelian groups.
  - order_three_fibre_bound: T1, |D| − |E| <= (K + u₀)³. The hypothesis is Re F(η) >= −K for every nontrivial
    additive character η.
  - order_three_runTops_bound: |B_t| <= |E| + (K + u₀)³ + 1, with B_t = {m ∈ A : m − t ∈ A, m + t ∉ A}.
  - order_four_fibre_bound: T2/O4⁺, 4|D₂| <= |E| + |D₃| + (K + u₀)⁴.
  - order_three_zero_fibre and order_four_zero_fibre: u₀ ∈ {0, −1}.
- lean/ChowlaCosine/HalfSet.lean, on ZMod p with g a ±1 function:
  - hat_conv_hat: T3(a).
  - shiftedHat_square_off_zero: T3(b).
  - shiftedHat_cube and cubicConstant_eq_brief: T3(c), with c₁ = p²(2λ + 3λ²g(0) + λ³).
  - spectral_gap: T3(d).
  - coefficient_upper_bound: T3(e).
No statement was refuted, weakened, or given an extra hypothesis.

## P25. Sharpened localization: the near-zero term of P24 is the Fejér-smoothed f itself (PROVED; lead 2026-10-18)
Setting as P24: f = f_A >= −M, F_H the Fejér kernel (F̂_H(k) = (1 − |k|/H)₊), and for m >= H and x₀ ∈ R
L_m(x₀) := Σ_a F̂_H(a − m)e^{iax₀}. Put g_H := f ∗ F_H = Σ_{a∈A} F̂_H(a)cos(ax). Note g_H >= −M and ∫g_H = 0.
Lemma. |L_m(x₀)| <= 2M + 2g_H(x₀) for every m >= H and every x₀.
Proof. This is P24's proof with the first term kept exact. With W(x) = F_H(x − x₀)(1 + cos(m(x − x₀) + φ)) >= 0 and
mean 1, (1/2π)∫fW = g_H(x₀) + ½Re(e^{−iφ}L_m(x₀)) >= −M. Then choose φ. ∎
(P24 is the special case g_H(x₀) <= Σ_{a<H}(1 − a/H).)
Corollaries:
- (a) Flat-minimum rigidity: if g_H(x₀) <= −M + η, then every window sum satisfies |L_m(x₀)| <= 2η. So if f is close to
  its minimum on most of a 1/H-neighbourhood of x₀, A is locally orthogonal to e^{iax₀} at every location at scale H.
- (b) L² form: summing |L_m|² over windows and integrating gives
      (2H/3)·|A ∩ [2H, ∞)| <= max A · [4M² + 2Σ_{a∈A, a<H}(1 − a/H)²].
  This is WEAKER than P24(a) whenever P24 applies.
Why this does not give √n (recorded so it is not retried): for random dense A, typical windows have
|L_m| ≈ √(δH), and 2g_H ≈ 2√(δH/3) matches it. The inequality is saturated by random sets, so (b) gives nothing for
uniformly dense A (the low-part energy cancels exactly). A √n bound needs a mechanism showing that the high part's
energy does NOT concentrate on {g_H > 0}, a set determined by A ∩ [1, H]: a decoupling or dichotomy statement.

## P26. Half-sets of Z_p ⟺ symmetric weighted near-planar difference sets (PROVED, exact equivalence; lead 2026-10-18)
Conventions: ĝ(γ) = Σ_x g(x)e(−γx/p), (u ⋆ v)(δ) = Σ_β u(β)v(δ − β) on Ẑ_p ≅ Z_p.
(⇐) Let u >= 0 be symmetric on Z_p with u ⋆ u = δ₀ + ε·1 for some ε >= 0, and s := Σu (so s² = 1 + pε).
  Put ĝ := pu − λ with λ ∈ {s − 1, s + 1}, and let g be its inverse transform.
  Then ĝ ⋆ ĝ = p²δ₀, because p²(u⋆u) − 2λps + pλ² = p²δ₀ + p((s − λ)² − 1). So g² ≡ 1, and g is real by symmetry:
  g is a ±1 function.
  Moreover ĝ(γ) = pu(γ) − λ >= −λ for all γ. With A := {g = 1}: 1̂_A(γ) = ĝ(γ)/2 >= −λ/2 for γ ≠ 0, and
  2|A| − p = ĝ(0) = pu(0) − λ.
(⇒) Conversely, if g = 2·1_A − 1 is even, ĝ >= −λ off 0 and ĝ(0) + λ >= 0, then u := (ĝ + λ)/p qualifies.
So min over symmetric half-sets of 2M_p equals min Σu ∓ 1 over symmetric u >= 0 with flat autocorrelation and
u(0) = (λ ± 1)/p.
Consequences:
- Without symmetry, planar difference sets (u = 1_D/√(k−1), Singer parameters) give Σu ≈ p^{1/4}. The elementary
  bound λ >~ p^{1/4} (line D) is exactly the non-symmetric planar bound; symmetry enters only through
  u(γ)² <= (u⋆u)(2γ).
- Sanders' question (M_p ≍ p^{1/3}, p^{1/2}, or below?) asks how far SYMMETRIC weighted near-planar sets are from
  planar.
Falsification of the natural construction (done): weights on D ∪ (−D) for a Singer set D cannot be exactly flat
(the sum-representation parity on 2D breaks it). The exact symmetric half-set optima (E41) at the Singer primes
p = 13, 31, 73 have 2M_p ≈ 1.02–1.28·√p, nowhere near the p^{1/4} scale (2.9 at p = 73).
So no near-planar symmetric weights exist at small p. A p^{1/4} construction would need weights far from 0/1.

## P27. OR(2)-weak for residue-strip 2-run sets (codex agent "or2" 2026-10-18, report .research/agents/or2_report.md;
## PROVED on paper; proof re-checked line by line by the lead; finite checks by the agent on dirichlet)
Theorem B (phase-coherence inequality). Let t, q >= 1, R ⊂ {0, …, R*} with q > R* + 2t, Y_r ⊂ Z_{>=0} (0 ∉ Y_0 if
0 ∈ R), S = ∪_r (qY_r + r), n_r = |Y_r|, n = Σn_r, A = S ∪ (S + t). Assume S ∩ (S + jt) = ∅ for j = ±1, ±2. Put
C_y = Σ_{r : y∈Y_r} e^{iπr/t}, C = 2(Im C_0)² + Σ_{y>=1}|C_y|², G = Σ_r [r² + (r+t)²]√n_r. Then
    M(A) >= t²C/(4G) − π²G/(2q²).
Proof (checked):
- (i) Exact lifting. At u = (θ + 2πj)/q, f_A(u) = h_θ(u) := Re[(1 + e^{itu})Σ_r e^{iru}z_r(θ)], with
  z_r = Σ_{y∈Y_r} e^{iyθ}.
- (ii) Bounds on h_θ: |h_θ''| <= L(θ) = Σ_r[r² + (r+t)²]|z_r(θ)|; h_θ(π/t) = 0; h_θ'(π/t) = t·Im Σ_y C_y e^{iyθ}.
- (iii) Sampled-derivative lemma, from a Taylor upper bound at the grid point nearest u₀ − h'/L:
  if h(u₀) = 0, |h''| <= L and h >= −M on a 2π/q-grid, then h'(u₀)² <= 2LM + π²L²/q².
- (iv) Integrate in θ. Orthogonality with nonnegative levels gives ∫(Im b)² = C/2; also ∫L <= G and ∫L² <= G².
Theorem A. If R ⊂ [0, t/2], k = |R| and q >= 32t√k, then M(S ∪ (S+t)) >= √(n/k)/80, and >= √(n/k)/32 if min S >= q.
- The phases e^{iπr/t} lie in an arc of width π/2, so |C_y|² >= ℓ_y/2 and C >= (n − k)/2.
- G <= (5/2)t²√(kn), and the error term is <= (1/80)√(n/k).
- n < 2k is covered by M >= 1/2.
Consequences:
- OR(2)-weak holds on this class when k <= n^{1/2−2δ}: M >= n^{1/4+δ}/80. For example k <= n^{1/4} gives
  exponent 3/8.
- Bounded k gives a square-root bound.
- The class strictly contains the dilated class qY of the rotation sweep, and also non-dilates (gcd 1).
Limits (agent, checked):
- R = {0, 3t} with Y_0 = Y_{3t} gives C_y = 0 identically, so (B) is empty. The theorem is not universal.
- No argument puts general small-M sets into residue strips.
Status: PROVED (paper), lead-verified; not yet kernel-checked. Novelty outside the project unchecked.
Theorem C (agent, final report §5; PROVED; lead re-checked every step, including constants). Fix L >= 0, B = L² + (L+1)²,
J = 2L + 3. If min S >= q, the residues of S mod q lie in [0, Lt] (k classes), the 2-run conditions hold, and
q >= 16BJtk, then
    M(S ∪ (S + t)) >= √n / (32BJ²k^{3/2}).
Proof skeleton:
- Theorem B at every zero u_j = (2j+1)π/t, averaged over j: C_* = Σ_y Σ_a b_{y,a}², with b_{y,a} the alternating
  counts along residues a + ht. Cauchy–Schwarz gives N_alt² <= N·C_*.
- Macro profile H(u) = Σ_r n_r[cos ru + cos(r+t)u] with m = −min H. Coefficient domination gives n <= 2k(n_0 + m).
- The t-shift average H̄ = (1 + cos v)·R̄ with deg R̄ <= L. A J-point grid with Σ 1/(1 + cos v_j) = J²/2 gives
  N <= J²C_* + (J² − 1)m, hence n <= 2kJ²(C_* + m).
- Either derivative energy (Theorem B) or the macro dip (exact on the grid 2πa/q plus Taylor) gives the bound.
Corollaries:
- Square-root bound for bounded unions of translated dilates.
- n^{3/8} for k <= n^{1/12}.
- The cancellation family S = qY ∪ (qY + 3t) has M >= |S|/16 for q >= 24t (a linear macro dip).
Status: PROVED (paper), lead-verified, not kernel-checked; novelty unchecked. Unrestricted OR(2)-weak remains OPEN.
Theorem D (codex agent OR3, .research/agents/or3_report.md; PROVED; lead re-checked every step and constant
2026-10-19). Same hypotheses as Theorem C with min S >= q, but with q >= 16BJ√(L+1)·t√k. Then
    M(S ∪ (S + t)) >= √(n/k) / (32BJ²√(L+1)).
- So k^{3/2} becomes k^{1/2}.
- For fixed L: exponent 1/4 + δ whenever k <= n^{1/2 − 2δ}.
- Key change: the derivative branch is projected onto the residue classes ≡ 0 mod t only. The t-shift average g_θ
  has g_θ(π) = 0, g'_θ(π) = Im Σ b_y e^{iyθ}, |g''| <= K. Hence C_0/2 <= 2∫K(M + e), and the curvature involves only
  the L + 1 fibres ht.
- D0 (also in the report, not re-checked line by line): drops min S >= q, with q >= 24BJ√(L+1)t√k and constant 64.
- (D8), a data-dependent form for arbitrary residue positions: M >= C_+/(4G_0) − π²G_all/(2q²). Structural only.
- Unrestricted spread and general OR(2)-weak remain OPEN. The report also proves an obstruction to exact
  positive-filter localization.
Mechanism: the coset grid (θ + 2πZ)/q of the real line separates the micro (quotient) phase from the macro (residue)
profile. The exact zero of the pair factor plus a sampled-derivative/Taylor lemma converts either derivative energy
or a macro dip into a negative value. Z-specific: it uses genuine real sample points, not a group character.

## P28. Averaged local-maximal bound (PROVED, lead 2026-10-19; numerics src/p28_test.py)
Statement. Let K >= 0 be a 2π-periodic kernel with K̂(0) = 1 and K̂(k) = 0 for |k| >= H (for example the Fejér kernel F_H).
For every finite A ⊂ Z_{>0},
    M(A) >= (1/4π) ∫_0^{2π} sup_{m >= H} |Σ_{a∈A} K̂(a − m) e^{iax}| dx.
Proof.
- P25 with K in place of F_H: W = K(x − x₀)(1 + cos(m(x − x₀) + φ)) >= 0 has mean K̂(0) + ½Re(e^{iφ}K̂(m)) = 1 for
  m >= H. So |Σ_a K̂(a − m)e^{iax₀}| <= 2M + 2(f ∗ K)(x₀) for all m >= H and all x₀.
- Take the sup over m, then integrate over x₀. Use ∫(f ∗ K) = 2π·(mean of f)·K̂(0) = 0. ∎
Remarks.
- H = 1 (K ≡ 1) gives M >= 1/2.
- The trivial L¹ bound M >= ‖f_A‖₁/(4π) uses Re F_A globally. P28 improves it in two ways: it uses the full modulus,
  and the sup over window locations sits INSIDE the x-integral.
- Heuristic dichotomy, NOT proved:
  - local randomness (windows with Gaussian-like spectra) gives M >~ √(local variance);
  - a counterexample must be locally deterministic at every scale (all windows' spectra concentrated on a common small
    set of frequencies), the Bohr-type regime where the Gibbs constraints (P24/P25) act.
  Making "deterministic ⇒ Gibbs" quantitative is the open step.

## P29. Fejér-grid Turán bound: density above 1/2 forces linear M (PROVED, lead 2026-10-19; elementary, novelty unchecked)
Statement. For integers L >= h >= 1, ψ(a) = (1 − |a|/h)₊ and every finite A ⊂ Z_{>0},
    (L − h)·M(A) >= h|A| − L·Σ_{a∈A} Σ_{k∈Z} ψ(a − kL).
Corollary (L = X + h, A ⊂ [1, X], n = |A|): the inner sum is ψ(a) and is at most (h−1)/2 in total, so
    X·M(A) >= h·n − (X + h)(h − 1)/2   for every h >= 1,   hence   M(A) >= (n − X/2)²/(2X)   (h ≈ X(n/X − 1/2)).
Proof.
- G(a) = Σ_k ψ(a − kL) is L-periodic with DFT Ĝ_j = F_h(2πj/L) >= 0 (Fejér kernel), F_h(0) = h, and
  Σ_{j=0}^{L−1} F_h(2πj/L) = L·G(0) = L (h <= L).
- Pairing ±A with G gives 2Σ_{a∈A} G(a) = (1/L) Σ_j F_h(x_j)·2f_A(x_j), x_j = 2πj/L.
- Use the j = 0 term 2hn, and bound f_A >= −M on the remaining weight L − h. ∎
Remarks.
- h = 1 is P13(a), (q − 1)M >= |A| − q|A ∩ qZ|. P29 is one fixed nonnegative weight, so it is not a route to √n for
  sparse sets.
- Sharp in order: the profile model with a clipped triangle density min(1, (1 + η)(1 − t)) has FT negativity ≍ η² at
  density 1/2 + η/2, so (n − X/2)²/X is the right size.
- Interval [1, X]: bound X/8, true 0.2172X.
- Numerics (all slacks positive): N50 bound 1.96 vs M = 4.03; N45 2.34 vs 3.84; general (L, h) family brute-checked
  on 6 sets.
Consequence for constructions (PROVED). If M(A) <= R√n with A ⊂ [1, X], then
    n − X/2 <= √(2RX)·n^{1/4},   i.e. density <= 1/2 + O(n^{−1/4}).
- Current dense records (density 0.69–0.74 at X <= 72) are pre-asymptotic. Any family extrapolating them to large N
  must taper to density 1/2.
- At the threshold the profile must be close to the Turán extremal triangle (stability, heuristic).
- Z_p half-sets sit exactly at this density, with no Turán constraint (the wrap-around removes the endpoint): a
  structural reason why the Z_p optima (E41) can be better than Z.
P29(b), twisted form: spectral front-loading (PROVED, same proof with the grid shifted by x₀).
- For every x₀ and integers L >= h >= 1:
      M(L − h) >= h·f_A(x₀) − L·Re Σ_{a∈A} G(a) e^{iax₀}.
  The j = 0 grid term is now h·f_A(x₀); G is even, so the pairing gives 2Re Σ G(a)e^{iax₀}.
- With L = X + h and A ⊂ [1, X]:
      f_A(x₀) <= ((X + h)/h)·(f ∗ F_h)(x₀) + (X/h)·M,   (f ∗ F_h)(x₀) = Σ_{a∈A, a<h} (1 − a/h) cos(a x₀).
- Meaning: every peak of f_A must already be present, proportionally, in the frequencies below h. The low part's
  Fejér mean at x₀ is at least (h/X)·f_A(x₀) − M.
- At x₀ = 0: |A ∩ [1, h)| >= hn/(X + h) − MX/(X + h), i.e. initial segments carry at least their proportional
  share minus M (front-loading, consistent with the Turán triangle profile).
- Back-loaded sets lose. A ⊂ [X/2, X] gives f_A <= 2M everywhere, hence M >= n/2.
- Compare P25, which bounds one window by the same low part:
  |Σ_a F̂_H(a − m)e^{iax₀}| <= 2M + 2(f ∗ F_H)(x₀).
  P29(b) bounds the whole sum instead, at the cost of a factor X/h.

## P31. Window–Nikolskii inequality: Chowla for every set that is not front-loaded
(lead 2026-10-19; PROVED modulo the constant ρ_L, see "Status")
Definitions.
- ρ_L := sup ‖v ∗ v‖₂² / ((L + 1)‖v‖₂⁴) over v >= 0 supported on {0, …, L}.
  Equivalently ‖U‖₄⁴ <= ρ_L (L + 1)‖U‖₂⁴ for every trigonometric polynomial U of degree <= L (pass to |coefficients|).
- For an integer w >= 1, κ(k) = (1 − |k|/(w + 1))₊ (Fejér kernel F = Σ κ(k)e^{ikx} >= 0), W = Σ_k κ(k)², and
  S_A = Σ_{a∈A} κ(a)².
Theorem. For every finite A ⊂ Z_{>0} with X = max A, n = |A|, M = M(A), and L = X + w:
    W·(n/2 + M²) <= ρ_L (L + 1)·(M² + S_A/2).                                                    (P31)
Proof.
- Fix x₀. h(x) = F(x − x₀)(f_A(x) + M) is >= 0 and is a trigonometric polynomial of degree <= L.
- Fejér–Riesz gives h = |U|² with deg U <= L. So (1/2π)∫h² = ‖U‖₄⁴ <= ρ_L(L + 1)‖U‖₂⁴ = ρ_L(L + 1)((1/2π)∫h)².
- Integrate over x₀ ∈ [0, 2π) with (1/2π)dx₀:
  - left side: [(1/2π)∫F²]·[(1/2π)∫(f + M)²] = W(n/2 + M²);
  - right side: (1/2π)∫h = s(x₀) = M + Σ_{a∈A} κ(a)cos(a x₀), and (1/2π)∫s² = M² + S_A/2. ∎
Corollary (the bound). If ρ := ρ_L, then
    M² >= [W n/2 − ρ(L + 1) S_A/2] / [ρ(L + 1) − W],   and   ρ(L + 1) > W always.
Take w = εX. Then W ≈ (2/3)εX. Let d_ε := 2S_A/W ∈ [0, 1], the Fejér²-weighted density of A in [1, εX], and
δ = n/X. This gives
    M² >~ (ε/3)·n·(1 − ρ(1 + ε)d_ε/(2δ)) / (ρ(1 + ε) − 2ε/3).
So M >= c(ε, η)√n whenever d_ε <= (1 − η)·2δ/(ρ(1 + ε)).
Consequences (given ρ_L <= ρ):
- (i) CHOWLA (M >> √n) for every A that is NOT FRONT-LOADED: the density near 0 at some fixed proportional scale ε
  is below 2δ/ρ ≈ 2.9δ (numerical ρ) or 2.6δ (ρ = 0.7698). This includes all sets of roughly uniform density, at
  any sparsity.
- (ii) DENSE SETS: d_ε <= 1, so every A ⊂ [1, X] with |A| >= (ρ/2)(1 + ε)(1 + η)X has M >> √n. Thresholds:
  δ > 0.344 (numerical ρ_∞) or δ > 0.385 (ρ = 0.7698).
- (iii) Any counterexample family (R -> 0) must have d_ε >= (2/ρ − o(1))δ at EVERY fixed scale ε. With P29 (which
  needs d >= 2δ), it must be strictly more front-loaded than Turán requires.
Relation to P29.
- P29 gives linear M when δ > d'/2 (linear Fejér weights). P31 gives √n on the larger range δ > ρd/2.
- With ρ = 1, P31 is weaker than P29. All new content comes from ρ_L < 1, i.e. from the doubly-positive/Nikolskii
  gap: a nonnegative polynomial cannot be as peaked in L² as Fejér's bound max <= (deg + 1)·mean allows on average.
Status.
- The identity/inequality chain is PROVED (elementary). Numerically checked on 5 sets × 2 values of w: all implied
  lower bounds lie below the true M, and the needed ρ (0.14–0.51) stays below the per-window ratios (0.35–0.60).
- ρ_L (E48, src/scratch/rhoL.py): 1 (L=0), 0.75, 0.714, 0.6967 (L=4), 0.6894 (L=9), 0.6876 (L=19), 0.6871 (L=49),
  0.6870 (L=119). Optimizer is dome-shaped, not constant (constant gives -> 2/3).
- RIGOROUS bounds available:
  - ρ_∞ := lim ρ_L <= A_{4/3}⁴ = 0.7698 (Beckner sharp Young for complex ĝ on an interval, plus Hölder). The
    convergence ρ_L -> ρ_∞ should follow from Levin–Lubinsky's theorem that normalized polynomial Nikolskii constants
    converge to the entire-function constant (p = 2, q = 4). CITED-UNVERIFIED: check the exact statement and
    normalization.
  - A uniform bound for all L, sketch: with the cumulative mass a(s) = Σ_{j<=s} v_j² and C–S per s,
    Σ_s (v∗v)_s² <= 1 − 2∫A(1 − A) (continuum form). Splitting on the shortest interval carrying 1 − θ of the mass
    gives ρ_L <= ~0.95. Needs a careful discrete write-up; too weak for (ii), but enough for a nonempty (i).
- Literature check: Levin–Lubinsky 2015 prove only a limsup bound for finite q and conjecture the limit, so they do
  not give the needed upper bound. Replaced by a self-contained proof.
- Lemma P31-N (asymptotic constant; PROOF SKETCH by lead, truncation errors to be written out):
      ρ_L <= A_{4/3}⁴ + O(1/T + T log T / L) = 0.7698 + o(1).
  - Choose B̂ smooth with Σ_m |B̂(ξ + 2πm)|² ≡ 1 and B̂ = 1 on [−π + 1/T, π − 1/T] (square-root partition of unity).
    Set h(t) = Σ_j u_j e^{ijθ} B(t − j).
  - Periodization: ∫|h|² = ‖u‖², and ∫|h ∗ h|² = (1/2π)∫|U(x + θ)|⁴ Φ(x)dx with Φ = Σ_m|B̂(x + 2πm)|⁴ >= 1 off the
    two aliasing bands of width 2/T.
  - Averaging over θ, some θ puts at most (2/(πT))‖U‖₄⁴ in the bands.
  - Beckner's sharp Young inequality on R (complex h, exponents 4/3, 4/3 -> 2, constant A_{4/3}² = 0.87738) plus
    Hölder on supp h. B decays superpolynomially at scale T, so truncate to length O(T log T).
  - Conclusion: (1 − 2/(πT))‖U‖₄⁴ <= 0.7698‖u‖⁴(L + 1 + O(T log T)).
  Hence the dense corollary (ii) holds RIGOROUSLY for large X with any threshold δ > 0.385 (once the lemma is written
  out). The numerical ρ_∞ ≈ 0.687 would lower it to 0.344.
- NOT kernel-checked; novelty unchecked. Next:
  - adversarial check by the codex agent (running);
  - full write-up of Lemma P31-N;
  - Lean (Fejér–Riesz and the integration step are mathlib-friendly; Beckner is not in mathlib, so keep it as a cited
    hypothesis or use the crude uniform bound).
Lemma P31-E (ELEMENTARY uniform constant; PROVED by lead 2026-10-19, Lean-friendly, no Beckner).
For every L >= 0:
    ρ_L <= μ + λ/(3(L + 1))   with λ = 0.71, μ = 0.8110, i.e.   ρ_L <= 0.8110 + 0.2367/(L + 1).
Proof. Take v >= 0 on {0..L}, ‖v‖ = 1, N = L + 1, p_j = v_j², a_j = Σ_{i<=j} p_i, w(A) = A(1 − A).
- (E1) Bound each (v∗v)_s by Cauchy–Schwarz on its own index range: (v∗v)_s <= a_s for s <= L and
  <= 1 − a_{s−L−1} for s > L. Call this bound m_s. Then
      Σ(v∗v)_s² <= Σ_s (v∗v)_s m_s <= Σ_j v_j² G(j)        (AM–GM v_iv_j <= (v_i² + v_j²)/2)
  with G(j) = Σ_{i=0}^{L} m_{i+j} = N − D(j). Abel summation gives Σ_j v_j² D(j) = 2Σ_{j<L} w(a_j). Hence
      ‖v∗v‖² <= E1 := N − 2Σ_{j<L} w(a_j)          (exact at constant v: gives 2N/3).
- (E2) ‖v∗v‖² <= max_s (v∗v)_s · Σ_s (v∗v)_s <= (Σ v)².
- Change of variables. Put I_j = [a_{j−1}, a_j], g = p_j^{−1/2} on I_j (when p_j > 0), φ = 1 − 2w. Then:
  - Σ_{j<L} w(a_j) = Σ_j (w(a_{j−1}) + w(a_j))/2 (telescoping);
  - trapezoid rule for the quadratic w: (1/p)∫_I w = trapezoid + p²/6;
  - hence E1 = ∫_0^1 g²φ dA + (1/3)Σ p_j² + Σ_{p_j=0} φ(a_j), with ∫g² dA = #{p_j > 0} and ∫g dA = Σ v_j.
- Weighted Cauchy–Schwarz: (∫g)² <= ∫g²(μ − λφ) · ∫dA/(μ − λφ), and (1 − λ)∫_0^1 dA/(μ − λφ) <= 1.
  The integral equals √(2/(λc))·artanh(√(λ/(2c))) with c = μ − λ/2; numerically 0.99914 at (0.71, 0.811). So
      λ∫g²φ + (1 − λ)(∫g)² <= μ∫g².
- Combine, using λ <= μ for the zero entries:
      min(E1, E2) <= λE1 + (1 − λ)E2 <= μN + λ/3. ∎
Checks (numerical, 4000 random v including zeros): trapezoid identity to 2e−14; no violation of
‖v∗v‖² <= min(E1, E2) <= μN + λ/3. Code: src/scratch/rho_elem.py; the secular optimum λ = 0.7100, μ = 0.81080 is
from src/scratch/rho_secular.py. Optimized sup of min(E1, E2)/N ≈ 0.8083 (N >= 60).
Consequence: P31 is UNCONDITIONAL with ρ = 0.8110 + 0.2367/(L + 1) (paper proof):
- dense Chowla for |A| >= 0.41(1 + ε)(1 + η)·max A, X large;
- non-front-loaded Chowla for d_ε < 2.47δ.
The sharper constants (0.7698 via Beckner, ≈ 0.687 numerically) only move the thresholds.
LEAN PLAN (verification route = kernel check; no outside review):
- (L1) Fejér–Riesz for nonnegative trig polynomials (finite, via FTA root pairing). Check whether mathlib has it.
- (L2) Lemma P31-E: Cauchy–Schwarz, Abel summation, and the integral constant. For Lean, replace the arctanh closed
  form by a rational upper Riemann sum (the integrand is monotone in |A − 1/2|), with margin from μ slightly above
  0.811.
- (L3) The window inequality: x₀-integration of finite trig sums, Fubini for finite sums, the Fejér kernel F_{w+1} >= 0
  and its coefficients.
- (L4) Corollaries with explicit constants.
P31(c), multi-scale form (PROVED, lead 2026-10-19; same proof applied to a low-passed polynomial).
- For H >= 1, g_H := f_A ∗ F_H = Σ_{a∈A} (1 − a/H)₊ cos(a x) satisfies g_H >= −M (F_H >= 0 has mass 1) and has
  degree < H.
- Run the P31 argument on h = F_{w+1}(· − x₀)(g_H + M) >= 0, of degree <= H − 1 + w. This gives
      W(n_H/2 + M²) <= ρ_{H−1+w}(H + w)(M² + S_H/2),
  with n_H = Σ_{a∈A} (1 − a/H)₊² and S_H = Σ_{a∈A} (1 − a/H)₊² κ(a)².
- Consequence: M² >~ ε n_H (1 − ρ(1 + ε)d_ε(H)/(2δ_H)), with δ_H = n_H/H and d_ε(H) the weighted density of A in
  [1, εH]. So M >> √(n_H) as soon as A is not front-loaded AT SCALE H.
- "Core + sparse tail" sets are covered whenever the core (the scale H carrying most of the weighted mass) is not
  front-loaded at its own scale.
- REMAINING ESCAPE CLASS for P31/P31(c): sets front-loaded at EVERY scale H with every ε. Model case: power-law
  density profiles φ(t) ∝ t^{−α}, 0 < α < 1. These are Turán-compatible (|t|^{−α} is p.d.) and scale-invariant.
  This class is now the precise target for both tracks:
  - lower bound: a new argument for self-similar front-loaded sets;
  - construction: optimize within power-law profiles (E49 follow-up).
