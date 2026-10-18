#!/bin/zsh
# Run one computation on THIS LAPTOP under a memory guard, using at most 4 cores (user rule 2026-10-18; heavy or
# long jobs still prefer F4 via src/f4run.sh).
#   src/localrun.sh [-m GB] [-t seconds] [-s MB] <command ...>
# Threads: OMP/BLAS/vecLib/numexpr = 4 and CHOWLA_WORKERS=4 (process pools).  A watchdog polls every second and kills the
# job's whole process group if (a) its total RSS exceeds -m GB (default 3), (b) system swap use rises more than -s MB
# (default 512) above its value at launch, or (c) the wall time exceeds -t seconds (default 3600).  Exit 137 = killed.
# A leading `python` means the project venv .venv/bin/python (python-flint, highspy, numpy).
m=3; t=3600; s=512
while getopts "m:t:s:" o; do case $o in m) m=$OPTARG;; t) t=$OPTARG;; s) s=$OPTARG;; *) exit 2;; esac; done
shift $((OPTIND-1))
(( $# )) || { sed -n 2,8p $0 >&2; exit 2; }
export OMP_NUM_THREADS=4 OPENBLAS_NUM_THREADS=4 MKL_NUM_THREADS=4 VECLIB_MAXIMUM_THREADS=4 NUMEXPR_NUM_THREADS=4
export CHOWLA_WORKERS=4 PYTHONUNBUFFERED=1
swapused() { sysctl -n vm.swapusage | awk '{v=$6; sub("M","",v); print int(v)}'; }
swap0=$(swapused); lim=$(( m * 1024 * 1024 )); t0=$SECONDS
args=("$@"); [[ ${args[1]} == python ]] && args[1]=/Users/jmercedes/Desktop/Projects/Research/chowla-cosine/.venv/bin/python
perl -e 'setpgrp(0,0); exec @ARGV or die "exec failed: $!"' -- "${args[@]}" &   # own process group = pid
pid=$!
pg=$pid
reason=""
while kill -0 $pid 2>/dev/null; do
  rss=$(ps -axo pgid=,rss= | awk -v g=$pg '$1==g {s+=$2} END {print s+0}')
  sw=$(swapused)
  if (( rss > lim )); then reason="RSS $((rss/1024)) MB > ${m} GB"
  elif (( sw - swap0 > s )); then reason="swap grew by $((sw - swap0)) MB"
  elif (( SECONDS - t0 > t )); then reason="wall time > ${t} s"; fi
  if [[ -n $reason ]]; then
    kill -TERM -$pg 2>/dev/null; sleep 2; kill -KILL -$pg 2>/dev/null
    echo "localrun.sh: job killed ($reason)" >&2; exit 137
  fi
  sleep 1
done
wait $pid
