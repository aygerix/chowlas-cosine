# Advisor audit: the analytic square-root signed witness

2026-10-21. Independent paper derivation by the one internal advisor.
Only this assigned note was edited. No research computation, VM job,
provisioning, spending, new agent, or external communication was performed.
No Lean/kernel-checked mathematical proof or external specialist review is
claimed. The unrestricted Chowla problem remains open.

All circle integrals below use dx/(2*pi). Let A be a finite nonempty set of
distinct positive integers, n=|A|, X=max(A),

    F(z)=sum_(a in A) z^a, f=Re F, D=2f, M=-min f, K=2M.

The branch considered here has the ACTUAL all-circle hypothesis M<=sqrt(n).
Set lambda=2sqrt(n), s=sqrt(lambda), and

    g(z)=sqrt(lambda+F(z))-s, q=2s Re g, G=integral |g|^2.

The square root is the principal analytic branch. The estimates in Sections
1--4 are proved for arbitrary A. Their missing coupling estimate is not
proved, and no max-frequency hypothesis enters their statement. The
frequency-density hypothesis in Section 7 is used only to refute a proposed
higher-power witness principle, not in an unrestricted Chowla conclusion.

## 1. Analyticity and exact identities

The boundary bound Re(lambda+F)>=lambda-M>=lambda/2>0 also holds on the
closed disk by the harmonic minimum principle. Hence the square root is
analytic on a neighborhood of that disk, g(0)=0, and its Taylor coefficients
are real. In particular mean(g)=mean(g^2)=mean(g^3)=0. Write g=u+iv and put

    theta=sqrt(1-M/lambda), c=1+theta,
    c0=1+1/sqrt(2), so theta>=1/sqrt(2), c>=c0.

The elementary identity and real-part bound are

    F=2s g+g^2,
    Re sqrt(lambda+F)>=sqrt(lambda-M),
    u>=-s(1-theta).

Since |sqrt(lambda+F)|^2=|lambda+F| and mean(Re g)=0,

    G=integral |lambda+F|-lambda.

The mean-zero real witness has the exact squared norm

    Q=integral q^2=2lambda G.                         (1.1)

For the coupling a=integral Dq, write B=integral |g|^2 u. The identity
mean(g^3)=0 gives integral u^3=3 integral uv^2 and therefore
integral u(u^2-v^2)=B/2. Expanding F and q now gives

    a=4lambda G+2s B
     >=2lambda(1+theta)G
     =c Q>=c0 Q.                                    (1.2)

Thus coupling is positive for nonempty A. This is not yet macroscopic
coupling: Q, equivalently G, could be too small.

## 2. Uniform norm and mixed-cost bounds

Let phi=sqrt(lambda+F). Since Re phi>=0,

    |phi+s|>=|phi-s|,  (phi-s)(phi+s)=F,
    |g|^2<=|F|.                                     (2.1)

Also |phi+s|>=s(1+theta), so Parseval gives

    G<=n/[lambda(1+theta)^2],
    Q<=2n/(1+theta)^2<=2n/c0^2<2n.                 (2.2)

At lambda=2sqrt(n), this also says G/sqrt(n)<=3-2sqrt(2).

For H=integral Dq^2, use (2.1), ||D||_2=sqrt(2n), and ||F||_2=sqrt(n):

    |H|<=4lambda integral |D||g|^2
        <=4lambda integral |D||F|
        <=4sqrt(2)lambda n
         =8sqrt(2)n^(3/2).                          (2.3)

These proofs use only analytic positive-frequency F, its L2 norm, and its
lower real-part bound. They do not yet exploit Boolean coefficients.

## 3. Degree less than 2X with EXACTLY the same coupling

Let Fejer_N have multiplier (1-|j|/N)_+ and mean one, and define

    V=2Fejer_(2X)-Fejer_X, q_B=V*q.

Its Fourier multiplier is one for |j|<=X, belongs to [0,1], and vanishes
for |j|>=2X. Its L1 norm is at most three. Consequently

    mean(q_B)=0, degree(q_B)<2X,
    integral Dq_B=a, Q_B<=Q.                        (3.1)

There is no truncation loss in a. By (2.1), integral |g|^4<=n, and hence

    ||q||_4^2<=4lambda sqrt(n),
    ||q_B||_4<=3||q||_4,
    |H_B|<=||D||_2 ||q_B||_4^2
           <=36sqrt(2)lambda n
            =72sqrt(2)n^(3/2).                     (3.2)

This supplies an explicit finite-band signed seed with automatic norm and
cost bounds. Only its coupling remains unproved at scale n. It is a
concrete realization within the existing C* programme, not a new proof of
the arbitrary-Boolean estimate.

## 4. Coupling and L1 flatness: both directions, with constants

Put t=G/sqrt(n). The identity f=2s u+Re(g^2) and Cauchy--Schwarz give

    ||f||_1<=sqrt(2lambda G)+G,
    ||f||_1/sqrt(n)<=2sqrt(t)+t.                    (4.1)

