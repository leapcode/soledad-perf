#!/usr/bin/env python

from io import BytesIO
import time
import treq
from argparse import ArgumentParser
from twisted.internet import reactor, task, defer
from twisted.web.client import readBody, HTTPConnectionPool
from urlparse import urljoin
from uuid import uuid4


BASE_URI = 'http://127.0.0.1:8000/'
BLOBS_URI = urljoin(BASE_URI,
                    'blobs/{}/'.format(time.strftime('%Y-%m-%d_%H-%M-%s')))
CONCURRENT = 10

pool = HTTPConnectionPool(reactor)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('amount', type=int, help="the amount of blobs")
    parser.add_argument('size', type=int, help="size in blocks of 1024 bytes")
    parser.add_argument('--put', action='store_true',
                        help="noop")
    parser.add_argument('--baseline', action='store_true',
                        help="GET /")
    parser.add_argument('--list', action='store_true',
                        help="GET /blobs/")
    parser.add_argument('--get', action='store_true',
                        help="PUT + GET /blobs/someuser/someid")
    parser.add_argument('--flag', action='store_true',
                        help="PUT + POST /blobs/someuser/someid")
    parser.add_argument('--delete', action='store_true',
                        help="PUT + DELETE /blobs/someuser/someid")
    args = parser.parse_args()
    return args


def _finished(_, amount, size):
    print("Finished putting {} blobs of size {}K.".format(amount, size))
    reactor.stop()


def _error(failure):
    print("Failed: %r" % failure)
    reactor.stop()


def main(generator):
    cooperator = task.Cooperator()
    cooptask = cooperator.cooperate(generator)
    d = cooptask.whenDone()
    return d


def requests_generator(args):
    data = "a" * args.size * 1024

    def _get(_, uri):
        d = treq.get(uri, pool=pool)
        d.addCallback(lambda response: readBody(response))
        return d

    def _flag(_, uri):
        flags = BytesIO('["PROCESSING"]')
        d = treq.post(uri, data=flags, pool=pool)
        return d

    def _delete(_, uri):
        d = treq.delete(uri, pool=pool)
        return d

    deferreds = []
    for i in xrange(args.amount):
        if args.baseline:
            d = treq.get(BASE_URI, pool=pool)

        elif args.list:
            d = treq.get(BLOBS_URI, pool=pool)

        else:
            uri = urljoin(BLOBS_URI, uuid4().hex)
            d = treq.put(uri, data=data, pool=pool)
            if args.get:
                d.addCallback(_get, uri)
            if args.flag:
                d.addCallback(_flag, uri)
            if args.delete:
                d.addCallback(_delete, uri)

        deferreds.append(d)
        yield None

    yield defer.gatherResults(deferreds)


if __name__ == "__main__":
    args = parse_args()
    generator = requests_generator(args)
    d = main(generator)
    d.addCallback(_finished, args.amount, args.size)
    d.addErrback(_error)
    reactor.run()
