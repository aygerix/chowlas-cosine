# Full W2 falsification: deterministic rounding and multiscale supports

Date: 2026-10-20. This is a new computational and analytic pass, not a proof of universal Chowla.

## Conventions and outcome

For A⊂positive integers, S=±A, N=|S|, W2={0}∪S∪(S+S), and B(u,v)=1_S(u−v), report K=−λ_min(B) and K/√N. A counterfamily must make this ratio tend to zero. Small restricted Rayleigh quotients cannot establish that.

No such family was found. Two natural enlargement operations are ruled out rigorously below. Several deterministic triangular roundings and clustered enlargements fail numerically, with normalized full-W2 certificates increasing rather than disappearing. The distinction between these rigorous exclusions and numerical observations is essential.

## 1. Fixed geometric-orbit supports cannot falsify W2

**Theorem.** Fix an integer b≥2 and a finite nonempty R⊂positive integers with b∤r for every r∈R. Let S be any finite symmetric subset of

    {±r b^j : r∈R, j≥0}.

Write N=|S|, H=floor(log_b(2 max R)), and Δ=2|R|(2H+1). Then

    K_W2 ≥ (sqrt(Δ²+4N)−Δ)/2 ≥ sqrt(N)−Δ/2.

Consequently every growing sequence in a fixed collection of these geometric orbits has liminf K_W2/√N≥1. One need not include complete orbits or initial segments.

**Proof.** If u−v=w with u,v,w∈S, express their signed coefficients as primitive elements of ±R and their b-adic exponents as i,j,k. The smallest exponent must occur at least twice: if it appeared once, division by that power of b followed by reduction modulo b would give a primitive coefficient divisible by b. If all exponents coincide there is nothing to prove. Otherwise the two terms at the minimum exponent sum, with signs, to a coefficient of absolute value at most 2 max R, times the same power of b. Hence the largest exponent exceeds the smallest by at most H. For fixed u, each neighbor v in B restricted to S therefore has an exponent within H of u's and one of 2|R| signed primitive coefficients. Its degree is at most Δ.

The compression of B on {δ_0,N^(−1/2)1_S} is exactly

    [[0, sqrt(N)], [sqrt(N), a]],

where a is the average degree of the induced graph on S, so 0≤a≤Δ. Its negative eigenvalue has magnitude (sqrt(a²+4N)−a)/2, decreasing in a. Variational comparison proves the result. This is an actual lower certificate for the full operator, which is the direction needed to exclude counterfamilies. ∎

**Observed finite-size trap.** For the prior n=50 near-sharp seed A0 and A_J=∪_{j=0}^J 2^j A0, K/√N declines substantially over the measured range. This does not suggest an asymptotic failure once the theorem is applied: A0 has only 24 primitive odd parts, maximum 65. An exact enumeration over all exponent offsets −7,…,7 improves the crude uniform degree bound to 289; the bulk average degree is 132.5. These constants explain why the elementary asymptotic exclusion is not numerically strong at the tested sizes. The exact degree enumeration is in dyadic_proof.py and dyadic_degree.json.

This theorem does not cover a seed that grows with J. That remains a real loophole, not something the data close.

## 2. Symmetric interval-fiber blowups cannot amplify a seed deficit

**Theorem.** Suppose finite symmetric S⊂Z\{0} satisfies S⊂S+S. Set W=S+S, h≥0, q>5h an integer, and

    S'={q s+r : s∈S, −h≤r≤h}.

