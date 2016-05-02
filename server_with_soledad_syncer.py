# -*- coding: utf-8 -*- 
#!/usr/bin/env python


import os
import datetime
from klein import run, route, resource
from twisted.internet import reactor

import soledad_sync as sync


@route('/start-sync')
def home(request):
    print "GOT REQUEST FOR STARTING SYNC..."
    d = sync.upload_soledad_stuff()
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
    return "%d %d" % (pid, sync.phase * 50)


if __name__ == "__main__":
    run("localhost", 8080)
