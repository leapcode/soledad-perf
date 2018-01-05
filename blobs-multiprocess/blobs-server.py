#!/usr/bin/env python

import errno
import os

from argparse import ArgumentParser
from sys import stdout

from twisted.internet import reactor
from twisted.python import log
from twisted.web.resource import Resource
from twisted.web.server import Site

from leap.soledad.server._blobs import BlobsResource


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('dir', type=str,
                        help="The directory to store blobs.")
    parser.add_argument('port', type=int,
                        help="The port in which to listen.")
    args = parser.parse_args()
    return args


class DummyResource(Resource):

    def render_GET(self, request):
        return ''


def start_server(dir, port):
    resource = Resource()
    resource.putChild("", DummyResource())
    resource.putChild("blobs", BlobsResource("filesystem", dir))
    site = Site(resource)
    reactor.listenTCP(port, site)


def main(dir, port):
    mkdir_p(dir)
    log.startLogging(stdout)
    start_server(dir, port)
    reactor.run()


if __name__ == "__main__":
    args = parse_args()
    main(args.dir, args.port)
