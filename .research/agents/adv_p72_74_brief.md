# Adversarial verification brief (codex): P72, P73 (T version), P74

You are an adversarial checker. Do NOT do new research; try to BREAK the three proofs below.
- Read CLAUDE.md (certification and quantifier rules) and .research/PROOFS.md sections P72, P73, P74.
- Rules:
  - Do NOT edit .research/*.md. Do not commit. Do not launch subagents.
  - Report: .research/agents/adv_p72_74_report.md. Scratch: .research/agents/adv_p72_74_scratch/.
  - All numerical computation goes on the VM:
        DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 <cmd>
    Never run heavy numerics on the laptop.

For each of P72 (a)–(e), P73 (T version and Z version) and P74:
1. Check every step and every quantifier. Normalizations: T = R/Z with Haar probability; 1̂_Ω(k) = ∫_Ω e(−kx)dx.
   Check:
   - Sion minimax applicability in P72(a);
   - the Parseval constant in P72(b);
   - Danskin in P72(c);
   - Macbeath/Raikov |A + B| >= min(1, |A| + |B|) for measurable sets on T in P73(T), including measurability and
     inner-measure issues;
   - Bernstein's inequality constant 2πL for frequencies in [−L, L] in P74;
   - the numeric constants (1/300, 2.5e-4).
2. Search for counterexamples numerically (on the VM).
   - P74: random and structured symmetric unions of arcs with 1̂_Ω(k) >= 0 for |k| <= L. Check
     U >= 2.5e-4·min(|Ω|, 1/L).
   - P73(T): random PD trig polynomials g and sets Ω; check ‖g − 1_Ω‖² >= δ²|Ω|/3 whenever g(0) < (4 − 5δ)/3.
   - P72(a): compare max_μ Σ(−c_a − τ|c_a|) (LP over measures on a fine grid) with min over weights (LP), for small A.
3. Verdict per item: CORRECT / GAP (state it exactly) / FALSE (give the counterexample). Keep the report current.
