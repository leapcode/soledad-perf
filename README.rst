soledad performance tests
-------------------------
some minimalistic benchmarks.
small prototypes to compare async behavior under load.

intended to evolve to small prototypes that:

* run soledad
* try different options for the decryption pool (inline, threads, processes).
* serve also a simple server to test how reactor is able to respond under cpu
  load.


You can use the makefile to launch different servers and compare their
performance::
  make inline-server  # executes cpu load inline
  make thread-server  # cpu load in a twisted threadpool
  make ampoule-server # cpu load in an ampoule process pool
  make perf           # runs httperf against the server, with a moderate cpu load.
  make perf-little    # runs httperf against the server, (less requests).
  make perf-easy      # runs httperf against a no-cpu load.

If you want to modify the cpu load, you can pass the FIB parameter as an
environment variable::
  FIB=20 make inline-server
  curl localhost:8080/
  $ answer is >>> 6765


Analysis
---------------
Let's run some experiments, in the three situations.

A) Compare a **fixed, moderate cpu load** (ie, parameters to the fib function in the range fib(25)/fib(30)) in terms of req/sec.

* Very similar rates. For fib(30), this gives something ~3 req/s in my machine.
* some overhead is appreciated.
* RAM usage??
* graph it!!

B) Stablish a **baseline for the no-cpu** perf case (perf-easy). In my machine this varies, but
   it's in the range 600-800 req/s. Note: since w/o cpu load this target runs very
   fas, this can be scripted to log one measure ever 500ms or so.

c) **Simultaneous easy+load**: Observe how the no-cpu perf case degrades when run
   against each one of the three servers, *while the servers are handling a moderate cpu load*.
   Still have to graph this properly, and measure std etc, but looking quickly
   at data I have three conclusions (yes, I'm biased!).

   * inline cpu load is a no-go: it blocks the reactor.
   * threaded is better,
   * but ampoule-multiprocessing is superior when we look at how responsive the reactor is still.

   to do still for this case:

   * RAM usage?? graph before, during, after
   * graph it!!
   * experiment with different parameters for the process pool.


To-Do
--------------
* [x] make the cpu load variable (parameter to fib function: pass it as env var).
* [ ] graph req/sec in response to variable cpu loads (parameter to fib).
* [ ] graph response of perf-easy DURING a run of perf/perf-little. 
* [ ] compare the rate of responsiveness against variable cpu loads.
* [ ] scale these minimalistic examples to realistic payload decryption using gnupg.
