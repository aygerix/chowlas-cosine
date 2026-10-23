# A signed centroid constraint for arbitrary Boolean autocorrelations

2026-10-23. Paper theorem independently checked in
[the signed audit](advisor_signed_centroid_2026-10-23.md).
The previous goal turn is progress: checkpoint1735ac3 proved the
positive-factor and multiplicity centroid results. This continuation
removes the nonnegative-coefficient assumption from an inverse
inequality. No universal Chowla bound, kernel check or external
novelty claim follows without the additional factor estimates below.

## Quantified statement

Let A be any finite nonempty set of distinct positive integers,
n=|A|, f=sum_A cos(ax). Suppose, on the entire circle,

    lambda+f=|Q|², Q=sum_(b in B)q_b*z^b,

where Q is a finite real-coefficient Laurent polynomial; signs are
arbitrary and zero coefficients are omitted. Orient its overall
sign so S=sum q_b=sqrt(lambda+n)>0. Define

    Nminus=sum max(-q_b,0), P=sum max(q_b,0)=S+Nminus,
    mu=(sum b*q_b)/S, y_b=b-mu,
    Vplus=sum_(q_b>0)q_b*y_b²,
    Vminus=sum_(q_b<0)|q_b|*y_b²,
    Vabs=Vplus+Vminus, alpha=Vminus/Vabs,
    qmax=max |q_b|.

Then lambda>1/2, Vabs>0, 0<=alpha<1/2, and

    S*(1-4alpha)<=4*(lambda-1/2)*qmax+2*Nminus.     (1)

The signed centroid can be outside the convex hull of B. No step
assumes otherwise. All ratios in (1) are invariant under translation
or nonzero integer dilation of the factor support. Root reflections
may change them; (1) holds for every real branch.

For every Boolean A, the usual real Fejer--Riesz construction supplies
such a Q at lambda=M(A): multiply the nonnegative even trigonometric
polynomial by z^maxA, pair reciprocal/conjugate zeros, and choose
half of each even-multiplicity unit-circle zero. Choosing conjugate
pairs together gives real coefficients. Thus (1) is an actual
constraint for arbitrary A at its optimal floor, not an assertion
that all supports have a nonnegative factor.

## 1. Exact Boolean Gram identity

Let R(d)=sum_b q_b*q_(b+d). Coefficient matching says
R(d)=1/2 on plus/minus A and zero on all other nonzero lags;
R(0)=lambda. Put x_b=y_b*q_b, so sum x_b=0, and
U_d=sum_b x_b*q_(b+d). Define the ORDERED missing-lag term

    Tmissing=sum_(b!=c,|b-c| notin A)x_b*x_c.

The row Gram has diagonal lambda, off-diagonal1/2 on present lags,
and zero on missing lags. Hence

    sum_d U_d²=(lambda-1/2)*sum q_b²*y_b²-Tmissing/2. (2)

For d>0, U_(-d)=U_d+d*R(d). Pair squares and discard U_0²>=0:

    sum_d U_d² >=(1/2)*sum_(d>0)R(d)²*d²
               =(1/4)*sum_(d>0)R(d)*d²
               =S*(Vplus-Vminus)/4.               (3)

The middle equality uses EXACT zero-or-one-half correlations and
cannot be imported from a weighted positive spectrum. The pair
variance identity also proves

    Vintrinsic=Vplus-Vminus=sum_(a in A)a²/(2S)>0.  (4)

It follows that alpha<1/2 automatically, but no uniform smaller
margin is proved. U_0 generally does not vanish.

## 2. Control the missing-lag phase cancellation

For a missing positive lag d, sum_b q_b*q_(b+d)=0. Consequently

    sum_b q_b*q_(b+d)*y_b*y_(b+d)
      =sum_b q_b*q_(b+d)*(b+d/2-mu)².

The constant -d²/4 cancels. Negative terms on the right require
opposite coefficient signs. Both lag orientations occur in
Tmissing; use2*((y_b+y_c)/2)²<=y_b²+y_c² on each opposite-sign
unordered pair. Extending the sum to all opposite-sign pairs yields

    Tmissing>=-(Nminus*Vplus+P*Vminus).             (5)

The factor2 is already consumed by the midpoint inequality; it
must not be inserted a second time. Also |R(a)|<lambda for any
a in A by strict finite-support Cauchy, so lambda>1/2. Apply
sum q_b²*y_b²<=qmax*Vabs in (2), combine (3),(5), and divide by
Vabs>0. This gives

    S*(1-2alpha)/4
      <=(lambda-1/2)*qmax+(Nminus+S*alpha)/2,

which rearranges to (1).

## 3. A sufficient stable branch and the remaining universal task

If a factor satisfies

    qmax<=C, Nminus<=S/8, alpha<=1/8,

then (1) proves S<=16C*(lambda-1/2), hence
lambda>=sqrt(n)/(16C). At lambda=M this is a square-root theorem
under the three stated factor conditions. No proof that an arbitrary
optimal factor can be selected to satisfy them has been obtained.
It is a sufficient mechanism, not a complete characterization.

In a hypothetical small-ratio family with bounded qmax, (1) forces

    4alpha+2*Nminus/S >=1-o(1).

This gives a quantitative cancellation alternative, not a
contradiction. Without a qmax bound, its growth is a third allowed
branch. Do not assume any of these alternatives away.

The base constant4 is already sharp at
Q=(1+z/2+z²)/sqrt2, A={1,2}, lambda=9/8. The middle coefficient
lies at mu=1 and contributes no variance; equality holds in the
nonnegative version of (1).

## 4. Exact finite signed recovery; no new minimum record

For A={1,...,5}, the [finite certificate](optimal_endpoint_n5_2026-10-23.md)
shows every optimal nonnegative real factor has qmax about1.043797,
so the proposed constant1 is false even with branch choice. Reflecting
one negative real root gives a signed optimal factor with the SAME
A and M. Exact rational intervals certify

    qmax<0.786161, Nminus/S<0.068887, alpha<0.002623.

All three C=1 stable conditions hold. The sole negative coefficient
is close to the NEW signed centroid, making its variance cost small.
This is one finite recovery, not evidence of a universal selection
theorem or an improved finite cosine minimum.

## 5. One-step budget and the false greedy shortcut

For Q=(z+t)C, t>1, reflect to Qr=(1+t*z)C. Then
q_j=t*c_j+c_(j-1), q'_j=c_j+t*c_(j-1),
mu'=mu+(t-1)/(t+1). S,lambda and (4) are unchanged. In particular
alpha<=1/8 is exactly Vminus<=Vintrinsic/6 on every branch.
The audit gives the full signed mass/variance update, including
the moving centroid term.

Balancing endpoints alone is insufficient. The allpass quotient
(1+tz)/(t+z) has coefficients l0=1/t and
l_j=(1-t^-2)*(-1/t)^(j-1), j>=1. For initially positive Q it gives
Nminus_new<=S/t, but also

    q'_1=q_1/t+(1-t^-2)*q_0.

A large endpoint can move almost unchanged into the interior.
No monotone maximum-reduction or universal bounded-budget sequence
has been proved. The next genuine step is a coupled branch-selection
estimate or an exact counterfamily, not another arbitrary constant
replacement or successful-control sweep.
