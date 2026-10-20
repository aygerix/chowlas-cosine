# Targeted W1-groundstate translation and leakage checks

20 October 2026. No universal Chowla or W2 bound is proved here.

## Normalization and exact compression

S=±A, N=|S|, D=Σ_{s∈S}e_s, I={0}∪S. Let q be a unit bottom eigenvector of B_I, with eigenvalue −κ. Its coefficient polynomial Q has support I. Every Qe_s, s∈I, is supported in W2.

The translated space has exact Gram G_st = ∫|Q|² e_(s−t), and cost H_st = ∫D|Q|² e_(s−t). Its certificate is −λ_min(H,G). Coefficient autocorrelation and convolution calculate these entries without constructing W2. Laurent multiplication is injective, so G is positive definite mathematically.

An independent explicit construction F_{w,s}=q_{w−s}, w∈W2, verifies G=F*F and H=F*B_W2 F for the first sample: maximum discrepancies 1.7e−16 and 1.8e−15. The compressed certificate is 12.91165, versus full W2 14.07608.

Write r=(D+κ)Q, R=||r||² and g=∫D|r|²/R. Then r is supported outside I and orthogonal to Q. The two-vector certificate is the negative minimum eigenvalue of [[−κ,√R],[√R,g]]. This distinction matters: success of all translations may already be explained by this smaller space.

## Exact rejection of a groundstate energy guess

The inequality ||DQ||²≥N for a W1 groundstate is false, even at A={1,2}.

Put φ=(1+√5)/2. On rows (−2,−1,0,1,2), the vector

    q=(1,−φ,0,φ,−1)/sqrt(2(1+φ²))

is the unique bottom eigenvector, with eigenvalue −φ. The odd block gives this eigenvalue. The even block plus φI has successive leading principal minors φ, √5, 3−√5, all positive, proving that no even eigenvalue is smaller.

Direct coefficient convolution gives ||DQ||²=3, whereas N=4. Hence R=(3−√5)/2. This refutes the exact constant-one inequality, not a conditional unspecified positive lower bound in the regime κ=o(√N).

## E99c-style tapered controls

Independent positive-frequency inclusion p_a=2α(1−a/X), X=round(n_target/α); reflect to form S. All ratios below use √N, not √|A|. Fresh seeds are in the scripts, and these are floating-point experiments, not asymptotic proofs.

For α=n_target^(−1/3), actual positive sizes 29,80,127,269,512,1006,2074,4086,8247 were tested. At the largest three:

- n=2074: κ/√N=.63641, translated certificate/√N=3.45476, R/N=1.29668, g=−69.1063.
- n=4086: κ/√N=.55882, translated certificate/√N=3.62662, R/N=1.19332, g=−76.9038.
- n=8247: κ/√N=.49675, translated certificate/√N=2.98793, R/N=1.07110, g=−71.8114.

All three bottom eigenvectors are odd, with center mass below 7e−25. R/N^(3/2) falls .02013,.01320,.00834. Thus an R~N^(3/2) sufficient condition for a shift-pair estimate does not match these finite controls. These observations alone are not an asymptotic refutation of an unspecified constant.

At n1006, the two-vector certificate already gives 1.75677√N, compared to 2.71306√N from all translations. Consequently the favorable full-space result does not establish a new universal mechanism beyond favorable signed exterior cost.

Changing exponent to β=.45 produces a center-mode transition at actual n2015: center mass .71535; κ/√N=.44444; R/N=14.68275; g=3498.414 (N4030). The two-vector ratio is .70750 while the full translated ratio is1.91928. The previously favorable exterior cost is therefore not robust under this modest change. No asymptotic conclusion is drawn.

At β=.4 and actual n2114 the state remains odd; κ ratio .49723 and translated ratio3.07297. The β=.45 n4079 test completed: q0²=.753257, κ/√N=.424190, R/N=21.04996, g=7235.987, two-vector ratio .684715, translated ratio1.459625. The n8192target run was deliberately interrupted after its groundstate diagnostics (q0²=.780482,R/N=29.75138,g=14772.939); no full translated certificate at that target is claimed. The new rigorous decoupling proof made further large numerics unnecessary.

## Boolean near-extremizer controls

For the previously recorded A50 support, κ/√N=.550789, R/N=.067995, g=4.857293, two-vector ratio .612691, translated ratio .683960. The known full W2 ratio is about .705699. Singer difference supports through p31 have translated ratios .8587–.9934, with no observed collapse. These controls are not universal evidence.

## New structural obstruction, now with a proved weak-W1 base

An odd interval groundstate can be implanted on an independent coordinate beside a base support T. For S=(T×{0})∪({0}×±[1,L]), a vector supported solely on the interval coordinate remains an exact W1 eigenvector. A rigorous interval even/odd gap of order L permits it to remain the bottom state if K_W1(T)=o(L).

The entire translated groundstate space is then of the form

    Q_U(y)[p_T(x)+p_U(y)],

not a tensor-product trial space. For every fixed y its x-frequency support is {0}∪T, so the T energy is bounded below by −K_W1(T) times its norm. Pointwise the interval energy is at least −2L. Therefore this entire product-space certificate is at most K_W1(T)+2L.

The missing base family is now established in weak_w1_taper_proof.md by three-color decoupling and matrix Bernstein, independently checked in this research pass. It was important not to silently promote the old E99c numerical scaling to a theorem. Choose K_W1(T)≪L≪√|T|; this defeats the full translated-bottom-vector square-root programme when combined with the interval-gap proof in the Schur report. This does not refute full W2: W2 includes mixed directions absent from this trial space.

## Reproduction

- translated_kernel.py/json: dense generalized compression, β=1/3 up to target1024.
- translated_kernel_large.py/json: FFT matrix-free generalized compression through target8192.
- translated_kernel_large_moments.py/json: independent groundstate moment and Gram diagnostics on the same larger supports.
- translated_kernel_beta.py/json: β=.4,.45 controls.
- translated_kernel_beta_large.py/json: larger β=.45 runs.
- translated_kernel_controls.py/json: A50, Singer and intervals.
- verify_translated.py and verification.json: independent direct W2 assembly check.

Generalized eigensolver residuals near1e−7 establish numerical consistency, not a rigorous enclosure of a least eigenvalue. The trial vectors nevertheless define valid variational lower certificates when their Rayleigh quotients are evaluated with controlled arithmetic; no interval arithmetic certification is claimed in these files.

### Unconditional consequence of the implant, regardless of the missing base family

The reduction is more informative than a conditional counterexample. Choose a universal C large enough and L=ceil(C(K_W1(T)+1)). The interval spectral gap ensures the localized odd groundstate is unique. Since K_W1(T)≥1 for nonempty T, L≤C'K_W1(T). The above fixed-y energy bound yields

    K_translated(S) ≤ C'' K_W1(T),       |S|≥|T|.

Consequently, a universal positive square-root bound for the full translated-bottom-vector space implies a universal positive square-root bound for W1 itself. The converse is immediate, because the translated space includes its original bottom vector. Thus, using the independently derived interval-gap proof, the two universal programmes are equivalent up to constants. This does not need a proved weak-W1 family, and it does not refute full W2. It says that adapting only by multiplying a single W1 groundstate cannot universally repair a failure of W1.


Final additions: weak_w1_taper_proof.md contains the new probabilistic theorem and primary source. exact_groundstate_energy.py verifies the exact A={1,2} counterexample in SymPy. implant_check.py/json independently assembles full W1 and translated compression on the implanted examples.
