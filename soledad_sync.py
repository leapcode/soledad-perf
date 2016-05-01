import os
from leap.soledad.client.api import Soledad
from twisted.internet import defer

# EDIT THIS TO MATCH YOUR TEST ENVIRONMENT -------------
UUID = '1234567890abcdef'
#HOST = 'http://futeisha:2323'
HOST = 'http://localhost:2424'
NUM_DOCS = 100
PAYLOAD = '/tmp/payload'
# ------------------------------------------------------



DO_THESEUS = os.environ.get('THESEUS', False)


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
    print "SYNC DONE!", result


def upload_soledad_stuff():

    with open(PAYLOAD, 'r') as f:
        payload = f.read()

    if DO_THESEUS:
        from theseus import Tracer
        t = Tracer()
        t.install()

    s = _get_soledad_instance_from_uuid(
        UUID, 'pass', '/tmp/soledadsync', HOST, '', 'an-auth-token')

    def do_sync(_):
        d = s.sync()
        d.addCallback(onSyncDone)
        return d

    def stop_tracing(_):
        if DO_THESEUS:
            with open('callgrind.theseus', 'wb') as outfile:
                t.write_data(outfile)
            print "STOPPED TRACING, DUMPED IN CALLGRIND.THESEUS<<<<"

    cd = []
    for i in range(NUM_DOCS):
        cd.append(s.create_doc({'payload': payload}))
    d1 = defer.gatherResults(cd)



    # XXX comment out to nuke out the actual sync
    #d1.addCallback(do_sync)
    d1.addCallback(stop_tracing)


    return d1
