#!/bin/python

import sys


n = int(raw_input().strip())

for f in xrange(1, n+1):
    str = ''
    for i in xrange(1, n+1):
        if i <= (n-f):
            str += ' '
        else:
            str += '#'
    print str
