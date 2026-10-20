# Exact center-response amplification and exploratory balanced-layer check

20 October 2026. The identity below is proved; the Laguerre calculations are floating diagnostics only.

## Exact amplification tool

For a finite symmetric base T, write W=({0} union T)+({0} union T), J=W\{0}, A=B_J, b=1_T. Take m independent coordinate copies of T and their axis union S. The principal submatrix on the center and the m singly occupied copies of J is the bouquet

    [0, b*, b*, ..., b*;
     b, A, 0, ..., 0;
     b, 0, A, ..., 0;
     ...].

Different singly occupied axes have no edges. For any unit g in l2(J), let a=<b,g>, h=<g,Ag>. The compression to the center and m^(-1/2) times the sum of the copies of g is exactly

    [[0, sqrt(m)a], [sqrt(m)conjugate(a),h]].

Therefore

    K_W2(S) >= (sqrt(h^2+4m|a|^2)-h)/2.                 (1)

At K> -lambda_min(A), positivity of K times identity plus this entire bouquet is equivalent to

    K >= m <b,(A+K)^(-1)b>.                            (2)

At a pole one must use the PSD/range/pseudoinverse form, not an undefined inverse. These are generic exact block identities, not a new universal Boolean bound.

They identify the error in bounding an axis union by independent base minima plus a weak pair-axis correction: copies of the base share one center. The response in (2) can be much larger than n divided by the uniform W1 cost after the single-axis exterior coordinates have been eliminated.

## Fixed-interior extension as a sufficient criterion

If one can find r supported in W\({0} union T) with q=D_T+r satisfying

    ||q||^2 <= C n,
    <q,D_T q> <= C n^(3/2),

then <D_T,q>=n exactly, by disjoint Fourier supports. Normalizing q supplies |a|>=sqrt(n/C), h<=C sqrt(n) if a matching lower bound ||q||^2>=n is used. Formula (1) then gives square-root negativity for sufficiently many independent copies, and with m=1 gives a constant depending only on C. This is a sufficient universal target, not a proof that the extension always exists.

## Balanced-layer radial diagnostics

axis_laguerre_diagnostic.py uses the exact integer limiting matrix from the previous pass, whose entries are triple products of signed Laguerre polynomials. It adds the symmetric m-axis center/pair sector. The matrix has the old one-axis radial block except that its center-to-k entry is sqrt(m); one new pair state has diagonal 2F_k and coupling sqrt(2(m-1)) to radial level k.

For k=1,...,10 and m approximately F_k times the one-base negative magnitude, the observed normalized negative ratios K/sqrt(m) lie between about 0.73 and 0.83 for k>=2. Thus the attempted many-axis suppression does not occur in this tested radial subspace. This is a lower-bound diagnostic, not an upper bound on full W2, not a rigorous finite-r theorem, and not evidence that an unspecified universal constant has been proved. The input Laguerre JSON is a separately labeled dependency from the earlier pass.

A further exploratory check on the punctured radial matrix found that its level-k vector has squared mass roughly 0.33--0.48 below normalized spectral threshold 1 for k=2,...,10. That is consistent with bounded-norm central-response corrections, but is not a proof or asymptotic assertion.

Finally, Euclidean closeness of an actual eigenvector's coefficients on T to the uniform vector does not prove the fixed-interior extension statement. Replacing an o(sqrt(n)) coefficient error by zero can change energy substantially when the adjacency operator norm is of order n. A successful universal extension argument must control that energy effect, not merely coefficient norm.
