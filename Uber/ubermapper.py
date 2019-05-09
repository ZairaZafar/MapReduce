#!/usr/bin/env python

import sys
import datetime

for line in sys.stdin:
    line = line.split(",")
    date = datetime.datetime.strptime(line[1], '%m/%d/%Y')
    arr = line[0] + " " + str(date.weekday())
    print('%s\t%s' % (arr, line[-1]))

