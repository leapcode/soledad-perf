#!/usr/bin/env python

"""
Preload the server database with a certain amount of documents so we can
receive them during the sync process and gather meaningful statistics for that
specific phase of sync.

Gets uuid, payload file path and amount of documents to preload from
"defaults.conf" config file:

  UUID = some-uuid
  PAYLOAD = /path/to/payload/file
  NUM_DOCS = 100
"""

import os
from ConfigParser import ConfigParser
from leap.soledad.common.couch import CouchDatabase

parser = ConfigParser()
parser.read('defaults.conf')

UUID = parser.get('client', 'uuid')
PAYLOAD = parser.get('sync', 'payload')
NUM_DOCS = int(parser.get('sync', 'num_docs'))

db = CouchDatabase.open_database(
    'http://127.0.0.1:5984/user-%s' % UUID,
    False)  # should create database?

payload = None
if os.path.isfile(PAYLOAD):
    with open(PAYLOAD, 'r') as f:
        payload = f.read()

for i in xrange(NUM_DOCS):
    db.create_doc({'payload': payload})

db.close()
