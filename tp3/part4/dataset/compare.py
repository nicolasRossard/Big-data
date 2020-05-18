#!/usr/bin/python
## RUN ON LINUX
# To run this main you have to configure hadoop streaming in bashrc.
# Files used:
#	sparkApp.py
# 	mapClean.py
# 	map2Clean.py
# 	red.py
#
## Arguments :
#      	1: hadoop file input
#      	2: X
#      	3:  output Folder which it will have:
#		=> './1/' first MapReduce result (result of fileInput with map.py red.py) 
#             	=> './hadoop/' second MapReduce result => final result (result of mapReduce 1 with map2.py red.py)
#		=>  './spark/ final result with spark
# Return time for each process
####

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
        fileOut2 = fileOut+'/hadoop/'
	
	# ---------------- Hadoop ---------------
        # Time execution
        start_time = time.time()

        # Run 1st mapReduce on hadoop
        hadoop_streaming('./hadoop/mapClean.py','./hadoop/red.py','./hadoop/mapClean.py','./hadoop/red.py',fileIn,fileOut1)

        st1 = time.time()

        # Run 2nd mapReduce on hadoop
        hadoop_streaming('\'./hadoop/map2Clean.py '+ str(x) +'\'','./hadoop/red.py','./hadoop/map2Clean.py','./hadoop/red.py',fileOut1,fileOut2)

        stop_time = time.time()

       
	# Save times	
	time_mr1 = st1 - start_time
	time_mr2 = stop_time - st1
	time_hadoop = stop_time - start_time
	
	# ---------------- Spark -------------------
	# Output Spark
	start_time=time.time()
	os.system('./spark/sparkApp.py '+ fileIn + ' '+str(x) + ' '+ fileOut)
	time_spark = time.time() - start_time
	

	# Display performance
	print("--------------------- Hadoop performance ----------------------------")
	print('---- %.3f seconds first MapReduce' % time_mr1)
        print('---- %.3f seconds second MapReduce' % time_mr2)
        print('---- %.3f seconds total' % time_hadoop)
	print("--------------------- Spark performance ----------------------------")
        print('---- %.3f seconds total' % (time_spark))
	print(" -------------------- Performance ----------------------------------")	
	if time_spark < time_hadoop:
		print('Spark is  %.2f faster than hadoop. Execution time is  %.1f times faster' % ((time_hadoop - time_spark),(time_hadoop / float(time_spark))))
	else: 
		print('Hadoop is  %.2f faster than Spark. Execution time is  %.1f times faster' % ((time_spark - time_hadoop),(time_spark / float(time_hadoop))))
	

if __name__ == '__main__':
	main()
