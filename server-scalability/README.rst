Blobs Server Scalability Tests Results
======================================

These are results obtained by running the blobs scalability tests that can be
found in:

  https://0xacab.org/leap/soledad/tree/master/scripts/scalability

Overview
--------

The blobs server scalability tests aim to find the maximum amount of parallel
blobs upload and download requests that the server is able to respond to. We
use FunkLoad[1] to launch an increasing number of parallel upload/download
requests and to create reports with a summary of the results. The metrics
obtained are:

- The number of Successful Tests Per Second given the number of Concurrent
  Users.

- The number of Successful Pages Per Second given the number of Concurrent
  Users. A Page in the context of FunkLoad is a request to the server. For
  tests that have only one Page request, this number is the same as the above.

- The total number of Requests Per Second (successful or not) given the number
  of Concurrent Users.

- Graphs with the associated response times.

[1] https://funkload.nuxeo.org/


Scenarios
---------

The size of the uploaded/downloaded blobs and the client and server bandwidth
are parameters that highly influence the results of these tests. See the file
results/README.txt for information on the scenario used for each test.
