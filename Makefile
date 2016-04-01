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
