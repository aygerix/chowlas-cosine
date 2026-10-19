# ROUTES — ledger of proof routes and what each reduces to (created 2026-10-19 after the user caught the circling)

RULE: before ANY new route gets work (lead or agent), add a row. The row must say which existing entry the route
reduces to, or give a concrete reason it does not. A new statement that is "new wording" of a row below is NOT a new
route. Grep PROOFS/NOTEBOOK for the MECHANISM, not just the statement.

## The core obstruction C* (first recorded 2026-10-18: NOTEBOOK "localization" note ~l.700, P24/P25, P28's open step; restated P53, day 2)
- Sign-preserving operations on f_A + M >= 0 localize only at the FRONT. PD multipliers satisfy |ψ(m)| <= ψ(0); the
  available family is front windows, dilation-restrictions, products of these, and test measures (P29(b) = M, P70.6).
- Interior (mesoscopic) information is reachable only through the MODULUS (P24/P25/P28), which loses the sign.
- Chowla needs: a set that is locally deterministic / spiky at mesoscopic heights √n << h << n (forced by P28, P40)
  ⇒ a sign (Gibbs) contradiction, quantitatively, with no accumulating loss across scales.
- Every row marked "= C*" below is this statement in different language. Do not re-derive it.

## Ledger
| Route | Where | Reduces to | Status |
|---|---|---|---|
| "deterministic ⇒ Gibbs" quantitative | P28 open step, day 1 | = C* | open |
| Localization + 2-run structure (OR(2)-weak) | NOTEBOOK day 1, P27 | partial C* (bounded unions of dilates done, P27) | open in general |
| Self-reducibility SR | NOTEBOOK day 1 | NOT AUDITED | audit before reuse |
| Spike truncation / bulk fraction (SB) | P40, E67/E68 | = C* (spike-dominated ⇔ band-limited, P40(c)) | open |
| Macro twisted profiles | P48, P53 | C* at MACROSCOPIC scale: PROVED (qualitative, any rank) | done; mesoscopic = C* |
| Dense second/third order | P59–P66 | sub-problem; proven barrier: second-order reach 1/D (P61), bounded-M sharpness | T-dense C < 7.72 (½), 13.7 (1/3) |
| Scalar moments | R12-S | capped at 1/3 (proved) | dead |
| Group-agnostic (finite groups) | JMTZ, F_p⁴ quadric | capped at ¼ (proved) | dead |
| Cyclic CSFG / PK | round 12, P64 | C* in cyclic costume (Z_q has no front) | paused |
| Cyclic WRS(η) | rounds 15–16, P68–P69 | C* in cyclic costume; heavy-core fake (P69) | paused |
| Self-difference graph dichotomy | cont. 19.7–9 | P40 (graph form) + P9 | corrected (cont. 19.10–11) |
| Four-way cover | round 17, P70 | = C* | open |
| TAPER (correlated roundings) | round 18 brief | = C* | stopped 2026-10-19 |
| Positivity–resolution PR | cont. 20 | = P53 step 5, quantitative | dropped |
| Szegő / OPUC (Verblunsky energy <= log K) | cont. 21.1(c) | P40(c) band-limitation, plus a log loss | dropped |
| Window-variance bound VB | cont. 21.1(d), E101 | weak L² form of P28 | dropped |
| Hardy/Fejér–Riesz factor WINDOWING | cont. 21.3 | CLAIMED not C*: a sign-preserving INTERIOR localization (|U_I|² >= 0) | UNTESTED; kill test E102 |
