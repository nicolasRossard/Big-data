#!/usr/bin/python
import sys
import csv
import re

firstLine = 1

reader = csv.reader(sys.stdin, delimiter ="\t")

for line in reader:
	if firstLine == 1:
		firstLine = 0
		continue
	body = line[4]
	node = line[0]
	# Regexp \w = word and . , ! ? ;
	words = re.findall(r"[\w']+",body)
	for word in words:
		print("{0}\t{1}".format(word,node))
