# Literature brief 2: the explicit structure of the Jedwab–Li / Polhill non-PCP Latin-square-type PDS

You are a literature-check agent for the lead. Use web browsing (arXiv:2012.00979, Jedwab–Li, "Packings of partial
difference sets", Combinatorial Theory 1 (2021) #18; and Polhill, Electron. J. Combin. 15 (2008) #R125). Write the
report to `.research/agents/lit_jedwabli_report.md`. Do not edit other files. Do not commit. No heavy computation; a
small exact check of one example (say p = 3, a = 3, s = 1, so G = Z_27^2) is welcome if cheap, run on the VM via
`DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 1 -t 600 python <script>` from the repo root.

Questions, answered with exact definitions and theorem numbers:
1. Write out EXPLICITLY the set D of Jedwab–Li Theorem 5.3 (regular LS_{p^{(a-1)s}}(p^{as}) PDS in Z_{p^a}^{2s}) for
   s = 1, in coordinates (x, y) in Z_{p^a}^2. Give the recursion/lifting exactly as in the paper.
2. Is D ∪ {0} a union of subgroups of G (of ANY orders, overlaps allowed)? If not, what is the smallest description:
   unions of sets H \ K (subgroup minus subgroup)? unions of cosets? Decide this by an argument or by an exact check
   for p = 3, a = 3, s = 1 (list the maximal subgroups contained in D ∪ {0} and test whether they cover D).
3. The character values of D: confirm the two values n − r and −r and how they arise (which characters see the
   large value). Is the large-value set a union of subgroups of the dual group?
4. Same questions, briefly, for Polhill's positive LS_{(p-1)(p^2+1)}(p^4) PDS in Z_{p^2}^4.
Report format: precise statements, source locations, and confidence ("read in source" / "checked by computation" /
"recalled"). End with a 3-line summary answering: are these high-ratio exact two-valued objects unions of subgroups?
