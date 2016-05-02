import os
import json
from ConfigParser import ConfigParser
from leap.soledad.client.api import Soledad
from twisted.internet import defer


# get configs from file
parser = ConfigParser()
parser.read('defaults.conf')
HOST = parser.get('server', 'host')
UUID = parser.get('client', 'uuid')
NUM_DOCS = int(parser.get('sync', 'num_docs'))
PAYLOAD = parser.get('sync', 'payload')
AUTH_TOKEN = parser.get('sync', 'auth-token')
STATS_FILE = parser.get('test', 'stats-file')




DO_THESEUS = os.environ.get('THESEUS', False)


phase = 0


def _get_soledad_instance_from_uuid(uuid, passphrase, basedir, server_url,
                                    cert_file, token):
    secrets_path = os.path.join(basedir, '%s.secret' % uuid)
    local_db_path = os.path.join(basedir, '%s.db' % uuid)
    return Soledad(
        uuid,
        unicode(passphrase),
        secrets_path=secrets_path,
        local_db_path=local_db_path,
        server_url=server_url,
        cert_file=cert_file,
        auth_token=token,
        defer_encryption=True,
        syncable=True)


def onSyncDone(result):
    #-------- PHASE 3: sync done.
    global phase
    phase += 1
    print "SYNC DONE!", result


def upload_soledad_stuff():
    global phase

    with open(PAYLOAD, 'r') as f:
        payload = f.read()

    if DO_THESEUS:
        from theseus import Tracer
        t = Tracer()
        t.install()

    s = _get_soledad_instance_from_uuid(
        UUID, 'pass', '/tmp/soledadsync', HOST, '', AUTH_TOKEN)

    def dumpStats(_):
        stats = s.sync_stats()
        with open(STATS_FILE, 'w') as f:
            f.write(json.dumps(stats))

    def do_sync(_):
        global phase
        #-------- PHASE 2: docs created, defer sync
        phase += 1
        d = s.sync()
        d.addCallback(onSyncDone)
        d.addCallback(dumpStats)
        return d

    def stop_tracing(_):
        if DO_THESEUS:
            with open('callgrind.theseus', 'wb') as outfile:
                t.write_data(outfile)
            print "STOPPED TRACING, DUMPED IN CALLGRIND.THESEUS<<<<"

    cd = []
    #-------- PHASE 1: deferring doc creation
    phase += 1
    for i in range(NUM_DOCS):
        cd.append(s.create_doc({'payload': payload}))
    d1 = defer.gatherResults(cd)

    # XXX comment out to nuke out the actual sync
    d1.addCallback(do_sync)
    d1.addCallback(stop_tracing)

    return d1
