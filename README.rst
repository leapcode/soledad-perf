soledad performance tests
-------------------------
some minimalistic benchmarks.
small prototypes to compare async behavior under load.

intended to evolve to small prototypes that:

  - run soledad
  - try different things for the decryption pool
  - serve also a simple server to test how reactor is able to respond under cpu
    load.


You can use the makefile to launch different servers and compare their
performance::
  make inline-server  # executes cpu load inline
  make thread-server  # cpu load in a twisted threadpool
  make ampoule-server # cpu load in an ampoule process pool
  make perf           # runs httperf against the server

