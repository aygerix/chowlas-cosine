# Full W2: a coupled square-root mode invisible to both principal blocks

20 October 2026. CHAIN / ATTACK LOG. Text-only checkpoint. This resolves the proposed exterior-only alternative and identifies the surviving mixed mechanism on one adversarial family; it does not prove the universal full-W2 or Chowla claim. No new P/E identifier is assigned.

## Outcome and scope

There is a single deterministic sequence of genuine symmetric Boolean integer supports S_t, with N_t=|S_t| tending to infinity, such that

    K_W1(S_t)/sqrt(N_t) -> 0,
    K_E(S_t)/sqrt(N_t) -> 0,
    K_(W2 minus {0})(S_t)/sqrt(N_t) -> 0,
    K_W2(S_t)/sqrt(N_t) -> 1.

Here E=W2 minus W1. Thus neither a negative direction confined to the original first neighborhood nor one confined to the exterior supplies the square-root bound on this family. Even the entire noncentral full-W2 block is weak. The surviving bound is a mixed, center-coupled mode.

For each fixed 0<c<1, eventually exactly one full-W2 eigenvalue is below -c sqrt(N_t). Its normalized bottom eigenvector has center mass tending to 1/2 and exterior squared norm tending to zero. The exterior is nevertheless energetically essential: deleting it leaves only the weak W1 compression. Small coefficient norm does not license discarding its energy or cross terms.

The main theorem and its spectral corollaries passed [independent audit](../experiments/coupled_mode_2026-10-20/audit/FULL_W2_COMPANION_AUDIT.md). These are research paper proofs with independent algebraic audit, not formal proof-assistant verification, numerical extrapolations, or claims of literature priority. The universal existence of c>0 with K_W2(S)>=c sqrt(|S|), and the underlying Chowla square-root target, remain unproved here.

Proof sources, audits, exact finite checks and exploratory diagnostics are in the [source archive](../experiments/coupled_mode_2026-10-20/README.md). Only this pass is packaged, with the small prior inputs needed to make its proofs and scripts portable. The restored research files are not a restored Git repository: no unavailable index was reconstructed, and no commit or remote push was made.

## 1. Definitions and what is actually being refuted

For finite nonempty S=-S in Z excluding 0, put

    N=|S|,  D_S(theta)=sum_(s in S) exp(i s theta),
    I(S)={0} union S=W1(S),
    W2(S)=I(S)+I(S),  E(S)=W2(S) minus I(S).

All Fourier integrals and inner products use normalized Haar measure. For a finite row set U, define B_U(u,v)=1_S(u-v) and K_U(S)=-lambda_min(B_U). The global certificate is K_global(S)=-min D_S, and K_U<=K_global. If S=A union (-A), then D_S=2 sum_(a in A) cos(a theta), so K_global=2M in the cosine-minimum normalization.

The statement refuted is the existence of a universal c>0 such that every Boolean symmetric support satisfies

    K_W1(S)>=c sqrt(N)  OR  K_E(S)>=c sqrt(N).

This is strictly stronger than allowing arbitrary full-W2 trial vectors, because the latter retain the cross block. Weak diagonal principal blocks do not imply a weak full matrix. Conversely, a lower bound for full W2 on this particular family is not a universal theorem.

## 2. The exact independent-axis reduction

Start with T=-T in Z excluding 0, n=|T|, C=B_T, and m>=2. On independent axes set

    S=union_(j=1)^m T e_j in Z^m,  N=mn.

The exterior is the disjoint union of one-axis pieces E(T)e_j and two-axis pieces T e_i+T e_j, i<j. There are no edges between different pieces. Each one-axis block is B_E(T); each two-axis block is the Kronecker sum C tensor Id+Id tensor C. Consequently, exactly,

    K_E(S)=max(K_E(T), 2K_C(T)).

Assume the selected base adjacency has a rank-one mean lower bound

    C >= a J-e Id,  a>0, e>=0.

