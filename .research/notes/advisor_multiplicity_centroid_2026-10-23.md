# Independent audit: a global line-centroid multiplicity defect bound

2026-10-23. Internal AI advisor, paper proof and read-only ledger audit.
Only this assigned note is edited. No research computation, VM operation,
GPU, extra agent or external outreach. Shared Dirichlet remains on.

The lead's proposed bound is CORRECT. The path geometry sharpens its
denominator from8 to6. This closes the specific growing-multiplicity
L1-defect construction mechanism considered immediately before this note.
It does not lower-bound the actual cosine minimum of an arbitrary A.

## 1. Quantified statement

Let B be any set of k>=2 distinct integers. For every positive difference
d in A=diff_+(B), let

    r_d=#{b in B:b+d in B}.

Fix an integer r>=2 and set

    E=sum_(d in A)|r_d-r|.

Then

    E>=((r-2)*k+2r)/6.                             (1)

In particular the lead's weaker proposed estimate

    E>=((r-2)*k+2r)/8                              (2)

holds. No diameter, density, symmetry, modular lifting, low-M hypothesis
or relation between r and k is required. The same proof even works for
distinct real positions, with sums over their finitely many real lags;
integrality is not the source of this obstruction.

## 2. Exact centroid Gram identity and its upper bound

Write x_b=b-mean(B) and V=sum_b x_b^2>0. For every signed integer lag d
define

    S_d=sum_(b,b+d in B) x_b.

Only finitely many S_d are nonzero and S_0=0. Expanding their squares,

    sum_(d in Z) S_d^2 = x^T G x,
    G_bc=#{d:b+d,c+d in B}.

Here G_bb=k and G_bc=r_|b-c| for b!=c. Every nonzero |b-c| belongs to A,
which is important: the comparison baseline r is applied only at actual
off-diagonal B-pairs, not at absent difference classes. Thus

    G=r*J+(k-r)*I+R,
    R_bb=0, R_bc=r_|b-c|-r for b!=c.

For each row b and each positive lag d there are at most two possible
columns b-d,b+d. Consequently

    sum_c |R_bc|<=2E.

As R is symmetric, the elementary estimate 2|x_b*x_c|<=x_b^2+x_c^2
gives |x^T R x|<=2E*V. Centering kills x^T J x exactly. Therefore

    sum_d S_d^2 <= (k-r+2E)*V.                     (3)

This is a global finite matrix identity, not the conditional finite-lift
concentration estimate in old P77.

## 3. Lower bound and the path improvement

For d>0, the change from lower to upper endpoint gives

    S_-d=S_d+r_d*d.

Hence

    S_d^2+S_-d^2 >= r_d^2*d^2/2.

Also the standard pair-variance identity gives

    sum_(d>0) r_d*d^2
      =sum_(b<c in B)(b-c)^2=k*V.                 (4)

Writing delta_d=r_d-r, one has r_d^2>=r*r_d-|delta_d|*r_d.
The lead used the general maximum-degree-two graph estimate

    r_d*d^2<=4V.

It is valid: the lag-d edges form a union of paths, and summing
(x_b-x_c)^2<=2(x_b^2+x_c^2) uses degree at most2. This would give

    sum_d S_d^2 >= (r*k/2-2E)*V,

which combined with (3) proves (2), with all factors as proposed.

For this particular position vector, the paths give the better bound

    r_d*d^2<=2V.                                  (5)

Indeed a component with m>=2 vertices consists of equally spaced
positions x_0,x_0+d,...,x_0+(m-1)d. Its sum of squares is at least
its variance about its OWN mean,

    d^2*m*(m^2-1)/12 >= (m-1)*d^2/2.

The last inequality is m*(m+1)>=6. Summing over all components,
including isolated vertices, proves (5). No choice of component
means alters the original global centroid or identity (3).

Equations (4)--(5) now yield

    sum_d S_d^2
      >= (r/2)*sum_(d>0)r_d*d^2
           -(1/2)*sum_(d>0)|delta_d|*r_d*d^2
      >= (r*k/2-E)*V.                             (6)

Comparing (3) and (6), then dividing by V>0, gives

    3E>=(r/2-1)*k+r,

which is precisely (1). The assumption k>=2 is essential to this
division; k=1 has no positive difference support and is excluded.

## 4. Consequence for the proposed all-circle certificate

Let N=|A| and T=k*(k-1)/2. The construction certificate was

    U=(k+2E)/(2r), M(A)<=U,
    |r*N-T|<=E.                                   (7)

If r tends to infinity along ANY sequence of B, (1) implies

    E/(k*sqrt(r))
      >=(r-2)/(6*sqrt(r))+sqrt(r)/(3k) ->infinity.

