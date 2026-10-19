# E111 brief: completely-positive (nonnegative-coefficient SOS) certificate costs (side computation, falsification)

You are a side-computation agent. You do not do the core math. All heavy computation runs on the VM `dirichlet` via
`DIRICHLET_IP=34.148.157.169 src/dirun.sh -c <cores> -t <secs> python <script> ...`, launched from the repo root. Never
compute heavily on the laptop. Gurobi 13 is available on dirichlet (gurobipy, licence at /opt/gurobi1303/gurobi.lic);
Clarabel/SCS are available via cvxpy. Write code to `src/e111_cp.py` (and helpers if needed) and data to
`examples/e111/`. Write your report to `.research/agents/e111_report.md`. Do NOT edit any `.research/*.md` file other
than your report. Do not commit.

## Mathematical setting (exact; convention f_A(θ) = Σ_{a∈A} cos(2π a θ))
A ⊂ [1, X] finite, n = |A|, M(A) = −min_θ f_A(θ).
A CP certificate of cost C is a finite family of nonnegative sequences P_j on Z with
    Σ_j (P_j ⋆ P̃_j)(k) = 1_{±A}(k)  for every k ≠ 0,     Σ_j ‖P_j‖₂² = C,
where (P ⋆ P̃)(k) = Σ_b P(b)P(b+k). Then 2f_A + C = Σ_j |P̂_j|² >= 0, so M(A) <= C/2.
Facts (proved by the lead):
- supp P_j is a clique: (supp P_j − supp P_j) ⊂ ±A ∪ {0}, translation is irrelevant (normalise min supp = 0), and
  diam ≤ max A.
- C >= 2n/(ω − 1), with ω the clique number of the Cayley graph Cay(Z, ±A).
- Sidon differences A = {b' − b > 0 : b, b' ∈ B}, B Sidon, have C = |B| ≈ √(2n): R_CP := C/(2√n) ≈ 1/√2.
The open question (CP-CHOWLA): is C_CP(A) >= c√n for all A? Equivalently: can cancellation-free certificates reach
R_CP well below 1/√2? Near-optimal sets have R = M/√n ≈ 0.56–0.6 (dense, N <= 50) and Singer–Bu ≈ 0.55.

## Tasks
1. FLAT-BLOCK LP with column generation. Restrict P_j = √w_j · 1_{B_j} (B_j a clique, w_j >= 0). Then
       minimise Σ_B w_B |B|   s.t.   Σ_B w_B m_B(k) = 1_A(k)  (k = 1..X),   w >= 0,
   with m_B(k) = #{(b, b') ∈ B² : b' − b = k}. Use column generation. The pricing problem, given duals y_k (k = 1..X),
   is max over cliques B ∋ 0 of Σ_{b<b' ∈ B} y_{b'−b} − |B|, which is a binary quadratic program over x ∈ {0,1}^{X+1}
   with x_b x_{b'} = 0 whenever b' − b ∉ A. Solve it with Gurobi (nonconvex BQP or linearised MILP), exactly for
   small X; with a time limit plus a heuristic for larger X, saying which.
   Report C_flat (an UPPER bound on C_CP), the LP dual bound for the flat class, and R_CP = C_flat/(2√n).
2. TWO-LEVEL BLOCKS (optional, if task 1 is fast). Allow P_j with values in {0, 1, 2}·√w_j (or a few levels) to see
   whether non-flat nonnegative vectors lower the cost.
3. Sets to run (compare R_CP against R = M/√n; M from an FFT grid of 2^16 points, uncertified):
   - examples/construct/N50_certified.json (both rows);
   - examples/dense_certified.json rows with maxA <= 120;
   - Singer difference sets from src/singer.py: q = 5, 7, 11 (A = positive differences);
   - the intervals [1, 20] and [1, 40];
   - random A ⊂ [1, 60] at density 1/2 (seed 20261019);
   - Sidon-difference unions (A = (B₁ − B₁) ∪ (B₂ − B₂), two Sidon sets), for small cases.
4. ADVERSARIAL (falsification target "no CP-flat certificate beats R_CP = 1/√2 asymptotically"). For X <= 40, run a
   local search over A (add/remove/swap moves, objective C_flat(A)/(2√|A|), |A| >= 10). Report the best sets found,
   their R_CP, their true R, and the block structure of the optimal certificate (block sizes, weights, and whether the
   blocks are APs, Sidon sets or other). Record seeds, move counts and run times.

## Report format (.research/agents/e111_report.md)
- A table: set | n | X | R (grid) | R_CP (flat UB) | flat-class LP lower bound | blocks used.
- The adversarial search's best R_CP per X, with the sets written out.
- Exact statements of what is a numerical LP result versus what is exact (state solver tolerances).
- Any set with R_CP < 0.68 must be listed explicitly, with its certificate saved to examples/e111/ as JSON (blocks and
  weights) and the identity Σ w_B m_B = 1_A checked in exact rational arithmetic after rounding the weights.
