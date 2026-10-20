# Full-cost W2 repair: a rigorous obstruction and a surviving certificate

20 October 2026. CHAIN / ATTACK LOG. This completes the direct proof attempt based on repairing a first-neighborhood bottom mode; it does not complete the universal full-W2 or Chowla proof. No new P/E identifier is assigned.

## Outcome and scope

- **PROVED, independently audited:** explicit Boolean integer supports have first-neighborhood certificate o(sqrt(N)). This is a local spectral statement, not a small global cosine minimum.
- **PROVED, independently audited:** an interval implant traps a unique first-neighborhood bottom vector. Its entire translated trial space is weak, and, separately, the entire odd full-W2 sector is weak. Even the complete exterior resolvent coupled to that bottom mode cannot repair it to square-root scale.
- **PROVED, independently audited:** the deterministic balanced-layer base nevertheless has K_W2 >= sqrt(N)/22 for every k>=1 and r>=4k^2. The bound transfers to the implant via a trial polynomial independent of the interval coordinate. Thus the example separates bottom-mode repair from full W2 rather than refuting full W2.
- **PROVED, independently audited:** a three-color decoupling argument also supplies random tapered weak-W1 supports. The formerly numerical weak-W1 premise is no longer being assumed.
- **OPEN:** a universal c>0 with K_W2(S)>=c sqrt(|S|), and the corresponding Chowla target. Neither finite numerical successes nor this restricted obstruction settle them.

Complete proofs, audits, scripts and data are in the [experiment archive](../experiments/groundstate_repair_2026-10-20/README.md). These are research paper proofs and independent algebraic audits, not formal kernel checks. “Proved” describes this research pass, not a claim of literature priority; no exhaustive novelty search was performed.

## 1. Definitions and the exact full-cost compression

Let S=-S be a finite nonempty subset of Z excluding 0, N=|S|=2|A|, D_S=sum_(s in S)e(sx)=2f_A(x), I={0} union S, W2=I+I. For a finite row set V, B_V has entries 1_S(u-v), and K_V=-lambda_min(B_V). The global K=-min D_S equals 2M; K_W2<=K. A weak local certificate is therefore not a counterexample to Chowla.

For a unit W1 bottom polynomial q with eigenvalue -k, set r=(D_S+k)q and R=||r||^2. The eigen-equation makes r vanish on I and gives <q,r>=0. For translates e_s q, s in I, define

    Gamma_st = integral |q|^2 e_(s-t),
    E_st = integral (D_S+k)|q|^2 e_(s-t).

Gamma is positive definite because multiplication by a nonzero Laurent polynomial is injective. The energy compression is exactly E-k Gamma. Thus K_W2>=k-lambda_min(E,Gamma), without discarding the exterior cost. For a pair of translates, with d=s-t,

    K_W2 >= k + |E_d|/(1-sign(E_d) gamma_d).

The identities sum_(s in S)gamma_s=-k and sum_(s in S)E_s=R give K_W2>=k+R/(N+k). This estimate needs much more than R of order N to supply a square-root increment. The exact q,r compression is

    [[-k, sqrt(R)], [sqrt(R), g]],  g=<r,D_S r>/R.

Its negative eigenvalue magnitude is (k-g+sqrt((k+g)^2+4R))/2. A large positive g cannot be replaced by zero or by a favorable norm surrogate. See [derivation](../experiments/groundstate_repair_2026-10-20/schur/translated_kernel_derivation.md).

## 2. Explicit weak-W1 balanced layers

Let T_(r,k) in Z^r have exactly k entries +1 and k entries -1. Put

    n=binom(r,k)binom(r-k,k),
    F_k=sum_(a=0)^k binom(k,a)^3,
    d=F_k binom(r-2k,k),
    e=F_k[binom(r-k,k)-binom(r-2k,k)].

On the noncentral rows, adjacency holds exactly when there is no opposite-sign overlap and exactly k equal-sign overlaps. The incidence matrix of signed k-subsets has Gram entries binom(c(s,t),k). Its difference E from adjacency is entrywise nonnegative, symmetric and regular with row sum e. Consequently ||E||=e and the noncentral minimum eigenvalue is at least -e. The full W1 matrix is the cone over this regular graph. Therefore, with

    kcentral=(sqrt(d^2+4n)-d)/2,

one has kcentral<=K_W1(T)<=max(kcentral,e). This is an enclosure, not equality for every finite r.

For the explicit diagonal r_k=ceil(4F_k^2 k^2), binomial-product bounds give e/sqrt(n)<=1/F_k and d/sqrt(n)>=F_k/2. Hence K_W1(T)/sqrt(n)<=2/F_k ->0. No unproved random premise, unspecified diagonal selection or uniform-in-k asymptotic error is used.

