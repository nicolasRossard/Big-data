#!/usr/bin/python
import sys
from datetime import datetime
weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data)==6:
		date, time, store, item, cost, payment = data
		weekday = datetime.strptime(date,"%Y-%m-%d").weekday()
		print("{0}\t{1}".format(weekDays[weekday],cost))
