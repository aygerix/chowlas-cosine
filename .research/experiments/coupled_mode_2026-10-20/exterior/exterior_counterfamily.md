# Exact Boolean weak-W1 family with weak exterior spectrum

20 October 2026. Research proof; the independent audits are archived in ../audit. This refutes the exterior-only alternative, not the full mixed W2 conjecture. The construction uses the previously audited three-color taper noise bound but supplies the additional uniform Fourier bound and exact direct-union reduction.

## 1. Axis-union identity

Let T=-T subset Z\{0}, n=|T|. Write C=B_T, E_T=({0} union T)+({0} union T)\({0} union T). For m>=2 form S=union_{j=1}^m T e_j in Z^m and N=mn.

Its exterior splits into the disjoint sets E_T e_j and T e_i+T e_j (i<j). A difference in S has exactly one nonzero coordinate. Thus no edge connects two distinct sets of this partition: if two distinct supports differ, a coordinate that is present at only one endpoint would have to vanish, unless one set is a single-axis component sharing an axis with a two-axis component; in that case the shared coordinate would have to agree, which is impossible because E_T and T are disjoint. Each pair block is C tensor Id+Id tensor C. Consequently

    K_E(S)=max(K_E(T),2K_C(T)).                         (1)

If C >= a J-e Id with a>0, then

    K_W1(S)<=max(e,m/a).                               (2)

Indeed W1 is a common cone over m copies of C. For k>=e its shifted quadratic form dominates

    k|z|^2+2 Re(conj(z) sum_j h_j)+a sum_j |h_j|^2,
    h_j=sum_{x in T}v_j(x).

This equals a sum_j |h_j+z/a|^2+(k-m/a)|z|^2, which is nonnegative when k>=m/a. Neither regularity nor a uniform eigenvector of C is assumed.

If D_T(theta)>=-G for every theta, every principal Fourier compression has minimum at least -G. Equation (1), together with C>=aJ-eI, yields

    K_E(S)<=max(G,2e).                                (3)

The mixed I/E edges have not been discarded from a claimed full-W2 bound: (1) and (3) concern the exterior principal block only.

## 2. Taper events with explicit safe constants

Let X>=2, 0<alpha<=1/2. Independently choose eta_d with probability p_d=2alpha(1-d/X), d=1,...,X. Put T=+-{d:eta_d=1}, mu=alpha(X-1), and L>=log(4X), L>=1.

The previously proved three-color noise argument gives C=P_T-2alpha I+Z_T and P_T >= (2alpha/3)J. An explicit safe expectation constant is

    E||Z|| <= 216 alpha sqrt(X L)+72L+3.                (4)

For completeness, condition on a coloring and selected endpoints. The centered lag matrices have rectangular variance v<=4alpha n_* and summand norm R<=2. Matrix Bernstein gives tail d exp[-s^2/(2(v+Rs/3))], d<=4X. At s(u)=sqrt(2v(L+u))+(2R/3)(L+u), that tail is <=exp(-u). Integrating through this parametrization gives expected norm <=2sqrt(2vL)+(4R/3)L. Jensen and E n_*<=2alpha X give <=8alpha sqrt(XL)+(8/3)L. Multiply by 27, then add the at-most-three degenerate entries per row. This proves (4). The three-color identity and variance derivation are in the cited prior source.

By Markov, with probability >=3/4,

    C >= aJ-eI,
    a=2alpha/3,
    e=2alpha+864alpha sqrt(XL)+288L+12.                (5)

For the additional global bound, write

    D_T(theta)=2alpha(F_X(theta)-1)+R(theta),
    R(theta)=2 sum_d (eta_d-p_d)cos(d theta),

where F_X>=0 is the Fejer kernel. Each summand in R is centered, bounded by 2, and total variance <=4alpha X. Also deterministically |R'|<=X(X+1). Take J=ceil(32X^2) equally spaced angles. Nearest-grid interpolation error is <1. Scalar Bernstein and a union bound show that with probability >=7/8,

    ||R||_infinity <=1+sqrt(8alpha X log(16J))+(4/3)log(16J).

