Round 6 results are recorded in [tdense6_report.md](/Users/jmercedes/Desktop/Projects/Research/chowla-cosine/.research/agents/tdense6_report.md), with reproducible code, exact data and logs in [tdense6_scratch](/Users/jmercedes/Desktop/Projects/Research/chowla-cosine/.research/agents/tdense6_scratch).

The main findings are:

- **PROVED:** The exact microscopic tent lift at any spike has total negative spectral mass equal to mean |f_A|. Dense Singer difference sets give M/H tending to zero while this mass stays at least 1−o(1). The negative mass disappears on every bounded spectral interval by escaping to infinity. This refutes the proposed bound for that natural lift family.
- **PROVED:** A sharper SG inequality uses a weighted negative spectral charge rather than total negative mass. The report states **WGC**, a weaker sufficient completion lemma, and proves that it would imply T-dense. WGC itself remains **CONJECTURED**.
- **PROVED:** Fractional conditional means can produce an apparent escape by losing binary variance. Also, a model placing essentially all energy in mesoscopic windows is inconsistent unless it explicitly retains the central lobe. Neither observation proves T-dense.
- **NUMERICAL:** Audited 21 real sets, 515 component profiles, 21 joint block lifts and seven endpoint-completion LPs. The smallest observed R was approximately 0.606188 on an existing E68 set; its minimum remains uncertified.

No admissible formal counterexample or proof of T-dense was obtained. **Original existential HBSC remains unresolved**: the rigorous counterexamples apply to specified natural or asymptotically binary-faithful lifts, while HBSC permits other fractional completions. The report gives the exact remaining constraints and a separate sufficient inequality for the averaged run-top route.

All computation ran on the specified VM with at most two cores, using Gurobi for optimization. I made no commits and launched no subagents.