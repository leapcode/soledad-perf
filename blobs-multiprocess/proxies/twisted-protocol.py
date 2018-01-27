#!/usr/bin/env python

import sys

from io import BytesIO
from argparse import ArgumentParser
from twisted.internet import protocol, reactor, task
from twisted.protocols import basic, policies
from twisted.python import log


LISTEN_PORT = 8080
SERVER_PORT = 2626
SERVER_ADDR = "127.0.0.1"


class ProxyClient(basic.LineReceiver, policies.TimeoutMixin):

    def __init__(self, revproxy):
        self.revproxy = revproxy

    def connectionMade(self):
        self.revproxy.buffer.attachTarget(self.transport)

    def lineReceived(self, line):
        self.resetTimeout()
        self.revproxy.transport.write(line)
        self.revproxy.transport.write('\r\n')
        self.setRawMode()

    def rawDataReceived(self, data):
        self.resetTimeout()
        self.revproxy.transport.write(data)

    def connectionLost(self, reason=protocol.connectionDone):
        self.revproxy.transport.loseConnection()


class ProxyClientFactory(protocol.ClientFactory):

    protocol = ProxyClient

    def __init__(self, revproxy):
        self.revproxy = revproxy

    def buildProtocol(self, addr):
        p = self.protocol(self.revproxy)
        p.factory = self
        return p

    def clientConnectionFailed(self, connector, reason):
        log.msg("Connection failed: %r" % reason)
        self.revproxy.transport.loseConnection()


class Buffer(object):

    chunk_size = 2 ** 14

    def __init__(self):
        self.buffer = BytesIO()
        self.target = None
        self.buffered = True

    def attachTarget(self, target):
        self.target = target
        task.cooperate(self._gen_data())

    def _gen_data(self):
        current = self.buffer.tell()
        self.buffer.seek(0, 0)
        data = self.buffer.read(self.chunk_size)
        self.last = len(data)
        self.buffer.seek(current)
        while data:
            yield
            self.target.write(data)
            current = self.buffer.tell()
            self.buffer.seek(self.last)
            data = self.buffer.read(self.chunk_size)
            self.last += len(data)
            self.buffer.seek(current)
        self.buffered = False

    def write(self, data):
        if self.buffered:
            self.buffer.write(data)
        else:
            self.target.write(data)


class ReverseProxy(basic.LineReceiver, policies.TimeoutMixin):

    routes = {'blobs': (SERVER_ADDR, SERVER_PORT)}

    def __init__(self):
        self.buffer = Buffer()

    def getRoute(self, method, path):
        backend = path.split('/')[1]
        return self.routes[backend]

    def lineReceived(self, line):
        self.resetTimeout()
        self.buffer.write(line)
        self.buffer.write('\r\n')
        method, path, version = line.split()
        host, port = self.getRoute(method, path)
        factory = ProxyClientFactory(self)
        reactor.connectTCP(host, port, factory)
        self.setRawMode()

    def rawDataReceived(self, data):
        self.resetTimeout()
        self.buffer.write(data)


def main():
    args = parse_args()
    if args.verbose:
        log.startLogging(sys.stdout)

    ReverseProxy.routes = {'blobs': (args.server_addr, args.server_port)}
    factory = protocol.ServerFactory()
    factory.protocol = ReverseProxy
    reactor.listenTCP(args.listen_port, factory)
    reactor.run()


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Output logs to stdout.')
    parser.add_argument('--listen-port', '-p', type=int, default=LISTEN_PORT,
                        help='The port in which to listen.')
    parser.add_argument('--server-addr', '-H', type=str, default=SERVER_ADDR,
                        help='The port to which connect.')
    parser.add_argument('--server-port', '-P', type=int, default=SERVER_PORT,
                        help='The port to which connect.')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
