#!/bin/sh

export SOLEDAD_STATS=1

# assume the cli is in the environment
CLI="soledad_test_env.py"

_server_setup() {
  ${CLI} couch start
  ${CLI} shared-db create
  ${CLI} token-db create
  ${CLI} token-db insert-token #--uuid 1234567890abcdefa --auth-token an-auth-token2
  ${CLI} soledad-server start
}

function _server_reset() {
  ${CLI} user-db delete #--uuid 1234567890abcdefa
  ${CLI} user-db create #--uuid 1234567890abcdefa
  ./scripts/create_payload.py
  ./scripts/preload_server_database.py
}

function _client_reset() {
  rm -rf /tmp/soledad_client_test
}

_server_setup

if [ ! "${SKIP_SERVER_RESET}" ]; then
  _server_reset
fi
if [ ! "${SKIP_CLIENT_RESET}" ]; then
  _client_reset
fi

# start local test server
make soledad-sync-server | grep -v stats | grep -v ping  &
sleep 5

# create documents
make trigger-create-docs

# launch background series measurement
make measure-series &
sleep 5  # wait a bit for some data points

# trigger sync and stop afterwards
make trigger-sync
make trigger-stop