The base-7 encoding s -> sum_j s_j 7^j preserves all W2 adjacency relations: every tested relation has coordinate coefficients of absolute value at most five, so the highest nonzero place cannot cancel. These are genuine Boolean integer supports.

Sources: [full theorem, sections 6–6.1](../experiments/groundstate_repair_2026-10-20/schur/groundstate_product_no_amplification.md), [independent audit](../experiments/groundstate_repair_2026-10-20/audit/groundstate_product_obstruction_audit.md), [separate layer audit](../experiments/groundstate_repair_2026-10-20/translation/balanced_sign_weak_w1_independent_check.md).

## 3. The interval implant defeats bottom-mode repair

For any nonempty symmetric integer T, form S=(T x {0}) union ({0} x U_L), U_L={-L,...,-1,1,...,L}. For a sufficiently large absolute C0, choose L=ceil(C0 K_W1(T)).

The interval W1 matrix has an eventual simple odd bottom eigenvalue -k_L, with k_L/L ->2/(3pi). Its even bottom divided by L tends to -1/(2pi-arctan(3/4)). Their strictly positive difference gives a linear parity gap. This follows from norm convergence to the integral kernel 1[|x-y|<=1] on [-1,1], whose parity eigenproblems can be solved explicitly.

Eliminating the noncentral T block at diagonal k_L subtracts only a center rank-one form of norm at most K_W1(T). The odd interval eigenvector vanishes at the center, so it survives unchanged. The even gap dominates the correction, proving that the full W1 bottom is simple and exactly q_L(y).

Every permitted product q_L(y)p(x,y), p supported on I(S), has x-frequency support in I(T) for each fixed y. First-neighborhood positivity for T and D_U>=-2L imply

    K_translated(S,q_L) <= K_W1(T)+2L = O(K_W1(T)).

Separately, every odd-in-y W2 polynomial vanishes on rows with y=0. All rows with x outside I(T) have y=0, so the same argument proves

    K_W2,odd(S) <= K_W1(T)+2L.

The odd-sector obstruction and the translated-space obstruction are complementary, **not nested**: multiplying odd q_L by an odd multiplier produces even parity. The exterior coupling and every defined exterior resolvent preserve parity, so the old odd bottom mode cannot access an independent even negative direction. The statement does not use an inverse at a pole and does not control the even sector.

For the weak-W1 base above, both bounds are o(sqrt(|S|)). Encoding (t,u) as t+Qu with Q>5 max|T| preserves W1/W2 adjacency and product Gram/energy integrals. Parity becomes an inherited matrix involution after encoding, not necessarily ordinary scalar-frequency reflection.

Sources: [implant proof](../experiments/groundstate_repair_2026-10-20/schur/groundstate_product_no_amplification.md), [main audit](../experiments/groundstate_repair_2026-10-20/audit/groundstate_product_obstruction_audit.md), [odd-sector audit and wording correction](../experiments/groundstate_repair_2026-10-20/translation/interval_implant_odd_sector_audit.md).

## 4. Leakage is plentiful; its cost is hostile

With r_U=(D_U+k_L)q_L and n=|T|, the implanted residual satisfies exactly

    R=n+||r_U||^2,
    <r,D_S r>=integral D_T^3-k_L n+<r_U,D_U r_U>.

W1 positivity on the center/uniform two-dimensional subspace implies integral D_T^3>=n^2/K_W1(T)-K_W1(T)n. Also ||r_U||^2=O(L^2) and the final numerator term is O(L^3). Along the weak-W1 diagonal with L=O(K_W1(T)),

    R=(1+o(1))n,
    g >= (1-o(1))n/K_W1(T) >> sqrt(n).

Thus leakage of order N alone is insufficient. The same hypothesis making W1 weak forces a hostile positive residual cost here. A universal proof must not attribute all missing negativity to repairing this single bottom mode.

## 5. Full W2 survives: an exact square-root certificate on the same base

For T=S_k, let S_j be the j-balanced layer, S_0={0}, N_j=|S_j|, and psi_j=D_j/sqrt(N_j). For r>=4k, every S_j with 0<=j<=2k lies in S_k+S_k by an explicit canceling-coordinate completion.

Choose i+j=k and 2i<k. Multiplication by D_k on span{psi_i,psi_j}, divided by sqrt(N_k), is exactly

    [[0,a rho],[a rho,h eta]],
    a=binom(k,i),
    rho^2=binom(r-2i,2j)/binom(r,2j),
    eta=binom(r-2j,k)/sqrt(N_k).

