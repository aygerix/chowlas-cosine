# Exact residue-balanced lifts: a full-W₂ falsification test

Date: 2026-10-20. Scope: new correlated finite-group lifts, not independent product-Fejér rounding or restricted fixed-profile trial spaces.

## Finding

No vanishing-ratio construction was found. Two strongly dependent families whose finite quotient has negative spectral minimum exactly 1 retain a square-root-sized (or larger) negative spectral minimum after lifting to integers and using the FULL W₂ operator. This is numerical evidence about these families, not a universal theorem, not a proof that full W₂ works, and not exhaustion of correlated lifts.

The strongest tested algebraic family has N=8,010 and |W₂|=30,105. Its full numerical spectral ratio is K_W₂/sqrt(N)=0.94395601895. Restricting to an optimized or prescribed trial space was never used to declare a small full-operator value.

## Definitions and exact finite quotient

S is symmetric, excludes 0, N=|S|, D(x)=sum_{s in S} exp(2πisx). W₂={0} union S union (S+S); B(u,v)=1_S(u-v), and K_W₂=-lambda_min(B).

For an odd q, take exactly one symmetric integer representative of every nonzero residue. Then N=q-1 and D(k/q)=-1 for k=1,...,q-1. The finite cyclic quotient adjacency matrix is J-I, with negative minimum 1 and normalized ratio 1/sqrt(N) tending to zero. The purpose of the experiment is to see whether strongly correlated representative choices preserve that small negative spectrum in the integer W₂ lift.

## Family 1: balanced triangular quotient histograms

For r=1,...,(q-1)/2, set a_r=r+q h_r and S={±a_r}. The h_r are rounded equally spaced quantiles of the triangular distribution on [-H,H], with H=round(sqrt(q)). Assignment to residues is varied without changing the histogram:

- seeded random permutation;
- permutation by quadratic residues r² mod q;
- bit reversal;
- sorted assignment;
- alternating assignment.

All have exact Booleanity and the exact finite quotient above. Shared histogram constraints break coefficient independence. At q=31,61,127,251, random assignments give K/sqrt(N)=2.00491,2.32904,3.18542,3.09879. Quadratic assignments give 2.34656,2.46508,2.70043,3.14808. Bit reversal, sorted and alternating are worse, reaching ratios 6.09,7.33,6.44 respectively at N=250.

Larger random and quadratic assignments:

| N | Random K/sqrt(N) | Quadratic K/sqrt(N) |
|---:|---:|---:|
|508|3.30517945|3.61077992|
|1020|3.77445831|4.43608933|

### Targeted adversarial optimization

A simulated-annealing search swaps two h-values, preserving every residue and the triangular histogram. It uses full-W₂ smallest-eigenvalue evaluations, not a fixed profile. Budgets: 1,500,1,500,1,200,800 proposals for N=30,60,126,250. These are heuristic searches, not globally optimal assignments.

| N | Best K/sqrt(N) |
|---:|---:|
|30|1.36952325|
|60|1.62675722|
|126|2.16608325|
|250|2.56958370|

The optimized family still gives no decreasing-ratio lead. The full representative lists are reconstructible from the saved h arrays.

## Family 2: Singer perfect difference-set lifts

Let p be prime, q=p²+p+1, and T⊂Z/qZ be a Singer perfect difference set of size p+1. Construct it as the exponent classes k in [0,q) for which Tr_{F_(p³)/F_p}(α^k)=0, with α primitive. Choose those exponent integers as representatives, and set S={t-u:t,u∈T,t≠u}.

Exact properties, verified directly in the implementation:

1. Every nonzero residue mod q occurs exactly once as an ordered difference, so all integer differences are distinct, N=p(p+1), and S is Boolean and symmetric.
2. On the circle, D(x)=|sum_{t∈T} exp(2πitx)|²-(p+1). Hence the global negative minimum satisfies K_global≤p+1, rigorously. In particular K_W₂/sqrt(N)≤sqrt((p+1)/p).
3. The quotient still has K=1, despite the strong endpoint dependence among integer coefficients.

Full-W₂ numerical results:

| p | N | K_W₂/sqrt(N) |
|---:|---:|---:|
|2|6|0.93917049|
|3|12|1.02516245|
|5|30|0.87939746|
|7|56|0.93105216|
|11|132|0.93977382|
|17|306|0.95289235|
|23|552|0.96146774|
|31|992|0.93865336|
|47|2256|0.94729642|
|61|3782|0.94907542|
|89|8010|0.94395602|

The finite quotient's vanishing ratio has not survived the integer lift. The exact global upper bound and observed full-W₂ lower certificates squeeze these examples into a square-root regime, without proving an asymptotic limit.

### All cyclic cuts

