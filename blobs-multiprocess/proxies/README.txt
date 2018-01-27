Proxies
=======

During development of the blobs multiprocessing server there were multiple
possibilities of handling incoming connections with multiple processes. At that
time, not many resources for the LEAP Platform development were available, and
the simplest approach appeared to be to come up with a separate multiprocessing
blobs server to which Soledad Server could forward incoming requests to blobs.

This directory contains code to run some different possibilities of proxies and
a blobs server for benchmarking. It also contains results of the benchmarks for
future reference.

All tests were made using "lynx" as a client node and "giraffe" as a server
node. This is their configuration:

lynx (client VM):
- processor: Intel(R) Xeon(R) CPU E5-2620 v2 @ 2.10GHz
- allocated cores: 4 (only 2 real)
- ram: 8 GB
- os: Debian 8.10
- ab: 2.3

giraffe (server VM):
- processor: Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz
- allocated cores: 2 (only 1 real)
- ram: 4 GB
- os: Debian 8.10
- python: 2.7.9
