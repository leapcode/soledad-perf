#!/bin/bash

# Run Multiprocessing Test
# ========================
#

# This script measures the time of several interactions with the Blobs Server
# and outputs them to a text file.
#
# The different test scenarios are:
#   - 1, 2, 4, and 8 server processes.
#   - several client actions (baseline, list, put, get, flag, delete)
#   - 
#
# Client actions
# --------------

# Baseline: is a GET / to a dummy server that returns an empty reply. Nothing
# can be faster than this.

# List: is a GET /blobs/username, which lists the (empty) set of blobs stored
# in the server.

set -e


kill_multiproc() {
  pids=$(ps aux | grep python | grep "\(multiproc\|blobs-server\)" \
         | grep -v grep | sed -e "s/\s\+/ /g" | cut -d' ' -f 2)
  if [ ! -z "${pids}" ]; then
    for pid in ${pids}; do
      kill -9 ${pid}
    done
  fi
}


start_multiproc() {
  procs=${1}
  kill_multiproc
  make multiproc PROCS=${procs} > /dev/null &
  sleep 3
  make roundrobin PROCS=${procs}
  sleep 1
}


get_best() {
  statement=$*
  result=$(python -m timeit -n 1 -r 5 -s "import os" "os.system('${statement}')")
  best=$(echo $result | sed -e s/.\*best\ of\ 5:\ // -e s/per\ loop//)
  echo $best
}


get_mean() {
  statement=$*
  python -c "import timeit; t = timeit.timeit('import os; os.system(\'./${statement} > /dev/null\');', number=5); print t / 5"
}


request() {
  action=${1}
  procs=${2}
  amount=${3}
  size=${4}
  best=$(get_mean ./request.py --${action} ${amount} ${size})
  echo "${procs} ${action} ${amount} ${size} ${best}"
}


run_test() {
  for procs in 1 2 4 8; do
    start_multiproc ${procs}
    for action in baseline list put get flag delete; do
      #for amountsize in "10 1000" "100 100" "1000 10"; do
      for amountsize in "1000 10"; do
        rm -rf /tmp/blobs/*
        request ${action} ${procs} ${amountsize} >> results.txt
      done
    done
    kill_multiproc
  done
}

run_test
