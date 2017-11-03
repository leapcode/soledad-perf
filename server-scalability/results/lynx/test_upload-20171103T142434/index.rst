======================
FunkLoad_ bench report
======================


:date: 2017-11-03 14:24:34
:abstract: Upload and download blobs
           Bench result of ``Blobs.test_upload``: 
           Upload blobs stress test

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents
.. |APDEXT| replace:: \ :sub:`1.5`

Bench configuration
-------------------

* Launched: 2017-11-03 14:24:34
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

* 2472 tests
* 2472 pages
* 2472 requests


Test stats
----------

The number of Successful **Tests** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ================== ================== ================== ================== ==================
                CUs               STPS              TOTAL            SUCCESS              ERROR
 ================== ================== ================== ================== ==================
                 25              7.800                234                234             0.00%
                 50             10.433                313                313             0.00%
                 75             11.600                348                348             0.00%
                100             10.433                313                313             0.00%
                125             11.333                340                340             0.00%
                150             10.867                326                326             0.00%
                175             10.233                307                307             0.00%
                200              9.700                291                291             0.00%
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
                 25              0.585               POOR              7.800             18.000                234                234             0.00%              0.223              1.817              2.494              1.306              1.924              2.180              2.214
                 50              0.486       UNACCEPTABLE             10.433             42.000                313                313             0.00%              2.428              4.490              6.956              4.151              4.426              4.925              5.538
                 75              0.251       UNACCEPTABLE             11.600             75.000                348                348             0.00%              1.208              5.915              8.066              5.271              6.049              6.743              7.167
                100              0.059       UNACCEPTABLE             10.433             81.000                313                313             0.00%              2.712              8.522             12.533              5.432              8.599             10.718             11.193
                125              0.066       UNACCEPTABLE             11.333             81.000                340                340             0.00%              2.550              9.355             13.484              5.314             10.504             10.793             10.871
                150              0.061       UNACCEPTABLE             10.867             80.000                326                326             0.00%              2.672             11.126             15.999              5.504             12.972             13.627             13.845
                175              0.054       UNACCEPTABLE             10.233             80.000                307                307             0.00%              2.645             12.954             18.112              5.747             15.568             16.684             16.805
                200              0.038       UNACCEPTABLE              9.700             83.000                291                291             0.00%              3.542             14.751             23.030              6.674             16.362             19.714             21.410
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
                 25              0.585               POOR              7.800             18.000                234                234             0.00%              0.223              1.817              2.494              1.306              1.924              2.180              2.214
                 50              0.486       UNACCEPTABLE             10.433             42.000                313                313             0.00%              2.428              4.490              6.956              4.151              4.426              4.925              5.538
                 75              0.251       UNACCEPTABLE             11.600             75.000                348                348             0.00%              1.208              5.915              8.066              5.271              6.049              6.743              7.167
                100              0.059       UNACCEPTABLE             10.433             81.000                313                313             0.00%              2.712              8.522             12.533              5.432              8.599             10.718             11.193
                125              0.066       UNACCEPTABLE             11.333             81.000                340                340             0.00%              2.550              9.355             13.484              5.314             10.504             10.793             10.871
                150              0.061       UNACCEPTABLE             10.867             80.000                326                326             0.00%              2.672             11.126             15.999              5.504             12.972             13.627             13.845
                175              0.054       UNACCEPTABLE             10.233             80.000                307                307             0.00%              2.645             12.954             18.112              5.747             15.568             16.684             16.805
                200              0.038       UNACCEPTABLE              9.700             83.000                291                291             0.00%              3.542             14.751             23.030              6.674             16.362             19.714             21.410
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Slowest requests
----------------

The 5 slowest average response time during the best cycle with **25** CUs:

* In page 001, Apdex rating: POOR, avg response time: 1.82s, put: ``/blobs/0/231``
  `Upload blob`

Page detail stats
-----------------


PAGE 001: Upload blob
~~~~~~~~~~~~~~~~~~~~~

* Req: 001, put, url ``/blobs/0/231``

     .. image:: request_001.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                     25              0.585               POOR                234                234             0.00%              0.223              1.817              2.494              1.306              1.924              2.180              2.214
                     50              0.486       UNACCEPTABLE                313                313             0.00%              2.428              4.490              6.956              4.151              4.426              4.925              5.538
                     75              0.251       UNACCEPTABLE                348                348             0.00%              1.208              5.915              8.066              5.271              6.049              6.743              7.167
                    100              0.059       UNACCEPTABLE                313                313             0.00%              2.712              8.522             12.533              5.432              8.599             10.718             11.193
                    125              0.066       UNACCEPTABLE                340                340             0.00%              2.550              9.355             13.484              5.314             10.504             10.793             10.871
                    150              0.061       UNACCEPTABLE                326                326             0.00%              2.672             11.126             15.999              5.504             12.972             13.627             13.845
                    175              0.054       UNACCEPTABLE                307                307             0.00%              2.645             12.954             18.112              5.747             15.568             16.684             16.805
                    200              0.038       UNACCEPTABLE                291                291             0.00%              3.542             14.751             23.030              6.674             16.362             19.714             21.410
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