#!/usr/bin/env python

import sys

vidId = None
vidUploaded = 0
sum = 0
vidList = []
for line in sys.stdin:
    key, value = line.strip().split('\t')

    if vidId == key:
        sum += value
        vidUploaded += 1

    else:
        if vidId:
            vidList.append((vidId, value))

        vidId = key
        sum = 0

sortedMax = sorted(vidList, key=lambda t: t[1], reverse=True)[:5]
for vidId, value in sortedMax:
    print('%s %s' % (vidId, value))
