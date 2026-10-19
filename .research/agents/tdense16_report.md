# Round 16 report — adaptive flatness and multiplicative Gauss phases

Status: COMPLETED through the brief's precise-obstruction alternative. WRS remains unproved; no new exponent or integer corollary is claimed. The main result is the explicit quarter-scale adaptive-core-sumset obstruction below, with independent finite verification.

## Scope, exact target, and source record

PROVED scope: the active brief is `.research/agents/tdense16_brief.md`. Only this report and `.research/agents/tdense16_scratch/` will be written. No commits, subagents, or local mathematical computation. Computations will use `DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4`, with bash for command scripts. All convolution sums below are unnormalized on Z_q; inverse additive Fourier transform has factor 1/q.

CONJECTURED target WRS(eta): find absolute eta>0, A>0, delta0>0 so every prime q=1 mod 4 and every symmetric nonzero half-set B gives h>=0, h(0)=t=K-1/2, sum h=qt, h*h=(q^2/4)delta_0+q(t^2-1/4)1, and max h outside 0 <= A q^((1-eta)/2)t^(1+eta) when 1/2<t<=delta0 sqrt(q). Alternatively provide the precise conditional or obstruction deliverable specified in the brief.

PROVED source loading: read CLAUDE.md, PROOFS P64–P68, NOTEBOOK continuation 18 (including both corrections to the proposed window mechanism), and round 15 Part B. The number-theory-research skill is applied, with this report replacing its default notebook location under the brief's explicit write restrictions. P68's exact flat model and WRS reduction are quoted, not new.

## Research frontier and current work

| Status | Known fact / exact gap | Discriminating operation |
|---|---|---|
| PROVED, quoted P68 | Full off-zero flat convolution is equivalent to the Boolean plateau with the stated trace | Keep all zero-mode terms in every identity |
| PROVED, quoted P68 | A fixed local defect only improves the quarter-exponent constant | Seek a defect that tends to one at a power rate |
| UNKNOWN | Adaptive D+D equations might impose more than scalar/segment identities | Expand core/bulk cross terms, then average with exact representation weights |
| UNKNOWN | Multiplicative Gauss phases might distinguish prime Boolean spectra from fakes | Derive normalized convolution and phase correlations before invoking bounds |
| PROVED, quoted P65–P68 | Scalar moments, fixed-order arithmetic, fixed segments, and parity alone are insufficient | Test all proposed intermediate statements on the preserved adversaries |

## Historical checkpoint log

- Initial checkpoint: loaded the brief and prior exact obstructions. Next: simultaneous core-sum equations and the genuinely distinct multiplicative transform. No new mathematical claim yet.

## First derivation: simultaneous core/bulk bookkeeping

PROVED. For any genuine half-set in the stated setting, let D={a!=0:h(a)>=L/2}, s=|D|, p=h*1_D (pointwise product), u=h-p>=0, f=1_D, and r=f*f. At every nonzero xi in D+D,

    p*p(xi)+2p*u(xi)+u*u(xi)=C0.

Every summand is nonnegative. For any nonnegative weights w supported on (D+D) outside zero, the exact simultaneous equation is

    sum w(xi)[p*p(xi)+2p*u(xi)+u*u(xi)]=C0 sum w(xi).

In particular, with w=r and Eadd(D)=sum r^2,

    (L^2/4)[Eadd(D)-s^2] <= C0(s^2-s).

This retains the zero displacement separately: r(0)=s. It also yields the exact smoothing identity

    sum_x (f*h)(x)^2 = q^2*s/4+C0*s^2,
    sum_x [(f*h)(x)-s*t]^2 = q*s*(q-s)/4.

Proof: expand the left side as sum_{d,e in D}(h*h)(d-e); the diagonal uses q^2/4+C0 and the other pairs use C0. The variance formula uses sum h=qt and C0=q(t^2-1/4). Only the equations on D-D=D+D and at zero were used. The Boolean input is precisely the flat convolution equation; the expansion alone does not impose Booleanity.

