# Product-Fejér Boolean model: a rigorous W2 square-root certificate

Checkpoint: 2026-10-20T06:12:18.377072+00:00. Ongoing research; no universal Chowla/C* or W2 constant is established. [Reproduction index](../experiments/cstar_structural_2026-10-20/README.md).

2026-10-20. CHAIN(c). This proves a high-probability theorem for the specified independent product-Fejér model, not for arbitrary Boolean supports. 

## 1. Model and theorem

Let U={-2,-1,0,1,2}^d⊂Z^d and set

  p_s=product_{j=1}^d (1-|s_j|/3),  s∈U,
  p_s=0 outside U.

For each unordered sign class {s,-s} with s≠0 choose an independent Bernoulli variable b_s=b_-s of mean p_s. Let S={s≠0:b_s=1}, let D=sum_{s∈S}e(s·x), and put

  W2={0}∪S∪(S+S),
  K_W2=-lambda_min(B_W2),  (B_W2)_{u,v}=1_S(u-v),
  v_d=sum_{s≠0}p_s(1-p_s)=3^d-(19/9)^d.

**Theorem.** With probability at least

  1 - 5^d exp(-[(10/9)^d-3]/6) - 12/sqrt(v_d) - 728/v_d,

one has

  K_W2 ≥ 1+sqrt(v_d)/6.

In particular this probability tends to one, and since |S|/3^d→1 in probability,

  K_W2/sqrt(|S|) ≥ 1/6-o(1)

with probability tending to one. Thus this product-Fejér family is NOT an asymptotic counterexample to the W2 square-root assertion. The argument is a concrete finite-row Rayleigh certificate, not an appeal to the global minimum of D.

## 2. The full original cube lies in W2 with high probability

For t∈Z^d let

  R_t=sum_{s∈Z^d}p_s p_{t-s}.

The one-coordinate convolution takes values

  (19,16,10,4,1)/9

at absolute coordinates 0,1,2,3,4 respectively. Hence for every t∈U,

  R_t≥(10/9)^d.

Fix t≠0. Discard ordered representations t=s+(t-s) involving 0, or with equal summands. Their total product-probability mass is at most 2p_t+p_{t/2}²≤3, with the latter term omitted when t/2 is not an integer point of U. The remaining representations have two different independent sign classes; the possibility t-s=-s would require t=0 and has already been excluded.

Make a graph whose vertices are the independent sign classes [s]={s,-s}, and whose edges are the remaining unordered representations of t. Each edge has weight p_s p_{t-s}. The graph is simple: two different signed representations using the same two nonzero sign classes could give the same nonzero sum only if one summand were 0 or the sum were 0. Each vertex [s] has at most two neighbors, [t-s] and [t+s]. Therefore this graph has maximum degree at most 2 and admits an edge coloring with at most 3 colors.

The total edge weight is at least (R_t-3)/2. One color class is a matching of weight at least (R_t-3)/6. The events that both endpoints of each matching edge are chosen are independent. Consequently

  P(t∉S+S)≤exp(-(R_t-3)/6).

The point 0 is explicitly in W2. Union bounding over the at most 5^d nonzero target points gives

  P(U⊄W2)≤5^d exp(-[(10/9)^d-3]/6).                       (1)

The bound is useful asymptotically; it need not be numerically sharp at low d.

## 3. Centering needs U, which is why W1 did not supply this test

Define the centered coefficients

  X_s=b_s-p_s for s∈U\{0},  X_0=0,
  X_s=0 outside U,

and the column vector w=(X_s)_{s∈U}. Let V=||w||². In particular w has entries -p_s at unselected candidate frequencies. It is not supported in {0}∪S in general. The cube-filling result (1) is what makes w an admissible W2 vector.

Let P be the matrix on U with entries p_{u-v}, and let X be the matrix on U with entries X_{u-v}. Then

  B_U=P-I+X.

The scalar Fourier polynomial sum p_s e(s·x) is the product of the one-dimensional nonnegative Fejér polynomials

  1+(4/3)cos(2πx)+(2/3)cos(4πx).

Thus P is PSD. Moreover X delta_0=w.

Use the explicit random vector

  q=delta_0-w/sqrt(v_d).

Since w_0=0,

  ||q||²=1+V/v_d,
  q*B_U q=q*Pq-||q||²-2V/sqrt(v_d)+C/v_d,               (2)

where

  C=w*Xw=sum_{s,t∈Z^d} X_s X_t X_{s-t}.

The negative quadratic term in (2) is of order sqrt(v_d). The key point is that the positive mean cost has bounded expectation and the centered cubic has variance only O(v_d²).

## 4. Mean cost, quadratic fluctuation, and exact cubic covariance

