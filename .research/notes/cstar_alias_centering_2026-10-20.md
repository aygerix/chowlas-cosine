# Residue-fiber centering: an exact variance identity

Checkpoint: 2026-10-20T05:56:36.620284+00:00. Ongoing research; no universal Chowla/C* or W2 constant is established. [Reproduction index](../experiments/cstar_structural_2026-10-20/README.md).

2026-10-20. Auxiliary calculation for one-representative finite-group lifts; not a universal Chowla estimate.

Suppose a symmetric integer support S maps injectively to a symmetric subset D of a finite quotient G, with 0 not in D. Let W be any finite set of integer rows, partitioned into fibers W_g by their quotient class. Let B be actual integer Cayley adjacency and L_uv=1_D(pi(u)-pi(v)) the quotient kernel pulled back to W. For nonempty fibers of size m_g, set Q_g=I-J/m_g and Q=directsum Q_g.

Then QLQ=0. Moreover tr(QBQ)=0: cyclicity reduces the trace to tr(BQ), and actual B has no entries within a residue fiber because 0 is not in D.

For two fibers i,j, the actual adjacency block M is a partial matching. Injectivity of S under the quotient means that one fixed integer lag is allowed for that ordered pair of residue classes; each row and each column therefore has at most one edge. If M contains k ones, direct expansion gives

    ||Q_i M Q_j||_F^2
      = k - k/m_i - k/m_j + k^2/(m_i m_j).

In particular, if m_i,m_j>=4, this is at least k/2. Summing over ordered fiber pairs gives an exact lower bound for ||QBQ||_F^2 in terms of actual edges between high-multiplicity fibers. It is a genuinely exact 0/1 partial-matching calculation, not a fractional covariance approximation.

## Why this is not a spectral square-root bound

Put C=QBQ on ran Q, r=rank Q, and a=-lambda_min(C). Since tr C=0, positivity of (lambda+a)(N-lambda) for every eigenvalue lambda in [-a,N], N=|S|, implies

    ||C||_F^2 <= a N r,
    a >= ||C||_F^2/(N r).

Thus even a Frobenius norm squared comparable to Nr gives only a constant lower bound, not sqrt(N). A square-root conclusion would follow from the *additional* positive-spectrum cap lambda_max(C)<=C0 sqrt(N), together with retained edge energy ||C||_F^2>=c Nr; then a>=c sqrt(N)/C0. Neither condition is shown to hold universally. In particular one must not infer the cap merely because the exact quotient kernel is annihilated: positive modes caused by the choice of integer lift can remain in the centered fibers.

This calculation isolates two testable requirements: enough actual edge energy between repeated fibers, and control of the positive spectrum after fiber centering. It does not assert that every hypothetical counterexample has a useful finite quotient with these properties.

## Explicit failure of the hoped-for positive-spectrum cap

Take S={±1,...,±m}, quotient q=2m+1, and W=W2=[−2m,2m]. Every nonzero residue has exactly two representatives; zero has one. An orthonormal basis for ran Q is

    v_i=(e_{−2m+i}−e_{1+i})/sqrt(2),  i=0,...,2m−1.

The centered adjacency in this basis is exactly

    C_ii=0;
    C_ij=1 if 1<=|i−j|<=m;
    C_ij=−1/2 if m+1<=|i−j|<=2m−1.

The constant vector gives the exact Rayleigh quotient

    lambda_max(C) >= (5m−1)/4.

Indeed the directed short-pair count is 3m²−m and the directed long-pair count is m²−m. Thus centering the quotient's positive spike does NOT leave only O(sqrt(N)) positive spectrum, even for this simplest exact Boolean lift, with N=2m. The proposed positive-spectrum cap is refuted, not left as an untested universal premise. It remains a valid sufficient condition on subclasses satisfying it.

Diagnostic eigenvalues (ordinary floating point) at m=4,8,16,32 have minima −2.37591,−3.48273,−5.95286,−11.03612 and maxima 5.16188,10.71372,21.81666,44.02191. These values are not needed for the exact refutation. Both signs can grow linearly; the positive cap was simply too restrictive.
