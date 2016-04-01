from klein import run, route

from tasks import fib


@route('/')
def home(request):
    return 'answer is >> %s' % fib(30)

if __name__ == "__main__":
    run("localhost", 8080)
