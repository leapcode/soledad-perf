Blobs Server Multiprocessing Improvement Assessment
===================================================

The code in this directory has the purpose of showing whether multiprocessing
improves the Soledad Blobs Server or not.

It uses a haproxy instance listening on local port 8000 to route between
different processes listening on ports 8001-8008. The number of processes
depends on the testing scenario.

Then, it runs a set of tests using 1, 2, 4 and 8 blobs server processes and
stores the results in a text file. Those results can then be graphed and
compared visually.


Dependencies
------------

To run the testing script, you will need to have:

- A python virtualenv with Soledad Server installed on it.
- A working haproxy installation.
- curl

To generate the graph, you will need:

- numpy
- matplotlib/pyplot


Description of files
--------------------

.
├── blobs-in-parallel.png - A graph generated from ./results.txt
├── blobs-server.py       - A simple blobs server.
├── graph.py              - The graphing script.
├── haproxy               - A directory with haproxy config.
├── makefile              - Rules for starting up pieces of the test.
├── multiproc.py          - A service that spawns multiple blobs servers.
├── proxies               - Study with different possibilities of proxy.
├── README.txt            - This file.
├── request.py            - A stressing blobs client.
├── results               - A directory with some results stored.
├── results.txt           - The file that ./graph.py reads from.
└── run-test.sh           - The script to run tests and produce output.


Actions
-------

The following set of actions are tested in each scenario, and compose the
X axis of the final graph:

  - baseline: a simple GET / to the root of the webserver, returning an empty
    page. Nothing can be faster than that.

  - list: a simple GET /blobs/some-user which lists the current blobs. In the
    present case, the result will always be an empty set of blobs.

  - put: a PUT /blobs/some-user/some-blob-id. The size of the blob depends on
    the scenarios configured in ./run-test.sh.

  - get: a PUT /blobs/some-user/some-blob-id followed by a GET to the same
    blob.

  - flag: a PUT /blobs/some-user/some-blob-id followed by a POST to the same
    blob setting one flag.

  - delete: a PUT /blobs/some-user/some-blob-id followed by a DELETE of the
    same blob.

When testing, each action is run 5 times (so the numbers in ./results.txt are
the accumulated time of the 5 runs) and the mean of the time taken is used when
graphing.

Usage
-----

Configure the scenarios you want tests to be run by editing ./run-test.sh, and
then run the script. It will:

  - iterate through desired number of processes and startup haproxy and
    multiproc blobs server for each scenario.

  - iterate through all the actions tested (baseline, put, put+get, etc).

  - iterate through amount x size blobs scenarios.

  - delete the contents of /tmp/blobs/* and run tests for each scenario.

Check the makefile for rules to help debugging (i.e. `make server` and `make
get`).
