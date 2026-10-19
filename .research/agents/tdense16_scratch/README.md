# Round 16 artifacts

The report is `../tdense16_report.md`. It contains the infinite-family paper proof; these finite checks do not substitute for that proof.

Run each command from the project root with a bash command shell:

```bash
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -t 600 python .research/agents/tdense16_scratch/adaptive_fake.py
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -t 600 python .research/agents/tdense16_scratch/adversaries.py
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -t 600 python .research/agents/tdense16_scratch/verify_round16.py
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -t 600 python .research/agents/tdense16_scratch/final_audit.py
```

- `adaptive_fake.py/json/log`: compressed support construction, exact monomial counts, 200-bit Arb level and residual checks at three primes. The represented support sizes reach 7.6 million; no dense array of size q is allocated.
- `adversaries.py/json/log`: NUMERICAL additive and multiplicative diagnostics on 23 genuine half-sets and two preserved scalar fakes. Seed 151019. Phase moments use orders 1 through 6 and every character twist. No optimization.
- `verify_round16.py`, `verification.json/log`: independent sorted-window support verifier, exact rational convolution values, and 256-bit Arb repair/capacity checks. It does not import the constructor.
- `final_audit.py`, `manifest.json`, `final_audit.log`: package versions, artifact/input hashes and final consistency checks. Logs are excluded from hashes because they can still be open during the audit; the manifest excludes itself.

No kernel verification is claimed. The exact support arithmetic and the floating genuine-set measurements have separate status labels in the report.
