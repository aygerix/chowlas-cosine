# Independent proof check: an explicit Boolean family with weak W1 certificates

2026-10-20. This checks the balanced-sign construction proposed in the current direct-proof pass. It proves a weak-W1 family, not a weak-W2 family and not a Chowla counterexample.

## 1. Support, cardinality and adjacency

For integers k>=1 and r>=3k, let S_(r,k) consist of vectors in {-1,0,1}^r having exactly k entries +1 and k entries -1. It is symmetric and excludes zero. Write

N=|S|=binom(r,k) binom(r-k,k),
I={0} union S,
A_(s,t)=1_S(s-t), s,t in S.

For s,t in S define l(s,t) to be their number of same-sign nonzero coordinate overlaps, and o(s,t) their number of opposite-sign nonzero coordinate overlaps. Then

A_(s,t)=1 iff l(s,t)=k and o(s,t)=0.

Indeed opposite overlap creates a coordinate +/-2 in s-t, which is forbidden. Without opposite overlap, s-t has 4k-2l nonzero entries. It always has coordinate sum zero, so having 2k nonzero entries is equivalent to belonging to S.

The graph is regular by permutation transitivity. Its exact degree is

D=binom(r-2k,k) F_k,
F_k=sum_(a=0)^k binom(k,a)^3.

To see this, select a shared positive coordinates and k-a shared negative coordinates in s, in binom(k,a)^2 ways. All k remaining nonzero coordinates of t must lie outside supp(s). Assign k-a of them positive signs and a negative signs, in binom(r-2k,k) binom(k,a) ways.

## 2. The signed-subset Gram matrix and its error

Let Z have columns indexed by S and rows indexed by signed k-element coordinate subsets. Put Z_(U,s)=1 when U is a signed subset of s. Then G=Z^T Z is positive semidefinite and

G_(s,t)=binom(l(s,t),k),

with the convention that the binomial is zero when l<k. Entrywise A<=G. If G_(s,t)-A_(s,t) is nonzero, then the total support overlap j=l+o is at least k+1. This includes diagonal entries: l=2k there.

Proof of the support claim: a nonzero G entry has l>=k. If l=k and o=0, the pair is adjacent and G=A=1. All remaining possibilities have l+o>=k+1.

For fixed s, the number of t in S with j>=k+1 is at most

binom(2k,k) sum_(j=k+1)^(2k) binom(2k,j) binom(r-2k,2k-j).

The first factor is a bound on the number of balanced sign assignments on a chosen support of size 2k. Every entry of E=G-A is at most binom(2k,k). Consequently

||E||_op <= max_row sum |E_st| <= C_k r^(k-1),
C_k=4^k binom(2k,k)^2.

This crude constant is sufficient and uniform for fixed k. The first operator inequality follows from symmetry and the maximum absolute row-sum bound. Since G is PSD,

lambda_min(A) >= -C_k r^(k-1).                       (1)

An optional exact check on the row sums is

sum_t G_(s,t)
= sum_(a=0)^k binom(k,a)^2 binom(r-k,k-a) binom(r-2k+a,a).

Subtracting D gives the exact nonnegative row sum of E. Its leading degree-k term cancels, consistent with (1).

## 3. Full W1 spectrum

The central W1 adjacency is

B_I = [[0, 1^T],[1,A]].

On the span of the central coordinate and the normalized constant vector on S, it is

[[0,sqrt(N)],[sqrt(N),D]].

The negative eigenvalue of this 2x2 block is -h(D/sqrt(N))sqrt(N), where

h(d)=(sqrt(d^2+4)-d)/2.

The other eigenvalues are those of A on the subspace orthogonal to constants. Thus

K_1=-lambda_min(B_I)
<= max{h(D/sqrt(N))sqrt(N), C_k r^(k-1)},

and K_1 is always at least the first quantity. For fixed k, as r tends to infinity,

sqrt(N) ~ r^k/k!,
D/sqrt(N) -> F_k,
C_k r^(k-1)/sqrt(N) -> 0.

