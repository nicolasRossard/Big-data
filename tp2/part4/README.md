# PART IV

## Goal
Use combiner on hadoop

### Dataset
purchases.txt

### mapper.py and reducer.py
MapReduce which calculates the sum of sells for each day of the week

### Execute on hadoop
hsc.txt

$ hsc mapper.py reducer.py [path_hadoo]/purchases.txt [path_hadoop]/out/

### Observation
The result is the same (totalWith.txt, totalWithout.txt) but it is faster with the combiner

### Example with shell.sh
(431)	Execute the mapReduce in local

