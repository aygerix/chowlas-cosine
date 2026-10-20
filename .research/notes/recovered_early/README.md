# Recovered early reports: historical PDF-derived text

Recovered on **20 October 2026 (UTC)** from two surviving PDFs, both dated **20 October 2026**. The original Markdown notes and original Git objects were not recovered by this operation. This directory supplies readable text reconstructions and page-delimited extraction records; it does not pretend to restore original source files or their proof/experiment numbering. The source PDFs are intentionally excluded from this text-only recovery bundle.

## Files and provenance

| Source PDF | Pages | SHA-256 | Readable reconstruction | Extraction record |
|---|---:|---|---|---|
| `chowla-negative-sublevels.pdf` | 5 | `b9668b72b5b0b72f0171f32a98b1630de61c986fde33f537f271731eb5927ecf` | [Negative sublevels report](negative_sublevels_report_2026-10-20.recovered.md) | [Page-delimited text](negative_sublevels_report_2026-10-20.pdftotext.txt) |
| `chowla-research-handoff.pdf` | 10 | `3597a4312aae50c55e0ebf5d41c0816951353953a298e3253e24605489e0f3a7` | [Research handoff](research_handoff_2026-10-20.recovered.md) | [Page-delimited text](research_handoff_2026-10-20.pdftotext.txt) |

The shorter report cites public baseline `dfd51a19d0b094850f451d1cc82c88880be77b17`. The handoff cites local snapshot `446367d948fedba07c5e70e3fdf9d9fcd106b08b` and the same public baseline. These are **source-reported historical locators**. The public baseline was independently recovered in the restored repository history; this PDF recovery does not supply that history. The local snapshot `446367d948fedba07c5e70e3fdf9d9fcd106b08b` has not been recovered.

The handoff names `negative_sublevels_2026-10-20.md` and `negative_sublevels_2026-10-20_appendix.md` as source notes. Neither name is used for the reconstructions: the PDFs do not recover their exact original Markdown. Other named source notes, such as `cstar_cyclotomic_determinants_2026-10-20.md` and `cstar_boolean_boundary_tests_2026-10-20.md`, should be consulted directly where separately restored.

## Contents and current status

- The exact finite Boolean augmentation argument and its conditional closure statement are recovered in both reports. These are conditional constructions, not actual counterexamples to Chowla.
- The advisor-attributed L1 strengthening is explicitly present on **handoff page 6**. Its attribution is preserved as reported; this recovery does not independently establish the advisor's identity or priority.
- Both reports contain the fixed-kernel packet limit and the bounded fractional Fejér-padding obstruction to a stable profile-only discriminator.
- The handoff also includes cyclotomic norm/variance tests, the arbitrary-index Toeplitz determinant argument, and the high-rank boundary-Schur counterexample, with their stated restrictions.
- Numeric table entries and figure captions are recovered. **Chart images, full threshold samples, and underlying early numerical data/scripts cannot be reconstructed from the PDFs alone.** References to an experiment bundle or scripts remain historical locators, not an assertion that those specific early assets were restored.

These are historical reports. Their conclusions about the then-current research agenda are **superseded as overall project status** by the [research checkpoint](../cstar_research_checkpoint_2026-10-20.md), [research addendum](../cstar_research_addendum_2026-10-20.md), [full-W2 falsification pass](../cstar_full_w2_falsification_2026-10-20.md), [groundstate repair](../cstar_groundstate_repair_2026-10-20.md), and [coupled-mode results](../cstar_coupled_mode_2026-10-20.md), where applicable. This does not assert that every historical theorem was invalidated. In particular, the checkpoint explicitly retains the earlier L1/fixed-depth obstruction in its stated scope. None of these reports proves the universal Chowla bound; no historical candidate or speculative route is promoted to a current theorem by this recovery.

## Extraction and reconstruction limitations

The `.pdftotext.txt` files use `pdftotext -layout` and retain the extracted page bodies unchanged, including footers, apart from replacing form-feed separators with explicit page labels and adding provenance headers. Formula glyphs and reading order can be lossy. The `.recovered.md` files reflow prose, restore readable mathematical notation, and retain the source page mapping. They are editorial transcriptions of the surviving reports, **not byte-for-byte original Markdown**, and should be checked against the extraction records and source hashes when exact wording matters.

The mathematical displays in the central augmentation/L1/fractional sections were checked against rendered source pages. This is transcription QA, not a fresh independent audit or a formal proof verification. No charts have been fabricated, no numerical computations have been rerun by this operation, and no original proof/experiment index has been silently amended.
