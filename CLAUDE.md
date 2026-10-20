# CLAUDE.md — Chowla's Cosine Problem (FrontierMath: Open Problems)

## Mission: sustained original mathematical research

Throughout this campaign load the Number Theory research skill.

This is an open-ended, **30-day mathematical research project** whose objective is to make a decisive advance on **Chowla's cosine problem**, prioritizing an explicit construction that would satisfy Epoch AI's challenge while also seriously pursuing the competing possibility that Chowla's square-root conjecture is true.

It is **not** a one-session attempt, a literature survey, a request for another numerical search without mathematical understanding, or an essay about why the problem is hard. The assignment is to conduct original mathematics beyond the present frontier.

Official problem: https://epoch.ai/frontiermath/open-problems/chowla-cosine

**Crucial distinction:** Epoch asks for an algorithm constructing counterexamples to Chowla's conjectured square-root lower bound. Such an algorithm may not exist. Do not assume that the benchmark's preferred direction is mathematically correct. Keep two honest, active tracks: **constructive disproof** and **universal lower-bound proof**. A rigorous resolution in either direction is a major success, even if a proof that Chowla is true would not produce an Epoch-valid `solution` function.

Treat orientation, literature review, reproducing existing examples, and baseline code as **Phase 0 only**. Complete them efficiently and proceed to new conjectures, proofs, counterexamples, and constructions. Do not keep revisiting the literature in lieu of doing mathematics. Check novelty in detail after a serious result, not at the cost of discovering it.

## Exact mathematical target and conventions

Let `A` be a **finite set** of **distinct positive integers**. Define the real trigonometric polynomial

    f_A(x) = sum(cos(a*x) for a in A),                 x in R.

Because `f_A` is `2*pi`-periodic, its global minimum exists. Let

    N(A) = |A|
    M(A) = -min_{x in R} f_A(x)       (> 0 for nonempty A)
    R(A) = M(A) / sqrt(N(A))
    K(n) = inf_{|A|=n} M(A).

Chowla's square-root conjecture asserts the existence of an **absolute constant** `c0 > 0` such that

    M(A) >= c0 * sqrt(|A|)

for **every** finite nonempty `A` of distinct positive integers. Equivalently, `K(n) >= c0*sqrt(n)` for all positive `n`.

The desired constructive negation is a **uniform algorithm**, not a single example: for every real `c > 0` and every integer `n >= 1`, produce an `A` with

    |A| >= n
    min_{x in R} f_A(x) >= -c * sqrt(|A|).

There must be no dependence of `c0` on `n`, `A`, `max(A)`, or the choice of `x`. Maintain exact quantifiers in every proposed proof or counterexample.

**Do not confuse** an upper bound on `M(A)` (a successful *construction*) with a lower bound on `M(A)` (a *barrier* satisfied by every `A`). Do not silently switch between `cos(a*x)` and `cos(2*pi*a*t)` without the change of variables. Use the entire circle, not a sampled grid, as the mathematical domain.

### Epoch submission specification — preserve verbatim in substance

Implement a Python script containing

```python
def solution(c: float, n: int) -> str:
    ...
```

For every finite positive `c` and positive integer `n`, the returned string must list **at least `n` distinct positive integers** separated by whitespace and/or commas, and those integers must satisfy

    f_A(x) >= -c * sqrt(|A|)   for every real x.

No zero frequencies, negatives, repeated frequencies, coefficient weights other than `+1`, or arrays of multisets. Returning a spectacular example for one `c` or one `n` does **not** solve the quantified challenge. A nonconstructive existence theorem is significant, but an Epoch submission additionally needs an effective, terminating generator (and ideally a proof of termination and correctness).

Epoch warns that its **numerical verifier** may fail for very large frequencies and recommends `max(A)` **well below `10^6`**, with a lower practical ceiling for smaller `c`. This is a *verifier limitation*, **not a mathematical restriction** or a fixed cap to impose on every possible `n`. Do not mistake passing an approximate numerical verifier for a rigorous certificate. Do not pretend that a finite frequency ceiling is compatible with outputting arbitrarily many distinct positive integers.

### What counts as success

**Decisive constructive success:** Give an explicit, terminating algorithm for arbitrary inputs `c > 0`, `n >= 1`, together with a proof that its output is a valid set satisfying the **global** trigonometric inequality. Produce the actual `solution(c,n)` implementation and independently validated outputs. If asymptotic constructions require a threshold, prove or compute a finite-case completion; explain any verifier-size limits honestly.

