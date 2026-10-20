Completed the brief. The report is at [e111_report.md](/Users/jmercedes/desktop/projects/research/chowla-cosine/.research/agents/e111_report.md).

- Ran all **20 benchmark cases** and adversarial searches for every **X=10,…,40**. The best flat certificate found has ratio **0.73854895** for Singer `q=11`; the best search ratio is **0.75377836** at `X=12`.
- The optional two-level computation found a certificate for `X30_s0` with ratio **0.65487078**, versus **0.80836270** for its flat optimum. Its [certificate JSON](/Users/jmercedes/desktop/projects/research/chowla-cosine/examples/e111/X30_s0_two_level.json) contains exact rational weights. This is a finite non-flat result.
- **63 certificate files passed independent exact rational verification.** Numerical gaps closed for 15/20 benchmarks and all 31 search winners; the five remaining benchmark gaps are explicitly reported.

All heavy computation ran on `dirichlet`. Code is in [src/e111_cp.py](/Users/jmercedes/desktop/projects/research/chowla-cosine/src/e111_cp.py), with data under [examples/e111/](/Users/jmercedes/desktop/projects/research/chowla-cosine/examples/e111). No commit was made.