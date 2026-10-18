# Literature (versioned, concise) — read 2026-10-17

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
