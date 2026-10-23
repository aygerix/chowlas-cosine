# Predeclared bounded R0 adversary, 2026-10-23

Question: does the SPECIFIC calibrated reciprocal witness fail on a
genuine Boolean support, even though its global M remains below sqrt(n)?
Maximize H0/(Q0 sqrt(n)), rather than minimize M. This changes the
objective from the previous successful-control and construction pilots.

Finite proposal box: n56, frequencies1..165, grid8192, four annealed
chains, at most3000steps/12000proposals, seed20261023. Start with the
existing n56 projection output. One-, two-, and four-frequency exchanges
are allowed; sample lowM cap .98sqrt(n). Following the PAPER-derived
qualitative-sign amplification corollary, and BEFORE any computation,
the early-stop target is positive normalized energy>.005. Otherwise
stop at the declared count. No box enlargement. Both the R0 numerical
margin and the weaker universal nonpositive-sign target are reported.

Floating proposals are followed by the existing Arb all-grid/Taylor
ALL-CIRCLE M certificate and the exact-residual INFINITE reciprocal
certificate at fixed lambda=2sqrt(n), band32maxA. Independently verify
the saved residual and selected inverse coefficients. A certified lower
quotient above-.01 refutes R0, while a negative upper below-.01 proves
only that the one saved output satisfies R0. Search failure establishes
no general principle and justifies no GPU run.

CPU budget: Dirichlet only,2cores/6GB,180seconds for search/certification,
150seconds for independent verification. Dirichlet will be started only
for these bounded jobs and stopped after artifacts are retrieved. No
RunPod use or credit spending. The paper tensor/padding theorem is
independently reviewed separately and is not inferred from this test.
