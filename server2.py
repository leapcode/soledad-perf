from klein import run, route
from twisted.internet.threads import deferToThread

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


@route('/')
def home(request):
    d = deferToThread(fib, 25)
    d.addCallback(lambda result: 'answer is >> %s' % result)
    return d

if __name__ == "__main__":
    run("localhost", 8080)
