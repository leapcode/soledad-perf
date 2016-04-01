from klein import run, route
from twisted.internet.threads import deferToThread

from tasks import fib


@route('/')
def home(request):
    d = deferToThread(fib, 30)
    d.addCallback(lambda result: 'answer is >> %s' % result)
    return d

if __name__ == "__main__":
    run("localhost", 8080)
