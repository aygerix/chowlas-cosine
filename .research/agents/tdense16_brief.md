# Math brief (codex research agent), round 16: WRS(η) — a power-decaying defect from the full Boolean equation

You are a research mathematician working on Chowla's cosine problem in /Users/jmercedes/Desktop/Projects/Research/chowla-cosine.
- Read CLAUDE.md first: conventions, honesty labels, and the rule that numerics are not proofs.
- Rules (unchanged):
  - Do NOT edit .research/*.md. Do not commit. Do not launch subagents. No LaTeX; markdown only.
  - Report: `.research/agents/tdense16_report.md` (keep it current). Scratch: `.research/agents/tdense16_scratch/`.
  - Computation ONLY on the VM via `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 ...` (at most 4 cores; bash, not
    zsh).
  - Gurobi for every LP/MILP/QP. SDPs, if any, use Clarabel or SCS via cvxpy.
  - Label every claim PROVED / NUMERICAL / HEURISTIC / CONJECTURED, with exact quantifiers.
  - Grep .research/PROOFS.md before any novelty claim.

## State (read PROOFS P64–P68, NOTEBOOK cont. 18, and your round-15 report)
- Setting: q is a prime ≡ 1 mod 4; B = −B, 0 ∉ B, |B| = (q − 1)/2; λ(γ) = Σ_{b∈B} e(γb/q);
  K = −min_{γ≠0} λ; Λ = max_{γ≠0} λ.
- Exact flat model (P68.4). Put t = K − ½, h(0) = t and h(γ) = λ(γ) + K (γ ≠ 0). Then h >= 0 and
      h⋆h = (q²/4)δ_0 + C0·1,   C0 = q(t² − ¼).
  Consequences:
  - L := Λ + K satisfies L² <= C0;
  - E = (q − 1)[tL − t² − q/4] >= 0;
  - K >= (½ + o(1))q^{1/4}.
- The missing lemma (P68.7), WRS(η): max h <= A q^{(1−η)/2} t^{1+η} for ½ < t <= δ0√q.
  - It implies K >~ q^{(1+η)/(4+2η)}. η = 1 (Λ <~ K²) is Sanders' half-set 1/3.
  - Equivalently, with Δ_a = [2t h(2a) + R_a]/C0 at a peak a (P68.8), it requires
        1 − Δ_a <= (4/3)A²(t/√q)^{2η}:
    the defect must DECAY with t/√q, not merely stay away from 0.
- Dead ends (do not repeat; P63–P68, E96):
  - scalar moments (R12-S);
  - partial convolution along a fixed segment (R13-C);
  - fixed-order arithmetic (R13-M2);
  - centred Sanders powers (R14-CENTER);
  - fixed-dilate unions (R14-UNION);
  - low-degree symmetric SOS (E96);
  - equality exclusion by a fixed defect (P68.8);
  - parity alone (forces only E >~ q);
  - Galois separation (exponentially small);
  - positivity plus sparse frequencies without the Boolean plateau (the cos^{2d} example).
- Useful structure (lead, NOTEBOOK cont. 18.6–18.8). Peaks carrying the Parseval mass force the negative set 𝒩 to
  nearly avoid 2γ − 𝒩 for every heavy γ. This hints at approximate translation invariance and a single dilation
  direction, but 18.7(a) was refuted (windowed difference sets are flat), so it is HEURISTIC only.

## Task 1 (main): prove WRS(η) for some η > 0, or find the exact obstruction
Your round-15 report names the next discriminating derivation. A global estimate for the nonnegative remainder
    R_a = Σ_{β∉{0,a,2a}} h(β)h(2a − β)
that forces the WRS scale, using the full equation h⋆h = C0 at an ADAPTIVELY chosen, growing set of displacements.
Carry it out. Concretely:
1. Multi-displacement bookkeeping.
   - For the heavy core D (h >= L/2) and the near-saturated negative set, write the exact equations h⋆h(ξ) = C0 at
     all ξ ∈ D + D at once. Average them with weights you choose: by r_D(ξ), by h(ξ/2), or by powers of h.
   - Track exactly which products are forced to be large.
   - Small cores (s << q) need these equations to be nearly saturated by core–core terms. Large cores have an L²
     budget: Parseval gives sL² ≈ q²/4, and h⋆h = C0 everywhere off 0.
   - Decide whether "D + D covers ξ uniformly with r_D ≈ s²/q" is compatible with the half-set structure OFF D. The
     non-core values must make h⋆h EXACTLY flat as well.
   - Exploit the second-order interaction: the equation at ξ ∈ D + D involves h at ξ − β for β ∈ D, which is mostly
     the negative or near-zero bulk.
2. A second, genuinely different mechanism: the multiplicative (Gauss-sum) structure.
   - On G = Z_q^*/{±1} (cyclic of order h' = (q − 1)/2), λ = 1_B ⋆_G c with c(x) = 2cos(2πx/q). The multiplicative
     Fourier coefficients of c are even Gauss sums of modulus √q at every nontrivial even character.
   - So λ̂(χ) = 1̂_B(χ)τ(χ). The Chowla condition says this Gauss-phase rotation of the balanced Boolean function
     1_B − ½ on G is >= −K/√q·(√q-normalized).
   - Paley is the index-2 subgroup of G, i.e. a single character.
   - Question: does the one-sided condition force 1̂_B(χ) to concentrate on few characters, or force a quantitative
     Gauss-sum phase relation? Use Weil/Deligne-type bounds on sums of Gauss-sum phases, and the Hasse–Davenport
     product formula.
   - The exact interplay of the additive and multiplicative structure is what Z_q has and the R13 fakes lack. Say
     precisely which hypotheses the fakes violate.
3. Any other mechanism you judge stronger. Candidates: one-sided sign-uncertainty principles for Z_p
   (Gonçalves–Oliveira e Silva–Ramos type) combined with the Boolean plateau; entropy or compression arguments.
   Quote exact statements before use.
4. Adversaries, before investing in any lemma:
   - Paley (E = 0, K ≈ √q/2);
   - stored small-q optima (examples/zp_half/, examples/e90/, examples/r15_certificates/stability_probe.json);
   - R13-PK and R14-UNION random-profile sets;
   - the R12-S, R13-C and R13-M2 fakes, including the exact scalar counterexample of your round-15 B3;
   - every intermediate inequality must hold on genuine half-sets and must use Booleanity where the fakes fail it.
5. Deliverable for Task 1, one of:
   - WRS(η) for some explicit η > 0 (any exponent > ¼ for prime-cyclic half-sets is new relative to the project
     record; check JMTZ 2509.03490 and Sanders 0807.5104 before claiming novelty);
   - a conditional theorem with ONE named lemma strictly weaker than WRS that survives all the adversaries;
   - a precise obstruction: an explicit family of nonnegative even h satisfying h⋆h = (q²/4)δ_0 + C0 at all
     displacements in some stated growing set, consistent with every estimate you derived, at
     t ~ q^{1/4}·polylog(q). Say exactly which global equations it violates.

## Task 2 (bounded, at most about 20% of your effort): integer corollary bookkeeping
If Task 1 yields any η > 0:
- state the fixed-density version needed for the integer embedding (density α ∈ [1/(4C), ½]; P67's
  (1 − 2α)qλ term);
- decide whether the argument survives α ≠ ½ uniformly;
- give the integer corollary with exact quantifiers.
Otherwise state in one paragraph exactly where density ½ was used.

## Deliverable
The report, with proofs, adversarial tables and a final strategic recommendation: continue WRS, or pivot (and to
which mechanism). Say exactly what is new versus quoted.
