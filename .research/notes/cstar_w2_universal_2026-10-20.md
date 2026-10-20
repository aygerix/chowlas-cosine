# Full W2 universal candidate: adversarial integer-set tests

Checkpoint: 2026-10-20T05:46:32.196395+00:00. Ongoing research; no universal Chowla/C* or W2 constant is established. [Reproduction index](../experiments/cstar_structural_2026-10-20/README.md).

Target: for every finite symmetric S subset Z excluding0, let W2={0} union S union(S+S) and H_xy=1_S(x-y) on ALL W2. Is K_W2=-lambda_min(H)>=c sqrt(|S|) for some absolute c>0? This is stronger than universal Chowla and is NOT asserted here. Objective rho=|S|/K_W2². A genuine countermodel requires rho unbounded, not merely rho>2.

## Exact result: the SHARP constant fails

Take A (50 elements)

1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,40,41,42,47,48,50,52,57,61,62,64,65,68.

This is the existing repository N50_x71-labelled support (the actual maximum is68), not a newly optimized Chowla example. Set S=±A. Its W2 has267 elements, exactly [-136,136] excluding ±131,±134,±135.

EXACT certificate: every leading principal minor of the267×267 integer matrix

50 H + 353 I

is positive. Verified by fraction-free Bareiss symmetric elimination, exact integer division checked at every update. Sylvester therefore gives H+(353/50)I positive definite. Hence

K_W2 < 353/50 = 7.06 < sqrt(50),
rho > 250000/124609 = 2.00627563017... .

This rigorously disproves K_W2>=sqrt(|S|/2), the sharp C-half scale, but DOES NOT disprove any unspecified absolute-c bound. The floating least eigenvalue gives K_W2≈7.056993539807 and rho≈2.007985444027.

Boundary diagnostic: filling the six missing integer indices gives the full interval [-136,136] with numerical K≈7.07449765645, just ABOVE sqrt(50). Thus the sharp failure is already sensitive to six outer boundary sites. Existing repository certification has true global K≈8.0966213. This is not a high global Chowla-ratio example.

Certificate and full reproducible procedure:
- w2_exact_certificate.py
- w2_exact_certificate.json (support, rational bound, final integer determinant, exact-completion flag)
- w2_exact_certificate.log (pivot progress and result)

Reproduction files are in [the experiment directory](../experiments/cstar_structural_2026-10-20/README.md).

## Exhaustive and annealing tests

All adjacency entries use exact integer support membership. Eigenvalues used for exploration are floating SciPy symmetric eigensolver values, not interval-certified. Only the preceding rational witness is certified.

1. Exhaustive all65,535 nonempty subsets A of[1,16]: maximum observed rho=1.648106395348 at A={1,2,3,4,5,6,7,9,10,11,12,13,16}, K≈3.971861093582, |W2|61. This includes an earlier all16,383-subsets scan of[1,14], whose maximumrho was1.54792020435. No all-angle minimum is used or needed.

2. General sparse starts, seed6526, 4,400 proposed single-swap moves: (X,n)=(24,8),(48,12),(80,16),(160,12),(1000,10). Best rho1.186033242624 at A={3,4,6,7,10,13,16,20}. Sparse huge-diameter starts did not produce increasingrho.

3. Requested ranges, seed6527, 34,000 proposed moves across (X,n)=(16,4),(16,8),(16,12),(32,8),(32,16),(32,24),(64,12),(64,24),(64,40). Best rho1.575587935039 at n24,X32. Objective computed from ALL W2, not scalar moments, a fixed Ritz vector, or a chosen subset of rows.

4. Warm starts, seed6528, 15,000 proposed moves from existing dense n20 and two n50 supports. The existing n50 support above gave the largest value2.007985444027; no improving swap was found in those runs. This illustrates why sparse random-start annealing alone would have missed the sharp-constant failure.

5. Variable-cardinality seed6530 run completed 10,000 proposed toggles/swaps, initialized at the certified support. No improvement over rho2.007985444027 was found. The complete log is w2_variable.log.

Reproduction scripts/logs: w2_anneal.py, w2_targeted.py, w2_exhaustive16.py, w2_warm.py, w2_variable.py and matching .log files. Proposed counts include skipped swaps when the new element already belongs to A.

## Scope

These finite searches supply no universal constant, no asymptotic countermodel, and no evidence strong enough to assert the candidate. The exact sharp failure limits the constant one could hope for. The companion collective-boundary and second-neighborhood notes examine high-rank structured families and how two-step rows overcome known one-step tapered countercontrols.