Thus L25, namely ||f||_1>=sqrt(n)/10 on the actual low-M branch, would imply

    t>=(sqrt(11/10)-1)^2.                            (4.2)

For the converse, let N=D_- and L=||D||_1. Since N<=K,

    a^2<=L integral |D|q^2<=L(H+2KQ).

Using (1.1), (1.2), K<=lambda, and (2.3), this yields

    ||f||_1/sqrt(n)>=c0^2 t^2/(sqrt(2)+2t).

The simpler Q<=2n version gives the weaker but useful bound

    ||f||_1/sqrt(n)>=[(1+sqrt(2))/2] t^2.            (4.3)

Therefore a uniform positive lower bound G>=epsilon sqrt(n) is equivalent,
UP TO CHANGING ABSOLUTE CONSTANTS, to positive-constant L1 flatness in the
same low-M class. This is not an equivalence between the specific numerical
threshold (4.2) and the exact L25 constant 1/10.

Likewise, (1.2) and a^2<=2nQ show

    G>=epsilon sqrt(n) => a>=4c0 epsilon n,
    a>=alpha n        => G>=alpha^2 sqrt(n)/8.       (4.4)

So proving macroscopic coupling for this particular seed would close the
same qualitative L1 gap; the analytic change of variables alone does not
supply the Boolean input. It does give a finite, exact coefficient test for
that missing estimate, as follows.

## 5. Exact Boolean coefficient recurrence and a finite diagnostic

Define the analytic function

    h=2s g=sum_(j>=1) v_j z^j, so q=Re h.

Its exact algebraic equation and coefficient recurrence are

    F=h+h^2/(4lambda),
    v_j=1_A(j)-(1/(4lambda))*sum_(u=1)^(j-1) v_u v_(j-u).   (5.1)

In particular

    a=sum_(a in A) v_a, Q=(1/2)*sum_(j>=1) v_j^2.    (5.2)

Coupling requires coefficients only through X. The degree-<2X seed requires
only coefficients through 2X-1, multiplied by the explicit rational V
multiplier. All these coefficients lie in Q(sqrt(n)); the intermediate
sqrt(lambda) introduces no quartic extension in h. Exact algebraic
arithmetic or certified rational reconstruction can therefore evaluate the
finite seed without whole-circle square-root quadrature.

Equation (5.1) is the precise additional restriction from zero/one Fourier
coefficients. It is not itself a lower bound on the sum in (5.2). A putative
proof must control cancellations in this recurrence using low M; applying
only the positivity and norm estimates above also applies to weighted
escapes and cannot do so.

An elementary subcase illustrates the restriction without claiming a new
route. If a in A is not a sum of two or more elements of A, with repetitions
allowed, the formal power series gives v_a=1. Thus, if p elements have this
property, G>=p/(4lambda), Q>=p/2, a>=c0*p/2. These elements form an
A-independent subset: a>b and a-b in A would decompose a. A positive
proportion is therefore already an easy branch of the recorded P9/star
method. This observation does not treat the hard, highly decomposable case.

No rigorous low-M BOOLEAN example with G/sqrt(n)->0 was found in this
audit. Such an example would also disprove qualitative low-M L1 flatness by
(4.1), rather than merely refute a stronger implementation choice.

## 6. Weighted escape and inadmissible interval test

For m>=2 let

    F_m(z)=sum_(a=1)^(m-1) (1-a/m) z^a,
    n_eff=sum (1-a/m)^2=(m-1)(2m-1)/(6m).

Then f_m=(Fejer_m-1)/2>=-1/2, so the corresponding low-M condition holds.
Also ||f_m||_1<=1. The identity

    F_m(z)=z/(1-z)-z(1-z^m)/[m(1-z)^2]

implies ||F_m||_1=O(log m): use |F_m|<=m/2 on |x|<=1/m, and
C/|x|+C/(m*x^2) on the remainder of [-pi,pi]. Therefore, with
lambda=2sqrt(n_eff),

    0<=G_m=integral |lambda+F_m|-lambda
          <=||F_m||_1=O(log m)=o(sqrt(n_eff)).

Cauchy--Schwarz and Q=2lambda G then also give a=o(n_eff). Thus the
coefficient-relaxed universal coupling assertion is false, including under
a strong actual lower real-part bound. The recurrence's Boolean right-hand
side is essential.

For Boolean intervals A={1,...,n}, ||F||_1=O(log n) also forces small G, but
M has linear scale. They are not counterexamples under M<=sqrt(n). This
distinction must be checked for every proposed falsifier.

## 7. Every fixed power alpha>1/2 has excessive cost on dense low-M inputs

This is a paper obstruction to a witness principle, not a new exclusion of
a counterexample construction. It uses a finite elementary front and no
specialized Singer asymptotic.

