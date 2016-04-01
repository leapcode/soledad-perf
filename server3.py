from klein import run, route

from twisted.internet import defer
from twisted.internet import reactor

from ampoule import pool

import tasks

import sys
from twisted.python import log

log.startLogging(sys.stdout)


@route('/')
def home(request):

    d = pp.doWork(tasks.Fib)
    d.addCallback(lambda res: str(res['fib']))
    return d

@route('/hi')
def ping(request):
    return 'easy!'


pp = None


@defer.inlineCallbacks
def start_pool():
    global pp
    pp = pool.ProcessPool(tasks.FibCalculator, min=1, max=2)
    print 'starting pool'
    yield pp.start()

if __name__ == "__main__":
    reactor.callWhenRunning(start_pool)
    run("localhost", 8080)