PROVED caution. Parseval gives s*L^2/4 <= V, with V=q^2/4+C0. It does NOT give s*L^2 approximately V without an additional core-energy hypothesis. At t=q^(1/4) times a growing logarithm the endpoint defect need not be small; P68.8 and round 15 B3 forbid silently adding that hypothesis. The next construction tests this distinction on the full sumset of the actual threshold core.

## Second derivation: exact multiplicative normalization

PROVED. Let G=F_q^*/{+1,-1}, n=(q-1)/2. A half-set is a Boolean f:G->{0,1} of mean 1/2; put F=f-1/2. With c(x)=2cos(2*pi*x/q), lambda(a)=sum_x f(x)c(ax). For the normalized Mellin transform hat v(chi)=n^(-1)sum_x v(x)conj(chi(x)), define tau(chi)=sum_{x!=0}chi(x)e(x/q), theta_chi=tau(chi)/sqrt(q). Then

    X=(lambda+1/2)/sqrt(q),
    hat X(1)=hat F(1)=0,
    hat X(chi)=theta_conj(chi) * hat F(conj(chi))   (chi!=1).

The inversion of the character index matters: this is multiplicative correlation, rather than convolution without a reflected argument. On mean-zero functions the cosine matrix divided by sqrt(q) is a real orthogonal involution: C^2=qI-2J. Hence mean X=0 and mean X^2=1/4 exactly. The one-sided condition is X>=-epsilon with epsilon=t/sqrt(q).

PROVED anti-concentration consequence. Positivity of X+epsilon gives |hat X(chi)|<=epsilon for chi!=1. Gauss-sum modulus then gives

    max_{chi!=1}|hat F(chi)| <= epsilon,
    #{chi:hat F(chi)!=0} >= 1/(4epsilon^2)=q/(4t^2).

More generally, any collection carrying at least (1-rho)/4 of the Mellin energy has size at least (1-rho)q/(4t^2), for every 0<=rho<1. Thus, in the small-epsilon regime, concentration on a bounded number of multiplicative characters is incompatible with the one-sided condition. Paley is the boundary case F=chi_quadratic/2 and epsilon=1/2. This does not refute concentration on a growing collection; it specifies its necessary minimum size.

PROVED Boolean phase constraint. In addition to the preceding linear transformation, F^2=1/4 is exactly equivalent to

    sum_psi hat F(psi)hat F(chi/psi) = (1/4)*1_{chi=1}.

For nontrivial chi, substitution expresses this as a Jacobi-sum weighted quadratic constraint on the coefficients of X. The character phases alone do not supply this Boolean identity: it is the multiplicative form of the missing global constraint. Detailed source bounds and completed adversarial tests follow below.

- Checkpoint: obtained exact core/bulk equations and the multiplicative anti-concentration bound. An adaptive-sumset obstruction is being constructed with a growing threshold core; no WRS estimate has followed.

## Task 1 obstruction theorem: exact flatness on the full adaptive core sumset

PROVED (paper). For every sufficiently large prime q=1 mod 4 there is a real, nonnegative, even array h on Z_q with the following properties. Set g=ceil(log q), m=g^2, s=2m, t=q^(1/4)g, C0=q(t^2-1/4), V=q^2/4+C0, and

    L=sqrt(C0/(4s)),
    D=+/-{10m+1,...,11m},
    S=(D+D) outside zero.

Then h(0)=t, sum h=qt, sum h^2=V, max h=L, and D is EXACTLY {a!=0:h(a)>=L/2}. Moreover

    |D|=2g^2,    |S|=6g^2-4,
    h*h(xi)=C0 for every xi in S,
    h*h(0)=V.

Thus all the equations on D+D, including zero, hold at once for the actual growing threshold core. The same construction works under multiplication of every support index by any nonzero residue. At every xi in S, the core-core contribution is at most C0/4; the non-core terms supply at least 3C0/4. The core energy fraction is

    sum_D h^2 / V = C0/(4V) ~ g^2/sqrt(q) -> 0.

The array fails WRS(eta) for every fixed eta>0 and every fixed A>0 for all sufficiently large q in this family, because

    L ~ q^(3/4)/sqrt(8),
    L/[q^((1-eta)/2)t^(1+eta)] ~ q^(eta/4)/(sqrt(8)*g^(1+eta)) -> infinity.