**Decisive proof success:** Establish Chowla's conjecture by proving a universal `c0 > 0`, with full quantitative hypotheses and a rigorous proof for all `A`. This would show that Epoch's requested algorithm cannot exist.

**Substantial partial success:** Improve the exponent in a universal lower bound; improve the construction-side asymptotic constant or exponent; prove a new infinite parametric family with certified values of `R(A)`; discover a rigorous obstruction to a broad class of constructions; or give a nontrivial exact positivity certificate. Preserve partial results without presenting them as resolution of Chowla or Epoch.

Distinguish **heuristic**, **numerically observed**, **interval-certified finite case**, **proved on paper**, **kernel-checked**, and **externally scrutinized**. A paper proof and its Lean formalization are separate deliverables. Never silently upgrade one status to another.

## Minimum literature baseline — then do new mathematics

Read only enough to understand the strongest relevant mechanisms and to avoid trivial rediscovery. As of October 2026, useful starting points include:

1. Epoch's precise problem statement: https://epoch.ai/frontiermath/open-problems/chowla-cosine
2. Benjamin Bedert, *Polynomial bounds for the Chowla Cosine Problem*: https://arxiv.org/abs/2509.05260
3. Abhishek Shankar, *A Log-Free n^(1/5) Bound for Chowla's Cosine Problem*: https://arxiv.org/abs/2609.05338 — claimed uniform lower bound `M(A) >= C |A|^(1/5)`.
4. Bryan Bu and collaborators, *A Half-Constant Upper Bound for Chowla's Cosine Problem*: https://arxiv.org/abs/2610.17160 — preprint claiming constructions with `K(n) <= (1/2)*sqrt(n) + O(n^(1/4)*sqrt(log n))`.

These are **leads to read and verify**, not axioms or an exhaustive survey. Record versions and precise quantifiers. The square-root exponent on the construction side is not evidence by itself that the conjectured matching lower bound is true.

### Baseline identity: difference sets

For a finite integer set `B`, let `F_B(x) = sum_{b in B} exp(i*b*x)`. Then exactly

    |F_B(x)|^2 = |B| + 2*sum_{u<v in B} cos((v-u)*x).

If the positive differences `v-u` are **all distinct**, they form a genuine set `A` of size `|B|*(|B|-1)/2`, and

    f_A(x) = (|F_B(x)|^2 - |B|)/2 >= -|B|/2.

Thus `M(A) <= |B|/2 = O(sqrt(|A|))`. If differences collide, this identity creates **multiplicities**, not an admissible equal-coefficient cosine sum: address the collisions rigorously. This simple construction is only a starting point. Reproduce it once, then seek a genuinely different idea.

Also record the exact identities

    (1/(2*pi)) * integral_0^(2*pi) f_A(x) dx = 0,
    (1/(2*pi)) * integral_0^(2*pi) f_A(x)^2 dx = |A|/2.

Higher moments count signed additive relations among frequencies. Understand both their power and their limitations; low moments alone are not a solution.

## Research program: maintain at least three genuinely distinct active lines

### 1. Positive trigonometric polynomials and algebraic construction

Seek new identities

    C + 2*f_A(x) = sum_j |P_j(exp(i*x))|^2 + E(x)

or other certified lower bounds, with **exactly** the desired coefficient pattern (distinct positive frequencies, coefficient `1`). Investigate Fejér–Riesz factorization, autocorrelation sequences, Sidon/Golomb-ruler differences, two-sided difference constructions, Riesz products, Fejér kernels, cyclic difference sets, combinatorial designs, and structured cancellation of multiplicities.

Explore how to remove unwanted weighted coefficients **without losing the lower bound**. Generalize the ideas behind known `1/2`-constant constructions rather than endlessly tuning their parameters. Seek a mechanism that can drive `R(A)` toward zero, perhaps slowly, or prove a rigorous obstruction to whole families of such mechanisms.

### 2. Additive combinatorics and spectral structure

Relate the negative minimum to additive energy, signed relation counts, sumsets, difference sets, Cayley graph spectra, small eigenvalues, and large cuts. Develop inequalities that exploit the restriction that all nonzero Fourier coefficients are `0` or `1/2` with no repetitions.

