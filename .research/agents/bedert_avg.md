# Agent note: can Bedert's boundary bound be averaged over t ∈ A?  (2026-10-18)

Question.  A = −A ⊂ Z\{0}, n = |A|, F := 1̂_A ≥ −K on T = R/Z.  A_t = A∩(A+t), B_t = A_t \ (−A_t).
Is Σ_{t∈A} |B_t| ≪ n K^3 provable?  With Shankar's Σ_{t∈A}|B_t| ≥ T/3 ≥ n^2/(6K) (n ≥ 2K^2) this would give K ≫ n^{1/4}.

**Short answer.** Not by averaging Bedert's chain as it stands. What I found:
1. **[PROVED]** The proof of Prop 7.3 really shows a statement for an arbitrary function Q (§2). A localisation lemma follows from it (§3): every B_t keeps a fixed fraction of its Fourier L²-mass on the sublevel set {F < 181K³}.
2. **[PROVED]** After localisation, source (a) becomes a single number that does not depend on t: L(A) := ∫_{F<181K³}(F+K)² ≤ 182K⁴. Averaging over t therefore cannot improve (a). Any improvement past exponent 1/5 must either prove L(A) ≪ K^{4−δ} (no "middle layer" in the height distribution of F), or show that the B_t cannot all saturate the domination |Q_{1,t}| ≤ 4(F+K) on a common layer.
3. **[PROVED]** For (b): every multilinear piece of Q_2 that contains at least one factor T2 = min(F,0) has Σ_{t∈Z} ||·||_2² ≤ C(n+K⁴)K², i.e. O(K²) per t. This confirms and extends the lead's remark. The truncation remainders, which are pure in T1 = max(F,0) and nonlinear in t, are **not** covered (§4).
4. **[NUMERICAL]** On every family with K ≍ √n (Singer and Erdős–Turán Sidon differences, Bu sets, dense near-interval sets), Bedert's Q_{1,t} has ||Q_{1,t}||_1 ≈ 0.25K on average. So avg_t ||Q_{1,t}||_1² ≈ 0.06K², which grows like K² and not K. The same holds for ||1̂_{B_t}||_1² ≈ 0.13K² on Sidon differences. The lead's √K heuristic was wrong (§5).

