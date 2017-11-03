======================
FunkLoad_ bench report
======================


:date: 2017-11-03 14:15:37
:abstract: Upload and download blobs
           Bench result of ``Blobs.test_download``: 
           Download blobs stress test

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents
.. |APDEXT| replace:: \ :sub:`1.5`

Bench configuration
-------------------

* Launched: 2017-11-03 14:15:37
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

* 63520 tests
* 63790 pages
* 63790 requests


Test stats
----------

The number of Successful **Tests** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ================== ================== ================== ================== ==================
                CUs               STPS              TOTAL            SUCCESS              ERROR
 ================== ================== ================== ================== ==================
                 25            142.500               4275               4275             0.00%
                 50            252.467               7574               7574             0.00%
                 75            288.300               8649               8649             0.00%
                100            300.200               9006               9006             0.00%
                125            265.800               7974               7974             0.00%
                150            303.233               9097               9097             0.00%
                175            302.367               9071               9071             0.00%
                200            262.467               7874               7874             0.00%
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
                 25              1.000          Excellent            142.500            166.000               4275               4275             0.00%              0.022              0.157              0.361              0.100              0.159              0.198              0.218
                 50              1.000          Excellent            253.167            301.000               7595               7595             0.00%              0.008              0.143              0.409              0.077              0.137              0.204              0.274
                 75              1.000          Excellent            288.467            332.000               8654               8654             0.00%              0.011              0.143              0.390              0.064              0.145              0.213              0.230
                100              1.000          Excellent            300.433            331.000               9013               9013             0.00%              0.014              0.197              1.251              0.101              0.201              0.278              0.300
                125              0.999          Excellent            267.900            334.000               8037               8037             0.00%              0.010              0.268              1.648              0.079              0.224              0.522              0.585
                150              1.000          Excellent            304.233            360.000               9127               9127             0.00%              0.023              0.293              0.733              0.182              0.295              0.400              0.430
                175              1.000          Excellent            304.567            363.000               9137               9137             0.00%              0.016              0.342              1.039              0.204              0.347              0.471              0.506
                200              1.000          Excellent            265.067            305.000               7952               7952             0.00%              0.016              0.295              1.127              0.115              0.272              0.508              0.580
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
                 25              1.000          Excellent            142.500            166.000               4275               4275             0.00%              0.022              0.157              0.361              0.100              0.159              0.198              0.218
                 50              1.000          Excellent            253.167            301.000               7595               7595             0.00%              0.008              0.143              0.409              0.077              0.137              0.204              0.274
                 75              1.000          Excellent            288.467            332.000               8654               8654             0.00%              0.011              0.143              0.390              0.064              0.145              0.213              0.230
                100              1.000          Excellent            300.433            331.000               9013               9013             0.00%              0.014              0.197              1.251              0.101              0.201              0.278              0.300
                125              0.999          Excellent            267.900            334.000               8037               8037             0.00%              0.010              0.268              1.648              0.079              0.224              0.522              0.585
                150              1.000          Excellent            304.233            360.000               9127               9127             0.00%              0.023              0.293              0.733              0.182              0.295              0.400              0.430
                175              1.000          Excellent            304.567            363.000               9137               9137             0.00%              0.016              0.342              1.039              0.204              0.347              0.471              0.506
                200              1.000          Excellent            265.067            305.000               7952               7952             0.00%              0.016              0.295              1.127              0.115              0.272              0.508              0.580
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Slowest requests
----------------

The 5 slowest average response time during the best cycle with **175** CUs:

* In page 001, Apdex rating: Excellent, avg response time: 0.34s, get: ``/blobs/0/3263``
  `Download blob`

Page detail stats
-----------------


PAGE 001: Download blob
~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url ``/blobs/0/4320``

     .. image:: request_001.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                     25              1.000          Excellent               4275               4275             0.00%              0.022              0.157              0.361              0.100              0.159              0.198              0.218
                     50              1.000          Excellent               7595               7595             0.00%              0.008              0.143              0.409              0.077              0.137              0.204              0.274
                     75              1.000          Excellent               8654               8654             0.00%              0.011              0.143              0.390              0.064              0.145              0.213              0.230
                    100              1.000          Excellent               9013               9013             0.00%              0.014              0.197              1.251              0.101              0.201              0.278              0.300
                    125              0.999          Excellent               8037               8037             0.00%              0.010              0.268              1.648              0.079              0.224              0.522              0.585
                    150              1.000          Excellent               9127               9127             0.00%              0.023              0.293              0.733              0.182              0.295              0.400              0.430
                    175              1.000          Excellent               9137               9137             0.00%              0.016              0.342              1.039              0.204              0.347              0.471              0.506
                    200              1.000          Excellent               7952               7952             0.00%              0.016              0.295              1.127              0.115              0.272              0.508              0.580
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