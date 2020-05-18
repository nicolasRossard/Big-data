# BIG Data
This repository presents some exercices using Mapper and Reducer. For each part, there is a report in French which explains my work and my remarks.

To use correctly mapper and reducer you can use shell.sh


## TP1
### Goals
Create Mapper, Reducer and put in Hadoop in JAVA and in Python

### Dataset (smalldata.txt):
[date] \t [time] \t [shop] \t [product] \t [cost] \t [payment]

The script shell.sh is configured for cloudera quickstartVM with  Hadoop 2.6.0-cdh5.12.0.
Don't forget to modify this script if you want to use it in your machine. To execute all commands you have also to create a file in data/ named purchases.txt (like smalldata.txt but much bigger).


## TP2
### Goals
Create Mapper, reducer and put in hadoop in Python (get a field from a dataset, merge datasets, use combiner in Hadoop)

### Datasets
#### clean_forum:
Contains all informations posts (example test.tsv):

[postID] \t [title] \t [tagnames] \t [authorID] \t [body] \t [node_type] \t  [parent_id] \t [abs_parent_ID] \t [addet_at] \t [score] ...

### forum_users:
Contains all informations of the author (used only part5):

[authorID] \t [reputation] [gold] \t  [silver] \t [bronze]


## TP3
### Goals
Use Spark and compare performance with Hadoop

### part3
Use Spark on a sample dataset

### part4
Compare Spark and Hadoop on a sample datset and a special dataset

INSA de Toulouse 
