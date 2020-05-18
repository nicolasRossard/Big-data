#!/usr/bin/python

## RUN ON LINUX
# To run this main you have to configure hadoop streaming in bashrc:
# Check README before
# arguments :
#	 arg[0]: ./main 
# 	arg[1]: hadoop file input
# 	arg[2]: X
# 	arg[3]: hadoop output:	'1/' first MapReduce result 
#				'2/' second MapReduce result
##

import os
import sys
import time

#Hadoop_streaming_path
hadoop_str_path = '/usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.12.0.jar'

# Execute hadoop streaming
def hadoop_streaming(mapper,reducer,mapFile,redFile,inputFile,outputFile):
	os.system('hadoop jar ' + hadoop_str_path + ' -mapper ' + mapper + ' -reducer ' + reducer + ' -file ' + mapFile
		+ ' -file ' + redFile + ' -input ' + inputFile + ' -output ' + outputFile)
def main():
	args = sys.argv
	if len(args) != 4:
		sys.stderr.write("***** ERROR main.py : invalid arguments: "+str(args)+"\n")
		return
	try:
		x = int(args[2])
	except ValueError:
		sys.stderr.write("***** ERROR main.py : argument numero 2 is not an integer: "+args[2]+"\n")
	# Get informations:
	fileIn = args[1]
	fileOut = args[3]
	
	#Output 1st MapReduce
	fileOut1 = fileOut+'/1/'

	# Output 2nd MapReduce 	
	fileOut2 = fileOut+'/2/'
	
	# Test in local with linux
	#os.system('cat inputfile.txt | ./map.py | sort |./red.py | ./map2.py 3 | sort | ./red.py ')
	
	# Time execution
	start_time = time.time()
	
	# Run 1st mapReduce on hadoop
	hadoop_streaming('map.py','red.py','map.py','red.py',fileIn,fileOut1)
	
	st1 = time.time()

	# Run 2nd mapReduce on hadoop
	hadoop_streaming('\'map2.py '+ str(x) +'\'','red.py','map2.py','red.py',fileOut1,fileOut2)
	
	stop_time = time.time()

	print('---- %s seconds first MapReduce ----' % (st1 - start_time))
	print('---- %s seconds second MapReduce ----' % (stop_time - st1))
	print('---- %s seconds total ----' % (stop_time - start_time))


if __name__ =="__main__":
	main()
