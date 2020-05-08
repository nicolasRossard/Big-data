#!/usr/bin/python

import csv
import sys
import os

file1="clean_forum"
first_line_file1 = True

file2 = "forum_users"
first_line_file2 =True

#args = sys.argv[1:]
#print(args)
print("MAPPER")
for line in sys.stdin:
	print("DATA : " +line)
	file_name = os.getenv('map_input_file')
	if file1 in file_name: #line from forum_node
		print("**********************")
		print(file1)
		print(file_name)
		data = line.strip().split("\t")
		if first_line_file1 or len(data) <= 9:
			#print("****** kick out; file: "+file1+" datas:" + str(data))
			first_line_file1 = False
			continue
		fields = data[1:3]
		# fielfs.append(data[5:9])
		print("{0}\t{1}\t{2}".format(data[0], fields, file1)) # post id, fields, "forum_node"
		print("**********************")
	elif file2 in file_name:
		print("**********************")
		print(file2)
		print(file_name)
		data = line.strip().split("\t")
                if first_line_file2 or len(data) <= 4:
                        first_line_file2 = False
			#print("****** kick out; file: "+file1+" datas:" + str(data))
                        continue
		print("{0}\t{1}\t{2}".format(data[0],data[1:4], file2)) # post author_id, fields, "forum_users"
		print("**********************")