This is an obstruction for the stated relaxation, not a genuine Boolean half-set or a counterexample to WRS.

PROVED local-defect diagnosis at every peak a in D. Since 2a belongs to S, its exact equation gives

    1-Delta_a = L^2/C0 = 1/(4s) = 1/(8g^2).

Thus the leftover peak fraction decays only logarithmically, while the WRS requirement is a fixed positive power of t/sqrt(q)=q^(-1/4)g. Averaging these identities over every peak, or weighting every displacement in D+D, cannot turn this fake's logarithmic decay into the required power decay.

PROVED scalar normalization check. Set K=t+1/2, lambda(0)=(q-1)/2, and lambda(a)=h(a)-K off zero. Then min lambda outside zero is exactly -K, max lambda outside zero is L-K, sum lambda=0, and sum lambda^2=q(q-1)/2. The inverse weighted b has b(0)=0 and total mass (q-1)/2, but is not Boolean. Its centered restriction F to G has mean zero and mean square 1/4, so the multiplicative normalization and anti-concentration test apply literally to this relaxation.

PROVED construction and support geometry. Write B0=100m and ell=16s. Let r_D be the ordered representation function. The positive elements of S are {1,...,m-1} together with {20m+2,...,22m}. For each such d define

    a_d=sqrt((C0-L^2*r_D(d))/(2ell)).

These are positive and a_d<=L/sqrt(8)<L/2. Put h=t at zero and h=L on D. Allocate ell clusters for each d. The j-th cluster has support {B0*j,B0*j+d,-B0*j,-B0*j-d}, with value a_d on its four sites, using j=1,2,... consecutively. Different positive clusters are separated by at least 78m; the initial core ends at 11m, and reflected clusters are equally separated. Hence no cross-cluster or core-cluster difference lies in S. All support is interpreted as signed residues; the eventual support is contained in an interval shorter than q/2, so there are no wraparound differences in S. Since h is even, convolution equals autocorrelation. Each d-cluster contributes exactly 2a_d^2 at d and -d, and no other element of S. The value h(d) is zero for every d in S, so no h(0) cross term has been discarded. Consequently h*h(d)=L^2*r_D(d)+2ell*a_d^2=C0.

PROVED exact mass and energy repair. Let M0,Q0 be the mass and energy already placed, and put T=qt-M0, E0=V-Q0. The displayed parameters give

    M0=O(m^(3/2)*sqrt(q)*t)=o(qt),
    Q0=O(m*q*t^2)=o(q^2),
    T~qt, E0~q^2/4.

Choose n0=4*ceil(3T^2/(8E0)), mu=T/n0, v=E0/n0-mu^2. For all sufficiently large q,

    (3/2)T^2/E0 <= n0 <= 2T^2/E0,
    0<=v<=mu^2,
    0<=mu-sqrt(v)<=mu+sqrt(v)<=2mu <=(4/3)E0/T < L/2.

After the last cluster, place n0/2 positive repair sites on the grid B0*j, with the first n0/4 at height mu+sqrt(v) and the next n0/4 at height mu-sqrt(v). Reflect them to supply n0 sites in total. They have exactly mass T and energy E0; they create no correlation at S. The entire used half-line has length

    O(m^3+m*t^2)=O(g^6+sqrt(q)*g^4)=o(q).

This proves capacity, absence of wraparound, and the exact threshold-core assertion. Also t<L/2 for large q, so the zero site does not affect the threshold.

PROVED explicit missing equation. The displacement B0=100m lies outside D+D. Write a=mu+sqrt(v), b=mu-sqrt(v). Adjacent repair sites alone give

    h*h(B0) >= E0-2(a^2+b^2-a*b) = (1/4+o(1))*q^2.

The upper bound h*h(B0)<=V=(1/4+o(1))*q^2 follows by Cauchy–Schwarz. Since C0=o(q^2),

    h*h(B0)-C0 = (1/4+o(1))*q^2.