For integer X>=2, J=32X^2 and log(16J)=log(512X^2)<=4log(4X)<=4L. Therefore one safe simplification is

    D_T(theta)>=-G,
    G=2alpha+1+6sqrt(alpha X L)+6L.                    (6)

Indeed sqrt(32)<6 and 16/3<6. All angles are controlled, not just a numerical mesh.

Finally Var|A|<=mu, so with probability >=1-4/mu one has mu/2<=|A|<=3mu/2, and hence mu<=n<=3mu. For mu>32 the three good events intersect with positive probability, by the union bound.

## 3. A completely specified deterministic counterfamily

For integer t>=8 put

    X=t^8, alpha=t^-2, m=t,
    L=2+8 ceil(log_2 t),
    a_t=2/(3t^2),
    e_t=2/t^2+864t^2 L+288L+12,
    H_t=1+6t^3 L+6L, G_t=2/t^2+H_t,
    mu_t=t^6-t^-2.

Here L>=log(4X), sqrt(L)<=L, and mu_t>32. Define A_t as the first subset in lexicographic order of its length-X characteristic bit vector (0<1), among subsets of {1,...,X} for which, with T_t=+-A_t,

    mu_t <= |T_t| <= 3mu_t,
    B_(T_t) >= a_t J-e_t I,
    ||R_t||_infinity <= H_t,
    [-X,X] subset W2(T_t),
    P_t=integral 2alpha F_X R_t^2 <=32alpha n0,
    R_t=D_(T_t)-2alpha(F_X-1), n0=2mu_t.               (7)

These stronger joint conditions ensure the full-W2 companion uses the exact same family, not a potentially different good realization. The matrix event fails with probability at most 1/4 and the supremum event at most 1/8. The nonnegative P_t has expectation at most 4alpha n0, so its event fails with probability at most 1/8. The size event fails with probability at most 4/mu_t<1/8. For filling, each h in [1,X] has at least X/24 signclass-disjoint representations h=u+v with nonzero |u|,|v|<=floor(3X/4) when X>=32: there are at least X/4-2 unordered candidates, their signclass graph has maximum degree 2, and a greedy matching retains at least one third. Each matching pair succeeds independently with probability at least alpha^2/4. Thus filling failure is at most X exp(-alpha^2 X/96)=t^8 exp(-t^4/96)<1/8 for t>=8. The total failure probability is less than 3/4, so (7) is nonempty for every t>=8.

This is an exact, albeit computationally impractical, deterministic definition: the matrix test is rational PSD; supremum bounds on R_t become rational Chebyshev polynomial inequalities on [-1,1]; P_t is the rational constant Fourier coefficient of 2alpha F_X R_t^2; and support filling is a finite set check. Exact real-algebraic decision procedures determine all tests. The supremum condition implies D_(T_t)>=-G_t. No pseudorandom seed or unverified numerical eigensolver is part of the definition.

Form S_t=union_{j=0}^{t-1} Q_t^j T_t in Z, Q_t=10X+1. The base encoding preserves W2 adjacency: every coordinate coefficient in u-v-s is at most 5X in absolute value, and Q_t-1=10X makes cancellation of the highest nonzero place impossible. In particular this is an ordinary finite symmetric Boolean integer support, with

    N_t=t|T_t| asymp t^7.

Equations (2),(3),(7) give

    K_W1(S_t)<=max(e_t,3t^3/2)=O(t^3+t^2 log t),
    K_E(S_t)<=max(G_t,2e_t)=O(t^3 log t).

Therefore

    K_W1(S_t)/sqrt(N_t)->0,
    K_E(S_t)/sqrt(N_t)->0.                             (8)

Thus any universal square-root full-W2 proof must genuinely allow mixed I/E directions or some equivalent mechanism. Independent exterior negativity alone is false even conditional on weak W1. The joint conditions in (7) also permit the rigorous full-W2 lower certificate in section 6 below.

## 4. Existing balanced-layer example is not a countercontrol

