# Git bundle handoff — 20 October 2026

This handoff is based on the public remote history of
`aygerix/chowlas-cosine`, fetched at commit
`3873843090179751cb8732f5c0e9dcd21c1188bc`. The new research is committed on
`research/oct20-handoff`. No remote push was performed.

The bundle contains complete history for this branch, not an unrelated
snapshot and not an incremental bundle requiring an unavailable local commit.
The former unpublished local commit `446367d` was not recovered as a Git object.
Recovered reports and experiments are committed anew on the fetched history.
See [recovery index](RECOVERY_INDEX.md) and [documentation audit](RECOVERY_AUDIT.md)
for coverage and limitations.

## Safest review: clone into a new directory

```sh
git clone --branch research/oct20-handoff \
  /path/to/chowlas-cosine-research-2026-10-20.bundle chowla-handoff
cd chowla-handoff
git log -1 --format=fuller
git status --short
```

Start with `.research/STATE.md` and `.research/RECOVERY_INDEX.md`.

## Bring the branch into an existing clone

First make sure your working tree is clean or save your local changes.
Fetch the bundle without changing the checked-out branch:

```sh
git bundle verify /path/to/chowlas-cosine-research-2026-10-20.bundle
git fetch /path/to/chowlas-cosine-research-2026-10-20.bundle \
  refs/heads/research/oct20-handoff:refs/heads/research/oct20-handoff
git log --oneline main..research/oct20-handoff
git diff --stat main...research/oct20-handoff
```

Review the changes before merging or cherry-picking. If a local branch already
has that name, choose another destination name in the fetch refspec rather
than force-updating it. The bundle does not authorize a remote push.

## Research status

The reports distinguish paper proofs, independent audits, exact finite checks,
and floating-point diagnostics. They do not claim a universal Chowla bound or
a universal full-W2 theorem. Earlier historical reports are labeled as such;
later refutations and corrections are indexed in the current-status ledgers.

The accompanying text receipt records the final commit, bundle SHA-256, and
verification results. A successful Git integrity check verifies the handoff
bytes and history, not the mathematical proofs.
