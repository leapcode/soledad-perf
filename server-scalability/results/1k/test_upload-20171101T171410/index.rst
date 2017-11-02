======================
FunkLoad_ bench report
======================


:date: 2017-11-01 17:14:10
:abstract: Upload and download blobs
           Bench result of ``Blobs.test_upload``: 
           Upload blobs stress test

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents
.. |APDEXT| replace:: \ :sub:`1.5`

Bench configuration
-------------------

* Launched: 2017-11-01 17:14:10
* From: pajeh
* Test: ``test_Blobs.py Blobs.test_upload``
* Target server: http://giraffe.cdev.bitmask.net:2424/
* Cycles of concurrent users: [25, 50, 75, 100, 125, 150, 175, 200]
* Cycle duration: 30s
* Sleeptime between requests: from 0.0s to 0.0s
* Sleeptime between test cases: 0.0s
* Startup delay between threads: 0.01s
* Apdex: |APDEXT|
* FunkLoad_ version: 1.17.1


Bench content
-------------

The test ``Blobs.test_upload`` contains: 

* 1 page
* 0 redirects
* 0 links
* 0 images
* 0 XML-RPC calls

The bench contains:

* 2816 tests
* 2816 pages
* 2816 requests


Test stats
----------

The number of Successful **Tests** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ================== ================== ================== ================== ==================
                CUs               STPS              TOTAL            SUCCESS              ERROR
 ================== ================== ================== ================== ==================
                 25             10.433                313                313             0.00%
                 50             13.367                401                401             0.00%
                 75             13.633                409                409             0.00%
                100             13.600                408                408             0.00%
                125             11.900                357                357             0.00%
                150             11.233                337                337             0.00%
                175              9.800                294                294             0.00%
                200              9.900                297                297             0.00%
 ================== ================== ================== ================== ==================



Page stats
----------

The number of Successful **Pages** Per Second (SPPS) over Concurrent Users (CUs).
Note: an XML-RPC call counts as a page.

 .. image:: pages_spps.png
 .. image:: pages.png

 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                CUs             Apdex*             Rating               SPPS            maxSPPS              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                 25              0.490       UNACCEPTABLE             10.433             25.000                313                313             0.00%              1.925              2.394              6.598              2.122              2.285              2.546              2.671
                 50              0.500               POOR             13.367             50.000                401                401             0.00%              1.656              3.484              3.959              2.914              3.568              3.895              3.918
                 75              0.394       UNACCEPTABLE             13.633             63.000                409                409             0.00%              3.095              5.100             13.851              3.581              4.577              7.437              8.389
                100              0.250       UNACCEPTABLE             13.600             60.000                408                408             0.00%              3.657              6.590             14.301              5.065              6.000              8.942             10.234
                125              0.041       UNACCEPTABLE             11.900             80.000                357                357             0.00%              4.430              9.006             19.551              6.798              8.543             11.813             13.253
                150              0.040       UNACCEPTABLE             11.233             79.000                337                337             0.00%              4.363             10.927             20.239              6.999             10.742             14.903             16.030
                175              0.026       UNACCEPTABLE              9.800             80.000                294                294             0.00%              4.929             12.964             25.006              6.828             13.628             16.938             19.187
                200              0.012       UNACCEPTABLE              9.900             79.000                297                297             0.00%              5.480             14.725             29.801              7.949             15.108             21.244             23.073
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Request stats
-------------

The number of **Requests** Per Second (RPS) (successful or not) over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png
 .. image:: time_rps.png

 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                CUs             Apdex*            Rating*                RPS             maxRPS              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                 25              0.490       UNACCEPTABLE             10.433             25.000                313                313             0.00%              1.925              2.394              6.598              2.122              2.285              2.546              2.671
                 50              0.500               POOR             13.367             50.000                401                401             0.00%              1.656              3.484              3.959              2.914              3.568              3.895              3.918
                 75              0.394       UNACCEPTABLE             13.633             63.000                409                409             0.00%              3.095              5.100             13.851              3.581              4.577              7.437              8.389
                100              0.250       UNACCEPTABLE             13.600             60.000                408                408             0.00%              3.657              6.590             14.301              5.065              6.000              8.942             10.234
                125              0.041       UNACCEPTABLE             11.900             80.000                357                357             0.00%              4.430              9.006             19.551              6.798              8.543             11.813             13.253
                150              0.040       UNACCEPTABLE             11.233             79.000                337                337             0.00%              4.363             10.927             20.239              6.999             10.742             14.903             16.030
                175              0.026       UNACCEPTABLE              9.800             80.000                294                294             0.00%              4.929             12.964             25.006              6.828             13.628             16.938             19.187
                200              0.012       UNACCEPTABLE              9.900             79.000                297                297             0.00%              5.480             14.725             29.801              7.949             15.108             21.244             23.073
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Slowest requests
----------------

