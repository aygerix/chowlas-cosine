# Proofs and exact reformulations

Status labels: PROVED (paper proof here), CITED, HEURISTIC, CONJECTURED, REFUTED.

## P1. Fejér–Riesz reformulation (PROVED, standard)
For finite A ⊂ N, M(A) = min ||q||_2^2 over finitely supported q: Z -> C with autocorrelation
r_q(d) = sum_k q_{k+d} conj(q_k) = (1/2) 1_{±A}(d) for all d != 0.
Proof: f_A + C >= 0 is a nonnegative trig polynomial iff = |Q(e^{ix})|^2 (Fejér–Riesz); coefficient matching; ||q||^2 = C.
Consequence: R(A)^2 = ||q||^4 / (|Q(0)|^2 - ||q||^2), with |Q(0)|^2 = M + N. Equivalently (Bu et al. Prop 8.1, h=0):
R = M2 / sqrt(2(M4 - M2^2)), M_p = (1/2pi) ∫|Q|^p. R -> 0 iff M4/M2^2 -> infinity.

## P2. Probabilistic reformulation (PROVED)
Good A <=> integer symmetric random variable S with characteristic function phi_S >= 0 and P(S=g) in {0, eps} for g != 0;
then M = p0/(2 eps), N = (1-p0)/(2 eps), R^2 = p0^2/(2 eps (1-p0)), p0 = P(S=0).

## P3. Dimension-free / projection principle (PROVED)
For finite symmetric S ⊂ Z^k \ {0} and b ∈ Z^k with s -> |<b,s>| injective on S/± and nonzero:
A = {|<b,s>|} satisfies f_A(x) = (1/2) F_S(x b) >= (1/2) min_{T^k} F_S, |A| = |S|/2.
So the problem over Z is the same as over all f.g. free abelian groups; a line restriction can only raise the min.

## P4. Exact t-fold uniform difference sets do not exist in torsion-free groups for t >= 2 (PROVED)
If B ⊂ Z^k finite, |B| >= 2, the difference v-w maximizing a generic linear functional is represented once.
Moreover the only maps of pairs induced by point maps preserving the difference are translations and the reversal
(u,v) -> (c-v, c-u); hence "multiplicity by symmetry" is at most 2 (this is Bu et al.'s factor 2).

## P5. Intersection lemma (PROVED)
M(A1 ∩ A2) <= 2 M(A1) M(A2). Proof: (f1+M1)*(f2+M2) (normalized convolution on the circle) >= 0 has
constant M1 M2 and coefficient 1/4 at ±a for a ∈ A1∩A2, i.e. equals M1M2 + f_{A1∩A2}/2.

## P6. Additive-energy lower bound (PROVED, elementary; cf. Roth/Bedert)
M >= ||f||_1/2 >= ||f||_2^3/(2||f||_4^2), ||f||_2^2 = N/2, ||f||_4^4 = m4 = (6E(A)+8Q3(A))/16
(E = #{a+b=c+d}, Q3 = #{a+b+c=d}). Hence R(A) >= N/(2^{5/2} sqrt(m4)): R -> 0 forces m4/N^2 -> infinity.
Third moment version: M >= max_alpha (alpha N - (3/4)T3)/(alpha^2+N/2), T3 = #{a+b=c}; sum-free A have R >= 1/sqrt2... (check constant: M >= sqrt(N/2) for T3=0).

## P7. Cube (torus) framework — rigorous construction template (PROVED)
Let J be a family of nonempty subsets of [k]; alpha_1..alpha_k positive integers such that the signed sums
sum_{j in S} eps_j alpha_j (S in J, eps in {±1}^S) are pairwise distinct up to global sign and nonzero.
Then A = {|sum_{j∈S} eps_j alpha_j|} has |A| = sum_{S∈J} 2^{|S|-1} and
f_A(x) = (1/2) p_J(2cos alpha_1 x, ..., 2cos alpha_k x),  p_J(y) = sum_{S∈J} prod_{j∈S} y_j,
hence min f_A >= (1/2) min_{eps ∈ {±1}^k} sum_{S∈J} 2^{|S|} eps^S   (multilinear => vertex minimum).
R_cube(J) := -min_eps g_J / sqrt(2 sum_J 2^{|S|}) bounds R(A) rigorously for every admissible alpha.
Hypercontractivity gives only R_cube >= (1/2)(sqrt2/3)^d for degree-d families: no a priori barrier.

## H1. Gaussian-chaos heuristic and the 1/2 barrier (HEURISTIC; see NOTEBOOK 2026-10-17)
At typical x, blockwise cosine sums behave like independent Gaussians; set-ness forces WICK-ordered chaos with
fixed positive coefficients kappa_a = (1/2) prod t_i^{a_i}/a_i! (t_i^2 = 2k_i). Degree-2 chaos: R >= 1/2, equality
iff single block (= Bu). Degree 4 single block: R = sqrt3*... = 0.866. Non-Wick z^4-3 would give 0.2165 but needs
lower-chaos multiplicities ~ block size. CONJECTURE H1: large-block Wick models have inf R = 1/2.
