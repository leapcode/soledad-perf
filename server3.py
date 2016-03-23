from klein import run, route

from twisted.internet.threads import deferToThread
from twisted.protocols import amp
from twisted.internet import reactor

from ampoule import child, pool

import sys
from twisted.python import log
log.startLogging(sys.stdout)

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


class Fib(amp.Command):
    response = [('total', amp.Integer())]

class DelayedFib(amp.AMP):
    def slowFib(self):
        result = fib(25)
        return result
    Fib.responder(slowFib)

@route('/')
def home(request):
    d = pp.doWork(Fib)
    return d


pp = None

def start_pool():
    global pp
    pp = pool.ProcessPool(child.AMPChild, recycleAfter=5000)
    pp.min = 1
    pp.max = 5
    pp.start()


if __name__ == "__main__":
    reactor.callWhenRunning(start_pool)
    run("localhost", 8080)
