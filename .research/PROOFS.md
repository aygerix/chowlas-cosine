# Proofs and exact reformulations

Status labels: PROVED (paper proof here), CITED, HEURISTIC, CONJECTURED, REFUTED.

## L25. Low-ratio L1 flatness (CONJECTURED, 2026-10-21)

Canonical statement of the advisor's proposed unrestricted target. For EVERY
finite nonempty set A of distinct positive integers, put n=|A|,
f_A(x)=sum_{a in A} cos(ax), M(A)=-min_{x in R} f_A(x), and use the normalized
circle average <g>=(1/(2*pi))*integral_0^(2*pi) g(x) dx. The conjecture is

    M(A)<=sqrt(n)  ==>  <|f_A|> >= sqrt(n)/10.             L25

Equivalently, with D_A=2f_A and K=2M(A), it says

    K<=2*sqrt(n)  ==>  ||D_A||_1 >= sqrt(n)/5.

STATUS: CONJECTURED and unproved. Constants 1 and 1/10 are provisional.
There is no density, max-frequency, Sidon, or construction-family hypothesis.
The GPU timing pilot did not test or establish this conjecture. The name L25
comes from its connection to the beta=25 sign-witness norm budget, not a
claim that 25 is optimal. See the [independent internal advisor review](notes/phd_advisor_review_2026-10-21.md#6-one-prioritized-post-pilot-mathematical-test).

Conditional implication (PROVED, elementary): since <f_A>=0,

    <|f_A|> = 2*<(f_A)_-> <= 2*M(A).

Thus L25 would give M(A)>=sqrt(n)/20 when M(A)<=sqrt(n); the complementary
case M(A)>sqrt(n) already satisfies that conclusion. A proof of L25 would
therefore prove square-root Chowla for every A with absolute constant 1/20.
The reverse implication from Chowla to L25 is not established.

Falsification standard: exhibit a genuine Boolean set with a certified
ALL-CIRCLE upper M(A)<=sqrt(n) and a certified upper <|f_A|><sqrt(n)/10.
Sampled minima and sampled absolute averages are diagnostics only. A violation
would refute L25's stated constants, without disproving Chowla or every
possible low-ratio flatness constant. Weighted escape controls are outside
the Boolean domain and must be labeled as such.

## L26. Finite-band sign witness for arbitrary A (PROVED on paper, 2026-10-21)

Put D=2f_A, n=|A|, X=max(A), L=||D||_1. For EVERY nonempty finite Boolean
positive-integer A, there is a real mean-zero q of degree<2X with

    a=n, Q<=n^2/L^2, |H|<=8n^2/L.

Take V=2F_(2X)-F_X for normalized Fejer kernels and q=(n/L)(V*signD-<signD>).
Vhat=1 through X, lies in[0,1], vanishes at2X, and ||V||_1<=3. Exact coupling,
Parseval contraction, and ||q||_infinity<=4n/L prove the assertions; D's
positive/negative masses are both L/2. Lead derivation, independent advisor
paper audit; no kernel/priority claim. Thus L25 implies a=n,Q<=25n,H<=40n^1.5
in the FULL band below2X. This controls sufficient-witness bandwidth, not
arbitrary approximation of the full-space optimum. [Proof](notes/advisor_L25_derivation_2026-10-21.md#7-positive-finite-band-theorem-for-arbitrary-supports).

## Fixed-degree scalar witness principle (REFUTED, 2026-10-21)

Canonical cyclic perfect-difference supports satisfy M<=sqrt(n) exactly,
yet for every fixed d, all sufficiently large members have H>0 and
a²/H<=C_d for EVERY nonzero mean-zero q=P(D), degP<=d. Hence a=n forces
H>=n²/C_d and such certificates give only constant dip bounds. This is a
paper theorem with the verified classical MZ sampling dependency, not a
statement about arbitrary representatives, growing degree or general
Fourier seeds. The normalized cubic also grows as(11/5)sqrt(n), so low M
does not force bounded normalized triples. [Complete proof and scope](notes/advisor_L25_derivation_2026-10-21.md).

FINITE EXACT: n496/8128 have complete degree4 M caps13.7233/31.3755, while
broader rational witnesses prove M>15.091991495/58.53525904. Integer moments
through9 have independent packed-integer recounts; rational Schur checks
verify all caps. CPU and GPU witnesses have independently recounted square
moments. Arb quadrature certifies L25 on both inputs. These are method
separations, not counterexamples to L25 or Chowla. [Integrated cycle](notes/cstar_l25_gpu_cycle_2026-10-21.md).

## OP140. Linked Boolean inverse target (CONJECTURED, 2026-10-21)

For arbitrary A, X=max A, let c=1_A in R^(2X) and

    C_jk=(1_A(|j-k|)+1_A(j+k))/2, 1<=j,k<=2X,
    Z=C+2sqrt(n)I, J=c^T Z^(-1)c.

Conjecture: K=-min D<=2sqrt(n) implies J>=sqrt(n)/140. In this domain
C>=-sqrt(n)I, hence Z>=sqrt(n)I. L26 gives

    J >= L²/(8L+4sqrt(n)),

so L25 implies OP140. Conversely positivity gives a²<=K(H+KQ), hence
J=sup (c·v)²/(v^TZv)<=K. OP140 would therefore prove universal
M>=sqrt(n)/280. No proof is known in this record. This is the SAME C* gap
in an explicit finite operator, not an independently resolved mechanism.

For any rational w, put r=c-Zw and E=2c^Tw-w^TZw. Exactly,

    J=E+r^TZ^(-1)r, so E<=J<=E+||r||²/sqrt(n).

Exact/ball Cw and sqrt(n) enclosures can rigorously bracket J, including an
upper bound capable of refuting OP140 on a certified low-K input. Merely
failing to find a witness proves nothing. The stronger finite-C-only branch
C>=-sqrt(n)I is optional/unproved and must not be confused with the global
low-K hypothesis. Positive weighted Fejer escapes refute the non-Boolean
relaxation even with n interpreted as squared coefficient mass. A proof
must use linked zero/one entries c and C. [Advisor derivation](notes/advisor_L25_derivation_2026-10-21.md).

## 2026-10-20 supplement: arbitrary-support fixed-coupling attempt

Uniform adaptive a,Q,H remains OPEN. In any finite mean-zero trial space containing D_A, a=n iff q=D_A/2+u with u perpendicular to D_A; then Q=n/2+||u||^2 and H=<D_A^3>/4+<D_A^2,u>+<D_A,u^2>. This gives an exact finite ball-constrained quadratic, whose numerical solutions are proposals only. FINITE EXACT:20 reconstructed witnesses satisfy a=n,Q<=25n,H<0 on ten supports in two spaces. No arbitrary-support bound follows.

PROVED elementary calibration: on A=[1,n], nonnegative selected-frequency q has H=2(sum c)^2-Q+2sum_(i+j<=n)c_i c_j, so its two-dimensional determinant root is below2. For n=2m, signed q=4D_(2m)-7D_m has a=2m,Q=50m,H=-4m^2-26m and M>=(n+13)/50. A period-five P61 weighted control rigorously defeats positivity/two-profile-only bounds on constrained H; nearest Boolean rounding becomes a progression with linear M. [Proofs and limitations](notes/cstar_arbitrary_coupling_2026-10-20.md). No novelty, universal or kernel-verification claim.

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
    X·M(A) >= h·n − (X + h)(h − 1)/2   for every h >= 1,   hence   M(A) >= (n − X/2)₊²/(2X)   (h ≈ X(n/X − 1/2)).
CORRECTION (P31 review agent): the positive part is required. A = {12} has M = 1 < 25/24.
PRIOR ART: the density > 1/2 mechanism is CLASSICAL. Kolountzakis, J. Number Theory 56 (1996) 4–11, Thm 2, proves
M >= Cε²N for distinct frequencies <= (2 − ε)N, by Fejér multiplication + Fejér–Riesz. P29 is a rediscovery (same
order, explicit constant).
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
**Consolidated clean write-up (2026-10-19): .research/notes/dense_chowla_P31.md.**
**KERNEL-CHECKED (lead-audited 2026-10-19):**
- Fejér–Riesz, P31-E and P31 with the elementary constant.
- Dense theorem |A| >= 0.41·max A ⇒ M >= √|A|/1000.
- See CERTIFICATES.md.
- Theorem 1, Lemma 2 (P31-E) and Theorem 3 with explicit (a)/(b).
- Corollaries: dense c(δ) table, threshold 0.4055 with the elementary constant.
- The dyadic and no-small-elements corollaries are void: linear M holds trivially there (P31-C correction).
- The text below keeps the history and the corrections.
(lead 2026-10-19; PROVED modulo the constant ρ_L, see "Status")
Definitions.
- ρ_L := sup ‖v ∗ v‖₂² / ((L + 1)‖v‖₂⁴) over v >= 0 supported on {0, …, L}.
  Equivalently ‖U‖₄⁴ <= ρ_L (L + 1)‖U‖₂⁴ for every ANALYTIC polynomial U = Σ_{j=0}^{L} u_j e^{ijx} (pass to
  |coefficients|). CORRECTION (review agent): this fails for two-sided polynomials of degree L, e.g. L = 1 and
  U = 1 + 2cos x (ratio 19/9 > 3/2). Fejér–Riesz supplies an analytic U, so the main inequality is unaffected.
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
  is below 2δ/ρ ≈ 2.9δ (numerical ρ) or 2.6δ (ρ = 4/(3√3)≈0.76980). This includes all sets of roughly uniform density, at
  any sparsity.
- (ii) DENSE SETS: d_ε <= 1, so every A ⊂ [1, X] with |A| >= (ρ/2)(1 + ε)(1 + η)X has M >> √n. Thresholds:
  δ > 0.344 (numerical ρ_∞) or δ > 0.385 (ρ = 4/(3√3)≈0.76980).
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
  - ρ_∞ := lim ρ_L <= A_{4/3}⁴ = 4/(3√3)≈0.76980 (Beckner sharp Young for complex ĝ on an interval, plus Hölder). The
    convergence ρ_L -> ρ_∞ should follow from Levin–Lubinsky's theorem that normalized polynomial Nikolskii constants
    converge to the entire-function constant (p = 2, q = 4). CITED-UNVERIFIED: check the exact statement and
    normalization.
  - A uniform bound for all L, sketch: with the cumulative mass a(s) = Σ_{j<=s} v_j² and C–S per s,
    Σ_s (v∗v)_s² <= 1 − 2∫A(1 − A) (continuum form). Splitting on the shortest interval carrying 1 − θ of the mass
    gives ρ_L <= ~0.95. Needs a careful discrete write-up; too weak for (ii), but enough for a nonempty (i).
- Literature check: Levin–Lubinsky 2015 prove only a limsup bound for finite q and conjecture the limit, so they do
  not give the needed upper bound. Replaced by a self-contained proof.
- Lemma P31-N (asymptotic constant; PROOF SKETCH by lead, truncation errors to be written out):
      ρ_L <= A_{4/3}⁴ + O(1/T + T log T / L) = 4/(3√3)≈0.76980 + o(1).
  - Choose B̂ smooth with Σ_m |B̂(ξ + 2πm)|² ≡ 1 and B̂ = 1 on [−π + 1/T, π − 1/T] (square-root partition of unity).
    Set h(t) = Σ_j u_j e^{ijθ} B(t − j).
  - Periodization: ∫|h|² = ‖u‖², and ∫|h ∗ h|² = (1/2π)∫|U(x + θ)|⁴ Φ(x)dx with Φ = Σ_m|B̂(x + 2πm)|⁴ >= 1 off the
    two aliasing bands of width 2/T.
  - Averaging over θ, some θ puts at most (2/(πT))‖U‖₄⁴ in the bands.
  - Beckner's sharp Young inequality on R (complex h, exponents 4/3, 4/3 -> 2, constant A_{4/3}² = 0.87738) plus
    Hölder on supp h. B decays superpolynomially at scale T, so truncate to length O(T log T).
  - Conclusion: (1 − 2/(πT))‖U‖₄⁴ <= 4/(3√3)≈0.76980‖u‖⁴(L + 1 + O(T log T)).
  Hence the dense corollary (ii) holds RIGOROUSLY for large X with any threshold δ > 0.385 (once the lemma is written
  out). The numerical ρ_∞ ≈ 0.687 would lower it to 0.344.
- NOT kernel-checked; novelty unchecked. Next:
  - adversarial check by the codex agent (running);
  - full write-up of Lemma P31-N;
  - Lean (Fejér–Riesz and the integration step are mathlib-friendly; Beckner is not in mathlib, so keep it as a cited
    hypothesis or use the crude uniform bound).
Lemma P31-N, rigorous (review agent, .research/agents/p31_report.md; lead re-checked every step 2026-10-19):
    ρ_L <= β(1 + 2/√(L + 1))³,   β = A_{4/3}⁴ = 4/(3√3) = 0.769800…
- Proof: exact sinc interpolation h_θ(t) = Σ u_j e^{ijθ} sinc(π(t − j)).
  - ĥ = 1_{[−π, π]}·U, so ‖h‖₂ = ‖u‖ and ‖h∗h‖₂² = ‖u∗u‖² EXACTLY (the band is one period: no aliasing).
  - Beckner's Theorem 3 (Ann. Math. 102 (1975)).
  - Hölder on [−R, N − 1 + R]. The tails are controlled by averaging over θ: E_θ|h_θ(t)|^{4/3} <= (Σ|u_j|²B(t−j)²)^{2/3}
    and B² <= 1/(π² dist²). Take R = √N.
- This supersedes the lead's smooth-cutoff sketch, whose truncation step was incomplete.
- The agent also gives an elementary ρ_L <= 19/20 for all L >= 1 (orthogonal decomposition around the constant
  vector). Note ρ_0 = 1.
- Explicit: ρ_L <= 0.95 for 1 <= L < 249999 and ρ_L <= 0.78 for L >= 249999.
Explicit dense theorem (review agent, PROVED, uses Beckner): every A with |A| >= (2/5)·max A has M(A) >= √|A|/1000.
For every fixed δ₀ > 2/(3√3) ≈ 0.3849 there is an explicit c(δ₀) > 0 with M(A) >= c(δ₀)√|A| whenever
|A| >= δ₀·max A. The small-ε limit is needed; at ε = 1 the threshold is r, not r/2.
CORRECTION to (iii): the fixed-scale threshold is 2δ/(ρ(1 + ε)). Exact relative form:
d/δ >= 2X/C − (4X/W)(M²/n).
Novelty (agent's audit): the averaged second-moment inequality and the density threshold β/2 were not found.
Predecessor framework: Kolountzakis 1996 (Fejér multiplication + Fejér–Riesz). No priority claim.

Lemma P31-E (ELEMENTARY uniform constant; PROVED by lead 2026-10-19, Lean-friendly, no Beckner; not reviewed by the
agent, which worked from the earlier brief).
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
P31(c), multi-scale form (inequality PROVED; claimed consequence RETRACTED, see below).
- For H >= 1, g_H := f_A ∗ F_H = Σ_{a∈A} (1 − a/H)₊ cos(a x) satisfies g_H >= −M (F_H >= 0 has mass 1) and has
  degree < H.
- Run the P31 argument on h = F_{w+1}(· − x₀)(g_H + M) >= 0, of degree <= H − 1 + w. This gives
      W(n_H/2 + M²) <= ρ_{H−1+w}(H + w)(M² + S_H/2),
  with n_H = Σ_{a∈A} (1 − a/H)₊² and S_H = Σ_{a∈A} (1 − a/H)₊² κ(a)².
- Consequence: M² >~ ε n_H (1 − ρ(1 + ε)d_ε(H)/(2δ_H)), with δ_H = n_H/H and d_ε(H) the weighted density of A in
  [1, εH]. So M >> √(n_H) as soon as A is not front-loaded AT SCALE H.
- "Core + sparse tail" sets are covered whenever the core (the scale H carrying most of the weighted mass) is not
  front-loaded at its own scale.
- RETRACTION (review agent's obstruction plus lead check). The low-pass weights (1 − a/H)² impose a (1 − t)² factor.
  So even a FLAT-density core has weighted ratio d/δ_H ≈ 3 > 2/ρ, and P31(c) gives nothing for it.
  - Exact obstruction: A ⊇ [1, H − 1] gives g_H = (F_H − 1)/2 with minimum >= −1/2.
  - Any nonnegative mean-one kernel of degree < H behaves the same way.
  - Even the optimal p.d. kernel is only borderline (its squared-weight average ≈ ρ/2, which reproduces the
    threshold 2/ρ).
  Positive low-pass smoothing alone cannot handle cores.
- What does handle cores (review agent, PROVED): M(B ∪ T) >= M(B) − |T| (degree-free). For an interval core
  {1..Y}: M >= 2Y/(3π) − |T|.
- REMAINING ESCAPE CLASS: sets front-loaded at EVERY scale H with every ε. Model case: power-law
  density profiles φ(t) ∝ t^{−α}, 0 < α < 1. These are Turán-compatible (|t|^{−α} is p.d.) and scale-invariant.
  This class is now the precise target for both tracks:
  - lower bound: a new argument for self-similar front-loaded sets;
  - construction: optimize within power-law profiles (E49 follow-up).

## P31-C. Explicit sparse-front corollary of P31 (all scales, all X) — PROVED (lead 2026-10-19), modulo P31's inputs
Inputs: P31 (window inequality: Fejér window + Fejér–Riesz + analytic Nikolskii) and Lemma P31-E (ρ_L <= 0.8110 + 0.2367/(L + 1)).
STATEMENT. Let A ⊂ Z_{>0} be finite and nonempty, X = max A, n = |A|, M = −min_R f_A. Then for every integer w with
0 <= w <= X:
    M² >= (w + 1)·n / (3·(0.811·(X + w + 1) + 0.2367))  −  ½·|A ∩ [1, w]|.            (C)
Proof:
- P31 at window w, with L = X + w and C = ρ_L(L + 1), gives
      W(n/2 + M²) <= C(M² + S_A/2),   W = 2(w + 1)/3 + 1/(3(w + 1)),   S_A = Σ_{a∈A}(1 − a/(w + 1))₊² <= |A ∩ [1, w]|.
- C > W: the Fejér kernel shows ρ_L(L + 1) >= W_L >= W, and the gap is strict for X >= 1. So
      M² >= (Wn − C·S_A)/(2(C − W)).
- If Wn >= C·S_A, then M² >= (Wn − C·S_A)/(2C) = Wn/(2C) − S_A/2. Otherwise Wn/(2C) − S_A/2 < 0 <= M².
- Finally use W >= 2(w + 1)/3 and ρ_L <= 0.811 + 0.2367/(L + 1), i.e. C <= 0.811(X + w + 1) + 0.2367. ∎
COROLLARIES (exact constants, every X >= 1, no asymptotics):
(a) DYADIC SETS. If A ⊂ (X/2, X], then M(A) >= 0.3701·√|A|.
    Take w = ⌊X/2⌋, so A ∩ [1, w] = ∅. Then w + 1 >= (X + 1)/2 and X + w + 1 <= (3X + 2)/2, giving
        M² >= n(X + 1)/(7.299X + 6.286).
    This is decreasing in X, with limit 1/7.299 = 0.13700 (checked numerically for X <= 2·10⁵, min 0.137005).
(b) SETS WITHOUT SMALL ELEMENTS. If A ∩ [1, εX] = ∅ (0 < ε <= 1), then
        M² >= εn/(2.433(1 + ε) + 0.7101/X).
    (Use w = ⌊εX⌋, w + 1 >= εX, and that the right side of (C) increases in w + 1.) Examples: ε = ¼ gives M >= 0.2867√n;
    ε = ¾ gives M >= 0.4197√n (asymptotic constants; the 0.7101/X term costs < 1% once X >= 100).
(c) SPARSE FRONT. M >= c√n whenever, for some w,
        |A ∩ [1, w]| <= 2(w + 1)n/(3(0.811(X + w + 1) + 0.2367)) − 2c²n.
    In words: once the density of A in [1, w] falls below about (2/2.433)·(1 + w/X)^{−1} ≈ 0.82/(1 + w/X) times the
    global density n/X, Chowla holds for A with an explicit constant.
Sharper constants:
- With P31-N (Beckner, ρ_L -> 4/(3√3)≈0.76980) the dyadic constant becomes 0.380 asymptotically.
- With the numerical ρ_∞ ≈ 0.687 (E48; not proved) it would be 0.402.
CORRECTION (lead, 2026-10-19, same day; found while testing E54). (a) and (b) are TRUE but TRIVIALLY SUPERSEDED.
- Sets without small elements have LINEAR M by a one-line test-point argument.
- If A ⊂ (X/2, X] and θ ∈ [1, 3/2], every a ∈ A has aθπ/X ∈ (π/2, 3π/2), so cos(aθπ/X) < 0. Averaging over θ,
      mean_θ f_A(θπ/X) = Σ_a (2X/(aπ))(sin(1.5aπ/X) − sin(aπ/X)) <= −0.3729·n,
  since for t = a/X ∈ (1/2, 1] the summand is <= −0.3729, approached only as t -> ½. Hence M(A) >= 0.3729·|A|.
- E54 confirms: SA over dyadic sets finds M ≈ 0.85n.
- For A ⊂ [Y, KY], linear test measures give M >= c(K)|A| (E58 LP computes c(K)). The PSD argument on the points
  0, Y, 2Y, … shows c(K) <= ~1/K.
- So the dyadic 0.370√n and the √n of (b) are mathematically void. Do not cite them.
- (c) and the dense corollaries are unaffected. Sets with small elements (dense, Singer-type, triangle profiles) CAN
  have M ~ √n, so √n is the right order there.
- P31's genuine content is Chowla for sets with a front that is not front-loaded beyond about 2.4–2.9× the average
  density, including all dense sets with δ > 0.4055 (elementary) / 0.385 (Beckner).
Status: paper proof complete given P31 + P31-E. Lean: P31 is kernel-checked conditionally on FejerRiesz (agent T3).
(C) is the natural T4 target. Literature: no √n bound for dyadic or sparse-front sets was found in the 2026-10-19
dense-case check. Not a thorough survey.

## P33. Ratio lemma: M(A) >= |A|·min(A)/max(A) — PROVED (lead 2026-10-19; elementary; probably folklore)
STATEMENT. For every finite nonempty A ⊂ Z_{>0} with Y = min A and Z = max A:
    M(A) >= (Y/Z)·|A|.
Proof:
- Let N = Y + Z, c = Y/Z, and for b ∈ Z_N let b̄ ∈ (−N/2, N/2] be its representative. Define
      D(b) = (1 + c)·(1 − |b̄|/Y)₊ − c   and   m_j = (1/N)Σ_{b∈Z_N} D(b)e^{−2πijb/N}.
- The triangle has support |b̄| <= Y − 1 < N/2, so there is no wrap. Hence
      m_j = (1 + c)F_{Y−1}(2πj/N)/N − c·1[j = 0],   F_{Y−1} = Fejér kernel (>= 0, F_{Y−1}(0) = Y).
  So m_j >= 0 for j ≠ 0, and m_0 = (1 + c)Y/N − c = 0.
- μ = Σ_j m_j δ_{2πj/N} is a probability measure (Σ m_j = D(0) = 1). Since D is even, ∫cos(ax)dμ = D(a mod N).
- For a ∈ [Y, Z] = [Y, N − Y] we have |ā| >= Y, so D(a) = −c. Hence ∫f_A dμ = −c|A| and min f_A <= −(Y/Z)|A|. ∎
Optimality of the linear-test constant:
- E58 (Gurobi LP over all probability measures, A ⊂ [Y, KY]) gives c(K)·K = 0.998–1.000 for K = 2 … 20; the LP atoms
  approach a grid of spacing 2π/((K+1)Y).
- PSD upper bound: the points 0, Y, …, mY force c <~ 1/K.
- So Y/Z is the best constant any single-measure (linear) test can give uniformly over A ⊂ [Y, Z].
Consequences:
- A ⊂ (X/2, X] has M >= |A|/2·(1 − O(1/X)). This supersedes the 0.373n test-point bound and P31-C(a).
- A ⊂ [εX, X] has M >= ε|A|, linear. This supersedes P31-C(b).
- Chowla-type √n behaviour is only possible when min A <~ max A/√|A|. Small elements are NECESSARY.
- Combined with P31: a counterexample needs elements down to scale X/√n and a front-loaded profile at every scale
  above that. P33 handles the bottom; P31 handles every scale with a sub-threshold front.
Novelty: almost certainly folklore (a one-measure Fejér construction). Recorded because the project needed it and P31-C
had wrongly occupied this case.

## P32. Two-scale spike-support inequality (route R3) — PROVED (lead 2026-10-19; elementary from P31's window step)
Setup: A ⊂ Z_{>0} finite, X = max A, f = f_A >= −M. w >= 1, F = Fejér kernel of degree w with F̂(0) = 1, κ(k) the
same Fejér weights as in P31, g = f ∗ F (so g(x) = Σ_{a∈A} κ(a)cos(ax), g >= −M, mean 0). W = (1/2π)∫F², L = X + w,
C_L = ρ_L(L + 1).
Local window inequality (pointwise in x₀; P31's step before integrating):
    (1/2π)∫F(x − x₀)²(f(x) + M)²dx <= C_L(M + g(x₀))².
Integrate over x₀ ∈ E with dx₀/2π. Let S be any set with S + [−c/w, c/w] ⊂ E. Then
    (W − τ_c)·(1/2π)∫_S (f + M)² <= C_L·(1/2π)∫_E (M + g)²,
where τ_c := (1/2π)∫_{|y|>c/w} F² <= π³w/(3c³). Use F(y) <= π²/((w + 1)y²) on |y| <= π. So τ_c/W <= 15.5/c³.
Splitting g: (1/2π)∫_{g <= K'M} g² <= (K' + 1)M², as for f. Hence for any η > 0:
    (1/2π)∫_S (f + M)² <= [C_L/(W − τ_c)]·[(1 + η)((1/2π)∫_{E ∩ {g > K'M}} g² + (K' + 1)M²) + (1 + 1/η)M²|E|/2π].
Numbers: C_L/(W − τ_c) ≈ (3ρ/2)(1 + X/w)/(1 − 15.5/c³). With w = X and ρ = 4/(3√3)≈0.76980 + o(1), this is 2.31/(1 − 15.5/c³).
Meaning: f's spike mass on S is at most a constant times g's spike mass on a c/w-neighbourhood, plus O(M²(1 + |E|)).
Choosing S outside the central region (|x| >= C/w) removes g's own profile peak from the right side.
FULL-FRONT COROLLARY (PROVED). If A ⊇ [1, w], then g = (F − 1)/2 exactly, with g <= −1/2 + O(w/(C²w²)·…) on |x| >= C/w,
so it has no spikes there. Hence f's spike mass above KM outside |x| < (C + c)/w is O_ρ(M²(1 + K)), and so
    (1/2π)∫_{|x| >= (C + c)/w} f² = O(M²(1 + K + |E|)).
So for a full-front set with M = R√n and R -> 0, ‖f‖₂² concentrates in the central window |x| < (C + c)/w.
Remaining step for full-front sets (OPEN, but it looks tractable):
- Central-window mass is ≈ (n/2)·d_loc, where d_loc is A's average local density at scale w/(C + c).
- Concentration forces d_loc -> 1: A is a union of long full runs at scale w/C. Such sets should have large M, by a
  localized Turán/Gibbs argument (to be proved: P24/P29 localized to runs).
General fronts: need the recursion f -> g -> g ∗ F' … to contract. The constant 2.31 per step must be beaten by
g's spike mass on E being a fraction <= 1/2.31 of f's, i.e. a "noise-transfer ratio". To be measured and bounded.

## P34. One-sided Littlewood bound: −min Σ_{j=1}^n cos(jt − θ_j) >= 0.28√n (sharp order) — PROVED (lead 2026-10-19)
Full statement and proof: .research/notes/littlewood_onesided_P34.md.
Theorem. Let T(x) = Σ_{j=1}^n Re(b_j e^{ijx}) with b_j ∈ ℂ, |b_j| <= 1, E = Σ|b_j|², and T >= −M on ℝ. Then for every
0 <= w <= n:
    W_w(M² + E/2) <= C_L(M² + S_w/2),
where:
- L = n + w;
- S_w = Σ_{j=1}^w (1 − j/(w+1))²;
- W_w = 1 + 2S_w;
- C_L is any constant in the Nikolskii inequality (N_L) for nonnegative degree-L polynomials:
  - L + 1 (trivial);
  - 0.811(L + 1) + 0.2367 (P31-E, kernel-checked).
Proof. This is P31's chain with general coefficients. Fejér window K_w(x − x₀)(T + M) >= 0, (N_L), average over x₀.
Only |b_j|² enters, so phases are free.
Corollaries.
- (A) Unit amplitudes, any phases, every n: −min T >= 0.189√n (trivial C_L; asymptotic √(7/2 − 2√3)) and
  >= 0.28√n (P31-E). The same holds for max T.
- (B) ±1 Littlewood cosine polynomials: −min Σ_{j=0}^n a_j cos jt >= 0.28√n − 1.
- (C) |b_j| <= 1 with E >= δn, δ > 0.4055: −min T >= c(δ)√n. This is the complex form of dense Chowla.
Sharp order: Rudin–Shapiro gives |T| <= √(2n).
Relation to the literature: Erdélyi arXiv:2607.21877v1 claims n^{1/3}/60 for both one-sided quantities and records only
the trivial two-sided √n. Its v1 proof has a gap (LITERATURE). P34 gives the sharp order.
Novelty: one web search plus Erdélyi's own 2026 survey of prior results. No √n one-sided bound was found.
Checks: E61 adversarial search (phases best −min T/√n ≈ 0.61, flat in n; ±1 signs >= 0.73). All above the bound.
Lean: **KERNEL-CHECKED 2026-10-19 (lead-audited, CERTIFICATES).** The complex-coefficient window inequality is
`p34_elementary`. Corollaries: `p34_A`, `p34_A_phases` (√n/4 for every n >= 1 and all phases), `p34_B` (±1, both
signs, ∓1 for the constant term) and `p34_C` (dense complex, √n/1000).
Meaning for Chowla: the window method is phase-blind and sees only the energy profile |b_j|². Unit amplitudes on [1, n]
are the flattest profile, so the one-sided Littlewood problem is exactly the δ = 1 instance of dense Chowla. Sparse
0/1 sets (Chowla proper) are hard precisely because their profile can be front-loaded (escape class).

## P36. Truncation at gaps: M is almost monotone under cutting A at a gap — PROVED (lead 2026-10-19; elementary); KERNEL-CHECKED 2026-10-19 (`p36_truncation`, `p36_gap`, `p36_gap_pi`; exact constant; CERTIFICATES)
Statement. For every finite A ⊂ ℤ_{>0} and every integer D >= 1,
    M(A) >= M(A ∩ [1, D]) − (1 − cos(π/(D + 2)))·Σ_{a∈A, a<=D} a².
In particular, if A ∩ (Y, D] = ∅:
    M(A) >= M(A ∩ [1, Y]) − (π²/2)·(Y/(D + 2))²·|A ∩ [1, Y]|.
Proof.
1. Let J >= 0 be the Fejér–Egerváry–Szász extremal polynomial of degree D: Ĵ(0) = 1 and Ĵ(1) = cos(π/(D + 2)), the
   maximum over nonnegative polynomials of degree D.
2. Ĵ is positive definite, so 1 − Ĵ(a) = ∫(1 − cos ax)J <= a²∫(1 − cos x)J = a²(1 − Ĵ(1)), using
   1 − cos(aθ) <= a²(1 − cos θ).
3. f_A ∗ J = Σ_{a∈A, a<=D} Ĵ(a)cos(ax) >= −M(A), since J is a probability density of degree D and kills every
   frequency > D.
4. Hence f_{A∩[1,D]} = f_A ∗ J + Σ_{a<=D}(1 − Ĵ(a))cos(ax) >= −M(A) − Σ_{a<=D}(1 − Ĵ(a)). ∎
Notes.
- The Fejér kernel gives the weaker linear error Σ a/(D + 1). The quadratic error is what makes the lemma useful.
- This is the "gap" exception to the frequency-localization no-go (NOTEBOOK): localization is free where A has no
  elements to be damaged.
- Application (E60): for Bu + far outliers (gap ratio T), M(A) >= M(core) − O(n/T²). P16/P31 then apply to the core.
  So E60's sets escape P31 but not P31 + P36 once T >~ √(n/M).
- Corollary (P31 + P36): Chowla holds for every set that, after cutting at a gap of ratio >= C·(|core|/√|core|)^{1/2},
  has a non-front-loaded core of size >= η|A|.
Novelty: elementary. Folklore-level ingredients (Fejér–Egerváry–Szász, PD increments). Recorded as a tool.

## P37. The P31/P36 escape class contains sets with R -> ½ (Bu + far outliers) — PROVED modulo Bu et al.'s theorem
## (lead 2026-10-19)
Setting:
- S is a Sidon set of size k from Bu et al.'s construction (2610.17160). Their theorem gives
  B := max_x (g_S/2 − ρ_S²) = M(A(S)) − k/2 = O(√(k log k)).
- O is a set of k_o "outliers" at distance about T·L (L = max|S|), chosen so that S ∪ O is still Sidon. Generic offsets
  work: E60 does this greedily.
- Bu's identity holds for every Sidon set: f_{A(S∪O)} = ρ² − K/2 − g/2, with ρ = ρ_S + ρ_O, g = g_S + g_O and
  K = k + k_o.
Claim. M(A(S∪O)) <= K/2 + B + k_o√(2k) + k_o/2 whenever k_o <= √(k/2). Hence
    R(A(S∪O)) <= ½ + O(√(log k/k)) + O(k_o/√k),
which tends to ½ for k_o = o(√k).
Proof.
1. |ρ_O| <= k_o and g_O <= k_o, so g/2 − ρ² <= (g_S/2 − ρ_S²) + 2|ρ_S|k_o + k_o/2.
2. Put r = |ρ_S|. Then g_S/2 − ρ_S² <= min(B, k/2 − r²), using g_S <= k.
3. For r <= √(k/2) the total is <= B + k_o√(2k) + k_o/2.
4. For r > √(k/2) >= k_o, the function −r² + 2rk_o is decreasing, so k/2 − r² + 2rk_o <= 2k_o√(k/2). ∎
Escape:
- For T >= 8 the profile of A(S∪O) is front-loaded at every scale (E60: factors 20–200). P31 gives nothing.
- For fixed T and k -> ∞, P36's error ≈ (π²/2)k²/T² >> k. So P36 + P31 give nothing either.
- Only structural arguments (P16) see these sets. P16 still gives R >= ½ − o(1) for them, being a statement about
  every Sidon set.
Meaning: profile and gap methods are provably insufficient for Chowla, even near the conjectured extremal constant.

## P38. Denominator filters: Chowla for cumulative rounding of decreasing profiles (TD1/TD2) — PROVED on paper
## (codex T-dense agent 2026-10-19, report .research/agents/tdense_report.md §TD1–TD2; every step of TD1 re-derived by
## the lead; not kernel-checked; priority unchecked)
Statement (TD1). Fix integers q >= 1, 1 <= r <= q. Let p: [0,1] -> [0, r/q] be nonincreasing with p(0) = r/q, and
assume:
- (a) 0 <= r/q − p(t) <= L·t on [0,1];
- (b) there is t0 < 1 with p <= 1/(q+1) on [t0, 1] and μ := ∫_{t0}^1 p > 0.
For any X >= 1 and phase σ ∈ [0,1), let U_j = ⌊σ + Σ_{i<=j} p(i/X)⌋ (U_0 = 0), a_j = U_j − U_{j−1} ∈ {0,1} and
A = {j <= X : a_j = 1}, n = |A| >= 1. Then M(A) >= c(p,q)·√n, with explicit
c = min(1/(2√X0), √(θμ/192)), where:
- θ = min(1/4, μ/(100q(L+1)));
- X0 = ⌈max(100, 2q/θ, 2(q+3)/μ, 72q/(θμ))⌉.
Proof skeleton (lead-checked):
1. Positive multiplier. T = (1 − cos qx)·f_A + a_q/2 = Σ_j b_j cos jx, with b_j = a_j − (a_{j−q} + a_{j+q})/2
   (a extended evenly, a_0 = 0). T >= −2M + a_q/2 =: −m.
2. Coefficient window inequality (P31's chain applies to ANY real coefficients; it uses only T + m >= 0, Fejér–Riesz/
   Nikolskii and Parseval): W(m² + E/2) <= C(m² + S/2), with E = Σb_j² and S = Σ_{j<=w} b_j²(1 − j/(w+1))².
3. Tail. Where p <= 1/(q+1), cumulative rounding puts at most one element in any q+1 consecutive indices, so b_j = 1
   on A ∩ [t0X + q, X] and E >= μX − q − 3.
4. Front (the arithmetic ingredient). Let d_j = U_{j+q} − U_j <= r and z_j = r − d_j >= 0. Then
   (a_{j+q} − a_j)² = |d_j − d_{j−1}| <= z_j + z_{j−1}. Telescoping with the rounding errors gives
   Σ_{j<=w} z_j <= qL(w+1)(w+q)/X + q, hence S <= 3q + 2qL(w+1)(w+q)/X.
5. Window w = ⌊θX⌋: WE − CS >= θμX²/12, so (2M)² >= m² >= θμX/48. Small X: M >= ½.
TD2 (explicit instance). p_j = ½(1 − j/X)², q = 2: M(A_X) >= √n/1000 for all X >= 8. Here n ≈ X/6, A_X has NO
two consecutive elements, and the profile escapes the original P31 at every proportional scale. The agent's exact
audit is tdense_scratch/verify_exact.py; the lead checked TD1, of which TD2 is an instance with tuned constants.
Meaning:
- The first √n theorem for a front-loaded (P31-escaping) dense family, via a NONLINEAR certificate: b_j² contains
  products of membership indicators.
- It refutes the shortcut "front-loaded ⇒ long runs".

## P39. Third-moment reduction (TD4) and its physical-space form — PROVED (TD4: agent; identities re-verified by
## the lead in exact arithmetic, src/scratch_lm/lead_td4_check.py: 0 mismatches over 300 random A and all q)
For H >= 0 and G = f_A + M >= 0: with T = H·f − mean(H·f) and m = M·‖H‖∞ + mean(H·f), we have T >= −m and mean T = 0.
Cauchy–Schwarz on T + m >= 0 gives
    V² <= m²V + mW,    V = mean T², W = mean T³.                                (TD4.moment)
Hence V >= ηn and W <= B·V^{3/2} imply m >= √(ηn)(√(B²+4) − B)/2.
For H_q = 1 − cos qx (so m = 2M − a_q/2), put S = A ∪ (−A) and g_q = D_q 1_S = 2·1_S − 1_{S+q} − 1_{S−q}:
    V_q = (‖g_q‖₂² − 4a_q)/16   (CORRECTED by the round-2 agent, lead-checked: g_q(0) = −2a_q is the mean, which
                                  centering removes; for A = {1}, q = 1 this gives V = 5/8, not 7/8),
    W_q = Δ_q/32 + (3a_q/2)V_q + a_q/8,
    Δ_q = 10c(0) − 15c(q) + 6c(2q) − c(3q) = ½·Σ_{x+y+z=0} g_q(x)g_q(y)g_q(z),
with c = 1_S∗1_S∗1_S. So Δ_q is the signed Schur-triple count of the second difference g_q. Equivalently
Δ_q = ½·∫(2 − 2cos qξ)³·1̂_S(ξ)³. It vanishes to leading order whenever the triple count c is a quadratic on [0, 3q].
- Intervals: c is a quadratic spline with knots ±X, ±3X, so Δ_q = O(n) for q < X/3. LM holds with q ≈ X/4.
- Sets of multiples dZ: take q ∈ dZ.
LM-dense (CONJECTURED, agent): for every C there are η(C), B(C) such that every A ⊂ [1, Cn] has some q <= max A with
V_q >= ηn and W_q <= B·V_q^{3/2}. It implies T-dense. Exhaustively true for max A <= 18 (agent, exact).
STATUS: probably FALSE as stated (P39-O below); the reduction itself is proved.

## P39-O. Obstructions to single-filter third-moment certificates (lead 2026-10-19; (i) PROVED modulo routine
## error terms, (ii) HEURISTIC)
Pure-component excess. Write A as a union of pieces A_p, with S_p = ±A_p. For any H >= 0 of degree d,
∫(H f)³ = (1/8)Σ_k (H³)^(k)·c(k). If every pure triple sum of A_p lies in pZ and 3d < p, the pure-p part of this
sum is (H³)^(0)·c_p(0)/8 = mean(H³)·c_p(0)/8 > 0: H cannot see it.
(i) General sets: A = ∪_{p ∈ 𝒫} p·[1, L_p], with 𝒫 the primes in [P, 2P], P = L^θ (0 < θ < 1/2), and lengths making
    the total profile convex decreasing.
    - For H = 1 − cos qx: at most O(1/θ) of the p divide q. Every other p contributes 10·c_p(0) = 30L_p(L_p − 1) to Δ_q.
    - Mixed triples give the profile envelope, which is >= 0 by Pólya, plus errors O(J³L).
    - So W_q >= c·J·L² while V_q <= 2n = 2JL. Then W_q/V_q^{3/2} ≳ √(L/J) → ∞ for every q.
    - The same holds for EVERY multiplier H of degree < P/3, since mean H³ >= (mean H²)²/mean H.
    - Density ~ 1/log P, and M is LINEAR (sidelobes of the dilated Dirichlet kernels align). So this only blocks the
      certificate, not Chowla.
(ii) Dense sets (C fixed): A = union of J randomly thinned Bohr sets {m <= X : ‖mα_i‖ < ε} with ε ≈ 1/(4CJ),
     α_i chosen so that for every q <= X at most J/2 indices have min_{j<=3} ‖jqα_i‖ < 3ε. This needs
     J·log(1/ε) ≫ log X, i.e. J ~ log X/log log X.
     - "Inactive" components contribute +10·env_i(0)(κ_i(0) − 1) ≈ +5n²/J in total.
     - Active ones contribute at least −5/10 of that.
     - The envelope is >= 0 when the profile is convex decreasing.
     - So W_q ≳ n²/J ≫ n^{3/2} for every q: LM-dense fails.
     M is still >= √n·(something): >= n/J with sharp Bohr cut-offs (negative sinc weights give anti-spikes), or
     ≈ √(n log n) for positive-definite modulation with random thinning.
Lesson. Independent arithmetic structures need PRODUCT filters Π(1 − cos q_i x). Their normalized variance decays like
(3/8)^J, so the third-moment route loses n^{−O(1/log log n)} on (ii) unless the statistic changes. The truth for
(ii) comes from the bulk (Gaussian rounding noise), which the third moment cannot see behind tall positive spikes.

## P40. Spike-truncation reduction (Bhatia–Davis) — PROVED (lead 2026-10-19; elementary). NOT NEW HERE.
## It restates the session-2 identity behind E47/P30 (share_{>KM} >= 1 − 2(1+K)R², NOTEBOOK "P30"), with threshold
## λ = K√n instead of K·M. Recorded for the explicit truncation form used in P41.
For any A, every λ > 0 and every H >= 0 with ‖H‖∞ <= 1 (H = 1 for the basic form):
    ∫_{f<=λ} f² − μ_λ² <= (λ + μ_λ)·M,    μ_λ = ∫(f − λ)₊ <= ∫f₊ = ∫f₋ <= M.
Proof: Y = min(f, λ) ∈ [−M, λ] has mean −μ_λ. Bhatia–Davis gives Var Y <= (λ + μ)(M − μ), and E[Y²] >= ∫_{f<=λ} f².
Consequences:
- (a) If M <= √n/4, then ∫_{f > n/(8M)} f² >= n/4, on a set of measure <= 8M²/n.
- (b) A Chowla counterexample (M = ε√n) is SPIKE-DOMINATED: ∫_{f > √(n/ε)} f² >= (½ − √ε − 2ε²)n on a set of
  measure <= ε^{3/2}. The same holds for H·f for every admissible H (with m = M + mean(H·f)).
- (c) Equivalently 1_A is ℓ²-close to its projection onto the characters in U = {f > λ}: ‖P_U 1_A‖² >= (1 − O(√ε))|A|,
  with |U| <= ε^{3/2}. So A must be "almost U-band-limited": a union of long Bohr-type pieces.
- (d) TD4 (P39) is the computable third-moment surrogate of this distributional statement.

## P41. Curved cumulative rounding: M >= c√n via spike truncation + van der Corput — PROVED on paper (lead
## 2026-10-19; first application of P40; not kernel-checked; priority unchecked)
Setting:
- p: [0,1] -> [0,1] of bounded variation V(p). X >= 1, σ ∈ [0,1), p_m = p(m/X), Φ(m) = Σ_{i<=m} p_i.
- a_m = ⌊σ + Φ(m)⌋ − ⌊σ + Φ(m−1)⌋ ∈ {0,1}, A = {m <= X : a_m = 1}, n = |A|, β_m = a_m − p_m.
Hypotheses: [0,1] = 𝒢 ∪ ℬ (disjoint), where:
- 𝒢 is a union of N_G closed intervals, on each of which p ∈ C² with c₁ <= |p'| <= c₂ and |p''| <= c₃
  ("curved part");
- ℬ is a union of N_B intervals, on each of which p <= ½ or p >= ½;
- γ := ∫_𝒢 p(1−p) − 24·∫_ℬ min(p, 1−p) > 0. (Both terms are linear in the density, so the hypothesis is not weak at
  small densities.)
Theorem. There are c = c(c₁, c₂, c₃, N_G, γ) > 0 and X₀ = X₀(p) such that for every σ and every X:
- M(A) >= c√X >= c√n when X >= X₀;
- M(A) >= ½ >= √n/(2√X₀) when X < X₀.
NO monotonicity, rationality of densities or front-loading condition is needed.
Proof.
1. Sawtooth identity. Let s(m) = {σ + Φ(m)} − ½. Then β_m = s(m−1) − s(m) exactly.
2. Vaaler (1985; Graham–Kolesnik Thm A.6). There is ψ_K(θ) = Σ_{1<=|k|<=K} c_k e(kθ), |c_k| <= 1/(2π|k|), with
   |{θ} − ½ − ψ_K(θ)| <= F_K(θ)/(2K+2), where F_K = Σ_{|k|<=K}(1 − |k|/(K+1))e(k·) >= 0.
   Put s_K(m) = ψ_K(σ + Φ(m)) and r = s − s_K.
3. Decomposition: f_A = f_ρ + P + Q + f_ℬ.
   - f_ρ = Σ p_m cos mx.
   - P = Σ_{m∈𝒢_X} (s_K(m−1) − s_K(m)) cos mx.
   - Q = Σ_{m∈𝒢_X} (r(m−1) − r(m)) cos mx.
   - f_ℬ = Σ_{m∈ℬ_X} β_m cos mx.
4. P is uniformly O(√(KX)).
   - On a curved piece I = [u, v], summation by parts gives
     Σ_I (s_K(m−1) − s_K(m))e^{imx} = (e^{ix} − 1)Σ_{u<=m<v} s_K(m)e^{imx} + O(1 + log K).
   - Midpoint Euler–Maclaurin: Φ(m) = Φ̃(m) + O(c₃/X), where Φ̃(t) = const + X·P̄((t+½)/X), P̄' = p, so that
     Φ̃'' = p'/X ∈ ±[c₁, c₂]/X.
   - Van der Corput's 2nd-derivative test (Graham–Kolesnik Thm 2.2) for F(t) = kΦ̃(t) + tx/2π, uniformly in x:
     |Σ_I e(kΦ(m) + mx/2π)| <= C(c₂ + 1)c₁^{−1/2}√(|k|X) + O(|k|c₃).
   - So sup_x |P| <= C₆√(KX) for X >= K³, with C₆ = C₆(c₁, c₂, N_G), using Σ_{k<=K} k^{−1/2} <= 2√K.
5. Small-L² pieces (normalized ∫ dx/2π; x₀ := X^{−0.6}).
   - Q: |r| <= F_K/(2K+2), so ‖Q‖² <= (1/(2K+2))·Σ_{𝒢_X^+} F_K(σ + Φ(m)). By step 4 the k ≠ 0 terms are
     O(K^{3/2}√X), so ‖Q‖² <= X/(2K) for large X.
   - f_ℬ: cumulative rounding has interval discrepancy < 1, and (a − p)² <= a + p (when p <= ½; symmetric otherwise).
     So Σ_ℬ β² <= 2Σ_ℬ min(p_m, 1−p_m) + N_B and ‖f_ℬ‖² <= X∫_ℬ min(p, 1−p) + o(X).
   - f_ρ: one Abel summation gives |f_ρ(x)| <= π(1 + V(p))/|x|, so ∫_{|x|>=x₀} f_ρ² <= 2π²(1 + V)²X^{0.6} = o(X).
   - f_β near 0: |f_β(x)| <= |x|X/2 + 1, so ∫_{|x|<x₀} f_β² = O(X^{0.2}). The bulk lives away from the central spike.
6. Spike truncation (P40). Let λ = 2C₆√(KX) and f_bad = f_ρ + Q + f_ℬ.
   - On G* = {|x| >= x₀, |f_bad| <= λ/2} we have f <= λ.
   - Chebyshev on B* = {|x| >= x₀, |f_bad| > λ/2} gives ∫_{B*} f² <= 4‖f_bad 1_{|x|>=x₀}‖².
   - Hence ∫_{G*} f² >= ½Σ_𝒢 β² − 12‖…‖² − o(X) >= X(½∫_𝒢 p(1−p) − 12∫_ℬ min − 6/K) − o(X) >= γX/8 for
     K = ⌈24/γ⌉.
   - Here Σ_I β² = Σ_I p(1−p) ± (1 + V(p|_I)) on each curved piece I, exactly: Σβ² = Σa(1−2p) + Σp², and Abel
     summation with β = s(m−1) − s(m) gives |Σ_I β(1−2p)| <= 1 + V(p|_I).
   - P40: ∫_{G*} f² <= (λ + M)M + M². So M >= min(√γ/8, 3γ/(64C₆√K))·√X. ∎
Covers:
- every cumulative rounding of a C² profile with p' ≠ 0, at ANY start density (irrational included), e.g.
  g(1 − t) or g(1 − t)²;
- non-monotone profiles;
- TD2's ½(1 − t)² (the end region p' -> 0 is in ℬ, with ∫_ℬ min ≈ c₁³/6, small);
- power-law pieces away from cusps.
Exactly what escapes: rounding energy on FLAT pieces (p' ≈ 0), i.e. locally Sturmian words of fixed slope α.
- These are spike-dominated: spikes at 2πkα of height ≈ length/(πk).
- Rational α: P38's denominator filter (1 − cos qx).
- Irrational flat α: open (needs a Bohr filter with ‖qα‖ small; agent T3).
Meaning:
- Minimal-discrepancy (Sturmian) rounding of a CURVED density carries an O(√X)-bounded bulk of energy ≍ X, so
  spikes cannot hide it.
- This is a mechanism different from P31 (linear profile constraint) and P38 (window on filtered energy), and it
  does not care about front-loading.

## P42. LM-dense is FALSE (TD5) — PROVED on paper (round-2 agent 2026-10-19, report .research/agents/tdense2_report.md
## §TD5; every step checked by the lead; not kernel-checked)
For every t >= 1024 there is (by a terminating search; existence via the probabilistic method) A_t ⊂ [1, X], X = 2^t,
n >= X/16, such that for EVERY 1 <= q <= X:
    V_q >= X/256,    W_q >= X²/(2^28 J²),    J = 128(t+1).
So W_q/V_q^{3/2} -> ∞ uniformly in q, and no single filter (1 − cos qx) with TD4 gives c√n. Also M(A_t) >= √n/128,
witnessed at x = π: this disproves the certificate, not T-dense.
Construction:
- B = F_N + (1/4J)Σ_i [F_N(x − θ_i) + F_N(x + θ_i)], with Fejér F_N, N = X + 1, and θ_i uniform on 16X points.
- Profile p_m = ½(1 − m/N)[1 + (1/2J)Σ cos mθ_i] ∈ [w/4, 3w/4]; independent Bernoulli(p_m) rounding.
Mechanism:
- For each q, the order of q mod 16X is >= 16, so >= J/4 bumps have cos(qθ_i) <= 0 (Chernoff, union bound over q).
- Each such bump survives the filter (H_q >= 3/4 on it) and contributes N²/8192·(4J)^{−3} to ∫(H_q B)³; cubes of
  nonnegative summands add.
- The rounding noise is uniformly <= R ≍ √(X log X) and perturbs the cube by <= 63R³.
This is the rigorous form of P39-O(ii), using positive Fejér bumps instead of sharp Bohr sets.

## P43. Reciprocal spike masks (TD6) — PROVED on paper for the P42 family (agent; lead-checked)
- With H = 1/(1 + B) (0 < H <= 1, H >= 1/13 off {B > 12}, a set of measure <= 1/8), with probability >= 1 − O(1/X)
  over the rounding:
  - |∫Hf| <= 33;
  - Var(Hf) >= X/2^20;
  - centered ∫|Hf − μ|³ <= 2^16 X^{3/2}.
- TD4 then gives M >= √X/2^58, with NO dependence on J: no (3/8)^{J/2} product-filter loss.
- H can be replaced by the polynomial H_d = Σ_{k<=d}(L − B)^k/(1 + L)^{k+1}, L = 3N/2, of degree O(N log X).
- Exact moment formulas for any finite positive multiplier: μ = R₁, V = R₂ − μ², W = R₃ − 3μR₂ + 2μ³, with
  R_j = (h^{*j} ∗ s^{*j})(0)/2^j.

## P44. P38 under bounded discrepancy plus local overshoot (TD7) — PROVED on paper (agent; lead-checked)
- Hypotheses: P38's profile hypotheses (q, r/q start, slope L, tail mass μ_tail), and ANY binary a with prefix
  discrepancy |Σ_{i<=j}(a_i − p(i/X))| <= D, plus the averaged local-overshoot bound
  (LO) O_q(w) = Σ_{j<=w}(d_j − r)₊ <= K0 + K1(w+1)(w+q)/X, where d_j = Σ_{i=j+1}^{j+q} a_i.
- Conclusion: M >= c(p, q, D, K0, K1)√n.
- Proof:
  - Σz <= qL(w+1)(w+q)/X + 2qD, and Σ|z| = Σz + 2O_q(w), which gives the front energy.
  - Tail energy: discrepancy bounds q-chain runs by K_run = ⌈2D(q+1)⌉ + 1, and b_j >= ½ at every run start.
  - Then the TD-window as in P38.
- P44-O (TD7-O, PROVED): bounded discrepancy alone does not suffice for the FIXED filter q = 2.
  - Block construction mixing 1100-patterns in the front with q-chains later; D = B + 1 fixed.
  - The TD-window numerator is negative at every proportional scale. Filters q = 4, 8, 16 are not excluded
    (they work numerically).

## P45. Fixed-order moment certificates cannot see bulk behind spikes (TD8) — PROVED (agent; lead-checked)
- For every r there is C_r < ∞ and a centered distribution T_X with variance ≍ X and min T_X = −√X − O(1)
  (bulk ±√X plus a rare spike X·U[1,2] with probability 1/X), such that every shifted Hankel matrix through moment
  2r+1 is PSD at m = C_r.
- So moment-PSD certificates of bounded order give only m >= O(1) on spike-plus-bulk laws.
- Exact Schur thresholds r = 1, 2, 3: 80/27, 69125/4488, 792130993/2241000 (the report's 107/27 for r = 1 is a looser
  sufficient value).
- Lesson: an ADAPTIVE mask (P43) or a cosine-specific relation is required.

## P46. Mask-selection reduction MS (T4) — PROVED reduction; MS itself CONJECTURED (agent; lead-checked)
- MS: for every C there are K, L, η > 0 such that every large A ⊂ [1, Cn], |A| = n, admits:
  - a nonnegative trigonometric polynomial B with ∫B <= K;
  - a real γ with |γ| <= K;
  such that, with H = 1/(1 + B) and R = f_A − γ(B − ∫B):
    ∫H²R² >= ηn,   |∫HR| <= K,   ∫|HR|³ <= L·n^{3/2}.
- MS ⇒ T-dense (via TD4: the bounded structural part γH(B − ∫B) costs O(K²)).
- MS is the moment-computable relative of SB (NOTEBOOK): remove bounded-mass positive structure and a bulk must remain.
- It holds on the P42 family (P43). The deterministic case is the open core.

## P47. Smoothing-defect filter + window: Chowla for bounded-discrepancy roundings with non-front-loaded rounding
## energy — PROVED on paper (lead 2026-10-19; not kernel-checked; numerically audited E69b)
Setting.
- X >= 1; a model sequence P_1, …, P_X ∈ [0,1] (P_j := 0 for j > X); any a ∈ {0,1}^X; A = {j : a_j = 1}.
- β = a − P; D₀ = max_k |Σ_{j<=k} β_j| (prefix discrepancy); V = Σ_{j=1}^{X} |P_{j+1} − P_j|.
- P̄ = even extension of P to Z with P̄_0 := P_1; Q₂ = Σ_{j∈Z} |P̄_{j+1} − 2P̄_j + P̄_{j−1}|.
- Rounding energy e_j = P_j(1 − P_j).
- Integers h, w >= 1; κ_w(j) = (1 − j/(w+1))₊, W = 1 + 2Σ_{j<=w} κ_w(j)², L = X + h + w, ρ_L as in P31
  (ρ_L <= (4/(3√3))(1 + 2/√(L+1))³).
- δ = 4D₀/(h+1) (assume δ <= 1).
Theorem. Put
    E⁻ = Σ_{j<=X} e_j − D₀(1 + 2V) − 2δ Σ_{j<=X}|β_j|,
    S⁺ = Σ_{j<=w} κ_w(j)² e_j + D₀(2 + 2V) + 3δw,
    Δ  = W·E⁻ − ρ_L(L+1)·S⁺.
If Δ > 0, then
    M(A) >= √(Δ / (2(ρ_L(L+1) − W))) − π² h(h+2) Q₂/96 − δ/2.
Proof.
1. Filter. H(x) = 1 − K_h(x)/(h+1), with K_h the Fejér kernel Σ_{|k|<=h}(1 − |k|/(h+1))e^{ikx}. Then 0 <= H <= 1, so
   T := H·f_A >= −M.
2. Split f_A = f_P + f_β (f_P = Σ_{j<=X} P_j cos jx). Then G := H f_β = T − H f_P >= −(M + U), with U := sup_x H f_P.
3. U bound (the smooth part is invisible after filtering). Φ(x) = Σ_j P̄_j e^{ijx} = P̄_0 + 2f_P, so
   H f_P = ½HΦ − ½P̄_0 H <= ½ H|Φ|.
   - Second summation by parts: −4 sin²(x/2) Φ(x) = Σ_j (Δ²P̄)_j e^{ijx}, so |Φ| <= Q₂/(4 sin²(x/2)).
   - H = Σ_k κ̃_k(1 − cos kx) <= x² Σ κ̃_k k²/2 = x² h(h+2)/12, with κ̃_k = (1 − |k|/(h+1))/(h+1).
   - With x²/sin²(x/2) <= π² on [−π, π]: U <= π² h(h+2) Q₂/96.
4. Coefficients of G. G = ½Σ_j γ_j e^{ijx} with γ = β̄ − κ̃ ∗ β̄ (β̄ = even extension, β̄_0 = 0).
   - Every interval sum of β̄ is at most 2D₀ in modulus, and TV(κ̃) = 2/(h+1).
   - Abel summation gives |(κ̃ ∗ β̄)_j| <= 4D₀/(h+1) = δ for all j; in particular |γ_0| <= δ.
5. Energy pinning (the nonlinear input a² = a).
   - Σ_{j<=k} β_j² = Σ_{j<=k} e_j + Σ_{j<=k} β_j(1 − 2P_j).
   - Abel summation: |Σ u_j β_j| <= D₀(sup|u| + TV(u)).
   - Hence |Σ_{j<=X} β_j² − Σ e_j| <= D₀(1 + 2V), and |Σ_{j<=w} κ_w(j)²(β_j² − e_j)| <= D₀(2 + 2V).
   - Then E := Σ_{j>=1} γ_j² >= Σ_{j<=X} β_j² − 2δΣ|β_j| >= E⁻, and S := Σ_{j<=w} κ_w(j)²γ_j² <= S⁺,
     using γ_j² <= β_j² + 3δ.
6. Window. Apply the P31 chain to G + m >= 0, m = M + U. The degree is <= L, and the mean of G is γ_0/2. With
   m' = m + γ_0/2 >= 0:
       W(m'² + E/2) <= ρ_L(L+1)(m'² + S/2),
   so m'² >= Δ/(2(ρ_L(L+1) − W)), and M = m − U >= m' − δ/2 − U. ∎
Corollary (asymptotic form).
- Fix p: [0,1] → [0,1] of bounded variation and piecewise C², and take P_j = p(j/X). Let e = p(1 − p),
  ē = ∫_0^1 e, ē_θ = (1/θ)∫_0^θ (1 − t/θ)² e(t) dt, ρ = 4/(3√3), and
      Γ(θ) := (2/3)ē − ρ(1 + θ)ē_θ.
- If Γ(θ) > 0 for some θ ∈ (0,1], choose w = ⌊θX⌋ and h + 1 = ⌈48D₀/Γ(θ)⌉. Then for every rounding a with prefix
  discrepancy D₀ <= c(p)X:
      M(A) >= c(p, θ)√X − C(p)(1 + D₀² Q₂),
  with Q₂ = O_p(1/X) if p is Lipschitz with p(1) = 0, and Q₂ = O_p(1) if p has finitely many jumps.
- Hence √X up to D₀ ≍ X^{3/4} (Lipschitz) or X^{1/4} (jumps).
- No cumulative structure, curvature, Diophantine condition or local-overshoot hypothesis is used.
- Front condition: Γ(0+) > 0 ⟺ e(0) < (2/ρ)ē ≈ 2.598ē.
  - Every profile with p(0) = 1 (e(0) = 0) qualifies at small θ: e(t) ≈ |p'(0)|t, so Γ(θ) > 0 for
    θ < 8ē/(ρ|p'(0)|).
  - TD2's ½(1 − t)² qualifies (e(0)/ē = 2.143). ½(1 − t)³ does not (2.8), nor ½(1 − t)⁴ (3.46).
Relation to P38/P44/P41.
- P44 (bounded discrepancy) needed the local-overshoot hypothesis LO, and P44-O shows the fixed q = 2 filter fails
  without it. P47 needs no LO for profiles in its class, including TD2's ½(1 − t)².
- P41 and TD11 need cumulative rounding and curvature. P47 needs neither.
- The escape class moves from FRONT-LOADED DENSITY (P31: p(0)/p̄ >= 2.6) to FRONT-LOADED ROUNDING ENERGY
  (e(0)/ē >= 2.6 at every scale).
Meaning.
- This is the separation that session 2 lacked (NOTEBOOK "Front-loaded sets reduce to signed problems": f = P + N, and
  f >= −M gave no bound on N alone).
- The defect filter 1 − K_h/K_h(0) makes the smooth part uniformly O(h²Q₂). For bounded-discrepancy fluctuations it
  is the identity up to O(D₀/h).
- The identity a² = a pins the fluctuation's energy profile to p(1 − p), up to O(D₀(1 + V)).

## P48. Macroscopic twisted-profile constraint (TD9) — PROVED on paper (round-3 agent, .research/agents/
## tdense3_report.md §TD9; lead re-derived every step 2026-10-19)
- Statement.
  - Let X_j → ∞, A_j ⊂ [1, X_j], M(A_j)/X_j → 0, and let θ_j be any angles.
  - Put ν_j = (1/X_j) Σ_{a∈A_j} e^{iaθ_j} δ_{a/X_j}. Every weak limit is q(t)dt on [0,1], with |q| <= 1.
  - Put H(t) = q(t)/2 on (0,1), conj(q(−t))/2 on (−1,0), and 0 outside. Then H has a continuous positive-definite
    representative, i.e. F(y) = Re∫_0^1 q(t)e^{ity}dt >= 0 for all real y.
  - Hence q is continuous on (0,1), q(0+) is real, and q(1−) = 0. A nonzero step function q is impossible.
- Proof: f_{A_j}(θ_j + y/X_j)/X_j → F(y) locally uniformly, and f >= −M. F >= 0 integrable (Gaussian/Fubini), then
  Bochner/inversion.
- Scope: heights ≍ X only. Spikes of height ≍ √n vanish after dividing by X. Macroscopic, not √n-scale.

## P49. Fixed fractional flat piece ⇒ LINEAR M (TD10) — PROVED on paper (agent; lead checked the coefficient
## formula and the contradiction step)
- Fixed profile p with a finite partition into flat pieces and C² pieces with |p'| bounded away from 0. Cumulative
  rounding with any phase σ. If some flat piece has value α ∈ (0,1), then M(A_X) >= c(p)X uniformly in σ.
- Mechanism: at θ = 2πα the twisted density on that piece has modulus d_α = sin(πα)/π (irrational α) or
  sin(πr/q)/(q sin(π/q)) (α = r/q). Curved pieces contribute 0 (van der Corput), so q_θ is a nonzero step function,
  which P48 forbids.
- Ineffective constant (compactness). Corollary: every fixed finite staircase with positive integral has linear M.
- It closes the "flat pieces" escape in P41 for FIXED profiles. Staircases with X-dependent step counts remain open.

## P50. P41+ and P41-B for fixed profiles (TD11, TD12, TD12-F) — PROVED on paper (agent; lead spot-checked the energy
## identity and the cohomology step, not every exponential-sum constant)
- TD11: fixed flat/curved profile with curved rounding energy η = ∫_curved p(1 − p) > 0 ⇒ M >= c(p)√X. Flat energy is
  excluded. With P49 this matters only when the flat values are in {0,1}.
- TD12: cumulative rounding of p_m = P(m/X, mα), P smooth on [0,1]×T^d, α Diophantine, |P0'| ∈ [c1, c2],
  η = ∫∫P(1 − P) > 0 ⇒ M >= c(P,α)√X.
  - Cohomological equation P − P0 = Ω(t,θ) − Ω(t,θ−α), giving Φ = Φ0 + Ω + O(1/X).
  - Weighted van der Corput, then the bounded-bulk Tool C.
- TD12-F: a fixed finite Fourier profile needs no Diophantine condition (use the orbit-closure average).
- Tool C (reusable): if f = P + B + E with ‖P‖_∞ <= L√X, ‖P‖₂² >= aX, ‖E‖₂ <= δ√X (δ <= √a/8), and B is
  o(√X) in L² off sets of measure → 0, then M >= min(√a/4, a/(16L))√X.

## P51. Bump obstructions (TD13, TD14) — PROVED (agent; lead checked)
- TD13: φ_L = F_L·(1 + cos 2Lx) >= 0 is localized at width 1/L, yet φ̂_L(L) = 0 and φ̂_L(2L) = ½. Positivity plus
  localization does NOT force monotone Fourier decay. The "positive bumps have decaying transforms" route (brief T1(b))
  is killed in its unrestricted form.
- TD14: if f_A + m = Σ_{j<=J} w_j F_L(x − θ_j) exactly (w_j > 0, L > X = max A), then J >= L − X and
  m >= L/(2(L − X)). Proof: coefficient at k = X, plus Vandermonde on k = X+1..L−1.
  No robust (L²-error) version is known.

## P52. Local Bessel budget for macroscopic twisted profiles — PROVED (lead 2026-10-19; elementary)
- Setting as in P48: X_j → ∞, A_j ⊂ [1, X_j], and twisted limits q_θ at finitely many distinct fixed angles
  θ ∈ Θ, with q_0 = p (the density profile). No hypothesis on M.
- Statement: p(t)² + Σ_{θ∈Θ\{0}} |q_θ(t)|² <= p(t) for a.e. t. Equivalently Σ_{θ≠0}|q_θ|² <= e := p(1 − p).
- Proof.
  - For smooth ψ >= 0 on (0,1), put b_m = 1_A(m)ψ(m/X). Then ‖b‖² = Σ_{a∈A} ψ(a/X)² = X∫pψ² + o(X), using a² = a.
  - For |y| <= Y: b̂(θ + y/X) = X∫ψ q_θ e^{ity} dt + o(X). So the energy of b̂ on |x − θ| <= Y/X is
    X∫|ψq_θ|² − O(X/Y) + o(X) (Plancherel on R, plus the tail of a smooth transform).
  - The windows are disjoint for distinct θ, so Bessel gives Σ_θ ∫ψ²|q_θ|² <= ∫ψ²p. Since ψ is arbitrary, the
    statement follows. ∎
- Meaning.
  - The macroscopic rounding energy e(t) = p(1 − p) is a budget. Macroscopic atoms (heights ≍ X) can absorb part of it.
  - The residual b(t) = e(t) − Σ_{θ≠0}|q_θ(t)|² >= 0 must sit in MESOSCOPIC spikes (√n << height << X) or in the bulk.
  - With P48, each absorbed atom must have a PD continuous profile q_θ with q_θ(1) = 0.

## P53. Macro-SB: M = o(X) forces a NON-ATOMIC local spectrum (joint form of P48) — PROVED on paper (lead
## 2026-10-19; not yet adversarially checked; priority unchecked)
Setting.
- X_j → ∞, A_j ⊂ [1, X_j], |A_j| >= X_j/C, M(A_j) = o(X_j).
- Γ = a countable additive group of angle sequences θ = (θ_j)_j that is NONDEGENERATE: X_j‖θ_j‖_{R/2πZ} → ∞ for every
  θ ≠ 0 in Γ. Examples: the group generated by finitely many fixed angles that are rationally independent mod 2π;
  X-dependent atom locations are allowed.
- K = Γ^ (compact, metrizable). ι_j: Z → K, ι_j(a)(θ) = e^{iaθ_j}. χ_θ(ω) = ω(θ).
Construction.
- ν_j = (1/X_j) Σ_{a∈A_j} δ_{(a/X_j, ι_j(a))} on [0,1] × K. Pass to a weakly convergent subsequence: ν_j → ν.
- Nondegeneracy gives (1/X)Σ_{m∈[sX,tX]} e^{imθ_j} → 0 for θ ≠ 0, so the full-integer measures tend to Leb × Haar.
  Hence ν = g dt dω with 0 <= g <= 1.
- Twisted limits: (1/X)Σ_a e^{iaθ_j} δ_{a/X} → q_θ(t)dt, with q_θ(t) = ∫_K g(t,ω)χ_θ(ω)dω. q_0 = p, the density profile.
- Local Bessel/Parseval on K: Σ_{θ∈Γ}|q_θ(t)|² = ∫_K g(t,·)² <= ∫_K g(t,·) = p(t).
  - The defect b(t) = ∫_K g(1 − g) is the local spectral mass NOT carried by Γ-atoms. (P52 is the case of finitely
    many θ.)
Theorem. ∫_0^1 ∫_K g(1 − g) dω dt > 0. Consequently Γ-atoms never carry all of the local spectral mass.
Moreover the reflection g̃(t,ω) = g(t,ω) (t > 0), g(−t,−ω) (t < 0), 0 (|t| >= 1) is a.e. equal to a continuous
positive-definite function on R × K.
Proof.
1. Partial transform: ∫_K g̃(t,ω)χ_θ(ω)dω = q_θ(t) for t > 0 and conj(q_θ(−t)) for t < 0.
   Hence Ĝ(y,θ) := ∫_R∫_K g̃ e^{ity}χ_θ = 2Re∫_0^1 q_θ(t)e^{ity}dt.
2. P48, applied at the angle sequence θ_j for each θ ∈ Γ (P48 allows j-dependent angles), gives Ĝ(y,θ) >= 0 for all
   (y,θ) ∈ R × Γ.
3. Ĝ ∈ L¹(R × Γ), with ‖Ĝ‖₁ <= 2π.
   - Test against φ_δ(y,θ) = e^{−δy²}ψ_δ(θ), where ψ_δ(θ) = |F_δ ∩ (F_δ + θ)|/|F_δ| for a Følner sequence F_δ of Γ
     (ψ_δ is PD, ψ_δ → 1 pointwise, and its inverse transform is >= 0 with mass 1).
   - Then ⟨Ĝ, φ_δ⟩ = 2π⟨g̃, φ̌_δ⟩ <= 2π‖g̃‖_∞. Fatou gives the bound.
4. Fourier inversion: g̃ is a.e. equal to a continuous PD function g_c.
5. If g ∈ {0,1} a.e., then g_c ∈ {0,1} everywhere: Leb × Haar charges every nonempty open set.
   - For each ω, t ↦ g_c(t,ω) is continuous, {0,1}-valued, and 0 for |t| > 1, so it is ≡ 0.
   - Hence ∫∫g = 0, contradicting ∫∫g = lim|A_j|/X_j >= 1/C. ∎
Corollaries and meaning.
- TD10/P49 follows. On a fractional flat piece the local pattern is the 0/1 Sturmian window. On curved pieces it is
  uniform (g = p). Continuity of g_c in t fails at the junctions.
- Bohr-interval sets A = {m : {mα} ∈ E(m/X)} (α irrational, E(t) ⊂ T Jordan-measurable windows of measure p(t))
  have g ∈ {0,1}. So M >= c·X along every sequence: LINEAR M for every Bohr-window set with a nonzero profile, whatever
  the windows. Same for finite-rank Bohr patterns over T^d and for residue-class patterns (finite K).
- For the √n problem: a counterexample has M = o(X), so a positive part of its local spectrum is not carried by ANY
  countable nondegenerate family of macroscopic atoms. That part lives in spikes of height o(X) (mesoscopic) or in the
  bulk. This is the first step of a descent: macroscopic structure alone cannot produce a counterexample.
- Not quantitative: compactness, and the defect is upper semicontinuous in the wrong direction for a direct
  finite-X version. A quantitative, multiscale form is the next target (NOTEBOOK).

## P54. Torus level-1 inequality (TL1) — PROVED (lead 2026-10-19; elementary; uses the classical Steinhaus rotation
## trick; priority unchecked)
Statement.
- Let K be a compact abelian group with Haar probability measure and Γ = K^.
- Let Λ ⊂ Γ be a set of characters on which some homomorphism ψ: Γ → R is ≡ 1 (a level set of a real grading). For
  example, Λ = rationally independent irrational frequencies, or any subset of a free basis. Torsion characters are
  excluded.
- Then for every measurable E ⊂ K with |E| = p:
      W_Λ(E) := Σ_{λ∈Λ∪(−Λ)} |1̂_E(λ)|² <= θ(p)·p(1 − p),   θ(p) := 2·env(p)/(π² p(1 − p)) <= 8/π² = 0.8106,
  where env = the concave envelope of sin²(πx) on [0,1]:
  - env(x) = (sin²(πx₀)/x₀)·x for x <= x₀, with tan(πx₀) = 2πx₀, x₀ ≈ 0.371;
  - env(x) = sin²(πx) on [x₀, 1 − x₀];
  - env is symmetric.
- Equality θ = 8/π² iff p = ½ and E is a half-circle in a single coordinate.
Proof.
1. L := P_Λ(1_E − p) = Re Z with Z = Σ_{λ∈Λ} c_λ χ_λ, and W_Λ = ‖L‖² = E[1_E L].
2. Rotation invariance. φ ↦ τ_φ with χ(τ_φ) = e^{iφψ(χ)} is a continuous one-parameter subgroup of K. Translating by τ_φ
   multiplies Z by e^{iφ}, and Haar measure is invariant, so Z has a rotation-invariant law. Hence (Z, E) can be coupled
   as Re Z = R cos Φ with R = |Z| and Φ uniform and independent of R.
3. For any F with P(F) = p, conditional on R, the best set in Φ is an arc. So
   E[1_F R cos Φ] <= E[R·sin(π π_R)/π], with π_R = P(F | R) and E π_R = p.
4. Cauchy–Schwarz: <= (1/π)√(E R²)·√(E sin²(π π_R)) <= (1/π)·√(2‖L‖²)·√(env(p)).
5. Hence ‖L‖² = E[1_E L] <= (1/π)√(2 env(p))·‖L‖, i.e. W_Λ <= 2 env(p)/π². ∎
Checks.
- E71: the numerical sup is 0.8106 (p = ½), 0.7637 (p = 0.4; bound 0.764), 0.632 (p = 0.3; bound 0.659),
  0.34 (p = 0.1; bound 0.51). The bound holds and is sharp for p ∈ [x₀, 1 − x₀] at S = 1.
- Without the grading hypothesis the inequality fails. For Z_2 characters (Rademacher), a dictator has W = 100%.
Meaning for Chowla (NOTEBOOK 2026-10-19 night, cont. 2).
- A 0/1 local pattern can keep at most 81% of its variance on any graded-homogeneous set of spike frequencies (e.g.
  rationally independent spikes). At least 19% must sit at other levels (combinations Σk_s x_s with Σk_s ≠ ±1,
  including differences and torsion) or in continuous spectrum.
- Finite-window use needs the window to equidistribute in the relevant torus (length >> (1/η)^S), so it serves only for
  boundedly many tall spikes.

## P55. Round-4 agent results (.research/agents/tdense4_report.md; lead re-checked the items marked ✓) — 2026-10-19
- Audit verdicts:
  - P47 CONFIRMED-WITH-FIX. Finite theorem as written. The asymptotic corollary needs D₀ <= d·X^{3/4} with d small
    (Lipschitz case; X^{1/4} with jumps), the right limit e(0+), and positive total variance.
  - P53 CONFIRMED-WITH-FIX. The Bohr-window corollary needs B ⊂ [0,1] × T with boundary of product measure zero. The
    fiberwise version is FALSE: the agent's counterexample builds windows from Singer difference sets with prime X_j.
  - The Bohr-window numerics (1,044,480 Arb-certified memberships; α = golden ratio; p = (1−t)^k/2, k = 1, 2, 4) show
    M/X stable at 0.02–0.14.
- ✓ Pointwise defect (Krein/Gram): if h is continuous and PD on R × K, 0 <= h <= 1, and h = 0 for |t| > 1, then
  h(t,ω) <= 1 − t²/4. Hence the P53 defect is b >= (1/4)∫t²p >= m³/12 >= 1/(12C³), uniformly in K and its rank.
- Finite fixed-complexity QD (PROVED, ineffective). For fixed C, J, K there are η, X0 such that every A ⊂ [1, X] with
  n >= X/C, X >= X0 and M <= ηX has cosine energy >= X/(48C³) outside ANY J windows of radius K/X.
  - Moving centers with near-relations are handled by quotienting the relation lattice.
- ✓ Separated-window cover. A maximal 1/X-separated set of points of {f > H} has J <= 3πXn/H² points, and the radius-1/X
  windows around them cover {f > H}.
  - Proof: f(θ)² <= X∫_I f² + 2∫_I|ff'| on |I| = 1/X; sum; ∫f² = πn and ∫f'² <= πX²n.
- MP48 obstructions (PROVED).
  - The H-normalized twisted measures have total variation n/H → ∞, so they have no weak-measure limit.
  - L² profiles with nonnegative transform can be unbounded (h_α(t) = ∫_1^∞ s^{α−1}(1 − s|t|)₊ ds).
  - A formal joint-PD profile system on R × T^J saturates the Bessel budget exactly: q_0 = p, q_{±e_l} = aφ,
    a = 1/(4√J). It has h_J(0,e) = p(0) + √J/2 → ∞ and negative values. So PD plus Bessel cannot force a residual;
    the binary [0,1] bound must be retained.
    - LEAD NOTE: this system puts 100% of the variance on level-1 characters. P54 (TL1) caps that at 81% for every
      genuine [0,1] pattern. TL1 is exactly the binary input this obstruction asks for.
- HBCG (CONJECTURED; the precise missing inequality).
  - Statement: for every C there are c, B > 0 such that for large X, every A ⊂ [1, X] with n >= X/C, every H >= √n,
    and every union U of <= ⌈3πXn/H²⌉ radius-1/X windows centred at points with f_A > H:
        ∫_{U^c} f_A² dx/2π >= c·X − B·X·M(A)/H.
  - HBCG ⇒ T-dense (PROVED, agent; ✓ lead): take H = √(n/ε) and use P40 plus the cover above.
  - HBCG is the window form of QD-½ (NOTEBOOK cont. 5). Numerics: residual/X + M/H >= 0.1245 over 304 rows
    (76 sets).
- Corrections to the lead's notes.
  - Bu sets have an exact macroscopic residue atom f_A(2π/3) = n/4 (3-adic structure, known as T8). They do NOT have
    uniform local patterns at every fixed frequency.
  - "P31 is the h = 0 case of P47's filter" is literally false (H_0 = 0). P31 is the identity-multiplier case.

## P56. Round-5 agent results (.research/agents/tdense5_report.md; lead re-checked the items marked ✓) — 2026-10-19
- ✓ FTL1 (finite TL1, PROVED). Setting: any 0 <= a_m <= 1 on m = 1..Y with mean p, b = a − p, arbitrary angles x_s,
  c_s = mean b_m e^{imx_s}, W = Σ|c_s|², R = Σ|c_s|, Z_m = Σ c̄_s e^{imx_s}, L = Re Z. Then
      2W <= 2env(p)/π² + 2B_abs + 32R/(πD) + (16/π + 4p)·R·U_D,
  where:
  - B_abs is the pair large-sieve term;
  - U_D = Σ_{d<=D}|Δ_d|/d² measures the Chebyshev moment defects against the rotated law. These expand into
    phase-coherent UNBALANCED moments E Z^jZ̄^k, j ≠ k.
  - Positive-count form: U_D <= C_D Q_D, C_D = Σ3^d/d².
  - Proof (checked): hinge (Rcosθ − λ)₊ has |a_d| <= 4R/(πd²); Chebyshev majorant of degree D; CVaR comparison with
    L* = Re(e^{iΦ}Z); P54's rotation bound; W = E(aL) − pE L.
  The error is R/D, so the degree must grow with R = Σ|c_s|.
- FTL1-tail: R can be replaced by any T, at the price of the radial moment q_D(T) = E(|Z|/T)^D. This gives a
  dimension-free version under (E|Z|^D)^{1/D} <= L0√(DW). Binary obstruction: graded spike sets with divergent 4th
  moment ((1,j) on T², realized by actual words).
- GTL1 (Gaussian regime, Lindeberg): constant φ(Φ^{−1}(1 − p)), i.e. 2/π at p = ½, with explicit E_D errors.
- ✓ CY1 (exact cyclic P40 → TL1 bridge). Y even > 2X, a = 1_{A∪−A} on Z/Y, c_k = 2f_A(2πk/Y)/Y,
  Λ = {k < Y/2 : f > H}. Then
      2W >= p(1−p) − (4/Y)(HM + 2M²) − T_N,
  with B = 0 and E L = 0 exactly. CY2 = CY1 + FTL1 gives the relation alternative R·U_D >= (π/16)[γp(1−p) − … ].
  - LEAD CAVEATS (NOTEBOOK cont. 7):
    - (P1) The padded support/profile (central lobe, an AP with all c_k > 0) is never graded and supplies E L³ ≍ δ²p
      by itself, so the relation branch carries no information on the rounding spikes. It must be run block-locally,
      with the local mean removed.
    - (P2) L(0) = R ≈ M, so (E|Z|^D)^{1/D} >= R·Y^{−1/D}, and the radial-moment branch holds automatically for
      mesoscopic spikes.
- ✓ SG (stable Gram, PROVED). Let h be continuous on R × K, 0 <= h <= 1, h = 0 for |t| > 1, and the transform of a
  signed measure with negative mass δ. Then h <= 1 − t²/4 + 2δ and b >= m³/12 − 2δm. No rank or J dependence.
- HBSC (CONJECTURED; agent's single sufficient lemma). Height-uniform binary spectral completion: the tall windows
  of a counterexample sequence admit [0,1] lifts h_j with captured energy, mass n/X + o(1) and negative spectral
  mass <= B(C)M/H + o(1). HBSC ⇒ (SG) HBCG ⇒ T-dense (✓ chain).
- ✓ Interval obstruction: E_out([1,n]; μ) <= C/μ. So QD with any exponent β > ½ is FALSE (μ = n^{−a},
  1/(2β) < a < 1). This replaces the invalid Singer-at-μ=1 sharpness remark.
- Fixed-period residue families: M >= 2dX/(3π) − (q + 1)(1 + 3π/2) (Abel at x = 3π/(2X)). Bu sets have the torsion
  atom f(2π/3) = n/4 but are excluded rigorously by P16 and P31.
- NUMERICAL: 90 saved sets, 360 tall-spectrum and 360 cyclic rows (tdense5_scratch/). The golden half-window has
  two-sided mass 0.81066 → 8/π². Cosine-majority words with S = 4, 16, 64: 0.656, 0.640, 0.6395 → 2/π.
  No zoo row approaches ε → 0.
- Lead addition (PROVED, NOTEBOOK cont. 7): uniform LAW-LEVEL TL1 by radial truncation.
      W <= k_p√(W + B) + 4√(2(W + B)/(πD)) + A_D + p|E L|,
  where A_D is the angular-harmonic defect of the law of Z truncated to |Z| <= √(πD E|Z|²/2). The relative error
  4√(2/(πD)) is uniform in S, R and the tails. The bridge from the angular defect to usable structure is the gap.

## P57. Round-6 agent results (.research/agents/tdense6_report.md; adversarial "formal escape" round) — 2026-10-19
Lead re-checked the items marked ✓.
- ✓ Tent-lift identity (PROVED). Let X = max A, Y = X + 1, φ = (1 − |u|)₊, and
  h_θ(t) = Σ_a [e^{iaθ}φ(Yt − a) + e^{−iaθ}φ(Yt + a)]. Then
      Q_θ(y) = (2/Y) sinc²(y/(2Y)) f_A(θ + y/Y),
  and the total negative spectral mass is exactly mean_circle|f_A| >= n/(n + M), for every center θ.
  - Proof: the triangle transform plus the periodization Σ_k 4sin²(u/2)/(u + 2πk)² = 1.
  - On |y| <= T the negative mass is <= 2TM/(πY). So the negative mass ESCAPES to spectral infinity (microscopic
    scales). It is invisible to compact-frequency limits, yet ≍ 1.
  - Singer differences with H = n^α (½ < α < 1) have M/H → 0 but negative mass >= 1 − o(1). This refutes O(M/H)
    negative mass for these natural lifts.
- ✓ Binary-faithful lifts: from SG, b = o(1) forces δ >= m²/24 − o(1). Any lift preserving the microscopic binary
  pattern fails the HBSC bound. HBSC must coarse-grain, i.e. become fractional.
- ✓ Weighted Gram (sharpens SG; PROVED). D_N(u) = (1 − cos u) − (1 − cos Nu)/N² is >= 0 (and <= 2), from
  |1 − e^{iNu}| <= N|1 − e^{iu}|. Then:
      h(z) <= 1 − 1/N(t)² + ∫D_N(arg χ_ξ(z)) dν₋(ξ),   b >= m³/12 − G(h).
  D_N vanishes to fourth order at u = 0, so only high-phase negative mass counts. WGC (CONJECTURED) is HBSC with
  G(h) in place of δ; WGC ⇒ T-dense.
- ✓ Fractional relaxation (PROVED, elementary). Over weights 0 <= a_m <= 1 with Σa = n <= (X+1)/2, min(−min F) = n/X
  EXACTLY.
  - Lower bound: Σ_j F(2πj/(X+1)) = 0.
  - Attained by the Fejér weights a_m = (2n/X)(1 − m/(X+1)), F = (n/X)(K_X − 1).
  - Missing binary energy fraction → 1 − 4/(3C) >= 1/3.
  So the fractional problem has CONSTANT M, and all of Chowla's difficulty is the 0/1 constraint. The (1 − t) Fejér
  profile is the fractional extremiser.
- Exact energy audit: replacing words by conditional means loses Σa(1 − a) of binary energy (Parseval). Exact phase
  conditioning (gcd 1) recovers the word, so no fractional completion arises from it.
- Central-lobe audit: a literal model with all energy in mesoscopic windows (heights o(X)) is inconsistent, because
  the central peak forces >= cos(¼)²n/(4πC) energy outside. Valid formal tests must keep the central profile.
- OBSF (CONJECTURED): "ordered Boolean spectral floor" on the padded grid, i.e. HBCG on the exact idempotent array.
  OBSF ⇒ T-dense (✓; via P40 on the grid).
- Run-tops:
  - sharpened count Σ_{t>0}|B_t| = N(N−1)/2 − T₃ >= n² (ordered-rank count);
  - explicit averaged sufficient inequality Σ_t[‖Q2_t‖² + Kμ‖Q1_t‖₁²] <= D n K^{3−η}μ for Bu et al.'s Lemma 9.3
    split. LEAD (E76): this is FALSE on Bu sets, see NOTEBOOK cont. 9.
- NUMERICAL: 21 real sets, 515 component profiles, 21 genuine joint block lifts (negative mass 2–37, growing with q),
  7 endpoint LPs. Smallest R seen 0.606 (existing E68 set). No formal escape and no inconsistency proof.
- Verdicts:
  - HBSC is false for natural and binary-faithful lifts; the existential HBSC remains unresolved.
  - T-dense, WGC and OBSF remain open.

## P58. Round-7 agent results: T-dense(C) for every C < 4.4393 (C < 4.2138 with the elementary P31-E constant) —
## PROVED on paper, INEFFECTIVE constant; lead re-checked every step (2026-10-19). Report .research/agents/tdense7_report.md
Theorem (T-dense(C), C < C_7 := (2/r)(1 + √(1 − ρ*))², ρ* = the doubly-positive constant of P17).
- There is c(C) > 0 with M(A) >= c(C)√|A| for every nonempty finite A ⊂ Z_{>0} with max A <= C|A|.
- Here r is any asymptotic upper bound for P31's Nikolskii constant ρ_L:
  - r = 0.811 (P31-E, elementary, kernel-checked) gives C_7 = 4.2138;
  - r = 4/(3√3) (P31-N, Beckner) gives C_7 = 4.4393.
  These use P17(a)'s ρ* <= (1 + √17)/(4√2) = 0.90565.
- The sharp numerical ρ* ≈ 0.7239–0.7245 (E16, E78) would give C_7 ≈ 6.04–6.05.
- Previously proved: C < 2.44, effective (P31 dense theorem). Kolountzakis 1996 gave linear M for C < 2.
Proof (compactness; the lead checked each step).
1. Contradiction sequence: X_j <= C n_j, M_j/√n_j → 0. Since M >= 1/2, n_j → ∞.
   - The scaled coefficient measures (1/X)Σ_m 1_A(|m|)δ_{m/X} converge weak-* to p dt, with p even, 0 <= p <= 1,
     supported in [−1, 1], and d = ∫_0^1 p >= 1/C.
2. PD profile (untwisted P48). f_A(y/X)/X → ∫_0^1 p(t)cos(ty)dt >= 0 since M = o(X), so p̂ >= 0.
   - Gaussian testing plus monotone convergence gives p̂ ∈ L¹. Hence p is (a.e.) continuous and PD, with
     a := p(0) = max p and p(±1) = 0.
3. Exact high-pass diagonal (NEW, round 7). q = k_h ∗ a (normalized triangle kernel k_h on the coefficient
   sequence), r = a − q.
   - Choose h_j → ∞ with h_j/X_j → 0 (diagonal over h = εX, then ε → 0) so that the scaled q → p strongly in L².
   - Since a² = a, (a − q)² = a − 2aq + q², and the scaled measures Σ r_m²δ_{m/X}/X → e dt with e = p(1 − p).
     The cross term a·q → p² by Cauchy–Schwarz against the strong L² limit.
   - H_h = 1 − K_h/(h+1) ∈ [0,1], so T = H_h f_A >= −M. Its coefficients are r_m. T − r_0/2 >= −m with 0 <= m <= M.
4. Windows. P31's chain needs no coefficient positivity (Fejér–Riesz + Parseval; the lead re-derived it for the
   centred T). Apply it to f_A and to T with w = θX, divide by X², and let j → ∞:
       (2θ/3)∫_0^1 v <= r(1 + θ)∫_0^θ (1 − t/θ)² v(t)dt   for v = p and v = e.
   - θ → 0 gives (W): a >= 2d/r and a(1 − a) >= 2b/r, with b = ∫_0^1 e = d − ∫_0^1 p².
5. PD L²/L¹ gap (= P17(a)). For q = p/a (nonnegative, PD, q(0) = 1): ∫q² <= ρ*∫q, so ∫p² <= ρ* a d and
   b >= d(1 − ρ* a).
6. Combine: d <= (r/2)·a(1 − a)/(1 − ρ* a) <= (r/2)/(1 + √(1 − ρ*))². The maximum over a is at
   a = 1/(1 + √(1 − ρ*)). This contradicts d >= 1/C when C < C_7. ∎
   - Rational certificate (moment_gap.py, exact Fractions; lead checked the logic): with k = 2/r, C is valid when
     k − (kρ + C)²/(4C) > 0, i.e. Ca² − (C + kρ)a + k > 0 for all a.
   - C = 44393/10000, r = 0.769801 (0.769801² > 16/27), ρ = 0.905646 > ρ*: margin 3.3e-6.
   - C = 4.213 with r = 0.811: margin 1.4e-4.
- Round 7's first version R7-T used the stable Gram bound p(t) <= a(1 − t²/4) instead of step 5 and gave
  C = 3 (exact algebra: algebra.py, margin 640985/3409625664). The CF envelope p(t) <= a·cos(π/(⌊1/t⌋ + 2)) gives
  C = 4.164 (r = 0.811) and C = 4.331 (r = 0.77) (envelope_exact.py). Both are superseded by step 5 and kept as
  independent routes.
Lead's verification notes.
- Every limit is taken at fixed θ before θ → 0. Weak convergence of r² measures uses compact support and an
  absolutely continuous limit (no atom at 0).
- M² = o(X) is the only √n-scale input; PD needs only M = o(X).
- The lead re-ran witness.py and algebra.py on the VM: exact outputs reproduced.
- NOVELTY: step 5 is the project's own P17(a) (session 2; same constant, via a tangent-line variant). The agent
  re-derived it without citing P17. NEW here: the exact high-pass diagonal (step 3) and the assembly into T-dense(C_7).
  External priority unchecked beyond the agent's short search (Bu et al. 2026: dense n^{1/4}; Kolountzakis 1996:
  density > 1/2).
Obstruction to this method (PROVED, exact; lead re-ran the verifier).
- An explicit rational piecewise-linear profile p (48 cells, witness_B48.json) is PD (Sturm: symbol S has 0 roots in
  [−1, 1], S(1) > 0). It satisfies BOTH window inequalities for every θ ∈ (0, 1] (exact Bernstein certificates, 48
  cells each, r = 0.7698).
  - Values: p(0) = 0.6563, d = 0.165184, 1/d = 6.053863, b/d = 0.525.
- So "PD profile + density and energy windows" cannot prove T-dense(C) for C >= 6.0539. The method's reach C_PD lies
  in (4.4393, 6.0539], and numerically C_PD ≈ (2/r)(1 + √(1 − ρ*))² ≈ 6.046 (E78: ρ* ≈ 0.72387).
  - The extremal shape is the scaled half-sine autocorrelation q(s) = (1 − s)cos πs + sin(πs)/π (ρ = π²/24 + 5/16 =
    0.72373), with a ≈ 0.655 and support ≈ 0.62X, plus a vanishing tail.
- Realisations of the witness (cumulative and conditional-Bernoulli rounding, n = 512…4096) have R = 1.82–2.45 (point
  certificates R >= 1.82). These sets are Chowla-safe for other reasons: random rounding is bulk-dominated (P40), and
  cumulative rounding falls under the P41 regime. So the witness marks the limit of the METHOD, not a construction.
Supplementary (PROVED, elementary): dip filling M(F ∪ B) >= u − √(|B|/(2α)) when {f_F <= −u} has measure α. P31's
minimum bound alone gives no dip measure (interval: measure O(N^{−1/2})).
Status: paper proof, lead-verified, ineffective constant, NOT kernel-checked. Effective version and sharp ρ* OPEN.

## P59. Round-8 agent results (report .research/agents/tdense8_report.md; lead re-checked every item marked ✓) — 2026-10-19
1. ✓ ENERGY-PD ("product window"; NEW, short).
   - Setting: in P58's setting, T = H_h f = r_0/2 + g with g >= −m, 0 <= m <= M. Then g + m >= 0 POINTWISE, so its
     autocorrelation is >= 0 everywhere:
         m² + ½ Σ_{k>=1} r_k² cos(kx) >= 0   for all x.
   - Put x = y/X and divide by X. Since m² = o(X), the limiting residual energy profile e = p(1 − p) has a
     nonnegative cosine transform. So e is PD (continuous, compact support).
   - Consequence: e(t) <= e(0) for all t. If a = p(0) > ½, the continuous p crosses ½ (p(1) = 0), where e = ¼ > a(1 − a).
     Hence a <= ½.
   - The same identity for any filter 0 <= H <= 1 of degree o(X) makes every filtered energy marginal PD in t.
     For H = 1 it is trivial (f/2 + M² >= 0).
2. ✓ T-dense(C) for C < 4(2 − ρ)/r, where ρ is any rigorous doubly-positive constant.
   - Proof: P58's bound d <= (r/2)a(1 − a)/(1 − ρa), with a <= ½. The function is increasing on [0, ½], since its
     derivative has numerator 1 − 2a + ρa² >= 0.
   - Without ρ at all: a >= 2d/r (density window) and a <= ½ give T-dense(C) for C < 4/r = 5.196.
3. ✓ ρ* <= (2 + √2)/4 = 0.85355 (NEW, two lines). With s = 1/√2, w(t)² <= s·w(t) + (1 − s)·w(2t) pointwise:
   - for x = w(t) <= s use x² <= sx;
   - for x >= s use y = w(2t) >= 2x² − 1 >= 0, and (2s − 1)(x − s)(x − 1) <= 0.
   Integrate, using ∫w(2t)dt = ½∫w.
4. ρ* <= 203819/250000 = 0.815276 (computer-assisted; agent's exact Bernstein + Sturm certificates; lead's independent
   float grid (2·10⁵ points) and exact-rational grid (2001 points) re-check, E79: min exactly 0 at x = 0, β' > 0).
   - Separable potential: ρx − x² + β(y_min(x)) − β(x)/2 >= 0 on [0,1], with β increasing, β(0) = 0, β of degree 8,
     and y_min = max(0, 2x² − 1, x − √(1 − x)).
   - The last branch is the 4-point Toeplitz antisymmetric block [1 − z, x − y; x − y, 1 − x] ⪰ 0 (lead re-derived it).
   - Integrating, the β terms cancel (∫β(w(2t)) = ½∫β(w)).
   - P58 alone with this ρ gives T-dense(5.311).
5. ✓ STRONGEST (paper, ineffective): T-dense(C) for every C < 4(2 − ρ)/r = 6.156001…
   - Rational check: 4(2 − ρ) − (1539/250)r = 261/250000000 > 0, with r = 0.769801 > 4/(3√3).
   - With the elementary r = 0.811 the same proof gives C < 5.843.
6. ✓ EXPLICIT c(3) = 10^{−6000005} (paper; compactness-free; inputs: elementary P31-E plus Gaussian/Poisson lemmas).
   - Setup: Gaussian smoothings k_s at scales s_j = βX·K^j (K = J = 10⁶, β = 10^{−6000003}).
   - Pigeonhole on the identity values Q_s(0) of the PD sequences Q_s = k_s∗a + 2M·k_s (transform 2L_s(f + M) >= 0)
     gives a scale with sup_m |q_s − q_{Ks}| <= 2/J + 42c.
   - Approximate binary energy: |k_s∗(a − q)² − q(1 − q)| <= 4ω, with ω = 1.8·10⁻⁵.
   - The finite product window applied to (1 − L_s)f gives q(m)(1 − q(m)) <= q(0)(1 − q(0)) + 8ω + 2β (EM).
   - P31-E at one window (w + 1 = ⌊4s⌋) gives q(0) > 0.53 when X <= 3n.
   - A discrete crossing of ½ (steps of order 10⁻⁵) contradicts (EM).
   - Lead's note: the stated step bound "< 7·10⁻⁶" should read "<= 2(2/J + 42c) + 3/S <= 7.1·10⁻⁶ or so". This is
     immaterial: the margin is 9·10⁻⁴ against 1.5·10⁻⁴.
   - This is the first EFFECTIVE (explicit-constant) dense theorem beyond P31's C = 2.44. It is a natural Lean target:
     finite sums, trigonometric-polynomial positivity, P31-E (already kernel-checked), Gaussian/Poisson facts
     (mathlib has the Jacobi-theta functional equation).
7. Two-scale bookkeeping (PROVED, exact).
   - A height-tagged measure records the tall residual energy (P40 on g).
   - Cell decomposition: c_k = (2/X)Σ_s h_s e^{−ikx_s}w_s(k/X), with Hermitian-PD cell profiles w_s.
   - This identifies the HBSC support/tightness issue precisely.
   - Quantitative P32 local window: θ²/(2π)∫sinc(θy/2)⁴Φ² <= r(1 + θ)[Re∫_0^θ(1 − t/θ)v_s]² for isolated packets.
   - Finite L⁶ window with the trivial constant: mesoscopic parts are erased at proportional windows.
8. NUMERICAL.
   - ρ* lower bounds: autocorrelation class 0.7238796 (N = 800); general PWL 0.723864 (B = 160). The general class does
     not beat the autocorrelation class at a common resolution.
   - E79 (lead): the ρ*-extremal shape p = a·q (half-sine autocorrelation) VIOLATES energy-PD (min of the FT of e is
     −0.0094 near y ≈ 7.8, a = ½). So the enlarged class {p PD, e PD, windows} has reach STRICTLY above
     4(2 − ρ*)/r ≈ 6.63. E80 estimates it.
Correction of the lead's NOTEBOOK cont. 10: the "macroscopic barrier ≈ 6.05" was the reach of the two scalar windows
only. Energy-PD is a further MACROSCOPIC constraint (the product window), and it defeats the round-7 witness: at
t = 7/48, e(t) − e(0) ≈ 0.024 > 0.
Status: items 1–3 and 5–6 paper proofs, lead-verified; 4 computer-assisted exact; none kernel-checked.

## P60. Round-9 agent results (report .research/agents/tdense9_report.md; lead re-checked every item marked ✓) — 2026-10-19
1. ✓ CATALAN PARAMETRISATION (NEW, short). Since a <= ½ (P59.1) and p(t) <= p(0), p = (1 − √(1 − 4e))/2 =
   Σ_{k>=1} Catalan(k−1)e^k, a series with nonnegative coefficients converging uniformly on [0, ¼]. Schur products
   preserve PD, so "e PD, 0 <= e <= ¼" already implies p PD.
2. ✓ SCALAR REDUCTION. Put q = e/e(0) (PD, nonnegative, q(0) = 1). The θ → 0 energy window gives ∫_0^1 q <= r/2. Since
   ψ(x) = 1 − √(1 − x) is convex with ψ(0) = 0 and 4e(0) <= 1, p = ψ(4e(0)q)/2 <= 2e(0)ψ(q). Hence d <= rκ/4, where
   κ = sup ∫ψ(q)/∫q over normalized nonnegative PD q (any support).
   - The density windows are REDUNDANT once e is PD with all its windows: p = p² + e, and p² inherits every window
     from p PD by lattice sampling. The agent's scalar class therefore EQUALS the two-profile class.
3. ✓ κ <= 749089/10⁶ (computer-assisted, exact).
   - 18 rational supporting lines q(2t) >= m q(t) + b. Each comes from T_2(z) − mz − b − Σ_{n=3}^{24} λ_n T_n(z) >= 0 on
     [−1, 1] with λ_n >= 0, integrated against q's Bochner measure (uses q(nt) >= 0).
   - Plus the Gram branches q(2t) >= 2q(t)² − 1 and q(2t) >= q(t) − √(1 − q(t)) (P59.4).
   - A monotone degree-24 potential β with κx − ψ(x) + β(L(x)) − β(x)/2 >= 0 on [0,1]; substitute x = 1 − u².
   - 29 leaves cover u ∈ [0,1]. The β terms cancel on integration.
   - Lead's independent re-check (E81, exact-rational Taylor models; a different method from the agent's Bernstein +
     Sturm): all 18 lines, all 29 leaves, β' > 0 on [−10⁻⁵, 1], Bernstein = power form, every branch argument
     >= −10⁻⁵ on its leaf, leaves cover [0,1].
4. ✓ T-dense(C) for every C < 4/(rκ) = 4·10¹²/576649461289 = 6.936623…, with r = 0.769801 > 4/(3√3); r² > 16/27
   checked exactly. INEFFECTIVE constant. With the elementary r = 0.811: C < 6.5842.
5. ✓ (numerical + exact witness) Two-profile reach. Integer spectral factor (160 cells) with d = 0.1376008148…, so
   1/d = 7.2673988… < 7.267398825422. q_i were recomputed from the integers, and d from closed-form cell integrals at
   60 digits (E81). Exact PD from the factor identity; all-θ windows certified by the agent. Gurobi local searches give
   ≈ 7.267; E80 (lead, sampled constraints, unverified) found d = 0.13866 (1/d = 7.212). So the class's reach is
   <= 7.2674, and possibly <= 7.21.
6. ✓ COMPLETELY POSITIVE covariances (NEW).
   - For h = g + m >= 0, the matrices (1/X)∫h(x + y_i/X)h(x + y_j/X) are completely positive.
   - In the limit, [½∫_0^1 e(t)cos((y_i − y_j)t)dt]_{ij} is CP for every finite y. CP is strictly stronger than
     "e PD, e >= 0" (= doubly nonnegative) once k >= 5.
   - Strictness inside the two-profile class: q = Λ(t/ε) + ½[Λ((t − ½)/ε) + Λ((t + ½)/ε)], ε = 1/1000, satisfies
     every window. Its 5-point Horn form at y_i = 4πi/5 is −0.0011803… (Arb; the lead re-derived it by hand as
     ≈ ε(10 − 13.09 + 1.91) and in mpmath).
   - The lead turned this into an exact theorem: P61.
7. EXPLICIT constants on the whole old range C < 4(2 − ρ)/r0 = 6.156. Paper proof; the lead read it but did not
   re-derive every constant.
   - Inputs: P59.6's Gaussian pigeonhole; a ROBUST doubly-positive lemma; mass-to-zero truncation of the Gaussian
     filter; a finite energy window.
   - The robust doubly-positive lemma: Q_cont = continuous Gaussian smoothing + 2M·Gaussian is an exactly PD
     function on R, so the ρ inequality applies without compactness.
   - Parameters: η = min(10⁻³, g/1000), J = ⌈10⁸/η²⌉, K = J³, β = min(η/(4J), 1/(X0 + 1))K^{−J}, c(C) = β/100.
   - Examples: C = 5 gives c = 10^{−9·10¹⁶}; C = 6 gives 10^{−8.2·10¹⁸}. The c(3) = 10^{−6000005} of P59.6 is much
     better at C = 3.
8. Formal two-scale escape and the cubic gap (Task 3). Weighted Fejér packets at J = X^{0.9} random centres have the
   correct first two binary moment profiles and min >= −o(√X), but zero coefficient skew. A binary sequence needs
   Σr_k³ ≈ X∫p(1 − p)(1 − 2p) > 0. The agent's cubic-resonance target is CONJECTURED. The lead generalized the escape
   to every CP generator in P61(c).
9. Formal corrections by the agent (kept): a simultaneous-PWL ansatz for (p, e) cannot be exactly doubly PD; a
   160-cell batch failed by integer-digit overflow (no claim from it).
Status: 1–4 and 6 paper or exact-computer proofs, lead-verified; none kernel-checked.

## P61. The SECOND-ORDER REACH theorem (lead, 2026-10-19; paper proof; awaiting adversarial codex check and Lean)
Definitions.
- φ(x) = (1 − √(1 − x))/2 on [0,1]. It is convex and increasing, φ(0) = 0, φ(1) = ½, and φ(x)/x is increasing.
- 𝒲 = {w : R → C continuous, Hermitian PD, supp w ⊂ [−1,1], w(0) = 1}.
- D := sup_{w∈𝒲} ∫_0^1 φ(|w(t)|²) dt.
- WLOG w = G ⋆ G̃ with G >= 0 on [0,1] and ∫G² = 1. Reason: Boas–Kac/Krein give w = G ⋆ G̃ with G ∈ L²[0,1]; then
  |w| <= |G| ⋆ |G̃|, and φ(x²) is increasing in x.
Theorem.
(a) In the P58 limit of any dense counterexample sequence: ∫_0^1 φ(e(t)/e(0))dt <= D, and d = ∫_0^1 p <= D.
    Consequently T-dense(C) holds for EVERY C < 1/D (ineffective constant).
(b) SHARPNESS. For every w ∈ 𝒲 there are real cosine polynomials E_X of degree X with min E_X >= −o(√X), coefficient
    profile p = φ(|w|²), and coefficient-square profile p (so residual energy e = |w|²/4 = p − p²). Hence no argument
    that uses only positivity (of f + M and of anything built from it by filters, products, shifts or averages) together
    with the first two binary moment profiles can prove T-dense(C) for any C > 1/D.
(c) NUMERICAL (E82): D ≈ 0.1166747 at N = 320 (all five starts agree at every N), so 1/D ≈ 8.5708.
    - N: 20 → 8.5954, 40 → 8.5778, 80 → 8.5727, 160 → 8.5712, 320 → 8.5708.
    - Optimiser G*: a symmetric bump with G*(0)/G*(½) ≈ 0.38; ∫w² = 0.3400.
    - Triangle (G = 1): (1 − π/4)/2 = 0.10730 (1/D <= 9.3196; round 9's formal escape). G = 1 is not stationary: the
      first variation is Ψ(x) + Ψ(1 − x) with Ψ(x) = ½√(2x − x²), which is not constant.
    - Companion constants (E82): N₂ := sup ∫_0^1 w² ≈ 0.34349 (Beckner gives r/2 = 0.38490) and
      κ_w := sup ∫φ(w²)/∫w² ≈ 0.3557 (still creeping up with N). Their product ≈ 0.1222.
(d) RIGOROUS now: D <= rκ/4 with round 9's κ. Proof: q = w² is nonnegative and PD with q(0) = 1;
    ∫_0^1 w² <= r/2 by sharp Young (Beckner) at exponents (4/3, 4/3; 2) on a unit-length support. This recovers
    T-dense(6.9366). Any better rigorous D₁ >= D gives T-dense(C < 1/D₁).
Proof of (a).
1. Set-up (P58, P59). T = H_h f >= −M, with coefficients r_m = a_m − (k_h ⋆ a)_m. Write T = r_0/2 + g with
   g >= −m, 0 <= m <= M. Then h := g + m >= 0, ĥ(0) = m and ĥ(k) = r_k/2 for k ≠ 0, with degree <= X(1 + o(1)). The
   diagonal gives (1/X)Σ r_k²δ_{k/X} → e(s)ds weakly, e = p(1 − p) continuous, and a <= ½, so p = φ(4e).
2. Rescale H_X(v) := h(v/X)/√X, a nonnegative trigonometric polynomial in v with frequencies ω_k = k/X ∈ [−1 − o(1),
   1 + o(1)].
3. Pick ψ >= 0 in L¹(R) with ψ̂ continuous, supported in [−ε, ε], and ∫|ψ̂|² = 1 (e.g. a normalized Fejér kernel).
   Put ρ = |ψ̂|², a probability density on [−ε, ε].
4. Gabor pieces. s_u(v) := H_X(v)ψ(v − u) >= 0 for u ∈ R. Then ŝ_u(t) = Σ_k α_k e^{i(ω_k − t)u}ψ̂(t − ω_k), with
   α_k = ĥ(k)/√X.
   - Each ŝ_u is continuous and Hermitian PD (the transform of a nonnegative L¹ function), with
     supp ŝ_u ⊂ [−(1 + δ), 1 + δ], δ = ε + o(1).
   - EXACT identity (orthogonality of e^{i(k − k')u/X} over a period):
         avg_{u ∈ [0, 2πX)} |ŝ_u(t)|² = (1/X)Σ_k |ĥ(k)|² ρ(t − k/X)
                                     = (1/X)[m²ρ(t) + ¼Σ_{k≠0} r_k² ρ(t − k/X)] → ¼(e ⋆ ρ)(t),
     uniformly in t, using m² <= M² = o(X) and weak convergence against the equicontinuous family ρ(t − ·).
5. Normalize. With λ_u = ŝ_u(0)² and c_u = ŝ_u/ŝ_u(0): each c_u is PD with c_u(0) = 1 and |c_u| <= 1. Put
   μ_u = 16λ_u, Y(t) = avg μ_u|c_u(t)|² (→ 4(e ⋆ ρ)(t)) and M̄ = Y(0).
6. Jensen (φ convex on [0,1], probability weights μ_u/M̄): M̄φ(Y(t)/M̄) <= avg_u μ_uφ(|c_u(t)|²) pointwise.
7. Integrate over t >= 0 (Tonelli). Dilating each c_u by 1 + δ puts it in 𝒲, so the right side is <= M̄(1 + δ)D.
   Hence ∫_0^{1+δ} φ(Y/M̄) <= (1 + δ)D.
8. Let X → ∞ (dominated convergence; Y/M̄ → (e ⋆ ρ)/(e ⋆ ρ)(0)), then ε → 0 (e ⋆ ρ → e uniformly). This gives
   ∫_0^1 φ(e/e(0)) <= D.
9. Finally 4e(0) <= 1 and φ(sx) <= sφ(x) give p = φ(4e) <= φ(e/e(0)), so d <= D. Also e(0) > 0, since otherwise e ≡ 0
   and p ≡ 0.
10. P58 gives d >= 1/C, which contradicts C < 1/D. ∎
- Inputs: P58 steps 1–3 (compactness, diagonal), P59.1 (a <= ½), Bochner, Boas–Kac (only for the WLOG). NOT used: P31
  windows, Beckner, ρ*, κ. Those are implied by (a) and enter only through the rigorous bound in (d).
Proof sketch of (b) (round-9 Task 3, generalized to arbitrary w; take G >= 0 so w is real and nonnegative).
- Smooth part: P_X = Σ_{k>=1} φ(w(k/X)²)cos kx >= −¼, since φ(w²) is PD (Catalan series of Schur powers) and sampling
  a PD function gives a PD sequence.
- Packets: S_X(x) = Σ_k w(k/X)e^{ikx} >= 0 (sampled PD). Put
      g_X = c Σ_{j<=J}[S_X(x − θ_j) + S_X(x + θ_j) − 2],   c = 1/√(32J),   J = ⌊X^{0.9}⌋,   θ_j i.i.d. uniform.
  Then g_X >= −√(J/8) = o(√X), and r_k = 4c·w(k/X)Σ_j cos kθ_j with E r_k = 0 and E r_k² = w(k/X)²/4.
- The law of large numbers on test functions gives the profiles (p, p).
- E_X := P_X + g_X is ≥ −o(√X) and is a genuine positive-plus-constant polynomial. So every positivity consequence
  holds. In particular the windows hold automatically; E82 confirms all P31 windows on the D-optimiser, with
  r = 4/(3√3).
Meaning.
- The second-order (macroscopic + mesoscopic, positivity + two binary moments) theory of T-dense is now EXACTLY
  solved: its reach is 1/D ≈ 8.571.
- The rounds 7–9 classes were relaxations of 𝒲:
  - two windows: 6.05;
  - plus energy-PD (two-profile class): ≈ 7.21–7.27.
  - Their missing ingredient was complete positivity, whose exact form is the Gabor mixture representation
    e ⋆ ρ = avg |ŝ_u|².
- Beyond 1/D: only THIRD-or-higher binary information can help (the escapes have zero coefficient skew).
- NOVELTY: grep of PROOFS for Gabor/STFT/completely positive/copositive found only P60.6 (round 9's CP observation,
  which seeded this). External priority unchecked.
Status: paper proof (lead). Needs: (i) an adversarial codex check of every step (round 10, Task 1); (ii) a rigorous
D₁ < rκ/4 (round 10, Task 2); (iii) Lean, later.

## P62. Round-10 agent results (report .research/agents/tdense10_report.md; lead re-checked every item marked ✓) — 2026-10-19
1. ✓ P61 AUDIT. P61(a) has no gap (normalizations, uniform limits, continuous Jensen with weights λ_u, dilation,
   ε → 0).
   - P61(b) REPAIRED for complex Hermitian w by the reflected-translate formula
         g_X = c Σ_j [S_X(x − θ_j) + S_X(−x − θ_j) − 2],
     with cosine coefficients r_k = 4c Σ_j Re(w(k/X)e^{−ikθ_j}) and the same moments.
   - P58's actual smoothing diagonal (h = X^{2/5}) is verified for the escape.
   - The Boas–Kac WLOG is valid as an equality of the two suprema (Ehm–Gneiting–Richards Thm 2.1(a)).
   - Scope (agreed): sharpness concerns physical-space positivity. The escape's coefficients are not nonnegative or
     bounded by 1, which is additional binary information.
2. ✓ D <= 1333/10000, hence T-dense(C) for EVERY C < 10000/1333 = 7.501875… (including C = 7.5). INEFFECTIVE constant;
   computer-assisted.
   - Certificate (support-coupled, t-dependent): for w = G ⋆ G̃, G >= 0, the pointwise inequality is
         φ(x²) <= a(t)x + B(2t, y) − B(t, x)/2,   x = w(t), y = w(2t),
     where:
     - a and B are piecewise constant in t on 64 cells (B(t, ·) = β_j, monotone, degree 10, β_j(0) = 0; B = 0 for
       t >= 1);
     - x <= cos(π/(k + 2)) with k = ⌈1/t_lo⌉ − 1 (Egerváry–Szász on the sampled sequence w(nt));
     - y >= max(0, 2x² − 1, x − √(1 − x)).
   - Integration cancels the potentials (∫B(2t, w(2t)) = ½∫B(s, w(s)), and B = 0 beyond 1), so
     ∫_0^1 φ(w²) <= ∫_0^1 a w = ½⟨G, T_a G⟩.
   - Schur test with U = 1 + (4/5)x(1 − x): T_a U <= (1333/5000)U on [0, 1], exactly.
   - Lead's independent check (E84): Arb ball arithmetic directly in x, the max over all valid branches, mean-value
     enclosures and adaptive bisection, versus the agent's u-substitution, squared form and Bernstein. Results: 2475
     leaves, 0 failures; all 64 Schur cells pass, with cubics re-derived by my own exact integration; β_j monotone with
     β_j(0) = 0; a_j >= 0; power form agrees. The agent's own independent QQ/FLINT check also passed (527 leaves, 127 CF
     caps, 64 Schur cells).
3. ✓ THIRD-ORDER SHARPNESS (NEW, paper; lead re-derived).
   - Sparse gadget: for any continuous s on [0, 1], put L = ⌊X^{4/5}⌋ and z_k = L^{1/3}s(k/X)^{1/3} on multiples of
     L (zero elsewhere). Its first and second coefficient profiles tend to 0, its third tends to s, and
     |Σz_k cos kx| <= X^{7/15} = o(√X).
   - Adding it to the P61(b) escape with s = e(1 − 2p) matches the first THREE binary raw-moment profiles
     (a, a², a³ → p).
   - So "positivity + three moment profiles" has the same reach 1/D. Round 9's cubic target (Σr³ <= BM² + o(X)) is
     dead for weighted coefficients.
   - The gadget's fourth moment diverges like L^{1/3}.
   - Four matching raw profiles force normalized coefficient L² proximity to {0,1}: a²(a − 1)² = a⁴ − 2a³ + a² → 0.
     Three suffice if the coefficients are nonnegative.
4. Rounding evidence: threshold rounding of the X = 2²⁰ examples gives R > 2.079 and R > 2.081 (Arb point
   certificates). Failed, as predicted (NOTEBOOK cont. 13.5).
Status: 1 and 3 paper proofs (lead-checked); 2 computer-assisted exact with two independent verifications; none
kernel-checked.

## P63. Round-11 agent results (report .research/agents/tdense11_report.md; lead re-checked every item marked ✓) — 2026-10-19
1. ✓ D <= 259/2000, hence T-dense(C) for EVERY C < 2000/259 = 7.722007… INEFFECTIVE constant; computer-assisted.
   - NEW ingredient: support-specific symbol lines.
     - Lemma. Let k >= 2, nodes z_l ∈ [−1, 1], weights α_l >= 0, A_n = 2Σ_l α_l T_n(z_l), c = Σ_l α_l and
       R = Σ_{n=3}^k max(A_n, 0). If A_2 > 0, every normalized nonnegative PD w with w(nt) = 0 for n > k satisfies
       w(2t) >= (−A_1 w(t) − c − R)/A_2.
     - Proof. The sampled sequence (w(nt))_n is PD and supported in |n| <= k, so its symbol 1 + 2Σ_{n<=k} w(nt)cos nθ
       is >= 0. Evaluate at θ_l = arccos z_l, weight by α_l, and use 0 <= w(nt) <= 1 for n >= 3.
     - Valid on every t-cell with t_lo >= 1/(k + 1), i.e. for k >= k_jj = ⌈1/t_lo⌉ − 1. Example: k = 2 or 3 gives
       w(2t) >= w(t) − ½.
   - Certificate: the pointwise inequality φ(x²) <= a(t)x + B(2t, y) − B(t, x)/2 on 384 half-cells.
     - 192 cells for a and B; B has degree 12, is monotone, with B(t, 0) = 0, and B = 0 for t >= 1.
     - Branches for y = w(2t): 0, Gram, P59.4, the 18 round-9 long lines, and the support lines.
     - Schur test with U = 1 + (4/5)x(1 − x): T_a U <= (259/1000)U.
     - Minimum Schur margin 104315471167/26542080000000000.
   - Discovery values (Gurobi, not certificates):
     - K = 192, degree 12: 0.1292047;
     - long lines alone: 0.1328880;
     - an extra third-dilation potential: 0.1323699 at K = 48.
   - Verifications.
     - Agent: SymPy/FLINT reconstruction (1865 leaves, 383 CF caps, 188 support lines, 18 long lines by Sturm,
       192 Schur cells).
     - Lead (E85, a different method): Arb directly in x. I RE-DERIVED all 188 support lines from their stored LP nodes
       and weights. None is bad, and every stored line is implied by my derivation. I used my own per-half-cell branch
       set, allowing support lines only with k >= k_jj. Results: 22615 leaves, 0 failures; all 192 Schur cells pass.
2. ✓ DC-BARRIER THEOREM (precise form of NOTEBOOK cont. 14).
   - Statement. For every Hermitian PD τ on Z, h = m + Σ_{k=1}^X r_k cos kx and j >= 2:
         Re Σ_k τ(k)ĥ(k)^j >= τ(0)(m^j − 2^{1−j}Σ|r_k|^j).
     Proof: |τ(k)| <= τ(0), plus the triangle inequality.
   - Corollary. Give P62's three-profile escapes a DC offset m with X^{1/3} << m << √X. Then they satisfy EVERY anchored
     convolution test of every fixed order j >= 3 (and h^{*j} >= 0 pointwise).
   - Correction to cont. 14: physical positivity of a test needs τ PD, not τ >= 0. Example: τ = (1, −½) gives 1 − cos x.
   - The meta-claim "every higher-order argument is blind" remains HEURISTIC.
3. ✓ REPAIR-ENERGY LEMMA (new to the record).
   - Statement: |avg(u³ − v³)| <= √E(√F_u + (F_uF_v)^{1/4} + √F_v), where E = avg(u − v)² and F = avg(·)⁴.
   - Consequence. Any weighted escape u with the four binary raw profiles is order-X L²-far from every base escape v
     with bounded fourth moments and the Gaussian profiles (cube p³ + 3pe, fourth F = ∫(p⁴ + 6p²e + 3e²)):
         liminf X⁻¹Σ(u − v)² >= S²/(√d + (dF)^{1/4} + √F)²,   S = ∫e(1 − 2p) > 0.
     Triangle generator: d = (1 − π/4)/2, S = π/64, F = 67/120 − 5π/32, and the bound is > 3/1000 (Arb).
   - Also |avg z³|² <= avg z² · avg z⁴. This explains why every sparse cubic gadget (P62.3) has a divergent fourth
     moment.
   - Base escapes are realizable deterministically, using Q-independent angles such as 2π√prime_i.
   - Correction: four raw profiles IMPLY normalized L² proximity to {0, 1}. The converse needs uniform integrability
     of fourth powers.
4. ✓ TORSION BUDGET (extends cont. 14).
   - Apply p_q(0) <= ½ (P59.1 for the counterexample A_q) with q = lcm(1, …, L), then let L grow:
         Σ_{θ ∈ 2πQ/2πZ, θ ≠ 0} W_θ(0) <= ½ − a.
   - Hence the rational macroscopic part satisfies |R(t)| <= ½ − a, and at a = ½ every rational atom vanishes.
   - Also ∫p_q <= 4a_q(1 − a_q)D. This constrains rational atoms only; it leaves atom-free P61 escapes untouched.
   - Classification (classical assembly): a positive linear coefficient mask that maps every binary array to a binary
     array is restriction to a subgroup qZ. So subgroup restrictions are the only binary-derived objects of that kind.
5. ✓ KURTOSIS AND THE PALEY BOUNDARY.
   - Full-Haar inequality: kurtosis >= 3 − (3/2)Σa⁴/(Σa²)², hence >= 3/2. It holds for positive-amplitude finite cosine
     sums on a compact abelian group, with distinct characters and no order-2 character. Zero-sum quadruples are
     nonnegative; keep the three pairings.
   - The DC-subtracted version is FALSE. With S_q(k) = Σ_{a ∈ QR} cos(2πak/q) = (−1 + √q χ(k))/2 (k ≠ 0,
     q ≡ 1 mod 4), the kurtosis off the DC class is exactly 1.
   - Positive Paley escape: r_k = w(k/X)S_q(k)/√(2q), q -> ∞, q = o(X).
     - min >= −(q − 1)/(4√(2q)) − ¼ = o(√X), with profiles (p, p).
     - (1/(Xq))Σr⁴ -> (1/64)∫w⁴, so the fourth moment diverges.
     - Nearest-rounding energy >= (X/8)∫w².
     - Half the variance sits on the exceptional class qZ.
   - Deleting the class (r' = wχ/2): f(2πa/q) = −(X/(2√q))∫w + O(q) at nonresidues a, so M/√X -> ∞ for
     q = o(X^{2/3}).
   - Arb at X = 65536, q = 257: the positive family's minimum lies in [−3.07292, −3.07242]; the deleted family has a
     value of −977.208.
6. ✓ LITERATURE (Task 3, quoted).
   - Sanders arXiv:0807.5104v2, Thm 1.2: polynomial bound for symmetric half-sets of Z_p, with exponent 1/3; Thm 1.3:
     distance to a subgroup.
   - Nontrivial strongly regular circulants are the prime Paley graphs (Liu–Zhou, EJC 29(2) P2.9, Thm 259; Bridges–Mena,
     Hughes–van Lint–Wilson, Ma 1984).
   - The unqualified cyclic √-statement is false (complete graph).
   - Embedding: for a prime p > 2X, a cyclic √-bound at density δ implies T-dense(1/δ). The converse does not hold.
7. NUMERICAL (VM, examples/r11_certificates/fourth_probe.*):
   - random packets and positive/deleted Paley at X = 4096 and 65536 (table in the report);
   - nearest roundings fail, with R > 1.7995 and R > 1.9944 (Arb point certificates, re-evaluated at 220 bits).
Status:
- Item 1: computer-assisted, with two independent verifications.
- Items 2–5: paper proofs, lead-checked.
- None kernel-checked.
- The four-moment alternative (A)/(B) is UNRESOLVED. The missing statement is either a positive-packet configuration
  with bounded fourth moment and the non-symmetric local Bernoulli law, or a binary-specific second-order inequality
  excluding all of them.

## P64. Round-12 agent results (report .research/agents/tdense12_report.md; lead re-checked every item marked ✓) — 2026-10-19
No new unconditional T-dense endpoint: it stays C < 2000/259 (P63). Round 12 gives the coupled reduction, the nested
exclusion theorem, cyclic homogenization, and a precise barrier for scalar cyclic arguments.
1. ✓ R12-N, NESTED PERIODIC SCHEDULES (paper proof; lead re-derived; E89: 538 cases, 0 violations).
   - Statement. Let N >= 1, A finite with n = |A|, r = #{a mod N}, l0 = |A ∩ NZ|. If A ∩ NZ = {N, 2N, …, l0·N}
     (possibly empty), then M(A) >= n/((3π + 2)r). With symmetric residue counts (l_c = l_{−c}), M >= 2n/((3π + 2)r).
   - Proof.
     - Let v_s = f_A(2πs/N). Then Σ_s v_s = N·l0 and Σ_s v_s² = NΣ_c((l_c + l_{−c})/2)² >= N n²/(2r).
     - From (v_s + M)(n − v_s) >= 0: n²/(2r) <= n(l0 + M).
     - Averaging over the N shifts restricts f_A to A ∩ NZ. The progression at t = 3π/(2l0 + 1) has value
       −(1 + csc(3π/(4l0 + 2)))/2 <= −2l0/(3π), so M >= 2l0/(3π). Combine the two bounds.
   - Corollary (nested model A = {k <= H : k <= U_{k mod N}}): M >= dX/((3π + 2)p0·N). So dense nested schedules
     with N = o(√X) have M/√X -> ∞. The bound survives o(X/N) Hamming perturbations.
   - General form (lead): M(A) >= max(n/(2r_N) − l0(N), M((A ∩ NZ)/N)) for every N. This is useless when residues are
     equidistributed, which P63.4 forces for dense counterexamples at every fixed N.
2. ✓ EXACT FRONT AND CYCLIC IDENTITIES.
   - Front: S_Y(x) = Σ_{k<Y}(1 − k/Y)(2·1_A(k) − 1)cos kx = 2(F_Y ⋆ f_A)(x) − (F_Y(x) − 1)/2 (normalized
     convolution). So S_Y >= −2M − (π² − 1)/2 on Y^{−1/2} <= |x| <= π.
   - Cyclic: for even s: Z_q -> {±1} with H_γ = Σ_c s_c e(−γc/q),
         S_Y(x) = (1/(2q))Σ_γ H_γ F_Y(x + 2πγ/q) − s_0/2.
   - Root filter: Σ_γ F_Y(x + 2πγ/q) = q for 1 <= Y <= q; it equals qF_L(qx) for Y = Lq.
   - CORRECTION to NOTEBOOK cont. 16 (6b): H_γ = 2λ_γ (γ ≠ 0) and H_0 = 2|S| − q. The partial-period bound is
     S_Y >= −max(2K, 1)/2 − ½, not −K/2 − ½.
3. ✓ R12-H, CYCLIC HOMOGENIZATION (lead re-derived every step).
   - Statement. Let q_j -> ∞ be odd primes and B_j = −B_j ⊂ Z_{q_j} with |B_j|/q_j -> ½ and K_j = o(√q_j). Then every
     dilate is balanced on every cyclic interval: sup_I |Σ_{k∈I}(1_{B_j}(bk) − ½)|/q_j -> 0 for each fixed b ≠ 0.
     Also every fixed rational twist with continuous weight is o(q_j).
   - Proof.
     - Weak limits p of the coefficient measures have Fourier coefficients >= 0, so p is continuous and PD.
     - Energy-PD: r = b − smooth_h(b) has r̂ = (1 − L)λ >= −K, so r + Kδ_0 is PD. Its Schur square gives
       (r²)^ >= −K² − 2K. Strong smoothing gives r² -> p(1 − p) weakly, and K² = o(q) makes e = p(1 − p) PD.
     - At half density, p(0) = max p and e(0) = max e force p ≡ ½.
   - COROLLARY (lead): K = o(√q) ⇒ max_{γ≠0}|λ(γ)| = o(q), i.e. Fourier uniformity. Dilate by γ_j:
     λ_{γ_j B}(1) = λ_B(γ_j), and apply R12-H to the dilates.
   - Fourier form of the last step (lead): at p̂(0) = ½, ê(γ) = −Σ_{j≠0,γ} p̂(j)p̂(γ − j) <= 0 for γ ≠ 0. So
     energy-PD forces p̂(j)² = 0 (take γ = 2j).
   - Novelty: new to the project record. External priority unchecked. Compare Jin–Milojević–Tomon–Zhang (item 10):
     they get proximity to a subgroup for K <= q^γ with γ < 1/4; R12-H gets uniformity, a weaker conclusion, for all
     K = o(√q).
4. ✓ CYCLIC BARRIER, EXACT QUANTIFIERS. Asymptotic TBS (balanced sign sequences without rational atoms have
   front dips >= c√Y) ⇒ some c' > 0 with −min_{γ≠0} λ_B(γ) >= c'√q for every symmetric half-set B of Z_q (q >= 5).
   - Proof: take Y_j = q_j; R12-H supplies both TBS hypotheses, and item 2 gives S >= −max(2K, 1)/2 − ½.
   - Integer side: with p(0) = ½, a slow diagonal Y_j = ε_j X_j shows TBS excludes the exact endpoint a = ½.
   - A UNIFORM a* < ½ needs a stability statement, because p(0) is not weakly continuous (narrowing PD bumps).
5. CSFG(20) (CONJECTURED) and ✓ R12-B (conditional theorem).
   - CSFG(20). There is η ∈ (0, ½) such that, for symmetric B_j ⊂ {|c| <= q_j/4} ⊂ Z_{q_j} with |B_j|/q_j >= 1/80
     and K_j = o(√q_j), every weak profile has P(0) <= ½ − η.
   - R12-B. CSFG(20) ⇒ T-dense(C) for every C < min(20, 1/D_σ), where σ = 1 − 4η² and
     D_σ = sup ∫φ(σw²) <= σD < D.
   - Proof: embed B = A ∪ (−A) into Z_q with a prime q ∈ (4X, 8X]. Then λ_B(γ) = 2f_A(2πγ/q) >= −2M and
     P(t) = p(u|t|). Run P61 with x ↦ φ(σx), using 4a(1 − a) <= σ.
   - CSFG is a cyclic statement about an integer-shaped object; it implies the integer FRONT gap. Its value is that
     it isolates exactly what is needed.
6. ✓ FINITE EXACT TD-COUPLE IS VACUOUS. On a fixed finite group, continuous binary tapers are constant. A usable
   finite-envelope lemma needs an explicit approximation norm and rate.
7. ✓ ROUGHNESS IDENTITIES.
   - General (no nestedness): Σ_{s≠0}|Z_s(ξ)|² = ∬(|E_t ∩ E_v|/N)e^{iξ(t−v)} − |∫p e^{iξt}|².
   - Real part: Σ_s(Re Z_s)² = (1/(2N))Σ_c(|B_c|² + Re B_cB_{−c}).
   - Nested case: ξ²·(complex energy) -> 2p0 − p0², not 2p0 (the brief's version was wrong). Symmetric real energy
     -> p0/2.
   - The L²-vector increment identity Σ_s|e_s(t) − e_s(v)|² = |p(t) − p(v)| holds. Individual envelopes are NOT
     Hölder-½ (they are staircases).
   - Positive energy does not give negative spikes. Counterexample: a subgroup pattern at ξ = 0.
8. ✓ R12-U, NONNESTED COUNTEREXAMPLE TO X/N.
   - Random full/empty cells of length L ≍ √X with probabilities following (1 − t)/2. The cells are locally
     2-periodic and not nested.
   - Hoeffding on an O(X³) grid gives M = O(X^{3/4}√log X) = o(X).
   - So M >= c·X/N and M >= c·X√(p0/N) are false for general nonnested schedules. A bound on the number of time changes
     is indispensable.
9. ✓ PK(η) AND THE SCALAR BARRIER R12-S (cyclic half-set exponent).
   - PK(η) (CONJECTURED): max h <= Cλ^{2−η} for h = ĝ + λ, where λ is the actual negative threshold. Then
     λ >= (p/C)^{1/(3−η)}, because p² <= Σh² <= max h·Σh <= max h·pλ.
   - R12-S. At λ = p^{1/3}, a symmetric nonnegative h with h(0) = λ − 1 matches EXACTLY:
     - mass and energy;
     - the off-zero bound h(γ)² <= pλ(λ − 2);
     - max h <= λ³/2.
     Its values are H ± √v on m = 4⌈T'²/(4E')⌉ points.
   - Lead check: m >= T'²/E' gives v >= 0, and m < T'²/E' + 4 <= 2T'²/E' gives v <= H².
   - So no argument that keeps only these scalar deductions beats exponent 1/3. The FULL off-zero convolution
     (equivalently, binarity) is required.
10. LITERATURE (quoted, versions checked by the agent).
    - Sanders 0807.5104v2 Thm 1.2: exponent 1/3 for half-sets.
    - Jin–Milojević–Tomon–Zhang 2509.03490v2 Thm A.1: K <= |G|^γ with γ < 1/4 ⇒ δ|G|-close to a subgroup, in any
      finite group; polynomial proximity for γ < 1/6.
    - Bu et al. 2610.17160v1 Prop. 9.7: M >= ((n − 1)/(64·C·200000))^{1/4} for A ⊂ [1, Cn]. Our T-dense gives exponent
      ½ for C < 7.72.
    - Bedert v3 (1/5 − o(1)); Shankar v1 (log-free 1/5).
    - No 2024–2026 improvement of the half-set exponent beyond 1/3 was found (bounded search).
11. NUMERICAL (VM; archived in examples/r12_certificates/).
    - Structured removal schedules: coset, multiplicative, Bohr and random removals at N <= 257.
    - Gurobi schedule MILPs: N = 29 optimal; N = 61 incumbent 0.0334.
    - Every tested schedule keeps a square-root-sized dip. Arb point certificates: −5474 (N = 29), −8351 (61),
      −10139 (64), −32574 (257).
    - Nonnested probe: M/H = 0.073, 0.036, 0.034 at H = 2^16, 2^18, 2^20.
12. Lead additions (finite cyclic spectral bounds; for symmetric B ⊂ Z_q with |B| = (q − 1)/2, 0 ∉ B,
    Λ = max_{γ≠0} λ, K = −min_{γ≠0} λ).
    - Exact off-zero identity: Σ_{β≠0,γ} λ(β)λ(γ − β) = λ(γ) for γ ≠ 0. This is b² = b, i.e. λ⋆λ = qλ, with the
      β ∈ {0, γ} terms removed.
    - Parseval: Σλ⁺ <= (K − ½)(q − 1), so Λ >= ((q + 1)/4 − K²)/(K − ½).
    - Second order: dilate so Λ = λ(1), and read the identity at γ = 2. Mixed-sign pairs are >= −2KΣλ⁺, so
      Λ² <= Λ + 2K(K − ½)(q − 1), hence Λ <= √(2q)K + 1. Combined with Parseval this gives K >~ 0.42q^{1/4} (the
      elementary exponent).
    - PK(1), i.e. Λ <= CK, would give √q. Paley has Λ ≈ K ≈ √q/2.
Status:
- Items 1–4, 6–9, 12: paper proofs, lead-checked. Item 5: R12-B is proved and CSFG is CONJECTURED. None
  kernel-checked.
- Missing statement, in its sharpest form:
  - integer side: a uniform front gap (CSFG);
  - cyclic side: PK(η) for some η > 0, which beats Sanders.
  Both need the full convolution identity, not scalar moments.

## P65. Round-13 agent results (report .research/agents/tdense13_report.md; lead re-checked every item marked ✓) — 2026-10-19
Cyclic peak problem. Round 13 gives no exponent gain, but three precise barriers, plus the refutation of PK.
Notation as in P64.12.
1. ✓ R13-PK: universal PK is FALSE, for genuine half-sets.
   - Construction. Fix ε ∈ (0, ½). Include each pair ±a independently with probability ½ + ε·cos(2πa/q). Then
     E λ(±1) = εq/2 − ½ − ε and E λ(γ) = −½ − ε otherwise.
   - Hoeffding plus a union bound plus O(√(q log q)) repair flips give exact half-sets with Λ ~ εq/2 and
     K = O(√(q log q)) for all large q ≡ 1 mod 4.
   - Lead re-derived the expectations.
   - Consistent with QU: the second-order bound forces K >= (ε/(2√2) + o(1))√q here.
   - Corrected intermediate:
         QU(β): K <= δ√q with δ <= δ0  ⇒  Λ <= Cqδ^β,
     which gives exponent ½ − 1/(2(β + 1)). β = 1 is the elementary ¼, β = 2 is Sanders' 1/3, β > 2 is new.
2. ✓ R13-C, PARTIAL-CONVOLUTION BARRIER.
   - For any J(q) = o(q^{1/3}) there is a real even array with:
     - exact trace and Parseval;
     - K = q^{1/3}/2 and Λ = λ(1) = 2q^{2/3} − q^{1/3}/2;
     - the exact off-zero identity Σ_{β≠0,γ} λ(β)λ(γ − β) = λ(γ) at every γ ∈ ±{1, …, J}.
   - Construction (h = 2λ + u, u = q^{1/3}):
     - h(0) = u − 1, h(±1) = 4u²;
     - for each displacement d <= J, ℓ = ⌈u⌉ reflected two-site clusters of amplitude √((C − R_d)/(2ℓ)), with
       C = qu(u − 2), spaced more than J apart;
     - mass/energy repair on spread sites.
   - Lead checked z⋆z(γ) = h⋆h(γ) − qu(u − 2), so the identity holds exactly where h⋆h = C.
   - The omitted equation at 2J + 2 has defect ≈ 0.97q² (Arb). So the missing information sits at unprescribed
     frequencies.
   - Kills: any argument using the identity along a prescribed initial segment of the peak orbit.
3. ✓ R13-M1 / M2, ARITHMETIC MOMENT BARRIER.
   - M1: the literal R12-S fake fails cubic integrality, since qT_3 − ((q − 1)/2)³ would be irrational, with
     coefficient 3a(m − a)(m − 2a)/m² on u².
   - M2: for every FIXED r there are arrays with K = q^{1/3}/2, Λ ≍ q^{2/3} and all of the following:
     - all shifted-moment and Hankel positivity;
     - integral T_k for k <= r, in the right ranges;
     - Newton integrality modulo r!.
     The proof adjusts r distinguished peaks by an inverse-function argument (Vandermonde Jacobian).
   - Kills every fixed-order scalar, integrality or congruence route. Growing-order or full-Galois arithmetic stays
     OPEN.
4. ✓ (re-derived) The cubic positive-convolution truncation gives Λ <= O(K³) when K = o(√q), hence only q^{1/4}.
   The kurtosis/spike route also gives only q^{1/4}; the lead's NOTEBOOK cont. 17.7(c) reached the same conclusion
   independently.
5. NUMERICAL, with certificates (examples/r13_certificates/).
   - Exact trade-off staircases Λ_max(κ) at q = 17 and 37, by interval-enclosed exhaustive enumeration (70 and 48620
     sets).
   - Gurobi scans at q = 61 … 109: a finite staircase (q = 61: +2.5% in κ doubles the attainable peak). Small q
     cannot probe δ -> 0.
   - Binary-escape probe (Track C): 20 constructions up to X = 2^20 following the E82 extremal profile with front ½.
     - Laws: Paley textures at q ≈ X^{½, ⅔, 1}, dilated near-intervals, spectral error diffusion, Gurobi rounding.
     - All have R > 0.6 and R increasing, each with a 220-bit Arb dip.
     - Mechanism: q = o(X) repeats the cyclic negative spectrum about X/q times; fixed block clocks create rational
       spikes with negative sidelobes. Best large-X family: Paley at θ = 1, R ≈ 2.9 at X = 2^20.
   - E41's printed q = 89 value is wrong; the pair list gives 4.630072322.
Status: paper proofs (agent), lead spot-checked items 1–3. None kernel-checked. The cyclic exponent stays at Sanders'
1/3. Directions left by round 13:
- full-frequency incidence (adaptive, not prescribed frequencies);
- growing-degree or full Galois arithmetic;
- block-free coordinated q ≈ X binary tapers.

## P66. CUBIC FRONT CAP: dense Chowla with exponent 1/3 for every C < 9(1 + √3)/2 = 12.294 (lead, 2026-10-19; paper proof)
Theorem. For every C < 9(1 + √3)/2 = 12.2942… there is c(C) > 0 with M(A) >= c(C)|A|^{1/3} for every finite
A ⊂ Z_{>0} with max A <= C|A|. The constant is INEFFECTIVE. The proof is fully analytic: no computer assistance.
Numerically the method reaches C ≈ 15.6 (E93b).
Position.
- Bu et al. 2610.17160v1 Prop. 9.7 gives exponent ¼ for every C.
- T-dense (P63) gives exponent ½ for C < 7.722.
- So the range 7.722 <= C < 12.294 newly gets exponent 1/3 > ¼.
Proof.
1. Contradiction sequence: X_j <= Cn_j, M_j = o(X_j^{1/3}). P58 steps 1–3: p is continuous and PD with
   a = p(0) = max p <= ½ (P59.1), p(±1) = 0, d = ∫_0^1 p >= 1/C.
   - High-pass: T = (1 − κ_h)f_A >= −M, where κ_h ∈ [0, 1] is the normalized Fejér multiplier. Then h = T − r_0/2 + m
     is >= 0 with ĥ(0) = m <= M, ĥ(k) = r_k/2 for k ≠ 0, r = a − k_h⋆a.
2. Cubic Schur. ĥ is a PD sequence (h >= 0), so ĥ³ is PD: m³ + 2Σ_{k>=1}(r_k/2)³cos kx >= 0, i.e.
       Σ_{k>=1} r_k³ cos kx >= −4m³   for every x.
3. Cubic profile. For binary a (a² = a³ = a):
       r³ = a − 3aq + 3aq² − q³ = r(1 − 3q + 3q²) + g(q),   g(u) = u(1 − u)(1 − 2u).
   The scaled q -> p strongly (P58.3), so (1/X)Σ_k r_k³δ_{k/X} -> g(p(t))dt.
4. Put x = y/X in step 2 and divide by X. Since 4m³/X -> 0, ∫_0^1 g(p(t))cos(ty)dt >= 0 for all y.
   - So the even extension of g∘p (continuous, bounded, >= 0) is PD, and g(p(t)) <= g(a) for all t.
5. On [0, ½], g has its unique maximum at u* = (3 − √3)/6 = 0.21132…, where g(u*) = √3/18.
   - If a > u*, the intermediate value theorem (p continuous, p(0) = a, p(1) = 0) gives t with p(t) = u*. Then
     g(p(t)) > g(a), contradicting step 4.
   - Hence a <= u*, and e(0) = a(1 − a) <= 1/6.
6. P61 with x ↦ φ(σx), as in R12-B (P64.5): p = φ(4e) <= φ(σ·e/e(0)) with σ = 4e(0) <= 2/3. Jensen over the Gabor
   mixture gives d <= D_{2/3} := sup_{w∈𝒲} ∫_0^1 φ((2/3)|w|²).
   - Convexity and φ(0) = 0 give φ(σx) <= φ(σ)·x on [0, 1], and φ(2/3) = (1 − 1/√3)/2 = u*. Beckner's sharp Young
     inequality (P61(d)) gives ∫_0^1 |w|² <= 2/(3√3).
   - So d <= u*·2/(3√3) = (√3 − 1)/9 = 0.081339…, contradicting d >= 1/C for C < 9/(√3 − 1) = 9(1 + √3)/2. ∎
   - The weaker route D_{2/3} <= (2/3)D <= (2/3)(259/2000) gives only C < 3000/259 = 11.583.
Remarks.
- Why it was missed. NOTEBOOK cont. 13.3 used only the anchored total (x = 0), Σĥ(k)³ >= −m³, which binarity does not
  contradict. The PROFILE version (all x) costs m³/X: it is invisible at exponent ½ (consistent with the DC barrier,
  P63.2) but available at exponent 1/3.
- The exact identity r³ = r(1 − 3q + 3q²) + g(q) shows the cubic information is "g(p) is PD up to a residual
  fluctuation". The fluctuation is o(X), so m³ ~ X is the true limit: the method stops at exponent 1/3.
- The cubic constraint binds beyond the cap: at the D_{2/3} optimiser, FT[g(p)] dips to −0.0022 (E93). So the
  numerical reach exceeds 15.11; E93b gives the constrained value.
- Higher orders. M = o(X^{1/j}) makes the j-th central Bernoulli moment profile PD. j = 4 gives e(1 − 3e), whose
  maximum is again at e = 1/6. NOTEBOOK cont. 13.2's square hierarchy at exponent ¼ gives a <= 0.146. Both are
  dominated by Bu's ¼ for all C.
- ADDENDUM (lead, E94b; RIGOROUS, computer-assisted). The rigorous range is now C < 13.2548.
  - Mixing. φ(2x/3) <= α1φ(x) + α2x on [0, 1] with α1 = 233809/10⁶ and α2 = 117344/10⁶.
    - Exact-rational certificate (src/e94b_mix_certify.py): 910 cells of bisection on G = F/x with monotone
      enclosures and isqrt-directed square roots.
    - Multipliers found by a Gurobi LP (src/e94_mix_bound.py).
  - Both bounds hold for the same w ∈ 𝒲 (|w| <= 1). So
        D_{2/3} <= α1·D + α2·(2√3/9) <= α1(259/2000) + α2(2√3/9) = 0.0754440,
    hence exponent 1/3 for C < 13.2548 (Beckner alone: 12.294).
  - Status: the 13.2548 range inherits P63's computer-assisted certificate. 12.294 remains the fully analytic range.
- Rigorous improvement path:
  - a rigorous N₂ = sup∫_0^1|w|² (≈ 0.3435 numerically) would give C < 1/(u*N₂) ≈ 13.8;
  - a dedicated D_{2/3} certificate (P63 machinery with φ(2x/3)) plus the cubic PD constraint would approach 15.6.
Status: paper proof (lead). Its inputs are P58, P59.1, P61(a) and Beckner's sharp Young inequality; it adds only
steps 2–6.
Not kernel-checked; codex adversarial check pending. Novelty: grep of PROOFS/NOTEBOOK for cubic profile, Schur cube,
X^{1/3} and u* found only the anchored-total remark (cont. 13.3) and the exponent-¼ square hierarchy (cont. 13.2).
External priority is unchecked.

## P67. Round-14 agent results: Sanders at every density — precise obstructions, no exponent gain (report .research/agents/tdense14_report.md; lead re-checked every item marked ✓) — 2026-10-19
No unconditional cyclic exponent above ¼ at fixed density, and no dense integer exponent above ¼ for all C. The best
for every C stays Bu et al.'s ¼; ours is 1/3 for C < 13.2548 (P66).
1. ✓ R14-CENTER (exact; lead re-derived).
   - Setup: u = (b − a)/(1 − 2a) is two-valued, so u^r = A_r u + m_r with
         A_r = ((1 − a)^r − (−a)^r)/(1 − 2a)^{r−1},   m_r = (a(1 − a)^r + (1 − a)(−a)^r)/(1 − 2a)^r.
     In Fourier: U^{(r)} = A_r U + q m_r δ. So U⋆U = U + qcδ off zero does NOT give U^{(3)} = U; the δ term
     regenerates at every order.
     - Witness: q = 17, B = {±1}.
     - Projecting the zero mode away after each product is non-associative (Z_5 example).
   - First-order coefficient after deleting the peak atom: A_r − r·m_{r−1}.
     - At r = 3, 4 it equals 1 − 2c, with c = a(1 − a)/(1 − 2a)². Lead check (exact): −½ at a = ¼; 11/18 at a = ⅛;
       −3 at a = ⅓.
     - The first favourable order is ≍ 1/a: exactly m − 1 (m even) or m (m odd) at a = 1/m. Its gap is
       −(m − 2)^{−(m−3)}.
   - Even at a favourable r, the truncation norm ‖U‖₁ <= 2K/(1 − 2a) gives only T = O(K^r), so K^{r+1} >> q. That is
     exponent <= ¼ at r = 3.
   - So the centred fixed-order Sanders transfer cannot beat ¼ by this estimate at any density.
2. ✓ R14-UNION (paper proof; lead re-derived the expectation).
   - Construction: pairs ±x are chosen independently with p_x = a + ε cos(2πx/q).
   - Then C = B ∪ 3^{−1}B has P(x ∈ C) = 2a − a² + ε(1 − a)(cos x + cos 3x) − (ε²/2)(cos 2x + cos 4x). So
     λ_C(2) = −ε²q/4 + O(√(q log q)), while K_B = O(√(q log q)) (bounded differences plus a union bound).
   - So union with a fixed dilate is not a usable density boost: it can create order-q negativity.
3. ✓ Half-set small-spectrum gap (lead re-derived).
   - Sanders' Lemma 3.2 mechanism at r = 3 (a = ½) gives 0 <= (1 − 3a)t + 3t³/q² + 3KL² + …, so
     Λ = O(KL²) = O(K³). This holds when every nonprincipal coefficient is < m/32.
   - With Parseval Λ >> q/K this gives only K⁴ >> q, the same ¼ as our second-order Λ <= √(2q)K.
   - Sanders' "1/3 by careful accounting" is NOT reconstructed in this small-spectrum branch; the large-coefficient
     branch does give 1/3 via Lemma 3.1. No counterexample to Sanders' assertion is claimed.
4. ✓ Embedding correction. q ∈ (2X, 4X] can give density a > ½ (A = {1, 2}, q = 5). Use q ∈ (4X, 8X]: then
   1/(4C) <= a < ½ (as P64.5 already did).
   - A per-density bound c(a) yields the integer corollary only if it is UNIFORM on [1/(4C), ½].
5. Soft half-density boost (w = ½ + (b − a)/2): any binary rounding has two-sided Fourier error >= √(q/32). This is
   an absolute-error obstruction only.
6. Data (examples/r14_certificates/).
   - Exact K_min for symmetric sets at densities ¼ and ⅛: exhaustive with Arb enclosures for q <= 31; Gurobi
     (floating point) for q <= 61.
   - Union probes up to q = 1048583.
   - Sanders v2 statements quoted with versions in the report. JMTZ, Bu Prop 9.7, Bedert, Shankar and Yip v2 are
     re-quoted: none has an exponent above ¼ at every density.
Lead's reading.
- Every density-transfer of Sanders tried here ends at ¼. Both the centred powers and the half-set
  small-spectrum branch fail through the same estimate, ‖P^{(r)} − F^{(r)}‖ <= rKL^{r−1}.
- An exponent above ¼ needs an estimate of the peak Λ that is better than O(KL²). This is the QU(2) wall of P65.

## P68. Round-15 agent results: P66 audited CORRECT and extended to C < 1000/73; the cyclic ¼ equality case made exact (report .research/agents/tdense15_report.md; lead re-checked every item marked ✓) — 2026-10-19
1. ✓ P66 AUDIT: every step CORRECT, with these qualifications (lead read all of them).
   - The cubic weak limit at fixed ε has the cross term (p − Q_ε)(1 − 3Q_ε + 3Q_ε²). It vanishes as ε -> 0,
     bounded by 2‖Q_ε − p‖_∞‖ψ‖₁.
   - Normalization: Ĥ(0) = m and Ĥ(k) = r_k/2, so Σ r_k³ cos kx >= −4m³ exactly.
   - The front cap needs only p(0) <= ½, continuity and p(1) = 0, not p(0) = max p. But p = φ(4e) needs p <= ½
     EVERYWHERE, which follows from P58/P59 or from a second IVT on e.
   - The Gabor/Jensen weights and σ-monotonicity are as stated.
   - Complex w ∈ 𝒲 are majorized by |G|⋆|G|~ (Boas–Kac root), so P63 and Beckner apply to the SAME w.
2. ✓ E94b re-proved by a DIFFERENT method.
   - Put s = √(1 − x); the inequality becomes √((1 + 2s²)/3) >= R(s) with R > 0.
   - Squaring gives (1 − s)T(s) with T a cubic. Exact Sturm: T has no roots in [0, 1].
   - Lead re-ran it on the VM: reproduced (examples/r15_certificates/mixing_sturm.*).
3. ✓ D_{2/3} <= 73/1000 (exact rational certificate, computer-assisted). Hence:
       THEOREM (P66 range): for every C < 1000/73 = 13.6986…, M(A) >= c(C)|A|^{1/3} for all finite
       A ⊂ Z_{>0} with max A <= C|A|; c(C) is ineffective.
   - The P63 certificate is ported: the only change is the radical, u²(2 − u²)/4 -> 1/12 + u²/3 − u⁴/6, i.e.
     √(1 − (2/3)(1 − u²)²)/2 squared; the lead checked the algebra.
   - Input: the E95 K = 64, degree 10, shape 0.1 discovery, with monotone rational repair.
   - Schur test: U = 1 + (2/5)s(1 − s), with T_aU <= (73/500)U. Minimum margin 1704250072843/1966080000000000.
   - Checks: 767 leaves, 127 caps, 188 support lines, 18 long lines, 64 Schur cells.
   - Lead re-ran BOTH the certifier and the independent verifier on the VM: PROVED by both
     (src/r15_rerun_lead.sh).
4. ✓ EXACT FLAT MODEL for cyclic half-sets (quoted from P26, renormalized; lead re-derived).
   - Definitions: t = K − ½, h(0) = t, h(γ) = λ(γ) + K (γ ≠ 0).
   - Then ȟ = b − ½ + Kδ_0 and h⋆h = (q²/4)δ_0 + qK(K − 1)·1 (unnormalized convolution). Hence:
     - (Λ + K)² <= qK(K − 1);
     - the endpoint defect E = Σ_{γ≠0}(Λ − λ)(λ + K) = (q − 1)[tL − t² − q/4] >= 0.
   - Together: (q − 1)t⁴ − (3q/4)t² − q²/16 >= 0, i.e.
         K >= ½ + √(q[3 + √(4q + 5)]/(8(q − 1))) = (½ + o(1))q^{1/4}.
     This is the best explicit constant in the record (cf. 0.42q^{1/4} in P64); the exponent is unchanged.
   - Correction to NOTEBOOK 18.5: P̌ − Ň = b − (q − 1)/(2q), not b − ½. The exactly flat object is h, not P.
5. ✓ Parity lemma (elementary; lead checked).
   - For any D ⊂ Z_q with 0 < |D| < q − 1: r_D(ξ) ≡ 1_D(ξ/2) (mod 2). So r_D − c is non-constant: some
     |r_D(ξ) − c| >= ½. This is the odd-order case of Brualdi 1965 (cyclic reversible difference sets are trivial).
   - Robust form: E + t² >= L²/[4(√(s + ½) + √s)²] for the rounded heavy core D = {h >= L/2}, s = |D|. At the ¼
     scale this forces only E >~ q: no power gain.
6. Quantitative rounding, saturation and zero-spike bounds (B3) are proved with explicit constants; they are not
   re-derived line by line by the lead.
   - Retained limitations:
     - thresholded-core support only;
     - a scalar counterexample with q^{3/4} weak positive modes;
     - the cos^{2d}(πx/q) counterexample: positivity plus sparse frequencies gives no polynomial size bound on half
       the group.
     - Galois separation is only exponentially small.
     - Exact Tao uncertainty gives |supp h| >= (q − 1)/2.
7. ✓ Missing lemma, stated exactly (CONJECTURED), and its conditional theorem.
   - WRS(η): max_{γ≠0} h <= A q^{(1−η)/2} t^{1+η} whenever h >= 0 is even with h(0) = t, Σh = qt,
     h⋆h = (q²/4)δ_0 + q(t² − ¼)·1 and ½ < t <= δ0√q. These hypotheses reconstruct exactly the Boolean half-sets.
   - WRS(η) ⇒ K >~ q^{(1+η)/(4+2η)}. Lead check: L >= q/(4t) gives t^{2+η} >= q^{(1+η)/2}/(4A).
   - η = 1 is Λ <~ K², i.e. PK(0) = QU(2), Sanders' 1/3.
8. Obstruction (proved algebra). Excluding equality by a fixed defect changes only the constant. A power gain needs
   1 − Δ_a <= (4/3)A²(t/√q)^{2η}, i.e. a defect that DECAYS with t/√q.
Status: items 1–3 are rigorous (paper plus exact certificates; P66 is now independently audited, not
kernel-checked). Items 4–8 are paper proofs or conjectures as labeled. No cyclic exponent above ¼.

## P69. Round-16 agent results: WRS still open; the heavy-core-sumset route is closed by an exact fake (report .research/agents/tdense16_report.md; lead re-checked every item marked ✓) — 2026-10-19
1. ✓ OBSTRUCTION (paper proof; finite instances exact/Arb-verified by the agent).
   - Parameters: g = ceil(log q), m = g², s = 2m, t = q^{1/4}g, L = √(C0/(4s)), D = ±{10m+1,…,11m}.
   - There is a nonnegative even h with h(0) = t, Σh = qt, Σh² = V, max h = L, and D EXACTLY the core {h >= L/2}.
   - h⋆h = C0 holds at EVERY ξ ∈ (D+D)∖0, but h⋆h(100m) − C0 = (¼ + o(1))q².
   - The construction uses separated 4-site clusters for each needed displacement plus an AP repair of mass and
     energy.
   - Lead re-derived it: the core–core term is <= L²s = C0/4; clusters have no cross differences in S; h vanishes on
     S; the repair run's adjacent products give ~E0 at displacement B0.
   - It violates WRS(η) for every fixed η > 0. Equations on the sumset of the maximum-relative core cannot force a
     power-decaying defect.
2. ✓ Mellin anti-concentration (proved; lead checked). X = (λ + ½)/√q satisfies X̂(χ) = θ·F̂(χ̄) with |θ| = 1 (Gauss
   sums). X >= −t/√q gives max|F̂| <= t/√q, so the Mellin support has >= q/(4t²) characters. Booleanity is exactly the
   Jacobi-weighted quadratic system Σ J̄·u u = 0. Unweighted Deligne phase bounds do not control these data-dependent
   weights (explicit algebraic counterexample).
3. Sign uncertainty (Gonçalves–Oliveira e Silva–Ramos, Thm 3.1) gives no t-dependence. Uniform r_D does not
   contradict Booleanity (Paley). All 23 genuine half-sets pass every new identity (NUMERICAL).
4. Next threshold proposed by the agent: A = {h >= V/(2qt)} carries >= ½ of Parseval and sees the fake's missing
   displacement. With cardinality bounds alone it still gives only ¼.
Status: no exponent gain. WRS remains CONJECTURED. The cyclic-WRS line is PAUSED in favour of the all-sets
architecture (NOTEBOOK cont. 19): sub-multiplicativity + the torsion-free boundary constraint.

## P70. Round-17 agent results: self-difference-graph programme corrected; CLIQUE-S refuted; sharp-boundary Gibbs lemma; √n for independent roundings (report .research/agents/tdense17_report.md; lead re-checked every item marked ✓) — 2026-10-19
1. ✓ CLIQUE-S IS FALSE for every pair of constants (paper proof, lead re-derived; deterministic terminating family).
   - Construction: L = t⁶, k = t⁵, g = (L − |j|)⁺, p_a = (g⋆g)(a)/Q. Then 1 + 2Σp_a cos(ax) = |ĝ|²/Q >= 0.
   - Force [1, k] ⊂ A and round a > k independently. The forcing cost is Σ_{a<=k}(1 − p_a) <= (3/2)√L, by
     Cauchy–Schwarz on telescoped increments.
   - Hoeffding on the grid G = 16L², plus the derivative bound, gives M <= ⌈√(L log₂(128L²))⌉ + 2√L + 1.
   - Hence the clique {0, …, k} satisfies |C|/K ~ L^{1/3}/√(log L) -> ∞.
   - Finite instance (L = 4096, seed 17): n = 3086, max A = 7587. Agent: pure-Arb certificate M <= 384437/5000.
     LEAD re-certified by a different method (blocked Arb-DFT + Taylor, src/r17_rerun_lead.py): M <= 76.884, with
     prefix [1, 1034] ⊂ A, so clique/K >= 6.73 (examples/r17_certificates/).
   - These sets are dense (max A/n < 4), so P63 still gives them √n. Clusters inside smooth tapers cost nothing.
2. ✓ SHARP-BOUNDARY GIBBS LEMMA (elementary; lead re-derived). For all finite A and all integers d, k >= 1:
       M(A) >= c₀k − D_d(k),   c₀ = 2/(3π) − 1/8 = 0.0872…,
       D_d(k) = |[1, k] ∖ A_d| + Σ_{b ∈ A_d, k<b<4k} (1 − b/(4k)),   A_d = {a/d : a ∈ A, d | a}.
   Proof:
   - Average over d-th roots of unity: M(A_d) <= M(A).
   - Fejér smoothing of degree 4k − 1 gives g = Σ_{b<4k}(1 − b/4k)cos(bx) >= −M.
   - At x = 3π/(2k+1) the full interval gives −(1 + csc(3π/(4k+2)))/2 <= −½ − (2k+1)/(3π).
   - The weights cost <= (k+1)/8; missing or extra frequencies cost <= D_d(k).
   - This is the correct structured-branch input: the boundary must be sharp in the AMBIENT difference spectrum.
     The item-1 family has D_1(k) ≈ (9/8)k, so it fails the lemma's hypothesis, as it must.
3. ✓ √n FOR INDEPENDENT ROUNDINGS (new; lead re-derived every step). Let A be the random set with independent
   P(a ∈ A) = p_a, let w be a P28 triangular window, and let v = Σp_a(1 − p_a)w_a².
   - Statement: P28 gives M >= B := ½E_x|Σw_aX_a e^{iax}|, with
         E B >= v/(2√(6v+1)),   Var B <= ¼.
   - Proof: symmetrize, take a fourth moment (E|W|⁴ <= 3Q² + Q) and use Hölder; the variance step is Efron–Stein
     for a convex ½-Lipschitz functional.
   - Corollary: if v >= cμ (μ = E|A| -> ∞), then M >= √(c/224)·√|A| with probability >= 1 − O(1/μ).
   - Tapered profile p_a = 2α(1 − a/X), uniformly in α <= ¼: M >= √|A|/(8√21) with probability >= 1 − 169/μ.
   - So the E99c tapered sets at density n^{−1/3}, where all graph certificates are ~n^{1/3}, are covered rigorously
     with high probability. Selected (correlated) roundings are NOT covered.
4. ✓ Obstruction (proved, lead checked the spectrum): for the shifted intervals {m+1, …, 3m}, Cay[A] is bipartite
   with singular values 1/(2 sin((2j−1)π/(4m−2))). The √n-bulk is o(n²) and the Frobenius distance to the PSD cone is
   >~ n, for W = A, A ∪ {0} and A ∪ (A+t), uniformly in t. Since M is linear here, the dichotomy must be
   conditioned on λ_min >= −ε√n.
5. ✓ Joint necessary conditions under M <= ε√n (lead checked the star constants).
   - Star: the 2×2 compression of Cay[{0} ∪ ±A] is [[0, √(2n)], [√(2n), 3e/n]], with T_S = 6e and
     e = #{a < b : b − a ∈ A}. Hence e >= (1/(3ε) − 2ε/3)n^{3/2}.
   - Bulk: Σ_{|λ|<=γ√n}λ²/n² <= 2ε·max(γ, 2ε).
   - P28 spikiness keeps its energy factor.
   - P48/P53 do NOT extend to vanishing density: all scale-X twisted limits vanish there.
6. ✓ Circularity warning (lead checked): the unrestricted P29(b) certificate EQUALS M. At h = 1, L = 2,
   f(θ) − 2Σ_{a even}cos(aθ) = −f(θ + π). So an adversary defeating fully optimized P29(b) is a Chowla counterexample;
   searches must use restricted families.
7. Also proved (agent):
   - Gram positivity alone is not a clique statement: the induced P3 has λ_min = −√2.
   - o(n⁴) C4-quasirandomness does not give a √n-bulk (blow-up counterexample).
8. NUMERICAL: 58 adversarial sets plus 4000 swap proposals, minimizing the MAX of the restricted certificates
   (P28 sample, W2, Bhatia–Davis, restricted P29(b)). Best ≈ 0.43√n; no family defeats all four.
Status: items 1–6 are paper proofs (1 also has two independent finite certificates). The FOUR-WAY COVER remains
OPEN. The remaining adversary class: CORRELATED (selected) roundings at vanishing density that hide P28 window
variance without creating a sharp ambient boundary.

## P71. Arc-mass bound (lead), and round-18 agent results (report .research/agents/tdense18_report.md, completed before the stop; items marked ✓ lead-checked) — 2026-10-19
1. ✓ ARC-MASS BOUND (lead; PROVED, elementary). Let K >= 2M(A), K > 1, p = 1 + D_S/K (density w.r.t. λ = dx/2π).
   Then for every x ∈ T and every ρ ∈ (0, π):
       p(B(x, ρ)) < max(4/K, 2√(ρ/π)).
   In f-terms (K = 2M): ∫_{x−ρ}^{x+ρ} (M + f) dy < max(4π, 4M√(πρ)).
   - Proof. Y, Y' iid ~ p; Y + Y' has density p⋆p = p/K + (1 − 1/K) (P-exact mixing). Y, Y' ∈ B(x, ρ) gives
     Y + Y' ∈ B(2x, 2ρ). So τ' := p(B(2x, 2ρ)) >= K(τ² − 2ρ/π), with τ = p(B(x, ρ)).
   - Set τ_k = p(B(2^k x, 2^k ρ)), so τ_{k+1} >= K(τ_k² − 2^{k+1}ρ/π). If τ_0 >= 4/K and τ_0² >= 4ρ/π, induction gives
     τ_k >= 2^k τ_0 and τ_k² >= 2^{k+2}ρ/π: the second makes the bracket >= τ_k²/2, so τ_{k+1} >= (Kτ_0/2)τ_k >= 2τ_k.
     Hence τ_k > 1 for 2^k > 1/τ_0, while the arcs still have radius < π (2^kρ <= πτ_0/2). Contradiction. ∎
   - Content: iterated form of the spike sub-multiplicativity (NOTEBOOK cont. 19.5(a)). A heavy arc (p-mass τ >= 4/K)
     must have half-length > πτ²/4.
   - Limits (checked): vacuous at the origin. There it reads Σ_{a∈A} sin(aρ)/a < 2π for ρ <= 4π/K², which every
     A satisfies up to the harmonic tail. As an L² bound it gives only n <~ XK (P33 territory). A FACT, not a route.
2. ✓ PERIODIC TRIANGULAR BOHR TAPERS HAVE LINEAR M (agent; lead re-derived every step). KERNEL-CHECKED 2026-10-19:
   lean/ChowlaCosine/BohrTaper.lean (sha256 749641df…7e93fa), theorems `lower_bound` and `lower_bound_card`, exact
   statement with no added hypotheses; axioms propext, Classical.choice, Quot.sound only (rebuilt and audited by lead).
   - Set-up. L ∈ 20Z_{>0}, P >= 100, q >= 4L + 1, r_q = centred residue. A(L,q,P) = {1 <= a <= Pq : |r_q(a)| <= L(1 − a/(Pq))}.
   - Packets. With h = L/20 and J = ⌊P/8⌋:
       U = {jq + r : 1 <= j <= J, −16h <= r < −14h},  V: −h <= r < h,  W: 14h <= r < 16h.
     - All three lie in A, since a/(Pq) <= 0.127 and the residue radius is >= 0.873L > 0.8L.
     - U, V, W are cliques, U–V and V–W are complete, and U–W has no edges:
       - every pairwise difference has |d| <= 0.129Pq, so the allowed radius is >= 0.871L;
       - residue differences are < 0.85L inside packets and across U–V and V–W, and >= 1.4L across U–W;
       - there is no wrap, since 1.6L < q/2.
   - Certificate. The vector (2, −3, 2) has norm² 17m and form −7m² − 17m. P9 gives M >= 7m/34 + 1/2.
   - Counting. m >= LP/90 and n <= (41/20)LP, so M >= 7n/6290 + 1/2. This holds uniformly in density: q = P = L²
     gives n = L³ and density n^{−1/3}.
   - Mechanism: tapering along the long coordinate does not smooth the TRANSVERSE Boolean cutoff (Gibbs seen by a
     blown-up induced P3). This matches the per-character-envelope reduction of the quadric lift (NOTEBOOK cont. 22).
3. BOUNDED-OCCUPANCY BLOCK SELECTORS (agent; lead checked the fourth-moment pairing E|ΣY_j|⁴ <= 3Q² + ΣE|Y_j|⁴ and
   the logic of the Efron–Stein step, but not every constant).
   - Set-up. Blocks are independent with arbitrary dependence inside each block, at most b selections per block,
     and v = Σp_a(1 − p_a)w_a².
   - Statement:
       E B >= v/(2√(6bμ + 4b²)),   Var B <= b/2.
     Hence M >= c√|A|/(4√(20b)) with probability >= 1 − (80b²/c² + b)/μ.
   - This extends P70.3 to antithetic pairs and to one-point-per-cell sampling. It does not cover globally selected
     outcomes.
   - Exact identity (any correlated selector): the circle average of E|centred window sum|² equals v. Hidden variance
     must therefore mean SPECTRAL CONCENTRATION, not smaller variance.
4. NUMERICAL (agent; uncertified FFT/Newton R, certificates exact).
   - Of 11 adversary families (cumulative, antithetic, Thue–Morse, nested Bohr of rank 1 and 2, dilation unions,
     forced-prefix thinning), only TAPERED SINGER–BU gets R < 1:
     - n = 756, X/n = 54: R ≈ 0.77, with W2 = 0.215√n and P28 = 0.245√n;
     - n = 72: certified M ∈ [7.427, 7.444], so R = 0.876.
   - All other families have R >= 2.
   - The best adversaries are ALGEBRAIC (square/difference-set) objects, not roundings.

## P72. Robust duality for near-Boolean weights (lead, 2026-10-19; PROVED, elementary; context E103, Ruzsa's question)
Setting: finite A ⊂ Z_{>0}, n = |A|, τ ∈ [0, 1). M_τ(A) := min over w ∈ [1−τ, 1+τ]^A of max_x −Σ_a w_a cos(ax).
For a probability measure μ on T write c_a(μ) = ∫cos(ax) dμ(x).
(a) Duality. M_τ(A) = max over μ of Σ_a (−c_a(μ) − τ|c_a(μ)|).
    Proof: the payoff Σ_a w_a(−c_a(μ)) is bilinear. The box and P(T) (weak-*) are compact and convex, so Sion's minimax
    applies. The inner minimum over the box is coordinatewise: min over w_a of w_a(−c_a) is −c_a − τ|c_a|.
(b) Flat lemma. If λ_s := |{x : f_A(x) <= −s}|/2π > 0, then M_τ(A) >= s − τ√(n(1/λ_s − 1)/2).
    Proof: take μ = normalized Lebesgue measure on that set. Then −Σc_a = −∫f_A dμ >= s. Also c_a² <= |μ̂(a)|², and
    Σ_{a>=1}|μ̂(a)|² = (‖dμ/dx‖²_{L²(dx/2π)} − 1)/2 = (1/λ_s − 1)/2, since μ is real. Finish with Cauchy–Schwarz over
    the n frequencies.
(c) Slope at τ = 0. τ ↦ M_τ is a maximum of affine functions, hence convex. Its right derivative at 0 is
    −min over μ ∈ Opt₀ of Σ_a |c_a(μ)| (Danskin), where Opt₀ = probability measures on argmin f_A.
    In particular M_τ >= M_0 − τ·min_{Opt₀} Σ|c_a|.
(d) Certificate spread (for 0 < τ < 1 only). Any μ certifying M_τ >= m satisfies Σ_a |c_a(μ)| <= (M_0 − m)/τ. A
    ROBUST √n certificate (m >= c√n with M_0 <= C√n) is therefore A-spread: Σ|c_a| = O(√n/τ). Compare the spatial
    AVERAGE ∫Σ_a|cos(2πax)|dx = (2/π)n. [Audit 2026-10-19: "a point mass has Σ|c_a| ≈ (2/π)n" is FALSE pointwise:
    δ_0 gives n, and δ_{1/4} on odd A gives 0. Only the average holds.]
(e) Weighted intervals stay linear (continuum form; the discrete statement needs a compactness argument, not written).
    A bounded φ on R, supported in [−1, 1], with φ >= 1 − τ > 0 there, has a jump at ±1. If φ̂ >= 0, the Fejér means at
    0 bound ∫φ̂ <= sup φ, so φ̂ ∈ L¹ and φ is continuous: contradiction. Hence the weighted Dirichlet profile has Gibbs
    >= c(τ)n.
    [Audit 2026-10-19: the qualitative claim (each such φ has some φ̂ < 0) is CORRECT. A uniform depth c(τ) is NOT proved,
    and is FALSE without the common upper bound φ <= 1 + τ: take φ_B = c·1_[−1,1] + B(1 − |x|)_+. Then
    φ̂_B = B[y + c·cos(t)/B]² − c²cos²(t)/B >= −c²/B, with t = πξ and y = sin t/t. For the intended box-bounded class the
    compactness argument and the discrete passage remain unwritten. Status of "Gibbs >= c(τ)n": GAP.]
Adversarial audit 2026-10-19 (codex, .research/agents/adv_p72_74_report.md): (a)–(c) CORRECT; (d) GAP (domain τ > 0;
point-mass remark false); (e) GAP (qualitative only). The lead checked both counterexamples by hand (δ_{1/4}: cos(πa/2) = 0
for odd a; φ_B: completing the square).
Reading (HEURISTIC): Chowla_τ (√n for all [1−τ, 1+τ] weights) is a strictly stronger statement than Chowla. On flat
sets (negative region of positive measure) it holds by (b); E103 measures only constant-factor losses there. In the
spiky regime (the C* regime) (b) is empty, and (d) says a proof must either use exact Booleanity or find an A-spread
certificate that is not a level-set measure.

## P73. Robust few-spike lemma: Boolean sets are L²-far from PD functions with peak < 4/3 (lead, 2026-10-19; PROVED, elementary)
This supplies the L² (Freiman-type) robust version that NOTEBOOK cont. 19.2(iv) asked for, in Z and on T.
Statement (Z). Let S ⊂ Z be finite and nonempty, and φ: Z -> C positive definite with φ(0) = m₀. Let
E = ‖φ − 1_S‖²_{ℓ²(Z)}. For every δ ∈ (0, ½): if m₀ < (4 − 5δ)/3, then E >= δ²(|S| − 1)/3.
Statement (T). Let Ω ⊂ T be measurable with 0 < |Ω| <= ½, and g ∈ C(T) positive definite with g(0) < (4 − 5δ)/3. Then
‖g − 1_Ω‖²₂ >= δ²|Ω|/3.
Proof (Z; T is identical, with Macbeath |A + B| >= min(1, |A| + |B|) in place of Cauchy–Davenport).
1. ψ := m₀ − Re φ >= 0 is conditionally negative definite. Indeed, the GNS vectors e_k with ⟨e_k, e_l⟩ = φ(k − l) give
   ‖e_k − e_l‖² = 2ψ(k − l). So √ψ is subadditive: √ψ(k + l) <= √ψ(k) + √ψ(l).
2. Let G = {k : |φ(k) − 1_S(k)| <= δ}. Chebyshev gives |Z \ G| <= E/δ².
3. Take k, l ∈ S ∩ G with k + l ∈ G \ S. Then ψ(k), ψ(l) <= m₀ − 1 + δ and ψ(k + l) >= m₀ − δ, so subadditivity forces
   3m₀ >= 4 − 5δ. Under the hypothesis this is impossible, hence (S_G + S_G) ⊂ S ∪ (Z \ G), where S_G = S ∩ G.
4. Cauchy–Davenport in Z: 2|S_G| − 1 <= |S| + |Z \ G|. With |S_G| >= |S| − |Z \ G| this gives |Z \ G| >= (|S| − 1)/3,
   hence E >= δ²(|S| − 1)/3. ∎
Consequences.
- (a) Chowla architecture, cont. 19.2(iii)–(iv). If the front S' = ±B ∪ {0} is ℓ²-approximated by the PD spike sum φ
  within δ²(|S'| − 1)/3, then the total front spike amplitude is m₀ >= 4/3 − 5δ/3. This closes the few-spike/AP
  alternative ROBUSTLY. The core (m₀ >~ √|B|) is untouched: for large m₀ the CND metric no longer separates S' from
  its complement (ratio (m₀ − 1)/m₀ -> 1). That is exactly the Chowla Gram problem again.
- (b) PR(1) in its small-peak regime (cont. 20.3). For Ω = −Ω with 1̂_Ω(k) >= 0 for |k| <= L and g = P_L1_Ω:
  - Exact identity: ∫g(1 − g) = Σ_{|k|>L} 1̂_Ω(k)² (the unresolved mass U), since ∫gh = 0 and ∫h = 0 for h = 1_Ω − g.
  - So U >= δ²|Ω|/3 whenever g(0) = Σ_{|k|<=L} 1̂_Ω(k) <= (4 − 5δ)/3.
  - The conjectured extremizers have g(0) ≈ 1.137 (half-density square wave) and ≈ 1.18 (arc of radius 1/(2L)), so
    both sit in this regime. The arc allows δ <= 0.092, i.e. U >= 2.8·10^{-3}|Ω|; the square wave allows δ <= 0.118,
    i.e. U >= 4.6·10^{-3}|Ω|. Not sharp (conjectured 0.0947).
  - The large-peak case g(0) >= 4/3 is OPEN. Example: Ω = {D_L > 0} has g(0) ~ (2/π²)log L and still U/|Ω| ≈ 0.30, so a
    large peak does not by itself contradict PR.
Status: PROVED on paper; elementary. A fact, not a C* tool. Adversarial audit 2026-10-19: Z and T versions CORRECT (5,005 T-tests, no violation).
KERNEL-CHECKED (Z version) 2026-10-19: lean/ChowlaCosine/FewSpike.lean (sha256 204985…c032731).
- Theorems: `fewSpike_core` (bad-set count >= (#S − 1)/3) and `fewSpike` (E >= δ²(#S − 1)/3).
- PD is defined by finite sums plus Hermitian symmetry.
- The proof uses the 3-point test (1, −2, 1), i.e. ψ(k + l) <= 2ψ(k) + 2ψ(l), in place of the GNS square root.
- Axioms: propext, Classical.choice, Quot.sound. Rebuilt and audited by the lead.

## P74. PR(1) at the resolution scale: U >= 2.5·10^{-4}·min(|Ω|, 1/L) (lead, 2026-10-19; PROVED, elementary)
Setting: Ω = −Ω ⊂ T = R/Z measurable, μ = |Ω| ∈ (0, ½], and a_k := 1̂_Ω(k) >= 0 for |k| <= L. Put g = P_L1_Ω (PD, real,
γ := g(0) = ‖g‖_∞) and U := Σ_{|k|>L} a_k² = ‖1_Ω − g‖²₂ = ∫g(1 − g).
Theorem. U >= 2.5·10^{-4}·min(μ, 1/L).
Proof. Take δ = 1/10 in P73(T), so γ₀ = (4 − 5δ)/3 = 7/6.
- (A) If γ < 7/6, P73 gives U >= δ²μ/3 = μ/300.
- (B) If γ >= 7/6, apply Bernstein twice to the degree-L polynomial g: ‖g''‖_∞ <= (2πL)²γ. Since g is even with its
  maximum at 0,
      g(x) >= γ(1 − 2π²L²x²) >= (7/6)(1 − 2π²L²x²).
  For |x| <= h := √(3/56)/(πL) this gives g(x) >= 25/24, so (g − 1_Ω)² >= 1/576 there (1_Ω <= 1). Hence
      U >= 2h/576 = √(3/56)/(288πL) >= 2.5·10^{-4}/L. ∎
Scope.
- This is PR(1) with a non-sharp constant for every window at the resolution scale (μ <= 1/L). That includes the
  extremal arcs of E100 (radius 1/(2L)).
- For μL >> 1 with a large peak it is OPEN: case (B) gives only ~1/L. Numerically E105 finds U/μ >= 0.104 there (L <= 16).
- Not a C* tool: PR is step (d) of the cont. 20 architecture, rank 1 only.
- Adversarial audit 2026-10-19: CORRECT; both constants re-derived; 4,358 accepted numerical cases, no violation.

## P75. Automatic sets: a domination-or-twin criterion forces LINEAR M (lead, 2026-10-19; PROVED on paper, elementary; CSTAR A2 / T-A2)
Setting.
- Deterministic automaton on states S, base b, 0/1 digit matrices C_d, and C = Σ_d C_d PRIMITIVE with Perron root λ,
  1 < λ < b.
- Right eigenvector r > 0 and left eigenvector π > 0, normalized πᵀr = 1. Start state s₀ with δ(s₀, 0) = s₀;
  A_L = {1 <= k < b^L : the L-digit string of k is accepted}.
- μ := the stationary Parry measure on T: μ([v]) = λ^{−|v|} Σ_s π_s r_{δ(s,v)}, read via base-b expansion.
- τ_v := the state map s ↦ δ(s, v) (reject allowed). ρ(v)_t := Σ_{s : τ_v(s) = t} π_s. E_t := mean of the Parry
  measure ν_t (from t) on [0, 1].
- For u = m/b^p and N >= 0 (k = p + N): w, w⁻ are the p-digit expansions of m and m − 1, and
      I(u) := R(w0^N) + L(w⁻(b−1)^N),  R(v) = Σ_t ρ(v)_t r_t (1 − E_t),  L(v) = Σ_t ρ(v)_t r_t E_t,
  with I(0) := R(0^k) + L((b−1)^k).
Theorem. Suppose EITHER some u = m/b^p, N >= 0 has G(u) := I(u) + I(−u) − 2I(0) > 0, OR there are twins
u_i = m_i/b^{p_i} (each with some N_i, G(u_i) = 0) whose reduced denominators q_i satisfy b | lcm(q_i). Then Re μ̂(j) < 0 for some j ∈ Z. Consequently M(A_L) >= (c − o(1))|A_L| for a constant c > 0
(LINEAR M).
Proof.
1. Suppose Re μ̂ >= 0. Then σ := (μ + μ̃)/2 has σ̂ = Re μ̂ >= 0. With Λ_r := 1_[0,r] ⋆ 1_[−r,0] (triangle on [−r, r],
   Λ̂_r(j) = (sin πjr/πj)² >= 0) and r := b^{−k}, φ := σ ⋆ Λ_r is continuous and positive definite (φ̂ = σ̂Λ̂_r >= 0,
   summable).
2. Translate structure. μ restricted to a cylinder [v] satisfies μ([vx]) = λ^{−|vx|} Σ_s π_s r_{δ(τ_v(s), x)}. So it
   depends on v only through (|v|, τ_v), and its triangle weights are λ^{−|v|}b^{−|v|}·R(v) on the right of the
   cylinder's left endpoint and λ^{−|v|}b^{−|v|}·L(v) on the left of its right endpoint.
   - B(u, b^{−k}) = [w⁻(b−1)^N] ∪ [w0^N]; B(0, b^{−k}) = [(b−1)^k] ∪ [0^k]. Parry measures are atomless, so the
     endpoints are null.
   - Hence φ(u) = (I_μ(u) + I_μ(−u))/2 and φ(0) = I_μ(0) up to the common factor λ^{−k}b^{−k}, where I_μ(x) =
     ∫Λ_r(x − y)dμ(y) and Λ_r is even. So G(u) >= 0 means φ(u) >= φ(0).
3. A PD function is maximal at 0, so G(u) > 0 is a contradiction. If G(u) = 0, PD gives |φ(x + u) − φ(x)|² <=
   2φ(0)(φ(0) − Re φ(u)) = 0, so φ is u-periodic: σ̂(j)Λ̂_r(j)(e(jm/b^p) − 1) = 0 for all j.
4. Take j with b ∤ j. Then Λ̂_r(j) ≠ 0, since its zeros are jr ∈ Z \ {0}, i.e. j ∈ b^kZ \ {0}. Each twin gives
   σ̂(j)(e(j u_i) − 1) = 0. Since b | lcm(q_i) and b ∤ j, j is not divisible by every q_i, so e(j u_i) ≠ 1 for some i.
   Hence σ̂(j) = 0. (A single twin with gcd(m, b) = 1 has q = b^p, so it suffices on its own.)
5. ×b-invariance (μ̂(bj) = μ̂(j)) extends this to σ̂(j) = 0 for every j ≠ 0. So σ = Lebesgue and μ <= 2·Lebesgue.
   But μ is supported on the sofic set X, which has ≍ λ^k admissible length-k cylinders and Lebesgue measure 0
   (λ < b): μ is singular. Contradiction.
6. Transfer to A_L. Let ν be the Parry measure from s₀. Then A_L/b^L → ν weakly, so f_{A_L}(t/b^L)/|A_L| → Re ν̂(t)
   for fixed t. Primitivity gives (×b)^m_* ν → μ, so Re ν̂(b^m j) → Re μ̂(j) < 0. Fix m with Re ν̂(b^m j) < 0, and set
   t = b^m j. ∎
Coverage (E108d, FLOAT evaluation of G; p <= 4, N = 40): 20,476 of 71,840 small automata (28.5%) satisfy the
hypothesis: 15,829 by domination (G > 1e-9) and 4,647 by twins (|G| < 1e-12, b | lcm q_i). Uncovered, 51,364:
- b = 4 (43,435): typically one tie at u = 1/2 only (lcm = 2). These automata carry a base-2 symmetry. The tie gives
  σ̂(odd) = 0, so σ' := (×2)_*σ is again PD and ×4-invariant, with σ' = Lebesgue ⇒ σ = Lebesgue. Re-running the test
  on σ' (a base-2 rewrite) would be the next step. NOT implemented.
- b = 5 (7,726) and b = 3 (203): G < 0 strictly at every tested u (0 is the strictly heaviest triangle point).
  The 2-point test cannot decide these; a >= 3-point Gram test (Σ c_i c̄_j φ(x_i − x_j) < 0) is needed.
In general T-A2 remains a CONJECTURE: "the max-entropy measure of a proper positive-entropy sofic subshift of the
b-shift is never positive definite".
Separately, ALL 71,840 small automata (sector_all: b = 3: 213, b = 4: 58,377, b = 5: 13,250) are INTERVAL-CERTIFIED
dead by the advisor's finite-prefix certificate (E108a): each has a certified t with Re ν̂(t) < −0.084 (worst case
−0.0843, b = 5, t = 241/25, h = 5). The stationary μ has min_{j<=J} Re μ̂(j) < 0 for all 71,840 (float; the largest
value is −0.0106).
Status: PROVED on paper; elementary. It is a construction-class obstruction (CSTAR DESIGN), NOT a C* proof step: it
kills automatic families at the MACROSCOPIC level, before the mesoscopic (depth-dependent) question arises.

## P76. Nonnegative-Gram and completely positive square certificates (PROVED, lead 2026-10-19 cont. 29; elementary)
Side lemma (CSTAR A5). Setting: f_A + λ = v*Qv with v = (e(iθ))_i and diagonal sums Σ_iQ_{i,i+k} = ½·1_A(k), k >= 1.
(a) DNN = PSD on an unbounded index set: inf{tr Q : Q ⪰ 0, Q >= 0 entrywise} = M(A).
    Proof: Q_T = (1/T)Toep_T(λδ + ½1_{±A}) is >= 0 entrywise and PSD for λ >= M. Add (k/(2T))·J₂ on {0, k} for each
    k ∈ A. The extra trace is ΣA/T → 0.
(b) CP bound. If 2f_A + C = Σ_j|P̂_j|² with every P_j >= 0 coefficientwise, then each supp P_j is a clique of
    Cay(Z, ±A), and C >= 2n/(ω − 1). Proof: Σ‖P_j‖₁² = 2n + C, and ‖P_j‖₁² <= |supp P_j|·‖P_j‖₂² <= ω‖P_j‖₂².
(c) Extreme-lag multiplicities. If B = {b_1 < … < b_s} ⊂ Z, then #{(b, b') ∈ B² : b' − b = b_s − b_i} <= i.
    Consequence: no finite B ⊂ Z has flat multiplicities (contrast the subgroup blocks of F_p^r quadrics). Also
    |A ∩ (a* − Δ, a*]| <= C·(|A ∩ [1, Δ]| + 1) for any CP certificate.
(d) Sublattice restriction: C_CP(A_q) <= C_CP(A), where A ∩ qZ = q·A_q. Proof: replace each P_j by its q
    residue-class parts. Their autocorrelations are exactly the qZ-lags, and Σ‖·‖₂² is unchanged. This is the CP
    form of P13. Hence C_CP(A) >= max_q 2|A_q|/(ω(A_q) − 1).
Open: CP-Chowla, C_CP >= c√n (E111).

## P77. CENTROID BARRIER for Boolean lifts of a finite set (lead, 2026-10-20 cont. 31; PROVED on paper, elementary;
## codex-audited CORRECT after routine repairs; numerical inputs E117/E118; context CSTAR A10 / E116; not kernel-checked)
Setting. n >= 2, D ⊂ Z_n² with D = −D, 0 ∉ D, finite spectrum D̂(χ) = Σ_{g∈D} cos(2πχ·g/n) (χ ∈ Z_n²).
Fix r' and a NONEMPTY SYMMETRIC (B = −B) background set B ⊂ {χ ≠ 0 : D̂(χ) <= −r'}; put N = Z_n² ∖ B; D nonempty.
(Repairs from the codex audit, 2026-10-20: without B = −B, P_N need not preserve odd real functions — counterexample
n = 3, D = {±(1,0)}, B = {(1,0)}; alternatively define λ_odd as the top of the quadratic-form compression to odd real
functions. If A2 = 0, (a) reads K >= r' by evaluating at a background point. The averaging weights ω are nonnegative.) A ONE-REP LIFT is an odd map z: D → Z²
with z(g) ≡ g (mod n); T = z(D), F(ξ) = Σ_{g∈D} cos(2π z(g)·ξ) on T², K(T) = −min F. Define
  W(χ) = Σ_g z(g) sin(2πχ·g/n) ∈ R²,   A2 = Σ_{χ∈B} |W(χ)|²,   Z4 = (Σ_g |z(g)|⁴)^{1/2},
and λ_odd = top eigenvalue of the concentration operator C = 1_D·P_N·1_D on ODD real functions on D,
P_N f = (1/n²)Σ_{χ∈N} f̂(χ)χ (so Σ_{χ∈N}|f̂(χ)|² = n²⟨f, Cf⟩).
Theorem. (a) K(T) >= r' + A2/(8n|B|^{1/2}Z4).
(b) A2 >= (1 − λ_odd)·n²·Σ_g |z(g)|². Hence, since |B| <= n²,
        K(T) >= r' + ((1 − λ_odd)/8) · Σ_g|z(g)|² / (Σ_g|z(g)|⁴)^{1/2}.
(c) If every |z(g)| <= √2·Vn (reps within V periods) and Σ_g|z(g)|² >= β|D|n², then
        K(T) >= r' + (1 − λ_odd)·β·|D|^{1/2}/(16V²).
Proof. (a) z(g) ≡ g gives e(z(g)·(χ + α)/n) = e(χ·g/n)e(z(g)·α/n). For χ ∈ B pick u_χ ∈ U = {±e₁, ±e₂} with
u_χ·W(χ) = |W(χ)|_∞ and put h_χ(t) = F((χ + t u_χ)/n) = Σ_g cos(2π(χ·g + t z(g)·u_χ)/n). Then h_χ(0) = D̂(χ) <= −r',
h_χ'(0) = −(2π/n)|W(χ)|_∞, h_χ''(t) = −(4π²/n²)Re Q_{u_χ}(χ, t) with Q_u(χ, t) = Σ_g e((χ·g + t z(g)·u)/n)(z(g)·u)².
For fixed u and t, Parseval over all χ ∈ Z_n² gives Σ_χ|Q_u(χ,t)|² = n²Σ_g(z(g)·u)⁴ <= n²Z4². For weights ω on B
(Σω = 1), Cauchy–Schwarz on each B_u = {χ : u_χ = u} and over the four u:
  Σ_χ ω_χ|h_χ''(t)| <= (4π²/n²)·Σ_u ‖ω|_{B_u}‖₂·nZ4 <= (8π²/n)Z4‖ω‖₂.
Taylor with integral remainder and min F <= Σ_χ ω_χ h_χ(ρ):
  min F <= −r' − (2πρ/n)Σ_χ ω_χ|W(χ)|_∞ + (4π²ρ²/n)Z4‖ω‖₂.
Take ω_χ = |W(χ)|_∞/S₁ (S₁ = Σ_B|W|_∞, S₂ = Σ_B|W|_∞²) and optimise ρ: min F <= −r' − S₂^{3/2}/(4nS₁Z4). Then
S₁ <= (|B|S₂)^{1/2} and S₂ >= A2/2. ∎(a)
(b) Each coordinate f_k = z_k·1_D is odd and real, so f̂_k = i·W_k and Σ_χ|W(χ)|² = n²Σ_g|z(g)|² (Parseval).
Σ_{χ∈N}|W|² = Σ_k n²⟨f_k, Cf_k⟩ <= λ_odd n²Σ_g|z(g)|², and W(0) = 0. ∎(b)   (c) is (b) with Z4 <= √|D|·2V²n².
Remarks.
- FRACTIONAL lifts escape exactly here: for the PD taper τ = Λ(z₁/n)Λ(z₂/n), Σ_{z≡g} τ(z) z = 0 for EVERY class (the
  τ-weighted centroid of the lattice translates vanishes), so the first-order term is identically 0, while
  Σ_{z≡g}τ(z) = 1 and F_w >= −r (Poisson). A Boolean lift with 1 <= m(g) < n reps in class g has centroid sum
  M_g ≡ m(g)·g (mod n), never 0 for g of order n. The same proof with z(g) replaced by M_g (and D̂ by m̂, Z4 by
  (Σ_g(Σ_{z≡g}|z|²)²)^{1/2}) covers lifts with class multiplicities m(g); for constant m ≡ c it gives
  ratio = c|D|/K² <= C·c³V⁴/((1 − λ_odd)²β²).
- Scope. This is a barrier for a MODEL CLASS (Boolean lifts of a fixed finite set with bounded spread V), not for Z.
  For an arbitrary S ⊂ Z reduced mod N the hypothesis λ_odd < 1 is exactly what a C* object would violate (its own
  position field is concentrated on its spikes, since F' ≈ 0 on a flat background), so P77 says nothing about C*
  in general. It lower-bounds the Z² minimum; a 1D Freiman image (z₁ + Vz₂) has K_1D <= K_2D, with K_1D → K_2D as
  V → ∞, so P77 transfers to 1D images only for large V.
- Inputs (E117, numerical eigenvalues, not certified): JL a = 2, j = 1: λ_odd = 0.605 (p=3), 0.542 (5), 0.390 (7),
  0.303 (11), 0.353 (13); a = 3, p = 3: 0.801 (j=1), 0.756 (j=0). Centred lifts have φ := Σ_N|W|²/Σ|W|² = 0.05–0.32;
  SA-optimised one-rep lifts (E116) push φ to 0.48, 0.27, 0.11 (p = 3, 5, 7), approaching λ_odd at p = 3.
- AUDIT (codex, 2026-10-20, .research/agents/p77_check_report.md; lead-read): every step of (a), (b), (c) and the PD-taper
  centroid remark CORRECT after the repairs above. Numerical falsification on dirichlet: 928 lifts (centred, random
  one-rep with V = 1, 2) of JL(3,2,1), JL(5,2,1), JL(7,2,1, partial), 0 violations; margins K − bound >= 6.7, 26, 61
  (the bound is far from tight). The random-D controls were not reached (agent stopped).
- E118 (CVP test): maximising φ alone (binary QP on the rep shifts) lowers K a lot against the centred lift but does not
  reproduce the K-optimal lifts at p = 7, where SA reaches lower K with LOWER φ. So the centroid term is real but not
  the binding cost; P77's increment (~r + 0.1√|D|) is an order below the observed K − r.
- So, IF λ_odd <= 1 − c uniformly in p (numerically <= 0.61 for a = 2, p <= 13; unproved), every bounded-spread
  one-rep lift of the JL a = 2 family has ratio <= C(c, V, β) uniformly in p: the "lift a high-ratio finite object"
  model cannot reach ratio → ∞. The constant is weak (p = 7: bound increment ≈ 1.2 against the observed K − r ≈ 38).

## P78. Taper-random one-rep lifts: K <= r + C√(|D| log n) (lead, 2026-10-20 cont. 31; PROVED on paper, elementary)
Setting. n odd, D ⊂ Z_n² ∖ 0 symmetric with D̂(χ) >= −r for χ ≠ 0. τ(z) = Λ(z₁/n)Λ(z₂/n), Λ(t) = max(0, 1 − |t|).
Theorem. There is an odd one-rep lift z: D → [−n, n]² (z(g) ≡ g, z(−g) = −z(g)) with
    K(T) <= r + 4√(|D|·ln(4π²n²|D|)) + √|D|,     T = z(D), F_T(ξ) = Σ_{g∈D} cos(2π z(g)·ξ).
For JL D_{2,j} (n = p², |D| = p(p² − 1), r = p): K_opt = O(p^{3/2}√log p) = o(p²), so ρ_opt >= c/log p.
Proof. (i) Σ_{z≡g} τ(z) = 1 for every class (codex audit of P77). Fractional lift F_τ(ξ) = Σ_z τ(z)1_D(z mod n)cos(2πz·ξ).
Poisson: 1_D(z mod n) = n⁻²Σ_χ D̂(χ)e(χ·z/n), so F_τ(ξ) = n⁻²Σ_χ D̂(χ)τ̂(ξ + χ/n), τ̂(η) = Φ_n(η₁)Φ_n(η₂) >= 0
(Fejér), Σ_χ τ̂(ξ + χ/n) = n²τ(0) = n² (τ vanishes on nZ² ∖ 0). With D̂(0) = |D| >= 0 and D̂ >= −r off 0:
F_τ(ξ) >= −r·n⁻²Σ_{χ≠0}τ̂(ξ + χ/n) >= −r.
(ii) For one g from each pair {g, −g} choose z(g) = ḡ + nt (t ∈ {−1, 0}²) with probability τ(z), independently; z(−g) = −z(g)
(τ is even, so −z(g) has law τ on the class −g). Then E F_T = F_τ, and F_T − F_τ = Σ_{pairs} Y_g with Y_g ∈ [−4, 4]
independent, mean 0. Hoeffding: P(F_T(ξ) − F_τ(ξ) < −λ) <= exp(−2λ²/(64·|D|/2)) = exp(−λ²/(16|D|)).
(iii) |∇F_T| <= 2πΣ_{g}|z(g)| <= 2π√2·n|D|. On the grid of spacing h = 1/(2πn√|D|) (N_g = h⁻² points) every ξ is within
Euclidean distance h/√2 of a grid point, so F_T(ξ) >= F_T(grid) − 2πn|D|h = F_T(grid) − √|D|. Union bound with
λ = 4√(|D| ln N_g) (strict inequality by any slack): with positive probability F_T >= −r − λ on the grid. ∎
Numerics (E119): taper-random K measured at p = 3..13 (examples/e119/scaling.jsonl).

## P79. Uniform odd-concentration gap for Jedwab–Li D_{2,j} (lead, 2026-10-20 cont. 31; PROVED on paper; reduction checked
## numerically against the direct eigenvalue to 1e−15 for (p,j) = (3,1),(3,2),(5,1),(5,2),(7,1),(7,3),(11,1),(13,1),(13,5): E121)
Setting. p odd prime, n = p², j ∈ {1, …, p−1}, D = D_{2,j} = D₀ ∪ D₁ (src/e114_cp_group.jl_set(p, 2, j)):
  D₀ = {(yv, y) : y ∈ (Z/n)^*, v ∈ V_j}, V_j = {jp + s : 0 <= s < p};  D₁ = {(x, py') : 1 <= y' < p, x ≡ jy' (mod p)}.
B = {χ ≠ 0 : D̂(χ) = −p}, N = Z_n² ∖ B, λ_odd = sup over odd real f ≠ 0 on D of Σ_{χ∈N}|f̂(χ)|²/(n²‖f‖²).
Theorem. λ_odd = max_ψ ‖M_ψ‖²/p² over PRIMITIVE odd characters ψ of (Z/n)^* (conductor-p characters give 0), where
    M_ψ = [[H, ψ̄(j)φ], [φᵀ, 0]] ∈ C^{(p+1)×(p+1)},  H[s₀, s] = ψ̄(s − s₀) (s ≠ s₀), H[s, s] = 0,  φ_s = ψ̄(1 − pj⁻¹s),
and λ_odd <= Λ(p) := [(p + 3) + √((p + 7)(p − 1))]/(4p) <= Λ(3) = (6 + 2√5)/12 < 0.8727, Λ(p) → 1/2.
Proof.
1. G = (Z/n)^* acts on Z_n² by scalars. D is G-invariant; the action on D is FREE with p + 1 orbits, representatives
   g_s = (jp + s, 1) (0 <= s < p) and g_* = (j, p). [(yv, y) = y·g_{v−jp}; (x, py') = u·g_* with u = xj⁻¹ mod n, a unit with
   u ≡ y' (mod p). Free: the coordinate 1 of g_s, resp. j of g_*, is a unit.] Sizes p(p−1); total |D| = p(p² − 1).
2. D̂(uχ) = D̂(χ), so B, N are G-invariant and the concentration form commutes with G. Odd real functions split into
   ψ-components (ψ(−1) = −1): f(u g_O) = ψ(u)a_O, ‖f‖² = p(p−1)Σ_O|a_O|². f̂(χ) = Σ_O a_O G_ψ(χ·g_O),
   G_ψ(t) = Σ_{u∈G}ψ(u)e(−ut/n). Gauss sums: ψ primitive (nontrivial on 1 + pZ): G_ψ(t) = ψ̄(t)G_ψ(1) for t a unit,
   |G_ψ(1)| = p, G_ψ(t) = 0 for p | t (group u by u mod p; Σ_{u≡w}ψ(u) = 0). ψ of conductor p: G_ψ(t) = 0 unless p ∥ t
   (t a unit: Σ_k e(−kt/p) = 0 inside each u ≡ w class; t ≡ 0: Σψ = 0).
3. Spectrum (Ramanujan sums c_n(t) = p(p−1), −p, 0 for t ≡ 0, p ∥ t, unit): D̂(χ) = Σ_O c_n(χ·g_O). Case analysis on
   χ = (α, β): α unit ⇒ exactly one s₀ with p | χ·g_{s₀}, χ·g_* a unit; α = pα' (α' ≢ 0): χ·g_s = pα's + β, χ·g_* = p(α'j + β);
   α = 0. Result: D̂ ∈ {p² − p, −p} off 0, and N ∖ 0 = N₁ ∪ N₂ with
     N₁ = {(α, −α(jp + s₀)) : α unit, 0 <= s₀ < p}  (orbit O_{s₀} has χ·g ≡ 0, all others units),
     N₂ = {(pα', β) : 1 <= α' < p, β unit, β ≡ −α'j (mod p)}  (O_* has χ·g ≡ 0, all g_s units).
   In particular on N no orbit has p ∥ χ·g_O, so conductor-p components have f̂ = 0 on N (f̂(0) = 0 by oddness).
4. Primitive ψ. On N₁: χ·g_s = α(s − s₀), χ·g_* = α(j − ps₀), ψ̄(j − ps₀) = ψ̄(j)φ_{s₀} (ψ(1 + pt) depends on t mod p), so
   f̂(χ) = G_ψ(1)ψ̄(α)(Mx)_{s₀}, x = (a_s, a_*). On N₂: χ·g_s = β(1 + pα'β⁻¹s), α'β⁻¹ ≡ −j⁻¹ (mod p), so
   f̂(χ) = G_ψ(1)ψ̄(β)(φᵀa). |N₁| = p²(p−1), |N₂| = p(p−1), each with |G_ψ(1)|² = p²:
   Σ_N|f̂|² = p³(p−1)‖Mx‖², while n²‖f‖² = p⁵(p−1)‖x‖². Hence the ψ-block of the concentration form is M*M/p².
5. ψ odd ⇒ H[s, s₀] = ψ̄(−1)ψ̄(s − s₀) = −H[s₀, s]: H is complex ANTISYMMETRIC. For antisymmetric A and A*Av = σ²v (σ > 0),
   J v := conj(Av)/σ satisfies A*A(Jv) = σ²Jv, ⟨v, Jv⟩ = conj(vᵀAv)/σ = 0, J² = −1 (antilinear quaternionic structure), so
   every nonzero singular value has even multiplicity (Youla). Hence σ₁(H)² <= ‖H‖_F²/2 = p(p−1)/2.
6. ‖Mx‖² = ‖Ha + ψ̄(j)a_*φ‖² + |φᵀa|² <= (σ₁‖a‖ + √p|a_*|)² + p‖a‖², ‖φ‖² = p. The top eigenvalue of
   [[σ₁² + p, σ₁√p], [σ₁√p, p]] is increasing in σ₁; at σ₁² = p(p−1)/2 it equals p[(p+3) + √((p+7)(p−1))]/4. Divide by p².
   Λ is decreasing for p >= 3 ((1 + 7/p)(1 − 1/p) decreases). ∎
Numerics (E121, NUMERICAL): λ_odd = 0.605 (p=3), 0.542/0.469 (5; j=1/2), 0.390/0.377 (7), 0.303 (11), 0.353/0.300 (13);
σ₁(H)²/p² = 0.33, 0.37, 0.35, 0.27, 0.30 (bound (p−1)/(2p)). Top pair always degenerate (step 5 confirmed).
Scope: j ≠ 0 only (j = 0 changes the orbit structure of D₁). Depth a >= 3 is NOT covered and there λ_odd → 1
numerically (E117: p = 3, a = 3, 4: 0.80, 0.94).

## P80. Bounded-spread one-rep lifts of D_{2,j} have bounded ratio, uniformly in p (lead, 2026-10-20; corollary of P77 + P79)
Statement. p odd prime, j ≠ 0, z: D_{2,j} → Z² an odd one-rep lift with ‖z(g)‖_∞ <= Vn. Then the Z² minimum satisfies
    K₂D(T) >= p + (1 − Λ(p))·√|D|/(192V²) >= p + 0.127·√|D|/(192V²),   so   ρ = |D|/K₂D² <= (192V²/(1 − Λ(p)))² <= 2.3·10⁶·V⁴.
Proof. P77(c) with r' = p, B = {D̂ = −p} (nonempty, symmetric), |z| <= √2Vn, and β >= 1/12: |z(g)|² >= (g_k)_c² for each
coordinate k (centred residue), and on O_s the second coordinate of u·g_s is u, on O_* the first coordinate of u·g_* is uj,
each running over all units once. So Σ|z|² >= (p+1)Σ_{u unit}u_c² = (p+1)(p² − 1)p²(p² − p + 1)/12 = |D|n²(p³ + 1)/(12p³). ∎
SHARPER FORM (lead, same day): Σ|z|⁴ <= max|z|²·Σ|z|² gives Σ|z|²/Z4 >= (Σ|z|²)^{1/2}/max|z|, so P77(b) yields
    K₂D >= p + (1 − Λ(p))·(Σ|z|²)^{1/2}/(8 max|z|) >= p + (1 − Λ(p))√|D|/(8√24·V) >= p + 0.00325·√|D|/V,
    ρ <= (8√24·V/(1 − Λ(p)))² <= 9.5·10⁴·V²   (V² instead of V⁴).
Self-check (E121b, codex unavailable until 2026-10-25): exact set identities (orbits, free action, two-valued spectrum,
N ∖ 0 = N₁ ∪ N₂), β >= (p³+1)/(12p³) (observed β ≈ 0.167–0.185), H antisymmetric with doubled top singular value for every
primitive odd ψ, and max_{j,ψ}‖M_ψ‖²/p² <= Λ(p): all TRUE for p = 3, 5, 7, 11, 13, 17, 19 and every j = 1..p−1;
reduction = direct eigenvalue at (17,1), (19,2).
With P78: K_opt(one-rep) ∈ [p + c√|D|, p + C√(|D| log p)], so the advisor's "K ≈ 0.92p²" cannot hold for optimal lifts as
p → ∞ (it is o(p²)); P77's √|D| order is the right order up to √log.
Scope (important). This bounds the Z² minimum. A 1D Freiman image S_V = {z₁ + Vz₂} has K₁D <= K₂D, with K₁D >= K₂D − 1 once
V >= C·n|D| (Lipschitz); for small V the 1D image is a different object and is NOT covered. Free subsets / variable
multiplicities (E116 SA, E120 MIQP), unbounded spread and depth a >= 3 are not covered. The constant is useless numerically
(observed ρ ~ 0.2); the content is uniformity in p: the JL a = 2 one-rep model cannot give ρ → ∞.

## P77-d. The centroid barrier in Z_n^d (lead, 2026-10-20; same proof as P77 with 2d directions; PROVED on paper)
D ⊂ Z_n^d ∖ 0 symmetric, B ⊂ {χ ≠ 0 : D̂(χ) <= −r'} nonempty symmetric, z: D → Z^d odd one-rep lift, W, A2, Z4, λ_odd as
in P77 (Parseval now n^d). Then
    K(T) >= r' + A2/(2√2·d^{3/2}·n^{d/2}·|B|^{1/2}·Z4)   and   K(T) >= r' + (1 − λ_odd)·(Σ|z|²)^{1/2}/(2√2·d^{3/2}·max|z|).
Changes from P77: U = {±e_k} has 2d elements, |W|_∞² >= |W|²/d, Σ_u‖ω|_{B_u}‖₂ <= √(2d)‖ω‖₂, Σ_χ|Q_u|² = n^dΣ(z·u)⁴ <= n^d Z4²;
the optimised decrement is S₂^{3/2}/(2√(2d)·n^{d/2}·S₁·Z4); then S₁ <= √(|B|S₂), S₂ >= A2/d, A2 >= (1−λ)n^dΣ|z|²,
|B| <= n^d, Z4 <= max|z|·(Σ|z|²)^{1/2}. (d = 2 recovers the constant 8 of P77.)

## P81. Quadric cones: the odd concentration operator is EXACTLY (1/p)·I; one-rep lifts are excluded (lead, 2026-10-20;
## PROVED on paper, two lines; E122b numerics: all odd eigenvalues = 1/p to 1e−15, r = 4 (p = 3..11), r = 6 (p = 3, 5))
Setting. p odd prime, r >= 4 even, Q nondegenerate on F_p^r with Gauss sign η = +1 (CSTAR O6), A = {x ≠ 0 : Q(x) = 0}.
Â(χ) = p^{r/2−1}(p−1) − 1 on the dual cone {Q*(χ) = 0, χ ≠ 0} and −p^{r/2−1} − 1 off it; r' = p^{r/2−1} + 1,
B = {Q*(χ) ≠ 0}, N = {Q*(χ) = 0} (including 0).
Theorem. On odd functions on A, 1_A P_N 1_A = (1/p)·Id. So λ_odd = 1/p and every odd function puts exactly 1/p of its
spectral energy on N (in particular the centred position field: φ = 1/p, observed).
Proof. c_N(d) := p^{−r}Σ_{χ∈N}e(χ·d/p) = p^{−r}[1 + Σ_{χ∈cone*∖0}e(χ·d/p)], and the dual cone's transform depends only on
whether d = 0, Q(d) = 0 or Q(d) ≠ 0 (same Gauss-sum computation with Q** ∝ Q; same sign η). For g ≠ ±h in A,
Q(g − h) = −B(g, h) = −Q(g + h) and g ± h ≠ 0, so c_N(g − h) = c_N(g + h): the odd kernel c_N(g − h) − c_N(g + h) vanishes
off the diagonal. On the diagonal 2g ∈ A, and c_N(0) − c_N(2g) = p^{−r}[|{Q = 0}| − p^{r/2−1}(p − 1)] = p^{−r}·p^{r−1} = 1/p,
using |{Q = 0}| = p^{r−1} + p^{r/2−1}(p − 1). ∎
Corollary (model exclusion). Every odd one-rep lift z: A → Z^r with ‖z‖_∞ <= Vp has (P77-d, β: on each line {ug}, a nonzero
coordinate g_k makes (ug_k) run over F_p^*, so Σ_{g∈A}|g_c|² >= |A|p(p+1)/12)
    K(T) >= p^{r/2−1} + 1 + (1 − 1/p)·√|A|/(4√6·r²·V),     r = 4:  K >= p + 1 + (1 − 1/p)√|A|/(157V),
and |A| = (p²−1)(p+1) for r = 4, so ρ = |A|/K² <= (157V)²/(1 − 1/p)² <= 5.6·10⁴V² uniformly in p (finite ρ_G = p − 1).
Scope as P80: Z^r minimum; 1D Freiman images with small V, free subsets, multiplicities and unbounded spread not covered.
Novelty (2026-10-20, two targeted web searches, advisor's request): no prior statement of the odd-concentration identity
found. Closest: strongly regular affine polar graphs VO^±(2m, q) (spectra, association schemes; e.g. arXiv 2402.05055,
aeb.win.tue.nl/graphs/VO.html) and symmetric uncertainty principles (J. Algebra 586 (2021) 899–934). The mechanism
(Q(g ± h) = ±B(g, h) on the cone) is classical, so P81 is very plausibly a short consequence of known VO⁺ structure; claim
no novelty for the identity itself, only for its use as a lifting barrier. Advisor independently confirmed p = 3, 5.
(η = −1 swaps the roles: then N ∖ 0 is the complement of the dual cone and the same computation gives 1 − 1/p; irrelevant,
since η = −1 has negative spikes.)

## P80c. Transfer of P80/P81 to 1D Freiman images (lead, 2026-10-20; d = 2 PROVED; d >= 3 statement WRONG as first
## written, REPAIRED per the advisor's review 4 (pasted by the user); repair checked numerically E123)
FIRST VERSION (kept for the record; WRONG for d >= 3): "K₁D(S_V) >= K_d(T) − (π²/2)Σ_{z∈T} z₁²/V² (d = 2; general d by the
same step in the first coordinate)". The d = 2 case is correct. For d >= 3 a single coordinate cannot be steered.
COUNTEREXAMPLE (advisor; verified E123): d = 3, T = {±e₂, ±e₃}, V = 8 (an odd one-rep lift over (Z/3)³): F_T has min −4,
f_{S_V}(x) = 2cos(16πx) + 2cos(128πx) has min −3.850015 (8x ≡ ½ forces 64x ≡ 0), while Σz₁² = 0. A random d = 3 trial
in E123 also violated the z₁-only bound. The quadric (r = 4) transfer claimed from it was therefore UNPROVED.
REPAIRED STATEMENT. T ⊂ Z^d finite symmetric, F_T(ξ) = Σ_{z∈T}cos(2πz·ξ), S_V = {Σ_k V^{k−1}z_k : z ∈ T} with V > 2max‖z‖_∞
(injective), f_{S_V}(x) = F_T(x, Vx, …, V^{d−1}x). Then
    K₁D(S_V) >= K_d(T) − (π²/(2V²))·Σ_{z∈T}(Σ_{k=1}^{d−1}|z_k|)².
Proof. Let ξ* minimise F_T (∇F_T(ξ*) = 0). Put x = (ξ*_d + m)/V^{d−1}, m = Σ_{i=0}^{d−2} m_iV^i, digits m_i ∈ {0, …, V−1}. Then
V^{d−1}x ≡ ξ*_d exactly, and for k < d, V^{k−1}x ≡ m_{d−k−1}/V + o_k (mod 1), where the offset o_k ∈ [0, 1/V) depends only on
ξ*_d and the digits m_i with i < d − k − 1. Choose m_0, m_1, …, m_{d−2} in this order; the candidates for coordinate
k = d − 1 − i form the full grid o_k + (1/V)Z, so its distance to ξ*_k is <= 1/(2V), and later digits never change it.
So (x, Vx, …) = ξ* + δ with δ_d = 0, |δ_k| <= 1/(2V). Taylor (integral remainder; |∂²_δF| <= 4π²Σ_z(z·δ)²):
f_{S_V}(x) <= F_T(ξ*) + 2π²Σ_z(z·δ)² <= −K_d + (π²/(2V²))Σ_z(Σ_{k<d}|z_k|)². ∎  (d = 2: the first version.)
Tightness: the counterexample has loss 0.1542 against actual gap 0.1500.
CONSEQUENCES.
- JL D_{2,j} (d = 2): unchanged. With g = (1 − Λ(p))√|D|/(8√24·W) and Σz₁² <= |D|W²n², V² >= π²|D|W²n²/g gives
  K₁D >= p + g/2, i.e. V >= C·W^{3/2}·n·|D|^{1/4}/√(1 − Λ).
- Quadric cones, r = 4 (d = 4): Σ_z(Σ_{k<=3}|z_k|)² <= 3Σ_zΣ_{k<=3}z_k² <= 9|A|W²p². With g_Q = (1 − 1/p)√|A|/(157W) (P81),
  V² >= 9π²|A|W²p²/g_Q, i.e. V >= 118·W^{3/2}·p·|A|^{1/4}/√(1 − 1/p), gives K₁D >= p + 1 + g_Q/2. Same shape as JL,
  different constant; max(S_V) ~ V³Wp is polynomial in p. So the quadric one-rep model is excluded IN Z for such V
  (now with a valid proof).
- Small V (e.g. V ≈ 4n in the experiments) remains uncovered.
E123 (NUMERICAL): 120 random odd lifts in d = 2, 3, 4 with random V: repaired bound never violated (min margins 0.10,
0.36, 2.36).

## P82. Local Taylor (centroid) inequality in 1D, continuous form (lead, 2026-10-20; PROVED on paper, elementary; side lemma)
For every real C² 1-periodic f, every r' and every measurable B ⊂ {f <= −r'} with |B| > 0:
    −min f >= r' + ∫_B f'² / (2√2·|B|^{1/2}·‖f''‖_{L²(T)}).
Proof. For x ∈ B step in the descent direction u_x = −sign f'(x): f(x + ρu_x) <= f(x) − ρ|f'(x)| + ∫_0^ρ(ρ − t)|f''(x + tu_x)|dt.
Average with ω = |f'|1_B/S₁ (S₁ = ∫_B|f'|, S₂ = ∫_B f'²); split B by the sign of f' and use Cauchy–Schwarz with translation
invariance of ‖f''‖₂: ∫ω|f''(x + tu_x)|dx <= √2‖ω‖₂‖f''‖₂. Optimise ρ: decrement S₂^{3/2}/(2√2S₁‖f''‖₂) >= S₂/(2√2|B|^{1/2}‖f''‖₂). ∎
It is the d = 1, q → ∞ form of P77 and uses no Booleanity. BAC (Boolean anti-concentration: ∫_{f<=0}f'² >= c∫f'² for Boolean
dense A) would give T-dense for all C via r' = 0; E124 shows BAC does not separate Boolean sets from fractional packets at
computable sizes, so it is a gap HYPOTHESIS, not a mechanism. Route closed (ROUTES, advisor review 5).

## Unnumbered proof supplement: recovered passes of 2026-10-20

Existing P identifiers above are unchanged. Full statements, proofs and their hypotheses remain in the linked notes; this ledger does not silently strengthen them. Unless stated otherwise, PROVED means paper proof with the archived independent audit where linked, not new Lean/kernel verification.

| Statement or mechanism | Status and precise scope | Source / audit |
| --- | --- | --- |
| Deterministic cyclic-Sidon fibers and adaptive windows | PROVED on paper: pairwise H<=416p^3 log^4, selective reference cutoff removes all actual marginal-law restrictions; M>=sqrt(n)/16 eventually for ANY p-point cyclic-Sidon assignments at U=sqrt(X), kernel gap>3X. Congruence-lattice count proves O(X^2U^2 log U) off-left triples. Dense windows with Fourier norm<=Bp^delta, delta<1/2, have deterministic M>=c sqrt(n) after matching window/cardinality. Fixed-profile partial-parabola extension REFUTED by Omega(p^4) cost. Exact independent finite checks; no unrestricted Chowla, novelty, agent or Lean audit | [Proofs, hypotheses, countercontrol, constants and checks](notes/cstar_sidon_deterministic_2026-10-20.md) |
| Nonlinear sign with a small Sidon-fiber mean | PROVED on paper: exact ruling cubic identity; off-left cost<=19683X^2U^4; uniform shift sixth moments imply expected positive left cost O(X^3). At U=X^(1/4), ANY coupling with uniform affine-parabola fiber marginals has Pr[M>=sqrt(n)/5]>=1/6 eventually, despite M(mean)=o(sqrt(n)). Degree-three kernel gap>3X suffices. Conditional coupling>=n_u/8 is proved; uniform conditional cubic cost remains OPEN. Exact finite certificates/population checks; no external/Lean or universal Chowla claim | [Argument, constants, finite evidence and next lemma](notes/cstar_sidon_mixed_2026-10-20.md) |
| Short-factor rank-one residue obstruction; scale-independent disk parity | PROVED on paper: uniform GL2(F_p) phases average every nonzero rank-one residue to -1/(p^2-1); scalar transfer gives M>=n/(8B^2) for ANY encoded rank-one selection with primitive u, ||w||<=B<=X. Thus truncated ||u||>=sqrt(X), n/X^2->infinity families have diverging R. Separately uniform disk-center marginals satisfy s/60<=M(mean)<=s/2 without scale gaps. Exact GL2/disk and independent finite checks; no universal/Lean/independent-agent claim | [Proof, hypotheses, center-law countercontrol, checks](notes/cstar_wide_parity_2026-10-20.md) |
| Fixed-cardinality attainment and record reduction | PROVED reduction; no quantitative Chowla bound | [Proof](notes/cstar_extremizer_compactness_2026-10-20.md) |
| Sharp local W2 constant | REFUTED by exact rational/integer positive-definiteness certificate; does not refute every positive constant | [Statement and certificate](notes/cstar_w2_universal_2026-10-20.md), [independent verifier](experiments/cstar_structural_2026-10-20/verify_w2_exact_certificate.py) |
| Independent product-Fejer rounding | PROVED high-probability model-specific W2 bound, with separate support-filling and independence hypotheses | [Proof](notes/cstar_product_fejer_asymptotic_2026-10-20.md), [audit](notes/cstar_product_fejer_independent_audit_2026-10-20.md) |
| Fixed positive-half autocorrelation 3D span | PROVED asymptotic obstruction for that span only | [Proof](notes/cstar_order_profile_asymptotic_2026-10-20.md), [audit](notes/cstar_order_profile_asymptotic_independent_audit_2026-10-20.md) |
| Full-W2 amplification exclusions | PROVED for the stated fixed/product/orbit/fiber classes; changing near-contained bases and adaptive fibers remain open | [Report and proof links](notes/cstar_full_w2_falsification_2026-10-20.md), [audit](experiments/full_w2_falsification_2026-10-20/audit.md) |
| Weak-W1 balanced layers and interval implant | PROVED: prescribed-bottom-mode translated repair and odd-sector resolvent stay weak; not a full-W2 counterexample | [Proof](experiments/groundstate_repair_2026-10-20/schur/groundstate_product_no_amplification.md), [audit](experiments/groundstate_repair_2026-10-20/audit/groundstate_product_obstruction_audit.md) |
| Balanced-layer full-W2 rescue | PROVED: K_W2>=sqrt(N)/22 for k>=1, r>=4k^2; transfers to implant via independent coordinate | [Proof](experiments/groundstate_repair_2026-10-20/translation/balanced_layers_full_w2_certificate.md), [audit](experiments/groundstate_repair_2026-10-20/audit/balanced_layers_full_w2_audit.md) |
| Random tapered weak W1 | PROVED using dependency-sensitive three-color decoupling and imported matrix concentration | [Proof](experiments/groundstate_repair_2026-10-20/obstructions/weak_w1_taper_proof.md), [audit](experiments/groundstate_repair_2026-10-20/audit/weak_w1_taper_audit.md) |
| Coupled axis-union family | PROVED: weak W1, exterior and center-deleted W2, but K_W2/sqrt(N)->1, with unique square-root negative outlier and localization; enhanced five-condition selection required | [Main proof](experiments/coupled_mode_2026-10-20/exterior/exterior_counterfamily.md), [companion](experiments/coupled_mode_2026-10-20/order/direct_union_order_audit.md), [audit](experiments/coupled_mode_2026-10-20/audit/FULL_W2_COMPANION_AUDIT.md) |
| Root-orbit low-spectral-cost obstruction and bouquet identities | PROVED restricted control; root family is not weak W1, and spectral projection differs from arbitrary low-Rayleigh mixtures | [Proof](experiments/coupled_mode_2026-10-20/multimode/root_orbit_low_cost_obstruction.md), [audit](experiments/coupled_mode_2026-10-20/audit/AUXILIARY_ROOT_ORBIT_AUDIT.md) |
| Universal full-W2 / Chowla square-root theorem | OPEN; neither proofs for special models nor finite searches settle it | [Current gap](notes/cstar_coupled_mode_2026-10-20.md), [STATE](STATE.md) |
| Fixed-interior restart calibration | PROVED on paper: C=2 fails on the 128-interval; explicit affine exterior correction gives C=95/16 for every interval. Exact rational witnesses at C=6 on 1,053 finite supports; universal criterion remains OPEN | [Proof and exact-check scripts](NOTEBOOK.md#2026-10-20--restart-audit-and-fixed-interior-calibration) |
| Global L4 completion and selector controls | PROVED on paper: unrestricted L4 certificate/dual; four-wise selectors p_i<=1/2, mu>=64 satisfy square-root bound 1/20 with probability>=1149/2048; three-wise raw-moment counterfamily has separate linear bound; one-sign completion fails at every constant. Fourteen finite witnesses checked exactly. Universal inverse/deletion step OPEN | [Proofs, limits, code and checks](NOTEBOOK.md#2026-10-20--active-goal-global-l4-completion-and-a-four-wise-selector-theorem) |
| Mean-zero partial majorants and deletion control | PROVED on paper: relaxed certificate, positive nonconstant multipliers, translation identity, and a weighted counterexample to equality-dual positivity. EXACT FINITE: computed rational-dual rank deletion misses an improving subset; 18 comparisons verified. Universal strict-record cost upper bound OPEN; no kernel/independent audit claimed | [Statements, proofs, scope, and checks](notes/cstar_partial_majorants_2026-10-20.md) |
| Boolean forced-plateau separation and adaptive coupling | PROVED on paper using Spencer: n~5L/12, M=Theta(sqrt(n)), J_≥/sqrt(N)>=c L^(1/8); refutes bounded-ratio cost control and J_≥^4=O(NK^2). Variable interior coefficients certify the same family. Four exact finite lower certificates independently checked, with separate Arb upper certificates. Full Chowla and strict-record cost condition OPEN | [Theorem, proof, energy pivot, checks and scope](notes/cstar_forced_plateau_2026-10-20.md) |
| Integer rank-one cone construction | PROVED on paper: Frobenius-ball encodings 1,S,R,RS with separated place values have M>=n/4000 uniformly eventually; box at B=2X+1 has M>=n/200 via a different resonance. Exact sign checks and finite Arb witnesses; no universal Chowla or independent-agent audit | [Proofs and qualifications](notes/cstar_integer_cone_2026-10-20.md) |
| Boolean variance/coupling identity | EXACT algebra: for q=D_A-D_p, a=Q/2+sum p(1-p)+n-sum p; a weighted row is unnecessary merely for macroscopic coupling when cardinality error is small. Does not construct a general profile | [Derivation](notes/cstar_integer_cone_2026-10-20.md#6-adaptive-profile-identity-and-why-it-is-not-yet-the-universal-step) |
| Plane isolation and alias packing for encoded cones | PROVED on paper: injective rank-one cone encoding with a primitive row/column norm>47X has M>=pi X^2/64 for X>=30,000,000. Comparable entries and |det C|<=H force that hypothesis; an explicit critical CRT escape is separately excluded with M>=n/100 eventually. Four positive-measure certificates independently checked. No universal Chowla or external/Lean audit | [Proof, exact hypotheses, and verification](notes/cstar_cone_alias_packing_2026-10-20.md) |
| Complete finite-cone noise spectrum and stable Boolean alternatives | PROVED on paper: full spectrum 1,1/p,1/p^2; exact confinement iff ruling-plane span, Boolean perfect selectors iff single-ruling unions. Balanced-ruling leakage >=(1-1/p) times variance; two-ruling threshold Hamming error <=4p/(p-1) times leakage. Relative single-ruling stability REFUTED by an exact mixed-plane family. Independent exact p=3,5,7 checks, no external/Lean audit | [Proof, countercontrol and checks](notes/cstar_cone_confinement_2026-10-20.md) |
| Directional-fiber and arbitrary-annular integer cone obstructions | PROVED on paper under distinct CRT hypotheses: complete radial fibers satisfy M>=n/50-154X^2 uniformly in selected directions; arbitrary rank-one subsets in [3X/5,X] satisfy M>=n/12 when coprime CRT moduli >=1000X. Rotational J0 sign checked exactly. Positive disk-autocorrelation radial profile evades rotational averages fractionally; no Boolean realization or universal Chowla conclusion | [Statements, proofs, finite independent checks and limits](notes/cstar_cone_confinement_2026-10-20.md) |
| Varying-marginal Boolean quantization leakage | PROVED on paper: arbitrary profile/Boolean rounding on finite det=0 cone leaks at least (1-1/p) sum of scalar-line quantization minima. Exact sorted-prefix formula; coefficient range<=1/2 gives profile variance. Exhaustive 84 line and 16 cone checks. L2 statement only, not a torsion-free sign bound | [Derivation and checks](notes/cstar_radial_boolean_2026-10-20.md) |
| Genuine Boolean radial front with a mesoscopic negative excursion | PROVED on paper: rational Halton lens-shell family has n~(3pi/32)X^2 log X and nonnegative EVERY fixed-matrix-phase front, yet M>=X^(3/2)/2^36 for L>=64 under the stated CRT encoding, by a uniform lens Fourier sign and positive Fejer isolation. Three finite supports independently reconstructed and certified. No universal Chowla, novelty, independent-agent or Lean claim | [Construction, all quantified statements, proof and verification](notes/cstar_radial_boolean_2026-10-20.md) |
| Small-fiber center fluctuations and sharp fractional mean budget | PROVED on paper: exact parity identity; independent-center CLT with variance~cX^3 after large-fiber removal. Weighted Poisson smoothing gives M(mean)~m/2 and diverging expected R for ANY same-marginal coupling. Growing-phase extension allows activation and bounded radius staggering; size-comparable whole-fiber samplers cannot guarantee ratio<=1/300 on every output. Explicit scopes; not a bound for arbitrary deterministic sets. Independent finite parity/point/mean checks; no external/Lean audit | [Theorems, dependencies, sampler quantifiers and verification](notes/cstar_fiber_centers_2026-10-20.md) |
| Correlated zero-circle repairs and their separate sign failure | PROVED on paper: a mod5 full/empty-center assignment repairs the whole limiting zero circle at the same leading cardinality, changes the prescribed marginals, and has M>=n/16 eventually at t=5. FINITE: three Gurobi target repairs have rigorous listed floors and missed negative points. Serialization snapshot bug repaired and all floors rechecked. No all-circle upper certificate | [Countercontrol, finite data and limits](notes/cstar_fiber_centers_2026-10-20.md) |

Dependency order: the coupled theorem imports the tapered selected-adjacency estimate, combines it with scalar Fourier bounds, filling and weighted-energy control on the same jointly selected base, then uses exact axis decomposition and carry-free encoding. Its small finite scripts check assembly, not the infinite-family quantifier. The bottom-mode obstruction is a separate preceding result, not an assumption of the coupled theorem. The full catalog of other restricted structural notes is in [RECOVERY_INDEX](RECOVERY_INDEX.md).
