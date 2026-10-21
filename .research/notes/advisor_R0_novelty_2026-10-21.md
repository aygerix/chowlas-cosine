# Bounded independent antecedent audit of provisional R0

Date/access date: 2026-10-21. Internal AI advisor review. This is a
bibliographic and statement-comparison task only. The research campaign
remains PAUSED. No proof attack, research computation, experiment, GPU
operation, additional agent or external outreach was undertaken. Only
this assigned note was edited.

## Statement being compared

For every nonempty finite set A of distinct positive integers, put

    n=|A|, F_A(z)=sum_{a in A}z^a, f_A(x)=Re F_A(e^{ix}),
    D_A=2*f_A, M(A)=-min_{x in R} f_A(x), lambda=2*sqrt(n),
    p=(lambda+F_A)^-1, q=Im p.

All integrals below use dx/(2*pi). Provisional **R0** is the claim that
ACTUAL M(A)<=sqrt(n) implies

    integral D_A*q^2 / integral q^2 <= -sqrt(n)/100.       (R0)

There is no span, density, frequency-band or construction assumption.
In particular lambda is fixed by n, not a freely oversized damping
parameter. This is the INFINITE analytic reciprocal, with its constant
automatically disappearing upon taking the imaginary part.

The already audited identities give, for

    S=integral |p|^2, g=lambda^2*S-1>0,
    T0=sum_{a in A}[z^a]p^2, tau=-lambda*T0/(2g),

    integral q^2=g/(2*lambda^2),
    integral D_A*q^2 / integral q^2=2*lambda*(tau-1).

Thus R0 is exactly tau<=399/400. It would imply the universal Chowla
bound M(A)>=sqrt(n)/200, using the trivial complementary branch
M(A)>sqrt(n). This implication is part of the prior audit, not new
proof work in this task. No converse from Chowla to this specified
reciprocal witness has been established.

## Classical analytic antecedents actually inspected

**1. The Cayley/Caratheodory/Schur correspondence is an explicit match
to the architecture, not to R0's Boolean inequality.**