Try to improve `M(A) >= C |A|^(1/5)` toward a square-root lower bound, or prove bounds under meaningful additive or density hypotheses. Look for structural consequences of a hypothetical `R(A) -> 0`, then force a contradiction or exploit those consequences constructively.

### 3. Extremal constructions and inverse mathematics

Treat a near-optimal set `A` as an extremal object. Study which transformations preserve or change its global minimum, including dilation, unions of separated blocks, tensor/product constructions, modular lifting, random thinning, affine frequency transformations, recursive composition, and symmetrization. **Prove** any preservation claim; e.g. multiplying all frequencies by a positive integer leaves the minimum unchanged but shifting them generally does not.

Search for a composition operation mapping good sets into much larger sets while improving `R(A)`. A rigorous rule with `R(A_k) -> 0` and `|A_k| -> infinity` could be a breakthrough. Analyze whether repeated composition creates collisions, amplified negative spikes, or a hidden square-root barrier.

### 4. Analytic inequalities and dual certificates

Investigate Fourier positivity, moment methods, `L^1`/`L^2`/`L^4` bounds, distribution of negative values, majorant/minorant constructions, Bohr sets, harmonic-analysis duality, and quantitative versions of Littlewood-type problems.

For a universal lower bound, aim for a test function, measure, or dual certificate that forces `min f_A <= -C sqrt(|A|)` uniformly over all `A`. For constructions, seek certificates proving `f_A(x) >= -B` for all real `x`.

### 5. Rigorously optimized finite examples as mechanism probes

Use small exact searches, nonlinear optimization, SAT/ILP/SDP, additive-structure enumeration, or randomized local search to identify *why* promising families work. Define and track `R(A)` and the location(s) of the global minima. Search adversarially for counterexamples to any proposed structural theorem.

A record-breaking single set is worth preserving, but finite optimization **cannot** establish the required `forall c, forall n` statement. Spend computation to distinguish mathematical mechanisms, not merely to increase input sizes.

### 6. Counterexample-to-counterexample and proof-by-obstruction track

Attempt to prove no proposed recursive construction can beat some positive normalized threshold, while carefully separating barriers for a **particular construction class** from the full Chowla conjecture. Conversely, deliberately attack all conjectured lower bounds with structured, pseudorandom, sparse, dense, and highly additive examples. Let the evidence choose the direction of future work; do not force a predetermined answer.

Do not let one approach dominate merely because it is easy to automate. Maintain **at least three active research lines**, including at least one aimed at a global lower bound and at least one aimed at a genuine counterexample family, unless clear mathematical evidence justifies a change.

## Certification: a numerical minimum is not a theorem

This is the most important domain-specific safeguard.

For an explicit finite candidate `A`, a floating-point plot, FFT, dense grid, or local optimizer only yields **evidence**, never a proof of

    f_A(x) >= -B   for all real x.

A missed, narrow negative excursion invalidates the claim. Develop at least two independent certification methods when possible:

1. **Certified interval subdivision:** use directed-rounding or ball arithmetic for rigorous cosine enclosures and derivative bounds. Since `|f_A'(x)| <= sum(A)`, a grid of `K` equally spaced points on `[0,2*pi)` has a nearest point at distance at most `pi/K`; hence

       min f_A >= min_{grid} f_A - (pi/K)*sum(A).

   The grid evaluations must themselves have rigorous error bounds, and the error budget must be smaller than the claimed margin. Adaptive subdivision and higher derivatives can be more efficient.

2. **Exact polynomial certification:** write `t = cos(x)` and `cos(a*x) = T_a(t)` using the Chebyshev polynomial `T_a`. Then

       f_A(x) + B >= 0 for all real x
       iff  sum_{a in A} T_a(t) + B >= 0 for all t in [-1,1].

   For rational `B`, exact Sturm/subresultant methods, rational interval isolation, or a rigorously checked SOS/Positivstellensatz certificate may establish nonnegativity. Degree is `max(A)`; anticipate scalability limits.

3. **Symbolic analytic proof:** explicit sum-of-squares identities, Fourier inequalities, or a parameterized closed-form lower bound are preferable for infinite families.

For input `c` represented by a Python float, handle its exact positive value (or choose a **strictly smaller rational threshold**) and prove a bound strong enough to imply `M(A) <= c*sqrt(|A|)`. Use rigorous rational enclosures for `sqrt(|A|)` as needed. Treat very small `c`, huge `n`, numerical conditioning, overflow, and verifier frequency constraints explicitly. A library reporting `success` is not an automatic mathematical certificate unless its guarantee is understood.

