# Adversarial check of P77 (centroid barrier for Boolean lifts) — codex agent brief

You are an adversarial verifier. Do NOT do new research. Your job is to find an error in P77 or confirm each step.
Read `.research/PROOFS.md`, section "## P77" (at the end of the file), and `.research/EXPERIMENTS.md` sections E116/E117.
Code: `src/e116_jl_taper.py` (lift, true_min), `src/e117_concentration.py` (λ_odd), `src/e114_cp_group.py` (jl_set).

Tasks:
1. Check every step of the proof of P77 (a), (b), (c) line by line: the identity e(z(g)·(χ+α)/n) = e(χ·g/n)e(z(g)·α/n);
   the derivative formulas for h_χ; the Parseval identity for Q_u(χ, t) at fixed u and t; the Cauchy–Schwarz over the
   four directions; the Taylor remainder; the choice of ω and the optimisation in ρ; S₁ <= (|B|S₂)^{1/2}; S₂ >= A2/2;
   Σ_χ|W|² = n²Σ|z|²; the concentration-operator bound in (b) (including the claim that W(0) = 0 and that odd real f
   has purely imaginary transform). State any missing hypothesis (e.g. injectivity of z, D symmetric, n odd?).
2. Numerically FALSIFY: on the VM (all computation via `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 3600 ...`,
   never on the laptop), for JL sets (p, a, j) ∈ {(3,2,1), (5,2,1), (7,2,1)} and also for random symmetric D ⊂ Z_n²
   (n ∈ {9, 15, 25}), generate >= 200 random one-rep lifts (reps in [−Vn, Vn]², V ∈ {1, 2}) plus the centred lift,
   compute K(T) by `true_min` (2D, FFT + BFGS) and the right-hand sides of (a) and (b) (compute λ_odd with
   e117_concentration logic for each D and B = {D̂ <= −r'} for r' = −max over the chosen B, or simply B = {χ ≠ 0 :
   D̂(χ) <= −r'} with r' = the background level). Report any instance where K(T) < RHS (a) or (b) beyond 1e−6.
3. Check the remark that the PD taper τ = Λ(z₁/n)Λ(z₂/n) gives Σ_{z≡g}τ(z)z = 0 and Σ_{z≡g}τ(z) = 1 for every class.
Write the report to `.research/agents/p77_check_report.md` (verdict per step: CORRECT / GAP / ERROR with details,
plus the numerical table). Do not edit any other file. Do not commit.
