# Literature brief: are Latin-square-type partial difference sets with small r always unions of subgroups?

You are a literature-check agent for the lead. Do not do new mathematics beyond checking exact statements. Use web
search/browsing if your environment allows it. If it does not, say so explicitly in the first line of your report and
then report only what you can state with certainty from memory, clearly labelled "FROM MEMORY, UNVERIFIED".
Write your report to `.research/agents/lit_lspds_report.md`. Do not edit any other file. Do not commit. No heavy
computation is needed. If you do any, it runs on the VM `dirichlet` via `src/dirun.sh` (see that file).

## Definitions (fix these conventions)
- G a finite abelian group of order n² (or v in general), D ⊂ G \ {0} with D = −D.
- D is a (v, k, λ, μ) partial difference set (PDS) if every nonzero element of D is represented λ times as a
  difference of two elements of D, and every nonzero element outside D is represented μ times.
- Equivalently, the character values χ(D) (χ nontrivial) take exactly two values. LATIN SQUARE TYPE LS_r(n):
  (n², r(n − 1), n + r² − 3r, r² − r), with nontrivial character values n − r and −r. NEGATIVE Latin square type
  NL_r(n): replace n by −n and r by −r.
- A partial congruence partition (PCP) of degree r: subgroups H_1, …, H_r of order n with H_i ∩ H_j = {0}. The union
  minus 0 is an LS_r(n) PDS. In elementary abelian groups this is a partial spread.

## Questions (answer each with exact statements, hypotheses, and citations with year and arXiv/DOI where possible)
1. Is there a theorem that every Latin-square-type PDS with r below some bound (in terms of n), or in some class of
   groups, must arise from a PCP (a union of r subgroups of order n meeting trivially)? Give the precise bound and
   the hypotheses (elementary abelian? abelian? n a prime power?).
2. Known Latin-square-type PDS that are NOT unions of subgroups. In which groups, and for which r relative to n?
   Look for examples from cyclotomy, from Galois rings in Z_4^m, from "product constructions", etc.
3. Classification of PDS in Z_p² and Z_p³, in particular De Winter–Kamischke–Wang (approx. 2016) on PDS in Z_p².
   What exactly is proved?
4. Any ROBUST or approximate versions: e.g. a set whose character values are nearly two-valued, or whose negative
   values are small (all >= −r), being forced to be close to a union of subgroups. Also any "stability" results for
   strongly regular Cayley graphs. Report even partial or nearby results.
5. Ma's theorem on PDS in cyclic groups (exact statement), and any extensions to "cyclic groups have no nontrivial
   Latin-square-type PDS" or to groups with cyclic Sylow subgroups.

## Report format
For each question: the precise statement(s), the source (authors, title, venue/arXiv, year), and how confident you
are that the statement is quoted correctly ("read in source" vs "recalled"). End with a 5-line summary of what is
KNOWN and what is OPEN for the implication "small negative eigenvalue r ⇒ union of subgroups".
