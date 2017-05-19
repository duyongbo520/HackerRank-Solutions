#!/bin/python

import sys
import copy

arr = map(int, raw_input().strip().split(' '))

minimum = []
maximum = []

arr1 = copy.copy(arr)
arr2 = copy.copy(arr)


for i in xrange(4):
    mi = min(arr1)
    minimum.append(mi)
    if len(arr1):
        arr1.remove(mi)

for i in xrange(4):
    mx = max(arr2)
    maximum.append(mx)

    if len(arr2):
        arr2.remove(mx)

print '%s %s' % (sum(minimum), sum(maximum))