## 0. Sources and checks
- Bedert, arXiv:2509.05260 **v3** (24 Jul 2026). §5 gives (4)–(7), Lemma 5.1 (‖f_t‖_min ≤ 4K) and Lemma 5.5. §7 (pp. 14–19) gives Lemma 7.1 (p. 14–15), (36)–(41), Lemma 7.2 (pp. 16–17), Prop 7.3 with (42)–(43) (pp. 18–19), and Lemma 7.4.
- Shankar, arXiv:2609.05338 **v1** (4 Sep 2026): Prop 2.1 (Roth: E ⊆ A, |E| ≥ 2K² ⇒ #{(u,v)∈E²: u−v∈A} ≥ |E|²/(2K)), Prop 2.2 (= Bedert Prop 7.3), Lemma 3.1 (Σ_{t∈A}|B_t| = 6Q−4I ≥ T/3, T = 6Q), and Thm 4.1. Remark 5 in his paper says that improving 1/5 by this route needs either a better exponent than K⁴ or "many boundary sets simultaneously large".
- Checks I ran (exact or float):
  - Lemma 7.2's table, by brute force over all 32 patterns (a_{m−2t},…,a_{m+2t}): max Re ρ = 4+1/√2, max |Im ρ| = 4+2√2, min_{m∈B}(−Im ρ_m) = 4+√2, all exact.
  - Shankar's identity on ET p=11: Σ_{t∈A}|B_t| = 2918 = 6Q−4I and T = 6Q = 3870.
  - The identity (§6) for f_t∗f_t, to float precision 4e−10.

## 1. The exact v3 chain (Prop 7.3), with constants
Notation: T1 = max(F,0) (τ = T̂1), T2 = min(F,0) (σ = T̂2), κ = ∫T1 = −∫T2 ≤ K, ||T2||_∞ ≤ K, ||T2||_2² ≤ K², ||T1||_2² ≤ n.
- **Lemma 5.1.** f_t = 2(1+sin 2πtx)F ≥ −4K and ∫f_t = 0. Then (37): f_t∗f_t + 16K² = (f_t+4K)∗(f_t+4K) ≥ 0.
- **Definitions.** r_t = (1−cos(2πtx+π/4))(f_t∗f_t) ≥ −32K². ψ_t and φ_t are its even and odd parts. (38): |φ_t| ≤ ψ_t + 32K².
- **Lemma 7.2.** ψ̂_t(m) ≤ α := 4+1/√2 and |φ̂_t(m)| ≤ γ := 4+2√2 for all m; −Im ρ_m ≥ β := 4+√2 for m ∈ B_t.
- **Lemma 7.1 (with L = K).** 1̂_{B_t} = Q1 + Q2 with |Q1| ≤ 4(F+K), so ||Q1||_1 ≤ 4K. Q2 is a sum of pieces each with ||·||_∞ ≪ K²:
  - V, V⁻: the truncation remainders of T1∗(e_{±t}T1), where |T1∗(e_tT1)| ≤ T1∗T1 ≤ (F+K)∗(F+K) = F+K².
  - The bilinear cross terms T1∗(e_{±t}T2), T2∗(e_{±t}T1), T2∗(e_{±t}T2).
  - v: the remainder of truncating U∗(e_{−t}T1).
  - U∗(e_{−t}T2), with ||·||_∞ ≤ ||U||_1||T2||_∞ ≤ K².
  - R'_2∗1̂_{A−t}, an L² contraction of the above.
  - The analogous pieces of the odd part F∗((e_t−e_{−t})F).
- **Prop 7.3.** Symmetrise so that Q1(−x) = conj Q1(x), and put H = |Q1|. Then
  - X := ∫(ψ_t+32K²)(H∗H) ≤ α||Q1||_2² + 32K²||Q1||_1²  (43)
  - X ≥ |∫φ_t (Q1∗Q1)| ≥ β|B| − 2γ|B|^{1/2}||Q2||_2 − γ||Q2||_2²
  - ||Q1||_2 ≤ |B|^{1/2} + ||Q2||_2  (42)
- **Where K⁴ appears.** (a) 32K²||Q1||_1² ≤ 512K⁴. (b) ||Q2||_2² ≤ ||Q2||_∞² ≪ K⁴. The cross term K²|B|^{1/2} is harmless. The lead's bookkeeping is correct.

## 2. Abstract Prop 7.3  [PROVED, from (38) + Lemma 7.2 only]
Lemma 7.1 is used only to supply Q. The argument works for **every** Q ∈ L²(T). Symmetrising Q never increases either norm.

> For all t ≠ 0 and all Q ∈ L²(T):  |B_t|^{1/2} ≤ 33.12·||1̂_{B_t} − Q||_2 + 6.727·K·||Q||_1,
> hence |B_t| ≤ 2193.9·||1̂_{B_t}−Q||_2² + 90.5·K²||Q||_1².

Derivation: with b = |B|^{1/2} and r = ||1̂_B − Q||_2,
(β−α)b² ≤ 2(α+γ)br + (α+γ)r² + 32K²||Q||_1², where β−α = 1/√2 and α+γ = 11.536. Solve the quadratic in b.

So the method's output is the K-functional Φ_t = inf_Q (r² + K²||Q||_1²), and Φ_t ≤ |B_t| ≤ 2194·Φ_t'. The prime denotes the same infimum with weights 2194 and 90.5.
- Numerically |B_t|/Φ_t ∈ [1.01, 1.13] on all families (table below). The optimal Q is essentially 0, so the method is far from binding on known sets.
- Consequence: an averaged bound on Σ_tΦ_t is *equivalent* to the averaged bound on Σ|B_t|. Nothing is gained for free; one must exhibit better decompositions.

## 3. Localisation lemma and refined Prop 7.3  [PROVED]
**Lemma X.** Take Q = 1̂_{B_t}·1_{F≥λ}. By Cauchy–Schwarz with weight F+K (which has integral K), ||Q||_1² ≤ K|B_t|/(λ+K). With λ = 181K³ this gives:

> |B_t| ≤ 4388 · ∫_{F(x) < 181K³} |1̂_{B_t}(x)|² dx   for every t ≠ 0.

**Refined Prop 7.3.** Combine Lemma X with Lemma 7.1, using |Q1| ≤ 4(F+K):

> |B_t| ≤ 140 416 · L(A) + 8 776 · ||Q_{2,t}||_2²,   where L(A) := ∫_{F<181K³} (F+K)² dx ≤ 182 K⁴.

Averaging with Shankar (n ≥ 2K²):

> n/(6K) ≤ 140 416 · L(A) + 8 776 · (1/n) Σ_{t∈A} ||Q_{2,t}||_2².   (★)

Reading of (★):
- **Source (a) is now t-independent.** It equals L(A), the L²-mass of F+K below height 181K³. Averaging over t does nothing to it.
- If (b) were averaged to ≪ K³, then (★) gives n ≪ K·L(A) + K⁴. Exponent 1/4 then requires **L(A) ≪ K³**: F+K must carry o(1) L¹-mass at heights ≍ K³ and o(K) at heights ≍ K², etc.
- A sharper sufficient condition (route ii) keeps the t-sum before using domination:
  ∫_{F<181K³} Σ_{t∈A}|Q_{1,t}(x)|² dx ≪ nK³, versus the trivial 16n·L(A).
  This says the B_t do not all saturate |Q_{1,t}| ≈ F+K at the same points.

**Extremal configuration for the exponent 1/5** [HEURISTIC; every inequality above is tight in it, up to constants]. F+K has two layers:
- a top layer at heights ≳ n/K carrying ∫F² = n;
- a middle layer at height ≍ K³ on measure ≍ K^{−2}, carrying L¹-mass ≍ K, so L(A) ≍ K⁴.
Every B_t (t ∈ A) puts its Fourier mass on the middle layer with |1̂_{B_t}| ≍ F+K. Then |B_t| ≍ K⁴ and Σ_B ≍ nK⁴ ≍ n²/K when n ≍ K⁵.
Contrast: if F+K had a single layer at some height H ≤ CK³, then n ≈ HK ≲ K⁴ automatically.
To beat 1/5 one must exclude the middle layer, or exclude simultaneous saturation on it.

## 4. Averaging of (b)
**[PROVED] Bilinear terms.** By Parseval in t (τ and σ are real and even):
- Σ_{t∈Z}||T1∗(e_tT2)||_2² = ||T1||_2²||T2||_2² ≤ nK²
- Σ_{t∈Z}||T2∗(e_tT1)||_2² ≤ nK²
- Σ_{t∈Z}||T2∗(e_tT2)||_2² ≤ K⁴

Since 1̂_{B_t} = Π_t(1̂_{A_t}), where Π_t is the 0/1 multiplier (1−a_{m+t}), this gives:

> 1̂_{B_t} = Π_t(T1∗(e_tT1)) + Err_t,   Σ_{t∈Z} ||Err_t||_2² ≤ 3(2nK² + K⁴).

**[PROVED] Trilinear terms with at least one T2.** For example,
Σ_tΣ_m τ_m²τ_{m−t}²σ_{m+t}² = Σ_m τ_m²(τ²∗σ²)(2m) ≤ ||τ||_4⁴||σ||_2² ≤ 8(n+K⁴)K²,
using ||τ||_4⁴ ≤ 8n + 8Σσ⁴ ≤ 8n + 8K⁴. The other positions are the same.

**[NOT averaged]** These pieces are not handled by Parseval in t:
- the truncation remainders V_t, V_t⁻, v_t and T1∗S'_1 − S1, which are pure in T1 and nonlinear in t;
- U_t∗(e_{−t}T2) = G_t∗(e_{−t}T2) − V_t∗(e_{−t}T2). The first part is averaged. The second is ≤ K||V_t||_2, so it needs Σ_t||V_t||² ≪ nK.

If the truncation is done at 2(F+K) instead of F+K (constants only), the remainders are supported on {F+K < K²}. Split T1 = T1^lo + T1^hi at level M ≍ K², and use the bound below for the terms containing T1^lo. Then averaging the remainders reduces to:

> (S')  ∫_{F<K²} ((T1^hi)² ∗ (T1^hi)²)(x) dx ≪ nK³.

This is an approximate additive-closure statement for the high spectrum {F > K²}. It holds automatically at the top (near-periods of A are approximately closed under addition, by positive-definiteness of F). It is unknown at intermediate heights. **OPEN.**

The low-factor terms satisfy Σ_{t∈Z}||T1^lo∗(e_tT1)||_2² ≤ ||T1^lo||_2²·n ≤ MKn = O(nK³).

Numerically the remainders are negligible: avg ||V_t||² ≈ 0.003K² on all families.

## 5. Numerical table  [NUMERICAL, UNCERTIFIED floats; FFT grid N ≥ 8–16·2maxA]
Code: src/agents/bedert_avg.py, src/agents/bedert_avg_run.py; raw output in src/agents/bedert_avg_results.json.
- Lemma 7.1 is reproduced literally (truncations at F+K and 2(F+K)). I checked |Q1| ≤ 3(F+K) pointwise; the violation is ≤ 4e−15.
- Up to 240 sampled t > 0 per family; B_{−t} = −B_t covers negative t.
- Φ is the exact pointwise K-functional (soft thresholding).
- CS_a = ∫Σ_t|Q_{1,t}|²/(F+K) / n is the Cauchy–Schwarz route for (a): Σ_t ℓ_t² ≤ K·n·CS_a. It is tight within a factor ≈ 1.6.
- ell = ||Q_{1,t}||_1 and q2 = ||Q_{2,t}||_2².

| family | n | K | avg\|B_t\|/K² | avg‖1̂_{B_t}‖₁²/K | avg ell/K | avg ell²/K | avg q2/K² | max‖Q2‖∞/K² | avg cross/K² | avg Vrem/K² | avg\|B\|/Φ | CS_a |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ET-Sidon-diff p=11 | 110 | 11.0 | 0.219 | 1.60 | 0.257 | 0.74 | 0.119 | 0.114 | 0.189 | 0.003 | 1.07 | 1.03 |
| ET-Sidon-diff p=23 | 506 | 23.0 | 0.233 | 3.23 | 0.258 | 1.55 | 0.113 | 0.083 | 0.179 | 0.005 | 1.08 | 2.26 |
| ET-Sidon-diff p=37 | 1332 | 37.0 | 0.212 | 4.85 | 0.262 | 2.55 | 0.106 | 0.057 | 0.176 | 0.006 | 1.06 | 3.75 |
| Singer-diff q=13 | 182 | 14.0 | 0.258 | 2.16 | 0.251 | 0.89 | 0.103 | 0.109 | 0.162 | 0.002 | 1.11 | 1.29 |
| Singer-diff q=23 | 552 | 24.0 | 0.258 | 3.49 | 0.249 | 1.49 | 0.097 | 0.073 | 0.153 | 0.003 | 1.11 | 2.20 |
| Singer-diff q=31 | 992 | 32.0 | 0.257 | 4.53 | 0.243 | 1.90 | 0.094 | 0.063 | 0.148 | 0.004 | 1.11 | 2.83 |
| Bu 61_12 | 264 | 19.0 | 0.117 | 1.24 | 0.270 | 1.39 | 0.075 | 0.064 | 0.128 | 0.000 | 1.03 | 1.69 |
| Bu 101_20 | 760 | 29.8 | 0.094 | 1.62 | 0.277 | 2.30 | 0.078 | 0.042 | 0.143 | 0.002 | 1.02 | 3.10 |
| dense X120_s0 | 146 | 11.5 | 0.305 | 2.08 | 0.251 | 0.73 | 0.131 | 0.129 | 0.206 | 0.004 | 1.13 | 1.06 |
| dense X180_s1 | 226 | 15.9 | 0.245 | 2.37 | 0.234 | 0.88 | 0.109 | 0.104 | 0.174 | 0.003 | 1.11 | 1.22 |
| dense X260_s0 | 300 | 18.3 | 0.244 | 2.67 | 0.233 | 1.01 | 0.108 | 0.092 | 0.174 | 0.003 | 1.11 | 1.42 |
| interval [1,100] | 200 | 44.7 | 0.025 | 0.18 | 0.026 | 0.03 | 0.008 | 0.022 | 0.009 | 0.000 | 1.02 | 0.33 |
| interval [1,400] | 800 | 174.9 | 0.007 | 0.07 | 0.009 | 0.01 | 0.002 | 0.006 | 0.002 | 0.000 | 1.01 | 0.35 |
| Singer31 diff, random p=1/2 | 516 | 55.2 | 0.033 | 1.22 | 0.099 | 0.55 | 0.023 | 0.013 | 0.034 | 0.000 | 1.02 | 0.70 |
| Singer31 diff, random p=1/4 | 232 | 45.8 | 0.012 | 0.37 | 0.075 | 0.26 | 0.012 | 0.010 | 0.017 | 0.000 | 1.01 | 0.31 |
| random dens 1/2 in [1,300] | 290 | 58.6 | 0.020 | 0.77 | 0.065 | 0.25 | 0.013 | 0.009 | 0.019 | 0.000 | 1.02 | 0.37 |

Findings:
- **(a) does not average on any √n-family.**
  - avg ||Q_{1,t}||_1 ≈ (0.23–0.28)K, essentially the same in every family.
  - avg ℓ²/K grows linearly in K: Singer 0.89 → 1.49 → 1.90, ET 0.74 → 1.55 → 2.55.
  - So "Σ_{t∈A}||Q_{1,t}||_1² ≪ nK^{2−δ}" is **FALSE** unconditionally. So is "Σ||1̂_{B_t}||_1² ≪ nK^{2−δ}" (≈ 0.13nK² on Sidon differences).
  - These families are the requested adversarial examples: the averaged (a)-quantity has the same K-scaling (K² per t) as the pointwise bound.
- **Correction to the lead's heuristic.** Singer and ET difference sets D−D are dense, with density ≈ 1/2 or 1/4 in (−v, v).
  - T ≈ 0.5n², so |A_t| ≈ n/2 on average, not ≈ 2|D|.
  - B_t is a random-like set of size ≈ n/4 ≈ 0.25K². Hence ||1̂_{B_t}||_1 ≈ 0.36K, not √K.
- **The data still allow the weaker averaged inequality** Σ_t ℓ_t² ≤ C(nK + K⁴), with C ≈ 0.05–0.07 fitted (Singer q=31: 0.056, ET p=37: 0.065, Bu 101_20: 0.064, dense X260: 0.047). Together with averaged (b) this would suffice for K ≫ n^{1/4}. Since n ≍ K² here, the data cannot discriminate.
  - Any true averaged lemma must carry an additive term ≳ K⁴, i.e. it must use n ≫ K³ (spikiness of F).
- **(b).** avg ||Q2||² ≈ 0.1K², consistent with the proved O(K²) averaging of the cross terms. ||Q2||_∞ ≈ 0.04–0.13K², so the per-t L^∞ scaling K² is real but Q2 is spiky.
- **Energy profile.** (src/agents/bedert_avg_profile.py, bedert_avg_profile.log)
  - E_B(x) = Σ_t|1̂_{B_t}(x)|² is ≈ flat in x on Sidon and dense families (log-slope vs F+K ≈ 0.1). It is ∝ (F+K) on Bu sets (slope ≈ 0.95).
  - Saturation s = E_B/(n(F+K)²) ≈ 0.1–0.25 at typical heights F+K ≈ K. So the domination is saturated up to constants at typical points even in known sets. In those sets F ≤ n ≲ K², so the sublevel set in Lemma X is all of T and Lemma X is vacuous for them.

## 6. Failed or limited levers (preserved)
- **Parseval in t for the pure-T1 term.** Σ_{t∈Z}|T1∗(e_tT1)(x)|² = (T1²∗T1²)(x), with total mass ≈ n². Restricting to t ∈ A gains at most a factor 2K (since T ≥ n²/(2K)). Needed in the regime n ≍ K⁴: a K³/n fraction on the low region, i.e. condition (S').
- **Minkowski for L¹ norms.** (Σ_t||G_t||_1²)^{1/2} ≤ ∫(T1²∗T1²)^{1/2} ≤ n. This gives avg ℓ² ≤ n, which is useless.
- **Averaged test functions.** (38) is linear in the test function, so Σ_t of per-t tests gives exactly Σ_t of per-t bounds. §2 shows the output is Σ_tΦ_t ≍ Σ|B_t|.
- **Improving the constant 16K² in f_t∗f_t ≥ −16K².** The exact identity [verified numerically] is
  f_t∗f_t = (4 − 2cos 2πtx)F + 2·1̂_{E_t} + 8·Im 1̂_{B_t},  E_t = (A+t)∩(A−t),  |E_t| = |A_{2t}|.
  - On Singer q=23, min_x f_t∗f_t ≈ −(13–16)K, not −K².
  - A universal bound min f_t∗f_t ≥ −K^{2−δ} would give |B_t| ≪ K^{4−δ} per t with no averaging. But it needs lower bounds on 2·1̂_{E_t} + 8 Im 1̂_{B_t}, which is circular.
  - Exploiting f_t+4K = 2(1+s)(F+K) + 2K(1−s) (with s = sin 2πtx) and (F+K)∗(F+K) = F+K² ≥ K²−K only improves the constant: f_t∗f_t ≥ −10K² − 8K.
- **The odd part alone** (bilinear, 1̂_B − 1̂_{−B} = F∗((e_t−e_{−t})F)) cannot replace 1̂_B in the lower bound: ∫φ_t(J∗J) = 0 for odd J. So the trilinear triple-intersection term is unavoidable in this method.

## 7. Precise next steps
1. Prove or refute **L(A) = ∫_{F<CK³}(F+K)² ≪ K^{4−δ}** for sets with F ≥ −K and n ≥ K⁴. This is a statement about the distribution of F alone, with no t involved.
   - Levers: Chang-type structure of the spectrum {F ≥ s} for s ≥ K (dimension ≲ K² log); positive-definiteness of F; the moments ∫F³ = T and ∫F⁴ = E(A).
2. Or prove **non-saturation**: ∫_{F<CK³} Σ_{t∈A}|Q_{1,t}|² ≪ nK³. Note Σ_t|1̂_{A_t}(x)|² = ⟨g_x, F∗g_x⟩ exactly, with g_x(z) = F(z)F(x−z). This is a 5-linear form; the needed bound is on its restriction to the sublevel set.
3. Prove (S') or find a decomposition that avoids pure-T1 truncation remainders, so that (b) averages to O(K³).
4. Falsification of 1–3 needs examples with F much spikier than in any known family (n/K² ≫ 1). None exist, so this has to be done theoretically, e.g. via weighted/measure relaxations, or a finite model with an ordering in which Chowla-type bounds fail. In Z_N, Prop 7.3 holds but Shankar's identity fails (A = H^⊥\{0}: K = 1, |B_t| = 1).