Therefore the central eigenvalue is eventually the bottom eigenvalue, and

K_1/sqrt(N) -> h(F_k).

Since F_k>=sum_a binom(k,a)=2^k, h(F_k) tends to zero with k.

## 4. An explicit diagonal sequence, avoiding an unspecified limiting choice

Set

r_k = max{6k^2, 2^k k! C_k F_k}.

These are integers. When r>=6k^2,

D/sqrt(N)
>= F_k ((r-3k+1)/r)^k
>= F_k(1-3k^2/r)
>= F_k/2.

Also sqrt(N)>=(r/2)^k/k!, since r>=4k. Hence at r=r_k,

C_k r^(k-1)/sqrt(N) <= C_k 2^k k!/r <= 1/F_k.

As h(d)<=1/d for d>0,

K_1/sqrt(N) <= 2/F_k <= 2^(1-k) -> 0.             (2)

This is a completely explicit finite Boolean-support sequence, with no random choice and no conditional assumption.

## 5. Encoding in integers without changing the W2 adjacency

Map v to L(v)=sum_(j=0)^(r-1) v_j 7^j. A nonzero integer vector whose coordinates have magnitude at most 5 cannot map to zero: its largest nonzero digit has magnitude at least 7^j, while all smaller digits together have magnitude at most 5(7^j-1)/6 <7^j.

Vectors in W2=I+I have coordinates of magnitude at most 2. Thus equality of two W2 vectors is tested by a relation with coordinate magnitudes at most 4, and a W2 adjacency relation u-v=s is tested by magnitudes at most 5. Both are faithfully preserved by L.

The integer support L(S) is symmetric, nonzero, and has the same cardinality and exactly the same W1 and W2 matrices. Taking its positive half gives a finite subset of the positive integers, as required in the cosine-sum setting.

## 6. Scope and executable checks

Equation (2) rigorously supplies the weak-W1 base family needed by constructions that previously assumed K_1=o(sqrt(N)). It says nothing by itself about the full W2 minimum or the global negative minimum.

The accompanying script balanced_sign_weak_w1_check.py enumerates small instances and verifies the adjacency condition, exact degree, exact Gram row sum, and support of G-A using integer arithmetic. It checks (r,k)=(4,1),(6,2),(7,2),(9,3); the corresponding (N,D) are (12,4),(90,10),(210,30),(1680,56). Small-matrix eigenvalue displays are numerical checks only and are not used in the proof above.

## 7. Subsequently checked sharper exact error and smaller diagonal

The exact Gram row sum simplifies as follows:

sum_t G_(s,t)=F_k binom(r-k,k).

This follows either directly by completing a signed k-subset, or by the identity

binom(r-k,k-a) binom(r-2k+a,a)
=binom(r-k,k) binom(k,a).

Hence the entrywise nonnegative symmetric error G-A has exact constant row sum

e=F_k[binom(r-k,k)-binom(r-2k,k)],

and its operator norm equals e. The finite enclosure improves to

kcentral <= K_1 <= max(kcentral,e).

The explicit choice r_k=ceil(4F_k^2 k^2) also works and is much smaller than the crude choice in Section 4. Indeed,

e/sqrt(N) <= F_k k^2/(r-2k+1),

because sqrt(binom(r-k,k)/binom(r,k))<=1 and

1-binom(r-2k,k)/binom(r-k,k)
<=sum_(j=0)^(k-1) k/(r-k-j)
<=k^2/(r-2k+1).

Similarly sqrt(N)<=binom(r,k), so

d/sqrt(N)>=F_k binom(r-2k,k)/binom(r,k)
>=F_k[1-2k^2/(r-k+1)].

At the stated r_k, these imply e/sqrt(N)<=1/F_k and d/sqrt(N)>=F_k/2, and therefore K_1/sqrt(N)<=2/F_k. This sharper diagonal has been independently checked; it supersedes the crude size choice, not the construction or the limiting claim.
