# -*- coding: utf-8 -*- 
#!/usr/bin/env python
import os

from klein import run, route, resource

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


if __name__ == "__main__":
    #s = sync._get_soledad_instance_from_uuid(
        #sync.UUID, 'pass', '/tmp/soledadsync', sync.HOST, '', '')

    run("localhost", 8080)
