#!/usr/bin/python
import re
import sys

def mapper():
	indexForum = 0
	first_line = True

	for line in sys.stdin:
		data = line.split("\t")
		indexForum += 1
       		if first_line or len(data) <= 9:
			#Delete line uncomplete
			first_line = False
                	continue
		
		# Get postID
		#postID = data[0]
        	
		# Check if postID is correct (it should be a digit)
		#print(postID)	
		
		# get Body
        	body = data[4]
		
		# Get all words 
		words = re.findall(r"[A-Za-z]+",body)
		
		# write all words
		for word in words:
			sys.stdout.write(word.lower() + "," +str(1)+"\n")

def main():
        mapper()

if __name__=="__main__":
        main()

