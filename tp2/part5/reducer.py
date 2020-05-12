#!/usr/bin/python

## Reducer can be executed in local or on hadoop with part5/mapper.py
# Input: 2 possibilities:
#	"AuthorID" \t fields' list \t "forum_users"
#	"postID" \t "fields' list" \t "clean_forum"
# Output: merge all fields:
# 	"postID" \t "fields of post" ... \t "fields of author" 
#
# To execute on Hadoop:
#  hadoop jar [your_path]/hadoop-streaming-2.6.0-mr1-cdh5.12.0.jar -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py -input [hadoop_path_datasets]/* -output [hadoop_path_folder_output]
##

import csv
import sys

# Display informations in stderr
display = False

# Files
file1 = "clean_forum"
file2 = "forum_users"

# Dict to save datas from both files
tab1 = {}
tab2 = {}

# Counting lines
count = 0

# Datas output
fields_names = ["postID", "title", "tagnames", "authorID", "node_type", "parent_id", "abs_parent_id", "addet_at", "score", "reputation", "gold", "silver", "bronze"]

sys.stderr.write("---------------------- START REDUCER -------------------------\n")
if display:
	sys.stderr.write("------------------------------------ STDIN -----------------------------------------\n")
for line in sys.stdin:
	count +=1
	# take back datas:  ID(author or post) ,datas , filename
	key, fields, filename = line.split("\t")

	# Get value of datas
	fields = eval(fields)
	key = eval(key)        
	if display:
		sys.stderr.write("\n---------- DATA IN " + line  +"\n")
	        sys.stderr.write("---------- LENGTH:  " + str(len(line))  +"\n")
		sys.stderr.write("---------- LINE:\t"+str(count)+"\n")
		sys.stderr.write(str(key) + "\t" + str(fields) + "\t" + filename+"\n")
		sys.stderr.write("---------- KEY:\t"+str(key)+"\n")
		sys.stderr.write("---------- DATAS:\t"+str(fields)+"\n")
		
	# clean_forum file 
	# ID post , [title, tagnames, author_ID,node_type, parent_id, abs_parent_id, added_at, score] , clean_forum
	if file1 in filename:
		tab1[key] = fields
	
	# forum_users file
	# ID_author , [reputation, gold, silver, bronze], forum_user
	else: 
		tab2[key] = fields
	if display:
		sys.stderr.write("-----------------------------------------------------------------------------\n")
if display:
	sys.stderr.write("---------------------------------- DICT ------------------------------------\n")
	sys.stderr.write("TAB1:\t"+str(tab1)+"\n\n")
	sys.stderr.write("TAB2:\n"+str(tab2)+"\n")
	sys.stderr.write("-----------------------------------------------------------------------------\n")
	sys.stderr.write("---------------------------------- MERGE ------------------------------------\n")

# First Line data  output: name of each field
sys.stdout.write('"'+fields_names[0]+'"')
if display:
	sys.stderr.write('"' + fields_names[0] + '"')
for name in fields_names[1:]:
	sys.stdout.write("\t" + '"' + name + '"')
	if display:
		sys.stderr.write("\t" + '"' + name +'"')

sys.stdout.write("\n")
if display:
	sys.stderr.write("\n")

for postID, postDatas in tab1.items():
	#Get Auhtor ID
	authorID = eval(postDatas[2])
	if display:
		sys.stderr.write("---------- POST ID: "+str(postID)+"\n")
		sys.stderr.write("---------- AUTHOR ID: " + str(authorID) +"\n")
		sys.stderr.write("---------- DATAS OUTPUT: \n")
	# 
	if authorID in tab2:
		#PostID	
		sys.stdout.write('"' + str(postID) + '"')
		if display:
			sys.stderr.write('"' + str(postID)+'"')

		#Display all datas from clean_forum
		for d in postDatas:
			sys.stdout.write("\t" + d)
			if display:
				sys.stderr.write("\t" + d)
		#Display all datas from users
		#authorDatas = tab2[authorID]

		for d in tab2[authorID]:
			sys.stdout.write("\t" + d)
			if display:
				sys.stderr.write("\t" + d)
		sys.stdout.write("\n")
		if display:
			sys.stderr.write("\n")
		if display:
			sys.stderr.write("-----------------------------------------------------------------------------\n")
	else:
		sys.stderr.write("---------- ERROR AUTHOR: "+str(authorID)+" not found\n")

sys.stderr.write("---------------------- END REDUCER -------------------------\n")

