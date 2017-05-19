#!/bin/python

import sys


n = int(raw_input().strip())
height = map(int,raw_input().strip().split(' '))

tallest = max(height)
num = 0

for h in height:
    if h >= tallest:
        num += 1

print num
