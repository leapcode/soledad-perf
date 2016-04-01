perf:
	httperf --server localhost --port 8080 --num-calls 200 --num-conns 10 --uri /

inline-server:
	python server.py

thread-server:
	python server2.py

ampoule-server:
	python server3.py
