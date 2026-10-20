# Brief: adversarial verification of P78, P79, P80 (.research/PROOFS.md, end of file)

You are an adversarial checker. Do NOT do new research and do NOT edit PROOFS.md or any source file; write only
.research/agents/p79_check_report.md (and scratch files under .research/agents/p79_check_scratch/). No commits.
All numerical computation must run on the VM via `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 3600 <cmd>`
(bash; never compute on the laptop). Do not read *.log files under .research/agents/.

Check line by line, with the exact quantifiers:
1. P79 step 1 (free action, p+1 orbits, representatives) and step 3 (complete classification of D̂ for D_{2,j}, j ≠ 0;
   N ∖ 0 = N₁ ∪ N₂). Verify against src/e114_cp_group.jl_set(p, 2, j) exactly (set equality) for p = 3, 5, 7, 11 and all j.
2. P79 step 2 Gauss-sum facts, and step 4 (the block of the concentration form equals M*M/p²; normalisations, the
   φ_s = ψ̄(1 − pj⁻¹s) entries, the ψ̄(j) factor, |N₁|, |N₂|). Recompute λ_odd both ways for p = 17, 19 (src/e121_lambda_char.py
   does p <= 13; extend in scratch), and all j for p <= 11.
3. P79 step 5: the antisymmetric pairing (Youla) argument, including the antilinear J with J² = −1 and orthogonality.
   Step 6: the 2×2 bound, monotonicity in σ₁, the closed form Λ(p), and that Λ is decreasing with Λ(3) = (6+2√5)/12.
4. P78: Fejér/Poisson step (F_τ >= −r), the coupling of z(−g) = −z(g) with the law τ, Hoeffding constants, Lipschitz/grid
   constants, the union bound. Is the final inequality as stated correct? Test numerically: taper-random lifts must
   satisfy the bound (they will, by a wide margin; report the margin).
5. P80: P77(c) hypotheses (B nonempty symmetric, |z| <= √2Vn), the β >= 1/12 computation (verify the closed form and the
   inequality for p <= 13 exactly, and that it holds for EVERY one-rep lift, not only centred), and the final constants.
   Check the stated scope: it bounds the Z² minimum; say whether anything in the text overclaims for 1D images.
6. Try to break P79's bound: search for (p, j, ψ) with ‖M_ψ‖²/p² > Λ(p) (should be impossible), and report the
   max observed ratio λ_odd/Λ(p).

Report: verdict per item (CORRECT / GAP (with repair) / WRONG (with counterexample)), the exact scripts run, and the
numerical tables. Be concise.
