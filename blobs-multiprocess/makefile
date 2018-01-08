DIR       = /tmp/blobs
PORT      = 8000
BASE_URI  = http://127.0.0.1:8000
BLOBS_URI = $(BASE_URI)/blobs/user
UUID      = $(shell uuidgen)
PROCS    ?= 4
SIZE     ?= 56

all: multiproc

server:
	python blobs-server.py $(DIR) $(PORT)

multiproc: roundrobin
	python multiproc.py --procs $(PROCS)

roundrobin: kill-haproxy
	/usr/sbin/haproxy -D -f haproxy/roundrobin-$(PROCS).cfg

kill-haproxy:
	-killall -9 haproxy

kill-server:
	pid=$$(ps aux | grep python\ blobs-server.py | grep -v grep | awk "{print \$$2}"); \
	kill -9 $${pid}

data:
	dd if=/dev/urandom of=/tmp/data bs=1024 count=$(SIZE)

list:
	curl -X GET $(BLOBS_URI)/

put: data
	curl -X PUT $(BLOBS_URI)/$(UUID) --data-binary @/tmp/data

get:
	UUID=$(UUID); \
	curl -X PUT $(BLOBS_URI)/$${UUID} --data-binary @/tmp/data; \
	curl -X GET $(BLOBS_URI)/$${UUID} > /dev/null

delete:
	UUID=$(UUID); \
	curl -X PUT $(BLOBS_URI)/$${UUID} --data-binary @/tmp/data; \
	curl -X DELETE $(BLOBS_URI)/$${UUID}

stress-baseline-ab: clean
	ab -c 10 -n 1000 http://127.0.0.1:8000/

stress-baseline: clean
	siege --concurrent=50 -t 5s http://127.0.0.1:8000/

stress-put: clean
	#ab -c 10 -n 1000 -T /tmp/data $(BLOBS_URI)/$(UUID)
	ab -c 10 -n 1000 -T /tmp/data $(BLOBS_URI)/$(UUID)

stress-get:
	@ab -c 10 -n 1000 -q $(BASE_URI)/ | grep ^Requests | awk '{print $$4}'

ab-get:
	@ab -c 10 -n 1000 -q -m GET $(URI) | grep ^Requests | awk '{print $$4}'

ab-put:
	@ab -c 10 -n 1000 -q -u /tmp/data $(URI) | grep ^Requests | awk '{print $$4}'

ab-flag:
	@ab -c 10 -n 1000 -q -p /tmp/flag $(URI) | grep ^Requests | awk '{print $$4}'

ab-delete:
	@ab -c 10 -n 1000 -q -m DELETE $(URI) | grep ^Requests | awk '{print $$4}'

clean:
	rm -rf /tmp/blobs/*

flag:
	echo '["PROCESSING"]' > /tmp/flag


.PHONY: server multiproc roundrobin kill-server kill-haproxy
