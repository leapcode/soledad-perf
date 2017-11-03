======================
FunkLoad_ bench report
======================


:date: 2017-11-01 18:32:58
:abstract: Upload and download blobs
           Bench result of ``Blobs.test_upload``: 
           Upload blobs stress test

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents
.. |APDEXT| replace:: \ :sub:`1.5`

Bench configuration
-------------------

* Launched: 2017-11-01 18:32:58
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

* 2486 tests
* 2486 pages
* 2486 requests


Test stats
----------

The number of Successful **Tests** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ================== ================== ================== ================== ==================
                CUs               STPS              TOTAL            SUCCESS              ERROR
 ================== ================== ================== ================== ==================
                 25              6.667                200                200             0.00%
                 50              9.967                299                299             0.00%
                 75             12.433                373                373             0.00%
                100             11.367                341                341             0.00%
                125             11.800                354                354             0.00%
                150             11.100                333                333             0.00%
                175              9.900                297                297             0.00%
                200              9.633                289                289             0.00%
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
                 25              0.500               POOR              6.667             25.000                200                200             0.00%              3.197              3.507              3.753              3.394              3.487              3.710              3.731
                 50              0.500               POOR              9.967             50.000                299                299             0.00%              4.290              4.863              5.399              4.321              4.889              5.241              5.256
                 75              0.204       UNACCEPTABLE             12.433             65.000                373                373             0.00%              1.712              5.846              9.084              2.416              6.112              8.016              8.170
                100              0.022       UNACCEPTABLE             11.367             80.000                341                341             0.00%              5.062              7.919             13.930              6.319              7.488             10.333             11.637
                125              0.018       UNACCEPTABLE             11.800             80.000                354                354             0.00%              5.320              9.245             16.804              7.596              8.775             12.163             12.860
                150              0.002       UNACCEPTABLE             11.100             80.000                333                333             0.00%              5.893             11.193             20.348              8.235             11.102             13.896             14.967
                175              0.000       UNACCEPTABLE              9.900             81.000                297                297             0.00%              6.294             13.575             23.655              8.073             14.041             17.512             18.597
                200              0.000       UNACCEPTABLE              9.633             80.000                289                289             0.00%              6.327             15.243             29.755              8.144             15.704             20.263             23.709
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
                 25              0.500               POOR              6.667             25.000                200                200             0.00%              3.197              3.507              3.753              3.394              3.487              3.710              3.731
                 50              0.500               POOR              9.967             50.000                299                299             0.00%              4.290              4.863              5.399              4.321              4.889              5.241              5.256
                 75              0.204       UNACCEPTABLE             12.433             65.000                373                373             0.00%              1.712              5.846              9.084              2.416              6.112              8.016              8.170
                100              0.022       UNACCEPTABLE             11.367             80.000                341                341             0.00%              5.062              7.919             13.930              6.319              7.488             10.333             11.637
                125              0.018       UNACCEPTABLE             11.800             80.000                354                354             0.00%              5.320              9.245             16.804              7.596              8.775             12.163             12.860
                150              0.002       UNACCEPTABLE             11.100             80.000                333                333             0.00%              5.893             11.193             20.348              8.235             11.102             13.896             14.967
                175              0.000       UNACCEPTABLE              9.900             81.000                297                297             0.00%              6.294             13.575             23.655              8.073             14.041             17.512             18.597
                200              0.000       UNACCEPTABLE              9.633             80.000                289                289             0.00%              6.327             15.243             29.755              8.144             15.704             20.263             23.709
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Slowest requests
----------------

The 5 slowest average response time during the best cycle with **25** CUs:

* In page 001, Apdex rating: POOR, avg response time: 3.51s, put: ``/blobs/0/181``
  `Upload blob`

Page detail stats
-----------------


PAGE 001: Upload blob
~~~~~~~~~~~~~~~~~~~~~

* Req: 001, put, url ``/blobs/0/181``

     .. image:: request_001.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                     25              0.500               POOR                200                200             0.00%              3.197              3.507              3.753              3.394              3.487              3.710              3.731
                     50              0.500               POOR                299                299             0.00%              4.290              4.863              5.399              4.321              4.889              5.241              5.256
                     75              0.204       UNACCEPTABLE                373                373             0.00%              1.712              5.846              9.084              2.416              6.112              8.016              8.170
                    100              0.022       UNACCEPTABLE                341                341             0.00%              5.062              7.919             13.930              6.319              7.488             10.333             11.637
                    125              0.018       UNACCEPTABLE                354                354             0.00%              5.320              9.245             16.804              7.596              8.775             12.163             12.860
                    150              0.002       UNACCEPTABLE                333                333             0.00%              5.893             11.193             20.348              8.235             11.102             13.896             14.967
                    175              0.000       UNACCEPTABLE                297                297             0.00%              6.294             13.575             23.655              8.073             14.041             17.512             18.597
                    200              0.000       UNACCEPTABLE                289                289             0.00%              6.327             15.243             29.755              8.144             15.704             20.263             23.709
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