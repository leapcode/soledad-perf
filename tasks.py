from twisted.protocols import amp
from ampoule import child


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


class Fib(amp.Command):
    response = [("fib", amp.Integer())]


class FibCalculator(child.AMPChild):
    @Fib.responder
    def fib(self):
        print 'called responder, fib...'
        n = 10
        return {"fib": fib(n)}
