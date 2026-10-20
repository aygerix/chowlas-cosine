# Complete cone-noise spectrum and Boolean confinement

2026-10-20. DESIGN / CHAIN(c) / ATTACK LOG. This is a quantitative test of the algebraic-taper question in CSTAR O6/F10, rather than a universal Chowla proof. The previous goal turn was progress: it excluded specified integer-cone encodings. This pass returns to the proposed confinement of rounding noise under quadric spikes. The older P81 computed the odd sector as 1/p; the calculation here resolves the entire operator, including its even exceptions. No novelty, external audit or Lean verification is claimed.

## Exact setting and theorem

Let p be any odd prime, V=Mat_2(F_p), Q={x:det x=0}, Q*=Q minus {0}. Use counting l2 norms and the unitary Fourier transform

    Ff(xi)=p^(-2) sum_x f(x) exp(2pi i <x,xi>/p).

The standard dot product or the polar form of determinant gives the same concentration operator, since the linear permutation/sign change relating them preserves Q. Let P_Q be support restriction and

    T=P_Q F* P_Q F P_Q on l2(Q).

Its COMPLETE spectrum is

| Eigenvalue | Multiplicity |
| --- | --- |
| 1 | 2p+1 |
| 1/p | (p+1)^2(p-2) |
| 1/p^2 | p^2+1 |

The 1-eigenspace W is exactly the span of the indicators of all maximal rank-one planes, from both rulings. Consequently every f supported on Q satisfies

    sum_(xi outside Q) |Ff(xi)|^2
        >=(1-1/p) dist(f,W)^2.

In particular Fourier support confined to Q is equivalent to membership in W. This is a uniform spectral gap for this explicit many-spike model; it is not a spectral gap for arbitrary integer supports or a statement that every finite-field construction fails.

## Elementary proof of the full spectrum

Write m=p+1, l=p-1. Nonzero rank-one matrices have unique coordinates (u,v,lambda), where u,v run over the normalized representatives (1,t), t in F_p, and (0,1), and lambda in F_p*. Thus Q* is an m-by-m grid of scalar lines, each of size l. The two rulings fix u or fix v. There are ml+1=p^2 points in each plane.

The underlying grid and two rulings are classical; see Cameron's [Notes on Classical Groups, p. 41](https://webspace.maths.qmul.ac.uk/p.j.cameron/class_gps/cg.pdf#page=41). This attribution is for the geometry, not a claim that the entire concentration/stability statement is quoted there. The local graph is an affine-polar local structure; no priority is claimed for the spectral calculation.

For the determinant polar form, each such plane is its own orthogonal complement. Moreover

    1_Q=sum_u 1_(plane u)-p delta_0.

Finite Fourier orthogonality therefore gives the unnormalized transform

    sum_(xi in Q) exp(2pi i <z,xi>/p)
      =p^3+p^2-p at z=0,
      =p^2-p at nonzero z in Q,
      =-p at z outside Q.

The standard dual cone is the same determinant-zero set. Hence, for x,y in Q,

    T_xy=(1/p)delta_xy+(1/p^2)1_Q(x-y)-1/p^3.

For nonzero x=u v^T and y=s t^T, det(x-y)=0 exactly when u,s have the same projective direction OR v,t do. Thus 1_Q(x-y) is a scalar-line blowup of the rook grid, with an additional origin joined to everything.

Split l2(Q) into the following orthogonal spaces.

1. Scalar fluctuations: sum zero separately on every scalar line, and value zero at the origin. The two nonidentity kernel terms vanish. Eigenvalue 1/p, dimension m^2(l-1).
2. Grid interactions: constant on scalar lines, value zero at the origin, and cell values with every row and column sum zero. The rook kernel acts by -l. Eigenvalue 1/p-l/p^2=1/p^2, dimension (m-1)^2=p^2.
3. Row/column effects: cell values alpha_u+beta_v, with sum alpha=sum beta=0, and origin zero. The rook kernel acts by pl. Eigenvalue 1/p+pl/p^2=1, dimension 2p.
4. The remaining two-dimensional radial space has value a at the origin and value b everywhere else. A direct substitution gives eigenvalue 1 on (a,b)=(m,1), and eigenvalue 1/p^2 on (a,b)=(-(p^2-1),1).

These dimensions sum to |Q|=p^3+p^2-p. Indicators of the two plane rulings span precisely the 2p row/column effects plus the first radial vector; their only linear relation is equality of the sums of the two rulings. This proves the spectrum, W identification and gap without a representation-theoretic assumption or an external eigenvalue theorem.

## Exact formula for arbitrary Boolean taper noise