The W1 matrix is a common center over m copies of C. For center coordinate z and copy vectors v_j, set h_j=sum_x v_j(x). After shifting by k>=e, its quadratic form is bounded below by

    a sum_j |h_j+z/a|^2+(k-m/a)|z|^2.

Hence K_W1(S)<=max(e,m/a). This uses neither regularity of C nor an assumed constant eigenvector. If also D_T>=-G pointwise, every Fourier compression of the base is bounded below by -G, and therefore

    K_E(S)<=max(G,2e).

Sources: [axis-union proof](../experiments/coupled_mode_2026-10-20/exterior/exterior_counterfamily.md), [independent reduction audit](../experiments/coupled_mode_2026-10-20/audit/EXTERIOR_AXIS_UNION_AUDIT.md).

## 3. Stronger: deleting only the center already makes W2 weak

Write H=B_(W2(S) minus {0}). Let v_i be the T e_i coordinates, w_i the E(T)e_i coordinates, and z_ij the pair coordinates as n-by-n arrays. The full one-axis (v_i,w_i) compression has energy at least -G(||v_i||^2+||w_i||^2).

The pair block has energy at least

    a(||z_ij 1||^2+||z_ij^* 1||^2)-2e||z_ij||^2.

Its only cross terms connect its row and column sums to v_i and v_j. Completing squares bounds the sum of these terms and the pair energy below by

    -(||v_i||^2+||v_j||^2)/a-2e||z_ij||^2.

There are no pair-to-E(T) edges and no edges between distinct pair blocks. Each v_i participates in m-1 pairs. Thus

    H >= -h Id,
    h=max(G+(m-1)/a, 2e).

This controls all noncentral W1/exterior coupling, not merely two separate diagonal blocks. Its proof and audit are in the archived axis-union sources.

## 4. The same random base satisfies every required event

Take integers t>=8 tending to infinity and

    X=t^8, alpha=t^-2, m=t,
    p_d=2alpha(1-d/X),  1<=d<=X.

Select the positive signclasses independently with Bernoulli variables eta_d of means p_d, and reflect to obtain T. Put n0=2alpha(X-1). The prior three-color decoupling theorem gives

    C >= (2alpha/3)J-e Id,
    E e=O(alpha sqrt(X log(4X))+log(4X)+alpha).

The diagonal shift can be absorbed into this estimate. The proof explicitly handles the dependence of endpoint and lag variables and the shared Bernoulli variable for opposite signs. Mere independent-entry concentration would be invalid. A copy of the [taper proof](../experiments/coupled_mode_2026-10-20/dependencies/weak_w1_taper_proof.md) and its [audit](../experiments/coupled_mode_2026-10-20/dependencies/weak_w1_taper_audit.md) is included.

Define the Fejer kernel and centered noise by

    F_X(theta)=(1/X)|sum_(r=0)^(X-1) exp(i r theta)|^2,
    Z=D_T-2alpha(F_X-1).

Use the explicit rational thresholds from the completed construction:

    L=2+8 ceil(log_2 t),  mu=t^6-t^-2,  n0=2mu,
    a=2/(3t^2),  e=2/t^2+864t^2 L+288L+12,
    H_t=1+6t^3 L+6L,  G=2/t^2+H_t.

Choose the lexicographically first length-X characteristic bit vector, with 0<1, whose support satisfies all five conditions:

1. mu<=n<=3mu.
2. C >= aJ-e Id.
3. ||Z||_infinity<=H_t, hence D_T>=-G.
4. [-X,X] is contained in W2(T), so all frequencies of Z are admissible.
5. P=integral 2alpha F_X Z^2 <=32alpha n0.

The scalar supremum event follows from Bernstein on a deterministic Fourier mesh with a rigorous derivative bound, not an unverified grid minimum. For support filling, each h in [1,X] has order X representations h=u+v with |u|,|v|<=3X/4 and distinct signclasses. Their representation graph has bounded degree, so order X of the pairs use disjoint signclasses. Each succeeds with probability at least alpha^2/4. A union bound gives failure at most X exp(-c alpha^2 X), which tends to zero.

