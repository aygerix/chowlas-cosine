# Run-top bound |B_t| << K^4: report of agent "runtop" (2026-10-18)

Brief: `.research/agents/runtop_brief.md`. Outcome type **(b) OBSTRUCTION**, together with an exact reformulation of what
any improvement must prove. No unconditional K^{4-δ} bound was obtained. Option (c) also failed: I found no
non-tautological conditional improvement. Scratch scripts (all runs < 2 s) are in the session scratchpad
`/private/tmp/claude-501/-Users-jmercedes-Desktop-Projects-Research-chowla-cosine/fde48ec6-19ca-4821-b9ff-9ab9929dd9e0/scratchpad/`.

## Conventions
- e(y) = e^{2πiy}, T = R/Z.
- A = −A ⊂ Z\{0} is a finite set and a_m = 1_A(m).
- F(x) = Σ_{a∈A} e(ax). The true hypothesis is F + K ≥ 0 on T. Write G := F + K.
- A_t = A∩(A+t) and B_t = {m : m ∈ A, m−t ∈ A, m+t ∉ A}.
- f_t = 2(1 + sin 2πtx)F, so f̂_t(m) = 2a_m − i a_{m−t} + i a_{m+t}.
- r_t = (1 − cos(2πtx + π/4))(f_t∗f_t). ψ_t and φ_t are the even and odd parts of r_t.
- Bedert (2509.05260v3 §7) uses three ingredients:
  - (37): f_t∗f_t ≥ −16K²;
  - (38): |φ_t| ≤ ψ_t + 32K²;
  - Lemma 7.1: 1̂_{B_t} = Q_1 + Q_2 with |Q_1| ≤ 4G and ||Q_2||_2 ≤ CK².
- Status labels: PROVED / OBSTRUCTION / NUMERICAL (float, uncertified) / INTERVAL-CERTIFIED (finite case, arb) /
  HEURISTIC / OPEN.

## 0. Results at a glance
1. **Theorem A (OBSTRUCTION, PROVED; probabilistic existence, explicit constants).** For every N ≥ 2.4·10^6 and every integer
   1 ≤ t ≤ N^{1/2} there is a symmetric A ⊂ [−N, N]\{0} with the following properties, where K_*⁴ ≤ 21 N log N:
   - f_t∗f_t ≥ −16K_*² on all of T. Hence (37) and (38) hold verbatim with K = K_*.
   - The norm-level conclusions of Lemma 7.1, which are all that Prop 7.3 uses, hold with K = K_*.
   - |B_t| ≥ 6.6·10^{-5} K_*⁴ / log K_*.
   - The Prop 7.3 machinery with the *optimal* Q gives nothing better: inf_Q (||1̂_{B_t} − Q||_2² + K_*²||Q||_1²) ≥ c|B_t|.

   So the deduction "(38) + Lemma 7.2 + norm form of Lemma 7.1 ⇒ |B_t| ≲ K⁴" is **sharp up to log K**. No better test
   function can improve it.
2. **Theorem B (OBSTRUCTION, PROVED).**
   - **Degree 2.** Fix any finite family of "Bedert-type" inequalities w·((m_1G + m_1'K)∗(m_2G + m_2'K)) ≥ 0, where w and
     the m's are nonnegative trigonometric polynomials in tx. Random sets satisfy all of them with K_* ≍ (N log N)^{1/4}
     while |B_t| ≍ N. Bedert's (37) is the case m = 2(1+sin), m' = 2(1−sin).
   - **Degree r.** For r-fold convolutions the cap is K^{2r}.
   - **Combined with the degree-1 barrier (§4):** any argument of the form "pointwise gap inequality + test function" is
     capped at K⁴. Prop 7.3 is optimal in that class.
3. **Proposition C (INTERVAL-CERTIFIED finite cases + HEURISTIC asymptotics).** The additive K² in (37)/(38) is really
   needed: it is attained up to a constant by genuine sets with F ≥ −K. Each case below is an arb enclosure at a single
   point, and K ≤ |D| holds exactly:

   | set | t | f_t∗f_t(x) |
   |---|---|---|
   | Singer q = 53 | 2035 | −1720.39 = −0.590·54² ≤ −0.59K² |
   | Singer q = 31 | 760 | −0.668·32² |
   | Erdős–Turán p = 59 | 3423 | −0.511·59² |

   The asymptotic constant in the triangle-profile model is ≈ −0.555. So no improvement of the *constant term* of (38)
   below cK² is possible.
