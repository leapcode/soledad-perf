======================
FunkLoad_ bench report
======================


:date: 2017-11-03 13:43:01
:abstract: Upload and download blobs
           Bench result of ``Blobs.test_upload``: 
           Upload blobs stress test

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents
.. |APDEXT| replace:: \ :sub:`1.5`

Bench configuration
-------------------

* Launched: 2017-11-03 13:43:01
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

* 2959 tests
* 2959 pages
* 2959 requests


Test stats
----------

The number of Successful **Tests** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ================== ================== ================== ================== ==================
                CUs               STPS              TOTAL            SUCCESS              ERROR
 ================== ================== ================== ================== ==================
                 25             12.467                374                374             0.00%
                 50             14.233                427                427             0.00%
                 75             13.433                403                403             0.00%
                100             13.267                398                398             0.00%
                125             13.367                401                401             0.00%
                150             10.100                303                303             0.00%
                175             11.200                336                336             0.00%
                200             10.567                317                317             0.00%
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
                 25              0.501               POOR             12.467             25.000                374                374             0.00%              0.935              1.952              3.201              1.763              1.979              2.114              2.148
                 50              0.500               POOR             14.233             48.000                427                427             0.00%              1.099              3.341              6.568              2.466              3.170              4.518              5.033
                 75              0.412       UNACCEPTABLE             13.433             46.000                403                403             0.00%              1.678              5.191              7.910              3.947              5.124              6.590              7.132
                100              0.095       UNACCEPTABLE             13.267             51.000                398                398             0.00%              1.845              6.735              9.799              3.889              7.001              8.405              9.339
                125              0.087       UNACCEPTABLE             13.367             70.000                401                401             0.00%              2.149              8.146             11.382              4.326              8.810             10.115             11.130
                150              0.091       UNACCEPTABLE             10.100             80.000                303                303             0.00%              2.189             11.679             18.975              4.069             14.256             16.196             17.071
                175              0.076       UNACCEPTABLE             11.200             80.000                336                336             0.00%              2.263             12.015             18.187              4.768             14.784             16.208             16.823
                200              0.065       UNACCEPTABLE             10.567             80.000                317                317             0.00%              2.541             13.732             24.099              5.263             15.311             19.942             20.955
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
                 25              0.501               POOR             12.467             25.000                374                374             0.00%              0.935              1.952              3.201              1.763              1.979              2.114              2.148
                 50              0.500               POOR             14.233             48.000                427                427             0.00%              1.099              3.341              6.568              2.466              3.170              4.518              5.033
                 75              0.412       UNACCEPTABLE             13.433             46.000                403                403             0.00%              1.678              5.191              7.910              3.947              5.124              6.590              7.132
                100              0.095       UNACCEPTABLE             13.267             51.000                398                398             0.00%              1.845              6.735              9.799              3.889              7.001              8.405              9.339
                125              0.087       UNACCEPTABLE             13.367             70.000                401                401             0.00%              2.149              8.146             11.382              4.326              8.810             10.115             11.130
                150              0.091       UNACCEPTABLE             10.100             80.000                303                303             0.00%              2.189             11.679             18.975              4.069             14.256             16.196             17.071
                175              0.076       UNACCEPTABLE             11.200             80.000                336                336             0.00%              2.263             12.015             18.187              4.768             14.784             16.208             16.823
                200              0.065       UNACCEPTABLE             10.567             80.000                317                317             0.00%              2.541             13.732             24.099              5.263             15.311             19.942             20.955
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Slowest requests
----------------

The 5 slowest average response time during the best cycle with **25** CUs:

* In page 001, Apdex rating: POOR, avg response time: 1.95s, put: ``/blobs/0/373``
  `Upload blob`

Page detail stats
-----------------


PAGE 001: Upload blob
~~~~~~~~~~~~~~~~~~~~~

* Req: 001, put, url ``/blobs/0/373``

     .. image:: request_001.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                     25              0.501               POOR                374                374             0.00%              0.935              1.952              3.201              1.763              1.979              2.114              2.148
                     50              0.500               POOR                427                427             0.00%              1.099              3.341              6.568              2.466              3.170              4.518              5.033
                     75              0.412       UNACCEPTABLE                403                403             0.00%              1.678              5.191              7.910              3.947              5.124              6.590              7.132
                    100              0.095       UNACCEPTABLE                398                398             0.00%              1.845              6.735              9.799              3.889              7.001              8.405              9.339
                    125              0.087       UNACCEPTABLE                401                401             0.00%              2.149              8.146             11.382              4.326              8.810             10.115             11.130
                    150              0.091       UNACCEPTABLE                303                303             0.00%              2.189             11.679             18.975              4.069             14.256             16.196             17.071
                    175              0.076       UNACCEPTABLE                336                336             0.00%              2.263             12.015             18.187              4.768             14.784             16.208             16.823
                    200              0.065       UNACCEPTABLE                317                317             0.00%              2.541             13.732             24.099              5.263             15.311             19.942             20.955
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