The prior balanced-layer two-level certificate uses levels i,j with i+j=k. For odd k>=3, (i,j)=((k-1)/2,(k+1)/2); for even k>=4, (i,j)=(k/2-1,k/2+1). Both indices are strictly between 0 and k. Those trial layers already lie entirely in E. The established sqrt(N)/22 bound therefore holds exterior-only on that particular weak-W1 family. It also survives the interval implant because the trial remains exterior and independent of the interval coordinate. This confirms that the present axis-union operation, not the old balanced example alone, is the needed obstruction.

## Sources and checks

Prior source: ../dependencies/weak_w1_taper_proof.md, sections 1-2. Prior independent audit: ../dependencies/weak_w1_taper_audit.md. The only imported concentration result is rectangular/scalar Bernstein; the prior source gives Tropp's User-Friendly Tail Bounds, Theorem 1.6.

Exact entry-level tests and integer-encoding checks: check_axis_decomposition.py and its JSON output in this directory. Floating-point eigenvalues only diagnose those finite instances; the asymptotic theorem is the algebraic/probabilistic argument above.

## 5. Stronger localization: even the entire noncentral W2 block is weak

Let H=B_{W2(S)\{0}}. This includes all I/E coupling except edges at the center. Let v_i be the T_i coordinates, w_i the E_T e_i coordinates, and z_ij the pair coordinates, viewed as an n-by-n array. The single-axis (v_i,w_i) block is a principal compression of multiplication by D_T, hence its energy is >=-G(||v_i||^2+||w_i||^2).

The pair diagonal is C tensor Id+Id tensor C. By C>=aJ-eI its energy is >=a(||z_ij 1||^2+||z_ij^*1||^2)-2e||z_ij||^2. The only pair/single-axis cross terms are 2Re<v_i,z_ij 1> and 2Re<v_j,z_ij^*1> (with conjugates arranged according to the array convention). Completing each square bounds their combined contribution below by

    -(||v_i||^2+||v_j||^2)/a-2e||z_ij||^2.

No pair-to-E_T or distinct-pair cross terms exist. Summing gives

    K_{W2(S)\{0}} <= max(G+(m-1)/a,2e).              (9)

For the exact S_t above this is O(t^3 log t)=o(sqrt(N_t)). Consequently any square-root Rayleigh witness in full W2(S_t), if one exists, must use the original center coordinate non-negligibly in the appropriate quantitative sense. Equation (9) does not compare its direction with the W1 bottom vector: that vector need not equal the coordinate vector at zero.


## 6. Full W2 stays strong on this exact same enhanced family

This companion was derived independently in ../order/direct_union_order_audit.md, section 5. Let V=||R_t||_2^2 and c0=<D_T,R_t>. Since p_d<=2alpha and n comparable to n0,

    V=n-4 sum_d eta_d p_d+2 sum_d p_d^2=(1+O(alpha))n,
    c0=2 sum_d eta_d(1-p_d)=(1+O(alpha))n.

The filling condition ensures R_t is supported on W2(T). It has mean zero. Hence q=(sum_{i=1}^m R_t(theta_i))/sqrt(mV) is a unit W2(S) polynomial orthogonal to the constant 1. The exact compression on span{1,q} is

    [[0,b],[b,d]],
    b=sqrt(m)c0/sqrt(V)=(1+O(alpha))sqrt(mn),
    d=integral D_T R_t^2/V.

Using (7),

    d=P_t/V-2alpha+integral R_t^3/V <=O(alpha)+H_t.

All cross-coordinate diagonal terms vanish by the zero means. Since H_t=O(t^3 log t)=o(sqrt(mn)), the negative eigenvalue gives

    K_W2(S_t)>=(1-o(1))sqrt(N_t).

Combining the noncentral upper bound (9), and the fact that the only deleted row has off-diagonal norm sqrt(N_t), also gives

    K_W2(S_t)<=sqrt(N_t)+o(sqrt(N_t)).

Thus the exact same counterfamily satisfies K_W2(S_t)/sqrt(N_t)->1, while its W1 block, exterior block, and whole center-deleted W2 block are all o(sqrt(N_t)). This is a separation, not a full-W2 counterexample.
