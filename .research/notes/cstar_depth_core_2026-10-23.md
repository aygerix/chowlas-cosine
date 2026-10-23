# A sharp deletion threshold for bounded positive-sum depth

2026-10-23. Paper theorem independently checked in
[the advisor audit](advisor_exponential_depth_2026-10-23.md).
This falsifies a proposed arbitrary-support inverse reduction. It is
not a new Chowla lower bound for the difference-set family, a novelty
claim, or a kernel-checked result. The only outside combinatorial
dependency is the standard finite-graph Turan theorem, in its exact
balanced multipartite form.

## Statement with the recomputed connection set

For a nonempty finite positive integer set S, define
h(S)=max{r>=1:S intersects rS}, allowing repeated summands.
Fix integers H>=1 and k>=H+1. Put q=H+1 and write k=q*m+s,
0<=s<q. For a Sidon integer set B of size k, let A=diff_+(B), and
let d_H(A) be the fewest FREQUENCIES removed to leave a nonempty
A' subset A with h(A')<=H. Representations are recomputed using A'.

Then

    d_H(A)>=s*binom(m+1,2)+(q-s)*binom(m,2).        (1)

For every such k,H an explicit Sidon B attains equality. Thus (1)
is the exact minimum over all Sidon B of the recomputed-depth
deletion parameter. Every starting A has n=k(k-1)/2 and the exact
all-circle bound M(A)<=k/2<=sqrt(n) for k>=2.

## Lower bound: remaining pair edges cannot contain a large clique

Sidon uniqueness identifies each frequency in A with one unordered
pair from B. Deleting d frequencies leaves a graph G on B with
binom(k,2)-d edges. If G contained a clique with H+2 vertices
b0<...<b_(H+1), every consecutive difference and the endpoint
difference would be in A'. Their telescoping identity would give
an (H+1)-term positive representation of a frequency in A',
contradicting h(A')<=H.

Hence G is K_(H+2)-free. Turan's theorem bounds its edges by the
balanced q-partite graph, with part sizes m or m+1. Its missing
edges are exactly the right side of (1). In particular, for fixed H,
the lower bound is k²/(2(H+1))+O_H(k)=Theta_H(n).

## Explicit attainment

Partition the labels0,...,k-1 into q consecutive blocks I_j of
balanced sizes m or m+1. Set

    delta=9^(k-1), T=(H+3)*delta,
    B_j={j*T+9^a:a in I_j}, j=0,...,H,
    B=union_j B_j.

B is Sidon. Indeed equality of two positive pair differences forces
their center-index differences to agree: the discrepancy in their
offset differences has absolute value<2delta<T. The offset equality
9^a-9^b=9^c-9^d then identifies the same ordered pair, by taking
the lowest power of9 and then the higher exponent.

Delete precisely the within-block differences. Sidon uniqueness
gives the deletion count in (1), leaving all cross-block differences.
Every retained frequency lies between T-delta and H*T+delta. Since

    (H+1)*(T-delta)>H*T+delta,

no retained frequency is a sum of H+1 or more retained frequencies.
Thus h(A')<=H. Choosing one B vertex in each block gives a
telescoping H-term representation inside A', so h(A')=H exactly.

## Correction of the stronger discarded claim

With the ORIGINAL connection set A frozen, the vertices A partition
into cliques C_j={b_i-b_j:i>j} of sizes1,...,k-1. Deleting vertices
to leave directed graph height<=H therefore costs at least
(k-H-1)*(k-H)/2. This is correct for that frozen graph.

It is incorrect for deleting frequencies and recomputing the
connection set. A deleted edge label can disconnect many retained
vertices. The q=2 construction above leaves a depth-one core of
size about n/2 after deleting about n/2, whereas the frozen-graph
formula would incorrectly demand n-O(k) deletions. The advisor also
gives a two-scale Sidon realization of the same distinction.

The corrected Theta_H(n) lower bound still decisively rules out
the proposed O(M)=O(k) deletion route to bounded depth on all
actual-lowM supports. It does not obstruct deleting a macroscopic
fraction, bound arbitrary signed witnesses, or resolve Chowla.
