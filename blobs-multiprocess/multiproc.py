#!/usr/bin/env python

from argparse import ArgumentParser
from twisted.internet import reactor
from twisted.internet.protocol import ProcessProtocol
from twisted.python.failure import Failure


class BlobsServerProtocol(ProcessProtocol):

    def outReceived(self, data):
        if not isinstance(data, Failure):
            data = data.strip()
        if data:
            print(data)

    def errorReceived(self, data):
        if not isinstance(data, Failure):
            data = data.strip()
        if data:
            print(data)

    def processEnded(self, data):
        if not isinstance(data, Failure):
            data = data.strip()
        if data:
            print(data)

    # def processExited(self, data):
    #     print(data)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--procs', type=int, default=4,
                        help="the number of processes to spawn")
    args = parser.parse_args()
    return args


def spawn_servers(procs):
    protocol = BlobsServerProtocol()
    children = []
    python = '/home/drebs/.virtualenvs/apps/bin/python'
    for port in range(8001, 8001 + procs):
        args = [python, './blobs-server.py', '/tmp/blobs', str(port)]
        child = reactor.spawnProcess(protocol, python, args)
        children.append(child)


def main():
    args = parse_args()
    spawn_servers(args.procs)
    reactor.run()


if __name__ == "__main__":
    main()
