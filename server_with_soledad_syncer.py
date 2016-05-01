# -*- coding: utf-8 -*- 
#!/usr/bin/env python


import os
from klein import run, route, resource
import soledad_sync as sync
from twisted.internet import reactor
import datetime


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


if __name__ == "__main__":
    run("localhost", 8080)
