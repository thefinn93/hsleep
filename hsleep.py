#!/usr/bin/env python
import sys


def helptext(error=None):
    print("Usage: %s <time specification>" % sys.argv[0])
    print("")
    print("Counts down until the specified time. May be specified as a")
    print("relative time (for example, '5 minutes' or 'tomorrow') or an")
    print("actual time (for example, '8am').")
    if error is not None:
        print("\n\n")
        print (error)
    sys.exit(1)

if len(sys.argv) == 1:
    helptext()

from parsedatetime import Calendar
from time import mktime, sleep
from datetime import datetime, timedelta

p = Calendar()
specifiedtime = p.parse(" ".join(sys.argv[1:]))
timeleft = datetime.fromtimestamp(mktime(specifiedtime[0])) - datetime.now()

length = 0

while timeleft > timedelta(microseconds=-1):
    interval = 10
    if timeleft < timedelta(hours=1):
        interval = 1
    if timeleft < timedelta(minutes=10):
        interval = 0.1
    if timeleft < timedelta(minutes=1):
        interval = 0.001
    sys.stdout.write("\b" * length)
    outline = str(timeleft)
    length = len(outline)
    sys.stdout.write(outline)
    sys.stdout.flush()
    sleep(interval)
    timeleft = timeleft - timedelta(seconds=interval)
print("")
