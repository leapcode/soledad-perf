#!/usr/bin/env python

from io import BytesIO
import time
import treq
from argparse import ArgumentParser
from twisted.internet import reactor, task, defer
from twisted.web.client import readBody, HTTPConnectionPool, Agent
from urlparse import urljoin
from uuid import uuid4


BASE_URI = 'http://127.0.0.1:8000/'
BLOBS_URI = urljoin(BASE_URI, 'blobs/user/')
#                    'blobs/{}/'.format(time.strftime('%Y-%m-%d_%H-%M-%s')))
CONCURRENT = 10


def get_client():
    pool = HTTPConnectionPool(reactor)
    agent = Agent(reactor, pool=pool)
    return treq.client.HTTPClient(agent)


_client = get_client()


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


def _finished(_, start, amount):
    end = time.time()
    print(float(amount) / (end - start))
    reactor.stop()


def _error(failure):
    print("Failed: %r" % failure)
    reactor.stop()


def main(generator, amount):
    cooperator = task.Cooperator()
    cooptask = cooperator.cooperate(generator)
    start = time.time()
    d = cooptask.whenDone()
    d.addCallback(_finished, start, amount)
    d.addErrback(_error)
    return d


def requests_generator(args):
    data = "a" * args.size * 1024

    def _get(_, uri):
        d = _client.get(uri)
        d.addCallback(lambda response: readBody(response))
        return d

    def _flag(_, uri):
        flags = BytesIO('["PROCESSING"]')
        d = _client.post(uri, data=flags)
        return d

    def _delete(_, uri):
        d = _client.delete(uri)
        return d

    deferreds = []
    for i in xrange(args.amount):
        if args.baseline:
            d = _client.get(BASE_URI)

        elif args.list:
            d = _client.get(BLOBS_URI)

        else:
            uri = urljoin(BLOBS_URI, uuid4().hex)
            d = _client.put(uri, data=data)

            if args.get:
                d.addCallback(_get, uri)

            if args.flag:
                d.addCallback(_flag, uri)

            if args.delete:
                d.addCallback(_delete, uri)

        deferreds.append(d)
        yield None

    d = defer.gatherResults(deferreds)
    yield d


if __name__ == "__main__":
    args = parse_args()
    generator = requests_generator(args)
    d = main(generator, args.amount)
    reactor.run()
