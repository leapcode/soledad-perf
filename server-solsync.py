from klein import run, route

import soledad_sync


@route('/start-sync')
def home(request):
    print "GOT REQUEST FOR STARTING SYNC..."
    d = soledad_sync.upload_soledad_stuff()
    return d


@route('/ping')
def ping(request):
    return 'easy!'

if __name__ == "__main__":
    run("localhost", 8080)