4. **The degree-1 barrier in the brief is CORRECT** (§4), with three caveats: the multiplier must not depend on A, the
   witness configurations must be admissible, and the barrier says nothing about degree-1 information used *without* a
   gap.
5. **Proposition M (PROVED).** The exact output of the Prop 7.3 method is
   |B_t| ≤ 4388 ∫_T min(|1̂_{B_t}|, 13.46·K·|B_t|^{1/2})² dx.

   Lemma 7.1 is used only to bound the right side by ≲ K⁴. An exponent gain through this method is therefore *equivalent*
   to a "spikiness" or large-values estimate for run-top spectra below height K³ (Target Lemma S, §6). Lemma S fails for
   the random relaxed sets, so it must use F ≥ −K at degree 1.
6. **Group remark (PROVED / OPEN).**
   - Bedert's Prop 7.3 holds verbatim in every finite abelian group.
   - A bound valid in all Z_N transfers to Z.
   - Whether some finite group admits |B_t| ≫ K^{2+ε} is OPEN. It is a decisive question: if such examples exist, an
     improvement must use torsion-freeness.
   - Every group family I examined gives |B_t| ≲ K² (§7).

---

## 1. What Prop 7.3 actually consumes
I re-derived the chain from the paper text (§7, pp. 14–19). It agrees with `.research/agents/bedert_avg.md` §1–2.

**Abstract Prop 7.3.** Let α = 4 + 1/√2, β = 4 + √2 and γ = 4 + 2√2 be the constants of Lemma 7.2. The inputs are:
- (38) with an additive constant E (Bedert: E = 32K²);
- Lemma 7.2 (pure combinatorics of 0/1 sequences);
- any Q ∈ L²(T), symmetrised.

The output is
|B|^{1/2} ≤ 33.12·||1̂_B − Q||_2 + (E/(β−α))^{1/2}·||Q||_1.

With E = 32K² the second coefficient is 6.727·K. Re-derivation:
- Test X = ∫(ψ + E)(H∗H) with H = |Q|.
- Upper bound: X ≤ α||Q||_2² + E||Q||_1².
- Lower bound: X ≥ β|B| − 2γ|B|^{1/2}r − γr², where r = ||1̂_B − Q||_2.
- Solve the resulting quadratic in |B|^{1/2}.

Lemma 7.1 enters **only** to supply Q, through ||Q_1||_1 ≤ 4K and ||1̂_B − Q_1||_2 ≤ CK². Its pointwise content
|Q_1| ≤ 4G is used only to get the L¹ bound.

**Useful identity (PROVED; checked numerically to 3·10^{-9} on 9 families).** From
(2β − iα + iγ)² = 4β − α − γ + 2αγ − 4iβα + 4iβγ:

f_t∗f_t(x) = (4 − 2cos 2πtx)·F(x) + 2·e(−tx)·1̂_{A_{2t}}(x) + 8·Im 1̂_{A_t}(x).

The middle term is real. The two bilinear terms satisfy |1̂_{A_{jt}}| ≤ G∗G + O(K) = G + K² + O(K). This is where the
scale K² of (37) comes from.

## 2. Theorem A: random sets saturate (37)/(38)  [OBSTRUCTION, PROVED]