Choose one lexicographically positive representative a of each nonzero sign class and write Y_a=X_a. These variables are independent, centered, and bounded by 1 in absolute value. Let sigma_a²=E Y_a². Then

  v_d=2 sum_a sigma_a²,
  E V=v_d,
  Var(V)=4 sum_a Var(Y_a²)≤4 sum_a E Y_a^4≤2v_d.          (3)

For the mean cost, covariance E[X_s X_t] vanishes except when t=s or t=-s. Hence

  E[w*P w]=sum_{s≠0} E X_s² (1+p_{2s})≤2v_d,
  E[q*Pq]≤3.                                             (4)

The cross term between delta_0 and w has expectation zero. Since P is PSD, q*Pq≥0, so Markov's inequality is applicable to (4).

The cubic has the exact expansion

  C=12 sum_{a<b, a+b=c} Y_a Y_b Y_c
      +6 sum_a Y_a² Y_{2a},                              (5)

where all indices are lex-positive, belong to U, and variables outside U are interpreted as zero. The coefficient 12 counts the two global signs and six permutations of a distinct triple; the coefficient 6 counts the repeated case.

Every monomial in (5) has mean zero. Distinct triples are mutually orthogonal unless their three-variable sets agree; the additive order makes such agreement the identical term. A distinct-variable triple is orthogonal to every repeated-variable term because it contains a variable missing from that term. Two different repeated terms Y_a²Y_{2a} and Y_b²Y_{2b} are also orthogonal: to avoid a singleton variable would require both 2a=b and 2b=a, impossible for nonzero points in Z^d. This is precisely where torsion-free arithmetic enters the cubic covariance argument.

Put L=sum_a sigma_a²=v_d/2. Bounding sigma_c²≤1 and E Y_a^4≤sigma_a² gives the safe estimate

  Var(C)
  =144 sum_{a<b,a+b=c} sigma_a² sigma_b² sigma_c²
    +36 sum_a E Y_a^4 sigma_{2a}²
  ≤144 L²+36 L²=45v_d².                                 (6)

The constant is deliberately not optimized.

## 5. The negative Rayleigh quotient

From (3), with probability at least 1-8/v_d,

  v_d/2≤V≤2v_d.

From (4), with probability at least 1-12/sqrt(v_d),

  q*Pq≤sqrt(v_d)/4.

From (6), with probability at least 1-720/v_d,

  |C|≤v_d^(3/2)/4.

On their intersection, (2) gives

  q*B_U q≤-||q||²-sqrt(v_d)/2,
  ||q||²≤3,
  (q*B_U q)/||q||²≤-1-sqrt(v_d)/6.

When U⊂W2, the same q extended by zero is an admissible vector on W2. Combining the four failure probabilities proves the theorem.

Finally E|S|=3^d-1 and Var(|S|)≤2(3^d-1), so |S|/3^d→1 in probability, while v_d/3^d→1. This justifies the ratio formulation in §1.

## 6. What the proof resolves, and what it does not

A large fraction of the much larger double cube [-4,4]^d can indeed lie outside W2, and typical occupied rows can concentrate near an entropy boundary. That fact does not decide the smallest eigenvalue: the much smaller but fully available original cube U already carries the centered-noise test above.

The gain is not supplied by a generic moment identity alone. It uses an exact support event that allows all negative centering entries -p_s at frequencies omitted from S. These entries are missing from W1. It also uses the positive-definite product-Fejér mean to bound the expectation of the positive cost and the exact independent-Boolean cubic covariance calculation.

The theorem does not apply to an arbitrary deterministic Boolean set, a dependent selection law, or a weighted mean whose original candidate support fails to fill inside S+S. No universal W2 lower bound, no universal Chowla theorem, and no claim of novelty is made.

## 7. General positive-definite rounding-and-filling lemma

The certificate does not depend on the tensor-product form of the probabilities. Let U⊂Z^r be finite and symmetric, with 0∈U. Let p:Z^r→[0,1] be symmetric, supported in U, with p_0=1, and suppose its Fourier polynomial sum_s p_s e(s·x) is nonnegative. Choose nonzero sign-class Bernoulli variables of means p_s that are six-wise independent (full independence is sufficient), and let S and W2 be as before. Set

  v=sum_{s≠0}p_s(1-p_s)>0,
  epsilon_fill=P(U⊄W2).

Exactly the same centered vector q=delta_0-(b-p)/sqrt(v) and the calculations in §§3–5 prove

  P(K_W2≥1+sqrt(v)/6)
    ≥1-epsilon_fill-12/sqrt(v)-728/v.                     (7)

