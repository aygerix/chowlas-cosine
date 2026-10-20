# Hereditary ratio-minimal selection: exact Boolean conditions and a failed KKT shortcut

Checkpoint: 2026-10-20T05:32:53.486301+00:00. Research remains ongoing; no universal Chowla/C* theorem is claimed. Reproduction: [experiment index](../experiments/cstar_structural_2026-10-20/README.md).

2026-10-20. All claims below are elementary paper derivations, not a proof of C*.

Let f_A(x)=sum_{a in A} cos(2πax), n=|A|, M=-min f_A, and H=f_A+M≥0. Assume every nonempty B⊂A has M(B)/sqrt(|B|)≥M/sqrt(n). Selecting a ratio minimizer inside each hypothetical counterexample makes this assumption without losing the counterexample: the selected cardinalities diverge because M(B)≥1/2.

## 1. Exact coordinated deletion and a tail-sensitive signing target

For D⊂A, d=|D|<n, delta_d=M(1−sqrt(1−d/n)), hereditary minimality is exactly

  sup_x [f_D(x)−H(x)] ≥ −delta_d.

For even n and d=n/2, put g_D=2f_D−f_A. Apply the inequality to D and its complement. Both

  sup_x [g_D(x)−H(x)] ≥ (sqrt(2)−1)M,
  sup_x [−g_D(x)−H(x)] ≥ (sqrt(2)−1)M.

Thus every balanced Boolean signing must have BOTH positive and negative excursions above the original nonnegative barrier H. The positive spikes of f_A do not automatically furnish witnesses, unlike an unpenalized supremum: they incur the cost H.

A sufficient contradiction would be a balanced partition with

  |g_D(x)| ≤ H(x)+beta M for all x, beta<sqrt(2)−1.

More generally |g_D|≤alpha H+beta M suffices for alpha≤1. This is a precise barrier-discrepancy target, not a consequence of ordinary supnorm discrepancy or of Parseval. Fractional signing g=0 satisfies it trivially, so the entire difficulty is Boolean rounding under this nonconstant barrier. The condition also holds for selected finite-group quadric counterexamples, and therefore does not itself use torsion-freeness or exclude those models.

## 2. Exact counterexample to equal active coefficient moments

Take A={1,2}, using t=cos(2πx). Then

  f_A=2t²+t−1=2(t+1/4)²−9/8.

M=9/8 and R=9/(8sqrt(2))<1. Both proper nonempty subsets have ratio 1, so A is hereditary ratio-minimal. Every global minimum has cosine vector

  (cos(2πx), cos(4πx))=(−1/4,−7/8).

Consequently no probability measure supported on the minimum set can have equal coefficient moments. In particular Boolean subset minimality does not give the KKT conditions of the unrestricted fixed-mass coefficient problem.

For comparison, among nonnegative weights w1+w2=2, the minimum possible M is 1, attained by (w1,w2)=(4/3,2/3). Indeed evaluation at t=−1/2 gives M≥(w1+w2)/2=1, and these weights attain this bound. This fractional optimizer has the equal cosine moments (−1/2,−1/2). For the capped fixed-mass problem w1+w2=1, 0≤wi≤1, the optimum is (2/3,1/3), M=1/2, while every Boolean choice of cardinality one has M=1. This is an exact factor-two integrality gap even though the original two-element set is ratio-minimal.

## 3. Near-minimum measures do not repair the shortcut for free

Here H=2(t+1/4)². Whenever H<1/8, necessarily −1/2<t<0, and

  cos(2πx)−cos(4πx)=(1−t)(2t+1)>0.

Hence no probability measure supported in {H≤eta}, eta<1/8, has equal coefficient moments either. At eta=1/8, the point t=−1/2 supplies equal moments. The required slack is exactly 1/8=(1/9)M. Thus an argument invoking approximate active-set stationarity must quantitatively pay a nonzero barrier-height error; compactness or a change of active measure alone is insufficient.

## 4. The failure need not involve nondifferentiability

