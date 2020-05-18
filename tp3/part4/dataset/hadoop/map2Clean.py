#!/usr/bin/python
import sys

def mapper():
	args = sys.argv
	if len(args) != 2:
		sys.stderr.write("***** ERROR map2.py invalid arguments: " + str(args)+"\n")
		return	
	x = args[1]
	#Check if x is a digit:
	try:
		x=int(x)
	except ValueError:
                sys.stderr.write("***** ERROR map2.py invalid argument X " + str(x)+"\n")
		return
	for line in sys.stdin: 	
		word, count = line.strip().split(',')
		count = int(count)
		#Check if word appears >= x times:
		if count>=x:
			sys.stderr.write("(" + word + "," + str(count) + ")\n")
			# return its letters
			for letter in word:
				sys.stdout.write(letter + ',' +str(1)+"\n")

def main():
	mapper()

if __name__=="__main__":
	main()
