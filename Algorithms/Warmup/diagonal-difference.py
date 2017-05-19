#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

primary_diagonal = 0
secondary_diagonal = 0

k = 0
for j in xrange(n):
    primary_diagonal += a[j][k]
    secondary_diagonal += a[j][n-k-1]
    k += 1

print abs(primary_diagonal - secondary_diagonal)
