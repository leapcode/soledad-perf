#!/usr/bin/env python

# This is a multiprocessing blobs server, mostly copied from:
# https://stackoverflow.com/questions/10077745/twistedweb-on-multicore-multiprocessor

from argparse import ArgumentParser

from multiprocessing import cpu_count
from os import environ
from sys import argv, executable, stdout
from socket import AF_INET

from twisted.internet import reactor
from twisted.python import log
from twisted.web.server import Site
from twisted.web.resource import Resource

from leap.soledad.server import get_config
from leap.soledad.server import BlobsResource


def run_server(fd=None, port=None, procs=None, verbose=False):
    if args.verbose:
        log.startLogging(stdout)
        environ['SOLEDAD_LOG_TO_STDOUT'] = '1'

    config = get_config()
    path = config["blobs_path"]
    if not port:
        port = int(config["blobs_port"])

    root = Resource()
    root.putChild('blobs', BlobsResource("filesystem", path))
    factory = Site(root)

    if fd is None:
        # Create a new listening port and several other
        # processes to help out.
        if procs is None:
            procs = cpu_count()
        log.msg('A total of %d processes will listen on port %d.' % (procs, port))
        port = reactor.listenTCP(port, factory)
        for i in range(procs - 1):
            reactor.spawnProcess(
                None, executable, [executable, __file__, str(port.fileno())],
                childFDs={0: 0, 1: 1, 2: 2, port.fileno(): port.fileno()},
                env=environ)
    else:
        # Another process created the port, just start listening on it.
        log.msg('Adopting file descriptor %d...' % fd)
        port = reactor.adoptStreamPort(fd, AF_INET, factory)

    reactor.run()


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('fd', nargs='?', type=int, help='A file descriptor to adopt.')
    parser.add_argument('--verbose', '-v', action='store_true', help='Output logs.')
    parser.add_argument('--port', '-p', type=int, help='The port in which to listen.')
    parser.add_argument('--procs', '-P', type=int, help='Total number of processes.')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    run_server(fd=args.fd, port=args.port, procs=args.procs, verbose=args.verbose)
