# Git bundle handoff — 20 October 2026

This handoff is based on the public remote history of
`aygerix/chowlas-cosine`, fetched at commit
`3873843090179751cb8732f5c0e9dcd21c1188bc`. The new research is committed on
`research/oct20-handoff`. No remote push was performed.

The chat-delivered `chowlas-cosine-research-updates-2026-10-20.bundle` is an
incremental bundle. It requires the public base commit above; it does not
require the unavailable old local commit. It contains every new research
change on this handoff branch. The separately generated full-history bundle
was verified but exceeds the chat attachment-size limit.
The former unpublished local commit `446367d` was not recovered as a Git object.
Recovered reports and experiments are committed anew on the fetched history.
See [recovery index](RECOVERY_INDEX.md) and [documentation audit](RECOVERY_AUDIT.md)
for coverage and limitations.

## Safest review: start with a fresh public clone

```sh
git clone https://github.com/aygerix/chowlas-cosine.git chowla-handoff
cd chowla-handoff
git bundle verify /path/to/chowlas-cosine-research-updates-2026-10-20.bundle
git fetch /path/to/chowlas-cosine-research-updates-2026-10-20.bundle \
  refs/heads/research/oct20-handoff:refs/heads/research/oct20-handoff
git switch research/oct20-handoff
git log -2 --format=fuller
git status --short
```

Start with `.research/STATE.md` and `.research/RECOVERY_INDEX.md`.
The incremental bundle cannot be cloned by itself into an empty repository.

## Bring the branch into an existing clone

First make sure your working tree is clean or save your local changes. Ensure
the public base is present; fetching the public remote can supply it. Then
verify and fetch the bundle without changing the checked-out branch:

```sh
git cat-file -e 3873843090179751cb8732f5c0e9dcd21c1188bc^{commit}
git bundle verify /path/to/chowlas-cosine-research-updates-2026-10-20.bundle
git fetch /path/to/chowlas-cosine-research-updates-2026-10-20.bundle \
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
