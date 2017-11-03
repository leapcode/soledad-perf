======================
FunkLoad_ bench report
======================


:date: 2017-11-03 14:10:00
:abstract: Upload and download blobs
           Bench result of ``Blobs.test_upload``: 
           Upload blobs stress test

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents
.. |APDEXT| replace:: \ :sub:`1.5`

Bench configuration
-------------------

* Launched: 2017-11-03 14:10:00
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

* 2775 tests
* 2775 pages
* 2775 requests


Test stats
----------

The number of Successful **Tests** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ================== ================== ================== ================== ==================
                CUs               STPS              TOTAL            SUCCESS              ERROR
 ================== ================== ================== ================== ==================
                 25              9.433                283                283             0.00%
                 50             13.600                408                408             0.00%
                 75             12.767                383                383             0.00%
                100             12.467                374                374             0.00%
                125             11.567                347                347             0.00%
                150             11.867                356                356             0.00%
                175             10.667                320                320             0.00%
                200             10.133                304                304             0.00%
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
                 25              0.560               POOR              9.433             22.000                283                283             0.00%              0.066              1.866              3.165              1.436              1.890              2.366              2.518
                 50              0.500               POOR             13.600             50.000                408                408             0.00%              1.641              3.512              5.607              2.863              3.389              4.422              4.822
                 75              0.401       UNACCEPTABLE             12.767             61.000                383                383             0.00%              1.336              5.390              7.387              3.995              5.425              6.476              7.021
                100              0.096       UNACCEPTABLE             12.467             68.000                374                374             0.00%              1.450              7.092              9.662              4.257              7.619              8.473              9.153
                125              0.088       UNACCEPTABLE             11.567             78.000                347                347             0.00%              1.985              8.865             12.704              4.340              9.898             11.125             11.627
                150              0.076       UNACCEPTABLE             11.867             80.000                356                356             0.00%              2.143             10.332             16.448              4.655             11.889             12.945             13.623
                175              0.080       UNACCEPTABLE             10.667             80.000                320                320             0.00%              2.538             12.250             19.850              4.683             14.434             16.914             17.575
                200              0.069       UNACCEPTABLE             10.133             79.000                304                304             0.00%              2.581             13.955             23.533              4.999             15.096             20.614             21.232
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
                 25              0.560               POOR              9.433             22.000                283                283             0.00%              0.066              1.866              3.165              1.436              1.890              2.366              2.518
                 50              0.500               POOR             13.600             50.000                408                408             0.00%              1.641              3.512              5.607              2.863              3.389              4.422              4.822
                 75              0.401       UNACCEPTABLE             12.767             61.000                383                383             0.00%              1.336              5.390              7.387              3.995              5.425              6.476              7.021
                100              0.096       UNACCEPTABLE             12.467             68.000                374                374             0.00%              1.450              7.092              9.662              4.257              7.619              8.473              9.153
                125              0.088       UNACCEPTABLE             11.567             78.000                347                347             0.00%              1.985              8.865             12.704              4.340              9.898             11.125             11.627
                150              0.076       UNACCEPTABLE             11.867             80.000                356                356             0.00%              2.143             10.332             16.448              4.655             11.889             12.945             13.623
                175              0.080       UNACCEPTABLE             10.667             80.000                320                320             0.00%              2.538             12.250             19.850              4.683             14.434             16.914             17.575
                200              0.069       UNACCEPTABLE             10.133             79.000                304                304             0.00%              2.581             13.955             23.533              4.999             15.096             20.614             21.232
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Slowest requests
----------------

The 5 slowest average response time during the best cycle with **25** CUs:

* In page 001, Apdex rating: POOR, avg response time: 1.87s, put: ``/blobs/0/281``
  `Upload blob`

Page detail stats
-----------------


PAGE 001: Upload blob
~~~~~~~~~~~~~~~~~~~~~

* Req: 001, put, url ``/blobs/0/281``

     .. image:: request_001.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                     25              0.560               POOR                283                283             0.00%              0.066              1.866              3.165              1.436              1.890              2.366              2.518
                     50              0.500               POOR                408                408             0.00%              1.641              3.512              5.607              2.863              3.389              4.422              4.822
                     75              0.401       UNACCEPTABLE                383                383             0.00%              1.336              5.390              7.387              3.995              5.425              6.476              7.021
                    100              0.096       UNACCEPTABLE                374                374             0.00%              1.450              7.092              9.662              4.257              7.619              8.473              9.153
                    125              0.088       UNACCEPTABLE                347                347             0.00%              1.985              8.865             12.704              4.340              9.898             11.125             11.627
                    150              0.076       UNACCEPTABLE                356                356             0.00%              2.143             10.332             16.448              4.655             11.889             12.945             13.623
                    175              0.080       UNACCEPTABLE                320                320             0.00%              2.538             12.250             19.850              4.683             14.434             16.914             17.575
                    200              0.069       UNACCEPTABLE                304                304             0.00%              2.581             13.955             23.533              4.999             15.096             20.614             21.232
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