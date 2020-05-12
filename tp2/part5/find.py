#!/usr/bin/python
##
# Looking an ID of an author or an ID of a post
# Give the reputation of the author if it's an ID of author
# Give the reputation of the author of the post if it's an ID of a Post


import sys

## MODIFY HERE ID LLOKING FOR
idLook = "100002517"

findAuthor = False
findPostID = False

print("ID LOOKING FOR:" + idLook)
for line in sys.stdin:
	datas = line.split("\t")
	
	# Stop the loop if postID and author was found
	if (findAuthor and findPostID):
		#print("AuthorID and postID was found")
		break
	authorID = eval(datas[3])
	postID = eval(datas[0])
	#print(postID + "\t" +authorID)
		
	if (postID == idLook and not(findPostID)):
		print("postID={0}\tAuthorID={1}\treputation={2}".format(postID,AuthorID,datas[9]))
		findPostID =True
        if (authorID == idLook and not(findAuthor)):
                print("postID={0}\tAuthorID={1}\treputation={2}".format(postID,authorID,datas[9]))
                findAuthor =True
if findAuthor:
	print("Author ID found")

if findPostID:
	print("Post ID found")