Thus whenever v→∞ and epsilon_fill→0, the model has a W2 lower bound of order sqrt(v) with high probability. The spectral proof needs only six-wise independence: each product in the cubic second moment involves at most six distinct sign-class variables; the other calculations need only one- or two-variable moments. Before any filling assumption, it proves the same probability bound for K_U=-lambda_min(B_U), with epsilon_fill omitted. This is also a global negative-value certificate, because all vectors on U are legitimate trigonometric tests. Filling is the additional fact making it a W2 certificate. Six-wise independence, positive definiteness of the deterministic mean profile, and actual support filling are not consequences of Booleanity for an arbitrary deterministic set.

Under FULL independence there is also a general sufficient filling condition. The matching argument in §2 works for every such finite symmetric U; six-wise independence alone does not justify its exponentially small failure bound. Writing

  R_min=min_{t∈U\{0}} (p*p)(t),

it gives

  epsilon_fill≤|U| exp(-(R_min-3)/6).                      (8)

Therefore R_min-6 log|U|→+infinity is one sufficient condition. The product-Fejér model satisfies it very strongly. Other mean profiles, including suitably dense one-dimensional triangular roundings, can be tested against (8) without changing the spectral argument.

### 7.1. Variable central mass

The normalization p_0=1 is unnecessary for the spectral certificate. More generally, let p be a real symmetric finitely supported profile on U with p_0=h, 0≤p_s≤1 for s≠0, and nonnegative Fourier polynomial. Keep six-wise independent sign-class Bernoulli rounding only at the nonzero frequencies, put X_0=0, and assume v=sum_{s≠0}p_s(1-p_s)>0. Positive semidefiniteness gives h>0 and |p_t|≤h for every t, by the two-by-two principal minors of the convolution matrix. In particular,

  E(w*P_U w)=sum_{s≠0}p_s(1-p_s)(h+p_{2s})≤2hv,
  E(q*P_U q)≤3h.

All variance estimates for V and C remain unchanged: they depend only on the nonzero Bernoulli variables, not on h. The exact matrix identity and test-vector identity are now

  B_U=P_U-hI+Xconv,
  q*B_U q=q*P_U q-h||q||²-2V/sqrt(v)+C/v.

Markov's inequality bounds the failure of q*P_U q≤sqrt(v)/4 by 12h/sqrt(v). Intersecting with the same V and C good events as before yields

  q*B_U q≤-h||q||²-sqrt(v)/2,
  K_U≥h+sqrt(v)/6.

Consequently, with epsilon_fill=P(U⊄W2),

  P(K_W2≥h+sqrt(v)/6)
    ≥1-epsilon_fill-12h/sqrt(v)-728/v.                   (9)

For K_U the same statement holds with epsilon_fill omitted. Thus v→∞, h=o(sqrt(v)), and epsilon_fill→0 suffice for a high-probability W2 square-root-variance certificate. This includes admissible positive mean profiles built from multiple packets, provided their nonzero coefficients are valid Bernoulli probabilities and the stated central-mass and filling conditions are separately verified. It is not a theorem for arbitrary deterministic Boolean sets or arbitrary dependent rounding.

Filling remains a separate condition. If the nonzero variables are fully independent, the matching proof also gives a version adapted to this normalization: with R_min=min_{t∈U\{0}}(p*p)(t), deletion of representations using zero or equal summands removes at most 2h+1 of ordered weight, so

  epsilon_fill≤|U| exp(-(R_min-(2h+1))/6).               (10)

Indeed the two zero representations contribute 2hp_t≤2h, and the equal-summand representation contributes at most 1. The remaining graph has maximum degree two and the same independent matching argument applies. Formula (10) reduces to (8) when h=1. Neither full filling nor its exponential estimate follows from six-wise independence alone. The product-model theorem and its constants are unchanged.

## 8. Exact carry-free transfer to positive integer frequencies

The product model is a genuine obstruction test for the integer problem, not merely a different ambient group. Map

  phi(s)=sum_{j=0}^{d-1}s_j 11^j.

On W2⊂[-4,4]^d this map is injective. Moreover for u,v∈W2 and s∈S, every coordinate of u-v-s lies in [-10,10]. If phi(u-v-s)=0, reduction modulo 11 forces its first coordinate to be 0; dividing by 11 and iterating forces every coordinate to be 0. Hence

  phi(u)-phi(v)∈phi(S) if and only if u-v∈S.

The W2 adjacency matrices before and after encoding are therefore identical up to relabeling. Selecting one positive integer from each pair ±phi(s) gives distinct positive frequencies. Thus the high-probability W2 bound transfers exactly to carry-free integer encodings of this model; no approximation or numerical alias check is required.
