#!/usr/bin/python
import sys
import csv
a = []
b = []
test = 0
reader = csv.reader(sys.stdin, delimiter="\t")
for line in reader:
	if len(line) == 0:
		continue
	else:
		a.append(line)
		test +=1
# Sort the list by the size of the body: element 4
a.sort(key=lambda a: len(a[:][4]), reverse =True)

# Take 10 longest body
for i in range(0,10):
	b.append(a[i])
b.sort(key=lambda b: len(b[4]))

print("Voila les 10 posts les plus longs !")

for bl in b:
	print(bl)
