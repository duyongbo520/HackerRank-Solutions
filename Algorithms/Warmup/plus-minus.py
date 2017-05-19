#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

positive_count = 0
negative_count = 0

for element in arr:
    if element > 0:
        positive_count += 1
    elif element < 0:
        negative_count += 1

print '%.6f' % (positive_count / float(n))
print '%.6f' % (negative_count / float(n))
print '%.6f' % ((n - positive_count - negative_count) / float(n))
