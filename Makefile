perf:
	httperf --server localhost --port 8080 --num-calls 200 --num-conns 10 --uri /

server:
	python server.py
