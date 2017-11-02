======================
FunkLoad_ bench report
======================


:date: 2017-11-01 17:32:13
:abstract: Upload and download blobs
           Bench result of ``Blobs.test_upload``: 
           Upload blobs stress test

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents
.. |APDEXT| replace:: \ :sub:`1.5`

Bench configuration
-------------------

* Launched: 2017-11-01 17:32:13
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

* 2661 tests
* 2661 pages
* 2661 requests


Test stats
----------

The number of Successful **Tests** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ================== ================== ================== ================== ==================
                CUs               STPS              TOTAL            SUCCESS              ERROR
 ================== ================== ================== ================== ==================
                 25              9.167                275                275             0.00%
                 50             11.500                345                345             0.00%
                 75             13.333                400                400             0.00%
                100             10.567                317                317             0.00%
                125             12.100                363                363             0.00%
                150             11.267                338                338             0.00%
                175             10.433                313                313             0.00%
                200             10.333                310                310             0.00%
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
                 25              0.502               POOR              9.167             25.000                275                275             0.00%              0.775              2.619              5.939              2.476              2.619              2.811              2.830
                 50              0.493       UNACCEPTABLE             11.500             50.000                345                345             0.00%              2.626              3.970              7.286              3.348              3.896              4.278              4.335
                 75              0.372       UNACCEPTABLE             13.333             64.000                400                400             0.00%              3.197              5.192             13.589              3.624              4.576              7.624              8.851
                100              0.088       UNACCEPTABLE             10.567             76.000                317                317             0.00%              4.494              8.039             17.479              5.684              7.547             11.132             13.010
                125              0.048       UNACCEPTABLE             12.100             69.000                363                363             0.00%              4.183              8.699             17.269              6.525              8.315             11.353             12.692
                150              0.025       UNACCEPTABLE             11.267             80.000                338                338             0.00%              5.062             10.968             23.591              6.827             10.795             14.272             16.208
                175              0.018       UNACCEPTABLE             10.433             80.000                313                313             0.00%              5.168             13.069             24.198              7.829             13.421             17.048             18.726
                200              0.027       UNACCEPTABLE             10.333             80.000                310                310             0.00%              5.003             14.184             29.234              6.808             15.795             19.865             21.150
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
                 25              0.502               POOR              9.167             25.000                275                275             0.00%              0.775              2.619              5.939              2.476              2.619              2.811              2.830
                 50              0.493       UNACCEPTABLE             11.500             50.000                345                345             0.00%              2.626              3.970              7.286              3.348              3.896              4.278              4.335
                 75              0.372       UNACCEPTABLE             13.333             64.000                400                400             0.00%              3.197              5.192             13.589              3.624              4.576              7.624              8.851
                100              0.088       UNACCEPTABLE             10.567             76.000                317                317             0.00%              4.494              8.039             17.479              5.684              7.547             11.132             13.010
                125              0.048       UNACCEPTABLE             12.100             69.000                363                363             0.00%              4.183              8.699             17.269              6.525              8.315             11.353             12.692
                150              0.025       UNACCEPTABLE             11.267             80.000                338                338             0.00%              5.062             10.968             23.591              6.827             10.795             14.272             16.208
                175              0.018       UNACCEPTABLE             10.433             80.000                313                313             0.00%              5.168             13.069             24.198              7.829             13.421             17.048             18.726
                200              0.027       UNACCEPTABLE             10.333             80.000                310                310             0.00%              5.003             14.184             29.234              6.808             15.795             19.865             21.150
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Slowest requests
----------------

The 5 slowest average response time during the best cycle with **25** CUs:

* In page 001, Apdex rating: POOR, avg response time: 2.62s, put: ``/blobs/0/260``
  `Upload blob`

Page detail stats
-----------------


PAGE 001: Upload blob
~~~~~~~~~~~~~~~~~~~~~

* Req: 001, put, url ``/blobs/0/260``

     .. image:: request_001.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                     25              0.502               POOR                275                275             0.00%              0.775              2.619              5.939              2.476              2.619              2.811              2.830
                     50              0.493       UNACCEPTABLE                345                345             0.00%              2.626              3.970              7.286              3.348              3.896              4.278              4.335
                     75              0.372       UNACCEPTABLE                400                400             0.00%              3.197              5.192             13.589              3.624              4.576              7.624              8.851
                    100              0.088       UNACCEPTABLE                317                317             0.00%              4.494              8.039             17.479              5.684              7.547             11.132             13.010
                    125              0.048       UNACCEPTABLE                363                363             0.00%              4.183              8.699             17.269              6.525              8.315             11.353             12.692
                    150              0.025       UNACCEPTABLE                338                338             0.00%              5.062             10.968             23.591              6.827             10.795             14.272             16.208
                    175              0.018       UNACCEPTABLE                313                313             0.00%              5.168             13.069             24.198              7.829             13.421             17.048             18.726
                    200              0.027       UNACCEPTABLE                310                310             0.00%              5.003             14.184             29.234              6.808             15.795             19.865             21.150
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