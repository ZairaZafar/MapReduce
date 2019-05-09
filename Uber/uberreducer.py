#!/usr/bin/env python

import sys
import re


sum = 0
driver = None
previousDay = None
arr = []
for line in sys.stdin:
    if re.match(r'^\s*$', line):
        continue
    
    key, trips = line.strip().split('\t')
    serial, day = key.split(' ')

    if driver == serial:
        if day == previousDay:
            sum += trips

        else:
            if driver:
                arr = sum
                sum = 0

            previousDay = day
            sum = trips
    else:
        if driver:
            print('%s %s %s' % (driver, day, max(arr)))
            arr = None
        driver = serial

print('%s %s %s' % (driver, day, max(arr)))
