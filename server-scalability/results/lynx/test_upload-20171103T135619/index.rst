======================
FunkLoad_ bench report
======================


:date: 2017-11-03 13:56:19
:abstract: Upload and download blobs
           Bench result of ``Blobs.test_upload``: 
           Upload blobs stress test

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents
.. |APDEXT| replace:: \ :sub:`1.5`

Bench configuration
-------------------

* Launched: 2017-11-03 13:56:19
* From: lynx
* Test: ``test_Blobs.py Blobs.test_upload``
* Target server: http://giraffe.cdev.bitmask.net:2424/
* Cycles of concurrent users: [25, 50, 75, 100, 125, 150, 175, 200]
* Cycle duration: 30s
* Sleeptime between requests: from 0.0s to 0.0s
* Sleeptime between test cases: 0.0s
* Startup delay between threads: 0.01s
* Apdex: |APDEXT|
* FunkLoad_ version: 1.17.2


Bench content
-------------

The test ``Blobs.test_upload`` contains: 

* 1 page
* 0 redirects
* 0 links
* 0 images
* 0 XML-RPC calls

The bench contains:

* 2892 tests
* 2892 pages
* 2892 requests


Test stats
----------

The number of Successful **Tests** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ================== ================== ================== ================== ==================
                CUs               STPS              TOTAL            SUCCESS              ERROR
 ================== ================== ================== ================== ==================
                 25             12.433                373                373             0.00%
                 50             14.767                443                443             0.00%
                 75             12.000                360                360             0.00%
                100             11.733                352                352             0.00%
                125             12.400                372                372             0.00%
                150             11.933                358                358             0.00%
                175             10.700                321                321             0.00%
                200             10.433                313                313             0.00%
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
                 25              0.509               POOR             12.433             26.000                373                373             0.00%              0.731              1.983              3.270              1.652              2.021              2.205              2.316
                 50              0.501               POOR             14.767             26.000                443                443             0.00%              0.951              3.209              5.661              2.547              3.005              4.306              4.923
                 75              0.294       UNACCEPTABLE             12.000             56.000                360                360             0.00%              1.776              5.770              9.846              4.009              5.641              7.655              8.012
                100              0.094       UNACCEPTABLE             11.733             76.000                352                352             0.00%              2.004              7.432             11.934              4.068              7.528              9.828             10.136
                125              0.073       UNACCEPTABLE             12.400             67.000                372                372             0.00%              2.038              8.742             13.401              4.766              9.233             10.805             11.626
                150              0.074       UNACCEPTABLE             11.933             77.000                358                358             0.00%              2.214             10.350             15.284              4.711             11.877             13.302             14.553
                175              0.053       UNACCEPTABLE             10.700             84.000                321                321             0.00%              2.471             12.659             21.390              5.602             14.860             16.877             18.067
                200              0.073       UNACCEPTABLE             10.433             82.000                313                313             0.00%              2.449             13.731             23.977              5.054             15.489             19.530             20.697
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
                 25              0.509               POOR             12.433             26.000                373                373             0.00%              0.731              1.983              3.270              1.652              2.021              2.205              2.316
                 50              0.501               POOR             14.767             26.000                443                443             0.00%              0.951              3.209              5.661              2.547              3.005              4.306              4.923
                 75              0.294       UNACCEPTABLE             12.000             56.000                360                360             0.00%              1.776              5.770              9.846              4.009              5.641              7.655              8.012
                100              0.094       UNACCEPTABLE             11.733             76.000                352                352             0.00%              2.004              7.432             11.934              4.068              7.528              9.828             10.136
                125              0.073       UNACCEPTABLE             12.400             67.000                372                372             0.00%              2.038              8.742             13.401              4.766              9.233             10.805             11.626
                150              0.074       UNACCEPTABLE             11.933             77.000                358                358             0.00%              2.214             10.350             15.284              4.711             11.877             13.302             14.553
                175              0.053       UNACCEPTABLE             10.700             84.000                321                321             0.00%              2.471             12.659             21.390              5.602             14.860             16.877             18.067
                200              0.073       UNACCEPTABLE             10.433             82.000                313                313             0.00%              2.449             13.731             23.977              5.054             15.489             19.530             20.697
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Slowest requests
----------------

The 5 slowest average response time during the best cycle with **25** CUs:

* In page 001, Apdex rating: POOR, avg response time: 1.98s, put: ``/blobs/0/372``
  `Upload blob`

Page detail stats
-----------------


PAGE 001: Upload blob
~~~~~~~~~~~~~~~~~~~~~

* Req: 001, put, url ``/blobs/0/372``

     .. image:: request_001.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                     25              0.509               POOR                373                373             0.00%              0.731              1.983              3.270              1.652              2.021              2.205              2.316
                     50              0.501               POOR                443                443             0.00%              0.951              3.209              5.661              2.547              3.005              4.306              4.923
                     75              0.294       UNACCEPTABLE                360                360             0.00%              1.776              5.770              9.846              4.009              5.641              7.655              8.012
                    100              0.094       UNACCEPTABLE                352                352             0.00%              2.004              7.432             11.934              4.068              7.528              9.828             10.136
                    125              0.073       UNACCEPTABLE                372                372             0.00%              2.038              8.742             13.401              4.766              9.233             10.805             11.626
                    150              0.074       UNACCEPTABLE                358                358             0.00%              2.214             10.350             15.284              4.711             11.877             13.302             14.553
                    175              0.053       UNACCEPTABLE                321                321             0.00%              2.471             12.659             21.390              5.602             14.860             16.877             18.067
                    200              0.073       UNACCEPTABLE                313                313             0.00%              2.449             13.731             23.977              5.054             15.489             19.530             20.697
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


Report generated with FunkLoad_ 1.17.2, more information available on the `FunkLoad site <http://funkload.nuxeo.org/#benching>`_.