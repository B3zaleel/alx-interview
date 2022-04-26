# Log Parsing

This project contains interview coding challenges.

## Tasks To Complete

+ [x] 0. **Log parsing**<br/>[0-stats.py](0-stats.py) contains a script that reads `stdin` line by line and computes metrics:
  + Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (if the format is not this one, the line must be skipped).
  + After every 10 lines and/or a keyboard interruption (`CTRL + C`), print these statistics from the beginning:
    + Total file size: `File size: <total size>`.
    + Where `<total size>` is the sum of all previous `<file size>` (see input format above)
    + Number of lines by status code:
      + Possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405` and `500`.
      + If a status code doesn’t appear or is not an integer, don’t print anything for this status code.
      + Format: `<status code>: <number>`.
      + Status codes should be printed in ascending order.
