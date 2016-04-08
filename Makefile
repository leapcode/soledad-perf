# Simple PoC toys

perf:
	httperf --server localhost --port 8080 --num-calls 200 --num-conns 20 --uri /

perf-little:
	httperf --server localhost --port 8080 --num-calls 5 --num-conns 20 --uri /

perf-easy:
	httperf --server localhost --port 8080 --num-calls 5 --num-conns 20 --uri /hi

inline-server:
	python server.py

thread-server:
	python server2.py

ampoule-server:
	python server3.py

# Actual soledad sync

soledad-sync-server:
	python server-solsync.py

measure-ping:
	httperf --server localhost --port 8080 --num-calls 5 --num-conns 20 --uri /ping

trigger-sync:
	time curl localhost:8080/start-sync

measure-series:
	# TODO make sure we have restarted the server, send SIGNUP ?
	# TODO rm series.log, name it with a timestamp
	# TODO measure, first of all, the number of seconds from the beginning!!! (right now it's biased)
	# TODO add cpu/ram usage (ping command COULD RETURN THAT!)
	rm -f /tmp/soledadsync/*
	rm -f series.log
	python series-ping.py

graph-series:
	data=series.log ./graphit
