import os
import sys
from klein import run, route

from twisted.internet import defer
from twisted.internet import reactor
from twisted.python import log

from ampoule import pool

import tasks

log.startLogging(sys.stdout)

FIB = os.environ.get('FIB', tasks.FIB_DEFAULT)


@route('/')
def home(request):
    d = pp.doWork(tasks.Fib, n=int(FIB)) 
    d.addCallback(lambda res: 'answer is >>> {r}\n'.format(r=res['fib']))
    return d

@route('/hi')
def ping(request):
    return 'easy!'


pp = None


@defer.inlineCallbacks
def start_pool():
    global pp
    # TODO get max number of processors
    pp = pool.ProcessPool(tasks.FibCalculator, min=1, max=4)
    print 'starting pool'
    yield pp.start()

if __name__ == "__main__":
    reactor.callWhenRunning(start_pool)
    run("localhost", 8080)
