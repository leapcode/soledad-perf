======================
FunkLoad_ bench report
======================


:date: 2017-11-01 17:19:26
:abstract: Upload and download blobs
           Bench result of ``Blobs.test_download``: 
           Download blobs stress test

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents
.. |APDEXT| replace:: \ :sub:`1.5`

Bench configuration
-------------------

* Launched: 2017-11-01 17:19:26
* From: pajeh
* Test: ``test_Blobs.py Blobs.test_download``
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

The test ``Blobs.test_download`` contains: 

* 1 page
* 0 redirects
* 0 links
* 0 images
* 0 XML-RPC calls

The bench contains:

* 20364 tests
* 20364 pages
* 20364 requests


Test stats
----------

The number of Successful **Tests** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ================== ================== ================== ================== ==================
                CUs               STPS              TOTAL            SUCCESS              ERROR
 ================== ================== ================== ================== ==================
                 25             58.800               1764               1764             0.00%
                 50             89.467               2684               2684             0.00%
                 75             89.400               2682               2682             0.00%
                100             85.367               2561               2561             0.00%
                125             96.600               2898               2898             0.00%
                150             89.200               2676               2676             0.00%
                175             87.067               2612               2612             0.00%
                200             82.900               2487               2487             0.00%
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
                 25              1.000          Excellent             58.800             69.000               1764               1764             0.00%              0.406              0.423              1.420              0.413              0.420              0.431              0.446
                 50              0.981          Excellent             89.467            130.000               2684               2684             0.00%              0.407              0.555              5.830              0.415              0.424              0.546              0.709
                 75              0.971          Excellent             89.400            167.000               2682               2682             0.00%              0.411              0.756              6.247              0.424              0.520              0.784              3.271
                100              0.941          Excellent             85.367            241.000               2561               2561             0.00%              0.410              1.073              6.078              0.422              0.497              5.193              5.442
                125              0.912               Good             96.600            285.000               2898               2898             0.00%              0.412              1.288              9.734              0.428              0.596              4.373              5.402
                150              0.883               Good             89.200            334.000               2676               2676             0.00%              0.412              1.630              6.589              0.429              0.573              5.412              5.620
                175              0.855               Good             87.067            348.000               2612               2612             0.00%              0.414              1.894              6.305              0.449              0.605              5.652              5.769
                200              0.831               FAIR             82.900            377.000               2487               2487             0.00%              0.415              2.111              9.849              0.495              0.684              5.596              5.668
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
                 25              1.000          Excellent             58.800             69.000               1764               1764             0.00%              0.406              0.423              1.420              0.413              0.420              0.431              0.446
                 50              0.981          Excellent             89.467            130.000               2684               2684             0.00%              0.407              0.555              5.830              0.415              0.424              0.546              0.709
                 75              0.971          Excellent             89.400            167.000               2682               2682             0.00%              0.411              0.756              6.247              0.424              0.520              0.784              3.271
                100              0.941          Excellent             85.367            241.000               2561               2561             0.00%              0.410              1.073              6.078              0.422              0.497              5.193              5.442
                125              0.912               Good             96.600            285.000               2898               2898             0.00%              0.412              1.288              9.734              0.428              0.596              4.373              5.402
                150              0.883               Good             89.200            334.000               2676               2676             0.00%              0.412              1.630              6.589              0.429              0.573              5.412              5.620
                175              0.855               Good             87.067            348.000               2612               2612             0.00%              0.414              1.894              6.305              0.449              0.605              5.652              5.769
                200              0.831               FAIR             82.900            377.000               2487               2487             0.00%              0.415              2.111              9.849              0.495              0.684              5.596              5.668
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Slowest requests
----------------

The 5 slowest average response time during the best cycle with **125** CUs:

* In page 001, Apdex rating: Good, avg response time: 1.29s, get: ``/blobs/0/3180``
  `Download blob`

Page detail stats
-----------------


PAGE 001: Download blob
~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url ``/blobs/0/1764``

     .. image:: request_001.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                     25              1.000          Excellent               1764               1764             0.00%              0.406              0.423              1.420              0.413              0.420              0.431              0.446
                     50              0.981          Excellent               2684               2684             0.00%              0.407              0.555              5.830              0.415              0.424              0.546              0.709
                     75              0.971          Excellent               2682               2682             0.00%              0.411              0.756              6.247              0.424              0.520              0.784              3.271
                    100              0.941          Excellent               2561               2561             0.00%              0.410              1.073              6.078              0.422              0.497              5.193              5.442
                    125              0.912               Good               2898               2898             0.00%              0.412              1.288              9.734              0.428              0.596              4.373              5.402
                    150              0.883               Good               2676               2676             0.00%              0.412              1.630              6.589              0.429              0.573              5.412              5.620
                    175              0.855               Good               2612               2612             0.00%              0.414              1.894              6.305              0.449              0.605              5.652              5.769
                    200              0.831               FAIR               2487               2487             0.00%              0.415              2.111              9.849              0.495              0.684              5.596              5.668
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