Take ANY T0 subset Q*, write eta=1_T0, d=|Q*|=(p-1)(p+1)^2, s=|T0|/d, and set e=eta-s 1_Q*. Thus e(0)=0 and sum e=0. No independence or symmetry is assumed; symmetric selectors are included.

Let t_uv be the fraction selected on the scalar line (u,v), r_u its row average, and c_v its column average. Define

    E_within=l sum_uv t_uv(1-t_uv),
    E_inter=l sum_uv (t_uv-r_u-c_v+s)^2,
    E_ruling=lm [sum_u(r_u-s)^2+sum_v(c_v-s)^2].

The orthogonal decomposition above gives the EXACT identities

    ||e||^2=d s(1-s)=E_within+E_inter+E_ruling,
    ||1_Q Fe||^2=E_ruling+E_within/p+E_inter/p^2,
    L:=||1_(V minus Q) Fe||^2
      =(1-1/p)E_within+(1-1/p^2)E_inter.

The radial components vanish because e has zero origin and total sum. This is why the Boolean statement has no unspecified radial remainder.

**Balanced-ruling corollary.** If every row and every column has the same mean s, then E_ruling=0 and at most a 1/p fraction of the rounding-noise energy lies on Q. A selector constant on scalar lines and balanced in both rulings retains only a 1/p^2 fraction. Conversely concentration fraction at least 1-epsilon forces

    E_ruling >= [1-p epsilon/(p-1)] ||e||^2.

Thus nearly hidden noise must have quantitatively strong ruling effects; uniformly balanced non-ruling taper noise cannot hide under the dual-cone spikes. This includes the even sector left open by the old odd-only calculation. It does not constrain an arbitrary lift error that is not a function on this finite cone.

**Exact Boolean classification.** L=0 forces E_within=E_inter=0. Hence eta is constant along every scalar line and its binary cell matrix has the additive form alpha_u+beta_v. A binary matrix of this form depends only on u or only on v: two different rows differ by a nonzero constant, so they must be the all-zero and all-one rows, forcing every column to agree. If all rows agree, dependence is only on v. Therefore the selectors with perfectly confined centered noise are exactly unions of planes from a SINGLE ruling, with their common origin removed. Empty/full selectors are included.

## A false stability strengthening and a valid replacement

It is FALSE that vanishing relative leakage forces relative Hamming proximity to a single ruling. Select the union of one plane from each ruling, removing the origin. Its binary grid is eta_uv=1 when u=u0 OR v=v0. All formulas are exact:

    |T0|=(p-1)(2p+1),
    s=(2p+1)/(p+1)^2,
    L=(p-1)^2/(p+1),
    L/||e||^2=(p^2-1)/[p^2(2p+1)] ->0.

Yet the nearest Boolean union from a single ruling differs in p(p-1) points, a fraction p/(2p+1)->1/2 of |T0|. These are even selectors. Exact classification cannot be silently promoted to density-independent relative one-ruling stability.

A weaker uniform stability theorem DOES follow. Define the two-ruling threshold selector

    B={lambda u v^T : r_u+c_v-s >=1/2, lambda nonzero}.

The additive approximation g_uv=r_u+c_v-s has

    sum_Q* |eta-g|^2=E_within+E_inter <=p L/(p-1).

Every misclassified Boolean point contributes at least 1/4 to this sum. Therefore

    |T0 symmetric_difference B| <=4p L/(p-1).

After sorting row and column means, B has nested row sets. Small relative leakage therefore forces proximity to a threshold pattern formed from both ruling directions, rather than arbitrary random-like choices. The mixed-two-plane counterexample is itself such a pattern. This is an explicit structural alternative with a uniform quantitative error, not just exact zero-leakage rigidity.

## Testing the exact escape in an integer radial-fiber model

The exact classification identifies a genuine finite-field escape, not just an obstruction. Test its one-ruling integer analogue as follows. For each X choose ANY subset U_X of primitive integer vectors modulo sign with ||u||<=X. Retain every rank-one matrix u w^T with u in U_X and 0<||w||<=X/||u||, including both signs of w. Let N be its symmetric cardinality, n=N/2. U_X can vary arbitrarily with X and need not have uniform angular density.

Use the critical injective CRT encoding from the previous pass: X divisible by four, h=(3X/2)+(1,3,5,7), P=product h_i, C_i=P/h_i. Its fixed CRT residues (0,1,-1,0) give a phase matrix Y/X with singular values 2pi X/h_2 and 2pi X/h_3. For X>=72 both belong to [4,44/7]. The earlier rational Sturm/Bernstein certificate proves that the unit-disk transform is less than -1/50 throughout this interval.

