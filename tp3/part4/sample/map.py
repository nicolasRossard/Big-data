#!/usr/bin/python

import sys

for line in sys.stdin:
	words = line.strip().split(' ')
	for word in words:
		sys.stdout.write(word.lower() + "," +str(1)+"\n")