Replacing T by (T-t) mod q, for each t∈T, exhausts distinct choices of the cut of this cyclic difference set, up to integer translation between cut transitions. Every cut was tested for p=7,11,17,23,31. The minimum ratios across all cuts are respectively:

0.91679844, 0.92956707, 0.91908230, 0.91730849, 0.93407252.

Cut choice alone provides no evidence of decay. This is not an exhaustive search over multipliers, all perfect difference sets, or arbitrary lifts.

## Full operator, support verification, and numerical limits

For R=max|S|, a zero-padded cyclic convolution with grid length at least 6R+1 realizes the integer matrix exactly on W₂: W₂⊂[-2R,2R], so its differences are in [-4R,4R], and circular wrap cannot introduce an S-edge. No finite-quotient adjacency is substituted for the integer matrix.

The W₂ support inferred from FFT integer convolution was independently checked by exact Python-integer bitset sums for all 11 Singer cases and all 4 optimized balanced lifts. All 15 checks passed. Two small full matrices were separately formed entry by entry, and dense eigenvalues agreed with the FFT/Lanczos results to better than 1e-8.

Final eigenvalues use scipy eigsh, smallest algebraic eigenvalue, deterministic initial vector, tolerance 1e-8. The largest Singer residual is about 8.4e-7. A small residual does not by itself certify that no lower eigenvalue was missed. These are full-operator numerical estimates, not interval-certified spectral upper bounds. Every computed vector nevertheless supplies a genuine full-space Rayleigh lower bound for K up to floating-point error. No numerical result here is claimed as a rigorous counterexample to the universal spectral conjecture.

## Interpretation and missing ingredient

This experiment isolates lifting, rather than generic independent Bernoulli noise: both families have exact quotient balance, and Singer supports have a strong algebraic square-modulus identity. Neither produced a full-W₂ escape. It remains possible that a more adaptive representative assignment, a different finite-group design, or a family with controlled carry correlations can suppress the integer negative spectrum. The finite quotient spectrum alone cannot establish that.

A positive theorem suggested by, but NOT established by, these data is: every symmetric complete-residue lift has K_W₂≥c sqrt(q). Such a theorem would exclude this branch, not settle Chowla. Conversely, a rigorously certified family of complete-residue lifts with K_W₂=o(sqrt(q)) would refute full-W₂ universality while leaving Chowla open. No such construction or general theorem is supplied here.

## Files

- lifts.py; balanced_lifts.json; large_lifts.json: explicit families and unoptimized full spectra.
- optimize_lifts.py; optimized_results.json; optimization.log: residue-preserving search, winning h arrays, budgets.
- singer.py; singer_results.json: finite-field construction, integer T lists, spectra.
- singer_cuts.py; singer_cuts_results.json; singer_cuts.log: all-cut tests and winning T lists.
- validate.py; validation.json: independent entrywise dense checks.
- check_supports.py; support_checks.json: exact W₂ bitset checks.

Run scripts from this directory with OPENBLAS_NUM_THREADS=1. They use NumPy and SciPy, not Gurobi or gurobipy. The default lifts.py output name is lifts_results.json; archived named copies preserve each completed batch. These are local research results; no external push is part of this checkpoint.

## Addendum: Boolean collapsed difference supports

A third dependent family takes a seeded uniform m-subset T of {0,...,X-1} and S=(T-T)\{0}, discarding multiplicities. Write λ=m²/X. This is genuinely Boolean, but unlike the Singer family repeated integer differences occur and are collapsed.

| m | λ=1 ratio | λ=1/4 ratio | λ=m^(-1/2) ratio |
|---:|---:|---:|---:|
|16|1.51389646|1.49149987|1.52225463|
|32|1.72684086|1.45488369|1.38750256|
|64|1.92678870|1.66938436|1.50047565|

The two λ=1/4 cases at m=16 are independent seeded realizations, not duplicate calculations. The sparsest largest case has N=3,874, |W₂|=111,595, and residual 7.9e-7. There is no decreasing-ratio trend supported by these three scales. These few samples do not establish a distributional or asymptotic assertion.

Exact algebra explains one limitation of the construction. If r(s) is the ordered difference multiplicity and E(s)=r(s)-1 on S, then D_S=|F_T|²-m-D_E. Therefore K_global≤m+sum_s E(s)=m+[m(m-1)-N]. This is an exact upper bound, but it does not make the normalized ratio tend to zero and can be very loose when collisions are common. The square-modulus identity alone cannot supply the desired full-operator counterexample.

Files: collapsed_differences.py, collapsed_results.json (including T and collision counts), collapsed.log. Independent exact bitset checks have now passed for these nine supports too, 24 checked supports in total. The report's conclusion remains unchanged: no asymptotic counterfamily is established; all three dependent constructions remain unproved in their untested asymptotic regimes.
