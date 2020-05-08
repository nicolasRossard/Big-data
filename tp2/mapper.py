#!/usr/bin/python

import csv
import sys
import os

file1="clean_forum"
first_line_file1 = True

file2 = "forum_users"
first_line_file2 =True

for line in sys.stdin:
	file_name = os.getenv('MAP_INPUT_FILE')
	if file1 in file_name: #line from forum_node
		#print(file_name)
		data = line.strip().split("\t")
		if first_line_file1 or len(data) <= 9:
			print("****** kick out; file: "+file1+" datas:" + str(data))
			first_line_file1 = False
			continue
		fields = data[1:3]
		# fielfs.append(data[5:9])
		print("{0}\t{1}\t{2}".format(data[0], fields, file1)) # post id, fields, "forum_node"
	elif file2 in file_name:
		data = line.strip().split("\t")
                if first_line_file2 or len(data) <= 4:
                        first_line_file2 = False
			print("****** kick out; file: "+file1+" datas:" + str(data))
                        continue
		print("{0}\t{1}\t{2}".format(data[0],data[1:4], file2)) # post author_id, fields, "forum_users"


