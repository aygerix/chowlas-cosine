# Exact five-count test for a movable odd polynomial plane

2026-10-23. Candidate and falsification protocol written before the
bounded computation. All averages are normalized circle averages;
F=sum_(a in A)z^a, f=Re F, D=2f, n=|A|. No GPU work.

## Candidate mechanism and implication

This plane is {Im F,Im F²}, rather than a scalar polynomial in D or
the reciprocal plane P2. Put

    t=<F,F²>, E4=||F²||2², B=<F³,F²>, C=<F,F⁴>, C5=2B-C.

All five quantities are finite exact integer additive counts. Its
norm and D-energy matrices are respectively

    Q=(1/2)*[[n,t],[t,E4]], E=(1/2)*[[t,E4],[E4,C5]].

The cross identity is D*Im F=Im F². The last diagonal follows from
(Im F²)²=(|F|⁴-Re F⁴)/2. Thus a nonpositive direction exists exactly
when t*C5<=E4² (t=0 already gives an indefinite energy matrix).

The precise candidate is stronger: there is an absolute theta<1
such that t*C5<=theta*E4² for every Boolean actual-lowM support.
For t>0, q=Im F²-(E4/t)Im F has energy at most
-(1-theta)*E4²/(2t), and norm at most
(E4+E4²*n/t²)/2 <= E4²*n/t², using t²<=n*E4.
Consequently its Rayleigh quotient is at most
-(1-theta)*t/(2n). The high-triple branch t>=n^(3/2) would then
give M>=((1-theta)/4)*sqrt(n). The complementary cubic branch has
an existing square-root certificate. This is a sufficient mechanism,
not a proved count inequality.

First falsification test: exact counts on the already all-circle-lowM
projection n56,n306 and coherent-prefix n337 supports. Independently
rebuild both matrices by signed Laurent convolution. If any has
t*C5>E4², stop this universal phase-plane candidate immediately.
Only otherwise enumerate subsets of [1,16] until a falsifier or the
declared finite exhaustion. No reciprocal optimization, larger minimum
search, new global-M certificate, or GPU throughput test is needed.

Source: src/cstar_phase_five_count.py. Results:
experiments/phase_five_count_2026-10-23/results.json.

## Outcome: refuted inside actual lowM

All three predeclared supports have strictly positive energy matrices:

| Support | t*C5/E4² | 4*det(E) |
|---|---|---:|
| projection n56 | 4403870565/3991532552 | 824676026 |
| projection n306 | 202384475200231/174820913784196 | 27563561416035 |
| coherent-prefix n337 | 450929716891995/397811681177089 | 53118035714906 |

Both matrices independently match signed Laurent convolution exactly.
Their actual-lowM premises come from the existing all-circle saved
certificates, not a new sampled minimum. The finite counterexamples
refute even theta=1. The [advisor](advisor_P2_boolean_2026-10-23.md)
independently checks the n56 integer matrix. The optional small-support
enumeration was not run, because the declared falsification already
succeeded. The VM job completed normally; shared Dirichlet is untouched.

The polynomial phase-plane route is retired. The failure motivates a
broader [fixed-degree phase-polynomial obstruction](cstar_phase_polynomial_obstruction_2026-10-23.md),
not an expansion of successful controls. Reciprocal and unrestricted
signed witnesses remain available; no universal bound was proved.
