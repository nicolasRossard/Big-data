#!/usr/bin/python

import sys
total = 0
lastWord = None
for line in sys.stdin:
	# Get word and count = 1
	word, count= line.strip().split(',')
	
	if lastWord and lastWord != word:
		sys.stdout.write(lastWord +","+str(total)+"\n")
		total = 0
	lastWord = word
	total += int(count)
if lastWord != None:
	sys.stdout.write(lastWord +","+str(total)+"\n")
	