## Analytical follow-on: induced stars, bicliques, and bounded coloring

### A. Exact obstruction to a universal induced-bipartite certificate

Take S={±1,...,±m}, so W2=[-2m,2m]. An independent set in H[W2] has consecutive elements separated by at least m+1. Therefore

alpha(H[W2]) <= floor(4m/(m+1))+1 <=4.

Every induced bipartite subgraph has at most8 vertices, and its negative eigenvalue magnitude is at most sqrt(pq)<=4 (the two color classes have p,q<=4). Yet sqrt(|S|)=sqrt(2m) tends to infinity. Thus the assertion

"W2 always contains an induced star or biclique, or an arbitrary induced bipartite subgraph, with negative eigenvalue at least c sqrt(|S|)"

is FALSE for every c>0. This covers arbitrary locations of the selected vertices inside W2, not just the first neighborhood. More generally every induced r-colorable subgraph has at most4r vertices, hence cannot give a growing bound for fixed r. A positive combination of Rayleigh certificates each supported on such bounded pieces also cannot improve their worst lower spectral value. Correlating many stars can evade this only by introducing cross terms whose total support has growing chromatic complexity; it is not a bipartite reduction anymore.

This is a concrete obstruction to the proposed restricted proof architecture, not a counterexample to W2 or Chowla: the full interval matrix does have a negative eigenvalue of linear order m.

### B. Independent-set versus long-progression dichotomy is also false

Let r_i=b^i, 0<=i<m, with b>=9, and S={r_j-r_i:i!=j}. Encode root e_j-e_i by r_j-r_i. Bounded-digit uniqueness preserves all equations needed below.

There is NO nontrivial three-term arithmetic progression in S. Every unencoded root has Euclidean norm sqrt(2), while the midpoint of two distinct roots has strictly smaller norm, so alpha+gamma=2beta is impossible for distinct roots. The large-base encoding introduces no new relation of this form.

The graph induced on S has independence number exactly m. Adjacent roots have inner product1, equivalently their directed edges share a head or share a tail. An independent collection therefore has indegree<=1 and outdegree<=1 at each of the m root coordinates, so it has at most m roots. A directed m-cycle achieves m (a2-cycle works at m=2).

Here |S|=m(m-1), so alpha/|S| tends to0 while every arithmetic progression has length at most2. Consequently no dichotomy of the form "a fixed positive fraction of S is independent, OR S contains an arithmetic progression of length c sqrt(|S|)" is valid. This precisely quantifies the root-difference obstruction rather than assuming dense support is the only obstacle to induced stars.

### C. What genuine overlap of several independent stars would certify

Let T,U be disjoint independent subsets of W2. Put

r_T(u)=|{t in T:u-t in S}|, u in U.

The rectangular incidence matrix M_{tu}=1_S(t-u) has

||M||op² >= (1/|T|) sum_[u in U] r_T(u)²,

by applying M^T to the normalized all-ones vector on T. Because BOTH diagonal blocks vanish, the induced bipartite adjacency has least eigenvalue -||M||op. Hence the exact conditional certificate is

K_W2² >= (1/|T|) sum_[u in U] r_T(u)².

This records the relevant distinction: counting many stars gives first moments of r_T, whereas a gain from correlated stars requires actual shared-leaf overlap, the second moment. No scalar moment of D or the first-neighborhood root compression is being substituted here. It is nevertheless a standard graph certificate, not an established new universal Boolean ingredient. Sections A and B show why neither independent-set selection alone nor a simple independent/progression dichotomy guarantees the required T,U.

An explicit ordered case where overlap improves the certificate: S=±([L,L+m] intersect Z), L>2m. Set a=floor(m/2), T={0,...,a}, U={L+a,...,L+m}. Both lie in W2, both are independent, and every cross difference lies in S. Therefore K_W2>=sqrt((a+1)(m-a+1))>=m/2. A single root star only gives order sqrt(m). This proves the mechanism works on sharply separated frequency blocks, while the dense interval counterexample proves it cannot be the whole universal argument.

Current outcome: a universal bounded-color/star/biclique route is rigorously excluded, and an overlap-sensitive conditional certificate is explicit. No argument here produces the growing-chromatic signed cancellations needed for arbitrary S. That missing requirement is not claimed to be exhausted or impossible.
