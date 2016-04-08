import os
from leap.soledad.client.api import Soledad
from twisted.internet import defer

# EDIT THIS TO MATCH YOUR TEST ENVIRONMENT -------------
UUID = 'deadbeef'
#HOST = 'http://futeisha:2323'
HOST = 'http://localhost:2323'
NUM_DOCS = 5
PAYLOAD = '/tmp/payload'
# ------------------------------------------------------


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

    s = _get_soledad_instance_from_uuid(
        UUID, 'pass', '/tmp/soledadsync', HOST, '', '')

    def do_sync(_):
        d = s.sync()
        d.addCallback(onSyncDone)
        return d

    cd = []
    for i in range(NUM_DOCS):
        cd.append(s.create_doc({'payload': payload}))
    d1 = defer.gatherResults(cd)
    d1.addCallback(do_sync)
    return d1
