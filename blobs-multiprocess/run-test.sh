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


ab-get() {
  action=${1}
  procs=${2}
  amount=${3}
  size=${4}
  statement="make stress-get UUID=blob"
  python -c "import timeit; t = timeit.timeit('import os; os.system(\'${statement} > /dev/null\');', number=5); print t / 5"
  echo "${procs} ${action} ${amount} ${size} ${time}"
}


ab-baseline() {
  make ab-get URI=http://127.0.0.1:8000/
}


ab-put() {
  port=${1}
  if [ -z "${port}" ]; then port=8000; fi
  make ab-put URI=http://127.0.0.1:${port}/blobs/user/blob_id
}


ab-get() {
  make ab-get URI=http://127.0.0.1:8000/blobs/user/blob_id
}


ab-list() {
  make ab-get URI=http://127.0.0.1:8000/blobs/user/
}


ab-flag() {
  make ab-flag URI=http://127.0.0.1:8000/blobs/user/blob_id
}


ab-delete() {
  make ab-delete URI=http://127.0.0.1:8000/blobs/user/blob_id
}


run_test() {
  echo "" > results.txt
  #for procs in 1 2 4 8; do
  for procs in 1 2 3 4; do
    echo ":: Running tests for ${procs} proceesses..."

    # setup
    make clean
    make data SIZE=56
    start_multiproc ${procs}
    sleep 2

    echo ":::: Running baseline test..."
    result="${procs} baseline $(ab-baseline)"
    echo ${result}
    echo ${result} >> results.txt
    sleep 2
    #read temp

    echo ":::: Running put test..."
    result="${procs} put $(ab-put)"
    echo ${result}
    echo ${result} >> results.txt
    sleep 2
    #read temp

    # setup tests that depend on existence of blobs
    kill_multiproc
    make clean
    make kill-haproxy
    for port in 8001 8002 8003 8004; do
      echo ":::::: creating blobs prefixed with ${port}-..."
      make server PORT=${port} > /dev/null &!
      sleep 1
      ab-put ${port}
      #read temp
      make kill-server
    done
    sleep 2

    echo ":::: Running list test..."
    start_multiproc ${procs}
    result="${procs} list $(ab-list)"
    echo ${result}
    echo ${result} >> results.txt
    sleep 2

    echo ":::: Running flag test..."
    make flag
    result="${procs} flag $(ab-flag)"
    echo ${result}
    echo ${result} >> results.txt
    sleep 2

    echo ":::: Running get test..."
    kill_multiproc
    start_multiproc ${procs}
    result="${procs} get $(ab-get)"
    echo ${result}
    echo ${result} >> results.txt
    sleep 2

    echo ":::: Running delete test..."
    kill_multiproc
    start_multiproc ${procs}
    result="${procs} delete $(ab-delete)"
    echo ${result}
    echo ${result} >> results.txt
    kill_multiproc
  done
}


run_test