The same holds at -B0. Thus the global off-zero equation fails by a maximal-order amount at an explicitly identified bulk displacement. This is the exact equation that the adaptive core-sumset test misses.

PROVED consistency statement. This family satisfies every core/bulk weighted identity above, for arbitrary nonnegative weights on S, as well as the exact smoothing/variance identity, mass, energy, the elementary peak square bound L^2<=C0, endpoint-rounding bounds, and the multiplicative linear Gauss transformation and anti-concentration estimate. The latter statements need only evenness, trace, energy, and the one-sided condition; they do not force a coefficientwise Boolean plateau. The full Boolean quadratic phase constraint is NOT asserted for the fake: the displayed failure at B0 proves it cannot hold.

PROVED finite artifact, distinct from the infinite-family proof. `tdense16_scratch/adaptive_fake.py` works with the same parameterized construction and checks every correlation monomial exactly, using a compressed arithmetic-progression representation of the repair sites. Three finite prime inputs with t=2*(floor(q^(1/4))+1) were verified with 200-bit Arb. These finite parameter choices illustrate the construction's general formula; they are not a numerical inference of its asymptotic theorem. Output: `adaptive_fake.json`; VM log: `adaptive_fake.log`. No optimizer was used.

| Status | q | m | actual core size | nonzero core-sum equations | support size | (h*h)(100m)/C0 |
|---|---:|---:|---:|---:|---:|---:|
| PROVED finite counts + Arb | 1000000009 | 1 | 2 | 2 | 760179 | >1973 |
| PROVED finite counts + Arb | 10000000033 | 2 | 4 | 8 | 2411085 | >6220 |
| PROVED finite counts + Arb | 100000000057 | 4 | 8 | 20 | 7604369 | >19718 |

- Checkpoint: the permitted precise-obstruction deliverable is now proved. It strengthens the old fixed-segment fake by enforcing the entire sumset of the actual growing heavy core at the quarter-power scale. It does not settle the global Boolean problem. Next: genuine-set adversarial checks and the limits of phase moment/product bounds.

## What uniform core coverage does and does not contradict

PROVED. Near-uniform r_D outside zero is compatible with genuine Boolean half-sets in general. For Paley, take D to be the nonzero quadratic residues. Then s=(q-1)/2, t=sqrt(q)/2, L=sqrt(q), h=L*1_D+t*delta_0, and for xi!=0,

    r_D(xi)=(q-3-2*chi_quadratic(xi))/4,
    L^2*r_D(xi)+2tL*1_D(xi)=C0=q(q-1)/4.

Thus r_D=(1+O(1/q))*s^2/q uniformly off zero, and the exact non-core contribution fills the deficit on D; off D the core-core term already equals C0. A claim that uniform coverage alone contradicts Booleanity is false. This example has t~sqrt(q), so it does not establish realizability in the small-t regime.

PROVED exact scalar restriction from the full equations. For any core part p=h*1_D, put M_D=sum p and Q_D=sum p^2. Its mean off-zero convolution is (M_D^2-Q_D)/(q-1), and nonnegativity gives

    M_D^2-Q_D <= (q-1)C0.

For an exactly constant core p=L*1_D, write theta=sL^2/V. The restriction becomes s<=1+(q-1)C0/(theta*V). In a sequence with t=o(sqrt(q)), s tending to infinity, and theta bounded below, this gives s<=(4+o(1))*t^2/theta. It allows s^2/q of logarithmic size when t=q^(1/4) times logarithms. Integer/parity fluctuations of order one then have small relative size; no power gain follows from this scalar restriction. No Boolean realization with small t is asserted. The exact realization problem is the nonnegative completion u satisfying 2p*u+u*u=C0-p*p at EVERY off-zero displacement, with the fixed zero equation and trace; replacing this by independent residual variables would lose the shared translates of u.

## Strategic review after the two mechanisms