A. Bultheel, A. Cuyt, W. Van Assche, M. Van Barel and B. Verdonk,
*Generalizations of orthogonal polynomials*, Journal of Computational
and Applied Mathematics 179 (2005), 57--95, DOI
[10.1016/j.cam.2004.09.036](https://doi.org/10.1016/j.cam.2004.09.036).
I inspected the title/author page and the discussion on printed p.61
(PDF page 5), specifically the Riesz--Herglotz transform and the
following Cayley-to-Schur formula, in the
[author/institution-hosted full text](https://medialibrary.uantwerpen.be/oldcontent/container2652/files/papers/Bu_Cu_ea_gen_05.pdf).
It explicitly describes analytic functions of positive real part and
their conversion into bounded Schur functions. This 2005 article is
unrelated to the 2026 Bu et al. Chowla paper reviewed by the lead.

The identification with our existing notation is exact:

    C_A=1+2*F_A/lambda,
    zeta=(C_A-1)/(C_A+1)=F_A/(lambda+F_A),
    p=(1-zeta)/lambda, q=-Im(zeta)/lambda.

The low-M hypothesis makes Re C_A>=0. In the usual convention the
associated Schur function in the cited formula includes division by z;
zeta is z times that function. This conventional normalization does not
make the reciprocal ansatz a new analytic construction. The source
does not state the uniform selected Boolean Rayleigh estimate R0.

**2. Herglotz representation and positive Toeplitz forms are old
antecedents of the positivity framework.**

M. Tsuji, *On Positive Definite Sequences and Functions*, Tohoku
Mathematical Journal, Second Series 2 (1950), 142--165. I inspected the
introduction on printed p.142, equations (1)--(3), in the
[journal-hosted full text](https://www.jstage.jst.go.jp/article/tmj1949/2/2/2_2_142/_pdf/-char/en).
It states the Herglotz integral representation and the resulting
nonnegative Hermitian forms. The journal's
[official general index](https://www.math.tohoku.ac.jp/tmj/2ndGeneralIndex.pdf)
confirms the year, volume and pages. These statements supply broad
positive-real/Toeplitz machinery; the inspected passage does not assert
R0 or its fixed-cardinality coefficient restriction.

For historical provenance I also inspected the Saxon Academy's
[catalog entry for Herglotz's 1911 paper](https://archiv.saw-leipzig.de/saw-archive/publikationen-quellen/publikationen/berichte-ueber-die-verhandlungen-der-koeniglich-saechsischen-gesellschaft-der-wissenschaften-zu-leipzig-mathematisch-physische-klasse-bd-1/berichte-ueber-die-verhandlungen-der-koeniglich-saechsischen-gesellschaft-der-wissenschaften-zu-leipzig-mathematisch-physische-klasse-bd-63/ueber-potenzreihen-mit-positivem-reellen-teil-im-einheitskreis),
*Uber Potenzreihen mit positivem, reellen Teil im Einheitskreis*,
vol.63, pp.501--511. This was catalog metadata, NOT a reading of the
original paper. Schur's original 1917 article has publisher DOI
[10.1515/crll.1917.147.205](https://doi.org/10.1515/crll.1917.147.205),
*Uber Potenzreihen, die im Innern des Einheitskreises beschrankt sind*,
147, 205--232. The publisher metadata was indexed, but opening its full
page returned HTTP405; I do not claim to have inspected that original
text. The mathematical attribution here rests on the accessible
full-text antecedents above, not on inaccessible originals.

**3. The norm/coefficient identities use standard Hardy-space
orthogonality and bounded analytic multiplication.**

J. H. Shapiro, *Lectures on Composition Operators and Analytic Function
Theory* (Padua short course, summer 1998),
[author-hosted notes](https://users.math.msu.edu/users/shapiro/pubvit/Downloads/CompIntro/CompIntro.pdf).
I inspected the author/course description and printed p.14,
Propositions 3.9 and 3.11 and Corollary 3.12. These give the circle
integral characterization of the H2 norm, its coefficient-square
interpretation, and the H-infinity multiplier bound. They support
classifying our Parseval/Schur norm manipulations as routine analytic
machinery. They do not give the sign or root-scale size of the Boolean
mixed energy in R0.

**4. Negative-energy certification is a standard Rayleigh principle.**

R. M. Gray, *Toeplitz and Circulant Matrices: A review*,
[author-hosted full text](https://ee.stanford.edu/~gray/toeplitz.pdf).
I inspected Lemma 2.1 on Rayleigh extrema, Section 4.2/Lemma 4.1 and
equation (4.14), printed pp.41--42. These identify Toeplitz quadratic
forms with symbol-weighted integrals and bound their eigenvalues by
the symbol's extreme values. The source supports the classical
variational framework; it does not specify our reciprocal trial
function or prove its R0 estimate. A general minimum-eigenvalue
theorem also does not automatically establish a bound for this ONE
prescribed vector.

## Targeted search and its limits

In addition to locating the sources above, I searched combinations of
the following exact terms and close variants:

- `"Chowla" "reciprocal" cosine`;
- `"Chowla" "Herglotz"`;
- `"Chowla" "imaginary part" reciprocal polynomial`;
- `"Chowla cosine" "Hilbert transform"`;
- `"Chowla cosine" "Schur"`;
- `"Chowla" "reciprocal" "Rayleigh"`;
- `"cosine problem" "Caratheodory"`;
- `"cosine polynomials" "reciprocal" inequality`.

No primary-source statement matching the fixed-lambda, unrestricted
Boolean inequality R0 was located in this bounded search. The returned
material included unrelated Chowla conjectures and uses of
"reciprocal polynomial" to mean a reversed/self-reciprocal algebraic
polynomial; those are not the inverse analytic function used here.
Search snippets and AI-generated research pages were not used as
mathematical evidence.

I did NOT duplicate the lead's full-text reviews of Bedert, Shankar,
JMTZ or Bu et al., nor the lead's additional Ruzsa/Sanders/Yip checks.
This note therefore makes no independent full-text claim about those
papers. No exhaustive journal/MathSciNet/Zentralblatt search, backward
citation audit of every antecedent, or specialist review was performed.
An inaccessible text and an unindexed formulation can both defeat
keyword matching. Search absence cannot establish priority, truth,
or that no known theorem could settle the statement.

## Candid classification and exact resumption point

**Classical method; unproved internal uniform proposal; publication
priority undetermined.** Taking a reciprocal of a positive-real
analytic function, applying Cayley/Schur transformations, using Hardy
orthogonality and evaluating a Rayleigh quotient are established
methods. The displayed identities are routine applications of those
methods and should not be advertised as a new analytic technique.

The potentially substantive claim is the UNIFORM BOOLEAN estimate R0
at lambda=2*sqrt(n). None of the precise named results inspected here
settles or refutes it. That is a bounded comparison verdict, not a
claim that R0 has never appeared. Its truth is not established by the
three certified finite successes, and novelty must not be inferred
from their existence or from this search.

On an explicitly authorized resumption, first read this audit together
with the lead's four-paper/additional-source review and the existing
zero-carrier proof note. The next mathematical task is exactly:
**derive or falsify tau<=399/400 for arbitrary Boolean A under ACTUAL
M<=sqrt(n), focusing on the unresolved norm-gap range.** Documentation
precision added by the lead after this audit: g>9/16 gives the sign,
whereas the specific R0 margin follows from the existing sufficient
bound at g>=10000/17689. Thus the precise remaining range is
0<g<10000/17689, including the interval just above9/16. The large-gap
bound and the failed oversized-lambda/padding argument are already
recorded. A counterexample to R0 would refute this prescribed-witness
principle, not Chowla. Do not rerun successful controls or authorize a
GPU simply to document the next step. This note does not resume that
research task.