For each u put R=X/||u||>=1. The phase on its w-disk is a linear form of norm t/R, with t in that interval, so its integral is at most -pi R^2/50. Unit-cell comparison bounds the lattice error by 76R: the union of cells differs from the radius-R disk in area at most 4pi R, the within-cell phase error is less than 5/R, and there are at most 4pi R^2 cells. Thus the total error is less than 24pi R<76R. Removing the origin improves the upper bound. The nonzero disk count N_u is at most pi R^2+10R, so

    sum_(0<||w||<=R) cos(phase) <=-N_u/50+77R.

On the square shell ||u||_infinity=k there are at most 4k canonical vectors, each of Euclidean norm at least k. Consequently sum_(u in U_X) R<=4X^2. Summing proves the uniform paper bound

    D_A(theta)<=-N/50+308X^2,
    M(A)>=n/50-154X^2.

In particular if n/X^2 tends to infinity, M(A)>=n/100 eventually; explicitly n>=15400X^2 suffices. This rules out ALL such directional choices retaining the logarithmic counting surplus under this CRT encoding. It does not cover arbitrary scalar encodings, angular truncations within each w-disk, or the two-ruling threshold patterns which simultaneously restrict both factors.

The removal of all ||u||<sqrt(X) still leaves n~(3/2)X^2 log X, by the earlier primitive harmonic sum and its O(X^2) error. Thus deleting every individually large plane does not escape this bound. The finite test additionally changes the allowed angular half-plane with the size of u, so it does not assume a common angular profile. This is an extension of the existing disk-resonance mechanism, not a separate universal proof architecture.

## A different test removes both angular and full-fiber assumptions

The preceding estimate still assumes complete w-disks. A rotational-average test removes that assumption on an outer annulus, at the price of a stronger encoding hypothesis.

**Annular-subset theorem.** Let X>=1 and take ANY nonempty collection of distinct sign-pairs of integer rank-one matrices satisfying

    3X/5<=||M||_F<=X.

Choose four pairwise coprime positive integers h_i>=1000X, P=product h_i, and C_i=P/h_i. Their scalar encoding is injective on the full Euclidean ball of radius X: a nonzero kernel vector has at least two coordinates divisible by different h_i and therefore norm at least sqrt(2) min h_i>2X. Form A from the positive absolute encodings, n=|A|. Then

    M(A)>=n/12.

There is no angular regularity, density, full-fiber or asymptotic cardinality hypothesis in this theorem. The encoding assumption is substantial.

Proof: for a planar rotation R_phi and any rank-one M,

    (1/(2pi)) integral cos(5<R_phi,M>/X) dphi
       =J0(5||M||_F/X).

Here J0(t) is the circle average of cos(t cos phi), with series sum_k (-1)^k(t^2/4)^k/(k!)^2. Indeed <R_phi,M>=(M11+M22)cos(phi)+(M21-M12)sin(phi), and the sum of the squares of these two coefficients equals ||M||_F^2+2det M=||M||_F^2. The rational even Taylor sum through degree 40 proves

    J0(t)<-1/10 for 3<=t<=5.

The omitted alternating tail is decreasing and begins negative. The entire interval sign is independently certified by exact Sturm root count and rational Bernstein controls. Thus for SOME phi the sum of these continuous matrix-phase cosines is less than -n/10, regardless of how the angular subset was selected.

Put Y=5R_phi. Round h_i Y_i/(2pi X) to an integer k_i, and choose j modulo P by j=k_i mod h_i. At theta=2pi j/P the scalar encoding phase agrees modulo 2pi with the coefficient matrix (2pi k_i/h_i). Its Frobenius distance from Y/X is at most 2pi/(1000X), so the phase error on every M is at most 2pi/1000. Cosine is 1-Lipschitz. Hence

    f_A(theta)<(-1/10+2pi/1000)n<-n/12.

The last strict inequality follows already from pi<22/7. This proves the theorem, not merely a collection of sampled phase dips.

The explicit finite tests use X=24,64 and h=(1500X)+(1,3,5,7), which are pairwise coprime at those X. They include the whole annulus, a genuinely two-ruling threshold u1^2/||u||^2+w1^2/||w||^2>=1, a modularly coupled selection, and a seeded arbitrary sign-pair selection. None of the last three requires complete radial fibers. All eight point certificates have M>n/12; the largest annular support has n=41804 and certified R>67.86. These are failed constructions, not new small-ratio records.

**Countercontrol to overextension.** A positive radial taper can evade ALL such rotational averages. Let rho be the autocorrelation of the indicator of a radius-1/2 disk, normalized at the origin, so

    rho(r)=(2/pi)[arccos(r)-r sqrt(1-r^2)] for 0<=r<=1,
    rho(r)=0 for r>1.

