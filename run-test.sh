#!/bin/sh

CLI="python /home/drebs/projetos/leap/repos/soledad/scripts/soledad_test_env/soledad_test_env.py"
${CLI} couch start
${CLI} user-db delete
${CLI} user-db create
${CLI} shared-db create
${CLI} token-db create
${CLI} token-db insert-token
${CLI} soledad-server start

make soledad-sync-server | grep -v stats | grep -v ping  &
sleep 5
make measure-series &
sleep 5
make trigger-sync
