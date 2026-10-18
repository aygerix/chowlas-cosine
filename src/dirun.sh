#!/bin/zsh
# Run one computation on the GCP VM "dirichlet" (project littlewood-paley-8375, us-east1-b; c2d-standard-8: 8 vCPU,
# 32 GB, Ubuntu 24.04, gcc 13, venv ~/chowla_venv with numpy/scipy/mpmath/python-flint/highspy). Assigned to this
# project by the user on 2026-10-18; the lead AND its agents run all calculations here. Do not touch the VM "fejer".
#   src/dirun.sh [-c cores] [-m GB] [-t seconds] <command ...>    e.g.  src/dirun.sh -c 8 -t 7200 python src/exh2_driver.py 43 60
# -c: CPU quota and thread/worker count (default 4, max 8; use 8 only for a job that should own the machine)
# -m: memory cap enforced by the kernel, no swap (default 12 GB, max 30)
# -t: wall-time limit (default 3600 s, max 86400 s)
# Runs from ~/chowla_cosine on the VM, a copy of this project (code + small data; .venv, .git, lean/.lake, .build and
# files >= 20 MB are not copied). `python` means ~/chowla_venv/bin/python. New/changed files under 20 MB are copied back.
# C sources are compiled on the VM by the scripts themselves (cc -O3 -march=native); never copy local binaries.
c=4; m=12; t=3600
while getopts "c:m:t:" o; do case $o in c) c=$OPTARG;; m) m=$OPTARG;; t) t=$OPTARG;; *) exit 2;; esac; done
shift $((OPTIND-1))
(( $# )) || { sed -n 2,11p $0 >&2; exit 2; }
(( c > 8 )) && c=8; (( c < 1 )) && c=1
(( m > 30 )) && m=30
(( t > 86400 )) && t=86400
R=/Users/jmercedes/Desktop/Projects/Research/chowla-cosine
# DIRICHLET_IP (optional) skips the gcloud lookup, e.g. for codex agents whose sandbox cannot write ~/.config/gcloud.
IP=${DIRICHLET_IP:-$(gcloud compute instances describe dirichlet --zone us-east1-b --project littlewood-paley-8375 \
       --format='get(networkInterfaces[0].accessConfigs[0].natIP)' 2>/dev/null)}
[[ -n $IP ]] || { echo "dirun.sh: cannot resolve dirichlet's IP (is the VM running?)" >&2; exit 255; }
SSH=(ssh -i $HOME/.ssh/google_compute_engine -o UserKnownHostsFile=$HOME/.ssh/google_compute_known_hosts
     -o HostKeyAlias=compute.2840844007150016813 -o BatchMode=yes -o ConnectTimeout=15 -o ServerAliveInterval=60)
H=jmercedes@$IP
$SSH $H true || { echo "dirun.sh: ssh to dirichlet failed" >&2; exit 255; }
tag=$(date +%s)-$$
rsync -a --update --max-size=20M -e "${(j: :)SSH}" --exclude '.venv' --exclude '.git' --exclude 'lean/.lake' \
  --exclude '*.pyc' --exclude '.build' --exclude '.DS_Store' --exclude '__pycache__' $R/ ${H}:chowla_cosine/
args=("$@"); [[ ${args[1]} == python ]] && args[1]=/home/jmercedes/chowla_venv/bin/python
cmd=${(j: :)${(q)args}}
$SSH $H "touch /tmp/ccmark.$tag; cd ~/chowla_cosine && sudo systemd-run --quiet --scope --uid=jmercedes \
  -p MemoryMax=${m}G -p MemorySwapMax=0 -p CPUQuota=$((100 * c))% \
  --setenv=PATH=/home/jmercedes/chowla_venv/bin:/opt/gurobi1303/linux64/bin:/usr/local/bin:/usr/bin:/bin --setenv=HOME=/home/jmercedes \
  --setenv=GUROBI_HOME=/opt/gurobi1303/linux64 --setenv=LD_LIBRARY_PATH=/opt/gurobi1303/linux64/lib \
  --setenv=GRB_LICENSE_FILE=/opt/gurobi1303/gurobi.lic \
  --setenv=CHOWLA_WORKERS=$c --setenv=OMP_NUM_THREADS=$c --setenv=OPENBLAS_NUM_THREADS=$c \
  --setenv=MKL_NUM_THREADS=$c --setenv=PYTHONUNBUFFERED=1 --working-directory=/home/jmercedes/chowla_cosine \
  timeout -s KILL $t $cmd < /dev/null 2>&1; rc=\$?; \
  find . -newer /tmp/ccmark.$tag -type f -size -20M ! -name '*.pyc' ! -path './.build/*' ! -path '*/__pycache__/*' \
    > /tmp/ccnew.$tag; exit \$rc"
rc=$?
$SSH $H "cat /tmp/ccnew.$tag; rm -f /tmp/ccmark.$tag /tmp/ccnew.$tag" > /tmp/ccnew.$tag 2>/dev/null
[[ -s /tmp/ccnew.$tag ]] && rsync -a --update -e "${(j: :)SSH}" --files-from=/tmp/ccnew.$tag ${H}:chowla_cosine/ $R/
rm -f /tmp/ccnew.$tag
(( rc == 137 || rc == 124 )) && echo "dirun.sh: job killed (time limit $t s or memory limit ${m} GB)" >&2
exit $rc
