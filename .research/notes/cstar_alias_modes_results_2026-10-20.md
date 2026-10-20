# Alias modes: completed model-specific calculation and precise unresolved bound

Checkpoint: 2026-10-20T05:56:36.620284+00:00. Ongoing research; no universal Chowla/C* or W2 constant is established. [Reproduction index](../experiments/cstar_structural_2026-10-20/README.md).

2026-10-20. This supplements [the residue-fiber centering note](cstar_alias_centering_2026-10-20.md). It does not repeat its partial-matching Frobenius derivation or claim a universal W2 theorem.

## Setup and exact identities

S is a symmetric one-representative lift of D in a finite quotient G, W2={0}∪S∪(S+S), and Q projects onto vectors whose coordinates sum to zero on each residue fiber of W2. There are no actual adjacency edges inside a residue fiber because 0∉D. Hence tr(Q B_W2 Q)=0. Between two fibers each allowed lifted difference supplies a partial matching. The periodic lifted kernel annihilates Q, so these directions measure genuinely nonperiodic interactions.

## Full alias-compression eigenvalues

These are numerical smallest eigenvalues of Q B_W2 Q, NOT whole-polynomial Fourier minima. FFT convolution is used only for exact finite-graph matvecs with nonaliasing padding. All row sets are integer pair sums. The quotient averaging projection is implemented exactly in formula using bincounts. Largest saved residual is 1.5e-7.

- JL p=3,a=2: N=24, alias dimension122, K_alias=7.23273, K_alias/sqrt(N)=1.47637.
- JL p=5,a=2: N=120, alias dimension1364, K_alias=20.38526, ratio1.86091.
- JL p=7,a=2: N=336, alias dimension5712, K_alias=57.92922, ratio3.16030.
- JL p=3,a=3: N=234, alias dimension1896, K_alias=42.14189, ratio2.75490.
- JL p=3,a=4: N=2160, alias dimension18886, K_alias=337.80797, ratio7.26847.
- Quadric p=3,d=4: N=32, alias dimension232, K_alias=6.61861, ratio1.17002.
- Quadric p=5,d=4: N=144, alias dimension3144, K_alias=20.48836, ratio1.70736.
- Quadric p=3,d=6: N=260, alias dimension9592, K_alias=39.42486, ratio2.44503.

Thus alias directions alone recover most of the full-W2 certificate on these centered lifts. This is useful diagnostic information, not proof of an arbitrary-lift or universal statement.

## Positive versus negative squared spectral energy

For three moderate cases, constructed an explicit orthonormal Helmert basis within each residue fiber, then diagonalized its entire compressed matrix. Write Eplus=sum_{lambda>0}lambda², Eminus=sum_{lambda<0}lambda², r=rank Q.

- JL(3,2): (Eplus+Eminus)/(N r)=0.50091; Eplus/Eminus=1.14641; lambda_max=11.29383, lambda_min=-7.23273.
- JL(5,2): normalized Frobenius0.64406; energy ratio1.59677; lambda_max=69.44116, lambda_min=-20.38526.
- JL(3,3): normalized Frobenius0.69535; energy ratio1.53197; lambda_max=144.64860, lambda_min=-42.14189.

The positive operator norm is already substantially larger than sqrt(N); the energy ratio is modest in these cases. The exact interval example in the residue-fiber centering note refutes a universal positive-operator-norm cap, so such a cap is not retained.

A sufficient pair of inequalities would instead be

    ||Q B Q||_F² >= c N r,
    Eplus <= C Eminus,

with absolute constants in the relevant high-ratio regime. They imply K_alias²>=Eminus/r>=cN/(1+C). Neither inequality is proved here in general.

## Exact countermodel to generic signed-energy balance

Partial-matching blocks, zero trace, and commuting fiber permutations do NOT imply the second inequality.

Take any finite Cayley graph B_G with degree N and small negative eigenvalue K_G, and form TWO disjoint copies. Put the two copies of each group vertex into one fiber. Every nonzero between-fiber block is I_2, a perfect matching; all the fiber permutation matrices commute. The alias space is spanned by differences of the two copies. On that space, the compressed adjacency is exactly B_G.

For the simplest choice G of size N+1 and D=G\{0}, the alias matrix is J-I. Its trace is zero, Frobenius squared is N(N+1), positive squared energy is N² and negative squared energy is N. Thus Eplus/Eminus=N→infinity, while K_alias=1.

This graph is not an actual torsion-free integer W2 graph. That distinction is the point: even the full partial-matching and commutation structure lacks the ordered-boundary information needed to force balance. Any proof must use that these are partial TRANSLATIONS of one finite integer row set, with unavoidable carries/endpoints, not merely abstract matching blocks or an abelian finite cover.

## Exact remaining quantitative issue

For actual W2 of a one-representative torsion-free lift of a high-ratio finite-group support, show that either the residue-mean/cross-sector block already has a sqrt(N) negative certificate, or the alias negative energy satisfies

    sum_{lambda<0}lambda² >= c N rank(Q)

(or another sufficient bound with an appropriately selected alias subspace). The two-copy model shows why deleting the torsion-free/W2 assumptions is invalid; the star example in w2_near_realization.md shows why discarding cross-sector coupling is invalid; the interval example shows why bounding only lambda_max is invalid.

This is a precise unproved ingredient, not an established new route or a claim of exhaustion. Model-specific computations support it only on the listed finite centered lifts.

Files: alias_modes.py/json; alias_signed_energy.py/json. All completed and stable.