HEURISTIC decision, based on the proved obstruction. Discontinue a single maximum-relative core D={h>=L/2} as the sole adaptive test set: its sumset can miss almost all the Parseval energy even when every equation on that sumset holds. Discontinue the proposed bounded-character concentration conclusion: the one-sided condition proves the opposite quantitative direction. Continue to test a Parseval-carrying adaptive threshold, and retain the nonlinear Boolean constraint in the multiplicative variables. These are specific changes, rather than an inference that all full-equation methods fail.

PROVED next threshold and its test. In the small branch t^2<(q-1)/4, let

    A={a:h(a)>=V/(2qt)}.

Then 0 is outside A, sum_A h^2>=V/2, |A|<=2(qt)^2/V, and |A|>=V/(2L^2). Indeed the complement has energy at most [V/(2qt)]sum h=V/2, and the two cardinality bounds use mass and the maximum respectively. Applying all equations on A+A to the new fake detects the omitted displacement 100m: the upper repair run belongs to A for large q, and adjacent upper repair sites differ by 100m. The repair heights divided by E0/T tend to (2/3)(1+/-1/sqrt(2)), while the threshold divided by E0/T tends to 1/2. Thus the upper run lies in A and its length tends to infinity. Symmetry gives A-A=A+A, so the missing displacement really belongs to the newly selected sumset.

PROVED limitation of this follow-up. Combining these size estimates with L^2<=C0 still gives only the quarter exponent. Its purpose is to choose equations that actually see the bulk obstruction. A proof still needs a gain from the shared completion equations beyond these cardinality inequalities.

## Gauss phase moment and product bounds: exact use and obstruction

PROVED, quoted external inputs. For any prime q, nontrivial multiplicative chi has |tau(chi)|=sqrt(q), with tau(1)=-1. If eta has order r dividing q-1, the Hasse–Davenport product formula, in the convention tau(1)=-1, is

    product_{j=0}^{r-1} tau(chi*eta^j)
      = chi(r)^(-r) * tau(chi^r) * product_{j=1}^{r-1} tau(eta^j).

