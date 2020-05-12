#!/usr/bin/python

## Mapper running only on hadoop with part5/reducer.py
# Input: two filesnamed: clean_forum.* and forum_users.*
# Output: 
# 	clean_forum line: "postID" \t fields' list except "body" \t "clean_forum"
#	forum_users line: "authorID" \t fields' list \t "forum_users" 
# 
# CLEAN_FORUM dataset (split by a tab "\t"):
# "postID", "title", "tagnames", "authorID", "body", "node_type", "parentID" "abs_parent_ID", "added_at", "score"
#
# FORUM_USERS dataset (split by a tab "\t"):
# "authorID, "reputation", "gold", "silver", "bronze"
#
# To run it:
#  hadoop jar [your_path]/hadoop-streaming-2.6.0-mr1-cdh5.12.0.jar -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py -input [hadoop_path_datasets]/* -output [hadoop_path_folder_output]
##


import csv
import sys
import os






#Display in stderr: False displays only line which are not saved
display = False

# Clean_forum file
file1="clean_forum"
first_line_file1 = True

#Forum_users file
file2 = "forum_users"
first_line_file2 =True

#Counting lines
indexForum = 0
indexUsers = 0
sys.stderr.write("----------------------------------  MAPPER de NICO----------------------------------\n")
if display:
	sys.stderr.write("--------------------------------------------------------------------\n")

for line in sys.stdin:
	file_name = os.getenv('map_input_file')
	if display:
		sys.stderr.write("\n---------- DATA IN " + line  +"\n")
		#sys.stderr.write("---------- LENGTH:  " + str(len(line))  +"\n")

	# CLEAN_FORUM
	if file1 in file_name:
		indexForum +=1 
		data = line.split("\t")
		if first_line_file1 or len(data) <= 9:
			#Delete line uncompplete
			first_line_file1 = False
			continue
		# Get postID
		postID = data[0]
		# Get datas [title, tagnames, authorID, node_type, parentID, abs_parent_ID, addet_at, score]
		fields = data[1:4] + data[5:10] # Data[4] body
		
		# Check if postID is correct (it should be a digit)
		try:
			postID =eval(postID)
		except SyntaxError:
			sys.stderr.write("ERROR EVAL\n---------- POSTID: \n"+ str(postID) +"\tLine: "+ str(indexForum) +"\n")
			continue
		if not(postID.isdigit()):
			sys.stderr.write("ERROR DIGIT\n---------- POSTID: \n"+ str(postID) +"\tLine: "+ str(indexForum) +"\n")
			continue
		# Print into stderr for informations
		if display:
			sys.stderr.write("---------- CLEAN_FORUM  LINE  " + str(indexForum) +"\n")
			#sys.stderr.write("Length: " + str(len(fields)) + "\tType data :"+str(type(fields)) +"\n")
			#sys.stderr.write("---------- TYPE POSTID: \n"+ str(type(postID)) +"\t"+str(len(postID))+"\n")
			sys.stderr.write("---------- DATA OUT: \n"+ str(postID) +"\t"+str(fields)+"\t" +str(file1)+"\n")
			sys.stderr.write("--------------------------------------------------------------------\n")
		# Save datas
		sys.stdout.write(str(postID) +"\t" + str(fields) + "\t" + file1 +"\n")
		#print("{0}\t{1}\t{2}".format(postID, fields, file1)) # post id, fields, "forum_node"
	
	# FORUM_USERS
	elif file2 in file_name:
		data = line.strip().split("\t")
                indexUsers +=1
		if first_line_file2 or len(data) <= 4:
                        first_line_file2 = False
                        continue
		# Get Author ID
		authorID = data[0]
		# Get datas : [reputation , gold, silver, bronze]
		fields = data[1:]
		if display:
			sys.stderr.write("---------- FORUM_USERS LINE: " + str(indexUsers) +"\n")
			#sys.stderr.write("Datas: " + str(data[1])+"\t" +str(data[2]) + "\t" + str(data[3]) +"\n")
			#sys.stderr.write("Length: " + str(len(data)) +"\n")
			sys.stderr.write("---------- DATA OUT: \n"+ str(authorID) +"\t"+str(fields)+"\t" +str(file2)+"\n")
			sys.stderr.write("--------------------------------------------------------------------\n")
		# Save datas		
		sys.stdout.write(str(authorID) +"\t" + str(fields) + "\t" + file2 +"\n")
		#print("{0}\t{1}\t{2}".format(authorID,fields, file2)) # post author_id, fields, "forum_users"
	
sys.stderr.write("----------------------------------  MAPPER de Nico FIN----------------------------------\n")
