# Partial translations: exact identities and the remaining quantitative gap

2026-10-20. Direct full-W2 proof attempt. No universal square-root estimate is proved here.

Let S=-S be finite in Z\{0}, I={0} union S, W=I+I, and g(0)=K, g(u)=1_S(u) for nonzero u in W-W. Suppose H_W=(g(u-v)) is positive semidefinite. Choose its Gram vectors v_w and put V=span{v_t:t in I}, with orthogonal projection P onto V.

For s in S, T_s:V -> span{v_w:w in W} is the isometry determined by T_s v_t=v_(s+t). This is well defined even when the central Gram matrix is singular: the norm of every translated linear combination equals the norm of the original combination.

## 1. Compressing the translations does not yield commuting operators

Set A_s=P T_s and R_s=(1-P)T_s. Then, exactly,

- A_s*=A_(-s).
- A_s* A_t + R_s* R_t = T_s* T_t.
- A_s* A_s + R_s* R_s = identity on V.
- R_s v_0=0 and A_s v_0=v_s.
- A_s A_t v_0=A_t A_s v_0=P v_(s+t).

The last identity is commutation on one vector, not operator commutation. The defect matrices R_s*R_t are jointly positive as a block matrix. These identities are consequences of the original Gram matrix, not additional inequalities independent of it.

A concrete exact witness is S={-1,1}, W={-2,-1,0,1,2}, K=sqrt(3). The full matrix is K times identity plus the adjacency of the 5-vertex path, hence is positive semidefinite. In the ordered central basis (v_-1,v_0,v_1),

H = [[sqrt(3),1,0],[1,sqrt(3),1],[0,1,sqrt(3)]],

A_+ = [[0,0,sqrt(3)/3],[1,0,-1],[0,1,2sqrt(3)/3]],
A_- = [[2sqrt(3)/3,1,0],[-1,0,1],[sqrt(3)/3,0,0]].

Their commutator is

[[-2/3,0,1/3],[sqrt(3)/3,0,-sqrt(3)/3],[-1/3,0,2/3]],

which annihilates v_0 but is not zero. In coefficient coordinates the positive defect form H-C_+* H^-1 C_+ is diag(0,0,sqrt(3)/3), where C_+(a,b)=g(a-b-1).

## 2. Even an actual unitary dilation does not automatically finish the argument

For this same example there is an explicit positive measure with all the prescribed moments. Using angle theta rather than circle coordinate x, give each point theta=+/-pi/6 mass 1/sqrt(3), and each point theta=+/-pi/2 mass 1/(2sqrt(3)). Its moments satisfy

mu_hat(0)=sqrt(3), mu_hat(+/-1)=1,
mu_hat(+/-2)=mu_hat(+/-3)=mu_hat(+/-4)=0.

Thus multiplication by exp(i theta) on L2(mu) is a genuine unitary extension of the partial shift data. However,

mu_hat(+/-5)=-1,

while K+2cos(theta) is negative at theta=pi because sqrt(3)<2.

Equivalently, the kernel polynomial of the 5-path Gram matrix is

1-sqrt(3) z+2z^2-sqrt(3)z^3+z^4
= (z^2+1)(z^2-sqrt(3)z+1),

whose roots are exactly the four atoms above.

The conclusion is narrow but important: establishing a positive-definite completion or commuting unitary dilation of the truncated data does not force the unprescribed Fourier moments to be zero. It therefore does not establish global nonnegativity of K+D. This is not a counterexample to the desired W2 square-root estimate; it identifies an additional tail-control requirement for that particular proof strategy.

## 3. Relation to the translated bottom-eigenvector test

Let q, supported on I, have L2 norm 1 and satisfy P_I(D+k)q=0, with k=-lambda_min(B_I). Put h=(D+k)q, supported on W\I. The translate trial space q times span{e_s:s in I} lies in W. Its ordinary Gram matrix and shifted energy matrix are

Gamma_st = integral |q|^2 exp(2pi i(s-t)x),
E_st = integral (D+k)|q|^2 exp(2pi i(s-t)x).

Every diagonal of E is zero. Furthermore,

sum_(s in S) E_s0 = integral D(D+k)|q|^2 = ||h||_2^2,

so sum_(s in S)|E_s0|^2 >= ||h||_2^4/|S|.

This retains the whole simultaneous family rather than only one exterior direction. But aggregating the family to the sum of its translates recovers the two-vector q,Dq test and its positive exterior cost. A universal proof still needs a quantitative bound on a negative generalized eigenvalue of (E,Gamma), not merely a large central coupling or zero diagonal. Generic traceless-matrix estimates lose a factor growing with the number of translates, and Gamma need not be well conditioned.

No bound controlling that cost from exact Booleanity and translation compatibility was established in this pass. In particular, neither the operator identities nor the extension example may be presented as progress toward the universal inequality N <= C K^2.

## 4. A concrete proposed leakage inequality fails

A possible intermediate claim was that the normalized bottom eigenvector q of B_I always obeys integral D^2 |q|^2 >= N. A small exhaustive floating-point falsification pass (all A subset {1,...,12}, 1 <= |A| <= 7) disproves this candidate numerically with a wide margin:

A={1,2,3,4,5,6,8}, N=14,
k approximately 2.445124904035096,
R=||(D+k)q||^2 approximately 2.046263239215422,
(R+k^2)/N approximately 0.5732070739677184.

A second support A={1,2,4,5,6,7,8} has k approximately 3.3196384666993035 and R approximately 0.8542923947649385, so R/N approximately 0.06102088534 even though k/sqrt(N)<0.9.

The script test_leakage.py reproduces these numbers. They are numerical falsifications with large margins, not exact algebraic certificates. They do not exclude a positive absolute leakage bound under the stronger asymptotic hypothesis k/sqrt(N)->0. No such conditional bound was proved, and it would still leave the signed exterior-energy issue.

There is also a simpler exact counterexample, so the first failure need not rest on floating point. Take A={1,2}, N=4, phi=(1+sqrt(5))/2. In central order (-2,-1,0,1,2), the bottom eigenvector is proportional to

q=(-1,phi,0,-phi,1), with k=phi.

The characteristic polynomial is (lambda^2+lambda-1)(lambda^3-lambda^2-5lambda-2). The cubic has its smallest root strictly between -phi and -1: it is increasing below -1, has value 2phi-4<0 at -phi and value 1>0 at -1. Hence -phi is indeed the least eigenvalue.

Direct convolution gives, after normalizing q,

integral D^2 |q|^2=3 < N=4,
R=3-phi^2=2-phi,
R/N=(2-phi)/4 approximately 0.0954915.

This exactly refutes the unconditional candidate integral D^2 |q|^2 >= N.
