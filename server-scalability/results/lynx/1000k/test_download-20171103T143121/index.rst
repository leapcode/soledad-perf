======================
FunkLoad_ bench report
======================


:date: 2017-11-03 14:31:21
:abstract: Upload and download blobs
           Bench result of ``Blobs.test_download``: 
           Download blobs stress test

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents
.. |APDEXT| replace:: \ :sub:`1.5`

Bench configuration
-------------------

* Launched: 2017-11-03 14:31:21
* From: lynx
* Test: ``test_Blobs.py Blobs.test_download``
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

The test ``Blobs.test_download`` contains: 

* 1 page
* 0 redirects
* 0 links
* 0 images
* 0 XML-RPC calls

The bench contains:

* 16922 tests
* 16974 pages
* 16974 requests


Test stats
----------

The number of Successful **Tests** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ================== ================== ================== ================== ==================
                CUs               STPS              TOTAL            SUCCESS              ERROR
 ================== ================== ================== ================== ==================
                 25             40.433               1213               1213             0.00%
                 50             69.500               2085               2085             0.00%
                 75             78.167               2345               2345             0.00%
                100             46.933               1408               1408             0.00%
                125             97.633               2929               2929             0.00%
                150             91.100               2733               2733             0.00%
                175             63.600               1908               1908             0.00%
                200             76.700               2301               2301             0.00%
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
                 25              0.969          Excellent             40.433             82.000               1213               1213             0.00%              0.096              0.508              8.061              0.222              0.283              0.441              1.287
                 50              0.970          Excellent             69.500            107.000               2085               2085             0.00%              0.095              0.649              2.986              0.431              0.537              0.769              1.617
                 75              1.000          Excellent             78.167            116.000               2345               2345             0.00%              0.200              0.770              1.372              0.624              0.768              0.925              0.981
                100              0.921               Good             48.567            108.000               1457               1457             0.00%              0.479              2.004             15.087              0.904              1.071              1.243             15.001
                125              0.983          Excellent             97.633            134.000               2929               2929             0.00%              0.438              1.198              2.337              0.974              1.221              1.434              1.466
                150              0.650               POOR             91.100            142.000               2733               2733             0.00%              0.537              1.603              2.869              1.372              1.602              1.825              1.941
                175              0.498       UNACCEPTABLE             63.700            170.000               1911               1911             0.00%              0.297              2.668              7.506              1.584              1.903              4.667              6.578
                200              0.511               POOR             76.700            184.000               2301               2301             0.00%              0.694              2.471              9.090              1.707              2.044              3.646              5.422
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
                 25              0.969          Excellent             40.433             82.000               1213               1213             0.00%              0.096              0.508              8.061              0.222              0.283              0.441              1.287
                 50              0.970          Excellent             69.500            107.000               2085               2085             0.00%              0.095              0.649              2.986              0.431              0.537              0.769              1.617
                 75              1.000          Excellent             78.167            116.000               2345               2345             0.00%              0.200              0.770              1.372              0.624              0.768              0.925              0.981
                100              0.921               Good             48.567            108.000               1457               1457             0.00%              0.479              2.004             15.087              0.904              1.071              1.243             15.001
                125              0.983          Excellent             97.633            134.000               2929               2929             0.00%              0.438              1.198              2.337              0.974              1.221              1.434              1.466
                150              0.650               POOR             91.100            142.000               2733               2733             0.00%              0.537              1.603              2.869              1.372              1.602              1.825              1.941
                175              0.498       UNACCEPTABLE             63.700            170.000               1911               1911             0.00%              0.297              2.668              7.506              1.584              1.903              4.667              6.578
                200              0.511               POOR             76.700            184.000               2301               2301             0.00%              0.694              2.471              9.090              1.707              2.044              3.646              5.422
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Slowest requests
----------------

The 5 slowest average response time during the best cycle with **125** CUs:

* In page 001, Apdex rating: Excellent, avg response time: 1.20s, get: ``/blobs/0/686``
  `Download blob`

Page detail stats
-----------------


PAGE 001: Download blob
~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url ``/blobs/0/1212``

     .. image:: request_001.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                     25              0.969          Excellent               1213               1213             0.00%              0.096              0.508              8.061              0.222              0.283              0.441              1.287
                     50              0.970          Excellent               2085               2085             0.00%              0.095              0.649              2.986              0.431              0.537              0.769              1.617
                     75              1.000          Excellent               2345               2345             0.00%              0.200              0.770              1.372              0.624              0.768              0.925              0.981
                    100              0.921               Good               1457               1457             0.00%              0.479              2.004             15.087              0.904              1.071              1.243             15.001
                    125              0.983          Excellent               2929               2929             0.00%              0.438              1.198              2.337              0.974              1.221              1.434              1.466
                    150              0.650               POOR               2733               2733             0.00%              0.537              1.603              2.869              1.372              1.602              1.825              1.941
                    175              0.498       UNACCEPTABLE               1911               1911             0.00%              0.297              2.668              7.506              1.584              1.903              4.667              6.578
                    200              0.511               POOR               2301               2301             0.00%              0.694              2.471              9.090              1.707              2.044              3.646              5.422
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