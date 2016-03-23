from klein import run, route

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


@route('/')
def home(request):
    return 'answer is >> %s' % fib(25)

if __name__ == "__main__":
    run("localhost", 8080)