Fix alpha>1/2, C0,C1,C2>0 with C2>=2C1. For every sequence of Boolean sets
with n->infinity,

    X<=C0*n, M<=C1*sqrt(n), lambda=C2*sqrt(n),

put

    q_alpha=lambda^(1-alpha)*Re[(lambda+F)^alpha-lambda^alpha].

It is mean zero and uses the principal analytic power. There is a positive
constant c, depending only on the displayed fixed parameters, such that
eventually

    H_alpha=integral D*q_alpha^2>=c*n^(1+alpha).     (7.1)

PROOF. Let eta=pi/[4 max(1,alpha)]. On |x|<=eta/X, every z^a has argument
in [-eta,eta]. The same is true of F and lambda+F; Re F>=n cos(eta).
Consequently

    Re(lambda+F)^alpha
       >=cos(alpha*eta)*(n cos(eta))^alpha.

Subtracting lambda^alpha=O(n^(alpha/2)) leaves at least c_alpha*n^alpha
for large n. On this interval D>=2n cos(eta), q_alpha^2>=c*n^(1+alpha),
and its normalized measure eta/(pi X)>=eta/(pi C0 n). Its positive
contribution to H_alpha is therefore at least c*n^(1+alpha).

The negative contribution cannot cancel this scale. Along the straight
path lambda+tF, 0<=t<=1, Re(lambda+tF)>=lambda-M>=lambda/2, so

    (lambda+F)^alpha-lambda^alpha
       =alpha F integral_0^1 (lambda+tF)^(alpha-1) dt.

For 1/2<alpha<=1, the negative exponent gives |q_alpha|<=C_alpha |F|,
hence Q_alpha=O(n). For alpha>=1, use |F|<=n and lambda+n<=C*n to obtain
|q_alpha|<=C*n^((alpha-1)/2)|F| and Q_alpha=O(n^alpha). Thus

    integral D_- q_alpha^2<=2M Q_alpha
       =O(n^(3/2))             if alpha<=1,
       =O(n^(alpha+1/2))       if alpha>=1.

Both are o(n^(1+alpha)) for the stated alpha range. This proves (7.1).
No exact asymptotic or matching upper bound for H_alpha is asserted.

This failure survives normalizing nonzero coupling to a=n. By
a_alpha^2<=2nQ_alpha, the normalized mixed cost is bounded below by

    c*n^(1+alpha)              if 1/2<alpha<=1,
    c*n^2                     if alpha>=1.         (7.2)

If the coupling vanishes, it supplies no certificate. Either way these
powers cannot yield the required universal O(n^(3/2)) normalized cost.

The existing canonical perfect-difference supports provide infinitely many
inputs with X<=2n and M<=sqrt(n): for a cyclic (k(k-1)+1,k,1) difference
set, positive integer differences are distinct, n=k(k-1)/2, and
D=|F_B|^2-k>=-k. Their existence and the exact identity are already recorded
in advisor_L25_derivation_2026-10-21.md. This supplies the necessary actual
Boolean low-M examples; no new family experiment is needed.

At alpha=1/2 the q_alpha convention is half the original q. Including a
factor 1/alpha would match it exactly; all obstruction constants only
change by a fixed factor. The argument establishes why alpha>1/2 is too
large. It does not claim that alpha=1/2 is the only possible useful
nonlinear function or that smaller powers solve the coupling problem.

## 8. Decision and first discriminating test

The square-root ansatz is mathematically valid, has automatic uniform norm
and mixed-cost bounds, and has an explicit degree-<2X implementation with
the same coupling. Its exact open statement is

    exists alpha0>0, for EVERY finite nonempty Boolean A:
    M(A)<=sqrt(|A|) => sum_(a in A) v_a>=alpha0*|A|,

where v is specified by (5.1) at lambda=2sqrt(|A|). The constants are
absolute; no span, density, or construction restriction may be inserted in
this claim. A proof would be a real advance; it is not proved here. The
weighted escape refutes the relaxed version, and Section 4 identifies its
precise relationship to the existing L1 gap.

The appropriate bounded implementation test is the exact/certified
coefficient recurrence on an already saved low-M Boolean input, paired
with the weighted Fejer control, checking a/n as well as Q/n and H/n^1.5.
The comparison with a certified full-space optimizer may distinguish a
weak seed from a genuinely low-leverage input. Finite success alone
justifies neither expansion of canonical family sweeps nor GPU work.
An actual vanishing Boolean coupling sequence, with certified global low M,
would falsify this seed's universal estimate and qualitative L1 flatness.

Retain the unrestricted signed/resolvent route and independent all-circle
construction track. Retire the fixed powers alpha>1/2 as a universal
bounded-cost substitute. The next substantive mathematical step is a
Boolean estimate for the selected-coefficient sum in (5.2), or a different
signed certificate with a demonstrably distinct missing ingredient.
