# Literature (versioned, concise) — read 2026-10-17

## Limited source/novelty check after the cubic-envelope result (2026-10-23)

A targeted arXiv search for the dense cosine problem with exponent1/3
and the constants400/29,13.793 or13.698 returned no matching exact
claim. This is NOT a priority check sufficient for publication and
does not establish novelty. The result is reported as an extension
of the repository's P66/P68 theorem, independently internally audited.

The primary [Bu et al. abstract, arXiv2610.17160v1](https://arxiv.org/abs/2610.17160v1),
submitted12Oct2026, was reopened. Its dense lower-bound statement is
exponent1/4 for supports inside[1,Cn]; the same abstract states a
mixed L1/cubic inequality. No claim about absence of stronger results
elsewhere follows from this limited search. The new proof depends
on the already-audited P58-P68 inputs and a fresh exact certificate,
not on an unverified literature decimal or search absence.

## Scoped source checks: conditional discrepancy and the quadratic floor (2026-10-23)

Larsen, *Fast Discrepancy Minimization with Hereditary Guarantees*,
[arXiv2207.03268v2](https://arxiv.org/pdf/2207.03268v2),24Nov2022,
PDFp2/printedp1, Introductionitem2: directly reverified the REAL
square-matrix Spencer bound |a_ij|<=1,disc(A)<=6sqrt(m). The
old author-hostedHereditary.pdf URL returned404 this cycle; the
versioned primary arXiv text was accessible. Only this classical
existence input is used; no algorithmic claim from later theorems.
The arbitrary-fractional dyadic argument and bounded-component
conditional-observable extension are derived in the new proof record.

Bedert, [2509.05260v3](https://arxiv.org/html/2509.05260v3),24Jul2026,
Section7,equations36–38: rechecked the Fourier-square convention,
the generic16K² self-convolution floor and its use in the pointwise
even/odd inequality. No claim is made that the new sharpness family
resolves the later truncation or averaged-boundary bottleneck.

Local P19 PropositionC's source labels its finite cases certified
and asymptotic explanation HEURISTIC. The new integer rounding
theorem supplies a uniform quadratic-loss family by a different
mechanism; no Singer asymptotic constant or publication priority is
claimed. A limited targeted search is not a novelty certification.
[Proof, dependencies and exact scope](notes/modulated_triangle_2026-10-23.md).

## Scoped source check: phase stability (2026-10-23)

Ephremidze--Shargorodsky--Spitkovsky,
[scalar spectral-factor continuity, v2, Theorems1--2](https://arxiv.org/html/1603.01101v2),
was inspected in primary text. Its perturbation results concern
the OUTER factor; they do not establish a uniform choice among
all polynomial root-reflection branches. They were not used to
infer scalar closeness from a near-square signal.

Bu et al., [v1 Proposition2.1 and Theorem1.2](https://arxiv.org/html/2610.17160v1),
were rechecked for the precise two-sided identity and construction
upper bound; Sections3--6 give ambient spanO(k²). Combined with
the repository's P16' lower theorem this supplies the cited
near-square asymptotic in the new certificate-class no-go.
No external novelty claim or broad absence-of-prior-art claim.

## Bounded priority check: exact power rigidity (2026-10-23)

Six targeted queries on reciprocal0/1 polynomial powers, a free
central coefficient, and rational critical-value denominators did
not establish a priority result. A related lead was Kolountzakis,
[arXiv:0806.1809v2](https://arxiv.org/abs/0806.1809v2), abstract
and version metadata inspected only. Its abstract concerns maximum
coefficients/sparsity of squares whose ROOT has0/1 coefficients;
it does not state the exact central-exception condition considered
here. The author notice acknowledges stronger prior work by
Cilleruelo and asks not to cite the preprint; it is recorded only
as a search lead, not used as a theorem or priority reference.
A related Dubickas PDF fetch failed, so its contents were not read.

The new internal proof uses elementary valuation comparisons and
has independent internal review. This bounded check establishes
neither novelty nor absence of prior art. No manuscript, submission
or specialist outreach follows.

## Bounded primary-source check: growing multiplicity (2026-10-23)

Kravitz, [Generalized difference sets and autocorrelation integrals,
arXiv:2004.06611v1](https://arxiv.org/html/2004.06611), introduction
and Theorem1.2, relates minimum-size g-difference coverings of a
fixed interval to a continuous autocorrelation extremum, in iterated
limits g then interval size. This is distinct from the all-class
l1 defect on an arbitrary positive difference support considered
here. No theorem from that paper is needed for the new elementary
centroid bound. Xu, [Popular differences and generalized Sidon sets,
v5](https://arxiv.org/abs/1706.05969v5), abstract inspected only,
studies the maximum representation count on a short difference
interval; its full proof was not reviewed in this bounded check.

These are related antecedents, not a priority determination. The
general defect bound and weighted extension are paper-proved and
internally audited; external novelty remains unassessed. No broad
absence-of-prior-art claim follows from the two targeted searches.

## Targeted check: finite Fourier normalization for Sidon shift moments (2026-10-20)

Tao, [247B Lecture Notes9, Q3, p.13](https://www.math.ucla.edu/~tao/247b.1.07w/notes9.pdf), states finite-group Hausdorff-Young with probability measure on the group and counting measure on its dual. By duality, inverse Fourier synthesis maps counting l^(6/5) to probability L^6 with norm<=1. This is the classical ingredient used in the new cyclic-shift estimate; alternatively apply Plancherel and three-fold Young convolution. The primary source was read for this exact normalization, without a novelty/literature-wide claim. The Sidon-fiber mixed-certificate result has its own [paper derivation](notes/cstar_sidon_mixed_2026-10-20.md).

## Targeted check: singular integer matrix counts (2026-10-20)

Chapman–Mudgal, *Counting 2x2 integer matrices with a given determinant*, [arXiv:2509.20259v1](https://arxiv.org/html/2509.20259v1), introduction following Proposition 1.3: the h=0 box count is (16/zeta(2))X^2 log X+O(X^2). This matches the independent elementary count used here; the counting surplus is not claimed new. The construction-side resonance exclusions have separate derivations in the [integer-cone note](notes/cstar_integer_cone_2026-10-20.md). No literature-wide novelty conclusion was drawn from the narrow search.

## Targeted check: real-matrix discrepancy (2026-10-20)

Larsen, *Fast Discrepancy Minimization with Hereditary Guarantees*, [primary paper](https://cs.au.dk/~larsen/papers/Hereditary.pdf), introduction: Spencer's square-matrix theorem applies to real entries of absolute value<=1 and gives discrepancy<=6sqrt(m). Lovett–Meka, [arXiv:1203.5747v2](https://arxiv.org/pdf/1203.5747), Theorem 4, verifies the arbitrary-vector/starting-point partial-coloring formulation. The forced-plateau proof derives the required fractional rounding directly by dyadic rounding and square padding; it does not infer a real-matrix theorem merely from an incidence-matrix abstract. [Application and scope](notes/cstar_forced_plateau_2026-10-20.md).

## Targeted check: partial majorants (2026-10-20)

Fournier–Vrecko, *Minimal Fourier majorants in L^p*, [arXiv:2112.13799v1](https://arxiv.org/html/2112.13799v1), Section 2, Lemma 2.3 / Corollary 2.4. Verified the finite-support partial-majorant variational structure for general 1<p<infinity. Our mean-zero p=4 problem requires an additional free constant multiplier. The special full-majorant conclusion at p=4/3 must not be applied to equality completion at p=4. [Own derivation and weighted sign countercontrol](notes/cstar_partial_majorants_2026-10-20.md).

Convention in this project: f_A(x) = sum_{a in A} cos(a x). Papers using cos(2 pi a x) have identical minima.

## Epoch problem statement (fetched 2026-10-17)
https://epoch.ai/frontiermath/open-problems/chowla-cosine
- Task: for every c>0, n>=1 produce a SET A of positive integers, |A|>=n, f_A(x) >= -c sqrt|A| for all real x.
- `solution(c: float, n: int) -> str`, distinct positive decimal integers separated by whitespace/commas.
- Verifier is numerical sampling; recommends max(A) well under 1e6 (lower for small c). "No known example achieves c <= 1/20."
- If Chowla is true the problem is unsolvable.

## Upper bounds (constructions)
- Classical Sidon-difference: A=(B-B)^+, B Sidon |B|=k: f_A = (|F_B|^2-k)/2 >= -k/2, R -> 1/sqrt2. Reproduced (EXPERIMENTS E0).
- Mercer (Integers 19 (2019) A4, Fact 2.1): lambda(m) <= sqrt(2m)+1/2 for all m (padding). Exact K(n) known only n=2,3 (Mercer 2012, arXiv:1206.5012).
- **Bu, Khan, Yi, Jha, Vajpeyi, Chandupatla, Nagpal, arXiv:2610.17160v1 (12 Oct 2026)** "A Half-Constant Upper Bound".
  * Identity (Prop 2.1): S Sidon, |S|=k, A(S)={3|s_i-s_j|} ∪ {|3(s_i+s_j)+1|}, |A|=k(k-1):
    f_A(x) = rho(x)^2 - k/2 - g(x)/2, rho = sum cos((3s_j+1/2)x), g = sum cos((6s_j+1)x).
  * S = random tent-weighted thinning of a shifted Singer set, with an odd-offset "parity block" deleted; Fejér majorant controls g.
  * Thm 1.3: lambda(n) <= sqrt(n)/2 + O(n^{1/4} sqrt(log n)). Asymptotic only (q >= ~1e5). Numerics uncertified; R=0.635 at n=25440.
  * §8: L^4 criterion lambda/sqrt n = M2/sqrt(2(M4 - M2^2 - M(h^2))) for lambda+f = |P|^2 - h; constant-modulus P needs multiplicity m>2 per frequency to beat 1/2 (Prop 8.2). Authors: below 1/2 "appears to require an idea outside the square-identity paradigm".
  * Agent read full text and hand-checked §§2,3,5,6 (internal check only).

## Lower bounds
- Chronology: Uchiyama–Uchiyama 1960 (->inf); Roth 1973 ((log/loglog)^{1/2}); MPS/Konyagin 1981 (log n); Bourgain 1984/86 (exp((log n)^eps)); Ruzsa 2004 (exp(c sqrt log n)); Sanders 2010 (poly, frequencies O(n)).
- JMTZ arXiv:2509.03490v2 (27 Oct 2025): n^{1/10-o(1)} via Cayley graph small-eigenvalue => large clique. Caps at 1/6 even with conjectured optimal clique theorem (agent's analysis).
- **Bedert arXiv:2509.05260v3 (24 Jul 2026)**: n^{1/5-o(1)}. Key: Lemma 4.1 (Roth: E ⊂ A, |E|>=2K^2 => #{(u,v) in E^2 : u-v in A} >= |E|^2/(2K)); Prop 7.3: |B_t| <= C0 K^4 for B_t = A_t \ (-A_t), A_t = A∩(A+t) (A symmetric); Lemma 7.4: some t with |B_t| >> n/(K log^4 n). The K^4: (one self-convolution K^2) x ||H||_1^2 and ||Q2||_2^2 = K^4.
  * Agent's observation: the two-step scheme (max_t |B_t| <= K^a, some |B_t| >= n/K^b) caps at 1/(a+b) >= 1/3 since a>=2 (dense Sidon, exact counts p<=41) and b>=1 (lacunary Sidon {2^i}).
- **Shankar arXiv:2609.05338v1 (4 Sep 2026)**: K(N) >> N^{1/5} (log-free). Exact identity sum_{t in A}|B_t| = 6Q - 4I >= T/3 replaces Bedert Lemma 7.4. Read in full; short; argument checked here line-by-line (it is elementary given Bedert's Props).
- Yip arXiv:2610.01657v1: >> n^{1/6.43} (cited by Bu et al.; not read).
- Belov–Konyagin: multisets with coefficients in {1..O(log^3 n)} can have min >= -O(log n)^3 (cited by Bedert) — set-ness is essential.
- 2026-10-18 novelty check for C½ (alphaXiv discover "Chowla cosine problem", recency): only 2610.17160, 2609.05338,
  2509.05260, 2509.03490, 1206.5012 relevant; none states a sharp-constant 1/2 conjecture (Bu et al. say going below 1/2
  "appears to require an idea outside the square-identity paradigm"). Absence of a hit is not proof of novelty.
- JMTZ 2509.03490 (ETH/Stanford): every graph with average degree d and |λ_min| <= d^γ contains a clique of size
  d^{1−O(γ)}; corollary gives the first polynomial Chowla bound. Our P9 star lemma is the elementary special case of
  their induced-subgraph viewpoint.
- 2026-10-18 search 'Newman polynomials minimum modulus unit circle' (alphaXiv): no result on lower-flat 0/1 (Newman) or Sidon-support polynomials; nearest: flat Littlewood polynomials exist (BBMST 1907.09464). SNZ novelty unverified.

## References used by P16 (2026-10-18)
- B. Lindström, "An inequality for B_2-sequences", J. Combin. Theory 6 (1969) 211–212: a Sidon set in {1,…,n} has fewer
  than n^{1/2} + n^{1/4} + 1 elements (used for the visit-lemma counting; the trivial bound k(k−1)/2 <= n−1 also works with
  worse constants).
- Triangle (Fejér) kernel transform: ∫ (1/h)(1−|y|/h)_+ e^{iνy} dy = (sin(νh/2)/(νh/2))^2 (standard).
- Novelty of P16: independent agent checking Bu et al. 2610.17160 and citing literature (report .research/agents/p16_review.md).
- Kahane's ultraflat unimodular polynomials (J.-P. Kahane, "Sur les polynômes à coefficients unimodulaires", Bull. LMS 12
  (1980) 321–342) show that 2-D "visit" statements need arithmetic input (NOTEBOOK 2026-10-18).
- Profile constant ρ* (E16): sup ||h⋆h||_2^2/(||h⋆h||_∞ ||h⋆h||_1) over h with h⋆h >= 0 (doubly-positive profiles; w depends
  only on |ĥ|^2, so real even h is fully general). This is the autoCORRELATION analogue of the Martin–O'Bryant /
  Matolcsi–Vinuesa autoCONVOLUTION constant (>= 0.8892, Matolcsi–Vinuesa 2010; best constant 1 for signed f, de Dios Pont–
  Madrid arXiv:2106.13873 §5). de Dios Pont–Madrid treat ∫∫ f f w <= C||f||_1||f||_2 (C ≈ 0.8056 box, 0.7152 Gaussian
  weight) — a different functional. Our ρ* ≈ 0.7239 (h >= 0), 0.7245 (signed, slightly infeasible): not found in the
  literature in this form (quick check only, 2026-10-18).

## Littlewood cosine polynomials (signed / free-phase analogue) — read 2026-10-18
- Erdélyi, arXiv:2607.21877v1 (24 Jul 2026) claims max T_n >= n^{1/3}/60 and −min T_n >= n^{1/3}/60 for every
  T_n = Σ_{j=1}^n cos(jt − θ_j) (unit amplitudes, full support; includes ±1 cosine polynomials). Remark 2.3:
  max(max T, −min T) >= (n/4)^{1/2} trivially.
  **Lead's check: the proof of Thm 2.1 has a gap (v1).** The display after (4.15) bounds Σ_E ∫_E|T'|^2 by
  (∫_0^{2π}|T'|)·Σ_E m(E)·max_E|T'|, but (4.3) only gives ∫_E|T'|^2 <= (∫|T'|)·max_E|T'| (no m(E) factor); the m(E)
  factors do not follow. The chain uses only −n <= T <= δ, deg T <= n, ∫T = 0, and would give
  ∫|T'|^2 <= 4π^2·12.26·n^{5/2}δ^{3/2}. T = 1 − F_n (F_n = Fejér kernel) meets these hypotheses with δ = 1 and has
  ∫|T'|^2 = πΣ_{j<n} 4j^2(1−j/n)^2 ≈ 0.419 n^3 > 484 n^{5/2} for n >= 2e6 (checked numerically: n = 2e6 gives
  3.35e18 > 2.74e18). Correcting the step (keeping ∫_E|T'| instead) loses everything: the region {T <= −n/4} can carry
  all of ∫|T'|^2 with δ = O(1). Whether the n^{1/3} statement is true for unit-amplitude T is open to us. Not used
  anywhere in this project.
  **SUPERSEDED (lead 2026-10-19, P34).** The P31 window–Nikolskii chain with general coefficients gives
  −min T_n >= 0.28√n and max T_n >= 0.28√n for every T_n = Σ cos(jt − θ_j). Even the trivial Nikolskii constant gives
  0.189√n. This is the sharp order (Rudin–Shapiro). Erdélyi's introduction lists only exp(c√log n)-type bounds for ±1
  maxima ([Er11], via Ruzsa [Ru04]) and Theorem 1.2 (L¹ / McGehee–Pigno–Smith). No one-sided √n bound appears there. (An adaptation to dense 0/1 sets A ⊂ [1,X] would have given M(A) >> N^{5/3}/X^{4/3}; it
  fails for the same reason.)

## Minimum modulus of 0/1 (Newman) polynomials — relevance to Sidon differences (quick check 2026-10-18)
- For Sidon B (|B| = k), A = positive differences: min|F_B|² = k − 2M(A), so C½ restricted to Sidon differences is
  EXACTLY min_x |F_B(x)|² <= (1 − 1/√2 + o(1))k ("SNZ-weak", STATE line 1). A general theorem "Newman polynomials have
  min modulus o(√k) on the circle" would settle the whole class (R -> 1/√2).
- Status found: open. Mercer (Integers / "Newman polynomials not vanishing on the unit circle", via math.colgate.edu
  m67) defines µ(n) = max over n-term Newman polynomials of min_{|z|=1}|P| and conjectures µ(n) -> ∞, perhaps like a
  power of n; known: n-term Newman polynomials without unimodular roots exist for every n > 2; Boyd's degree-12
  example with min > 1; smallest degree with min > 2 is 38 (Springer s40598-019-00102-1). No o(√n) upper bound known
  to us. So no free result: SNZ-weak must be proved using the Sidon property (E8/E12/E15/E29 numerics: c -> 0).
- Contrast: flat ±1 (Littlewood) polynomials exist, δ√n <= |P| <= Δ√n (Balister–Bollobás–Morris–Sahasrabudhe–Tiba,
  arXiv:1907.09464). Their autocorrelations are not 0/1, so this does not transfer to cosine sums with unit
  coefficients; it does show "flat from below" is not forbidden by L²/L⁴ considerations alone.

## Group analogue of Chowla (context for P20/P21; quick check 2026-10-18)
- Sanders, "Chowla's cosine problem", arXiv:0807.5104 (2008): for finite G and symmetric A with |A| ≍ |G|, either A is
  close (small symmetric difference) to a subgroup, or some nontrivial character has −1̂_A(χ) >= |A|^c. In groups
  M_Γ(A) = 0 for subgroups, so Chowla fails; only the near-subgroup dichotomy survives. JMTZ (2509.03490) restate the
  stability form. A Fields talk "Chowla's cosine problem in abelian groups" exists (not read).
- Consistency with P20/P21: our K³ sets are dense, |A| = (1 − 1/p)|Γ| with complement ≈ |Γ|/p, i.e. near-subgroup
  (near Γ itself), and K ≍ |Γ|^{1/4}, matching Sanders' dichotomy. No literature found on run-tops (B_t) in groups;
  the P19–P21 questions appear to be ours. Partial-difference-set / two-weight-code literature (quadric complements
  have the familiar three-valued spectrum) not searched.
- Novelty check for P22 (2026-10-18 night; arXiv HTML of Bedert 2509.05260v3 and Shankar 2609.05338v1). Neither paper
  discusses sharpness of |B_t| << K⁴, finite-group or finite-field models, or barriers. Bedert §1: "It seems plausible
  that our method can produce an even better exponent than 1/5." Shankar §5 names two ways past 1/5: "a stronger exponent
  than K⁴" in the run-top bound, or "additional information showing that many boundary sets are simultaneously large".
  P22 (Theorem O4 + E36b) answers both for group-agnostic arguments. In O4, |B_t| = K⁴/4 − K²/2 for one t, and the average
  of |B_t| over t ∈ A is ≈ K⁴/8, so many boundary sets are simultaneously large there. Any improvement must use Z.
  Galois-ring relative difference sets are classical (Hammons–Kumar–Calderbank–Sloane–Solé 1994; Ma–Schmidt on
  (2^a,2^a,2^a,1)-RDS, which as I recall need exponent <= 4, so they are not cyclic for a >= 2; this recollection is NOT
  verified). Their use as run-top extremisers was not found in these two papers. No wider search was done.

## Dense case in Z (quick novelty check 2026-10-19, one extended web search)
- No Chowla-type √n (or any power better than the general n^{1/5}) lower bound was found specifically for dense
  A ⊂ [1, N] with |A| >= δN.
- Closest results: Sanders 0807.5104 (dense symmetric sets in finite groups: M_G(A) >= |A △ H|^{Ω(1)} for some
  subgroup H) and Spencer's half-sets of Z/pZ with M = O(p^{1/2}).
- A proofatlas.ai collaboration page on the conjecture exists (not read).
- So the heuristic dense-Chowla argument (NOTEBOOK 2026-10-19 item 5: Turán + Bessel + doubly positive) would be new
  if made rigorous. This is not a thorough survey: re-check before claiming novelty.
- Sources:
  - https://arxiv.org/pdf/0807.5104
  - https://arxiv.org/pdf/2509.03490
  - https://www.proofatlas.ai/collaboration/chowla-cosine-conjecture/

## Found by the P31 review agent (2026-10-19)
- M. N. Kolountzakis, "The density of B_h[g] sequences and the minimum of dense cosine sums", J. Number Theory 56
  (1996) 4–11, Thm 2:
  - M >= Cε²N for distinct frequencies <= (2 − ε)N, i.e. density above 1/2 in [1, max A] forces linear M;
  - the proof multiplies by a Fejér kernel and uses Fejér's peak/mean bound (via Fejér–Riesz);
  - so our P29 is classical, and P31's multiplication/factorization framework has a direct predecessor;
  - P31's x₀-averaged second-moment inequality and its threshold β/2 were not found there.
  - https://eigen-space.org/mk/ps/dense.pdf
- W. Beckner, "Inequalities in Fourier analysis", Ann. Math. 102 (1975) 159–182, Thm 3: sharp Young on R^d with
  constant (A_pA_qA_{r'})^d. It is used for P31-N with p = q = 4/3, r = 2.
- Levin–Lubinsky (2015 manuscript) Thm 1: limsup N^{1/p−1/q}Λ_{N,p,q} <= E_{p,q}, with Λ an INFIMUM of ‖P‖_p/‖P‖_q.
  - For p = 2, q = 4 this points toward a LOWER bound on lim ρ, not the needed upper bound.
  - The limit is conjectured there.
- Correction to the 2026-10-19 quick check above: a dense-set result in Z DOES exist (Kolountzakis 1996, density
  > 1/2, linear). The √n result for density in (0.385, 1/2] (P31) is what was not found.

## Novelty check for P31-C (dyadic / sparse-front Chowla), 2026-10-19 (one extended web search)
- Hits: JMTZ 2509.03490, Yip 2610.01657, Bedert 2509.05260, Shankar 2609.05338, Quanta (Jan 2026), proofatlas.
- None states a √n (Chowla-strength) lower bound for A ⊂ [N, 2N] or for dense A.
- Closest: Sanders' POLYNOMIAL estimate when every frequency is O(N) (cited in Bedert/Shankar). That is a power loss,
  not √n.
- So the dense corollary δ > 0.385 (0.4055 elementary) appears new relative to these sources. Not a thorough survey.
- CORRECTION (same day): the dyadic statement is trivial. Sets in (X/2, X] have M >= 0.373|A| by a test-point
  average (PROOFS P31-C correction), so there is nothing to claim there.
- Sources:
  - https://arxiv.org/pdf/2509.05260
  - https://arxiv.org/html/2609.05338
  - https://arxiv.org/html/2610.01657
  - https://www.quantamagazine.org/networks-hold-the-key-to-a-decades-old-problem-about-waves-20260128/

## Dense sets: Bu et al. 2610.17160v1 Prop. 9.7 vs our P31 (checked 2026-10-19)
- Bu et al., arXiv:2610.17160v1 (12 Oct 2026), Proposition 9.7 ("Frequencies O(n)"), quoted via the arXiv HTML. For C >= 1
  and A ⊂ [1, Cn] with |A| = n >= 2:
      λ_A³‖f_A‖₁ >= (n − 1)/(32CC₁),   hence λ_A >= ((n − 1)/(64CC₁))^{1/4},   C₁ = 2·10⁵.
  - Method: an L¹-sensitive boundary (run-top) estimate, Prop. 9.1, summed over t ∈ [1, 2Cn].
  - Remark 9.8(iii): the proposition "says nothing about whether √n is the true order for dense sets".
- Ours:
  - **Kernel-checked** (`dense_elementary`): |A| >= 0.41·max A ⇒ λ_A >= √|A|/1000. Paper constants c(δ)√n with
    c(0.5) = 0.064, c(1) = 0.23. This is the sharp order √n for every C < 1/0.4055 ≈ 2.466.
  - P31: the sharp order for every C whenever the profile is not front-loaded.
  - Open even for us: A ⊂ [1, Cn] with C > 2.466 and a front-loaded profile. That is exactly where their n^{1/4} is the
    best known.
- Also from the same search: the Epoch page's remark that no example with c <= 1/20 is known. Unchanged.

## Ruzsa, Acta Arith. 111 (2004) 179–186 — read in full 2026-10-19 (free PDF from impan.pl); Bourgain, Acta Arith. 45 (1986) via Ruzsa's account
- Result: min Σ_{a∈A} e(ax) < −c₄ exp(c₅√log n) with c₅ = √((log 2)/8). Bourgain (1986) had exp((log n)^c).
- Lemma 2.1 (Bourgain's structure step).
  - Small K ⇒ B + {Σ_{i<=k} ε_iβ_i} ⊂ A, with distinct cube sums, k = ⌊log n/(4 log K + c₆)⌋ and |B| >= √n.
  - Iteration B' = B ∩ (B − α), carrying g = h₁ + h₂ + h₃ with |h₁| <= f + K, ‖h₂‖_∞ <= 4^jK^{j+1} and
    ‖h₃‖₁ <= (8K²)^j n^{−1/2}.
  - Propagation: |h₁∗h₁e_α| <= (f+K)∗(f+K) = f + K². This is the exact-mixing identity (NOTEBOOK cont. 19.5(a)).
  - Size loss per level: E(B) >= |B|³/(2K²), from Hölder with ‖g − h₂‖₁ <= K + η. So |B'| >= |B|/(4K²).
  - h₂∗h₂e_α is handled by AVERAGING over α (Parseval). h₁∗h₁e_α is NOT averaged; that is where K² − K enters.
- Lemma 3.1 (boundary certificate). U ⊂ A, V ∩ A = ∅, 0 ∉ V, U − V ⊂ A ⇒ K >= (1/|U| + 1/|V|)^{−1/2}.
  - Proof: h = avg_U e(u·) − avg_V e(v·), with ∫h(f + K) = 1 and ∫|h|²f <= 0, then Cauchy–Schwarz.
  - Lead: this is P9 on W = {0} ∪ U ∪ V. It is found from S + T + {0, d} ⊂ A by walking the run along d until it ends
    (torsion-freeness), i.e. the run-top mechanism.
  - Lead's weighted form: with D = 2δ(U,V) − ρ(U) − ρ(V) (cross minus internal A-difference densities),
        M >= (D + √(D² + 4σ²))/(4σ²),   σ² = 1/|U| + 1/|V|.
- Ledger verdict (ROUTES): structure step = group-agnostic energy/Hilbert-cube iteration with loss K² per level;
  certificate = P9/run-top. The scale-combining loss is by design: O(1) loss per level needs ‖g‖₁ = O(1), i.e.
  K = O(1). Not a tool for C*.
- 2026-10-19 extended web search for "approximate / robust partial difference sets, stability of two-valued spectra,
  robust Ma theorem": nothing found. The hits are only spectral sets in cyclic groups (Forum Math Sigma 2022), which use
  Ma's lemma exactly, and PDS packings. Absence of a hit is not proof of novelty.


## Latin-square-type PDS and subgroup structure (codex literature check, 2026-10-19 cont. 30; report .research/agents/lit_lspds_report.md)
- Exact PCP forcing: a regular LS_r(n) PDS in ANY finite abelian group with 2 <= r < n and n > ½(r−1)(r³ − r² + r + 2)
  (≈ r⁴/2) is a degree-r PCP (union of r order-n subgroups meeting in 0). Specialization of Bruck, Pacific J. Math. 13
  (1963) Thm 4.3 (pseudo-net graphs, n > P(r − 1), P(x) = ½x⁴ + x³ + x² + 3x/2) plus Leung–Ma–Schmidt, JCTA 115 (2008)
  Cor. 7–8 (abelian Singer group ⇒ the lines through 0 are subgroups). Agent read both; the combination is the agent's
  specialization, not a quoted theorem.
- In F_p², every nontrivial regular PDS is a union of punctured lines (Heinze thesis 2001, Prop. 3.2.19).
- Non-PCP LS PDS exist: Shrikhande (Z_4², LS_2(4)); Davis–Xiang (Z_4^{2ℓ}, r = 4^{ℓ−1} + 1); Jedwab–Li, Comb. Theory 1
  (2021) #18, Thm 5.3: LS_{p^{(a−1)s}}(p^{as}) in Z_{p^a}^{2s}, non-PCP for a >= 3, with ratio (n − 1)/r ≈ p^s → ∞;
  Polhill EJC 15 (2008) R125: LS_{(p−1)(p²+1)}(p⁴) in Z_{p²}⁴. Whether these are unions of subgroups of OTHER orders:
  queued (lit_jedwabli brief).
- Ma (1984, 1994): a regular PDS in a CYCLIC group is a subgroup, a subgroup complement, or Paley (prime order ≡ 1 mod 4).
  An abelian group with a cyclic Sylow subgroup (order not prime) has no nontrivial PDS (Schur–Wielandt; Heinze Thm
  3.2.16).
- Robust versions: Sanders, Israel J. Math. 179 (2010) Thm 1.4 (O(M) subgroups, |A △ ∪H| <= exp(O(M^C))); JMTZ
  2509.03490v2 Thm A.1 (M <= N^γ, γ < 1/4 ⇒ |A △ H| <= δN for a subgroup H; errors relative to |G|); Ihringer, Discrete
  Math. 346 (2023) (approximately SRGs; absolute bound, no subgroup conclusion). No near-LS ⇒ PCP stability theorem was
  found.
- FOLLOW-UP (codex, report .research/agents/lit_jedwabli_report.md, with exact checks on dirichlet): Jedwab–Li Thm 5.3
  blocks in Z_{p^a}² (realization U = horizontal axis) are D_{a,j} = {(x, y) : y ≠ 0, with k = v_p(y), b = a − k,
  z = y/p^k: [(x mod p^b)z^{−1}]_{p^b} ∈ [jp^{b−1}, (j + 1)p^{b−1})} = ⊔_k ⊔_t (H_{k,ℓ} \ K_{k,ℓ}), ℓ = t + jp^{b−1}, with
  H_{k,ℓ} = ⟨(ℓ, p^k), (p^b, 0)⟩ (order p^a) and K = H ∩ {p^{k+1} | y} (index p). Character values exactly
  {n − r, −r} = {p^a − p^{a−1}, −p^{a−1}}; the large-value set is J(D), J(x, y) = (−y, x). For a >= 3, D ∪ {0} is NOT a
  union of subgroups of any orders (witness (1,1) ∈ D, (3,3) ∉ D for p = a = 3; for j ≠ 0 it contains no nontrivial
  subgroup at all). Exact check p = 3, a = 3: |D| = 234, (v,k,λ,μ) = (729, 234, 81, 72), values 18 (×234), −9 (×494).
  Polhill's positive ingredient in Z_{p²}⁴ likewise is a union of full punctured subgroups and subgroup shells, not
  closed under ×p.

## 2026-10-20 cone-confinement attribution check

The rank-two hyperbolic quadric's two rulings and projective grid are classical: Peter J. Cameron, [Notes on Classical Groups](https://webspace.maths.qmul.ac.uk/p.j.cameron/class_gps/cg.pdf), course notes January–March 2000, p. 41 / Figure 1, checked directly. Brouwer's [affine-polar graph page](https://aeb.win.tue.nl/drg/graphs/VO.html) identifies the affine graph and points to Brouwer–Shult (1990) for local structure; that paper was not read in this pass. The current full cone-concentration spectrum is derived directly from the rook-grid geometry and Fourier orthogonality, with Boolean confinement consequences. No novelty/priority claim or inference from a search failing to find an exact statement is made. The squared-disk fractional countercontrol follows from the elementary autocorrelation identity, rather than an imported specialized theorem.

## 2026-10-20 small-fiber mean and CLT dependencies

- Amir Dembo, [Probability Theory: STAT310/MATH230](https://stanford.edu/~montanar/TEACHING/Stat310A/lnotes.pdf), September12,2010, Theorem3.1.3, p.96. Checked the within-row independent triangular-array CLT with normalized variance sum tending to1 and vanishing truncated variance. The current array has maximal normalized summand O(X^(-1/2)); its third-moment Lyapunov ratio is also O(X^(-1/2)). No independence across different X is assumed.
- [NIST DLMF10.17.3](https://dlmf.nist.gov/10.17.E3), checked for fixed real order nu=1 on the positive real axis: J1(s)=O(s^(-1/2)). This gives disk-transform decay O(s^(-3/2)). The weighted parity-coset O(R^(2/3)) estimate is DERIVED in the current note via smooth disk comparison and absolutely convergent Poisson summation; it is not quoted from DLMF. That estimate makes the positive-Gram origin cost sharp and extends to growing isoclinic phases. No novelty claim for these classical ingredients or the project's consequences.

## 2026-10-21 addendum — exact reciprocal-witness conjecture R0

Bounded novelty check requested while the campaign is PAUSED. No exact
R0 antecedent was located; mathematical priority remains UNVERIFIED.
The reciprocal/Caratheodory–Schur machinery, signed weighted certificates
and exploitation of Boolean idempotency have established antecedents.
The unproved content is a uniform selected-coefficient upper bound at
lambda=2sqrt(n), under ACTUAL lowM, sufficient for full Chowla.

[Full versioned primary-source comparison, exact statement, search scope
and limitations](notes/R0_novelty_2026-10-21.md). The review includes
Ruzsa2004, Sanders0807.5104v2, Bedert2509.05260v3,
Shankar2609.05338v1, Jin–Milojevic–Tomon–Zhang2509.03490v2,
Bu et al.2610.17160v1 and Yip2610.01657v2. Do not treat search absence
as evidence of truth, priority or an established route to Chowla.
