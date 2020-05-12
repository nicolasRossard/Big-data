#! /usr/bin/python
with open("forum_node.tsv","r") as _in:
	with open("clean_forum.tsv", "w") as _out:
		for l in _in.readlines():
			print(l)
			if (len(l) <= 1):
				# Only a "\n"
				_out.write(l.strip())
			else:	
				#Check if at the end ot the line we have "\r\n"  
				if(l[-2]) == "\r" :
					# End of the line	
					_out.write(l.strip()+"\n")
				else:
					# Line not ended
					_out.write(l.strip())
