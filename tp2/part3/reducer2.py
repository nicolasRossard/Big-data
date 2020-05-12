#!/usr/bin/python
import sys

total = 0
nb = 0
oldDay = None
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 2:
		day,cost = data
		if oldDay and oldDay != day:
			avg = total / nb
			print("{0}\t{1}".format(oldDay,avg))
			total = 0
			nb = 0
	nb += 1
	total += float(cost)
	oldDay = day

if oldDay != None:
	avg = total / nb
	print("{0}\t{1}".format(oldDay,avg))

