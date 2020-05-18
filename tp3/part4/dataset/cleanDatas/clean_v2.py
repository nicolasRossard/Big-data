#! /usr/bin/python
first_line = True
with open("clean_forum.tsv","r") as _in:
        with open("clean_forum_v2.tsv", "w") as _out:
                for l in _in.readlines():
			# Write first line
			if first_line:
				first_line = False
				_out.write(l)
				continue

			# Get datas
			data = l.split("\t")

			# Get postID
                	postID = data[0]
	                
			# Check if postID is correct (it should be a digit) : '"128831"'
			# Delete double quote
        	        try:
                	        postID =eval(postID)
                	except SyntaxError:
				print("---- SYNTAX ERROR: "+ postID)
                        	continue

			# Should be only a string
			if type(postID) != str:
				print("---- STRING ERROR: "+ str(postID))
				continue
			# Check if the string is a digit
			try:
                		if not(postID.isdigit()):
					print("---- NOT A DIGIT ERROR: "+ postID)
                        		continue
			except AttributeError:
				print("---- ATTRIBUTE DIGIT ERROR: "+ postID)
				print(postID)
			_out.write(l)