Then |S'|=(2h+1)|S|, W2(S')={q w+r : w∈W, −2h≤r≤2h}, and, in the unique indicated coordinates,

    B_W2(S') = B_W2(S) ⊗ T_h,
    T_h(r,t)=1_{|r−t|≤h},  r,t∈[−2h,2h].

Indeed the only possible digit discrepancy when testing an edge has magnitude ≤5h<q, so there are no carry aliases. The rowset equality follows from S⊂S+S and the fact that two interval digits fill [−2h,2h].

Consequently

    K(S') ≥ K(S) λ_max(T_h)
           ≥ K(S) [(2h+1)−h(h+1)/(4h+1)].

The second inequality tests T_h on its constant vector and counts ordered pairs with |r−t|≤h. Dividing by √|S'| shows that the normalized certificate grows at least on the order of √h times that of the seed. In fact the exact K is

    max(K(S) λ_max(T_h), λ_max(B_W2(S)) (−λ_min(T_h))).

The prior n=50 seed satisfies S⊂S+S. Exact Kronecker eigenvalues were checked against independently assembled full 1D FFT operators for h=0,1,2,4,8,16,32. Thus this common form of clustered enlargement rigorously cannot turn the small finite sharp-constant deficit into a zero-constant family. This does not rule out general adaptive clusters with varying fibers.

## 3. Numerical deterministic rounding tests

Take X=round(n^(4/3)), p_a=(2n/X)(1−a/(X+1)), 1≤a≤X. Actual n=|A| is measured after selection; target n is not silently used in normalization.

Families:

- Cumulative balanced rounding: select a when floor(1/2+Σ_{j≤a}p_j) exceeds its previous value.
- Golden rotation: select when {aθ}<p_a, θ=(√5−1)/2.
- Quadratic phase: select when {a²θ}<p_a.
- Independent uniform control, seeded deterministically.
- Centered golden/quadratic variants: select when 2 min({phase},1−{phase})<p_a.
- Two centered rotations: simultaneous conditions with phases aθ and a√2, each threshold √p_a.

The first four were run at target n=32,64,128,256,512,1024. The last three extend through 2048 and 4096. None trends toward zero in this range. Centering removes an unnecessary asymmetry but does not rescue the rotation construction. The rotation families have much larger negative certificates than the independent control. This is only numerical evidence about these explicit sequences, not an asymptotic proof.

## 4. Additional clustered tests

Using the same n=50 seed, L=1,2,4,…,128:

- Filled blocks: ∪_{a∈A0} ((2L+1)a+{0,…,L−1}).
- Tapered blocks: block a has max(1,floor(L(1−a/69))) entries.
- Dyadic unions, as above.

Filled and tapered block certificates grow rapidly; at L=128 the ratios are respectively 44.83185 and 40.68546. These asymmetric blocks are distinct from the exactly factored symmetric blowup in Section 2.

## Numerics and reproducibility

search.py assembles the entire W2 rowset using the integer self-convolution of 1_S, including {0}∪S explicitly. Integer convolution values are recovered by rounding, with maximum floating disagreement recorded. These checks are numerical safeguards, not formal interval certificates. FFT length exceeds 5 max A, avoiding cyclic aliases. scipy eigsh solves the full symmetric operator, not a small trial space, with tolerance 1e−9; eigenpair residuals are recorded for every run. Independent dense eigh comparisons are made for small cases. The source computations saved A, W2, eigenvectors and K. This text-only archive instead includes support JSON with A, K, W2 cardinality and a hash of the original W2 row array; eigenvectors are omitted. The scripts can regenerate the operators and eigenvectors.

verify_sparse.py independently constructs W2 by direct integer pair sums, assembles the sparse adjacency without FFT, and computes two lowest eigenvalues for the declining dyadic J=8 case. blowup_exact.py provides an independent Kronecker verification on all symmetric blowups.

Source files: search.py, centered.py, clusters.py, dyadic_extend.py, dyadic_proof.py, blowup_exact.py, verify_sparse.py. Raw numerical records: results.jsonl. These computations need only NumPy/SciPy, not Gurobi.

## What remains open

These results do not settle full W2, much less full Chowla. They exclude fixed-seed geometric replication and exact symmetric interval-fiber replication, and provide negative numerical outcomes for explicit deterministic roundings. A genuinely different adversarial family would need, for example, a growing primitive seed and carefully correlated varying fibers rather than these fixed templates. No universal lower bound is claimed.

## Selected raw results

|Family|Actual n|Full rows|K/√N|Residual|
|---|---:|---:|---:|---:|
|tri_cumulative_1024|1024|35699|3.671880989|8.8e-09|
|tri_golden_1024|1023|12107|20.561945423|5.1e-09|
|tri_quadratic_1024|1061|36119|3.497483319|2.5e-08|
|tri_random_1024|1028|35407|3.437275541|1.9e-08|
|tri_golden_centered_1024|1023|8163|7.253305881|1.9e-07|
|tri_quadratic_centered_1024|1061|36077|2.984588552|9.8e-08|
|tri_two_rotations_1024|1019|15715|4.585726995|3.4e-08|
|tri_golden_centered_4096|4095|32717|14.467318364|2e-10|
|tri_quadratic_centered_4096|4210|234073|3.578729171|4.4e-10|
|tri_two_rotations_4096|4092|64491|9.199987155|4.6e-07|
|dyadic_extended_J8|242|21587|2.070612886|1.7e-08|
|dyadic_extended_J9|266|31811|1.975431805|1.6e-08|
|dyadic_extended_J10|290|44339|1.907825736|4.5e-08|
|dyadic_extended_J11|314|59171|1.863968530|1.2e-08|
|dyadic_extended_J12|338|76307|1.819337578|3.5e-08|