## Scientific workflow: proof-first, conjecture-driven, adversarial

Repeat throughout the 30-day project:

1. State a precise candidate theorem or construction, with quantifiers, normalization, and the exact implication to either Chowla or Epoch.
2. Attempt the mathematical derivation before large experimentation. Identify the single missing mechanism or implication.
3. Check easy cases and develop two independent evaluators; use targeted search to **falsify** overly strong claims and expose worst cases.
4. When a construction appears successful, attempt a global-in-`x` certificate immediately. When a lower bound survives, seek a full proof and explicit dependence on constants.
5. Subject each new conjecture to **adversarial examples** before investing days in it: difference-set families, arithmetic progressions, lacunary/geometric sets, unions of blocks, random sets, and deliberately optimized extremizers. Preserve failed statements and smallest counterexamples.
6. Pass mature statements and proofs to a separate Lean formalization agent. Incorporate feedback into the next research attempt.
7. Record exact progress and continue. A failed lemma is a research event, not permission to stop.

**Never** claim an Epoch solution from a single very small normalized ratio. **Never** claim a universal lower bound because a search failed to find a counterexample. Do not confuse the mathematical problem with the constraints or numerical approximations of Epoch's verifier.

## Computation: targeted, modest, reproducible

The primary bottleneck should be mathematical ideas, not brute-force GPU time. Favor exact integer combinatorics, small rational LP/SDP certificates, analytic constructions, and rigorous interval arithmetic.

- Build two independent cosine-sum evaluators and verify the cosine convention, periodicity, normalization, and the set constraint. Where possible, compare FFT sampling, direct high-precision evaluation, and analytic identities.
- Record cardinality, distinctness, `max(A)`, normalization `R(A)`, estimated minimizing angle, numerical uncertainty, and **certificate status** for every notable candidate.
- For finite integer searches, preserve seeds, search space, completeness, runtime, and source code. Label heuristic results honestly.
- Use exact arithmetic for additive identities and collision counts. If probabilistic existence is asserted, prove the probability bound and effective sampling/derandomization algorithm; avoid presenting Monte Carlo luck as a proof.
- Treat speed and practical `max(A)` bounds as secondary optimization criteria **after** obtaining a mathematically correct construction.
- Prefer experiments that discriminate between a square-root barrier and a credible sub-square-root construction over incremental tuning of already understood families.

## Lean 4 formalization and adversarial proof review

The lead research agent discovers the mathematical argument; the Lean agent independently scrutinizes claims, tests overlooked quantifiers, and formalizes mature theorems. Both should receive the *same* exact statement, not a weakened substitute.

For each prospective theorem, provide the formalizer:

- Complete quantified statement, including positivity, distinctness, cardinality, `forall x`, and any dependence of constants on parameters.
- Human-readable derivation, precise dependencies, and any non-elementary outside result cited.
- Mathematical meaning of every definition and normalization.
- Boundary cases and known candidate counterexamples.
- A precise distinction between finite certified checks and global mathematical claims.

Useful Lean foundations include finite sets of natural frequencies, complex exponential/trigonometric polynomials, `cos` periodicity, nonnegative squares, discrete convolution, Fourier orthogonality, and real inequalities. Formalize the difference-set identity and basic moment formulas early; after that, focus on the most consequential new lemmas. If a proof relies on specialized analytic machinery missing from mathlib, document that obstacle and provide an independent complete paper proof; do not silently replace an unformalized theorem with an approximation.

Track `sorry`, new axioms, opaque `native_decide`/unchecked external solvers, and imported theorem assumptions. Only call a result **kernel-verified** when its intended statement is checked under explicitly acceptable axioms. Source compilation by itself does not prove that an intended external theorem has been formalized correctly.

The formalizer must **not** replace `forall real x` with a finite grid, replace a set with a multiset, weaken an arbitrary-`c` statement to a particular constant, or restrict `n` without announcing the change. If it finds a gap, feed it back immediately.

## Persistent research record

