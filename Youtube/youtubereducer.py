#!/usr/bin/env python

import sys

category = None
sum = 0
categoryList = []
for line in sys.stdin:
    key, value = line.strip().split('\t')
    
    if key == category:
        sum += 1
    
    else:
        if category:
            categoryList.append((category, sum))

        category = key
        sum = 0

sortedMax = sorted(categoryList, key=lambda t: t[1], reverse=True)[:5]
for category, sum in sortedMax:
    print('%s %s' % (category, sum))
