#!/usr/bin/python
import sys

total = 0
oldDay = None
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 2:
		day,cost = data
		if oldDay and oldDay != day:
			print("{0}\t{1}".format(oldDay,total))
			total = 0
	total += float(cost)
	oldDay = day

if oldDay != None:
	print("{0}\t{1}".format(oldDay,total))

