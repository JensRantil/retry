Retry
=====
Retry is a small script that wraps retrying logic in any CLI command. It can be
very useful when doing healthchecks (wrapping `curl`), but can equally be used
when you have unstable commands.

Example
-------

    $ ./retry.py curl -s http://localhost:8080

Usage
-----
```
$ ./retry.py --help
usage: retry.py [-h] [--max-wait SECONDS] [--check-interval SECONDS] ...

Retry an executable with backoff until it passes or a timeout occurs.

positional arguments:
  CMD ARG1 ARG2 ... ARG3

optional arguments:
  -h, --help            show this help message and exit
  --max-wait SECONDS
  --check-interval SECONDS
```
