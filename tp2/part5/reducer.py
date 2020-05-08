#!/usr/bin/python
import csv
import sys

file1 = "clean_forum"
file2 = "forum_users"
tab1 = {}
tab2 = {}
for line in sys.stdin:
	key, fields, filename = line.split("\t")
	if file1 in filename:
		tab1[key] = fields
		print(fields)
		print(type(fields))
	else: tab2[key] = fields.split(',')

print("-------------------------")

for key1, value1 in tab1.item():
	if value[2] in tab2:
		print("{0}\t{1}\t{2}".format(key1, value1, tab2[key1]))