For the fifth event, independence and the nonnegative Fejer weight give

    E P <= 4alpha n0.

For t>=8 the five failure probabilities are, in order, less than 1/8, at most 1/4, at most 1/8, less than 1/8, and at most 1/8. In particular the filling failure is at most t^8 exp(-t^4/96)<1/8. Their sum is less than 3/4, so a simultaneous good base exists for every t>=8. No independence between these good events is asserted or needed. All defining tests are finite rational or real-algebraic tests: matrix positivity, set membership, rational Fourier sums, and polynomial nonnegativity on [-1,1]. Thus the selection is exact, although computationally impractical.

This quantifier is essential. The original three-condition selection, using only cardinality, adjacency and a Fourier lower bound, did not establish the full lower bound. The completed source now strengthens that definition with the centered supremum, support-filling and weighted-energy conditions above. Every assertion here concerns this enhanced, jointly selected family.

For this sequence,

    n is comparable to t^6,  N is comparable to t^7,
    e=O(t^2 log t),  G=O(t^3 log t),  m/a=(3/2)t^3.

Consequently K_W1=O(t^3), K_E=O(t^3 log t), and h=O(t^3 log t). All are o(sqrt(N)). A stricter asymptotic joint selection gives n=(2+o(1))t^6 and the sharper O(t^3 sqrt(log t)) bound, but those stronger rates are not silently attributed to the displayed rationalized selection. Sources: [explicit enhanced family](../experiments/coupled_mode_2026-10-20/exterior/exterior_counterfamily.md), [joint-event audit](../experiments/coupled_mode_2026-10-20/audit/FULL_W2_COMPANION_AUDIT.md), [same-family full-W2 proof](../experiments/coupled_mode_2026-10-20/order/direct_union_order_audit.md).

## 5. Centering exposes the square-root mixed mode

On the same realization let

    V=||Z||_2^2=2 sum_d(eta_d-p_d)^2,
    c0=<D_T,Z>=2 sum_d eta_d(1-p_d).

Since p_d<=2alpha and n is comparable to n0,

    V=(1+O(alpha))n,  c0=(1+O(alpha))n.

The diagonal energy of the normalized centered polynomial satisfies

    d=integral D_T Z^2/V
      =P/V-2alpha+integral Z^3/V
      <=O(alpha)+||Z||_infinity.

Only an upper bound for d is needed. No unsupported assertion that the cubic noise integral cancels is used.

For the axis union define

    q=(1/sqrt(m V)) sum_(i=1)^m Z(theta_i).

Support filling puts q inside W2(S). Its zero mean makes q orthogonal to the center polynomial 1, and ||q||=1. All mixed-coordinate contributions to its diagonal energy vanish by a zero-mean factor. The exact compression on span{1,q} is

    [[0,b],[b,d]],
    b=sqrt(m)c0/sqrt(V)=(1+O(alpha))sqrt(N).

Its negative eigenvalue magnitude is

    (sqrt(d^2+4b^2)-d)/2 >= b-max(d,0)/2.

Since max(d,0)=o(sqrt(N)), this proves K_W2(S)>=(1-o(1))sqrt(N). The trial is neither confined to E nor required to arise from a prescribed W1 bottom vector. Its negative coefficients on unselected base frequencies supply a small but important exterior component.

### An exact fixed-interior correction on this special family

The centered profile can also be corrected to have coefficient exactly 1 on the original support, but this requires an energy argument rather than Euclidean alignment. Define on the base

    W=sum_(s in T) p_|s| exp(i s theta),  q0=Z+W.

Then q0 has coefficient 1 on T and coefficient -p_|s| on unselected centered frequencies. Support filling makes the latter exterior frequencies. Hence

    ||q0||^2=n+O(alpha n),  ||W||^2<=4alpha^2 n.

Since D_T+G>=0 pointwise, weighted Cauchy gives

    integral (D_T+G)|Z+W|^2
       <=2 integral (D_T+G)|Z|^2
          +2 integral (D_T+G)|W|^2.