Thus the proposed sufficient condition E=o(k*sqrt(r)) is impossible.
This is an unconditional obstruction to the EXACT full-support,
single-target-multiplicity L1 certificate, not merely the failure
of the one pilot or a reflection-symmetric subclass.

There is also a finite floor on this certificate's normalized upper
value R_cert=U/sqrt(N). Already the weaker bound (2) proves

    R_cert>1/2 for EVERY k>=2,r>=2.                 (8)

To verify it without any asymptotic assumption, put

    e=((r-2)*k+2r)/8.

Since N<=(T+E)/r and E>=e>=0,

    R_cert^2 >= (k+2E)^2/[4r*(T+E)]
                >=(k+2e)^2/[4r*(T+e)].

The middle expression increases with E because the derivative of
(k+2E)^2/(T+E) has the sign of 4T-k+2E>0 for k>=2. Finally,

    16*((k+2e)^2-r*(T+e))
       =(r-2)^2*k^2+2r*(r+10)*k>0.

This proves (8). It means the completed r=8 pilot's half-constant
CERTIFICATE gate was analytically impossible in advance. It says
neither that its actual R exceeds1/2 nor that arbitrary cosine
supports satisfy a half-constant lower bound.

For fixed r and k tending to infinity, (2) gives the lead's stated
asymptotic certificate floor

    liminf R_cert >= (r+2)/(4*sqrt(2r)),

whose minimum over r>=2 is1/2 at r=2. The sharper estimate (1)
improves this fixed-r floor to (r+1)/(3*sqrt(2r)), again minimized
on r>=2 at r=2 with value1/2. When r=o(k), the corresponding
lower estimates hold with a relative factor1+o(1). They should
not be quoted with an omitted denominator correction for arbitrary
joint growth of r and k. The exact finite bound above needs no
such restriction.

## 5. Ledger comparison and status

I inspected the actual statements of PROOFS P76, P77 and its scope,
and the corresponding centroid/CP route entries. P76(c) is the
extreme-lag inequality r_(b_k-b_i)<=i and the impossibility of
EXACT flat multiplicities. It does not contain this uniform L1
defect bound. P77 is a finite-model Boolean-lift centroid/Taylor
bound requiring a background set and concentration eigenvalue;
its arbitrary-support caveat is explicit. Neither inspected
statement contains (1) or the unrestricted Gram calculation here.
This is a within-project comparison, not an external novelty search
or a claim of mathematical priority.

This note SUPERSEDES the provisional unresolved-obstruction statement
in advisor_exponential_depth_2026-10-23.md Section5. The root's
new centroid argument resolves that specific missing step, and the
path refinement improves its constant. The previous endpoint and
parity gates remain valid but are no longer the decisive bounds.

Status: (1)--(8) are independently checked paper proofs, not Lean
or other kernel-checked mathematical proofs. No numerical result
was used. The global Chowla conjecture and independent arbitrary
signed-certificate track remain open. Stop this growing-r L1
mechanism and do not enlarge its completed pilot. Other methods of
handling multiplicities, or other constructions, are not excluded.

## 6. Fractional reference multiplicities do not evade the floor

For the SAME fixed B with k>=2, positive difference support of size N,
and T=k*(k-1)/2, allow ANY real reference r>0. Define

    E(r)=sum_(d in A)|r_d-r|,
    R_cert(r)=[k/2+E(r)]/[r*sqrt(N)].

Then

    inf_(r>0) R_cert(r)>1/2.                       (9)

Indeed the finitely many breakpoints are the positive integer
multiplicities r_d. On each interval between them, E(r)=a+b*r,
so R_cert(r)=[b+(k/2+a)/r]/sqrt(N) is monotone or constant.
As r decreases to0 the expression diverges. Beyond the largest
multiplicity, E(r)=N*r-T and the tail is exactly

    R_cert(r)=sqrt(N)+k*(2-k)/[2r*sqrt(N)].

This is increasing for k>2 and constant for k=2. Thus the global
minimum is attained at one of the finitely many integer breakpoints;
constant intervals or the k=2 tail have the same value at an endpoint.
The mere existence of the limiting value sqrt(N) would not, without
this tail-sign check, have proved finite attainment.

At the integer reference r=1, E>=0 and N<=T give

    R_cert(1)>=k/[2sqrt(N)]>=k/[2sqrt(T)]>1/sqrt(2).

At every integer reference r>=2, (8) gives R_cert(r)>1/2.
Taking the minimum over finitely many breakpoints proves (9).
This closes the fractional-reference loophole for the exact
single-target L1 remainder certificate. It still gives no lower
bound on the actual M(A) or R(A).
