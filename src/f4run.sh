#!/bin/zsh
# Run one heavy computation on the shared F4 server (f4-magma: 16 cores, 128 GB; shared with the Dujella team).
#   src/f4run.sh [-t seconds] [-m GB] <command ...>        e.g.  src/f4run.sh -t 7200 -m 16 python src/lns_milp.py 120 80 400 1
# Runs from ~/chowla_cosine on the server, a copy of this project (code + small data; .venv, .git, lean/.lake and files
# >= 20 MB are not copied). `python` means the project venv ~/chowla_venv (numpy, scipy, highspy, python-flint, mpmath).
# Memory is capped by the kernel (-m, default 8 GB, no swap); wall time by -t (default 3600 s, max 43200 s).
# New/changed files under 20 MB are copied back. Refuses to start while the server load is >= 12 (leave room for others).
t=3600; m=8
while getopts "t:m:" o; do case $o in t) t=$OPTARG;; m) m=$OPTARG;; *) exit 2;; esac; done
shift $((OPTIND-1))
(( $# )) || { sed -n 2,8p $0 >&2; exit 2; }
(( t > 43200 )) && t=43200
(( m > 64 )) && m=64
R=/Users/jmercedes/Desktop/Projects/Research/chowla-cosine
H=f4-magma
ssh -o ConnectTimeout=10 -o BatchMode=yes $H true 2>/dev/null || { echo "f4run.sh: server unreachable" >&2; exit 255; }
load=$(ssh $H "cut -d' ' -f1 /proc/loadavg")
(( ${load%.*} >= 12 )) && { echo "f4run.sh: server load is $load; wait or run a smaller job" >&2; exit 75; }
tag=$(date +%s)-$$
rsync -a --update --max-size=20M --exclude '.venv' --exclude '.git' --exclude 'lean/.lake' --exclude '*.pyc' \
  --exclude '.build' --exclude '.DS_Store' $R/ ${H}:chowla_cosine/
args=("$@"); [[ ${args[1]} == python ]] && args[1]=/home/ubuntu/chowla_venv/bin/python
cmd=${(j: :)${(q)args}}
ssh $H "touch /tmp/ccmark.$tag; cd ~/chowla_cosine && sudo systemd-run --quiet --scope --uid=ubuntu -p MemoryMax=${m}G -p MemorySwapMax=0 \
  --setenv=PATH=/home/ubuntu/chowla_venv/bin:/usr/local/bin:/usr/bin:/bin --working-directory=/home/ubuntu/chowla_cosine \
  timeout -s KILL $t $cmd < /dev/null 2>&1; rc=\$?; \
  find . -newer /tmp/ccmark.$tag -type f -size -20M ! -name '*.pyc' ! -path './.build/*' > /tmp/ccnew.$tag; exit \$rc"
rc=$?
ssh $H "cat /tmp/ccnew.$tag; rm -f /tmp/ccmark.$tag /tmp/ccnew.$tag" > /tmp/ccnew.$tag 2>/dev/null
[[ -s /tmp/ccnew.$tag ]] && rsync -a --update --files-from=/tmp/ccnew.$tag ${H}:chowla_cosine/ $R/
rm -f /tmp/ccnew.$tag
(( rc == 137 || rc == 124 )) && echo "f4run.sh: job killed (time limit $t s or memory limit ${m} GB)" >&2
exit $rc
