# λ-fold rulers, λ = 3 (and 4): exact optima, families, obstructions — agent report (2026-10-18)

Brief: `.research/agents/lambda_brief.md`. Scratch code and raw outputs: `.research/agents/lambda_scratch/`
(`out/` holds every raw output quoted below). All computation ran on dirichlet via `src/dirun.sh -c 4` (C compiled
on the VM). Status labels: PROVED / NUMERICAL-EXACT (exhaustive or solver-certified) / NUMERICAL (heuristic) /
CONJECTURED / FAILED / HEURISTIC.

Notation as in the brief. D ⊂ Z, |D| = k, r(d) = #{(u,v) ∈ D²: u − v = d}, A = {d > 0: r(d) = λ}, Δ = defect classes,
**def = Σ_{d∈Δ} r(d)** (defect pairs), **W = 2·def**, φ = λ|A|/C(k,2) = 1 − def/C(k,2). Naive bound
R(A) ≤ (k+W)/(2λ√|A|); for λ = 3 it is < 1/2 only if W < 0.2247k (with φ → 1).

## 0. Summary

| item | result | status |
|---|---|---|
| exact optima λ = 3 | k = 4..12 (spans L up to 40–60); k = 13, 14 within certified span ranges (see §1). **min W/k ∈ [1, 2] for every k ≤ 12; W ≥ k for all 4 ≤ k ≤ 12**; k = 13: W/k = 2.31 (L ≤ 46); k = 14: 3.14 for L ≤ 38, and 2.71 found at L = 52 | NUMERICAL-EXACT (k = 14 at L = 52: tabu) |
| Conjecture C-W | λ = 3: W ≥ k for every k ≥ 4, tight at k = 6 (§6) | CONJECTURED |
| exact optima λ = 4 | k = 4..11 (L ≤ 36–40); W/k ∈ [2, 3] | NUMERICAL-EXACT |
| E35 comparison | E35's SA was slightly suboptimal at k = 12 (0.773 vs exact 0.818) and badly search-limited for k ≥ 18 (k = 30: 0.57 vs 0.835 here); "φ decreases with k" is an artefact | NUMERICAL |
| best φ, large k | product family D = {0,1,2} + 3B (B Sidon): **φ = 0.80–0.85 for k = 18…216**, with W ≈ k²/6 | PROVED formula + NUMERICAL-EXACT values |
| target "φ ≤ 2/3 + o(1)" | refuted for all k ≤ 216 (explicit sets); heuristic limit of the family 7/9 | FAILED (as a hoped-for theorem) |
| boundary bound | W ≥ 6 for λ ≥ 3, k ≥ 3, tight at k = 3, 4, 6 | PROVED |
| symmetric sets, odd λ | φ ≤ λ/(k−1) for every reflection-symmetric D | PROVED |
| homometric triples / separated blocks | T5: an isolated cross family between Sidon blocks has more than a (1 − 2/λ) fraction of defect pairs; separated homometric triples have W ≥ (2/27)k² | PROVED |
| product family, general | D = A + N·B: λ-fold off-diagonal classes need A cyclic (N,a,λ) d.s.; aligned classes need A = interval | PROVED |
| mod-p route (W ≥ #{d: p∤r(d)} ≥ k?) | FALSE: #{d≠0: 2∤r(d)} = 2 at k = 7, 10, 11; #{d≠0: 3∤r(d)} = 8 at k = 9, 10, 11 | FAILED (exhaustive counterexamples) |
| cyclic lifts (all multipliers, shifts) | (15,7,3): φ ≤ 0.571; (40,13,4): 0.564; (156,31,6): 0.452; (19,9,4): 0.444; (101,25,6): 0.36 | NUMERICAL-EXACT (complete over (m,c)) |
| actual R(A) of all candidates | **min R = 0.680** (k = 10); every candidate ≥ 0.68; product family 1.36–1.71 | NUMERICAL (FFT + Newton, uncertified) |
| anatomy | "ideal" R if E vanished on the near-zero set of F_D: 0.45–0.50 for every candidate; the actual minimiser sits where E ≈ 0.4–0.9k and \|F_D\|² is moderately small | NUMERICAL |
| λ-dependence | λ = 2 (tabu): W = k exactly, φ → 1, symmetric optima (Bu). λ = 3–8: W/k grows with k and λ (2.4–9.6), φ = 0.6–0.8 | NUMERICAL (heuristic) |
| even-λ symmetric route (λ = 4, 6) | D = H ∪ (c−H): only the fixed classes c − 2h are harmless (Bu type). Non-harmless W'/k = 3.6 → 7.0 (λ = 4, k = 10 → 30), 5.2 → 9.9 (λ = 6); actual R 0.91–2.5 | FAILED (numerical) |
| signed multisets (extension) | at the unsigned-optimal \|A\| signs never lower min W (exhaustive, k ≤ 10, λ = 3, 4). They cut W_s by 3–4× only by shrinking \|A\|. Best naive Rn 0.943, best actual R 0.692 (λ = 3, k = 10, one negative) | NUMERICAL-EXACT (small k) / NUMERICAL |
| calibration | Reflection-symmetric λ = 2 sets with **zero** non-harmless defects have actual R = 0.69–0.96 at k ≤ 30. This is the class of Bu's construction, whose R → 1/2 is claimed by Bu et al. and analysed in P16; the tabu sets were not optimised for R. So small-k R does not separate the mechanisms; W' does | NUMERICAL |

Bottom line for the route.
- No near-3-fold ruler with W = O(εk) exists for k ≤ 12: the exact minimum is W_min ≥ k, and W_min/k rises to 2.31 at
  k = 13 (exact within span ≤ 46) and to ≤ 2.71 at k = 14.
- The best known large-k constructions have W ≍ k² (φ ≈ 0.8, not → 1).
- Neither signs nor even λ with reflection symmetry supplies the missing "harmless defects": only λ = 2 has them, via
  the involution x ↦ c − x.
- No candidate has R(A) < 0.68. This last point is weak evidence by itself, because reflection-symmetric λ = 2 sets with zero
  non-harmless defects are equally bad at these sizes.
- Nothing found supports the λ ≥ 3 route to R < 1/2, but no theorem beyond W ≥ 6 rules it out asymptotically.

## 1. Exact optima

### Method (two independent exact methods + one heuristic)
- `bb_lambda.c`: DFS over interior points in increasing order, span exactly L (0, L ∈ D), symmetry D ↔ L − D broken
  by x₂ ≤ L − x_{k−1} (which also caps every interior point at L − x₂). Lower bound on the final def at a node with m
  points still to place in (x_c, L), each part valid:
  (i) over-full weight Σ_{r_S(d) > λ} r_S(d) (r only grows);
  (ii) dead deficient classes: a class with 0 < r_S(d) < λ whose capacity (pairs with a new larger end:
       ≤ min(m, #{u ∈ S∖{L}: x_c < u+d < L} + [d ≤ L−x_c−2](m−1)), plus ≤ 1 pair (L, y) if d ≤ L−x_c−1) is below
       λ − r_S(d) keeps all its r_S(d) pairs defective;
  (iii) fractional knapsack: the Q = C(m,2) + m|S| new pairs can complete at most the cheapest deficient classes;
  (iv) def ≡ C(k,2) (mod λ) (since def = C(k,2) − λ|A|), so the bound is rounded up to that residue class.
  Optional "full-hit" bound (pairs of future points landing in classes with r ≥ λ) — valid but gave only ~13 % fewer
  nodes. Search is complete; printed values are exact for span exactly L.
- Cross-checks: CP-SAT (OR-tools 9.15, `cpsat_lambda.py`, status OPTIMAL) agrees at (λ,k,L) = (3,10,15), (3,10,20),
  (3,10,24) (def 18, 15, 9). The tabu search `tabu_lambda.c` (heuristic) re-finds every exact optimum for
  k = 10, 11, 12 (λ = 3) and k = 11 (λ = 4) from random starts in < 1 s; E35's SA values never exceed the exact ones.
- Drivers: `driver.py` (per-L, either full or "UB = running best + slack": a line `none<=UB` certifies opt(L) > UB),
  `driver2.py` (fixed UB decision). Max over spans ≤ L_max is exact in every mode.

### λ = 3: best over all spans L ≤ L_max (NUMERICAL-EXACT)

| k | L_max | min def | W = 2def | W/k | max φ | primitive optimal D (other optima at multiples are dilates) |
|---|---|---|---|---|---|---|
| 3 | – | 3 | 6 | 2.0 | 0 | any |
| 4 | 40 | 3 | 6 | 1.5 | 0.500 | {0,1,2,3} (4-AP) |
| 5 | 40 | 4 | 8 | 1.6 | 0.600 | {0,1,2,3,4} at L=4, dilates |
| 6 | 40 | 3 | 6 | 1.0 | 0.800 | {0,1,3,4,5,7} |
| 7 | 40 | 6 | 12 | 1.71 | 0.714 | {0,1,2,4,6,7,10}, {0,1,3,5,6,7,11} |
| 8 | 40 | 7 | 14 | 1.75 | 0.750 | {0,1,3,6,8,9,10,15}, {0,2,3,5,8,9,10,16} |
| 9 | 45 | 9 | 18 | 2.0 | 0.750 | {0,1,2,5,8,9,10,11,15}, {0,1,4,6,7,8,12,15,17}, … (8 primitive, L = 15..23) |
| 10 | 60 | 9 | 18 | 1.8 | 0.800 | {0,2,4,5,10,11,13,14,18,24}; also L = 22, 23, 25, 26 |
| 11 | 50 | 10 | 20 | 1.82 | 0.818 | {0,2,4,5,11,12,15,17,20,21,28} |
| 12 | 46 | 12 | 24 | 2.0 | 0.818 | {0,1,3,7,9,14,17,18,19,22,28,35} |
| 13 | 46 | 15 | 30 | 2.31 | 0.808 | {0,2,13,16,17,20,22,25,30,31,32,38,42} (§1.3) |
| 14 | 38 | 22 | 44 | 3.14 | 0.758 | {0,1,2,3,8,9,10,20,21,22,24,25,26,35} (§1.3). Beaten at L = 52, outside the certified range: def 19, W/k = 2.71, φ = 0.791 (tabu, NUMERICAL) |

E35 (SA) gave for k = 10, 12: 0.80, 0.773 (12: def 15) — the exact k = 12 optimum is def 12 (φ = 0.818).

**L-dependence (per-span exact optimum, def; `>x` = certified larger than x):**
- k = 10: L=13:21, 14:15, 21:12, **22–26: 9**, 27–32: 12, 33–41: 15, 42:12, then 9 only at even L = 44..52 (dilates by 2), 12 or 15 otherwise (L ≤ 60).
- k = 11: 17:16, 21:16, 25–27:13, **28: 10**, 30–31: 13, all L ∈ [32, 50]: > 12.
- k = 12: 20:18, 25:18, 28–31:18, 32–34:15, **35: 12**, 36–38:15, all L ∈ [39, 46]: > 12.
- Raw tables: `out/ex3_k*.txt`. Pattern: optima are attained at L ≈ 1.3–1.6·k²/6 (k = 13: L = 42 ≈ 1.49·k²/6; best known k = 14: L = 52 ≈ 1.59·k²/6) (the smallest spans that can host
  |A| ≈ 0.8·C(k,2)/3 distinct differences); larger spans only reproduce dilates and are otherwise worse.

### λ = 4 (NUMERICAL-EXACT, L ≤ 40, k = 11: L ≤ 36)

| k | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|
| min def | 6 | 6 | 7 | 9 | 8 | 12 | 13 | 15 |
| max φ | 0 | 0.40 | 0.533 | 0.571 | 0.714 | 0.667 | 0.711 | 0.727 |
| W/k | 3.0 | 2.4 | 2.33 | 2.57 | 2.0 | 2.67 | 2.6 | 2.73 |

Optimal examples: k = 8 {0,2,3,4,5,7,8,12}; k = 10 {0,1,3,6,7,8,10,12,15,16}; k = 11 {0,1,4,6,9,11,12,13,15,19,20}.
Raw: `out/ex4_k*.txt`.

### 1.3 k = 13, 14 (λ = 3; decision runs, NUMERICAL-EXACT within the stated span ranges)
- **k = 13, spans L ≤ 46** (`out/dec3_k13.txt`, UB = 18; a reported value ≤ 18 is the exact per-span optimum, `none`
  certifies > 18): **min def = 15 (W = 30, W/k = 2.31, φ = 0.808), only at L = 42**:
  D = {0,2,13,16,17,20,22,25,30,31,32,38,42}. Per span: L ≤ 32, L = 34–37 and L = 39: > 18 (certified);
  L = 33, 38, 40, 41, 43, 44, 45, 46: exactly 18 (e.g. L = 46: {0,2,7,8,11,15,20,23,25,26,27,36,46}).
  The tabu sweep (spans 30, 39, 50, 67) had only found def 18 — the exact search beats it here. Under the B₂[3]
  restriction (no class with r > 3; `BB_STRICT=1`), the exact optimum at L = 50 is def 18, attained by
  {0,1,3,7,9,14,17,18,19,22,28,35,50} = (k = 12 optimum) ∪ {50}.
- **k = 14, spans L ≤ 38** (`out/dec3_k14.txt`, UB = 22): **min def = 22 (W = 44, W/k = 3.14, φ = 0.758), only at
  L = 35**: D = {0,1,2,3,8,9,10,20,21,22,24,25,26,35} (a Type II / block set); every other L ≤ 38 has def > 22.
  **Larger spans do better.** Tabu at L = 52 (`out/tabu_lam.txt`, `out/tabu_k1316.txt`) found def = 19 (W/k = 2.71,
  φ = 0.791): D = {0,8,17,20,21,24,26,31,32,34,36,45,51,52}; def is ≡ 91 ≡ 1 (mod 3), so the next possible value is 16.
  The earlier sweep at L ∈ {45, 58, 78} gave 22, 22, 25. Spans ≥ 39 not certified (a decision run at
  UB = 19 for L = 39–44 was stopped after 2 h without finishing any span; no information from it).

### 1.4 Dependence on λ (NUMERICAL, tabu heuristic; `tabu_lam.sh`, `out/tabu_lam.txt`)
Tabu (40 000 iterations, 3 seeds) for k = λ·t + 2, t = 2..5, with only four spans L = c·k²/(20λ), c ∈ {10, 13, 16, 20}.
That grid is coarse, so these are upper bounds on min def; e.g. at λ = 3, k = 11 it gives def 13, while the exact value
is 10 at L = 28. Best W/k (φ):

| λ | k: W/k (φ) |
|---|---|
| 2 | 6: 1.00 (0.80); 8: 1.00 (0.857); 10: 1.00 (0.889); 12: 1.00 (0.909) |
| 3 | 8: 2.50 (0.64); 11: 2.36 (0.76); 14: 2.71 (0.79); 17: 4.00 (0.75) |
| 4 | 10: 2.60 (0.71); 14: 3.29 (0.75); 18: 5.00 (0.71); 22: 5.73 (0.73) |
| 5 | 12: 4.33 (0.61); 17: 4.82 (0.70); 22: 7.82 (0.63); 27: 9.33 (0.64) |
| 6 | 14: 4.43 (0.66); 20: 6.40 (0.66); 26: 9.31 (0.63) |
| 8 | 18: 6.33 (0.63); 26: 9.62 (0.62) |

- λ = 2 stands apart. W = k exactly at every k, φ → 1, and the optima for k = 8, 10, 12 are reflection-symmetric
  (e.g. {0,2,3,7,13,17,18,20}). Their defects are the ⌊k/2⌋ odd classes c − 2x with r = 1 (T2), which is Bu's
  mechanism. Minimality of W = k at λ = 2 was not checked exhaustively.
- For λ ≥ 3, W/k grows with both k and λ and φ stays at 0.6–0.8. Going from λ = 2 to λ = 3 is a jump: there is no
  λ ≥ 3 analogue of the symmetric family, where W stays linear and φ → 1.

### Where the defects are (NUMERICAL-EXACT for the listed sets)
Two structure types appear.
- **Type I** (all exact optima k = 10–13, the best known k = 14 set at L = 52, tabu bests k = 15, 16): every class
  d ≤ θL is good (3-fold, with almost complete coverage of [1, θL]), where θ ≈ 0.35–0.6 (k = 13: θ = 0.43; k = 14:
  θ = 0.33). The defects are the top differences, almost all with r = 1 (a few r = 2).
  These are B₂[3] sets (no class with r > 3). Counting: if [1, θL] is covered 3-fold by a roughly uniform D with
  L = k²/c, then (1 − θ/2) ≈ 3/c, i.e. θ = 2 − 6/c; c ≈ 4.3 gives θ ≈ 0.6, matching the data (HEURISTIC).
- **Type II** (the exact L ≤ 38 optimum at k = 14; tabu bests k = 18, 20–24): block structure = the product family of §2 (diagonal defects at d = 1, 2
  or at the block dilation), e.g. k = 14: {0,1,2,3,8,9,10,20,21,22,24,25,26,35}.

## 2. Theorems

### T1 (boundary bound; PROVED). For λ ≥ 3 and k ≥ 3: W ≥ 6, and def ≡ C(k,2) (mod λ).
Proof. Let D ⊂ [x₁, x_k], L = x_k − x₁, U = D − x₁, V = x_k − D (both contain 0 and L). For 0 ≤ s < L,
r(L − s) = #{(u,v) ∈ U × V: u + v = s} (pair (x₁+u, x_k−v)). Class L has r = 1. Let m = min(U' ∪ V'), U' = U∖{0},
V' = V∖{0}; m < L as k ≥ 3. Pairs with both u, v ≥ m sum to ≥ 2m, so r(L − m) = [m∈U] + [m∈V] ∈ {1, 2}: a defect. If
it equals 2, W ≥ 2(1 + 2) = 6. If it equals 1, say m ∈ U∖V; put m' = min V' (> m, and m' = x_k − x_{k−1} < L). Any pair
with v ∈ V' has v ≥ m', so r(L − m') = 1 + [m' ∈ U] ∈ {1, 2}, a third defect class: W ≥ 2(1+1+1) = 6. The congruence
is def = C(k,2) − λ|A|. ∎  Tight: exact optima at k = 3, 4, 6 have W = 6. (This is the O(λ²) boundary count; it does
not grow with k.)

### T2 (symmetric sets cannot carry odd λ; PROVED).
If D = c − D (reflection-symmetric), then the number of classes with odd r is ⌊k/2⌋. Hence for odd λ,
|A| ≤ ⌊k/2⌋ and φ ≤ λ⌊k/2⌋/C(k,2) ≤ λ/(k − 1).
Proof. σ(u,v) = (c−v, c−u) maps pairs to pairs with the same difference; non-fixed pairs come in σ-orbits of size 2.
Fixed pairs are {x, c−x} (x < c/2); their differences c − 2x are pairwise distinct, so each class holds at most one.
So r(d) is odd iff class d contains a fixed pair, and there are ⌊k/2⌋ fixed pairs. ∎
(Complements P4: symmetry supplies even multiplicities only — Bu's mechanism is intrinsically λ = 2.)

### T3 (interval ⊕ dilated set; PROVED). Let N ≥ 2, B ⊂ Z, |B| = b, D = {a + N·x: 0 ≤ a < N, x ∈ B} (k = Nb).
For m ≥ 0, 0 ≤ e < N, (m,e) ≠ (0,0):
    r_D(Nm + e) = (N − e)·r_B(m) + e·r_B(m + 1),     r_B(0) := b.
Proof. (a + Nx) − (a' + Nx') = Nm + e with |a − a'| < N forces a − a' ∈ {e, e − N} (only a − a' = 0 if e = 0); the
first case has N − e choices of (a, a') and needs x − x' = m, the second has e choices and needs x − x' = m + 1. ∎
**Corollary (λ = N, B Sidon, b > N).** With S = (B − B) ∩ Z_{>0} and R(B) = number of maximal runs (intervals) of S:
class Nm (m ≥ 1) is N-fold iff m ∈ S; class Nm + e (m ≥ 1, 1 ≤ e < N) is N-fold iff m, m+1 ∈ S; classes e < N are
defects (r = (N−e)b + e·r_B(1) > N). Hence exactly
    def(D) = C(N,2)·(b + 2R(B)),      φ = 1 − C(N,2)(b + 2R(B))/C(Nb, 2).
(Verified against brute force for all Golomb rulers b ≤ 10, N = 3, 4.)
- Values (λ = N = 3, `out/interval_sidon.txt`, NUMERICAL-EXACT for the listed explicit B): optimal Golomb rulers
  b = 6, 10, 12, 14 → k = 18, 30, 36, 42: φ = 0.804, 0.835, 0.838, 0.826; Singer sets mod q²+q+1 (best of all /
  20 000 sampled lifts) q = 11, 17, 19, 29, 41, 59, 71 → k = 36, 54, 60, 90, 126, 180, 216: φ = 0.848, 0.849, 0.851,
  0.843, 0.836, 0.827, 0.822. λ = 4 analogues: φ = 0.80–0.83 up to k = 288.
- So φ ≥ 0.82 is attainable at least up to k = 216: the hoped-for "φ ≤ 2/3 + o(1)" is false in this range. If S
  behaves like independent bits with P(m ∈ S) ≈ 1 − m/v, R ≈ v/6 ≈ b²/6 and φ → 1 − (N−1)/(3N) = 7/9 (HEURISTIC; best
  lifts do better than typical ones).
- But W = 2C(N,2)(b + 2R) ≥ (N − 1)k always, and ≍ k² for every Sidon B we tried (R(B)/b² ≈ 0.05–0.13): the family is
  far from W = O(εk). Its actual R(A) is 1.36–1.71 (§4): the diagonal classes d < N (weight ≈ (N−1)k) sit exactly where
  F_B(Nx) ≈ 0 with x small, giving M ≈ k/2 and R ≈ √(N/2) (HEURISTIC derivation in §5).
- φ → 1 in this family ⟺ Sidon sets with R(B) = o(b²) (difference set a union of o(b²) intervals). Not excluded by
  anything we proved; all data have R(B)/b² ∈ [0.05, 0.13] (it grows slowly with b for best Singer lifts).

### T4 (general products; PROVED). For A ⊂ [0, N), B ⊂ Z: r_{A+NB}(Nm + e) = r_A(e) r_B(m) + r_A(e−N) r_B(m+1).
If B is Sidon and m, m+1 ∈ S, the class Nm + e (e ≠ 0) has multiplicity ρ_A(e) = r_A(e) + r_A(e − N), the periodic
autocorrelation of A in Z_N; so all such classes are λ-fold iff A is a cyclic (N, |A|, λ) difference set, while the
aligned classes Nm have multiplicity |A|·r_B(m) = |A|, which equals λ only for A = Z_N (= the interval of T3). For a
nontrivial difference set the aligned classes (a fraction ≈ 1/|A| of all pairs) are all defects. E.g. A = Singer
(15,7,3): φ ≈ 0.64 heuristically, below T3. (Proof: same as T3.)

### T5 (isolated cross families; PROVED). Homometric triples and separated-block designs cost W ≍ k².
Let U, V ⊂ D with |U| = s, |V| = t, and suppose the cross family X = U × V is isolated: every u − v is positive, and
no pair of D outside X has a difference in {u − v: u ∈ U, v ∈ V}. Then

    #(pairs of X in λ-fold classes) ≤ (1/λ)·Σ_δ r_U(δ) r_V(δ) ≤ √(E(U)E(V))/λ,

where E(·) = Σ_δ r(δ)² is the additive energy, with r(0) = |U|.
- If U, V are Sidon, Σ_δ r_U r_V ≤ st + min(s² − s, t² − t). So for s = t at least s² − (2s² − s)/λ pairs of X are
  defects: more than a fraction 1 − 2/λ of the family (1/3 at λ = 3, 1/2 at λ = 4).

Proof. On the classes met by X, isolation gives r_D(d) = c(d) := #{(u,v) ∈ X: u − v = d}. A good class has c = λ, so
λ·#(good pairs of X) = Σ_good c² ≤ Σ_d c(d)² = #{(u,v,u',v'): u − v = u' − v'} = #{u − u' = v − v'} = Σ_δ r_U(δ)r_V(δ).
The rest is Cauchy–Schwarz, and for Sidon sets r(δ) ≤ 1 when δ ≠ 0. ∎

Corollary (separated homometric triples).
- Construction. D = (U₁+t₁) ∪ (U₂+t₂) ∪ (U₃+t₃) with U_i ⊂ [0, w] pairwise homometric Sidon sets of size s (k = 3s).
  Within-part classes are then exactly 3-fold.
- With equal gaps t₂ − t₁ = t₃ − t₂ > 2w, the (1,3) family is isolated, so at λ = 3: def ≥ (s² + s)/3 and
  W ≥ (2/27)k² + (2/9)k.
- With three distinct, well-separated gaps all three cross families are isolated, so W ≥ (2/9)k² + O(k) and
  φ ≤ 7/9 + o(1).
- So separated homometric triples, and more generally any design whose low-energy blocks have isolated cross families,
  cannot give W = O(k).
- T3 is not of this form: its blocks are intervals of high energy (E ≈ (2/3)N³), and its cross families overlap.

### T2′ (signed version; PROVED). For signs ε ∈ {±1}^D put c(g) = Σ_{u−v=g} ε_u ε_v. Then c(g) ≡ r(g) (mod 2), so
for odd λ every class with c(g) = λ has r(g) odd. Hence for reflection-symmetric support D and odd λ, at most ⌊k/2⌋
classes have c = λ, whatever the signs. Also c(L) = ε_{x₁}ε_{x_k} = ±1, so exact signed λ-fold sets do not exist
(W_s ≥ 2), but the T1 argument does not extend beyond that: a class with two representations can have c = 0.

## 2b. Signed multisets (optional extension; `signed_ex.c` exhaustive, `signed_tabu.c` heuristic)
Setup (lead's extension): q = Σ_{d∈D} ε_d z^d, c(g) = Σ_{u−v=g} ε_u ε_v, A = {g > 0: c(g) = λ},
W_s = Σ_{c(g)∉{0,λ}} 2|c(g)|. Then 2λ f_A = |q|² − k − E_s with |E_s| ≤ W_s, so the rigorous naive bound is
R(A) ≤ Rn := (k + W_s)/(2λ√|A|). Also Σ_{g>0} c(g) = ((k₊ − k₋)² − k)/2 exactly, so λ|A| ≤ ((k₊−k₋)² − k)/2 + W_s/2.
A signed set with W_s = O(k) therefore has Rn ≈ (1 + W_s/k)/(√(2λ)(1 − 2ρ₋)), with ρ₋ = k₋/k.

**Exhaustive (NUMERICAL-EXACT).** All D ⊂ [0, L] containing 0 and L, all signs with ε(0) = +1; λ = 3: k = 6, 7, 8
(L ≤ 18), 9 (L ≤ 20), 10 (L ≤ 24); λ = 4: k = 6, 7, 8 (L ≤ 18), 9 (L ≤ 20), 10 (L ≤ 22). Files: `out/signed_ex*.txt`.

| λ | k | min Rn, signed | its D (−x means ε = −1) | min Rn, unsigned | min W_s at \|A\| ≥ unsigned-optimal \|A\| |
|---|---|---|---|---|---|
| 3 | 6 | 1.000 | {0,1,3,4,5,7} (no negatives) | 1.000 | 6, attained unsigned |
| 3 | 7 | 1.059 | {0,−1,−4,−5,−6,−7,−8} (= one negative, after a global flip) | 1.416 | 12, unsigned |
| 3 | 8 | 1.000 | {0,−1,2,3,5,7,9,10} | 1.386 | 14, unsigned |
| 3 | 9 | 1.059 | {0,−1,−3,−4,−6,7,−8,−9,−10} | 1.500 | 18, unsigned |
| 3 | 10 | **0.943** | {0,−1,2,3,4,7,10,12,14,15} | 1.347 | 18, unsigned |
| 4 | 8 | 1.155 | {0,−1,−4,−5,−6,−7,−8,−9} | 1.342 | 16, unsigned |
| 4 | 9 | 1.313 | {0,−1,−5,−6,−8,−9,−10,−11,−12} | 1.684 | 24, unsigned |
| 4 | 10 | 1.155 | {0,−1,−4,5,6,7,8,9,10,11} | 1.591 | 26, unsigned |

- At the |A| of the unsigned optimum, signs never lower the minimum defect weight. In every case the minimum of W_s
  over all signed sets with that |A| is attained by an unsigned set (k ≤ 10, the spans above).
- Signs help only by trading |A| for W_s. The signed optima have one or two negatives and much smaller W_s, e.g.
  λ = 3, k = 10: W_s = 6, |A| = 8, compared with W = 18, |A| = 12 unsigned. Since W_s ≥ 2 is the only proved signed
  bound (T2′), signed sets reach W_s near the T1 floor at small k. Even so, the naive Rn stays ≥ 0.94.

**Tabu, k = 10–20, λ = 3–6 (NUMERICAL; `out/signed_tabu.txt`; objective Rn, 2 seeds × 3 spans).** Signed vs unsigned
best Rn: λ = 3: 1.04/1.35 (k=10), 1.18/1.70 (12), 1.35/2.02 (14), 1.60/2.31 (16), 2.02/3.61 (20); λ = 4: 1.34/1.59,
1.23/1.73, 1.17/1.82, 1.23/2.13, 1.87/3.18; λ = 5: 1.41/1.63 … 1.74/3.00; λ = 6: 1.67/2.17 … 1.65/2.98. The signed
optima have 2–4 negatives (ρ₋ ≈ 0.15–0.2), W_s/k = 0.4–1.9 (unsigned: 1.8–7), and |A| at 40–60 % of the unsigned |A|.
So signs cut W_s by a factor of 3–4, but the factor (1 − 2ρ₋)⁻¹ ≈ 1.4–1.7 takes back most of the gain.
Actual R(A) for the signed candidates is in §4.

Files for this section: `signed_ex.c`, `signed_tabu.c`, `signed1.sh`, `cands_signed.txt`; outputs `out/signed_ex*.txt`,
`out/signed_tabu.txt`, `out/evalR_signed.txt`.

## 3. Refuted ideas (FAILED), with the smallest counterexamples
- **F1 mod-p counting.** For p | λ every d with p ∤ r(d) is a defect, so W ≥ n_p(D) := #{d ≠ 0: p ∤ r(d)}. Hoped:
  n_p(D) ≥ k − O(1) (it holds with equality for symmetric D at p = 2, for intervals n_3 ≈ 4k/3, and for D = {0,1}^m in
  base 4). FALSE (exhaustive `minnp.c`, all D ⊂ [0, 24] for k ≤ 9, [0, 22] for k = 10, 11):
  n_2 = 2 for D = {0,1,2,6,7,9,10} (k = 7), {0,1,2,3,6,8,9,10,13,14} (k = 10), {0,1,2,3,4,5,6,14,15,21,22} (k = 11);
  n_3 = 8 for k = 9, 10, 11, e.g. {0,1,2,3,4,5,9,10,11} = {0,1,2} + 3·{0,1,3} (k = 9). Mechanism (k = 9): in F₃,
  P = (1−z)²·Q(z)³ with Q the Sidon set {0,1,3}, and P P* = (1−z)(1−z³)·(QQ*)(z³): the factor (1 − w)·QQ*(w)
  telescopes because r_Q is constant on [1, 3]. Congruence information alone gives only O(1).
- **F2 cyclic lifts.** All (m, c) ∈ Z_v^* × Z_v for Singer PG(3,q) q = 2, 3, 5, PG(4,2), QR(11,19,23,31,43),
  biquadratic (37, 101), twin-prime (15, 35) and complements (`out/cyclic_lifts.txt`). Best coherent φ: (15,7,3)
  0.571, (11,6,3) 0.600, (40,13,4) 0.564, (19,9,4) 0.444, (23,11,5) 0.455, (156,31,6) 0.452, (101,25,6) 0.360,
  (31,15,7) 0.400, (43,21,10) 0.286 — decreasing in λ, always below the exact optimum at the same k. Reason: a
  residue's λ representations wrap independently; a d.s. inside a half-interval would be an exact λ-fold set in Z,
  impossible by P4. For λ = 2: biquadratic (37,9,2) reaches 0.778.
- **F3 "φ decreases with k" (E35).** Search artefact: SA at k = 18, 21, 24, 30 gave φ = 0.69, 0.67, 0.62, 0.57; T3 gives
  0.804, 0.786, 0.783, 0.835 there, and the exact k = 12 optimum (0.818) beats SA's 0.773.
- **F4 "φ ≤ 2/3 + o(1)" as the kill criterion.** False for k ≤ 216 (T3). The relevant quantity is W, not φ.
- **F5 even λ with reflection symmetry (λ = 4, 6; NUMERICAL, `symtabu.c`, `out/symtabu.txt`).**
  - Idea. For D = H ∪ (c − H), r(d) = 2r_H(d) + 2#{h < h': h + h' = c − d} + [d ∈ c − 2H]. So even λ = 2μ needs only
    ρ_H(d) := r_H(d) + #{h<h': h+h' = c−d} ∈ {0, μ}. This sidesteps T2 (which blocks odd λ). The forced defects are
    the fixed classes c − 2h with r = 1, which are harmless exactly as in Bu (E_fix(x) = P(2x)). If the remaining
    defects were W' = o(k), then R ≈ 1/√(2λ), e.g. 0.354 at λ = 4.
  - Validation. At λ = 2 the same code finds W' = 0 at every k ≤ 30 once c ≳ k²/3.
  - Result. At λ = 4, W'/k = 3.6, 3.9, 4.3, 4.9, 6.1, 7.0 for k = 10, 14, …, 30; at λ = 6, 5.2 → 9.9. φ = 0.53–0.74,
    actual R ≥ 0.91. This is worse than unconstrained λ = 4 tabu (W/k 2.6–5.7) and grows with k.
- **F6 signs as a substitute for coherence (NUMERICAL-EXACT for k ≤ 10).** At the unsigned-optimal |A|, the minimum
  W_s over all signed sets equals the unsigned minimum in every case checked (λ = 3: k = 6–10; λ = 4: k = 8–10).
  Signs lower W_s only by lowering |A|. Under tabu at k ≤ 20 the signed W_s/k still grows with k
  (λ = 3: 0.40, 0.67, 1.0, 1.25, 1.5 for k = 10, 12, 14, 16, 20).

## 4. Actual R(A) and the E-versus-F_D anatomy (NUMERICAL, uncertified; `evalR.py`, `out/evalR2.txt`, `out/evalR_signed.txt`, `out/evalR_sym.txt`, `out/evalR3.txt`)
Dense FFT grid (≥ 64·max A points) + Newton on the 20 lowest grid minima; identity 2λf_A = |F_D|² − k − E checked at
the minimiser to 1e−12.

| set | k | \|A\| | φ | W/k | R(A) | E(x*) | \|F_D(x*)\|² | "ideal" R (E = 0 on near-zeros) |
|---|---|---|---|---|---|---|---|---|
| λ=3 opt {0,1,3,4,5,7} | 6 | 4 | 0.80 | 1.0 | 0.760 | 4.0 | 0.89 | 0.500 |
| λ=3 opt k=9, L=17 | 9 | 9 | 0.75 | 2.0 | 0.692 | 3.9 | 0.48 | 0.474 |
| **λ=3 opt k=10, L=24** | 10 | 12 | 0.80 | 1.8 | **0.680** | 5.7 | 1.56 | 0.478 |
| λ=3 opt k=11, L=28 | 11 | 15 | 0.818 | 1.82 | 0.775 | 8.0 | 1.00 | 0.473 |
| λ=3 opt k=12, L=35 | 12 | 18 | 0.818 | 2.0 | 0.793 | 9.1 | 0.91 | 0.471 |
| λ=3 tabu k=13, L=50 | 13 | 20 | 0.769 | 2.77 | 0.724 | 7.5 | 1.08 | 0.484 |
| λ=3 exact k=13, L=42 {0,2,13,16,17,20,22,25,30,31,32,38,42} | 13 | 21 | 0.808 | 2.31 | 0.838 | 11.4 | 1.34 | 0.470 |
| λ=3 tabu k=14, L=52 {0,8,17,20,21,24,26,31,32,34,36,45,51,52} | 14 | 24 | 0.791 | 2.71 | 0.872 | 17.5 | 5.92 | 0.475 |
| λ=3 tabu k=15, L=52 | 15 | 27 | 0.771 | 3.2 | 0.760 | 12.8 | 4.11 | 0.481 |
| λ=3 tabu k=16, L=76 | 16 | 31 | 0.775 | 3.38 | 0.834 | 14.6 | 2.78 | 0.479 |
| λ=3 T3, Golomb b=10 | 30 | 121 | 0.835 | 4.8 | 1.443 | 75.9 | 10.7 | 0.455 |
| λ=3 T3, Golomb b=12 | 36 | 176 | 0.838 | 5.67 | 1.358 | 77.0 | 5.0 | 0.452 |
| λ=4 opt k=8, L=12 | 8 | 5 | 0.714 | 2.0 | 0.773 | 6.1 | 0.26 | 0.446 |
| λ=4 opt k=11, L=20 | 11 | 10 | 0.727 | 2.73 | 0.756 | 10.6 | 2.45 | 0.435 |
| λ=4 T3, Golomb b=10 | 40 | 159 | 0.815 | 7.2 | 1.713 | 153 | 20.6 | 0.397 |
| λ=3 signed k=10 {0,−1,2,3,4,7,10,12,14,15} | 10 | 8 | (0.53) | 0.6 (W_s) | **0.692** | 2.3 | 0.59 | – |
| λ=5 signed k=16 (tabu; `cands_signed.txt`) | 16 | 11 | (0.46) | 1.88 | 0.707 | 8.9 | 1.47 | – |
| other signed candidates (λ = 3–6, k = 7–20) | | 3–17 | | 0.2–1.9 | 0.76–1.22 | | | |
| λ=2 symmetric, W' = 0 (k = 10, 14, 18, 22, 26, 30; `out/evalR_sym.txt`) | 10–30 | 20–210 | 0.89–0.97 | 1.0 | 0.894, 0.768, 0.752, 0.707, 0.961, 0.694 | | | |
| λ=4 symmetric, best W' (k = 10–30) | 10–30 | 6–80 | 0.53–0.74 | 4.2–7.7 | 1.32–1.73 | | | |
| λ=6 symmetric, best W' (k = 10–30) | 10–30 | 3–47 | 0.40–0.65 | 5.4–10.2 | 0.91–2.54 | | | |

Reading. The would-be R if E vanished on the near-zero set of F_D is 0.45–0.50 for every candidate (≈ 1/√(2λφ));
the realised R is 0.68–1.7 because the minimiser of f_A sits where E ≈ 0.4–0.9k (Type I) or ≈ 2k (T3, diagonal) while
|F_D|² is merely small, not zero. M(A) = max_x (k + E(x) − |F_D(x)|²)/(2λ), so R < 1/2 at λ = 3 needs
max_x(E − |F_D|²) < (√(1.5φ) − 1)k ≈ 0.1k (φ = 0.8) — an order of magnitude below what any candidate achieves.
- Defect locations of the new sets: k = 13 (L = 42) has all classes d ≤ 18 good and defects at 19..42; k = 14 (L = 52)
  has all d ≤ 17 good and defects at 18..52. Both are Type I.
- Signed φ in parentheses is λ|A|/C(k,2). For signed sets the natural normaliser is ((k₊−k₋)² − k)/2: the λ = 3, k = 10
  set reaches 24/27 of it.
- Calibration. The λ = 2 rows are sets with only Bu-type defects (W' = 0), the λ = 2 analogue of what the route needs
  at λ = 3, and still have R = 0.69–0.96 at k ≤ 30. Small-k R is dominated by E_fix(x) = P(2x) at the zeros of P,
  which is finite-size noise. So R ≥ 0.68 at k ≤ 16 does not by itself refute λ = 3. The discriminating statistic is
  the non-harmless defect weight: W' = 0 at λ = 2, against W ≥ k growing at λ = 3.

## 5. Heuristics worth keeping (HEURISTIC, not proofs)
- Continuum density. If D has density profile g on [0,1] and L = k²/c, the pair density at difference tL is
  c·(g ⋆ g̃)(t), which tends to c∫g² ≥ c as t → 0+ (for d in the range L/k ≪ d ≪ L). Excess pairs above 3 per class are
  defects, so φ → 1 at λ = 3 needs c ≤ 3, i.e. L ≳ k²/3, the sparse regime. All exact optima (k ≤ 12) live at
  c ≈ 4–4.5 (Type I; finite-size), and both exact per-span tables and tabu get worse as L grows past the optimum. No
  structured candidate is known in the regime c ≤ 3.
- T3 lower bound on M. f_A(x) = f_S(Nx) + Re[F_T(Nx)·Σ_{e=1}^{N−1}e^{iex}] with T = S ∩ (S−1); if R(B) = o(b²) this is
  ≈ Re[F_S(Nx)·Σ_{e<N}e^{iex}] ≈ N f_S(Nx) for x ≪ 1/N, whose minimum is ≈ −Nb/2 = −k/2 at a near-zero of F_B. With
  |A| ≈ k²/(2N): R ≈ √(N/2) (≥ 1.22 for λ = 3). The imaginary-part cross term is what a rigorous version must control.
- W growth. Best known W/k (λ = 3): 1.0 (k=6), 1.8 (10), 2.0 (12), 2.31 (13, exact L ≤ 46), 2.71 (14, tabu), 3.2 (15), 3.38 (16), 3.33 (18,
  T3), 4.29 (21, T3), 5.0 (24, T3), 4.8 (30, T3) — increasing; exact only for k ≤ 12 (≤ 14 partially). Consistent with
  W ≍ k² (φ bounded away from 1), but tabu is search-limited for k ≥ 18 (it rediscovers T3-type blocks but does not
  reach the best T3 values), so this is evidence, not proof.

## 6. Most promising next step

**Decision.** Kill the λ ≥ 3 near-ruler line as a construction route. The lead had already demoted it to low priority
pending a structural idea. Every source of coherent multiplicity ≥ 3 tested here costs W ≥ k, and W/k grows with k:
- exact optima (k ≤ 14);
- Type I and Type II structures;
- products A + N·B, and cyclic lifts over all (m, c);
- separated homometric triples (T5 proves W ≍ k² for them);
- signs;
- even λ with reflection symmetry.

The only known source of harmless defects is the involution x ↦ c − x, which caps coherent multiplicity at 2. The
finite subgroups of the isometry group of Z (translations and reflections) have order ≤ 2, so any λ ≥ 3 coherence must
come from coincidences not induced by a symmetry of Z (an informal reading, not a theorem). Those are what all the
data show to be expensive.

**Single next step if the line is kept: a proof attempt of Conjecture C-W.**
- Statement. For λ = 3 and every D ⊂ Z with |D| = k ≥ 4: W(D) ≥ k, equivalently def ≥ k/2.
- Evidence. NUMERICAL-EXACT for k ≤ 12; within the certified spans for k = 13, 14. Tight at k = 6 with
  {0,1,3,4,5,7}, where all three defect classes are the T1 top classes L, L−1, L−2.
- Why. It would be the first forced-defect bound that grows with k (T1 gives only 6), and it is the natural stepping
  stone to the kill statement W'/k → ∞.
- What a proof must use. Congruences cannot work (F1 shows mod-3 information gives O(1)). Nor can a top-window count
  alone (T1 is tight, and at k = 6 the window becomes 3-fold immediately). The proof must therefore combine both ends
  (U + V for U = D − x₁, V = x_k − D) with the global count λ|A| + def = C(k,2).
- First concrete derivation. Classify the exact optimum structures for k = 6–12 (all recorded in `out/ex3_k*.txt`)
  by where their defects sit relative to the two extreme gaps, and look for a charging scheme that assigns ≥ 1/2 defect
  pair to each point of D.
- Caution. C-W alone does not kill the mechanism: λ = 2 has W = k too, and Bu survives because those defects are
  harmless. The full obstruction needs W' (non-harmless weight) ≥ ck^{1+δ}, or directly max_{F_D(x)≈0} E(x) ≥ ck.

**What would revive the line.** Either of two explicit sets would do it:
- a D with λ = 3 and W < k at some k ≥ 7, which refutes C-W;
- better, a D with W < 0.22k and φ near 1, which gives R < 1/2 through the naive bound alone.

None exists for k ≤ 12 (exact). Tabu and T3 give W/k ≥ 2.3 for 13 ≤ k ≤ 30.
