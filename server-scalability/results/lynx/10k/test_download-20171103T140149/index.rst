======================
FunkLoad_ bench report
======================


:date: 2017-11-03 14:01:49
:abstract: Upload and download blobs
           Bench result of ``Blobs.test_download``: 
           Download blobs stress test

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents
.. |APDEXT| replace:: \ :sub:`1.5`

Bench configuration
-------------------

* Launched: 2017-11-03 14:01:49
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

* 73806 tests
* 74024 pages
* 74024 requests


Test stats
----------

The number of Successful **Tests** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ================== ================== ================== ================== ==================
                CUs               STPS              TOTAL            SUCCESS              ERROR
 ================== ================== ================== ================== ==================
                 25            293.767               8813               8813             0.00%
                 50            289.200               8676               8676             0.00%
                 75            293.900               8817               8817             0.00%
                100            286.233               8587               8587             0.00%
                125            284.867               8546               8546             0.00%
                150            340.167              10205              10205             0.00%
                175            322.467               9674               9674             0.00%
                200            349.600              10488              10488             0.00%
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
                 25              1.000          Excellent            293.800            331.000               8814               8814             0.00%              0.008              0.068              0.229              0.051              0.068              0.086              0.092
                 50              1.000          Excellent            289.533            316.000               8686               8686             0.00%              0.006              0.132              0.361              0.087              0.131              0.178              0.203
                 75              1.000          Excellent            294.167            319.000               8825               8825             0.00%              0.005              0.179              0.520              0.105              0.182              0.243              0.262
                100              1.000          Excellent            286.967            318.000               8609               8609             0.00%              0.007              0.187              0.577              0.054              0.184              0.318              0.354
                125              1.000          Excellent            286.267            321.000               8588               8588             0.00%              0.007              0.164              0.664              0.042              0.131              0.334              0.388
                150              1.000          Excellent            343.367            388.000              10301              10301             0.00%              0.005              0.250              0.683              0.117              0.260              0.365              0.392
                175              0.996          Excellent            322.667            420.000               9680               9680             0.00%              0.007              0.337              3.486              0.093              0.316              0.554              0.720
                200              1.000          Excellent            350.700            396.000              10521              10521             0.00%              0.005              0.357              1.268              0.183              0.369              0.505              0.548
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
                 25              1.000          Excellent            293.800            331.000               8814               8814             0.00%              0.008              0.068              0.229              0.051              0.068              0.086              0.092
                 50              1.000          Excellent            289.533            316.000               8686               8686             0.00%              0.006              0.132              0.361              0.087              0.131              0.178              0.203
                 75              1.000          Excellent            294.167            319.000               8825               8825             0.00%              0.005              0.179              0.520              0.105              0.182              0.243              0.262
                100              1.000          Excellent            286.967            318.000               8609               8609             0.00%              0.007              0.187              0.577              0.054              0.184              0.318              0.354
                125              1.000          Excellent            286.267            321.000               8588               8588             0.00%              0.007              0.164              0.664              0.042              0.131              0.334              0.388
                150              1.000          Excellent            343.367            388.000              10301              10301             0.00%              0.005              0.250              0.683              0.117              0.260              0.365              0.392
                175              0.996          Excellent            322.667            420.000               9680               9680             0.00%              0.007              0.337              3.486              0.093              0.316              0.554              0.720
                200              1.000          Excellent            350.700            396.000              10521              10521             0.00%              0.005              0.357              1.268              0.183              0.369              0.505              0.548
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Slowest requests
----------------

The 5 slowest average response time during the best cycle with **200** CUs:

* In page 001, Apdex rating: Excellent, avg response time: 0.36s, get: ``/blobs/0/361``
  `Download blob`

Page detail stats
-----------------


PAGE 001: Download blob
~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url ``/blobs/0/3998``

     .. image:: request_001.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                     25              1.000          Excellent               8814               8814             0.00%              0.008              0.068              0.229              0.051              0.068              0.086              0.092
                     50              1.000          Excellent               8686               8686             0.00%              0.006              0.132              0.361              0.087              0.131              0.178              0.203
                     75              1.000          Excellent               8825               8825             0.00%              0.005              0.179              0.520              0.105              0.182              0.243              0.262
                    100              1.000          Excellent               8609               8609             0.00%              0.007              0.187              0.577              0.054              0.184              0.318              0.354
                    125              1.000          Excellent               8588               8588             0.00%              0.007              0.164              0.664              0.042              0.131              0.334              0.388
                    150              1.000          Excellent              10301              10301             0.00%              0.005              0.250              0.683              0.117              0.260              0.365              0.392
                    175              0.996          Excellent               9680               9680             0.00%              0.007              0.337              3.486              0.093              0.316              0.554              0.720
                    200              1.000          Excellent              10521              10521             0.00%              0.005              0.357              1.268              0.183              0.369              0.505              0.548
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