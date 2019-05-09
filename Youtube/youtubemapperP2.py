#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip().split('\t')

    if len(line) > 5:
        print('%s\t%s' % (line[0], line[6]))