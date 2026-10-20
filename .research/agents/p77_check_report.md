# Adversarial verification of P77

Scope: the P77 text in `.research/PROOFS.md`, E116/E117 in `.research/EXPERIMENTS.md`, and the three source files named in the brief. No new research was undertaken. All numerical mathematical computation was run on dirichlet (`34.148.157.169`) through `src/dirun.sh -c 2 -t 3600`. No source/proof/experiment file was edited, and no commit was made.

## Verdict

**GAP in the literal statement; CORRECT proof and constants after the following routine repairs.** No algebraic error was found in (a), the energy bound or its consequence in (b), or (c).

1. Require **nonempty D and B**. Otherwise Z4 or |B| in the denominators can vanish, and the top eigenvalue on an empty odd space is undefined.
2. For the concentration operator in (b), require **B = -B** (equivalently N = -N), or explicitly define lambda_odd using the **compression/quadratic form on odd real functions**. An arbitrary B allowed by the current statement need not be symmetric; then the displayed C does not in general map odd real functions into themselves, so its claimed restriction has no top eigenvalue as stated. The actual E117 background set is symmetric and has no such problem.
3. In (a), handle **A2 = 0** before choosing weights. Then the claimed bound is simply K(T) >= r', already obtained by evaluating at any chi/n with chi in B. If A2 > 0, S1 and S2 are positive and the displayed optimisation is valid.
4. The Taylor averaging weights must be nonnegative. This is implicit in “weights” and is satisfied by the chosen weights; state it explicitly if arbitrary weights are introduced.

**Numerical verdict:** RUNNING; the completed table and diagnostics will replace this sentence.

## Exact statement checked and hypotheses

