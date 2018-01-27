#!/usr/bin/env python

from argparse import ArgumentParser
from sys import stdout

from twisted.internet import reactor
from twisted.python import log
from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.web.proxy import ReverseProxyResource


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--verbose', '-v', action='store_true', help='Output logs to stdout.')
    parser.add_argument('port', type=int,
                        help="The port in which to listen.")
    parser.add_argument('destport', type=int,
                        help="The port to which forward requests.")
    args = parser.parse_args()
    return args


class DummyResource(Resource):

    def render_GET(self, request):
        return ''


def start_server(port, destport):
    revproxy = ReverseProxyResource("127.0.0.1", destport, "/blobs")
    resource = Resource()
    resource.putChild("", DummyResource())
    resource.putChild("blobs", revproxy)
    site = Site(resource)
    reactor.listenTCP(port, site)


def main(port, destport):
    start_server(port, destport)
    reactor.run()


if __name__ == "__main__":
    args = parse_args()
    if args.verbose:
        log.startLogging(stdout)
    main(args.port, args.destport)
