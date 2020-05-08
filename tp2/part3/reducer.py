#!/usr/bin/python

import sys
import csv


reader = csv.reader(sys.stdin, delimiter ="\t")

oldWord = None
occ = 1
idList = []

for line in reader:
	#Continue if there are no datas on the line
	if len(line)==0:
		continue
	thisWord = line[0]
	id_node = line[1]
	if oldWord and oldWord.lower() != thisWord.lower():
		# Print informations
		print("{0}\t{1}\t{2}".format(oldWord,occ,list(dict.fromkeys(idList))))
		# Initialize occ and the list of id_node
		occ = 0
		idList = []

	oldWord = thisWord.lower()
	# + 1 for number of occurences
	occ +=1
	if id_node not in idList:
		#Add node of ID
		idList.append(id_node)
# Last word
if oldWord != None:
	print("{0}\t{1}\t{2}".format(oldWord,occ,idList))