Write e(x) = exp(2 pi i x), and use unnormalised finite Fourier transforms and the counting inner product. For a nonempty symmetric D contained in Z_n^2 minus {0}, an odd one-representative lift is a function z: D -> Z^2 with z(-g) = -z(g) and z(g) congruent to g modulo n. Put
F(xi) = sum_D cos(2 pi z(g).xi), K = -min F,
W(chi) = sum_D z(g) sin(2 pi chi.g/n),
A2 = sum_B |W(chi)|^2, and Z4 = (sum_D |z(g)|^4)^(1/2).
For a nonempty B contained in {chi != 0: Dhat(chi) <= -r'}, the checked assertions are

- (a) K >= r' + A2/(8 n sqrt(|B|) Z4).
- (b) A2 >= (1-lambda_odd) n^2 sum_D |z(g)|^2; hence
  K >= r' + (1-lambda_odd) sum_D |z(g)|^2/(8 Z4).
- (c) If V > 0, |z(g)| <= sqrt(2) V n and sum_D |z(g)|^2 >= beta |D| n^2, then
  K >= r' + (1-lambda_odd) beta sqrt(|D|)/(16 V^2).

In (b) and (c), lambda_odd is the stated operator eigenvalue when B is symmetric, or the top eigenvalue of its compression if that convention is explicitly adopted.

**Injectivity: CORRECT, automatic.** If z(g) = z(h), reducing modulo n gives g = h. Distinct residue labels already suffice for the finite Parseval calculation. There is no separate missing injectivity hypothesis.

**D symmetry: CORRECT, already stated.** It permits the odd coordinate fields used in (b). Part (a) itself only needs the residue-indexed sum and the stated background inequalities.

**Odd n: not required.** Existence of a nonempty odd lift requires that D contain no nonzero g with 2g = 0: oddness would force z(g) = -z(g), hence z(g) = 0, contradicting its residue. Odd n guarantees this automatically; even n is allowed when D avoids these classes. For example, D = {+(1,0), -(1,0)} modulo 4 has an odd lift. For n = 2 there is no nonempty admissible D. This is an existence restriction already implied by “odd map”, not a hidden need for n odd in the calculations.

There is no need to assume r' > 0 for the algebra. If r' > 0 is intended as a useful background level, it is an optional stronger hypothesis. For nonempty D as above, Z4 > 0.

## Line-by-line audit of (a)

| Step | Verdict | Verification |
|---|---|---|
| Exponential identity | CORRECT | Write z(g) = g + n k(g). Then e(z(g).chi/n) = e(g.chi/n) because k(g).chi is an integer. Multiplying by e(z(g).alpha/n) proves the identity for every real vector alpha and every character chi. |
| Choose u_chi in {+e1,-e1,+e2,-e2} | CORRECT | Choose a coordinate achieving max(|W1|,|W2|) and its sign. Then u_chi.W = |W|_infinity >= 0. Zero vectors allow any direction. Freeze these choices before varying t. |
| h_chi(0) = Dhat(chi) <= -r' | CORRECT | The residue identity removes integer multiples of 2 pi. |
| First derivative | CORRECT | Differentiating each cosine yields h'_chi(0) = -(2 pi/n) sum_g (z(g).u_chi) sin(2 pi chi.g/n) = -(2 pi/n)|W(chi)|_infinity. |
| Second derivative and Q | CORRECT | A second derivative gives -(4 pi^2/n^2) sum_g (z(g).u)^2 cos(2 pi(chi.g+t z(g).u)/n), exactly -(4 pi^2/n^2) Re Q_u(chi,t). |
| Fixed-u, fixed-t Parseval | CORRECT | Define a_g = (z(g).u)^2 e(t z(g).u/n) on D and zero elsewhere. Orthogonality over all n^2 characters gives sum_chi |Q_u|^2 = n^2 sum_g |a_g|^2 = n^2 sum_g (z(g).u)^4 <= n^2 Z4^2. The t-dependent phase has modulus one. No averaging over t or changing u inside this application is allowed or needed. |
| Cauchy-Schwarz on B_u | CORRECT | For nonnegative omega, sum_{B_u} omega_chi |Q_u| <= ||omega restricted to B_u||_2 (sum_{B_u}|Q_u|^2)^(1/2) <= n Z4 ||omega restricted to B_u||_2. |
| Cauchy-Schwarz over four directions | CORRECT | The B_u partition B, so sum_u ||omega restricted to B_u||_2 <= sqrt(4) (sum_u ||omega restricted to B_u||_2^2)^(1/2) = 2 ||omega||_2. The two signs of a direction may be treated separately; this merely uses a valid, possibly loose bound. Thus sum_B omega |h''_chi(t)| <= (8 pi^2/n) Z4 ||omega||_2 for every t. |
| Taylor remainder | CORRECT | For rho >= 0, h(rho) = h(0)+rho h'(0)+integral_0^rho (rho-t)h''(t) dt. The integral of (rho-t) is rho^2/2, giving the displayed +(4 pi^2 rho^2/n) Z4 ||omega||_2. Smooth periodicity puts no upper restriction on rho. |
| min F <= sum omega h_chi(rho) | CORRECT | Every h_chi(rho) is a value of F. A convex combination of these values is at least min F. |
| omega_chi = |W|_infinity/S1 | GAP at S1 = 0; CORRECT otherwise | The displayed formula is undefined when A2 = 0. In that case evaluate F at a background character to prove K >= r'. If A2 > 0 then S1,S2 > 0, the weights are nonnegative and sum to one, sum omega |W|_infinity = S2/S1, and ||omega||_2 = sqrt(S2)/S1. |
| Optimisation in rho | CORRECT | The optimum is rho_* = sqrt(S2)/(4 pi Z4), and the decrement is S2^(3/2)/(4 n S1 Z4). The factor 1/n in the quadratic coefficient is essential and is used correctly. |
| S1 <= sqrt(|B| S2) | CORRECT | Cauchy-Schwarz applied to the vector of |W|_infinity values and the all-ones vector. |
| S2 >= A2/2 | CORRECT | For W in R^2, |W|_infinity^2 >= |W|^2/2, pointwise. |
| Final constant 1/8 | CORRECT | S2^(3/2)/(4 n S1 Z4) >= S2/(4 n sqrt(|B|) Z4) >= A2/(8 n sqrt(|B|) Z4). |

For clarity, the quadratic being minimised is
-r' - a rho + b rho^2, where
a = (2 pi/n) S2/S1 and b = (4 pi^2/n) Z4 sqrt(S2)/S1.
Thus a/(2b) = sqrt(S2)/(4 pi Z4), and a^2/(4b) is exactly the stated decrement.

## Line-by-line audit of (b)

| Step | Verdict | Verification |
|---|---|---|
| f_k = z_k 1_D is odd and real | CORRECT | Extend by zero outside symmetric D. The oddness of z makes f_k(-g) = -f_k(g). |
| Odd real f has purely imaginary transform | CORRECT | The real part is sum f(g) cos(2 pi chi.g/n), which cancels under g -> -g. The imaginary part is the sine sum. At self-inverse classes f vanishes, so the argument also works for even n. |
| fhat_k = i W_k | CORRECT with the positive-exponent forward convention | If fhat(chi) = sum f(g)e(+chi.g/n), this is literally +i W_k and the inverse uses negative characters. With NumPy's negative-exponent FFT it is -i W_k. The sign convention has no effect on any norm, Parseval identity, projection, or conclusion. |
| sum_chi |W|^2 = n^2 sum_g |z(g)|^2 | CORRECT | Apply unnormalised finite Parseval to each f_k, use |fhat_k|^2 = |W_k|^2, and sum over the two coordinates. There is no factor 1/2 from using sine: the odd field and both members of every +/-pair are already included. |
| W(0) = 0 | CORRECT | Every summand contains sin(0). Oddness is not needed for this particular identity. In fact W also vanishes at each self-inverse character. Including 0 in N contributes no energy. |
| C is an operator on odd real functions | GAP unless B is symmetric or compression is defined | The current statement permits nonsymmetric B. Then P_N need not preserve reality or oddness. A restriction to the asserted real odd space is not defined in general. See the explicit example below. |
| Concentration identity | CORRECT | For any supported f, unnormalised Fourier orthogonality gives sum_N |fhat|^2 = n^2 <f,1_D P_N 1_D f>. This identity remains true with the usual complex inner product even if N is not symmetric. |
| Rayleigh/eigenvalue upper bound | CORRECT with the repaired operator definition | For symmetric N, C is self-adjoint, positive semidefinite, maps odd real functions to themselves, and is a contraction. Hence 0 <= lambda_odd <= 1 and <f_k,C f_k> <= lambda_odd ||f_k||_2^2. The same variational inequality holds for the explicitly defined compression when N is not symmetric. |
| Subtract the N energy | CORRECT | B and N partition all characters, so A2 = n^2 sum|z|^2 - sum_N |W|^2 >= (1-lambda_odd)n^2 sum|z|^2. |
| Derived K bound | CORRECT | Substitute this into (a), giving the stronger increment (1-lambda_odd)n sum|z|^2/(8 sqrt(|B|) Z4). Since sqrt(|B|) <= n and 1-lambda_odd >= 0, this implies the displayed weaker bound. |

**Explicit demonstration of the symmetry gap.** Let n = 3,
D = {(1,0),(2,0)}, f(1,0) = 1, f(2,0) = -1, and take
B = {(1,0)}, r' = 1. This B satisfies the current statement because Dhat(1,0) = -1.
With the negative-exponent forward Fourier convention and positive-exponent inverse,
C f(1,0) = 5/6 - i sqrt(3)/18 and C f(2,0) = -5/6 - i sqrt(3)/18.
Thus C f is neither real nor odd. A “top eigenvalue of C on odd real functions” is not defined by restriction here.

An adequate alternative repair is to let H be the odd real subspace and define lambda_odd as the supremum of <f,Cf>/||f||^2 over nonzero f in H, equivalently the largest eigenvalue of the real symmetric quadratic-form compression to H. Its kernel uses the cosine/symmetrised part of N, and the proof then works for arbitrary B. This is a clarification of the quantity in the given argument, not a new estimate. Adding B = -B is the simpler repair for the E117 application.

**E117 matrix normalisation: CORRECT.** For one h from each +/-pair, use the orthonormal odd basis b_h = (delta_h-delta_-h)/sqrt(2). If c_N(x) = n^-2 sum_{chi in N} cos(2 pi chi.x/n), then
<b_g,Cb_h> = c_N(g-h)-c_N(g+h).
This is precisely the E117 code; the missing-looking factor of two is already accounted for by the basis normalisation. Equivalently the matrix is (2/n^2) S_N^T S_N, where (S_N)_{chi,h} = sin(2 pi chi.h/n). Both constructions were compared in the VM run. E117's B is the entire minimum/background level, so B and N are symmetric.

## Audit of (c)

**CORRECT after the hypotheses above.** The spread condition gives
|z(g)|^4 <= (sqrt(2) V n)^4 = 4 V^4 n^4, so
Z4 <= 2 V^2 n^2 sqrt(|D|).
Using sum|z(g)|^2 >= beta |D| n^2 in the bound in (b) gives
(1-lambda_odd) beta |D| n^2 /
(8 * 2 V^2 n^2 sqrt(|D|))
= (1-lambda_odd) beta sqrt(|D|)/(16 V^2).
The factor 16, the power V^2, and cancellation of n^2 are all correct.

## Triangular PD taper remark

**CORRECT** for Lambda(t) = max(1-|t|,0), with the sums over all lattice representatives of the specified class.

First work in one dimension with a in {0,...,n-1}. The only representatives with positive weight are a and a-n, with weights 1-a/n and a/n; at a = 0 the latter has weight zero, and the representative 0 has weight one. Therefore
sum_{z congruent to a} Lambda(z/n) = (1-a/n)+a/n = 1,
and
sum_{z congruent to a} Lambda(z/n) z
= a(1-a/n)+(a-n)(a/n) = 0.
Endpoint representatives +/-n have weight zero and cause no exception.

For g = (a,b), the two-dimensional weight is a product. Its mass factors as 1*1 = 1. The first-coordinate moment factors as the one-dimensional first moment in a times the one-dimensional mass in b, hence 0; the second coordinate is identical with the roles exchanged. Consequently
sum_{z congruent to g} tau(z) = 1 and
sum_{z congruent to g} tau(z) z = (0,0)
for **every** class, including zero and coordinate-axis classes. The first-order contribution from these weighted class centroids is therefore identically zero. This identity does not require n odd or a special D.

## Numerical falsification

NUMERICAL_RESULTS_PENDING

## Reproduction

The exact script executed on the VM is below. It imports the unmodified `true_min` and calls it with its default FFT resolution and default 12 BFGS starts; L is the actual maximum coordinate magnitude of the particular lift. No minima or eigenvalues are interval-certified. A negative numerical result only applies to the sampled lifts.

To run directly from this report without creating another repository file:

```sh
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 2 -t 3600 python -B -c "$(python3 -c 'from pathlib import Path; t=Path(".research/agents/p77_check_report.md").read_text(); print(t.split("```python\n",1)[1].split("\n```",1)[0])')"
```

Here the local Python command only extracts source text; all numerical computation is performed by Python on the VM. The script writes per-trial data only to /tmp on the VM, outside the repository. Seeds and source hashes below permit reconstruction if that temporary file is removed.

```python
import sys, os, json, time, math, platform, hashlib
sys.dont_write_bytecode = True
sys.path.insert(0, "src")
import numpy as np
import scipy
from e114_cp_group import jl_set
from e116_jl_taper import true_min, Fval, lift

COUNT = 200
BASE_SEED = 770019
RAW = "/tmp/p77_check_770019.jsonl"
T0 = time.time()
raw = open(RAW, "w")
def emit(x):
    print(json.dumps(x, sort_keys=True), flush=True)
def record(x):
    raw.write(json.dumps(x, sort_keys=True) + "\n")
    raw.flush()
def neg(g, n):
    return ((-g[0]) % n, (-g[1]) % n)
def setup(label, D, n):
    assert (0, 0) not in D and D and {neg(g, n) for g in D} == D
    half = np.array([g for g in sorted(D) if g < neg(g, n)], dtype=np.int64)
    assert 2 * len(half) == len(D)
    arr = np.zeros((n, n))
    for g in D:
        arr[g] = 1
    dhc = np.fft.fft2(arr)
    assert np.max(np.abs(dhc.imag)) < 1e-9
    dh = dhc.real
    B = dh < -1e-9
    B[0, 0] = False
    rev = (-np.arange(n)) % n
    assert np.array_equal(B, B[np.ix_(rev, rev)]) and B.any()
    rp = -float(dh[B].max())
    N = ~B
    cN = np.fft.fft2(N.astype(float)).real / n**2
    dm = (half[:, None, :] - half[None, :, :]) % n
    dp = (half[:, None, :] + half[None, :, :]) % n
    Codd = cN[dm[..., 0], dm[..., 1]] - cN[dp[..., 0], dp[..., 1]]
    lam = float(np.linalg.eigvalsh(Codd)[-1])
    chisN = np.argwhere(N)
    sine = np.sin(2 * np.pi * (chisN @ half.T) / n)
    Ccheck = 2 * sine.T @ sine / n**2
    c_error = float(np.max(np.abs(Codd - Ccheck)))
    assert c_error < 1e-10 and -1e-10 <= lam <= 1 + 1e-10
    data = dict(label=label, n=n, D=len(D), B=int(B.sum()), rprime=rp,
                lambda_odd=lam, concentration_matrix_maxerr=c_error,
                D_sha256=hashlib.sha256(repr(sorted(D)).encode()).hexdigest())
    emit(dict(type="SETUP", **data))
    return half, B, rp, lam, data

def one(half, B, rp, lam, n, pairs, V, full_check=False):
    assert np.array_equal(pairs % n, half)
    assert np.max(np.abs(pairs)) <= V * n
    field = np.zeros((n, n, 2))
    field[half[:, 0], half[:, 1]] = pairs
    minus = (-half) % n
    field[minus[:, 0], minus[:, 1]] = -pairs
    ft = np.fft.fft2(field, axes=(0, 1))
    W = -ft.imag
    z2 = np.sum(pairs.astype(float)**2, axis=1)
    sumz2 = 2 * float(z2.sum())
    Z4 = math.sqrt(2 * float(np.dot(z2, z2)))
    total = float((W**2).sum())
    A2 = float((W[B]**2).sum())
    pars_err = abs(total / (n**2 * sumz2) - 1)
    phi = float((W[~B]**2).sum() / total)
    a2_lower = (1 - lam) * n**2 * sumz2
    rhs_a = rp + A2 / (8 * n * math.sqrt(int(B.sum())) * Z4)
    rhs_b = rp + (1 - lam) * sumz2 / (8 * Z4)
    beta = sumz2 / (len(half) * 2 * n**2)
    rhs_c = rp + (1 - lam) * beta * math.sqrt(2 * len(half)) / (16 * V**2)
    direct_error = 0.0
    q_pars_error = 0.0
    if full_check:
        chars = np.indices((n, n)).reshape(2, -1).T
        wd = 2 * np.sin(2 * np.pi * (chars @ half.T) / n) @ pairs
        direct_error = float(np.max(np.abs(wd - W.reshape(-1, 2))))
        for u in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            udot = field[..., 0] * u[0] + field[..., 1] * u[1]
            coeff = np.exp(2j * np.pi * 0.137 * udot / n) * udot**2
            Q = n**2 * np.fft.ifft2(coeff)
            target = n**2 * float((udot**4).sum())
            if target:
                q_pars_error = max(q_pars_error, abs(float((abs(Q)**2).sum()) / target - 1))
    L = int(np.max(np.abs(pairs)))
    fmin, xi, grid, G = true_min(pairs, np.ones(len(pairs)), L)
    K = -fmin
    witness_K = -float(Fval(pairs, np.ones(len(pairs)), xi)[0])
    out = dict(K=K, rhs_a=rhs_a, rhs_b=rhs_b, rhs_c=rhs_c,
               margin_a=K-rhs_a, margin_b=K-rhs_b, margin_c=K-rhs_c,
               A2=A2, A2_lower=a2_lower, A2_margin=A2-a2_lower,
               phi=phi, G=G, L=L, parseval_relerr=pars_err,
               direct_W_maxerr=direct_error, Q_parseval_relerr=q_pars_error,
               Fourier_real_maxerr=float(np.max(np.abs(ft.real))),
               minvalue_recheck_error=abs(witness_K-K),
               xi=xi.tolist())
    assert pars_err < 1e-10 and phi <= lam + 1e-10
    assert direct_error < 1e-7 and q_pars_error < 1e-10
    assert abs(witness_K-K) < 1e-7
    return out

def group(label, half, B, rp, lam, n, V, centred=False, case_index=0):
    count = 1 if centred else COUNT
    rng = np.random.default_rng(BASE_SEED + 10000 * case_index + V)
    candidates = [[[q for q in range(-V*n, V*n+1) if q % n == int(g[k])]
                   for k in range(2)] for g in half]
    allrows = []
    violations = []
    for i in range(count):
        if centred:
            pairs = ((half + n//2) % n) - n//2
            canonical = lift(set(map(tuple, np.vstack((half, (-half) % n)))), n, n//2)
            assert set(map(tuple, np.vstack((canonical, -canonical)))) == set(map(tuple, np.vstack((pairs, -pairs))))
        else:
            pairs = np.array([[rng.choice(c[0]), rng.choice(c[1])] for c in candidates], dtype=np.int64)
        start = time.time()
        out = one(half, B, rp, lam, n, pairs, V, full_check=(i == 0))
        out.update(label=label, V=V, kind="centred" if centred else "random",
                   index=i, seconds=time.time()-start)
        bad = out["margin_a"] < -1e-6 or out["margin_b"] < -1e-6 or out["A2_margin"] < -1e-6
        if bad:
            out["pairs"] = pairs.tolist()
            violations.append(out)
            emit(dict(type="VIOLATION", **out))
        record(out)
        allrows.append(out)
        if not centred and (i+1) % 25 == 0:
            emit(dict(type="PROGRESS", label=label, V=V, done=i+1,
                      elapsed=time.time()-T0))
    summary = dict(type="SUMMARY", label=label, V=V,
                   kind="centred" if centred else "random", count=count,
                   K_min=min(x["K"] for x in allrows), K_max=max(x["K"] for x in allrows),
                   rhs_a_min=min(x["rhs_a"] for x in allrows),
                   rhs_a_max=max(x["rhs_a"] for x in allrows),
                   rhs_b_min=min(x["rhs_b"] for x in allrows),
                   rhs_b_max=max(x["rhs_b"] for x in allrows),
                   min_margin_a=min(x["margin_a"] for x in allrows),
                   min_margin_b=min(x["margin_b"] for x in allrows),
                   min_margin_c=min(x["margin_c"] for x in allrows),
                   min_A2_margin=min(x["A2_margin"] for x in allrows),
                   phi_max=max(x["phi"] for x in allrows),
                   parseval_relerr_max=max(x["parseval_relerr"] for x in allrows),
                   direct_W_maxerr=max(x["direct_W_maxerr"] for x in allrows),
                   Q_parseval_relerr_max=max(x["Q_parseval_relerr"] for x in allrows),
                   Fourier_real_maxerr=max(x["Fourier_real_maxerr"] for x in allrows),
                   minvalue_recheck_error_max=max(x["minvalue_recheck_error"] for x in allrows),
                   G_values=sorted(set(x["G"] for x in allrows)),
                   violations=len(violations), seconds=sum(x["seconds"] for x in allrows))
    emit(summary)
    return summary

meta = dict(type="META", python=platform.python_version(), numpy=np.__version__,
            scipy=scipy.__version__, count_per_V=COUNT, base_seed=BASE_SEED,
            raw_path=RAW, source_sha256={p:hashlib.sha256(open(p,"rb").read()).hexdigest()
                for p in ("src/e114_cp_group.py","src/e116_jl_taper.py","src/e117_concentration.py")})
emit(meta)
cases = []
for p in (3, 5, 7):
    D, n = jl_set(p, 2, 1)
    cases.append((f"JL({p},2,1)", D, n))
for n in (9, 15, 25):
    rng = np.random.default_rng(BASE_SEED+n)
    half_all = [(x,y) for x in range(n) for y in range(n)
                if (x,y) < neg((x,y),n)]
    chosen = [g for g in half_all if rng.random() < 0.30]
    D = set(chosen) | {neg(g,n) for g in chosen}
    cases.append((f"random(n={n},density=0.30)", D, n))
summaries = []
for ci, (label, D, n) in enumerate(cases):
    half, B, rp, lam, data = setup(label, D, n)
    summaries.append(group(label,half,B,rp,lam,n,1,centred=True,case_index=ci))
    for V in (1, 2):
        summaries.append(group(label,half,B,rp,lam,n,V,case_index=ci))
raw.close()
emit(dict(type="DONE", trials=sum(s["count"] for s in summaries),
          violations=sum(s["violations"] for s in summaries),
          seconds=time.time()-T0, summaries=summaries))

```

