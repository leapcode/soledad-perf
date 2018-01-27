#!/usr/bin/env python

import sys
from argparse import ArgumentParser
from twisted.internet import reactor
from twisted.web import proxy, http
from twisted.python import log


LISTEN_PORT = 8080
SERVER_PORT = 8001


class BlobsClientFactory(proxy.ProxyClientFactory):

    host = '127.0.0.1'
    port = SERVER_PORT


class BlobsRequest(proxy.ReverseProxyRequest):

    proxyClientFactoryClass = BlobsClientFactory
    factory = BlobsClientFactory

    def finish(self):
        return proxy.ReverseProxyRequest.finish(self)


class BlobsReverseProxy(proxy.ReverseProxy):

    requestFactory = BlobsRequest


def main():
    args = parse_args()
    if args.verbose:
        log.startLogging(sys.stdout)
    start_revproxy(args.listen_port)


def start_revproxy(listen_port):
    factory = http.HTTPFactory()
    factory.protocol = BlobsReverseProxy
    reactor.listenTCP(listen_port, factory)
    reactor.run()


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Output logs to stdout.')
    parser.add_argument('--listen-port', '-p', type=int, default=LISTEN_PORT,
                        help='The port in which to listen.')
    parser.add_argument('--server-port', '-P', type=int, default=SERVER_PORT,
                        help='The port to which connect.')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