The first term is O(Gn), using the already proved centered-energy bound. The second is O((n+G)alpha^2 n), because D_T<=n pointwise. Consequently

    integral D_T|q0|^2<=O(Gn+alpha^2 n^2).

Let Q0=sum_i q0(theta_i)=D_S+r, with r supported in E(S). Zero means eliminate cross-coordinate terms, giving

    ||Q0||^2=(1+O(alpha))N,  ||r||^2=O(alpha N),
    integral D_S|Q0|^2
       <=O(mGn+m alpha^2 n^2)=o(N^(3/2)).

Indeed the normalized upper bound is O(G/sqrt(mn)+alpha^2 sqrt(n/m))=O(t^(-1/2)log t+t^(-3/2)). This proves the exact fixed-interior extension criterion for this particular joint family. It does not prove the criterion for arbitrary Boolean supports, and does not follow merely by replacing nearly uniform eigenvector coefficients with uniform ones. See the [independent fixed-interior audit](../experiments/coupled_mode_2026-10-20/audit/FULL_W2_COMPANION_AUDIT.md#8-optional-exact-interior-extension-on-this-same-family).

## 6. The star upper bound gives the exact asymptotic constant

In the center/noncenter decomposition write

    B_W2=[[0,s*],[s,H]],  ||s||^2=N,  H>=-h Id.

Here s is exactly 1 on S and 0 on E. Replacing H by -h Id gives the sharp star comparison

    K_W2 <= (h+sqrt(h^2+4N))/2.

Because h=o(sqrt(N)), the upper bound is (1+o(1))sqrt(N). Together with the centered two-mode lower bound,

    K_W2(S_t)/sqrt(N_t) -> 1.

This statement concerns the finite W2 compression. No matching upper bound for the global cosine minimum is asserted.

## 7. One negative outlier; vanishing exterior norm does not mean negligible exterior energy

Cauchy interlacing gives lambda_2(B_W2)>=lambda_1(H)>=-h. For each fixed 0<c<1, the bottom eigenvalue is eventually below -c sqrt(N), and every other eigenvalue is above that threshold. Thus the bottom is simple and is the unique square-root-scale negative outlier in this precise sense. Other smaller negative eigenvalues are not ruled out.

Let (z,v) be a normalized bottom eigenvector, with eigenvalue -kappa. Its energy and H>=-h Id imply

    kappa <= 2sqrt(N)|z| ||v||+h||v||^2.

Since kappa/sqrt(N)->1 and |z|^2+||v||^2=1, necessarily |z|^2->1/2 and ||v||^2->1/2. The center equation is s*v=-kappa z, so

    ||v+(kappa z/N)s||^2
       =||v||^2-(kappa^2/N)|z|^2 -> 0.

After a global phase choice the entire bottom vector therefore approaches the normalized negative star vector supported on {0} union S. Since s vanishes on E, the exterior squared norm tends to zero.

Nevertheless, write the bottom vector as u+w on W1 and E, with cross block M. The separate spectral lower bounds give

    <u,B_W1 u> >= -o(sqrt(N)),
    <w,B_E w> >= -o(sqrt(N)).

Their sum cannot account for the total energy -(1+o(1))sqrt(N). Hence

    2 Re <w,M u> <= -(1-o(1))sqrt(N).

This is an essential mixed energetic contribution even though ||w||->0. No claim is made that the diagonal energies separately have small absolute value: they can have large positive parts canceled by mixed terms. Treating small exterior mass as a small energy error would be invalid without an operator-norm estimate.

## 8. Carry-free encoding gives genuine integer supports

Use Q=10X+1 and the map

    (x_1,...,x_m) -> sum_(j=1)^m x_j Q^(j-1).

All coordinates tested in a full-W2 adjacency relation u-v-s have absolute value at most 5X. If their encoded sum were zero, reduction modulo Q would force the first coefficient to vanish because its absolute value is less than Q; repeat after division by Q. Thus the only vanishing relation is the coordinatewise zero relation.

The encoding preserves distinct W2 vertices, membership, all adjacency entries and the center/interior/exterior partition. Every theorem above therefore holds for ordinary finite symmetric Boolean subsets of Z, not a multiset, a weighted relaxation, or a torsion model. Cardinality has the stated scale; the largest encoded frequency is much larger and is not being bounded polynomially in N.

## 9. Exact checks, numerical diagnostics and the remaining question

The archive separates finite exact set/matrix identities from floating eigenvalue diagnostics. Exhaustive small-support checks verify the exterior decomposition, full-W2 integer encoding, and three-color identity by integer arithmetic. A separate exact compression check verifies ||sum Z_i||^2, the center coupling and diagonal energy. These finite checks corroborate assembly; the probabilistic and spectral proofs establish the infinite sequence.

Fresh tapered FFT samples with t=2,3,4,5,6 have N=264, 4368, 32208, 157790, 558936. Their computed two-dimensional certificate ratios are approximately 0.82248, 0.91245, 0.96359, 0.97302, 0.98103. The exterior fractions of the noncentral trial norm squared decrease from 0.29821 to 0.03692. These are seeded illustrative samples, not the lexicographically selected theorem family; the joint good-event conditions were not verified. The values are two-space calculations, not full-W2 minimum eigenvalues or certified spectral enclosures. Rounded FFT convolution diagnoses interval filling in all five samples, with maximum reported rounding discrepancy about 1.46e-11, but is not an exact membership certificate. See [script and data](../experiments/coupled_mode_2026-10-20/numeric/centered_taper_check.json).

The balanced-layer axis/Laguerre experiments are exploratory controls, not evidence that finite ratios force a universal asymptotic. Their floating eigenvalues are not certified spectral enclosures. Uncompleted searches are not reported as completed results.

The preceding bottom-mode repair obstruction showed that a successful direction need not repair one prescribed W1 ground state. This pass goes further: even searching for a strong negative direction wholly inside E can fail. What survives here is center coupling to an adaptively centered profile, with the positive Fejer mean removed.

The correct universal target must allow arbitrary mixed directions or an equivalent full coupled spectral argument. Whether Boolean support structure always forces such a square-root direction remains open. This checkpoint disproves the narrower exterior-only route and gives a rigorous sharp full-W2 certificate on the same counterfamily, not a solution to the universal problem.

## Optional continuation: allow positive spectral cost as well

A separate root-difference control uses S_r={e_i-e_j:i!=j}, N=r(r-1), and the center-deleted full-W2 matrix A. For its central coupling b=1_(S_r), an exact five-orbit reduction gives, for every tau_r=o(r),

    ||1_(-infinity,tau_r](A)b||^2/N -> 0,

while an explicit three-orbit Rayleigh vector gives K_W2(S_r)>=4r/9 for r>=4. The relevant punctured modes can therefore have positive cost comparable to sqrt(N); a universal response estimate cannot simply discard all of them. This control is not a weak-W1 family and does not refute a statement conditioned on weak W1. The [exact orbit proof](../experiments/coupled_mode_2026-10-20/multimode/root_orbit_low_cost_obstruction.md) passed [independent audit](../experiments/coupled_mode_2026-10-20/audit/AUXILIARY_ROOT_ORBIT_AUDIT.md). In fact this family has liminf K_W1/sqrt(N)>=sqrt(2)-1. The obstruction concerns a spectral projection; it does not exclude every low-Rayleigh-cost mixture using independent negative modes.

The exact bouquet compression [[0,sqrt(m)a],[sqrt(m)conj(a),h]] and its nonsingular Schur response are useful identities, but still need a universal Boolean estimate. A sufficient unproved extension target is to find r supported in E with ||D_S+r||^2<=C N and integral D_S|D_S+r|^2<=C N^(3/2). The weighted energy argument in section 5 proves this exact fixed-interior criterion on the present special family; its universal version remains unproved. Asymptotic alignment of a bottom eigenvector alone does not justify replacing its interior coefficients by exactly uniform ones, because the operator norm can be large. See [response identities and scope](../experiments/coupled_mode_2026-10-20/multimode/bouquet_response_and_scope.md).
