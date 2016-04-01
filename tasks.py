import os
from twisted.protocols import amp
from ampoule import child

FIB_DEFAULT = 30


def fib(n):
    '''very silly fibonacci function.
    do not try to optimize this, the idea is to make your cpu suffer for a
    while'''
    n = int(n)
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# ampoule stuff

class Fib(amp.Command):
    arguments = [('n', amp.Integer())]
    response = [('fib', amp.Integer())]


class FibCalculator(child.AMPChild):
    @Fib.responder
    def fib(self, n):
        #print "FIB FUNCTION CALLED WITH", n
        return {"fib": fib(n)}
