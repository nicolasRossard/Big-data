#!/usr/bin/pyspark
##
# MapReduce counts how many time appears each word  and then display letters of each word which have their number of occurences >= X
# arguments :
#	pathHDFS of fileIn
#	pathHDFS of fileOut
#	int X number of occurences a word should have minimum to be saved
##

from pyspark import SparkContext
import sys
import re
def mapReduce(fileIn,x,fileOut):
	sc = SparkContext()
	
	# Get file
	lines = sc.textFile(fileIn)
	
	# save header
	header = lines.first()
	
	# Function taking the value minumn of occurences for a word to be saved
	# word : tuple(word, nb of occurences)
	# x: int
	# return : (word,nb of occurences) if nb of occurences >=x
	def chooseWord(word,x = x):
		#print("choose word "+str(word) + "\t" + str(x))
		if word[1] >= x:
			return word
		
	## Get column of body:
	# - filter: Delete header
	# - map: Separe columns
	# - filter: delete line where column 4 is empty
	# - map: get only the column 4 ==> body
	body = lines.filter(lambda line: line != header)\
			.map(lambda line: line.split("\t"))\
			.filter(lambda line: line[4] !="\"\"")\
			.map(lambda body: body[4])

	## Wordcount:
	# - flatMap: get all words
	# - map: get a tuple(word,1) where word is converted to a String without uppercase
	# - reduceByKey: count nb of occurences for each word
	word_counts = body.flatMap(lambda words: re.findall(r"[A-Za-z]+",words))\
			.map(lambda word: (str(word).lower(),1))\
			.reduceByKey(lambda count1, count2: count1 + count2)

	# Get letters:
	# - map : Get all words where their nb of occurences >= x with chooseword function
	# - flatmap: convert the string into a list of tuples(letter,1)
	# - reduceByKey: Count nb of occurences for each lettet
	# - sort: sort result 
	#letter_counts = word_counts.filter(lambda (word,x=x): word if word[1] >=x else None)\
	letter_counts = word_counts.filter(lambda word: chooseWord(word))\
				.map(lambda word: word[0])\
				.flatMap(lambda word: [(letter,1) for letter in word])\
				.reduceByKey(lambda _,_2: _ + _2)\
				.sortByKey()

	# To print in local
	#			.collect()
	#for (letter,count) in letter_counts:
	#	print(letter,count)
				
	letter_counts.saveAsTextFile(fileOut)	
def main():
	args = sys.argv
        if len(args) != 4:
                sys.stderr.write("***** ERROR sparkMapReduce.py : invalid arguments: "+str(args)+"\n")
                return
        try:
                x = int(args[2])
        except ValueError:
                sys.stderr.write("***** ERROR sparkMapReduce.py : argument numero 2 is not an integer: "+args[2]+"\n")
	
	# Save args	
	fileIn = args[1]

	# Output in hadoop filOut in arg + /sparRes
	fileOutSpark = args[3] + "/sparkRes"
	
	print("-----args {0}\t{1}\t{2}".format(fileIn,x,fileOutSpark))
	
	# Run mapReduce	
	mapReduce(fileIn,x,fileOutSpark)
	
	# To block the job and take a look at localhost:4040
	# input("press ctrl + c to exit")
if __name__ == '__main__':
	main() 