We use its nonexceptional range chi^r!=1. The Gauss/Jacobi relation is tau(psi)tau(phi)=J(psi,phi)tau(psi*phi) when psi*phi!=1. These precise conventions are checked against [Keith Conrad, Gauss and Jacobi sums, Theorem 2.2 and Appendix A, (A.5)–(A.6)](https://kconrad.math.uconn.edu/blurbs/gradnumthy/Gauss-Jacobi-sums.pdf).

PROVED specialized phase relation. For q=1 mod 4 and eta the quadratic character, theta_eta=1, so for every even chi with chi^2!=1,

    theta_chi * theta_(chi*eta) = conj(chi(4)) * theta_(chi^2).

This is a genuine relation among multiplicative phases; no independence assumption on them is made.

PROVED, quoted deep bound in an explicit normalization. Put

    S_k(b)=sum_{x_1*...*x_k=b, all x_i!=0} e((x_1+...+x_k)/q).

For every integer k>=1, prime q, and b!=0, Deligne's hyper-Kloosterman bound is |S_k(b)|<=k*q^((k-1)/2). The k=1 case is immediate; the quoted general result is [Kowalski, The Second Moment Theory of Families of L-functions, Proposition 3.1, with (3.2)–(3.4)](https://people.math.ethz.ch/~kowalski/moment-theory.pdf).

PROVED application by character orthogonality, with the principal term retained. For every a!=0,

    (1/n)*sum_{chi even} theta_chi^k * chi(a)
       = q^(-k/2)[S_k(a^(-1))+S_k(-a^(-1))],
    absolute value <= 2k/sqrt(q).

Here theta_1=-1/sqrt(q), so deleting the principal character changes the normalized sum by at most q^(-k/2)/n. This is an unweighted or single-character-twisted phase estimate; it is not an estimate with arbitrary Boolean-dependent weights.

PROVED exact Boolean weighted constraint. Write u_chi=hat X(chi) and set u_1=0. For every nontrivial chi, F^2=1/4 gives

    sum_{psi!=1,psi!=chi} conj(J(psi,chi/psi))
           * u_conj(psi) * u_conj(chi/psi) = 0.

Indeed hat F(psi)=conj(theta_psi)*u_conj(psi), and the Gauss/Jacobi relation removes a common nonzero factor conj(theta_chi)/sqrt(q). At chi=1 the equation is sum |u_psi|^2=1/4. These quadratic equations for all chi, together with the reality conditions, recover the coefficientwise Boolean plateau. Triangle inequality only gives at most sqrt(q)/4 for the magnitude of the displayed sum; it discards the exact cancellation and gives no power gain.

PROVED why the quoted phase bounds do not complete the argument. In general, a bound for every sum of fixed phases against a single character does not bound a sum against weights chosen from those phases. Already weights w_chi=conj(theta_chi^k) on the nontrivial characters make sum theta_chi^k*w_chi=n-1. This algebraic counterexample is not claimed to arise from a half-set; it identifies the missing hypothesis in any use of unweighted equidistribution. Hasse–Davenport changes the character indices and phases, but neither bounds these data-dependent quadratic weights nor forces a small support. Also, the operator on F is an involution: U^2=I on the mean-zero space. Its powers are not multiplication by theta_chi^k, because each application reverses the character index. Iterating U therefore cannot be justified as repeated independent phase mixing using Deligne's moment bound.

PROVED precise fake distinction. Every real even prime-cyclic array, including the R12-S/R13-C/R13-M2 relaxations when placed at prime q, has the same Mellin/Gauss transform, the same fixed Gauss phases, and the same Hasse–Davenport and unweighted Deligne relations. Trace and Parseval also give the centered weighted physical function mean zero and mean square 1/4. What those fakes lack is F(x)^2=1/4 at every x in G, equivalently the full family of weighted quadratic phase equations just displayed. The interplay of the two transforms alone does not reject them. The round-16 fake fails the same Boolean hypothesis, as witnessed both by its equation at 100m and by the finite Arb values of h-inverse(1), far outside +/-1/2.

## Third mechanism checked: sign uncertainty with the Boolean plateau

PROVED, quoted exact statement. For any odd order Q>=3, any nonzero real even v on Z_Q, and sign sigma in {+1,-1}, if sigma*v(0)<=0 and its unitary Fourier transform vhat satisfies vhat(0)<=0, then

    #{x:v(x)<0} * #{a:sigma*vhat(a)<0} >= Q/16.

This is [Goncalves–Oliveira e Silva–Ramos, New Sign Uncertainty Principles, Theorem 3.1](https://arxiv.org/pdf/2003.10771), in the paper's unitary discrete Fourier normalization. The theorem applies to all odd orders, so it does not use primeness.

PROVED application retaining the actual Boolean plateau. Let v(0)=0 and v(x)=b(x)-1/2 off zero. Then vhat(0)=0 and vhat(a)=(h(a)-t)/sqrt(q) for every a. The negative set of v has size (q-1)/2. Applying the theorem with either sign gives only that the negative and positive sets of vhat each have size at least q/[8(q-1)] (and hence are nonempty; evenness supplies pairs). The estimate contains no magnitude t and yields no WRS power. Shifting to the 0/1 plateau changes the origin/mean hypotheses; those hypotheses cannot be dropped. This tests the stated theorem, without claiming that all strengthened sign-uncertainty principles are impossible.

## Adversarial audit and verification record

NUMERICAL, with exact finite input sets. `adversaries.py` reconstructed every genuine pair-list case in `examples/r15_certificates/stability_probe.json`, including the selected small-q enumeration outputs, E41 lists from `examples/zp_half/`, E90 candidate lists from `examples/e90/`, and Paley. It regenerated the R13-PK and R14-UNION repaired half-sets with the prior seed 151019. All 23 genuine cases were checked against the simultaneous decomposition, weighted-energy bound, exact smoothing variance, Mellin/Gauss identity, Boolean quadratic Mellin identity, Hasse–Davenport duplication, and all character twists of phase moments k=1,...,6. The largest genuine core-sum convolution relative error was 3.11e-15. These floating checks are not new certificates of optimality, global minima, or infinite-family statements.

NUMERICAL selected genuine cases. The energy fraction is sum_D h^2/V; the effective Mellin count is (sum |hat F|^2)^2/sum |hat F|^4. The latter is PROVED to be at least q/(4t^2) by the coefficient bound and Parseval, as is the literal support count.

| Family | q | core size | core energy fraction | epsilon=t/sqrt(q) | max Mellin coefficient | effective Mellin count |
|---|---:|---:|---:|---:|---:|---:|
| selected small-q candidate | 37 | 2 | 0.569757 | 0.471367 | 0.166667 | 14.878 |
| E41 stored list | 61 | 12 | 0.869588 | 0.458590 | 0.214896 | 7.353 |
| E41 stored list | 89 | 14 | 0.794709 | 0.437787 | 0.157594 | 20.015 |
| E90 stored candidate | 149 | 2 | 0.367248 | 0.472177 | 0.111999 | 44.707 |
| E90 stored candidate | 601 | 2 | 0.271643 | 0.557036 | 0.072835 | 163.422 |
| Paley | 65537 | 32768 | 0.999992 | 0.500000 | 0.500000 | 1.000 |
| repaired R13-PK profile | 65537 | 2 | 0.006098 | 1.918815 | 0.008448 | 16527.115 |
| repaired R14-UNION profile | 65537 | 4 | 0.001674 | 2.147220 | 0.010866 | 12321.677 |

NUMERICAL scope of the last two rows: their epsilon is large, so they test unqualified intermediate assertions rather than the small-epsilon conclusion of WRS. They confirm that a small maximum-relative core can have very little energy even for genuine half-sets. The new obstruction theorem supplies the small-epsilon relaxation analogue.

| Adversary | Status and test | Exact missing hypothesis / outcome |
|---|---|---|
| Paley | PROVED formulas above; NUMERICAL q=257,4093,65537 | Survives every stated inequality; shows uniform r_D and a one-character Mellin spectrum can occur at epsilon=1/2 |
| Stored optima/candidates | NUMERICAL 16 pair-list inputs, q<=1601, plus the 3 Paley cases | Survive all new inequalities; optimality is not re-certified |
| R13-PK and R14-UNION profiles | NUMERICAL 4 repaired genuine half-sets, q=4093,65537 | Survive the identities; outside the asymptotic small-epsilon branch |
| R12-S | NUMERICAL q=1000033 reconstructed from its scalar formulas | Passes linear Gauss transformation, coefficient bound and Hasse–Davenport; violates Boolean plateau and core-sum flatness |
| Round-15 B3 scalar counterexample | NUMERICAL reconstruction of the stored exact rational input q=1000033, K=32, r=30000, s=3720 | Same distinction; weak positive modes cannot be silently discarded |
| R13-C | PROVED prior prime-family construction quoted from P65; prior finite certificate at composite q=201^3 is quoted, not treated as a prime | Preserves its assigned segment; fails a bulk displacement. New theorem replaces the segment by the whole actual growing core sumset and changes the scale to q^(1/4)*log q |
| R13-M2 | PROVED prior fixed-order repair quoted from P65 | Scalar arithmetic repair does not impose coefficientwise Booleanity or the full weighted quadratic Mellin system; no new numerical instance is claimed |
| Round-16 adaptive fake | PROVED infinite-family paper construction and independent exact/Arb finite checks | Passes all equations on its true D+D and the linear multiplicative tests; violates the explicit equation at 100m |

NUMERICAL fake diagnostics, in the current normalization. For R12-S the maximum relative core-sum convolution error is about 102.02, and for B3 it is about 251.89. Their maximum multiplicative Boolean quadratic residuals are respectively 0.18293 and 0.13738, while the linear Gauss transform residual is below 4.45e-16 across all cases. Hasse–Davenport's worst floating residual, including the million-point fake cases, is 8.39e-11. This cleanly distinguishes a true Boolean test from a transform identity that every real even array satisfies.

PROVED independent finite check. `verify_round16.py` does not import the fake constructor. It scans sorted explicit support sites through short difference windows, checks every required convolution as an EXACT rational polynomial in squared level variables, and separately reconstructs the mass/energy repair and capacity using 256-bit Arb. It verified all three finite instances, including the 7,604,369-site compressed support. The omitted-displacement repair-only lower bounds divided by q^2 are respectively >0.24987, >0.24973, and >0.24977. Source and results: `verify_round16.py`, `verification.json`, `verification.log`.

## Task 2 — density and integer corollary

PROVED limitation, with no new integer conclusion. Density one half was used in the exact two-valued plateau b(x)-1/2=+/-1/2 off zero, which makes its square constant and gives the flat convolution equation; it was also used to make the quotient function f have mean 1/2, so F=f-1/2 has both mean zero and F^2=1/4. At general density alpha=|B|/q, removing the two principal terms from lambda*lambda=q*lambda leaves sum_{beta outside {0,xi}}lambda(beta)lambda(xi-beta)=(1-2alpha)q*lambda(xi), precisely P67's extra term. The constant-flatness and balanced-Boolean phase equations above therefore do not transfer unchanged, and the obstruction construction proves no lower bound at any density. A future integer embedding would require constants uniform for alpha in [1/(4C),1/2], using primes q in (4X,8X]; no such uniform theorem or new integer corollary is asserted.

## Novelty boundary and final strategic recommendation

PROVED source/novelty audit relative to the project record. Before calling any result new, searched PROOFS.md for adaptive sumsets, energy-carrying sets, Mellin/anti-concentration, Gauss sums and Davenport. The new project artifacts are the quarter-scale fake with exact flatness on the full sumset of its actual growing heavy core, its explicit bulk defect, the simultaneous smoothing/variance formulation, and the normalized Mellin anti-concentration/Boolean-phase audit. The separated-cluster mass/energy repair method itself is adapted from R13-C; the exact flat model, endpoint defects, R13-M2, and all external Gauss-sum and uncertainty theorems are quoted. No external priority claim is made.

PROVED literature scope checked directly. [Sanders, 0807.5104v2, Theorem 1.2 and its following sentence](https://arxiv.org/pdf/0807.5104) gives a polynomial half-set lower bound and states that accounting yields exponent 1/3, for symmetric sets of size (q+1)/2. Adding zero to our B shifts each nonprincipal eigenvalue by 1, so this applies to the present half-set convention with an additive constant change. It is not a stated pointwise WRS peak estimate. [Jin–Milojevic–Tomon–Zhang, 2509.03490v2, Theorem A.1](https://arxiv.org/html/2509.03490v2#A1) says that, for each delta>0 and 0<gamma<1/4, sufficiently large finite groups with inverse-closed A and M(A)<=|G|^gamma have A within delta|G| of a subgroup; the quantitative second conclusion uses gamma<1/6. Neither quoted statement is presented here as a proof of WRS. This round claims no improved cyclic exponent.

HEURISTIC final decision: PIVOT within the full-Boolean program, away from the sole maximum-relative core and toward adaptive sets that carry a fixed fraction of Parseval energy. The first concrete next derivation is to exploit all equations on A+A for A={h>=V/(2qt)}, retaining the shared nonnegative completion u and its equations outside A+A. This specific A already rejects the new fake through its long upper repair run. In the multiplicative formulation the useful open target is a bound for the Boolean-dependent Jacobi-weighted quadratic sums, with the lower support requirement q/(4t^2) retained; bounded-character concentration and unweighted phase equidistribution cannot supply it as used here. If that strengthened adaptive program again reduces to scalar size bounds, pivot to the integer taper/CSFG mechanism, whose hard support boundary is absent in these cyclic relaxations. WRS remains open in this round; the requested precise-obstruction alternative is delivered.

PROVED reproducibility and honesty scope. All mathematical computations were run on the designated VM through DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4, with bash command shells. Python 3.12.3, NumPy 2.5.4, SymPy 1.14.0, and python-flint/Arb were used; no optimizer was invoked. There were no subagents or commits, and no top-level .research/*.md files were edited. New work is confined to this report and the designated scratch directory. The infinite-family theorem is a paper proof; the finite support identities use rational arithmetic and Arb; the genuine-set diagnostics are NUMERICAL. Nothing is kernel-checked, and no unattended continuation is implied.