Continuously delete coefficient 2: f_s=t+(1−s)(2t²−1). For 0≤s≤3/4, the minimizing cosine coordinate is uniquely

  t_s=−1/[4(1−s)],
  M_s=(1−s)+1/[8(1−s)].

For 3/4≤s≤1, the minimum is at t=−1 and M_s=s. The first branch is smooth, and even the join is C1. Thus improvement under infinitesimal coefficient deletion can disappear by the Boolean endpoint through ordinary curvature, without switching between distinct active branches. The minimizer measures shortcut is not blocked only by nondifferentiability.

## 5. General curvature accounting for a coordinated deletion

Suppose along f_s=f_A−s f_D, a minimizing point x_s is smooth and nondegenerate. Let F(s)=M(f_s). The envelope identities are

  F'(s)=f_D(x_s),
  F''(s)=[f_D'(x_s)]² / f_s''(x_s) ≥0.

If the branch remains global through [0,1], hereditary minimality forces

  integral_0^1 (1−s) [f_D'(x_s)]²/f_s''(x_s) ds
  ≥ −delta_d−f_D(x_0).

With switches, replace the left side by the convex distributional second derivative integral; its nonnegative atoms account for derivative jumps. This is a valid quantitative susceptibility requirement, not a contradiction: unrestricted frequencies and small curvature can meet it. In the two-frequency example the entire compensation is smooth. Any route using active minima must control this relaxation energy, not merely their initial Fourier moments.

## Status

Actual output: exact coordinated barrier-discrepancy condition; explicit hereditary-minimal counterexample to active/near-active equal-moment claims; exact capped rounding gap; curvature identity explaining why infinitesimal deletion is insufficient. No universal Boolean rounding estimate, no C* lower bound, and no model exclusion beyond disproving the proposed variational shortcuts have been established.

## 6. Certified larger example: ratio-minimal selection does NOT remove the Fejér relaxation obstruction

A bounded search over all 4095 nonempty subsets of [1,12] identified the set

  A={1,2,3,4,5,6,7,9}, n=8, M=2, R=1/sqrt(2).

Unlike the search itself, the following conclusions have exact computer-assisted certificates in [subset_certificate.py](../experiments/cstar_structural_2026-10-20/subset_certificate.py) and [subset_certificate.json](../experiments/cstar_structural_2026-10-20/subset_certificate.json).

Writing t=cos(2πx),

  f_A+2=(t+1)Q(t),
  Q(t)=256t^8−256t^7−256t^6+288t^5+48t^4−88t^3+8t²+4t+1.

Exact rational Sturm root counting gives zero roots of Q in [-1,1]. Since Q(0)=1, Q>0 there. Thus f_A≥−2, with equality at t=−1. For each of all 254 proper nonempty subsets B, the certificate supplies t_B=j/10000 in [-1,1] such that, exactly in rational arithmetic,

  f_B(t_B)<0 and 2 f_B(t_B)^2>|B|.

Therefore every proper nonempty B has R(B)>1/sqrt(2): A is strictly hereditary ratio-minimal. Floating polynomial roots only propose t_B; the proof checks the displayed rational inequalities and uses exact Sturm arithmetic for the full set. No floating comparison is relied on in the certificate.

Now choose fractional half-mass weights

  w_a=(8−a)/7 for a=1,...,7, and w_9=0.

All weights lie in [0,1], sum to 4, and

  sum_a w_a cos(2πax)=(4/7)(K_8(x)−1),

where K_8 is the nonnegative normalized Fejér kernel. Consequently M(w)=4/7. Every Boolean cardinality-four subset instead has M(B)>sqrt(2). The integral optimum divided by the fractional optimum is therefore strictly greater than 7sqrt(2)/4≈2.47487 (the fractional optimum could be smaller; equality 4/7 is not needed).

This is a concrete, exactly certified counterexample to any claim that selecting a hereditary ratio-minimal Boolean support removes Fejér-type fractional controls. It does NOT show an unbounded gap as n grows, nor does it refute the possibility of a bounded-gap rounding theorem. Its contribution is to isolate the genuinely remaining integrality issue after the subset selection.
