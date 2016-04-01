import os
from klein import run, route
from twisted.internet.threads import deferToThread
import tasks

FIB = os.environ.get('FIB', tasks.FIB_DEFAULT)


@route('/')
def home(request):
    d = deferToThread(tasks.fib, FIB)
    d.addCallback(lambda result: 'answer is >>> %s\n' % result)
    return d

@route('/hi')
def ping(request):
    return 'easy!'

if __name__ == "__main__":
    run("localhost", 8080)
