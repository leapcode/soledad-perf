# Actual soledad sync

soledad-sync-server:
	twistd -n web --port 8080 --class=server_with_soledad_syncer.resource

soledad-sync-server-lineprof:
	kernprof -l server_with_soledad_syncer.py


soledad-sync-server-debug:
	#twistd --profile=stats_obj --profiler=cProfile -n web --port 8080 --class=server_with_soledad_syncer.resource
	python -m cProfile -o sync.cprofile server_with_soledad_syncer.py 

view-lineprofile:
	python -m line_profiler server_with_soledad_syncer.py.lprof


view-profile:
	cprofilev -f sync.cprofile

measure-ping:
	httperf --server localhost --port 8080 --num-calls 5 --num-conns 20 --uri /ping

trigger-sync:
	#time curl localhost:8080/start-sync
	curl localhost:8080/start-sync

measure-series:
	# TODO make sure we have restarted the server, send SIGNUP ?
	# TODO rm series.log, name it with a timestamp
	# TODO measure, first of all, the number of seconds from the beginning!!! (right now it's biased)
	# TODO add cpu/ram usage (ping command COULD RETURN THAT!)
	rm -f /tmp/soledadsync/*
	rm -f series.log
	python measure-perf-series.py

graph-series:
	data=series.log ./graphit
