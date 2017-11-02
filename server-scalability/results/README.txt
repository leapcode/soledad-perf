Tests Scenarios and Results
===========================

This folder contains some results for Blobs Server Scalability Tests.

Scenarios
---------

The test results that are currently in this folder were run in the following
scenario:

- client download bandwidth: 150 Mb/s
- client upload bandwidth:   150 Mb/s
- server:                    giraffe.cdev.bitmask.net

Three blob sizes were used (1KB, 10KB, 100KB) and the results for each size can
be found in each of the subdirectories of this folder.

The information above is related to the following folders:

.
├── 100k
│   ├── test_download-20171101T183840
│   └── test_upload-20171101T183258
├── 10k
│   ├── test_download-20171101T173739
│   └── test_upload-20171101T173213
└── 1k
    ├── test_download-20171101T171926
    └── test_upload-20171101T171410
