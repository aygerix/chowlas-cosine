# Brief: improve Bedert's run-top bound |B_t| << K^4 (exponent 1/5 -> 1/4), or exhibit why the hypotheses cannot

## Setting (exact)
A = −A ⊂ Z \ {0} finite, n = |A|, F(x) = Σ_{a∈A} e(ax) (real, e(y) = e^{2πiy}, x ∈ T = R/Z), and K > 0 with F + K >= 0 on T.
A_t := A ∩ (A + t),  B_t := A_t \ (−A_t) = {m ∈ A : m − t ∈ A, m + t ∉ A}  (t ≠ 0).
|B_t| = number of maximal t-progressions ("t-runs") of length >= 2 inside A (Bedert Lemma 5.3).
Chowla's conjecture ⟺ K >> n^{1/2}.

## Known (verified by us)
- Roth (Bedert Lemma 4.1): #{(a,b) ∈ A^2 : a − b ∈ A} >= n^2/K − nK.  (Gram/Cauchy–Schwarz on ν = (F+K)/K.)
- Shankar 2609.05338: Σ_{t∈A} |B_t| = 6Q − 4I >= T/3 (T = Schur-triple count), so some t has |B_t| >> n/K.
- Bedert 2509.05260v3 Prop 7.3: |B_t| << K^4 for every t ≠ 0.  Together: K >> n^{1/5}.
- Bedert's proof (read §7 in full): Lemma 7.2/(38) gives a pointwise inequality |φ_t| <= ψ_t + O(K^2) where φ_t, ψ_t are
  the odd/even parts of (1 − cos(2πtx + π/4))·(f_t ∗ f_t), f_t = 2(1 + sin 2πtx)F >= −4K; Fourier GAP: −Im ρ_m >= 4+√2 on
  B_t while ψ̂_t <= 4 + 1/√2 everywhere. Lemma 7.1: 1̂_{B_t} = Q_1 + Q_2, |Q_1| <= 4(F + K), ||Q_2||_2 << K^2. Test (38)
  against H∗H, H = |Q_1|: |B| <~ K^2·||H||_1^2 + K^2|B|^{1/2} => |B| << K^4.
- Our barrier (.research/NOTEBOOK.md, "Where Bedert's K^4 comes from"): no inequality of degree 1 in the pattern (single
  nonnegative multiplier m(x) = Σ c_j e(jtx) times F) has a coefficient gap, because on B_t-patterns min|Im Λ| <= |c_1| <= c_0
  <= max Re Λ. Degree 2 costs an additive K^2. So within "gap inequality + nonnegative test function" one gets
  |B_t| <~ K^2·||H||_1^2; K^3 needs a test H >= |Q| with Q̂ ≈ 1 on B_t (in L^2) and ||H||_1 <~ K^{1/2}.
- All known sets satisfy K^2 >~ n >= |B_t|, so numerics cannot test |B_t| <= C K^2 directly (it follows from C½).

## Task (pure mathematics; computations only as tiny sanity checks, < 10 s and < 500 MB, no long jobs — the laptop is
## running a guarded 4-core job; use src/localrun.sh -m 1 if you run anything at all)
Aim for ONE of:
(a) PROOF of |B_t| << K^{4−δ} (ideally K^3 or K^2) for all t ≠ 0 under F + K >= 0 — complete, line-by-line checkable,
    explicit about every inequality and constant. Ideas worth trying (not prescriptions): exploit that B_t is defined by a
    3-window pattern so 1̂_{B_t} is a trilinear form in shifted F's; use run structure (Claim 7.5: |A ∩ (A + jt)| >=
    |A_t| − j|B_t|) to build better test functions; use the probability-measure form ν = (F+K)/K, ν∗ν = (1 − 1/K) + ν/K;
    replace H∗H by a test whose L^1 norm is O(K) instead of O(K^2) (e.g. H∗(F+K)/K-type mixed tests); combine with the
    Gram-vector view (vectors v_x, <v_x, v_y> = Kδ_{x=y} + 1_A(x − y)).
(b) OBSTRUCTION: identify exactly which consequences of F + K >= 0 Bedert's proof uses, define the corresponding RELAXED
    model (e.g. "f_t∗f_t >= −16K^2 and the 5-window coefficient table" or a positive-semidefinite/Gram relaxation), and
    construct a relaxed example with |B_t| ≍ K^4 (or >> K^3). That shows the method needs new input; say precisely what.
(c) A conditional or restricted improvement (e.g. |B_t| << K^3 if A ⊂ [1, X] with n >= X^{1−ε}, or if A has no
    3-term APs with difference t, or under an L^4 hypothesis), with proof.
Also double-check our barrier lemma (degree 1 has no gap) and say if it is wrong.

## Deliverable
Write .research/agents/runtop_report.md: the exact statement(s) obtained with status (PROVED / CONDITIONAL / OBSTRUCTION /
FAILED), complete proofs or the explicit relaxed example, and the single most promising next lemma. Do not edit other
.research files or src/; do not commit. Never weaken quantifiers silently (∀ t ≠ 0, ∀ x ∈ T, sets not multisets).