After normalization to total mass one, its two-dimensional Fourier transform is F_disk(t/2)^2>=0. Mixing the corresponding positive-definite plane profiles over primitive directions also gives a nonnegative full matrix-phase front. This is a fractional-profile identity, not a Boolean construction. It shows exactly why the annular sign argument cannot be extended to arbitrary radial tapers: the inner layers can compensate the negative outer average. The next attempt must address Boolean realization of this radial profile, not silently assume that every compact cutoff has a negative rotational transform.

## Finite checks, status and next decision

The producer src/cstar_cone_confinement.py runs on Dirichlet. For p=3,5,7 it constructs the full integer matrix p^3 T, verifies its cubic polynomial EXACTLY over the integers, and verifies the stated multiplicities from dimension and two trace identities. Separate exact residue counts on all p^4 Fourier arguments check the underlying cone transform. Full ambient unitary FFTs corroborate the exact rational noise energies; they are not used as proof of the identities.

The probes include a single ruling, a ruling-balanced permutation pattern, an even scalar fluctuation, a mixed pair of planes, and seeded even selectors (seed 20261022). Data include every Boolean mask, exact energies, closest single-ruling distances, and two-ruling threshold errors. The p=3 even scalar probe is the whole cone and has zero variance; no nonzero ratio is attributed to it.

An independent standard-library verifier enumerates the cone in a different order, reconstructs the Fourier kernel by exact residue counts, checks an explicit complete eigenbasis and the plane span's exact Gram rank, and rechecks all 15 Boolean probes and threshold inequalities without importing producer code or floating arithmetic. This is a computational cross-check, not an independent mathematical-agent review. A new required reviewer launch failed with the configured default model gpt-daybreak-blue-latest unavailable; independent-agent/Lean audit remains incomplete.

The separate radial-fiber producer tests three patterns at X=96,128: deleting all short u, restricting additionally to a wedge, and changing the angular half-plane with u's dyadic scale. It verifies exact distinctness and the CRT identities, and certifies a negative point with 112-bit Arb. These are lower witnesses for M, not global upper estimates. The paper inequality is uniform in the directional subset and does not rely on six finite cases.

The reverse-factor radial verifier independently re-enumerates w before u and uses the smaller direct off-diagonal phase period h_2 h_3 instead of the producer's encoded CRT root, checking all six set hashes and rational point bounds at 160 bits. The rotational producer verifies its J0 interval by two exact algorithms and uses 128-bit Arb at the chosen exact CRT roots. Its independent reverse-factor verifier reconstructs all masks and hashes, rechecks the Bernstein certificate, and evaluates the direct four-residue phase at 176 bits. FFTs or floating-angle probes only choose candidate points.

Reproduce on Dirichlet:

    src/dirun.sh -c 2 -m 4 -t 180 python src/cstar_cone_confinement.py
    src/dirun.sh -c 2 -m 4 -t 180 python src/cstar_cone_confinement_verify.py
    src/dirun.sh -c 2 -m 4 -t 180 python src/cstar_cone_directional.py
    src/dirun.sh -c 2 -m 4 -t 180 python src/cstar_cone_directional_verify.py
    src/dirun.sh -c 2 -m 4 -t 180 python src/cstar_cone_rotation.py
    src/dirun.sh -c 2 -m 4 -t 180 python src/cstar_cone_rotation_verify.py

Data: experiments/cone_confinement_2026-10-20/{results,verification,directional,directional_verification,rotation,rotation_verification}.json. The full-spectrum paper statement holds for every odd prime; computation covers only p=3,5,7. The two integer model theorems have distinct explicit encoding and support hypotheses. None constructs a general adaptive certificate or resolves full Chowla. No novelty or external/Lean audit is asserted.

**Strategic review.** Stop treating arbitrary correlated taper noise as automatically capable of hiding on the cone: its exact escape space is small and geometrically specified. Also stop the stronger single-ruling stability claim: the explicit mixed-plane sequence refutes it. Continue with the valid two-ruling threshold alternative. The exact one-ruling escape was tested in an integer model: arbitrary directional selection with complete radial fibers is excluded when it retains the counting surplus, under the stated critical CRT encoding. Rotation averaging then excluded arbitrary angular selections in an outer annulus under a different, phase-rich CRT encoding. A positive radial autocorrelation supplies an actual fractional escape from that averaging test, so do not broaden the hard-annulus theorem to all tapers.

The next concrete construction question is Boolean radial realization of that disk-autocorrelation profile with error confined to its spikes, including the finite-field ruling effects forced by the exact spectrum. A zero/one support has not been produced and the finite-field constant-density formula does not automatically apply to a changing radial marginal. On the proof side this becomes the still-missing multiscale/coupled Boolean estimate, with a specified smooth profile rather than a generic restatement. Keep a construction line outside cone/ruling models and the unrestricted adaptive-certificate line active; these model results do not close either. Full Chowla remains open.
