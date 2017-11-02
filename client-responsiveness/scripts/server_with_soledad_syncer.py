# -*- coding: utf-8 -*- 
#!/usr/bin/env python


import os
from klein import run, route, resource
import soledad_sync as sync
from twisted.internet import reactor
import datetime


@route('/create-docs')
def create_docs(request):
    d = sync.create_docs()
    return d


@route('/start-sync')
def start_sync(request):
    d = sync.start_sync()
    return d


@route('/ping')
def ping(request):
    return 'easy!'


@route('/pid')
def pid(request):
    return str(os.getpid())


@route('/stop')
def stop(request):
    reactor.callLater(1, reactor.stop)
    return ''

@route('/stats')
def stats(request):
    pid = os.getpid()
    sync_phase, sync_exchange_phase = sync.stats()
    return "%d %d %d" % (pid, sync_phase, sync_exchange_phase)


if __name__ == "__main__":
    run("localhost", 8080)
