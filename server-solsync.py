#!/usr/bin/env python
from klein import run, route

import soledad_sync as sync


s = None


@route('/start-sync')
def home(request):
    print "GOT REQUEST FOR STARTING SYNC..."
    d = sync.upload_soledad_stuff(s)
    return d


@route('/ping')
def ping(request):
    return 'easy!'

if __name__ == "__main__":
    global s
    s = sync._get_soledad_instance_from_uuid(
        sync.UUID, 'pass', '/tmp/soledadsync', sync.HOST, '', '')

    run("localhost", 8080)