Maintain a resumable record at minimum:

    .research/NOTEBOOK.md         # Dated ideas, derivations, failures, and next questions
    .research/STATE.md            # CURRENT targets and honest proof/certification status
    .research/PROOFS.md           # Statements, proof attempts, dependency graph
    .research/EXPERIMENTS.md      # Exact tests, seeds, candidates, global-minimum bounds
    .research/LITERATURE.md       # Concise relevant prior art and versioned sources
    .research/CONSTRUCTIONS.md   # Parametric families, algorithms, output sizes, limitations
    .research/CERTIFICATES.md    # Rigorous all-x certificates and how to verify them
    src/                       # Generators, independent evaluators, optimization tools
    lean/                      # Definitions and formalized mature theorems
    examples/                  # Strong examples and explicit failed conjectures
    solution.py                # Epoch interface, only when a valid general algorithm exists

For each promising candidate, save `A`, generator or seed, tested input `(c,n)`, `N`, `max(A)`, claimed and certified `M(A)` intervals, certificate proof, code version, and rationale. For infinite families, save the parameter map and the quantified theorem proving their behavior.

Commit meaningful changes. Never overwrite a refuted conjecture without retaining its counterexample and explanation. **Keep `.research/STATE.md` current**: if the main route fails, update the handoff immediately, rather than allowing future sessions to continue pursuing a theorem already known to be false.

At every session boundary produce a succinct handoff: (a) mathematical theorems proved and formalized; (b) constructions certified and still heuristic; (c) refuted intermediates; (d) three distinct promising active directions; and (e) the **first concrete next derivation or experiment**. Handoff documents are operational memory, not promotional summaries.

## Continuation and reporting

The research horizon is **30 days** subject to authorized time, cost, and execution constraints. A session ending is **not** completion of the project. If external orchestration is needed to restart work, checkpoint it; do not imply work continues without such orchestration.

Report periodic, concise progress centered on newly discovered formulas, proved special cases, validated constructions, unexpectedly negative minima, killed conjectures, and precise next experiments. Do not repeatedly explain that Chowla's problem has been open for decades or that existing techniques seem inadequate.

Do **not** declare the investigation finished because an approach fails, a numeric constant stalls near `1/2`, an algorithm cannot beat the verifier's practical ceiling, or a full proof has not emerged quickly. Continue to investigate genuinely different mechanisms until explicit stop, exhausted authorization, or a handoff imposed by session limits.

## Immediate next task

1. Verify the official Epoch task's exact input/output conditions, and implement two independent checkers for `A` distinctness, cosine values, and rigorous (or explicitly uncertified) minima. Fix the convention `cos(a*x)`.
2. Reproduce the **difference-set square identity** symbolically and with small examples; audit collisions and the resulting coefficient multiplicities. Also reproduce one meaningful published construction-side improvement and one current universal lower-bound argument at the level required to understand their bottlenecks—not as an extended survey.
3. Formulate **at least five genuinely different research strategies** spanning constructions, a universal lower bound, and exact certification. For each, give a precise mathematical claim that would constitute progress, how to disprove it quickly, and the first missing lemma.
4. Maintain **at least three active lines**. Select the most promising new construction mechanism and begin deriving it **now**; in parallel pursue a lower-bound mechanism with a plausible route from exponent `1/5` toward `1/2`. Do not end after proposing a plan.
5. If a proposed family offers `R(A_k) -> 0`, derive explicit parameter bounds sufficient for arbitrary inputs `(c,n)` and construct `solution(c,n)`. Request an independent proof and Lean review of the central theorem; construct a global-in-angle certificate, not merely a plot.

## Non-negotiable research attitude

**Do not respond with generic explanations of why Chowla's cosine problem is difficult.**

The task is to conduct original mathematical research beyond what is already known. A literature map, a failure diagnosis, or a familiar upper-bound example is an intermediate event, **not** the end of the investigation.

**Do not assume Chowla is false merely because Epoch rewards a counterexample. Do not assume it is true merely because known constructions have square-root scale.**

Keep asking: *What specific structural ingredient would force a square-root negative dip? What new construction could evade it? What exact identity or invariant would distinguish the two possibilities?*

**Identify the missing ingredient. Attempt to derive it. If it fails, find out why, preserve the obstruction, and pursue a different mechanism.**

**Do not confuse understanding the current mathematical frontier with exhausting the mathematics beyond it.**

**DO NOT INVEST TIME INTO WRITING UP MANUSCRIPTS AND LATEX PAPERS UNLESS INSTRUCTED TO DO SO**
