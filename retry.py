#!/usr/bin/env python

from __future__ import print_function
import sys
import os
import time
import subprocess
import argparse

def main():
    parser = argparse.ArgumentParser(description="Retry an executable with backoff until it passes or a timeout occurs.")
    parser.add_argument("--max-wait", type=int, default=300, metavar="SECONDS")
    parser.add_argument("--check-interval", type=int, default=10, metavar="SECONDS")
    parser.add_argument("args", nargs=argparse.REMAINDER, metavar="CMD ARG1 ARG2 ... ARG3")
    args = parser.parse_args()

    if not args.args:
        parser.error("Please specify an application to run.")

    endtime = time.time() + args.max_wait
    output = ""
    returncode = 0
    while time.time() < endtime:
        try:
            output = subprocess.check_output(args.args, stderr=subprocess.STDOUT).strip()
            returncode = 0
            break
        except subprocess.CalledProcessError as e:
            output = e.output.strip()
            returncode = e.returncode
            print("Sleeping for {0} seconds until next check...".format(
                args.check_interval))
            time.sleep(args.check_interval)

    if returncode != 0:
        print("Command failed for over {} seconds.".format(args.max_wait))
    print("Result from last retry:")
    print(output)

    return returncode

if __name__ == "__main__":
    sys.exit(main())
