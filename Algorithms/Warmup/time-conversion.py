#!/bin/python

import sys
import datetime
import time


t = raw_input().strip()

t = datetime.datetime.strptime(t, "%I:%M:%S%p").strftime("%H:%M:%S")

print t
