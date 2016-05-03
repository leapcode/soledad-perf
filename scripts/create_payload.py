#!/usr/bin/env python

"""
Create a payload file in disk to use during tests. Reads the name of the file
and the intended size of the payload from the "defaults.conf" file:

  PAYLOAD = /path/to/payload/file
  PAYLOAD_SIZE = 500  # in Kb
"""

import os
from ConfigParser import ConfigParser

parser = ConfigParser()
parser.read('defaults.conf')

PAYLOAD = parser.get('sync', 'payload')
PAYLOAD_SIZE = int(parser.get('sync', 'payload_size')) * 1024

if os.path.isfile(PAYLOAD):
    os.unlink(PAYLOAD)

content = 'a' * 1024

with open(PAYLOAD, 'w') as f:
    length = 0
    while length < PAYLOAD_SIZE:
        f.write(content)
        length += len(content)
