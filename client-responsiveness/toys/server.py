import os
from klein import run, route
import tasks

FIB = os.environ.get('FIB', tasks.FIB_DEFAULT)


@route('/')
def home(request):
    return 'answer is >>> %s\n' % tasks.fib(FIB)

@route('/hi')
def ping(request):
    return 'easy!'

if __name__ == "__main__":
    run("localhost", 8080)