**Construction.**
- Profile: W(u) = ½(1 − |u|)_+ and h(w) = (√(1+2w) − 1)/2, so that 2h + 2h² = w.
- Set π = h∘W and p_j = π(j/N) for j ≥ 1. Then:
  - 0 ≤ p_j ≤ (√2 − 1)/2 < 0.21;
  - π is decreasing on [0, ∞) and ¼-Lipschitz (h' ≤ ½ and W is ½-Lipschitz);
  - p_j ≥ 0.207(1 − j/N), by concavity of h.
- Take independent ξ_j ~ Bernoulli(p_j) for 1 ≤ j ≤ N−1, and put A = {±j : ξ_j = 1}. This is a symmetric set in
  [−N, N]\{0}.

**Statement.** Let N ≥ N_0 := 2.4·10^6 and 1 ≤ t ≤ N^{1/2}. Define

E_0 := 21t + 43·(N log(512N²))^{1/2} + 1 and K_* := (E_0/16)^{1/2}.

Then K_*⁴ ≤ 20.8·N log N, and with probability ≥ 1/2:
- (i) f_t∗f_t(x) ≥ −16K_*² for every x ∈ T. Hence r_t(±x) ≥ −32K_*², and (38) holds with constant 32K_*².
- (ii) |B_t| ≥ 0.0055N ≥ 6.6·10^{-5}·K_*⁴/log K_*.
- (iii) The norm conclusions of Lemma 7.1 hold with Q_1 = 0 and Q_2 = 1̂_{B_t}:
  - ||Q_1||_1 = 0 ≤ 4K_*;
  - ||Q_2||_2 = |B_t|^{1/2} ≤ (2N)^{1/2} ≤ K_*².
- (iv) For some absolute c > 0 and N ≥ N_0' (also with positive probability):
  inf_{Q∈L¹∩L²} (||1̂_{B_t} − Q||_2² + K_*²||Q||_1²) ≥ c·N ≥ (c/2)|B_t|.

The pointwise form |Q_1| ≤ 4(F + K_*) is unsatisfiable here, because F + K_* < 0 somewhere. So is F ≥ −K_* itself.
The true K of these sets is ≍ (N log N)^{1/2} ≍ K_*², which is consistent with Chowla.

**Proof.** Write Φ := f_t∗f_t = Σ_m c_m e(mx), with c_m = (2a_m − i a_{m−t} + i a_{m+t})². Then |c_m| = 4a_m + (a_{m+t} − a_{m−t})² ≤ 5,
and Φ is real.

*Step 1 (mean).*
- For m > t the indices m−t, m, m+t are distinct positive integers, so they are independent. This gives
  Ec_m = 4p_m − p_{m−t} − p_{m+t} + 2p_{m−t}p_{m+t} + 4i·p_m(p_{m+t} − p_{m−t}).
- Use |p_{m±t} − p_m| ≤ t/(4N) and p ≤ 0.21, together with W(m/N) = 2p_m + 2p_m².
  - The real-part defect is ≤ t/(2N) + 2·(0.42·t/(4N)).
  - The imaginary part is ≤ 0.42·t/N.
  - Hence |Ec_m − W(m/N)| ≤ 1.2t/N.
- For m < −t the same holds by c_{−m} = conj c_m. For |m| ≤ t, |Ec_m| ≤ 5. Also c_m = 0 for |m| > N + t.
- The key point: Σ_m W(m/N) e(mx) = (1/(2N))·|Σ_{j=0}^{N−1} e(jx)|² ≥ 0 (Fejér kernel).
- Hence EΦ(x) ≥ −[1.2t(2N + 2t + 1)/N + 5.5(2t + 1)] ≥ −21t (using t ≤ N/4).

*Step 2 (concentration, uniform in x).*
- Changing one ξ_j changes a_{±j}, hence c_m only for m ∈ {±j, ±j ± t}, by at most 10 each. So |ΔΦ(x)| ≤ 60.
- McDiarmid gives P(|Φ(x) − EΦ(x)| ≥ λ) ≤ 2exp(−2λ²/(3600N)).
- Use the grid x_k = k/J with J = 64N², and λ = 43(N log 8J)^{1/2}. The union bound gives failure probability
  ≤ 2J(8J)^{−1.027} ≤ ¼.
- Off the grid: Φ − EΦ has degree ≤ N + t ≤ 1.25N and coefficients bounded by 10, so its derivative is
  ≤ 20π(N+t)(N+t+1) ≤ 120N². It therefore moves by < 1 within distance 1/(128N²).
- So with probability ≥ ¾: Φ ≥ −21t − λ − 1 = −E_0 = −16K_*² on all of T. This proves (i), since 0 ≤ 1 − cos(·) ≤ 2.

*Step 3 (|B_t|).*
- B_t contains every m ∈ [t+1, N−1] with ξ_m = ξ_{m−t} = 1 and ξ_{m+t} = 0.
- Each such event has probability ≥ 0.79·p_m·p_{m−t} ≥ 0.79·p_m², since π is decreasing.
- Σ_{m≤N−1} p_m² ≥ 0.0429·Σ_k (k/N)² ≥ 0.0143N − 0.03. Hence E|B_t| ≥ 0.0113N − 0.04t − 0.02 ≥ 0.011N.
- Changing one ξ_j changes |B_t| by ≤ 6. McDiarmid then gives P(|B_t| < 0.0055N) ≤ exp(−1.68·10^{−6}N) ≤ ¼ for N ≥ N_0.
- Together with Step 2: with probability ≥ ½ both (i) and |B_t| ≥ 0.0055N hold.

*Step 4 (constants).*
- For N ≥ N_0 and t ≤ N^{1/2}: E_0 ≤ 73(N log N)^{1/2}, so K_*⁴ ≤ 20.8 N log N.
- Also K_*⁴ ≥ N, so log N ≤ 4 log K_*. This gives (ii).
- (iii) follows from K_*² ≥ (43/16)·(N log(512N²))^{1/2} ≥ (43/16)·(35.6N)^{1/2} ≥ 16N^{1/2} ≥ (2N)^{1/2}.

*Step 5 (iv).*
- Let q_m = P(m ∈ B_t), Z := 1̂_{B_t} − E1̂_{B_t} and M := E1̂_{B_t}. The same bounded-difference, grid and Bernstein
  argument (differences ≤ 6, coefficients ≤ 1) gives:
  - ||Z||_∞ ≤ C(N log N)^{1/2};
  - ||Z||_2² = Σ(1_B(m) − q_m)² ≥ 0.79·Σq_m − O((N log N)^{1/2}) ≥ 0.004N;
  - |⟨M, Z⟩| = |Σ q_m(1_B(m) − q_m)| ≤ C(N log N)^{1/2}.
  Each holds with probability ≥ 7/8 for large N.
- For any Q: ||1̂_B − Q||_2 ≥ |⟨1̂_B − Q, Z⟩|/||Z||_2 ≥ (||Z||_2² − |⟨M, Z⟩| − ||Q||_1·||Z||_∞)/||Z||_2.
- If ||Q||_1 ≤ c_1(N/log N)^{1/2}, this is ≥ c_2 N^{1/2}.
- Otherwise K_*²||Q||_1² ≥ c_1²·N^{1/2}(log N)^{1/2}·N/log N ≫ N. ∎

**Remarks.**
- The same sets satisfy the conclusions of other degree-2 or norm-level results with K = K_*. Each check is routine.
  - Roth/Bedert Lemma 4.1: #{(a,b) ∈ A²: a − b ∈ A} ≍ N² ≥ n²/K_*.
  - Ruzsa's AP bound: the longest AP in A has length O(log N) ≤ K_*², with high probability.
  - Lemma 5.5: ||1̂_{B_t}||_1 ≤ |B_t|^{1/2} ≤ K_*³.
  - Shankar's identity Σ_t|B_t| = 6Q − 4I holds for every set.
- What fails is exactly the degree-1 content: F ≥ −K_*, ||F||_1 ≤ 2K_* (here ||F||_1 ≍ K_*²), and the pointwise
  domination |Q_1| ≤ 4G.
- Here n ≍ K_*⁴ (not K_*⁵). The relaxed model therefore saturates Prop 7.3 but says nothing about the final exponent
  1/5.

**NUMERICAL check** (`randrel.py`, exactly this profile, t = 1 and 3):

| N | min f_t∗f_t / (N log N)^{1/2} | \|B_t\|/N | \|B_t\|/K_*⁴ |
|---|---|---|---|
| 2·10³ | −2.9 to −3.1 | 0.019–0.032 | 0.065–0.133 |
| 1.28·10⁵ | −3.4 | 0.026 | 0.050 |

Here K_* = (E/32)^{1/2} with E = −2 min f_t∗f_t. The ratio |B_t|/K_*⁴ decays roughly like 1/log, as predicted. The
proved constants are far from the observed ones.

## 3. Theorem B: no Bedert-type degree-2 inequality beats K⁴  [OBSTRUCTION, PROVED]

**Setting.** An inequality I is given by nonnegative trigonometric polynomials w, m_1, m_1', m_2, m_2' in the variable
tx, of degree ≤ d, with m_i + m_i' ≢ 0. It reads
w·((m_1G + m_1'K) ∗ (m_2G + m_2'K)) ≥ 0 on T.

Every such I holds when F ≥ −K, because then G ≥ 0. Bedert's (37) is the case w = 1, m_i = 2(1 + sin 2πtx),
m_i' = 2(1 − sin 2πtx). Bedert's (38) follows from it.

**Theorem B.** Fix a finite family 𝓘 of such inequalities and fix t. Then there are c, C > 0 and N_1, depending on 𝓘
and t, such that for every N ≥ N_1 some symmetric A ⊂ [−N, N]\{0} satisfies every I ∈ 𝓘 with
K = K_* := C(N log N)^{1/4}, and has |B_t| ≥ cN ≥ c'K_*⁴/log K_*.

**Degree-r analogue (PROVED in sketch).** For r-fold convolutions ∗_{i≤r}(m_iG + m_i'K) the same holds with
K_* ≍ (N log N)^{1/(2r)} and |B_t| ≍ K_*^{2r}/log K_*.

**Proof.**
- *Exact expansion.* Let Λ_i(k) := Σ_j c^{(i)}_j a_{k−jt}, where m_i = Σ_j c^{(i)}_j e(jtx). Use Ĝ(k) = a_k + Kδ_{k0}.
  Then
  (m_1G + m_1'K)∗(m_2G + m_2'K) = Ψ + K·R + K²·μ, where:
  - Ψ(x) = Σ_k Λ_1(k)Λ_2(k)e(kx) is the quadratic pattern sum;
  - R is a trigonometric polynomial in tx built from the a_{jt} with |j| ≤ 2d, so ||R||_∞ ≤ C(𝓘);
  - μ = (m_1 + m_1')∗(m_2 + m_2').
- *μ is strictly positive.* μ(x) = ∫u(y)v(x−y)dy with u, v nonnegative trigonometric polynomials, not ≡ 0. Each has only
  finitely many zeros, so μ ≥ μ_0 > 0. As w ≥ 0, it suffices to show Ψ ≥ −½μ_0K² once K ≥ 2||R||_∞/μ_0.
- *Mean.* For |k| > 2dt:
  E[Λ_1Λ_2](k) = Q_I(p(k)) + O(t/N), where Q_I(p) = p²·m_1(0)m_2(0) + p(1−p)·σ_I.
  Here σ_I = Σ_j c^{(1)}_j c^{(2)}_j = ∫m_1(y)m_2(−y)dy ≥ 0. So Q_I is real and ≥ 0 on [0, 1].
  - Check: for Bedert's inequality Q(p) = 4p² + 2p(1−p) = 2p + 2p². This is exactly the W of Theorem A.
- *A common profile.* Take π = επ_0 with π_0(u) = (1 − |u|)_+·(1 + cos πu)/2.
  - π̂_0(ξ) = ½sinc²(ξ) + ¼(sinc²(ξ − ½) + sinc²(ξ + ½)). This is continuous and positive (the three summands have no
    common zero), and ~1/(2π²ξ²) at infinity. Hence π̂_0 ≥ c_0/(1 + ξ²).
  - π_0² is Lipschitz and piecewise C², with one kink at u = 0. Hence |(π_0²)^(ξ)| ≤ C_0/(1 + ξ²).
  - So Ŵ_I := (Q_I∘π)^ ≥ ε(σ_I·c_0 − ε·C_0·|m_1(0)m_2(0) − σ_I|)/(1 + ξ²) ≥ 0 for every I ∈ 𝓘, once ε is small.
  - Poisson summation then gives Σ_k W_I(k/N)e(kx) = N·Σ_j Ŵ_I(N(j − x)) ≥ 0. Hence EΨ ≥ −C(𝓘)t.
  - For degree r: Q_I(p) = p·(m_1∗…∗m_r)(0) + O(p²), which is real by reflection symmetry and positive. The same choice
    works.
- *Concentration* is as in Theorem A. Each ξ_j affects O(d) coefficients by O(1), giving Ψ ≥ EΨ − C(N log N)^{1/2}
  uniformly in x. Take a union bound over the finitely many I. The bound on |B_t| is as in Theorem A. ∎

**Meaning.** A proof that uses F ≥ −K only through finitely many such degree-2 (or higher) inequalities can never
prove |B_t| ≪ K^{4−δ}. This holds for any test functions, any windows and any multipliers that do not depend on A.

## 4. The degree-1 barrier: audit  [PROVED, statement corrected and extended]

**Statement (correct).** Let 𝔪 ≥ 0 be any trigonometric polynomial on T, not depending on A, with arbitrary frequency
support S = supp 𝔪̂. The coefficient of 𝔪F at frequency m is Λ_m = Σ_{k∈S} 𝔪̂(k)·a_{m−k}. Consider two configurations,
which can coexist far apart in one symmetric set A:
- (i) a point m ∈ B_t with a_{m−k} = 0 for all k ∈ S \ {0, t};
- (ii) an isolated point m' (a_{m'} = 1 and a_{m'−k} = 0 for k ∈ S\{0}).

Then |Im Λ_m| = |Im 𝔪̂(t)| ≤ |𝔪̂(t)| ≤ 𝔪̂(0) = Re Λ_{m'}. So the odd part never strictly beats the even part's
coefficients, and no gap can hold uniformly. The K-terms of 𝔪·(F + K) only touch the finitely many frequencies in S, so
they cannot create a gap on a large B_t. The notebook's version (frequencies in tZ only) is the special case S ⊂ tZ.

**Scope and caveats.**
- (a) 𝔪 must not depend on A. Gram/Roth tests with A-dependent vectors are not covered.
- (b) The witnesses (i) and (ii) must be admissible. In classes where every t-run is long, the argument does not apply.
  There Re Λ_top = (𝔪̂(0) + 𝔪(0))/2 and |Im Λ_top| = |m̃(0)|/2, with m̃ the conjugate function. High-degree multipliers
  with |m̃(0)| > 𝔪̂(0) + 𝔪(0) exist, so a gap is not excluded in such classes (HEURISTIC; I did not check all patterns). But such classes have |B_t| ≤ |A_t|/R. They are not
  the relevant regime: in the heuristic 1/5-extremal configuration, runs have length O(1).
- (c) The barrier says nothing about degree-1 information used *without* a gap. This is exactly what Lemma 7.1 does,
  and exactly what Theorems A and B say must be added.

**Degree-2 complement.** By §3, for every Bedert-type degree-2 inequality the additive term is K²·μ with μ ≥ μ_0 > 0.
This is intrinsic to the algebra. Proposition C shows it is also attained.

## 5. Proposition C: the K² in (37)/(38) is attained by genuine sets  [INTERVAL-CERTIFIED finite cases; HEURISTIC limit]

For a Sidon set D, A = (D − D)\{0} satisfies F = |1̂_D|² − |D| ≥ −|D|, so K ≤ |D| exactly. Values of f_t∗f_t at one
point, as arb balls (`cert_singer.py`, 80-bit precision; the minimiser was located by FFT):

| set | t | x | f_t∗f_t(x) | ratio to \|D\|² |
|---|---|---|---|---|
| Singer q = 31 | 760 | 32744/32768 | −684.15 ± 10^{−16} | −0.668 |
| Singer q = 53 | 2035 | 131037/131072 | −1720.39 ± 10^{−15} | −0.590 |
| Erdős–Turán p = 59 | 3423 | 262111/262144 | −1779.78 ± 10^{−15} | −0.511 |

**NUMERICAL** (`ftft2.py`, float, full t-scan): over Singer q ∈ {13, 23, 31, 41, 53} and ET p ∈ {37, 59},
min_t min_x f_t∗f_t / K² ranges over [−1.07, −0.50]. The worst t has t/X ∈ [0.49, 0.87], and the worst x satisfies
x·X ≈ −0.7 to −0.9 (mod X). The corresponding min r_t reaches about −1.3K².

**HEURISTIC explanation.** Singer differences have triangle profile ρ(u) = (1 − |u|)_+ at scale v = q² + q + 1 ≍ K².
By the §1 identity, the main term at t = τv and x = ξ/v is v·M(τ, ξ), where

M(τ, ξ) = (4 − 2cos 2πτξ)·sinc²ξ + 2∫ρ(w+τ)ρ(w−τ)cos(2πwξ) dw + 8∫ρ(u)ρ(u−τ)sin(2πuξ) du.

Numerically min M = −0.555 at τ = 0.48, ξ = −0.81 (`profile_M.py`). The source is the odd part of the *asymmetric*
profile of A_t when t ≍ X. So (37) and (38) cannot hold with error o(K²) for all t, and Bedert's 16 and 32 are off from
the truth by a constant factor only, about 25 for (38).

**Consequence.** The (38) error *is* testable on known sets, unlike |B_t| ≤ CK², and it is ≍ K². Together with Theorem
A, both the size of E and its use are sharp: (38) with E ≍ K² is consistent with |B_t| ≍ E²/log E.

## 6. What an improvement must prove: Proposition M and Target Lemma S

**Proposition M (PROVED; uses only (38) and Lemma 7.2).** For every t ≠ 0:

|B_t| ≤ 4388·∫_T min(|1̂_{B_t}(x)|, τ)² dx, with τ = 13.46·K·|B_t|^{1/2}.

Combined with Bedert's |B_t| ≤ C_0K⁴ this gives |B_t| ≤ C·∫ min(|1̂_{B_t}|, K³)².

*Proof.* Take Q = 1̂_B·1_{|1̂_B|>τ} in the abstract Prop 7.3.
- Chebyshev: ||Q||_1 ≤ |B|/τ.
- Then |B| ≤ 2193.9·∫_{|1̂_B|≤τ}|1̂_B|² + 90.5·K²|B|²/τ².
- With τ² = 181·K²|B| the last term equals |B|/2. ∎

Conversely, Lemma 7.1 gives |1̂_B| ≤ 4G + |Q_2|. Hence ∫min(|1̂_B|, K³)² ≤ 2K³·4∫G + 2||Q_2||² ≲ K⁴, which is Bedert's
bound. In the random relaxed sets the integral is ≍ |B_t| (Theorem A(iv)). So Proposition M is the exact power of the
method.

**Target Lemma S (the single most promising next lemma; OPEN).** There is δ > 0 such that for all A, K and t ≠ 0 with
F ≥ −K:

∫_T min(|1̂_{B_t}(x)|, K³)² dx ≤ C·K^{4−δ}.

- By Proposition M it implies |B_t| ≪ K^{4−δ}. With Shankar this gives K ≫ n^{1/(5−δ)}; δ = 1 gives exponent 1/4.
- Write the integral as ∫_0^{K³} 2s·meas{|1̂_{B_t}| ≥ s} ds. It then splits into two sufficient parts:
  - **(S1) low heights:** ∫_{|1̂_{B_t}| ≤ K²}|1̂_{B_t}|² ≪ K^{4−δ}. Lemma 7.1 gives only 8K³ + 2||Q_2||_2² ≲ K⁴.
  - **(S2) large values in the middle range:** meas{x : |1̂_{B_t}(x)| ≥ s} ≪ K^{1−δ}/s for K² ≤ s ≤ K³. Lemma 7.1 gives
    only 8K/s + 4||Q_2||²/s², i.e. "1̂_{B_t} has the distribution function of G".
- Why this is the right target:
  - (1) It is necessary and sufficient for the Prop 7.3 method.
  - (2) It fails for the Theorem A sets. Any proof must therefore use F ≥ −K at degree 1 (pointwise, through
    ||F||_1 ≤ 2K, or through the domination |1̂_{B_t}| ≤ 4G + |Q_2| used beyond its norms), consistent with Theorems A
    and B.
  - (3) It holds trivially in every known genuine family, where |B_t| ≲ K².
  - (4) Its quantities are intrinsic to B_t and do not involve the multiplier gymnastics of Lemma 7.2.
- The heuristic 1/5-extremal configuration of bedert_avg.md §3 has |1̂_{B_t}| ≈ G ≈ K³ on measure K^{−2}. It violates
  (S2) at s = K³ by exactly the factor K^δ. Excluding this configuration *is* Lemma S.

## 7. Group setting  [PROVED remarks; main question OPEN]

- **Prop 7.3 is group-agnostic.** Lemma 7.1, (37), (38) and the test argument are Fourier analysis on a compact dual;
  only G ≥ 0, ∫G = K and idempotence are used. In Lemma 7.2 the positions m + jt (|j| ≤ 2) may coincide when ord t ≤ 4.
  That only restricts patterns, so the table maxima still hold. B_t-patterns need 2t ≠ 0; otherwise B_t = ∅. Hence
  |B_t| ≤ C_0K⁴ holds in every finite abelian group.
- **Transfer to Z.** Embed A ⊂ [−X, X] into Z_N with N > 4X + 4|t|. Then F on Z_N consists of samples of F on T, so
  F ≥ −K is preserved, and B_t is unchanged. So any bound valid in all Z_N transfers to Z. Conversely, a finite-group
  example with |B_t| ≫ K^{4−δ} would force an improvement to use torsion-freeness.
- **Evidence that groups behave like K² (PROVED for the stated classes).**
  - (a) A ∪ {0} = ∪_{i≤r} H_i with H_i ∩ H_j = {0}: F = Σ_i |H_i|·1_{H_i^⊥} − r. If the H_i^⊥ do not cover the dual,
    then K = r. Also |B_t| ≤ r(r−1) + 1: if m and m − t lie in the same H_i then m = −t; otherwise m ∈ H_i ∩ (H_j + t),
    which has at most one point. So |B_t| ≤ K² + 1.
  - (b) In F_3^d, take U = V ∪ S with V a hyperplane and S = ±(w + R), R ⊂ V. Then F ≥ −K forces
    max_{ξ≠0}|1̂_R(ξ)| ≲ K. Taking t ∈ V, |B_t| counts t-lines meeting R in exactly 2 points, which is ≤ 3·min(|R|, |V\R|).
    Parseval gives K² ≳ min(|R|, |V\R|)/2, so |B_t| ≲ K².
  - (c) Paley/QR sets in F_q: |B_t| ≈ q/8 ≈ K²/2 (HEURISTIC, by Weil).
  - (d) Exhaustive search over all symmetric A ⊂ Z_N, N ≤ 30 (`zn_runs2.py`): subgroups give |B_t| ≤ 1 at K ≤ 1.5;
    max |B_t|/K² ≤ 0.9 for K ≥ 1.5. This is NUMERICAL and uninformative about exponents.
- **OPEN question.** Is |B_t| ≤ C·K^{2+o(1)}, or even C·K^{4−δ}, in every finite abelian group?
  - A proof valid in all Z_N would settle the Z case.
  - A counterexample would show that Lemma S must use torsion-freeness.
  - This is cheaper to probe than Z: structure theory (Green–Sanders) applies, and Chowla itself fails there.

## 8. A small degree-1 by-product  [PROVED, elementary; likely folklore]

**Fibre domination.** Fix t ≥ 1. For a residue r mod t let S_r = {s : r + st ∈ A}. Then for all θ ∈ T and r ≢ 0:

|1̂_{S_r}(θ)| ≤ K + 1̂_{S_0}(θ).

*Proof.* (1̂_{S_r}(θ)·e(rθ/t))_r is the inverse DFT of the nonnegative vector (F + K)((θ + j)/t), j = 0..t−1. For
r ≠ 0, a Fourier coefficient of a nonnegative vector is bounded by its mean. ∎

**Corollaries.**
- Each class r mod t contains at most K² + |A ∩ tZ| elements of A.
- It carries at most ∫(K + 1̂_{S_0})²(1 − cos 2πθ) dθ = K² + ρ_0 − 2K·1_A(t) maximal t-runs, where ρ_0 is the number of
  t-runs of A ∩ tZ.

This degree-1 fact is violated by the Theorem A sets. Summed over the t classes it gives nothing better than |B_t| ≤ n.
I record it as a possible ingredient for Lemma S, not as progress.

## 9. Refuted, closed or weakened statements (preserve)
- "The K² error in (38) might be o(K²) on genuine sets" (my own conjecture E during this session) is **FALSE**. Singer
  and ET sets give f_t∗f_t ≤ −0.5K² for t ≍ X (§5).
- "A better test function H in Prop 7.3 could give K³" is **closed**. No Q helps on the Theorem A sets (Theorem A(iv)).
  Any gain must change the inputs.
- "More degree-2 inequalities (other multipliers or windows) could give K^{4−δ}" is **closed** for every finite family
  of A-independent Bedert-type inequalities (Theorem B).

## 10. Next concrete steps
1. Attack (S1)/(S2) of Lemma S on the extremal configuration. The degree-1 input to test first: on Ω = {|1̂_{B_t}| ≈ G ≈ K³}
   (measure ≈ K^{−2}), idempotence 1̂_B = 1̂_B∗1̂_B forces the convolution over Ω∩(x−Ω) to be phase-coherent and
   saturating. Meanwhile G∗G ≤ G + K² forces 1_Ω∗1_Ω ≲ K^{−3} on Ω. Determine whether these two constraints are
   compatible once the Q_2-error is controlled.
2. Decide the group question of §7 on F_3^d or Z_m^d. This is a structured search for large |B_t| at fixed K among
   ±-combinations of a few cosets. It is a small, discriminating computation.
