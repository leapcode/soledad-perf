DIR    = /tmp/blobs
PORT   = 8000
URI    = http://127.0.0.1:8000/blobs/user
UUID   = $(shell uuidgen)
PROCS ?= 4

all: multiproc

server: killall
	python blobs-server.py $(DIR) $(PORT)

multiproc:
	python multiproc.py --procs $(PROCS)

roundrobin: killall
	/usr/sbin/haproxy -D -f haproxy/roundrobin-$(PROCS).cfg

killall:
	-killall -9 haproxy

data:
	dd if=/dev/urandom of=/tmp/data bs=1024 count=100

list:
	curl -X GET $(URI)/

put:
	curl -X PUT $(URI)/$(UUID) --data-binary @/tmp/data

get:
	UUID=$(UUID); \
	curl -X PUT $(URI)/$${UUID} --data-binary @/tmp/data; \
	curl -X GET $(URI)/$${UUID} > /dev/null

delete:
	UUID=$(UUID); \
	curl -X PUT $(URI)/$${UUID} --data-binary @/tmp/data; \
	curl -X DELETE $(URI)/$${UUID}

put-ab:
	ab -c 10 -n 1000 -T /tmp/data $(URI)/$(UUID)


.PHONY: server multiproc roundrobin killall