The 5 slowest average response time during the best cycle with **25** CUs:

* In page 001, Apdex rating: UNACCEPTABLE, avg response time: 2.39s, put: ``/blobs/0/300``
  `Upload blob`

Page detail stats
-----------------


PAGE 001: Upload blob
~~~~~~~~~~~~~~~~~~~~~

* Req: 001, put, url ``/blobs/0/300``

     .. image:: request_001.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                     25              0.490       UNACCEPTABLE                313                313             0.00%              1.925              2.394              6.598              2.122              2.285              2.546              2.671
                     50              0.500               POOR                401                401             0.00%              1.656              3.484              3.959              2.914              3.568              3.895              3.918
                     75              0.394       UNACCEPTABLE                409                409             0.00%              3.095              5.100             13.851              3.581              4.577              7.437              8.389
                    100              0.250       UNACCEPTABLE                408                408             0.00%              3.657              6.590             14.301              5.065              6.000              8.942             10.234
                    125              0.041       UNACCEPTABLE                357                357             0.00%              4.430              9.006             19.551              6.798              8.543             11.813             13.253
                    150              0.040       UNACCEPTABLE                337                337             0.00%              4.363             10.927             20.239              6.999             10.742             14.903             16.030
                    175              0.026       UNACCEPTABLE                294                294             0.00%              4.929             12.964             25.006              6.828             13.628             16.938             19.187
                    200              0.012       UNACCEPTABLE                297                297             0.00%              5.480             14.725             29.801              7.949             15.108             21.244             23.073
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|

Definitions
-----------

* CUs: Concurrent users or number of concurrent threads executing tests.
* Request: a single GET/POST/redirect/XML-RPC request.
* Page: a request with redirects and resource links (image, css, js) for an HTML page.
* STPS: Successful tests per second.
* SPPS: Successful pages per second.
* RPS: Requests per second, successful or not.
* maxSPPS: Maximum SPPS during the cycle.
* maxRPS: Maximum RPS during the cycle.
* MIN: Minimum response time for a page or request.
* AVG: Average response time for a page or request.
* MAX: Maximmum response time for a page or request.
* P10: 10th percentile, response time where 10 percent of pages or requests are delivered.
* MED: Median or 50th percentile, response time where half of pages or requests are delivered.
* P90: 90th percentile, response time where 90 percent of pages or requests are delivered.
* P95: 95th percentile, response time where 95 percent of pages or requests are delivered.
* Apdex T: Application Performance Index,
  this is a numerical measure of user satisfaction, it is based
  on three zones of application responsiveness:

  - Satisfied: The user is fully productive. This represents the
    time value (T seconds) below which users are not impeded by
    application response time.

  - Tolerating: The user notices performance lagging within
    responses greater than T, but continues the process.

  - Frustrated: Performance with a response time greater than 4*T
    seconds is unacceptable, and users may abandon the process.

    By default T is set to 1.5s. This means that response time between 0
    and 1.5s the user is fully productive, between 1.5 and 6s the
    responsivness is tolerable and above 6s the user is frustrated.

    The Apdex score converts many measurements into one number on a
    uniform scale of 0-to-1 (0 = no users satisfied, 1 = all users
    satisfied).

    Visit http://www.apdex.org/ for more information.
* Rating: To ease interpretation, the Apdex score is also represented
  as a rating:

  - U for UNACCEPTABLE represented in gray for a score between 0 and 0.5

  - P for POOR represented in red for a score between 0.5 and 0.7

  - F for FAIR represented in yellow for a score between 0.7 and 0.85

  - G for Good represented in green for a score between 0.85 and 0.94

  - E for Excellent represented in blue for a score between 0.94 and 1.


Report generated with FunkLoad_ 1.17.1, more information available on the `FunkLoad site <http://funkload.nuxeo.org/#benching>`_.