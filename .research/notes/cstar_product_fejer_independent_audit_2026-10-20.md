# Independent audit: product-Fejér W2 certificate

Checkpoint: 2026-10-20T05:56:49.635343+00:00. Ongoing research; no universal Chowla/C* or W2 constant is established. [Reproduction index](../experiments/cstar_structural_2026-10-20/README.md).

Audited [the product-Fejer theorem](cstar_product_fejer_asymptotic_2026-10-20.md), including its general lemma and carry-free transfer. Verdict: the stated theorem and constants are valid. No missing independence, support, symmetry, or normalization hypothesis was found. This is an audit of the specified random model, not a proof of universal W2 or Chowla.

## Checks performed

1. Product coefficients: the one-coordinate profile is (1/3,2/3,1,2/3,1/3), with sum3 and squared sum19/9. Its convolution at absolute offsets0..4 is exactly (19,16,10,4,1)/9. Thus v=3^d-(19/9)^d and R_t>=(10/9)^d for every t in the original cube.

2. Filling graph: after deleting zero/equal summands, each ordered representation t=s+u has two distinct sign classes. For nonzero t, a pair of sign classes cannot represent t in two different ways: changing a sign alone would force the changed summand to0, while changing both signs changes t to-t. Each graph edge is therefore counted exactly twice by ordered representations. Every vertex has at most two neighbors, represented by t-s and t+s. The graph is simple with maximum degree2, so three matchings partition its edges. The discarded probability mass is <=3, giving a matching of weight >=(R_t-3)/6. Independence of its endpoint classes gives the stated exponential no-representation bound. Full independence is used here; six-wise independence alone cannot justify the product over an arbitrarily large matching.

3. Rayleigh normalization: with X_0=0, B_U=P-I+X, X delta_0=w, and w_0=0, direct expansion gives

q*B_Uq=q*Pq-||q||²-2V/sqrt(v)+C/v,
||q||²=1+V/v.

There is no omitted diagonal or factor2. P is PSD because its Fourier symbol is the product of (1/3)|1+e(x)+e(2x)|².

4. Covariance: symmetry means E[X_s X_t] is nonzero for BOTH t=s and t=-s. Including both gives E[w*Pw]=sum_s sigma_s²(1+p_2s)<=2v, hence E[q*Pq]<=3. Likewise V=2 sum_a Y_a² yields VarV<=4 sum_a sigma_a²=2v, not the unsymmetrized variance.

5. Cubic coefficient audit: the coefficient12 for a<b,a+b=c and coefficient6 for a=a,b=2a are correct. Independent exact monomial enumeration for d=1,2,3 found respectively1,26,547 monomials, with total ordered coefficients6,288,6486. Every monomial matched the claimed expansion. The script also verified simplicity and maximum degree2 of every nonzero-target filling graph in those dimensions.

6. Cubic cross terms: distinct three-variable monomials have zero covariance unless their supports agree. In an ordered torsion-free group the same three positive elements admit only one additive-triple orientation. A three-variable term versus a two-variable repeated term always leaves a singleton. For two distinct repeated terms, any potential nonzero covariance would require a doubling cycle or equality of the repeated terms; torsion-free arithmetic rules the former out. Every term is centered. Therefore the displayed exact variance decomposition is correct. Bounding each sum by L², L=v/2, gives144L²+36L²=45v². The constant is loose but safe.

7. Probability constants: Chebyshev for V outside[v/2,2v] gives <=8/v; Markov for q*Pq>sqrt(v)/4 gives <=12/sqrt(v); Chebyshev for |C|>v^(3/2)/4 gives <=720/v. On the intersection the numerator is <=-||q||²-sqrt(v)/2 and ||q||²<=3, yielding K>=1+sqrt(v)/6. The failure sum728/v is correct.

8. Six-wise independence: every second-moment product used in VarC contains at most six distinct sign classes. Repeated powers do not increase this number. Six-wise Bernoulli independence therefore suffices for all spectral calculations. The note correctly keeps support filling as a separate assumption in that version.

9. Integer encoding: W2 is inside[-4,4]^d. For u,v in W2 and s in S, the coordinates of u-v-s lie in[-10,10]. A zero base11 encoding forces each digit to0 successively modulo11, so there are no extra adjacency relations. Injectivity on W2 follows similarly from its difference-coordinate bound8. The claimed graph transfer is exact.

10. Small exact sanity case d=1: v=8/9, VarC=16/27, VarV=16/81, and E[q*Pq]=13/6. These agree with the formulas and lie below their stated bounds.

## Scope preserved

The asymptotic filling estimate tends to1 despite being useless at low dimension. The theorem controls full W2, not the first neighborhood: the centered vector has nonzero entries at unselected candidate frequencies. It requires a positive-definite mean profile and independence (or six-wise moments plus separately supplied filling). None of these follows for an arbitrary deterministic Boolean support.

Reproducible combinatorial audit: [audit_product_fejer.py](../experiments/cstar_structural_2026-10-20/audit_product_fejer.py). The audit does not change the theorem hypotheses.
