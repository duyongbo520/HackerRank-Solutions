#!/bin/python

import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    point_a = 0
    point_b = 0

    pa = (a0, a1, a2)
    pb = (b0, b1, b2)

    for i in range(3):
        if pa[i] > pb[i]:
            point_a += 1
        elif(pa[i] < pb[i]):
            point_b += 1
    return (point_a, point_b)

a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))