For r>=4k^2, rho^2>=1/2 and 0<=eta<=1. For k=2m+1 take (i,j)=(m,m+1), giving h=2(m+1)a and a^2/(h+a)>=1/3. For k=2m take (i,j)=(m-1,m+1), giving a=m binom(2m,m)/(m+1), h=(2m^2+2m+1)binom(2m,m), and a^2/(h+a)>=1/11. The negative eigenvalue magnitude is at least a^2/[2(h+a)], hence

    K_W2(S_k) >= sqrt(N_k)/22.

The explicit weak-W1 diagonal already satisfies the finite-r hypothesis. No Laguerre-limit approximation or numerical eigenvalue enclosure is needed for this conclusion.

For the interval implant, use this base trial polynomial F(x), independent of y. It is supported on W2(T) x {0}, and integral D_U=0, so its energy is unchanged. Hence K_W2(S)>=sqrt(|T|)/22. Since |S|=|T|+2L=(1+o(1))|T| along the weak diagonal, this is a nonvanishing square-root bound for the implanted sequence too. It comes from the even sector and is inaccessible to the odd bottom-mode resolvent.

Source: [exact two-layer proof and Laguerre diagnostic](../experiments/groundstate_repair_2026-10-20/translation/balanced_layers_full_w2_certificate.md). The [independent audit](../experiments/groundstate_repair_2026-10-20/audit/balanced_layers_full_w2_audit.md) checks the finite-r bound and implant transfer.

## 6. Independent random tapered weak-W1 theorem

Select positive integers a<=X independently with p_a=2alpha(1-a/X), 0<alpha<=1/2, and reflect. With positive probability bounded away from zero as alpha(X-1)->infinity,

    |A| is comparable to alpha X,
    K_W1 <= C[alpha sqrt(X log(4X))+log(4X)+alpha^(-1)].

For X=t^4 and alpha=1/t, K_W1/sqrt(N)->0 in probability.

The proof separates at most three degenerate signclass collisions per row, then colors positive signclasses with three colors. Conditional on endpoint variables, the remaining lag variables are independent. Rectangular matrix Bernstein controls the masked noise with variance at most 4alpha times the selected endpoint count. The triangular mean kernel has the stronger lower bound P >= (2alpha/3)J, via interval-feature Cauchy–Schwarz; mere PSD would not suffice to control the added center. This proves weak W1 rather than extrapolating finite E99c curves.

Sources: [proof](../experiments/groundstate_repair_2026-10-20/obstructions/weak_w1_taper_proof.md), [independent audit](../experiments/groundstate_repair_2026-10-20/audit/weak_w1_taper_audit.md). Imported concentration result: [Tropp, Theorem 1.6](https://tropp.caltech.edu/papers/Tro11-User-Friendly-preprint.pdf).

## 7. Numerical evidence and exact countercontrols

The archive records dense/FFT translated-space tests, residual costs, interval implants, A50 and Singer controls. Explicit F*F and F*B_W2 F checks give discrepancies about 1.7e-16 and 1.8e-15 in the first sample. These checks validate assembly, not a universal lower bound.

At the largest beta=1/3 taper sample, |A|=8247, the numerical W1 ratio is about 0.49675, translated ratio 2.98793, R/N=1.07110, and g=-71.8114. At beta=.45, |A|=4079, g becomes positive (about 7235.987), with translated ratio about 1.459625. The beta=.45 target-8192 run stopped after groundstate diagnostics; no completed translated certificate is claimed there. Eigensolver residuals around 1e-7 are not certified spectral enclosures.

The exact A={1,2} example disproves ||Dq||^2>=N: its unique bottom eigenvalue is -phi and ||Dq||^2=3<4=N. It does not disprove an unspecified conditional leakage constant in the weak-W1 regime.

The Laguerre diagnostic computes exact integer limiting matrices and floating-point minima for k=1,...,10; the latter are diagnostics, not the proof of the finite 1/22 bound. No finite plot establishes a vanishing asymptotic ratio.

## 8. Honest remaining universal gap

The old single-bottom-mode repair principle is false, including a full parity-preserving exterior resolvent. A successful full-W2 argument may instead discover an independent exterior negative direction or an adaptive trial space unrelated to the original bottom vector. The balanced-layer two-level certificate proves this distinction on one explicit adversarial family only; no analogous quantitative direction is forced for arbitrary Boolean supports by the present argument.

Partial-translation Gram identities remain exact, but compressed translations need not commute. The exact S={-1,1} witness and the remaining gap are recorded in [partial_translation_gap.md](../experiments/groundstate_repair_2026-10-20/translation/partial_translation_gap.md). Neither those identities nor positive leakage alone prove a universal c. The all-mode Schur method itself is not refuted. A universal multimode/adaptive certificate for all Boolean S remains unproved; full W2 and Chowla remain open in this research.
