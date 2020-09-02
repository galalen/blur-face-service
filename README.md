# Blur-Face Service
#### ~~Be Anonymous~~
 Test FastAPI async/await with computation expensive operation (Detecting faces and blurring)
Tool used for the benchmarking: [Apache Benchmark](https://httpd.apache.org/docs/2.4/programs/ab.html)

#### Test the API with Sync:
```
Server Software:        uvicorn
Server Hostname:        localhost
Server Port:            8000

Document Path:          /api/blur/encoded/sync
Document Length:        332439 bytes

Concurrency Level:      100
Time taken for tests:   414.574 seconds
Complete requests:      1000
Failed requests:        24
   (Connect: 0, Receive: 0, Length: 24, Exceptions: 0)
Total transferred:      332557820 bytes
Total body sent:        213219000
HTML transferred:       332428820 bytes
Requests per second:    2.41 [#/sec] (mean)
Time per request:       41457.383 [ms] (mean)
Time per request:       414.574 [ms] (mean, across all concurrent requests)
Transfer rate:          783.37 [Kbytes/sec] received
                        502.25 kb/s sent
                        1285.62 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   1.0      0       4
Processing:   448 39727 9393.9  42729   49812
Waiting:      441 39723 9394.0  42729   49812
Total:        449 39728 9393.2  42730   49812

Percentage of the requests served within a certain time (ms)
  50%  42730
  66%  45175
  75%  46096
  80%  46714
  90%  47866
  95%  48535
  98%  49047
  99%  49308
 100%  49812 (longest request)
 ```
---
#### Test the API with Async:
```
Server Software:        uvicorn
Server Hostname:        localhost
Server Port:            8000

Document Path:          /api/blur/encoded
Document Length:        332439 bytes

Concurrency Level:      100
Time taken for tests:   565.946 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      332568000 bytes
Total body sent:        213214000
HTML transferred:       332439000 bytes
Requests per second:    1.77 [#/sec] (mean)
Time per request:       56594.562 [ms] (mean)
Time per request:       565.946 [ms] (mean, across all concurrent requests)
Transfer rate:          573.86 [Kbytes/sec] received
                        367.91 kb/s sent
                        941.77 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    4   3.2      4      15
Processing:  2396 55249 8477.1  57094   64087
Waiting:      365 35735 15569.3  36947   64058
Total:       2396 55254 8477.4  57099   64088

Percentage of the requests served within a certain time (ms)
  50%  57099
  66%  57488
  75%  58535
  80%  58666
  90%  61440
  95%  63933
  98%  63934
  99%  64088
 100%  64088 (longest request)
```

---
#### Example:
`curl -F "image=@path/to/image.png" https://blur-face.herokuapp.com/api/blur`

#### Check the docs: [API DOCS](https://blur-face.herokuapp.com/docs)